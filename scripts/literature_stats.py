#!/usr/bin/env python3
"""检索并统计三个主题的年度论文数量。

数据源：Semantic Scholar Graph API 的 paper/search/bulk 接口（开放访问、无需密钥）。
检索式、字段、年份范围、来源范围、纳入与排除规则见同目录 queries.json 与 README.md。

用法：
    python3 scripts/literature_stats.py fetch     # 抓取并缓存原始响应
    python3 scripts/literature_stats.py analyze   # 生成清单与年度统计
    python3 scripts/literature_stats.py all

原始响应保存在 docs/literature_stats/raw/；清洗后的论文清单、排除清单、年度统计表、
相关性抽样表及绘图用数据写入 docs/literature_stats/。脚本只使用 Python 标准库。
"""

from __future__ import annotations

import csv
import json
import random
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "title,year,venue,publicationVenue,externalIds,publicationTypes,fieldsOfStudy"
ROOT = Path(__file__).resolve().parent.parent
STATS = ROOT / "docs" / "literature_stats"
RAW = STATS / "raw"
CONFIG = STATS / "queries.json"


def load_config() -> dict:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if "retrieval_year_range" in cfg:
        raise RuntimeError("当前数据已升级，请使用 scripts/literature_stats_v2.py；本文件仅保留旧版处理逻辑。")
    return cfg


def get(url: str, retries: int = 10) -> dict:
    delay = 6
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=180) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504):
                print(f"    HTTP {exc.code}，等待 {delay}s 后重试（{attempt + 1}/{retries}）")
                time.sleep(delay)
                delay = min(delay * 2, 90)
                continue
            raise
        except Exception as exc:
            print(f"    请求异常 {exc}，等待 {delay}s 后重试")
            time.sleep(delay)
            delay = min(delay * 2, 90)
    raise RuntimeError(f"检索失败：{url}")


