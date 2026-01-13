"""
YixuanTrailsOfInk Character Hash Commands
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
    Returns YixuanTrailsOfInk's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'ac8e9ee3': [(log, ('2.5: YixuanTrailsOfInk Hair IB Hash',)),      (add_ib_check_if_missing,)],
'95de0d39': [(log, ('2.5: YixuanTrailsOfInk Body IB Hash',)),      (add_ib_check_if_missing,)],
'064cd7d3': [(log, ('2.5: YixuanTrailsOfInk Bottle IB Hash',)),    (add_ib_check_if_missing,)],
'0fdae851': [(log, ('2.5: YixuanTrailsOfInk Ink IB Hash',)),       (add_ib_check_if_missing,)],
'8b067f99': [(log, ('2.5: YixuanTrailsOfInk Face IB Hash',)),      (add_ib_check_if_missing,)],

# Shared Texture Hash - NormalMap (used across Hair, Body, Bottle)
'ebac056e': [
        (log,                           ('2.5: YixuanTrailsOfInk Shared NormalMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],

# Hair Textures
'7e38b38b': [
        (log,                           ('2.5: YixuanTrailsOfInk Hair Diffuse Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'086ac064': [
        (log,                           ('2.5: YixuanTrailsOfInk Hair LightMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'83b02982': [
        (log,                           ('2.5: YixuanTrailsOfInk Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures - Object A
'fe2cc6f3': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle Diffuse Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'867e3b95': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle LightMap Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'c72a2356': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle MaterialMap Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],

# Body/Bottle Textures - Object B/C
'7683c132': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle Diffuse Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'a22695c9': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle LightMap Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'7e6747ac': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle MaterialMap Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],

# Face Textures
'7d9ee001': [
        (log,                           ('2.5: YixuanTrailsOfInk Face Diffuse Hash',)),
        (add_section_if_missing,        ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YixuanTrailsOfInk',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Bottle', 'Ink', 'Face'],
}
