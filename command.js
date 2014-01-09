var exec = require('child_process').exec;
var commandJSON = {
    "play" : 'osascript playMusic.scpt',
    "pause" : 'osascript pauseMusic.scpt',
    "stop" : 'osascript stopMusic.scpt',
    "up": 'osascript upVolume.scpt',
    "down" : 'osascript downVolume.scpt'
}



 
    execCmd = function(cmd) {
	return exec(cmd, {timeout: 1000},
		    function(error, stdout, stderr) {
			//console.log('stdout: '+(stdout||'none'));
			//console.log('stderr: '+(stderr||'none'));
			console.log("execCmd fired to"+cmd);
			if(error !== null) {
			    console.log('exec error: '+error);
			}
		    }
		    )
    };


execCmd(commandJSON["pause"]);