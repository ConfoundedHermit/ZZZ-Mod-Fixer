"""
Pulchra Character Hash Commands
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
    Returns Pulchra's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'bd385763': [(log, ('2.5: Pulchra Body (Hair) IB Hash',)), (add_ib_check_if_missing,)],
'5b30f4da': [(log, ('2.5: Pulchra Mask IB Hash',)), (add_ib_check_if_missing,)],
'62de5837': [(log, ('2.5: Pulchra Face IB Hash',)), (add_ib_check_if_missing,)],

# === Face Textures ===
'1626aafe': [
        (log,                           ('2.5: Pulchra FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('32f923f1', 'Pulchra.FaceA.Diffuse.1024')),
    ],
'32f923f1': [
        (log,                           ('2.5: Pulchra FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1626aafe', 'Pulchra.FaceA.Diffuse.2048')),
    ],

# === Hair Textures (BodyB) ===
'57be79d6': [
        (log,                           ('2.5: Pulchra HairB Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fb0a816a', 'Pulchra.HairB.Diffuse.1024')),
    ],
'fb0a816a': [
        (log,                           ('2.5: Pulchra HairB Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('57be79d6', 'Pulchra.HairB.Diffuse.2048')),
    ],
'12c44063': [
        (log,                           ('2.5: Pulchra HairB LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f475e822', 'Pulchra.HairB.LightMap.1024')),
    ],
'f475e822': [
        (log,                           ('2.5: Pulchra HairB LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('12c44063', 'Pulchra.HairB.LightMap.2048')),
    ],
'a553df20': [
        (log,                           ('2.5: Pulchra HairB MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('64d75415', 'Pulchra.HairB.MaterialMap.1024')),
    ],
'64d75415': [
        (log,                           ('2.5: Pulchra HairB MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a553df20', 'Pulchra.HairB.MaterialMap.2048')),
    ],

# === Body Textures (BodyA) ===
'7fc03353': [
        (log,                           ('2.5: Pulchra BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf7eba0f', 'Pulchra.BodyA.Diffuse.1024')),
    ],
'bf7eba0f': [
        (log,                           ('2.5: Pulchra BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7fc03353', 'Pulchra.BodyA.Diffuse.2048')),
    ],
'd8462af0': [
        (log,                           ('2.5: Pulchra BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('47040200', 'Pulchra.BodyA.LightMap.1024')),
    ],
'47040200': [
        (log,                           ('2.5: Pulchra BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d8462af0', 'Pulchra.BodyA.LightMap.2048')),
    ],
'd404b789': [
        (log,                           ('2.5: Pulchra BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a66a11d0', 'Pulchra.BodyA.MaterialMap.1024')),
    ],
'a66a11d0': [
        (log,                           ('2.5: Pulchra BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d404b789', 'Pulchra.BodyA.MaterialMap.2048')),
    ],

# === Mask Textures (MaskA) ===
'46bab365': [
        (log,                           ('2.5: Pulchra MaskA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'03d28ecd': [
        (log,                           ('2.5: Pulchra MaskA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'320a1179': [
        (log,                           ('2.5: Pulchra MaskA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pulchra',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
