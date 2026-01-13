"""
Miyabi Character Hash Commands
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
    Returns Miyabi's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'4faabaac': [(log, ('1.4: Miyabi Hair IB Hash',)),   (add_ib_check_if_missing,)],
'981c1a1e': [(log, ('1.4: Miyabi Body IB Hash',)),   (add_ib_check_if_missing,)],
'd8003df3': [(log, ('1.4: Miyabi Legs IB Hash',)),   (add_ib_check_if_missing,)],
'dbd59d30': [(log, ('1.4: Miyabi Face IB Hash',)),   (add_ib_check_if_missing,)],
'1d487fd5': [
        (log,                           ('1.4: Miyabi FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('92599e94', 'Miyabi.FaceA.Diffuse.1024')),
    ],
'92599e94': [
        (log,                           ('1.4: Miyabi FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1d487fd5', 'Miyabi.FaceA.Diffuse.2048')),
    ],
'012e84e9': [
        (log,                           ('1.4: Miyabi HairA, LegsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('ed6b94f7', 'Miyabi.HairA.Diffuse.1024')),
    ],
'a6ea6d83': [
        (log,                           ('1.4: Miyabi HairA, LegsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8b5708f4', 'Miyabi.HairA.LightMap.1024')),
    ],
'd5462e37': [
        (log,                           ('1.4: Miyabi HairA, LegsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a84d9003', 'Miyabi.HairA.MaterialMap.1024')),
    ],
'ed6b94f7': [
        (log,                           ('1.4: Miyabi HairA, LegsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('012e84e9', 'Miyabi.HairA.Diffuse.2048')),
    ],
'8b5708f4': [
        (log,                           ('1.4: Miyabi HairA, LegsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('a6ea6d83', 'Miyabi.HairA.LightMap.2048')),
    ],
'a84d9003': [
        (log,                           ('1.4: Miyabi HairA, LegsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d5462e37', 'Miyabi.HairA.MaterialMap.2048')),
    ],
'09a2bbd1': [
        (log,                           ('1.4: Miyabi BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('1a3644e7', 'Miyabi.BodyA.Diffuse.1024')),
    ],
'fd289380': [
        (log,                           ('1.4: Miyabi BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('0492f64a', 'Miyabi.BodyA.LightMap.1024')),
    ],
'450770fd': [
        (log,                           ('1.4: Miyabi BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('168b1df9', 'Miyabi.BodyA.MaterialMap.1024')),
    ],
'1a3644e7': [
        (log,                           ('1.4: Miyabi BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('09a2bbd1', 'Miyabi.BodyA.Diffuse.2048')),
    ],
'0492f64a': [
        (log,                           ('1.4: Miyabi BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('fd289380', 'Miyabi.BodyA.LightMap.2048')),
    ],
'168b1df9': [
        (log,                           ('1.4: Miyabi BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('450770fd', 'Miyabi.BodyA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Miyabi HairA, BodyA & LegsA NormalMap Hash',)),
        (add_section_if_missing,        ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Miyabi',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
