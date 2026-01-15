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

# === VB Hashes ===
# Hair VBs
'00e453e9': [(log, ('2.5: Dialyn Hair draw VB Hash',)), (add_section_if_missing, ('68f00074', 'Dialyn.Hair.DrawVB', 'match_priority = 0\n'))],
'a486f1bb': [(log, ('2.5: Dialyn Hair position VB Hash',)), (add_section_if_missing, ('68f00074', 'Dialyn.Hair.PositionVB', 'match_priority = 0\n'))],
'339f41eb': [(log, ('2.5: Dialyn Hair blend VB Hash',)), (add_section_if_missing, ('68f00074', 'Dialyn.Hair.BlendVB', 'match_priority = 0\n'))],
'46019c5e': [(log, ('2.5: Dialyn Hair texcoord VB Hash',)), (add_section_if_missing, ('68f00074', 'Dialyn.Hair.TexcoordVB', 'match_priority = 0\n'))],

# Body VBs
'2e77bd1d': [(log, ('2.5: Dialyn Body draw VB Hash',)), (add_section_if_missing, ('af39a873', 'Dialyn.Body.DrawVB', 'match_priority = 0\n'))],
'ff36809b': [(log, ('2.5: Dialyn Body position VB Hash',)), (add_section_if_missing, ('af39a873', 'Dialyn.Body.PositionVB', 'match_priority = 0\n'))],
'3d7e53cf': [(log, ('2.5: Dialyn Body blend VB Hash',)), (add_section_if_missing, ('af39a873', 'Dialyn.Body.BlendVB', 'match_priority = 0\n'))],
'3f2079bc': [(log, ('2.5: Dialyn Body texcoord VB Hash',)), (add_section_if_missing, ('af39a873', 'Dialyn.Body.TexcoordVB', 'match_priority = 0\n'))],

# PhoneCable VBs
'38ce65ff': [(log, ('2.5: Dialyn PhoneCable draw VB Hash',)), (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.DrawVB', 'match_priority = 0\n'))],
'd0470351': [(log, ('2.5: Dialyn PhoneCable position VB Hash',)), (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.PositionVB', 'match_priority = 0\n'))],
'312b6e12': [(log, ('2.5: Dialyn PhoneCable blend VB Hash',)), (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.BlendVB', 'match_priority = 0\n'))],
'2e6484db': [(log, ('2.5: Dialyn PhoneCable texcoord VB Hash',)), (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.TexcoordVB', 'match_priority = 0\n'))],

# Face VBs
'fe5fb676': [(log, ('2.5: Dialyn Face draw VB Hash',)), (add_section_if_missing, ('facb2461', 'Dialyn.Face.DrawVB', 'match_priority = 0\n'))],
'c44d2531': [(log, ('2.5: Dialyn Face position VB Hash',)), (add_section_if_missing, ('facb2461', 'Dialyn.Face.PositionVB', 'match_priority = 0\n'))],
'08923d3e': [(log, ('2.5: Dialyn Face blend VB Hash',)), (add_section_if_missing, ('facb2461', 'Dialyn.Face.BlendVB', 'match_priority = 0\n'))],
'f6c5296e': [(log, ('2.5: Dialyn Face texcoord VB Hash',)), (add_section_if_missing, ('facb2461', 'Dialyn.Face.TexcoordVB', 'match_priority = 0\n'))],

# Brows VBs
'fecc9606': [(log, ('2.5: Dialyn Brows draw VB Hash',)), (add_section_if_missing, ('d860525e', 'Dialyn.Brows.DrawVB', 'match_priority = 0\n'))],
'c4de0541': [(log, ('2.5: Dialyn Brows position VB Hash',)), (add_section_if_missing, ('d860525e', 'Dialyn.Brows.PositionVB', 'match_priority = 0\n'))],
'7ec67741': [(log, ('2.5: Dialyn Brows blend VB Hash',)), (add_section_if_missing, ('d860525e', 'Dialyn.Brows.BlendVB', 'match_priority = 0\n'))],
'd90368ed': [(log, ('2.5: Dialyn Brows texcoord VB Hash',)), (add_section_if_missing, ('d860525e', 'Dialyn.Brows.TexcoordVB', 'match_priority = 0\n'))],

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
