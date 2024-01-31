#!/bin/sh

while :; do
    socat -dd -T1800 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"/app/a.out",stderr
done