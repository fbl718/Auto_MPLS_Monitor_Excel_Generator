# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py', 'Get_excel.py', 'Get_node_list.py', 'Auto_login.py', 'Excel.py'],
             pathex=['C:\\Users\\fbl71\\PycharmProjects\\Auto MPLS Monitor Generator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='Auto MPLS Monitor Excel Generator.ico')
