"""
Dialyn Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json data
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Dialyn's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hash Updates ===
'6ff0e4ad': [(log, ('2.5: 1 Dialyn Body blend',)), (update_hash, ('3d7e53cf',))],

# === IB Hashes ===
'68f00074': [(log, ('2.5: Dialyn Hair IB Hash',)), (add_ib_check_if_missing,)],
'af39a873': [(log, ('2.5: Dialyn Body IB Hash',)), (add_ib_check_if_missing,)],
'cd519abe': [(log, ('2.5: Dialyn PhoneCable IB Hash',)), (add_ib_check_if_missing,)],
'd860525e': [(log, ('2.5: Dialyn Brows IB Hash',)), (add_ib_check_if_missing,)],
'facb2461': [(log, ('2.5: Dialyn Face IB Hash',)), (add_ib_check_if_missing,)],

# === Hair Textures (shared with PhoneCable) ===
'4f8d9492': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA Diffuse Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.Diffuse', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA, BodyA NormalMap Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe', 'af39a873'), 'Dialyn.NormalMap', 'match_priority = 0\n')),
    ],
'a3f74f7d': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA LightMap Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.LightMap', 'match_priority = 0\n')),
    ],
'17aadaf6': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA MaterialMap Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.MaterialMap', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'52ea588e': [
        (log,                           ('2.5: Dialyn BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.Diffuse', 'match_priority = 0\n')),
    ],
'5cc175fe': [
        (log,                           ('2.5: Dialyn BodyA LightMap Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.LightMap', 'match_priority = 0\n')),
    ],
'28a10401': [
        (log,                           ('2.5: Dialyn BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.MaterialMap', 'match_priority = 0\n')),
    ],

# === Face/Brows Textures ===
'ad65abbf': [
        (log,                           ('2.5: Dialyn FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('facb2461', 'd860525e'), 'Dialyn.FaceA.Diffuse', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Dialyn',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'PhoneCable', 'Brows', 'Face'],
}
