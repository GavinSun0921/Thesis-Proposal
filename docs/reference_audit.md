# 参考文献发表状态核查

核查日期：2026-10-09。范围：当前正文实际引用的 45 条文献，其中中文 6 条、英文 39 条。优先核对会议论文集、出版社页面及其书目元数据；未找到正式出版记录时再核对作者项目页和 arXiv。以下链接仅供维护与复核，报告参考文献列表统一隐藏 URL、访问日期，保留 DOI。

8 条原先按预印本引用的论文已改为正式出版版本。LiveWorld 已确认被 ECCV 2026 录用，但本次未找到正式卷页及 DOI，单独注明录用状态。V-JEPA 2、3D-Belief 和 BridgeVLA++ 未查到正式出版记录，继续注明预印本身份。本记录只核查书目信息与发表状态，不能替代对实验协议和结论的深入阅读。

本轮新增 23 条文献：6 条中文正式期刊文章、17 条英文正式会议论文。新增引用分别落实到背景、状态基础、特征预测、动态三维表示、预测可靠性和机器人操作的论述中，未通过未引用条目扩充列表。代表工作比较表中，每个代表工作名称后均标注对应文献，并补充持续高斯/稀疏运动控制和三维操作两个比较条目。中文文献按原文语言著录；PerAct 与 OpenVLA 的年份采用 PMLR 正式论文集年份 2023、2025，与会议举行年份区分。

