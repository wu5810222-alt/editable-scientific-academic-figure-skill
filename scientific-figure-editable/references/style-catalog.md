# Architecture Figure Style Catalog

Use the style ID verbatim in planning notes and deliverable summaries. These styles describe information organization, not just color.

## Selection Matrix

| Method structure | Recommended style | Secondary option |
| --- | --- | --- |
| Simple end-to-end novelty | `clean-pipeline` | `result-first-editorial` |
| Tokens, patches, queries, masks | `token-grid` | `query-decoder` |
| Multi-scale vision backbone | `hierarchical-pyramid` | `clean-pipeline` |
| Detection/segmentation/prompts | `query-decoder` | `token-grid` |
| SSM, video memory, world model | `recurrent-state` | `closed-loop-agent` |
| MoE or conditional compute | `sparse-routing` | `system-swimlane` |
| Multimodal LLM or training system | `system-swimlane` | `result-first-editorial` |
| NeRF, 3DGS, spatial field | `geometry-field` | `clean-pipeline` |
| Robotics/world model | `closed-loop-agent` | `system-swimlane` |
| Weather, molecule, mesh, graph | `scientific-graph` | `hierarchical-pyramid` |

## `clean-pipeline`

**Influences:** DETR concept figure, NeRF overview, classical encoder-decoder papers.  
**Use for:** one dominant left-to-right computation with 4-8 stages.  
**Layout:** input thumbnail -> encoder/core -> novel module -> output; one baseline or loss branch may sit below.  
**Visual language:** white background, thin black/gray strokes, compact rectangular modules, one saturated accent for the contribution.  
**Strength:** fastest comprehension and easiest Draw.io/PPTX editing.  
**Avoid:** large enclosing cards, multiple feedback loops, dense matrices.

## `token-grid`

**Influences:** ViT, MAE, Perceiver IO, Qwen2-VL positional/token diagrams.  
**Use for:** patchification, token masking, latent arrays, query construction, positional organization.  
**Layout:** visual/input grid on the left, token strip or matrix in the center, repeated backbone block, output tokens/head on the right.  
**Visual language:** aligned square tiles, restrained categorical colors, braces for groups, dotted outlines for masked/missing tokens.  
**Strength:** makes representation shape and token correspondence explicit.  
**Avoid:** labeling every token, random cell values, excessive rainbow colors.

## `hierarchical-pyramid`

**Influences:** Swin Transformer, ConvNeXt comparisons, feature-pyramid vision systems.  
**Use for:** spatial downsampling, multi-resolution features, coarse-to-fine processing.  
**Layout:** four aligned stages whose spatial tiles shrink while channels/depth increase; include one zoomed block inset.  
**Visual language:** stepped bands, shallow 3D-like feature stacks only when needed, same hue with controlled value changes plus one contribution accent.  
**Strength:** communicates scale transitions immediately.  
**Avoid:** equal-sized stage boxes, perspective decoration without dimension labels.

## `query-decoder`

**Influences:** DETR, Mask2Former, SAM.  
**Use for:** object queries, mask queries, prompts, set prediction, promptable outputs.  
**Layout:** dense image feature lane plus sparse query/prompt lane -> decoder/cross-attention -> parallel output set/masks.  
**Visual language:** feature maps as grids, queries as circles or short token strips, correspondence lines used sparingly, output masks overlaid on real images.  
**Strength:** separates dense evidence from sparse control.  
**Avoid:** crossing every query to every pixel; show one symbolic attention relation instead.

## `recurrent-state`

**Influences:** Mamba selective SSM, SAM 2 memory, DreamerV3 world-model state.  
**Use for:** recurrent state, selective scan, temporal memory, streaming video, latent dynamics.  
**Layout:** horizontal time/input line with a parallel persistent state or memory line; use one loop/back edge and one expanded cell/block inset.  
**Visual language:** repeated time markers, state circles/bars, selective gates highlighted by input-dependent color, dashed temporal memory links.  
**Strength:** exposes what persists and what changes over time.  
**Avoid:** duplicating the full model for every frame; ambiguous arrows pointing both forward and backward.

## `sparse-routing`

