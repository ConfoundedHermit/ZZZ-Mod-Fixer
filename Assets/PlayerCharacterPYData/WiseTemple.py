"""
Wise Temple Outfit Character Hash Commands
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
    Returns Wise Temple outfit's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# =============================================================================
# WiseTemple IB Hashes
# =============================================================================
'01c42a1d': [(log, ('2.5: WiseTemple Neck IB Hash',)), (add_ib_check_if_missing,)],
'1eca2097': [(log, ('2.5: WiseTemple Body IB Hash',)), (add_ib_check_if_missing,)],
'1fdaf388': [(log, ('2.5: WiseTemple Face IB Hash',)), (add_ib_check_if_missing,)],
'd5ca0411': [(log, ('2.5: WiseTemple Hair IB Hash',)), (add_ib_check_if_missing,)],
'e7f527ea': [(log, ('2.5: WiseTemple DiskPlayer IB Hash',)), (add_ib_check_if_missing,)],

# =============================================================================
# WiseTemple Face Textures
# =============================================================================
'5d75fddc': [
        (log,                           ('2.5: WiseTemple Face Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
    ],

'a15aa6b3': [
        (log,                           ('2.5: WiseTemple Face/DiskPlayer MaterialMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# WiseTemple Hair Textures
# =============================================================================
'28005a5b': [
        (log,                           ('2.5: WiseTemple Hair Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],

'8d8269f8': [
        (log,                           ('2.5: WiseTemple Hair LightMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],

'f1b20f3d': [
        (log,                           ('2.5: WiseTemple Hair MaterialMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# WiseTemple Body/Neck Shared Textures
# =============================================================================
'81406abe': [
        (log,                           ('2.5: WiseTemple Body/Neck Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],

'05b25d35': [
        (log,                           ('2.5: WiseTemple Body/Neck LightMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],

'24af1f48': [
        (log,                           ('2.5: WiseTemple Body/Neck MaterialMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# WiseTemple DiskPlayer Textures
# =============================================================================
'3fef0e14': [
        (log,                           ('2.5: WiseTemple DiskPlayer Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

'08b27f4a': [
        (log,                           ('2.5: WiseTemple DiskPlayer LightMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# Shared NormalMap (Hair/Body/Neck/DiskPlayer)
# =============================================================================
'ebac056e': [
        (log,                           ('2.5: WiseTemple Shared NormalMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseTemple',
    'display_name': 'Wise (Temple Outfit)',
    'base_character': 'Wise',
    'outfit_type': 'Temple',
    'game_versions': ['2.5'],
}
