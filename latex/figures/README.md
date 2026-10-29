# 插图与素材

## 当前正文插图

[dynamic_world_motivation.tex](dynamic_world_motivation.tex)作为图 1 放在 1.1 第二段之后。图中采用 PhysTwin（ICCV 2025）同一布料提拉案例的真实历史观测、三维模型渲染及留出未来预测，真实执行参考另列。图按两行三列排布：上行为视觉观测，下行为三维状态，横轴依次为 $t_1$、$t_2=t$ 及 $t+\Delta t$；竖直箭头表示构建、更新及评价对照，横向箭头表示给定动作后的预测，$\tau$ 标示采样间隔内的查询时刻。图题为“连续动态世界模型的状态构建与演化预测概念示意（PhysTwin 案例素材）”，原工作画面与本课题添加的时间轴、查询及更新箭头已在正文中区分，用于说明研究背景和基本范式。图 2–4 分别放在 1.2 的三个主题中，图 5 为下述研究框架，放在 2.2 开头；图 6–9 分别说明四项研究内容的具体问题；图 10–14 在 3.2 展开总体及四项技术路线，图 15–16 在 3.3 说明候选数据与运动评价。

## 插图版式约定（2026-10-28）

带子图的插图统一采用自然子图版式：各子图共享一条基线、等高排列，宽度按各自长宽比确定，不额外加面板边框；子图编号与标题排在**图的下方并相对该子图水平居中**，使标题与图形读作一个整体。全图仍只保留一个总图题。

分项技术路线图 11–14 采用“编号阶段带”：阶段按序号排列，彼此以箭头连接，阶段标题上方一条细线，承载本研究机制的阶段加浅色底纹与实心序号标记，仅接收或传递信息的阶段用空心序号标记。总体图 10 沿用相同的编号、顶线、底纹和箭头语言，但以共同场景状态为中枢，不画成与分项图相同的顺序流水线。层次由编号、底纹和标记粗细表达，灰度打印不依赖颜色区分。

## 数据与运动评价图（正文图 15–16）

图 15 的 [可编辑图源](evaluation_datasets.tex)为每类数据选取一帧代表性观测，按自然子图版式单行排列，用于区分真实动态、合成、变形交互和机器人操作四种证据类型；不再并列展示同一数据集的多个视角，具体序列条件由正文说明。图 16 的 [可编辑图源](evaluation_motion_metrics.tex)左右并列两项指标，采用与数据集图一致的自然子图版式：左侧以三个容许圆说明 PCK 的“阈值内计数”，逐点标出命中与未命中；右侧以三维坐标框中的误差段说明 EPE 的“同一时刻位置差”。两格共用一条垂直分隔线，公式与子图标题分层放置，标题位于图形下方并居中。读图说明放在图后，图中示例和分数均不作为本课题实验结果。

原始素材、图注范围和指标定义见[来源说明](materials/evaluation/README.md)，逐图裁剪及校验见[生成清单](generated/evaluation/manifest.json)。运行 [build_evaluation_figures.py](build_evaluation_figures.py) 使用本地素材导出[矢量图](generated/evaluation/)、彩色与灰度预览；日常主报告编译直接载入 TikZ 图源及已生成裁图，无需下载数据。

## 技术路线图（正文图 10–14）

五图均为拟研究机制的可编辑 TikZ 图。图 11–14 上方为带序号的阶段流程，下方为无框草图条带，草图标题在图下方居中；图 10 则以三项研究共同完善同一场景状态为总览，再接入动作条件演化及执行后观测反馈。文字保持黑色，以浅蓝、浅绿、浅赭和浅紫区分时间、空间、拓扑和动作响应四项研究；蓝色表示连续轨迹、候选部件 A、保留连接及材料历史，赭色区分时间节点、候选部件 B、失效连接及新边界历史，紫色表示速度、动作作用及未来预测，含义随相邻方法正文说明。灰度打印时层次由序号、底纹和标记粗细表达。

图 10 与图 5 的分工已明确：图 5 说明四项研究的组织关系，图 10 以共同场景状态为中枢说明实现层面的信息流，底部文字限定预测只使用截至 $t_0$ 的历史，执行后的新观测通过虚线写回状态。图 12 图题已与小节名统一为“空间结构表征”。五图的线型解释、示意声明及小示意图内的成句解说均移入相邻正文，图内只保留阶段、变量、时段和必要关系标签。图片与首次实质讨论它的段落相邻，图题仅保留标题。

