"""
Yidhari Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Yidhari's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'2022936e': [(log, ('2.5: Yidhari Hair IB Hash',)),   (add_ib_check_if_missing,)],
'12251f42': [(log, ('2.5: Yidhari Body IB Hash',)),   (add_ib_check_if_missing,)],
'4cb99618': [(log, ('2.5: Yidhari Tentacles IB Hash',)),   (add_ib_check_if_missing,)],
'1c164f7f': [(log, ('2.5: Yidhari RgbBars IB Hash',)),   (add_ib_check_if_missing,)],
'02072970': [(log, ('2.5: Yidhari Brows IB Hash',)),   (add_ib_check_if_missing,)],
'a2406060': [(log, ('2.5: Yidhari Face IB Hash',)),   (add_ib_check_if_missing,)],

# Hair Textures
'd0587bc2': [
        (log,                           ('2.5: Yidhari HairA Diffuse Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'42ef8882': [
        (log,                           ('2.5: Yidhari HairA LightMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'bc5d6f24': [
        (log,                           ('2.5: Yidhari HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures
'ca51f269': [
        (log,                           ('2.5: Yidhari BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'5b985a6f': [
        (log,                           ('2.5: Yidhari BodyA LightMap Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'0e91ed54': [
        (log,                           ('2.5: Yidhari BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],

# Tentacles Textures
'2156a161': [
        (log,                           ('2.5: Yidhari TentaclesA Diffuse Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'8bf59f48': [
        (log,                           ('2.5: Yidhari TentaclesA LightMap Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'e0bb4de9': [
        (log,                           ('2.5: Yidhari TentaclesA MaterialMap Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],

# Face/Brows Shared Diffuse Texture
'c6e0cfbe': [
        (log,                           ('2.5: Yidhari Face & Brows Diffuse Hash',)),
        (add_section_if_missing,        ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02072970', 'Yidhari.Brows.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (Hair, Body, Tentacles)
'ebac056e': [
        (log,                           ('2.5: Yidhari Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yidhari',
    'game_versions': ['2.5'],
}
