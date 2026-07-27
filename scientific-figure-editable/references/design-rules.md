# Scientific Figure Design Rules

## 1. Separate Story From Style

Decide these independently:

1. **Figure purpose**: concept overview, detailed architecture, training framework, inference pipeline, ablation explanation, or system deployment.
2. **Narrative topology**: pipeline, parallel branches, hierarchy, recurrent loop, sparse routing, coordinate field, graph, or closed-loop agent.
3. **Visual style**: select a named style from `style-catalog.md` and `style-presets.yaml`.

Do not imitate a paper's colors before confirming that its narrative topology matches the method.

## 2. Write The Five-Second Claim

Before drawing, write one sentence with this grammar:

`Given <inputs>, C1 produces <intermediate>, C2 enforces <property>, and <fusion/update> yields <output>.`

The figure must visibly answer:

1. What enters the method?
2. What does each contribution solve?
3. What named representation leaves each contribution?
4. How are branches fused, routed, updated, or decoded?
5. What output demonstrates the claimed property?

If these cannot be traced through arrows, restructure before styling.

## 3. Choose Concept Figure Or Architecture Figure

### Concept Figure

Use when introducing a new task, behavior, geometric intuition, or capability. Prefer 3-7 large semantic objects, a real input/output example, and one visual contrast. Examples include DETR's set prediction, SAM's promptable segmentation system, NeRF's rays-to-color concept, and DINOv2's feature behavior.

### Architecture Figure

Use when the contribution lies in block structure, routing, memory, hierarchy, or training/inference decomposition. Show named intermediate representations and repeat modules symbolically. Examples include ViT patch tokens, Swin stages, Switch routing, Perceiver IO queries, Mamba selective state, and SAM 2 memory attention.

### Two-Figure Strategy

When one canvas would exceed roughly 12 major modules or mix task motivation with low-level block internals, create:

- Figure A: contribution overview.
- Figure B: detailed architecture or block design.

Do not compress both into unreadable miniature modules.

## 4. Information Hierarchy

- Level 1: figure conclusion and contribution/stage titles.
- Level 2: main modules and their named outputs.
- Level 3: variables, schedules, losses, constraints, routing scores.
- Level 4: repeated layers, token cells, sample thumbnails, implementation detail.

Level 1 and 2 must dominate. Repeated matrices, tokens, experts, layers, frames, or graph nodes should be symbolic rather than exhaustive.

## 5. Semantic Encoding

### Color

Assign colors by meaning, not by position. Use 3-5 role colors and one neutral family. A reliable base palette is:

| Role | Fill | Stroke |
| --- | --- | --- |
| Input/output or observation | `#DCEBFA` | `#7EA6D8` |
| Semantic/text/query branch | `#FFF0C2` | `#D6A93A` |
| Spatial/geometry/state branch | `#E6F6D5` | `#75A95B` |
| Selected/novel/contribution | `#F6C7C0` | `#C66B62` |
| Shared/frozen/neutral core | `#F7F8FA` | `#667085` |
| Primary data path | none | `#2563EB` |

Named styles may override the palette. Keep role semantics stable within a figure and preserve differences in grayscale using labels, borders, hatching, or line styles.

### Arrow Grammar

- Solid arrow: tensor/data flow.
- Dashed arrow: condition, supervision, mask, prompt, or control.
- Thin line: residual, skip, reference, or correspondence.
- Thick arrow: primary stage transition or inference route.
- Curved line: temporal/geometric trajectory or feedback loop only.
- Fan-out/fan-in: routing or aggregation; label the operation.

Every arrow must have a source and consumer. Avoid decorative arrows and ambiguous bidirectional arrows.

### Shapes

- Rectangle: computation/module.
- Small tiles: tokens, patches, experts, frames, or feature levels.
- Circle: state, latent point, query, or aggregation node.
- Trapezoid/pyramid: spatial resolution change only.
- Cylinder: memory, dataset, replay buffer, or persistent store.
- Real thumbnail: actual input/output evidence, not decoration.

