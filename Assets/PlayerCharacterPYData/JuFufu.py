"""
JuFufu Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from RawAssets/PlayerCharacterData/JuFufu/hash.json
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns JuFufu's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'a4fd9113': [(log, ('2.5: JuFufu Hair IB Hash',)), (add_ib_check_if_missing,)],
'de303163': [(log, ('2.5: JuFufu Body IB Hash',)), (add_ib_check_if_missing,)],
'f8ab3141': [(log, ('2.5: JuFufu Tail IB Hash',)), (add_ib_check_if_missing,)],
'321768df': [(log, ('2.5: JuFufu Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'37b277db': [
        (log,                           ('2.5: JuFufu FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (Hair, Body, Tail)
'ebac056e': [
        (log,                           ('2.5: JuFufu Shared NormalMap Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],

# Hair and Tail Shared Textures
'db3bdffa': [
        (log,                           ('2.5: JuFufu HairA, TailA Diffuse Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'5c948f7b': [
        (log,                           ('2.5: JuFufu HairA, TailA LightMap Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'9f4d4f72': [
        (log,                           ('2.5: JuFufu HairA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],

# Body Textures
'16e4cac1': [
        (log,                           ('2.5: JuFufu BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'c952431f': [
        (log,                           ('2.5: JuFufu BodyA LightMap Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'd555b4f8': [
        (log,                           ('2.5: JuFufu BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JuFufu',
    'game_versions': ['2.5'],
}
