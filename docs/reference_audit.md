# 参考文献发表状态核查

## 2026-10-30 当前引用与公开数据核查

本轮撤销航空维修替代试件及实采、实机验证安排。`cairepublic`、`ifamscarf` 随案例退出正文，`probrobotics2005` 不再单独引用；`splinegs2025` 和 `pointodyssey2023` 在第一部分补引。第二、三部分均无编号引文，方法名保留归属。当前 96 条实际引用全部在第一部分出现，文献库由 121 条清理至 96 条；移除的是 25 条当前未引用记录，保留原有在用键名。

2026-10-31：“研究条件落实情况—数据与验证条件”改为以数据源表汇总各候选数据源的类型、主要观测与参考、适用验证及使用条件，表内逐行标注文献，正文不再逐一列举；复用 `dycheck2022`、`pointodyssey2023`、`nerfies2021`、`hypernerf2021`、`droid2024`、`ref06`、`phystwin2025`，分别对应 DyCheck、PointOdyssey、Nerfies-HyperNeRF、DROID、PointWorld-DROID 及 PhysTwin。七个键均已在第一部分引用，实际引用仍为 96 条，首次引用编号不变；第三部分其余段落未加编号引文。

2026-10-31：3.1 补写“动态场景表示与连续时间运动”“空间结构与拓扑关系”“状态空间模型与动态演化”三小节，复用 `dnerf2021`、`nerfies2021`、`nsff2021`、`dynamicgs2024`、`gs4d2024`、`pomdp1998`、`worldmodels2018`、`ref01`、`dreamer2020`、`ref02`，均为第一部分已引条目，实际引用仍为 96 条。

2026-10-31：按作者新稿重写 1.1“选题依据及研究意义”，正文按首次引用顺序使用 12 条资料，对应 `worldmodels2018`、`ref02`、`nsfcworldmodel2026`、`nsfworldmodel2025`、`deepmindgenie2025`、`nvidiacosmos2025`、`nasarrrm2026`、`retimegs2026`、`consistentinstance2026`、`gaustar2025`、`ref06`、`phystwin2025`，即新编号 [1]–[12]。新增 NASA RRM 条目 `nasarrrm2026`；原 1.1 使用而新稿不再引用的 `cnworld2026`、`tencentworld2025`、`aiplus2025`、`nasadrone2025`、`nasamaintenance2026`、`nasavms2026` 退出正文，实际引用由 96 条调整为 91 条。核查：NSFC 通告日期为 2026-09-18；NSF Award 2443468 经 NSF 公开奖项接口核对（CAREER，2025，UCSD，PI Zhiting Hu）；Genie 3 博文日期为 2025-08-05；Cosmos 新闻稿日期为 2025-01-06；NASA 官网对 RRM 页面限流，未能直接打开，RRM 任务内容按 NASA RRM 资料与 NTRS 记录交叉核对。

2026-10-31：1.2 按作者新稿整体重写，1.2.2 标题由“面向交互的世界模型”调整为“世界模型”，1.2.1—1.2.3 均改用以代表性工作脉络图为核心的叙述。新增 `savostyanov2026`、`vjepa2_2025`、`deepmindgenie2_2024`、`deepmindgenie4_2026`、`infiniteworld2026`、`tasksufficientwm2026`、`geniedrive2026`、`vectorworld2026`、`gamengen2024`、`drivedreamer2024`、`drivedreamer2_2025`、`epona2025`、`occworld2024` 共 13 条；由于新条目在 1.2.2 首次引用，全文编号按首次引用顺序重排，实际引用为 98 条。原 1.2 使用而新稿不再引用的 `semanticscholarapi2026`、`bundlesdf2023`、`tesseract2025`、`ensembles2017`、`calibration2017` 等退出正文。另据 [Google DeepMind 官方页面](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)核对，`deepmindgenie4_2026` 作者为 Raia Hadsell、Diego Rivas、Hang Qi，文献库作者字段已据此更正。

2026-10-31：1.2.1“四维动态场景重建”按作者新稿重写，按隐式场、显式图元与点级几何三类组织，并以现行图 3（2021—2026 年代表性工作脉络，SVG 导出版）为纲；图题年份范围与图中刻度一致，未改图。新稿不再引用 `sobolevfusion2018`、`gaussianflow2024`、`se3bspline2026`、`atgs2025`、`raft2020`、`raft3d2021`、`tapir2023`、`cotracker3`，按“文献库只保留正文实际引用条目”的约定从 `references.bib` 清除，实际引用由 98 条调整为 90 条，文献库由 110 条调整为 102 条。编号由 BibTeX 按首次引用顺序重排，1.2.1 现为 DynamicFusion [16]、NeRF [17]、D-NeRF [18]、Nerfies [19]、NSFF [20]、HyperNeRF [21]、3DGS [22]、Dynamic 3D Gaussians [23]、4D-GS [24]、Deformable 3D Gaussians [25]、SC-GS [26]、SplineGS [27]、ParticleGS [28]、MoSca [29]、Shape of Motion [30]、MovingParts [31]、USplat4D [32]、DUSt3R [33]、VGGT [34]、MonST3R [35]、CUT3R [36]、D4RT [37]、DyCheck [38]、TAP-Vid [39]、TAPVid-3D [40]、PointOdyssey [41]；RetimeGS [8]、Consistent Instance Field [9]、GauSTAR [10] 已在 1.1 首次引用，此处沿用。新稿开头的三类综述引用 `cndynamic2024`、`cnnerf2025`、`cndynamicgs2026` 予以保留。图 3 仍列 AT-GS、4DSurf 等正文未逐一点名的节点，按代表性工作概览处理，不据此新增引用；`surf4d2026` 仅见于图 3 节点，与其余 11 条历史未引用记录暂留库中，未在本轮一并清理。

下列为 2026-10-30 根据作者项目、官方代码或正式数据发布页面核对的验证来源；本次未下载完整数据，也未执行研究实验。

