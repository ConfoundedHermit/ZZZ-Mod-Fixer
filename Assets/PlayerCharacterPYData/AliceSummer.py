"""
AliceSummer Character Hash Commands
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
    Returns AliceSummer's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'd131acb1': [(log, ('2.5: AliceSummer Hair IB Hash',)), (add_ib_check_if_missing,)],
'cf8612e6': [(log, ('2.5: AliceSummer Body IB Hash',)), (add_ib_check_if_missing,)],
'2fcd160b': [(log, ('2.5: AliceSummer Backpack IB Hash',)), (add_ib_check_if_missing,)],
'24d07797': [(log, ('2.5: AliceSummer Sensor IB Hash',)), (add_ib_check_if_missing,)],
'b078ff22': [(log, ('2.5: AliceSummer Face IB Hash',)), (add_ib_check_if_missing,)],
'9f3e582c': [
        (log,                           ('2.5: AliceSummer FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n')),
    ],
'705caac9': [
        (log,                           ('2.5: AliceSummer HairA Diffuse Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: AliceSummer HairA, BodyA, BackpackA NormalMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],
'03543db2': [
        (log,                           ('2.5: AliceSummer HairA LightMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'508530fe': [
        (log,                           ('2.5: AliceSummer HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'18601d57': [
        (log,                           ('2.5: AliceSummer BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'3409fcce': [
        (log,                           ('2.5: AliceSummer BodyA LightMap Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'212fc22a': [
        (log,                           ('2.5: AliceSummer BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'4eff9bd8': [
        (log,                           ('2.5: AliceSummer BackpackA Diffuse Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],
'2a09a850': [
        (log,                           ('2.5: AliceSummer BackpackA LightMap Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],
'1cd2807e': [
        (log,                           ('2.5: AliceSummer BackpackA MaterialMap Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AliceSummer',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
