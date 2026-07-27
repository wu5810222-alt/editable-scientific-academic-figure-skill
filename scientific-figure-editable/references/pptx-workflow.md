# Editable PPTX Workflow

## Meaning Of Editable

An editable PPTX method figure must represent modules, labels, arrows, equations, and decorative geometry as independent native PowerPoint objects. A single selectable image is flattened, not editable.

Raster images are acceptable only for genuine image samples or thumbnails. They must not contain the entire architecture.

## Preferred Paths

1. **Author directly in PowerPoint-compatible native shapes** when PPTX is the primary deliverable.
2. **Convert Draw.io XML to native PPTX objects** by mapping rectangles, ellipses, polygons, text, and connectors individually.
3. Use SVG only when the user accepts grouped vector artwork and does not require every internal component to be independently draggable.

Do not use a full-slide PNG or SVG as a substitute for native object-level editability.

## Conversion Mapping

| Draw.io | PowerPoint |
| --- | --- |
| Rectangle / rounded rectangle | AutoShape |
| Ellipse | AutoShape ellipse |
| Polygon / trapezoid | Freeform or closest native AutoShape |
| Text label | TextBox or shape text frame |
| Straight/orthogonal edge | Connector or line segments |
| Dashed edge | Connector with dash style |
| Group/container | PowerPoint group when stable; otherwise independent shapes |
| Embedded sample image | Picture |

Preserve z-order: backgrounds first, connectors second, modules third, labels and highlights last.

## Verification

1. Open the PPTX with `python-pptx` and count pictures, shapes, connectors, and text objects.
2. Run `scripts/audit_pptx.py file.pptx --max-pictures N`, where `N` equals the number of legitimate sample images.
3. Round-trip through LibreOffice or PowerPoint and render a preview.
4. Inspect the rendered result for clipping, missing fonts, changed line breaks, shadow differences, and connector drift.
5. State any approximated proprietary Draw.io icons or unsupported geometry.

## Common Failures

- Flattening the entire Draw.io page into one PNG.
- Importing one full-page SVG and calling it editable.
- Turning every connector into a decorative arrow shape that cannot remain attached to nodes.
- Losing text wrapping during conversion.
- Using rasterized equations when the user needs to edit variables.
- Failing to test LibreOffice/PowerPoint rendering after generating the PPTX.
