#!/bin/bash

mkdir -p ~/.local/share/kservices5/
cp plasma-runner-dioxionary.desktop ~/.local/share/kservices5/
kquitapp5 krunner
pkill python3
python3 src/krunner_dioxionary.py
