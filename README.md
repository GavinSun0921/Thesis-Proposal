# Thesis Proposal

本仓库用于整理博士开题的研究主线、科学问题、已有工作与后续计划。

## 当前建议题目

**面向空间智能的动态场景时空状态表征与演化建模研究**

备选题目：

- 复杂动态场景的连续时空状态表征与运动建模研究
- 面向物理世界模型的动态场景状态表征、估计与演化研究（暂不作为首选，待未来状态预测与长期 rollout 证据更充分后再考虑）

## 核心科学问题

> 在不完全、含噪的时空观测下，如何构建能够恢复动态场景、描述其连续演化，并进一步支持预测与交互决策的时空状态表示？

统一形式可写为：

```math
S_t = U(S_{t-1}, z_t),
```

```math
S_{t+Delta} = F(S_t, a_t, Delta),
```

其中，(z_t) 表示不完整或含噪观测，(a_t) 表示可选的智能体动作，(S_t) 表示对动态物理世界当前状态的内部表示。

## 当前两条工作主线

1. **显式时空状态恢复与连续运动建模**
   - 项目：[Pomelo4D-v0 / exp/mosca-submodule-baseline](https://github.com/GavinSun0921/Pomelo4D-v0/tree/exp/mosca-submodule-baseline)
   - 关注 dense correspondence、遮挡/漂移/深度误差、不确定观测融合、稀疏运动自由度、连续时间三维运动。
   - 对应博士问题中的 **State Representation / Recovery** 与部分 **State Evolution**。

2. **面向交互决策的潜在状态估计与动作条件演化**
   - 项目：[BridgeVLA-Sequence / dev-gavinsun](https://github.com/npucvr/BridgeVLA-Sequence/tree/dev-gavinsun)
   - 关注 partial observability、历史状态维护、observation update、action-conditioned transition、predictive hidden state。
   - 对应博士问题中的 **State Evolution / Prediction / Utilization**。

## 研究主线

博士课题暂时按三个层级收敛：

1. **State Representation / Recovery**：如何从不完整、不可靠观测中恢复 geometry-consistent 的动态时空状态；
2. **State Evolution**：如何描述状态随连续时间或动作的演化，并在遮挡、缺测和较长时间尺度下保持一致；
3. **State Prediction / Utilization**：如何让时空状态真正支持未来状态预测、动态重建和 embodied decision-making。

详细讨论、当前证据边界、三项研究内容和开题前一个月计划见：

- [docs/research_scope.md](docs/research_scope.md)

## 当前定位

“空间智能 / World Model”用于说明研究背景与长期目标；当前开题不直接把完整 World Model 作为已经成立的方法 claim。现阶段更核心、也更可验证的问题是 **动态场景时空状态的表征、恢复与演化**。