**Influences:** Switch Transformer, DeepSeek-V3 MoE.  
**Use for:** routers, top-k experts, conditional computation, multi-branch specialization.  
**Layout:** tokens -> router scores -> sparse fan-out to expert bank -> weighted merge -> shared continuation.  
**Visual language:** experts as aligned small modules, selected routes saturated, inactive routes light gray, capacity/load annotations outside the main path.  
**Strength:** makes sparsity and sharing visible.  
**Avoid:** coloring every expert differently, drawing all-to-all routing, omitting the merge.

## `system-swimlane`

**Influences:** large multimodal model reports, RT-2, Llama/Qwen technical systems, data-engine/model-engine diagrams.  
**Use for:** multiple encoders/adapters, data pipelines, pretraining/post-training, foundation-model systems.  
**Layout:** horizontal or vertical lanes for data/encoders, shared backbone, training objectives, adapters/decoders, outputs.  
**Visual language:** neutral shared core, modality-specific edge colors, phase bands instead of nested cards, numbered contribution badges.  
**Strength:** handles complex systems without losing ownership boundaries.  
**Avoid:** tiny modules across the entire slide, unexplained line crossings, mixing training and inference without phase labels.

## `geometry-field`

**Influences:** NeRF, 3D Gaussian Splatting, flow/trajectory figures.  
**Use for:** cameras, rays, points, fields, trajectories, rendering, continuous coordinates.  
**Layout:** spatial scene or coordinate representation dominates the center; small network/field module connects coordinates to properties; renderer/integrator leads to view/output.  
**Visual language:** real or schematic cameras/rays/point clouds, coordinate labels, thin trajectory lines, limited green/cyan/orange accents.  
**Strength:** preserves physical intuition instead of hiding it inside boxes.  
**Avoid:** turning every geometric operation into a generic rectangle; decorative 3D perspective that changes the meaning.

## `closed-loop-agent`

**Influences:** DreamerV3, Genie, RT-2 and robotics policy diagrams.  
**Use for:** observation-action loops, world models, imagined rollouts, policies, environment interaction.  
**Layout:** environment -> observation encoder -> latent/world model -> policy/action -> environment; place imagined rollout inside a distinct inner band.  
**Visual language:** real interaction in solid blue, imagination in dashed amber, state/memory in green, reward/value heads as compact side branches.  
**Strength:** distinguishes learning inside the model from actions in the world.  
**Avoid:** an open pipeline that omits feedback; mixing real frames and imagined frames without labels.

## `scientific-graph`

**Influences:** GraphCast and graph/mesh-based scientific learning systems.  
**Use for:** physical grids, meshes, molecular graphs, weather fields, PDE surrogates, structured scientific states.  
**Layout:** observations/grid -> graph construction/encoder -> repeated message-passing processor -> decoder -> predicted physical field; use an inset for local connectivity.  
**Visual language:** graph nodes/edges, maps or fields as real scientific visual assets, cool neutral palette with one warm prediction/error accent.  
**Strength:** keeps physical representation and neural computation distinct.  
**Avoid:** generic MLP boxes without the underlying graph/mesh; decorative network graphs unrelated to the actual discretization.

## `result-first-editorial`

**Influences:** SAM system overview, DINOv2 feature visualizations, modern foundation-model reports.  
**Use for:** capability-first overview when qualitative behavior is a major contribution.  
**Layout:** large real result strip or central example, with a compact mechanism diagram below/alongside and 2-3 labeled capability callouts.  
**Visual language:** high-quality aligned samples, white background, minimal boxes, one brand-neutral accent, short captions.  
**Strength:** creates immediate evidence and visual impact.  
**Avoid:** capability collage without mechanism, inconsistent sample crops, marketing slogans.

## Mixing Styles

Allowed combinations:

- `result-first-editorial` overview + `clean-pipeline` mechanism.
- `system-swimlane` macro architecture + `token-grid` inset.
- `hierarchical-pyramid` backbone + `query-decoder` head.
- `closed-loop-agent` outer loop + `recurrent-state` world-model inset.
- `geometry-field` main scene + `clean-pipeline` training path.

Name one primary style. Use at most one secondary style in a clearly bounded inset.
