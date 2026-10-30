#!/usr/bin/env python3
"""Resolve merged scholarly-index records against official proceedings/DOI data.

Cached source manifests preserve the selected volumes and their publication
(year, not event) dates. Usage: literature_catalogs.py fetch|analyze|all.
No fuzzy title matching or inferred acceptance is used.
"""
import concurrent.futures,hashlib,html,importlib.util,json,re,sys,time
import urllib.parse,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
STATS=ROOT/'docs/literature_stats'
RAW=STATS/'raw/proceedings'
def clean(s):return html.unescape(re.sub(r'<[^>]+>','',s)).strip()
def norm(s):
    import unicodedata
    return re.sub(r'[^\w]+',' ',unicodedata.normalize('NFKC',clean(s)).casefold()).strip()
def sources():
    return json.loads((STATS/'proceedings_sources.json').read_text())
def fetch():
    RAW.mkdir(parents=True,exist_ok=True)
    for source in sources():
        url=source['url'];key=hashlib.sha256(url.encode()).hexdigest();path=RAW/(key+'.html')
        if not path.exists():
            with urllib.request.urlopen(url,timeout=40) as r:raw=r.read().decode('utf-8')
            path.write_text(raw);path.with_suffix('.json').write_text(json.dumps(source))
            time.sleep(.5)
        print(source['venue'],source['year'],url,flush=True)
def analyze():
    titles={};counts={}
    def add(title,venue,year,url,catalog,source):
        if not title or not year:return
        row=dict(title=clean(title),venue=venue,year=int(year),url=url,catalog_url=catalog)
        if source.get('cutoff_observed_on'):
            row['cutoff_observed_on']=source['cutoff_observed_on']
            row['availability_evidence']=source.get('availability_evidence','official_proceedings_publicly_accessible_on_cutoff')
        key=norm(title)
        if key not in titles or titles[key]['year']>row['year']:titles[key]=row
    for source in sources():
        url=source['url'];key=hashlib.sha256(url.encode()).hexdigest();h=(RAW/(key+'.html')).read_text();n=len(titles)
        venue,year=source['venue'],source['year']
        if venue in ('NeurIPS','ICLR','ECCV'):
            for match in re.finditer(r'<a\b[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>',h,re.S|re.I):
                href,title=match.groups()
                if venue=='ECCV':
                    m=re.search(r'eccv_(20\d{2}).*/html/',href,re.I)
                    if not m:continue
                    y=int(m[1])
                else:
                    if not re.search(r'-Abstract(?:-Conference)?\.html$',href):continue
                    y=year
                add(title,venue,y,urllib.parse.urljoin(url,href),url,source)
        elif venue=='CVPR':
            for href,title in re.findall(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',h,re.S|re.I):
                if re.search(r'/CVPR20\d{2}/html/.+_paper\.html$',href):
                    add(title,venue,year,urllib.parse.urljoin(url,href),url,source)
        else:
            for block in re.findall(r'<div class="paper">(.*?)</div>',h,re.S):
                title=re.search(r'<p class="title">(.*?)</p>',block,re.S)
                link=re.search(r'href="([^\"]+\.html)"[^>]*>abs</a>',block)
                if title and link:add(title[1],venue,year,urllib.parse.urljoin(url,link[1]),url,source)
        counts[url]=len(titles)-n
    (STATS/'official_titles.json').write_text(json.dumps(titles,ensure_ascii=False,indent=2))
    (STATS/'official_catalog_audit.json').write_text(json.dumps(dict(unique_titles=len(titles),catalog_new_titles=counts),indent=2))
    print('Official title/year records',len(titles),flush=True)
if __name__=='__main__':
    command=sys.argv[1] if len(sys.argv)>1 else 'all'
    if command in ('fetch','all'):fetch()
    if command in ('analyze','all'):analyze()
