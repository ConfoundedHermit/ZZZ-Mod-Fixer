"""
Corin Character Hash Commands
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
    Returns Corin's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# =========================
# IB Hashes (Index Buffers)
# =========================
'5a839fb2': [(log, ('1.0 -> 2.5: Corin Hair IB Hash',)), (add_ib_check_if_missing,)],
'e74620b5': [(log, ('1.0 -> 2.5: Corin Body IB Hash',)), (add_ib_check_if_missing,)],
'5f803336': [(log, ('1.0 -> 2.5: Corin Bear IB Hash',)), (add_ib_check_if_missing,)],
'a0c80593': [(log, ('1.0 -> 2.5: Corin Head IB Hash',)), (add_ib_check_if_missing,)],

# =========================
# VB Hashes (Vertex Buffers)
# =========================
# Hair VBs
'7e7eee0d': [(log, ('2.5: Corin Hair Position VB Hash',))],
'5fa50113': [(log, ('2.5: Corin Hair Blend VB Hash',))],
'abc95b03': [(log, ('2.5: Corin Hair Texcoord VB Hash',))],
'8d999156': [(log, ('1.3 -> 1.4: Corin Hair Blend Hash (Old)',)), (update_hash, ('5fa50113',))],
'2cf242f4': [(log, ('1.3 -> 1.4: Corin Hair Texcoord Hash (Old)',)), (update_hash, ('abc95b03',))],

# Body VBs
'5dc40184': [(log, ('2.5: Corin Body Position VB Hash',))],
'aa71e514': [(log, ('2.5: Corin Body Blend VB Hash',))],
'4c6b7bda': [(log, ('2.5: Corin Body Texcoord VB Hash',))],

# Bear VBs
'4e1c9e44': [(log, ('2.5: Corin Bear Position VB Hash',))],
'6ffea6f6': [(log, ('2.5: Corin Bear Blend VB Hash',))],
'21987873': [(log, ('2.5: Corin Bear Texcoord VB Hash',))],

# =========================
# Texture Hashes - Face
# =========================
'6d662824': [
        (log,                           ('1.0 -> 2.5: Corin HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0c80593', 'Corin.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('97022d3c', 'Corin.HeadA.Diffuse.1024')),
    ],
'97022d3c': [
        (log,                           ('1.0 -> 2.5: Corin HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0c80593', 'Corin.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6d662824', 'Corin.HeadA.Diffuse.2048')),
    ],

# =========================
# Texture Hashes - Hair
# =========================
# Diffuse
'60526444': [
        (log,                           ('1.0 -> 2.5: Corin HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('651e96f8', 'Corin.HairA.Diffuse.1024')),
    ],
'651e96f8': [
        (log,                           ('1.0 -> 2.5: Corin HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('60526444', 'Corin.HairA.Diffuse.2048')),
    ],

# LightMap
'929aca42': [
        (log,                           ('1.0 -> 1.4: Corin HairA LightMap 2048p Hash (Old)',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (update_hash,                   ('74d66671',)),
    ],
'74d66671': [
        (log,                           ('2.5: Corin HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('edff2372', 'Corin.HairA.LightMap.1024')),
    ],
'edff2372': [
        (log,                           ('1.0 -> 2.5: Corin HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('74d66671', 'Corin.HairA.LightMap.2048')),
    ],

# MaterialMap
'c6398bc8': [
        (log,                           ('2.5: Corin HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
    ],

# NormalMap
'4a68ef99': [
        (log,                           ('1.0 -> 1.4: Corin HairA NormalMap 2048p Hash (Old)',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Corin Hair/Body/Bear Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ab8956c8', 'Corin.HairA.NormalMap.1024')),
    ],
'ab8956c8': [
        (log,                           ('1.0 -> 2.5: Corin HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Corin.HairA.NormalMap.2048')),
    ],

# =========================
# Texture Hashes - Body/Bear (Shared Textures)
# =========================
# Diffuse
'af9d845a': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('681f5162', 'Corin.BodyA.Diffuse.1024')),
    ],
'681f5162': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('af9d845a', 'Corin.BodyA.Diffuse.2048')),
    ],

# LightMap
'75e05cdc': [
        (log,                           ('1.0 -> 1.4: Corin BodyA, BearA LightMap 2048p Hash (Old)',)),
        (update_hash,                   ('e1c1718f',)),
    ],
'e1c1718f': [
        (log,                           ('2.5: Corin BodyA, BearA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('af7eda82', 'Corin.BodyA.LightMap.1024')),
    ],
'af7eda82': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e1c1718f', 'Corin.BodyA.LightMap.2048')),
    ],

# MaterialMap
'50a0faea': [
        (log,                           ('1.0 -> 1.4: Corin BodyA, BearA MaterialMap 2048p Hash (Old)',)),
        (update_hash,                   ('e58d9767',)),
    ],
'e58d9767': [
        (log,                           ('2.5: Corin BodyA, BearA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('9dc9c0f6', 'Corin.BodyA.MaterialMap.1024')),
    ],
'9dc9c0f6': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e58d9767', 'Corin.BodyA.MaterialMap.2048')),
    ],

# NormalMap (Note: Uses same hash as Hair - ebac056e)
'289f4c58': [
        (log,                           ('1.0 -> 1.4: Corin BodyA, BearA NormalMap 2048p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'640141d4': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA NormalMap 1024p Hash',)),
        (multiply_section_if_missing,   ('ebac056e', 'Corin.BodyA.NormalMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Corin',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
