#!/usr/bin/python

import wx
import os
import sys,traceback
from threading import Thread
import time 

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(260, 260)) 
        self.SetBackgroundColour("white")

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        pImage = wx.Image('images/pebble.png').Scale(100, 100)
        iImage = wx.Image('images/itunes.png').Scale(100, 100)
        aImage = wx.Image('images/arrow.png').Scale(30, 30)
        self.pBitmap = pImage.ConvertToBitmap()
        self.aBitmap = aImage.ConvertToBitmap()
        self.iBitmap = iImage.ConvertToBitmap()
        hbox0.Add(wx.StaticBitmap(self, -1, self.pBitmap, (0,0),(100,100)),1,wx.ALL|wx.EXPAND,5) 
        hbox0.Add(wx.StaticBitmap(self, -1, self.aBitmap, (0,0),(100,100)),1,wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL,5)
        hbox0.Add(wx.StaticBitmap(self, -1, self.iBitmap, (0,0),(100,100)),1,wx.ALL|wx.EXPAND,5) 

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.Button(self, 1, "Connect"),1,wx.ALL|wx.EXPAND,5) 
        hbox1.Add(wx.Button(self, 2, "Disconnect"),1,wx.ALL|wx.EXPAND,5)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.statusLabel = wx.StaticText(self, 3, "Status: ") 
        hbox2.Add(self.statusLabel,1,wx.ALL|wx.EXPAND,35) 

        vbox.Add(hbox0)
        vbox.Add(hbox1)
        vbox.Add(hbox2)
        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON,self.connect,id=1)
        self.Bind(wx.EVT_BUTTON,self.disconnect,id=2)

        self.count = 0
        self.commands = { \
            "play" : 'osascript scpt/playMusic.scpt', \
            "pause" : 'osascript scpt/pauseMusic.scpt', \
            "stop" : 'osascript scpt/stopMusic.scpt', \
            "up": 'osascript scpt/upVolume.scpt', \
            "down" : 'osascript scpt/downVolume.scpt', \
            "next" : 'osascript scpt/nextTrack.scpt', \
            "back" : 'osascript scpt/prevTrack.scpt', \
            }
        self.disconnect_flag = False 
        
    def togglePlay(self):
        if self.count == 0:
            print "|> Play a song"
            os.system(self.commands['play'])
            self.count = 1
        else:
            print ">|| Pause a song"
            os.system(self.commands['pause'])
            self.count = 0
 
 
    def connect(self,event):
        print "try to connect..." 
        try: 
            self.fin = open("/dev/tty.Pebble9DA4-SerialPortSe")
            print "pebble connected"
            self.statusLabel.SetLabel("Connected to Pebble") 

            self.collector_thread = MyCollector(self)
            self.collector_thread.start()

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                                  limit=2, file=sys.stdout)
            print "pebble not found"
            self.statusLabel.SetLabel("Pebble not found") 
 
    def disconnect(self,event):
        print "try to disconnect..."
        
        try:
            #self.collector_thread._Thread__delete()
            self.disconnect_flag = True 
            while self.collector_thread.is_alive():
                time.sleep(0.1)
            self.fin.close()
            print "pebble disconnected"
            self.statusLabel.SetLabel("Pebble disconnected") 
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                                  limit=2, file=sys.stdout)
            print "something weird happend"
            self.statusLabel.SetLabel("Something weired :(") 
 

class MyCollector(Thread):
    def __init__(self, collect_from):
        Thread.__init__(self) # must be called !
        self.collect_from = collect_from

    def run(self):
        while True:
            get = self.collect_from.fin.read(1)
            code = ord(get)
            if code == 5:
                print ">> Next Track"
                os.system(self.collect_from.commands['next'])
            elif code == 8:
                self.collect_from.togglePlay()
            elif code == 4:
                print "<< Previous Track"
                os.system(self.collect_from.commands['back'])
            if self.collect_from.disconnect_flag:
                break 

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'pTunes')
        menubar = wx.MenuBar()
        frame.SetMenuBar(menubar)
        frame.Show(True)
        frame.Centre()
        return True

app = MyApp(0)
app.MainLoop()