| 来源 | 可用证据与用途 | 核查入口与限制 |
| --- | --- | --- |
| DyCheck iPhone | 真实动态观测，共可见区域及关键点评价；按序列的相机和深度条件使用 | [官方数据说明](https://github.com/KAIR-BAIR/dycheck/blob/main/docs/DATASETS.md)、[PCK 实现](https://github.com/KAIR-BAIR/dycheck/blob/main/dycheck/core/metrics/keypoint.py) |
| PointOdyssey | 合成 RGB、深度、实例、相机与二维／三维轨迹；部分序列有同步多视角 | [作者发布](https://pointodyssey.com/)。实例标注不直接等同于任意部件粒度 |
| Nerfies-HyperNeRF | 公开动态序列及相应训练／测试划分，支持观测恢复与结构变化分析 | [HyperNeRF 官方数据发布](https://github.com/google/hypernerf/releases/tag/v0.1)、[DyCheck 处理说明](https://github.com/KAIR-BAIR/dycheck/blob/main/docs/DATASETS.md)。图像序列不直接提供完整材料连接或新生表面形成真值 |
| DROID | 公开交互示范和动作记录，按片段筛选预测输入与后续参考 | [作者项目及读取说明](https://droid-dataset.github.io/) |
| PointWorld-DROID | 作者处理后的三维轨迹及有效性信息 | [NVIDIA 数据发布](https://huggingface.co/datasets/nvidia/PointWorld-DROID)、[官方实现](https://github.com/NVlabs/PointWorld)。自动估计轨迹按带误差参考单列 |
| PhysTwin | 作者公开原始数据、处理数据及结果，按具体片段核对响应参考 | [官方代码与数据下载说明](https://github.com/Jianghanxiao/PhysTwin)。不把重建或优化结果直接当作独立物理真值 |
| GauSTAR 比较条件 | 公开实现提供 ActorsHQ 数据处理路径 | [作者说明](https://github.com/eth-ait/GauSTAR)：论文捕获序列受许可限制未发布，不能据演示序列承诺公共切割基准 |

PCK 的阈值与三维误差定义保留为评价约定，不属于性能目标。物理连接精确率、召回率及形成时间误差仅在存在直接参考时计算；其他公开序列的结论限于其可评价分量。默认验证不新增自建数据或实体实验。

## 历史核查记录

以下保留此前的来源核验与写作变化，其中已退出正文的条目、案例及旧引用数量仅用于追溯，当前范围以上节为准。



2026-10-30：暂定题名统一为“连续动态世界模型构建方法研究”；当前正文与方法图按语义使用观测置信度、不确定性及观测支持等表述。文献原始题名、作者、发表信息及引文键不因本轮术语调整而改动；下文按日期记录的旧题名保留用于追溯。

2026-10-30：贯穿案例改为公开航空维修背景下的薄壁替代试件局部切除与夹持移取。西北工业大学官网“学校简介”仅用于核实学校公开介绍的航空航天、材料和国防装备研究背景；Lufthansa Technik 与 Fraunhofer IFAM 的公开页面仅用于说明航空复合材料维修中的扫描、材料去除和修补准备等工艺背景。替代试件、切除过程、动作序列及预测结果均为拟建验证场景，不把上述公开资料表述为本课题数据或实验结果。

| 文献键 | 题名 | 正式出版信息或状态 | 核验来源 |
| --- | --- | --- | --- |
| `nwpuintro2026` | 学校简介 | 西北工业大学官网公开页面，页面数据截至 2026-08-05 | [学校官方页面](https://www.nwpu.edu.cn/xxgk/xxjj.htm) |
| `cairepublic` | CAIRE repair robot: Robot for inspection and repairs | Lufthansa Technik 官方公开产品页面，未标发布日期 | [机构公开页面](https://www.lufthansa-technik.com/en/caire-repair-robot) |
| `ifamscarf` | Abrasive pre-treatment with vacuum suction blasting | Fraunhofer IFAM 官方公开技术页面，未标发布日期 | [机构公开页面](https://www.ifam.fraunhofer.de/en/technologies/abrasive-pre-treatment-vacuum-suction-blasting.html) |
| `splinegs2025` | SplineGS: Robust Motion-Adaptive Spline for Real-Time Dynamic 3D Gaussians from Monocular Video | CVPR 2025：26866–26875 | [CVF 正式记录](https://openaccess.thecvf.com/content/CVPR2025/html/Park_SplineGS_Robust_Motion-Adaptive_Spline_for_Real-Time_Dynamic_3D_Gaussians_from_CVPR_2025_paper.html) |
## 2026-10-29 重写 1.2 后的当前引文

2026-10-29 按导师意见重写 1.2“国内外研究现状及发展态势”，保留四维动态场景重建、面向交互的世界模型、
具身操作中的动作学习三个主题，各主题重建为总分总结构并按方法类别重新组织。本轮文献调整如下。

**新增三条正式会议论文**，用于支撑学习式前馈恢复路线的论述与时间轴节点：

| 文献键 | 题名 | 正式出版信息 | 核验来源 |
| --- | --- | --- | --- |
| `dust3r2024` | DUSt3R: Geometric 3D Vision Made Easy | CVPR 2024：20697–20709 | [CVF 正式记录](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html) |
| `vggt2025` | VGGT: Visual Geometry Grounded Transformer | CVPR 2025：5294–5306 | [CVF 正式记录](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) |
| `d4rt2026` | Efficiently Reconstructing Dynamic Scenes One D4RT at a Time | CVPR 2026：7382–7392；CVPR 2026 最佳论文 | [CVF 正式记录](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html)、[CVPR 2026 最佳论文公告](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) |

三条均为作者、题名、年份、页码由 CVF 正式记录逐项核对的前馈几何恢复代表工作；正文仅用于说明
免标定点图回归与单次前馈几何的能力，不据此推断其在动态场景上的连续时间建模能力。D4RT 是用户在
2026-10-29 讨论中特别指出的工作，最佳论文身份来自 CVPR 官方公告；正文只据其统一查询接口说明重建
与跟踪的联系，不把最佳论文奖项当作方法适用范围的证据。

**新增两条已在库中但此前未引用的条目**：`genie2024`（Genie，ICML 2024，PMLR 235：4603–4623）与
`worldvla2025`（WorldVLA，arXiv:2506.21539，预印本）。前者用于说明可交互环境的生成式建模，
后者用于说明动作与后续图像的联合预测。WorldVLA 与 DreamZero 均按预印本处理，在正文中明确标注，
并在时间轴图中以空心节点和 `†` 区分。

**移除三条结果示例图及其图源引用**：原图 2“动态场景重建的代表性结果”、图 3“动作条件下的三维场景预测”、
图 4“具身操作的典型建模仿真”不再载入正文，相应读图文字一并删除；Shape of Motion、RetimeGS、PointWorld、
OpenVLA 的引用改由正文论证承担，引用关系保留。图源文件、素材与来源记录按用户要求保留供追溯。

**新增 1.2 的统计与时间轴图**：图 2—4 分别为三个主题的年度论文检索数量，图 5—7 为三个主题的方法路线时间轴。
时间轴节点全部对应上表及既有核查记录中的正式出版条目，年份取论文集或卷期出版年；预印本节点单独标注。
按用户要求，年度统计由 2015—2025 扩展到 2026 年，2026 年只计入截至 2026-10-29 已正式发表的记录，
图中以星号和白柱标出，不能与完整年度直接比较。统计口径、检索式、清单与年度表见[统计说明](literature_stats/README.md)。

本轮重写后全文实际引用 **96 条**：正式会议论文 70 篇、正式期刊论文 13 篇、正式出版专著 1 部、
政策、基金项目、企业、图片来源及数据接口的官方在线资料 10 条、预印本 2 篇（WorldVLA、DreamZero）。
原有文献键保持不变，首次引用编号由 BibTeX 按正文顺序重新生成。

## 2026-10-29 1.1 重写时的引文记录（保留）

2026-10-29 重写 1.1 后，全文实际引用 **92 条**：正式会议论文 68 篇、正式期刊论文 13 篇、正式出版专著 1 部、政策、基金项目、企业及图片来源的官方在线资料 9 条、近期预印本 1 篇。本轮新增八条在线资料，其中五条用于国家政策、美国 NSF 相关项目及国内外企业布局的事实说明，三条用于真实照片的来源引用，不计入正式学术论文数量；既有论文发表状态沿用 2026-10-27 的逐条核验记录。新增条目均被正文引用，全文首次引用编号随新结构重新生成。

本轮核查中，美国 NSF 项目网页未能由浏览工具读取，改由 [NSF 官方公开 API](https://api.nsf.gov/services/v1/awards/2443468.json) 读取项目 2443468 的正式题名、摘要及 2025—2030 年执行期；摘要明确涉及世界模型、多模态建模和具身交互经验，正文只据此说明相关项目内容，不泛化为 NSF 专项指南。国家政策依据网信办转载的国务院原文，区分一般人工智能需求与世界模型研究的关联。企业资料仅用于说明公开布局及所述研究方向，不以企业宣传替代方法性能评价。基金委通告只核实专项名称和发布事实。

DreamZero 为 **2026 年预印本**：截至本轮核查，作者项目与 arXiv 页面未给出可确认的正式期刊或会议论文集版本。它用于说明近期世界动作模型联合生成视频和动作的代表方向，保留预印本标识，不作为已正式发表论文。其余实际引用不含长期未发表的旧预印本；较早的文献均有正式出版记录，并用于交代基础方法或经典进展。

### 当前正文逐条出版信息及核验来源

下表按正文首次引用顺序列出实际使用的全部条目。表中年份、卷期及页码采用书目著录值；链接指向论文集、出版社、期刊、正式发布机构或可确认会议状态的作者／研究机构页面。CoTracker 的会议届次与论文集出版年、Diffusion Policy 的在线日期与正式卷期年不同，按上文说明处理。部分期刊网页可能要求访问验证；对应卷期也由此前记录的期刊目录或登记元数据核对。

| 文献键 | 题名 | 正式出版信息或状态 | 核验来源 |
| --- | --- | --- | --- |
| `cnworld2026` | 大模型技术演进：世界模型让人工智能从感知走向决策(特邀) | 计算机工程，2026，卷 52（2）：1–6 | [出版或来源记录](https://www.ecice06.com/CN/10.19678/j.issn.1000-3428.0253281) |
| `ref02` | Mastering diverse control tasks through world models | Nature，2025，卷 640（8059）：647–653 | [出版或来源记录](https://doi.org/10.1038/s41586-025-08744-2) |
| `nsfcworldmodel2026` | 关于发布2026年度国家自然科学基金“空间智能与世界模型”专项项目申请指南的通告 | 国家自然科学基金委员会公开通告，2026 | [出版或来源记录](https://www.nsfc.gov.cn/p1/3381/2824/142425.html) |
| `nsfworldmodel2025` | CAREER: From Language Models to World Models: New Inference, Learning, and Modeling for Machine Reasoning | NSF 官方项目记录，2025；项目 2443468 | [NSF 官方 API](https://api.nsf.gov/services/v1/awards/2443468.json) |
| `deepmindgenie2025` | Genie 3: A new frontier for world models | Google DeepMind 官方发布，2025-08-05 | [官方发布](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) |
| `nvidiacosmos2025` | NVIDIA Launches Cosmos World Foundation Model Platform to Accelerate Physical AI Development | NVIDIA 官方发布，2025-01-06 | [官方发布](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Launches-Cosmos-World-Foundation-Model-Platform-to-Accelerate-Physical-AI-Development/default.aspx) |
| `tencentworld2025` | 腾讯混元3D世界模型1.0 | 腾讯官方模型页，2025；以指定版本介绍为依据 | [官方模型页](https://3d-models.hunyuan.tencent.com/world/?currentTab=HunyuanWorld-1.0) |
| `aiplus2025` | 关于深入实施“人工智能+”行动的意见 | 国务院政策文件，国发〔2025〕11号；2025-08-21 成文，网信办 2025-08-27 转载 | [官方转载全文](https://www.cac.gov.cn/2025-08/27/c_1758018277755538.htm) |
| `nasadrone2025` | Testing Drones for Mars in the Mojave Desert | NASA 官方图片页，2025-12-05；图片署名 NASA/JPL-Caltech | [官方图源](https://www.nasa.gov/image-article/testing-drones-for-mars-in-the-mojave-desert/) |
| `nasamaintenance2026` | Keeping NASA Flying: Ground Crews Ensure Aircraft Readiness | NASA 官方文章，2026-05-22；选用 AFRC2026-0004-036，署名 NASA/Christopher LC Clark | [官方图源](https://www.nasa.gov/centers-and-facilities/armstrong/keeping-nasa-flying-ground-crews-ensure-aircraft-readiness/) |
| `nasavms2026` | Vertical Motion Simulator (VMS) | NASA Ames 官方设施介绍，网页元数据更新于 2026-03-27；选用驾驶舱照片 acd26-0039-005 | [官方图源](https://www.nasa.gov/ames/aviationsystems/vms/) |
| `cndynamicgs2026` | 基于三维高斯泼溅的动态场景重建研究综述 | 计算机辅助设计与图形学学报，2026，卷 38（1）：61–77 | [出版或来源记录](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2025-00251) |
| `retimegs2026` | RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：7340–7350 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_RetimeGS_Continuous-Time_Reconstruction_of_4D_Gaussian_Splatting_CVPR_2026_paper.html) |
| `cut3r2025` | Continuous 3D Perception Model with Persistent State | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2025：10510–10522 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Continuous_3D_Perception_Model_with_Persistent_State_CVPR_2025_paper.html) |
| `d4rt2026` | Efficiently Reconstructing Dynamic Scenes One D4RT at a Time | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：7382–7392；CVPR 2026 最佳论文 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html)、[最佳论文公告](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) |
| `phystwin2025` | PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos | Proceedings of the IEEE/CVF International Conference on Computer Vision，2025：7219–7230 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) |
| `ref06` | PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：20765–20779 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.html) |
| `cndynamic2024` | 动态场景的三维重建研究综述 | 计算机科学与探索，2024，卷 18（4）：831–860 | [出版或来源记录](https://opaj.napstic.cn/periodicalArticle/0120240401922522) |
| `cnnerf2025` | 神经辐射场技术及应用综述 | 计算机辅助设计与图形学学报，2025，卷 37（1）：51–74 | [出版或来源记录](https://jcad.cn/cn/article/Y2025/I1/51) |
| `nerf2020` | NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | Computer Vision – ECCV 2020，2020，卷 12346：405–421 | [出版或来源记录](https://link.springer.com/chapter/10.1007/978-3-030-58452-8_24) |
| `dnerf2021` | D-NeRF: Neural Radiance Fields for Dynamic Scenes | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)，2021：10318–10327 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2021/html/Pumarola_D-NeRF_Neural_Radiance_Fields_for_Dynamic_Scenes_CVPR_2021_paper.html) |
| `nerfies2021` | Nerfies: Deformable Neural Radiance Fields | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)，2021：5865–5874 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2021/html/Park_Nerfies_Deformable_Neural_Radiance_Fields_ICCV_2021_paper.html) |
| `hypernerf2021` | HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields | ACM Transactions on Graphics，2021，卷 40（6）：238:1–238:12 | [出版或来源记录](https://doi.org/10.1145/3478513.3480487) |
| `nsff2021` | Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2021：6498–6508 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Neural_Scene_Flow_Fields_for_Space-Time_View_Synthesis_of_Dynamic_CVPR_2021_paper.html) |
| `gs2023` | 3D Gaussian Splatting for Real-Time Radiance Field Rendering | ACM Transactions on Graphics，2023，卷 42（4）：139:1–139:14 | [出版或来源记录](https://doi.org/10.1145/3592433) |
| `dynamicgs2024` | Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis | 2024 International Conference on 3D Vision (3DV)，2024：800–809 | [出版或来源记录](https://doi.org/10.1109/3dv62453.2024.00044) |
| `gs4d2024` | 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2024：20310–20320 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_4D_Gaussian_Splatting_for_Real-Time_Dynamic_Scene_Rendering_CVPR_2024_paper.html) |
| `scgs2024` | SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)，2024：4220–4230 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_SC-GS_Sparse-Controlled_Gaussian_Splatting_for_Editable_Dynamic_Scenes_CVPR_2024_paper.html) |
| `deformablegs2024` | Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)，2024：20331–20341 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Deformable_3D_Gaussians_for_High-Fidelity_Monocular_Dynamic_Scene_Reconstruction_CVPR_2024_paper.html) |
| `gaussianflow2024` | Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)，2024：21136–21145 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2024/html/Lin_Gaussian-Flow_4D_Reconstruction_with_Dynamic_3D_Gaussian_Particle_CVPR_2024_paper.html) |
| `ref05` | MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2025：6165–6177 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_MoSca_Dynamic_Gaussian_Fusion_from_Casual_Videos_via_4D_Motion_CVPR_2025_paper.html) |
| `shapeofmotion2025` | Shape of Motion: 4D Reconstruction from a Single Video | Proceedings of the IEEE/CVF International Conference on Computer Vision，2025：9660–9672 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Shape_of_Motion_4D_Reconstruction_from_a_Single_Video_ICCV_2025_paper.html) |
| `movingparts2024` | MovingParts: Motion-based 3D Part Discovery in Dynamic Radiance Field | International Conference on Learning Representations，2024 | [出版或来源记录](https://proceedings.iclr.cc/paper_files/paper/2024/hash/c34ddd05eb089991f06f3c5dc36836e0-Abstract-Conference.html) |
| `consistentinstance2026` | Consistent Instance Field for Dynamic Scene Understanding | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：3783–3793 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Consistent_Instance_Field_for_Dynamic_Scene_Understanding_CVPR_2026_paper.html) |
| `dynamicfusion2015` | DynamicFusion: Reconstruction and Tracking of Non-Rigid Scenes in Real-Time | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition，2015：343–352 | [出版或来源记录](https://openaccess.thecvf.com/content_cvpr_2015/html/Newcombe_DynamicFusion_Reconstruction_and_2015_CVPR_paper.html) |
| `sobolevfusion2018` | SobolevFusion: 3D Reconstruction of Scenes Undergoing Free Non-Rigid Motion | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition，2018：2646–2655 | [出版或来源记录](https://openaccess.thecvf.com/content_cvpr_2018/html/Slavcheva_SobolevFusion_3D_Reconstruction_CVPR_2018_paper.html) |
| `bundlesdf2023` | BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2023：606–617 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2023/html/Wen_BundleSDF_Neural_6-DoF_Tracking_and_3D_Reconstruction_of_Unknown_Objects_CVPR_2023_paper.html) |
| `gaustar2025` | GauSTAR: Gaussian Surface Tracking and Reconstruction | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2025：16543–16553 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_GauSTAR_Gaussian_Surface_Tracking_and_Reconstruction_CVPR_2025_paper.html) |
| `atgs2025` | Adaptive and Temporally Consistent Gaussian Surfels for Multi-View Dynamic Reconstruction | Proceedings of the Winter Conference on Applications of Computer Vision，2025：742–752 | [出版或来源记录](https://openaccess.thecvf.com/content/WACV2025/html/Chen_Adaptive_and_Temporally_Consistent_Gaussian_Surfels_for_Multi-View_Dynamic_Reconstruction_WACV_2025_paper.html) |
| `surf4d2026` | 4DSurf: High-Fidelity Dynamic Scene Surface Reconstruction | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：22539–22549 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_4DSurf_High-Fidelity_Dynamic_Scene_Surface_Reconstruction_CVPR_2026_paper.html) |
| `raft2020` | RAFT: Recurrent All-Pairs Field Transforms for Optical Flow | Computer Vision – ECCV 2020，2020，卷 12347：402–419 | [出版或来源记录](https://link.springer.com/chapter/10.1007/978-3-030-58536-5_24) |
| `raft3d2021` | RAFT-3D: Scene Flow Using Rigid-Motion Embeddings | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2021：8375–8384 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2021/html/Teed_RAFT-3D_Scene_Flow_Using_Rigid-Motion_Embeddings_CVPR_2021_paper.html) |
| `tapir2023` | TAPIR: Tracking Any Point with Per-Frame Initialization and Temporal Refinement | Proceedings of the IEEE/CVF International Conference on Computer Vision，2023：10061–10072 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2023/html/Doersch_TAPIR_Tracking_Any_Point_with_Per-Frame_Initialization_and_Temporal_Refinement_ICCV_2023_paper.html) |
| `cotracker2024` | CoTracker: It Is Better to Track Together | Computer Vision – ECCV 2024，2025，卷 15120：18–35 | [出版或来源记录](https://link.springer.com/chapter/10.1007/978-3-031-73033-7_2) |
| `cotracker3` | CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos | Proceedings of the IEEE/CVF International Conference on Computer Vision，2025：6013–6022 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2025/html/Karaev_CoTracker3_Simpler_and_Better_Point_Tracking_by_Pseudo-Labelling_Real_Videos_ICCV_2025_paper.html) |
| `omnimotion2023` | Tracking Everything Everywhere All at Once | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)，2023：19795–19806 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_Tracking_Everything_Everywhere_All_at_Once_ICCV_2023_paper.html) |
| `monst3r2025` | MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion | International Conference on Learning Representations，2025 | [出版或来源记录](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ce1710ff5b66f89b0d707bf1ec2850bf-Abstract-Conference.html) |
| `se3bspline2026` | Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：33291–33300 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Learning_Explicit_Continuous_Motion_Representation_for_Dynamic_Gaussian_Splatting_from_CVPR_2026_paper.html) |
| `particlegs2026` | ParticleGS: Learning Neural Gaussian Particle Dynamics from Videos for Prior-free Physical Motion Extrapolation | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2026：8331–8341 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2026/html/Quan_ParticleGS_Learning_Neural_Gaussian_Particle_Dynamics_from_Videos_for_Prior-free_CVPR_2026_paper.html) |
| `usplat4d2026` | Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D Reconstruction | International Conference on Learning Representations，2026 | [出版或来源记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/26300457961c3e056ea61c9d3ebec2a4-Abstract-Conference.html) |
| `ensembles2017` | Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Advances in Neural Information Processing Systems，2017，卷 30 | [出版或来源记录](https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html) |
| `calibration2017` | On Calibration of Modern Neural Networks | Proceedings of the 34th International Conference on Machine Learning，2017，卷 70：1321–1330 | [出版或来源记录](https://proceedings.mlr.press/v70/guo17a.html) |
| `dycheck2022` | Monocular Dynamic View Synthesis: A Reality Check | Advances in Neural Information Processing Systems，2022，卷 35：33768–33780 | [出版或来源记录](https://papers.nips.cc/paper/2022/hash/dab5a29f6614ec47ea0ca85c140226fd-Abstract-Conference.html) |
| `tapvid2022` | TAP-Vid: A Benchmark for Tracking Any Point in a Video | Advances in Neural Information Processing Systems，2022，卷 35：13610–13626 | [出版或来源记录](https://proceedings.neurips.cc/paper_files/paper/2022/hash/58168e8a92994655d6da3939e7cc0918-Abstract-Datasets_and_Benchmarks.html) |
| `tapvid3d2024` | TAPVid-3D: A Benchmark for Tracking Any Point in 3D | Advances in Neural Information Processing Systems，2024，卷 37：82149–82165 | [出版或来源记录](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9566607d423f8c32a2d5ce09a8b62232-Abstract-Datasets_and_Benchmarks_Track.html) |
| `pomdp1998` | Planning and acting in partially observable stochastic domains | Artificial Intelligence，1998，卷 101（1–2）：99–134 | [出版或来源记录](https://doi.org/10.1016/S0004-3702%2898%2900023-X) |
| `worldmodels2018` | Recurrent World Models Facilitate Policy Evolution | Advances in Neural Information Processing Systems，2018，卷 31 | [出版或来源记录](https://proceedings.neurips.cc/paper_files/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html) |
| `muzero2020` | Mastering Atari, Go, chess and shogi by planning with a learned model | Nature，2020，卷 588（7839）：604–609 | [出版或来源记录](https://doi.org/10.1038/s41586-020-03051-4) |
| `ref01` | Learning Latent Dynamics for Planning from Pixels | Proceedings of the 36th International Conference on Machine Learning，2019，卷 97：2555–2565 | [出版或来源记录](https://proceedings.mlr.press/v97/hafner19a.html) |
| `dreamer2020` | Dream to Control: Learning Behaviors by Latent Imagination | International Conference on Learning Representations，2020 | [出版或来源记录](https://danijar.com/project/dreamer/) |
| `ijepa2023` | Self-Supervised Learning From Images With a Joint-Embedding Predictive Architecture | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)，2023：15619–15629 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2023/html/Assran_Self-Supervised_Learning_From_Images_With_a_Joint-Embedding_Predictive_Architecture_CVPR_2023_paper.html) |
| `ref03` | DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning | Proceedings of the 42nd International Conference on Machine Learning，2025，卷 267：79115–79135 | [出版或来源记录](https://proceedings.mlr.press/v267/zhou25t.html) |
| `pets2018` | Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models | Advances in Neural Information Processing Systems，2018，卷 31 | [出版或来源记录](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) |
| `tdmpc2_2024` | TD-MPC2: Scalable, Robust World Models for Continuous Control | International Conference on Learning Representations (ICLR)，2024 | [出版或来源记录](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) |
| `gns2020` | Learning to Simulate Complex Physics with Graph Networks | Proceedings of the 37th International Conference on Machine Learning，2020，卷 119：8459–8468 | [出版或来源记录](https://proceedings.mlr.press/v119/sanchez-gonzalez20a.html) |
| `savi2022` | Conditional Object-Centric Learning from Video | International Conference on Learning Representations，2022 | [出版或来源记录](https://research.google/pubs/conditional-object-centric-learning-from-video/) |
| `slotformer2023` | SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models | International Conference on Learning Representations，2023 | [出版或来源记录](https://slotformer.github.io/) |
| `tesseract2025` | Learning 4D Embodied World Models | Proceedings of the IEEE/CVF International Conference on Computer Vision，2025：5337–5347 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) |
| `gwm2025` | GWM: Towards Scalable Gaussian World Models for Robotic Manipulation | Proceedings of the IEEE/CVF International Conference on Computer Vision，2025：9263–9274 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html) |
| `ref10` | Beyond Pixel Histories: World Models with Persistent 3D State | Proceedings of the 43rd International Conference on Machine Learning，2026，卷 306：34048–34070 | [出版或来源记录](https://proceedings.mlr.press/v306/garcin26a.html) |
| `ref07` | Future Dynamic 3D Reconstruction: Toward 3D World Modeling with Disentangled Ego-Motion | Proceedings of the 43rd International Conference on Machine Learning，2026，卷 306：90232–90250 | [出版或来源记录](https://proceedings.mlr.press/v306/morbitzer26a.html) |
| `ref08` | Flow Equivariant World Models: Structured Memory for Dynamic Environments | Proceedings of the 43rd International Conference on Machine Learning，2026，卷 306：73968–74002 | [出版或来源记录](https://proceedings.mlr.press/v306/lillemark26a.html) |
| `mvmwm2023` | Multi-View Masked World Models for Visual Robotic Manipulation | Proceedings of the 40th International Conference on Machine Learning，2023，卷 202：30613–30632 | [出版或来源记录](https://proceedings.mlr.press/v202/seo23a.html) |
| `cnvla2026` | 面向具身操作的视觉–语言–动作模型综述 | 自动化学报，2026，卷 52（1）：18–51 | [出版或来源记录](https://www.aas.net.cn/article/2026/1) |
| `rt22023` | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Proceedings of The 7th Conference on Robot Learning，2023，卷 229：2165–2183 | [出版或来源记录](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| `openvla2025` | OpenVLA: An Open-Source Vision-Language-Action Model | Proceedings of The 8th Conference on Robot Learning，2025，卷 270：2679–2713 | [出版或来源记录](https://proceedings.mlr.press/v270/kim25c.html) |
| `pi02025` | π₀: A Vision-Language-Action Flow Model for General Robot Control | Proceedings of Robotics: Science and Systems，2025 | [出版或来源记录](https://roboticsproceedings.org/rss21/p010.html) |
| `ref12` | BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models | Advances in Neural Information Processing Systems，2025，卷 38：63635–63673 | [出版或来源记录](https://papers.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html) |
| `peract2023` | Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation | Proceedings of The 6th Conference on Robot Learning，2023，卷 205：785–799 | [出版或来源记录](https://proceedings.mlr.press/v205/shridhar23a.html) |
| `rvt22024` | RVT-2: Learning Precise Manipulation from Few Demonstrations | Proceedings of Robotics: Science and Systems，2024 | [出版或来源记录](https://www.roboticsproceedings.org/rss20/p055.html) |
| `diffusionpolicy2025` | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | The International Journal of Robotics Research，2025，卷 44（10–11）：1684–1704 | [出版或来源记录](https://doi.org/10.1177/02783649241273668) |
| `roboflamingo2024` | Vision-Language Foundation Models as Effective Robot Imitators | International Conference on Learning Representations，2024 | [出版或来源记录](https://proceedings.iclr.cc/paper_files/paper/2024/hash/71639c317fb0bf398835627b4418693e-Abstract-Conference.html) |
| `dreamzero2026` | World Action Models are Zero-shot Policies | arXiv 预印本，2026 | [出版或来源记录](https://arxiv.org/abs/2602.15922) |
| `bridgedata2023` | BridgeData V2: A Dataset for Robot Learning at Scale | Proceedings of the 7th Conference on Robot Learning，2023，卷 229：1723–1736 | [出版或来源记录](https://proceedings.mlr.press/v229/walke23a.html) |
| `droid2024` | DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | Proceedings of Robotics: Science and Systems，2024 | [出版或来源记录](https://www.roboticsproceedings.org/rss20/p120.html) |
| `rlbench2020` | RLBench: The Robot Learning Benchmark & Learning Environment | IEEE Robotics and Automation Letters，2020，卷 5（2）：3019–3026 | [出版或来源记录](https://doi.org/10.1109/LRA.2020.2974707) |
| `libero2023` | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | Advances in Neural Information Processing Systems，2023，卷 36：44776–44791 | [出版或来源记录](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) |
| `calvin2022` | CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks | IEEE Robotics and Automation Letters，2022，卷 7（3）：7327–7334 | [出版或来源记录](https://doi.org/10.1109/LRA.2022.3180108) |
| `robocasa2024` | RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots | Proceedings of Robotics: Science and Systems，2024 | [出版或来源记录](https://www.roboticsproceedings.org/rss20/p050.html) |
| `robotwin2025` | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition，2025：27649–27660 | [出版或来源记录](https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html) |
| `simpler2025` | Evaluating Real-World Robot Manipulation Policies in Simulation | Proceedings of The 8th Conference on Robot Learning，2025，卷 270：3705–3728 | [出版或来源记录](https://proceedings.mlr.press/v270/li25c.html) |
| `probrobotics2005` | Probabilistic Robotics | MIT Press，2005 | [出版或来源记录](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) |
| `pointodyssey2023` | PointOdyssey: A Large-Scale Synthetic Dataset for Long-Term Point Tracking | Proceedings of the IEEE/CVF International Conference on Computer Vision，2023：19855–19865 | [出版或来源记录](https://openaccess.thecvf.com/content/ICCV2023/html/Zheng_PointOdyssey_A_Large-Scale_Synthetic_Dataset_for_Long-Term_Point_Tracking_ICCV_2023_paper.html) |

### 此前轮次的核查记录

2026-10-27 补充 3.3 数据和评价，复用书目中的 `pointodyssey2023` 和 `droid2024`，引用总数由 42 条增至 44 条，均为正式会议论文；同时复用 DyCheck、PhysTwin 和 PointWorld。候选数据内容、示例来源及 PCK 定义核查见 [PointOdyssey 作者项目](https://pointodyssey.com/)、[DROID 正式论文](https://www.roboticsproceedings.org/rss20/p120.html)、[PointWorld-DROID 数据说明](https://huggingface.co/datasets/nvidia/PointWorld-DROID)、[PhysTwin 正式论文](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html)及 [DyCheck 官方实现](https://github.com/KAIR-BAIR/dycheck/blob/main/dycheck/core/metrics/keypoint.py)。自动估计的 PointWorld-DROID 轨迹不视为完整真值；指标图解为原创示意，不作为实测结果。

2026-10-27 撰写 3.2，复用 `scgs2024`、`ref05`、`se3bspline2026`、`shapeofmotion2025`、`gaustar2025`、`gns2020` 和 `ref06`，实际引用及首次引用顺序保持 42 条。基于作者全文复核[连续 SE(3) 样条](https://arxiv.org/html/2603.25058)、[MoSca](https://arxiv.org/html/2405.17421)、[GauSTAR](https://arxiv.org/html/2501.10283)、[PointWorld](https://arxiv.org/html/2601.03782)及[图网络物理模拟正式记录](https://proceedings.mlr.press/v119/sanchez-gonzalez20a.html)，说明已有实现依据。证据权重、关联及门控、历史存在门控和连续响应公式用于展开拟研究设计，未作为原论文已经验证的统一流程或本课题已完成成果。图 10–14 全部为原创可编辑机制示意，不使用他人结果充作本课题实验，也不增加未核实发表条目。

3.3 补充完成时实际引用 44 条；后续扩充后的当前数量及逐条记录见上表。文献表独立置于报告末尾第四部分，按全文首次引用顺序生成；保留旧库未使用条目，但不以未引用条目增加列表。以下旧稿记录仅供追溯。

2026-10-27 撰写 3.1“主要理论及研究方法”，复用库中已核实的 `probrobotics2005`，说明状态空间建模和贝叶斯预测—更新的通用基础，实际引用由 41 条增至 42 条。该书为 MIT Press 2005 年正式出版专著，作为经典理论来源使用，不属于旧未发表文章。其余引用均复用前两部分已有条目，原有 41 条首次引用编号保持不变。共同状态和可变结构记法用于描述本课题对象；连续轨迹、观测残差加先验、刚体距离不变性及贝叶斯滤波关系作为已有理论形式说明，各项拟研究机制分别表述，不将通用公式作为本课题原创成果。

本轮复核采用一手来源：[MIT Press 专著信息](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/)、[连续 SE(3) 样条作者摘要及 CVPR 2026 录用说明](https://arxiv.org/abs/2603.25058)、[MoSca 作者全文](https://arxiv.org/html/2405.17421)、[HyperNeRF 作者项目](https://hypernerf.github.io/)、[GauSTAR 作者全文](https://arxiv.org/html/2501.10283)、[PlaNet 正式论文集](https://proceedings.mlr.press/v97/hafner19a.html)、[图网络物理模拟正式论文集](https://proceedings.mlr.press/v119/sanchez-gonzalez20a.html)。同胚形变的拓扑保持仅用于其适用假设，不泛化为全部连续场均不能表达拓扑变化；图元或网格增加不直接等同于真实物理表面新生；标准滤波形式不作为本课题已实现精确后验推断的证据。

2026-10-26 在 1.2 三个主题分别加入重建结果、交互预测及动作学习示意图，复用已有的 `shapeofmotion2025`、`retimegs2026`、`ref06`、`openvla2025`、`dreamzero2026`，不新增书目或改变发表状态。来源段落放在相关论文首次介绍之后，实际引用仍为 41 条，首次出现顺序保持不变。素材来自对应作者项目及 PointWorld 作者 PDF Figure 16，当时的素材来源、提取位置和校验记录可通过 Git 历史追溯。RetimeGS 中间图为观测区间内插值；PointWorld 预测和参考标注来自同一案例、同一时域，参考标注不充作模型结果；动作学习图的三幅照片为各自工作的独立场景示例。

2026-10-26 本次重构第二部分，增补 `se3bspline2026`、`usplat4d2026` 两条正式会议论文，实际引文由 39 条增至 41 条。第一项承认连续轨迹、自适应运动表达及不确定性传播已有直接基础，进一步提出观测置信度、有效时间范围及表达自由度的研究思路。同步在 1.2.1 补充领域比较，未新增预印本，四个科学问题名称保持不变。

本次事实核查使用一手来源：[SE(3) B 样条正式记录](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Learning_Explicit_Continuous_Motion_Representation_for_Dynamic_Gaussian_Splatting_from_CVPR_2026_paper.html)、[作者全文](https://arxiv.org/html/2603.25058)、[USplat4D 正式记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/26300457961c3e056ea61c9d3ebec2a4-Abstract-Conference.html)、[RetimeGS 作者第 5 节及附录 B、C.8](https://arxiv.org/html/2603.13783v1)、[Shape of Motion 作者第 5 节](https://arxiv.org/html/2407.13764)、[GauSTAR 作者第 5 节](https://arxiv.org/html/2501.10283)、[AT-GS 作者方法及结论](https://arxiv.org/html/2411.06602)、[GWM 作者第 3.2 节](https://arxiv.org/html/2508.17600)、[PointWorld 作者附录 A.1](https://arxiv.org/html/2601.03782)。论文报告的限制只用于相应方法及条件，本课题拟研究机制和预期收益不作为原论文已经证明的结论。

2026-10-26 按用户要求将文献表从第一部分末尾移至第三部分之后，恢复独立的第四部分。实际引用仍为 39 条，文献条目及全文首次引用顺序保持不变。

2026-10-26 配合 1.1 六段结构重写 1.2。实际引用仍为 39 条，未增删书目；因图 1 和学习式三维感知的引入前移，首次引用编号重新生成。1.2 增加已有 PhysTwin 的 RGB-D 输入、质点弹簧模型及给定控制点运动下的预测说明，区分其物理重建路线和本文连续状态的整体目标。再次核对基金委通告、MonST3R、CUT3R、PhysTwin、GWM、PointWorld、PERSIST 及 DreamZero 的一手资料；RetimeGS 的低采样率及大位移限制依据作者论文及补充材料，不作为所有连续时间方法的共同局限。未将预印本改记为正式发表。

本轮方法事实复核来源：[基金委通告](https://www.nsfc.gov.cn/p1/3381/2824/142425.html)、[MonST3R 作者项目](https://monst3r-project.github.io/)、[CUT3R 作者项目](https://cut3r.github.io/)、[PhysTwin 作者项目](https://jianghanxiao.github.io/phystwin-web/)、[GWM 作者全文](https://arxiv.org/html/2508.17600)、[PointWorld 作者全文附录 A.1](https://arxiv.org/html/2601.03782)、[PERSIST 正式摘要](https://proceedings.mlr.press/v306/garcin26a.html)、[RetimeGS 补充材料](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Wang_RetimeGS_Continuous-Time_Reconstruction_CVPR_2026_supplemental.pdf)、[DreamZero 作者预印本](https://arxiv.org/abs/2602.15922)。

2026-10-25 重新设计 1.1 背景图，新增 PhysTwin 的 ICCV 2025 正式论文作为图源。作者、题名、年份和 7219–7230 页由 CVF 正式出版记录核对；图中原始图像从作者公开 PDF 内嵌对象提取，当时的来源映射和校验记录可通过 Git 历史追溯。Figure 3、Figure 9 的同一布料案例分别提供建模区间观测、多视角模型渲染及留出未来预测，真实未来参考单独标识。动态图的概念曲线及观测更新箭头不作为该论文已经实现连续状态更新的证据。实际引用增加为 39 条，未新增预印本。

2026-10-25 暂定题目调整为“连续动态世界模型的构建方法研究”，同步修改总体定位、研究内容及图示。沿用当前 38 条引用和既有方法事实，本轮不新增书目，也不将文献的连续时间表达、持续观测更新和动作条件预测混为同一能力；发表状态沿用下述既有核查记录。

2026-10-25 按总分总重写 1.1，保留基金委通告作为背景依据，并复用 DreamerV3 说明环境预测参与行为学习。全部实际引用仍为 38 条；因 DreamerV3 首次引用前移，同步调整 1.2 的一处组内引文顺序。书目及发表状态沿用既有核查，不新增文献。

2026-10-24 将 1.2 重组为“四维动态场景重建—面向交互的世界模型—具身操作中的动作学习”，调整代表工作的组织、比较和首次引用顺序，保留全部 38 条实际引用。本轮未新增文献，书目信息及发表状态沿用 2026-10-23 的核查。世界模型一节分别说明 TesserAct 的图像及任务指令条件、GWM 的历史状态及动作条件；动作学习一节讨论预测的使用及 DreamZero 的联合生成，不将几类建模目标混同。

2026-10-22 初稿引用 29 条正式论文，其中新增 10 条。2026-10-23 按四维重建及具身智能的领域脉络重组 1.1、1.2，保留原 29 条引用，重新启用已有库中的基金委通告、VLA 中文综述、RT-2 及 OpenVLA，新增 MonST3R、CUT3R、$\pi_0$、TesserAct 和 DreamZero 五条。优先核对 CVF、ICLR、PMLR、RSS 正式论文集。方法及能力边界由论文正文或作者全文复核，不能将正文中的本课题研究判断当作被引论文已经证明的共同局限。

基金委通告发布于 2026-09-18，公开页只说明专项名称及申请指南在科学基金网络信息系统发布；正文据此说明研究背景，不引用未获得的登录后指南细则。DreamZero 于 2026-02-17 提交 arXiv，本次未核定正式出版记录，保持 `@online` 及预印本编号，用于直接说明 WAM 联合建模未来视频与动作的形式。它属于近期代表性进展，不作为正式论文统计，也不据其特定实验推断 WAM 普遍优于 VLA。未启用旧库中的 WorldVLA 或 WAM 综述预印本来扩充引用数量。

| 文献库键 | 正式版本及用途 | 核查来源 |
| --- | --- | --- |
| se3bspline2026 | CVPR 2026：33291–33300；联合位置和朝向的连续 SE(3) B 样条运动，自适应运动基及控制点；作者、题名、年份和页码由正式记录核对 | [CVF 正式记录](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Learning_Explicit_Continuous_Motion_Representation_for_Dynamic_Gaussian_Splatting_from_CVPR_2026_paper.html)、[作者全文](https://arxiv.org/html/2603.25058) |
| usplat4d2026 | ICLR 2026；时变不确定性及运动信息传播，用于说明观测置信度已有研究基础；作者、题名、年份由正式论文集核对 | [ICLR 正式记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/26300457961c3e056ea61c9d3ebec2a4-Abstract-Conference.html) |
| phystwin2025 | ICCV 2025：7219–7230；用于图 1 同一布料案例的历史观测、三维渲染、留出未来预测和真实执行参考；不将其内部方法或更新能力等同于本课题范式 | [CVF 正式记录](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html)、[作者全文](https://arxiv.org/pdf/2503.17973)、[项目页](https://jianghanxiao.github.io/phystwin-web/) |
| nsfcworldmodel2026 | 2026-09-18 基金委信息科学部公开通告；仅用于研究背景 | [官方通告](https://www.nsfc.gov.cn/p1/3381/2824/142425.html) |
| cnvla2026 | 自动化学报 52(1)：18–51，2026；具身操作及 VLA 发展背景 | [期刊记录](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250394) |
| rt22023 | CoRL，PMLR 229：2165–2183，2023；预训练视觉语言知识进入动作模型 | [正式版本](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| openvla2025 | CoRL，PMLR 270：2679–2713，2025；开放 VLA 及任务微调；年份采用正式论文集年份 | [正式版本](https://proceedings.mlr.press/v270/kim25c.html) |
| monst3r2025 | ICLR 2025；动态逐时刻点图及几何恢复，区分预测和后续对齐 | [正式版本](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ce1710ff5b66f89b0d707bf1ec2850bf-Abstract-Conference.html)、[作者项目](https://monst3r-project.github.io/) |
| cut3r2025 | CVPR 2025：10510–10522；持续循环状态及三维点图读取，支持静态和动态内容；不据“continuous updating”推断显式连续时间运动 | [正式记录](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Continuous_3D_Perception_Model_with_Persistent_State_CVPR_2025_paper.html)、[作者全文](https://arxiv.org/abs/2501.12387) |
| d4rt2026 | CVPR 2026：7382–7392；统一查询接口同时给出深度、时空对应和相机参数，用于说明重建与跟踪的联系；最佳论文以官方公告为据，不据此扩展方法能力 | [正式记录](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html)、[最佳论文公告](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) |
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

PointWorld 的静态初始状态限制以[作者全文附录 A.1](https://arxiv.org/html/2601.03782)为依据，不泛化为其他模型的限制；该方法已有部分观测及物体性研究。GauSTAR 和 AT-GS 作为已有局部表面更新参考，不将其文献中的所有拓扑变化自动解释为真实切割、撕裂。前期 CoFuse4D、PS-VLA 的说明沿用归档及工作文档，仅描述探索基础；两项工作按用户说明注明尚未发表、计划投稿至 CVPR 2027，未据此改写文献核查或引用。

## 归档旧稿的历史核查记录

以下记录对应于 2026-10-22 之前的旧稿（存档于标签 `20261028v1` 的 Git 历史中），保留供文献库维护和复核。下述 87 条数量及引用分布均指旧稿。

核查日期：2026-10-09，增补日期：2026-10-12、2026-10-13、2026-10-15、2026-10-18、2026-10-20。范围：归档旧稿实际引用的 87 条文献，其中中文 7 条、英文 80 条。优先核对会议论文集、出版社页面及其书目元数据；未找到正式出版记录时再核对作者项目页和 arXiv。以下链接仅供维护与复核，报告参考文献列表统一隐藏 URL、访问日期，保留 DOI。

8 条原先按预印本引用的论文已改为正式出版版本。LiveWorld 已确认被 ECCV 2026 录用，但本次未找到正式卷页及 DOI，单独注明录用状态。V-JEPA 2、3D-Belief 和 BridgeVLA++ 未查到正式出版记录，继续注明预印本身份。本记录只核查书目信息与发表状态，不能替代对实验协议和结论的深入阅读。

此前综述扩充新增 23 条文献：6 条中文正式期刊文章、17 条英文正式会议论文。2026-10-12 另增补 2 条英文研究文献与 1 条中文政策公告。新增引用分别落实到背景、状态基础、特征预测、动态三维表示、预测不确定性和机器人操作的论述中，未通过未引用条目扩充列表。代表工作比较表中，每个代表工作名称后均标注对应文献，并补充持续高斯/稀疏运动控制和三维操作两个比较条目。中文文献按原文语言著录；PerAct 与 OpenVLA 的年份采用 PMLR 正式论文集年份 2023、2025，与会议举行年份区分。

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
| cotracker2024 | CoTracker | ECCV 2024，Springer 论文集引用年份为 2025，LNCS 15120：18–35；论文 2024 年先在线发表。确认六位作者、卷页及 DOI，说明多点联合跟踪。 | [Springer](https://link.springer.com/chapter/10.1007/978-3-031-73033-7_2) |
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
