#!/bin/bash

mkdir -p public/

cd public/

rm -rf s/
mkdir -p s/

time ../gen.py > index.html || exit -1