Do not assign multiple meanings to the same shape in one figure.

## 6. Layout Grammar By Model Family

### Transformer / Token Models

Show tokenization once, a symbolic repeated block, positional information, and the task head. Use matrices or token strips only when token organization is central. Do not draw every transformer layer.

### Hierarchical Vision Backbones

Use stages with visibly decreasing spatial size and increasing channel depth. Align stage labels and use one inset for the repeated block. Avoid equal-sized stage boxes that hide the hierarchy.

### Detection And Segmentation

Separate dense image features from sparse queries/prompts and output masks/sets. Make bipartite matching, mask attention, or prompt conditioning visually explicit only when it is the contribution.

### State Space / Recurrent Memory

Use a horizontal sequence with a persistent state line or a closed loop. Distinguish state update, input-dependent selection, and output readout. For video/world models, show memory across time without copying the full network per frame.

### Mixture Of Experts

Show router, top-k selection, parallel experts, capacity/load behavior when relevant, and merge. Use a sparse fan-out: only selected routes receive saturated color; inactive routes remain light gray.

### Multimodal Foundation Models

Use parallel modality adapters only until the first true shared representation. Put the shared LLM/transformer in a neutral central lane, then separate task/output heads. Distinguish tokenizer/encoder, projector, shared backbone, and decoder.

### World Models And Agents

Use a closed loop: observation -> encoder/state -> dynamics/imagination -> policy/action -> environment. Visually separate real interaction from imagined rollout with line style or background band.

### Geometry / Neural Rendering / 3D

Use spatial anchors: cameras/rays/points/Gaussians/coordinates -> field or representation -> renderer -> image. Keep network blocks secondary to geometry. Preserve coordinate frame and viewing direction.

### Graph And Scientific AI

Use encoder -> processor/message passing -> decoder, plus the physical grid/mesh or structural representation. Distinguish observed variables, latent graph state, and predicted physical fields. Use small multiples only for true multi-scale or temporal evolution.

### Diffusion / Flow Matching

Distinguish probability path, learned vector/score field, condition, sampler/integrator, and decoder. Do not jump directly from fused velocity to a final image when ODE/SDE integration is part of the method.

## 7. Typography And Geometry

- Prefer white or very light gray backgrounds.
- Use small, consistent corner radii equivalent to 4-8 px.
- Avoid heavy shadows and thick black borders.
- Use three type sizes: stage title, module label, annotation.
- Use noun phrases for modules and verbs only on arrows/operations.
- Keep formulas beside the transformation they define.
- Check readability at intended single- or double-column width.
- Do not scale font size by viewport width.
- Use whitespace as routing corridors, not as unused canvas.

## 8. Results And Evidence

Use output examples when they demonstrate the claimed behavior. Mark edited/preserved regions with restrained outlines or overlays. Keep result thumbnails aligned and comparable. Do not use placeholders such as `xxx`, `text`, `edited`, or random heatmap numbers in final figures.

## 9. Style Selection Protocol

1. Run `scripts/list_styles.py` or read `style-catalog.md`.
2. Present 2-3 compatible choices when the user has not specified a style.
3. Recommend one choice and explain the narrative fit in one sentence.
4. Record the selected style ID before drawing.
5. Apply its layout, palette, shape vocabulary, and avoid rules consistently.
6. If mixing styles, name one primary style and at most one secondary accent style.

Never mix three visual systems in one figure.

## 10. Anti-Patterns

- Large empty slide containing a narrow, compressed diagram strip.
- Giant dashed container with a tiny title.
- Nested decorative cards and inconsistent radii.
- Repeated random heatmap values with no analytic meaning.
- Many arrow colors without a legend or stable semantics.
- Raw code, raw XML, broken LaTeX, or unexplained abbreviations.
- A fusion equation drawn as an ordinary process box.
- Full architecture duplicated once per time step, expert, or modality.
- Capability collage used as a substitute for explaining the method.
- Architecture rendered as one image when editable objects were requested.
