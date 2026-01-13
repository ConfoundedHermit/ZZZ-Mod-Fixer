"""
PanYinhu Character Hash Commands
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
    Returns PanYinhu's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'cb1a6db9': [(log, ('2.5: PanYinhu Body IB Hash',)), (add_ib_check_if_missing,)],
'ff7e9b40': [(log, ('2.5: PanYinhu Hat IB Hash',)), (add_ib_check_if_missing,)],
'ebb6a59b': [(log, ('2.5: PanYinhu Face IB Hash',)), (add_ib_check_if_missing,)],

# Body A & B + Hat B Textures (Shared)
'c0928025': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B Diffuse Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'7d3c4c3d': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B LightMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'42fc25f0': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B MaterialMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],

# Body C + Hat A Textures (Shared)
'f2433e17': [
        (log,                           ('2.5: PanYinhu Body C + Hat A Diffuse Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'ddeaa4c3': [
        (log,                           ('2.5: PanYinhu Body C + Hat A LightMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'de553410': [
        (log,                           ('2.5: PanYinhu Body C + Hat A MaterialMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],

# Body D + Face A Textures (Shared)
'ed361b8f': [
        (log,                           ('2.5: PanYinhu Body D + Face A Diffuse Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'96280008': [
        (log,                           ('2.5: PanYinhu Body D + Face A LightMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'57446a22': [
        (log,                           ('2.5: PanYinhu Body D + Face A MaterialMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (across all components)
'ebac056e': [
        (log,                           ('2.5: PanYinhu Shared NormalMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhu',
    'game_versions': ['2.5'],
    'components': ['Body', 'Hat', 'Face'],
    'variants': {
        'Body': ['A', 'B', 'C', 'D'],
        'Hat': ['A', 'B'],
        'Face': ['A']
    },
}
