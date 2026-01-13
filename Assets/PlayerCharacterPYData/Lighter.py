"""
Lighter Character Hash Commands
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
    Returns Lighter's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'542b8aa9': [(log, ('2.5: Lighter Hair IB Hash',)),           (add_ib_check_if_missing,)],
'037b6287': [(log, ('2.5: Lighter Hair Position Hash',))],
'22a08e39': [(log, ('2.5: Lighter Hair Texcoord Hash',))],
'd88fa0aa': [(log, ('2.5: Lighter Hair Blend Hash',))],

# === Body Component ===
'8899e0fd': [(log, ('2.5: Lighter Body IB Hash',)),           (add_ib_check_if_missing,)],
'f6bbabb5': [(log, ('2.5: Lighter Body Position Hash',))],
'e1ae7f38': [(log, ('2.5: Lighter Body Texcoord Hash',))],
'da216bb6': [(log, ('2.5: Lighter Body Blend Hash',))],

# === Face Component ===
'039f30cf': [(log, ('1.3 -> 1.4: Lighter Face IB Hash',)),    (update_hash, ('dcc7bb78',))],
'dcc7bb78': [(log, ('2.5: Lighter Face IB Hash',)),           (add_ib_check_if_missing,)],

# === Glasses Component ===
'b20b7cd5': [(log, ('2.5: Lighter Glasses IB Hash',)),        (add_ib_check_if_missing,)],
'fc862707': [(log, ('2.5: Lighter Glasses Position Hash',))],
'527dad23': [(log, ('2.5: Lighter Glasses Texcoord Hash',))],
'3395524c': [(log, ('2.5: Lighter Glasses Blend Hash',))],

# === Legacy Hash Updates ===
'0baec6b7': [(log, ('1.3 -> 1.4: Lighter Body Position Hash',)), (update_hash, ('5e461440',))],
'710bca71': [(log, ('1.3 -> 1.4: Lighter Body Texcoord Hash',)), (update_hash, ('25ad7289',))],
'5e461440': [(log, ('1.5 -> 1.6: Lighter Body Position Hash',)), (update_hash, ('f6bbabb5',))],
'25ad7289': [(log, ('1.5 -> 1.6: Lighter Body Texcoord Hash',)), (update_hash, ('e1ae7f38',))],

# === Face Textures ===
'8ec33dd0': [
        (log,                           ('2.5: Lighter FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('dcc7bb78', '039f30cf'), 'Lighter.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4524e91a', 'Lighter.FaceA.Diffuse.2048')),
    ],
'4524e91a': [
        (log,                           ('2.5: Lighter FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('dcc7bb78', '039f30cf'), 'Lighter.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8ec33dd0', 'Lighter.FaceA.Diffuse.1024')),
    ],

# === Hair Textures ===
'1cd2d442': [
        (log,                           ('2.5: Lighter HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c5d60a1d', 'Lighter.HairA.Diffuse.2048')),
    ],
'62ec7f01': [
        (log,                           ('2.5: Lighter HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6d3f91bc', 'Lighter.HairA.LightMap.2048')),
    ],
'8687f7b8': [
        (log,                           ('2.5: Lighter HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d5ba9ea6', 'Lighter.HairA.MaterialMap.2048')),
    ],
'c5d60a1d': [
        (log,                           ('2.5: Lighter HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1cd2d442', 'Lighter.HairA.Diffuse.1024')),
    ],
'6d3f91bc': [
        (log,                           ('2.5: Lighter HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('62ec7f01', 'Lighter.HairA.LightMap.1024')),
    ],
'd5ba9ea6': [
        (log,                           ('2.5: Lighter HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8687f7b8', 'Lighter.HairA.MaterialMap.1024')),
    ],

# === Body Textures ===
'be46890b': [
        (log,                           ('2.5: Lighter BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5ed96bf2', 'Lighter.BodyA.Diffuse.2048')),
    ],
'5b828635': [
        (log,                           ('2.5: Lighter BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da6f4dc0', 'Lighter.BodyA.LightMap.2048')),
    ],
'65f3bb7c': [
        (log,                           ('2.5: Lighter BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('94aebd7e', 'Lighter.BodyA.MaterialMap.2048')),
    ],
'5ed96bf2': [
        (log,                           ('2.5: Lighter BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('be46890b', 'Lighter.BodyA.Diffuse.1024')),
    ],
'da6f4dc0': [
        (log,                           ('2.5: Lighter BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5b828635', 'Lighter.BodyA.LightMap.1024')),
    ],
'94aebd7e': [
        (log,                           ('2.5: Lighter BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('65f3bb7c', 'Lighter.BodyA.MaterialMap.1024')),
    ],

# === Glasses Textures (Uses Body Textures) ===
# Note: Glasses component shares BodyA textures, no separate texture hashes needed
# The IB and VB hashes are defined above in the Glasses Component section
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lighter',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
