"""
WiseSummer Character Hash Commands
ZZZ Mod Fixer v2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WiseSummer's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes (v2.5)
'1fdaf388': [(log, ('2.5: WiseSummer Face IB Hash (shared with Wise)',)), (add_ib_check_if_missing,)],
'4fe696c8': [(log, ('2.5: WiseSummer Body IB Hash',)), (add_ib_check_if_missing,)],
'cb272754': [(log, ('2.5: WiseSummer Hair IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures (v2.5)
'5d75fddc': [
        (log,                           ('2.5: WiseSummer FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
    ],
'c2c8606e': [
        (log,                           ('2.5: WiseSummer FaceA, BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],

# Body Textures (v2.5)
'd476035d': [
        (log,                           ('2.5: WiseSummer BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: WiseSummer BodyA, HairA NormalMap Hash (shared)',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'0fa8f99c': [
        (log,                           ('2.5: WiseSummer BodyA LightMap Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],

# Hair Textures (v2.5)
'28005a5b': [
        (log,                           ('2.5: WiseSummer HairA Diffuse Hash',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('2.5: WiseSummer HairA LightMap Hash',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('2.5: WiseSummer HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseSummer',
    'variant': 'Summer',
    'game_versions': ['2.5'],
}
