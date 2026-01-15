from pathlib import Path
from datetime import datetime

out_path = Path(snakemake.output[0])
out_path.parent.mkdir(parents=True, exist_ok=True)

out_path.write_text(
    "Hello from Snakemake + Python!\n"
    f"Timestamp: {datetime.now().isoformat(timespec='seconds')}\n"
)
print(f"Wrote: {out_path}")
