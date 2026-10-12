#!/usr/bin/env python3
"""分别绘制图 1 的三个 2D 子图；在任意目录运行均输出到本脚本所在目录。"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle


# 场景参数：相机朝向 +y，目标沿墙后方的水平直线从左向右移动。
CAMERA = (0.0, 0.0)
WALL_LEFT, WALL_RIGHT = -1.4, 1.4
WALL_FRONT, WALL_DEPTH = 3.3, 0.18
TARGET_Y = 6.0
HISTORY_START = -4.45
VISIBLE_X, HIDDEN_X = -3.65, 0.2
# 重观测时刻：先验仍按匀速/减速推演、未穿出遮挡区；真实目标加速后提前可见。
PRIOR_X, REOBSERVED_X = 2.15, 3.9
TARGET_RADIUS = 0.22
X_LIMITS, Y_LIMITS = (-4.9, 4.9), (-0.95, 7.25)

# 统一画布与样式；图内不写文字，子图编号、标题和图注由 LaTeX 生成。
FIGURE_SIZE = (3.6, 3.1)
PREVIEW_DPI = 240
BLUE, AMBER, GREEN = "#2474B5", "#D68A16", "#20864B"
WALL_COLOR, SHADOW_COLOR, GUIDE_COLOR = "#8B9097", "#F0F2F4", "#C1C6CC"
PREDICTION_DASHES = (0, (3.5, 2.5))


def shadow_bounds(y):
    """相机经墙体近侧两端的切线，在给定深度 y 处形成的遮挡区间。"""
    scale = (y - CAMERA[1]) / (WALL_FRONT - CAMERA[1])
    return tuple(CAMERA[0] + (x - CAMERA[0]) * scale for x in (WALL_LEFT, WALL_RIGHT))


def is_occluded(x, y):
    if y <= WALL_FRONT:
        return False
    left, right = shadow_bounds(y)
    return left <= x <= right


def draw_scene():
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    ax.set(xlim=X_LIMITS, ylim=Y_LIMITS, aspect="equal")
    ax.set_axis_off()

    far_left, far_right = shadow_bounds(Y_LIMITS[1])
    ax.add_patch(Polygon(
        [(WALL_LEFT, WALL_FRONT), (WALL_RIGHT, WALL_FRONT),
         (far_right, Y_LIMITS[1]), (far_left, Y_LIMITS[1])],
        closed=True, facecolor=SHADOW_COLOR, edgecolor="none", zorder=0,
    ))
    # 阴影仅位于墙后；相机与墙之间不填充阴影。
    for edge, far in ((WALL_LEFT, far_left), (WALL_RIGHT, far_right)):
        ax.plot([CAMERA[0], edge, far], [CAMERA[1], WALL_FRONT, Y_LIMITS[1]],
                color=GUIDE_COLOR, lw=0.75, linestyle=(0, (2.5, 3)), zorder=1)
    ax.add_patch(Rectangle(
        (WALL_LEFT, WALL_FRONT), WALL_RIGHT - WALL_LEFT, WALL_DEPTH,
        facecolor=WALL_COLOR, edgecolor="#575D65", lw=0.9, zorder=4,
    ))

    # 平面相机符号：矩形机身与朝向 +y 的镜头，镜头顶端即 CAMERA。
    cx, cy = CAMERA
    ax.add_patch(Rectangle((cx - 0.32, cy - 0.67), 0.64, 0.43,
                           facecolor="white", edgecolor="#49515B", lw=1.1, zorder=5))
    ax.add_patch(Polygon([(cx - 0.18, cy - 0.24), (cx + 0.18, cy - 0.24),
                          (cx + 0.11, cy), (cx - 0.11, cy)],
                         facecolor="#D7DCE1", edgecolor="#49515B", lw=1.0, zorder=5))
    return fig, ax


def draw_target(ax, x, color, predicted=False):
    ax.add_patch(Circle(
        (x, TARGET_Y), TARGET_RADIUS,
        facecolor="white" if predicted else color, edgecolor=color,
        lw=1.55 if predicted else 1.4,
        linestyle=PREDICTION_DASHES if predicted else "solid", zorder=7,
    ))


def draw_history(ax, end):
    ax.plot([HISTORY_START, end], [TARGET_Y, TARGET_Y], color=BLUE, lw=1.55,
            solid_capstyle="butt", zorder=3)
    for fraction in (0.2, 0.6):
        x = HISTORY_START + (end - HISTORY_START) * fraction
        ax.plot(x, TARGET_Y, "o", color=BLUE, ms=2.5, zorder=4)


def draw_sightline(ax, x, color):
    ax.plot([CAMERA[0], x], [CAMERA[1], TARGET_Y], color=color,
            lw=0.85, linestyle=(0, (1.5, 2.5)), zorder=2)


def draw_visible():
    fig, ax = draw_scene()
    draw_history(ax, VISIBLE_X)
    draw_sightline(ax, VISIBLE_X, BLUE)
    draw_target(ax, VISIBLE_X, BLUE)
    return fig


def draw_hidden():
    fig, ax = draw_scene()
    entry, _ = shadow_bounds(TARGET_Y)
    draw_history(ax, entry)
    # 预测轨迹严格从遮挡边界开始，不覆盖左侧有观测依据的轨迹。
    ax.plot([entry, HIDDEN_X], [TARGET_Y, TARGET_Y], color=AMBER, lw=1.55,
            linestyle=PREDICTION_DASHES, dash_capstyle="butt", zorder=3)
    draw_target(ax, HIDDEN_X, AMBER, predicted=True)
    # 朝向预测位置的视线在墙体近侧停止，不穿过墙体。
    hit_x = CAMERA[0] + (HIDDEN_X - CAMERA[0]) * (
        (WALL_FRONT - CAMERA[1]) / (TARGET_Y - CAMERA[1]))
    ax.plot([CAMERA[0], hit_x], [CAMERA[1], WALL_FRONT], color="#717983",
            lw=0.85, linestyle=(0, (1.5, 2.5)), zorder=2)
    ax.plot(hit_x, WALL_FRONT, "x", color="#717983", ms=4, mew=1.0, zorder=6)
    return fig


def draw_corrected():
    fig, ax = draw_scene()
    entry, right = shadow_bounds(TARGET_Y)
    # 先验轨迹止于遮挡区内部，表示匀速/减速假设下目标尚未完全运动出来。
    ax.plot([entry, PRIOR_X], [TARGET_Y, TARGET_Y], color=AMBER, lw=1.55,
            linestyle=PREDICTION_DASHES, dash_capstyle="butt", zorder=3)
    draw_target(ax, PRIOR_X, AMBER, predicted=True)
    draw_sightline(ax, REOBSERVED_X, GREEN)
    draw_target(ax, REOBSERVED_X, GREEN)
    # 加速使真实位置越过先验，新观测把状态校正到重观测位置。
    ax.add_patch(FancyArrowPatch(
        (PRIOR_X + TARGET_RADIUS * 1.15, TARGET_Y),
        (REOBSERVED_X - TARGET_RADIUS * 1.15, TARGET_Y),
        arrowstyle="-|>", mutation_scale=10, lw=1.35, color=GREEN,
        shrinkA=0, shrinkB=0, zorder=8,
    ))
    return fig


def main():
    if not CAMERA[1] < WALL_FRONT < WALL_FRONT + WALL_DEPTH < TARGET_Y:
        raise ValueError("应依次放置相机、横向墙体、墙后运动路线。")
    entry, right = shadow_bounds(TARGET_Y)
    if not VISIBLE_X < entry < HIDDEN_X < PRIOR_X < right < REOBSERVED_X:
        raise ValueError("目标位置应依次对应左侧可见、墙后遮挡、遮挡区内的先验，以及右侧重观测。")
    if is_occluded(VISIBLE_X, TARGET_Y) or is_occluded(REOBSERVED_X, TARGET_Y):
        raise ValueError("可见阶段的相机视线不能与墙体相交。")
    if not is_occluded(PRIOR_X, TARGET_Y):
        raise ValueError("先验位置应仍处于遮挡区，表示预测尚未完全穿出。")

    output_dir = Path(__file__).resolve().parent
    for name, draw in (("occlusion_visible", draw_visible),
                       ("occlusion_hidden", draw_hidden),
                       ("occlusion_corrected", draw_corrected)):
        fig = draw()
        # 固定 PDF 元数据，使不修改参数的重复绘制不会制造版本差异。
        fig.savefig(output_dir / f"{name}.pdf", facecolor="white",
                    metadata={"Creator": "draw_occlusion.py", "CreationDate": None, "ModDate": None})
        fig.savefig(output_dir / f"{name}.png", dpi=PREVIEW_DPI, facecolor="white",
                    metadata={"Software": "draw_occlusion.py"})
        plt.close(fig)
        print(f"已生成：{output_dir / name}.pdf / .png")


if __name__ == "__main__":
    main()
