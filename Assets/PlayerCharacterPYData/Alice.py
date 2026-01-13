"""
Alice Character Hash Commands
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
    Returns Alice's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'd131acb1': [(log, ('2.5: Alice Hair IB Hash',)), (add_ib_check_if_missing,)],
'8a512b21': [(log, ('2.5: Alice Body IB Hash',)), (add_ib_check_if_missing,)],
'625c2692': [(log, ('2.5: Alice Legs IB Hash',)), (add_ib_check_if_missing,)],
'993d2ddd': [(log, ('2.5: Alice Sensor IB Hash',)), (add_ib_check_if_missing,)],
'bd2277ef': [(log, ('2.5: Alice Backpack IB Hash',)), (add_ib_check_if_missing,)],
'b078ff22': [(log, ('2.5: Alice Face IB Hash',)), (add_ib_check_if_missing,)],
'9f3e582c': [
        (log,                           ('2.5: Alice FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],
'705caac9': [
        (log,                           ('2.5: Alice HairA, LegsA Diffuse Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Alice HairA, LegsA, BodyA, BackpackA NormalMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'03543db2': [
        (log,                           ('2.5: Alice HairA, LegsA LightMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'508530fe': [
        (log,                           ('2.5: Alice HairA, LegsA MaterialMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'269185ed': [
        (log,                           ('2.5: Alice BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'0d72cb85': [
        (log,                           ('2.5: Alice BodyA LightMap Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'95967afb': [
        (log,                           ('2.5: Alice BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'79cbbcc4': [
        (log,                           ('2.5: Alice BackpackA Diffuse Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'a226ce08': [
        (log,                           ('2.5: Alice BackpackA LightMap Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'9ada942b': [
        (log,                           ('2.5: Alice BackpackA MaterialMap Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Alice',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
