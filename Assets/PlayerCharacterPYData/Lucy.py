"""
Lucy Character Hash Commands
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
    Returns Lucy's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'69ad9d08': [(log, ('2.5: Lucy Hair IB Hash',)),     (add_ib_check_if_missing,)],
'272dd7f6': [(log, ('2.5: Lucy Snout IB Hash',)),    (add_ib_check_if_missing,)],
'9b6370f6': [(log, ('2.5: Lucy Belt IB Hash',)),     (add_ib_check_if_missing,)],
'be5f4c7d': [(log, ('2.5: Lucy Body IB Hash',)),     (add_ib_check_if_missing,)],
'1fe6e084': [(log, ('2.5: Lucy RedCloth IB Hash',)), (add_ib_check_if_missing,)],
'a0ed04de': [(log, ('2.5: Lucy Helmet IB Hash',)),   (add_ib_check_if_missing,)],
'df3e3965': [(log, ('2.5: Lucy Head IB Hash',)),     (add_ib_check_if_missing,)],
'5315f036': [(log, ('1.2 -> 1.3: Lucy Hair Blend Hash',)),    (update_hash, ('a37c7537',))],
'751e21a5': [(log, ('1.2 -> 1.3: Lucy Hair Texcoord Hash',)), (update_hash, ('c8810832',))],
'198e99d7': [
        (log, ('1.2 -> 1.3: Lucy Hair IB Hash',)),
        (update_hash, ('69ad9d08',)),
        (transfer_indexed_sections, {
            'src_indices': ['0', '-1'],
            'trg_indices': ['0', '5253'],
        })
    ],
'5da9dafc': [(log, ('1.2 -> 1.3: Lucy Body Position Hash',)), (update_hash, ('246b93e2',))],
'b94b02e8': [(log, ('1.2 -> 1.3: Lucy Body Blend Hash',)),    (update_hash, ('66948a0f',))],
'00f11ea6': [(log, ('1.2 -> 1.3: Lucy Body Texcoord Hash',)), (update_hash, ('f60dbb9e',))],
'e0ad50ed': [(log, ('1.2 -> 1.3: Lucy Body IB Hash',)),       (update_hash, ('be5f4c7d',))],
'fca15ccb': [(log, ('1.2 -> 1.3: Lucy Head IB Hash',)),       (update_hash, ('df3e3965',))],
'483b418a': [(log, ('1.2 -> 1.3: Lucy HeadA Diffuse 1024p Hash',)), (update_hash, ('2578d35b',))],
'2a6df536': [(log, ('1.2 -> 1.3: Lucy HeadA Diffuse 1024p Hash',)), (update_hash, ('4e2d5baa',))],
'2578d35b': [
        (log,                           ('2.5: Lucy HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('df3e3965', 'fca15ccb'), 'Lucy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4e2d5baa', '2a6df536'), 'Lucy.HeadA.Diffuse.2048')),
    ],
'4e2d5baa': [
        (log,                           ('2.5: Lucy HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('df3e3965', 'fca15ccb'), 'Lucy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('2578d35b', '483b418a'), 'Lucy.HeadA.Diffuse.1024')),
    ],
'b50eb71c': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA Diffuse 1024p Hash',)),     (update_hash, ('753baa45',))],
'd1241cfc': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA MaterialMap 1024p Hash',)), (update_hash, ('368f931c',))],
'aa513afa': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA Diffuse 2048p Hash',)),     (update_hash, ('0fa60fe1',))],
'919b608c': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA MaterialMap 2048p Hash',)), (update_hash, ('068aba7f',))],
'0fa60fe1': [
        (log,                           ('2.5: Lucy HairA, SnoutA, BeltA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('753baa45', 'b50eb71c'), 'Lucy.HairA.Diffuse.1024')),
    ],
'753baa45': [
        (log,                           ('2.5: Lucy HairA, SnoutA, BeltA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('0fa60fe1', 'aa513afa'), 'Lucy.HairA.Diffuse.2048')),
    ],
'1a3b30ba': [
        (log,                           ('2.5: Lucy HairA, SnoutA, BeltA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('810c0878', 'Lucy.HairA.LightMap.1024')),
    ],
'810c0878': [
        (log,                           ('2.5: Lucy HairA, SnoutA, BeltA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('1a3b30ba', 'Lucy.HairA.LightMap.2048')),
    ],
'068aba7f': [
        (log,                           ('2.5: Lucy HairA, SnoutA, BeltA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   (('368f931c', 'd1241cfc'), 'Lucy.HairA.MaterialMap.1024')),
    ],
'368f931c': [
        (log,                           ('2.5: Lucy HairA, SnoutA, BeltA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   (('068aba7f', '919b608c'), 'Lucy.HairA.MaterialMap.2048')),
    ],
'edcb9661': [(log, ('1.0 -> 2.5: Lucy HairA, SnoutA, BeltA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'9114c7c7': [(log, ('1.0 -> 2.5: Lucy HairA, SnoutA, BeltA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],
'474c7aa2': [
        (log,                           ('2.5: Lucy BodyA, RedClothA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('f810e7ac', 'Lucy.BodyA.Diffuse.1024')),
    ],
'f810e7ac': [
        (log,                           ('2.5: Lucy BodyA, RedClothA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('474c7aa2', 'Lucy.BodyA.Diffuse.2048')),
    ],
'855d9fa3': [
        (log,                           ('2.5: Lucy BodyA, RedClothA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e89f7814', 'Lucy.BodyA.LightMap.1024')),
    ],
'e89f7814': [
        (log,                           ('2.5: Lucy BodyA, RedClothA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('855d9fa3', 'Lucy.BodyA.LightMap.2048')),
    ],
'1fd24fd8': [
        (log,                           ('2.5: Lucy BodyA, RedClothA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('86ca6cfd', 'Lucy.BodyA.MaterialMap.1024')),
    ],
'86ca6cfd': [
        (log,                           ('2.5: Lucy BodyA, RedClothA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('1fd24fd8', 'Lucy.BodyA.MaterialMap.2048')),
    ],
'463b4f55': [(log, ('1.0 -> 2.5: Lucy BodyA, RedClothA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'1711cafd': [(log, ('1.0 -> 2.5: Lucy BodyA, RedClothA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],
'a0be0ed3': [
        (log,                           ('2.5: Lucy HelmetA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('919ab7e5', 'Lucy.HelmetA.Diffuse.1024')),
    ],
'919ab7e5': [
        (log,                           ('2.5: Lucy HelmetA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a0be0ed3', 'Lucy.HelmetA.Diffuse.2048')),
    ],
'8d9a16c7': [
        (log,                           ('2.5: Lucy HelmetA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6a8fca92', 'Lucy.HelmetA.LightMap.1024')),
    ],
'6a8fca92': [
        (log,                           ('2.5: Lucy HelmetA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8d9a16c7', 'Lucy.HelmetA.LightMap.2048')),
    ],
'b3013a33': [(log, ('1.0 -> 2.5: Lucy HelmetA MaterialMap 2048p Hash',)), (update_hash, ('0a99d9d5',))],
'4227db77': [(log, ('1.0 -> 2.5: Lucy HelmetA MaterialMap 1024p Hash',)), (update_hash, ('0a99d9d5',))],
'ca5fd23a': [(log, ('1.0 -> 2.5: Lucy HelmetA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'f4d44970': [(log, ('1.0 -> 2.5: Lucy HelmetA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('2.5: Lucy Shared NormalMap Hash (All Components)',)),
        (multiply_section_if_missing,   (('edcb9661', '9114c7c7', '463b4f55', '1711cafd', 'ca5fd23a', 'f4d44970'), 'Lucy.Shared.NormalMap')),
    ],
'0a99d9d5': [
        (log,                           ('2.5: Lucy HelmetA MaterialMap Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4227db77', 'b3013a33'), 'Lucy.HelmetA.MaterialMap')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lucy',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
