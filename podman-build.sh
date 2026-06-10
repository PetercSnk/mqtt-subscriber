#!/bin/sh

DIR="logs"
if [ ! -d "$DIR" ]; then
    mkdir "$DIR"
fi

podman build -t mqtt-subscriber .