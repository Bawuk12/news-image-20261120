# news-image-20261120 entry (Python 3.13, standard library only).
# The image beside this file sums up Friday 20 November 2026's world
# news: the Shenzhen Trump-Xi-Putin summit, Russia's bombardment of
# Kyiv, the global stock slide, the ICJ Rohingya ruling, tankers struck
# in the Strait of Hormuz, and more. This program copies the image to
# /output/entry.png; the grader runs it twice and both runs must write
# the same bytes, so the copy is byte-for-byte with no timestamps.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
