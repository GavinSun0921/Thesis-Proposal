# 开题研究主线收敛草案

> 状态：working draft  
> 更新时间：2026-09-25  
> 目的：在正式开题前，先收敛博士阶段的上位科学问题，避免将 4D Reconstruction、VLA、World Model 作为彼此割裂的技术方向简单拼接。

## 1. 当前建议题目

### 首选

**面向空间智能的动态场景时空状态表征与演化建模研究**

这个题目的边界相对合适：

- “空间智能”给出总体背景，但不要求当前已经实现完整 World Model；
- “动态场景”限定研究对象；
- “时空状态”统一显式几何状态与潜在预测状态；
- “表征与演化”覆盖当前 Pomelo4D 与 BridgeVLA-Sequence 两条已有工作；
- 后续可以自然延伸到 future prediction、embodied interaction 和 spatial world model。

### 备选 1：更偏传统 Computer Vision

**复杂动态场景的连续时空状态表征与运动建模研究**

优点是问题更具体、风险较低；缺点是后续 VLA / embodied interaction 放入整体论文时需要额外解释。

### 备选 2：更偏 World Model

**面向物理世界模型的动态场景状态表征、估计与演化研究**

暂不建议作为当前首选。原因不是方向不成立，而是当前已有工作还没有充分证明：

- action-conditioned latent state 可以稳定 long-horizon rollout；
- hidden state 对应可解释或可验证的 physical / geometric state；
- future-state prediction 在更长期尺度具有可靠性；
- 当前方法已经形成完整的 world model，而不是具有部分 world-model-like properties 的状态估计模块。

因此现阶段更适合把 **World Model 作为长期落点**，而不是作为开题时已经成立的核心 claim。

---

## 2. 一句话科学问题

> **在不完全、含噪的时空观测下，如何构建能够恢复动态场景、描述其连续演化，并进一步支持预测与交互决策的时空状态表示？**

这一问题可以用统一状态模型表达：

```math
S_t = U(S_{t-1}, z_t),
```

```math
S_{t+Delta} = F(S_t, a_t, Delta),
```

其中：

- (z_t)：当前可获得的观测，例如 RGB、depth、correspondence、point cloud、视觉 token 等；
- (S_t)：模型内部对当前动态场景的状态表示；
- (U)：observation update / state estimation；
- (a_t)：可选的 agent action；纯 reconstruction 场景中可以为空；
- (F)：状态演化模型；
- (Delta)：连续或离散时间间隔。

博士课题不需要预先假设 (S_t) 必须只有一种形式。当前两条工作恰好对应两类互补状态：

1. **explicit geometric state**：能够被三维查询、渲染和几何验证；
2. **latent predictive state**：由历史观测和动作维护，用于预测与决策。

---

## 3. 当前已有工作的统一解释

## 3.1 Pomelo4D：显式时空状态恢复与连续运动

当前项目：

