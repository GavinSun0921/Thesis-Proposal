# 开题研究主线收敛草案

> 状态：working draft  
> 更新时间：2026-09-26  
> 当前原则：从“空间智能 / World Model”大框架中进一步收窄，形成一个正常博士开题规模的核心问题。

## 1. 当前题目

### 首选

**面向不完全观测的动态场景时空状态表征与演化研究**

相较上一版“面向空间智能的动态场景时空状态表征与演化建模研究”，本版主动收窄：

- 删除“面向空间智能”这一上位领域限定；
- 把“不完全观测”提升为核心问题条件；
- 研究对象固定为“动态场景时空状态”；
- 研究任务集中在“状态表征 / 恢复”和“状态演化”；
- Prediction / Interaction 作为后续递进研究，而不是与前两项并列的巨大方向；
- World Model 仅作为长期可能落点。

### 备选 1：进一步收窄

**动态场景的时空状态表征与连续运动建模研究**

如果导师希望开题更偏传统 Computer Vision，这一版本最稳。它几乎完全围绕当前 Pomelo4D 展开，但对后续 VLA / embodied interaction 的容纳能力较弱。

### 备选 2：长期 umbrella

**面向空间智能的动态场景时空状态表征与演化建模研究**

可作为博士论文最终 umbrella 或专项语境下的表述，但当前不建议作为正式开题首选。

---

## 2. 研究边界：只研究一个核心对象

本开题不以以下方式组织：

