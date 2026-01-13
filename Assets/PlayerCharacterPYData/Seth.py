"""
Seth Character Hash Commands
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
    Returns Seth's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'35cf83ad': [(log, ('1.1: Seth Hair IB Hash',)), (add_ib_check_if_missing,)],
'00172ec3': [(log, ('1.1: Seth Body IB Hash',)), (add_ib_check_if_missing,)],
'52f5aa74': [(log, ('1.1: Seth Head IB Hash',)), (add_ib_check_if_missing,)],
'a72f760f': [
        (log,            ('1.3 -> 1.4: Seth Hair Texcoord Hash',)),
        (update_hash,    ('a91eeef2',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '14_Seth_Hair',
            ('4f','2e','2f','2e'),
            ('4B','2e','2f','2e')
        )),
    ],
'fe5b7534': [
        (log,                           ('1.1: Seth HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('09981aff', 'Seth.HeadA.Diffuse.2048')),
    ],
'09981aff': [
        (log,                           ('1.1: Seth HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fe5b7534', 'Seth.HeadA.Diffuse.1024')),
    ],
'dc8e244d': [
        (log,                           ('1.1: Seth HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d3756c37', 'Seth.HairA.Diffuse.1024')),
    ],
'd3756c37': [
        (log,                           ('1.1: Seth HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc8e244d', 'Seth.HairA.Diffuse.2048')),
    ],
'd4de9ec1': [
        (log,                           ('1.1 -> 2.5: Seth HairA LightMap 2048p Hash',)),
        (update_hash,                   ('a855884d',)),
    ],
'c01dbf6c': [
        (log,                           ('1.1 -> 2.5: Seth HairA LightMap 1024p Hash',)),
        (update_hash,                   ('a855884d',)),
    ],
'3c256565': [
        (log,                           ('1.1: Seth HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('833e9405', 'Seth.HairA.MaterialMap.1024')),
    ],
'833e9405': [
        (log,                           ('1.1: Seth HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3c256565', 'Seth.HairA.MaterialMap.2048')),
    ],
'3376b58c': [
        (log,                           ('1.1 -> 2.5: Seth HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'24d52dd8': [
        (log,                           ('1.1 -> 2.5: Seth HairA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'7f8416ab': [
        (log,                           ('1.1: Seth BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dbc90150', 'Seth.BodyA.Diffuse.1024')),
    ],
'dbc90150': [
        (log,                           ('1.1: Seth BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7f8416ab', 'Seth.BodyA.Diffuse.2048')),
    ],
'3d97c2ef': [
        (log,                           ('1.1 -> 2.5: Seth BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('5b205468',)),
    ],
'9436aa83': [
        (log,                           ('1.1 -> 2.5: Seth BodyA LightMap 1024p Hash',)),
        (update_hash,                   ('5b205468',)),
    ],
'732d3f81': [
        (log,                           ('1.1: Seth BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('56775fcb', 'Seth.BodyA.MaterialMap.1024')),
    ],
'56775fcb': [
        (log,                           ('1.1: Seth BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('732d3f81', 'Seth.BodyA.MaterialMap.2048')),
    ],
'dde45d3d': [
        (log,                           ('1.1 -> 2.5: Seth BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'62b047c5': [
        (log,                           ('1.1 -> 2.5: Seth BodyA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Seth Shared NormalMap Hash (Hair & Body)',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'a855884d': [
        (log,                           ('2.5: Seth HairA LightMap Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'5b205468': [
        (log,                           ('2.5: Seth BodyA LightMap Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seth',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
