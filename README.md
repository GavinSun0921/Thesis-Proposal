# 孙国栋博士开题报告

题目：**非完备观测下动态世界模型的状态表征与预测研究**。

报告正文以 LaTeX 为唯一维护源，工程保留一层 `latex/` 目录，入口为 [latex/main.tex](latex/main.tex)。编译结果统一放入 `latex/build/`，不再维护个人 Word 稿或重复的工程包。学校原始模板保留在 `材料/`。

## 编辑位置

| 内容 | 文件 |
| --- | --- |
| 一、学位论文研究依据 | [latex/chapters/01-basis.tex](latex/chapters/01-basis.tex) |
| 二、学位论文研究内容 | [latex/chapters/02-content.tex](latex/chapters/02-content.tex) |
| 三、学位论文研究计划及预期目标 | [latex/chapters/03-plan.tex](latex/chapters/03-plan.tex) |
| 四、参考文献（输出位置） | [latex/chapters/04-references.tex](latex/chapters/04-references.tex) |
| 姓名、学号、导师、日期及勾选项 | [latex/metadata.tex](latex/metadata.tex) |
| 封面、页框、表格和标题样式 | [latex/npu-report-style.sty](latex/npu-report-style.sty) |
| 学校模板的六条填写要求 | [latex/requirements.tex](latex/requirements.tex) |
| 参考文献条目 | [latex/references.bib](latex/references.bib) |
| 参考文献排版规则 | [latex/npu-gbt7714-numerical.bst](latex/npu-gbt7714-numerical.bst) |
| 文献发表状态核查 | [docs/reference_audit.md](docs/reference_audit.md) |
| 插图及生成说明 | [latex/figures/](latex/figures/) |
| 总体研究框架图（可编辑矢量源） | [latex/figures/research_framework.tex](latex/figures/research_framework.tex) |
| 写作安排和此前研究讨论 | [docs/](docs/) |

第一部分按“1.1 选题背景及研究意义—1.2 国内外研究现状与发展态势—1.3 已有工作积累与研究基础”组织。

第二部分按“2.1 研究目标—2.2 研究内容—2.3 拟解决的关键科学问题”组织。2.2 和 2.3 各设四个 `subsubsection`，对应四项研究内容及科学问题，仅增加这一层细分；研究特色融入研究内容，不单设小节。2.2 每项以一段概述研究问题、核心思路与预期能力，具体算法、基线、指标和实验流程在第三部分展开。

第三部分在同一文件中组织研究方法、可行性、时间计划及预期成果。模板原有三个分项标题和字面“1./2./3.”作为固定文字保留；研究方法与可行性使用普通 `subsection`，按 3.1—3.8 连续编号。“3.研究计划及预期成果”后直接接计划表，随后使用无编号标题“预期创新点及成果形式”。第二、第三、第四大部分均另起新页；参考文献统一置于末尾第四部分，按正文首次引用顺序编号。

## 编译

使用 **XeLaTeX + BibTeX**，建议安装完整 TeX Live / MacTeX。进入 `latex/` 目录编译：

```sh
cd latex
latexmk -xelatex -halt-on-error -interaction=nonstopmode main.tex
```

生成的报告为 `latex/build/main.pdf`，编辑器的主文件选择 `main.tex`。[latex/.latexmkrc](latex/.latexmkrc) 已统一编译目录，中间文件无需提交到仓库。

中文字体默认回退到 TeX Live 自带的 Fandol，优先使用已安装的宋体、黑体和楷体；英文字体优先 Times New Roman，缺失时使用 TeX Gyre Termes。字体文件不随项目复制。

## 远端同步范围

版本控制保留报告正文、研究笔记、文献库、排版规则、编译配置、封面信息和正文引用的插图。[.gitignore](.gitignore) 排除 `材料/` 中的原始模板和参考报告、`tmp/` 中的临时检查文件、`latex/build/` 中的编译产物，以及系统及编辑器临时文件。这些文件保留在本地，不随仓库同步；远端源码的编译不依赖 `材料/` 或 `tmp/`。

