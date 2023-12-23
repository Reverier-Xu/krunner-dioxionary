#!/bin/bash

# Exit if something fails
set -e

rm ~/.local/share/kservices5/plasma-runner-dioxionary.desktop
rm ~/.local/share/dbus-1/services/org.kde.dioxionary.service

kquitapp5 krunner
