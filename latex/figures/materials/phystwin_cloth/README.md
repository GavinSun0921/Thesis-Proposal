# 图 1：PhysTwin 同一布料提拉案例

用于 1.1 的研究背景及基本范式示意。选材于 2026-10-25 核对。

- 正式论文：Hanxiao Jiang 等，*PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos*，ICCV 2025，7219–7230。
- [正式出版记录](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html)、[作者项目页](https://jianghanxiao.github.io/phystwin-web/)、[作者全文](https://arxiv.org/pdf/2503.17973)。正文引用键为 `phystwin2025`。
- 七张 JPEG 均从作者全文的 PDF 内嵌图像直接提取，保留原始编码字节；不截取基线方法，也不保留原图的箭头、标题和基线标签。
- [source-manifest.json](source-manifest.json)记录原 PDF 校验值、页码、图号、行列、XObject 路径、时间阶段、尺寸和逐文件 SHA-256。这里的页码指下载 PDF 的物理页码，列号从零计数。

## 同一场景的对应关系

只使用论文 Figure 3 和 Figure 9 **最上方红金色布料提拉案例**。Figure 3 前三列为 Reconstruction & Resimulation，后三列明确标为 Future Prediction；Figure 9 展示对应模型状态的多视角渲染。

| 插图角色 | 原图位置 | 使用边界 |
| --- | --- | --- |
| `observation_t1.jpg`、`observation_t2.jpg` | Figure 3，Observation 行，第 1、3 列 | 已观测的建模区间，图中标为 $t_1$ 和 $t_2=t$ |
| `state_t1_view2.jpg`、`state_t2_view2.jpg` | Figure 9，Viewpoint 2 行，第 1、3 列 | 同一模型在前述时刻的另一视角渲染，表示历史和当前三维状态 |
| `state_t2_view3.jpg` | Figure 9，Viewpoint 3 行，第 3 列 | 当前状态的又一视角，不是更晚时刻；本次图 1 版面未采用，保留备用 |
| `prediction_future.jpg` | Figure 3，PhysTwin (Ours) 行，第 4 列 | 论文明确标注的未观测未来预测 |
| `execution_future.jpg` | Figure 3，Observation 行，第 4 列 | 与预测同列、同一未来时刻的真实执行参考，不作为历史输入 |

论文第 4.1 节说明 RGB-D 视频按 7:3 划分建模和测试区间，仅前段用于构建；交互由控制点位置给定。图中两张 RGB 是历史视觉证据的代表帧，**不表示 PhysTwin 仅以两帧单目 RGB 为输入**。$t_1,t_2$ 及 $t+\Delta t$ 只表达顺序和预测边界，不赋予原论文未提供的秒数。给定动作采用符号 $\mathbf a$ 表示，未伪造动作测量或控制轨迹。

中央使用真实三维模型的多视角渲染，并非本仓库另行恢复的点云或网格。[素材脚本](../../build_world_model_paradigm.py)仅按图像轮廓和颜色掩膜裁去背景，保留原 JPEG，不改写前景 RGB 像素；不改变物体姿态、合成中间帧、补全不可见表面或生成未来。两块状态裁图按同一像素比例放置，相对位置取自 477×320 原帧，避免同一视角下的尺寸被排版放大或缩小。两行三列的排布、时间轴、查询时刻、动作箭头及对照箭头在 [TikZ 图源](../../dynamic_world_motivation.tex)中绘制，用于说明基本范式，不是标定几何、实测轨迹或该文已完成连续观测更新的证据。

## 选材理由

比较过 [Ditto](https://ut-austin-rpl.github.io/Ditto/)、[GWM](https://gaussian-world-model.github.io/) 和 [PointWorld](https://point-world.github.io/) 的官方展示。Ditto 的关节对象重建适合说明数字孪生，但关节动画不直接等于动作条件未来预测；PointWorld 项目中的抽屉视频是机器人执行，不能直接标作预测。PhysTwin 同一案例同时提供历史观测、三维多视角状态和明确标注的留出未来预测，因而适合本图。布料提拉属于用户允许的“其他存在明显动态变化的场景”。

图用于解释本课题希望联系的观测、状态和动作后果，不将 PhysTwin 等同于本课题拟研究的全部能力，不展示其内部物理或网络架构，也不对应四项研究内容。

## 修改及复现

普通修改只需编辑 `dynamic_world_motivation.tex` 中的图片位置、宽度、箭头和标签；源 JPEG 无需改写。

```sh
python3 latex/figures/build_world_model_paradigm.py
./scripts/build.sh
python3 latex/figures/export_world_model_paradigm.py
```

素材处理需要 Pillow；PDF 导出需要 pypdf 和 pdfplumber，预览优先用 pdftoppm，缺少时回退到 Ghostscript。从作者 PDF 重新提取七张原图时，另需 pypdf：

```sh
python3 latex/figures/build_world_model_paradigm.py --paper /path/to/phystwin-paper.pdf
```

该示例采用正式论文已公开的视觉材料，来源在正文和本记录注明。用于正式提交或再次公开发布时沿用来源署名。
