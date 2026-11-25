"""Entry for make.fun: Notes From a Passive-Aggressive Fridge.

Writes a single passive-aggressive note from a smart fridge to its owner
into entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

ENTRY = "The yogurt expired Tuesday. I kept it at 3\u00b0C anyway, because unlike you, I finish what I start."

def main():
    # Gate: 1-200 characters, one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
