#!/bin/bash
set -xe

mkimg=$(buildah from docker.io/nginx/unit:1.24.0-python3.9)
buildah config --author='sycured' "$mkimg"
buildah config --label Name='streaming-calc-fastapi' "$mkimg"
buildah config --port 8000 "$mkimg"
buildah copy --chown unit:unit "$mkimg" config.json /docker-entrypoint.d/config.json
buildah copy --chown unit:unit "$mkimg" requirements.txt /opt/requirements.txt
buildah run "$mkimg" -- pip install --no-cache-dir -r /opt/requirements.txt
buildah copy --chown unit:unit "$mkimg" main.py /opt
buildah commit --squash "$mkimg" "scfa"
buildah rm "$mkimg"