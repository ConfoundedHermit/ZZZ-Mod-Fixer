"""
YuzuhaSummer Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YuzuhaSummer's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'7a504287': [(log, ('2.5: YuzuhaSummer Hair IB Hash',)), (add_ib_check_if_missing,)],
'b298482d': [(log, ('2.5: YuzuhaSummer Body IB Hash',)), (add_ib_check_if_missing,)],
'a8de520e': [(log, ('2.5: YuzuhaSummer Accessories IB Hash',)), (add_ib_check_if_missing,)],
'14ac0d52': [(log, ('2.5: YuzuhaSummer Kama IB Hash',)), (add_ib_check_if_missing,)],
'507384ea': [(log, ('2.5: YuzuhaSummer Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'd394bc13': [
        (log,                           ('2.5: YuzuhaSummer FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n')),
    ],

# Hair Textures
'521a3242': [
        (log,                           ('2.5: YuzuhaSummer Hair Diffuse Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'c400f5b7': [
        (log,                           ('2.5: YuzuhaSummer Hair LightMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'3f70d124': [
        (log,                           ('2.5: YuzuhaSummer Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures (shared between Body and Kama components)
'4f4c2b65': [
        (log,                           ('2.5: YuzuhaSummer Body/Kama Diffuse Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'c3e64779': [
        (log,                           ('2.5: YuzuhaSummer Body/Kama LightMap Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'ac2f3dcb': [
        (log,                           ('2.5: YuzuhaSummer Body/Kama MaterialMap Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],

# Accessories Textures
'54591ef6': [
        (log,                           ('2.5: YuzuhaSummer Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'a78340ed': [
        (log,                           ('2.5: YuzuhaSummer Accessories LightMap Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'1d0dabdb': [
        (log,                           ('2.5: YuzuhaSummer Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (used across Hair, Body, Accessories, and Kama)
'ebac056e': [
        (log,                           ('2.5: YuzuhaSummer Shared NormalMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YuzuhaSummer',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Accessories', 'Kama', 'Face'],
}
