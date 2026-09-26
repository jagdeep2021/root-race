"""Inline the image and font into src/game.html and write the playable, single-file index.html.

Usage (from the repo root):  python3 src/build.py [extra_copy_path]
The optional path gets a second copy, e.g. the offline file for a showcase laptop.
"""
import base64, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "src/game.html").read_text()
b64 = lambda p: base64.b64encode((root / "src/assets" / p).read_bytes()).decode()
body = (src.replace("__AER__", "data:image/jpeg;base64," + b64("aerenchyma_crosssection.jpg"))
           .replace("__FONT__", "data:font/woff2;base64," + b64("fredoka.woff2")))
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
page = head + body + "\n</html>\n"
(root / "index.html").write_text(page)
for extra in sys.argv[1:]:
    pathlib.Path(extra).write_text(page)
print(f"index.html written ({len(page) // 1024} KB)")
