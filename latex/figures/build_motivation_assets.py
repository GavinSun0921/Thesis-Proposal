"""Reproduce the measured-depth visual elements of the Section 1.1 figure.

Requires NumPy and Pillow. Raw source bytes and their hashes are retained under
materials/dycheck_apple. No reconstruction model or prediction model is run.
"""

from pathlib import Path
import json

import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "materials/dycheck_apple"
MEASUREMENTS = SOURCE / "measurements"
OUTPUT = ROOT / "generated/motivation"
FRAMES = [0, 190, 332]
# Full-resolution pixel coordinates; each crop is square and is applied in TeX
# to the RGB original. The matching 2x sensor-depth crop is visualized here.
CROPS = {0: (100, 420, 440), 190: (160, 460, 440), 332: (260, 450, 440)}


def rotation(x_degrees=0, y_degrees=0, z_degrees=0):
    x, y, z = np.deg2rad([x_degrees, y_degrees, z_degrees])
    rx = np.array([[1, 0, 0], [0, np.cos(x), -np.sin(x)],
                   [0, np.sin(x), np.cos(x)]])
    ry = np.array([[np.cos(y), 0, np.sin(y)], [0, 1, 0],
                   [-np.sin(y), 0, np.cos(y)]])
    rz = np.array([[np.cos(z), -np.sin(z), 0],
                   [np.sin(z), np.cos(z), 0], [0, 0, 1]])
    return rz @ ry @ rx


def point_image(points, colors, view, destination, marker_points=None, point_radius=2.1):
    """Orthographic visualization of a partial RGB-D point set; no completion."""
    center = np.median(points, axis=0)
    transformed = (points - center) @ view.T
    lower = transformed[:, :2].min(axis=0)
    upper = transformed[:, :2].max(axis=0)
    width, height = 1000, 960
    scale = min((width - 140) / (upper[0] - lower[0]),
                (height - 140) / (upper[1] - lower[1]))
    middle = (lower + upper) / 2
    xy = (transformed[:, :2] - middle) * scale + [width / 2, height / 2]
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    # Draw far points before near points. Original RGB colors are retained.
    for index in np.argsort(transformed[:, 2])[::-1]:
        px, py = xy[index]
        rgb = tuple(int(v) for v in colors[index])
        draw.ellipse((px - point_radius, py - point_radius,
                      px + point_radius, py + point_radius), fill=rgb + (255,))
    image.save(destination)
    result = {}
    if marker_points:
        for key, point in marker_points.items():
            projected = ((point - center) @ view.T)[:2]
            projected = (projected - middle) * scale + [width / 2, height / 2]
            result[key] = (projected / [width, height]).tolist()
    return result


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    layout = {"frames": {}, "pointcloud": {}}
    for frame in FRAMES:
        stem = f"0_{frame:05d}"
        depth = np.load(MEASUREMENTS / f"depth/2x/{stem}.npy",
                        allow_pickle=False).squeeze()
        x, y, size = CROPS[frame]
        crop = depth[y // 2:(y + size) // 2, x // 2:(x + size) // 2]
        valid = np.isfinite(crop) & (crop > 0)
        # One shared qualitative scale; gray explicitly indicates missing data.
        fraction = np.clip((np.where(valid, crop, .16) - .16) / .39, 0, 1)
        anchors = np.array([[45, 81, 112], [53, 133, 145], [153, 202, 198],
                            [228, 237, 224]], dtype=float)
        scaled = fraction * 3
        low = np.minimum(scaled.astype(int), 2)
        weight = (scaled - low)[..., None]
        mapped = (anchors[low] * (1 - weight) + anchors[low + 1] * weight).astype("uint8")
        mapped[~valid] = [212, 217, 220]
        Image.fromarray(mapped).resize((660, 660), Image.Resampling.NEAREST).save(
            OUTPUT / f"depth_{frame:05d}.png")
        keypoints = json.loads((MEASUREMENTS / f"keypoint/2x/train/{stem}.json").read_text())
        layout["frames"][str(frame)] = {"crop": [x, y, size], "keypoints": keypoints}

    frame = 332
    stem = f"0_{frame:05d}"
    rgb = np.asarray(Image.open(MEASUREMENTS / f"rgb/2x/{stem}.png").convert("RGB"))
    depth = np.load(MEASUREMENTS / f"depth/2x/{stem}.npy", allow_pickle=False).squeeze()
    camera = json.loads((MEASUREMENTS / f"camera/{stem}.json").read_text())
    fx = camera["focal_length"] / 2
    fy = fx * camera["pixel_aspect_ratio"]
    cx, cy = np.asarray(camera["principal_point"]) / 2
    yy, xx = np.indices(depth.shape)
    xyz = np.stack(((xx - cx) * depth / fx, (yy - cy) * depth / fy, depth), axis=-1)
    neighborhood = np.lib.stride_tricks.sliding_window_view(
        np.pad(depth, 2, mode="edge"), (5, 5))
    local_median = np.median(neighborhood, axis=(-2, -1))
    valid = np.isfinite(depth) & (depth > .16) & (depth < .235)
    valid &= np.abs(depth - local_median) < .012
    valid &= (xx >= 145) & (xx < 273) & (yy >= 245) & (yy < 393)
    points, colors = xyz[valid], rgb[valid]
    markers = {}
    for key in [0, 1, 4, 6]:
        u, v, visible = layout["frames"]["332"]["keypoints"][key]
        if visible:
            ix, iy = int(u), int(v)
            patch = depth[max(0, iy - 2):iy + 3, max(0, ix - 2):ix + 3]
            near = patch[np.isfinite(patch) & (patch > .16) & (patch < .235)]
            if not len(near):
                continue
            z = np.median(near)
            markers[str(key)] = np.array([(u - cx) * z / fx, (v - cy) * z / fy, z])
    projected = point_image(points, colors, rotation(-8, -18, 0),
                            OUTPUT / "observed_geometry.png", markers)
    # The two action illustrations rotate only this observed partial surface.
    # They are conceptual alternatives, not learned forecasts or ground truth.
    fruit = valid & (((xx - 213) / 51) ** 2 + ((yy - 320) / 57) ** 2 < 1)
    fruit &= yy >= 279
    fruit_points, fruit_colors = xyz[fruit], rgb[fruit]
    point_image(fruit_points, fruit_colors, rotation(-5, -13, -30),
                OUTPUT / "action_1_concept.png", point_radius=3.3)
    point_image(fruit_points, fruit_colors, rotation(-5, 13, 30),
                OUTPUT / "action_2_concept.png", point_radius=3.3)
    layout["pointcloud"] = {"frame": frame, "points": int(len(points)),
                            "markers_normalized_from_top_left": projected,
                            "fruit_points": int(len(fruit_points)),
                            "note": "Single-frame, depth-derived visible geometry; trajectories and action alternatives are conceptual."}
    (OUTPUT / "layout.json").write_text(json.dumps(layout, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(layout["pointcloud"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
