"""
YeShunguangUlt Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json in RawAssets/PlayerCharacterData/YeShunguangUlt
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YeShunguangUlt's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.5: YeShunguangUlt Ears IB Hash',)),         (add_ib_check_if_missing,)],
'4df52aae': [(log, ('2.5: YeShunguangUlt Legs IB Hash',)),         (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.5: YeShunguangUlt Brows IB Hash',)),        (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.5: YeShunguangUlt Tail IB Hash',)),         (add_ib_check_if_missing,)],
'8e7f72d5': [(log, ('2.5: YeShunguangUlt Torso IB Hash',)),        (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.5: YeShunguangUlt HairTassels IB Hash',)),  (add_ib_check_if_missing,)],
'bafd232d': [(log, ('2.5: YeShunguangUlt Dress IB Hash',)),        (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.5: YeShunguangUlt Face IB Hash',)),         (add_ib_check_if_missing,)],
'f383537b': [(log, ('2.5: YeShunguangUlt Bow IB Hash',)),          (add_ib_check_if_missing,)],
'85d52cb7': [(log, ('2.5: YeShunguangUlt RibbonFlower IB Hash',)), (add_ib_check_if_missing,)],
'be28e18b': [(log, ('2.5: YeShunguangUlt Hair IB Hash',)),         (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: YeShunguangUlt Shared NormalMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '4df52aae', '869976a3', '8e7f72d5', '9258d5f8', 'bafd232d', 'f383537b', '85d52cb7', 'be28e18b'), 'YeShunguangUlt.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'6ed0c951': [
        (log,                           ('2.5: YeShunguangUlt FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
    ],

# === Brows Textures ===
'ac8c7ca2': [
        (log,                           ('2.5: YeShunguangUlt BrowsA Diffuse Hash',)),
        (add_section_if_missing,        ('611df76d', 'YeShunguangUlt.Brows.IB', 'match_priority = 0\n')),
    ],

# === Ears Textures ===
'e8a8ac0b': [
        (log,                           ('2.5: YeShunguangUlt EarsA Diffuse Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],
'652e15a3': [
        (log,                           ('2.5: YeShunguangUlt EarsB Diffuse Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],
'9f7defbc': [
        (log,                           ('2.5: YeShunguangUlt Ears LightMap Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],
'c74f9710': [
        (log,                           ('2.5: YeShunguangUlt Ears MaterialMap Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'652e15a3': [
        (log,                           ('2.5: YeShunguangUlt HairA Diffuse Hash',)),
        (add_section_if_missing,        ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'e8a8ac0b': [
        (log,                           ('2.5: YeShunguangUlt HairB Diffuse Hash',)),
        (add_section_if_missing,        ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'9f7defbc': [
        (log,                           ('2.5: YeShunguangUlt Hair LightMap Hash',)),
        (add_section_if_missing,        ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'c74f9710': [
        (log,                           ('2.5: YeShunguangUlt Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],

# === Legs, Tail Textures (Shared) ===
'c28b9829': [
        (log,                           ('2.5: YeShunguangUlt LegsA, TailA Diffuse Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangUlt.LegsTail.IB', 'match_priority = 0\n')),
    ],
'87d4dd37': [
        (log,                           ('2.5: YeShunguangUlt LegsA, TailA LightMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangUlt.LegsTail.IB', 'match_priority = 0\n')),
    ],
'4700e4bd': [
        (log,                           ('2.5: YeShunguangUlt LegsA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangUlt.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === Torso, Bow Textures (Shared) ===
'956bcfbd': [
        (log,                           ('2.5: YeShunguangUlt TorsoA, BowA Diffuse Hash',)),
        (add_section_if_missing,        (('8e7f72d5', 'f383537b'), 'YeShunguangUlt.TorsoBow.IB', 'match_priority = 0\n')),
    ],
'8e815da2': [
        (log,                           ('2.5: YeShunguangUlt TorsoA, BowA LightMap Hash',)),
        (add_section_if_missing,        (('8e7f72d5', 'f383537b'), 'YeShunguangUlt.TorsoBow.IB', 'match_priority = 0\n')),
    ],
'2f2c27b5': [
        (log,                           ('2.5: YeShunguangUlt TorsoA, BowA MaterialMap Hash',)),
        (add_section_if_missing,        (('8e7f72d5', 'f383537b'), 'YeShunguangUlt.TorsoBow.IB', 'match_priority = 0\n')),
    ],

# === HairTassels, RibbonFlower Textures (Shared) ===
'8d400443': [
        (log,                           ('2.5: YeShunguangUlt HairTasselsA, RibbonFlowerA Diffuse Hash',)),
        (add_section_if_missing,        (('9258d5f8', '85d52cb7'), 'YeShunguangUlt.HairTasselsRibbon.IB', 'match_priority = 0\n')),
    ],
'68e162a7': [
        (log,                           ('2.5: YeShunguangUlt HairTasselsA, RibbonFlowerA LightMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '85d52cb7'), 'YeShunguangUlt.HairTasselsRibbon.IB', 'match_priority = 0\n')),
    ],
'fdd44e2a': [
        (log,                           ('2.5: YeShunguangUlt HairTasselsA, RibbonFlowerA MaterialMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '85d52cb7'), 'YeShunguangUlt.HairTasselsRibbon.IB', 'match_priority = 0\n')),
    ],

# === Dress Textures ===
'f6d35967': [
        (log,                           ('2.5: YeShunguangUlt DressA Diffuse Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangUlt.Dress.IB', 'match_priority = 0\n')),
    ],
'405fa4b6': [
        (log,                           ('2.5: YeShunguangUlt DressA LightMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangUlt.Dress.IB', 'match_priority = 0\n')),
    ],
'e67e5577': [
        (log,                           ('2.5: YeShunguangUlt DressA MaterialMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangUlt.Dress.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangUlt',
    'game_versions': ['2.5'],
}
