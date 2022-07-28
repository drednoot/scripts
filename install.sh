#!/usr/bin/bash

scripts_list=(
	taskbar
	ytwl
	YTwl
	batch-dl
	rbvol
	sfx
	mute
)

for entry in "${scripts_list[@]}"; do
	sudo cp -vr "./$entry" "/usr/local/bin/"
done
