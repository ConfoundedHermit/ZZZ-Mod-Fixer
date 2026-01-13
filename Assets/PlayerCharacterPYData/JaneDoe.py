"""
JaneDoe Character Hash Commands
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
    Returns JaneDoe's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ===== IB Hashes (Current v2.5) =====
'9268a5af': [(log, ('2.5: Jane Hair IB Hash',)), (add_ib_check_if_missing,)],
'ba4255a5': [(log, ('2.5: Jane Body IB Hash',)), (add_ib_check_if_missing,)],
'ef86fc9f': [(log, ('2.5: Jane Head/Face IB Hash',)), (add_ib_check_if_missing,)],

# ===== Buffer Hashes (Current v2.5) =====
'2d06e785': [(log, ('2.5: Jane Hair Draw Hash',))],
'e7a3b7dc': [(log, ('2.5: Jane Hair Position Hash',))],
'8721477f': [(log, ('2.5: Jane Hair Blend Hash',))],
'acec29f8': [(log, ('2.5: Jane Hair Texcoord Hash',))],
'0e1c6740': [(log, ('2.5: Jane Body Draw Hash',))],
'10050266': [(log, ('2.5: Jane Body Position Hash',))],
'e27f398e': [(log, ('2.5: Jane Body Blend Hash',))],
'949549de': [(log, ('2.5: Jane Body Texcoord Hash',))],

# ===== Version Update Paths =====
'c8ad344e': [
        (log, ('1.1 -> 1.2: Jane Hair Texcoord Hash',)),
        (update_hash, ('257a90d6',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'5721e4e7': [(log, ('1.3 -> 1.4: Jane Hair Draw Hash',)),     (update_hash, ('2d06e785',)),],
'24323bf9': [(log, ('1.3 -> 1.4: Jane Hair Position Hash',)), (update_hash, ('e7a3b7dc',)),],
'0a10c747': [(log, ('1.3 -> 1.4: Jane Hair Blend Hash',)),    (update_hash, ('8721477f',)),],
'257a90d6': [(log, ('1.3 -> 1.4: Jane Hair Texcoord Hash',)), (update_hash, ('acec29f8',)),],
'7b16a708': [(log, ('1.3 -> 1.4: Jane Hair IB Hash',)),       (update_hash, ('9268a5af',)),],
'd1aa4b85': [(log, ('1.3 -> 1.4: Jane Body Draw Hash',)),     (update_hash, ('0e1c6740',)),],
'06f9bc49': [(log, ('1.3 -> 1.4: Jane Body Position Hash',)), (update_hash, ('10050266',)),],
'9727a184': [(log, ('1.3 -> 1.4: Jane Body Blend Hash',)),    (update_hash, ('e27f398e',)),],
'8b85c03e': [(log, ('1.3 -> 1.4: Jane Body Texcoord Hash',)), (update_hash, ('949549de',)),],
'e2c0144e': [(log, ('1.3 -> 1.4: Jane Body IB Hash',)),       (update_hash, ('ba4255a5',)),],
'689639a5': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 1024p Hash',)), (update_hash, ('d823ac80',)),],
'd823ac80': [
        (log,                           ('1.1: Jane HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3b75aa2c', '8974fb74'), 'Jane.HeadA.Diffuse.2048')),
    ],
'8974fb74': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 2048p Hash',)), (update_hash, ('3b75aa2c',)),],

# ===== Texture Hashes (Current v2.5) =====
'3b75aa2c': [
        (log,                           ('2.5: Jane HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d823ac80', '689639a5'), 'Jane.HeadA.Diffuse.1024')),
    ],
'd823ac80': [
        (log,                           ('2.5: Jane HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3b75aa2c', '8974fb74'), 'Jane.HeadA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Jane Shared NormalMap Hash',)),
        (add_section_if_missing,        ('9268a5af', 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n')),
    ],
'f7ef1a53': [
        (log,                           ('2.5: Jane HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b33a9770', 'Jane.HairA.Diffuse.1024')),
    ],
'b33a9770': [
        (log,                           ('2.5: Jane HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f7ef1a53', 'Jane.HairA.Diffuse.2048')),
    ],
'9ec4cd4f': [
        (log,                           ('2.5: Jane HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5e12acc1', 'Jane.HairA.LightMap.1024')),
    ],
'5e12acc1': [
        (log,                           ('2.5: Jane HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9ec4cd4f', 'Jane.HairA.LightMap.2048')),
    ],
'5e34e275': [
        (log,                           ('2.5: Jane HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('40fca454', 'Jane.HairA.MaterialMap.1024')),
    ],
'40fca454': [
        (log,                           ('2.5: Jane HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5e34e275', 'Jane.HairA.MaterialMap.2048')),
    ],
'd1f56c7d': [
        (log,                           ('2.5: Jane BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e62ae3b5', 'Jane.BodyA.Diffuse.1024')),
    ],
'e62ae3b5': [
        (log,                           ('2.5: Jane BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d1f56c7d', 'Jane.BodyA.Diffuse.2048')),
    ],
'3087f82a': [
        (log,                           ('2.5: Jane BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('52fa9861', 'Jane.BodyA.LightMap.1024')),
    ],
'52fa9861': [
        (log,                           ('2.5: Jane BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3087f82a', 'Jane.BodyA.LightMap.2048')),
    ],
'99eae42e': [
        (log,                           ('2.5: Jane BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5dce2408', 'Jane.BodyA.MaterialMap.1024')),
    ],
'5dce2408': [
        (log,                           ('2.5: Jane BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('99eae42e', 'Jane.BodyA.MaterialMap.2048')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoe',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
