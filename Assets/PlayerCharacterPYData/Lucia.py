"""
Lucia Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Lucia's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'340fc999': [(log, ('2.5: Lucia Hair IB Hash',)),           (add_ib_check_if_missing,)],
'78043df0': [(log, ('2.5: Lucia Hair Position Hash',))],
'97dde567': [(log, ('2.5: Lucia Hair Texcoord Hash',))],
'bfd60db5': [(log, ('2.5: Lucia Hair Blend Hash',))],

# === Body Component ===
'd39c304d': [(log, ('2.5: Lucia Body IB Hash',)),           (add_ib_check_if_missing,)],
'234c641a': [(log, ('2.5: Lucia Body Position Hash',))],
'0400f04f': [(log, ('2.5: Lucia Body Texcoord Hash',))],
'3f4f9fa9': [(log, ('2.5: Lucia Body Blend Hash',))],

# === Cape Component ===
'cd80d116': [(log, ('2.5: Lucia Cape IB Hash',)),           (add_ib_check_if_missing,)],
'08ae4b5d': [(log, ('2.5: Lucia Cape Position Hash',))],
'dd0e570f': [(log, ('2.5: Lucia Cape Texcoord Hash',))],
'b917fca5': [(log, ('2.5: Lucia Cape Blend Hash',))],

# === CapeExtra Component ===
'692a4e10': [(log, ('2.5: Lucia CapeExtra IB Hash',)),      (add_ib_check_if_missing,)],
'c035f6bd': [(log, ('2.5: Lucia CapeExtra Position Hash',))],
'90f30bc1': [(log, ('2.5: Lucia CapeExtra Texcoord Hash',))],
'946dc2ff': [(log, ('2.5: Lucia CapeExtra Blend Hash',))],

# === Face Component ===
'6986f28e': [(log, ('2.5: Lucia Face IB Hash',)),           (add_ib_check_if_missing,)],

# === Face Textures ===
'20a6224d': [
        (log,                           ('2.5: Lucia FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures (Shared between HairA and HairB) ===
'5b0b47c9': [
        (log,                           ('2.5: Lucia Hair Diffuse Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'243feee8': [
        (log,                           ('2.5: Lucia Hair LightMap Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'211a5700': [
        (log,                           ('2.5: Lucia Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Lucia NormalMap Hash (Shared across components)',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Shared between BodyA and BodyB) ===
'2ca45943': [
        (log,                           ('2.5: Lucia Body Diffuse Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'f117c868': [
        (log,                           ('2.5: Lucia Body LightMap Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'a16861d2': [
        (log,                           ('2.5: Lucia Body MaterialMap Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],

# === Cape Textures (Shares Hair textures) ===
# Note: Cape component uses the same textures as Hair (5b0b47c9, 243feee8, 211a5700)
# These are already defined in the Hair Textures section above and will apply to Cape as well

# === CapeExtra Textures (Shares Hair textures) ===
# Note: CapeExtra component uses the same textures as Hair (5b0b47c9, 243feee8, 211a5700)
# These are already defined in the Hair Textures section above and will apply to CapeExtra as well
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lucia',
    'game_versions': ['2.5'],
    'notes': 'New character in version 2.5. Hair, Cape, and CapeExtra components share the same texture set.',
}
