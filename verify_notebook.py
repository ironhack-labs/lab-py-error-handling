import json
import builtins
from pathlib import Path

builtins.input = lambda prompt="": "42"
path = Path("lab-error_handling.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))

for i, cell in enumerate(nb["cells"], 1):
    if cell.get("cell_type") != "code":
        continue
    source = "".join(cell.get("source", []))
    if not source.strip():
        continue
    print(f"Running cell {i}")
    exec(compile(source, f"{path.name} cell {i}", "exec"), {})

print("NOTEBOOK VERIFICATION COMPLETE")
