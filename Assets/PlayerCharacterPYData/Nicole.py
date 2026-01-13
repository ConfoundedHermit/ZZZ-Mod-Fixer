"""
Nicole Character Hash Commands
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
    Returns Nicole's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'6847bbbd': [(log, ('1.0-2.5: Nicole Hair IB Hash',)),    (add_ib_check_if_missing,)],
'5a4c1ef3': [(log, ('1.0-2.5: Nicole Body IB Hash',)),    (add_ib_check_if_missing,)],
'7435fc0e': [(log, ('1.0-2.5: Nicole Head IB Hash',)),    (add_ib_check_if_missing,)],
'6abd3dd3': [
        (log,                           ('1.0-1.7: Nicole HeadA Diffuse 1024p Hash (Removed in 2.5)',)),
    ],
'd1e84a34': [
        (log,                           ('1.0-2.5: Nicole HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7435fc0e', 'Nicole.Head.IB', 'match_priority = 0\n')),
    ],
'6d3868f9': [
        (log,                           ('1.0-2.5: Nicole HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'7a45adcd': [
        (log,                           ('1.0-1.7: Nicole HairA Diffuse 1024p Hash (Removed in 2.5)',)),
    ],
'1dfd9e16': [
        (log,                           ('1.0-1.7: Nicole HairA LightMap 2048p Hash',)),
        (update_hash,                   ('8c9c25d5',)),
    ],
'9adc04ed': [
        (log,                           ('1.0-1.7: Nicole HairA LightMap 1024p Hash (Removed in 2.5)',)),
    ],
'8c9c25d5': [
        (log,                           ('2.5: Nicole HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'a05c2386': [
        (log,                           ('2.5: Nicole HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'bffb4a66': [
        (log,                           ('1.0-1.7: Nicole HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'b8db0209': [
        (log,                           ('1.0-1.7: Nicole HairA NormalMap 1024p Hash (Removed in 2.5)',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Nicole HairA, BodyA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
'f86ffe2c': [
        (log,                           ('1.0-2.5: Nicole BodyA, AmillionA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'9ee9b402': [
        (log,                           ('1.0-1.7: Nicole BodyA, AmillionA Diffuse 1024p Hash (Removed in 2.5)',)),
    ],
'80855e0f': [
        (log,                           ('1.0-2.5: Nicole BodyA, AmillionA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'2b5aa784': [
        (log,                           ('1.0-1.7: Nicole BodyA, AmillionA LightMap 1024p Hash (Removed in 2.5)',)),
    ],
'95cabef3': [
        (log,                           ('1.0-2.5: Nicole BodyA, AmillionA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'bb33129d': [
        (log,                           ('1.0-1.7: Nicole BodyA, AmillionA MaterialMap 1024p Hash (Removed in 2.5)',)),
    ],
'8cf23419': [
        (log,                           ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'580df52d': [
        (log,                           ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 1024p Hash (Removed in 2.5)',)),
    ],
'40e64ae2': [(log, ('2.5: Nicole Amillion IB Hash',)),    (add_ib_check_if_missing,)]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Nicole',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
