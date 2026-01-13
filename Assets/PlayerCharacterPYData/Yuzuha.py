"""
Yuzuha Character Hash Commands
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
    Returns Yuzuha's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'7a504287': [(log, ('2.5: Yuzuha Hair IB Hash',)), (add_ib_check_if_missing,)],
'5144c409': [(log, ('2.5: Yuzuha Body IB Hash',)), (add_ib_check_if_missing,)],
'73757570': [(log, ('2.5: Yuzuha Legs IB Hash',)), (add_ib_check_if_missing,)],
'e72984d1': [(log, ('2.5: Yuzuha Kama IB Hash',)), (add_ib_check_if_missing,)],
'507384ea': [(log, ('2.5: Yuzuha Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'd394bc13': [
        (log,                           ('2.5: Yuzuha FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
    ],

# Hair Textures (shared between Hair and Legs components)
'521a3242': [
        (log,                           ('2.5: Yuzuha Hair/Legs Diffuse Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'c400f5b7': [
        (log,                           ('2.5: Yuzuha Hair/Legs LightMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'3f70d124': [
        (log,                           ('2.5: Yuzuha Hair/Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],

# Body Textures (shared between Body and Kama components)
'be85f061': [
        (log,                           ('2.5: Yuzuha Body/Kama Diffuse Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
'ef192425': [
        (log,                           ('2.5: Yuzuha Body/Kama LightMap Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
'76e5c6b7': [
        (log,                           ('2.5: Yuzuha Body/Kama MaterialMap Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (used across Hair, Body, Legs, and Kama)
'ebac056e': [
        (log,                           ('2.5: Yuzuha Shared NormalMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yuzuha',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Legs', 'Kama', 'Face'],
}
