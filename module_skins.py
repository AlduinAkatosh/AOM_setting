# -*- coding: UTF-8 -*-

from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.8, "Jaw Width"),
(210,0,-0.5,1.0, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,1.0, "Mouth Width"),
(50,0,-1.5,1.0, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,0.7, "Nose Width"),
(80,0,1.0,-0.1, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.5, "Cheek Bones"),
(150,0,-0.2,3.0, "Eye Width"),
(110,0,1.5,-0.9, "Eye to Eye Dist"),
(120,0,1.9,-1.0, "Eye Shape"),
(130,0,-0.5, 1.1, "Eye Depth"),
(140,0,1.0,-1.2, "Eyelids"),

(160,0,1.3,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.9, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-1.1,1.6, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.9,-0.6, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
woman_face_keys = [
(230,0,0.8,-1.0, "Chin Size"), 
(220,0,-1.0,1.0, "Chin Shape"), 
(10,0,-1.2,1.0, "Chin Forward"),
(20,0, -0.6, 1.2, "Jaw Width"), 
(40,0,-0.7,1.0, "Jaw Position"),
(270,0,0.9,-0.9, "Mouth-Nose Distance"),
(30,0,-0.5,1.0, "Mouth Width"),
(50,0, -0.5,1.0, "Cheeks"),

(60,0,-0.5,1.0, "Nose Height"),
(70,0,-0.5,1.1, "Nose Width"),
(80,0,1.5,-0.3, "Nose Size"),
(240,0,-1.0,0.8, "Nose Shape"),
(90,0, 0.0,1.1, "Nose Bridge"),

(100,0,-0.5,1.5, "Cheek Bones"),
(150,0,-0.4,1.0, "Eye Width"),
(110,0,1.0,0.0, "Eye to Eye Dist"),
(120,0,-0.2,1.0, "Eye Shape"),
(130,0,-0.1,1.6, "Eye Depth"),
(140,0,-0.2,1.0, "Eyelids"),


(160,0,-0.2,1.2, "Eyebrow Position"),
(170,0,-0.2,0.7, "Eyebrow Height"),
(250,0,-0.4,0.9, "Eyebrow Depth"),
(180,0,-1.5,1.2, "Eyebrow Shape"),
(260,0,1.0,-0.7, "Temple Width"),

(200,0,-0.5,1.0, "Face Depth"),
(210,0,-0.5,0.9, "Face Ratio"),
(190,0,-0.4,0.8, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]



man_face_keys_new = [(10, 0, -0.600000, 0.500000, "Temple Width"),
(20, 0, 0.600000, -0.250000, "Cheeks"),
(40, 0, -0.200000, 0.300000, "Nose Width"),
(50, 0, 0.200000, -0.300000, "Nose Shape"),
(60, 0, 0.250000, -0.250000, "Nose Height"),
(70, 0, -0.300000, 0.400000, "Nose Size"),
(80, 0, -0.300000, 0.650000, "Nose Bridge"),
(90, 0, 0.550000, -0.550000, "Mouth Width"),
(100, 0, 0.200000, -0.200000, "Mouth-Nose Distance"),
(110, 0, -0.200000, 0.600000, "Jaw Position"),
(130, 0, -0.500000, 1.000000, "Jaw Width"),
(140, 0, -0.400000, 0.500000, "Face Width"),
(150, 0, -0.250000, 0.450000, "Face Ratio"),
(160, 0, -0.200000, 0.250000, "Eye Width"),
(160, 0, 0.200000, -0.200000, "Eyebrow Position"),
(170, 0, -0.850000, 0.850000, "Eye Shape"),
(180, 0, -1.500000, 1.500000, "Eyelids"),
(190, 0, -0.250000, 0.150000, "Eye to Eye Dist"),
(200, 0, -0.300000, 0.700000, "Eye Depth"),
(210, 0, -0.750000, 0.750000, "Eyebrow Shape"),
(220, 0, -0.100000, 0.900000, "Eyebrow Depth"),
(220, 0, 0.800000, -0.800000, "Eyebrow Height"),
(230, 0, -0.400000, 0.800000, "Chin Shape"),
(240, 0, -0.400000, 0.300000, "Chin Size"),
(250, 0, -0.250000, 0.550000, "Chin Forward"),
(260, 0, -0.600000, 0.500000, "Cheek Bones"),
(270, 0, -0.300000, 1.000000, "Face Depth"),
(280, 0, 1.000000, 1.000000, "Post-Edit"),
]

east_face_keys = [(10, 0, -1.000000, 1.000000, "Chin Forward"),
(20, 0, -0.600000, 0.600000, "Jaw Width"),
(30, 0, -0.500000, 0.500000, "Mouth Width"),
(40, 0, -0.700000, 0.700000, "Jaw Position"),
(50, 0, -0.500000, 0.500000, "Cheeks"),
(60, 0, -1.500000, 1.500000, "Nose Height"),
(70, 0, -0.500000, 0.500000, "Nose Width"),
(80, 0, 1.500000, -1.500000, "Nose Size"),
(90, 0, -0.500000, 0.500000, "Nose Bridge"),
(100, 0, -0.500000, 0.500000, "Cheek Bones"),
(110, 0, 1.000000, -1.000000, "Eye to Eye Dist"),
(120, 0, -1.300000, 1.300000, "Eye Shape"),
(130, 0, -1.500000, 1.500000, "Eye Depth"),
(140, 0, -1.200000, 1.200000, "Eyelids"),
(150, 0, -1.400000, 1.400000, "Eye Width"),
(160, 0, -1.200000, 1.200000, "Eyebrow Position"),
(170, 0, -1.200000, 1.200000, "Eyebrow Height"),
(180, 0, -1.500000, 1.500000, "Eyebrow Shape"),
(190, 0, -0.400000, 0.400000, "Face Width"),
(200, 0, -0.500000, 0.500000, "Face Depth"),
(210, 0, -0.500000, 0.800000, "Face Ratio"),
(220, 0, -1.000000, 1.000000, "Chin Shape"),
(230, 0, 0.800000, -0.800000, "Chin Size"),
(240, 0, -1.000000, 1.000000, "Nose Shape"),
(250, 0, -1.400000, 1.400000, "Eyebrow Depth"),
(260, 0, 0.500000, -0.500000, "Temple Width"),
(270, 0, 0.900000, -0.900000, "Mouth-Nose Distance"),
(280, 0, -1.000000, 1.000000, "Post-Edit"),
]

undead_face_keys = []


chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "man", 0,#tf_male男
    "man_body", "man_calf_l", "m_handL",
    "male_head_new", man_face_keys_new,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_y3", "man_hair_t_new", "man_hair_y6_new", "man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u_new","man_hair_y_new","man_hair_y2","man_hair_y4_new", 
"man_hair_song_01", "man_hair_song_02", "man_hair_song_04", "man_hair_song_05", "man_hair_song_06", "man_hair_song_08", "man_hair_song_10", "man_hair_song_11", "man_hair_song_13", "man_hair_song_14", "man_hair_song_15", "man_hair_song_17", "man_hair_song_18", "man_hair_song_19", "man_hair_song_20"], 
    ["beard_new_a", "beard_new_b", "beard_new_c", "beard_new_d", "beard_new_e", "beard_new_f", "beard_new_g", "beard_new_h", "beard_new_i", "beard_new_k", "beard_new_l", "beard_new_m", "beard_new_n", "beard_new_o", "beard_new_p", "beard_new_q", "beard_new_r", "beard_new_s", "beard_new_t", "beard_new_u", "beard_new_v", "beard_new_y", "beard_new_z"], #beard meshes
    ["hair_blonde", "hair_red", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_black","beard_white"], #beard_materials
    [
#西方人
     ("manface_young_new",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
     ("manface_young_2_new",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_young_3_new",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
     ("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
#北方人
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_rugged_new",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
#南方人
     ("manface_mideast1",0xffaf9f7e,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("manface_african_new",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),   
     ("manface_black1",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#东方人
     ("manface_asian1",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_asian3",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_asian2",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_aisa02",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_aisa03",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
  
  (
    "woman", skf_use_morph_key_10,#tf_female女
    "woman_body",  "woman_calf_l", "f_handL",
    "female_head", woman_face_keys,
["woman_hair_p","woman_hair_n","woman_hair_o","woman_hair_q","woman_hair_r","woman_hair_t","woman_hair_s","hair_fdtk_14", "woman_hair_yu22","woman_hair_yu21","woman_hair_yu20","woman_hair_yu19","woman_hair_yu18","woman_hair_yu17","woman_hair_yu15","woman_hair_yu14","woman_hair_yu11","woman_hair_yu10","woman_hair_yu5", "woman_hair_t_new","woman_hair_rr","woman_hair_qq","woman_hair_q_new","woman_hair_p_new","woman_hair_o_new","woman_hair_nn","woman_hair_n_new", "woman_hair_gaolu_2_obsolete", "woman_hair_gaolu_1", "woman_hair_EOS_06", "woman_hair_EOS_03", "woman_hair_EOS_02", "woman_hair_EOS_01", "longshoulder2", "longshoulder","hairmessyhi","EOS_woman_hair_25","EOS_woman_hair_24","EOS_woman_hair_23","EOS_woman_hair_22","EOS_woman_hair_21","EOS_woman_hair_20","EOS_woman_hair_19","EOS_woman_hair_18","EOS_woman_hair_17","EOS_woman_hair_16","EOS_woman_hair_15","EOS_woman_hair_14","woman_hair_gaolu_0"], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [("womanface_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_b",0xffdfdfdf,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("womanface_a",0xffe8dfe5,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("womanface_brown",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
     ("womanface_african",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("womanface_aisa04",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("womanface_aisa05",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("womanface_aisa06",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
  ),


  (
    "east_woman", skf_use_morph_key_10,#0x2tf_east_female东方女
    "female_nakebody",  "female_nakefoot_l", "f_handL",
    "female_head_diaochan", east_face_keys,
[], #woman_hair_meshes
    ["hair_fdtk_01", "hair_fdtk_02", "hair_fdtk_03", "hair_fdtk_04", "hair_fdtk_05", "hair_fdtk_06", "hair_fdtk_07", "hair_fdtk_08", "hair_fdtk_09", "hair_fdtk_10", "hair_fdtk_11", "hair_fdtk_12", "hair_fdtk_13", "hair_fdtk_14", "hair_fdtk_15", "hair_fdtk_16", "hair_fdtk_17", "hair_fdtk_18", "hair_fdtk_19", "hair_fdtk_20", "hair_fdtk_21", "hair_fdtk_22",  "hair_fdtk_01", ],
    ["hair_black", "hair_white"], #hair textures
    [],
    [
     ("face_01",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_02",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_03",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_04",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_05",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_06",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_07",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_08",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_09",0xffe3e8ef,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("face_01o",0xffaf9f7e,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ],
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
  ),


      (
        "pretty_women", skf_use_morph_key_10,#0x3tf_pretty_female漂亮女
        "female_nakebody",  "female_nakefoot_l", "f_handL",
        "corprus_female_head", 
        [
         (40, 0, -1.000000, 0.000000, "Face Shape 1"),
         (30, 0, 0.000000, 1.000000, "Face Shape 2"),
         (10, 0, 0.000000, 1.000000, "Forehead"),
         (280, 0, 0.000000, 1.000000, "Post-Edit"),
        ],["woman_hair_p","woman_hair_n","woman_hair_o","woman_hair_q","woman_hair_r","woman_hair_t","woman_hair_s","woman_hair_yu23","woman_hair_yu22","woman_hair_yu21","woman_hair_yu20","woman_hair_yu19","woman_hair_yu18","woman_hair_yu17","woman_hair_yu15","woman_hair_yu14","woman_hair_yu11","woman_hair_yu10","woman_hair_yu5", "woman_hair_t_new","woman_hair_rr","woman_hair_qq","woman_hair_q_new","woman_hair_p_new","woman_hair_o_new","woman_hair_nn","woman_hair_n_new", "woman_hair_gaolu_2_obsolete", "woman_hair_gaolu_1", "woman_hair_EOS_06", "woman_hair_EOS_03", "woman_hair_EOS_02", "woman_hair_EOS_01", "longshoulder2", "longshoulder","hairmessyhi","EOS_woman_hair_25","EOS_woman_hair_24","EOS_woman_hair_23","EOS_woman_hair_22","EOS_woman_hair_21","EOS_woman_hair_20","EOS_woman_hair_19","EOS_woman_hair_18","EOS_woman_hair_17","EOS_woman_hair_16","EOS_woman_hair_15","EOS_woman_hair_14","woman_hair_gaolu_0"],
        [],
        ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
        [],
        [("womanface_young_gaolu",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_caucas_gaolu",0xffe8dfe5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_b_gaolu",0xffdfdfdf,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_brown_gaolu",0xffaf9f7e,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_african_gaolu",0xff808080,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_young_2_gaolu",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_east_gaolu",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ], 
        [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
        "skel_human", 0.95,
        psys_game_blood,psys_game_blood_2,
      ),


      (
        "special_women", skf_use_morph_key_10,#0x4tf_special_female特殊女脸
        "female_nakebody",  "female_nakefoot_l", "f_handL",
         "cw_no_head",        
        [],
        ["woman_hair_t_new", "woman_hair_p_new", "woman_hair_o_new", "woman_hair_n_new", "EOS_woman_hair_24", "EOS_woman_hair_16"],
        ["knight_femailtk", "milinfashi_alter", "FKamael_m000_t00_f", "head_2_human", "special_elf_head_1", "FKamael_m000_t01_f"],
        [
         "hair_purple", "hair_red", "hair_white", "elf_hair_ancester", "elf_hair_vita", "beard_blonde"], #头发贴图
        [
         "face_diff", "milinfashi_1_7", "FKamael_m000_t00_f", "v_spirit01_head", "elf_face_special_1", "FKamael_m000_t01_f"], #胡子（面部）贴图
        [
         ("cw_shield_tex", 0xffe3e8ef, ["hair_purple"],[0xffffffff, 0xffb04717]),#克莉斯特
         ("cw_shield_tex", 0xffe3e8ef, ["hair_red"],[0xffffffff, 0xffb04717]),#范伦汀娜
         ("cw_shield_tex", 0xffe3e8ef, ["hair_white"],[0xffffffff, 0xffb04717]),#丽莲
         ("cw_shield_tex", 0xffe3e8ef, ["elf_hair_ancester"],[0xffffffff, 0xffb04717]),#劳瑞
         ("cw_shield_tex", 0xffe3e8ef, ["elf_hair_vita"],[0xffffffff, 0xffb04717]),#爱丽克希亚
         ("cw_shield_tex", 0xffe3e8ef, ["beard_blonde"],[0xffffffff, 0xffb04717]),
         ], 
        [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
        "skel_human", 0.95,
        psys_game_blood,psys_game_blood_2,
      ),



#——————————————————————不死者——————————————————————————
  
      (
        "zombie", 0,#0x5僵尸
        "undead_body", "undead_calf_l", "undead_handL",
        "undead_head", undead_face_keys,
        [], #hair_meshes
        [], #beard meshes
        ["hair_blonde"], #hair textures
        ["hair_blonde"], #beard_materials
        [("undeadface",0xffffffff,["hair_blonde"]),
         ("root_human",0xff7b7563,["hair_blonde"]),#根生者
         ("crimson_world",0xff990000,["hair_blonde"]),#绯世之影
         ], #undead_face_textures
        [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit")], #voice sounds
        "skel_human", 1.0,
        -1,-1,
      ),

      (
        "skeleton", 0,#0x6骷髅
        "barf_skeleton", "barf_skeleton_calf_l", "barf_skeleton_handL",
        "barf_skull", undead_face_keys,
        ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
        [], #beard meshes ,"beard_q"
        ["hair_blonde", "hair_black", "hair_white"], #hair textures
        [], #beard_materials
        [("barf_skull",0xffffffff,["hair_blonde","hair_red", "hair_brunette"]),
         ], #undead_face_textures
        [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit")], #voice sounds
        "skel_human", 1.0,
        -1,-1,
      ),

      (
        "walker", 0,#0x7丧尸
        "zombie_body", "man_calf_l", "z_handL",
        "wight_face_1_1", undead_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_black", "hair_white"], #hair textures
    [], #beard_materials
        [("wight_face_1",0xffffffff,["hair_blonde","hair_red", "hair_brunette"]),
         ("wight_face_2",0xffffffff,["hair_blonde","hair_red", "hair_brunette"]),
         ], #undead_face_textures
        [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit")], #voice sounds
        "skel_human", 1.0,
        psys_game_blood,psys_game_blood_2,
      ),

  (
    "ghost", 0,#0x8幽灵
        "ghost_body", "ghost_calf_l", "ghost_handL",
        "female_head", woman_face_keys,#face keys
    ["woman_hair_t_new","woman_hair_rr","woman_hair_qq","woman_hair_q_new","woman_hair_p_new","woman_hair_o_new","woman_hair_nn","woman_hair_n_new", "woman_hair_gaolu_2_obsolete", "woman_hair_gaolu_1", "woman_hair_EOS_06", "woman_hair_EOS_03", "woman_hair_EOS_02", "woman_hair_EOS_01", "longshoulder2", "longshoulder","hairmessyhi","EOS_woman_hair_25","EOS_woman_hair_24","EOS_woman_hair_23","EOS_woman_hair_22","EOS_woman_hair_21","EOS_woman_hair_20","EOS_woman_hair_19","EOS_woman_hair_18","EOS_woman_hair_17","EOS_woman_hair_16","EOS_woman_hair_15","EOS_woman_hair_14"], #woman_hair_meshes
    [], #beard meshes
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [], #beard textures
    [("ghostface_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit")], #voice sounds
    "skel_human", 1.0,
    -1,-1,
  ),


#——————————————————————亚人种族——————————————————————————

      (
        "elf", skf_use_morph_key_10,#0x9tf_elf精灵
        "female_nakebody",  "female_nakefoot_l", "f_handL",
        "corprus_female_head",        
        [
         (40, 0, -1.000000, 0.000000, "Face Shape 1"),
         (30, 0, 0.000000, 1.000000, "Face Shape 2"),
         (10, 0, 0.000000, 1.000000, "Forehead"),
         (280, 0, 0.000000, 1.000000, "Post-Edit"),
        ],
   [
   #遮耳发型
   "woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_yu22", "woman_hair_yu21", "woman_hair_yu15", "woman_hair_yu14", "woman_hair_yu11", "woman_hair_yu5", "woman_hair_rr", "woman_hair_qq", "woman_hair_p_new", "woman_hair_o_new", "woman_hair_n_new", "woman_hair_gaolu_1", "woman_hair_EOS_03", "woman_hair_EOS_02", "woman_hair_EOS_01", "longshoulder2", "longshoulder", "EOS_woman_hair_24", "EOS_woman_hair_23", "EOS_woman_hair_22", "EOS_woman_hair_18", "EOS_woman_hair_17", "EOS_woman_hair_16", "EOS_woman_hair_15", "woman_hair_gaolu_0", 
   #露耳发型
   "woman_hair_yu20", "woman_hair_yu23", "woman_hair_yu19", "woman_hair_yu18", "woman_hair_yu17", "woman_hair_yu10", "woman_hair_t_new", "woman_hair_q_new", "woman_hair_nn", "woman_hair_gaolu_2_obsolete", "woman_hair_EOS_06", "hairmessyhi", "EOS_woman_hair_25", "EOS_woman_hair_21", "EOS_woman_hair_20", "EOS_woman_hair_19", "EOS_woman_hair_14"],

        ["half_elf_ear", "Jimmy_ear", "lion_ear", "bear_ear", "wolf_ear"],
        [
         #劣等精灵
         "half_elf_hair_green", "half_elf_hair_green_2", 
         #高等精灵
         "elf_hair_soul", "elf_hair_death", "elf_hair_ancester", "elf_hair_vita", "elf_hair_birth"], #hair textures
        [
         #劣等精灵
         "Jimmyears", "Jimmyears", 
         #高等精灵
         "Jimmyears", "Jimmyears", "Jimmyears", "Jimmyears", "Jimmyears"],
        [
         #劣等精灵
         ("womanface_b_gaolu",0xffe3e8ef,["half_elf_hair_green"],[0xffffffff]),
         ("womanface_b_gaolu",0xffe3e8ef,["half_elf_hair_green_2"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["half_elf_hair_green"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["half_elf_hair_green_2"],[0xffffffff]),
         #灵魄之树纯血精灵
         ("womanface_b_gaolu",0xffe3e8ef,["elf_hair_soul"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["elf_hair_soul"],[0xffffffff]),
         #死亡之树纯血精灵
         ("womanface_b_gaolu",0xffe3e8ef,["elf_hair_death"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["elf_hair_death"],[0xffffffff]),
         #先祖之树纯血精灵
         ("womanface_b_gaolu",0xffe3e8ef,["elf_hair_ancester"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["elf_hair_ancester"],[0xffffffff]),
         #生命之树纯血精灵
         ("womanface_b_gaolu",0xffe3e8ef,["elf_hair_vita"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["elf_hair_vita"],[0xffffffff]),
         #降生之树纯血精灵
         ("womanface_b_gaolu",0xffe3e8ef,["elf_hair_birth"],[0xffffffff]),
         ("womanface_caucas_gaolu",0xffe3e8ef,["elf_hair_birth"],[0xffffffff]),
         ], 
        [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
        "skel_human", 0.95,
        psys_game_blood,psys_game_blood_2,
      ),


  (
    "beast_man", 0,#0x10tf_beast_man兽人男
    "beastman_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_y9","man_hair_u","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["lion_ear", "bear_ear", "wolf_ear", "tiger_ear", "cow_horn", "goat_horn", "deer_ear", "rabbit_ear", "dog_ear", "fox_ear", "cat_ear"], #兽耳 
    ["hair_blonde", "hair_black", "hair_white", "hair_tiger", "hair_cow", "hair_sheep", "hair_deer", "hair_rabbit", "hair_dog", "elf_hair_ancester", "hair_cat"], #hair textures
    ["helm_Roman_standard_bearer", "Bear_helmet_diffuse", "wolf_head_mat", "tiger", "cow_mod_a", "goat", "deer", "costumes3", "young_wolf", "fox_head", "cat_head"], #beard_materials
    [    #狮兽人
         ("manface_young_new",0xffd0e0e0, ["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("manface_young_2",0xffcbe0e0, ["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         #熊兽人
         ("manface_african_new",0xff807c8a, ["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         ("manface_african",0xff807c8a, ["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         #狼兽人
         ("manface_midage",0xffdfefe1,["hair_white"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         ("manface_young_3_new",0xffdceded, ["hair_white"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         #虎兽人
         ("manface_young_2_new",0xffd0e0e0,["hair_tiger"],[0xffffffff, 0xffffdc35, 0xffff5809, 0xff272727]),
         #牛兽人
         ("manface_mideast1",0xffaf9f7e, ["hair_cow"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         ("manface_black1",0xff807c8a, ["hair_cow"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         #羊兽人
         ("manface_7",0xffc0c8c8,["hair_sheep"],[0xffffffff, 0xff642100]),
         #鹿兽人
         ("manface_young",0xffd0e0e0,["hair_deer"],[0xffffffff, 0xffc4c400, 0xff600000]),
         ("manface_young_3",0xffdceded, ["hair_deer"],[0xffffffff, 0xffc4c400, 0xff600000]),
         #兔兽人
         ("manface_midage",0xffdfefe1,["hair_rabbit"],[0xffffffff, 0xffc4c400, 0xff600000]),
         ("manface_young_3",0xffdceded, ["hair_rabbit"],[0xffffffff, 0xffc4c400, 0xff600000]),
         #狗兽人
         ("manface_midage_2",0xfde4c8d8,["hair_dog"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         ("manface_rugged_new",0xffb0aab5, ["hair_dog"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         #狐兽人
         ("manface_young_3_new",0xffc0c8c8,["elf_hair_ancester"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         ("manface_young_3",0xffdceded, ["elf_hair_ancester"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         #猫兽人
         ("manface_young_new",0xffd0e0e0, ["hair_cat"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("manface_young",0xffcbe0e0, ["hair_cat"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ], #man_face_textures,
[(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),


      (
        "beast_woman", skf_use_morph_key_10,#0x11tf_beast_woman兽人女
        "female_nakebody",  "female_nakefoot_l", "f_handL",
        "corprus_female_head",        
        [
         (40, 0, -1.000000, 0.000000, "Face Shape 1"),
         (30, 0, 0.000000, 1.000000, "Face Shape 2"),
         (10, 0, 0.000000, 1.000000, "Forehead"),
         (280, 0, 0.000000, 1.000000, "Post-Edit"),
        ],
   [
   #遮耳发型
   "woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_yu22", "woman_hair_yu21", "woman_hair_yu15", "woman_hair_yu14", "woman_hair_yu11", "woman_hair_yu5", "woman_hair_rr", "woman_hair_qq", "woman_hair_p_new", "woman_hair_o_new", "woman_hair_n_new", "woman_hair_gaolu_1", "woman_hair_EOS_03", "woman_hair_EOS_02", "woman_hair_EOS_01", "longshoulder2", "longshoulder", "EOS_woman_hair_24", "EOS_woman_hair_23", "EOS_woman_hair_22", "EOS_woman_hair_18", "EOS_woman_hair_17", "EOS_woman_hair_16", "EOS_woman_hair_15", "woman_hair_gaolu_0", 
   #露耳发型
   "woman_hair_yu23", "woman_hair_yu20", "woman_hair_yu19", "woman_hair_yu18", "woman_hair_yu17", "woman_hair_yu10", "woman_hair_t_new", "woman_hair_q_new", "woman_hair_nn", "woman_hair_gaolu_2_obsolete", "woman_hair_EOS_06", "hairmessyhi", "EOS_woman_hair_25", "EOS_woman_hair_21", "EOS_woman_hair_20", "EOS_woman_hair_19", "EOS_woman_hair_14"],
        ["lion_ear", "bear_ear", "wolf_ear", "tiger_ear", "cow_horn", "goat_horn", "deer_ear", "rabbit_ear", "dog_ear", "fox_ear", "cat_ear"],
        [
         "hair_blonde", "hair_black", "hair_white", "hair_tiger", "hair_cow", "hair_sheep", "hair_deer", "hair_rabbit", "hair_dog", "elf_hair_ancester", "hair_cat"], #hair textures
        [
          "helm_Roman_standard_bearer", "Bear_helmet_diffuse", "wolf_head_mat", "tiger", "cow_mod_a", "goat", "deer", "costumes3", "young_wolf", "fox_head", "cat_head"],
        [
         #狮兽人
         ("womanface_brown_gaolu",0xffc78865, ["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_african_gaolu",0xff664445, ["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         #熊兽人
         ("womanface_brown_gaolu",0xffc78865, ["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         ("womanface_african_gaolu",0xff664445, ["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         #狼兽人
         ("womanface_brown_gaolu",0xffc78865,["hair_white"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         ("womanface_african_gaolu",0xff664445, ["hair_white"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         #虎兽人
         ("womanface_caucas_gaolu",0xffe3e8ef,["hair_tiger"],[0xffffffff, 0xffffdc35, 0xffff5809, 0xff272727]),
         #牛兽人
         ("womanface_brown_gaolu",0xffc78865, ["hair_cow"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         ("womanface_african_gaolu",0xff664445, ["hair_cow"],[0xffffffff, 0xffb04717, 0xff502a19, 0xffd9d9d9]),
         #羊兽人
         ("womanface_young_2_gaolu",0xffe3e8ef,["hair_sheep"],[0xffffffff, 0xff642100]),
         #鹿兽人
         ("womanface_caucas_gaolu",0xffe3e8ef,["hair_deer"],[0xffffffff, 0xffffdc35, 0xffff5809, 0xff272727]),
         ("womanface_brown_gaolu",0xffc78865,["hair_deer"],[0xffffffff, 0xffc4c400, 0xff600000]),
         #兔兽人
         ("womanface_young_2_gaolu",0xffe3e8ef,["hair_rabbit"],[0xffffffff, 0xffc4c400, 0xff600000]),
         ("womanface_b_gaolu",0xffe3e8ef, ["hair_rabbit"],[0xffffffff, 0xffc4c400, 0xff600000]),
         #狗兽人
         ("womanface_brown_gaolu",0xffc78865,["hair_dog"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         ("womanface_east_gaolu",0xffe3e8ef, ["hair_dog"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         #狐兽人
         ("womanface_east_gaolu",0xffe3e8ef,["elf_hair_ancester"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         ("womanface_brown_gaolu",0xffc78865, ["elf_hair_ancester"],[0xffffffff, 0xffb04717, 0xffdf1b1b, 0xff0c0404]),
         #猫兽人
         ("womanface_young_2_gaolu",0xffe3e8ef, ["hair_cat"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_b_gaolu",0xffe3e8ef, ["hair_cat"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ], 
        [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
        "skel_human", 0.95,
        psys_game_blood,psys_game_blood_2,
      ),


  (
    "deep_one_man", 0,#0x12tf_deep_one_man深渊族男
    "man_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_y9","man_hair_u","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["deep_diver_ear", "deep_diver_ear_with_ear_ring"], #鱼耳 
    ["elf_hair_vita"], #hair textures
    ["lizard_hair1"], #beard_materials
    [
     ("manface_young_new",0xffd0e0e0,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19]),     
     ("manface_young_2_new",0xffcbe0e0,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_young_3_new",0xffdceded,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_7",0xffc0c8c8,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_rugged_new",0xffb0aab5,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ], 
[(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),


  (
    "deep_one_woman", skf_use_morph_key_10,#0x13tf_deep_one_woman深渊族女
    "female_nakebody",  "female_nakefoot_l", "f_handL",
    "corprus_female_head",        
    [
         (40, 0, -1.000000, 0.000000, "Face Shape 1"),
         (30, 0, 0.000000, 1.000000, "Face Shape 2"),
         (10, 0, 0.000000, 1.000000, "Forehead"),
         (280, 0, 0.000000, 1.000000, "Post-Edit"),
    ],
   [
   #遮耳发型
   "woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_yu22", "woman_hair_yu21", "woman_hair_yu15", "woman_hair_yu14", "woman_hair_yu11", "woman_hair_yu5", "woman_hair_rr", "woman_hair_qq", "woman_hair_p_new", "woman_hair_o_new", "woman_hair_n_new", "woman_hair_gaolu_1", "woman_hair_EOS_03", "woman_hair_EOS_02", "woman_hair_EOS_01", "longshoulder2", "longshoulder", "EOS_woman_hair_24", "EOS_woman_hair_23", "EOS_woman_hair_22", "EOS_woman_hair_18", "EOS_woman_hair_17", "EOS_woman_hair_16", "EOS_woman_hair_15", "woman_hair_gaolu_0", 
   #露耳发型
   "woman_hair_yu23", "woman_hair_yu20", "woman_hair_yu19", "woman_hair_yu18", "woman_hair_yu17", "woman_hair_yu10", "woman_hair_t_new", "woman_hair_q_new", "woman_hair_nn", "woman_hair_gaolu_2_obsolete", "woman_hair_EOS_06", "hairmessyhi", "EOS_woman_hair_25", "EOS_woman_hair_21", "EOS_woman_hair_20", "EOS_woman_hair_19", "EOS_woman_hair_14"],
    ["deep_diver_ear", "deep_diver_ear_with_ear_ring"], #鱼耳 
    ["elf_hair_vita"], #hair textures
    ["lizard_hair1"], #beard_materials
    [
         ("womanface_young_2_gaolu",0xffe3e8ef,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_east_gaolu",0xffe3e8ef,["elf_hair_vita"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_b_gaolu",0xffe3e8ef,["elf_hair_vita"],[0xffffffff, 0xffffdc35, 0xffff5809, 0xff272727]),
    ], 
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
  ),

]

