# 博士学位论文开题报告

暂定题目：**连续动态世界模型构建方法研究**。当前写作口径更新于 2026-10-30。

本课题以连续动态场景表征及其动作条件预测为基础研究对象，研究有限观测下运动、空间归属和有效结构的共同恢复，以及这些信息对响应预测的作用。验证依托公开可获取的数据，采用方法比较、机制消融和误差分析；概念例子与图中机制示意用于说明研究内容，不构成特定应用任务或数据采集承诺。

## 当前阅读与源码入口

- [当前报告 PDF](latex/build/main.pdf)
- [主文件](latex/main.tex)
- [第一部分：研究依据](latex/chapters/01-basis.tex)
- [第二部分：研究内容与科学问题](latex/chapters/02-content.tex)
- [第三部分：研究方案、验证与计划](latex/chapters/03-plan.tex)
- [第四部分：参考文献](latex/chapters/04-references.tex)

## 当前结构

第一部分按选题依据、研究现状和前期积累组织。研究现状保留四维动态场景重建、世界模型和具身操作动作学习三个专题，各配代表性工作与发展趋势图；年度数量趋势并入图内，不再单列数量图，统计口径见[统计说明](docs/literature_stats/README.md)。前期积累分别介绍 CoFuse4D 和 PS-VLA，不将其表述为已经完成本课题的四项研究。

第二部分包含整体目标、四项内容和两个科学问题。四项内容为不确定性感知的连续时间场景表征、连续运动引导的对象时空一致性建模、物理连接变化下的动态结构表征与更新，以及动作后果预测与连续动态表征协同建模。问题一研究不完备观测下运动与结构的可区分条件，由前三项共同支撑；问题二研究动作响应预测的状态表征需求与误差传递机理，由第四项展开，连接变化同时联系两个问题。

第三部分依次说明共同理论、总体及四项技术路线、实施验证、可行性、研究条件、困难应对及阶段计划。3.3 目前保留四项技术路线标题，具体实施验证正文待补；数据、参考标注与指标逐项对应。表征恢复与动作条件预测分别评价；连接等直接参考不足时，限定相应结论。研究条件与进度不包含实体试件、实采、机械臂操作或定制应用场景建设。

参考文献在第一部分集中引用，列表置于报告末尾并按首次引用顺序生成。文献库只保留当前正文实际引用的条目；发表状态、数据来源及历史核查见[引文核查记录](docs/reference_audit.md)。

## 写作与图件

- [当前写作约定](docs/proposal_content_plan.md)
- [活动图件登记表](latex/figures/manifest.json)
- [图件目录与路径规范](latex/figures/README.md)
- [图内字体与字号记录](docs/figure_typography_audit.md)
- [第一项工作讨论](docs/continuous_time_representation.md)
- [第二项工作讨论](docs/structured_spatial_representation.md)
- [第三项工作讨论](docs/topology_change_representation.md)
- [第四项工作讨论](docs/action_conditioned_interaction.md)
- [待研究的学术问题](docs/third_part_open_questions.md)

活动图件按章节和语义 ID 收纳于 `latex/figures/chapters/{ch01-basis,ch02-content,ch03-plan}/`，共 13 项，由[活动图件登记表](latex/figures/manifest.json)列明。各项按实际情况保留可用图源、依赖素材及 PDF/PNG 导出；主报告的当前图件以清单中的 `included` 状态和正文引用为准。

总体技术路线当前图源是 [`diagram.svg`](latex/figures/chapters/ch03-plan/overall-technical-route/diagram.svg)，配套 PDF 位于同一语义目录。图件引用统一使用项目内相对路径；SVG 中的图片资源内嵌保存，正常编译不依赖本机临时目录或网络资源。

## 编译

在项目根目录运行：

```sh
./scripts/build.sh
```

当前源码的阅读版构建输出为 `latex/build/main.pdf`，由 `./scripts/build.sh` 根据当前正文和活动图件生成。编辑器主文件选择 `latex/main.tex`；学校模板、匿名开关及字体约定沿用现有配置。日常编译只读取项目内保存的图源和导出件，无需联网下载素材或重新导出 SVG。

`output/` 仅保存正式发布版：[20261030v2](output/main-20261030v2.pdf) 和 [20261028v1](output/main-20261028v1.pdf)，分别对应同名 Git 标签。后续正式版本沿用 `main-YYYYMMDDvN.pdf` 命名；临时预览和候选构建放在本地 `tmp/`，不提交。当前阅读版以 `latex/build/main.pdf` 为准，默认编译不会覆盖正式发布版。

## 文件范围

`latex/` 维护正文及当前活动图件，图源、依赖素材和导出件按章节与语义 ID 放在 `latex/figures/chapters/`，以 `latex/figures/manifest.json` 为登记入口。`docs/` 维护当前写作约定、研究讨论和文献核查记录，`scripts/` 提供编译与统计入口。学校模板与参考材料保留在本地 `材料/`，不提交到版本控制。文献检索的原始响应、逐条大表和过程预览可由脚本重新生成，只在本地保留；当前入库的是年度统计、纳入清单、核查记录及汇总清单。`latex/build/` 只将当前阅读版 `main.pdf` 纳入版本控制，其余编译中间文件由 `.gitignore` 排除。`output/` 保存正式发布版，`tmp/` 用于可清理的临时检查文件。
