import python_latex
from pathlib import Path

cwd = Path(__file__).parent

picture = []
for i in range(1, 7):
    picture.append(f"\\node ({i}) at (-1.5*{i},0) {{{i}}};")
for k, bend in [(1, ""), (2, "bend left"), (3, "bend right")]:
    for i in range(1, 6-k+1):
        picture.append(f"\\draw[->, >=latex] ({i+k}) to[{bend}] ({i});")

python_latex.render(cwd/"template.tex", cwd/"test.tex", picture=picture)
