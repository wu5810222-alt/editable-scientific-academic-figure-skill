# Style Evidence From Representative Papers

This file records the visual observations that informed the reusable styles. Treat venue/year metadata as bibliographic context; use the papers themselves for exact method claims.

| Paper | Reusable visual observation | Style mapping |
| --- | --- | --- |
| [ViT](https://arxiv.org/abs/2010.11929) | Image patches become aligned token tiles; one compact transformer block represents repetition. | `token-grid` |
| [MAE](https://arxiv.org/abs/2111.06377) | Visible/masked patches are distinguished spatially; asymmetric encoder-decoder is shown without drawing every layer. | `token-grid` |
| [Swin Transformer](https://arxiv.org/abs/2103.14030) | Staged spatial hierarchy plus a separate repeated-block inset. | `hierarchical-pyramid` |
| [ConvNeXt](https://arxiv.org/abs/2201.03545) | Architecture evolution is communicated through controlled stage comparisons rather than a decorative pipeline. | `hierarchical-pyramid` |
| [DETR](https://arxiv.org/abs/2005.12872) | Figure 1 explains the set-prediction contribution with a short pipeline; detailed architecture moves to Figure 2. | `clean-pipeline`, `query-decoder` |
| [Mask2Former](https://arxiv.org/abs/2112.01527) | Sparse learnable queries interact with dense mask features; attention scope is visually constrained. | `query-decoder` |
| [Segment Anything](https://arxiv.org/abs/2304.02643) | System-level contribution is established before the detailed image encoder/prompt encoder/mask decoder diagram. | `result-first-editorial`, `query-decoder` |
| [SAM 2](https://arxiv.org/abs/2408.00714) | Streaming video adds persistent memory and temporal interaction to the promptable image architecture. | `recurrent-state`, `query-decoder` |
| [Mamba](https://arxiv.org/abs/2312.00752) | State-space evolution and input-dependent selection are shown as structured signal paths, followed by a block inset. | `recurrent-state` |
| [Mamba-2](https://arxiv.org/abs/2405.21060) | Theoretical correspondence is shown with sparse mathematical schematics rather than colorful module cards. | `recurrent-state` |
| [Switch Transformer](https://arxiv.org/abs/2101.03961) | Router and selected experts form a clear sparse fan-out/fan-in pattern; token routing gets its own explanatory figure. | `sparse-routing` |
| [DeepSeek-V3](https://arxiv.org/abs/2412.19437) | Large-system architecture distinguishes shared core, sparse experts, auxiliary objectives, and training system boundaries. | `sparse-routing`, `system-swimlane` |
| [Perceiver IO](https://arxiv.org/abs/2107.14795) | Arbitrary inputs and outputs are mediated by a fixed latent array and output queries. | `token-grid`, `system-swimlane` |
| [NeRF](https://arxiv.org/abs/2003.08934) | Rays, sampled coordinates, radiance field, volume rendering, and novel view form a physically grounded pipeline. | `geometry-field` |
| [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079) | Representation and rendering are explained with real spatial point/Gaussian visuals; densification receives a separate mechanism figure. | `geometry-field` |
| [GraphCast](https://arxiv.org/abs/2212.12794) | Physical grid, multimesh graph, message passing, and decoded weather fields are kept visually distinct. | `scientific-graph` |
| [DreamerV3](https://arxiv.org/abs/2301.04104) | Training architecture is a loop among world model, imagined trajectories, critic, and actor. | `closed-loop-agent`, `recurrent-state` |
| [Genie](https://arxiv.org/abs/2402.15391) | Interactive environment generation is communicated through temporal frames, latent actions, and autoregressive dynamics. | `closed-loop-agent` |
| [RT-2](https://arxiv.org/abs/2307.15818) | Web-scale vision-language knowledge and robot actions are presented as connected system stages with real examples. | `system-swimlane`, `closed-loop-agent` |
| [DINOv2](https://arxiv.org/abs/2304.07193) | Feature visualizations and data pipeline evidence dominate; the backbone itself is not overdrawn. | `result-first-editorial`, `system-swimlane` |
| [Llama 3](https://arxiv.org/abs/2407.21783) | Technical-report figures favor restrained system diagrams, phase separation, and quantitative evidence over decorative blocks. | `system-swimlane` |
| [Qwen2-VL](https://arxiv.org/abs/2409.12191) | Capability results are separated from positional/token innovations such as multimodal RoPE. | `result-first-editorial`, `token-grid` |

General inference: strong papers frequently use different figures for the task-level insight, the complete system, and the novel internal block. This is why the skill must select both a figure purpose and a style.
