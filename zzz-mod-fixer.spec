# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Spec File for ZZZ Mod Fixer v2.5
Character Data Separation - Single Executable Build

This spec file packages the modular character data system
into a single executable with all character modules embedded.
"""

block_cipher = None

# List all character modules for explicit inclusion
character_modules = [
    'PlayerCharacterPYData.Alice',
    'PlayerCharacterPYData.AliceSummer',
    'PlayerCharacterPYData.Anby',
    'PlayerCharacterPYData.Anton',
    'PlayerCharacterPYData.AstraChandelier',
    'PlayerCharacterPYData.AstraYao',
    'PlayerCharacterPYData.Banyue',
    'PlayerCharacterPYData.Belle',
    'PlayerCharacterPYData.BelleSummer',
    'PlayerCharacterPYData.BelleTemple',
    'PlayerCharacterPYData.Ben',
    'PlayerCharacterPYData.Billy',
    'PlayerCharacterPYData.Burnice',
    'PlayerCharacterPYData.Caesar',
    'PlayerCharacterPYData.Corin',
    'PlayerCharacterPYData.Dialyn',
    'PlayerCharacterPYData.Ellen',
    'PlayerCharacterPYData.EllenCampus',
    'PlayerCharacterPYData.Evelyn',
    'PlayerCharacterPYData.Grace',
    'PlayerCharacterPYData.Harumasa',
    'PlayerCharacterPYData.Hugo',
    'PlayerCharacterPYData.JaneDoe',
    'PlayerCharacterPYData.JuFufu',
    'PlayerCharacterPYData.Koleda',
    'PlayerCharacterPYData.Lighter',
    'PlayerCharacterPYData.Lucia',
    'PlayerCharacterPYData.Lucy',
    'PlayerCharacterPYData.Lycaon',
    'PlayerCharacterPYData.Manato',
    'PlayerCharacterPYData.ManatoWhite',
    'PlayerCharacterPYData.Miyabi',
    'PlayerCharacterPYData.Nekomata',
    'PlayerCharacterPYData.Nicole',
    'PlayerCharacterPYData.NicoleCutie',
    'PlayerCharacterPYData.Orphie',
    'PlayerCharacterPYData.PanYinhu',
    'PlayerCharacterPYData.Piper',
    'PlayerCharacterPYData.Pulchra',
    'PlayerCharacterPYData.Qingyi',
    'PlayerCharacterPYData.Rina',
    'PlayerCharacterPYData.Seed',
    'PlayerCharacterPYData.Seth',
    'PlayerCharacterPYData.Soldier0',
    'PlayerCharacterPYData.Soldier11',
    'PlayerCharacterPYData.Soukaku',
    'PlayerCharacterPYData.Trigger',
    'PlayerCharacterPYData.Vivian',
    'PlayerCharacterPYData.VivianSummer',
    'PlayerCharacterPYData.Wise',
    'PlayerCharacterPYData.WiseSummer',
    'PlayerCharacterPYData.WiseTemple',
    'PlayerCharacterPYData.Yanagi',
    'PlayerCharacterPYData.YeShunguang',
    'PlayerCharacterPYData.YeShunguangSkin',
    'PlayerCharacterPYData.YeShunguangSword',
    'PlayerCharacterPYData.YeShunguangSwordUlt',
    'PlayerCharacterPYData.YeShunguangUlt',
    'PlayerCharacterPYData.Yidhari',
    'PlayerCharacterPYData.Yixuan',
    'PlayerCharacterPYData.YixuanTrailsOfInk',
    'PlayerCharacterPYData.Yuzuha',
    'PlayerCharacterPYData.YuzuhaSummer',
    'PlayerCharacterPYData.ZhuYuan',
]

a = Analysis(
    ['zzz-mod-fixer.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Include all character module files
        ('Assets/PlayerCharacterPYData/*.py', 'Assets/PlayerCharacterPYData'),
    ],
    hiddenimports=character_modules,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='zzz-mod-fixer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
