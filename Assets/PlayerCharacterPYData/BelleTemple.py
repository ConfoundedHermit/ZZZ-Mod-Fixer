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
'30e40390': [(log, ('2.5: BelleTemple HeadAcc IB Hash',)), (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.5: BelleTemple TorsoAcc IB Hash',)), (add_ib_check_if_missing,)],
'62ed56cc': [(log, ('2.5: BelleTemple Neck IB Hash',)), (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.5: BelleTemple Face IB Hash (Shared with Belle)',)), (add_ib_check_if_missing,)],
'aa9ffb85': [(log, ('2.5: BelleTemple Hair IB Hash',)), (add_ib_check_if_missing,)],
'bcc9e4e1': [(log, ('2.5: BelleTemple Legs IB Hash',)), (add_ib_check_if_missing,)],
'ce86946f': [(log, ('2.5: BelleTemple BackAcc IB Hash',)), (add_ib_check_if_missing,)],
'd509bdd4': [(log, ('2.5: BelleTemple Body IB Hash',)), (add_ib_check_if_missing,)],
'db72ceab': [(log, ('2.5: BelleTemple HairWAcc IB Hash',)), (add_ib_check_if_missing,)],

# =============================================================================
# BelleTemple VB Hashes - HeadAcc
# =============================================================================
'eeea5739': [(log, ('2.5: BelleTemple HeadAcc draw_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],
'17f8b9dc': [(log, ('2.5: BelleTemple HeadAcc position_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],
'e5a8578f': [(log, ('2.5: BelleTemple HeadAcc blend_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],
'fb8393bd': [(log, ('2.5: BelleTemple HeadAcc texcoord_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - TorsoAcc
# =============================================================================
'0406d75f': [(log, ('2.5: BelleTemple TorsoAcc draw_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'7109981c': [(log, ('2.5: BelleTemple TorsoAcc position_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'e147258a': [(log, ('2.5: BelleTemple TorsoAcc blend_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'3e725b6c': [(log, ('2.5: BelleTemple TorsoAcc texcoord_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - BackAcc
# =============================================================================
'83ba6b1f': [(log, ('2.5: BelleTemple BackAcc draw_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],
'601e27b5': [(log, ('2.5: BelleTemple BackAcc position_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],
'1a44a5ba': [(log, ('2.5: BelleTemple BackAcc blend_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],
'81fd09f8': [(log, ('2.5: BelleTemple BackAcc texcoord_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - Hair
# =============================================================================
'992d149f': [(log, ('2.5: BelleTemple Hair draw_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'71d2bf80': [(log, ('2.5: BelleTemple Hair position_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'39ac6700': [(log, ('2.5: BelleTemple Hair blend_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'a5e62ece': [(log, ('2.5: BelleTemple Hair texcoord_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - HairWAcc
# =============================================================================
'040e066c': [(log, ('2.5: BelleTemple HairWAcc draw_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'6824cbbe': [(log, ('2.5: BelleTemple HairWAcc position_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'd5b33c94': [(log, ('2.5: BelleTemple HairWAcc blend_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'c6fe65c9': [(log, ('2.5: BelleTemple HairWAcc texcoord_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - Face
# =============================================================================
'04abceb5': [(log, ('2.5: BelleTemple Face draw_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('2.5: BelleTemple Face position_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],
'0c9a075b': [(log, ('2.5: BelleTemple Face blend_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],
'ccc76aea': [(log, ('2.5: BelleTemple Face texcoord_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - Neck
# =============================================================================
'4c215c73': [(log, ('2.5: BelleTemple Neck draw_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],
'be75a4be': [(log, ('2.5: BelleTemple Neck position_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],
'3bd79a0b': [(log, ('2.5: BelleTemple Neck blend_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],
'dd2b89aa': [(log, ('2.5: BelleTemple Neck texcoord_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - Body
# =============================================================================
'19e5f486': [(log, ('2.5: BelleTemple Body draw_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],
'8a4e97cd': [(log, ('2.5: BelleTemple Body position_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],
'f3dedb50': [(log, ('2.5: BelleTemple Body blend_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],
'd761e076': [(log, ('2.5: BelleTemple Body texcoord_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple VB Hashes - Legs
# =============================================================================
'720d6a16': [(log, ('2.5: BelleTemple Legs draw_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],
'42b88f48': [(log, ('2.5: BelleTemple Legs position_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],
'f53b2eba': [(log, ('2.5: BelleTemple Legs blend_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],
'82d0aadd': [(log, ('2.5: BelleTemple Legs texcoord_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleTemple Body Hash Updates (Old → New)
# =============================================================================
'01b0c8b6': [(log, ('2.5: Updating BelleTemple Body blend_vb to f3dedb50',)), (update_hash, ('f3dedb50',))],
'862dc27a': [(log, ('2.5: Updating BelleTemple Body texcoord_vb to d761e076',)), (update_hash, ('d761e076',))],
'02c9dc4b': [(log, ('2.5: Updating BelleTemple Body draw_vb to 19e5f486',)), (update_hash, ('19e5f486',))],
'860e1558': [(log, ('2.5: Updating BelleTemple Body IB to d509bdd4',)), (update_hash, ('d509bdd4',))],

# =============================================================================
# BelleTemple Neck Hash Updates (Old → New)
# =============================================================================
'20d3a340': [(log, ('2.5: Updating BelleTemple Neck IB to 62ed56cc',)), (update_hash, ('62ed56cc',))],
'2f828e6a': [(log, ('2.5: Updating BelleTemple Neck draw_vb to 4c215c73',)), (update_hash, ('4c215c73',))],
'cdd7fc8a': [(log, ('2.5: Updating BelleTemple Neck texcoord_vb to dd2b89aa',)), (update_hash, ('dd2b89aa',))],
'db7add33': [(log, ('2.5: Updating BelleTemple Neck blend_vb to 3bd79a0b',)), (update_hash, ('3bd79a0b',))],

# =============================================================================
# BelleTemple Face Textures (shares Face IB and Head Diffuse with Belle)
# =============================================================================
# Face Diffuse 2048p: 75ec3614 (same as Belle HeadA Diffuse 2048p)
# This is handled by Belle.py but we ensure the IB check exists

# =============================================================================
# BelleTemple HeadAcc Textures
# =============================================================================
'5e12872e': [
        (log,                           ('2.5: BelleTemple HeadAcc/BackAcc Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],
'714e278c': [
        (log,                           ('2.5: BelleTemple HeadAcc/BackAcc NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],
'54bd71d8': [
        (log,                           ('2.5: BelleTemple HeadAcc/BackAcc LightMap 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],
'd7de8ddf': [
        (log,                           ('2.5: BelleTemple HeadAcc/BackAcc MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# BelleTemple TorsoAcc Textures
# =============================================================================
'5a8f8d57': [
        (log,                           ('2.5: BelleTemple TorsoAcc Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'a7e0cba0': [
        (log,                           ('2.5: BelleTemple TorsoAcc LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'07e9e8f5': [
        (log,                           ('2.5: BelleTemple TorsoAcc MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n')),
    ],

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
        (log,                           ('2.5: BelleTemple Body/Neck/Legs MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('93c5f5ff', 'BelleTemple.BodyNeckLegs.MaterialMap.1024')),
    ],
'93c5f5ff': [
        (log,                           ('2.5: BelleTemple Body/Neck/Legs MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('657402d0', 'BelleTemple.BodyNeckLegs.MaterialMap.2048')),
    ],

# =============================================================================
# BelleTemple Face Textures (Note: Face MaterialMap uses Hair MaterialMap)
# =============================================================================
'75ec3614': [
        (log,                           ('2.5: BelleTemple Face Diffuse 2048p Hash (Shared with Belle)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n')),
    ],
# Face MaterialMap 2048p: 34bdb036 (same as Belle Hair MaterialMap - handled by Belle.py)
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleTemple',
    'display_name': 'Belle (Temple Outfit)',
    'base_character': 'Belle',
    'outfit_type': 'Temple',
    'game_versions': ['2.5'],
}
