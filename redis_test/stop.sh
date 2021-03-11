#!/bin/bash
kill `cat /tmp/redis-server1.pid`
kill `cat /tmp/redis-server2.pid`
kill `cat /tmp/redis-server3.pid`

kill `cat "/tmp/redis-sentinel1.pid"`
kill `cat "/tmp/redis-sentinel2.pid"`
kill `cat "/tmp/redis-sentinel3.pid"`


