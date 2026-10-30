# 插图与素材

## 当前正文插图

[world_model_applications.tex](world_model_applications.tex)作为图 1，与 1.1 的应用需求段相邻。上方组合无人机试验、飞机维护及飞行仿真驾驶舱的真实照片，下方以世界模型的环境状态建模、动态演化预测及动作后果推演能力共同支撑三类场景。三组素材属于同一张图，不作为子图，不使用子图编号，普通场景标签置于照片下方。原图等比例摆放并裁切，标签、底纹和箭头保持矢量可编辑；配色沿用第二部分的蓝白方案（深蓝标题与箭头、中蓝引线与细边框、浅蓝底纹）。图片来自 NASA/JPL 与 NASA 官方来源，仅示意应用需求。原始图像、摄影署名及校验值见[素材说明](materials/world_model_applications/README.md)。

运行 [build_world_model_applications.py](build_world_model_applications.py) 可导出[独立 PDF](generated/world_model_applications/figure.pdf)、[彩色预览](generated/world_model_applications/figure.png)和[灰度预览](generated/world_model_applications/figure-gray.png)。主报告可直接用本地原图编译，日常构建无需联网。

此前 [dynamic_world_motivation.tex](dynamic_world_motivation.tex) 的 PhysTwin 布料背景图暂时停用，源文件、素材、来源及旧导出稿保留供追溯。1.2 的三个专题各有一张独立数量图和一张不等距时间轴，图号由正文顺延。2.2 只保留一张纯文字研究内容总框图；四张问题图源保留但不载入正文。3.2 展开总体及四项技术路线，3.3 说明候选数据与运动评价。以下按章节和图源名称定位，避免编号随前文增删失效。

## 1.3.1 前期工作方法图（2026-10-29）

[cofuse4d_method.tex](cofuse4d_method.tex)为 1.3.1 的 MoSca 风格四阶段方法图，图题为“CoFuse4D 的方法框架”，标签为 `fig:cofuse4d-method`。分栏沿用 MoSca 方法图的 (A)—(D) 组织：A 基础观测、B 背景与身份关联、C 连续时间运动、D 高斯联合重建；图内不出现具体 prior 模型名称，对象身份、轨迹和深度均用通用标签。图按自然尺寸载入，不套 `\resizebox`：图内用 `\useasboundingbox` 固定 14.75 cm 边界，可见内容约 14.4 cm；`\resizebox` 会把不可见边界余量一起缩放，导致图在栏内左移、右侧留白。2026-10-29 去掉 A→B、B→C、C→D 三根过短的灰色阶段箭头，避免被读成三角形或杂点；阶段顺序由 (A)—(D) 标签、图内布局和正文说明承担，保留时间轴、节点/查询指示、DQB 与 GP↔高斯联合更新等有语义的细箭头。

图像素材位于 [materials/cofuse4d/method/](materials/cofuse4d/method/)：DyCheck apple 序列的三帧 RGB（`input_00000/00118/00237.png`）、深度 `depth_118.png`、对象身份 `identity_118.png` 和轨迹叠加 `track_overlay_118.png`。输入帧与深度取自 `/remote_databuffer/pomelo4d/datasets/DyCheck/iphone/apple`；身份图为对象身份可视化，轨迹叠加为本报告绘制。素材仅用于说明方法流程，不作为实验结果。

## 1.3.2 前期工作方法图（2026-10-29）

[psvla_method.tex](psvla_method.tex)为 1.3.2 的 PS-VLA 方法图，图题为“PS-VLA 的方法框架”，标签为 `fig:psvla-method`。图沿用 BridgeVLA 的 2D 热图预训练与 3D 动作微调两阶段结构，底部增加 PS-VLA 的持续状态条：动作条件先验、观测更新和动态 LoRA 适配；冻结/训练分别用六角雪花和火焰标记。源图按 18.3 cm 宽绘制，报告使用导出的[矢量 PDF](generated/psvla_method/figure.pdf)按栏宽载入，[PNG 预览](generated/psvla_method/figure.png)供检查；TikZ 源保留可编辑。图内不写具体实验结果，只说明状态更新与动作适配的流程。2026-10-30 按确认预览统一顶部与中部主流程的水平箭头基线，调整上栏内边距及输入位置，并将 gate 回路弱化为外侧辅助虚线。

