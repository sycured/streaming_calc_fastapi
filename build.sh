#!/bin/bash
set -xe

mkbuild=$(buildah from docker.io/centos:latest)
buildah run "$mkbuild" -- dnf upgrade -y
buildah run "$mkbuild" -- dnf install python3 python3-pip python3-devel make gcc -y
mntbuild=$(buildah mount "$mkbuild")
mkdir "$mntbuild"/dependencies
cp requirements.txt "$mntbuild"/opt
buildah run "$mkbuild" -- pip3 install --no-cache-dir --install-option="--prefix=/dependencies" -r /opt/requirements.txt

mkfinal=$(buildah from scratch)
buildah config --author='sycured' "$mkfinal"
buildah config --label Name='streaming-calc-fastapi' "$mkfinal"
buildah config --workingdir='/opt' "$mkfinal"
buildah config --cmd 'uvicorn --host 0.0.0.0 --port 8000 main:app' "$mkfinal"
mntfinal=$(buildah mount "$mkfinal")
mkdir -p "$mntfinal"/opt
yum --nogpgcheck --installroot="$mntfinal" --repofrompath centos8,http://mirror.centos.org/centos/8/BaseOS/x86_64/os/ --repofrompath appstream,http://mirror.centos.org/centos/8/AppStream/x86_64/os/ --repofrompath  extras,http://mirror.centos.org/centos/8/extras/x86_64/os/ --repo=centos8,appstream, install glibc-langpack-en python3 -y
cp -r "$mntbuild"/dependencies "$mntfinal"/usr/local
cp main.py "$mntfinal"/opt

buildah unmount "$mkbuild"
buildah unmount "$mkfinal"
buildah rm "$mkbuild"
buildah commit --squash "$mkfinal" "scfa"
buildah rm "$mkfinal"
