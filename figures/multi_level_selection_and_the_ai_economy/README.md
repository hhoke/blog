# Figures: Multi-Level Selection and the AI Economy

Figures and source code for [Multi-Level Selection and the AI Economy](../../multi_level_selection_and_the_ai_economy.md).

| Figure | Source |
|---|---|
| [mosaic_triangle.svg](mosaic_triangle.svg): three people, three skills | [mosaic_triangle.py](mosaic_triangle.py) |
| [mosaic_gpqa.svg](mosaic_gpqa.svg): real data, a chemist and a physicist vs. GPT-4 (2023) and Claude Sonnet 4.6 (2026) on GPQA | [mosaic_gpqa.py](mosaic_gpqa.py) |

The scripts use only the Python standard library. To regenerate, run from the repo root:

```sh
python3 figures/multi_level_selection_and_the_ai_economy/mosaic_triangle.py
python3 figures/multi_level_selection_and_the_ai_economy/mosaic_gpqa.py
```

`mosaic_gpqa.py` imports its colors and fonts from `mosaic_triangle.py`.
The hypothetical GrokBot figure (`mosaic_2d`) was removed; it is in git history at commit `81b17d1`.
The data sources and caveats for `mosaic_gpqa.svg` are in the docstring of `mosaic_gpqa.py`.

Both figures are simplified versions of the mosaic intelligence figure in
[The Economics of Intelligence](https://institute.deepmind.com/essays/the-economics-of-intelligence/).
