"""
Vivian Character Hash Commands
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
    Returns Vivian's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'2e01f7f7': [(log, ('2.5: Vivian Hair Draw VB Hash',))],
'71d0dfd9': [(log, ('2.5: Vivian Hair Position VB Hash',))],
'ef4a8bb6': [(log, ('2.5: Vivian Hair Blend VB Hash',))],
'406beb54': [(log, ('2.5: Vivian Hair Texcoord VB Hash',))],
'c4eb6168': [(log, ('2.5: Vivian Hair IB Hash',)), (add_ib_check_if_missing,)],
'5c34690a': [(log, ('2.5: Vivian Body Draw VB Hash',))],
'64a6b06d': [(log, ('2.5: Vivian Body Position VB Hash',))],
'e7122fe8': [(log, ('2.5: Vivian Body Blend VB Hash',))],
'55dae493': [(log, ('2.5: Vivian Body Texcoord VB Hash',))],
'cd609d98': [(log, ('2.5: Vivian Body IB Hash',)), (add_ib_check_if_missing,)],
'8a6fd2f9': [(log, ('2.5: Vivian Gem Draw VB Hash',))],
'3c32547b': [(log, ('2.5: Vivian Gem Position VB Hash',))],
'a23da1ce': [(log, ('2.5: Vivian Gem Blend VB Hash',))],
'45c0ac67': [(log, ('2.5: Vivian Gem Texcoord VB Hash',))],
'14602a61': [(log, ('2.5: Vivian Gem IB Hash',)), (add_ib_check_if_missing,)],
'39944f20': [(log, ('2.5: Vivian Face IB Hash',)), (add_ib_check_if_missing,)],
'7b262ab6': [
        (log,                           ('2.5: Vivian FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('66b5da8e', 'Vivian.FaceA.Diffuse.1024')),
    ],
'66b5da8e': [
        (log,                           ('2.5: Vivian FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7b262ab6', 'Vivian.FaceA.Diffuse.2048')),
    ],
'a84d933f': [
        (log,                           ('2.5: Vivian Hair/GemA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2df6f7b5', 'Vivian.Hair/GemA.Diffuse.1024')),
    ],
'2df6f7b5': [
        (log,                           ('2.5: Vivian Hair/GemA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a84d933f', 'Vivian.Hair/GemA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Vivian NormalMap Hash (Hair/Body/Gem)',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
    ],
'8e3a20ea': [
        (log,                           ('2.5: Vivian Hair/GemA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('36b80366', 'Vivian.Hair/GemA.LightMap.1024')),
    ],
'36b80366': [
        (log,                           ('2.5: Vivian Hair/GemA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8e3a20ea', 'Vivian.Hair/GemA.LightMap.2048')),
    ],
'2af66072': [
        (log,                           ('2.5: Vivian Hair/GemA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2d5b1412', 'Vivian.Hair/GemA.MaterialMap.1024')),
    ],
'2d5b1412': [
        (log,                           ('2.5: Vivian Hair/GemA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2af66072', 'Vivian.Hair/GemA.MaterialMap.2048')),
    ],
'0635e2dd': [
        (log,                           ('2.5: Vivian BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da41fbd6', 'Vivian.BodyA.Diffuse.1024')),
    ],
'da41fbd6': [
        (log,                           ('2.5: Vivian BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0635e2dd', 'Vivian.BodyA.Diffuse.2048')),
    ],
'e21c3a6b': [
        (log,                           ('2.5: Vivian BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a86e169', 'Vivian.BodyA.LightMap.1024')),
    ],
'4a86e169': [
        (log,                           ('2.5: Vivian BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e21c3a6b', 'Vivian.BodyA.LightMap.2048')),
    ],
'81f7d37c': [
        (log,                           ('2.5: Vivian BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fa650e6c', 'Vivian.BodyA.MaterialMap.1024')),
    ],
'fa650e6c': [
        (log,                           ('2.5: Vivian BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('81f7d37c', 'Vivian.BodyA.MaterialMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Vivian',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
