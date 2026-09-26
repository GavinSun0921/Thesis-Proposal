# Thesis Proposal

本仓库用于整理博士开题的研究主线、科学问题、已有基础与后续计划。

## 当前建议题目

**面向不完全观测的动态场景时空状态表征与演化研究**

备选题目：

- **动态场景的时空状态表征与连续运动建模研究**：范围更窄，更偏 4D Reconstruction / Computer Vision。
- **面向空间智能的动态场景时空状态表征与演化建模研究**：保留为长期 umbrella，不作为当前开题首选。

当前原则是：**研究承诺收窄，长期愿景保留。**  
Spatial Intelligence 和 World Model 放在研究背景与长期目标中，不作为当前开题必须完成的范围。

## 核心科学问题

> 在不完全、含噪和存在遮挡的时空观测下，如何构建紧凑、几何一致且可持续更新的动态场景状态，并描述其随时间及交互过程的演化？

统一抽象为：

\`\`\`math
S_t = U(S_{t-1}, z_t),
\`\`\`

\`\`\`math
S_{t+\Delta} = F(S_t, a_t, \Delta),
\`\`\`

其中：

- \(z_t\)：不完整或含噪观测；
- \(S_t\)：动态场景的时空状态；
- \(U\)：状态估计 / observation update；
- \(F\)：状态演化模型；
- \(a_t\)：可选的交互动作；纯 reconstruction 场景中可以为空；
- \(\Delta\)：连续或离散时间间隔。

## 研究边界

当前开题只围绕一个研究对象：

> **不完全观测下的动态场景时空状态。**

三个递进问题为：

1. **状态恢复（State Recovery）**：从遮挡、漂移、深度误差和缺测观测中恢复几何一致的动态状态；
2. **状态演化（State Evolution）**：建模状态随时间变化，并处理连续时间、缺测和长期一致性；
3. **状态预测与应用（State Prediction / Utilization）**：研究状态在部分可观测交互任务中的预测作用与应用。

第三项是前两项的自然延伸，不等价于“构建完整 World Model”。

## 当前工作基础

### 1. Pomelo4D：显式状态恢复与连续运动

项目：[Pomelo4D-v0 / exp/mosca-submodule-baseline](https://github.com/GavinSun0921/Pomelo4D-v0/tree/exp/mosca-submodule-baseline)

当前关注：

- dense correspondence；
- 遮挡、漂移和 depth uncertainty；
- sparse motion state；
- geometry / motion consistency；
- continuous-time motion；
- held-out time / NVS transfer。

它是当前开题最直接、最扎实的研究基础，主要支撑 **状态恢复 + 状态演化**。

### 2. BridgeVLA-Sequence：部分可观测交互中的潜在状态

项目：[BridgeVLA-Sequence / dev-gavinsun](https://github.com/npucvr/BridgeVLA-Sequence/tree/dev-gavinsun)

当前关注：

- partial observability；
- persistent hidden state；
- observation update；
- action-conditioned transition；
- prior-observation prediction。

它作为“状态预测与交互应用”的已有探索，用于说明时空状态问题可以进一步延伸到 embodied interaction；当前不把它定义成独立的第二条博士主线，更不直接等同于 World Model。

## 开题结构

当前建议按以下逻辑组织：

\`\`\`text
Incomplete / Noisy Observation
            ↓
   Spatiotemporal State
        ↙         ↘
   Recovery     Evolution
        \         /
         \       /
       Prediction / Interaction
\`\`\`

其中：

- **研究内容一**：不完全观测下的动态场景状态恢复；
- **研究内容二**：动态场景状态的连续时间演化建模；
- **研究内容三**：时空状态的预测建模与交互应用。

详细讨论、已有证据边界和开题前计划见：

- [docs/research_scope.md](docs/research_scope.md)

## 当前定位

Spatial Intelligence / World Model 是研究背景和可能的长期落点。

当前博士开题不承诺同时解决 4D Reconstruction、VLA 和 World Model 三个大方向，而是围绕一个更具体的问题展开：

> **不完全观测条件下动态场景时空状态的恢复、演化与预测。**
