#!/usr/bin/bash

scripts_list=(
	taskbar
	bluetooth
)

for entry in "${scripts_list[@]}"; do
	cp -v "./$entry" "/usr/local/bin/"
done
