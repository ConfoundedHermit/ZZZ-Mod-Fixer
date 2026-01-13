"""
BelleSummer Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json extraction
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns BelleSummer's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'43ed3c22': [(log, ('2.5: BelleSummer Body IB Hash',)), (add_ib_check_if_missing,)],
'69148073': [(log, ('2.5: BelleSummer Top IB Hash',)), (add_ib_check_if_missing,)],
'93f38bdd': [(log, ('2.5: BelleSummer Hat IB Hash',)), (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.5: BelleSummer Face IB Hash (Shared with Belle)',)), (add_ib_check_if_missing,)],
'ea055cac': [(log, ('2.5: BelleSummer Hair IB Hash',)), (add_ib_check_if_missing,)],

# === Face Textures ===
'75ec3614': [
        (log,                           ('2.5: BelleSummer FaceA Diffuse Hash (Shared with Belle)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'20954729': [
        (log,                           ('2.5: BelleSummer HairA, TopA, HatA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: BelleSummer HairA, TopA, HatA NormalMap Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
    ],
'e0a86379': [
        (log,                           ('2.5: BelleSummer HairA, TopA, HatA LightMap Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
    ],
'0298fba2': [
        (log,                           ('2.5: BelleSummer HairA, TopA, HatA, FaceA MaterialMap Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification A/B) ===
# Body Classifications A and B share the same texture set as Hair/Top/Hat
# These are already covered by the hash entries above: 20954729, ebac056e, e0a86379, 0298fba2

# === Body Textures (Classification C) ===
'24639b77': [
        (log,                           ('2.5: BelleSummer BodyC Diffuse Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'7947679c': [
        (log,                           ('2.5: BelleSummer BodyC LightMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'33f28c6d': [
        (log,                           ('2.5: BelleSummer BodyC MaterialMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification D) ===
'1ce58567': [
        (log,                           ('2.5: BelleSummer BodyD Diffuse Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log,                           ('2.5: BelleSummer BodyD LightMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log,                           ('2.5: BelleSummer BodyD MaterialMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ]
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleSummer',
    'game_versions': ['2.5'],
}
