"""
Koleda Character Hash Commands
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
    Returns Koleda's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'242a8d48': [(log, ('1.0: Koleda Hair IB Hash',)), (add_ib_check_if_missing,)],
'3afb3865': [(log, ('1.0: Koleda Body IB Hash',)), (add_ib_check_if_missing,)],
'0e74656e': [(log, ('1.0: Koleda Head IB Hash',)), (add_ib_check_if_missing,)],
'1a9b182a': [
        (log,            ('1.2 -> 1.3: Koleda Hair Texcoord Hash',)),
        (update_hash,    ('e35571a9',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '13_koleda_hair',
            ('4B','2e','2f','2e'),
            ('4B','2f','2f','2f')
        )),
    ],
'e3021a32': [
        (log,            ('1.2 -> 1.3: Koleda Body Texcoord Hash',)),
        (update_hash,    ('38b31082',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '13_koleda_body',
            ('4B','2e','2f','2e'),
            ('4B','2f','2f','2f')
        )),
    ],
'f1045670': [
        (log,                           ('1.0: Koleda HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('200db5c4', 'Koleda.HeadA.Diffuse.2048')),
    ],
'200db5c4': [
        (log,                           ('1.0: Koleda HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f1045670', 'Koleda.HeadA.Diffuse.1024')),
    ],
'e8e89f00': [
        (log,                           ('1.0: Koleda HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b0046e5a', 'Koleda.HairA.Diffuse.1024')),
    ],
'b0046e5a': [
        (log,                           ('1.0: Koleda HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e8e89f00', 'Koleda.HairA.Diffuse.2048')),
    ],
'8042506d': [
        (log,                           ('1.0 -> 2.5: Koleda HairA LightMap 2048p Hash',)),
        (update_hash,                   ('a451ca03',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('144ab293', 'Koleda.HairA.LightMap.1024')),
    ],
'a451ca03': [
        (log,                           ('2.5: Koleda HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('144ab293', 'Koleda.HairA.LightMap.1024')),
    ],
'144ab293': [
        (log,                           ('1.0: Koleda HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a451ca03', 'Koleda.HairA.LightMap.2048')),
    ],
'd1aac666': [
        (log,                           ('1.0 -> 2.5: Koleda HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7a46b52a', 'Koleda.HairA.NormalMap.1024')),
    ],
'ebac056e': [
        (log,                           ('2.5: Koleda HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7a46b52a', 'Koleda.HairA.NormalMap.1024')),
    ],
'7a46b52a': [
        (log,                           ('1.0: Koleda HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Koleda.HairA.NormalMap.2048')),
    ],
'058d85b5': [
        (log,                           ('2.5: Koleda HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
    ],
'337fd6a2': [
        (log,                           ('1.0: Koleda BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ce10237d', 'Koleda.BodyA.Diffuse.1024')),
    ],
'ce10237d': [
        (log,                           ('1.0: Koleda BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('337fd6a2', 'Koleda.BodyA.Diffuse.2048')),
    ],
'78e0f9f5': [
        (log,                           ('1.0 -> 2.5: Koleda BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('7c1bce32',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('db58787e', 'Koleda.BodyA.LightMap.1024')),
    ],
'7c1bce32': [
        (log,                           ('2.5: Koleda BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('db58787e', 'Koleda.BodyA.LightMap.1024')),
    ],
'db58787e': [
        (log,                           ('1.0: Koleda BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7c1bce32', 'Koleda.BodyA.LightMap.2048')),
    ],
'6f34885f': [
        (log,                           ('1.0 -> 2.5: Koleda BodyA MaterialMap 2048p Hash',)),
        (update_hash,                   ('b60ace0c',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('02e6cb95', 'Koleda.BodyA.MaterialMap.1024')),
    ],
'b60ace0c': [
        (log,                           ('2.5: Koleda BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('02e6cb95', 'Koleda.BodyA.MaterialMap.1024')),
    ],
'02e6cb95': [
        (log,                           ('1.0: Koleda BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b60ace0c', 'Koleda.BodyA.MaterialMap.2048')),
    ],
'e71d134f': [
        (log,                           ('1.0 -> 2.5: Koleda BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0914d3d3', 'Koleda.BodyA.NormalMap.1024')),
    ],
'0914d3d3': [
        (log,                           ('1.0: Koleda BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Koleda.BodyA.NormalMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Koleda',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