## 插图版式约定（2026-10-28）

带子图的插图统一采用自然子图版式：各子图共享一条基线、等高排列，宽度按各自长宽比确定，不额外加面板边框；子图编号与标题排在**图的下方并相对该子图水平居中**，使标题与图形读作一个整体。全图仍只保留一个总图题。

第三部分的五张技术路线图按各自内容组织布局，以深色标题条、浅色机制区和细框表达层次。相同层级的并列模块使用一致的宽高和内边距；关系、变量和图例留在所属模块内，连接通道只保留箭头。普通文字采用与正文相同的宋体，主要模块及需要强调的环节使用宋体加粗，数学符号沿用正文公式字体。灰度下由线型、节点形状和深浅保持可读。

## 运动评价图（3.3）

[可编辑指标图源](evaluation_motion_metrics.tex)并列解释二维 PCK 与三维轨迹误差：左侧按阈值内对应计数，右侧用误差段表示同一时刻的位置差。图中 2/3 是计数示例，不是实验结果。图形、公式和子图标题保持既有自然尺寸与灰度可读性。

2026-10-30 删除原航空维修与拟建试件图及其默认导出，正文不再引用 `fig:evaluation-datasets`。原始素材与历史来源保留供追溯，不构成当前验证条件。公开数据与参考类型见[当前来源说明](materials/evaluation/README.md)。

运行 [build_evaluation_figures.py](build_evaluation_figures.py) 仅导出指标图的独立 PDF、彩色与灰度预览，输出及校验见[清单](generated/evaluation/manifest.json)。主报告直接载入指标图 TikZ 源，日常编译无需下载数据或媒体。

## 技术路线图（3.2）

2026-10-30 连接术语统一为“物理连接”：$\mathcal E(t)$ 对应观测估计的物理连接，保持、失效或待定描述其状态。总体路线中的连接判断、拓扑分图的输出和动作预测图的关系类型采用同一名称；原有公式、字号及配色保持一致。

2026-10-30 按导师意见统一使用观测置信度及其高／低分级；观测支持、估计不确定性及置信度分别说明，不把一致性得到的分数当作正确概率。研究框架顶部题名同步为“连续动态世界模型构建方法研究”。当前研究定位、术语及页面核对以正文和本说明为准。

2026-10-30 统一第三部分机制图与指标图的字体与配色。共享字号在 [technical_route_styles.tex](technical_route_styles.tex) 维护：主标题 9.2 pt 宋体加粗，阶段标题 8.2 pt 宋体加粗，普通正文 8.2 pt，图例、辅助说明及卡片副标题均为 8 pt；主公式 9.2 pt，小号公式 8.5 pt，数学上下标按正常规则缩小。指标图的子图标题统一为 9.2 pt 宋体常规；全图图题沿用模板的 10.5 pt 宋体。全部采用自然尺寸载入，避免整体缩放后字号变化。

本轮同时统一并列框尺寸：总体图三列、各列阶段卡片、左下动作与历史输入、底部三个验证环节均按各自同层级等宽等高；连续时间图三机制面板、空间与拓扑图各自两个并列面板、动作预测图三输入框／三机制面板／四评价与更新步骤分别一致。拓扑图的形成区间与历史标签、响应图图例、总体图待定归属标注已错开图形线条；两个验证表也统一为 10.5 pt。当前报告页面及彩色／灰度检查以[技术路线图导出预览](generated/technical_routes/)为准。

