#!/usr/bin/bash

scripts_list=(
	taskbar
	bluetooth
	games
	screenshot
	"ytfs.py"
	ytwl
	ytuf
)

for entry in "${scripts_list[@]}"; do
	cp -v "./$entry" "/usr/local/bin/"
done
