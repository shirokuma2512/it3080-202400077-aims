"""Audit historical releases without changing the checkout (stdlib only)."""
import argparse
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git', help='Path to the Git executable')
    args = parser.parse_args()
    portable = ROOT / '.tools/git/cmd/git.exe'
    git = args.git or shutil.which('git') or (str(portable) if portable.exists() else None)
    if not git:
        parser.error('Install Git >= 2.40 or pass --git PATH')

    def command(*parts):
        return subprocess.check_output([git, *parts], cwd=ROOT, text=True, encoding='utf-8').strip()

    def release_ref(branch):
        for candidate in (branch, 'origin/' + branch):
            probe = subprocess.run([git, 'rev-parse', '--verify', candidate], cwd=ROOT,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if probe.returncode == 0:
                return candidate
        raise RuntimeError(f'Missing {branch}: fetch the complete repository history first')

    expected = {
        'v0.1.0': (None, False, False, False),
        'v0.2.0': (None, False, False, False),
        'v0.3.0': (None, False, False, False),
        'v1.0.0': ('1.0.0', False, False, False),
        'v1.0.1': ('1.0.1', True, False, False),
        'v1.1.0': ('1.1.0', True, True, True),
        'master': ('1.1.0', True, True, True),
    }
    forbidden = {'__pycache__', '.tools', '.venv', 'tmp', 'output', '.git'}
    for ref, (version, fixed, sorting, category) in expected.items():
        if ref != 'master':
            assert command('cat-file', '-t', ref) == 'tag', f'{ref}: not annotated'
        files = command('ls-tree', '-r', '--name-only', ref).splitlines()
        assert all(not forbidden.intersection(PurePosixPath(p).parts) for p in files), ref
        assert not any(p.endswith(('.pyc', '.pyo', '.zip', '.pem')) for p in files), ref
        with tempfile.TemporaryDirectory(prefix='aims-audit-') as directory:
            directory = Path(directory)
            archive = directory / 'source.zip'
            subprocess.run([git, 'archive', '--format=zip', '-o', str(archive), ref],
                           cwd=ROOT, check=True)
            with zipfile.ZipFile(archive) as source:
                source.extractall(directory / 'source')
            source_root = directory / 'source'
            demo = subprocess.check_output([sys.executable, 'main.py'], cwd=source_root,
                                           text=True, encoding='utf-8', env=_python_env())
            assert 'Total cost: 63.89 $' in demo, ref
            if version:
                assert demo.splitlines()[0] == f'AIMS-mini v{version}', ref
            if (source_root / 'tests').exists():
                subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                               cwd=source_root, check=True, env=_python_env())
            if ref not in ('v0.1.0',):
                code = (
                    'from aims.cart import Cart; '
                    'from aims.dvd import DigitalVideoDisc as D; '
                    'from aims.search import search_by_title; '
                    f'assert len(search_by_title([D("The Lion King")], "lion")) == {int(fixed)}; '
                    f'assert hasattr(Cart, "sort_by_cost") == {sorting}; '
                    'import aims.search as s; '
                    f'assert hasattr(s, "search_by_category") == {category}'
                )
                subprocess.run([sys.executable, '-c', code], cwd=source_root, check=True,
                               env=_python_env())
            print(f'{ref}: demo, version, tests, features and tracked-file audit OK', flush=True)

    patch_files = set(command('diff', '--name-only', 'v1.0.0', 'v1.0.1').splitlines())
    assert patch_files == {'aims/search.py', 'tests/test_search.py', 'aims/__init__.py', 'CHANGELOG.md'}
    for tag, branch in [('v1.0.1', 'release/lab04'), ('v1.1.0', 'release/lab05')]:
        assert command('rev-parse', f'{tag}^{{}}') == command('rev-parse', release_ref(branch))
    old_release = release_ref('release/lab04')
    fixes = command('log', old_release, '--format=%H', '--fixed-strings',
                    '--grep=fix: make title search case-insensitive').splitlines()
    assert len(fixes) == 1, fixes
    fix = fixes[0]
    copies = command('log', '--all', '--format=%H', '--grep', f'cherry picked from commit {fix}').splitlines()
    assert len(copies) == 2, copies
    for ref in ('master', 'release/lab05'):
        comparison = command('cherry', '-v', ref if ref == 'master' else release_ref(ref), old_release).splitlines()
        assert any(line.startswith('- ' + fix + ' ') for line in comparison), (ref, comparison)
    print('Hotfix: four-file patch, release pointers, two cherry-picks and patch equivalence OK')


def _python_env():
    import os
    return dict(os.environ, PYTHONIOENCODING='utf-8')


if __name__ == '__main__':
    main()
