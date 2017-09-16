# -*- mode: python -*-

block_cipher = None


a = Analysis(['DEVELOPPEMENT\\Qt\\5.9.1\\msvc2017_64\\bin', 'goslauncher.py'],
             pathex=['F:\\Programmes', 'D:\\Zone Documents\\ToF\\Documents\\GitHub\\GOSLauncher_A3_Python_version'],
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
          name='bin',
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
               name='bin')
