

import zipfile
import hashlib
import sys
from pathlib import Path
from typing import List, Tuple

# ========== USER CONFIG ==========
ZIP_PATH = "Data/task2.zip"   # path to the downloaded archive (change if needed)
EMAIL = "sajibulislampersonal"  # put your email here (will be lowercased automatically)
# ================================

def sha3_256_hex(data: bytes) -> str:
    h = hashlib.sha3_256()
    h.update(data)
    return h.hexdigest()  # already lowercase

def product_key_from_hexhash(hexhash: str) -> int:
    # hexhash is 64 hex chars (0-9a-f). For each hex digit d:
    #  - digit_value = int(d, 16)  (0..15)
    #  - factor = digit_value + 1  (1..16)
    # product over 64 factors -> big integer
    prod = 1
    for ch in hexhash:
        dv = int(ch, 16)
        prod *= (dv + 1)
    return prod

def main(zip_path: str, email: str):
    zip_path = Path(zip_path)
    if not zip_path.exists():
        print(f"Error: zip file not found at {zip_path}", file=sys.stderr)
        sys.exit(2)

    with zipfile.ZipFile(zip_path, "r") as z:
        # list all file entries that are files (not directories)
        namelist = [n for n in z.namelist() if not n.endswith("/")]

        # If the zip contains folders and you only want top-level files,
        # modify filter accordingly. The task likely expects exactly 256 files total.
        files = namelist

        print(f"Found {len(files)} files in archive (counting files only).")
        if len(files) != 256:
            print("Warning: expected exactly 256 files. The task requires processing exactly 256 files.", file=sys.stderr)
            # We continue, but you should check if your zip layout differs (subfolders, extra files).
            # Optionally you can sys.exit(1) to force an exact count.
            # sys.exit(1)

        hashes_and_keys: List[Tuple[str, int]] = []

        for fname in sorted(files):
            data = z.read(fname)  # bytes
            h = sha3_256_hex(data)
            if len(h) != 64:
                print(f"Error: unexpected hash length for {fname}: {h}", file=sys.stderr)
                sys.exit(3)
            key = product_key_from_hexhash(h)
            hashes_and_keys.append((h, key))

        # sort by key ascending; stable sort but keys may collide rarely
        hashes_and_keys.sort(key=lambda x: x[1])

        sorted_hashes = [hk[0] for hk in hashes_and_keys]
        joined = "".join(sorted_hashes)  # NO separator
        final_input = joined + email.lower()

        # Show some info
        print(f"Number of file-hashes computed: {len(sorted_hashes)}")
        print("First 3 sorted hashes (for quick sanity check):")
        for i, h in enumerate(sorted_hashes[:3], 1):
            print(f" {i}: {h}")

        # compute final sha3-256
        final_hash = sha3_256_hex(final_input.encode("utf-8"))
        print("\nFINAL SHA3-256 (lowercase hex):")
        print(final_hash)
        print("\nCommand to send (replace email and hash if you want to re-run):")
        print(f"!task2 {email.lower()} {final_hash}")

if __name__ == "__main__":
    main(ZIP_PATH, EMAIL)