\`\`\`text
4D Reconstruction
+ VLA
+ World Model
\`\`\`

因为这会形成三个规模都很大的平行方向。

当前只保留一个核心研究对象：

> **不完全观测下的动态场景时空状态。**

所有研究内容围绕这一对象递进展开：

\`\`\`text
Observation
    ↓
State Recovery
    ↓
State Evolution
    ↓
State Prediction / Interaction
\`\`\`

因此，Pomelo4D 与 BridgeVLA-Sequence 不再被描述成两个同等独立的博士方向，而是当前研究主线中处于不同阶段的工作基础。

---

## 3. 一句话科学问题

> **在遮挡、噪声、观测缺失和深度误差等不完全观测条件下，如何构建紧凑、几何一致且可持续更新的动态场景时空状态，并描述其随时间及交互过程的演化？**

统一形式：

\`\`\`math
S_t = U(S_{t-1}, z_t),
\`\`\`

\`\`\`math
S_{t+\Delta} = F(S_t, a_t, \Delta),
\`\`\`

其中：

- \(z_t\)：当前可获得但可能不完整、含噪的观测；
- \(S_t\)：动态场景的时空状态；
- \(U\)：状态估计或 observation update；
- \(F\)：状态演化模型；
- \(a_t\)：可选的交互动作，纯 reconstruction 问题中可以为空；
- \(\Delta\)：连续或离散时间间隔。

这里不预先要求 \(S_t\) 必须是某一种固定表示。当前主要研究两种相关形式：

1. **显式几何 / 运动状态**：可被三维查询、渲染和几何评测；
2. **潜在预测状态**：由历史观测与动作维护，用于预测或决策。

但开题的主要方法基础仍以第一类为主，第二类作为后续延伸与已有探索。

---

## 4. 三个递进研究问题

### RQ1：不完全观测下，动态场景状态如何可靠恢复？

核心困难：

- occlusion；
- correspondence drift；
- depth uncertainty；
- missing observation；
- dense observation 中存在大量冗余或错误信息；
- 状态需要同时满足 compactness、geometry consistency 和 queryability。

建议表述：

> **如何从存在遮挡、漂移、噪声和深度误差的多时刻观测中，恢复紧凑、几何一致且可查询的动态场景时空状态？**

这是当前最明确、最成熟的问题，对应 Pomelo4D 的主要研究基础。

---

### RQ2：动态场景状态如何随连续时间稳定演化？

核心困难：

- 离散观测与连续物理运动之间存在表征间隙；
- 遮挡或缺测期间缺少直接监督；
- 局部轨迹误差可能随时间累积；
- 状态演化既要保持 temporal consistency，也要尊重空间结构约束。

建议表述：

> **如何建立连续时间状态演化模型，使动态场景状态在稀疏观测、遮挡和缺测条件下保持时间连续性与空间一致性？**

这与 RQ1 是自然递进关系，而不是另起一个方向。

---

### RQ3：恢复出的时空状态能否支持预测与交互任务？

这一问题在开题中需要主动控制规模。

不表述为：

> 构建统一空间世界模型，实现长期物理预测和智能决策。

而表述为：

> **如何利用时空状态的历史信息和演化结构，提高未来状态预测或部分可观测交互任务中的状态估计能力？**

当前可以从两个较弱、可验证的方向进入：

1. future geometric / visual state prediction；
2. partially observable embodied control 中的 predictive latent state。

BridgeVLA-Sequence 是这一问题的已有探索，而不是要求博士课题再完整解决一套 VLA。

---

## 5. 三项研究内容

## 5.1 研究内容一：不完全观测下的动态场景状态恢复

### 目标

从含噪 dense observation 中恢复有限自由度、几何一致的动态状态。

### 当前技术问题

- 如何使用 dense correspondence，而不是先将大量非节点观测压缩丢弃；
- 如何处理 visibility / confidence / depth error；
- 如何避免 correspondence noise 直接污染 motion state；
- 如何在有限 state complexity 下保持复杂运动表达能力。

### 主要验证

- 2D / 3D trajectory accuracy；
- geometry consistency；
- missing / occluded observation recovery；
- dynamic reconstruction；
- NVS。

### 当前基础

**Pomelo4D。**

当前主线可概括为：

\`\`\`text
dense noisy correspondence
        ↓
uncertainty-aware observation fusion
        ↓
sparse motion state
        ↓
3D dynamic state
\`\`\`

---

## 5.2 研究内容二：动态场景状态的连续时间演化建模

### 目标

研究如何从有限时刻观测得到可查询的连续时间动态状态。

### 当前技术问题

- discrete frames 如何约束 continuous motion；
- 如何利用 sparse temporal support 表达复杂动态；
- 缺测时段如何保持合理轨迹；
- 如何约束位置、旋转、局部结构和长期 temporal consistency。

### 当前实现基础

Pomelo4D 中当前使用 temporal GP 作为时间建模工具，并保留 MoSca scaffold、topology 与 DQB query。

需要强调：

> GP 不是博士课题本身；“连续时间状态演化”才是研究问题。

未来可以替换为其他 continuous-time / trajectory representation，只要围绕同一科学问题。

### 关键证据缺口

当前最重要的不是继续堆模型，而是完成：

1. motion improvement → NVS transfer；
2. held-out / intermediate-time validation；
3. matched multi-scene protocol；
4. 必要的 seed / robustness 验证。

只有这些成立后，才能较强地支撑“连续状态演化改善动态重建”的 claim。

---

## 5.3 研究内容三：时空状态的预测建模与交互应用

这一项是前两项的延伸，范围故意保持较弱。

### 目标

研究恢复和维护的状态是否对未来观测、未来状态或交互决策具有预测价值。

不要求在博士开题阶段承诺：

- 完整 World Model；
- long-horizon imagination；
- 通用 VLA；
- 物理属性全量建模；
- multi-physics simulation。

### 当前已有探索：BridgeVLA-Sequence

当前实现：

\`\`\`math
y_t = F_\phi(y_{t-1}^+,u_{t-1}),
\`\`\`

\`\`\`math
y_t^+ = U_\omega(y_t,H_t),
\`\`\`

并加入：

\`\`\`math
\hat r_t = D_\eta(y_t),
\`\`\`

使历史 prior state 对当前视觉 representation 具有预测约束。

它可以作为以下问题的已有证据：

> 在 partial observability 下，显式维护一个 predictive state 是否比独立逐帧决策更有用？

但当前不能据此声称：

- hidden state 等价于真实物理状态；
- 已建立完整 environment dynamics；
- 已实现稳定 long-horizon rollout；
- 已形成完整 World Model。

### 后续可选方向

优先从弱约束开始，而不是直接做大：

\`\`\`text
latent state
    ↓
future visual / geometric representation
\`\`\`

例如：

- future depth；
- tracks / keypoints；
- occupancy；
- object-centric spatial state；
- compact geometric features。

如果这些方向获得可靠证据，再进一步讨论 action-conditioned spatial-state prediction。

---

## 6. 当前两项工作的关系

| 维度 | Pomelo4D | BridgeVLA-Sequence |
|---|---|---|
| 状态形式 | explicit geometric / motion state | latent predictive state |
| 主要问题 | state recovery + continuous evolution | partial observability + state prediction |
| 输入 | RGB / depth / correspondence | observation / language / history / action |
| 主要验证 | motion / geometry / NVS | manipulation success |
| 在开题中的地位 | **核心方法基础** | **后续预测/交互探索基础** |

因此当前不再使用“两条并列主线”的表述。

更准确的是：

> Pomelo4D 是当前博士开题的核心方法基础；BridgeVLA-Sequence 说明同一个“state under partial observation”问题可以进一步延伸到预测与交互。

这样可以避免为了包住已有工作而把开题题目无限放大。

---

## 7. Spatial Intelligence / World Model 在开题中的位置

### 作为背景

可以在“研究背景与意义”中说明：

- 空间智能需要 agent 对动态环境建立持续的内部状态；
- 单帧 perception 不足以支持遮挡恢复、动态理解和连续交互；
- World Model 等近期方向进一步强调 predictive state representation。

这些用于说明问题的重要性。

### 不作为当前研究承诺

开题不直接承诺：

\`\`\`text
完整 Spatial Intelligence
完整 World Model
通用 embodied agent
物理规律统一建模
\`\`\`

World Model 在当前框架中的位置更接近：

\`\`\`text
Dynamic State Representation
        ↓
State Evolution
        ↓
Predictive State
        ↓
potential future direction:
Spatial World Model
\`\`\`

而不是反过来先定一个 World Model 大题目，再向里面填现有工作。

---

## 8. 与“空间智能与世界模型”专项申请的关系

老师当前专项中的“物理世界时空状态表征及演化机理”可以作为上位背景，但个人博士课题只取其中与已有工作直接相关的部分。

### 可以自然对齐

- 动态空间几何；
- 时空观测；
- 非完全观测下状态恢复；
- 状态随时间演化；
- 遮挡和缺测；
- 后续的预测与交互。

### 当前不进入个人开题核心范围

- 材质、质量、刚度、摩擦等完整 physical attributes；
- 多物理场耦合；
- 因果机理发现；
- 复杂物理规律统一建模；
- 长时间尺度通用世界模拟。

参与专项申请与个人博士题目不需要一一等价。

---

## 9. 开题的建议故事线

正式报告尽量避免从技术名词出发：

\`\`\`text
4DGS → VLA → World Model
\`\`\`

而从问题出发：

### Step 1：现实动态环境天然是不完全观测的

原因包括：

- 遮挡；
- 视角限制；
- tracking error；
- depth uncertainty；
- temporal sampling；
- interaction 中无法直接访问真实环境状态。

### Step 2：需要维护一个跨时间的动态状态

这个状态应同时满足：

- compact；
- geometrically consistent；
- temporally persistent；
- queryable / predictable。

### Step 3：首先解决“恢复”

\`\`\`text
noisy observation → state
\`\`\`

对应 Pomelo4D。

### Step 4：再解决“演化”

\`\`\`text
state(t) → state(t + Δt)
\`\`\`

对应 continuous motion modeling。

### Step 5：最后验证这种状态是否对预测与交互真正有用

\`\`\`text
state/history → future observation/state/action
\`\`\`

这里再引入 BridgeVLA-Sequence。

这样三项内容是递进关系，而不是三个并列研究方向。

---

## 10. 当前已有证据与边界

## 10.1 Pomelo4D

当前已有：

- matched multi-scene Stage-1 motion evidence；
- complete-input single-scene soft-anchor evidence；
- track coverage / filtering / scaffold 等 diagnostic；
- 可复现 pipeline 与 evaluation contract。

仍缺：

- NVS transfer；
- held-out non-integer / intermediate-time 证据；
- 更严格的 multi-scene matched validation；
- 必要的 repeated-run robustness。

因此近期继续优先补这些，而不是再扩方法边界。

## 10.2 BridgeVLA-Sequence

当前已有：

- token-only hidden-state sequence route；
- prior-observation prediction；
- RLBench 18-task five-run evaluation；
- 当前单 checkpoint / 单 loss weight 下观察到小幅性能改善。

仍缺：

- matched \(\lambda_{\mathrm{obs}}=0\) 对照；
- multiple training seeds；
- sequence sampling / hidden state / route-only 的 factorized ablation；
- teacher-forcing 与 rollout state distribution shift 分析；
- latent state 与真实 spatial / geometric state 的 grounding。

因此它目前作为研究内容三的 preliminary exploration 更合理。

---

## 11. 开题前一个月的执行计划

### Week 1：确定研究问题和标题

产出：

- 当前主标题；
- 两个备选标题；
- 一句话科学问题；
- 3 个 RQ；
- 3 项研究内容；
- 明确已有工作与 planned work 的边界。

本文即为当前第一版。

### Week 2：建立 evidence map

分别整理 Pomelo 与 Bridge：

\`\`\`text
Problem
→ Assumption
→ Method
→ Evidence
→ Missing Evidence
→ Decisive Next Experiment
\`\`\`

重点是证据链，不是论文式包装。

### Week 3：补最关键实验

Pomelo：

1. NVS transfer；
2. held-out / intermediate-time；
3. matched multi-scene；
4. 必要的 robustness。

Bridge：

1. prior-observation matched weight=0；
2. training seed；
3. factorized ablation；
4. rollout mismatch。

### Week 4：形成导师讨论稿

先做 5–8 页即可：

1. 问题背景：dynamic scene + incomplete observation；
2. 核心科学问题；
3. 统一 state formulation；
4. RQ1：state recovery；
5. RQ2：state evolution；
6. RQ3：prediction / interaction；
7. 已有工作与 evidence gaps；
8. 博士阶段计划。

---

## 12. 与导师讨论时的版本

可以暂时这样表达：

> 我的开题现在不想直接写成“空间智能”或者“世界模型”，因为范围会过大。我希望先收敛到“不完全观测下动态场景时空状态的表征与演化”。核心问题是：面对遮挡、跟踪误差、深度误差和观测缺失，如何恢复一个几何一致、可持续更新的动态状态，并建模它随时间的演化。Pomelo4D 是当前状态恢复和连续运动建模的主要基础；BridgeVLA 是我对 partial observability 下 predictive state 的已有探索，放在第三项预测与交互应用中，而不是单独再开一个 VLA 大方向。Spatial Intelligence 和 World Model 作为背景和后续落点。

与导师优先确认三个问题：

1. **“不完全观测下动态场景时空状态”是否可以作为博士论文统一研究对象？**
2. **前两项是否以 reconstruction / continuous motion 为主，第三项只做预测与交互延伸？**
3. **正式题目是否用“面向不完全观测的动态场景时空状态表征与演化研究”？**

---

## 13. 当前结论

当前建议的规模控制为：

\`\`\`text
             Incomplete Observation
                     ↓
          Dynamic Spatiotemporal State
               /             \
              /               \
       State Recovery     State Evolution
              \               /
               \             /
           Prediction / Interaction
             (limited extension)
\`\`\`

其中：

- **状态恢复**和**状态演化**是博士开题的核心；
- **预测与交互**是递进的第三项研究，而不是另一个完整研究领域；
- Spatial Intelligence 是背景；
- World Model 是可能的长期落点。

一句话概括：

> **论文愿景可以面向空间智能，但当前博士研究承诺聚焦于不完全观测下动态场景状态的恢复、演化与有限预测。**
