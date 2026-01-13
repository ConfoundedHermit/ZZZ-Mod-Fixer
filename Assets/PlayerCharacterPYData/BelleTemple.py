"""
Belle Temple Outfit Character Hash Commands
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
    Returns Belle Temple outfit's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# =============================================================================
# BelleTemple IB Hashes
# =============================================================================
'62ed56cc': [(log, ('2.5: BelleTemple Neck IB Hash',)), (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.5: BelleTemple Face IB Hash (Shared with Belle)',)), (add_ib_check_if_missing,)],
'aa9ffb85': [(log, ('2.5: BelleTemple Hair IB Hash',)), (add_ib_check_if_missing,)],
'bcc9e4e1': [(log, ('2.5: BelleTemple Legs IB Hash',)), (add_ib_check_if_missing,)],
'd509bdd4': [(log, ('2.5: BelleTemple Body IB Hash',)), (add_ib_check_if_missing,)],

# =============================================================================
# BelleTemple Face Textures (shares Face IB and Head Diffuse with Belle)
# =============================================================================
# Face Diffuse 2048p: 75ec3614 (same as Belle HeadA Diffuse 2048p)
# This is handled by Belle.py but we ensure the IB check exists

# =============================================================================
# BelleTemple Hair Textures (shares texture hashes with Belle)
# =============================================================================
# Hair Diffuse 2048p: 1ce58567 (same as Belle HairA Diffuse 2048p)
# Hair LightMap 2048p: 7d562f53 (same as Belle HairA LightMap 2048p) 
# Hair MaterialMap 2048p: 34bdb036 (same as Belle HairA MaterialMap 2048p)
# Hair NormalMap 2048p: ebac056e (same as Belle shared NormalMap)
# These are handled by Belle.py but we ensure the IB check exists for BelleTemple Hair IB

# =============================================================================
# BelleTemple Body/Neck/Legs Shared Textures
# =============================================================================
'da2bfe2f': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0a2e0f42', 'BelleTemple.BodyNeckLegs.Diffuse.1024')),
    ],
'0a2e0f42': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da2bfe2f', 'BelleTemple.BodyNeckLegs.Diffuse.2048')),
    ],

# NormalMap: ebac056e (same as Belle - shared across Hair+Body)
# This is handled by Belle.py with add_section_if_missing calls

'74f2fae3': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs LightMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f8e4e93a', 'BelleTemple.BodyNeckLegs.LightMap.1024')),
    ],
'f8e4e93a': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs LightMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('74f2fae3', 'BelleTemple.BodyNeckLegs.LightMap.2048')),
    ],

'657402d0': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs/Face MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('93c5f5ff', 'BelleTemple.BodyNeckLegsFace.MaterialMap.1024')),
    ],
'93c5f5ff': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs/Face MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('657402d0', 'BelleTemple.BodyNeckLegsFace.MaterialMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleTemple',
    'display_name': 'Belle (Temple Outfit)',
    'base_character': 'Belle',
    'outfit_type': 'Temple',
    'game_versions': ['2.5'],
}
