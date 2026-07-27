# Scientific Figure Editable

A Codex skill for designing, reconstructing, reviewing, and delivering publication-ready scientific method figures as native editable Draw.io and PowerPoint files.

It provides selectable architecture styles for pipelines, token models, hierarchical vision, query decoders, recurrent/state-space models, mixture-of-experts, multimodal foundation models, agents/world models, neural rendering/3D, and graph/scientific AI.

## Install

Copy the skill folder into your Codex skills directory:

```bash
cp -r scientific-figure-editable "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Or install it from GitHub using the Codex skill installer and the repository/path containing `SKILL.md`.

## Included Resources

- `SKILL.md`: trigger description and core workflow.
- `references/design-rules.md`: scientific figure design rules.
- `references/style-catalog.md`: selectable style definitions.
- `references/style-presets.yaml`: machine-readable style tokens.
- `references/style-evidence.md`: representative-paper evidence.
- `references/drawio-workflow.md`: native Draw.io authoring and export workflow.
- `references/pptx-workflow.md`: object-level editable PPTX requirements.
- `scripts/list_styles.py`: list available styles.
- `scripts/audit_pptx.py`: audit whether a PPTX is composed of native objects.
- `assets/semgate-geoflow-style-template.drawio`: editable example template.

## Requirements

- Python 3
- PyYAML for `list_styles.py`
- `python-pptx` for `audit_pptx.py`
- Draw.io desktop CLI for Draw.io rendering/export

## Validation

Use the Codex `skill-creator` validator:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py scientific-figure-editable
```

## License

MIT
