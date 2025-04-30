#!/usr/bin/env bash

if [[ $3 == "--max_depth" ]]; then
    python3 main.py $1 $2 $4
else
    python3 main.py $1 $2 0
fi
