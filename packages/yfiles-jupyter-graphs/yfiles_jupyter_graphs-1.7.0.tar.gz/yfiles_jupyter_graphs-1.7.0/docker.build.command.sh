#!/usr/bin/env bash

docker build \
  --build-arg USERNAME=${USER} \
  --build-arg GROUPNAME=$(id -gn) \
  --build-arg USERID=$(id -u) \
  --build-arg GROUPID=$(id -g) \
  --no-cache \
  -t jupyter-diagrams .
