# 开题报告插图说明

当前包含两幅概念插图和一幅总体研究框架图。图 1 由 Python / Matplotlib 绘制三个独立的 2D 子图，图 3 使用内置图像生成工具制作；概念图无图内文字、标题、编号或图例，不代表实验结果。总体框架图使用 LaTeX 原生矢量绘制，保留必要的目标、研究内容和科学问题文字。图注及配套解释在正文中维护，图号以主稿编译结果为准。

## 图1

绘图源：`figures/draw_occlusion.py`，三个子图统一由此脚本分别绘制。

| 子图 | 矢量文件 | 预览文件 | 含义 |
| --- | --- | --- | --- |
| (a) | `figures/occlusion_visible.pdf` | `figures/occlusion_visible.png` | 左侧可见，形成观测历史 |
| (b) | `figures/occlusion_hidden.pdf` | `figures/occlusion_hidden.png` | 进入墙后遮挡区，基于历史预测 |
| (c) | `figures/occlusion_corrected.pdf` | `figures/occlusion_corrected.png` | 预测尚未穿出遮挡区，真实目标加速提前出现并被校正 |

场景为纯 2D 俯视布局。相机位于下方中央、朝向上方；墙体位于相机前方，沿水平方向展开；圆形表示目标位置，沿墙体后方的同一条水平路线从左向右移动。三幅图共享场景参数、范围与比例，图内不增加立体物体或文字。坐标仅用于表达布局，不表示实测尺度。

遮挡范围由相机经墙体近侧两端的切线计算，浅灰色区域仅绘制在墙后。子图 (b) 的蓝色实线在遮挡入口处结束，橙色虚线从该入口开始并止于预测位置；朝向隐藏目标的视线在墙前停止，不穿墙。子图 (c) 表示重观测时刻：橙色虚线与虚线圆是按匀速或减速假设推演的先验，仍处于遮挡区内、尚未完全运动出来；绿色目标表示真实运动加速后提前穿出并被再次观测，绿色箭头表示新观测把状态校正到实际位置。橙色先验轨迹止于遮挡区，不进入右侧可见区。

在项目根目录重新绘图并编译：

```sh
conda run -n main python latex/figures/draw_occlusion.py
./scripts/build.sh
```

依赖 Matplotlib。修改脚本开头的相机、墙体、目标位置、颜色、尺寸或线型参数即可迭代；脚本会检查三个阶段的可见性次序，并从自身位置定位输出目录，因此也可从其他工作目录通过绝对路径运行。

正文使用三个 PDF 进行矢量排版，PNG 用于预览。`chapters/01-basis.tex` 中的 `subfigure` 环境自动生成 (a)、(b)、(c) 及子标题，正文通过 `\subref` 引用对应子图，整个图仍使用 `fig:occlusion`。已经生成的 PDF 与 PNG 保留在工程中，日常编译无需 Matplotlib 或 conda。

## 图2

项目内路径：`figures/research_framework.tex`

用途：在第二部分 2.1 中概括总体研究目标、四项研究内容及其对应的关键科学问题。

框架采用三层四列布局：上层为统一目标，中层为四项研究内容及方法重点，下层为对应科学问题。纵向箭头表示目标分解与问题对应；横向实线表示可靠状态表征、缺测预测与重观测校正的递进关系，虚线表示向动作条件交互的扩展。文字凝练自 2.2 和 2.3，后续调整研究内容时同步维护。

图形直接通过 `\input{figures/research_framework.tex}` 参与主稿编译，依赖 TikZ 与 `arrows.meta`，已在项目样式中加载。图形、文字和连线保持矢量形式，可按列修改名称与描述，无需重新生成位图。

## 图3

项目内路径：`figures/state_prediction_loop.png`

用途：在总体技术路线中说明历史观测、内部状态、未来预测和观测修正的功能关系。

生成提示词：

```text
Use case: scientific-educational.
Asset type: a text-free scientific illustration for the technical-route section of a Chinese doctoral thesis proposal.
Primary request: show historical observations forming an internal dynamic state, projecting it forward, and correcting that state with a new observation.
Style: match a restrained academic orthographic 3D illustration, white background, thin crisp grey linework, blue for observed geometry, amber for predicted geometry, green for correction. Wide horizontal composition about 2.7:1. Minimal shading. No decorative elements.
Composition: left group is a small line-art camera beside three slightly staggered image planes showing a blue cube at successive positions near a light-grey occluder. A thin grey arrow leads to the center: a compact blue 3D point cloud/cube wireframe on a light-grey local coordinate floor, with a few motion traces showing history, visually representing a structured internal state. A thin grey arrow leads to the right: two amber dashed ghost cube/point-cloud positions along a short curved trajectory, representing successive future predictions. Under the right and central groups, a single small new-observation image plane containing a solid blue cube feeds a curved green arrow back to the central state. The returned arrow should point into the central point-cloud state and have one obvious arrowhead; distinguish this correction path from the top forward path. All arrows connect content groups cleanly; no disconnected branches.
Constraints: absolutely no text, no titles, no subheadings, no letters, no numeric labels, no legends, no watermark, no equation, no infographic text boxes. No claim of a specific network architecture or measured result. Keep the observation-to-state-to-prediction path visually dominant and the new-observation correction loop simple and legible when scaled down.
```
