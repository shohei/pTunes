tell application "iTunes"
	set current_volume to sound volume
	set current_volume to current_volume - 10
	set sound volume to current_volume
	set EQ enabled to true
	play
end tell

