"""
AstraChandelier Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 1.5 - 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns AstraChandelier's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==================== Hair Component ====================
'53cdac6c': [(log, ('2.5: AstraChandelier Hair IB Hash',)), (add_ib_check_if_missing,)],
'e634238a': [
        (log,                           ('2.5: AstraChandelier HairA Diffuse Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: AstraChandelier Hair/Body NormalMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'34f0706c': [
        (log,                           ('2.5: AstraChandelier HairA LightMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'883a578f': [
        (log,                           ('2.5: AstraChandelier HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],

# ==================== Body Component ====================
'02d8a2cb': [(log, ('1.5 - 2.5: AstraChandelier Body IB Hash',)), (add_ib_check_if_missing,)],
'7301ca3a': [
        (log,                           ('1.5 - 2.5: AstraChandelier BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
# Note: ebac056e NormalMap is shared with Hair component above
'7ce9f1db': [(log, ('1.5 -> 2.5: AstraChandelier BodyA LightMap Hash',)),   (update_hash, ('515f9beb',))],
'515f9beb': [
        (log,                           ('2.5: AstraChandelier BodyA LightMap Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'56abc3a3': [(log, ('1.5 -> 1.6: AstraChandelier BodyA MaterialMap Hash',)),   (update_hash, ('43a4d256',))],
'43a4d256': [(log, ('1.6 -> 2.5: AstraChandelier BodyA MaterialMap Hash',)),   (update_hash, ('fa2f509f',))],
'fa2f509f': [
        (log,                           ('2.5: AstraChandelier BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],

# ==================== Face Component ====================
'51831437': [(log, ('2.5: AstraChandelier Face IB Hash',)), (add_ib_check_if_missing,)],
'c41341b2': [
        (log,                           ('2.5: AstraChandelier FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AstraChandelier',
    'element': 'Fire',
    'faction': 'Obol Squad',
    'game_versions': ['1.5', '1.6', '1.7', '2.5'],
}
