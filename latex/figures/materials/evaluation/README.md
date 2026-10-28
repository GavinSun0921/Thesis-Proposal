# 3.3 数据与评价示例的来源

所有图片用于介绍候选数据的观测类型，不作为本课题的实验结果。正文图 15 的四类数据按当前研究范围选用，不承诺使用完整数据集或覆盖全部任务。

- **DyCheck iPhone**：复用 [apple 原始素材及来源](../dycheck_apple/README.md)中的第 0、332 帧，仅作矩形裁剪。两幅均为相机 0 的真实跨时刻观测，相机位姿可以变化；图中不叠加推断轨迹。
- **PointOdyssey**：`pointodyssey_pipeline.jpg` 从[作者项目](https://pointodyssey.com/)链接的[原始配图](https://pointodyssey.com/assets/pipeline.jpg)保存，原图 2338 × 968，保留原始字节。取右侧第一行和第三行的首幅合成 RGB 示例；两图属于不同场景。项目说明提供深度、实例、相机和二维／三维轨迹，图中展示的是 RGB，不能将实例标签当作部件级标注。
- **PhysTwin**：复用 [PhysTwin 素材](../phystwin_cloth/README.md)的 `observation_t1.jpg`、`observation_t2.jpg`。两幅均为论文 Figure 3 同一布料案例的真实观测，未使用模型渲染或未来预测图。
- **DROID / PointWorld**：复用[已有观测素材](../literature_review/README.md)中的 `point_observation_v1.jpg`、`point_observation_v2.jpg`，来自 PointWorld 作者全文 Figure 16 的同一 DROID 布料案例、同一时刻两视角 RGB。候选三维标注由 [PointWorld-DROID 官方发布](https://huggingface.co/datasets/nvidia/PointWorld-DROID)核查，包含自动估计的轨迹、可见性和有效深度标记；使用时须遵循其有效性及置信度规则。正式论文引用同时保留 PointWorld 和 [DROID](https://www.roboticsproceedings.org/rss20/p120.html)。

局部切割与撕裂的几何、材料连接及形成时间验证计划由可控序列补充。GauSTAR [官方实现](https://github.com/eth-ait/GauSTAR)说明论文演示序列受许可限制未发布，不能将演示图充作已经可用的公共切割数据。当前数据图不包含未采集的切割、撕裂画面。

图 16 为原创 TikZ 指标图解。PCK 按 [DyCheck 官方实现](https://github.com/KAIR-BAIR/dycheck/blob/main/dycheck/core/metrics/keypoint.py)使用误差严格小于 `ratio * max(image_width, image_height)` 的判定，默认比率为 0.05。图中的两个阈值内点和一个阈值外点给出 2/3 的示意分数，不是数据集得分。三维轨迹图以斜轴测坐标框、底面网格及投影辅助线表示空间关系，误差线连接相同单元、相同时刻的参考与估计位置；它不是二维 PCK 的直接三维推广，也不替代无对应表面距离。

[生成脚本](../../build_evaluation_figures.py)仅依赖本地原图、Pillow、MacTeX 和 Poppler；默认不下载媒体或数据集。逐图裁剪、源文件与导出文件哈希及语义范围见[清单](../../generated/evaluation/manifest.json)。两张图的文字和标注保持黑色，使用实心点、叉号、线型及公式保证灰度阅读。
