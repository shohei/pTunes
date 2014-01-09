import os

commands = { \
    "play" : 'osascript playMusic.scpt', \
    "pause" : 'osascript pauseMusic.scpt', \
    "stop" : 'osascript stopMusic.scpt', \
    "up": 'osascript upVolume.scpt', \
    "down" : 'osascript downVolume.scpt', \
    "next" : 'osascript nextTrack.scpt', \
    "back" : 'osascript prevTrack.scpt', \
    }

class Status:
    def __init__(self):
        self.count = 0

    def togglePlay(self):
        if self.count == 0:
            print "|> Play a song"
            os.system(commands['play'])
            self.count = 1
        else:
            print ">|| Pause a song"
            os.system(commands['pause'])
            self.count = 0

fin = open("/dev/tty.Pebble9DA4-SerialPortSe")
print "pebble connected"

s = Status()

while True:
    get = fin.read(1)
    code = ord(get)
    if code == 5:
        print ">> Next Track"
        os.system(commands['next'])
    elif code == 8:
        s.togglePlay()
    elif code == 4:
        print "<< Previous Track"
        os.system(commands['back'])

