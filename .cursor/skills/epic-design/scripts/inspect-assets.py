#!/usr/bin/env python3
"""Inspect image assets for epic-design pipeline (format, alpha, background heuristic)."""
from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore


def inspect_png(path: Path) -> dict:
    with path.open("rb") as f:
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            return {"format": "unknown", "error": "not a PNG"}
        f.read(4)
        chunk_len = struct.unpack(">I", f.read(4))[0]
        chunk_type = f.read(4)
        if chunk_type != b"IHDR":
            return {"format": "png", "error": "missing IHDR"}
        w, h = struct.unpack(">II", f.read(8))
        bit_depth, color_type = struct.unpack(">BB", f.read(2))
        has_alpha = color_type in (4, 6)
    return {"format": "png", "width": w, "height": h, "has_alpha_channel": has_alpha}


def inspect_jpeg(path: Path) -> dict:
    return {"format": "jpeg", "has_alpha_channel": False, "note": "JPEG cannot store transparency"}


def background_guess(path: Path, meta: dict) -> str:
    if meta.get("format") == "jpeg":
        return "solid_or_photo — keep if used as section background; remove only for floating depth-2/3 assets"
    if not meta.get("has_alpha_channel"):
        return "opaque — likely needs cutout if used as floating product/logo at depth-2/3"
    if Image is None:
        return "alpha present (install Pillow for corner transparency check)"
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    corners = [img.getpixel((0, 0)), img.getpixel((w - 1, 0)), img.getpixel((0, h - 1)), img.getpixel((w - 1, h - 1))]
    transparent_corners = sum(1 for p in corners if p[3] < 32)
    if transparent_corners >= 3:
        return "clean_cutout — use directly at depth-2/3"
    return "mixed_alpha — review visually; may be fake transparency on solid backdrop"


def inspect_file(path: Path) -> dict:
    ext = path.suffix.lower()
    if ext in (".jpg", ".jpeg"):
        meta = inspect_jpeg(path)
    elif ext == ".png":
        meta = inspect_png(path)
    elif ext == ".webp" and Image:
        img = Image.open(path)
        meta = {"format": "webp", "width": img.width, "height": img.height, "has_alpha_channel": img.mode in ("RGBA", "LA")}
    else:
        return {"path": str(path), "status": "skip", "reason": f"unsupported extension {ext}"}
    return {
        "path": str(path),
        "size_kb": round(path.stat().st_size / 1024, 1),
        **meta,
        "background_assessment": background_guess(path, meta),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Epic-design asset inspector")
    parser.add_argument("paths", nargs="+", help="Image files or directories")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    files: list[Path] = []
    for raw in args.paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.glob("**/*")))
        else:
            files.append(p)
    files = [f for f in files if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]

    if not files:
        print("No image files found.", file=sys.stderr)
        return 1

    if Image is None:
        print("Tip: pip install Pillow for richer alpha/background analysis", file=sys.stderr)

    reports = [inspect_file(f) for f in files]
    if args.json:
        print(json.dumps(reports, indent=2, ensure_ascii=False))
    else:
        for r in reports:
            print(f"\n{r['path']}")
            for k, v in r.items():
                if k != "path":
                    print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
