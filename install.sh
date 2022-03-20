#!/usr/bin/bash

scripts_list=(
	taskbar
	bluetooth
	games
	screenshot
	ytwl
	YTwl
	batch-dl
)

for entry in "${scripts_list[@]}"; do
	cp -vr "./$entry" "/usr/local/bin/"
done
