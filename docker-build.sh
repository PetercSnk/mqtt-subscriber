#!/bin/sh

DIR="logs"
if [ ! -d "$DIR" ]; then
    mkdir "$DIR"
fi

docker build -t mqtt-subscriber .