| 文献库键 | 工作 | 本次采用版本与处理 | 核查出处 |
| --- | --- | --- | --- |
| ref01 | PlaNet | ICML 2019，PMLR 97：2555–2565；保留正式会议版本 | [PMLR](https://proceedings.mlr.press/v97/hafner19a.html) |
| ref02 | DreamerV3 | Nature 640(8059)：647–653，2025；补充期号，保留 DOI | [出版社 DOI](https://doi.org/10.1038/s41586-025-08744-2) |
| ref03 | DINO-WM | 从 arXiv 2024 改为 ICML 2025；PMLR 267：79115–79135 | [PMLR](https://proceedings.mlr.press/v267/zhou25t.html) |
| ref04 | V-JEPA 2 | 暂保留 arXiv:2506.09985，2025；作者实验室仍将其列在预印本中 | [arXiv](https://arxiv.org/abs/2506.09985)、[作者实验室](https://chandar-lab.github.io/publications/preprints) |
| ref05 | MoSca | CVPR 2025：6165–6177；保留正式会议版本 | [CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_MoSca_Dynamic_Gaussian_Fusion_from_Casual_Videos_via_4D_Motion_CVPR_2025_paper.html) |
| ref06 | PointWorld | 改为 CVPR 2026：20765–20779 | [CVF 正式论文](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf)、[论文集](https://openaccess.thecvf.com/CVPR2026?day=2026-06-06) |
| ref07 | FR3D | 改为 ICML 2026，PMLR 306：90232–90250；按正式版本题名引用 | [PMLR](https://proceedings.mlr.press/v306/morbitzer26a.html) |
| ref08 | Flow Equivariant World Models | 改为 ICML 2026，PMLR 306：73968–74002；题名更新为 *Structured Memory for Dynamic Environments*，按正式版本修正作者姓名 | [PMLR](https://proceedings.mlr.press/v306/lillemark26a.html) |
| ref09 | LiveWorld | 按 ECCV 2026 会议条目列出，并注明 *Accepted at ECCV 2026*；未填未经核实的卷页或 DOI | [作者项目页](https://zichengduan.github.io/pages/LiveWorld/)、[作者录用公告](https://steve-zeyu-zhang.github.io/) |
| ref10 | PERSIST | 改为 ICML 2026，PMLR 306：34048–34070 | [PMLR](https://proceedings.mlr.press/v306/garcin26a.html) |
| ref11 | 3D-Belief | 暂保留 arXiv:2605.11367，2026；作者项目页未列出正式会议或期刊 | [arXiv](https://arxiv.org/abs/2605.11367)、[作者项目页](https://3d-belief.github.io/) |
| ref12 | BridgeVLA | 改为 NeurIPS 2025，卷 38：63635–63673；补充 DOI 10.52202/085713-2137 | [NeurIPS 正式论文集](https://papers.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html) |
| ref13 | BridgeVLA++ | 暂保留 arXiv:2608.05042，2026；与已发表的 BridgeVLA 区分 | [作者项目页](https://bridgevla-plus.github.io/)、[官方仓库](https://github.com/BridgeVLA/BridgeVLA) |
| pomdp1998 | 部分可观测规划基础 | Artificial Intelligence 101(1–2)：99–134，1998；保留正式期刊版本及 DOI | [出版社 DOI](https://doi.org/10.1016/S0004-3702(98)00023-X) |
| gpml2006 | Gaussian Processes for Machine Learning | MIT Press，2006；按作者提供的书目年份引用 | [作者书籍页](https://gaussianprocess.org/gpml/)、[出版社](https://mitpress.mit.edu/9780262182539/gaussian-processes-for-machine-learning/) |
| gs2023 | 3D Gaussian Splatting | ACM TOG 42(4)，2023；补充登记页码 1–14 与 DOI 10.1145/3592433 | [作者项目页](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)、[出版社 DOI](https://doi.org/10.1145/3592433) |
| gs4d2024 | 4D Gaussian Splatting | CVPR 2024：20310–20320；保留正式会议版本 | [CVF](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_4D_Gaussian_Splatting_for_Real-Time_Dynamic_Scene_Rendering_CVPR_2024_paper.html) |
| tapir2023 | TAPIR | ICCV 2023：10061–10072；保留正式会议版本 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Doersch_TAPIR_Tracking_Any_Point_with_Per-Frame_Initialization_and_Temporal_Refinement_ICCV_2023_paper.html) |
| cotracker3 | CoTracker3 | 从 arXiv 2024 改为 ICCV 2025：6013–6022；第二作者姓名按正式论文集更新为 Yuri Makarov | [CVF](https://openaccess.thecvf.com/content/ICCV2025/html/Karaev_CoTracker3_Simpler_and_Better_Point_Tracking_by_Pseudo-Labelling_Real_Videos_ICCV_2025_paper.html) |
| rlbench2020 | RLBench | IEEE RA-L 5(2)：3019–3026，2020；保留正式期刊版本及 DOI | [出版社 DOI](https://doi.org/10.1109/LRA.2020.2974707) |
| dycheck2022 | DyCheck | NeurIPS 2022，卷 35；补齐页码 33768–33780 和 DOI 10.52202/068431-2447 | [NeurIPS 正式论文集](https://papers.neurips.cc/paper_files/paper/2022/hash/dab5a29f6614ec47ea0ca85c140226fd-Abstract-Conference.html) |
| tapvid2022 | TAP-Vid | 改为 NeurIPS 2022 数据集与基准赛道，卷 35：13610–13626；补充 DOI 10.52202/068431-0989 | [NeurIPS 正式论文集](https://proceedings.neurips.cc/paper_files/paper/2022/hash/58168e8a92994655d6da3939e7cc0918-Abstract-Datasets_and_Benchmarks.html) |
| worldmodels2018 | World Models | NeurIPS 2018，卷 31；使用正式题名 *Recurrent World Models Facilitate Policy Evolution*，不引用同名早期预印本 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html) |
| psr2001 | 预测状态表示基础 | NIPS 2001，卷 14，MIT Press；年份沿用正式会议页面。网页导出遗漏 Satinder Singh，依据正式 PDF 首页补齐三位作者；未填网页没有提供的页码 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html)、[正式 PDF](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf) |
| dreamer2020 | Dreamer | ICLR 2020；作者项目页确认正式会议及作者，著录为会议论文 | [作者项目页](https://danijar.com/project/dreamer/)、[OpenReview](https://openreview.net/forum?id=S1lOTC4tDS) |
| pets2018 | PETS | NeurIPS 2018，卷 31；按正式 BibTeX 记录作者、题名及出版信息 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) |
| ensembles2017 | 深度集成不确定性 | NIPS 2017，卷 30；按正式 BibTeX 记录作者、题名及出版信息 | [NeurIPS](https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html) |
| ijepa2023 | I-JEPA | CVPR 2023：15619–15629；明确原始任务是图像空间区域的特征预测 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Assran_Self-Supervised_Learning_From_Images_With_a_Joint-Embedding_Predictive_Architecture_CVPR_2023_paper.html) |
| nerf2020 | NeRF | ECCV 2020，LNCS 12346：405–421，Springer；保留 DOI 10.1007/978-3-030-58452-8_24 | [Springer](https://link.springer.com/chapter/10.1007/978-3-030-58452-8_24) |
| dnerf2021 | D-NeRF | CVPR 2021：10318–10327 | [CVF](https://openaccess.thecvf.com/content/CVPR2021/html/Pumarola_D-NeRF_Neural_Radiance_Fields_for_Dynamic_Scenes_CVPR_2021_paper.html) |
| nerfies2021 | Nerfies | ICCV 2021：5865–5874 | [CVF](https://openaccess.thecvf.com/content/ICCV2021/html/Park_Nerfies_Deformable_Neural_Radiance_Fields_ICCV_2021_paper.html) |
| dynamicgs2024 | Dynamic 3D Gaussians | 3DV 2024：800–809；会议与年份由作者正式书目确认，页码与 DOI 由出版社登记元数据核对；DOI 10.1109/3DV62453.2024.00044 | [作者项目页](https://dynamic3dgaussians.github.io/)、[出版社 DOI](https://doi.org/10.1109/3DV62453.2024.00044) |
| deformablegs2024 | Deformable 3D Gaussians | CVPR 2024：20331–20341 | [CVF](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Deformable_3D_Gaussians_for_High-Fidelity_Monocular_Dynamic_Scene_Reconstruction_CVPR_2024_paper.html) |
| scgs2024 | SC-GS | CVPR 2024：4220–4230 | [CVF](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_SC-GS_Sparse-Controlled_Gaussian_Splatting_for_Editable_Dynamic_Scenes_CVPR_2024_paper.html) |
| gaussianflow2024 | Gaussian-Flow | CVPR 2024：21136–21145；使用正式题名及其时域/频域变形方法定位 | [CVF](https://openaccess.thecvf.com/content/CVPR2024/html/Lin_Gaussian-Flow_4D_Reconstruction_with_Dynamic_3D_Gaussian_Particle_CVPR_2024_paper.html) |
| rt22023 | RT-2 | 第 7 届 CoRL，PMLR 229：2165–2183，2023；作者姓名按正式论文集更新后的记录著录 | [PMLR](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| openvla2025 | OpenVLA | 第 8 届 CoRL，PMLR 270：2679–2713，2025；采用正式论文集年份 | [PMLR](https://proceedings.mlr.press/v270/kim25c.html) |
| peract2023 | PerAct | 第 6 届 CoRL，PMLR 205：785–799，2023；采用正式论文集年份 | [PMLR](https://proceedings.mlr.press/v205/shridhar23a.html) |
| rvt22024 | RVT-2 | RSS 2024，Delft；保留 DOI 10.15607/RSS.2024.XX.055 | [RSS 正式论文集](https://www.roboticsproceedings.org/rss20/p055.html) |
| cnworld2026 | 世界模型中文论述 | 王利民、朱光辉、吴涛，《大模型技术演进：世界模型让人工智能从感知走向决策(特邀)》，计算机工程 52(2)：1–6，2026；DOI 10.19678/j.issn.1000-3428.0253281 | [期刊官网](https://www.ecice06.com/CN/10.19678/j.issn.1000-3428.0253281) |
| cnvisualrl2026 | 视觉强化学习中文综述 | 王荣荣、程玉虎、王雪松，《视觉强化学习方法研究综述》，自动化学报 52(3)：381–410，2026；DOI 10.16383/j.aas.c250422 | [期刊官网](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250422) |
| cnnerf2025 | 神经辐射场中文综述 | 陈涛、杨启亮、陈寅，《神经辐射场技术及应用综述》，计算机辅助设计与图形学学报 37(1)：51–74，2025；DOI 10.3724/SP.J.1089.2023-00759 | [期刊官网](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2023-00759) |
| cndynamic2024 | 动态重建中文综述 | 孙水发等，《动态场景的三维重建研究综述》，计算机科学与探索 18(4)：831–860，2024；题名、作者及卷页由期刊目录核对，DOI 10.3778/j.issn.1673-9418.2305016 另由国家科技期刊平台元数据核对 | [期刊目录](https://kxts.chinajournal.net.cn/WKI/WebPublication/wkTextContent.aspx?colType=4&st=04&yt=2024)、[国家科技期刊平台](https://opaj.napstic.cn/periodicalArticle/0120240401922522) |
| cndynamicgs2026 | 动态高斯中文综述 | 连振晗、王章野、牛炯、程乐超，《基于三维高斯泼溅的动态场景重建研究综述》，计算机辅助设计与图形学学报 38(1)：61–77，2026；DOI 10.3724/SP.J.1089.2025-00251 | [期刊官网](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2025-00251) |
| cnvla2026 | 具身操作 VLA 中文综述 | 李浩然等，《面向具身操作的视觉−语言−动作模型综述》，自动化学报 52(1)：18–51，2026；DOI 10.16383/j.aas.c250394 | [期刊官网](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250394) |

新增或修订条目时，先查询正式出版记录，再核对作者、题名、会议或期刊、年份、卷页及 DOI。保持原有文献键稳定，由 BibTeX 自动维护引用编号。原始 URL 可继续存入文献库；工程内的 `npu-gbt7714-numerical.bst` 控制输出，避免新增条目重新带出 URL。

输出复核：45 条文献均在正文或表格中实际引用，无缺失引用或未使用条目；代表工作比较表中的 18 个代表工作逐项标注来源。参考文献不输出 URL 和访问日期，PDF 中保留的 16 个外部链接均为 DOI。第二部分重组为四项研究内容后，文献数量及上述输出规则保持一致。
