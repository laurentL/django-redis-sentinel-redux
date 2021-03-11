#!/bin/bash
mkdir -p /tmp/redis1 /tmp/redis2 /tmp/redis3
/usr/bin/redis-server  redis1.conf &
/usr/bin/redis-server  redis2.conf &
/usr/bin/redis-server  redis3.conf &

# sentinel
mkdir -p /tmp/redis-sentinel1 /tmp/redis-sentinel2 /tmp/redis-sentinel3
/usr/bin/redis-sentinel sentinel1.conf &
/usr/bin/redis-sentinel sentinel2.conf && echo $! >> /tmp/redis.pid &
/usr/bin/redis-sentinel sentinel3.conf && echo $! >> /tmp/redis.pid &

sleep 1
redis-cli -p 6380 info|grep role
redis-cli -p 6381 info|grep role
redis-cli -p 6382 info|grep role
