"""
Ben Character Hash Commands
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
    Returns Ben's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ===== IB HASHES =====
'9c4f1a9a': [(log, ('2.5: Ben Face IB Hash',)), (add_ib_check_if_missing,)],
'94288cca': [(log, ('2.5: Ben Body IB Hash',)), (add_ib_check_if_missing,)],

# ===== FACE TEXTURES =====
# Face Diffuse - unchanged between versions
'00002f2c': [
        (log,                           ('2.5: Ben FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# Face LightMap - v1.0 hash updated to v2.5
'cc195dc5': [
        (log,                           ('1.0: Ben FaceA LightMap Hash (OLD)',)),
        (update_hash,                   ('2fa5ffa7',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'2fa5ffa7': [
        (log,                           ('2.5: Ben FaceA LightMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# Face MaterialMap - v1.0 hash updated to v2.5
'0bbceea0': [
        (log,                           ('1.0: Ben FaceA MaterialMap Hash (OLD)',)),
        (update_hash,                   ('12e5120e',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'12e5120e': [
        (log,                           ('2.5: Ben FaceA MaterialMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# Face NormalMap - shared with Body, new in v2.5
'ebac056e': [
        (log,                           ('2.5: Ben Face/Body NormalMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# ===== BODY TEXTURES =====
# Body Diffuse - unchanged between versions
'0313ed95': [
        (log,                           ('2.5: Ben BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],

# Body LightMap - v1.0 hash updated to v2.5
'cb84ed5e': [
        (log,                           ('1.0: Ben BodyA LightMap Hash (OLD)',)),
        (update_hash,                   ('d27a8f6b',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'd27a8f6b': [
        (log,                           ('2.5: Ben BodyA LightMap Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],

# Body MaterialMap - v1.0 hash updated to v2.5
'3f4f6bc0': [
        (log,                           ('1.0: Ben BodyA MaterialMap Hash (OLD)',)),
        (update_hash,                   ('2edd6f62',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'2edd6f62': [
        (log,                           ('2.5: Ben BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],

# ===== LEGACY HASHES (1.0 - REMOVED IN 2.5) =====
# These hashes existed in v1.0 mods but are no longer used in v2.5
# Keeping them for backward compatibility with old mods

# Legacy 1024p texture variants (removed - v2.5 only uses single resolution)
'8d83daba': [
        (log,                           ('1.0: Ben FaceA Diffuse 1024p Hash (LEGACY)',)),
        (update_hash,                   ('00002f2c',)),
    ],
'1439d2b9': [
        (log,                           ('1.0: Ben FaceA LightMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('2fa5ffa7',)),
    ],
'd665246d': [
        (log,                           ('1.0: Ben FaceA MaterialMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('12e5120e',)),
    ],
'894ea737': [
        (log,                           ('1.0: Ben FaceA NormalMap 2048p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ba809960': [
        (log,                           ('1.0: Ben FaceA NormalMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],

'd8dc4645': [
        (log,                           ('1.0: Ben BodyA Diffuse 1024p Hash (LEGACY)',)),
        (update_hash,                   ('0313ed95',)),
    ],
'6a80c2d8': [
        (log,                           ('1.0: Ben BodyA LightMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('d27a8f6b',)),
    ],
'decc28c5': [
        (log,                           ('1.0: Ben BodyA MaterialMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('2edd6f62',)),
    ],
'1b79fa5c': [
        (log,                           ('1.0: Ben BodyA NormalMap 2048p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'f6ecc618': [
        (log,                           ('1.0: Ben BodyA NormalMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ben',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
