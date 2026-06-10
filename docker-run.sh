#!/bin/sh

docker run \
    --detach \
    --name subscriber \
    --publish 8000:8000 \
    mqtt-subscriber