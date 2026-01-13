"""
Anton Character Hash Commands
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
    Returns Anton's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'6b95c80d': [(log, ('1.0: Anton Hair IB Hash',)),   (add_ib_check_if_missing,)],
'653fb27c': [(log, ('1.0: Anton Body IB Hash',)),   (add_ib_check_if_missing,)],
'a21fcee4': [(log, ('1.0: Anton Jacket IB Hash',)), (add_ib_check_if_missing,)],
'a0201907': [(log, ('1.0: Anton Head IB Hash',)),   (add_ib_check_if_missing,)],
'15cb1aee': [
        (log,                           ('1.0: Anton HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('842119d6', 'Anton.HeadA.Diffuse.2048')),
    ],
'654134c1': [
        (log,                           ('1.0: Anton HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ac7fb2e2', 'Anton.HeadA.LightMap.2048')),
    ],
'842119d6': [
        (log,                           ('1.0: Anton HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('15cb1aee', 'Anton.HeadA.Diffuse.1024')),
    ],
'ac7fb2e2': [
        (log,                           ('1.0: Anton HeadA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('654134c1', 'Anton.HeadA.LightMap.1024')),
    ],
'571aa398': [
        (log,                           ('1.0: Anton HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d4c4c604', 'Anton.HairA.Diffuse.1024')),
    ],
'd4c4c604': [
        (log,                           ('1.0: Anton HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('571aa398', 'Anton.HairA.Diffuse.2048')),
    ],
'ee06579e': [
        (log,                           ('1.0→2.5: Anton HairA LightMap 2048p Hash',)),
        (update_hash,                   ('41601dfa',)),
    ],
'21ee9a3f': [
        (log,                           ('1.0→2.5: Anton HairA LightMap 1024p Hash',)),
        (update_hash,                   ('41601dfa',)),
    ],
'41601dfa': [
        (log,                           ('2.5: Anton HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'24caeb1f': [
        (log,                           ('1.0→2.5: Anton HairA MaterialMap 2048p Hash',)),
        (update_hash,                   ('d47c5823',)),
    ],
'6fc654e1': [
        (log,                           ('1.0→2.5: Anton HairA MaterialMap 1024p Hash',)),
        (update_hash,                   ('d47c5823',)),
    ],
'd47c5823': [
        (log,                           ('2.5: Anton HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'b216f758': [
        (log,                           ('1.0→2.5: Anton HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'77ae203f': [
        (log,                           ('1.0→2.5: Anton HairA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Anton Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'00abcf22': [
        (log,                           ('1.0: Anton BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('581a0958', 'Anton.BodyA.Diffuse.1024')),
    ],
'581a0958': [
        (log,                           ('1.0: Anton BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('00abcf22', 'Anton.BodyA.Diffuse.2048')),
    ],
'17cf1b74': [
        (log,                           ('1.0→2.5: Anton BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('ed6f4199',)),
    ],
'8e5ba7d0': [
        (log,                           ('1.0→2.5: Anton BodyA LightMap 1024p Hash',)),
        (update_hash,                   ('ed6f4199',)),
    ],
'ed6f4199': [
        (log,                           ('2.5: Anton BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'0238b0ff': [
        (log,                           ('1.0→2.5: Anton BodyA MaterialMap 2048p Hash',)),
        (update_hash,                   ('986c9716',)),
    ],
'b7ce5f0b': [
        (log,                           ('1.0→2.5: Anton BodyA MaterialMap 1024p Hash',)),
        (update_hash,                   ('986c9716',)),
    ],
'986c9716': [
        (log,                           ('2.5: Anton BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'1b4ad5b7': [
        (log,                           ('1.0→2.5: Anton BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'5b2ab0e0': [
        (log,                           ('1.0→2.5: Anton BodyA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'd4b15508': [
        (log,                           ('1.0: Anton JacketA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f7831517', 'Anton.JacketA.Diffuse.1024')),
    ],
'f7831517': [
        (log,                           ('1.0: Anton JacketA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d4b15508', 'Anton.JacketA.Diffuse.2048')),
    ],
'886a664a': [
        (log,                           ('1.0→2.5: Anton JacketA LightMap 2048p Hash',)),
        (update_hash,                   ('ef7880e3',)),
    ],
'c42628a5': [
        (log,                           ('1.0→2.5: Anton JacketA LightMap 1024p Hash',)),
        (update_hash,                   ('ef7880e3',)),
    ],
'ef7880e3': [
        (log,                           ('2.5: Anton JacketA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'd36a2f7a': [
        (log,                           ('1.0: Anton JacketA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('75bccc40', 'Anton.JacketA.MaterialMap.1024')),
    ],
'75bccc40': [
        (log,                           ('1.0: Anton JacketA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d36a2f7a', 'Anton.JacketA.MaterialMap.2048')),
    ],
'd7517d0e': [
        (log,                           ('1.0→2.5: Anton JacketA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ae3d5fb8': [
        (log,                           ('1.0→2.5: Anton JacketA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Anton',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
