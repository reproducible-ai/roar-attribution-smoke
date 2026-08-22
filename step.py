import sys, pathlib

# argv[2] is an optional nonce. Artifact identity in GLaaS is content-addressed,
# so a byte-identical artifact across runs collides with whatever scope first
# registered it -- and a delegated registration may then not be allowed to read
# its own output.
out = pathlib.Path(sys.argv[1])
out.parent.mkdir(parents=True, exist_ok=True)
nonce = sys.argv[2] if len(sys.argv) > 2 else "static"
out.write_text(f"smoke artifact {nonce}\n")
print("wrote", out)
