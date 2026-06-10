#!/bin/sh

podman run \
    --detach \
    --name subscriber \
    --publish 8000:8000/tcp \
    mqtt-subscriber