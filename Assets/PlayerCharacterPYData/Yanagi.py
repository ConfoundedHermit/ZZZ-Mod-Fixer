"""
Yanagi Character Hash Commands
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
    Returns Yanagi's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'9e12899f': [(log, ('2.5: Yanagi Hair IB Hash',)),    (add_ib_check_if_missing,)],
'13c75775': [(log, ('2.5: Yanagi Ring IB Hash',)),    (add_ib_check_if_missing,)],
'f478ee4c': [(log, ('2.5: Yanagi Body IB Hash',)),    (add_ib_check_if_missing,)],
'44d9123b': [(log, ('2.5: Yanagi Glasses IB Hash',)),    (add_ib_check_if_missing,)],
'0817204c': [(log, ('2.5: Yanagi Face IB Hash',)),    (add_ib_check_if_missing,)],

# === Hash Updates ===
'fd363c76': [(log, ('2.5: Yanagi Body blend (old hash)',)), (update_hash, ('b558d482',))],
'2e92fc77': [(log, ('2.5: Yanagi Glasses ib (old hash)',)), (update_hash, ('44d9123b',))],
'b558d482': [(log, ('2.5: Yanagi Body blend',)),    (add_ib_check_if_missing,)],

# === Face Textures ===
'cfe7ab46': [
        (log,                           ('2.5: Yanagi FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('95d9e92e', 'Yanagi.FaceA.Diffuse.2048')),
    ],
'95d9e92e': [
        (log,                           ('2.5: Yanagi FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cfe7ab46', 'Yanagi.FaceA.Diffuse.1024')),
    ],

# === Hair Textures ===
'4edb5c79': [
        (log,                           ('2.5: Yanagi HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ac5f6d76', 'Yanagi.HairA.Diffuse.2048')),
    ],
'5a43d985': [
        (log,                           ('2.5: Yanagi HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('99cfa935', 'Yanagi.HairA.LightMap.2048')),
    ],
'486e3c42': [
        (log,                           ('2.5: Yanagi HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f80b57f0', 'Yanagi.HairA.MaterialMap.2048')),
    ],
'ac5f6d76': [
        (log,                           ('2.5: Yanagi HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4edb5c79', 'Yanagi.HairA.Diffuse.1024')),
    ],
'99cfa935': [
        (log,                           ('2.5: Yanagi HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5a43d985', 'Yanagi.HairA.LightMap.1024')),
    ],
'f80b57f0': [
        (log,                           ('2.5: Yanagi HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('486e3c42', 'Yanagi.HairA.MaterialMap.1024')),
    ],

# === Body Textures ===
'c119dbd7': [
        (log,                           ('2.5: Yanagi BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c7c4f5c5', 'Yanagi.BodyA.Diffuse.2048')),
    ],
'f60602ec': [
        (log,                           ('2.5: Yanagi BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('616200aa', 'Yanagi.BodyA.LightMap.2048')),
    ],
'b29f0188': [
        (log,                           ('2.5: Yanagi BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c2ae5d2b', 'Yanagi.BodyA.MaterialMap.2048')),
    ],
'c7c4f5c5': [
        (log,                           ('2.5: Yanagi BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c119dbd7', 'Yanagi.BodyA.Diffuse.1024')),
    ],
'616200aa': [
        (log,                           ('2.5: Yanagi BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f60602ec', 'Yanagi.BodyA.LightMap.1024')),
    ],
'c2ae5d2b': [
        (log,                           ('2.5: Yanagi BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b29f0188', 'Yanagi.BodyA.MaterialMap.1024')),
    ],

# === Ring Textures (shares Hair textures) ===
# Ring uses same texture hashes as Hair: ac5f6d76, 99cfa935, f80b57f0

# === Glasses Textures (shares Hair textures) ===
# Glasses uses same texture hashes as Hair: ac5f6d76, 99cfa935, f80b57f0
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yanagi',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
