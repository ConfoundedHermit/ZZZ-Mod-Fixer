"""
Manato Character Hash Commands
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
    Returns Manato's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'de57398c': [(log, ('2.5: Manato Hair IB Hash',)), (add_ib_check_if_missing,)],

# Hair Textures (shared with LowerBody)
'81a04fa6': [
        (log,                           ('2.5: Manato Hair, LowerBody Diffuse Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'2bfdcb76': [
        (log,                           ('2.5: Manato Hair, LowerBody LightMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'b9654ab9': [
        (log,                           ('2.5: Manato Hair, LowerBody MaterialMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],

# === UpperBody Component ===
'f4c1c6d9': [(log, ('2.5: Manato UpperBody IB Hash',)), (add_ib_check_if_missing,)],

# UpperBody Textures (shared with Accessories)
'9e78d2c7': [
        (log,                           ('2.5: Manato UpperBody, Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'53c85c6a': [
        (log,                           ('2.5: Manato UpperBody, Accessories LightMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'fdc49789': [
        (log,                           ('2.5: Manato UpperBody, Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],

# === LowerBody Component ===
'c0425328': [(log, ('2.5: Manato LowerBody IB Hash',)), (add_ib_check_if_missing,)],

# === Accessories Component ===
'fe66c6d2': [(log, ('2.5: Manato Accessories IB Hash',)), (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: Manato Shared NormalMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Face Component ===
'f987f156': [(log, ('2.5: Manato Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'6d1343ec': [
        (log,                           ('2.5: Manato Face Diffuse Hash',)),
        (add_section_if_missing,        ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Manato',
    'game_versions': ['2.5'],
}
