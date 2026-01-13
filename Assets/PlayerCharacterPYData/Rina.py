"""
Rina Character Hash Commands
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
    Returns Rina's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'cdb2cc7d': [(log, ('1.0: Rina Hair IB Hash',)), (add_ib_check_if_missing,)],
'2825da1e': [(log, ('1.0: Rina Body IB Hash',)), (add_ib_check_if_missing,)],
'9f90cfaa': [(log, ('1.0: Rina Head IB Hash',)), (add_ib_check_if_missing,)],
'7ecc44ce': [
        (log,                           ('1.0: Rina HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9f90cfaa', 'Rina.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('802a3281', 'Rina.HeadA.Diffuse.2048')),
    ],
'802a3281': [
        (log,                           ('1.0: Rina HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9f90cfaa', 'Rina.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7ecc44ce', 'Rina.HeadA.Diffuse.1024')),
    ],
'eb5d9d1c': [
        (log,                           ('1.0: Rina HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4b005a79', 'Rina.HairA.Diffuse.1024')),
    ],
'4b005a79': [
        (log,                           ('1.0: Rina HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('eb5d9d1c', 'Rina.HairA.Diffuse.2048')),
    ],
'1145d2b8': [
        (log,                           ('1.0: Rina HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fb61499f', 'Rina.HairA.LightMap.1024')),
    ],
'fb61499f': [
        (log,                           ('1.0: Rina HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1145d2b8', 'Rina.HairA.LightMap.2048')),
    ],
'82153e28': [
        (log,                           ('1.0: Rina HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ea08fd96', 'Rina.HairA.MaterialMap.1024')),
    ],
'ea08fd96': [
        (log,                           ('1.0: Rina HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('82153e28', 'Rina.HairA.MaterialMap.2048')),
    ],
'83ac7993': [
        (log,                           ('1.0 -> 2.5: Rina HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Rina Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
    ],
'fa3c40e9': [
        (log,                           ('1.0: Rina HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('83ac7993', 'Rina.HairA.NormalMap.2048')),
    ],
'bf44bf67': [
        (log,                           ('1.0: Rina BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a23e2e14', 'Rina.BodyA.Diffuse.1024')),
    ],
'a23e2e14': [
        (log,                           ('1.0: Rina BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf44bf67', 'Rina.BodyA.Diffuse.2048')),
    ],
'95f4e9c8': [
        (log,                           ('1.0: Rina BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fad76987', 'Rina.BodyA.LightMap.1024')),
    ],
'fad76987': [
        (log,                           ('1.0: Rina BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('95f4e9c8', 'Rina.BodyA.LightMap.2048')),
    ],
'ed47722f': [
        (log,                           ('1.0: Rina BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9fa6dfd3', 'Rina.BodyA.MaterialMap.1024')),
    ],
'9fa6dfd3': [
        (log,                           ('1.0: Rina BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ed47722f', 'Rina.BodyA.MaterialMap.2048')),
    ],
'97637a8f': [
        (log,                           ('1.0 -> 2.5: Rina BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'd6b20159': [
        (log,                           ('1.0: Rina BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('97637a8f', 'Rina.BodyA.NormalMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Rina',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
