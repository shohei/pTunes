pTunes
=============
pTunes is a software to control iTunes via Pebble

### How to pair your Pebble to Mac

![bluetooth preference](photos/bluetooth_pref.png)

![pair](photos/pair.png)

![not connected](photos/not_connected.png)


Change XXXX below to your Pebble ID
```
fin = open("/dev/tty.PebbleXXXX-SerialPortSe")
```

Then,
```
$ python app.py
```

Or try also GUI (require wxPython)
```
$ python ptunes.py
```

