"""
Seed Character Hash Commands
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
    Returns Seed's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'6cb35165': [(log, ('2.5: Seed Hair IB Hash',)),        (add_ib_check_if_missing,)],
'634ac589': [(log, ('2.5: Seed Body IB Hash',)),        (add_ib_check_if_missing,)],
'1d81bcc7': [(log, ('2.5: Seed Bib IB Hash',)),         (add_ib_check_if_missing,)],
'914e39c6': [(log, ('2.5: Seed Accessories IB Hash',)), (add_ib_check_if_missing,)],
'09d9dca7': [(log, ('2.5: Seed Face IB Hash',)),        (add_ib_check_if_missing,)],

# Face Textures
'f02ebff3': [
        (log,                           ('2.5: Seed FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],

# Shared Textures (Hair, Bib, Accessories)
'2fff22a7': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA Diffuse Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'bf2c273a': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA LightMap Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'a1658bbd': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA MaterialMap Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],

# Body Textures
'7c7c2622': [
        (log,                           ('2.5: Seed BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'b14c9c6f': [
        (log,                           ('2.5: Seed BodyA LightMap Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'da2deeaa': [
        (log,                           ('2.5: Seed BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (Hair, Body, Bib, Accessories)
'ebac056e': [
        (log,                           ('2.5: Seed Shared NormalMap Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seed',
    'game_versions': ['2.5'],
}
