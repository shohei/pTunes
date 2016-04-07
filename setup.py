"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ptunes.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
 'iconfile': '/Users/shohei/.ghq/github.com/shohei/pTunes/pebble.icns',
'plist': {'CFBundleShortVersionString':'1.0.0',}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
