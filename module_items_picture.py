# -*- coding: UTF-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
picture_items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset

#item_modifier
["imod_0", "imod_plain", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_1", "imod_cracked", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_2", "imod_rusty", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_3", "imod_bent", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_4", "imod_chipped", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_5", "imod_battered", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_6", "imod_poor", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],     #no use
["imod_7", "imod_crude", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_8", "imod_old", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_9", "imod_cheap", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_10", "imod_fine", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_11", "imod_well_made", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_12", "imod_sharp", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_13", "imod_balanced", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_14", "imod_tempered", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_15", "imod_deadly", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_16", "imod_exquisite", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_17", "imod_masterwork", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_18", "imod_heavy", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_19", "imod_strong", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_20", "imod_powerful", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_21", "imod_tattered", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_22", "imod_ragged", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_23", "imod_rough", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_24", "imod_sturdy", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_25", "imod_thick", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_26", "imod_hardened", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_27", "imod_reinforced", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_28", "imod_superb", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_29", "imod_lordly", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_30", "imod_lame", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_31", "imod_swaybacked", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_32", "imod_stubborn", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_33", "imod_timid", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_34", "imod_meek", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none],      #no use
["imod_35", "imod_spirited", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_36", "imod_champion", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_37", "imod_fresh", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_38", "imod_day_old", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_39", "imod_two_day_old", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_40", "imod_smelling", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_41", "imod_rotten", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["imod_42", "imod_large_bag", [("round01", 0)], 0, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 


###########################################################技能###########################################################
#ACTIVE SKILL
["active_skills_begin", "active_skills_begin", [("sorcery_11_1", 0)], 0, 0, 1000, abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
#itp_unique represents martial arts, itp_always_loot represents sorcery, and itp_no_parry means magic. 
#abundance表示消耗（武技耗精力，术法耗时间咏唱(单位秒)，魔法耗蓝）
#max_ammo表示技能时间（×10），根据动作的时间得到，技能后摇
#food_quality表示基础伤害。
#difficulty表示受伤害武器加成时，使用的是刺的攻击力还是挥的攻击力。1表示挥，2表示刺。
#weapon length表示投技的捕捉范围

#——————————————————————————————————武技——————————————————————————————————
#穿刺
["active_lunge", "active_lunge", [("active_lunge", 0)], itp_martial_art|itp_damage_type, 0, 9, abundance(6)|max_ammo(16)|food_quality(14)|difficulty(2), imodbits_none], #0.9秒
["active_double_lunge", "active_double_lunge", [("active_double_lunge", 0)], itp_martial_art|itp_damage_type, 0, 1115, abundance(6)|max_ammo(18)|food_quality(14)|difficulty(2), imodbits_none], #1.1，1.5秒

#跳劈
["active_leap_attack", "active_leap_attack", [("active_leap_attack", 0)], itp_martial_art|itp_damage_type, 0, 506, abundance(6)|max_ammo(14)|food_quality(18)|difficulty(1), imodbits_none], #0.5，0.6秒

#刃旋舞
["active_double_slant_slash", "active_double_slant_slash", [("active_double_slant_slash", 0)], itp_martial_art|itp_damage_type, 0, 5061314, abundance(6)|max_ammo(21)|food_quality(15)|difficulty(1), imodbits_none], #0.5，0.6，1.3，1.4秒

#重斩
["active_thump", "active_thump", [("active_thump", 0)], itp_martial_art|itp_damage_type, 0, 910, abundance(6)|max_ammo(21)|food_quality(20)|difficulty(1), imodbits_none], #0.9, 1.0秒
["active_heavy_jump_chop", "active_heavy_jump_chop", [("active_heavy_jump_chop", 0)], itp_martial_art|itp_damage_type, 0, 80910, abundance(6)|max_ammo(18)|food_quality(22)|difficulty(1), imodbits_none], #0.8，0.9, 1.0秒
["active_heavy_spin_chop", "active_heavy_spin_chop", [("active_heavy_spin_chop", 0)], itp_martial_art|itp_damage_type, 0, 91011, abundance(6)|max_ammo(17)|food_quality(22)|difficulty(1), imodbits_none], #0.9，1.0，1.1秒

#盲击
["active_casual_attack", "active_casual_attack", [("active_casual_attack", 0)], itp_martial_art|itp_damage_type, 0, 612132021, abundance(12)|max_ammo(33)|food_quality(10)|difficulty(1), imodbits_none], #0.6, 1.2, 1.3, 2.0, 2.1秒
["active_heavy_casual_attack", "active_heavy_casual_attack", [("active_heavy_casual_attack", 0)], itp_martial_art|itp_damage_type, 0, 708151624, abundance(6)|max_ammo(31)|food_quality(18)|difficulty(1), imodbits_none], #0.7，0.8，1.5，1.6，2.4秒

#旋击斩
["active_spinning_slash_simple", "active_spinning_slash_simple", [("active_spinning_slash_simple", 0)], itp_martial_art|itp_damage_type, 0, 60708, abundance(8)|max_ammo(15)|food_quality(10)|difficulty(1), imodbits_none],#0.6，0.7, 0.8秒
["active_spinning_assault_slash", "active_spinning_assault_slash", [("active_spinning_assault_slash", 0)], itp_martial_art|itp_damage_type, 0, 60809, abundance(8)|max_ammo(13)|food_quality(12)|difficulty(1), imodbits_none], #0.6, 0.8, 0.9秒
["active_spinning_defense_slash", "active_spinning_defense_slash", [("active_spinning_defense_slash", 0)], itp_martial_art|itp_damage_type, 0, 20809, abundance(8)|max_ammo(13)|food_quality(12)|difficulty(1), imodbits_none], #0.2, 0.8, 0.9秒


["active_curve_sword", "active_curve_sword", [("active_curve_sword", 0)], itp_martial_art|itp_damage_type, 0, 40910, abundance(6)|max_ammo(18)|food_quality(12)|difficulty(1), imodbits_none], #0.4，0.9，1.0秒
["active_undercover_slash", "active_undercover_slash", [("active_undercover_slash", 0)], itp_martial_art|itp_damage_type, 0, 405, abundance(6)|max_ammo(12)|food_quality(15)|difficulty(1), imodbits_none], #0.4, 0.5秒
["active_sweep_away", "active_sweep_away", [("active_sweep_away", 0)], itp_martial_art|itp_damage_type, 0, 8091012, abundance(4)|max_ammo(16)|food_quality(15)|difficulty(1), imodbits_none], #check in 0.8, 0.9, 1.0, 1.2秒

#射术相关
["active_power_shot", "active_power_shot", [("active_power_shot", 0)], itp_martial_art|itp_special_type, 0, 11, abundance(10)|max_ammo(20)|food_quality(0)|difficulty(0), imodbits_none],#拉满弓 1.1秒射箭
["active_continuous_shooting", "active_continuous_shooting", [("active_continuous_shooting", 0)], itp_martial_art|itp_special_type, 0, 121620, abundance(15)|max_ammo(29)|food_quality(0)|difficulty(0), imodbits_none],#三连射 1.2、1.6、2.0秒射箭
["active_multiple_arrow", "active_multiple_arrow", [("active_multiple_arrow", 0)], itp_martial_art|itp_special_type, 0, 16, abundance(24)|max_ammo(30)|food_quality(0)|difficulty(0), imodbits_none],#多重箭 1.6秒射箭
["active_throwing_arrow", "active_throwing_arrow", [("active_throwing_arrow", 0)], itp_martial_art|itp_special_type, 0, 6, abundance(10)|max_ammo(15)|food_quality(0)|difficulty(0), imodbits_none],#投箭 0.6秒出手
["active_left_hand_block_arrow", "active_left_hand_block_arrow", [("active_left_hand_block_arrow", 0)], itp_martial_art|itp_special_type, 0, 0, abundance(8)|max_ammo(14)|food_quality(0)|difficulty(0), imodbits_none],

["active_earthsplitting_charge", "active_earthsplitting_charge", [("active_earthsplitting_charge", 0)], itp_martial_art|itp_special_type, 0, 9, abundance(15)|max_ammo(12)|food_quality(150)|difficulty(1), imodbits_none], #0.9秒砸地
["active_ground_heaving", "active_ground_heaving", [("active_ground_heaving", 0)], itp_martial_art|itp_special_type, 0, 13, abundance(15)|max_ammo(20)|food_quality(100)|difficulty(1), imodbits_none], #1.3秒掀地

#投技
["active_cutthroat", "active_cutthroat", [("active_cutthroat", 0)], itp_martial_art|itp_special_type|itp_grab_skill, 0, 13, abundance(10)|weapon_length(200)|max_ammo(25)|food_quality(40)|difficulty(2), imodbits_none],#割喉   #1.3秒时割开喉咙

["active_concealed_dissection", "active_concealed_dissection", [("active_concealed_dissection", 0)], itp_martial_art|itp_special_type, 0, 0, abundance(0)|max_ammo(14)|food_quality(0)|difficulty(0), imodbits_none],#隐匿肢解

#骑技
["active_war_stomp", "active_war_stomp", [("active_war_stomp", 0)], itp_martial_art|itp_riding_skill|itp_special_type, 0, 22, abundance(30)|max_ammo(40)|food_quality(170)|difficulty(1), imodbits_none], #2.2秒砸地
["active_silver_fall", "active_silver_fall", [("active_silver_fall", 0)], itp_martial_art|itp_riding_skill|itp_special_type, 0, 28, abundance(35)|max_ammo(50)|food_quality(200)|difficulty(1), imodbits_none], #2.8秒砸地


#元素
["active_flame_sweep", "active_flame_sweep", [("active_flame_sweep", 0)], itp_martial_art|itp_special_type, 0, 809101214, abundance(15)|max_ammo(27)|food_quality(0)|difficulty(0), imodbits_none],#0.9、1.1、1.3、1.5、1.7各射一箭

#毒
["active_release_toxin_fog", "active_release_toxin_fog", [("active_release_toxin_fog", 0)], itp_martial_art|itp_special_type, 0, 10172431, abundance(15)|max_ammo(42)|food_quality(0)|difficulty(0), imodbits_none],#1.0、1.7、2.4、3.1秒各释放一次

#猩红
["active_blood_strike", "active_blood_strike", [("active_blood_strike", 0)], itp_martial_art|itp_special_type, 0, 918, abundance(20)|max_ammo(26)|food_quality(100)|difficulty(0), imodbits_none],#0.9秒隐身＋瞬移，1.5秒现身，1.8秒造成伤害＋烟雾特效。

#不死者
["active_spectre_burst", "active_spectre_burst", [("active_spectre_burst", 0)], itp_martial_art|itp_special_type, 0, 8, abundance(5)|max_ammo(13)|food_quality(0)|difficulty(0), imodbits_none],#0.8秒起爆


#——————————————————————————————————术法——————————————————————————————————
#元素
["active_fire_arrow", "active_fire_arrow", [("active_fire_arrow", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(10)|food_quality(1), imodbits_none], 
["active_fire_throw", "active_fire_throw", [("active_fire_throw", 0)], itp_sorcery, 0, 0, abundance(1)|max_ammo(10)|food_quality(1), imodbits_none], 

["active_ice_arrow", "active_ice_arrow", [("active_ice_arrow", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(10)|food_quality(1), imodbits_none], 
["active_wind_blade", "active_wind_blade", [("active_wind_blade", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(10)|food_quality(1), imodbits_none], 

["active_stone_shoot", "active_stone_shoot", [("active_stone_shoot", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(10)|food_quality(1), imodbits_none], 

["active_flame_weapon", "active_flame_weapon", [("active_flame_weapon", 0)], itp_sorcery, 0, 0, abundance(6)|max_ammo(35)|food_quality(0), imodbits_none], 

#猩红
["active_warcy_blooddrum", "active_warcy_blooddrum", [("active_warcy_blooddrum", 0)], itp_sorcery, 0, 0, abundance(5)|max_ammo(35)|food_quality(0), imodbits_none], 
["active_warcy_bloodsteel", "active_warcy_bloodsteel", [("active_warcy_bloodsteel", 0)], itp_sorcery, 0, 0, abundance(5)|max_ammo(35)|food_quality(0), imodbits_none], 

["active_warcy_blooddrum_group", "active_warcy_blooddrum_group", [("active_warcy_blooddrum_group", 0)], itp_sorcery, 0, 0, abundance(12)|max_ammo(35)|food_quality(0), imodbits_none], 
["active_warcy_bloodsteel_group", "active_warcy_bloodsteel_group", [("active_warcy_bloodsteel_group", 0)], itp_sorcery, 0, 0, abundance(12)|max_ammo(35)|food_quality(0), imodbits_none], 
["active_warcy_bloodburst", "active_warcy_bloodburst", [("active_warcy_bloodburst", 0)], itp_sorcery, 0, 0, abundance(6)|max_ammo(11)|food_quality(0), imodbits_none], 
["active_warcy_red_tide", "active_warcy_red_tide", [("active_warcy_red_tide", 0)], itp_sorcery, 0, 0, abundance(8)|max_ammo(11)|food_quality(0), imodbits_none], 

["active_warcy_bloodrain", "active_warcy_bloodrain", [("active_warcy_bloodrain", 0)], itp_sorcery, 0, 0, abundance(60)|max_ammo(45)|food_quality(0), imodbits_none], 

#不死者
#food_quality用于管理需求的移动墓地的量或积怨的层数
["active_rib_shot", "active_rib_shot", [("active_rib_shot", 0)], itp_sorcery, 0, 0, abundance(1)|max_ammo(11)|food_quality(3), imodbits_none], 
["active_triple_rib_shot", "active_triple_rib_shot", [("active_triple_rib_shot", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(11)|food_quality(9), imodbits_none], 

["active_undead_creation_skeleton", "active_undead_creation_skeleton", [("active_undead_creation_skeleton", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(15)|food_quality(7), imodbits_none], 
["active_undead_creation_skeleton_pikeman", "active_undead_creation_skeleton_pikeman", [("active_undead_creation_skeleton_pikeman", 0)], itp_sorcery, 0, 0, abundance(3)|max_ammo(15)|food_quality(12), imodbits_none], 
["active_undead_creation_skeleton_swordman", "active_undead_creation_skeleton_swordman", [("active_undead_creation_skeleton_swordman", 0)], itp_sorcery, 0, 0, abundance(3)|max_ammo(15)|food_quality(16), imodbits_none], 
["active_undead_creation_skeleton_archer", "active_undead_creation_skeleton_archer", [("active_undead_creation_skeleton_archer", 0)], itp_sorcery, 0, 0, abundance(3)|max_ammo(15)|food_quality(16), imodbits_none], 
["active_undead_creation_wild_hunter", "active_undead_creation_skeleton_rider", [("active_undead_creation_wild_hunter", 0)], itp_sorcery, 0, 0, abundance(12)|max_ammo(15)|food_quality(500), imodbits_none], 

["active_undead_creation_giant", "active_undead_creation_giant", [("active_undead_creation_giant", 0)], itp_sorcery, 0, 0, abundance(4)|max_ammo(15)|food_quality(80), imodbits_none], 
["active_undead_creation_giant_sword", "active_undead_creation_giant_sword", [("active_undead_creation_giant_sword", 0)], itp_sorcery, 0, 0, abundance(4)|max_ammo(15)|food_quality(100), imodbits_none], 
["active_undead_creation_giant_spear", "active_undead_creation_giant_spear", [("active_undead_creation_giant_spear", 0)], itp_sorcery, 0, 0, abundance(4)|max_ammo(15)|food_quality(0), imodbits_none], 

["active_create_spectre", "active_create_spectre", [("active_create_spectre", 0)], itp_sorcery, 0, 0, abundance(2)|max_ammo(15)|food_quality(1), imodbits_none], 
["active_create_spectre_group", "active_create_spectre_group", [("active_create_spectre_group", 0)], itp_sorcery, 0, 0, abundance(3)|max_ammo(15)|food_quality(2), imodbits_none], 

#神术
["active_pray_holy_aegis", "active_pray_holy_aegis", [("active_pray_holy_aegis", 0)], itp_sorcery, 0, 0, abundance(16)|max_ammo(25)|food_quality(0), imodbits_none], 
["active_pray_heavenly_wall", "active_pray_heavenly_wall", [("active_pray_heavenly_wall", 0)], itp_sorcery, 0, 0, abundance(28)|max_ammo(25)|food_quality(0), imodbits_none], 
["active_pray_drop_of_reasoning_sea", "active_pray_drop_of_reasoning_sea", [("active_pray_drop_of_reasoning_sea", 0)], itp_sorcery, 0, 0, abundance(40)|max_ammo(25)|food_quality(0), imodbits_none], 

["active_pray_holy_healing", "active_pray_holy_healing", [("active_pray_holy_healing", 0)], itp_sorcery, 0, 0, abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["active_pray_heavenly_favor", "active_pray_heavenly_favor", [("active_pray_heavenly_favor", 0)], itp_sorcery, 0, 0, abundance(24)|max_ammo(0)|food_quality(0), imodbits_none], 
["active_pray_holy_strike", "active_pray_holy_strike", [("active_pray_holy_strike", 0)], itp_sorcery, 0, 0, abundance(8)|max_ammo(0)|food_quality(0), imodbits_none], 
["active_final_conjure", "active_final_conjure", [("active_final_conjure", 0)], itp_sorcery, 0, 0, abundance(255)|max_ammo(0)|food_quality(0), imodbits_none], 

["active_skills_end", "active_skills_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 




#PASSIVE SKILL
["passive_skills_begin", "passive_skills_begin", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], 
#itp_always_loot标签表示危险，abundance一项用于记录该被动最高等级

#基础技能
["passive_stoical", "passive_stoical", [("passive_stoical", 0)], itp_unique, 0, 0, abundance(4), imodbits_none], 
["passive_ricochet", "passive_ricochet", [("passive_ricochet", 0)], itp_unique, 0, 0, abundance(4), imodbits_none], 
["passive_critical_attack", "passive_critical_attack", [("passive_critical_attack", 0)], itp_unique, 0, 0, abundance(5), imodbits_none], 
["passive_fatal", "passive_fatal", [("passive_fatal", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 
["passive_critical_protection", "passive_critical_protection", [("passive_critical_protection", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_fake_shield", "passive_fake_shield", [("passive_fake_shield", 0)], itp_unique, 0, 0, abundance(6), imodbits_none], 
["passive_fake_shield_penetration", "passive_fake_shield_penetration", [("passive_fake_shield_penetration", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_force_unloading", "passive_force_unloading", [("passive_force_unloading", 0)], itp_unique, 0, 0, abundance(8), imodbits_none], 
["passive_collapse_force", "passive_collapse_force", [("passive_collapse_force", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_damage_management", "passive_damage_management", [("passive_damage_management", 0)], itp_unique, 0, 0, abundance(3), imodbits_none], 

["passive_desperate_counterattack", "passive_desperate_counterattack", [("passive_desperate_counterattack", 0)], itp_unique, 0, 0, abundance(4), imodbits_none], 
["passive_desperate_defense", "passive_desperate_defense", [("passive_desperate_defense", 0)], itp_unique, 0, 0, abundance(4), imodbits_none], 
["passive_obsession_blow", "passive_obsession_blow", [("passive_obsession_blow", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 

#潜入相关
["passive_concealing", "passive_concealing", [("passive_concealing", 0)], itp_unique, 0, 0, abundance(5), imodbits_none], 
["passive_lightly_run", "passive_lightly_run", [("passive_lightly_run", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_malicious_perception", "passive_malicious_perception", [("passive_malicious_perception", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 

#潜水相关
["passive_diving", "passive_diving", [("passive_diving", 0)], itp_unique, 0, 0, abundance(2), imodbits_none], #潜泳技艺2
["passive_scuba", "passive_scuba", [("passive_scuba", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], #水肺

#龙
["passive_dragon_power_surging", "passive_dragon_power_surging", [("passive_dragon_power_surging", 0)], itp_always_loot, 0, 0, abundance(8), imodbits_none], 

#圣
["passive_flesh_consecration", "passive_flesh_consecration", [("passive_flesh_consecration", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_holy_rebirth", "passive_holy_rebirth", [("passive_holy_rebirth", 0)], itp_always_loot, 0, 0, abundance(4), imodbits_none], 

#血液
["passive_blood_intoxication", "passive_blood_intoxication", [("passive_blood_intoxication", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], #流血相关
["passive_blood_addition", "passive_blood_addition", [("passive_blood_addition", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 
["passive_blood_armor", "passive_blood_armor", [("passive_blood_armor", 0)], itp_always_loot, 0, 0, abundance(6), imodbits_none], 

["passive_blood_churn", "passive_blood_churn", [("passive_blood_churn", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], #血潮汹涌相关
["passive_blood_motivation", "passive_blood_motivation", [("passive_blood_motivation", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 
["passive_blood_boil", "passive_blood_boil", [("passive_blood_boil", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 
["passive_blood_attack", "passive_blood_attack", [("passive_blood_attack", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 
["passive_blood_defend", "passive_blood_defend", [("passive_blood_defend", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 

["passive_strong_vitality", "passive_strong_vitality", [("passive_strong_vitality", 0)], itp_unique, 0, 0, abundance(5), imodbits_none], 
["passive_blood_arrogance", "passive_blood_arrogance", [("passive_blood_arrogance", 0)], itp_unique, 0, 0, abundance(5), imodbits_none], 
["passive_blood_jealousy", "passive_blood_jealousy", [("passive_blood_jealousy", 0)], itp_unique, 0, 0, abundance(5), imodbits_none], 
["passive_crazy_bloodthirsty", "passive_crazy_bloodthirsty", [("passive_crazy_bloodthirsty", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 
["passive_bloodswallower", "passive_bloodswallower", [("passive_bloodswallower", 0)], itp_always_loot, 0, 0, abundance(7), imodbits_none], 

["passive_blood_atresia", "passive_blood_atresia", [("passive_blood_atresia", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 

#不死者
["passive_dead_shell", "passive_dead_shell", [("passive_dead_shell", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 
["passive_undead_rebirth", "passive_undead_rebirth", [("passive_undead_rebirth", 0)], itp_always_loot, 0, 0, abundance(4), imodbits_none], 
["passive_bone_accumulation", "passive_bone_accumulation", [("passive_bone_accumulation", 0)], itp_always_loot, 0, 0, abundance(9), imodbits_none], 
["passive_resentment", "passive_resentment", [("passive_resentment", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 

["passive_spread_decay", "passive_spread_decay", [("passive_spread_decay", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 
["passive_spread_cancer", "passive_spread_cancer", [("passive_spread_cancer", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 
["passive_spread_submerge", "passive_spread_submerge", [("passive_spread_submerge", 0)], itp_always_loot, 0, 0, abundance(5), imodbits_none], 
["passive_infect_invalid", "passive_infect_invalid", [("passive_infect_invalid", 0)], itp_unique, 0, 0, abundance(3), imodbits_none], 

["powell_military_tradition", "powell_military_tradition", [("passive_powell_military_tradition", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["yishith_military_tradition", "yishith_military_tradition", [("passive_yishith_military_tradition", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["korouto_military_tradition", "korouto_military_tradition", [("passive_korouto_military_tradition", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["papal_military_tradition", "papal_military_tradition", [("passive_papal_military_tradition", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["longshu_military_tradition", "longshu_military_tradition", [("passive_longshu_military_tradition", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["starkhook_military_tradition", "starkhook_military_tradition", [("passive_starkhook_military_tradition", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["state_military_tradition", "state_military_tradition", [("passive_state_military_tradition", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 

["passive_stubborn_beast_body", "passive_stubborn_beast_body", [("passive_stubborn_beast_body", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_inner_domination", "passive_inner_domination", [("passive_inner_domination", 0)], itp_unique, 0, 0, abundance(5), imodbits_none], 
["passive_protecting_qi", "passive_protecting_qi", [("passive_protecting_qi", 0)], itp_unique, 0, 0, abundance(9), imodbits_none], 
["passive_vonbining_yin_and_yang", "passive_vonbining_yin_and_yang", [("passive_vonbining_yin_and_yang", 0)], itp_unique, 0, 0, abundance(4), imodbits_none], 
["passive_five_element_quenching_body", "passive_five_element_quenching_body", [("passive_five_element_quenching_body", 0)], itp_unique, 0, 0, abundance(6), imodbits_none], 
["passive_living_organs", "passive_living_organs", [("passive_living_organs", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 
["passive_sublimation_of_existence_form", "passive_sublimation_of_existence_form", [("passive_sublimation_of_existence_form", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 
["passive_human_summit", "passive_human_summit", [("passive_human_summit", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 

["passive_guess_seven_game", "passive_guess_seven_game", [("passive_guess_seven_game", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], 

["passive_heart_of_the_vast_reasoning_sea", "passive_heart_of_the_vast_reasoning_sea", [("passive_heart_of_the_vast_reasoning_sea", 0)], itp_unique, 0, 0, abundance(1), imodbits_none], 

["passive_skills_end", "passive_skills_end", [("sorcery_11_1", 0)], 0, 0, 0, weight(10.000000)|abundance(10), imodbits_none], 


###########################################################状态###########################################################

["state_begin", "state_begin", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
##                                           abundance           max_ammo               food_quality                                   value
#itp_timing_type计时型              增加值                   阈值                     减少值(1秒一次)                           伤害、治疗量等
#itp_count_type计次型                                       阈值（次数）                                                                伤害、治疗量等
#itp_unconditional_type无条件型                                                                                                           伤害、治疗量等

#普通毒
["state_weak_toxin", "state_weak_toxin", [("state_weak_toxin", 0)], itp_timing_type, 0, 1, abundance(0)|max_ammo(100)|food_quality(5), imodbits_none], #弱毒
["state_venom_toxin", "state_venom_toxin", [("state_venom_toxin", 0)], itp_timing_type, 0, 15, weight(15)|abundance(0)|max_ammo(100)|food_quality(5), imodbits_none], #猛毒
["state_strong_toxin", "state_strong_toxin", [("state_strong_toxin", 0)], itp_timing_type, 0, 3, weight(3)|abundance(0)|max_ammo(100)|food_quality(4), imodbits_none], #强毒
["state_paralytic_toxin", "state_paralytic_toxin", [("state_paralytic_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(40)|food_quality(8), imodbits_none], #惊厥毒
["state_weaken_toxin", "state_weaken_toxin", [("state_weaken_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(80)|food_quality(8), imodbits_none], #虚弱毒

#异毒
["state_highly_toxin", "state_highly_toxin", [("state_highly_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(100)|food_quality(0), imodbits_none], #剧毒
#supreme poison
["state_withered_toxin", "state_withered_toxin", [("state_withered_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(100)|food_quality(0), imodbits_none], 
["state_confusion_toxin", "state_confusion_toxin", [("state_confusion_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(100)|food_quality(0), imodbits_none], 
["state_cavity_toxin", "state_cavity_toxin", [("state_cavity_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(100)|food_quality(0), imodbits_none], 
["state_blood_toxin", "ross_cursed_blood", [("state_blood_toxin", 0)], itp_count_type, 0, 0, abundance(0)|max_ammo(8)|food_quality(0), imodbits_none], 
["state_requiem_toxin", "ross_requiem_blood", [("state_requiem_toxin", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(100)|food_quality(0), imodbits_none], 

#血液
["state_bleeding", "state_bleeding", [("state_bleeding", 0)], itp_timing_type, 0, 0, abundance(1)|max_ammo(20)|food_quality(0), imodbits_none], 
["state_lose_blood", "state_lose_blood", [("state_lose_blood", 0)], itp_unconditional_type, 0, 0, abundance(2)|max_ammo(0)|food_quality(0), imodbits_none], 
["state_blood_burst", "state_blood_burst", [("state_blood_burst", 0)], itp_count_type, 0, 0, abundance(0)|max_ammo(9)|food_quality(0), imodbits_none], 

["state_rebirth", "state_rebirth", [("state_rebirth", 0)], itp_count_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(0), imodbits_none], 
#不死者
["state_moving_cemetery", "state_moving_cemetery", [("state_moving_cemetery", 0)], itp_count_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(0), imodbits_none], 
["state_decay_changing", "state_decay_changing", [("state_walker_changing", 0)], itp_timing_type, 0, 0, abundance(1)|max_ammo(10)|food_quality(0), imodbits_none], 
["state_cancer_changing", "state_cancer_changing", [("state_walker_changing", 0)], itp_timing_type, 0, 0, abundance(1)|max_ammo(8)|food_quality(0), imodbits_none], 
["state_submerge_changing", "state_submerge_changing", [("state_walker_changing", 0)], itp_timing_type, 0, 0, abundance(1)|max_ammo(6)|food_quality(0), imodbits_none], 
#幽灵状态
["state_blurs", "stateblurs", [("state_walker_changing", 0)], itp_timing_type, 0, 0, abundance(1)|max_ammo(4)|food_quality(0), imodbits_none], 

#附魔
["state_flame_weapon", "flame_weapon", [("state_walker_changing", 0)], itp_timing_type|itp_enchant, 0, 0, abundance(1)|max_ammo(15)|food_quality(0), imodbits_none], 

["state_left_hand_block_arrow", "state_left_hand_block_arrow", [("state_encouraged", 0)], itp_timing_type, 0, 0, weight(0)|abundance(0)|max_ammo(0)|food_quality(1), imodbits_none], 

#通用提升攻防
["state_encouraged", "state_encouraged", [("state_encouraged", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(1), imodbits_none], 
["state_generous_death", "state_generous_death", [("state_generous_death", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(1), imodbits_none], 
["state_fighting_spirit", "state_fighting_spirit", [("state_fighting_spirit", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(1), imodbits_none], 
["state_war_anger", "state_war_anger", [("state_war_anger", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(1), imodbits_none], 

["state_lose_balance", "state_lose_balance", [("state_lose_balance", 0)], itp_timing_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(1), imodbits_none], #失去平衡
["state_breath_holding", "state_breath_holding", [("state_breath_holding", 0)], itp_count_type, 0, 0, abundance(3)|max_ammo(120)|food_quality(0), imodbits_none], #闭气

["state_emergancy_care", "state_emergancy_care", [("state_emergancy_care", 0)], itp_count_type, 0, 0, abundance(3)|max_ammo(0)|food_quality(0), imodbits_none], 
["state_sneak", "state_sneak", [("state_sneak", 0)], itp_unconditional_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(0), imodbits_none], 
["state_drop_gold", "state_drop_gold", [("state_drop_gold", 0)], itp_unconditional_type, 0, 0, abundance(0)|max_ammo(0)|food_quality(0), imodbits_none], 

["state_end", "state_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 





###########################################################地块###########################################################
#abundance（＋1防止溢出）表示该地块有几种变体，需要在那几个里面随机
#max_ammo表示该地块的扩散等级。用于处理在两种地块相接时的扩散，以防地块轮廓过于清晰显眼。默认空白地块的扩散等级为1，农田最低为0。如果等级相同，就会过一个随机相互扩散
##
["zone_none", "zone_none", [("sorcery_11_2", 0)], 0, 0, 0, abundance(1)|max_ammo(1), imodbits_none], 

["zone_water", "Terrain Water", [("zone_swamp", 0)], 0, 0, 0, abundance(1)|max_ammo(0), imodbits_none], #水体
["zone_cliff", "Terrain Cliff", [("zone_swamp", 0)], 0, 0, 0, abundance(1)|max_ammo(0), imodbits_none], #岩壁
["zone_swamp", "Terrain Swamp", [("zone_swamp", 0)], 0, 0, 0, abundance(2)|max_ammo(3), imodbits_none], #沼泽
["zone_forest", "Terrain Forest", [("sandbox_forest_1", 0)], 0, 0, 0, abundance(2)|max_ammo(2), imodbits_none], #森林
["zone_steppe_forest", "Terrain Steppe Forest", [("zone_steppe_forest", 0)], 0, 0, 0, abundance(2)|max_ammo(1), imodbits_none], #稀树草原
["zone_taiga_forest", "Terrain Taiga Forest", [("zone_taiga_forest", 0)], 0, 0, 0, abundance(2)|max_ammo(2), imodbits_none], #泰加林
["zone_oasis", "Terrain Oasis", [("sorcery_11_2", 0)], 0, 0, 0, abundance(2)|max_ammo(3), imodbits_none], #绿洲

["zone_field", "Terrain Field", [("sandbox_field_1", 0)], 0, 0, 0, abundance(2)|max_ammo(0), imodbits_none], #田野

["zone_tent", "Terrain Tent", [("state_sneak", 0)], 0, 0, 0, abundance(2)|max_ammo(1), imodbits_none], #帐篷区
["zone_rural", "Terrain Rural", #农村
   [("sandbox_rural_1", 0)], 
   0, 0, 0, abundance(2)|max_ammo(2), imodbits_none], 
["zone_slum", "Terrain Slum", #贫民窟
   [("sandbox_slum_1", ixmesh_inventory), ("sandbox_slum_1", imod_cracked), ("sandbox_slum_2", imod_rusty)], 
   0, 0, 0, abundance(3)|max_ammo(2), imod_cracked|imod_rusty],
["zone_residential_area", "Terrain Residential Area", #平民区
   [("sandbox_city_house_1", imod_cracked), ("sandbox_city_house_2", imod_rusty), ("sandbox_city_house_3", imod_bent), ("sandbox_city_house_4", imod_chipped), ("sandbox_city_house_5", imod_battered)], 
   0, 0, 0, abundance(6)|max_ammo(3), imod_cracked|imod_rusty|imod_bent|imod_chipped|imod_battered], 
["zone_rich_area", "Terrain Rich Area", #富人区
   [("sandbox_rich_area_1", imod_cracked), ("sandbox_rich_area_2", imod_rusty)], 
   0, 0, 0, abundance(3)|max_ammo(4), imod_cracked|imod_rusty], 

["zone_commercial_area", "Terrain Commercial Area", #商业区
   [("sandbox_commercial_area_1", 0)], 
   0, 0, 0, abundance(2)|max_ammo(3), imodbits_none], 
["zone_industry_area", "Terrain Industry Area", #工业区
   [("sandbox_industry_area_1", imod_cracked), ("sandbox_industry_area_2", imod_rusty), ("sandbox_industry_area_3", imod_bent)], 
   0, 0, 0, abundance(4)|max_ammo(3), imod_cracked|imod_rusty|imod_bent], 
["zone_ruin", "Terrain Ruins", [("state_sneak", 0)], 0, 0, 0, abundance(1)|max_ammo(2), imodbits_none], #废墟

["zone_end", "zone_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], 



###########################################################建筑###########################################################
#itp_unique表示城墙，需要对边角进行特殊处理
#itp_always_loot表示隐藏建筑，不会直接显示在界面上，需要探索。
##
["building_begin", "building_begin", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], 

["bridge", "Bridge", [("sandbox_bridge_1", 0)], 0, 0, 0, abundance(2)|max_ammo(8), imodbits_none], #桥梁 

#城墙
["small_wall", "Small_wall", [("sandbox_small_wall_1", 0)], itp_unique, 0, 0, abundance(2)|max_ammo(4), imodbits_none], #矮墙
["city_wall", "City_wall", [("sandbox_city_wall_1", 0)], itp_unique, 0, 0, abundance(2)|max_ammo(4), imodbits_none], #城墙
["high_wall", "High_wall", [("sandbox_city_wall_1", 0)], itp_unique, 0, 0, abundance(2)|max_ammo(4), imodbits_none], #高墙
["tremendous_wall", "Tremendous_wall", [("sandbox_city_wall_1", 0)], itp_unique, 0, 0, abundance(2)|max_ammo(4), imodbits_none], #巨墙

#营房
["barrack", "Barrack", [("sandbox_barrack_1", 0)], 0, 0, 0, abundance(2)|max_ammo(1), imodbits_none], #兵营
["base", "Base", [("sandbox_base_1", 0)], 0, 0, 0, abundance(2)|max_ammo(1), imodbits_none], #据点
["fort", "Fort", [("sandbox_fort_1", 0)], 0, 0, 0, abundance(2)|max_ammo(1), imodbits_none], #要塞

#行政
["office", "Office", #办公楼
   [("sandbox_office_1", imod_cracked), ("sandbox_office_2", imod_rusty)], 
   0, 0, 0, abundance(3)|max_ammo(1), imod_cracked|imod_rusty], 
["castle", "Castle", [("sandbox_castle_1", 0)], 0, 0, 0, abundance(2)|max_ammo(4), imodbits_none], #城堡
["palace", "Palace", [("state_sneak", 0)], 0, 0, 0, abundance(1)|max_ammo(4), imodbits_none], #宫殿

#生产
["farm", "Farm", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #农场
["ranch", "Ranch", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #牧场
["orchard", "Orchard", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #果园

#贸易
["warehouse", "Warehouse", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #仓库
["wharf", "Wharf", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #码头

#宗教
["church", "Church", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #教堂
["monastery", "Monastery", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #修道院
["temple", "Temple", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #神殿

#植被
["garden", "Garden", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #园林
["artificial_forest", "Artificial Forest", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #人造林

#犯罪
["criminal_den", "Criminal Den", [("state_sneak", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], #贼窝
["red_light_district", "Red Light District", [("state_sneak", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], #红灯区
["underworld_stronghold", "Underworld Stronghold", [("state_sneak", 0)], itp_always_loot, 0, 0, abundance(1), imodbits_none], #黑社会据点

["adventurer_station", "Adventurer Station", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #冒险者协会

#特殊
["cemetery", "Cemetery", [("state_sneak", 0)], 0, 0, 0, abundance(1), imodbits_none], #墓园

["building_end", "building_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10), imodbits_none], 



###########################################################阵型###########################################################
["formation_common", "Formation Common", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #普通
["formation_assault", "Formation Assault", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #进攻
["formation_suppress", "Formation Suppress", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #压制
["formation_counterattack", "Formation Counterattack", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #反冲击
["formation_defense", "Formation Defense", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #防御
["formation_fortress", "Formation Fortress", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #筑垒
["formation_station", "Formation Station", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #驻扎

["formation_end", "formation_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10), imodbits_none], 


##########################################################编队职能##########################################################
["detachment_common", "Detachment Common", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #普通
["detachment_strike", "Detachment Strike", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #强袭
["detachment_support", "Detachment Support", [("knight_a", 0)], 0, 0, 0, abundance(2), imodbits_none], #支援
["detachment_firepower", "Detachment Firepower", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #火力
["detachment_defend", "Detachment Defend", [("knight_a", 0)], 0, 0, 0, abundance(2), imodbits_none], #固守
["detachment_commander", "Detachment Commander", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #指挥
["detachment_special_force", "Detachment Special Force", [("knight_a", 0)], 0, 0, 0, abundance(2), imodbits_none], #特种
["detachment_strategic", "Detachment Strategic", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #战略
["detachment_cannon_fodder", "Detachment Cannon Fodder", [("knight_a", 0)], 0, 0, 0, abundance(2), imodbits_none], #炮灰
["detachment_sapper", "Detachment Sapper", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #工兵
["detachment_logistic", "Detachment Logistic", [("knight_a", 0)], 0, 0, 0, abundance(2), imodbits_none], #后勤
["detachment_monster", "Detachment Monster", [("knight_a", 0)], 0, 0, 0, abundance(1), imodbits_none], #敌意单位

["detachment_end", "detachment_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10), imodbits_none], 


##########################################################兵种职能##########################################################
["function_combat", "Function Combat", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #格斗
["function_strike", "Function Strike", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #突击
["function_maneuver", "Function Maneuver", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #机动支援
["function_defend", "Function Defend", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #防御
["function_commander", "Function Commander", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #指挥
["function_hero_agent", "Function Hero Agent", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #英雄单位
["function_reconnaissance", "Function Reconnaissance", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #侦察
["function_assassin", "Function Assassin", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #刺客
["function_curved_fire", "Function Curved Fire", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #曲射火力
["function_flat_fire", "Function Flat Fire", [("sorcery_11_1", 0)], 0, 0, 0, abundance(2), imodbits_none], #平射火力
["function_strategic_strength", "Function Strategic Strength", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #战略力量
["function_assistance", "Function Assistance", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #辅助
["function_cannon_fodder", "Function Cannon Fodder", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #炮灰
["function_non_military_personnel", "Function Non Military Personnel", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #非战斗人员
["function_monster", "Function Monster", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #敌意存在

["function_end", "function_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10), imodbits_none], 
]