# 插图与素材

## 当前正文插图

[dynamic_world_motivation.tex](dynamic_world_motivation.tex)是当前唯一参与正文编译的插图，放在 1.1 第二段之后。图中采用 PhysTwin（ICCV 2025）同一布料提拉案例的真实历史观测、三维模型渲染及留出未来预测，真实执行参考另列。图题为“连续动态世界模型的状态构建与演化预测示意”，用于说明研究背景和基本范式。

- [原图位置及来源说明](materials/phystwin_cloth/README.md)、[逐文件校验及时间阶段](materials/phystwin_cloth/source-manifest.json)。
- [素材处理脚本](build_world_model_paradigm.py)：保留七张原始 JPEG，只为中央渲染制作背景透明的轮廓裁图。
- [独立图导出脚本](export_world_model_paradigm.py)：主报告本地编译后导出[矢量图](generated/world_model_paradigm/figure.pdf)和[预览](generated/world_model_paradigm/figure.png)。文字、箭头、透明度和布局均在 TikZ 中修改。

素材和生成图随源码保存，日常编译只需运行项目根目录的 `scripts/build.sh`，无需重新下载论文或提取图片。修改素材时按上述来源说明重现；编译完成后可运行独立图导出脚本更新 PDF 和 PNG。

## 未采用的素材及草稿

- [DyCheck apple 素材](materials/dycheck_apple/README.md)、[处理脚本](build_motivation_assets.py)及 `generated/motivation/` 保留为历史候选，不参与当前编译。旧版人工旋转表面是概念示意，不作为模型未来预测。
- [research_framework.tex](research_framework.tex)为已撤下的“总体研究框架”草稿，保留待重画；相关引导文字和交叉引用已从正文移除。

## 重写前的旧稿

2026-10-22 之前的全部旧稿插图及脚本封存在[归档 ZIP](../../archives/2026-10-22-before-rewrite.zip)中。需要查看时解压到项目外的临时目录，包内对应 `latex/figures/`；仓库不再保留展开副本。
