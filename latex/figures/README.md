# 插图工程

更新：2026-10-31。以 `latex/main.tex` 的实际依赖为准，当前正文使用 **13 张图**，路径和校验值统一登记在 `manifest.json`。

## 目录与命名

```text
figures/
├── chapters/
│   ├── ch01-basis/       # 第一部分：研究依据，7 张图
│   ├── ch02-content/     # 第二部分：研究内容，1 张图
│   └── ch03-plan/        # 第三部分：技术路线，5 张图
├── scripts/             # 现用检查、导出脚本
├── manifest.json        # 活跃图源、导出物、校验值
└── README.md            # 目录规范与构建说明
```

每图一个稳定英文语义目录，不把自动图号或临时版本名作为正式文件名。`diagram.svg` / `diagram.tex` 是可编辑源，`figure.pdf` / `figure.png` 是正文输入；`assets/` 仅放该图必要的原始素材。临时预览放在仓库根目录的 `tmp/`，不纳入版本控制。

清单中的路径相对于 `latex/figures/`，正文中的图件路径相对于 `latex/`，Markdown 链接相对于所在文档。统一使用 `/` 分隔路径；图源、输出及素材都放在同一图件目录内。SVG 中的图片须内嵌，不引用本机绝对路径、外部文件或网络资源。

| 章节 | 当前图号 | 稳定目录 | 编辑源 / 正文输入 |
| --- | --- | --- | --- |
| 1.1 | 1 | [world-model-loop](chapters/ch01-basis/world-model-loop/) | `diagram.svg` / `figure.pdf` |
| 1.1 | 2 | [spacecraft-maintenance](chapters/ch01-basis/spacecraft-maintenance/) | 只有 `figure.png`；尚无独立可编辑源 |
| 1.2.1 | 3 | [reconstruction-timeline](chapters/ch01-basis/reconstruction-timeline/) | `diagram.svg` / `figure.pdf` |
| 1.2.2 | 4 | [world-model-evolution](chapters/ch01-basis/world-model-evolution/) | `diagram.svg` / `figure.pdf` |
| 1.2.3 | 5 | [action-learning-timeline](chapters/ch01-basis/action-learning-timeline/) | `diagram.svg` / `figure.pdf` |
| 1.3.1 | 6 | [cofuse4d-method](chapters/ch01-basis/cofuse4d-method/) | `diagram.tex` 直接由主工程编译，素材在 `assets/` |
| 1.3.2 | 7 | [psvla-method](chapters/ch01-basis/psvla-method/) | `diagram.tex` / 已保存的 `figure.pdf` |
| 2.2 | 8 | [research-framework](chapters/ch02-content/research-framework/) | `diagram.svg` / `figure.pdf` |
| 3.3 | 9 | [overall-technical-route](chapters/ch03-plan/overall-technical-route/) | `diagram.svg` / `figure.pdf` |
| 3.3.1 | 10 | [continuous-time-route](chapters/ch03-plan/continuous-time-route/) | `diagram.svg` / `figure.pdf` |
| 3.3.2 | 11 | [object-consistency-route](chapters/ch03-plan/object-consistency-route/) | `diagram.svg` / `figure.pdf` |
| 3.3.3 | 12 | [topology-change-route](chapters/ch03-plan/topology-change-route/) | `diagram.svg` / `figure.pdf` |
| 3.3.4 | 13 | [action-response-route](chapters/ch03-plan/action-response-route/) | `diagram.svg` / `figure.pdf` |

图号由 LaTeX 自动编号；目录名和 manifest ID 不随图号变化。

## 检查与构建

从仓库根目录运行：

```sh
python3 latex/figures/scripts/manage_figures.py --check
python3 latex/figures/scripts/manage_figures.py --inventory
./scripts/build.sh
```

图件管理器检查活跃依赖、清单文件及校验值；正常编译只读取保存好的 PDF/PNG 和 CoFuse4D TikZ，不联网、不重绘 SVG、不需要重新下载媒体。绘图脚本的可用命令及保留限制见 [scripts/README.md](scripts/README.md)。

四张分项路线图的导出器为 [scripts/export_route_diagrams.py](scripts/export_route_diagrams.py)，使用 CairoSVG/Cairo，校验原有画布、共享字号、字体及框体样式。图 10–12 保留原有 29 个文字块；图 13 使用 49 个文字块及带 `data-latex` 标注的矢量公式，并在同一画布内为双反馈适配结果区、反馈区和输出条高度，三个阶段及步骤框保持等宽等高。示例：

```sh
python3 latex/figures/scripts/export_route_diagrams.py --only continuous-time-route
```

这四图的脚本仅用于显式更新，不随报告构建自动运行。其他历史转换方式不能未经视觉对比直接替代：研究框架原为 macOS WebKit 导出（PingFang SC）；PS-VLA 保存的 PDF 使用 Fandol/Latin Modern，而正文模板使用本机 SimSun/Times，重新套模板导出会改变字形。世界模型闭环、时间轴和总体路线的早期转换步骤不完整，当前导出件及其哈希保留，不宣称已具备全部图的像素级可复现绘制链。

## 素材来源与审查范围

CoFuse4D 的六张素材保存在其 `assets/` 目录中：三帧 RGB 和深度来自 DyCheck apple 序列，对象身份图与轨迹叠加用于说明方法流程；逐文件校验值见 `manifest.json`。闭环图的 11 张插图内嵌于 SVG；在轨维护信息图只有位图，不能由 PDF 字体列表确认其字体。

字体/字号审查见[当前图内文字调查](../../docs/figure_typography_audit.md)。重点检查最终排入正文后的大小，而非只看 SVG 里的 px：版心宽 156 mm；图 1、2 使用 0.98 倍版心宽；PDF 点和 TeX 点之间有约 0.4% 的差异。数学上下标不作为普通中文标签小字计入同一阈值。

## 清理

图件目录只保存当前清单登记的图源、正文导出件及必要素材。新增或移动图件时同步更新正文引用、清单路径与校验值，并运行上述检查。临时预览、隔离构建和缓存可清理；正式报告版本由根目录的 `output/` 管理。