五张技术路线图均为拟研究机制的可编辑 TikZ 图，不是实验结果。总体图已于 2026-10-29 按确认版布局重绘，当前导出见[独立矢量 PDF](generated/technical_routes/technical_route_overview.pdf)，采用 [technical_route_styles.tex](technical_route_styles.tex) 的共享样式，当前自然画布为 15.56 cm 宽、约 15.66 cm 高；在保持文字尺寸的前提下调整阶段卡片间距与图例位置：顶部为视频观测输入；中部三项研究通过双向约束共同构建“时空一致的连续动态场景表征”，并沿用 3.1 的五分量公式及各分量中文含义；第四项读取 $t_0$ 表征、给定动作与已获历史，按关系类型组织响应并连续推演；预测结果保存后与后续记录对照，随后更新表征及历史；底部为公开数据与机制验证。

四张分项图 [technical_route_time.tex](technical_route_time.tex)、[technical_route_space.tex](technical_route_space.tex)、[technical_route_topology.tex](technical_route_topology.tex)、[technical_route_response.tex](technical_route_response.tex) 已于 2026-10-30 按第三版机制确认稿重绘并集成正文，当前导出见[技术路线图预览](generated/technical_routes/)。四图均以 **15.56 cm 宽、8.25–8.57 cm 高**的自然画布排入，按各自内容采用三列证据—支撑—联合求解、两栏归属—共享—联合恢复、单次切分事件加双分支历史、输入—编码—关系传播—动力学—预测、评价与观测更新链的布局；第三版的固定 16×10.5 cm 画布、大面板和重复示意已删除。字体、标题条、浅色示意区和细框线沿用图 10／图 11 与 [technical_route_styles.tex](technical_route_styles.tex)，四项主题色仍为蓝、绿、赭棕、紫；灰度由实线／虚线／点划线、圆／方／菱形和深浅共同区分。

普通说明文字为黑色，标题反白；浅蓝、浅绿、浅赭和浅紫分别对应时间、空间、拓扑和动作响应四项研究。示意图中的蓝色用于连续轨迹、部件 A 及材料运动历史，绿色区分部件 B，赭色用于连接变化及新生表面历史，紫色用于速度、动作作用及未来预测。具体含义由相邻标签说明；灰度由线型、圆／方／菱形及深浅共同区分。

总体技术路线图与研究框架图的分工已明确：研究框架图说明四项研究的组织关系，总体技术路线图以共同表征为中枢说明实现层面的信息流，底部文字限定预测只使用截至 $t_0$ 的历史，后续到达的新观测通过虚线写回表征。五图的线型解释、示意声明及小示意图内的成句解说均移入相邻正文，图内只保留阶段、变量、时段和必要关系标签；图片与首次实质讨论它的段落相邻，图题仅保留标题。主报告中的四张分图图题与 3.2 现行小节名称一致，总体图图题为“连续动态世界模型总体技术路线”。

| 位置 | 可编辑图源 | 说明 |
| --- | --- | --- |
| 3.2 总体路线 | [technical_route_overview.tex](technical_route_overview.tex) | 2026-10-29 已重绘：共同表征、各项输出、给定动作、离线评价及后续记录更新 |
| 3.2.1 连续时间 | [technical_route_time.tex](technical_route_time.tex) | 2026-10-30 已重绘：观测置信度、局部时间支撑与表达配置、观测残差与共享约束的联合更新及回校正 |
| 3.2.2 空间结构 | [technical_route_space.tex](technical_route_space.tex) | 2026-10-30 已重绘：多证据关联、跨时刻软归属、归属导出的共享权重及联合恢复 |
| 3.2.3 连接变化 | [technical_route_topology.tex](technical_route_topology.tex) | 2026-10-30 已重绘：一次切分事件、局部连接与表面更新、材料运动历史与表面存在区间 |
| 3.2.4 动作预测 | [technical_route_response.tex](technical_route_response.tex) | 2026-10-30 已重绘：三类关系传播、连续动力学与分步积分、预测输出、离线评价及后续观测修正 |

