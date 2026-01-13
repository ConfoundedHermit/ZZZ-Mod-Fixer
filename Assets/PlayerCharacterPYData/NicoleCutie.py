"""
NicoleCutie Character Hash Commands
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
    Returns NicoleCutie's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'776f5703': [(log, ('2.5: NicoleCutie Hair IB Hash',)), (add_ib_check_if_missing,)],
'52842f31': [(log, ('2.5: NicoleCutie Body IB Hash',)), (add_ib_check_if_missing,)],
'262c96ff': [(log, ('2.5: NicoleCutie Phone IB Hash',)), (add_ib_check_if_missing,)],
'40e64ae2': [(log, ('2.5: NicoleCutie Amillion IB Hash',)), (add_ib_check_if_missing,)],
'7435fc0e': [(log, ('2.5: NicoleCutie Face IB Hash',)), (add_ib_check_if_missing,)],
'd1e84a34': [
        (log,                           ('2.5: NicoleCutie FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'cdaa9ab5': [
        (log,                           ('2.5: NicoleCutie HairA Diffuse Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: NicoleCutie HairA, BodyA, PhoneA, AmillionA NormalMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'4c8b0bce': [
        (log,                           ('2.5: NicoleCutie HairA LightMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'a05c2386': [
        (log,                           ('2.5: NicoleCutie HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'4af0010c': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA Diffuse Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'c45a93a3': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA LightMap Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'592cee08': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA MaterialMap Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'6986beb1': [
        (log,                           ('2.5: NicoleCutie PhoneA Diffuse Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'4ae94b82': [
        (log,                           ('2.5: NicoleCutie PhoneA LightMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'4bbaadb9': [
        (log,                           ('2.5: NicoleCutie PhoneA MaterialMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NicoleCutie',
    'game_versions': ['2.5'],
}
