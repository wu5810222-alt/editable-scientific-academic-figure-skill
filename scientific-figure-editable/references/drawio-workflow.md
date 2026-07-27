# Draw.io Workflow

## Authoring

1. Use the `drawio-skill` XML authoring rules.
2. Create native `mxCell` vertices and edges. Give every edge an `mxGeometry` child.
3. Use unique non-reserved IDs; reserve `0` and `1` for the root.
4. Use true parent-child containment for semantic groups when practical.
5. Keep layout coordinates on a regular grid.
6. Use explicit ports and waypoints for crowded nodes.

## Formulas

- Prefer short plain-text equations when maximum portability matters.
- For rendered math, enable `math="1"` and use Draw.io native inline math `\(...\)`.
- Never write `<inline_LaTeX_Formula>` or similar custom tags into labels; Draw.io displays them as code.
- Replace unsupported macros with KaTeX-compatible forms; use `\text{}` instead of `\mathrm{}` when required by the environment.

## Validation

Run:

```bash
python3 ~/.codex/skills/drawio-skill/scripts/validate.py figure.drawio --score
```

Interpret overlaps with large background containers carefully, but fix real node-node overlaps, dangling edges, duplicate IDs, clipped labels, and through-node routing.

## Export And Visual Review

Preview without embedded XML:

```bash
drawio -x -f png --width 2000 -o figure.png figure.drawio
```

Inspect the PNG for hierarchy, text, arrow direction, cropping, and visual balance. Then export embedded deliverables:

```bash
drawio -x -f png -e -s 2 -o figure.drawio.png figure.drawio
python3 ~/.codex/skills/drawio-skill/scripts/repair_png.py figure.drawio.png
drawio -x -f svg -e -o figure.svg figure.drawio
```

Use `HOME=/tmp`, `--disable-gpu`, and `--no-sandbox` only when required by the local Linux/Electron environment and approved by the user.
