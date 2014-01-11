# -*- mode: python -*-
a = Analysis(['ptunes.py'],
             pathex=['/Users/shohei/Dropbox/Codes/python/pebble_itunes'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ptunes',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='ptunes')
app = BUNDLE(coll,
             name='ptunes.app',
             icon=None)
