import os

commands = { \
    "play" : 'osascript ../scpt/playMusic.scpt', \
    "pause" : 'osascript ../scpt/pauseMusic.scpt', \
    "stop" : 'osascript ../scpt/stopMusic.scpt', \
    "up": 'osascript ../scpt/upVolume.scpt', \
    "down" : 'osascript ../scpt/downVolume.scpt', \
    "next" : 'osascript ../scpt/nextTrack.scpt', \
    "back" : 'osascript ../scpt/prevTrack.scpt', \
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

