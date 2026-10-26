# 历史候选素材：DyCheck apple

2026-10-25 从 `gpu19` 上的 DyCheck iPhone 数据集中提取，曾用于 1.1 背景图草稿。当前正文已采用 PhysTwin 案例，本目录保留为历史候选，不参与当前主稿编译；其中 0、190、332 帧具有配对深度和关键点，其余原图为备选。

- 数据来源：[DyCheck 官方仓库](https://github.com/KAIR-BAIR/dycheck)，对应论文 *Monocular Dynamic View Synthesis: A Reality Check*（NeurIPS 2022）。
- 服务器目录：`/remote_databuffer/pomelo4d/datasets/DyCheck/iphone/apple/`。
- 图像来源：`rgb/1x/`，均来自训练序列的 `camera_id=0`；同一相机编号不表示相机位姿固定。
- 原图尺寸：720 × 960。六张 PNG 按原始字节复制，未裁剪、调色或合成。首批四张的来源及校验值见 [source-manifest.json](source-manifest.json) 和 [sha256.txt](sha256.txt)；补充的两张原图和三帧 RGB-D、关键点及相机信息见 [auxiliary-source-manifest.json](auxiliary-source-manifest.json)。`measurements/` 中的输入也保留原始字节。
- 时间根据服务器 `extra.json` 中的 30 fps 及 `splits/train.json` 的帧编号计算，以首帧为零点。这些图片是跨时刻抽样，不是相邻帧。

| 原图 | 帧编号 | 相对首帧时间 |
| --- | --- | --- |
| [0_00000.png](0_00000.png) | 0 | 0 s |
| [0_00120.png](0_00120.png) | 120 | 4 s |
| [0_00190.png](0_00190.png) | 190 | 约 6.33 s |
| [0_00210.png](0_00210.png) | 210 | 7 s |
| [0_00330.png](0_00330.png) | 330 | 11 s |
| [0_00332.png](0_00332.png) | 332 | 约 11.07 s |

## 候选素材及旧版示意

该序列可展示苹果转动、手部遮挡及不同表面的显露，并包含相机运动。旧版草图曾用 LaTeX 裁剪和组织画面，以 RGB 和对应点展示跨时刻联系、以配对深度展示局部几何。旋转后显露的是原有表面，不代表切割或撕裂产生的新生边界。

[绘图脚本](../../build_motivation_assets.py)可重现派生图像：深度采用固定的定性颜色范围，缺失值为灰色；点云由 332 帧的可见 RGB-D 和相机内参导出，在前景区域内筛除超出深度范围及局部不一致的点。点云不融合多个时刻，不补全不可见部分，也不作为表面真值。裁剪范围、深度筛选和视角均保留在脚本中。

中央的运动曲线、三维参照及关系线为 LaTeX 概念示意。右侧两幅形态由同一局部观测表面作不同旋转绘出，用于说明动作条件及可能后果，不运行预测模型，不作为预测结果或真值。该图用于引出研究问题，不报告实验性能。