| 位置 | 可编辑图源 | 说明 |
| --- | --- | --- |
| 3.2 总体路线 | [technical_route_overview.tex](technical_route_overview.tex) | 共同状态、各项输出、给定动作及执行后观测 |
| 3.2.1 连续时间 | [technical_route_time.tex](technical_route_time.tex) | 证据可靠性、局部时间支撑、样条表达配置及几何回校正 |
| 3.2.2 空间组织 | [technical_route_space.tex](technical_route_space.tex) | 多证据关联、软归属及共享约束反馈 |
| 3.2.3 拓扑适应 | [technical_route_topology.tex](technical_route_topology.tex) | 有事件信息条件的局部更新及两类历史 |
| 3.2.4 动作响应 | [technical_route_response.tex](technical_route_response.tex) | 因果初始状态、关系类型、连续演化及执行后修正 |

共用样式见 [technical_route_styles.tex](technical_route_styles.tex)。运行 [build_technical_route_figures.py](build_technical_route_figures.py) 可用本地 MacTeX 导出[五图的矢量 PDF、预览和灰度稿](generated/technical_routes/)，来源及校验映射见 [manifest.json](generated/technical_routes/manifest.json)。主报告直接载入 TikZ 源码，日常编译无需先导出独立图。

- [原图位置及来源说明](materials/phystwin_cloth/README.md)、[逐文件校验及时间阶段](materials/phystwin_cloth/source-manifest.json)。
- [素材处理脚本](build_world_model_paradigm.py)：保留六张原始 JPEG，只为中央渲染制作背景透明的轮廓裁图。
- [独立图导出脚本](export_world_model_paradigm.py)：主报告本地编译后导出[矢量图](generated/world_model_paradigm/figure.pdf)和[预览](generated/world_model_paradigm/figure.png)。文字、箭头、显示比例和布局均在 TikZ 中修改。

素材和生成图随源码保存，日常编译只需运行项目根目录的 `scripts/build.sh`，无需重新下载论文或提取图片。修改素材时按上述来源说明重现；编译完成后可运行独立图导出脚本更新 PDF 和 PNG。

## 研究现状插图（正文图 2–4）

正文的论证顺序决定图文布局，插图和首次实质讨论它的段落作为一个内容单元安排，图在该段前后均可。图 2 配合代表结果的比较，图 3 配合 PointWorld 接口及案例，图 4 配合三类输入输出的比较；随后继续展开相应方法或使用条件。

| 位置及图题 | 可编辑图源 | 代表素材及作用 |
| --- | --- | --- |
| 1.2.1 图 2：动态场景重建的代表性结果 | [literature_reconstruction.tex](literature_reconstruction.tex) | Shape of Motion 的观测、三维轨迹和新视角结果；RetimeGS 同一观测区间的帧间插值 |
| 1.2.2 图 3：动作条件下的三维场景预测 | [literature_prediction.tex](literature_prediction.tex) | PointWorld 同一布料案例的两视角 RGB、给定机器人点流及同一时域的模型预测、参考标注 |
| 1.2.3 图 4：具身操作的典型建模范式 | [literature_action_paradigms.tex](literature_action_paradigms.tex) | OpenVLA、PointWorld、DreamZero 的独立场景缩略图，三行共用“场景示例／研究路线／输入／是否预测后果／输出”列坐标，以中间列是否有内容区分三类形式 |

- [原始图片、来源及使用边界](materials/literature_review/README.md)、[逐图来源和裁剪清单](materials/literature_review/source-manifest.json)。图 2 中的插值不作为未来预测；图 3 明确区分模型预测和参考标注；图 4 不表示三种路线的替代顺序。
- [本地处理及导出脚本](build_literature_figures.py)：默认校验原图，生成裁图并用 MacTeX/XeLaTeX 导出独立矢量图及彩色、灰度预览；需要 Pillow 和 pdftoppm，日常运行不下载媒体。主报告直接使用已保存的图片及 TikZ 图源。
- 独立图：[重建](generated/literature_review/literature_reconstruction.pdf)、[预测](generated/literature_review/literature_prediction.pdf)、[动作学习](generated/literature_review/literature_action_paradigms.pdf)。彩色和 `-gray.png` 灰度预览位于同一目录。
- 文字统一为黑色，使用实线框、分行布局及文字区分角色，色彩仅保留真实素材自身的内容。图源只包含图形主体，图题及标签由正文维护。

## 研究框架图（正文图 5）

[research_framework.tex](research_framework.tex)是 2026-10-26 重画、2026-10-27 精简并纳入 2.2 的研究框架，图题为“连续动态世界模型研究框架”。前三项递进完善同一个场景状态 $S(t)$，第四项结合给定动作预测未来状态，代表性操作提供验证及新观测反馈。该图按研究能力组织，不预设具体网络或训练架构。

