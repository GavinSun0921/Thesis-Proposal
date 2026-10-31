# 1.2 主题论文统计与核查记录

本目录保存三个专题的年度数量统计与时间轴节点数据。统计量为**指定主要会议与期刊中的主题相关正式论文检索数量**，不是该领域全部产出，也不由报告参考文献表或时间轴中的代表工作计数替代。

## 当前口径

- 检索截止：2026-10-29；年度统计覆盖2015—2026年。2026年为不完整年度，只计入截至检索日已正式发表的记录，不能与完整年度直接比较。检索年份向前后各扩一年，用于纠正预印本与正式版本的归年差异。
- 发现来源：[Semantic Scholar bulk search](https://api.semanticscholar.org/api-docs/graph)，题名及摘要。检索式、来源清单及本地筛选约定见[queries.json](queries.json)；每页实际请求地址、响应与抓取时间由脚本写入本地 `raw/v2/` 缓存，不纳入仓库。不先按学科标签和publicationTypes筛选，以免丢失标签缺失或被合并的正式版本。
- 正式来源：主要视觉、图形学、机器学习及机器人会议与期刊，按27组来源维护（SIGGRAPH与ACM TOG合组），并非所有出版来源。Crossref容器采用完整规范名称匹配，ICCVDM、ICMLCA、ICMLC、ICRAS等相似名称不属于所列主会；CVPRF Findings不并入CVPR主会。ECCV采用正式DBLP标识或ECVA论文集识别，不因Springer分卷名称而遗漏。
- 主题筛选：在题名摘要命中后，要求与该专题有明确关系；动态重建包含动态几何、非刚性恢复、动态神经渲染及相关表征扩展；交互世界模型包含环境演化学习、生成、控制使用及相关评价；动作学习包含机器人操作、抓取、灵巧操作和相关学习表征。详细可执行规则为脚本中的`topic_match`。
- 排除边界：静态任务中附带提及动态、仅相机定位、移除动态对象后的静态建图、医学断层重建、small-world网络、纯神经群体动力学、纯导航、纯硬件及仅在展望中提及学习等；可识别的工作坊、海报、演示、课程及扩展摘要不计。纯文本四维生成与视觉观测重建作区分。
- 正式年份优先顺序：官方论文集的精确题名匹配；明确会议DOI中的会议年份；正式DBLP记录键（来自索引元数据）；Crossref正式出版元数据。期刊优先出版卷期的日期，不以通用IEEE DOI中的数字直接替代卷期年。仅arXiv DOI、未经核定正式来源或正式年份的记录不计。正式归年与截至日是否已公开分别保留证据，不能把预印本首发年作为正式出版年。
- 专题内按正式DOI及规范化题名去重，保留最早正式版本；同一主题检索主式与补充式按paperID合并。三个专题允许交叉，不加总为一个领域总量。

## 发表信息交叉核对

[proceedings_sources.json](proceedings_sources.json)列出正式论文集目录及其出版年份。精确题名、正式年份和论文链接的汇总（当前快照含 60100 条唯一题名）以及论文集目录、Crossref 的原始缓存均由抓取脚本在本地生成，不纳入仓库，用于核对索引中仍带有预印本年份的合并记录。PMLR按论文集出版年处理，例如CoRL 2024的PMLR 270按2025年计；这与本报告书目口径一致。NeurIPS 2025使用主会议目录，不把裸地址默认显示的Creative AI目录误认成主会全目录。

目前并未逐篇阅读全部纳入论文的全文。元数据缺失、数据库覆盖、题名版本差异和自动主题筛选仍可能造成遗漏或边界误差；因此这些值用于展示检索范围内的研究活跃程度，不用于给出全领域精确规模或方法优劣结论。未核定记录及原因由脚本写入本地 `excluded.csv`，不能把它们当作已经不存在的论文。

## 当前年度结果

| 年份 | 四维动态场景重建 | 面向交互的世界模型 | 具身操作动作学习 |
| --- | ---: | ---: | ---: |
| 2015 | 5 | 3 | 11 |
| 2016 | 8 | 0 | 13 |
| 2017 | 9 | 2 | 11 |
| 2018 | 10 | 3 | 71 |
| 2019 | 8 | 6 | 92 |
| 2020 | 12 | 5 | 127 |
| 2021 | 29 | 13 | 192 |
| 2022 | 18 | 23 | 207 |
| 2023 | 38 | 36 | 300 |
| 2024 | 84 | 71 | 377 |
| 2025 | 186 | 170 | 595 |
| 2026（截至10月29日，已核记录） | 83 | 139 | 209 |
| 合计（各专题分别计） | 490 | 471 | 2205 |

2026年一栏是**截至10月29日具有可核正式公开证据的部分年度检索数量**，不作年化。除年度尚未结束外，来源目录和出版元数据的完整性也影响这一栏；它不能与2025全年值直接比较增减，更不能仅据此解释为领域降温。未核定时点的候选记录保留待定，不当作未发表或不存在。

清洗结果见[quality_audit.json](quality_audit.json)，逐条纳入清单见[papers.csv](papers.csv)，排除及重复记录由脚本在本地生成 `excluded.csv`，绘图值见[yearly.csv](yearly.csv)与[yearly.json](yearly.json)。

## 2026年截止条件的实际执行

2026年记录需通过以下任一证据，才进入数量图：

1. 精确命中截至2026-10-29已公开可访问的正式主会目录。当前补核[CVPR 2026](https://openaccess.thecvf.com/CVPR2026?day=all)、[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026)、[ICML 2026 / PMLR 306](https://proceedings.mlr.press/v306/)，每条保留目录观察日与正式论文链接。目录观察日证明截至日可访问，不伪称论文在观察日才发表。
2. 正式来源和年份已核定，且Crossref的`published-online`、`published-print`或`published`具有真实日期，所表示的完整日期区间不晚于截止。日精度按该日；月精度按整月区间；年精度按整年区间。若只有2026年10月或仅2026年，区间跨过10月29日且缺更早正式online证据，则保守留待定；11—12月未来卷期同样不能仅凭已登记DOI计入。

`created`、`deposited`、`indexed`以及Semantic Scholar的预印本`publicationDate`均不充当正式出版截止证据。期刊若有更早的正式online日期，可据其判断截至日已公开，归属年份仍按已采用的正式卷期年保持一致；不以1月1日或月初伪补缺失日期。仅DBLP后缀26、会议接受状态或未来会议日程不足以证明已正式出版。NeurIPS 2026主会在12月，[官方日程](https://nips.cc/Conferences/2026/Dates)本身也不能证明10月已经出版；不把未来年度或待出版记录静默纳入。

逐条证据见`papers.csv`（排除记录在本地生成的`excluded.csv`）中的`publication_cutoff_status`、`publication_date_parts`、`publication_date_precision`、`publication_evidence_url`及区间边界；边界是日期精度表达，不是推测的实际出版日。[cutoff_2026_review.csv](cutoff_2026_review.csv)另列15条定向核查，包括预印本首发、正式期刊online、跨截止月/年精度、未来卷期及相似会议误匹配。

## 独立抽查及本轮修正

[relevance_review.csv](relevance_review.csv)记录60条命中抽样（每专题20条，固定随机种子）和30条定向边界复查，共90条记录、80个不同的专题内paperID。保留题名/摘要可读性、人工判定、判别依据、抽样时自动结果及当时自动判定，并新增最终快照结果列（原人工标签保留）；抽查用于发现并修正规则，不据此声称总体精确率或召回率。

本轮主要修正包括：

1. 原检索短语漏掉D-NeRF、Nerfies、HyperNeRF和DynamicFusion等代表工作，补充可变词序、非刚性融合及点图/持续感知相关表达，并回查MonST3R、CUT3R。
2. 不将S2合并记录中的首发年当正式发表年，例如4D-GS 2023→2024、MonST3R及Shape of Motion 2024→2025；正式目录或DOI的证据留在逐条清单。
3. 不从来源别名列表推断主会议，不把VISAPP误匹配成ICCV；SAD-GS错挂的CVPR22键也不能覆盖其CVPRW2024 DOI。先核体裁再处理来源和年份。
4. 排除GSplatLoc、SDD-SLAM、MetaEarth、纯导航和硬件展望提及学习等误命中。Q-Manipulation既非机器人操作学习，又由[IJCAI官方记录](https://ijcai.org/proceedings/2025/1244)确认为两页Doctoral Consortium，已从统计中排除。
5. 旧版统计的检索、来源和归年规则已停用，其配置与年度结果不再保留在仓库；新旧规则不同，不能将其差值解释成新增发表量。

## 复现与图表

原始响应、目录清单和 Crossref 元数据按需抓取，缓存在本地，不纳入仓库；仓库只保留清洗后的汇总结果。重新抓取并完整复现当前快照：

```sh
python3 scripts/literature_catalogs.py fetch
python3 scripts/literature_stats_v2.py fetch
python3 scripts/literature_catalogs.py analyze
python3 scripts/literature_stats_v2.py analyze
```

新抓取可能受索引更新影响，不能要求未来结果与当前快照完全一致。Crossref出版元数据缓存按DOI哈希命名，可用标准`https://api.crossref.org/works/{DOI}`重取。已入库的`yearly.json`、`timeline_nodes.json`等汇总值可直接查阅，无需联网。

当前三张专题图分别位于 `latex/figures/chapters/ch01-basis/` 下的 `reconstruction-timeline/`、`world-model-evolution/` 和 `action-learning-timeline/`，每项保留 `diagram.svg` 与正文使用的 `figure.pdf`。图源编辑与 PDF 导出独立于统计脚本，入口见[图件说明](../../latex/figures/README.md)；更新统计数据不会自动重绘 SVG。节点数据见[timeline_nodes.json](timeline_nodes.json)。

[analysis_manifest.json](analysis_manifest.json)保存统计快照的输入及处理脚本哈希、独立对账结果与年度数值；当前图源及导出件的校验值见[图件登记表](../../latex/figures/manifest.json)。统计清单中的哈希对应抓取当日的快照，其中排除表、目录汇总及原始缓存不随仓库分发。当前核验包括专题内唯一ID/DOI、正式年份范围、CSV与年度数独立对账、2026逐条截止证据，以及人工识别的排除项未进入最终统计。
