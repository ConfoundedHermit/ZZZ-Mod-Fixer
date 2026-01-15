"""
Harumasa Character Hash Commands
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
    Returns Harumasa's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'f51a89c1': [(log, ('1.4 -> 1.5: Harumasa Hair IB Hash',)), (update_hash, ('6324de38',))],
'6324de38': [(log, ('1.5 -> 2.5: Harumasa Hair IB Hash',)), (add_ib_check_if_missing,)],

# Hair Buffer Hashes
'fa851c10': [(log, ('1.4 -> 1.5: Harumasa Hair Draw Hash',)),     (update_hash, ('9f75c05c',))],
'f5727f53': [(log, ('1.4 -> 1.5: Harumasa Hair Position Hash',)), (update_hash, ('eddb9012',))],
'52787e7d': [(log, ('1.4 -> 1.5: Harumasa Hair Blend Hash',)),    (update_hash, ('2644c499',))],
'9879fba3': [(log, ('1.4 -> 1.5: Harumasa Hair Texcoord Hash',)), (update_hash, ('4f45a9c5',))],

# Hair Textures
'b8f268ee': [
        (log,                           ('1.4 -> 2.5: Harumasa HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5700ced5', 'Harumasa.HairA.Diffuse.1024')),
    ],
'd4838b9d': [(log, ('1.4 -> 2.5: Harumasa HairA LightMap 2048p Hash',)), (update_hash, ('11041778',))],
'11041778': [
        (log,                           ('2.5: Harumasa HairA LightMap Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
    ],
'7217c146': [
        (log,                           ('1.4 -> 2.5: Harumasa HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c2c9ad2d', 'Harumasa.HairA.MaterialMap.1024')),
    ],
'5700ced5': [
        (log,                           ('1.4 -> 2.5: Harumasa HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b8f268ee', 'Harumasa.HairA.Diffuse.2048')),
    ],
'a1310b4f': [(log, ('1.4 -> 2.5: Harumasa HairA LightMap 1024p Hash',)), (update_hash, ('11041778',))],
'c2c9ad2d': [
        (log,                           ('1.4 -> 2.5: Harumasa HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7217c146', 'Harumasa.HairA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Harumasa Shared NormalMap Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
    ],

# === Legs Component ===
'aa7ba2dc': [(log, ('2.5: Harumasa Legs IB Hash',)), (add_ib_check_if_missing,)],

# Legs Textures
'44d74a1a': [
        (log,                           ('1.4 -> 2.5: Harumasa LegsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('897c74d5', 'Harumasa.LegsA.Diffuse.1024')),
    ],
'4b4d0ff6': [
        (log,                           ('1.4 -> 2.5: Harumasa LegsA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('822ec07f', 'Harumasa.LegsA.LightMap.1024')),
    ],
'ba8e396b': [(log, ('1.4 -> 2.5: Harumasa LegsA MaterialMap 2048p Hash',)), (update_hash, ('72885950',))],
'72885950': [
        (log,                           ('2.5: Harumasa LegsA MaterialMap Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
    ],
'897c74d5': [
        (log,                           ('1.4 -> 2.5: Harumasa LegsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('44d74a1a', 'Harumasa.LegsA.Diffuse.2048')),
    ],
'822ec07f': [
        (log,                           ('1.4 -> 2.5: Harumasa LegsA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4b4d0ff6', 'Harumasa.LegsA.LightMap.2048')),
    ],
'bdbf66a1': [(log, ('1.4 -> 2.5: Harumasa LegsA MaterialMap 1024p Hash',)), (update_hash, ('72885950',))],

# === Body Component ===
'78bea30d': [(log, ('1.4 -> 1.5: Harumasa Body IB Hash',)), (update_hash, ('79679a10',))],
'79679a10': [(log, ('1.5 -> 2.5: Harumasa Body IB Hash',)), (add_ib_check_if_missing,)],

# Body Buffer Hashes
'cafffd37': [(log, ('1.4 -> 1.5: Harumasa Body Draw Hash',)),     (update_hash, ('1fb92e46',))],
'3fa41462': [(log, ('1.4 -> 1.5: Harumasa Body Position Hash',)), (update_hash, ('0899751e',))],
'c0b32d17': [(log, ('1.4 -> 1.5: Harumasa Body Blend Hash',)),    (update_hash, ('347a0e9d',))],
'95ee1030': [(log, ('1.4 -> 1.5: Harumasa Body Texcoord Hash',)), (update_hash, ('e14fbc30',))],

# Body Textures
'ba52ac92': [(log, ('1.4 -> 1.5: Harumasa BodyA Diffuse 2048p Hash',)), (update_hash, ('49f8aaf6',))],
'49f8aaf6': [
        (log,                           ('1.5 -> 2.5: Harumasa BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('999ec526', 'e0b0c6eb'), 'Harumasa.BodyA.Diffuse.1024')),
    ],
'cc51476a': [
        (log,                           ('1.5 -> 2.5: Harumasa BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2b1230cf', 'Harumasa.BodyA.LightMap.1024')),
    ],
'cd1e0187': [(log, ('1.4 -> 1.5: Harumasa BodyA MaterialMap 2048p Hash',)), (update_hash, ('6d105f7e',))],
'6d105f7e': [
        (log,                           ('1.5 -> 2.5: Harumasa BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('c90264db', '2b0017d5'), 'Harumasa.BodyA.MaterialMap.1024')),
    ],
'e0b0c6eb': [(log, ('1.4 -> 1.5: Harumasa BodyA Diffuse 1024p Hash',)), (update_hash, ('999ec526',))],
'999ec526': [
        (log,                           ('1.5 -> 2.5: Harumasa BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('49f8aaf6', 'ba52ac92'), 'Harumasa.BodyA.Diffuse.2048')),
    ],
'2b1230cf': [
        (log,                           ('1.5 -> 2.5: Harumasa BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cc51476a', 'Harumasa.BodyA.LightMap.2048')),
    ],
'2b0017d5': [(log, ('1.4 -> 1.5: Harumasa BodyA MaterialMap 1024p Hash',)), (update_hash, ('c90264db',))],
'c90264db': [
        (log,                           ('1.5 -> 2.5: Harumasa BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('6d105f7e', 'cd1e0187'), 'Harumasa.BodyA.MaterialMap.2048')),
    ],

# === Face Component ===
'b0688334': [(log, ('2.5: Harumasa Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'4394c0b2': [
        (log,                           ('1.4 -> 2.5: Harumasa FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c5596262', 'Harumasa.FaceA.Diffuse.1024')),
    ],
'c5596262': [
        (log,                           ('1.4 -> 2.5: Harumasa FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4394c0b2', 'Harumasa.FaceA.Diffuse.2048')),
    ],

# === Player Component (NEW in 2.5) ===
'28ddcf0f': [(log, ('2.5: Harumasa Player IB Hash',)), (add_ib_check_if_missing,)],

# Player Textures
'81f189a2': [
        (log,                           ('2.5: Harumasa PlayerA Diffuse Hash',)),
        (add_section_if_missing,        ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n')),
    ],
'4302efb7': [
        (log,                           ('2.5: Harumasa PlayerA LightMap Hash',)),
        (add_section_if_missing,        ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n')),
    ],
'38b0417f': [
        (log,                           ('2.5: Harumasa PlayerA MaterialMap Hash',)),
        (add_section_if_missing,        ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Harumasa',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
