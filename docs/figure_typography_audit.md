# 图内文字与字体检查

检查对象：`latex/main.tex` 当前引用的 13 张图；以 2026-10-31 当前主工程编译的 `latex/build/main.pdf` 为版面基准。RC08 是较早预览，不用作当前版面依据。本轮只测量和记录，没有修改图中文字、字体、字号或布局。

## 规范证据

开题表在 [main.tex](../latex/main.tex) 的模板说明要求“图、文、参考文献格式参照《西北工业大学博士研究生学位论文编写规则》”，但该说明未直接给出图中文字字体或字号。

西北工业大学研究生院于 2025-11-05 发布了[《西北工业大学研究生学位论文写作指南》通知](https://gs.nwpu.edu.cn/info/2284/30487.htm)。通知原文称：“西北工业大学研究生学位论文写作指南（2025版）已上传，详见附件。”官网附件下载要求验证码；本次无法核对附件中的图表字体条款。因而**目前没有足够材料证明某种字体或最小字号是本开题报告的校方硬性要求，也不能据此宣称现有字体不符合校规**。以下字号是可读性筛查，不是合规阈值。

## 逐图结果

普通标签大小根据 SVG 源文字大小、PDF 自身画布和报告中图的实际放置宽度换算。数学上下标会按公式排版自然变小，不与普通中文标签混为一谈。PDF 页为物理页码，括号中为正文页码。

| 图 | 位置、源文件 | 普通标签估计印刷字号 | 结论 |
| --- | --- | ---: | --- |
| 1 | p.3（正文 1）；[闭环图](../latex/figures/chapters/ch01-basis/world-model-loop/diagram.svg) | 约 4.4–8.6 pt；常规中文约 4.4–5.1 pt | **高风险**。部分普通中文标签在 A4 实际打印尺寸下明显偏小；最高优先复核。SVG 声明 Noto Sans CJK/Nimbus Roman 并内嵌 WOFF，导出的 PDF 实际嵌入 Arial Unicode MS，存在导出字体映射差异。 |
| 2 | p.4（正文 2）；[在轨维护信息图](../latex/figures/chapters/ch01-basis/spacecraft-maintenance/figure.png) | 无法从位图审计原字号；插入约 295 ppi | **字体不可验证**。这是 PNG 位图，不含可检索字体信息；画面中的主要中文标题可读。 |
| 3 | p.5（正文 3）；[重建时间轴](../latex/figures/chapters/ch01-basis/reconstruction-timeline/diagram.svg) | 约 4.8–9.9 pt；论文名约 4.8–5.6 pt | **中风险**。类别说明和主标签可读，英文论文名、会议名是最小文字。 |
| 4 | p.7（正文 5）；[世界模型时间轴](../latex/figures/chapters/ch01-basis/world-model-evolution/diagram.svg) | 约 4.6–10.0 pt；论文名约 4.6–5.6 pt | **中风险**。图例已放大，密集工作卡片中的英文标题/会议名仍小。 |
| 5 | p.9（正文 7）；[动作学习时间轴](../latex/figures/chapters/ch01-basis/action-learning-timeline/diagram.svg) | 约 4.8–9.9 pt；论文名约 4.8–5.6 pt | **中风险**。与图 3 相似，英文标题与 venue 小于中文类别说明。 |
| 6 | p.11（正文 9）；[CoFuse4D 方法图](../latex/figures/chapters/ch01-basis/cofuse4d-method/diagram.tex) | 约 6.6–9.2 pt；最小普通中文 6.6 pt | **中高风险**。小标签密集；灰字置于浅色底纹时对比度弱。主阶段标题 9.2 pt 相对清晰。 |
| 7 | p.12（正文 10）；[PS-VLA 方法图](../latex/figures/chapters/ch01-basis/psvla-method/diagram.tex) | 约 6.9–9.4 pt；公式正文约 7.3 pt，变量下标更小 | **中风险**。底部持续状态区域信息密、注释小且带彩色文字；整体仍可辨。PDF 中 Fandol 中文字形缺少 ToUnicode 映射，影响文本提取/搜索，不等同于视觉缺字。 |
| 8 | p.13（正文 11）；[研究框架图](../latex/figures/chapters/ch02-content/research-framework/diagram.svg) | 约 7.9–11.3 pt | **低风险**。主要中文内容较清楚，灰色辅助说明相对小。 |
| 9 | p.19（正文 17）；[总体技术路线](../latex/figures/chapters/ch03-plan/overall-technical-route/diagram.svg) | 约 7.4–10.8 pt | **低风险**。普通中文标签总体可读。 |
| 10 | p.20（正文 18）；[连续时间路线](../latex/figures/chapters/ch03-plan/continuous-time-route/diagram.svg) | 约 8.1–9.7 pt | **低风险**。 |
| 11 | p.22（正文 20）；[对象一致性路线](../latex/figures/chapters/ch03-plan/object-consistency-route/diagram.svg) | 约 8.1–9.7 pt | **低风险**。 |
| 12 | p.25（正文 23）；[结构更新路线](../latex/figures/chapters/ch03-plan/topology-change-route/diagram.svg) | 约 8.1–9.7 pt | **低风险**。 |
| 13 | p.26（正文 24）；[动作响应路线](../latex/figures/chapters/ch03-plan/action-response-route/diagram.svg) | 约 8.1–9.7 pt | **低风险**。 |

估算以正文图宽 `\linewidth=156 mm=442.20 pt` 为基准；图 1、2 使用 `0.98\linewidth`。CoFuse4D 图以自然宽度直接排入，宽度 14.75 cm。PNG 位图不能从字体元数据反推绘制时的 pt 字号。

## 字体与修订优先级

正文模板 [npu-report-style.sty](../latex/npu-report-style.sty) 使用 Times New Roman 与 SimSun；图题由模板单独设置为 `small`。插图中的字体由源图自己控制：CoFuse4D 使用宋体/黑体和数学字体；PS-VLA 使用 Fandol 与 Latin Modern/Computer Modern；部分 SVG 导出的 PDF 使用 Arial Unicode MS、PingFang SC 或 Helvetica；图 2 是位图。**字体族不统一是工程现状，但本身不是违反校规的证据。** 同时，SVG 声明字体和其 PDF 实际嵌入字体有差异，建议后续将转换器、版本和实际嵌入字体写进 manifest，避免不同环境导出后版式漂移。

建议顺序：

1. 图 1：优先放大或简化 4.4–5.1 pt 的普通中文标签，或重排/分拆信息；这是当前最明显的阅读问题。
2. 图 3–5：缩短工作标题和 venue、减少同一时间段卡片数量或拆图，再检查约 4.6–5.6 pt 英文文字。
3. 图 6：放大 6.6 pt 小字，删减辅助词，并增强灰字与底色的对比。
4. 图 7：精简底部公式注释和小型彩色标签；如重新导出，再处理中文文字的 Unicode 映射。
5. 获得并核对校方指南附件后，再判断是否需要统一字体族或设定最低字号；本报告不把设计建议伪称为官方规定。
