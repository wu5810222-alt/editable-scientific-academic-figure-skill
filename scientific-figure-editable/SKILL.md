---
name: scientific-figure-editable
description: Design, reconstruct, review, and deliver publication-ready scientific method figures as native editable Draw.io and PowerPoint files, with selectable visual systems for pipelines, token models, hierarchical vision, query decoders, recurrent/state-space models, mixture-of-experts, multimodal foundation models, agents/world models, neural rendering/3D, and graph/scientific AI. Use for paper overview or architecture figures, screenshot-to-editable reconstruction, visual redesign, Draw.io formula/routing problems, or requests requiring every PPTX element to remain independently movable and editable rather than a flattened image.
---

# Scientific Figure Editable

Create figures whose narrative is clear in five seconds and whose delivered objects remain editable.

## Select The Workflow

1. **Design or redraw a method figure**: read `references/design-rules.md`, then select a style using `references/style-catalog.md` or `scripts/list_styles.py`. Use `drawio-skill` and, for thesis/paper formatting, `thesis-figure-skill`.
2. **Reconstruct a screenshot**: inspect the image visually, extract the semantic graph, then create native Draw.io shapes. Never use the screenshot as the full-slide background.
3. **Review an existing figure**: read `references/review-checklist.md`; render the artifact before judging it.
4. **Deliver Draw.io**: follow `references/drawio-workflow.md`.
5. **Deliver editable PPTX**: follow `references/pptx-workflow.md`; run `scripts/audit_pptx.py` before claiming object-level editability.

## Core Workflow

1. **Recover the scientific claim**
   - Write one sentence stating the input, each contribution, and final output.
   - Convert it into a monotonic computation chain.
   - Mark contributions as `C1`, `C2`, `C3` when the paper has multiple novel components.

2. **Build a text wireframe**
   - List stages, inputs/outputs, variables, and directed relations.
   - Separate shared backbones from modality-specific or trainable/frozen modules.
   - Remove implementation details that do not support the central claim.

3. **Select figure purpose and style**
   - Choose concept overview or detailed architecture; split into two figures when necessary.
   - Select one primary style ID from `references/style-catalog.md`.
   - If the user did not choose, present 2-3 compatible styles and recommend one based on the method topology.
   - Use at most one secondary style for a bounded inset.

4. **Draw structure before styling**
   - Use native shapes and connectors.
   - Keep a single primary reading direction.
   - Use containers only for genuine semantic boundaries.
   - Route all edges before adding color, shadows, samples, or decoration.

5. **Apply semantic styling**
   - Encode roles with color; never use color as arbitrary decoration.
   - Use a restrained white/light-gray publication background.
   - Add real input/output thumbnails only when they prove the method's effect.
   - Use one formula per important transformation, placed beside that transformation.

6. **Validate**
   - Check scientific logic, arrow direction, parent-child containment, formula rendering, overlaps, text clipping, and grayscale readability.
   - Export a preview and inspect it at final publication size.
   - For PPTX, verify that the architecture is native shapes/connectors and not one picture.

## Non-Negotiable Rules

- Do not deliver a flattened screenshot when the user asks for editable Draw.io or PPTX.
- Do not claim PPTX editability merely because a picture can be selected.
- Do not invent method details, equations, conference status, or contribution claims.
- Do not use raw custom XML formula tags. In Draw.io use native `\(...\)` math when math rendering is enabled, or plain text for robust short equations.
- Do not place UI cards inside decorative cards. Use containers only for model stages or ownership boundaries.
- Do not allow arrow labels to overlap nodes, formulas, or other arrows.
- Do not copy a fashionable paper's visual style when its information topology does not match the user's method.
- Do not mix more than two named styles in one figure.
- Preserve user-authored changes in existing files.

## Deliverables

Default deliverables for a completed figure:

- Native `.drawio` source.
- Clean preview PNG.
- Embedded-editable `.drawio.png` or SVG when requested.
- Native object-based `.pptx` only when requested and verified.
- One concise English caption for paper use.

Report the validation performed and any unavoidable fidelity limitations.

## Style Resources

- `references/style-catalog.md`: selection matrix and detailed style definitions.
- `references/style-presets.yaml`: machine-readable layout, palette, and shape tokens.
- `references/style-evidence.md`: representative papers and the visual observations behind each style.
- `scripts/list_styles.py`: print the available styles as a table or JSON.