[generated/technical_routes/](generated/technical_routes/) 下的独立 PDF、彩色及灰度预览和 [manifest.json](generated/technical_routes/manifest.json) 已由 [build_technical_route_figures.py](build_technical_route_figures.py) 统一重导出：总体图状态为 `redrawn`，四张分图为 `integrated`；清单同时记录 15.56 cm 自然画布宽、各图页面尺寸和校验值。脚本按自然尺寸导出，总体图独立页面保留 3 mm 边框，四张分图为 1 mm 边框，报告直接载入 TikZ 源码，不套 `\resizebox`。可用 `--only` 只导出指定图；共享样式中的旧四阶段兼容定义已清理。四图的页面尺寸记录见[导出清单](generated/technical_routes/manifest.json)。

以下为已停用布料背景图的追溯入口，日常编译不使用，独立图导出脚本也暂时不运行：

- [原图位置及来源说明](materials/phystwin_cloth/README.md)、[逐文件校验及时间阶段](materials/phystwin_cloth/source-manifest.json)。
- [素材处理脚本](build_world_model_paradigm.py)：保留六张原始 JPEG，只为中央渲染制作背景透明的轮廓裁图。
- [独立图导出脚本](export_world_model_paradigm.py)：主报告本地编译后导出[矢量图](generated/world_model_paradigm/figure.pdf)和[预览](generated/world_model_paradigm/figure.png)。文字、箭头、显示比例和布局均在 TikZ 中修改。

素材和生成图随源码保存，日常编译只需运行项目根目录的 `scripts/build.sh`，无需重新下载论文或提取图片。修改素材时按上述来源说明重现；当前应用场景图使用本节所列新脚本导出；旧布料图恢复使用后才运行其导出脚本。

## 研究现状插图（1.2）

三个专题各自配一张年度论文数量图和一张不等距时间轴，数量与关键工作分开表达。正文直接载入 TikZ 源码，保持自然尺寸，不再对六张图统一使用 `\resizebox{\linewidth}{!}`。数量图采用较小幅面，时间轴按节点和标签需要确定宽高，不以铺满行宽为目的。

| 位置与图形 | 可编辑图源 | 读图重点 |
| --- | --- | --- |
| 1.2.1 重建论文年度数量 | [literature_counts_reconstruction.tex](literature_counts_reconstruction.tex) | 指定主要来源中的动态重建主题相关正式论文 |
| 1.2.1 重建关键工作时间轴 | [literature_timeline_reconstruction.tex](literature_timeline_reconstruction.tex) | 隐式场表征、显式图元表征、点图表征三类路线 |
| 1.2.2 世界模型论文年度数量 | [literature_counts_worldmodel.tex](literature_counts_worldmodel.tex) | 指定主要来源中的交互世界模型主题相关正式论文 |
| 1.2.2 世界模型关键工作时间轴 | [literature_timeline_worldmodel.tex](literature_timeline_worldmodel.tex) | 潜在状态、视觉表征、三维结构与未来观测四类预测量 |
| 1.2.3 动作学习论文年度数量 | [literature_counts_action.tex](literature_counts_action.tex) | 指定主要来源中的具身操作动作学习主题相关正式论文 |
| 1.2.3 动作学习关键工作时间轴 | [literature_timeline_action.tex](literature_timeline_action.tex) | 直接策略、预测辅助决策、世界动作联合生成三种使用方式 |

数量图统计 2015—2026 年，其中 2026 年为不完整年度（截至 2026-10-29 已正式发表的记录），图中以星号和白柱单独标出，不与完整年度直接比较。柱体为中蓝色、边框为深蓝色，2026 年柱为白底深蓝边框，与第二部分研究框架图的配色一致。它们反映明确检索范围内的正式论文数量，不是领域全量；三个主题可能交叉，不作加总。当前检索、主题筛选、来源核验、正式归年及 DOI／题名去重见[统计说明](../../docs/literature_stats/README.md)，入口为 [literature_stats_v2.py](../../scripts/literature_stats_v2.py)。`raw/v2/` 保存当前查询缓存，Crossref 和正式论文集目录用于核对正式发表信息；原脚本与旧缓存只供旧版追溯，不用于日常重算。

