"""
Soukaku Character Hash Commands
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
    Returns Soukaku's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'fe70c7a3': [(log, ('1.0 - 2.5: Soukaku Hair IB Hash',)), (add_ib_check_if_missing,)],
'ced49ff8': [(log, ('1.0 - 2.5: Soukaku Body IB Hash',)), (add_ib_check_if_missing,)],
'1315178e': [(log, ('1.1 - 2.5: Soukaku Mask IB Hash',)), (add_ib_check_if_missing,)],
'020f9ac6': [(log, ('1.1 - 2.5: Soukaku Head/Face IB Hash',)), (add_ib_check_if_missing,)],
'01f7369e': [(log, ('1.0 - 1.1: Soukaku Head IB Hash',)), (update_hash, ('020f9ac6',))],
'2ceacde6': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA Diffuse 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('427b39a4', 'Soukaku.HeadA.Diffuse.2048')),
    ],
'c20a8c82': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA LightMap 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('17110d01', 'Soukaku.HeadA.Diffuse.2048')),
    ],
'427b39a4': [
        (log,                           ('1.0 - 2.5: Soukaku HeadA/FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2ceacde6', 'Soukaku.HeadA.Diffuse.1024')),
    ],
'17110d01': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA LightMap 2048p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c20a8c82', 'Soukaku.HeadA.Diffuse.1024')),
    ],
'32ea0d00': [
        (log,                           ('1.0 - 2.5: Soukaku HairA/MaskA Diffuse 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('34a3ff5b', 'Soukaku.HairA.Diffuse.1024')),
    ],
'34a3ff5b': [
        (log,                           ('1.0: Soukaku HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('32ea0d00', 'Soukaku.HairA.Diffuse.2048')),
    ],
'04654e94': [(log, ('1.0 - 1.7: Soukaku HairA LightMap 2048p Hash',)), (update_hash, ('a70e24a2',))],
'7bbb3d02': [(log, ('1.0 - 1.7: Soukaku HairA LightMap 1024p Hash (deprecated)',))],
'a70e24a2': [
        (log,                           ('2.5: Soukaku HairA/MaskA LightMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'd1444c52': [
        (log,                           ('1.0 - 2.5: Soukaku HairA/MaskA MaterialMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('218689cf', 'Soukaku.HairA.MaterialMap.1024')),
    ],
'218689cf': [
        (log,                           ('1.0: Soukaku HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d1444c52', 'Soukaku.HairA.MaterialMap.2048')),
    ],
'8498ee4d': [(log, ('1.0 - 1.7: Soukaku HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'0003126a': [(log, ('1.0 - 1.7: Soukaku HairA NormalMap 1024p Hash (deprecated)',))],
'ebac056e': [
        (log,                           ('2.5: Soukaku HairA/BodyA NormalMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
'ee31954b': [
        (log,                           ('1.0 - 2.5: Soukaku BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6f5d31fc', 'Soukaku.BodyA.Diffuse.1024')),
    ],
'6f5d31fc': [
        (log,                           ('1.0 - 1.7: Soukaku BodyA Diffuse 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ee31954b', 'Soukaku.BodyA.Diffuse.2048')),
    ],
'112a36a4': [
        (log,                           ('1.0 - 2.5: Soukaku BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c0f0bb74', 'Soukaku.BodyA.LightMap.1024')),
    ],
'c0f0bb74': [
        (log,                           ('1.0 - 1.7: Soukaku BodyA LightMap 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('112a36a4', 'Soukaku.BodyA.LightMap.2048')),
    ],
'd638ddf9': [
        (log,                           ('1.0 - 2.5: Soukaku BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1ec28297', 'Soukaku.BodyA.MaterialMap.1024')),
    ],
'1ec28297': [
        (log,                           ('1.0 - 1.7: Soukaku BodyA MaterialMap 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d638ddf9', 'Soukaku.BodyA.MaterialMap.2048')),
    ],
'363e3d70': [(log, ('1.0 - 1.7: Soukaku BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'77c48d32': [(log, ('1.0 - 1.7: Soukaku BodyA NormalMap 1024p Hash (deprecated)',))]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soukaku',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
