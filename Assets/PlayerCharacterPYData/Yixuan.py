"""
Yixuan Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json data
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Yixuan's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'ac8e9ee3': [(log, ('2.5: Yixuan Hair IB Hash',)),      (add_ib_check_if_missing,)],
'029c1f5a': [(log, ('2.5: Yixuan Body IB Hash',)),      (add_ib_check_if_missing,)],
'1630f2d0': [(log, ('2.5: Yixuan Bottle IB Hash',)),    (add_ib_check_if_missing,)],
'0fdae851': [(log, ('2.5: Yixuan BottleGlass IB Hash',)),(add_ib_check_if_missing,)],
'67c61080': [(log, ('2.5: Yixuan Coins IB Hash',)),     (add_ib_check_if_missing,)],
'892858fd': [(log, ('2.5: Yixuan Hairpin IB Hash',)),   (add_ib_check_if_missing,)],
'8c2fc05e': [(log, ('2.5: Yixuan Jacket IB Hash',)),    (add_ib_check_if_missing,)],
'8b067f99': [(log, ('2.5: Yixuan Face IB Hash',)),      (add_ib_check_if_missing,)],

# Shared Texture Hashes (used across multiple components)
'ebac056e': [
        (log,                           ('2.5: Yixuan Shared NormalMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],

# Hair, Bottle, BottleGlass, Coins Shared Textures
'7e38b38b': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins Diffuse Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
    ],
'086ac064': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins LightMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
    ],
'83b02982': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins MaterialMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
    ],

# Body and Hairpin Shared Textures
'2a4f37a6': [
        (log,                           ('2.5: Yixuan Body/Hairpin Diffuse Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'5a291e85': [
        (log,                           ('2.5: Yixuan Body/Hairpin LightMap Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'd28370ec': [
        (log,                           ('2.5: Yixuan Body/Hairpin MaterialMap Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],

# Jacket Textures
'e6dca725': [
        (log,                           ('2.5: Yixuan Jacket Diffuse Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'59b2daf9': [
        (log,                           ('2.5: Yixuan Jacket LightMap Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'bb581f1e': [
        (log,                           ('2.5: Yixuan Jacket MaterialMap Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],

# Face Textures
'7d9ee001': [
        (log,                           ('2.5: Yixuan Face Diffuse Hash',)),
        (add_section_if_missing,        ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yixuan',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Bottle', 'BottleGlass', 'Coins', 'Hairpin', 'Jacket', 'Face'],
}
