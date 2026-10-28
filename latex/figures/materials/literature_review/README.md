# 1.2 研究现状插图素材

采集及核对日期：2026-10-26。三张图按“四维重建—交互预测—动作学习”组织。真实图片来自作者公开项目及论文，框线、文字和输入输出关系在 TikZ 中绘制。正文在引出每张图的段落中引用对应文献，图题保持简短。

## 文件及来源

| 本地原始素材 | 原始位置和角色 | 当前用法 |
| --- | --- | --- |
| `som_observation.png`、`som_tracks.png` | [Shape of Motion 项目](https://shape-of-motion.github.io/)的 `bear_input.mp4`、`bear-tracks.mp4`，分别取从 0 开始编号的第 40 帧；原始视频约 15 fps | 同一熊场景的输入观测、作者三维轨迹可视化 |
| `som_novel_view.jpg` | 同项目 `static/images/bear.jpg`，作者提供的新视角重建展示图 | 同一案例的新视角结果；不要求三幅图的视角或时刻严格一致 |
| `retime_t0.png`、`retime_mid.png`、`retime_t1.png` | [RetimeGS 项目](https://william-wang2.github.io/RetimeGS/)的 `static/images/core_idea/ours/interp_0066.png`、`interp_0069.png`、`interp_0072.png` | 同一七帧演示区间的两端及中点，统一裁取上半身区域；端点仅标采样时刻，中间结果为区间内插值 |
| `point_observation_v1.jpg`、`point_observation_v2.jpg` | [PointWorld 作者 PDF](https://arxiv.org/pdf/2601.03782)，物理第 33 页 Figure 16 第一个 DROID 布料案例，内嵌 `Image10.jpg`、`Image11.jpg` | 同一初始时刻的两视角 RGB；模型输入还包含深度及给定机器人点流 |
| `point_prediction_1s.jpg`、`point_reference_1s.jpg` | 同页同一案例的 `Image8.jpg`、`Image9.jpg` | 同一视角、同一 1.0 s 预测时域的模型点流和作者参考标注；图中的时间文字重新排版，未改动三维结果 |
| `openvla_teaser.jpg` | [OpenVLA 项目](https://openvla.github.io/)的 `static/images/openvla_teaser.jpg` | 裁取右下角 Franka 操作场景，作为 VLA 场景缩略图 |
| `dreamzero_overview.png` | [DreamZero 项目](https://dreamzero0.github.io/)的 `images/project_overview.png` | 裁取双臂积木场景，作为 WAM 场景缩略图；不将其标为模型生成帧 |

来源完整 URL、原文件 SHA-256、视频帧号、PDF 内嵌对象和裁剪坐标见 [source-manifest.json](source-manifest.json)。原始视频和完整 PDF 只保存在忽略的临时目录，仓库保留上述可复核图片，不重复保存大型下载文件。

## 图中含义

- 图 2 上半部展示 Shape of Motion 同一案例的不同输出，下半部展示 RetimeGS 的帧间恢复。两行不是跨方法对照实验，RetimeGS 的中间时刻也不表示未来预测。
- 图 3 只使用 PointWorld 同一布料案例。机器人点流是给定动作条件；“模型预测”和“参考标注”分别列出，二者都位于初始时刻后 1.0 s。参考图中的绿色点为作者标示的遮挡相关标注，原论文说明此类标注可能受遮挡影响；本图保留原样，不据此比较数值精度，也不将参考标注称为真实执行画面。
- 图 4 各行照片分别来自 OpenVLA、PointWorld 和 DreamZero，仅作对应工作的场景示例。旁边的输入输出框为本报告对典型形式的概括；三行不存在替代顺序，也不构成相同环境下的实验比较。实际系统可以组合这些方式。

## 修改及重建

[处理及导出脚本](../../build_literature_figures.py)校验原图，只做记录在清单中的二维裁剪、白色补边及 JPEG 编码，不合成几何、轨迹或未来帧。处理后的图片及校验清单位于 [generated/literature_review](../../generated/literature_review/)。

正常修改版式只需编辑三个 `.tex` 图源，并运行报告的本地编译脚本。更新独立矢量 PDF、彩色预览及灰度预览时运行：

```sh
python3 latex/figures/build_literature_figures.py
```

该步骤需要 Pillow、本地 MacTeX/XeLaTeX 及 pdftoppm，不访问网络。只有从作者媒体重新提取原图时才使用 `--download`，并额外需要 pypdf 和 PyAV；本次视频解码使用 PyAV 16.0.1。原始下载文件的校验值变化时脚本会停止，需先核对版本。