时间轴保留日历年份，较早年份压缩、近年年份展开，保留年份刻度与断轴标记，不再添加版式解释文字。各方法类别并行排列，节点仅以方法名称呈现，具体推进说明由正文承担；水平距离和节点疏密不用于量化热度，也不表示方法之间存在直接继承关系。正式节点按论文集或卷期年份归年，时间轴可延伸至 2026 年；WorldVLA、DreamZero 等预印本用空心节点和 `†` 单独标识。图中文字保持黑色，年份刻度、节点和标签连线采用深蓝—中蓝配色；每一类方法占一行，隔行以浅蓝色带区分；色带按行高铺满，节点及其上下的方法名称都落在色带内，白色行同理由行标签和年份线界定；所选年份的竖向参考线贯穿各行，轴端以箭头收束；底纹及实心／空心标记支持灰度阅读。

数据与图源分离：[yearly.json](../../docs/literature_stats/yearly.json)提供数量，[timeline_nodes.json](../../docs/literature_stats/timeline_nodes.json)提供节点、路线和文献键。[生成脚本](build_literature_trend_figures.py)导出六张图的独立矢量 PDF、彩色及灰度 PNG，保存在 [literature_trend/](generated/literature_trend/)。修改正文中的统计数值时保持该数据与生成的 `stat_values.tex` 一致。

```sh
python3 latex/figures/build_literature_trend_figures.py
```

`--timelines-only` 仅重绘三张时间轴，`--tex` 仅重写图源而不导出独立图。主报告使用已生成的本地图源及数据，日常编译不需要联网。

以下旧图已停用，源文件、素材、来源记录及历史导出稿可追溯，正文不再载入，也不纳入当前六图的生成流程：

- [literature_counts_overview.tex](literature_counts_overview.tex)：此前聚合三个专题的年度数量图，其旧统计值不作为当前数据。
- [literature_reconstruction.tex](literature_reconstruction.tex)：动态场景重建结果示例。
- [literature_prediction.tex](literature_prediction.tex)：动作条件三维场景预测示例。
- [literature_action_paradigms.tex](literature_action_paradigms.tex)：具身操作建模范式示例。

## 研究框架图（2026-10-29 版）

[research_framework.tex](research_framework.tex)为 2026-10-29 重绘并纳入 2.2 的研究内容总框图，图题为“连续动态世界模型研究框架”，标签 `fig:research-framework`，图号由 LaTeX 自动编号。图位于 2.2 总述之后、四项内容之前；正文插入时以 `\resizebox{\linewidth}{!}` 将整图等比缩放到版心宽度并用 `\centering` 居中，不逐元素挪移像素。

- 布局：顶层为总主题“连续动态世界模型构建方法研究”；两个科学问题各在完整边框内，按内容收窄并分别置于前三列与第四列上方；第一问统摄前三项研究内容，第二问对应第四项，框下以短引线和分配横线标示对应关系；四个研究内容列各有深色标题栏（标题居中，不设序号）和一个“研究问题”框（框内说明该项要解决的具体问题）；底部两组括线标“连续动态表征的协同构建”“表征与预测的内在联系”。
- 列标题采用 2.2 的四个小节名，科学问题标题采用 2.3 的两个小节名，图内名称与正文一致。2026-10-30 科学问题更新为“不完备观测下连续运动与场景结构的可区分条件”“动作响应差异的表征依赖与误差传递机理”，保留原有框架及字号。
- 图内不放箭头、数据流、观测或动作输入、状态变量、算法步骤、新观测修正、实验反馈回路和集成验证流程，也没有立方体、轨迹、点云等小示意图；研究组织只由文字、边框、无方向连线和括线表达。
- 配色为蓝白方案：深色标题栏配反白标题，浅蓝底纹、白底细边框，其余文字为黑色；灰度下由字号、框线和文字区分层次，另附灰度预览。
- [独立矢量 PDF](generated/research_framework/figure.pdf)、[PNG 预览](generated/research_framework/figure.png)、[灰度打印预览](generated/research_framework/figure-gray.png)。
- [本地构建脚本](build_research_framework.py)：使用 MacTeX/XeLaTeX 和 pdftoppm（缺少时回退到 Ghostscript），Python 只使用标准库。运行 `python3 latex/figures/build_research_framework.py` 即可更新独立图，不改动主报告。