## 模板与当前内容

版式以本年度教务系统下载的 `材料/西北工业大学研究生学位论文开题报告表.doc` 为准。保留封面字段、填写要求、三个正文栏目、研究计划表和备注栏，另将参考文献独立为第四部分。A4 纸，左右页边距 24 mm、上下 22 mm，正文边框及表格总宽 162 mm，正文小四、18 pt 行距。

正文围绕可靠状态表征与观测融合、缺测期间的状态演化与未来预测、重观测关联与持续校正、动作条件预测状态学习与交互验证四项内容展开，以 CoFuse4D 和 PS-VLA 为已有基础。四项内容分别明确输入输出、方法重点及评价证据。研究计划为 2026.10—2028.10，沿用已确认的题目和两幅无图内文字的概念插图；第二部分新增总体研究框架图，按“总体目标—四项研究内容—对应科学问题”组织。

两项工作暂用以下论文名称，均正在准备向 CVPR 2027 投稿。CVPR 属于 [CCF 推荐 A 类国际学术会议](https://www.ccf.org.cn/Academic_Evaluation/AI/zgjsjxhtjgjxshy/al/2017-04-25/592032.shtml)。

| 工作名称 | 暂定论文题目 |
| --- | --- |
| CoFuse4D | CoFuse4D: Dense Correspondence Fusion for Dynamic Gaussian Splatting |
| PS-VLA | PS-VLA: Learning Action-Conditioned Predictive States for Robotic Manipulation |

已形成可供通读和讨论的初版，包含 45 条参考文献（中文 6 条、英文 39 条）、两幅概念插图与一幅研究框架图、两张内容比较表及学校要求的研究计划表。框架图以 LaTeX 原生矢量方式绘制，随正文编译，文字及连线均可直接修改；横向实线表示前三项内容的递进，虚线表示向动作条件交互的扩展，纵向连接对应科学问题。综述补充了预测状态基础、视觉世界模型、动态辐射场与高斯运动表示、三维机器人操作及不确定性方法；代表工作比较表逐项标注引用。研究计划分项标题与计划表保持同页，表前不再增加编号小节及说明段落；备注保留在第三部分末页，参考文献随后另起一页。页数与各部分起始页以最新编译结果为准。

文献优先采用正式出版版本，已核对当前 45 条文献的书目信息与发表状态，具体结果见核查记录。新增 23 条均采用正式会议或期刊版本，中文文献保留中文作者、题名和刊名。参考文献不显示 URL 或访问日期，保留 DOI；预印本保留 arXiv 编号，仅确认录用的条目明确注明状态。原始出处 URL 作为元数据保留在文献库中，便于后续复核。排版规则在工程内统一设置，新增条目沿用相同规则。

## 内容规划与管理

[内容规划与管理](docs/proposal_content_plan.md) 按博士开题的七项要求逐项组织：文献综述、选题背景及其意义、研究内容、研究特色、工作难点、预期成果、可能的创新点。现稿已展开背景与文献比较、四项研究任务及科学问题、方法设想及目标函数、数据与评测、可行性和难点、阶段成果与候选创新。规划文件同步维护覆盖情况、证据缺口和后续讨论顺序；正式文字只在 LaTeX 中维护。

文献已核对出处和主要任务定位，最接近方法的详细协议仍需深入比较。两项已有工作按前期探索表述，尚未填入未经原始记录核验的性能数值；实际计算条件及实验预算待落实。后续通读优先讨论研究边界、第二项预测路线、第三项关联与校正的独立贡献，以及候选创新的具体差异。研究特色通过问题选择、状态组织和验证方式融入研究内容；可能创新点在第三部分结合比较对象和证据计划表述。预期成果与阶段任务对应。开题次数已选择“第一次”，论文类型同时勾选“基础研究”和“应用研究”。

[题目与主线调研](docs/world_model_topic_review.md) 和 [9 月 26 日讨论记录](docs/research_scope.md) 保留为研究笔记，后者已标明历史版本。
