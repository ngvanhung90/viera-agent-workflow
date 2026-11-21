# Viera Agent Workflow

**DC-PKT-02 · v3.0.2** · [Tiếng Việt](BAT_DAU.md) · [Compatibility](COMPATIBILITY.md)

Viera Agent Workflow gives coding agents a shared way to resume an existing task, identify work already done, verify the artifact on the intended execution path, and hand off the result through the project's existing records. Five skills point to [one workflow](QUY_TRINH_SKILL_VA_AGENT.md). [AGENTS.md](AGENTS.md) is the canonical Vietnamese policy. Projects retain their own approvals, access controls and release gates.

### Try the synthetic example

Extract the ZIP or open a clean checkout at tag `v3.0.2`. From its root, run `python -X utf8 kiem_tra_goi.py` with Python 3.10 or later. Open [the DEMO example](examples/README.md) to see how a fixed project map, packet and checkpoint guide a handoff. The example uses invented identities and grants no rights.

### Install and remove

1. Keep the bundle in a versioned folder. In an authorized project, record the previous binding and any skill entry points you would replace. Point the existing binding to the pinned policy and workflow, and identify the project's existing tree, packet and task record.
2. To try Codex in this repo, open its root with `.agents/skills/`. For another repo, check for naming conflicts and copy the five skill folders into its `.agents/skills/`. The entries use the shared workflow named in the project's binding. `.claude/skills/` is the equivalent layout checked statically. Verify [the Claude bridge](CLAUDE.md) and client behavior before use.
3. Start a fresh session. Verify that the client opens the bound source and applicable workflow section before allowing dependent changes. Use the affected cases in the [migration checks](LENH_CODEX_KIEM_TRA_SAU_THAY_LUAT.txt).
4. To uninstall, restore the exact previous binding and any replaced entries. Remove only the entries added by this install. Start a fresh session and verify the restored source. Keep existing checkpoints, receipts and project data.

### Verification limits

Windows Codex app-server `0.171.0-alpha.13` discovered and exercised all five skills against the shared workflow in synthetic tasks. The Codex Desktop GUI and standalone CLI have yet to be tested on this candidate. Claude Code was checked statically, with runtime behavior unverified. Backend execution model and effort were not exposed. Product adoption, effectiveness and savings remain unverified. Write controls and custody depend on the host and project.

[Migration and rollback](CHUYEN_DOI_LUAT_VA_TIEP_TUC.md) · [Compatibility](COMPATIBILITY.md) · [License](LICENSE) · [Credits](NOTICE.md)
