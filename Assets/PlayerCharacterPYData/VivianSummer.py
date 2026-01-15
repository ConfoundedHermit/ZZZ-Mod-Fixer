"""
VivianSummer Character Hash Commands
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
    Returns VivianSummer's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Body Component ===
'd96480bc': [(log, ('2.5: VivianSummer Body draw_vb Hash',))],
'5e46216b': [(log, ('2.5: VivianSummer Body position_vb Hash',))],
'723bccec': [(log, ('2.5: VivianSummer Body blend_vb Hash',))],
'fb44f88a': [(log, ('2.5: VivianSummer Body texcoord_vb Hash',))],
'3060793b': [(log, ('2.5: VivianSummer Body IB Hash',)), (add_ib_check_if_missing,)],

# === Face Component ===
'fcf74fc0': [(log, ('2.5: VivianSummer Face draw_vb Hash (shared with Vivian)',))],
'c6e5dc87': [(log, ('2.5: VivianSummer Face position_vb Hash (shared with Vivian)',))],
'ef07b6f6': [(log, ('2.5: VivianSummer Face blend_vb Hash (shared with Vivian)',))],
'0afe5a44': [(log, ('2.5: VivianSummer Face texcoord_vb Hash (shared with Vivian)',))],
'39944f20': [(log, ('2.5: VivianSummer Face IB Hash (shared with Vivian)',)), (add_ib_check_if_missing,)],

# === Hair Component ===
'713a8587': [(log, ('2.5: VivianSummer Hair draw_vb Hash',))],
'bec9acb0': [(log, ('2.5: VivianSummer Hair position_vb Hash',))],
'5b569848': [(log, ('2.5: VivianSummer Hair blend_vb Hash',))],
'128d277f': [(log, ('2.5: VivianSummer Hair texcoord_vb Hash',))],
'4108c0da': [(log, ('2.5: VivianSummer Hair IB Hash',)), (add_ib_check_if_missing,)],

# === Gem Component ===
'9829025f': [(log, ('2.5: VivianSummer Gem draw_vb Hash',))],
'3c88ea03': [(log, ('2.5: VivianSummer Gem position_vb Hash',))],
'53a21868': [(log, ('2.5: VivianSummer Gem blend_vb Hash',))],
'a55d2f46': [(log, ('2.5: VivianSummer Gem texcoord_vb Hash',))],
'ec7b047c': [(log, ('2.5: VivianSummer Gem IB Hash',)), (add_ib_check_if_missing,)],

# === Texture Hashes ===
'7b262ab6': [
        (log,                           ('2.5: VivianSummer FaceA Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n')),
    ],
'15dcce65': [
        (log,                           ('2.5: VivianSummer HairA, BodyC, BodyD, GemA Diffuse Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: VivianSummer HairA, BodyA, GemA NormalMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'8a82d289': [
        (log,                           ('2.5: VivianSummer HairA, BodyC, BodyD, GemA LightMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'c23ddbea': [
        (log,                           ('2.5: VivianSummer HairA, BodyC, BodyD, GemA MaterialMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'a84d933f': [
        (log,                           ('2.5: VivianSummer HairB, HairC Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'8e3a20ea': [
        (log,                           ('2.5: VivianSummer HairB, HairC LightMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'2af66072': [
        (log,                           ('2.5: VivianSummer HairB, HairC MaterialMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'136b3e29': [
        (log,                           ('2.5: VivianSummer BodyA, BodyB Diffuse Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'69a6a15f': [
        (log,                           ('2.5: VivianSummer BodyA, BodyB LightMap Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'527c3676': [
        (log,                           ('2.5: VivianSummer BodyA, BodyB MaterialMap Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'VivianSummer',
    'game_versions': ['2.5'],
}
