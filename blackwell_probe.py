import pathlib
import sys

import torch


if not torch.cuda.is_available():
    raise SystemExit("CUDA is not available")

device = torch.device("cuda:0")
major, minor = torch.cuda.get_device_capability(device)
if (major, minor) != (12, 0):
    raise SystemExit(f"expected CUDA capability 12.0, got {major}.{minor}")

a = torch.arange(4096, device=device, dtype=torch.float32).reshape(64, 64)
b = torch.eye(64, device=device, dtype=torch.float32)
c = torch.matmul(a, b)
torch.cuda.synchronize(device)
if not torch.equal(a, c):
    raise SystemExit("CUDA matmul result did not match the positive control")

out = pathlib.Path(sys.argv[1])
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(
    f"device={torch.cuda.get_device_name(device)}\n"
    f"capability=sm_{major}{minor}\n"
    f"matmul_checksum={c.sum().item():.1f}\n"
)
print(out.read_text(), end="")
