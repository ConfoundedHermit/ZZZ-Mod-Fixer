"""
Banyue Character Hash Commands
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
    Returns Banyue's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==================== Hair Component ====================
'f3b6e869': [(log, ('2.5: Banyue Hair IB Hash',)), (add_ib_check_if_missing,)],
'0a1f42fb': [
        (log,                           ('2.5: Banyue HairA Diffuse Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Banyue Hair/Legs/Body NormalMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'81cd7414': [
        (log,                           ('2.5: Banyue HairA LightMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'ef8ba12a': [
        (log,                           ('2.5: Banyue HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],

# ==================== Legs Component ====================
'5f855404': [(log, ('2.5: Banyue Legs IB Hash',)), (add_ib_check_if_missing,)],
'a75cf25e': [
        (log,                           ('2.5: Banyue LegsA Diffuse Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
# Note: ebac056e NormalMap is shared with Hair and Body components above
'1003c4df': [
        (log,                           ('2.5: Banyue LegsA LightMap Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
'1125ccff': [
        (log,                           ('2.5: Banyue LegsA MaterialMap Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],

# ==================== Body Component ====================
'698046e6': [(log, ('2.5: Banyue Body IB Hash',)), (add_ib_check_if_missing,)],
'19c3125c': [
        (log,                           ('2.5: Banyue BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
# Note: ebac056e NormalMap is shared with Hair and Legs components above
'f44f6316': [
        (log,                           ('2.5: Banyue BodyA LightMap Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'7099d2dc': [
        (log,                           ('2.5: Banyue BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Banyue',
    'element': 'Fire',
    'faction': 'Yunkui Summit',
    'game_versions': ['2.5'],
}
