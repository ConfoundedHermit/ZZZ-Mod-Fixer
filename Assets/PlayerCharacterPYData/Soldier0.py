"""
Soldier0 Character Hash Commands
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
    Returns Soldier0's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ========== Hair Component ==========
'217ec790': [(log, ('2.5: Soldier0 Hair IB Hash',)), (add_ib_check_if_missing,)],

# Hair Diffuse
'aa3d57ff': [
        (log,                           ('2.5: Soldier0 HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8cb4086a', 'Soldier0.HairA.Diffuse.1024')),
    ],
'8cb4086a': [
        (log,                           ('2.5: Soldier0 HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('aa3d57ff', 'Soldier0.HairA.Diffuse.2048')),
    ],

# Hair NormalMap
'ebac056e': [
        (log,                           ('2.5: Soldier0 HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f8e9a6c1', 'Soldier0.HairA.NormalMap.1024')),
    ],
'f8e9a6c1': [
        (log,                           ('2.5: Soldier0 HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Soldier0.HairA.NormalMap.2048')),
    ],

# Hair LightMap
'8d42a55b': [
        (log,                           ('2.5: Soldier0 HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('96a28554', 'Soldier0.HairA.LightMap.1024')),
    ],
'96a28554': [
        (log,                           ('2.5: Soldier0 HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8d42a55b', 'Soldier0.HairA.LightMap.2048')),
    ],

# Hair MaterialMap (v1.6 -> v2.5 update)
'464847b3': [(log, ('1.6: Soldier0 HairA MaterialMap 2048p Hash (Old)',)), (update_hash, ('0b059f91',))],
'0b059f91': [
        (log,                           ('2.5: Soldier0 HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ce3e73be', 'Soldier0.HairA.MaterialMap.1024')),
    ],
'ce3e73be': [
        (log,                           ('2.5: Soldier0 HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0b059f91', 'Soldier0.HairA.MaterialMap.2048')),
    ],

# ========== Body Component ==========
'53d3f4e5': [(log, ('2.5: Soldier0 Body IB Hash',)), (add_ib_check_if_missing,)],

# Body Diffuse
'627baf3f': [
        (log,                           ('2.5: Soldier0 BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0acef326', 'Soldier0.BodyA.Diffuse.1024')),
    ],
'0acef326': [
        (log,                           ('2.5: Soldier0 BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('627baf3f', 'Soldier0.BodyA.Diffuse.2048')),
    ],

# Body LightMap
'3a56b70b': [
        (log,                           ('2.5: Soldier0 BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('625ad0eb', 'Soldier0.BodyA.LightMap.1024')),
    ],
'625ad0eb': [
        (log,                           ('2.5: Soldier0 BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3a56b70b', 'Soldier0.BodyA.LightMap.2048')),
    ],

# Body MaterialMap
'7cfa12b6': [
        (log,                           ('2.5: Soldier0 BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dea3c5a0', 'Soldier0.BodyA.MaterialMap.1024')),
    ],
'dea3c5a0': [
        (log,                           ('2.5: Soldier0 BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7cfa12b6', 'Soldier0.BodyA.MaterialMap.2048')),
    ],

# ========== Face Component ==========
# Face IB (v1.6 -> v2.5 update)
'f2f539b8': [(log, ('1.6: Soldier0 Face IB Hash (Old)',)), (update_hash, ('e30ca87f',))],
'e30ca87f': [(log, ('2.5: Soldier0 Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Diffuse
'05d7b504': [
        (log,                           ('2.5: Soldier0 FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('692c6d2b', 'Soldier0.FaceA.Diffuse.1024')),
    ],
'692c6d2b': [
        (log,                           ('2.5: Soldier0 FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('05d7b504', 'Soldier0.FaceA.Diffuse.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soldier0',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
