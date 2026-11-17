"""Decode the split base64 weights into model.bin. Python 3.8+; no dependencies."""
import base64
import hashlib
import json
from pathlib import Path

def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as source:
        while block := source.read(8 * 1024 * 1024):
            value.update(block)
    return value.hexdigest()

def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    for name, expected in manifest["files"].items():
        if name != "model.bin" and digest(root / name) != expected:
            raise SystemExit(f"Checksum failed: {name}. Download the folder again.")
    target = root / "model.bin"
    if target.exists():
        if digest(target) == manifest["files"]["model.bin"]:
            print("model.bin already exists and is verified.")
            return
        raise SystemExit("model.bin already exists but differs. Move it aside first.")
    temporary = root / "model.bin.partial"
    output = temporary.open("xb")
    original_hash = hashlib.sha256()
    encoded_hash = hashlib.sha256()
    total = 0
    try:
        with output:
            for part in manifest["base64_parts"]:
                path = root / part["name"]
                part_hash = hashlib.sha256()
                part_size = 0
                with path.open("rb") as source:
                    while block := source.read(8 * 1024 * 1024):
                        encoded_hash.update(block)
                        part_hash.update(block)
                        part_size += len(block)
                        decoded = base64.b64decode(block, validate=True)
                        output.write(decoded)
                        original_hash.update(decoded)
                        total += len(decoded)
                if part_hash.hexdigest() != part["sha256"] or part_size != part["size"]:
                    raise ValueError(f"Corrupt part: {path.name}")
                print(f"Decoded {path.name}", flush=True)
        if encoded_hash.hexdigest() != manifest["base64_sha256"]:
            raise ValueError("Combined base64 SHA-256 mismatch")
        if original_hash.hexdigest() != manifest["files"]["model.bin"] or total != manifest["model_bytes"]:
            raise ValueError("Decoded model.bin SHA-256 or size mismatch")
        temporary.rename(target)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    print("Ready: model.bin restored and SHA-256 verified.")

if __name__ == "__main__":
    main()
