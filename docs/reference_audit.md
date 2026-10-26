# 参考文献发表状态核查

## 2026-10-26 当前新稿引文

第一、第二部分当前实际引用 **39 条文献**：37 条正式会议或期刊论文、1 条基金委公开通告、1 条 2026 年近期预印本；其中中文 3 条、英文 36 条。文献表独立置于报告末尾第四部分，按全文首次引用顺序生成。保留旧库未使用条目，未通过未引用条目增加列表。以下新稿记录与后文旧稿 87 条记录分别维护。

2026-10-26 按用户要求将文献表从第一部分末尾移至第三部分之后，恢复独立的第四部分。实际引用仍为 39 条，文献条目及全文首次引用顺序保持不变。

2026-10-26 配合 1.1 六段结构重写 1.2。实际引用仍为 39 条，未增删书目；因图 1 和学习式三维感知的引入前移，首次引用编号重新生成。1.2 增加已有 PhysTwin 的 RGB-D 输入、质点弹簧模型及给定控制点运动下的预测说明，区分其物理重建路线和本文连续状态的整体目标。再次核对基金委通告、MonST3R、CUT3R、PhysTwin、GWM、PointWorld、PERSIST 及 DreamZero 的一手资料；RetimeGS 的低采样率及大位移限制依据作者论文及补充材料，不作为所有连续时间方法的共同局限。未将预印本改记为正式发表。

