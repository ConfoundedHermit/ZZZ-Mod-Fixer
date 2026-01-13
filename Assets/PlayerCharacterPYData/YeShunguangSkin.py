"""
YeShunguangSkin Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YeShunguangSkin's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.5: YeShunguangSkin Ears IB Hash',)),          (add_ib_check_if_missing,)],
'4df52aae': [(log, ('2.5: YeShunguangSkin Legs IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.5: YeShunguangSkin Brows IB Hash',)),         (add_ib_check_if_missing,)],
'6dc6c880': [(log, ('2.5: YeShunguangSkin HairClips IB Hash',)),     (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.5: YeShunguangSkin Tail IB Hash',)),          (add_ib_check_if_missing,)],
'8e7f72d5': [(log, ('2.5: YeShunguangSkin Torso IB Hash',)),         (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.5: YeShunguangSkin HairTassels IB Hash',)),   (add_ib_check_if_missing,)],
'bafd232d': [(log, ('2.5: YeShunguangSkin Dress IB Hash',)),         (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.5: YeShunguangSkin Face IB Hash',)),          (add_ib_check_if_missing,)],
'f383537b': [(log, ('2.5: YeShunguangSkin HairBow IB Hash',)),       (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.5: YeShunguangSkin BraidRibbons IB Hash',)),  (add_ib_check_if_missing,)],
'85d52cb7': [(log, ('2.5: YeShunguangSkin RibbonFlower IB Hash',)),  (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.5: YeShunguangSkin Bangs IB Hash',)),         (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: YeShunguangSkin Shared NormalMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '4df52aae', '6dc6c880', '869976a3', '8e7f72d5', '9258d5f8', 'bafd232d', 'f383537b', '38b3bd13', '85d52cb7', '999bff94'), 'YeShunguangSkin.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face and Brows Textures ===
'6ed0c951': [
        (log,                           ('2.5: YeShunguangSkin FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguangSkin.Face.IB', 'match_priority = 0\n')),
    ],

# === Ears and Bangs Textures (Shared Set 1) ===
'79f6acd7': [
        (log,                           ('2.5: YeShunguangSkin EarsA, BangsA Diffuse Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangSkin.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'88269532': [
        (log,                           ('2.5: YeShunguangSkin EarsA, BangsA LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangSkin.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'825fbf26': [
        (log,                           ('2.5: YeShunguangSkin EarsA, BangsA MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangSkin.EarsBangs.IB', 'match_priority = 0\n')),
    ],

# === Legs and Tail Textures (Shared Set 2) ===
'37c5aae5': [
        (log,                           ('2.5: YeShunguangSkin LegsA, TailA Diffuse Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangSkin.LegsTail.IB', 'match_priority = 0\n')),
    ],
'01e54e40': [
        (log,                           ('2.5: YeShunguangSkin LegsA, TailA LightMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangSkin.LegsTail.IB', 'match_priority = 0\n')),
    ],
'18370cad': [
        (log,                           ('2.5: YeShunguangSkin LegsA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangSkin.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === HairClips, Torso, and HairBow Textures (Shared Set 3) ===
'956bcfbd': [
        (log,                           ('2.5: YeShunguangSkin HairClipsA, TorsoA, HairBowA Diffuse Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangSkin.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],
'8e815da2': [
        (log,                           ('2.5: YeShunguangSkin HairClipsA, TorsoA, HairBowA LightMap Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangSkin.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],
'2f2c27b5': [
        (log,                           ('2.5: YeShunguangSkin HairClipsA, TorsoA, HairBowA MaterialMap Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangSkin.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],

# === HairTassels, BraidRibbons, and RibbonFlower Textures (Shared Set 4) ===
'8d400443': [
        (log,                           ('2.5: YeShunguangSkin HairTasselsA, BraidRibbonsA, RibbonFlowerA Diffuse Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangSkin.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'68e162a7': [
        (log,                           ('2.5: YeShunguangSkin HairTasselsA, BraidRibbonsA, RibbonFlowerA LightMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangSkin.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'fdd44e2a': [
        (log,                           ('2.5: YeShunguangSkin HairTasselsA, BraidRibbonsA, RibbonFlowerA MaterialMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangSkin.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],

# === Dress Textures ===
'f6d35967': [
        (log,                           ('2.5: YeShunguangSkin DressA Diffuse Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n')),
    ],
'405fa4b6': [
        (log,                           ('2.5: YeShunguangSkin DressA LightMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n')),
    ],
'e67e5577': [
        (log,                           ('2.5: YeShunguangSkin DressA MaterialMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangSkin',
    'game_versions': ['2.5'],
}
