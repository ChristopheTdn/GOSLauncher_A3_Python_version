# -*- mode: python -*-

block_cipher = None


a = Analysis(['goslauncher.py'],
             pathex=['F:\\Programmes DEVELOPPEMENT\\Python\\Python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\Zone Documents\\ToF\\Documents\\GitHub\\GOSLauncher_A3_Python_version'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='goslauncher',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='goslauncher')
