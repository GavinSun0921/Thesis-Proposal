# 开题报告插图说明

当前包含两幅概念插图和一幅总体研究框架图。两幅概念图采用内置图像生成工具制作，无图内文字、标题、编号或图例，不代表实验结果；总体框架图使用 LaTeX 原生矢量绘制，保留必要的目标、研究内容和科学问题文字。图注及配套解释在正文中维护，图号以主稿编译结果为准。

## 图1

项目内路径：`figures/occlusion_evolution.png`

用途：在背景与研究意义中说明短时遮挡、状态推演及重新观测后的校正。

生成提示词：

```text
Use case: scientific-educational.
Asset type: a text-free scientific illustration for a Chinese doctoral thesis proposal, to be embedded at approximately 15 cm width.
Primary request: explain a moving object becoming occluded and then being observed again, with a maintained prediction that is corrected by the new observation.
Style: restrained, crisp academic illustration, simple orthographic 3D linework, white background, very light grey ground plane and occluding wall; clean blue, amber, and green accents. Wide horizontal composition, aspect ratio about 2.7:1. Minimal shadows, no decorative scenery.
Composition: three clear moments arranged from left to right with narrow white gutters and a small thin grey forward arrow between moments. The SAME low rectangular grey occluder, ground plane, and camera viewpoint repeat in all moments. Left: a small solid blue cube is visible to the left of the occluder, and a short blue path shows its past movement toward the wall. Middle: the cube has moved behind the opaque wall; show ONLY an amber dashed outline/ghost and an amber projected path as a conceptual estimate of its hidden position, clearly distinct from a directly seen solid object. Right: a solid green cube is visible beyond the right edge of the occluder; a faint amber dashed predicted cube sits slightly offset, with a tiny correction arrow toward the green cube. A small line-art camera icon and subtle line-of-sight cue in each moment reinforce observation versus occlusion.
Constraints: no words, no letters, no numbers, no symbols resembling labels, no panel titles, no subheadings, no legends, no captions, no watermark, no boxes around scenes. This is a conceptual schematic, not a data plot or claimed experiment. Keep all objects small enough to breathe, same object identity, same scale and stationary occluder across moments. Make dashed hidden prediction unmistakable while keeping the wall opaque.
```

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
