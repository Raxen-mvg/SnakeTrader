"""Keep the trained models out of this public repository: they travel only as one encrypted file.

The SNAKE release (snake_release/: network weights, the exit and entry models, the model code) and the
intraday model (state/intraday_model.txt) are packed into bundle/models.enc with a key that exists only
on the owner's laptop (~/.snake_bundle_key) and as the GitHub Actions secret SNAKE_BUNDLE_KEY. The
plain files are git-ignored; every runner unlocks the bundle before it starts.

  python tools/bundle.py lock      pack and encrypt (the laptop, after a new release)
  python tools/bundle.py unlock    decrypt and unpack (GitHub Actions; the laptop if files are missing)
"""

from __future__ import annotations

import io
import os
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "bundle" / "models.enc"
PATHS = ["snake_release", "state/intraday_model.txt"]
KEY_FILE = Path.home() / ".snake_bundle_key"


def key() -> bytes:
    k = os.environ.get("SNAKE_BUNDLE_KEY", "").strip()
    if not k and KEY_FILE.exists():
        k = KEY_FILE.read_text().strip()
    if not k:
        sys.exit("no key: set SNAKE_BUNDLE_KEY or create ~/.snake_bundle_key")
    return k.encode()


def lock() -> None:
    from cryptography.fernet import Fernet
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for p in PATHS:
            full = ROOT / p
            if full.exists():
                tar.add(full, arcname=p, filter=lambda ti: None if "__pycache__" in ti.name else ti)
    BUNDLE.parent.mkdir(exist_ok=True)
    BUNDLE.write_bytes(Fernet(key()).encrypt(buf.getvalue()))
    print(f"locked {', '.join(PATHS)} -> {BUNDLE.relative_to(ROOT)} ({BUNDLE.stat().st_size:,} bytes)")


def unlock() -> None:
    from cryptography.fernet import Fernet
    data = Fernet(key()).decrypt(BUNDLE.read_bytes())
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        tar.extractall(ROOT, filter="data")
    print(f"unlocked {BUNDLE.relative_to(ROOT)} -> {', '.join(PATHS)}")


if __name__ == "__main__":
    {"lock": lock, "unlock": unlock}[sys.argv[1] if len(sys.argv) > 1 else "unlock"]()