- [Pomelo4D-v0 / exp/mosca-submodule-baseline](https://github.com/GavinSun0921/Pomelo4D-v0/tree/exp/mosca-submodule-baseline)
- [当前研究主线文档](https://github.com/GavinSun0921/Pomelo4D-v0/blob/exp/mosca-submodule-baseline/docs/dense_correspondence_motion_field_research.md)

当前核心问题不是泛化的“做 4DGS”，而是：

> 如何用有限的运动状态，融合含遮挡、漂移和深度误差的 dense correspondence，恢复可查询且更准确的三维运动？

当前方法可以抽象为：

```text
noisy / incomplete observations
        ↓
sparse motion states
        ↓
continuous-time motion model
        ↓
3D motion query / dynamic reconstruction
```

当前实现保留 MoSca 的节点、拓扑和局部 DQB 查询，对节点时间运动与观测融合进行改造。研究变量包括：

- dense correspondence；
- visibility / reliability；
- tracker confidence；
- depth uncertainty；
- sparse motion degrees of freedom；
- continuous-time motion；
- geometry / motion consistency。

因此，这条线在博士课题中可以定义为：

> **不完全观测条件下的显式时空状态恢复与连续演化建模。**

### 当前已有证据

按照当前仓库记录：

- 历史 matched 7 场景 Stage-1 结果支持 GP motion 相对原生 MoSca 的整体 motion 指标改善；
- complete-input spin 上 soft anchor 出现进一步 motion 增益；
- 已建立针对 track coverage、filtering、scaffold compression、PCK 等较完整的诊断与实验路径。

### 当前不能过度外推的结论

现有证据还不足以声称：

- motion 指标改善已经稳定传递到 NVS；
- 连续时间建模已经被 non-integer / held-out time ground truth 充分验证；
- 单场景 soft-anchor 最优超参数可以跨场景直接泛化；
- 当前结果具有充分的多训练 seed 统计显著性。

因此，Pomelo 当前最重要的近期任务仍然是：

> **固定后续 MoSca pipeline，仅改变 motion stage，验证 motion improvement 是否向 NVS / held-out-time reconstruction 传递。**

---

## 3.2 BridgeVLA-Sequence：潜在预测状态与动作条件演化

当前项目：

- [BridgeVLA-Sequence / dev-gavinsun](https://github.com/npucvr/BridgeVLA-Sequence/tree/dev-gavinsun)
- [概率机器人建模文档](https://github.com/npucvr/BridgeVLA-Sequence/blob/dev-gavinsun/docs/bridgevla_probabilistic_robotics_model.md)
- [Prior-observation 实验报告](https://github.com/npucvr/BridgeVLA-Sequence/blob/dev-gavinsun/docs/bridgevla_prior_observation_prediction_eval_report.md)

原始 BridgeVLA 可以抽象成 POMDP 中的 observation-to-action policy。当前扩展增加了历史状态：

```math
y_t = F_phi(y_{t-1}^+, u_{t-1}),
```

```math
y_t^+ = U_omega(y_t, H_t),
```

```math
widetilde H_t = H_t + A_psi(H_t, y_t^+),
```

```math
u_t sim pi_	heta(u_t mid widetilde H_t).
```

其中：

- (y_t)：吸收当前观测前的 predictive prior state；
- (H_t)：当前视觉表征；
- (y_t^+)：observation update 后的 posterior-like hidden state；
- (F_phi)：action-conditioned state transition；
- (U_omega)：observation update；
- (A_psi)：用 hidden state 对 visual tokens 进行 residual correction。

进一步加入 prior-observation prediction：

```math
hat r_t = D_eta(y_t),
```

要求历史形成的 prior state 对当前视觉表征具有预测能力。

因此，这条线在博士课题中可以定义为：

> **面向交互决策的潜在时空状态估计、预测与动作条件演化。**

### 当前已有证据

当前仓库中的完整 RLBench 评测记录显示：

- token-only hidden-state route 在部分训练预算下相对本地官方 baseline 有小幅改善；
- prior-observation 路线在当前单一训练配置中达到约 (89.24%) 的 18-task 五轮平均成功率；
- 对应本地复测 baseline 约为 (87.38%)；
- 当前实验只更新少量新增模块，BridgeVLA / PaliGemma 主体保持冻结。

这些结果说明：

> predictive hidden state 可以与原有 action policy 共存，并可能改善部分需要时序记忆或多阶段组织的任务。

### 当前不能过度外推的结论

现有结果还不能证明：

- hidden state 已恢复 simulator true state；
- hidden state 等价于物理世界中的真实状态；
- 性能提升完全由 hidden state 本身造成，而不是 sequence sampling、冻结策略等因素；
- 已经实现稳定的 long-horizon world-model rollout；
- 单个训练 checkpoint 的五轮 evaluation variance 可以代表 training-seed variance；
- prior-observation loss 已通过 matched (lambda=0) 同预算实验严格隔离因果效果。

因此这一工作当前更准确的表述是：

> **predictive latent-state modeling for partially observable embodied control**，

而不是直接声称已经构建完整 World Model。

---

## 4. 两条已有工作之间真正的共同问题

两条工作可以统一成“状态”问题，但状态形式不同：

| 维度 | Pomelo4D | BridgeVLA-Sequence |
|---|---|---|
| 状态形式 | explicit geometric / motion state | latent predictive state |
| 主要输入 | RGB、depth、correspondence | observation、language、history、action |
| 主要困难 | 遮挡、漂移、深度误差、缺测 | partial observability、history dependency |
| 状态更新 | observation fusion / optimization | observation update |
| 状态演化 | continuous-time motion | action-conditioned transition |
| 主要验证 | geometry、motion、NVS | manipulation success |
| 主要作用 | reconstruction | prediction / decision |

共同的科学问题不是某一种具体模型结构，而是：

> **在不完整观测下，什么样的时空状态既能够准确解释当前动态世界，又能够支持未来状态演化与下游任务？**

这也是开题时最值得强调的主线。

---

## 5. 建议的三个研究问题

### RQ1：动态场景状态如何从不完整、不可靠观测中恢复？

核心关注：

- geometry consistency；
- correspondence uncertainty；
- depth uncertainty；
- occlusion / missing observation；
- sparse state vs. dense observation；
- 状态表示的可查询性与可验证性。

对应当前 Pomelo4D。

可表述为：

> 如何从存在遮挡、漂移、噪声与深度误差的多时刻观测中，构建紧凑、几何一致且可连续查询的动态场景状态？

---

### RQ2：时空状态应如何随时间和交互动作演化？

核心关注：

- continuous-time evolution；
- action-conditioned transition；
- observation update；
- state persistence；
- missing-data recovery；
- temporal consistency。

这是 Pomelo4D 与 BridgeVLA-Sequence 的交叉部分。

可表述为：

> 如何建立兼顾连续时间动态与交互动作影响的状态演化机制，使状态在长时间、遮挡和部分观测条件下保持一致性与预测能力？

---

### RQ3：显式空间状态与潜在预测状态如何建立联系，并服务预测与决策？

这是计划中的后续问题，目前还不是已经完成的结论。

潜在方向：

```math
y_t ightarrow 	ext{future depth / 3D keypoints / tracks / occupancy / object state},
```

或者：

```math
(y_t,a_t) ightarrow widehat S_{t+1}.
```

关键不是简单把 Pomelo 接到 BridgeVLA 前面，而是研究：

> latent state 是否能够被具有几何意义的 future-state supervision 约束，从而获得更可靠的 spatial grounding 与未来预测能力？

这部分如果最终成立，才会形成从 4D reconstruction 向 spatial world model 的方法级闭环。

---

## 6. 对应的三项博士研究内容

### 研究内容一：不确定观测驱动的显式动态场景状态恢复

目标：

- 从 dense but noisy correspondence 中保留有效观测；
- 以有限运动自由度描述复杂动态；
- 建立 observation uncertainty 与 sparse motion state 之间的融合机制；
- 在 held-out time / missing observation 条件下验证状态恢复能力。

预期支撑：

- motion accuracy；
- 3D trajectory accuracy；
- NVS；
- temporal interpolation / extrapolation；
- occlusion recovery。

当前基础：Pomelo4D。

---

### 研究内容二：部分可观测交互中的潜在预测状态建模

目标：

- 在 VLA policy 中维护 persistent latent state；
- 利用 observation update 和 action-conditioned transition 建模状态演化；
- 设计 predictive auxiliary objectives，使 hidden state 不只是 history cache，而具有可检验的未来预测能力；
- 研究时序状态对 multi-stage manipulation 的贡献。

预期支撑：

- matched baseline / ablation；
- multi training seed；
- rollout stability；
- long-horizon / memory-dependent tasks；
- teacher forcing vs. policy rollout 差异。

当前基础：BridgeVLA-Sequence。

---

### 研究内容三：几何约束的预测状态与空间世界模型

这一项作为博士后续计划，不在当前阶段假设已经解决。

目标可以逐步从弱到强：

1. latent state 预测更具有空间结构的 representation；
2. latent state 预测 future depth / correspondence / keypoint / occupancy；
3. 研究显式 3D/4D state 与 latent predictive state 的双向约束；
4. 再考虑 action-conditioned future spatial-state rollout。

如果做到这一层，博士论文可以自然形成：

```text
state recovery
    ↓
state evolution
    ↓
state prediction
    ↓
interaction / world modeling
```

---

## 7. 与“空间智能与世界模型”专项的关系

当前专项中“物理世界时空状态表征及演化机理”的表述，对博士课题最有价值的是提供一个上位问题，而不是要求把申请中的所有关键词都塞入个人开题。

### 与当前工作高度一致的部分

- 空间几何结构；
- 动态过程；
- 非完全观测下状态恢复；
- 时空观测与状态反演；
- 时空状态演化；
- 交互行为；
- 长期可进一步延伸到状态预测。

### 当前不应直接声称已经覆盖的部分

- 材质、质量、刚度、摩擦等明确 physical attributes；
- 多物理场耦合；
- 强因果机理辨识；
- 可验证的因果 world dynamics；
- 完整 long-horizon world model。

这些内容可以作为专项协作中的长期方向，但除非后续确实形成方法和实验，否则不建议写进博士开题题目或作为当前已完成基础。

---

## 8. 为什么不建议开第三条完全独立的 World Model 代码线

开题前最重要的任务不是同时做更多方向，而是证明已有研究可以被一个清晰的问题组织起来。

当前已经有：

- Pomelo4D：代码、实验、diagnostic、初步 motion evidence；
- BridgeVLA-Sequence：代码、sequence training、hidden-state modeling、完整 RLBench evaluation。

此时再单独启动第三个大型 World Model 项目，主要风险是：

1. 分散当前两条线尚未补齐的关键证据；
2. 开题时反而形成三个彼此独立的项目；
3. “World Model”容易成为概念标签，而不是由实验支持的问题；
4. 一个月后的题目讨论需要的是 abstraction 和 evidence map，而不是更多工程量。

更合适的顺序是：

> 先把 Pomelo 与 Bridge 中的“state”问题做扎实，再让第三项研究自然成为二者的连接，而不是重新开一个平行方向。

---

## 9. 开题前一个月的收敛计划

### Week 1：确定题目和统一问题

输出：

- 1 个主标题 + 2 个备选标题；
- 1 句话科学问题；
- 3 个 RQ；
- 3 项研究内容；
- 明确哪些属于已有成果，哪些属于 planned research。

当前本文已经完成第一版。

### Week 2：整理 evidence map

对两条现有工作分别整理一页：

**Pomelo**

```text
Problem
→ Assumption
→ Method
→ Evidence
→ Missing evidence
→ Next decisive experiment
```

**BridgeVLA**

同样使用这一结构。

重点不是堆实验数字，而是找到每一项工作的“决定性证据缺口”。

### Week 3：补关键实验，不扩大方法范围

Pomelo 优先级：

1. NVS transfer；
2. held-out / intermediate time；
3. multi-scene matched protocol；
4. 必要时补 seed / robustness。

Bridge 优先级：

1. prior-observation matched weight=0；
2. 多 training seed；
3. sequence / route / hidden-state factorized ablation；
4. teacher-forcing 与 rollout state mismatch。

### Week 4：形成第一次导师讨论稿

建议只准备约 5–8 页，而不是直接写完整开题：

1. 背景：Spatial Intelligence / dynamic world state；
2. 核心问题；
3. 统一状态建模框架；
4. Work I：explicit state；
5. Work II：latent predictive state；
6. Work III：future grounded predictive state；
7. 当前证据与关键缺口；
8. 博士阶段计划。

---

## 10. 与导师讨论时的简洁版本

可以用下面这段作为第一次讨论的核心表达：

> 我现在想把开题从具体的 4D Reconstruction 或 VLA 技术收敛到一个共同问题：不完全观测下，动态物理场景的时空状态应该如何表示、恢复和演化。目前 Pomelo4D 做的是显式几何状态和连续运动恢复，BridgeVLA 做的是交互过程中的 latent state update 和 action-conditioned transition。后续我希望进一步研究显式几何状态和 predictive latent state 的联系。因此暂时考虑题目叫“面向空间智能的动态场景时空状态表征与演化建模研究”，World Model 作为后续落点，而不是现在直接写进题目。

导师讨论时真正需要确认的不是具体模型结构，而是以下三个问题：

1. **博士论文是否可以以“时空状态”作为 Pomelo 与 VLA 的统一主线？**
2. **第三项工作是否应该明确走“geometry-grounded predictive state / spatial world model”的方向？**
3. **开题题目中是否保留“空间智能”，还是进一步收窄到“动态场景时空状态”？**

只要这三个问题得到导师确认，后续文献综述、开题结构和实验计划都会明显更容易收敛。

---

## 11. 当前结论

当前阶段建议保持：

```text
Spatial Intelligence
        ↓
Dynamic Spatiotemporal State
        ↓
┌───────────────────────────────┐
│  Explicit State Recovery      │  ← Pomelo4D
│  State Evolution              │
│  Predictive Latent State      │  ← BridgeVLA
│  Grounded Future Prediction   │  ← planned
└───────────────────────────────┘
        ↓
Reconstruction / Prediction / Interaction
        ↓
Towards Spatial World Models
```

最重要的边界是：

> **博士课题的核心是“状态表征、恢复、演化与预测”，World Model 是这条研究主线可能自然到达的结果，而不是现在为了概念完整性强行设定的起点。**
