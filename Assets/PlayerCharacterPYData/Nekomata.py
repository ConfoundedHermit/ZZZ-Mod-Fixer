"""
Nekomata Character Hash Commands
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
    Returns Nekomata's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'da11fd85': [(log, ('1.0: Nekomata Hair IB Hash',)),   (add_ib_check_if_missing,)],
'26a487ff': [(log, ('1.0: Nekomata Body IB Hash',)),   (add_ib_check_if_missing,)],
'74688145': [(log, ('1.0: Nekomata Swords IB Hash',)), (add_ib_check_if_missing,)],
'37119851': [(log, ('1.0: Nekomata Head IB Hash',)),   (add_ib_check_if_missing,)],
'd9370c84': [(log, ('1.0 -> 1.1: Nekomata HeadA Diffuse 1024p Hash',)), (update_hash, ('0834f635',))],
'0834f635': [
        (log,                           ('1.1: Nekomata HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ba411d22', 'fed3abbe'), 'Nekomata.HeadA.Diffuse.2048')),
    ],
'fed3abbe': [(log, ('1.0 -> 1.1: Nekomata HeadA Diffuse 2048p Hash',)), (update_hash, ('ba411d22',))],
'ba411d22': [
        (log,                           ('1.1: Nekomata HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('0834f635', 'd9370c84'), 'Nekomata.HeadA.Diffuse.1024')),
    ],
'2c317dda': [(log, ('1.0 -> 1.1: Nekomata Body Position Hash',)),  (update_hash, ('eaad1408',))],
'b5a4c084': [(log, ('1.0 -> 1.1: Nekomata Body Texcoord Hash',)),  (update_hash, ('f589a51f',))],
'd73bc96f': [(log, ('1.0 -> 1.1: Nekomata Body Blend Hash',)),  (update_hash, ('d27d0e6b',))],
'6abb714e': [(log, ('1.0 -> 1.1: Nekomata Swords Position Hash',)), (update_hash, ('3c4015fd',))],
'70f4875e': [(log, ('1.0 -> 1.1: Nekomata Swords Texcoord Hash',)), (update_hash, ('2a4f8c9e',))],
'25f3ae9b': [
        (log,                           ('1.0: Nekomata HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('aed3d8bd', 'Nekomata.HairA.Diffuse.1024')),
    ],
'aed3d8bd': [
        (log,                           ('1.0: Nekomata HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('25f3ae9b', 'Nekomata.HairA.Diffuse.2048')),
    ],
'548c7f7d': [(log, ('1.0 -> 2.5: Nekomata HairA LightMap 2048p Hash',)), (update_hash, ('1c0193dc',))],
'1c0193dc': [
        (log,                           ('2.5: Nekomata HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('f8accad8', 'Nekomata.HairA.LightMap.1024')),
    ],
'f8accad8': [
        (log,                           ('1.0: Nekomata HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('1c0193dc', 'Nekomata.HairA.LightMap.2048')),
    ],
'4ca5efc6': [(log, ('1.0 -> 2.5: Nekomata HairA MaterialMap 2048p Hash',)), (update_hash, ('3f73186f',))],
'3f73186f': [
        (log,                           ('2.5: Nekomata HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('0c22352c', 'Nekomata.HairA.MaterialMap.1024')),
    ],
'0c22352c': [
        (log,                           ('1.0: Nekomata HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('3f73186f', 'Nekomata.HairA.MaterialMap.2048')),
    ],
'799eb07d': [(log, ('1.0 -> 2.5: Nekomata HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'c936ea68': [(log, ('1.0: Nekomata HairA NormalMap 1024p Hash',)), (multiply_section_if_missing, ('ebac056e', 'Nekomata.HairA.NormalMap.2048'))],
'd3f67c0d': [
        (log,                           ('1.0: -> 1.1: Nekomata HairB, BodyA, SwordsA Diffuse 2048p Hash',)),
        (update_hash,                   ('207b8e63',)),
    ],
'207b8e63': [
        (log,                           ('1.0: Nekomata HairB, BodyA, SwordsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('60687646', '37d3154d'), 'Nekomata.HairB.Diffuse.1024')),
    ],
'37d3154d': [
        (log,                           ('1.0: -> 1.1: Nekomata HairB, BodyA, SwordsA Diffuse 1024p Hash',)),
        (update_hash,                   ('60687646',)),
    ],
'60687646': [
        (log,                           ('1.1 Nekomata HairB, BodyA, SwordsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('207b8e63', 'd3f67c0d'), 'Nekomata.HairB.Diffuse.2048')),
    ],
'fc53fc6f': [(log, ('1.0 -> 2.5: Nekomata HairB, BodyA, SwordsA LightMap 2048p Hash',)), (update_hash, ('25df29e7',))],
'25df29e7': [
        (log,                           ('2.5: Nekomata HairB, BodyA, SwordsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('4f3f7df0', 'Nekomata.HairB.LightMap.1024')),
    ],
'4f3f7df0': [
        (log,                           ('1.0: Nekomata HairB, BodyA, SwordsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('25df29e7', 'Nekomata.HairB.LightMap.2048')),
    ],
'f26828bd': [
        (log,                           ('1.0: Nekomata HairB, BodyA, SwordsA MaterialMap 2048p Hash',)),
        (update_hash,                   ('b3286755',)),
    ],
'b3286755': [
        (log,                           ('1.1: Nekomata HairB, BodyA, SwordsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   (('a5529690', '424da647'), 'Nekomata.HairB.MaterialMap.1024')),
    ],
'424da647': [
        (log,                           ('1.0 -> 1.1: Nekomata HairB, BodyA, SwordsA MaterialMap 1024p Hash',)),
        (update_hash,                   ('a5529690',)),
    ],
'a5529690': [
        (log,                           ('1.1: Nekomata HairB, BodyA, SwordsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   (('b3286755', 'f26828bd'), 'Nekomata.HairB.MaterialMap.2048')),
    ],
'ecaef71c': [(log, ('1.0 -> 2.5: Nekomata HairB, BodyA, SwordsA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'c1933b38': [(log, ('1.0: Nekomata HairB, BodyA, SwordsA NormalMap 1024p Hash',)), (multiply_section_if_missing, ('ebac056e', 'Nekomata.HairB.NormalMap.2048'))],
'ebac056e': [
        (log,                           ('2.5: Nekomata Shared NormalMap 2048p Hash (HairA, HairB, BodyA, SwordsA)',)),
        (multiply_section_if_missing,   (('c936ea68', 'c1933b38'), 'Nekomata.Shared.NormalMap.1024')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Nekomata',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
