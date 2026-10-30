# 3.3 公开数据与评价示例来源

更新：2026-10-30。原候选数据拼图和后续航空维修试件图均已退出当前正文，现行 3.3 只保留原创指标图。历史素材仅作来源追溯，公开数据核查统一见[当前记录](../../../../docs/reference_audit.md)。

## 当前指标图

[运动指标图源](../../evaluation_motion_metrics.tex)解释 PCK 与三维位置误差。PCK 遵循 [DyCheck 官方实现](https://github.com/KAIR-BAIR/dycheck/blob/main/dycheck/core/metrics/keypoint.py)，误差严格小于 `ratio * max(image_width, image_height)`，默认比率为 0.05。图中的两个命中点和一个未命中点给出 2/3 的示例分数。

三维图以坐标框及误差段表示同一单元、同一时刻的估计与参考位置偏差。数值和图形用于解释定义，不是研究结果；三维位置误差需要相应参考与统一坐标尺度。

[导出脚本](../../build_evaluation_figures.py)仅导出指标图的独立矢量 PDF、彩色和灰度预览；不下载媒体，不生成应用场景图。校验及语义范围见[清单](../../generated/evaluation/manifest.json)。

## 保留的历史素材

- DyCheck apple 的真实观测来自[原素材](../dycheck_apple/README.md)。
- PointOdyssey 配图取自[作者项目](https://pointodyssey.com/)，保留本地原始字节。
- PhysTwin 观测素材见[原来源](../phystwin_cloth/README.md)。
- DROID／PointWorld 示例来源见[文献素材](../literature_review/README.md)。

这些素材不构成完整基准、物理连接真值或新增实验承诺。连接等参考不足时按其可评价部分限定结论，不追加采集或定制场景建设。