- [独立矢量 PDF](generated/research_framework/figure.pdf)、[PNG 预览](generated/research_framework/figure.png)、[灰度打印预览](generated/research_framework/figure-gray.png)。
- [本地构建脚本](build_research_framework.py)：使用 MacTeX/XeLaTeX 和 pdftoppm（缺少时回退到 Ghostscript），Python 只使用标准库。运行 `python3 latex/figures/build_research_framework.py` 即可更新独立图，不改动主报告。
- 曲线、三维几何及拓扑变化均为可编辑矢量示意，不使用合成照片或其他场景的实验结果。
- 图中不再重复科学问题，各模块只保留研究名称和视觉示例；完整问句见正文 2.3。四项名称同 2.2 保持一致；第三项已确认为“拓扑自适应的动态场景表征”，局部表面更新作为其候选机制。
- 打印版式统一使用黑色文字。每项研究的标题和概念示意由同一模块包围，研究四只保留标题卡片；共同状态采用较粗实线框，主流程采用实线箭头，观测反馈采用虚线箭头，预测状态采用虚线框。浅色底纹仅辅助分区，转为灰度后仍由编号、位置、框线和文字表达层次。多行标题按固定行位置排布，保持主稿和独立图的一致性。

## 研究内容问题图（正文图 6–9）

四张图均为本报告原创的定性示意，分别同首次讨论轨迹 A/B、对象 A/B、结构事件中的历史关系及动作响应差异的段落相邻。第一项先用观测歧义明确问题，再讨论已有方法及剩余困难；第二项先交代空间组织的已有基础，再分析归属实例；第三项先建立真实结构改变及历史关系的直观含义，再讨论表面建模方法和观测判据；第四项从已有世界模型引出响应差异，再展开建模思路。图可位于相关段落前或后，均用于辅助附近的论证，图题只保留标题。

| 位置及图题 | 可编辑图源 | 读图重点 |
| --- | --- | --- |
| 2.2.1 图 6：有限观测下的连续运动歧义 | [research_problem_time.tex](research_problem_time.tex) | 两条轨迹经过完全相同的采样位置，帧间过程仍有差异；两条曲线均不指定为真实轨迹或方法结果 |
| 2.2.2 图 7：不完整观测下的空间归属 | [research_problem_space.tex](research_problem_space.tex) | 两个独立对象短时共动，后续相对运动提供关联证据；A 旋转后显露的已有表面补入原对象 |
| 2.2.3 图 8：真实结构变化后的表征更新 | [research_problem_topology.tex](research_problem_topology.tex) | 切割使旧共享约束失效并产生新生边界；右侧为稳定区域延续历史、从形成时刻记录新边界的预期能力 |
| 2.2.4 图 9：动作响应对初始状态的依赖 | [research_problem_response.tex](research_problem_response.tex) | 固定其余条件，分别改变初始运动或有效连接；在同一动作下示意不同后果，第二行的动作作用于右侧物体 |

- [共用样式](research_problem_styles.tex)维护字号、框线和箭头。图内文字及主体线条均为黑色；运动箭头、粗动作箭头、虚线未来轮廓及斜线表面标记共同表达含义。图 9 的浅灰轮廓表示当前参考位置，正文同时说明虚线角色。
- [本地导出脚本](build_research_problem_figures.py)只使用 Python 标准库、本地 MacTeX/XeLaTeX 及 pdftoppm，不下载媒体，不依赖照片。运行 `python3 latex/figures/build_research_problem_figures.py` 更新四份独立矢量图、彩色和 `-gray.png` 灰度预览。
- 独立图：[时间](generated/research_problems/research_problem_time.pdf)、[空间](generated/research_problems/research_problem_space.pdf)、[拓扑](generated/research_problems/research_problem_topology.pdf)、[响应](generated/research_problems/research_problem_response.pdf)；[生成清单及语义范围](generated/research_problems/manifest.json)记录图源及导出文件校验值。
- 示意图用于说明研究矛盾和拟达到的能力，不代表实验结果，也不预设网络、训练流程或已经验证的改进。图 7 的首次显露和图 8 的物理新生依据物理含义区分，斜线仅突出当前讨论的表面区域。

## 重写前的旧稿

2026-10-22 之前的全部旧稿插图及脚本封存在[归档 ZIP](../../archives/2026-10-22-before-rewrite.zip)中。需要查看时解压到项目外的临时目录，包内对应 `latex/figures/`；仓库不再保留展开副本。
