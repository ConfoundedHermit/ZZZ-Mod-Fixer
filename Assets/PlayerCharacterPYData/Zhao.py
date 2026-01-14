"""
Zhao Character Hash Commands
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
    Returns Zhao's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ===== IB Hashes (Current v2.5) =====
'2d519056': [(log, ('2.5: Zhao Hair IB Hash',)), (add_ib_check_if_missing,)],
'43c3c5a0': [(log, ('2.5: Zhao Face IB Hash',)), (add_ib_check_if_missing,)],
'6a57d06b': [(log, ('2.5: Zhao Body IB Hash',)), (add_ib_check_if_missing,)],

# ===== Buffer Hashes (Current v2.5) =====
'9bfc82f2': [(log, ('2.5: Zhao Hair Draw Hash',))],
'f86dba12': [(log, ('2.5: Zhao Hair Position Hash',))],
'4b9ea40c': [(log, ('2.5: Zhao Hair Blend Hash',))],
'e1fe5e10': [(log, ('2.5: Zhao Hair Texcoord Hash',))],
'b26f9258': [(log, ('2.5: Zhao Face Draw Hash',))],
'887d011f': [(log, ('2.5: Zhao Face Position Hash',))],
'd3c0fe17': [(log, ('2.5: Zhao Face Blend Hash',))],
'76c4a041': [(log, ('2.5: Zhao Face Texcoord Hash',))],
'a08c7b83': [(log, ('2.5: Zhao Body Draw Hash',))],
'ac4490da': [(log, ('2.5: Zhao Body Position Hash',))],
'06ce2ca1': [(log, ('2.5: Zhao Body Blend Hash',))],
'834b607a': [(log, ('2.5: Zhao Body Texcoord Hash',))],

# ===== Texture Hashes (Current v2.5) =====
'3400d1fc': [
        (log,                           ('2.5: Zhao HairA Diffuse Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Zhao Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'4c988418': [
        (log,                           ('2.5: Zhao HairA LightMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'bdc3666d': [
        (log,                           ('2.5: Zhao HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'6f06cdfa': [
        (log,                           ('2.5: Zhao FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
    ],
'e98b7e9e': [
        (log,                           ('2.5: Zhao Shared MaterialMap Hash (Face/Body)',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'77dc1746': [
        (log,                           ('2.5: Zhao BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'5ed57658': [
        (log,                           ('2.5: Zhao BodyA LightMap Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Zhao',
    'game_versions': ['2.5'],
}
