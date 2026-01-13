"""
Orphie Character Hash Commands
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
    Returns Orphie's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'6988bfcd': [(log, ('2.5: Orphie Hair IB Hash',)), (add_ib_check_if_missing,)],
'a5eac582': [(log, ('2.5: Orphie Body IB Hash',)), (add_ib_check_if_missing,)],
'80017921': [(log, ('2.5: Orphie Legs IB Hash',)), (add_ib_check_if_missing,)],
'3766fa59': [(log, ('2.5: Orphie MagusTail IB Hash',)), (add_ib_check_if_missing,)],
'389256d8': [(log, ('2.5: Orphie MagusNozzle IB Hash',)), (add_ib_check_if_missing,)],
'2935f885': [(log, ('2.5: Orphie MagusDrum IB Hash',)), (add_ib_check_if_missing,)],
'ed85f33b': [(log, ('2.5: Orphie Face IB Hash',)), (add_ib_check_if_missing,)],

# Hair Textures
'ce52779f': [
        (log,                           ('2.5: Orphie HairA Diffuse Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'77abe83b': [
        (log,                           ('2.5: Orphie HairA LightMap Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'94ed2491': [
        (log,                           ('2.5: Orphie HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures
'c9bea5d7': [
        (log,                           ('2.5: Orphie BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'9a0406fe': [
        (log,                           ('2.5: Orphie BodyA LightMap Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'1daf926d': [
        (log,                           ('2.5: Orphie BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],

# Legs Textures
'dd4120db': [
        (log,                           ('2.5: Orphie LegsA Diffuse Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'a9ae84df': [
        (log,                           ('2.5: Orphie LegsA LightMap Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'867ceb5b': [
        (log,                           ('2.5: Orphie LegsA MaterialMap Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],

# Magus Shared Textures (MagusTail, MagusNozzle, MagusDrum)
'dd80fa1d': [
        (log,                           ('2.5: Orphie Magus (Tail/Nozzle/Drum) Diffuse Hash',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'92c6b20b': [
        (log,                           ('2.5: Orphie Magus (Tail/Nozzle/Drum) LightMap Hash',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'cb65982e': [
        (log,                           ('2.5: Orphie Magus (Tail/Nozzle/Drum) MaterialMap Hash',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],

# Face Textures
'0df52ae7': [
        (log,                           ('2.5: Orphie FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (across all components)
'ebac056e': [
        (log,                           ('2.5: Orphie Shared NormalMap Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Orphie',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Legs', 'MagusTail', 'MagusNozzle', 'MagusDrum', 'Face'],
}
