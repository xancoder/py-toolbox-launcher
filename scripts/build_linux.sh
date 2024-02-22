#!/usr/bin/env bash

su -c 'apt install -y python3-poetry'
poetry install
poetry run build_linux_cli

mkdir -p dist/toolbox
cp toolbox/Linux/* dist/toolbox/
