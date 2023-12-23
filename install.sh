#!/bin/bash

# Exit if something fails
set -e

mkdir -p ~/.local/share/kservices5/
mkdir -p ~/.local/share/dbus-1/services/

cp plasma-runner-dioxionary.desktop ~/.local/share/kservices5/
sed "s|%{PROJECTDIR}/krunner_dioxionary.py|${PWD}/src/krunner_dioxionary.py|" "org.kde.dioxionary.service" > ~/.local/share/dbus-1/services/org.kde.dioxionary.service

kquitapp5 krunner
