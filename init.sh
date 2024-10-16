#!/bin/bash

if [ ! -d .venv ]; then
    python3 -m venv .venv
fi

pip install -r requirements.txt
cp -a hooks .git/hooks