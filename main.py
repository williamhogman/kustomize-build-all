#!/usr/bin/env python3
import sys
import subprocess
from os import listdir, path

def main(template, set_image):
    overlays = listdir(".")
    tasks = [(overlay, template.format(overlay)) for overlay in overlays if path.isdir(overlay)]
    for (overlay, output) in tasks:
        if set_image is not None:
            subprocess.run(['kustomize', 'edit', 'set', 'image', set_image], cwd="./" + overlay)
        subprocess.run(["kustomize", "build", overlay, "-o", output])

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("kustomize-build-all template [set-image]")
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
