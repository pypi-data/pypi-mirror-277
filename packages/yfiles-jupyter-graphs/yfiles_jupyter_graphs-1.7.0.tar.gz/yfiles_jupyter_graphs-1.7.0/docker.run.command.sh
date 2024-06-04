#!/usr/bin/env bash

docker run -i \
  -u ${USER}:$(id -gn) \
  -v "$PWD":/usr/jupyter-diagrams \
  -v "$PWD"/../yfiles-24.0.4.tgz:/usr/yfiles-24.0.4.tgz:ro \
  -w /usr/jupyter-diagrams \
  jupyter-diagrams
