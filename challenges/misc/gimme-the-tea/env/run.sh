#!/bin/bash
while :; do
    socat -dd -T900 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"/app/gimmetea",stderr
done