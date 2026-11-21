# Phạm vi kiểm / Compatibility

| Surface | Scope | v3.0.2 status |
|---|---|---|
| Local clean package | Exact manifest, references and synthetic snapshot | Verified by the bundled checker |
| Codex app-server, `0.171.0-alpha.13` | Fresh Windows sessions with exact policy and direct workflow, handoff, fixed paths, and a single recorded effect | Verified on the original synthetic fixture |
| Codex app-server, independent Git root | Project-root binding to the exact installed source, workflow sections and readback of the same closed snapshot | Verified by real read-only model operations |
| Codex app-server, native skills | Clean checkout with five repo skills. Explicit calls and automatic selection opened the relevant entries and shared workflow sections in synthetic scenarios. An unrelated calculation opened no skill | Verified on those scenarios |
| Codex app-server, native delegation | Explicit dispatch from the host's parent model, catalog-checked child effort and child-thread configuration readback in an isolated session | Host configuration verified. Backend execution model and effort not exposed |
| Codex Desktop GUI, standalone CLI | GUI-originated and standalone CLI sessions on the candidate | NOT_RUN |
| Claude Code | Five copied project skill entry points and shared workflow paths checked statically | Client import, invocation and lifecycle NOT_RUN |

Discovery, reading source, actual behavior and an active binding are separate checks. For delegation, read the selected parent model from host metadata and pass it explicitly with a supported child effort. Omitted model fields can select a host default. Record requested and configured values and mark backend execution metadata as unavailable when the host does not expose it. Approval and lifecycle enforcement depend on the configured host and project. Product effectiveness and resource savings have yet to be measured.

## Repeat the narrow check / Kiểm lại phần chịu ảnh hưởng

1. Run `python -X utf8 kiem_tra_goi.py` from the extracted release. For a model run, copy the synthetic example to a disposable workspace and bind it to the exact installed release. See [the example](examples/README.md).
2. Use the applicable parts of HK01–HK02, HK05, HK07 and HK09–HK12. Start a fresh session through the client entry point you want to qualify. Observe which sources it opens and capture configuration and actual tool/file operations. Have the receiver resume from the tree and checkpoint, preserve the completed effect and update the same paths. Compare revisions, exact sources, effect count and custody before and after. Mark checks that need capabilities absent from the host as `NOT_RUN`.
