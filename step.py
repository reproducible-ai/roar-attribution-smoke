import sys, pathlib
out = pathlib.Path(sys.argv[1]); out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(f"p023 repro output from {sys.argv[0]}\n")
print("wrote", out)
