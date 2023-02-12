import jinja2
from pathlib import Path
from itertools import chain
import subprocess

def render(template, file, **context):
    with open(template) as f:
        template = jinja2.Template(f.read())
        with open(file, 'w') as f:
            f.write(template.render(**context))
        subprocess.run(['lualatex', "-interaction=nonstopmode", "-shell-escape", file], cwd=Path(file).parent)
        for p in chain(*map(lambda x: Path('.').rglob(f"*.{x}"), ["aux", "log", "out"])):
            p.unlink()