def fetch() -> None:
    cfg = load_config()
    RAW.mkdir(parents=True, exist_ok=True)
    for topic in cfg["topics"]:
        tid = topic["id"]
        token, page, total = None, 0, None
        while True:
            page += 1
            params = {
                "query": topic["query"],
                "fields": FIELDS,
                "year": f"{cfg['year_range'][0]}-{cfg['year_range'][1]}",
                "fieldsOfStudy": cfg["field_of_study"],
                "publicationTypes": ",".join(cfg["publication_types"]),
            }
            if token:
                params["token"] = token
            url = API + "?" + urllib.parse.urlencode(params)
            print(f"[{tid}] 抓取第 {page} 页 …")
            data = get(url)
            total = data.get("total", total)
            (RAW / f"{tid}-p{page}.json").write_text(
                json.dumps(data, ensure_ascii=False), encoding="utf-8"
            )
            token = data.get("token")
            if not token:
                break
            time.sleep(4)
        (RAW / f"{tid}-meta.json").write_text(
            json.dumps(
                {
                    "topic": tid,
                    "name": topic["name"],
                    "query": topic["query"],
                    "fields": FIELDS,
                    "year": f"{cfg['year_range'][0]}-{cfg['year_range'][1]}",
                    "fieldsOfStudy": cfg["field_of_study"],
                    "publicationTypes": cfg["publication_types"],
                    "reported_total": total,
                    "pages": page,
                    "retrieved": cfg["retrieval_date"],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"[{tid}] 完成，接口报告命中 {total} 条，共 {page} 页")


def norm_title(title: str) -> str:
    t = unicodedata.normalize("NFKC", title or "").lower()
    t = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def clean_title(title: str) -> str:
    return re.sub(r"\s+", " ", (title or "")).strip()


def venue_text(rec: dict) -> str:
    pv = rec.get("publicationVenue") or {}
    parts = [pv.get("name") or "", rec.get("venue") or ""]
    parts += list(pv.get("alternate_names") or [])
    return " ; ".join(p for p in parts if p).lower()


def classify(text: str, cfg: dict):
    for pat in cfg["excluded_venue_patterns"]:
        if pat in text:
            return "excluded", pat
    for entry in cfg["venues"]:
        for pat in entry["patterns"]:
            if pat in text:
                return "included", entry["name"]
    return "unlisted", ""


def analyze() -> None:
    cfg = load_config()
    years = list(range(cfg["year_range"][0], cfg["year_range"][1] + 1))
    yearly = defaultdict(Counter)
    included, dropped = [], []
    seen_global = defaultdict(dict)
    unlisted_counter = Counter()

    for topic in cfg["topics"]:
        tid = topic["id"]
        records, ids = [], set()
        for path in sorted(RAW.glob(f"{tid}-p*.json")):
            for rec in json.loads(path.read_text(encoding="utf-8")).get("data", []):
                pid = rec.get("paperId")
                if pid in ids:
                    continue
                ids.add(pid)
                records.append(rec)

        for rec in records:
            text = venue_text(rec)
            verdict, label = classify(text, cfg)
            ext = rec.get("externalIds") or {}
            doi = (ext.get("DOI") or "").lower()
            arxiv = ext.get("ArXiv") or ""
            row = {
                "topic": tid,
                "year": rec.get("year"),
                "title": clean_title(rec.get("title")),
                "venue": label or (rec.get("publicationVenue") or {}).get("name")
                or rec.get("venue") or "",
                "venue_raw": (rec.get("venue") or "").replace("\n", " "),
                "doi": doi,
                "arxiv": arxiv,
                "paper_id": rec.get("paperId") or "",
                "s2_url": f"https://www.semanticscholar.org/paper/{rec.get('paperId')}",
            }
            if verdict != "included":
                row["reason"] = f"venue_{verdict}"
                if verdict == "unlisted":
                    unlisted_counter[row["venue_raw"][:45]] += 1
                dropped.append(row)
                continue
            key = norm_title(row["title"])
            if not key:
                row["reason"] = "empty_title"
                dropped.append(row)
                continue
            seen = seen_global[tid]
            if key in seen:
                prev = seen[key]
                # 同一工作保留正式版本中最早的一条；同时保留 DOI 记录
                if (bool(row["doi"]), -int(row["year"] or 0)) > (
                    bool(prev["doi"]), -int(prev["year"] or 0)
                ):
                    prev["reason"] = "duplicate_title"
                    dropped.append(prev)
                    included[included.index(prev)] = row
                    yearly[tid][prev["year"]] -= 1
                else:
                    row["reason"] = "duplicate_title"
                    dropped.append(row)
                    continue
            seen[key] = row
            if key not in [norm_title(r["title"]) for r in included if r["topic"] == tid and r is not row]:
                included.append(row)
                if row["year"]:
                    yearly[tid][int(row["year"])] += 1

    cols = ["topic", "year", "title", "venue", "doi", "arxiv", "paper_id", "s2_url"]
    with (STATS / "papers.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for row in sorted(included, key=lambda r: (r["topic"], r["year"] or 0, r["title"])):
            w.writerow(row)
    with (STATS / "excluded.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols + ["venue_raw", "reason"], extrasaction="ignore")
        w.writeheader()
        for row in sorted(dropped, key=lambda r: (r["topic"], r["year"] or 0, r["title"])):
            w.writerow(row)

    with (STATS / "yearly.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["year"] + [t["id"] for t in cfg["topics"]])
        for y in years:
            w.writerow([y] + [yearly[t["id"]][y] for t in cfg["topics"]])

    payload = {
        "source": cfg["source"],
        "source_url": cfg["source_url"],
        "retrieval_date": cfg["retrieval_date"],
        "year_range": cfg["year_range"],
        "field_of_study": cfg["field_of_study"],
        "publication_types": cfg["publication_types"],
        "topics": [
            {
                "id": t["id"],
                "name": t["name"],
                "query": t["query"],
                "counts": {str(y): yearly[t["id"]][y] for y in years},
                "total": sum(yearly[t["id"]][y] for y in years),
            }
            for t in cfg["topics"]
        ],
    }
    (STATS / "yearly.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    rng = random.Random(20261029)
    with (STATS / "relevance_sample.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["topic", "year", "title", "venue", "doi", "judgement"])
        for topic in cfg["topics"]:
            rows = [r for r in included if r["topic"] == topic["id"]]
            for row in rng.sample(rows, min(30, len(rows))):
                w.writerow([row["topic"], row["year"], row["title"], row["venue"],
                            row["doi"], ""])

    print("年度统计（纳入文献数）：")
    print("年份  " + "  ".join(f"{t['id']:>4}" for t in cfg["topics"]))
    for y in years:
        print(f"{y}  " + "  ".join(f"{yearly[t['id']][y]:4d}" for t in cfg["topics"]))
    print("合计  " + "  ".join(
        f"{sum(yearly[t['id']][y] for y in years):4d}" for t in cfg["topics"]))
    print(f"纳入 {len(included)} 条，排除 {len(dropped)} 条")
    print("未列入来源范围的会议／期刊（前 15）：")
    for name, n in unlisted_counter.most_common(15):
        print(f"  {n:5d}  {name}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("fetch", "all"):
        fetch()
    if cmd in ("analyze", "all"):
        analyze()
