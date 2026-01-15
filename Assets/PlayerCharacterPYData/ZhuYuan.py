"""
ZhuYuan Character Hash Commands
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
    Returns ZhuYuan's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'6619364f': [(log, ('1.1: ZhuYuan Body IB Hash',)),         (add_ib_check_if_missing,)],
'9821017e': [(log, ('1.0: ZhuYuan Hair IB Hash',)),         (add_ib_check_if_missing,)],
'fcac8411': [(log, ('1.0: ZhuYuan Extras IB Hash',)),       (add_ib_check_if_missing,)],
'5e717358': [(log, ('1.0: ZhuYuan ShoulderAmmo IB Hash',)), (add_ib_check_if_missing,)],
'a63028ae': [(log, ('1.0: ZhuYuan HipAmmo IB Hash',)),      (add_ib_check_if_missing,)],
'f1c241b7': [(log, ('1.0: ZhuYuan Head IB Hash',)),         (add_ib_check_if_missing,)],
'a4aeb1d5': [(log, ('1.0 -> 1.1: ZhuYuan Body IB Hash',)),  (update_hash, ('6619364f',))],
'5e942526': [(log, ('1.0 -> 1.1: ZhuYuan Body Blend Hash',)), (update_hash, ('01e0c8d9',))],
'f3569f8d': [(log, ('1.0 -> 1.1: ZhuYuan Body Position Hash',)), (update_hash, ('f595d24d',))],
'160872c0': [(log, ('1.0 -> 1.1: ZhuYuan Body Texcoord Hash',)), (update_hash, ('cb885260',))],
'fdc045fc': [
        (log, ('1.1 -> 1.2: ZhuYuan Hair Texcoord Hash',)),
        (update_hash, ('f3c092c5',)),
        (log, ('+ Reverting texcoord buffer remap',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'138c7d76': [
        (log,                           ('1.0: ZhuYuan HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f1c241b7', 'ZhuYuan.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a1eabb9f', 'ZhuYuan.HeadA.Diffuse.2048')),
    ],
'a1eabb9f': [
        (log,                           ('1.0: ZhuYuan HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f1c241b7', 'ZhuYuan.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('138c7d76', 'ZhuYuan.HeadA.Diffuse.1024')),
    ],
'9b86c2f6': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('7f823598', 'ZhuYuan.HairA.Diffuse.2048')),
    ],
'6eb346b9': [(log, ('1.0 -> 1.2: ZhuYuan HairA, ExtrasA NormalMap 1024p Hash',)),   (update_hash, ('ebac056e',))],
'8955095f': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d4ee59c7', 'ZhuYuan.HairA.LightMap.2048')),
    ],
'7d884663': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('12a407b1', 'ZhuYuan.HairA.MaterialMap.2048')),
    ],
'7f823598': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('9b86c2f6', 'ZhuYuan.HairA.Diffuse.1024')),
    ],
'4ac1defe': [(log, ('1.0 -> 1.2: ZhuYuan HairA, ExtrasA NormalMap 2048p Hash',)),   (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('1.2: ZhuYuan Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        (('9821017e', 'fcac8411', '5e717358', 'a63028ae', '6619364f'), 'ZhuYuan.Shared.NormalMap.2048', 'match_priority = 0\n')),
    ],
'd4ee59c7': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8955095f', 'ZhuYuan.HairA.LightMap.1024')),
    ],
'12a407b1': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7d884663', 'ZhuYuan.HairA.MaterialMap.1024')),
    ],
'b57a8744': [(log, ('1.0 -> 1.1: ZhuYuan BodyA Diffuse 1024p Hash',)),     (update_hash, ('f6795718',))],
'833bafd5': [(log, ('1.0 -> 1.1: ZhuYuan BodyA NormalMap 1024p Hash',)),   (update_hash, ('729ea75a',))],
'18d00ac6': [(log, ('1.0 -> 1.1: ZhuYuan BodyA LightMap 1024p Hash',)),    (update_hash, ('14b638b6',))],
'1daa379f': [(log, ('1.0 -> 1.1: ZhuYuan BodyA MaterialMap 1024p Hash',)), (update_hash, ('cd4dee2c',))],
'f6795718': [(log, ('1.1 -> 1.2: ZhuYuan BodyA Diffuse 1024p Hash',)),     (update_hash, ('46af14f8',))],
'729ea75a': [(log, ('1.1 -> 1.2: ZhuYuan BodyA NormalMap 1024p Hash',)),   (update_hash, ('d5b175bf',))],
'14b638b6': [(log, ('1.1 -> 1.2: ZhuYuan BodyA LightMap 1024p Hash',)),    (update_hash, ('fb385169',))],
'cd4dee2c': [(log, ('1.1 -> 1.2: ZhuYuan BodyA MaterialMap 1024p Hash',)), (update_hash, ('29e2ebc5',))],
'46af14f8': [
        (log,                           ('1.2: ZhuYuan BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('a271e894', '3ef82f41', 'c88e7660'), 'ZhuYuan.BodyA.Diffuse.2048')),
    ],
'd5b175bf': [(log, ('1.2 -> 2.5: ZhuYuan BodyA NormalMap 1024p Hash',)),   (update_hash, ('ebac056e',))],
'fb385169': [
        (log,                           ('1.2: ZhuYuan BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d02bc66c', '80ebf536', '13a38449'), 'ZhuYuan.BodyA.LightMap.2048')),
    ],
'29e2ebc5': [
        (log,                           ('1.2: ZhuYuan BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3e808ef6', '10415de8', 'b4e20235'), 'ZhuYuan.BodyA.MaterialMap.2048')),
    ],
'c88e7660': [(log, ('1.0 -> 1.1: ZhuYuan BodyA Diffuse 2048p Hash',)),     (update_hash, ('3ef82f41',))],
'a396c53a': [(log, ('1.0 -> 1.1: ZhuYuan BodyA NormalMap 2048p Hash',)),   (update_hash, ('7195a311',))],
'13a38449': [(log, ('1.0 -> 1.1: ZhuYuan BodyA LightMap 2048p Hash',)),    (update_hash, ('80ebf536',))],
'b4e20235': [(log, ('1.0 -> 1.1: ZhuYuan BodyA MaterialMap 2048p Hash',)), (update_hash, ('10415de8',))],
'3ef82f41': [(log, ('1.1 -> 1.2: ZhuYuan BodyA Diffuse 2048p Hash',)),     (update_hash, ('a271e894',))],
'7195a311': [(log, ('1.1 -> 1.2: ZhuYuan BodyA NormalMap 2048p Hash',)),   (update_hash, ('d81fb56e',))],
'80ebf536': [(log, ('1.1 -> 1.2: ZhuYuan BodyA LightMap 2048p Hash',)),    (update_hash, ('d02bc66c',))],
'10415de8': [(log, ('1.1 -> 1.2: ZhuYuan BodyA MaterialMap 2048p Hash',)), (update_hash, ('3e808ef6',))],
'a271e894': [
        (log,                           ('1.2: ZhuYuan BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('46af14f8', 'f6795718', 'b57a8744'), 'ZhuYuan.BodyA.Diffuse.1024')),
    ],
'd81fb56e': [(log, ('1.2 -> 2.5: ZhuYuan BodyA NormalMap 2048p Hash',)),   (update_hash, ('ebac056e',))],
'd02bc66c': [
        (log,                           ('1.2: ZhuYuan BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('fb385169', '14b638b6', '18d00ac6'), 'ZhuYuan.BodyA.LightMap.1024')),
    ],
'3e808ef6': [
        (log,                           ('1.2: ZhuYuan BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('29e2ebc5', 'cd4dee2c', '1daa379f'), 'ZhuYuan.BodyA.MaterialMap.1024')),
    ],
'222ae5ee': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('6a33b25e', 'ZhuYuan.ExtrasB.Diffuse.2048')),
    ],
'0fda74c3': [(log, ('1.0 -> 1.2: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA NormalMap 1024p Hash',)),   (update_hash, ('ebac056e',))],
'790183b4': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e30f025b', 'ZhuYuan.ExtrasB.LightMap.2048')),
    ],
'84842409': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('58d5c840', 'ZhuYuan.ExtrasB.MaterialMap.2048')),
    ],
'6a33b25e': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('222ae5ee', 'ZhuYuan.ExtrasB.Diffuse.1024')),
    ],
'fb35b7e9': [(log, ('1.0 -> 1.2: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA NormalMap 2048p Hash',)),   (update_hash, ('ebac056e',))],
'e30f025b': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('790183b4', 'ZhuYuan.ExtrasB.LightMap.1024')),
    ],
'58d5c840': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('84842409', 'ZhuYuan.ExtrasB.MaterialMap.1024')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ZhuYuan',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