本轮方法事实复核来源：[基金委通告](https://www.nsfc.gov.cn/p1/3381/2824/142425.html)、[MonST3R 作者项目](https://monst3r-project.github.io/)、[CUT3R 作者项目](https://cut3r.github.io/)、[PhysTwin 作者项目](https://jianghanxiao.github.io/phystwin-web/)、[GWM 作者全文](https://arxiv.org/html/2508.17600)、[PointWorld 作者全文附录 A.1](https://arxiv.org/html/2601.03782)、[PERSIST 正式摘要](https://proceedings.mlr.press/v306/garcin26a.html)、[RetimeGS 补充材料](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Wang_RetimeGS_Continuous-Time_Reconstruction_CVPR_2026_supplemental.pdf)、[DreamZero 作者预印本](https://arxiv.org/abs/2602.15922)。

2026-10-25 重新设计 1.1 背景图，新增 PhysTwin 的 ICCV 2025 正式论文作为图源。作者、题名、年份和 7219–7230 页由 CVF 正式出版记录核对；图中原始图像从作者公开 PDF 内嵌对象提取，来源映射和校验记录见[素材说明](../latex/figures/materials/phystwin_cloth/README.md)。Figure 3、Figure 9 的同一布料案例分别提供建模区间观测、多视角模型渲染及留出未来预测，真实未来参考单独标识。动态图的概念曲线及观测更新箭头不作为该论文已经实现连续状态更新的证据。实际引用增加为 39 条，未新增预印本。

2026-10-25 暂定题目调整为“连续动态世界模型的构建方法研究”，同步修改总体定位、研究内容及图示。沿用当前 38 条引用和既有方法事实，本轮不新增书目，也不将文献的连续时间表达、持续观测更新和动作条件预测混为同一能力；发表状态沿用下述既有核查记录。

2026-10-25 按总分总重写 1.1，保留基金委通告作为背景依据，并复用 DreamerV3 说明环境预测参与行为学习。全部实际引用仍为 38 条；因 DreamerV3 首次引用前移，同步调整 1.2 的一处组内引文顺序。书目及发表状态沿用既有核查，不新增文献。

2026-10-24 将 1.2 重组为“四维动态场景重建—面向交互的世界模型—具身操作中的动作学习”，调整代表工作的组织、比较和首次引用顺序，保留全部 38 条实际引用。本轮未新增文献，书目信息及发表状态沿用 2026-10-23 的核查。世界模型一节分别说明 TesserAct 的图像及任务指令条件、GWM 的历史状态及动作条件；动作学习一节讨论预测的使用及 DreamZero 的联合生成，不将几类建模目标混同。

2026-10-22 初稿引用 29 条正式论文，其中新增 10 条。2026-10-23 按四维重建及具身智能的领域脉络重组 1.1、1.2，保留原 29 条引用，重新启用已有库中的基金委通告、VLA 中文综述、RT-2 及 OpenVLA，新增 MonST3R、CUT3R、$\pi_0$、TesserAct 和 DreamZero 五条。优先核对 CVF、ICLR、PMLR、RSS 正式论文集。方法及能力边界由论文正文或作者全文复核，不能将正文中的本课题研究判断当作被引论文已经证明的共同局限。

基金委通告发布于 2026-09-18，公开页只说明专项名称及申请指南在科学基金网络信息系统发布；正文据此说明研究背景，不引用未获得的登录后指南细则。DreamZero 于 2026-02-17 提交 arXiv，本次未核定正式出版记录，保持 `@online` 及预印本编号，用于直接说明 WAM 联合建模未来视频与动作的形式。它属于近期代表性进展，不作为正式论文统计，也不据其特定实验推断 WAM 普遍优于 VLA。未启用旧库中的 WorldVLA 或 WAM 综述预印本来扩充引用数量。

| 文献库键 | 正式版本及用途 | 核查来源 |
| --- | --- | --- |
| phystwin2025 | ICCV 2025：7219–7230；用于图 1 同一布料案例的历史观测、三维渲染、留出未来预测和真实执行参考；不将其内部方法或更新能力等同于本课题范式 | [CVF 正式记录](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html)、[作者全文](https://arxiv.org/pdf/2503.17973)、[项目页](https://jianghanxiao.github.io/phystwin-web/) |
| nsfcworldmodel2026 | 2026-09-18 基金委信息科学部公开通告；仅用于研究背景 | [官方通告](https://www.nsfc.gov.cn/p1/3381/2824/142425.html) |
| cnvla2026 | 自动化学报 52(1)：18–51，2026；具身操作及 VLA 发展背景 | [期刊记录](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250394) |
| rt22023 | CoRL，PMLR 229：2165–2183，2023；预训练视觉语言知识进入动作模型 | [正式版本](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| openvla2025 | CoRL，PMLR 270：2679–2713，2025；开放 VLA 及任务微调；年份采用正式论文集年份 | [正式版本](https://proceedings.mlr.press/v270/kim25c.html) |
| monst3r2025 | ICLR 2025；动态逐时刻点图及几何恢复，区分预测和后续对齐 | [正式版本](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ce1710ff5b66f89b0d707bf1ec2850bf-Abstract-Conference.html)、[作者项目](https://monst3r-project.github.io/) |
| cut3r2025 | CVPR 2025：10510–10522；持续循环状态及三维点图读取，支持静态和动态内容；不据“continuous updating”推断显式连续时间运动 | [正式记录](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Continuous_3D_Perception_Model_with_Persistent_State_CVPR_2025_paper.html)、[作者全文](https://arxiv.org/abs/2501.12387) |
| pi02025 | RSS 2025，DOI 10.15607/RSS.2025.XXI.010；视觉语言模型基础上的连续动作流匹配 | [正式版本](https://roboticsproceedings.org/rss21/p010.html) |
| tesseract2025 | ICCV 2025：5337–5347；RGB、深度、法向联合生成、四维场景恢复及逆动力学 | [正式记录](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html)、[正式全文](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.pdf) |
| dreamzero2026 | arXiv:2602.15922，2026 预印本；未来视频和机器人动作的联合建模，明确保留版本身份 | [作者预印本](https://arxiv.org/abs/2602.15922)、[项目页](https://dreamzero0.github.io/) |
| retimegs2026 | CVPR 2026：7340–7350；连续时间重建、时间插值及样条设计 | [正式论文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RetimeGS_Continuous-Time_Reconstruction_of_4D_Gaussian_Splatting_CVPR_2026_paper.pdf)、[补充材料](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Wang_RetimeGS_Continuous-Time_Reconstruction_CVPR_2026_supplemental.pdf) |
| shapeofmotion2025 | ICCV 2025：9660–9672；持久轨迹、共享刚体运动基及软分组，区分运动分组与对象身份 | [正式版本](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Shape_of_Motion_4D_Reconstruction_from_a_Single_Video_ICCV_2025_paper.html)、[作者全文](https://arxiv.org/html/2407.13764) |
| movingparts2024 | ICLR 2024；基于粒子轨迹及部件运动发现空间组织 | [正式版本](https://proceedings.iclr.cc/paper_files/paper/2024/hash/c34ddd05eb089991f06f3c5dc36836e0-Abstract-Conference.html) |
| consistentinstance2026 | CVPR 2026：3783–3793；持续身份与可见性的区别，伪标签条件 | [正式版本](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Consistent_Instance_Field_for_Dynamic_Scene_Understanding_CVPR_2026_paper.html)、[作者全文附录 C.1](https://arxiv.org/html/2512.14126) |
| gaustar2025 | CVPR 2025：16543–16553；稳定区绑定、变化区解绑及表面更新；采用正式题名 GauSTAR，早期预印本曾用 GSTAR | [正式版本](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_GauSTAR_Gaussian_Surface_Tracking_and_Reconstruction_CVPR_2025_paper.html)、[作者全文](https://arxiv.org/html/2501.10283) |
| atgs2025 | WACV 2025：742–752；逐帧面元重建及曲率一致性，存储开销按作者讨论说明 | [正式版本](https://openaccess.thecvf.com/content/WACV2025/html/Chen_Adaptive_and_Temporally_Consistent_Gaussian_Surfels_for_Multi-View_Dynamic_Reconstruction_WACV_2025_paper.html)、[作者全文](https://arxiv.org/html/2411.06602) |
| surf4d2026 | CVPR 2026：22539–22549；大形变表面一致性，不据此推断真实断裂能力 | [正式版本](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_4DSurf_High-Fidelity_Dynamic_Scene_Surface_Reconstruction_CVPR_2026_paper.html) |
| gwm2025 | ICCV 2025：9263–9274；动作条件高斯场景生成；第 3.2 节已使用历史状态和动作 | [正式版本](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html)、[作者全文](https://arxiv.org/html/2508.17600) |
| particlegs2026 | CVPR 2026：8331–8341；连续动力学外推，区分于观测区间内插值和动作条件预测 | [正式版本](https://openaccess.thecvf.com/content/CVPR2026/html/Quan_ParticleGS_Learning_Neural_Gaussian_Particle_Dynamics_from_Videos_for_Prior-free_CVPR_2026_paper.html) |
| sobolevfusion2018 | CVPR 2018：2646–2655；说明拓扑变化重建已有基础，保留较早正式研究的历史作用 | [正式版本](https://openaccess.thecvf.com/content_cvpr_2018/html/Slavcheva_SobolevFusion_3D_Reconstruction_CVPR_2018_paper.html) |

复用条目包括 PlaNet、DreamerV3、动态高斯综述、MoSca、PointWorld、DyCheck、TAPVid-3D、NeRF、3DGS、D-NeRF、Nerfies、Dynamic 3D Gaussians、4D-GS、SC-GS、HyperNeRF、DINO-WM、PERSIST、图网络模拟器和 BridgeVLA。其中 [PlaNet](https://proceedings.mlr.press/v97/hafner19a.html)、[DINO-WM](https://proceedings.mlr.press/v267/zhou25t.html)、[PERSIST](https://proceedings.mlr.press/v306/garcin26a.html)、[图网络模拟器](https://proceedings.mlr.press/v119/sanchez-gonzalez20a.html)、[BridgeVLA](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html)等正式记录本轮再次核对；其他条目沿用既有正式版本，并按本轮实际使用的机制说明复核。

PointWorld 的静态初始状态限制以[作者全文附录 A.1](https://arxiv.org/html/2601.03782)为依据，不泛化为其他模型的限制；该方法已有部分观测及物体性研究。GauSTAR 和 AT-GS 作为已有局部表面更新参考，不将其文献中的所有拓扑变化自动解释为真实切割、撕裂。前期 CoFuse4D、PS-VLA 的说明沿用归档及工作文档，仅描述探索基础，不新增发表状态和实验成绩。

## 归档旧稿的历史核查记录

以下记录适用于[归档旧稿 ZIP](../archives/2026-10-22-before-rewrite.zip)，保留供文献库维护和复核。下述 87 条数量及引用分布均指旧稿。

核查日期：2026-10-09，增补日期：2026-10-12、2026-10-13、2026-10-15、2026-10-18、2026-10-20。范围：归档旧稿实际引用的 87 条文献，其中中文 7 条、英文 80 条。优先核对会议论文集、出版社页面及其书目元数据；未找到正式出版记录时再核对作者项目页和 arXiv。以下链接仅供维护与复核，报告参考文献列表统一隐藏 URL、访问日期，保留 DOI。

8 条原先按预印本引用的论文已改为正式出版版本。LiveWorld 已确认被 ECCV 2026 录用，但本次未找到正式卷页及 DOI，单独注明录用状态。V-JEPA 2、3D-Belief 和 BridgeVLA++ 未查到正式出版记录，继续注明预印本身份。本记录只核查书目信息与发表状态，不能替代对实验协议和结论的深入阅读。

此前综述扩充新增 23 条文献：6 条中文正式期刊文章、17 条英文正式会议论文。2026-10-12 另增补 2 条英文研究文献与 1 条中文政策公告。新增引用分别落实到背景、状态基础、特征预测、动态三维表示、预测可靠性和机器人操作的论述中，未通过未引用条目扩充列表。代表工作比较表中，每个代表工作名称后均标注对应文献，并补充持续高斯/稀疏运动控制和三维操作两个比较条目。中文文献按原文语言著录；PerAct 与 OpenVLA 的年份采用 PMLR 正式论文集年份 2023、2025，与会议举行年份区分。

2026-10-13 扩充 1.1 与 1.2：在现稿 53 条基础上新增 22 条正式论文或学术专著，补充状态估计、观测融合、遮挡对象持续性、身份关联、三维对象跟踪、对象动力学、预测校准和交互学习。1.1 实际引用由 2 条增至 10 条，1.2 由 49 条增至 73 条，两节合并去重为 75 条。另补记现稿此前已增加的 MuZero、TD-MPC2、Genie、HyperNeRF 和 OmniMotion 五条。新增条目核对正式论文集、作者项目或出版社登记元数据；对 PermaTrack、OC-SORT 和 BundleSDF 进一步检查论文正文，区分隐藏标注来源、重观测后的回溯更新、刚体与输入掩码等条件。

2026-10-15 随 1.2 四个综述主题的重组新增 WAM 综述与 WorldVLA 两条英文文献，保留原有 73 条 1.2 引用。WAM 综述核对 arXiv 的作者、题名、日期与摘要，用于界定未来世界预测与可执行动作生成之间的联系；WorldVLA 核对 arXiv 及作者发布页，用于说明图像到动作、图像与动作到未来图像的联合建模。两条均未在本次检索中确认正式会议或期刊版本，采用可核实的预印本，不补填卷页或 DOI，不据摘要声称具体实验优势。

2026-10-18 补齐 3.2.3、3.2.4 时复用 Deep SORT、Probabilistic Robotics、RKN、BridgeVLA 与 DINO-WM，不新增文献条目。再次核对 Deep SORT 作者论文、RKN 与 DINO-WM 正式论文集、BridgeVLA 正式论文集的机制说明；这些文献仅作为关联、状态更新、操作框架与特征预测的参考，具体网络和训练安排为本课题拟采用方案，不归属于被引工作的原始配置。

2026-10-20 扩充 3.4 的数据规划，新增 TAPVid-3D、PointOdyssey、BridgeData V2 与 DROID 四条正式论文。分别核对 NeurIPS、CVF、PMLR 与 RSS 正式论文集；TAPVid-3D 页码由论文集 BibTeX 确认，PointOdyssey 的二维和三维轨迹、深度等内容由作者项目页确认。D-NeRF、HyperNeRF、DyCheck 与 TAP-Vid 沿用已有条目。公开数据以连续段落列举并说明用途，按研究需要选用。

同日按用户意见扩展交互实验资源，新增 LIBERO、CALVIN、SimplerEnv、RoboCasa 与 RoboTwin 五条基准文献。LIBERO 卷页由 NeurIPS 正式 BibTeX 确认；CALVIN 采用 IEEE RA-L 期刊版本；SimplerEnv 采用 PMLR 270 的正式出版版本，年份按 2025 著录；RoboCasa 题名按 RSS 正式记录中的 Household Tasks 著录，与作者项目及 PDF 中的 Everyday Tasks 为同一工作；RoboTwin 采用 CVPR 2025 正式版本。正文仅概述这些资源可支持的实验范围，具体选用随研究进展调整。

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
| gns2020 | 图网络动力学 | 2026-10-18 新增。ICML 2020，PMLR 119：8459–8468；正式论文集确认六位作者、题名、年份与卷页，用于 3.2.2 节点消息传递的组织依据，不将其完整物理模拟设定直接等同于本课题的缺测预测任务。 | [PMLR](https://proceedings.mlr.press/v119/sanchez-gonzalez20a.html) |
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
| vsiwild2026 | VSI-Super-Wild | 2026-10-12 新增。按 ECCV 2026 会议条目列出，并注明 *Accepted at ECCV 2026*；作者截取前三人加 others；未填未经核实的卷页或 DOI。arXiv 页面确认题名、作者、录用状态及失效模式表述 | [arXiv](https://arxiv.org/abs/2607.13681) |
| ovggt2026 | OVGGT | 2026-10-12 新增。暂保留 arXiv:2603.05959，2026（v3）；作者实验室页面未列出正式会议或期刊。arXiv 页面确认题名、作者及固定资源预算、锚点保护方法定位 | [arXiv](https://arxiv.org/abs/2603.05959) |
| nsfcworldmodel2026 | “空间智能与世界模型”专项申请指南发布通告 | 2026-10-12 新增。国家自然科学基金委员会信息科学部发布，日期为 2026-09-18；按在线公告著录，用于 1.1 研究态势论述。2026-10-14 再核官网，确认发布机构、题名与日期；公开通告未展示指南正文，1.1 仅保留指南发布事实，不据此解读具体技术要求 | [基金委官方通告](https://www.nsfc.gov.cn/p1/3381/2824/142425.html) |
| muzero2020 | MuZero | Nature 588(7839)：604–609，2020；作者、卷页与 DOI 由出版社登记元数据核对。 | [出版社 DOI](https://doi.org/10.1038/s41586-020-03051-4) |
| tdmpc2_2024 | TD-MPC2 | ICLR 2024；作者项目书目确认会议、年份及三位作者。 | [作者项目页](https://www.tdmpc2.com/) |
| genie2024 | Genie | ICML 2024，PMLR 235：4603–4623；按正式论文集著录。 | [PMLR](https://proceedings.mlr.press/v235/bruce24a.html) |
| hypernerf2021 | HyperNeRF | ACM TOG 40(6)，2021，文章 238：1–12；DOI 及作者由登记元数据核对，完整题名见作者项目页。 | [出版社 DOI](https://doi.org/10.1145/3478513.3480487)、[作者项目页](https://hypernerf.github.io/) |
| omnimotion2023 | OmniMotion | ICCV 2023：19795–19806；按正式论文集核对题名、作者及页码，保留现有 DOI。 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_Tracking_Everything_Everywhere_All_at_Once_ICCV_2023_paper.html) |
| kalman1960 | Kalman 滤波 | Journal of Basic Engineering 82(1)：35–45，1960；ASME 登记元数据确认作者、卷页与 DOI，用于线性状态预测和更新的基础。 | [出版社 DOI](https://doi.org/10.1115/1.3662552) |
| probrobotics2005 | Probabilistic Robotics | MIT Press，2005；出版社确认三位作者、年份及 ISBN，作为含噪观测与贝叶斯状态估计的基础。 | [MIT Press](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) |
| rkn2019 | Recurrent Kalman Networks | ICML 2019，PMLR 97：544–552；高维特征空间的因子化状态估计，保留局部线性及高斯假设的适用条件。 | [PMLR](https://proceedings.mlr.press/v97/becker19a.html) |
| dvrl2018 | DVRL | ICML 2018，PMLR 80：2117–2126；生成模型推断与策略联合训练，用于部分可观测状态学习。 | [PMLR](https://proceedings.mlr.press/v80/igl18a.html) |
| savi2022 | SAVi | ICLR 2022；作者项目及研究机构页面确认发表状态和作者；按有首帧提示与光流监督的条件对象学习描述。 | [Google Research](https://research.google/pubs/conditional-object-centric-learning-from-video/)、[作者项目页](https://slot-attention-video.github.io/) |
| slotformer2023 | SlotFormer | ICLR 2023；作者项目确认五位作者与会议；对象槽上的自回归动力学，未将对象槽直接等同于度量三维真值。 | [作者项目页](https://slotformer.github.io/)、[正式论文](https://openreview.net/pdf?id=TFbwV6I0VLg) |
| cater2020 | CATER | ICLR 2020；作者项目确认正式发表，区分于 ICCV 2019 workshop；用于合成环境的遮挡、容器关系和时序诊断。 | [作者项目页](https://rohitgirdhar.github.io/CATER/) |
| permatrack2021 | PermaTrack | ICCV 2021：10860–10869；正式论文确认循环记忆和合成不可见对象标注，明确隐藏真值是监督信号而非推断输入。 | [CVF](https://openaccess.thecvf.com/content/ICCV2021/html/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.html) |
| dynamicfusion2015 | DynamicFusion | CVPR 2015：343–352；论文集页面及元数据确认 RGB-D、规范几何和稠密非刚性运动场。 | [CVF](https://openaccess.thecvf.com/content_cvpr_2015/html/Newcombe_DynamicFusion_Reconstruction_and_2015_CVPR_paper.html) |
| dynaslam2018 | DynaSLAM | IEEE RA-L 3(4)：4076–4083，2018；登记元数据核对卷页及 DOI；主要建立静态地图，避免将动态剔除写成动态对象状态维护。 | [出版社 DOI](https://doi.org/10.1109/LRA.2018.2860039)、[作者论文](https://arxiv.org/abs/1806.05620) |
| nsff2021 | Neural Scene Flow Fields | CVPR 2021：6498–6508；连续表示联合时变外观、几何与三维运动，输入视频拟合与未来外推分开论述。 | [CVF](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Neural_Scene_Flow_Fields_for_Space-Time_View_Synthesis_of_Dynamic_CVPR_2021_paper.html) |
| raft2020 | RAFT | ECCV 2020，LNCS 12347：402–419；采用 Springer 正式版本及 DOI，用于两帧二维对应。 | [Springer](https://link.springer.com/chapter/10.1007/978-3-030-58536-5_24) |
| raft3d2021 | RAFT-3D | CVPR 2021：8375–8384；区分立体或 RGB-D 输入下的逐像素刚体运动与二维光流。 | [CVF](https://openaccess.thecvf.com/content/CVPR2021/html/Teed_RAFT-3D_Scene_Flow_Using_Rigid-Motion_Embeddings_CVPR_2021_paper.html) |
| cotracker2024 | CoTracker | ECCV 2024，LNCS 15120：18–35；Springer 确认六位作者、卷页及 DOI，说明因果短窗口和多点联合跟踪。 | [Springer](https://link.springer.com/chapter/10.1007/978-3-031-73033-7_2) |
| sort2016 | SORT | ICIP 2016：3464–3468；IEEE 登记元数据核对作者、卷页及 DOI，用于运动估计与数据关联基础。 | [出版社 DOI](https://doi.org/10.1109/ICIP.2016.7533003)、[作者论文](https://arxiv.org/abs/1602.00763) |
| deepsort2017 | Deep SORT | ICIP 2017：3645–3649；IEEE 登记元数据核对作者、页码及 DOI，说明外观关联度量的作用。 | [IEEE](https://ieeexplore.ieee.org/document/8296962)、[作者论文](https://arxiv.org/abs/1703.07402) |
| ocsort2023 | OC-SORT | CVPR 2023：9686–9696；论文正文 4.1 节确认重新关联后以两端观测构造虚拟轨迹，属于事后修正，未作为无观测预测的证据。 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Cao_Observation-Centric_SORT_Rethinking_SORT_for_Robust_Multi-Object_Tracking_CVPR_2023_paper.html) |
| bundlesdf2023 | BundleSDF | CVPR 2023：606–617；论文正文确认单目 RGB-D、首帧对象掩码、刚体假设和因果处理；联合位姿跟踪与神经重建。 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Wen_BundleSDF_Neural_6-DoF_Tracking_and_3D_Reconstruction_of_Unknown_Objects_CVPR_2023_paper.html) |
| calibration2017 | 分类置信度校准 | ICML 2017，PMLR 70：1321–1330；仅用于说明置信度和正确率的关系，不将分类温度缩放直接等同于连续轨迹校准。 | [PMLR](https://proceedings.mlr.press/v70/guo17a.html) |
| mvmwm2023 | MV-MWM | ICML 2023，PMLR 202：30613–30632；区分多视角掩蔽表示学习、控制时输入条件与时间观测缺失。 | [PMLR](https://proceedings.mlr.press/v202/seo23a.html) |
| roboflamingo2024 | RoboFlamingo | ICLR 2024；正式论文首页确认作者及会议；视觉语言输入与时序策略头，不将历史策略直接视为环境预测器。 | [正式论文](https://openreview.net/pdf?id=lFYj0oibGR) |
| diffusionpolicy2025 | Diffusion Policy | 采用 IJRR 44(10–11)：1684–1704，2025 正式卷期版；区分 2024 在线发表和 2023 RSS 初版，作者按期刊版本著录。 | [期刊](https://journals.sagepub.com/doi/10.1177/02783649241273668)、[作者期刊稿](https://diffusion-policy.cs.columbia.edu/diffusion_policy_ijrr.pdf) |
| wam_survey2026 | World-Action Models for Robot Learning and Control: A Survey | arXiv:2609.16074，2026-09-13；核对 16 位作者、题名和摘要，用于 WAM 的概念与设计维度说明，采用预印本。 | [arXiv](https://arxiv.org/abs/2609.16074) |
| worldvla2025 | WorldVLA | arXiv:2506.21539，2025-06-26；核对 12 位作者、题名和摘要，说明动作模型与世界模型的联合学习；本次未确认正式出版版本。 | [arXiv](https://arxiv.org/abs/2506.21539)、[作者发布页](https://huggingface.co/Alibaba-DAMO-Academy/WorldVLA) |
| tapvid3d2024 | TAPVid-3D | NeurIPS 2024，37：82149–82165；正式论文集核对八位作者、卷页及 DOI 10.52202/079017-2611；真实视频三维点跟踪基准，按有效标注评价，与 TAP-Vid 的二维轨迹分别组织。 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9566607d423f8c32a2d5ce09a8b62232-Abstract-Datasets_and_Benchmarks_Track.html)、[项目页](https://tapvid3d.github.io/) |
| pointodyssey2023 | PointOdyssey | ICCV 2023：19855–19865；采用正式会议版本，作者项目确认合成长序列、深度和二维／三维点轨迹，用于缺测预测学习和运动诊断规划。 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Zheng_PointOdyssey_A_Large-Scale_Synthetic_Dataset_for_Long-Term_Point_Tracking_ICCV_2023_paper.html)、[项目页](https://pointodyssey.com/) |
| bridgedata2023 | BridgeData V2 | CoRL 2023，PMLR 229：1723–1736；正式论文集核对十四位作者，第一作者为 Homer Rich Walke；规划为真实操作数据候选，接入时核对观测与动作定义。 | [PMLR](https://proceedings.mlr.press/v229/walke23a.html)、[项目页](https://bridgedata-v2.github.io/) |
| droid2024 | DROID | Robotics: Science and Systems 2024；正式论文集核对题名、作者及 DOI 10.15607/RSS.2024.XX.120，按前三位作者加 others 著录；规划为真实操作数据候选，不预设与实验室机械臂直接兼容。 | [RSS](https://www.roboticsproceedings.org/rss20/p120.html) |
| libero2023 | LIBERO | NeurIPS 2023，36：44776–44791；正式论文集 BibTeX 确认七位作者、卷页及 DOI 10.52202/075280-1939，用于多任务操作与知识迁移评测资源概述。 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) |
| calvin2022 | CALVIN | IEEE RA-L 7(3)：7327–7334，2022；出版社记录及官方仓库确认四位作者及 DOI 10.1109/LRA.2022.3180108，用于语言条件长程操作评价。 | [IEEE](https://ieeexplore.ieee.org/document/9788026)、[官方代码](https://github.com/mees/calvin) |
| simpler2025 | SimplerEnv / SIMPLER | 第八届 CoRL 正式论文集，PMLR 270：3705–3728，2025；作者顺序和年份按 PMLR 著录，区别于 2024 预印本，用于接近真实机器人设置的仿真评测。 | [PMLR](https://proceedings.mlr.press/v270/li25c.html)、[项目页](https://simpler-env.github.io/) |
| robocasa2024 | RoboCasa | RSS 2024；正式记录确认八位作者和 DOI 10.15607/RSS.2024.XX.050，题名采用 Household Tasks；概述日常场景操作资源。 | [RSS](https://www.roboticsproceedings.org/rss20/p050.html)、[项目页](https://robocasa.ai/) |
| robotwin2025 | RoboTwin | CVPR 2025：27649–27660；CVF 正式 BibTeX 核对十四位作者、题名和页码，概述双臂操作基准资源。 | [CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html) |

新增或修订条目时，先查询正式出版记录，再核对作者、题名、会议或期刊、年份、卷页及 DOI。保持原有文献键稳定，由 BibTeX 自动维护引用编号。原始 URL 可继续存入文献库；工程内的 `npu-gbt7714-numerical.bst` 控制输出，避免新增条目重新带出 URL。

输出复核：87 条文献均在正文或表格中实际引用，无未使用条目，核查表逐项覆盖全部文献；1.1 为 10 条、1.2 为 75 条，两节合并去重为 77 条，3.2.2 新增图网络动力学一条，3.2.3、3.2.4 复用已有条目，3.4 新增数据文献四条及交互基准文献五条。代表工作比较表中的方法均标注对应来源，状态形式沿用“显式／隐式”的文字分类。引用编号由 BibTeX 按首次出现顺序生成；参考文献隐藏 URL 与访问日期、保留 DOI。最终引用对应、分页和排版以本轮编译检查为准。
