"""
YeShunguang Character Hash Commands
ZZZ Mod Fixer v2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YeShunguang's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.5: YeShunguang Ears IB Hash',)),         (add_ib_check_if_missing,)],
'3b1b73fe': [(log, ('2.5: YeShunguang Strip IB Hash',)),        (add_ib_check_if_missing,)],
'4a178546': [(log, ('2.5: YeShunguang Legs IB Hash',)),         (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.5: YeShunguang Tail IB Hash',)),         (add_ib_check_if_missing,)],
'8c8de427': [(log, ('2.5: YeShunguang Clips IB Hash',)),        (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.5: YeShunguang Hair IB Hash',)),         (add_ib_check_if_missing,)],
'ae840e72': [(log, ('2.5: YeShunguang Antenna IB Hash',)),      (add_ib_check_if_missing,)],
'c209c22b': [(log, ('2.5: YeShunguang Torso IB Hash',)),        (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.5: YeShunguang Face IB Hash',)),         (add_ib_check_if_missing,)],
'f9ce7b07': [(log, ('2.5: YeShunguang ArmTassels IB Hash',)),   (add_ib_check_if_missing,)],
'0534b536': [(log, ('2.5: YeShunguang BackTassel IB Hash',)),   (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.5: YeShunguang BraidStrips IB Hash',)),  (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.5: YeShunguang Bow IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.5: YeShunguang Brows IB Hash',)),        (add_ib_check_if_missing,)],

# === VB Hashes ===
'd1ffd339': [(log, ('2.5: YeShunguang TexCoord VB Hash',)),     (update_hash, ('dbb027eb',))],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: YeShunguang Shared NormalMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '3b1b73fe', '4a178546', '869976a3', '8c8de427', '999bff94', 'ae840e72', 'c209c22b', 'f9ce7b07', '0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'6ed0c951': [
        (log,                           ('2.5: YeShunguang FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguang.Face.IB', 'match_priority = 0\n')),
    ],

# === Ears, Clips, Hair, Antenna Textures (Shared Set 1) ===
'79f6acd7': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA Diffuse Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
    ],
'88269532': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
    ],
'825fbf26': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
    ],

# === Strip, Torso, ArmTassels Textures (Shared Set 2) ===
'5bd7d31b': [
        (log,                           ('2.5: YeShunguang StripA, TorsoA, ArmTasselsA Diffuse Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
    ],
'369a2106': [
        (log,                           ('2.5: YeShunguang StripA LightMap Hash',)),
        (add_section_if_missing,        ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n')),
    ],
'72c1cf72': [
        (log,                           ('2.5: YeShunguang TorsoA, ArmTasselsA LightMap Hash',)),
        (add_section_if_missing,        (('c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoArmSet.IB', 'match_priority = 0\n')),
    ],
'a5872c6e': [
        (log,                           ('2.5: YeShunguang StripA, TorsoA, ArmTasselsA MaterialMap Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
    ],

# === Legs, Tail Textures (Shared Set 3) ===
'727d3454': [
        (log,                           ('2.5: YeShunguang LegsA, TailA Diffuse Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
    ],
'4eb5aae2': [
        (log,                           ('2.5: YeShunguang LegsA, TailA LightMap Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
    ],
'7f5f0193': [
        (log,                           ('2.5: YeShunguang LegsA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === BackTassel, BraidStrips, Bow Textures (Shared Set 4) ===
'804099eb': [
        (log,                           ('2.5: YeShunguang BackTasselA, BraidStripsA, BowA Diffuse Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'5ca93726': [
        (log,                           ('2.5: YeShunguang BackTasselA, BraidStripsA, BowA LightMap Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'1ba6bebf': [
        (log,                           ('2.5: YeShunguang BackTasselA, BraidStripsA, BowA MaterialMap Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguang',
    'game_versions': ['2.5'],
}
