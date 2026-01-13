"""
Billy Character Hash Commands
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
    Returns Billy's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'21e98aeb': [(log, ('1.0: Billy Hair IB Hash',)), (add_ib_check_if_missing,)],
'3371580a': [(log, ('1.0: Billy Body IB Hash',)), (add_ib_check_if_missing,)],
'dc7978f3': [(log, ('1.0: Billy Head IB Hash',)), (add_ib_check_if_missing,)],
'a1d68c9e': [
        (log,                           ('1.0: Billy HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6f8a9cdb', 'Billy.HeadA.Diffuse.2048')),
    ],
'eed0cd5f': [
        (log,                           ('1.0: Billy HeadA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Billy.HeadA.NormalMap.2048')),
    ],
'877e1a0d': [
        (log,                           ('1.0: Billy HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cf4769ce', 'Billy.HeadA.LightMap.2048')),
    ],
'dc2f2dd2': [
        (log,                           ('1.0: Billy HeadA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3a7d88a1', 'Billy.HeadA.MaterialMap.2048')),
    ],
'6f8a9cdb': [
        (log,                           ('1.0: Billy HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a1d68c9e', 'Billy.HeadA.Diffuse.1024')),
    ],
'e5f2fc35': [
        (log,                           ('1.0->2.5: Billy HeadA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'9f02ef2b': [
        (log,                           ('1.0->2.5: Billy HeadA LightMap 2048p Hash',)),
        (update_hash,                   ('cf4769ce',)),
    ],
'cf4769ce': [
        (log,                           ('2.5: Billy HeadA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('877e1a0d', 'Billy.HeadA.LightMap.1024')),
    ],
'd166c3e5': [
        (log,                           ('1.0->2.5: Billy HeadA MaterialMap 2048p Hash',)),
        (update_hash,                   ('3a7d88a1',)),
    ],
'3a7d88a1': [
        (log,                           ('2.5: Billy HeadA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc2f2dd2', 'Billy.HeadA.MaterialMap.1024')),
    ],
'0475db07': [
        (log,                           ('1.0->2.5: Billy HairA Diffuse 2048p Hash',)),
        (update_hash,                   ('ff939fb7',)),
    ],
'ff939fb7': [
        (log,                           ('2.5: Billy HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c0360c81', 'Billy.HairA.Diffuse.1024')),
    ],
'c0360c81': [
        (log,                           ('1.0: Billy HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ff939fb7', 'Billy.HairA.Diffuse.2048')),
    ],
'4817b1bc': [
        (log,                           ('1.0->2.5: Billy HairA LightMap 2048p Hash',)),
        (update_hash,                   ('b6e1da4b',)),
    ],
'b6e1da4b': [
        (log,                           ('2.5: Billy HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d269a0a1', 'Billy.HairA.LightMap.1024')),
    ],
'd269a0a1': [
        (log,                           ('1.0: Billy HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b6e1da4b', 'Billy.HairA.LightMap.2048')),
    ],
'47bbe297': [
        (log,                           ('1.0->2.5: Billy HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('798adba3',)),
    ],
'798adba3': [
        (log,                           ('2.5: Billy HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('27185819', 'Billy.HairA.NormalMap.1024')),
    ],
'27185819': [
        (log,                           ('1.0: Billy HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('798adba3', 'Billy.HairA.NormalMap.2048')),
    ],
'058d85b5': [
        (log,                           ('2.5: Billy HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'399d9865': [
        (log,                           ('1.0: Billy BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('af07a583', 'Billy.BodyA.Diffuse.1024')),
    ],
'af07a583': [
        (log,                           ('1.0: Billy BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('399d9865', 'Billy.BodyA.Diffuse.2048')),
    ],
'789b054e': [
        (log,                           ('1.0->2.5: Billy BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('6305a7f4',)),
    ],
'6305a7f4': [
        (log,                           ('2.5: Billy BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0d5d374f', 'Billy.BodyA.LightMap.1024')),
    ],
'0d5d374f': [
        (log,                           ('1.0: Billy BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6305a7f4', 'Billy.BodyA.LightMap.2048')),
    ],
'9cb20fa9': [
        (log,                           ('1.0: Billy BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b3cabf65', 'Billy.BodyA.MaterialMap.1024')),
    ],
'b3cabf65': [
        (log,                           ('1.0: Billy BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9cb20fa9', 'Billy.BodyA.MaterialMap.2048')),
    ],
'56b5953e': [
        (log,                           ('1.0->2.5: Billy BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Billy BodyA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('71d95d5d', 'Billy.BodyA.NormalMap.1024')),
    ],
'71d95d5d': [
        (log,                           ('1.0: Billy BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Billy.BodyA.NormalMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Billy',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