2026-10-26 版曾以统一状态 $S(t)$、视觉示例和箭头／虚线反馈描述研究流程，属历史版本，已由本版替代，不再作为现行图描述。第二部分本轮只保留这张总图；四张旧问题图不再载入正文，源文件与旧导出保留追溯，见下节。

## 研究内容问题图（2026-10-26 旧图，保留追溯）

**历史（2026-10-26）。** 以下四张图曾配 2.2 各项问题分析，现已不再载入正文，仅保留源文件、素材及旧导出稿供追溯；表格与导出脚本说明保留，便于查阅。

四张图均为本报告原创的定性示意，曾分别同首次讨论轨迹 A/B、对象 A/B、结构事件中的历史关系及动作响应差异的段落相邻。第一项先用观测歧义明确问题，再讨论已有方法及剩余困难；第二项先交代空间组织的已有基础，再分析归属实例；第三项先建立真实结构改变及历史关系的直观含义，再讨论表面建模方法和观测判据；第四项从已有世界模型引出响应差异，再展开建模思路。图可位于相关段落前或后，均用于辅助附近的论证，图题只保留标题。

| 位置及图题 | 可编辑图源 | 读图重点 |
| --- | --- | --- |
| 2.2.1：有限观测下的连续运动歧义 | [research_problem_time.tex](research_problem_time.tex) | 两条轨迹经过完全相同的采样位置，帧间过程仍有差异；两条曲线均不指定为真实轨迹或方法结果 |
| 2.2.2：不完整观测下的空间归属 | [research_problem_space.tex](research_problem_space.tex) | 两个独立对象短时共动，后续相对运动提供关联证据；A 旋转后显露的已有表面补入原对象 |
| 2.2.3：真实结构变化后的表征更新 | [research_problem_topology.tex](research_problem_topology.tex) | 切割使旧共享约束失效并产生新生边界；右侧为稳定区域延续历史、从形成时刻记录新边界的预期能力 |
| 2.2.4：动作响应对初始状态的依赖 | [research_problem_response.tex](research_problem_response.tex) | 固定其余条件，分别改变初始运动或有效连接；在同一动作下示意不同后果，第二行的动作作用于右侧物体 |

- [共用样式](research_problem_styles.tex)维护字号、框线和箭头。图内文字及主体线条均为黑色；运动箭头、粗动作箭头、虚线未来轮廓及斜线表面标记共同表达含义。动作响应图的浅灰轮廓表示当前参考位置，正文同时说明虚线角色。
- [本地导出脚本](build_research_problem_figures.py)只使用 Python 标准库、本地 MacTeX/XeLaTeX 及 pdftoppm，不下载媒体，不依赖照片。运行 `python3 latex/figures/build_research_problem_figures.py` 更新四份独立矢量图、彩色和 `-gray.png` 灰度预览。
- 独立图：[时间](generated/research_problems/research_problem_time.pdf)、[空间](generated/research_problems/research_problem_space.pdf)、[拓扑](generated/research_problems/research_problem_topology.pdf)、[响应](generated/research_problems/research_problem_response.pdf)；[生成清单及语义范围](generated/research_problems/manifest.json)记录图源及导出文件校验值。
- 示意图用于说明研究矛盾和拟达到的能力，不代表实验结果，也不预设网络、训练流程或已经验证的改进。空间归属图的首次显露和拓扑变化图的物理新生依据物理含义区分，斜线仅突出当前讨论的表面区域。

## 重写前的旧稿

2026-10-22 之前的旧稿插图及脚本保留在 Git 历史（标签 `20261028v1`）的 `archives/2026-10-22-before-rewrite.zip` 中，需要查看时从该标签导出；当前工作区不再保留展开副本。
