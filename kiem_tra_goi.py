"""Check bundle bytes and the synthetic example. Does not run a coding agent."""

import argparse
import hashlib
import json
import posixpath
import re
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_files(source):
    if source.is_dir():
        return {p.relative_to(source).as_posix(): p.read_bytes()
                for p in source.rglob('*') if p.is_file() and '.git' not in p.relative_to(source).parts}
    with ZipFile(source) as archive:
        files = {}
        folded = set()
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            name = PurePosixPath(entry.filename)
            key = entry.filename.casefold()
            if name.is_absolute() or '..' in name.parts or ':' in entry.filename or '\\' in entry.filename or key in folded:
                raise ValueError(f'Unsafe or duplicate entry: {entry.filename}')
            folded.add(key)
            files[entry.filename] = archive.read(entry)
        return files


def verify(files):
    manifest = json.loads(files.pop('MANIFEST.json'))
    expected = {row['path']: (row['bytes'], row['sha256']) for row in manifest['files']}
    if (manifest['format'] != 'codex-claude-rule-bundle/v1'
            or len(expected) != len(manifest['files']) or files.keys() != expected.keys()):
        raise ValueError('Manifest path or format mismatch')
    for path, raw in files.items():
        if (len(raw), digest(raw)) != expected[path]:
            raise ValueError(f'Byte mismatch: {path}')
    workflow_name = 'QUY_TRINH_SKILL_VA_AGENT.md'
    workflow = files[workflow_name].decode('utf-8')
    sections = re.findall(r'^## ([4-8])\. Skill `([a-z0-9-]+)`', workflow, re.M)
    skills = {f'.agents/skills/{name}/SKILL.md': (section, name) for section, name in sections}
    if ([section for section, _ in sections] != ['4', '5', '6', '7', '8'] or len(skills) != 5
            or {p for p in files if p.startswith('.agents/skills/')} != skills.keys()):
        raise ValueError('Expected one native skill for each workflow section 4–8')
    for path, (section, name) in skills.items():
        content = files[path].decode('utf-8')
        metadata = re.match(r'^---\nname: ([a-z0-9-]{1,64})\ndescription: "([^"\n]{1,1024})"\n---\n', content)
        pointer = re.search(rf'mục {section} của \[workflow chung\]\(([^)]+)\)', content)
        if not metadata or metadata[1] != name or not pointer:
            raise ValueError(f'Invalid skill metadata or workflow section: {path}')
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), pointer[1]))
        if resolved != workflow_name:
            raise ValueError(f'Broken workflow pointer: {path}')
    tree = files['examples/PROJECT_MAP.md']
    packet = files['examples/Gui_ChatGPT_DEMO.md']
    revision = re.search(rb'^Revision: (\d+)$', tree, re.M)
    if not revision or b'Revision: ' + revision[1] not in packet.splitlines() or digest(tree).encode() not in packet:
        raise ValueError('Example snapshot mismatch')
    return manifest['version'], len(files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        version, count = verify(load_files(args.source))
    except (OSError, KeyError, ValueError) as exc:
        parser.exit(1, f'{exc}\n')
    print(f'{version}: {count} files match; workflow references and synthetic snapshot verified.')
