"""
Belle Character Hash Commands
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
    Returns Belle's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'bea4a483': [(log, ('1.0: Belle Hair IB Hash',)), (add_ib_check_if_missing,)],
'1817f3ca': [(log, ('1.0: Belle Body IB Hash',)), (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('1.0: Belle Head IB Hash',)), (add_ib_check_if_missing,)],
'caf95576': [
        (log,                         ('1.0 -> 1.1: Belle Body Texcoord Hash',)),
        (update_hash,                 ('801edbf4',)),
        (log,                         ('1.0 -> 1.1: Belle Body Blend Remap',)),
        (update_buffer_blend_indices, (
            'd2844c01',
            (3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 126, 127),
            (6, 7, 3, 5, 4, 18, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 25, 24, 20, 22, 23, 38, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 47, 48, 53, 56, 45, 46, 49, 50, 51, 52, 54, 55, 60, 61, 66, 58, 59, 62, 63, 64, 65, 104, 95, 96, 97, 98, 99, 100, 101, 102, 103, 127, 126),
        ))
    ],
'77eef7e8': [
        (log,                           ('1.0: Belle HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'Belle.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('75ec3614', 'Belle.HeadA.Diffuse.2048')),
    ],
'75ec3614': [
        (log,                           ('1.0: Belle HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'Belle.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('77eef7e8', 'Belle.HeadA.Diffuse.1024')),
    ],
'1ce58567': [
        (log,                           ('1.0: Belle HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('08f04d95', 'Belle.HairA.Diffuse.1024')),
    ],
'08f04d95': [
        (log,                           ('1.0: Belle HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1ce58567', 'Belle.HairA.Diffuse.2048')),
    ],
'f1ee2105': [(log, ('1.0 -> 2.5: Belle HairA LightMap 2048p Hash',)), (update_hash, ('7d562f53',))],
'7d562f53': [
        (log,                           ('2.5: Belle HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2e656f2f', 'Belle.HairA.LightMap.1024')),
    ],
'2e656f2f': [
        (log,                           ('1.0: Belle HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7d562f53', 'f1ee2105'), 'Belle.HairA.LightMap.2048')),
    ],
'24c47ca5': [(log, ('1.4 -> 1.5: Belle HairA MaterialMap 2048p Hash',)), (update_hash, ('34bdb036',))],
'34bdb036': [
        (log,                           ('1.5: Belle HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7542ef4b', '4b6ef993'), 'Belle.HairA.MaterialMap.1024')),
    ],
'4b6ef993': [(log, ('1.4 -> 1.5: Belle HairA MaterialMap 1024p Hash',)), (update_hash, ('7542ef4b',))],
'7542ef4b': [
        (log,                           ('1.5: Belle HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('34bdb036', '24c47ca5'), 'Belle.HairA.MaterialMap.2048')),
    ],
'89b147ff': [(log, ('1.0 -> 2.5: Belle HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('2.5: Belle Hair+Body NormalMap 2048p Hash (Shared)',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('6b55c039', 'c0bd8516'), 'Belle.HairBody.NormalMap.1024')),
    ],
'6b55c039': [
        (log,                           ('1.0: Belle HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '89b147ff'), 'Belle.HairA.NormalMap.2048')),
    ],
'd2960560': [(log, ('1.4 -> 1.5: Belle BodyA Diffuse 2048p Hash',)), (update_hash, ('24639b77',))],
'24639b77': [
        (log,                           ('1.5: Belle BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('b9c7f71b', '4454fb58'), 'Belle.BodyA.Diffuse.1024')),
    ],
'4454fb58': [(log, ('1.4 -> 1.5: Belle BodyA Diffuse 1024p Hash',)), (update_hash, ('b9c7f71b',))],
'b9c7f71b': [
        (log,                           ('1.5: Belle BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('24639b77', 'd2960560'), 'Belle.BodyA.Diffuse.2048')),
    ],
'bf286c84': [(log, ('1.4 -> 1.5: Belle BodyA LightMap 2048p Hash',)), (update_hash, ('7947679c',))],
'7947679c': [
        (log,                           ('1.5: Belle BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('a4d3687d', '2ed82c57'), 'Belle.BodyA.LightMap.1024')),
    ],
'2ed82c57': [(log, ('1.4 -> 1.5: Belle BodyA LightMap 1024p Hash',)), (update_hash, ('a4d3687d',))],
'a4d3687d': [
        (log,                           ('1.5: Belle BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7947679c', 'bf286c84'), 'Belle.BodyA.LightMap.2048')),
    ],
'33f28c6d': [
        (log,                           ('1.0: Belle BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b1abe877', 'Belle.BodyA.MaterialMap.1024')),
    ],
'b1abe877': [
        (log,                           ('1.0: Belle BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('33f28c6d', 'Belle.BodyA.MaterialMap.2048')),
    ],
'f04f7ab9': [(log, ('1.0 -> 2.5: Belle BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'c0bd8516': [
        (log,                           ('1.0: Belle BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', 'f04f7ab9'), 'Belle.BodyA.NormalMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Belle',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
