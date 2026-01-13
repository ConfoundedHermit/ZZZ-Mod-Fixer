"""
EllenCampus Character Hash Commands
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
    Returns EllenCampus's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    
    Note: EllenCampus reuses Ellen's face (IB: f6ef8f3a, Diffuse: 465a66eb)
    and shares NormalMap hash ebac056e across all components.
    """
    return {
# Hair Component
'f601f643': [(log, ('2.5: EllenCampus Hair IB Hash',)), (add_ib_check_if_missing,)],

'6e15911b': [
        (log,                           ('2.5: EllenCampus HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9a5c0d42', 'EllenCampus.HairA.Diffuse.1024')),
    ],
'9a5c0d42': [
        (log,                           ('2.5: EllenCampus HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6e15911b', 'EllenCampus.HairA.Diffuse.2048')),
    ],

'48fd827b': [
        (log,                           ('2.5: EllenCampus HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('72e65ade', 'EllenCampus.HairA.LightMap.1024')),
    ],
'72e65ade': [
        (log,                           ('2.5: EllenCampus HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('48fd827b', 'EllenCampus.HairA.LightMap.2048')),
    ],

'8740602f': [
        (log,                           ('2.5: EllenCampus HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d69b5a86', 'EllenCampus.HairA.MaterialMap.1024')),
    ],
'd69b5a86': [
        (log,                           ('2.5: EllenCampus HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8740602f', 'EllenCampus.HairA.MaterialMap.2048')),
    ],

# Body Component
'4a938c0a': [(log, ('2.5: EllenCampus Body IB Hash',)), (add_ib_check_if_missing,)],

'76f42184': [
        (log,                           ('2.5: EllenCampus BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fec9bbf8', 'EllenCampus.BodyA.Diffuse.1024')),
    ],
'fec9bbf8': [
        (log,                           ('2.5: EllenCampus BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('76f42184', 'EllenCampus.BodyA.Diffuse.2048')),
    ],

'e6c9a6e1': [
        (log,                           ('2.5: EllenCampus BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('82a31ce3', 'EllenCampus.BodyA.LightMap.1024')),
    ],
'82a31ce3': [
        (log,                           ('2.5: EllenCampus BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e6c9a6e1', 'EllenCampus.BodyA.LightMap.2048')),
    ],

'1d7b458d': [
        (log,                           ('2.5: EllenCampus BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('30427c9e', 'EllenCampus.BodyA.MaterialMap.1024')),
    ],
'30427c9e': [
        (log,                           ('2.5: EllenCampus BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1d7b458d', 'EllenCampus.BodyA.MaterialMap.2048')),
    ],

# Tail Component
'fafcfe36': [(log, ('2.5: EllenCampus Tail IB Hash',)), (add_ib_check_if_missing,)],

'0e474202': [
        (log,                           ('2.5: EllenCampus TailA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e0c36e7e', 'EllenCampus.TailA.Diffuse.1024')),
    ],
'e0c36e7e': [
        (log,                           ('2.5: EllenCampus TailA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0e474202', 'EllenCampus.TailA.Diffuse.2048')),
    ],

'8f2cb44d': [
        (log,                           ('2.5: EllenCampus TailA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f21e3fa3', 'EllenCampus.TailA.LightMap.1024')),
    ],
'f21e3fa3': [
        (log,                           ('2.5: EllenCampus TailA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8f2cb44d', 'EllenCampus.TailA.LightMap.2048')),
    ],

'51cc39d5': [
        (log,                           ('2.5: EllenCampus TailA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('78e70ba9', 'EllenCampus.TailA.MaterialMap.1024')),
    ],
'78e70ba9': [
        (log,                           ('2.5: EllenCampus TailA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('51cc39d5', 'EllenCampus.TailA.MaterialMap.2048')),
    ],

# Shared NormalMap (used by Hair, Body, and Tail - same as Ellen's)
# Note: This hash is already defined in Ellen.py and shared across multiple components
# Adding references here for EllenCampus components
'ebac056e': [
        (log,                           ('2.5: EllenCampus Shared NormalMap 2048p Hash (Hair/Body/Tail)',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d6715e09', 'EllenCampus.Shared.NormalMap.1024')),
    ],

# Face Component (Reuses Ellen's face)
# IB: f6ef8f3a and Diffuse: 465a66eb are already defined in Ellen.py
# No additional hash commands needed as EllenCampus uses Ellen's face directly
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'EllenCampus',
    'full_name': 'Ellen (Campus Outfit)',
    'game_versions': ['2.5'],
    'notes': 'Reuses Ellen\'s face (IB: f6ef8f3a, Diffuse: 465a66eb). Shares NormalMap (ebac056e) across Hair/Body/Tail.',
}
