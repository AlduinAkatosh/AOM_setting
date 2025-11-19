# -*- coding: UTF-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *
from module_items_picture import *
from module_items_faction import *

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


#血量控制
# trigger param 1 = defender agent_id
# trigger param 2 = attacker agent_id
# trigger param 3 = inflicted damage
# trigger param 4 = weapon item_id (ranged weapon in case of ranged attack)
# trigger param 5 = missile item_id (ammo in case of ranged attack)
shield_hit_point_trigger = (ti_on_shield_hit, [
        (store_trigger_param, ":defender_agent_no", 1),
#        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
#        (store_trigger_param, ":attacker_weapon_no", 4),
#        (store_trigger_param, ":missile_item_no", 5),
        (agent_get_wielded_item, ":item_no", ":defender_agent_no", 1),#盾
        (call_script, "script_shield_technique", ":defender_agent_no", ":damage_count", ":item_no"),
        (set_trigger_result, reg1),
    ])


#精灵弓折断
# trigger param 1 = attacker agent_id
#pos1 is weapon position
elf_bow_trigger = (ti_on_weapon_attack, [
        (store_trigger_param_1, ":attack_agent_no"),
#        (agent_get_troop_id, ":troop_no", ":attack_agent_no"),

        (agent_get_wielded_item, ":bow_no", ":attack_agent_no", 0),#right hand
        (agent_unequip_item, ":attack_agent_no", ":bow_no"),
        (agent_play_sound, ":attack_agent_no", "snd_shield_broken"),
        (particle_system_burst, "psys_gourd_piece_2", pos1, 5),
        (agent_deliver_damage_to_agent, ":attack_agent_no", ":attack_agent_no", 10),

        (try_begin),
           (eq, ":attack_agent_no", "$mission_player_agent"),
           (agent_set_slot, "$mission_player_agent", "$cur_weapon_left_hand", -1),
           (store_add, ":modifier_slot_no", "$cur_weapon_left_hand", 12),
           (agent_set_slot, "$mission_player_agent", ":modifier_slot_no", -1),#modifier

           (store_sub, ":inventory_slot_no", "$cur_weapon_left_hand", 31),
           (call_script, "script_player_remove_new_inventory_slot", ":inventory_slot_no"),
           (call_script, "script_troop_remove_new_inventory_slot_modifier", "trp_player", ":inventory_slot_no"),#modifier

           (display_message, "@弓 碎 了 ！"),
        (try_end),
    ])

#幽灵武器
# trigger param 1 = attacker agent_id
ghost_weapon_trigger = (ti_on_weapon_attack, [
        (store_trigger_param_1, ":attack_agent_no"),
        (call_script, "script_get_state_timer", ":attack_agent_no", "itm_state_blurs"),#状态：虚影化（幽灵）
        (ge, reg1, 1),                                                                                                                         #success
        (agent_set_visibility, ":attack_agent_no", 1),
        (call_script, "script_activate_state", ":attack_agent_no", "itm_state_blurs", 1),#攻击后解除虚影化，从一开始增加到重新虚影化为止
    ])

# trigger param 1 = attacker agent_id
weapon_visual_effect_trigger = (ti_on_weapon_attack, [
        (store_trigger_param_1, ":agent_no"),
        (agent_get_slot, ":value_no", ":agent_no", slot_agent_enchant),
        (gt, ":value_no", 0),                                     #已有附魔
        (val_mod, ":value_no", 1000),
        (val_add, ":value_no", "itm_state_begin"), #获取现有附魔
        (try_begin),
           (eq, ":value_no", "itm_state_flame_weapon"),#烈焰武装
           (call_script, "script_get_state_count", ":agent_no", "itm_state_flame_weapon"),
           (ge, reg1, 10000),                                      #未挂上特效
           (assign, ":value_no", reg1),
           (val_mod, ":value_no", 10000),
           (call_script, "script_activate_state", ":agent_no", "itm_state_flame_weapon", ":value_no"),#附魔过一次后开始减少时间。
           (agent_set_animation, ":agent_no", "anim_active_enchant_2", 1),

           (agent_get_wielded_item, ":weapon_no", ":agent_no", 0),
           (item_get_weapon_length, ":weapon_length", ":weapon_no"),
           (val_sub, ":weapon_length", 30),                   #粒子效果向下移
           (set_position_delta, 0, ":weapon_length", 0),
           (particle_system_add_new, "psys_sword_fire"),
           (set_current_color, 150, 130, 70),
           (add_point_light, 10, 30),
        (try_end),
    ])



# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["tutorial_spear", "Spear", [("spear", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield, 4222124851986688, 0, weight(4.500000)|abundance(100)|difficulty(0)|weapon_length(158)|spd_rtng(80)|swing_damage(0, cut)|thrust_damage(19, pierce), imodbits_polearm], 
["tutorial_club", "Club", [("club", 0)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary, 9223388529554358286, 0, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(95)|spd_rtng(95)|swing_damage(11, blunt)|thrust_damage(0, pierce), imodbits_none], 
["tutorial_battle_axe", "Battle_Axe", [("battle_ax", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 9223635923965575392, 0, weight(5.000000)|abundance(100)|difficulty(0)|weapon_length(108)|spd_rtng(88)|swing_damage(27, cut)|thrust_damage(0, pierce), imodbits_axe], 
["tutorial_arrows", "Arrows", [("arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, 2147483648, 0, weight(3.000000)|abundance(160)|weapon_length(95)|max_ammo(20)|thrust_damage(0, pierce), imodbits_missile], 
["tutorial_bolts", "Bolts", [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", 3458768911867052032)], itp_type_bolts, 1879048192, 0, weight(2.250000)|abundance(90)|weapon_length(55)|max_ammo(18)|thrust_damage(0, pierce), imodbits_missile], 
["tutorial_short_bow", "Short_Bow", [("short_bow", 0), ("short_bow_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, 5905584128, 0, weight(1.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(98)|shoot_speed(49)|max_ammo(0)|thrust_damage(12, pierce)|weapon_length(0), imodbits_bow], 
["tutorial_crossbow", "Crossbow", [("crossbow", 0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, 5637160960, 0, weight(3.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(42)|shoot_speed(68)|max_ammo(1)|thrust_damage(32, pierce)|weapon_length(0), imodbits_crossbow], 
["tutorial_throwing_daggers", "Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, 131072, 0, weight(3.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(102)|shoot_speed(25)|max_ammo(14)|thrust_damage(16, cut)|weapon_length(0), imodbits_missile], 
["tutorial_saddle_horse", "Saddle_Horse", [("saddle_horse", 0)], itp_type_horse, 0, 0, weight(0.000000)|abundance(90)|difficulty(0)|hit_points(0)|body_armor(3)|horse_speed(40)|horse_maneuver(38)|horse_charge(8)|horse_scale(0), imodbits_horse_basic], 
["tutorial_shield", "Kite_Shield", [("shield_kite_a", 0)], itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 118, weight(2.500000)|abundance(100)|difficulty(0)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(150), imodbits_shield, [shield_hit_point_trigger]], 
["tutorial_staff_no_attack", "Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, 4222129214062592, 9, weight(3.500000)|abundance(100)|difficulty(0)|weapon_length(115)|spd_rtng(120)|swing_damage(0, blunt)|thrust_damage(0, blunt), imodbits_none], 
["tutorial_staff", "Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, 4222129415393024, 9, weight(3.500000)|abundance(100)|difficulty(0)|weapon_length(115)|spd_rtng(120)|swing_damage(16, blunt)|thrust_damage(16, blunt), imodbits_none], 
["tutorial_sword", "Sword", [("long_sword", 0), ("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, 9223388564182532111, 0, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(102)|spd_rtng(100)|swing_damage(18, cut)|thrust_damage(15, pierce), imodbits_sword], 
["tutorial_axe", "Axe", [("iron_ax", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 9223635923965575392, 0, weight(4.000000)|abundance(100)|difficulty(0)|weapon_length(108)|spd_rtng(91)|swing_damage(19, cut)|thrust_damage(0, pierce), imodbits_axe], 

["tutorial_dagger", "Dagger", [("practice_dagger", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, 9223388529554358287, 3, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(40)|spd_rtng(103)|swing_damage(16, blunt)|thrust_damage(10, blunt), imodbits_none], 


["horse_meat", "Horse_Meat", [("raw_meat", 0)], itp_type_goods|itp_food|itp_consumable, 0, 12, weight(40.000000)|abundance(100)|max_ammo(40)|food_quality(30), imodbits_none], 
# Items before this point are hardwired and their order should not be changed!




#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************



#PRACTICE ITEM
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["practice_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["practice_sword", "Practice_Sword", [("practice_sword", 0)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary, 9223388529554358287, 3, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(90)|spd_rtng(103)|swing_damage(22, blunt)|thrust_damage(20, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["heavy_practice_sword", "Heavy_Practice_Sword", [("heavy_practicesword", 0)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary, 9223635919737716976, 21, weight(6.250000)|abundance(100)|difficulty(0)|weapon_length(128)|spd_rtng(94)|swing_damage(30, blunt)|thrust_damage(24, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["practice_dagger", "Practice_Dagger", [("practice_dagger", 0)], itp_type_one_handed_wpn|itp_no_parry|itp_wooden_attack|itp_primary|itp_secondary, 9223372037685248015, 2, weight(0.500000)|abundance(100)|difficulty(0)|weapon_length(47)|spd_rtng(110)|swing_damage(16, blunt)|thrust_damage(14, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["practice_axe", "Practice_Axe", [("hatchet", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, 9223388530091229198, 24, weight(2.000000)|abundance(100)|difficulty(0)|weapon_length(75)|spd_rtng(95)|swing_damage(24, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["arena_axe", "Axe", [("arena_axe", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, 9223388530091229198, 137, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(69)|spd_rtng(100)|swing_damage(24, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["arena_sword", "Sword", [("arena_sword_one_handed", 0), ("sword_medieval_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, 9223388564182532111, 243, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(95)|spd_rtng(99)|swing_damage(22, blunt)|thrust_damage(20, blunt), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["arena_sword_two_handed", "Two_Handed_Sword", [("arena_sword_two_handed", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, 9223635924301119728, 670, weight(2.750000)|abundance(100)|difficulty(0)|weapon_length(110)|spd_rtng(93)|swing_damage(30, blunt)|thrust_damage(24, blunt), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["arena_lance", "Lance", [("arena_lance", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head, 4222131026005760, 90, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(150)|spd_rtng(96)|swing_damage(20, blunt)|thrust_damage(25, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 
["practice_staff", "Practice_Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, 4222129415393024, 9, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(118)|spd_rtng(103)|swing_damage(18, blunt)|thrust_damage(18, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["practice_lance", "Practice_Lance", [("joust_of_peace", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head, 201326848, 18, weight(4.250000)|abundance(100)|difficulty(0)|weapon_length(240)|spd_rtng(58)|swing_damage(0, blunt)|thrust_damage(15, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["practice_shield", "Practice_Shield", [("shield_round_a", 0)], itp_type_shield|itp_wooden_parry, 5100273664, 20, weight(3.500000)|abundance(100)|difficulty(0)|hit_points(200)|body_armor(1)|spd_rtng(100)|shield_width(50), imodbits_none, [shield_hit_point_trigger]], 
["practice_bow", "Practice_Bow", [("hunting_bow", 0), ("hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, 5905584128, 0, weight(1.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(90)|shoot_speed(40)|max_ammo(0)|thrust_damage(21, blunt)|weapon_length(0), imodbits_bow], 
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
["practice_crossbow", "Practice_Crossbow", [("crossbow_a", 0)], itp_type_crossbow|itp_two_handed|itp_primary, 5637160960, 0, weight(3.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(42)|shoot_speed(68)|max_ammo(1)|thrust_damage(32, blunt)|weapon_length(0), imodbits_crossbow], 
["practice_javelin", "Practice_Javelins", [("javelin", 0), ("javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_primary|itp_civilian|itp_next_item_as_melee, 36507484160, 0, weight(5.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(91)|shoot_speed(28)|max_ammo(50)|thrust_damage(27, blunt)|weapon_length(75), imodbits_thrown], 
["practice_javelin_melee", "practice_javelin_melee", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield, 4222124851990272, 0, weight(1.000000)|abundance(100)|difficulty(0)|weapon_length(75)|spd_rtng(91)|swing_damage(12, blunt)|thrust_damage(14, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 
["practice_throwing_daggers", "Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, 131072, 0, weight(3.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(102)|shoot_speed(25)|max_ammo(10)|thrust_damage(16, blunt)|weapon_length(0), imodbits_thrown], 
["practice_throwing_daggers_100_amount", "Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, 131072, 0, weight(3.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(102)|shoot_speed(25)|max_ammo(100)|thrust_damage(16, blunt)|weapon_length(0), imodbits_thrown], 
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
["practice_horse", "Practice_Horse", [("saddle_horse", 0)], itp_type_horse, 0, 37, weight(0.000000)|abundance(100)|difficulty(0)|hit_points(0)|body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14)|horse_scale(0), imodbits_none], 
["practice_arrows", "Practice_Arrows", [("arena_arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, 2147483648, 0, weight(1.500000)|abundance(100)|weapon_length(95)|max_ammo(80)|thrust_damage(0, cut), imodbits_missile], 
["practice_bolts", "Practice_Bolts", [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", 3458768911867052032)], itp_type_bolts, 1879048192, 0, weight(2.250000)|abundance(100)|weapon_length(55)|max_ammo(49)|thrust_damage(0, cut), imodbits_missile], 
["practice_arrows_10_amount", "Practice_Arrows", [("arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, 2147483648, 0, weight(1.500000)|abundance(100)|weapon_length(95)|max_ammo(10)|thrust_damage(0, cut), imodbits_missile], 
["practice_arrows_100_amount", "Practice_Arrows", [("arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, 2147483648, 0, weight(1.500000)|abundance(100)|weapon_length(95)|max_ammo(100)|thrust_damage(0, cut), imodbits_missile], 
["practice_bolts_9_amount", "Practice_Bolts", [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", 3458768911867052032)], itp_type_bolts, 1879048192, 0, weight(2.250000)|abundance(100)|weapon_length(55)|max_ammo(9)|thrust_damage(0, cut), imodbits_missile], 


#######ARENA SHIELD#########
["arena_shield_red", "Shield", [("arena_shield_red", 0)], itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 42, weight(2.000000)|abundance(100)|difficulty(0)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60), imodbits_shield, [shield_hit_point_trigger]], 
["arena_shield_blue", "Shield", [("arena_shield_blue", 0)], itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 42, weight(2.000000)|abundance(100)|difficulty(0)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60), imodbits_shield, [shield_hit_point_trigger]], 
["arena_shield_green", "Shield", [("arena_shield_green", 0)], itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 42, weight(2.000000)|abundance(100)|difficulty(0)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60), imodbits_shield, [shield_hit_point_trigger]], 
["arena_shield_yellow", "Shield", [("arena_shield_yellow", 0)], itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 42, weight(2.000000)|abundance(100)|difficulty(0)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(60), imodbits_shield, [shield_hit_point_trigger]], 


#######ARENA HELMET#########
["red_tourney_helmet", "Red_Tourney_Helmet", [("flattop_helmet", 0)], itp_type_head_armor, 0, 126, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_none], 
["blue_tourney_helmet", "Blue_Tourney_Helmet", [("segmented_helm", 0)], itp_type_head_armor, 0, 126, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_none], 
["green_tourney_helmet", "Green_Tourney_Helmet", [("hood_c", 0)], itp_type_head_armor, 0, 126, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_none], 
["gold_tourney_helmet", "Gold_Tourney_Helmet", [("hood_a", 0)], itp_type_head_armor, 0, 126, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_none], 
["arena_helmet_red", "Arena_Helmet_Red", [("arena_helmetR", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_helmet_blue", "Arena_Helmet_Blue", [("arena_helmetB", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_helmet_green", "Arena_Helmet_Green", [("arena_helmetG", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_helmet_yellow", "Arena_Helmet_Yellow", [("arena_helmetY", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["steppe_helmet_white", "Steppe_Helmet_White", [("steppe_helmetW", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate], 
["steppe_helmet_red", "Steppe_Helmet_Red", [("steppe_helmetR", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate], 
["steppe_helmet_blue", "Steppe_Helmet_Blue", [("steppe_helmetB", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate], 
["steppe_helmet_green", "Steppe_Helmet_Green", [("steppe_helmetG", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate], 
["steppe_helmet_yellow", "Steppe_Helmet_Yellow", [("steppe_helmetY", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate], 
["tourney_helm_white", "Tourney_Helm_White", [("tourney_helmR", 0)], itp_type_head_armor|itp_covers_head, 0, 760, weight(2.750000)|abundance(100)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["tourney_helm_red", "Tourney_Helm_Red", [("tourney_helmR", 0)], itp_type_head_armor|itp_covers_head, 0, 760, weight(2.750000)|abundance(100)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["tourney_helm_blue", "Tourney_Helm_Blue", [("tourney_helmB", 0)], itp_type_head_armor|itp_covers_head, 0, 760, weight(2.750000)|abundance(100)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["tourney_helm_green", "Tourney_Helm_Green", [("tourney_helmG", 0)], itp_type_head_armor|itp_covers_head, 0, 760, weight(2.750000)|abundance(100)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["tourney_helm_yellow", "Tourney_Helm_Yellow", [("tourney_helmY", 0)], itp_type_head_armor|itp_covers_head, 0, 760, weight(2.750000)|abundance(100)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_turban_red", "Arena_Turban", [("tuareg_open", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_turban_blue", "Arena_Turban", [("tuareg_open", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_turban_green", "Arena_Turban", [("tuareg_open", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["arena_turban_yellow", "Arena_Turban", [("tuareg_open", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 187, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 


#######ARENA ARMOR#########
["red_tourney_armor", "Red_Tourney_Armor", [("tourn_armor_a", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 152, weight(15.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(6), imodbits_none], 
["blue_tourney_armor", "Blue_Tourney_Armor", [("mail_shirt", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 152, weight(15.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(6), imodbits_none], 
["green_tourney_armor", "Green_Tourney_Armor", [("leather_vest", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 152, weight(15.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(6), imodbits_none], 
["gold_tourney_armor", "Gold_Tourney_Armor", [("padded_armor", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 152, weight(15.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(6), imodbits_none], 
["arena_armor_white", "Arena_Armor_White", [("arena_armorW_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 650, weight(16.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor], 
["arena_armor_red", "Arena_Armor_Red", [("arena_armorR_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 650, weight(16.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor], 
["arena_armor_blue", "Arena_Armor_Blue", [("arena_armorB_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 650, weight(16.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor], 
["arena_armor_green", "Arena_Armor_Green", [("arena_armorG_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 650, weight(16.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor], 
["arena_armor_yellow", "Arena_Armor_Yellow", [("arena_armorY_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 650, weight(16.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor], 
["arena_tunic_white", "Arena_Tunic_White_", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 47, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], 
["arena_tunic_red", "Arena_Tunic_Red", [("arena_tunicR_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 27, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], 
["arena_tunic_blue", "Arena_Tunic_Blue", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 27, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], 
["arena_tunic_green", "Arena_Tunic_Green", [("arena_tunicG_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 27, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], 
["arena_tunic_yellow", "Arena_Tunic_Yellow", [("arena_tunicY_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 27, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth], 
#headwear


#######ARENA BOOT#########
["practice_boots", "Practice_Boots", [("boot_nomad_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_civilian|itp_next_item_as_melee, 0, 11, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth], 


#######TUTORIAL SWORD#########
["tutorial_sword", "Sword", [("long_sword", 0), ("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, 9223388564182532111, 0, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(102)|spd_rtng(100)|swing_damage(18, cut)|thrust_damage(15, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["tutorial_axe", "Axe", [("iron_ax", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 9223635923965575392, 0, weight(4.000000)|abundance(100)|difficulty(0)|weapon_length(108)|spd_rtng(91)|swing_damage(19, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["tutorial_spear", "Spear", [("spear", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield, 4222124851986688, 0, weight(4.500000)|abundance(100)|difficulty(0)|weapon_length(158)|spd_rtng(80)|swing_damage(0, cut)|thrust_damage(19, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["tutorial_club", "Club", [("club", 0)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary, 9223388529554358286, 0, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(95)|spd_rtng(95)|swing_damage(11, blunt)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["tutorial_battle_axe", "Battle_Axe", [("battle_ax", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 9223635923965575392, 0, weight(5.000000)|abundance(100)|difficulty(0)|weapon_length(108)|spd_rtng(88)|swing_damage(27, cut)|thrust_damage(0, pierce), imodbits_axe], 
["tutorial_arrows", "Arrows", [("arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, 2147483648, 0, weight(3.000000)|abundance(160)|weapon_length(95)|max_ammo(20)|thrust_damage(0, pierce), imodbits_missile], 
["tutorial_bolts", "Bolts", [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", 3458768911867052032)], itp_type_bolts, 1879048192, 0, weight(2.250000)|abundance(90)|weapon_length(63)|max_ammo(18)|thrust_damage(0, pierce), imodbits_missile], 
["tutorial_short_bow", "Short_Bow", [("short_bow", 0), ("short_bow_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, 5905584128, 0, weight(1.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(98)|shoot_speed(49)|max_ammo(0)|thrust_damage(12, pierce)|weapon_length(0), imodbits_bow], 
["tutorial_crossbow", "Crossbow", [("crossbow_a", 0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, 5637160960, 0, weight(3.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(42)|shoot_speed(68)|max_ammo(1)|thrust_damage(32, pierce)|weapon_length(0), imodbits_crossbow], 
["tutorial_throwing_daggers", "Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, 131072, 0, weight(3.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(102)|shoot_speed(25)|max_ammo(14)|thrust_damage(16, cut)|weapon_length(0), imodbits_missile], 
["tutorial_saddle_horse", "Saddle_Horse", [("saddle_horse", 0)], itp_type_horse, 0, 481, weight(0.000000)|abundance(90)|difficulty(1)|hit_points(130)|body_armor(14)|horse_speed(39)|horse_maneuver(36)|horse_charge(8)|horse_scale(0), imodbits_horse_basic], 
["tutorial_shield", "Kite_Shield", [("shield_kite_a", 0)], itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 118, weight(2.500000)|abundance(100)|difficulty(0)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(150), imodbits_shield, [shield_hit_point_trigger]], 
["tutorial_staff_no_attack", "Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, 4222129214062592, 9, weight(3.500000)|abundance(100)|difficulty(0)|weapon_length(115)|spd_rtng(120)|swing_damage(0, blunt)|thrust_damage(0, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["tutorial_staff", "Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, 4222129415393024, 9, weight(3.500000)|abundance(100)|difficulty(0)|weapon_length(115)|spd_rtng(120)|swing_damage(16, blunt)|thrust_damage(16, blunt), imodbits_none, [weapon_visual_effect_trigger]], 




#BOOK
#_______________________________________________________________________________________________________________________________________________________________________________
#A treatise on The Method of Mechanical Theorems Archimedes
 ["book_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######READABLE BOOK#########
#Native Books
#This book must be at the beginning of readable books
["book_tactics", "De_Re_Militari", [("book_a", 0)], itp_type_book, 0, 4000, weight(2.000000)|abundance(100), imodbits_none], 
["book_persuasion", "Rhetorica_ad_Herennium", [("book_b", 0)], itp_type_book, 0, 5000, weight(2.000000)|abundance(100), imodbits_none], 
["book_leadership", "The_Life_of_Alixenus_the_Great", [("book_d", 0)], itp_type_book, 0, 4200, weight(2.000000)|abundance(100), imodbits_none], 
["book_intelligence", "Essays_on_Logic", [("book_e", 0)], itp_type_book, 0, 2900, weight(2.000000)|abundance(100), imodbits_none], 
["book_trade", "A_Treatise_on_the_Value_of_Things", [("book_f", 0)], itp_type_book, 0, 3100, weight(2.000000)|abundance(100), imodbits_none], 
["book_weapon_mastery", "On_the_Art_of_Fighting_with_Swords", [("book_d", 0)], itp_type_book, 0, 4200, weight(2.000000)|abundance(100), imodbits_none], 
["book_engineering", "Method_of_Mechanical_Theorems", [("book_open", 0)], itp_type_book, 0, 4000, weight(2.000000)|abundance(100), imodbits_none], 

#AoM Books
["book_necromancer_low", "Undead_Listbook", [("book_open", 0)], itp_type_book|itp_unique, 0, 4000, weight(2.000000)|abundance(1), imodbits_none], 
["book_necromancer_middle", "Book_of_necromancer", [("book_open", 0)], itp_type_book|itp_unique, 0, 8000, weight(2.000000)|abundance(1), imodbits_none], 
["book_necromancer_high", "The_record_of_Being_Sect", [("book_open", 0)], itp_type_book|itp_unique, 0, 20000, weight(2.000000)|abundance(1), imodbits_none], 


#######CARRIABLE BOOK#########
#This book must be at the beginning of reference books
["book_wound_treatment_reference", "The_Book_of_Healing", [("book_c", 0)], itp_type_book, 0, 3500, weight(2.000000)|abundance(100), imodbits_none], 
["book_training_reference", "Manual_of_Arms", [("book_open", 0)], itp_type_book, 0, 3500, weight(2.000000)|abundance(100), imodbits_none], 
["book_surgery_reference", "The_Great_Book_of_Surgery", [("book_c", 0)], itp_type_book, 0, 3500, weight(2.000000)|abundance(100), imodbits_none], 




#GOOD
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["good_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######GOOD#########
#first one must be spice.
["spice", "Spice", [("spice_sack", 0)], itp_type_goods|itp_merchandise|itp_consumable, 0, 880, weight(40.000000)|abundance(25)|max_ammo(50)|food_quality(0), imodbits_none], 
["salt", "Salt", [("salt_sack", 0)], itp_type_goods|itp_merchandise, 0, 255, weight(50.000000)|abundance(120)|max_ammo(0)|food_quality(0), imodbits_none], 


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

 ["oil", "Oil", [("oil", 0)], itp_type_goods|itp_merchandise|itp_consumable, 0, 450, weight(50.000000)|abundance(60)|max_ammo(50)|food_quality(0), imodbits_none], 
 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],
 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],
 
 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],


#######FOOD#########
#Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
# Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],


#********
#Note that the order of various products, books, and food has been slightly adjusted here. If there are any problems in these areas in the future, remember to go to the constant to check if the beginning and end of these items are set accurately.



#ARMOR
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["armor_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######SEPCIAL SUIT#########
["vacuum_oath_armor", "Vacuum Oath Armor", #无誓板甲
   [("Black_Knight_player", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_unique, 0, 150000, 
   weight(31)|abundance(1)|difficulty(18)|head_armor(23)|body_armor(128)|leg_armor(75), 
   imodbits_good|imodbit_well_made|imodbit_superb|imodbit_lordly], 


#######POWELL ARMOR#########
#Milita Armors
["hongbai_pingmingyi", "hongbai_pingmingyi", [("cloth_orn_163", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 40, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(24)|leg_armor(14), imodbits_cloth], 
["hongbai_pingmingfu", "hongbai_pingmingfu", [("cloth_orn_164", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 40, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(24)|leg_armor(14), imodbits_cloth], 
["dahong_pingming_fu", "dahong_pingming_fu", [("cloth_orn_104", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 40, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(24)|leg_armor(14), imodbits_cloth], 
["honghuang_pingmingfu", "honghuang_pingmingfu", [("cloth_orn_114", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 40, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(24)|leg_armor(14), imodbits_cloth], 
["hongse_dianchengjia", "hongse_dianchengjia", [("padded_mtw_62", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(16), imodbits_cloth], 
["wangguo_mingbin_mianjia", "wangguo_mingbin_mianjia", [("padded_orn_172", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_cloth], 
["zonghong_mianjia", "zonghong_mianjia", [("padded_orn_173", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_cloth], 
["zonghong_diancheng_jia", "zonghong_diancheng_jia", [("padded_orn_174", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_cloth], 
["hongse_dianchengpao", "hongse_dianchengpao", [("padded_orn_171", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 467, weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(30), imodbits_cloth], 

#Soldier Armors
["wangguobubing_jia", "wangguobubing_jia", [("gambeson_7", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 690, weight(13.000000)|abundance(90)|difficulty(0)|head_armor(0)|body_armor(46)|leg_armor(24), imodbits_armor], 
["shububing_jia", "shububing_jia", [("powell_cuirass", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1872, weight(20.000000)|abundance(40)|difficulty(10)|head_armor(0)|body_armor(58)|leg_armor(37), imodbits_armor], 
["wangguo_sheshoulianjia", "wangguo_sheshoulianjia", [("ar_rho_t4_mailshirt_d", 0), ("ar_rho_t4_mailshirt_d.1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2725, weight(20.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(58)|leg_armor(42), imodbits_armor], 
["shicong_lianjiapao", "shicong_lianjiapao", [("ar_swa_t4_captain_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2642, weight(21.000000)|abundance(30)|difficulty(11)|head_armor(0)|body_armor(58)|leg_armor(45), imodbits_armor], 
["priest_chain_armor", "Priest Chain Armor", [("ibelin_surcoat_mail_a", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3562, weight(22.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor], 
["shidun_lianjiazhaopao", "shidun_lianjiazhaopao", [("surcoat_bur_141", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["red_chain_short_surcoat", "Red Chain Short Surcoat", [("andalusian_knight", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(63)|leg_armor(36), imodbits_armor], 
["puweier_lianjia", "puweier_lianjia", [("armor_24", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4062, weight(25.000000)|abundance(30)|difficulty(14)|head_armor(0)|body_armor(67)|leg_armor(36), imodbits_armor], 
["huali_hongselianxiongjia", "huali_hongselianxiongjia", [("new_mail_and_plate", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5563, weight(22.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(42), imodbits_armor], 
["light_mail_and_plate", "Light_Mail_and_Plate", [("light_mail_and_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5823, weight(22.500000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(50), imodbits_armor], 

#罗德里格斯公国装备
["dolphin_chest_armor", "Dolphin Chest Armor", [("breastplate_on_dolphin", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2873, weight(27.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["dolphin_chain_armor", "Dolphin Chain Armor", [("swangarde_surcoat_dolphin", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3762, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["dolphin_mail_and_plate", "Dolphin Mail and Plate", [("mail_and_plate_dolphin", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5763, weight(22.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(42), imodbits_armor], 
["dolphin_plate_chain_composite_armor", "Dolphin Plate Chain Composite Armor", [("early_transitional_blue_dolphin", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 6660, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 

#拜龙教装备
["lvlong_lianjaizhaopao", "lvlong_lianjaizhaopao", [("surcoat_mtw_71", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["dragon_worshipper_robe", "Dragon Worshipper Robe", #龙神祭装
   [("druid3", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 4853, 
   weight(22)|abundance(10)|difficulty(15)|head_armor(0)|body_armor(65)|leg_armor(53), 
   imodbits_armor], 
["dragon_attendant_light_armor", "Dragon Attendant Light Armor", #龙侍轻铁甲
   [("plate_falcon_armor_dragon_heart", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 5500, 
   weight(20)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(69)|leg_armor(30), 
   imodbits_armor], 
["dragon_worshipper_plate", "Dragon Worshipper Plate", #龙信徒板甲
   [("dragon_worshipper_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8055, 
   weight(26)|abundance(10)|difficulty(16)|head_armor(0)|body_armor(88)|leg_armor(48), 
   imodbits_armor], 
["dragon_sword_master_plate", "Dragon Sword Master Plate", #龙力大剑师板甲
   [("dragon_sword_master_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10211, 
   weight(29)|abundance(10)|difficulty(20)|head_armor(0)|body_armor(94)|leg_armor(70), 
   imodbits_armor], 

#普威尔正教装备
["puweierzhanjiao_jia", "puweierzhanjiao_jia", [("gambeson_it-eng", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 690, weight(13.000000)|abundance(90)|difficulty(0)|head_armor(0)|body_armor(46)|leg_armor(24), imodbits_armor], 
["powell_priest_plate", "Powell Priest Plate", [("powell_priest_plate", 0)], itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 9679, weight(28.000000)|abundance(10)|difficulty(18)|head_armor(3)|body_armor(91)|leg_armor(65), imodbits_armor], 
["powell_priest_plate_high", "Powell Priest Plate High", [("powell_priest_plate_high", 0)], itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 10679, weight(30.000000)|abundance(8)|difficulty(19)|head_armor(5)|body_armor(95)|leg_armor(75), imodbits_armor], 

#Knight Armors
["puweierguojiaqishi_jia", "puweierguojiaqishi_jia", [("Arponalir_lian_jia", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 6827, weight(26.000000)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(44), imodbits_armor], 
["honghuangcheng_banlian", "honghuangcheng_banlian", [("surcoat_mmx_29d", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 6360, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 
["powell_plate", "Powell Plate", #普威尔板甲
   [("plate_venezia", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9140, 
   weight(31)|abundance(30)|difficulty(18)|head_armor(1)|body_armor(92)|leg_armor(68), 
   imodbits_armor], 
["powell_light_knight_armor", "Powell Light Knight Armor", #轻普威尔骑士板甲
   [("west_man_at_arms_armor_light", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9040, 
   weight(28)|abundance(30)|difficulty(18)|head_armor(2)|body_armor(90)|leg_armor(69), 
   imodbits_armor], 
["powell_qishi_jia", "powell_qishi_jia", [("west_man_at_arms_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 9240, weight(30.000000)|abundance(30)|difficulty(18)|head_armor(2)|body_armor(93)|leg_armor(69), imodbits_armor], 
["powell_south_ligature_plate", "Powell South Ligature Plate", #普威尔南方板链复合甲
   [("vaegircuirasslate1", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7440, 
   weight(27)|abundance(30)|difficulty(16)|head_armor(0)|body_armor(80)|leg_armor(61), 
   imodbits_armor], 
["powell_patron_plate", "Powell Patron Plate", #普威尔庇护者板甲
   [("patron_plate_powell", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9613, 
   weight(31)|abundance(2)|difficulty(19)|head_armor(1)|body_armor(96)|leg_armor(71), 
   imodbits_armor], 
["powell_lifeguard_plate", "Powell Lifeguard Plate", #普威尔禁军板甲
   [("powell_lifeguard_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9370, 
   weight(29)|abundance(1)|difficulty(17)|head_armor(1)|body_armor(91)|leg_armor(68), 
   imodbits_armor], 
["powell_gorgeous_noble_plate", "Powell Gorgeous Noble Plate", #普威尔华丽贵胄板甲
   [("powell_churburg", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 11100, 
   weight(30)|abundance(10)|difficulty(18)|head_armor(2)|body_armor(93)|leg_armor(72), 
   imodbits_armor], 

#Special Armors
["holy_dragoon_armor", "Holy Dragoon Armor", [("holy_dragoon_armor", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 15660, weight(33.000000)|abundance(1)|difficulty(24)|head_armor(10)|body_armor(105)|leg_armor(88), imodbits_armor], 
["crown_knight_plate", "Crown Knight Plate", [("crown_knight_plate", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 9900, weight(31.000000)|abundance(1)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(69), imodbits_armor], 
["element_plate_chain_composite_armor", "Element Plate Chain Composite Armor", [("early_transitional_element", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 6660, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 
["elemental_ranger_plate", "Elemental Ranger Plate", [("half_plate_red", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 8210, weight(26.000000)|abundance(35)|difficulty(12)|head_armor(0)|body_armor(83)|leg_armor(37), imodbits_armor], 
["dragonblood_knight_plate", "Dragonblood Knight Plate", [("armour_targaryen_plate_B", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 9300, weight(29.000000)|abundance(10)|difficulty(17)|head_armor(1)|body_armor(91)|leg_armor(69), imodbits_armor], 
["preist_knight_plate", "Preist Knight Plate", [("milanese_Eng", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 9800, weight(29.000000)|abundance(10)|difficulty(16)|head_armor(0)|body_armor(90)|leg_armor(68), imodbits_armor], 
["sandboat_knight_plate", "Sandboat Knight Plate", [("rus_lamellar_armor_e", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 7670, weight(31.000000)|abundance(10)|difficulty(19)|head_armor(1)|body_armor(82)|leg_armor(66), imodbits_armor], 

["sedative_maid_cloth", "Sedative Maid Cloth", #镇静侍女服饰
   [("sedative_nurse_cloth", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 2432, 
   weight(3)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(2), 
   imodbits_cloth], 
["sedative_physician_cloth", "Sedative Physician Coth", #镇静医师服饰
   [("sedative_physician_cloth", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 3532, 
   weight(4)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(6), 
   imodbits_cloth], 
["sedative_chief_physician_cloth", "Sedative Chief Physician Coth", #镇静主治服饰
   [("sedative_chief_physician_cloth", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 6937, 
   weight(8)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(62)|leg_armor(31), 
   imodbits_cloth], 
["sedative_knight_plate", "Sedative Knight Plate", #镇静骑士护甲
   [("sedative_knight_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9860, 
   weight(20)|abundance(1)|difficulty(10)|head_armor(1)|body_armor(92)|leg_armor(64), 
   imodbits_plate], 

#龙孽
["dragon_abomination_body", "Dragon Abomination Body", #龙孽躯体
   [("dragonmonster_body", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_unique, 0, 9200, 
   weight(25)|abundance(1)|difficulty(25)|head_armor(37)|body_armor(82)|leg_armor(71), 
   imodbits_none], 
["dragon_abomination_body_with_armor", "Dragon Abomination Body With Armor", #覆甲龙孽躯体
   [("dragonmonster_light_armor", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_unique, 0, 11000, 
   weight(30)|abundance(1)|difficulty(28)|head_armor(39)|body_armor(101)|leg_armor(80), 
   imodbits_none], 
["dragon_abomination_heavy_armor", "Dragon Abomination Heavy Armor", #龙孽重甲
   [("dragonmonster_heavy_armor", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_unique, 0, 18000, 
   weight(38)|abundance(1)|difficulty(35)|head_armor(44)|body_armor(140)|leg_armor(93), 
   imodbits_none], 
["dragon_abomination_heavy_armor_with_wing", "Dragon Abomination Heavy Armor With Wing", #带翼龙孽重甲
   [("dragonmonster_wing", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_unique, 0, 27000, 
   weight(45)|abundance(1)|difficulty(40)|head_armor(44)|body_armor(156)|leg_armor(94), 
   imodbits_none], 

["human_dragon_body", "Human Dragon Body", #人龙躯体
   [("dragon_abomination", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_unique, 0, 17000, 
   weight(34)|abundance(1)|difficulty(30)|head_armor(71)|body_armor(101)|leg_armor(80), 
   imodbits_none], 
["human_dragon_heavy_armor", "Human Dragon Heavy Armor", #人龙重甲
   [("dragon_abomination_full_armor", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_unique, 0, 30000, 
   weight(49)|abundance(1)|difficulty(43)|head_armor(78)|body_armor(156)|leg_armor(94), 
   imodbits_none], 


#######YISHITH ARMOR#########
#精灵平民服装
["molter_cloth", "Molter Cloth", #蜕生精灵常服
   [("bakak", 0)], 
   itp_type_body_armor|itp_merchandise|itp_civilian, 0, 70, 
   weight(1.000000)|abundance(69)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(12), 
   imodbits_armor], 
["tint_elf_cloth", "Tint Elf Cloth", #浅色精灵常服
   [("mirkwood_clothes", 0)], 
   itp_type_body_armor|itp_merchandise|itp_civilian, 0, 100, 
   weight(1.000000)|abundance(69)|difficulty(0)|head_armor(0)|body_armor(19)|leg_armor(12), 
   imodbits_armor], 
["fusco_elf_cloth", "Fusco Elf Cloth", #深色精灵常服
   [("mirkwood_leather_1", 0)], 
   itp_type_body_armor|itp_merchandise|itp_civilian, 0, 100, 
   weight(1.000000)|abundance(69)|difficulty(0)|head_armor(0)|body_armor(19)|leg_armor(12), 
   imodbits_armor], 

#高精灵常服
["high_elf_suit", "High Elf Suit", #高精灵服饰
   [("drz_kaftan2", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 450, 
   weight(0.250000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(22)|leg_armor(10), 
   imodbits_armor], 

#精灵士兵通用的军装
["elf_light_leather_armor", "Elf Light Leather Armor", #精灵轻皮甲
   [("mirkwood_leather_vest", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 572, 
   weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(25)|leg_armor(10), 
   imodbits_armor], 
["elf_leather_armor", "Elf Leather Armor", #精灵皮甲
   [("mirkwood_leather", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 1113, 
   weight(4.000000)|abundance(60)|difficulty(0)|head_armor(0)|body_armor(36)|leg_armor(12), 
   imodbits_cloth], 
["elf_leather_scale_armor", "Elf Leather Scale Armor", #精灵皮鳞甲
   [("clan_leather_03", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 1798, 
   weight(7.000000)|abundance(60)|difficulty(5)|head_armor(0)|body_armor(45)|leg_armor(21), 
   imodbits_armor], 
["forest_guard_chain_armor", "Forest Guard Chain Armor", #巡林人链甲
   [("tasarim", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3330, 
   weight(18.000000)|abundance(20)|difficulty(8)|head_armor(0)|body_armor(54)|leg_armor(27), 
   imodbits_armor], 
["elf_leaf_scale_armor", "Elf Leaf Scale Armor", #精灵叶鳞甲
   [("mirkwood_light_scale", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 2103, 
   weight(9.000000)|abundance(30)|difficulty(7)|head_armor(0)|body_armor(58)|leg_armor(22), 
   imodbits_armor], 
["elf_ranger_scale_armor", "Ranger Scale Armor", #游侠鳞甲
   [("mirkwood_royal", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3227, 
   weight(11.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(65)|leg_armor(31), 
   imodbits_armor], 
["yishith_ranger_chest_armor", "Yishith Ranger Chest Armor", #伊希斯游骑兵胸甲
   [("eternal_guard", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3807, 
   weight(12.000000)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(66)|leg_armor(25), 
   imodbits_armor], 

#灵魄之树
["soul_full_elf_cloth", "Soul Full Elf Cloth", #灵魄纯血精灵常服
   [("mirkwood_noble_clothes", 0)], 
   itp_type_body_armor|itp_merchandise|itp_civilian, 0, 300, 
   weight(1.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(12), 
   imodbits_armor], 
["soul_elf_attendant_armor", "Soul Elf Attendant Armor", #灵魄精灵侍从甲
   [("mirkwood_warden_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 1758, 
   weight(6.000000)|abundance(10)|difficulty(4)|head_armor(0)|body_armor(44)|leg_armor(20), 
   imodbits_armor], 
["forestwarden_light_armor", "Forestwarden Light Armor", #灵森守护轻甲
   [("mirkwood_heavy", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 3758, 
   weight(9.000000)|abundance(5)|difficulty(8)|head_armor(0)|body_armor(64)|leg_armor(30), 
   imodbits_armor], 

["unicorn_chain_armor", "Unicorn Chain Armor", #独角兽轻链甲罩袍
   [("unicorn_maille", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3062, 
   weight(17.000000)|abundance(40)|difficulty(10)|head_armor(0)|body_armor(58)|leg_armor(40), 
   imodbits_armor], 
["spirittree_chain_armor", "Spirittree Chain Armor", #灵树链甲罩袍
   [("gondor_steward_guard", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, 
   weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 
["unicorn_ultra_light_plate_armor", "Unicorn Ultra Light Plate Armor", #独角兽超轻板甲
   [("unicorn_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8211, 
   weight(19.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(70)|leg_armor(48), 
   imodbits_armor], 

["spiritual_tree_armor", "Spiritual Tree Armor", #灵树庇佑甲
   [("lorien_palace_guard_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10211, 
   weight(15.000000)|abundance(1)|difficulty(12)|head_armor(3)|body_armor(85)|leg_armor(50), 
   imodbits_armor], 

#死亡之树
["dark_tight_leather_armor", "Dark Tight Leather Armor", #黯色紧身皮甲
   [("mirkwood_hunter", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 1100, 
   weight(3.5)|abundance(40)|difficulty(0)|head_armor(0)|body_armor(35)|leg_armor(12), 
   imodbits_cloth], 
["dark_tight_scale_armor", "Dark Tight Scale Armor", #黯色紧身链甲
   [("mirkwood_veteran_hunter", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 2200, 
   weight(6.000000)|abundance(30)|difficulty(6)|head_armor(0)|body_armor(51)|leg_armor(24), 
   imodbits_cloth], 
["dark_tight_composite_armor", "Dark Tight Composite Armor", #黯色紧身复合甲
   [("mirkwood_light_leather", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 4113, 
   weight(11.000000)|abundance(15)|difficulty(10)|head_armor(0)|body_armor(70)|leg_armor(32), 
   imodbits_cloth], 

["dark_chest_armor_shirt", "Dark Chest Armor Skirt", #黯色胸甲裙
   [("lorien_reward_chest_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 3098, 
   weight(9.000000)|abundance(15)|difficulty(7)|head_armor(0)|body_armor(76)|leg_armor(24), 
   imodbits_plate], 
["spiritrain_plate_skirt", "Spiritrain Plate Skirt", #灵雨板甲裙
   [("lorien_reward_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 9700, 
   weight(14.000000)|abundance(3)|difficulty(11)|head_armor(0)|body_armor(89)|leg_armor(45), 
   imodbits_plate], 

["root_borning_one_body", "Root Borning One Body", #根生者身体
   [("root_body", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 0, 
   weight(10)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(30), 
   imodbits_none], 

#先祖之树
["autumn_leather_armor", "Autumn Leather Armor", #秋意皮甲
   [("lorien_heavy_leather", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 1113, 
   weight(4.000000)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(36)|leg_armor(12), 
   imodbits_cloth], 
["autumn_scale_chest_armor", "Autumn Scale Chest Armor", #秋意鳞胸甲
   [("lorien_gold_scales", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 1998, 
   weight(7.000000)|abundance(25)|difficulty(5)|head_armor(0)|body_armor(48)|leg_armor(17), 
   imodbits_armor], 
["autumn_chest_armor_shirt", "Autumn Chest Armor Skirt", #秋意胸甲裙
   [("lorien_royal_chest_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 3098, 
   weight(9.000000)|abundance(15)|difficulty(7)|head_armor(0)|body_armor(70)|leg_armor(24), 
   imodbits_plate], 
["verdant_light_plate_chain_composite_armor", "Verdant Light Plate Chain Composite Armor", #青郁轻板链复合甲
   [("churburg_green2", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 5860, 
   weight(23.000000)|abundance(50)|difficulty(13)|head_armor(0)|body_armor(74)|leg_armor(47), 
   imodbits_plate], 
["wooden_plate", "Wooden Plate", #木板甲
   [("leaf_armour", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 7300, 
   weight(14.000000)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(80)|leg_armor(32), 
   imodbits_plate], 
["immortal_plate_skirt", "Immortal Plate Skirt", #永世者板甲裙
   [("lorien_royal_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs, 0, 9300, 
   weight(12.000000)|abundance(3)|difficulty(10)|head_armor(0)|body_armor(84)|leg_armor(42), 
   imodbits_plate], 

["molting_failer_body", "Molting Failer Body", #蜕生失败者身体
   [("human_apple", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 6000, 
   weight(80.000000)|abundance(1)|difficulty(20)|head_armor(160)|body_armor(70)|leg_armor(18), 
   imodbits_none], 

#生命之树
["westcoast_elf_noble_suit", "Westcoast Elf Noble Suit", #西海精灵贵族服
   [("janichareteksiz_mail", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 350, 
   weight(0.250000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(25)|leg_armor(5), 
   imodbits_armor], 
["yishith_westcoast_chain_armor", "Yishith Westcoast Chain Armor", #伊希斯西海锁甲
   [("gallic_armor_2", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2442, 
   weight(14.000000)|abundance(15)|difficulty(8)|head_armor(0)|body_armor(60)|leg_armor(33), 
   imodbits_armor], 
["spiritwind_light_plate", "Spiritwind Light Plate", #灵风轻板甲
   [("stag_plate", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8211, 
   weight(19.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(48), 
   imodbits_armor], 

#神选冠军
["selected_champion_windbreaker", "Selected Champion Windbreaker", #神选冠军风衣
   [("DELFbody1", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 30000, 
   weight(5)|abundance(1)|difficulty(8)|head_armor(28)|body_armor(105)|leg_armor(70), 
   imodbits_armor], 
["selected_champion_light_armor", "Selected Champion Light Armor", #神选冠军轻铁甲
   [("DELFbody2", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 45000, 
   weight(8)|abundance(1)|difficulty(10)|head_armor(32)|body_armor(116)|leg_armor(80), 
   imodbits_armor], 
["selected_champion_glass_armor", "Selected Champion Glass Armor", #神选冠军琉璃甲
   [("glasscuriass_m", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 60211, 
   weight(10.000000)|abundance(1)|difficulty(12)|head_armor(38)|body_armor(135)|leg_armor(90), 
   imodbits_plate], 
["selected_champion_graghite_armor", "Selected Champion Graghite Armor", #神选冠军墨钢甲
   [("elf_plate_harsess", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 70211, 
   weight(14.000000)|abundance(1)|difficulty(15)|head_armor(43)|body_armor(145)|leg_armor(100), 
   imodbits_plate], 

#伊希斯人类装备
["yixisirenlei_fu", "yixisirenlei_fu", [("armour_vale_sisterton", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, weight(6.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_cloth], 
["lvse_dianchengjia", "lvse_dianchengjia", [("padded_orn_201", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 467, weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(30), imodbits_cloth], 
["lvse_minbing_mianjia", "lvse_minbing_mianjia", [("padded_orn_204", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_cloth], 
["beifang_pijia", "beifang_pijia", [("armour_vale", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 730, weight(9.000000)|abundance(60)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(15), imodbits_cloth], 
["yixisirenlei_xiongjia", "yixisirenlei_xiongjia", [("armor_lam", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1356, weight(14.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(43)|leg_armor(26), imodbits_armor], 
["beifang_lingxiongjia", "beifang_lingxiongjia", [("armour_vale_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2505, weight(18.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(59)|leg_armor(24), imodbits_armor], 

#叛乱精灵装备
["light_ice_armor", "Light Ice Armor", #苦寒轻甲
   [("ice_knight_armor_light", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 36211, 
   weight(12)|abundance(1)|difficulty(11)|head_armor(25)|body_armor(98)|leg_armor(68), 
   imodbits_plate], 
["selected_champion_ice_armor", "Selected Champion Ice Armor", #神选冠军苦寒甲
   [("ice_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 66211, 
   weight(17)|abundance(1)|difficulty(16)|head_armor(40)|body_armor(138)|leg_armor(98), 
   imodbits_plate], 


#######STEPPE ARMOR#########
#Kouruto Therianthropy Armors
["nomad_vest", "Nomad_Vest", [("nomad_vest_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 510, weight(11.000000)|abundance(50)|difficulty(0)|head_armor(0)|body_armor(34)|leg_armor(28), imodbits_cloth], 
["khergit_guard_armor", "Khergit_Guard_Armor", [("lamellar_armor_a", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3007, weight(21.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(60)|leg_armor(34), imodbits_armor], 
["kelutuo_xilingjia", "kelutuo_xilingjia", [("steppe_dav_013", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3487, weight(24.000000)|abundance(70)|difficulty(12)|head_armor(0)|body_armor(63)|leg_armor(45), imodbits_plate], 
["kelutuo_zhajia", "kelutuo_zhajia", [("dorn_sand_snakes_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5513, weight(28.000000)|abundance(40)|difficulty(15)|head_armor(0)|body_armor(67)|leg_armor(46), imodbits_armor], 

#Kouruto Human Armors
["khergit_lady_dress", "Khergit_Lady_Dress", [("khergit_lady_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["khergit_lady_dress_b", "Khergit_Leather_Lady_Dress", [("khergit_lady_dress_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["kelutuo_pingming_fu", "kelutuo_pingming_fu", [("sar_pants", 0), ("sar_pants.1", 0), ("sar_pants.2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 193, weight(5.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(22)|leg_armor(12), imodbits_cloth], 
["sarranid_leather_armor", "Sarranid_Leather_Armor", [("sarranid_leather_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 650, weight(16.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(24), imodbits_armor], 
["kelutuo_fujun_zhajia", "kelutuo_fujun_zhajia", [("dshar_scale_d", 0), ("dshar_scale_d.1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3758, weight(25.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(55)|leg_armor(46), imodbits_armor], 
["sarranid_cavalry_robe", "Cavalry_Robe", [("arabian_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2849, weight(18.000000)|abundance(40)|difficulty(11)|head_armor(0)|body_armor(55)|leg_armor(30), imodbits_armor], 
["sarranid_mail_shirt", "Sarranid_Mail_Shirt", [("sarranian_mail_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2952, weight(19.000000)|abundance(40)|difficulty(11)|head_armor(0)|body_armor(56)|leg_armor(32), imodbits_armor], 
["mamluke_mail", "Mamluke_Mail", [("sarranid_elite_cavalary", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3800, weight(24.000000)|abundance(40)|difficulty(14)|head_armor(0)|body_armor(63)|leg_armor(55), imodbits_armor], 
["kelutuo_lianjia", "kelutuo_lianjia", [("scale_dav_021", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6564, weight(27.000000)|abundance(20)|difficulty(13)|head_armor(1)|body_armor(68)|leg_armor(45), imodbits_armor], 
["kelutuo_zhajia_pao", "kelutuo_zhajia_pao", [("scale_clov", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6377, weight(27.000000)|abundance(60)|difficulty(14)|head_armor(0)|body_armor(70)|leg_armor(47), imodbits_armor], 
["kelutuo_fujun_duizhangjia", "kelutuo_fujun_duizhangjia", [("heavy_yawshan", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7900, weight(29.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(78)|leg_armor(45), imodbits_armor], 

#Normal Kouruto Armors
["steppe_armor", "Steppe_Armor", [("lamellar_leather", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 250, weight(5.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(18), imodbits_cloth], 
["kelutuo_shense_pijia", "kelutuo_shense_pijia", [("steppe_dav_012", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2722, weight(16.000000)|abundance(50)|difficulty(9)|head_armor(0)|body_armor(48)|leg_armor(34), imodbits_cloth], 
["kelutuo_qianse_pijia", "kelutuo_qianse_pijia", [("steppe_dav_022", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2722, weight(16.000000)|abundance(50)|difficulty(9)|head_armor(0)|body_armor(48)|leg_armor(34), imodbits_plate], 
["lamellar_vest", "Lamellar_Vest", [("lamellar_vest_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1172, weight(18.000000)|abundance(100)|difficulty(7)|head_armor(0)|body_armor(49)|leg_armor(26), imodbits_cloth], 
["lamellar_vest_khergit", "Khergit_Lamellar_Vest", [("lamellar_vest_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1375, weight(18.000000)|abundance(100)|difficulty(7)|head_armor(0)|body_armor(49)|leg_armor(26), imodbits_cloth], 
["sarranid_elite_armor", "Sarranid_Elite_Armor", [("tunic_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2300, weight(21.000000)|abundance(100)|difficulty(10)|head_armor(0)|body_armor(50)|leg_armor(16), imodbits_armor], 
["khergit_elite_armor", "Khergit_Elite_Armor", [("lamellar_armor_d", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3827, weight(25.000000)|abundance(100)|difficulty(12)|head_armor(0)|body_armor(65)|leg_armor(46), imodbits_armor], 

["light_kouruto_heavy_lamellar_armor", "Light Colored Kouruto Heavy Lamellar Armor", #轻量科鲁托重型扎甲
   [("wei_xiadi_samurai_armor01", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6800, 
   weight(26)|abundance(100)|difficulty(16)|head_armor(0)|body_armor(72)|leg_armor(48), 
   imodbits_armor], 
["red_colored_kouruto_heavy_lamellar_armor", "Red Colored Kouruto Heavy Lamellar Armor", #红漆科鲁托重型扎甲
   [("wei_xiadi_samurai_armor03", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7000, 
   weight(27)|abundance(100)|difficulty(17)|head_armor(0)|body_armor(75)|leg_armor(48), 
   imodbits_armor], 
["kouruto_elite_heavy_lamellar_armor", "Kouruto Elite Heavy Lamellar Armor", #科鲁托精英重型扎甲
   [("lamellar_armor_c", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7100, 
   weight(27)|abundance(100)|difficulty(17)|head_armor(0)|body_armor(76)|leg_armor(48), 
   imodbits_armor], 
["strengthen_kouruto_heavy_lamellar_armor", "Strengthen Kouruto Heavy Lamellar Armor", #加强科鲁托重型扎甲
   [("wei_xiadi_samurai_armor02", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7200, 
   weight(28)|abundance(100)|difficulty(18)|head_armor(0)|body_armor(78)|leg_armor(48), 
   imodbits_armor], 

#Kouruto Knight Armors
["kouruto_elite_lamellar_armor", "Kouruto Elite Lamellar Armor", #科鲁托精锐扎甲
   [("dorn_immortal_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8200, 
   weight(28)|abundance(25)|difficulty(20)|head_armor(0)|body_armor(82)|leg_armor(41), 
   imodbits_armor], 
["kouruto_sword_fighter_lamellar_armor", "Kouruto Sword Fighter Lamellar Armor", #科鲁托剑斗士扎甲
   [("golden_worrior", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8800, 
   weight(30)|abundance(5)|difficulty(21)|head_armor(0)|body_armor(87)|leg_armor(44), 
   imodbits_armor], 

["watcher_sentry_lamellar_armor", "Watcher Sentry Lamellar Armor", #守望者哨兵扎甲
   [("heavy_armor_arabs_c_1", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 4491, 
   weight(25)|abundance(20)|difficulty(18)|head_armor(0)|body_armor(65)|leg_armor(35), 
   imodbits_armor], 
["watcher_knight_lamellar_plate_armor", "Watcher Knight Lamellar Plate Armor", #守望者骑士扎板甲
   [("marmont_armor_snouz", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8057, 
   weight(30)|abundance(20)|difficulty(19)|head_armor(0)|body_armor(86)|leg_armor(57), 
   imodbits_armor], 

["furnace_light_copper_armor", "Furnace Light Copper Armor", #侍炉轻铜甲
   [("dorn_guardsun_armor_light", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10000, 
   weight(32)|abundance(5)|difficulty(20)|head_armor(0)|body_armor(89)|leg_armor(61), 
   imodbits_armor], 
["furnace_copper_armor", "Furnace Copper Armor", #侍炉重铜甲
   [("dorn_guardsun_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 14000, 
   weight(35)|abundance(1)|difficulty(20)|head_armor(3)|body_armor(96)|leg_armor(61), 
   imodbits_armor], 

#Kouruto Refugee Armors
["nomad_robe", "Nomad_Robe", #浪民游牧袍
   [("nomad_robe_a", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 670, 
   weight(15.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(34)|leg_armor(17), 
   imodbits_cloth], 


#######CONFEDERATION ARMOR#########
#Slaver Armors
["westcoast_iron_ring_cotton_armor", "Westcoast Iron Ring Cotton Armor", #西海覆环棉甲
   [("broigne_shirt", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1278, 
   weight(13)|abundance(70)|difficulty(9)|head_armor(0)|body_armor(43)|leg_armor(33), 
   imodbits_armor], 
["westcoast_nailed_leather_armor", "Westcoast Nailed Leather Armor", #西海钉饰皮甲
   [("broigne_shirt_spiked_leather", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1250, 
   weight(15)|abundance(80)|difficulty(9)|head_armor(0)|body_armor(45)|leg_armor(32), 
   imodbits_armor], 
["westcoast_leather_scale_armor", "Westcoast Leather Scale Armor", #西海皮质鱼鳞甲
   [("broigne_shirt_metal_ring", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3200, 
   weight(20)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(54)|leg_armor(32), 
   imodbits_armor], 
["westcoast_leather_armed_clothing", "Westcoast Leather Armed Clothing", #西海皮质板甲衣
   [("broigne_shirt_metal_plate", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3200, 
   weight(20)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(56)|leg_armor(33), 
   imodbits_armor], 
["westcoast_covered_chain_armor_robe", "Westcoast Covered Chain Armor Robe", #西海覆板链甲罩袍
   [("broigne5", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3900, 
   weight(23)|abundance(40)|difficulty(13)|head_armor(0)|body_armor(65)|leg_armor(36), 
   imodbits_armor], 

#黑沼议事会
["phoenix_chain_armor_short_shirt", "Phoenix Chain Armor Short Shirt", #不死鸟链甲短衫
   [("imperial_leather", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3168, 
   weight(19)|abundance(20)|difficulty(10)|head_armor(0)|body_armor(55)|leg_armor(34), 
   imodbits_armor], 
["phoenix_chain_armor", "Phoenix Chain Armor", #不死鸟链甲衣
   [("royal_guard_armor", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3263, 
   weight(21)|abundance(20)|difficulty(11)|head_armor(0)|body_armor(57)|leg_armor(45), 
   imodbits_armor], 
["eagle_chain_armor", "Eagle Chain Armor", #花鹰链甲衣
   [("surcoat_mmx_042", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3263, 
   weight(21)|abundance(20)|difficulty(11)|head_armor(0)|body_armor(57)|leg_armor(45), 
   imodbits_armor], 
["phoenix_plate_chain_composite_armor", "Phoenix Plate Chain Composite Armor", #不死鸟板链复合甲
   [("surcoat_mmx_30b", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6360, 
   weight(25)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), 
   imodbits_armor], 
["marsh_flower_three_quarter_armour", "Marsh Flower Three Quarter Armour", #暗沼之花四分之三甲
   [("bnw_armour_stripes", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7433, 
   weight(24)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(81)|leg_armor(37), 
   imodbits_armor], 

#净世军
["brown_eagle_chain_armor_robe", "Brown Eagle Chain Armor Robe", #褐鹰链甲罩袍
   [("surcoat_hre_wb", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3362, 
   weight(21.5)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(60)|leg_armor(53), 
   imodbits_armor], 
["eagle_flock_chain_armor_robe", "Eagle Flock Chain Armor Robe", #鹰群链甲罩袍
   [("surcoat_mtw_61", 0)], 
   itp_type_body_armor|itp_wooden_attack|itp_covers_legs, 0, 3562, 
   weight(22)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 
["thunderwing_chain_armor_robe", "Thunderwing Chain Armor Robe", #雷翼链甲罩袍
   [("surcoat_mmx_011", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3762, 
   weight(22.5)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(62)|leg_armor(55), 
   imodbits_armor], 
["swayback_monk_breastplate", "Swayback Monk Breastplate", #破背僧胸甲
   [("swayback_monk", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 6200, 
   weight(23)|abundance(1)|difficulty(14)|head_armor(0)|body_armor(74)|leg_armor(47), 
   imodbits_armor], 

#乌之子女
["cormorant_chain_armor_robe", "Cormorant Chain Armor Robe", #鱼鹰链甲罩袍
   [("surcoat_mtw_191", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3562, 
   weight(22)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 
["bird_patterned_simple_medium_plate_chain_armor", "Bird Patterned Simple Medium Plate Chain Armor", #鸟纹简易中型板链甲
   [("transitional_plate_harness_10", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5294, 
   weight(23)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(73)|leg_armor(44), 
   imodbits_armor],
["cormorant_light_plate_chain_composite_armor", "Cormorant Light Plate Chain Composite Armor", #鱼鹰轻板链复合甲
   [("plate_mtw_203", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5860, 
   weight(23)|abundance(50)|difficulty(13)|head_armor(0)|body_armor(74)|leg_armor(47), 
   imodbits_armor], 

#贵族装备
["silver_plated_breastplate", "Silver Plated Breastplate", #镀银刻花胸甲
   [("surcoat_bur_04d", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5200, 
   weight(19)|abundance(20)|difficulty(8)|head_armor(0)|body_armor(68)|leg_armor(37), 
   imodbits_armor], 
["slaveholder_tight_chain_armor", "Slaveholder Tight Chain Armor", #奴隶主紧身链甲
   [("slave_chain_trainer", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 2812, 
   weight(9.5)|abundance(1)|difficulty(11)|head_armor(0)|body_armor(58)|leg_armor(37), 
   imodbits_armor], 
["confederation_female_cavalry_armor", "Confederation Female Cavalry Armor", #邦联女骑兵甲
   [("chainmail_skin", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 6904, 
   weight(23)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(72)|leg_armor(41), 
   imodbits_armor], 
["silver_plate_armor", "Silver Plate Armor", #白银板甲
   [("plate_armor2", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7000, 
   weight(24)|abundance(25)|difficulty(14)|head_armor(0)|body_armor(83)|leg_armor(50), 
   imodbits_armor], 
["brilliant_silver_plate_armor", "Brilliant Silver Plate Armor", #绚烂银板甲
   [("plate_silver", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8010, 
   weight(28)|abundance(25)|difficulty(15)|head_armor(0)|body_armor(82)|leg_armor(58), 
   imodbits_armor], 
["confederation_silver_carving_plate", "Confederation Silver Carving Plate", #邦联银刻板甲
   [("steel_armor", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 10000, 
   weight(29)|abundance(15)|difficulty(16)|head_armor(1)|body_armor(88)|leg_armor(52), 
   imodbits_armor], 

#Special Armors
["spotless_plate", "Spotless Plate", #无垢白板甲
   [("light_spotless_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9000, 
   weight(28)|abundance(5)|difficulty(19)|head_armor(0)|body_armor(90)|leg_armor(70), 
   imodbits_armor], 
["heavy_spotless_plate", "Heavy Spotless Plate", #重装无垢白板甲
   [("heavy_spotless_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10000, 
   weight(31)|abundance(2)|difficulty(21)|head_armor(1)|body_armor(99)|leg_armor(72), 
   imodbits_armor], 
["spotless_shadow_plate", "Spotless ShadowPlate", #无垢影板甲
   [("light_shadow_spotless_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9000, 
   weight(28)|abundance(5)|difficulty(19)|head_armor(0)|body_armor(90)|leg_armor(70), 
   imodbits_armor], 
["heavy_spotless_plate", "Heavy Spotless Plate", #重装无垢影板甲
   [("heavy_shadow_spotless_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9700, 
   weight(30)|abundance(2)|difficulty(20)|head_armor(1)|body_armor(97)|leg_armor(70), 
   imodbits_armor], 
["bloody_eagle_plate", "Bloody Eagle Plate", #血鹰板甲
   [("bloody_eagle_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9500, 
   weight(29)|abundance(1)|difficulty(20)|head_armor(1)|body_armor(4)|leg_armor(70), 
   imodbits_armor], 

["optihaze_light_armor", "Optihaze Light Armor", #光瘴轻甲
   [("valkyrie_light", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 7500, 
   weight(24)|abundance(1)|difficulty(17)|head_armor(0)|body_armor(78)|leg_armor(56), 
   imodbits_armor], 
["optihaze_heavy_armor", "Optihaze Heavy Armor", #光瘴重板甲
   [("valkyrie", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8800, 
   weight(27)|abundance(1)|difficulty(20)|head_armor(1)|body_armor(87)|leg_armor(63), 
   imodbits_armor], 

["marsh_extreme_heavy_armor", "Marsh Extreme Heavy Armor", #噩沼重板甲
   [("zhongjia_1", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10000, 
   weight(38)|abundance(1)|difficulty(22)|head_armor(3)|body_armor(98)|leg_armor(76), 
   imodbits_armor], 

#谬史
["light_armor_of_soldiers", "Light Armor of Soldiers", #士兵们的轻甲
   [("history_armor_light", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 1078, 
   weight(9)|abundance(1)|difficulty(7)|head_armor(0)|body_armor(40)|leg_armor(30), 
   imodbits_armor], 
["middle_armor_of_sergeants", "Middle Armor of Sergeants", #军士们的中甲
   [("history_armor_middle", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3778, 
   weight(18)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(47), 
   imodbits_armor], 
["heavy_armor_of_knights", "Heavy Armor of Knights", #骑士们的重甲
   [("history_armor_heavy", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 7278, 
   weight(26)|abundance(1)|difficulty(17)|head_armor(1)|body_armor(82)|leg_armor(60), 
   imodbits_plate], 


#######PAPAL ARMOR#########
#民用服装
["papal_noble_robe", "Papal Noble Robe", #教国贵族长袍
   [("cloth_orn_191", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 40, 
   weight(5.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(28)|leg_armor(15), 
   imodbits_cloth], 
["pilgrim_disguise", "Pilgrim Disguise", #朝圣者服
   [("pilgrim_outfit", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 35, 
   weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(31)|leg_armor(18), 
   imodbits_cloth], 
["nun_cloth", "nun_cloth", #修女服
   [("lady_dress_amazon", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 200, 
   weight(5.000000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(20), 
   imodbits_cloth], 
["friar_robe", "Friar Robe", #修士罩袍
   [("teu_black_surcoat", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 450, 
   weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(35)|leg_armor(32), 
   imodbits_armor], 

#杂兵装备
["papal_conscript_cotton_armor", "Papal Conscript Cotton Armor", #教国征召兵棉甲
   [("teu_sergeant_padded", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 540, 
   weight(7.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(35)|leg_armor(20), 
   imodbits_armor], 
["papal_refined_cotton_armor", "Papal Refined Cotton Armor", #教国精制棉甲
   [("tabard_hospitaller", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0, 650, 
   weight(8.000000)|abundance(40)|difficulty(8)|head_armor(0)|body_armor(38)|leg_armor(20), 
   imodbits_cloth], 
["friar_cotton_armor", "Friar Cotton Armor", #修士棉甲
   [("genoa_padded_a", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 450, 
   weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), 
   imodbits_armor], 
["traveling_friar_cloth", "Traveling Friar Cloth", #云游修士外衣
   [("surgeon", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 1725, 
   weight(8.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(26), 
   imodbits_cloth], 
["papal_chest_armor", "Papal Chest Armor", #教国胸甲
   [("breastplate_on_papal", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2873, 
   weight(27.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), 
   imodbits_armor], 
["papal_red_chain_cotton_armor", "Papal Red Chain  Cotton Armor", #教国红链甲棉袍
   [("hospitaller_gambeson_b", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3037, 
   weight(19.000000)|abundance(50)|difficulty(10)|head_armor(0)|body_armor(53)|leg_armor(34), 
   imodbits_armor], 
["papal_black_chain_cotton_armor", "Papal Black Chain  Cotton Armor", #教国黑链甲棉袍
   [("hospitaller_gambeson_a", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3037, 
   weight(19.000000)|abundance(50)|difficulty(10)|head_armor(0)|body_armor(53)|leg_armor(34), 
   imodbits_armor], 
["papal_red_light_chain_armor", "Papal Red Light Chain Armor", #教国红色轻链甲
   [("genoa_mail_b", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 3400, 
   weight(21.000000)|abundance(40)|difficulty(11)|head_armor(0)|body_armor(60)|leg_armor(32), 
   imodbits_armor], 
["papal_red_white_light_chain_armor", "Papal Red White Light Chain Armor", #教国红白轻链甲
   [("genoa_mail_c", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise|itp_covers_legs, 0, 3400, 
   weight(21.000000)|abundance(40)|difficulty(11)|head_armor(0)|body_armor(60)|leg_armor(32), 
   imodbits_armor], 

#驱魔师装备
["exorcist_leather_armor", "Exorcist Leather Armor", #驱魔师皮甲
   [("nightswatch", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 1650, 
   weight(8)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(32), 
   imodbits_armor], 
["exorcist_strengthening_chest_armor", "Exorcist Strengthening Chest Armor", #驱魔师补强胸甲
   [("drow_elite_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3000, 
   weight(15)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(57)|leg_armor(32), 
   imodbits_armor], 


#后备军装备
["papal_trainee_leather_armor", "Papal Trainee Leather Armor", #教国习武者皮甲
   [("armor_35", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_merchandise, 0, 878, 
   weight(12.000000)|abundance(40)|difficulty(9)|head_armor(0)|body_armor(48)|leg_armor(32), 
   imodbits_cloth], 
["papal_trainee_heavy_armor", "Papal Trainee Heavy Armor", #教国习武者重甲
   [("coat_of_plates_aa", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4350, 
   weight(17.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(65)|leg_armor(45), 
   imodbits_armor], 

#教会学校以及教会人员制服
["theology_student_cloth", "Theology Student Cloth", #神学生服装
   [("priest_1", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 725, 
   weight(8)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(28), 
   imodbits_cloth], 
["apprentice_priest_robe", "Apprentice Priest Robe", #见习神官罩袍
   [("priest_2", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 1125, 
   weight(12.000000)|abundance(20)|difficulty(10)|head_armor(0)|body_armor(45)|leg_armor(38), 
   imodbits_cloth], 

#教会神官装备
["priest_robe", "Priest Robe", #神官罩袍
   [("priest_2_1", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 1645, 
   weight(15)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(48)|leg_armor(38), 
   imodbits_cloth], 
["sword_pairing_friar_chain_armor", "Sword_pairing Friar Chain Armor", #佩剑修士链甲罩袍
   [("rnd_surcoat_21", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 3562, 
   weight(22)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 
["bishop_robe_armor", "Bishop Robe Armor", #主教圣袍铠
   [("bishop", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 8310, 
   weight(25)|abundance(1)|difficulty(13)|head_armor(0)|body_armor(83)|leg_armor(30), 
   imodbits_none], 
["heavy_bishop_robe_armor", "Heavy Bishop Robe Armor", #重装主教圣袍铠
   [("bishop_heavy", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9210, 
   weight(29)|abundance(1)|difficulty(16)|head_armor(1)|body_armor(91)|leg_armor(30), 
   imodbits_none], 

#圣教军团装备
["papal_soldier_chain_armor", "Papal Soldier Chain Armor", #教国士兵链甲罩袍
   [("teu_brother_surcoat_d", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 3562, 
   weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), 
   imodbits_armor], 
["well-painted_papal_chain_armor", "Well-painted Papal Chain Armor", #精绘教皇国链甲罩袍
   [("teu_brother_surcoat_papal", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 3662, 
   weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(62)|leg_armor(37), 
   imodbits_armor], 
["papal_knight_chain_armor", "Papal Knight Chain Armor", #教国骑士链甲罩袍
   [("papal_knight_armor", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 3862, 
   weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(64)|leg_armor(37), 
   imodbits_armor], 
["papal_knight_strengthen_chain_armor", "Papal Knight Strengthen Chain Armor", #教国骑士加强链甲
   [("shengdian_qishi", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 4000, 
   weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(68)|leg_armor(58), 
   imodbits_armor],

#圣廷
["pontifical_knight_chain_armor", "Pontifical Knight Chain Armor", #宗座骑士链甲罩袍
   [("armor_10", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3562, 
   weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 

["godward_plate_chain_composite_armor", "Godward Plate Chain Composite Armor", #圣誓板链复合甲
   [("tiaodun_qishi", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6360, 
   weight(25.000000)|abundance(40)|difficulty(15)|head_armor(0)|body_armor(80)|leg_armor(56), 
   imodbits_armor], 

["coffin_watcher_light_armor", "Coffin Watcher Light Armor", #圣棺看守者轻胸甲
   [("templar_watcher_light_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 4975, 
   weight(24.000000)|abundance(1)|difficulty(14)|head_armor(0)|body_armor(69)|leg_armor(33), 
   imodbits_armor], 
["coffin_watcher_armor", "Coffin Watcher Armor", #圣棺看守者胸甲
   [("templar_watcher_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 5075, 
   weight(25.000000)|abundance(1)|difficulty(15)|head_armor(0)|body_armor(71)|leg_armor(33), 
   imodbits_armor], 
["church_warden_armor", "Church Warden Armor", #教堂守卫重胸甲
   [("church_warden_armor", 0)], 
   itp_type_body_armor, 0, 5775, 
   weight(26)|abundance(1)|difficulty(16)|head_armor(0)|body_armor(79)|leg_armor(33), 
   imodbits_armor], 

["paladin_aide_armor", "Paladin Aide Armor", #圣骑士侍从甲
   [("knight_surcoat_01_with-mantle", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 14400, 
   weight(26.000000)|abundance(5)|difficulty(23)|head_armor(4)|body_armor(105)|leg_armor(75), 
   imodbits_armor], 
["paladin_armor", "Paladin Armor", #圣骑士铠
   [("paladin_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 20000, 
   weight(19.000000)|abundance(1)|difficulty(16)|head_armor(20)|body_armor(140)|leg_armor(100), 
   imodbits_none], 

#证信宗
["verification_crazy_monk_armor", "Verification Crazy Monk Armor", #证信宗癫僧甲胄
   [("crazy_monk_2", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3060, 
   weight(5.5)|abundance(1)|difficulty(7)|head_armor(0)|body_armor(51)|leg_armor(29), 
   imodbits_armor], 

["heresy_hunter_armor", "Heresy Hunter Armor", #异端猎手轻链甲
   [("heresy_hunter_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3200, 
   weight(9.000000)|abundance(1)|difficulty(5)|head_armor(0)|body_armor(53)|leg_armor(35), 
   imodbits_armor], 
["high_heresy_hunter_armor", "High Heresy Hunter Armor", #高阶异端猎手链甲
   [("yiyuan_qishi", 0)], itp_type_body_armor|itp_covers_legs, 0, 3400, 
   weight(10.000000)|abundance(1)|difficulty(5)|head_armor(0)|body_armor(56)|leg_armor(35), 
   imodbits_armor], 

["verification_chain_armor", "Verification Chain Armor",#证信宗链甲罩袍 
   [("surcoat_over_mail_hospitaller", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, 
   weight(22)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 
["judge_chain_armor", "Judge Chain Armor", #审判官复合链甲罩袍
   [("teu_mail_long_surcoat_h", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 7062, 
   weight(25)|abundance(20)|difficulty(14)|head_armor(1)|body_armor(81)|leg_armor(59), 
   imodbits_armor], 

["reaper_light_knight_plate", "Reaper Light Knight Plate", #轻装狩魔骑士复合甲
   [("reaper_knight_light_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 6410, 
   weight(22.000000)|abundance(1)|difficulty(10)|head_armor(0)|body_armor(72)|leg_armor(20), 
   imodbits_armor], 
["reaper_knight_plate", "Reaper Knight Plate", #狩魔骑士复合甲
   [("reaper_knight_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9410, 
   weight(28.000000)|abundance(10)|difficulty(18)|head_armor(1)|body_armor(91)|leg_armor(70), 
   imodbits_armor], 
["night_eliminater_plate", "Night Eliminater Plate", #狩夜板甲
   [("night_eliminater_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 11410, 
   weight(28.500000)|abundance(1)|difficulty(20)|head_armor(1)|body_armor(94)|leg_armor(72), 
   imodbits_armor], 
["reaper_high_knight_plate", "Reaper High Knight Plate", #高阶狩魔骑士复合甲
   [("reaper_high_knight_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 12410, 
   weight(29.000000)|abundance(1)|difficulty(21)|head_armor(3)|body_armor(96)|leg_armor(75), 
   imodbits_armor], 

#真信施洗会
["armed_priest_sui", "Armed Priest Suit", #武装修士袍
   [("armed_priest_suit", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 862, 
   weight(7)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(43)|leg_armor(38), 
   imodbits_armor], 
["veteran_chian_armor", "Veteran Chian Armor", #历战链甲罩袍
   [("mail_surcoat_a_kt", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 4512, 
   weight(25)|abundance(30)|difficulty(14)|head_armor(0)|body_armor(74)|leg_armor(58), 
   imodbits_armor], 
["armed_priest_plate", "Armed Priest Plate", #武装修士板甲
   [("armed_priest_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8200, 
   weight(28.000000)|abundance(10)|difficulty(16)|head_armor(1)|body_armor(85)|leg_armor(63), 
   imodbits_armor], 
["patron_plate", "Patron Plate", #庇护者板甲
   [("patron_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9213, 
   weight(32)|abundance(5)|difficulty(19)|head_armor(2)|body_armor(100)|leg_armor(72), 
   imodbits_armor], 
["patron_high_plate", "Patron High Plate", #高阶庇护者板甲
   [("patron_high_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9913, 
   weight(35.000000)|abundance(1)|difficulty(18)|head_armor(4)|body_armor(110)|leg_armor(86), 
   imodbits_armor], 

#神哲修道宗
["arcane_nun_breastplate", "Arcane Nun Breastplate", #奥术修女胸甲
   [("arcene_nun_breastplate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 1900, 
   weight(9.000000)|abundance(1)|difficulty(11)|head_armor(0)|body_armor(51)|leg_armor(14), 
   imodbits_armor], 
["arcane_nun_armor", "Arcane Nun Armor", #奥术修女甲
   [("arcene_nun_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 4200, 
   weight(14.000000)|abundance(1)|difficulty(13)|head_armor(0)|body_armor(56)|leg_armor(38), 
   imodbits_armor], 

["deism_philosophical_student_cloth", "Deism Philosophical Student Cloth", #神哲学士服装
   [("priest_robe_white", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 725, 
   weight(8)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(28), 
   imodbits_cloth], 
["armed_theologian_chain_armor", "Armed Theologian Chain Armor", #武装神学家链甲罩袍
   [("armor_30", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3062, 
   weight(21)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(59)|leg_armor(52), 
   imodbits_armor], 
["high_theologian_chain_armor", "High Theologian Chain Armor", #重装神学家链甲罩袍
   [("armor_30_high", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 4462, 
   weight(22.5)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(70)|leg_armor(57), 
   imodbits_armor], 

["gnosis_light_plate_armor", "Gnosis Light Plate Armor", #真知轻板甲
   [("key_knight_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8713, 
   weight(26)|abundance(1)|difficulty(14)|head_armor(0)|body_armor(85)|leg_armor(63), 
   imodbits_armor], 

["arcane_light_plate", "Arcane Light Plate", #奥术轻板甲
   [("arcene_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8800, 
   weight(24)|abundance(1)|difficulty(15)|head_armor(0)|body_armor(86)|leg_armor(57), 
   imodbits_armor], 
["arcane_eilte_plate", "Arcane Eilte Plate", #奥术精锐板甲
   [("elite_arcene_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9000, 
   weight(26)|abundance(1)|difficulty(16)|head_armor(2)|body_armor(90)|leg_armor(64), 
   imodbits_armor], 

#圣别渴求者
["armord_pilgrim_outfit", "Armord Pilgrim Outfit", #武装朝圣者外套
   [("armord_pilgrim_outfit", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 280, 
   weight(5.000000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(35)|leg_armor(24), 
   imodbits_cloth], 
["crazy_monk_armor", "Crazy Monk Armor", #癫僧甲胄
   [("crazy_monk", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3020, 
   weight(5)|abundance(1)|difficulty(7)|head_armor(0)|body_armor(50)|leg_armor(29), 
   imodbits_armor], 
["sanctification_seeker_chain_armor", "Sanctification Seeker Chain Armor", #圣别渴求链甲罩袍
   [("teu_mail_long_surcoat_e", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 3562, 
   weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), 
   imodbits_armor], 
["pilgrim_plate", "Pilgrim Plate", #朝圣者板甲
   [("pilgrim_plate", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8350, 
   weight(26.000000)|abundance(10)|difficulty(18)|head_armor(0)|body_armor(84)|leg_armor(57), 
   imodbits_armor], 

["temple_guardian_plate", "Temple Guardian Plate", #圣堂守卫板甲
   [("temple_guardian", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8940, 
   weight(29.000000)|abundance(1)|difficulty(19)|head_armor(0)|body_armor(89)|leg_armor(72), 
   imodbits_armor], 
["heavy_temple_guardian_plate", "Heavy Temple Guardian Plate", #护颈圣堂守卫板甲
   [("heavy_temple_guardian", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10500, 
   weight(30.000000)|abundance(1)|difficulty(19)|head_armor(6)|body_armor(100)|leg_armor(72), 
   imodbits_armor], 

["hymn_knight_plate_robeless", "Hymn Knight Plate Robeless", #无袍圣歌骑士板甲
   [("hymn_knight_armor_without_robe", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8900, 
   weight(27.000000)|abundance(1)|difficulty(16)|head_armor(0)|body_armor(88)|leg_armor(68), 
   imodbits_armor], 
["hymn_knight_plate_armor", "Hymn Knight Plate Armor", #圣歌骑士板甲
   [("hymn_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9090, 
   weight(29.000000)|abundance(1)|difficulty(18)|head_armor(6)|body_armor(91)|leg_armor(70), 
   imodbits_armor], 
["hymn_high_knight_plate", "Hymn High Knight Plate", #高阶圣歌骑士板甲
   [("hymn_high_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9700, 
   weight(30.000000)|abundance(1)|difficulty(19)|head_armor(6)|body_armor(97)|leg_armor(72), 
   imodbits_armor], 

["butcher_red_chain_cotton_armor", "Butcher Red Chain  Cotton Armor", #屠夫红链甲棉袍
   [("papal_buchter", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 2737, 
   weight(18)|abundance(1)|difficulty(9)|head_armor(0)|body_armor(50)|leg_armor(35), 
   imodbits_armor], 
["butcher_chain_armor", "Butcher Friar Chain Armor", #屠夫链甲罩袍
   [("buchter_surcoat", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3662, 
   weight(22.25)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(63)|leg_armor(55), 
   imodbits_armor], 
["butcher_plate", "Butcher Plate", #人屠板甲
   [("butcher_temple_guardian", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9040, 
   weight(29.25)|abundance(1)|difficulty(19)|head_armor(0)|body_armor(91)|leg_armor(73), 
   imodbits_armor], 

["saintess_chain_black", "Saintess Chain Black", #圣女黑链甲
   [("saintess_chain", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 2900, 
   weight(10.000000)|abundance(5)|difficulty(11)|head_armor(0)|body_armor(60)|leg_armor(37), 
   imodbits_armor], 
["high_saintess_chain_black", "High Saintess Chain Black", #高阶圣女黑链甲
   [("saintess_chain_high", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3100, 
   weight(11.000000)|abundance(5)|difficulty(11)|head_armor(0)|body_armor(62)|leg_armor(37), 
   imodbits_armor], 
["saintess_chain_white", "Saintess Chain White", #圣女白链甲
   [("saintess_cloth", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3100, 
   weight(11.000000)|abundance(5)|difficulty(11)|head_armor(0)|body_armor(62)|leg_armor(38), 
   imodbits_armor], 
["saintess_swordman_armor", "Saintess Swordman Armor", #圣女剑客铠
   [("saintess", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 18900, 
   weight(18.000000)|abundance(1)|difficulty(16)|head_armor(0)|body_armor(124)|leg_armor(77), 
   imodbits_none], 

["heroic_incarnation_stone_carving", "Heroic Incarnation Stone Carving", #英灵受肉石刻
   [("zhanshentouying1", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 100000, 
   weight(99.000000)|abundance(1)|difficulty(60)|head_armor(4)|body_armor(200)|leg_armor(170), 
   imodbits_none], 


#######EASTERN ARMOR#########
#Jianghu People Armors
["donfangpi_jia", "donfangpi_jia", [("khergit_leather_e", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 878, weight(10.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(22), imodbits_armor], 
["zongsejiading_kai1", "zongsejiading_kai1", [("armor_1", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1378, weight(13.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(26), imodbits_armor], 
["huisejiading_kai", "huisejiading_kai", [("armor_2", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1378, weight(13.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(26), imodbits_armor], 
["linjia_pao", "linjia_pao", [("chain_tab_2", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4012, weight(20.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(53)|leg_armor(42), imodbits_armor], 
["yulin_jia", "yulin_jia", [("khergit_scale_c", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4177, weight(24.000000)|abundance(40)|difficulty(13)|head_armor(0)|body_armor(67)|leg_armor(35), imodbits_armor], 
["dongfangzhalian_jia", "dongfangzhalian_jia", [("wei_xiadi_lamellar_armor03", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, weight(24.000000)|abundance(40)|difficulty(15)|head_armor(0)|body_armor(70)|leg_armor(48), imodbits_armor], 

#Eastern Soldier Armors
["dongfanfzhenzu_jia", "dongfanfzhenzu_jia", [("ylyq_bin_pijia_hei", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 321, weight(9.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(29)|leg_armor(18), imodbits_armor], 
["tuanlian_jia", "tuanlian_jia", [("ylyq_bin_linjia_bai", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 621, weight(9.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(41)|leg_armor(18), imodbits_cloth], 
["buba_shan", "buba_shan", [("fysg_bin_shazei01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 400, weight(4.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(41)|leg_armor(22), imodbits_armor], 
["fudang", "fudang", [("wei_xiadi_nord_lamellar_purple", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1100, weight(9.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(48)|leg_armor(26), imodbits_armor], 
["tuntian_kai", "tuntian_kai", [("armor_45", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1678, weight(16.000000)|abundance(100)|difficulty(10)|head_armor(0)|body_armor(52)|leg_armor(30), imodbits_armor], 
["shediaoshou_jia", "shediaoshou_jia", [("mon_a_from12th", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3580, weight(26.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(58)|leg_armor(37), imodbits_armor], 
["dongfangchangbai_lianjai", "dongfangchangbai_lianjai", [("bubinjia", 0), ("bubinjia.2", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4278, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(63)|leg_armor(38), imodbits_armor], 
["tieyinruishi_jia", "tieyinruishi_jia", [("DaMing_armor_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6900, weight(26.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(63)|leg_armor(46), imodbits_armor], 
["paishuoruishi_jia", "paishuoruishi_jia", [("DaMing_armor_03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6900, weight(26.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(63)|leg_armor(46), imodbits_armor], 
["strange_armor", "Strange_Armor", [("samurai_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5259, weight(24.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(68)|leg_armor(39), imodbits_armor], 
["jingqi_jia", "jingqi_jia", [("ylyq_jiangjia4", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9221, weight(28.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(78)|leg_armor(58), imodbits_armor], 

#Eastern Elite Armors
["gulamu_jia", "gulamu_jia", [("copy_hongfajia", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8490, weight(28.000000)|abundance(20)|difficulty(17)|head_armor(0)|body_armor(83)|leg_armor(50), imodbits_armor], 
["heigulamnu_juzu", "heigulamnu_juzu", [("domaru_inv", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8000, weight(28.000000)|abundance(20)|difficulty(17)|head_armor(0)|body_armor(79)|leg_armor(45), imodbits_armor], 
["hongzhenyugulamu_kai", "hongzhenyugulamu_kai", [("domaru_r", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8100, weight(28.000000)|abundance(10)|difficulty(17)|head_armor(0)|body_armor(80)|leg_armor(45), imodbits_armor], 
["huangzhenyugulamu_kai", "huangzhenyugulamu_kai", [("domaru_b", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8100, weight(29.000000)|abundance(10)|difficulty(17)|head_armor(0)|body_armor(80)|leg_armor(45), imodbits_armor], 
["lanzhenyugulamu_kai", "lanzhenyugulamu_kai", [("domaru_a", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8100, weight(29.000000)|abundance(10)|difficulty(17)|head_armor(0)|body_armor(80)|leg_armor(45), imodbits_armor], 
["cangyijun_jia", "cangyijun_jia", [("new_fysg_kuijia01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7221, weight(27.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(58), imodbits_armor], 
["buyong_jia", "buyong_jia", [("tddddddddd2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8600, weight(29.000000)|abundance(20)|difficulty(18)|head_armor(0)|body_armor(86)|leg_armor(52), imodbits_armor], 
["tower_heavy_armor", "Tower Heavy Armor", [("white_walker_armor_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, weight(30.000000)|abundance(10)|difficulty(18)|head_armor(0)|body_armor(89)|leg_armor(64), imodbits_armor], 
["modao_kai", "modao_kai", [("khassakileather", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 12000, weight(27.000000)|abundance(10)|difficulty(21)|head_armor(0)|body_armor(100)|leg_armor(80), imodbits_armor], 

#Eastern Special Armors
["huanguan_pao", "huanguan_pao", [("jingyiwei04", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 420, weight(8.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(37)|leg_armor(28), imodbits_armor], 
["huanguanjianjun_jia", "huanguanjianjun_jia", [("armor_afghan_mailiii", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3850, weight(22.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(62)|leg_armor(52), imodbits_armor], 
["jiuyijun_jia", "jiuyijun_jia", [("DaMing_armor_13", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8180, weight(26.000000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(83)|leg_armor(55), imodbits_armor], 
["tielinjun_kai", "tielinjun_kai", [("fysg_bin_jia_jinxiang_03", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9558, weight(30.000000)|abundance(20)|difficulty(23)|head_armor(0)|body_armor(82)|leg_armor(58), imodbits_armor], 
["yulinjun_kai", "yulinjun_kai", [("fysg_bin_kuijia_shu02", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8500, weight(30.000000)|abundance(20)|difficulty(18)|head_armor(0)|body_armor(85)|leg_armor(62), imodbits_armor], 
["longxiang_jia", "longxiang_jia", [("fysg_bin_jia_jinxiang_04", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 10558, weight(32.000000)|abundance(20)|difficulty(21)|head_armor(0)|body_armor(85)|leg_armor(45), imodbits_armor], 
["shenwu_jia", "shenwu_jia", [("ylyq_jiangjia55", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 15000, weight(30.000000)|abundance(20)|difficulty(27)|head_armor(0)|body_armor(95)|leg_armor(75), imodbits_none], 

["eastern_light_knight_armor", "Eastern Light Knight Armor", [("eastern_knight_armor_light", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 6000, weight(16.000000)|abundance(10)|difficulty(15)|head_armor(0)|body_armor(74)|leg_armor(35), imodbits_none], 
["eastern_tianbin_armor", "Eastern Tianbin Armor", [("eastern_shenwu_armor", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 8100, weight(25.000000)|abundance(5)|difficulty(19)|head_armor(1)|body_armor(86)|leg_armor(62), imodbits_none], 
["eastern_heavy_armor", "Eastern Heavy Armor", [("eastern_heavy_armor", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 9200, weight(30.000000)|abundance(5)|difficulty(21)|head_armor(1)|body_armor(93)|leg_armor(75), imodbits_none], 
["eastern_knight_armor", "Eastern Knight Armor", [("eastern_knight_armor", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 13000, weight(27.000000)|abundance(1)|difficulty(20)|head_armor(4)|body_armor(101)|leg_armor(80), imodbits_none], 


#######STARKHOOK ARMOR#########
#Soldier Armors
["shangyeguizu_fu", "shangyeguizu_fu", [("pirate_captain_body", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 440, weight(10.000000)|abundance(50)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(16), imodbits_armor], 
["zenyijianshi_jia", "zenyijianshi_jia", [("genericpikeman_08", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, weight(20.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(70)|leg_armor(27), imodbits_armor], 
["zenyifushi_jia", "zenyifushi_jia", [("genericpikeman_02", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, weight(20.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(70)|leg_armor(27), imodbits_armor], 
["grand_duchy_captain_half_plate", "Grand Duchy Captain Half-plate", [("officer_jacket_03", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 5278, weight(20.000000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(71)|leg_armor(20), imodbits_armor], 
["lansexiongbanjia", "lansexiongbanjia", [("half_plate_fra", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7200, weight(23.000000)|abundance(40)|difficulty(13)|head_armor(0)|body_armor(78)|leg_armor(41), imodbits_armor], 

#Elite Troops Armors
["xuandoushi_jia", "xuandoushi_jia", [("cavalry_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, weight(23.000000)|abundance(35)|difficulty(16)|head_armor(0)|body_armor(77)|leg_armor(35), imodbits_armor], 
["berserker_half_body_armor", "Berserker Half Body Armor", #狂战士半身甲
   [("acb1_body", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7170, 
   weight(24)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(15), 
   imodbits_armor], 
["gongguo_banshenjia", "gongguo_banshenjia", [("cuirassier2", 0), ("cuirassier2.2", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7679, weight(24.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(89)|leg_armor(35), imodbits_armor], 
["gongguo_banshenjia2", "gongguo_banshenjia2", [("cuirassier1", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7679, weight(24.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(89)|leg_armor(35), imodbits_armor], 
["starkhook_imported_plate_armor", "Starkhook Imported Plate Armor", [("plate_venezia2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0, 9179, weight(28.000000)|abundance(30)|difficulty(18)|head_armor(0)|body_armor(90)|leg_armor(65), imodbits_armor], 

#Special Armors
["bloodhonor_armor", "Bloodhonor Armor", #血勋四分之三甲
   [("bloodhonor_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8500, 
   weight(24.5)|abundance(1)|difficulty(16)|head_armor(0)|body_armor(90)|leg_armor(48), 
   imodbits_armor], 
["scarlet_bloodhonor_armor", "Scarlet Bloodhonor Armor", #血勋猩红四分之三甲
   [("scarlet_bloodhonor_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8400, 
   weight(23.5)|abundance(1)|difficulty(15)|head_armor(0)|body_armor(87)|leg_armor(40), 
   imodbits_armor], 
["azure_bloodhonor_armor", "Azure Bloodhonor Armor", #血勋湛蓝四分之三甲
   [("wolfkinght", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9500, 
   weight(28)|abundance(1)|difficulty(18)|head_armor(1)|body_armor(93)|leg_armor(65), 
   imodbits_armor], 
["xianhongchaozhongbanjia", "xianhongchaozhongbanjia", [("zhongjia_3", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 9500, weight(33.000000)|abundance(10)|difficulty(24)|head_armor(3)|body_armor(96)|leg_armor(70), imodbits_armor], 

#Mercenary Armors
["guyongbing_jia", "guyongbing_jia", [("armour_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4827, weight(25.000000)|abundance(70)|difficulty(15)|head_armor(3)|body_armor(72)|leg_armor(35), imodbits_armor], 

#绯世
["crimson_body", "Crimson Body", #绯影身躯
   [("crimson_shadow", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(15), 
   imodbits_none], 
["blood_crow_robe", "Blood Crow Robe", #血鸦帷幔
   [("crismon_raven", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 8000, 
   weight(3)|abundance(1)|difficulty(0)|head_armor(10)|body_armor(65)|leg_armor(15), 
   imodbits_none], 
["blood_pool_weaving_chain", "Blood Pool Weaving Chain", #血池织链
   [("crimson_chainmail", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 12000, 
   weight(8)|abundance(1)|difficulty(0)|head_armor(3)|body_armor(80)|leg_armor(45), 
   imodbits_none], 
["resonant_crimson_plate", "Resonant Crimson Plate", #赤脉异铠
   [("crimson_plate_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 18000, 
   weight(14)|abundance(1)|difficulty(0)|head_armor(5)|body_armor(115)|leg_armor(85), 
   imodbits_none], 
["resonant_crimson_heavy_plate", "Resonant Crimson Heavy Plate", #赤脉重铠
   [("crimson_heavy_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 28000, 
   weight(19)|abundance(1)|difficulty(0)|head_armor(8)|body_armor(145)|leg_armor(110), 
   imodbits_none], 
["red_apostle_armor", "Red Apostle Armor", #绯世使徒铠甲
   [("red_apostle_armor", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 30000, 
   weight(29)|abundance(1)|difficulty(24)|head_armor(13)|body_armor(155)|leg_armor(115), 
   imodbits_none], 



#######STATE ARMOR#########
#Soldier Armors
["ziyouchengbanggongming_fu", "ziyouchengbanggongming_fu", [("ukr_pure_jupan_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 70, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(25)|leg_armor(12), imodbits_cloth], 
["banded_armor", "Banded_Armor", [("banded_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2716, weight(23.000000)|abundance(100)|difficulty(11)|head_armor(0)|body_armor(49)|leg_armor(33), imodbits_armor], 
["cuir_bouilli", "Cuir_Bouilli", [("cuir_bouilli_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3107, weight(23.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(56)|leg_armor(35), imodbits_armor], 
["ziyouchengbang_bibanlian", "ziyouchengbang_bibanlian", [("leather_rein_ss", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 7810, weight(26.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(84)|leg_armor(58), imodbits_armor], 
["baoleihucong_jia", "baoleihucong_jia", [("new_state_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8990, weight(30.000000)|abundance(15)|difficulty(17)|head_armor(2)|body_armor(87)|leg_armor(57), imodbits_armor], 

#Noble Armors
["hualibanshen_jia", "hualibanshen_jia", [("pol_krilatiy_gusar_b", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6679, weight(26.000000)|abundance(30)|difficulty(15)|head_armor(0)|body_armor(89)|leg_armor(35), imodbits_armor], 

["scepter_heavy_plate", "Scepter Heavy Plate", #权杖重板甲
   [("scepter_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10740, 
   weight(35)|abundance(5)|difficulty(19)|head_armor(3)|body_armor(110)|leg_armor(72), 
   imodbits_armor], 
["scepter_knight_captain_plate", "Scepter Knight Captain Plate", #权杖骑士长甲
   [("scepter_armor_captain", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 10970, 
   weight(36)|abundance(5)|difficulty(20)|head_armor(3)|body_armor(112)|leg_armor(73), 
   imodbits_armor], 
["fasces_light_plate", "Fasces Light Plate", #束杖轻甲
   [("fasces_light", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 12940, 
   weight(30)|abundance(1)|difficulty(23)|head_armor(3)|body_armor(135)|leg_armor(72), 
   imodbits_none], 
["fasces_plate", "Fasces Plate", #束杖板甲
   [("fasces_heavy", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 15010, 
   weight(34)|abundance(1)|difficulty(24)|head_armor(3)|body_armor(142)|leg_armor(73), 
   imodbits_none], 


#######UNDEAD ARMOR#########
#Necromancer Armors
["necro_apprentice_robe", "Necro Apprentice Robe", #死灵学徒长袍
   [("necro_body_01", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 1600, 
   weight(6)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(36)|leg_armor(24), 
   imodbits_cloth], 
["necro_delicate_apprentice_robe", "Necro Delicate Apprentice Robe", #精致死灵学徒长袍
   [("necro_body_02", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 1700, 
   weight(6)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(37)|leg_armor(24), 
   imodbits_cloth], 

["necro_assistant_light_armor", "Necro Assistant Light Armor", #死灵侍从轻胸甲
   [("necro_female_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3324, 
   weight(12)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(60)|leg_armor(34), 
   imodbits_armor], 
["necro_assistant_armor", "Necro Assistant Armor", #死灵侍从胸甲
   [("necro_male_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3524, 
   weight(13)|abundance(10)|difficulty(11)|head_armor(0)|body_armor(61)|leg_armor(35), 
   imodbits_armor], 
["necro_warrier_armor", "Necro Warrier Armor", #死灵巫师扎甲
   [("g_reinf_jerkin", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 7324, 
   weight(26)|abundance(10)|difficulty(16)|head_armor(0)|body_armor(78)|leg_armor(47), 
   imodbits_armor], 
["necro_knight_light_armor", "Necro Knight Light Armor", #死灵骑士轻板甲
   [("necro_female_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8324, 
   weight(25)|abundance(1)|difficulty(16)|head_armor(0)|body_armor(87)|leg_armor(57), 
   imodbits_armor], 
["necro_knight_armor", "Necro Knight Armor", #死灵骑士板甲
   [("necro_knight_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9224, 
   weight(29)|abundance(1)|difficulty(19)|head_armor(2)|body_armor(92)|leg_armor(67), 
   imodbits_armor], 

#Zombie
["jiangshishen", "jiangshishen", [("undead_body", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(0.500000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(30), imodbits_none], 
["jiangshi_zhajia", "jiangshi_zhajia", [("kuyak_a", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5972, weight(26.000000)|abundance(10)|difficulty(20)|head_armor(0)|body_armor(70)|leg_armor(40), imodbits_armor], 
["jiangshi_zhongzhajia", "jiangshi_zhongzhajia", [("kuyak_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6172, weight(27.000000)|abundance(10)|difficulty(20)|head_armor(0)|body_armor(73)|leg_armor(43), imodbits_armor], 
["lvsejiangshizhongzhajia", "lvsejiangshizhongzhajia", [("rus_lamellar_b", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6172, weight(27.000000)|abundance(10)|difficulty(20)|head_armor(0)|body_armor(73)|leg_armor(43), imodbits_armor], 
["huangsejiangshizhongzhajia", "huangsejiangshizhongzhajia", [("rus_lamellar_a", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6172, weight(27.000000)|abundance(10)|difficulty(20)|head_armor(0)|body_armor(73)|leg_armor(43), imodbits_armor], 

#Skeleton
["kulou_shenti", "kulou_shenti", [("barf_skeleton", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(2.000000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(30), imodbits_armor], 
["xiongjiakulou", "xiongjiakulou", [("barf_skeleton_armor", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6360, weight(10.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["kulou_zhanshishenti", "kulou_zhanshishenti", [("barf_skeleton_armor_3", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6360, weight(13.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(64)|leg_armor(49), imodbits_armor], 
["skeleton_plate", "Skeleton Plate", [("lich_robe1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8000, weight(28.000000)|abundance(10)|difficulty(16)|head_armor(0)|body_armor(87)|leg_armor(55), imodbits_armor], 
["skeleton_ghost", "Skeleton Ghost", [("wight_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(0.050000)|abundance(1)|difficulty(0)|head_armor(16)|body_armor(30)|leg_armor(30), imodbits_none], 

["skeleton_unburned", "skeleton_unburned", [("barf_skeleton_unburned", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(0.050000)|abundance(1)|difficulty(0)|head_armor(16)|body_armor(30)|leg_armor(30), imodbits_none], 
["skeleton_candle", "skeleton_candle", [("barf_skeleton_candle", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(0.050000)|abundance(1)|difficulty(0)|head_armor(16)|body_armor(30)|leg_armor(30), imodbits_none], 
["skeleton_blazing_thing", "skeleton_blazing_thing", [("barf_skeleton_blazing_thing", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(0.050000)|abundance(1)|difficulty(0)|head_armor(16)|body_armor(30)|leg_armor(30), imodbits_none], 
["eternalflame_unburned_plate", "eternalflame_unburned_plate", [("eternalflame_unburned_plate", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1, weight(0.050000)|abundance(1)|difficulty(0)|head_armor(16)|body_armor(30)|leg_armor(30), imodbits_none], 

#Fantom
["ghost_dress", "Ghost Dress", [("ghost_dress", 0)], itp_type_body_armor|itp_covers_legs, 0, 200, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(7), imodbits_none], 
["ghost_court_dress", "Ghost Court Dress", [("ghost_court_dress", 0)], itp_type_body_armor|itp_covers_legs, 0, 200, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(7), imodbits_none], 
["ghost_woolen_dress", "Ghost Woolen Dress", [("ghost_woolen_dress", 0)], itp_type_body_armor|itp_covers_legs, 0, 200, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(7), imodbits_none], 
["ghost_nobleman_outf", "Ghost Nobleman Outfit", [("ghost_nobleman_outf", 0)], itp_type_body_armor|itp_covers_legs, 0, 400, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(16), imodbits_none], 
["ghost_merchant_outf", "Ghost Merchant Outfit", [("ghost_merchant_outf", 0)], itp_type_body_armor|itp_covers_legs, 0, 400, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(16), imodbits_none], 
["ghost_outfit", "Ghost Outfit", [("ghost_outfit", 0)], itp_type_body_armor|itp_covers_legs, 0, 800, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(26)|leg_armor(21), imodbits_none], 
["ghost_blue_gambeson", "Ghost Blue Gambeson", [("ghost_blue_gambeson", 0)], itp_type_body_armor|itp_covers_legs, 0, 1200, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(25), imodbits_none], 
["ghost_white_gambeson", "Ghost White Gambeson", [("ghost_white_gambeson", 0)], itp_type_body_armor|itp_covers_legs, 0, 1200, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(30)|leg_armor(25), imodbits_none], 

["ghost_assassin_cloth", "Ghost Assassin Cloth", [("ghost_assassin_cloth", 0)], itp_type_body_armor|itp_covers_legs, 0, 2000, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(36)|leg_armor(18), imodbits_armor], 
["ghost_surcoat", "Ghost Surcoat", [("ghost_surcoat", 0)], itp_type_body_armor|itp_covers_legs, 0, 3000, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(38), imodbits_armor], 
["ghost_bride_dress", "Ghost Bride Dress", [("ghost_bride_dress", 0)], itp_type_body_armor|itp_covers_legs, 0, 8000, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(49)|leg_armor(27), imodbits_none], 
["death_announcer_cloak", "Death Announcer Cloak", [("death_body", 0)], itp_type_body_armor|itp_covers_legs, 0, 12000, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(16)|body_armor(64)|leg_armor(37), imodbits_none], 

#Walker
["walker_body", "Walker Body", [("zombie_body", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 1, weight(0.500000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(20), imodbits_none], 


#######DEMON ARMOR#########
#Demon Worshipper Armors
["qishi_pao2", "qishi_pao2", [("heretic_robe", 0)], itp_type_body_armor|itp_covers_legs, 0, 331, weight(5.000000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(22)|leg_armor(17), imodbits_armor], 
["qishi_pao", "qishi_pao", [("heretic_padded_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 1192, weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(42)|leg_armor(30), imodbits_armor], 
["dark_apprentice_robe", "Dark Apprentice Robe", [("demonrobe", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 1500, weight(12.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(43)|leg_armor(26), imodbits_armor], 
["qishi_pibanlianjai", "qishi_pibanlianjai", [("heretic_hard_lthr", 0)], itp_type_body_armor|itp_covers_legs, 0, 3041, weight(23.000000)|abundance(100)|difficulty(12)|head_armor(0)|body_armor(56)|leg_armor(35), imodbits_armor], 
["dark_worshipper_leather_armor", "dark_worshipper_leather_armor", [("cuir_bouilli_sp", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 3041, weight(23.000000)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(56)|leg_armor(35), imodbits_armor], 
["anhei_shushizhaopao", "anhei_shushizhaopao", [("drow_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 3269, weight(20.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(56)|leg_armor(50), imodbits_cloth], 
["qishi_pao3", "qishi_pao3", [("heretic_surcoat_over_mail", 0)], itp_type_body_armor|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 

#High Grade Armors
["dark_magician_robe", "Dark Magician Robe", [("dark_robe", 0)], itp_type_body_armor|itp_covers_legs, 0, 3000, weight(8.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(54)|leg_armor(26), imodbits_armor], 
["devilman_berserker_coat_plate", "Devilman Berserker Coat Plate", [("spak_coat_of_plates_f", 0)], itp_type_body_armor|itp_covers_legs, 0, 10004, weight(29.000000)|abundance(10)|difficulty(21)|head_armor(0)|body_armor(84)|leg_armor(44), imodbits_armor], 
["devilman_warrior_fierce_armor", "Devilman Warrior Fierce Armor", [("knight_of_tiefling", 0)], itp_type_body_armor|itp_covers_legs, 0, 12456, weight(34.000000)|abundance(1)|difficulty(23)|head_armor(2)|body_armor(109)|leg_armor(79), imodbits_armor], 
["fear_spreader_super_plate", "Fear spreader Super Plate", [("knight_of_molag_bal_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 17456, weight(40.000000)|abundance(1)|difficulty(26)|head_armor(4)|body_armor(129)|leg_armor(89), imodbits_armor], 

["demon_leather_plate", "Demon Leather Plate", [("dark_leather_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 20456, weight(3.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(100)|leg_armor(79), imodbits_armor], 
["demon_knight_plate", "Demon Knight Plate", [("dark_plate_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 22456, weight(5.000000)|abundance(1)|difficulty(0)|head_armor(2)|body_armor(119)|leg_armor(89), imodbits_armor], 
["dark_oath_plate", "Dark Oath Plate", #黑誓板甲
   [("Black_Knight", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 50000, 
   weight(34)|abundance(1)|difficulty(20)|head_armor(23)|body_armor(135)|leg_armor(95), 
   imodbits_armor], 

#魔族专用
["lemure_body", "Lemure Body", #劣魔身
   [("krag_bloodhowler_body", 0)], 
   itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_unique, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(60)|leg_armor(60), 
   imodbits_none], 


#######WITCHCRAFT ARMOR#########
["wugushushi_jia", "wugushushi_jia", [("dark_armor_low", 0)], itp_type_body_armor|itp_covers_legs, 0, 4000, weight(18.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(67)|leg_armor(38), imodbits_armor], 
["duxueqishi_jia", "duxueqishi_jia", [("dark_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 10562, weight(28.000000)|abundance(20)|difficulty(25)|head_armor(1)|body_armor(98)|leg_armor(62), imodbits_armor], 

["snake_light_armor", "Snake light Armor", [("snake_light_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 7562, weight(25.000000)|abundance(1)|difficulty(14)|head_armor(4)|body_armor(78)|leg_armor(52), imodbits_armor], 
["snake_heavy_armor", "Snake Heavy Armor", [("snake_heavy_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 10632, weight(28.000000)|abundance(1)|difficulty(19)|head_armor(4)|body_armor(93)|leg_armor(72), imodbits_armor], 


#######SABIANISM ARMOR#########
["xingting_lianjiazhaopao", "xingting_lianjiazhaopao", [("sh_harp", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0, 3662, weight(20.000000)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["stardust_light_plate_armor", "Stardust Light Plate Armor", #星屑轻板甲
   [("ar_rho_t7_milan_b", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8213, 
   weight(23)|abundance(1)|difficulty(13)|head_armor(0)|body_armor(82)|leg_armor(63), 
   imodbits_armor], 


#######ECLIPSE ARMOR#########
["coppering_plate_armor", "Coppering Plate Armor", [("Sangrail_maserainnean_plate", 0)], itp_type_body_armor|itp_covers_legs, 0, 9213, weight(31.000000)|abundance(10)|difficulty(18)|head_armor(0)|body_armor(90)|leg_armor(70), imodbits_armor], 
["coppering_noble_plate_armor", "Coppering Noble Plate Armor", [("Sangrail_maserainnean_plate_1", 0)], itp_type_body_armor|itp_covers_legs, 0, 9813, weight(32.000000)|abundance(1)|difficulty(19)|head_armor(0)|body_armor(92)|leg_armor(70), imodbits_armor], 


#######ABYSS ARMOR#########
["abyss_plate_robe", "Abyss Plate Robe", #深潜板甲袍
   [("abyss_plate_robe", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8600, 
   weight(28.5)|abundance(5)|difficulty(17)|head_armor(0)|body_armor(86)|leg_armor(42), 
   imodbits_armor], 
["abyss_plate", "Abyss Plate", #深潜板甲
   [("abyss_plate", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 9500, 
   weight(30)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(93)|leg_armor(69), 
   imodbits_armor], 
["deep_binder_plate", "Deep Binder Plate", #深邃封印者板甲
   [("abyss_plate_fat", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 12500, 
   weight(40)|abundance(1)|difficulty(24)|head_armor(0)|body_armor(128)|leg_armor(47), 
   imodbits_armor], 


#######LIBRA ARMOR#########
["libra_chest_armor", "Libra Chest Armor", #权厄之秤胸甲
   [("breastplate_on_libra", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2873, 
   weight(27)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), 
   imodbits_armor], 
["libra_plate_chain_composite_armor", "Libra Plate Chain Composite Armor", #权厄之秤板链复合甲
   [("red_serdanan_plate_4", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7813, 
   weight(25.000000)|abundance(10)|difficulty(16)|head_armor(0)|body_armor(77)|leg_armor(60), 
   imodbits_armor], 


#######DESERT ARMOR#########
#Desert Women Dresses
["sarranid_lady_dress", "Sarranid_Lady_Dress", [("sarranid_lady_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["sarranid_lady_dress_b", "Sarranid_Lady_Dress", [("sarranid_lady_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["sarranid_common_dress", "Sarranid_Dress", [("sarranid_common_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["sarranid_common_dress_b", "Sarranid_Dress", [("sarranid_common_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 


["sarranid_cloth_robe", "Worn_Robe", [("sar_robe", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 200, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(12), imodbits_cloth], 
["sarranid_cloth_robe_b", "Worn_Robe", [("sar_robe_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 200, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(12), imodbits_cloth], 
["skirmisher_armor", "Skirmisher_Armor", [("skirmisher_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 460, weight(10.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(25)|leg_armor(14), imodbits_cloth], 
["archers_vest", "Archer's_Padded_Vest", [("archers_vest", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_cloth], 
["arabian_armor_b", "Sarranid_Guard_Armor", [("arabian_armor_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4122, weight(24.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(71)|leg_armor(36), imodbits_armor], 


#######BARBARIAN ARMOR#########
["tribal_warrior_outfit", "Tribal Warrior Outfit", #部落棉甲
   [("tribal_warrior_outfit_a_new", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 630, 
   weight(14.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(39)|leg_armor(25), 
   imodbits_cloth], 
["tribal_fur_coat", "Tribal Fur Coat", #部落毛皮甲
   [("ar_vae_ban_tribal_a", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 2968, 
   weight(14.000000)|abundance(30)|difficulty(13)|head_armor(2)|body_armor(43)|leg_armor(18), 
   imodbits_cloth], 
["manzu_shanxuanzhuang", "manzu_shanxuanzhuang", [("barb_fur", 0)], itp_type_body_armor|itp_covers_legs, 0, 2020, weight(5.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(0), imodbits_armor], 
["barbarian_soldier_suit", "Barbarian Soldier Suit", #蛮族士兵装
   [("barbar_armor_1", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 2768, 
   weight(12.000000)|abundance(20)|difficulty(9)|head_armor(0)|body_armor(46)|leg_armor(28), 
   imodbits_armor], 
["barbarian_berserker_suit", "Barbarian Berserker Suit", #蛮族狂战士装
   [("barbar_armor_2", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 2968, 
   weight(13)|abundance(20)|difficulty(9)|head_armor(0)|body_armor(48)|leg_armor(28), 
   imodbits_armor], 
["barbarian_warlord_suit", "Barbarian Warlord Suit", #蛮族霸主装
   [("barbar_armor_3", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3468, 
    weight(15)|abundance(10)|difficulty(9)|head_armor(0)|body_armor(52)|leg_armor(28), 
   imodbits_armor], 
["wailai_manzu_jia", "wailai_manzu_jia", [("a_h3", 0)], itp_type_body_armor|itp_covers_legs, 0, 3408, weight(12)|abundance(20)|difficulty(9)|head_armor(0)|body_armor(52)|leg_armor(28), imodbits_armor], 
["manzu_zhongjia", "manzu_zhongjia", [("bear_warrior", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 3680, weight(34.000000)|abundance(20)|difficulty(21)|head_armor(0)|body_armor(57)|leg_armor(26), imodbits_armor], 


#######DEATHBELL ARMOR#########
#Male Assassin Armors
["zhiyecike_jia", "zhiyecike_jia", [("shadow_outfit_a", 0)], itp_type_body_armor|itp_covers_legs, 0, 2000, weight(6.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(49)|leg_armor(14), imodbits_armor], 
["zhanzhengcike_jiaqiangjia", "zhanzhengcike_jiaqiangjia", [("shadow_outfit_b", 0)], itp_type_body_armor|itp_covers_legs, 0, 2583, weight(6.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(51)|leg_armor(14), imodbits_armor], 
["zhanzhengcike_jia", "zhanzhengcike_jia", [("shadow_outfit_c", 0)], itp_type_body_armor|itp_covers_legs, 0, 2883, weight(7.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(55)|leg_armor(14), imodbits_armor], 
["knell_assasin_armor", "Knell Assasin Armor", [("mirthanoiri_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 9883, weight(7.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(65)|leg_armor(34), imodbits_armor], 
["knell_plate", "Knell Plate", [("knell_plate", 0)], itp_type_body_armor|itp_covers_legs, 0, 28083, weight(16.000000)|abundance(1)|difficulty(12)|head_armor(1)|body_armor(80)|leg_armor(44), imodbits_armor], 

#Female Assassin Armors
["wunvfu", "wunvfu", [("belly_dancer", 0)], itp_type_body_armor|itp_covers_legs, 0, 4500, weight(6.000000)|abundance(5)|difficulty(0)|head_armor(0)|body_armor(40)|leg_armor(30), imodbits_plate], 
["siwangwuzhejia", "siwangwuzhejia", [("xena_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 1500, weight(6.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(50)|leg_armor(30), imodbits_armor], 
["bazhidaowuzhe_jia", "bazhidaowuzhe_jia", [("chaosfemale_armour", 0)], itp_type_body_armor|itp_covers_legs, 0, 1520, weight(6.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(52)|leg_armor(20), imodbits_good|imodbit_well_made|imodbit_superb|imodbit_lordly], 

#Powell Assassin Armors
["powell_knell_plate", "Powell Knell Plate", [("powell_knell_plate", 0)], itp_type_body_armor|itp_covers_legs, 0, 25883, weight(20.000000)|abundance(1)|difficulty(14)|head_armor(2)|body_armor(90)|leg_armor(59), imodbits_armor], 


#######ADVENTURER ARMOR#########
["baijing_maoxianzhe_jia", "baijing_maoxianzhe_jia", [("silver_fine_plate", 0)], itp_type_body_armor|itp_covers_legs, 0, 13410, weight(29.000000)|abundance(10)|difficulty(23)|head_armor(0)|body_armor(100)|leg_armor(75), imodbits_armor], 


#######JUDGMENT HAMMER ARMOR#########
["jugdement_light_armor", "Jugdement Light Armor", #审判者轻装
   [("jugdement_light_armor", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5000, 
   weight(22)|abundance(25)|difficulty(15)|head_armor(0)|body_armor(67)|leg_armor(33), 
   imodbits_armor], 
["jugdement_middle_armor", "Jugdement Middle Armor", #审判者中护甲
   [("jugdement_middle_armor", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6200, 
   weight(25.5)|abundance(25)|difficulty(17)|head_armor(0)|body_armor(74)|leg_armor(42), 
   imodbits_armor], 
["jugdement_heavy_plate", "Jugdement Heavy Plate", #审判者重型板甲
   [("jugdement_heavy_armor", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8300, 
   weight(30)|abundance(25)|difficulty(19)|head_armor(0)|body_armor(85)|leg_armor(57), 
   imodbits_armor], 


#######ANCIENT WORRIER ARMOR#########
["ancient_warrior_armor", "Ancient Warrior Armor", [("ancient_warrior_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 14200, weight(50.000000)|abundance(1)|difficulty(22)|head_armor(0)|body_armor(96)|leg_armor(74), imodbits_armor], 
["ancient_hero_armor", "Ancient Hero Armor", [("dragon_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 19200, weight(59.000000)|abundance(1)|difficulty(27)|head_armor(5)|body_armor(111)|leg_armor(84), imodbits_armor], 


#######GRAGHITE STEEL ARMOR#########
["mogang_zaoqi_banjia", "mogang_zaoqi_banjia", [("transitional_plate_harness_05", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9681, weight(30.000000)|abundance(11)|difficulty(14)|head_armor(0)|body_armor(89)|leg_armor(56), imodbits_armor], 
["mogang_gouhen_quanshenbanjia", "mogang_gouhen_quanshenbanjia", [("plate_harness_05", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 11000, weight(30.000000)|abundance(15)|difficulty(17)|head_armor(2)|body_armor(94)|leg_armor(70), imodbits_armor], 


#######GILDING ARMOR#########
["huijing_qingbanlianfuhe_jia", "huijing_qingbanlianfuhe_jia", [("churburg_13_mail", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 5860, weight(23.000000)|abundance(50)|difficulty(13)|head_armor(0)|body_armor(74)|leg_armor(47), imodbits_armor], 
["hongjing_qingbanlianfuhe_jia", "hongjing_qingbanlianfuhe_jia", [("churburg_13_brass", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 5860, weight(23.000000)|abundance(50)|difficulty(13)|head_armor(0)|body_armor(74)|leg_armor(47), imodbits_armor], 
["liujin_banjia", "liujin_banjia", [("armor12", 0), ("armor12.1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 12410, weight(28.000000)|abundance(10)|difficulty(19)|head_armor(3)|body_armor(93)|leg_armor(68), imodbits_armor], 

["red_bustling_armor", "Red Bustling Armor", [("gorieusred", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 18410, weight(30.000000)|abundance(1)|difficulty(19)|head_armor(5)|body_armor(93)|leg_armor(73), imodbits_armor], 
["black_bustling_armor", "Black Bustling Armor", [("gorieusebony", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 18410, weight(30.000000)|abundance(1)|difficulty(19)|head_armor(5)|body_armor(93)|leg_armor(73), imodbits_armor], 
["white_bustling_armor", "White Bustling Armor", [("gorieus", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 18410, weight(30.000000)|abundance(1)|difficulty(19)|head_armor(5)|body_armor(93)|leg_armor(73), imodbits_armor], 


#######COMMON ARMOR#########
#Weman Daily Wearings
["dress", "Dress", [("dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 50, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["peasant_dress", "Peasant_Dress", [("peasant_dress_b_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 50, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["blue_dress", "Blue_Dress", [("blue_dress_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["lady_dress_ruby", "Lady_Dress", [("lady_dress_r", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["lady_dress_green", "Lady_Dress", [("lady_dress_g", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["lady_dress_blue", "Lady_Dress", [("lady_dress_b", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["red_dress", "Red_Dress", [("red_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["brown_dress", "Brown_Dress", [("brown_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], 
["green_dress", "Green_Dress", [("green_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 100, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), imodbits_cloth], ["court_dress", "Court_Dress", [("court_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 170, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(14)|leg_armor(4), imodbits_cloth], 
["woolen_dress", "Woolen_Dress", [("woolen_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 75, weight(1.750000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(18)|leg_armor(14), imodbits_cloth], 

["red_noble_dress", "Red Noble Dress", #红色贵族裙
   [("vampire_lady_dress", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 820, 
   weight(1.75)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(26)|leg_armor(13), 
   imodbits_cloth], 
["purple_noble_dress", "Purple Noble Dress", #紫色贵族裙
   [("vampire_lady_dress_2", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 820, 
   weight(1.75)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(26)|leg_armor(13), 
   imodbits_cloth], 
["black_gorgeous_noble_dress", "Black Gorgeous Noble Dress", #黑色华丽贵族裙
   [("vampire_dress_3", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 930, 
   weight(2)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(28)|leg_armor(14), 
   imodbits_cloth], 
["red_gorgeous_noble_dress", "Red Gorgeous Noble Dress", #红色华丽贵族裙
   [("vampire_dress_4", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 930, 
   weight(2)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(28)|leg_armor(14), 
   imodbits_cloth], 

#Noble Daily Wearings
["courtly_outfit", "Courtly_Outfit", [("nobleman_outf", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 200, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(14)|leg_armor(10), imodbits_cloth], 
["nobleman_outfit", "Nobleman_Outfit", [("nobleman_outfit_b_new", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 200, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(12), imodbits_cloth], 
["rich_outfit", "Rich_Outfit", [("merchant_outf", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 170, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(4), imodbits_cloth], 
["red_noble_shirt", "Red Noble Shirt", #红色贵族衫
   [("baretunic_01", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 130, 
   weight(1.5)|abundance(50)|difficulty(0)|head_armor(0)|body_armor(18)|leg_armor(10), 
   imodbits_cloth], 
["blue_noble_shirt", "Blue Noble Shirt", #蓝色贵族衫
   [("baretunic_09", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 130, 
   weight(1.5)|abundance(50)|difficulty(0)|head_armor(0)|body_armor(18)|leg_armor(10), 
   imodbits_cloth], 
["leather_noble_gown", "leather_noble_gown", #贵族皮毛华服
   [("nobleman_outfit_c2", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 200, 
   weight(2)|abundance(40)|difficulty(0)|head_armor(0)|body_armor(23)|leg_armor(10), 
   imodbits_cloth], 
["red_gorgeous_noble_shirt", "Red GorgeousNoble Shirt", #红色华丽贵族衫
   [("vamp_noble_clothing", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 730, 
   weight(1.5)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(28)|leg_armor(10), 
   imodbits_cloth], 
["black_gorgeous_noble_shirt", "Black GorgeousNoble Shirt", #黑色华丽贵族衫
   [("vamp_noble_clothing_black", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 730, 
   weight(1.5)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(28)|leg_armor(10), 
   imodbits_cloth], 
["black_trench_coat", "Black Trench Coat", #黑风衣
   [("vampire_robe", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 1300, 
   weight(2.5)|abundance(50)|difficulty(6)|head_armor(0)|body_armor(36)|leg_armor(15), 
   imodbits_cloth], 

["female_ranger_light_armor", "Female Ranger Light Armor", #女游侠轻装
   [("FKamael_cloth", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 2500, 
   weight(3.5)|abundance(5)|difficulty(0)|head_armor(0)|body_armor(39)|leg_armor(28), 
   imodbits_cloth], 
["female_ranger_leather_armor", "Female Ranger Leather Armor", #女游侠皮护甲
   [("FKamael_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 3500, 
   weight(5)|abundance(5)|difficulty(10)|head_armor(0)|body_armor(49)|leg_armor(32), 
   imodbits_cloth], 

#Man Daily Wearings
["shirt", "Shirt", [("shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 30, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(0), imodbits_cloth], 
["linen_tunic", "Linen_Tunic", [("shirt_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 70, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(3), imodbits_cloth], 
["robe", "Robe", [("robe", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 140, weight(1.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(16)|leg_armor(8), imodbits_cloth], 
["short_tunic", "Red_Tunic", [("rich_tunic_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 80, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(1), imodbits_cloth], 
["coarse_tunic", "Tunic_with_vest", [("coarse_tunic_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 70, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(18)|leg_armor(10), imodbits_cloth], 
["burlap_tunic", "Burlap_Tunic", [("shirt", 0)], itp_type_body_armor|itp_covers_legs, 0, 70, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(18)|leg_armor(10), imodbits_armor], 
["leather_apron", "Leather_Apron", [("leather_apron", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 120, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(19)|leg_armor(11), imodbits_cloth], 
["tabard", "Tabard", [("tabard_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 200, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(12), imodbits_cloth], 
["padded_leather", "Padded_Leather", [("leather_armor_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 600, weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(37)|leg_armor(16), imodbits_cloth], 
["leather_jacket", "Leather_Jacket", [("leather_jacket_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 400, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(42)|leg_armor(0), imodbits_cloth], 
["pelt_coat", "Pelt_Coat", [("thick_coat_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 200, weight(8.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(6), imodbits_cloth], 
["fur_coat", "Fur_Coat", [("fur_coat", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 430, weight(6.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(45)|leg_armor(6), imodbits_armor], 

#Milita Armors
["red_tunic", "Red_Tunic", [("arena_tunicR_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 90, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(9), imodbits_cloth], 
["green_tunic", "Green_Tunic", [("arena_tunicG_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 90, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(9), imodbits_cloth], 
["blue_tunic", "Blue_Tunic", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 90, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(9), imodbits_cloth], 
["yellow_tunic", "Yellow Tunic", [("arena_tunicY_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 90, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(9), imodbits_cloth], 
["white_tunic", "White Tunic", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 90, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(9), imodbits_cloth], 

["tunic_with_green_cape", "Tunic_with_Green_Cape", [("peasant_man_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 56, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(20)|leg_armor(12), imodbits_cloth], 
["ragged_outfit", "Ragged_Outfit", [("ragged_outfit_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 430, weight(10.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(23)|leg_armor(12), imodbits_cloth], 
["gambeson", "Gambeson", [("white_gambeson", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 300, weight(10.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(33)|leg_armor(15), imodbits_cloth], 
["blue_gambeson", "Blue_Gambeson", [("blue_gambeson", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 300, weight(10.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(33)|leg_armor(15), imodbits_cloth], 
["red_gambeson", "Red_Gambeson", [("red_gambeson_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 300, weight(10.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(33)|leg_armor(15), imodbits_cloth], 
["leather_vest", "Leather_Vest", [("leather_vest_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 230, weight(4.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(36)|leg_armor(19), imodbits_cloth], 
["rawhide_coat", "Rawhide_Coat", [("coat_of_plates_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 120, weight(9.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(36)|leg_armor(0), imodbits_cloth], 
["padded_cloth", "Aketon", [("padded_cloth_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_cloth], 
["aketon_green", "Padded_Cloth", [("padded_cloth_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 450, weight(11.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(16), imodbits_cloth], 
["nomad_armor", "Nomad_Armor", [("nomad_armor_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 500, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(0), imodbits_cloth], 
["khergit_armor", "Khergit_Armor", [("khergit_armor_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 490, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(0), imodbits_cloth], 
["light_leather", "Light_Leather", [("light_leather", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 750, weight(9.000000)|abundance(90)|difficulty(0)|head_armor(0)|body_armor(38)|leg_armor(26), imodbits_armor], 
["leather_jerkin", "Leather_Jerkin", [("ragged_leather_jerkin", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian|itp_next_item_as_melee, 0, 480, weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(41)|leg_armor(21), imodbits_cloth], 
["maopipijia_pijia", "maopipijia_pijia", [("rough_leather_fur", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 830, weight(12)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(42)|leg_armor(28), imodbits_armor], 

#Soldier Armors
["red_studded_padded_armor", "Red Studded Padded Armor", #红色钉饰垫衬甲
   [("brigandine_a", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 873, 
   weight(12)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(43)|leg_armor(23), 
   imodbits_cloth], 
["leather_armor", "Leather_Armor", [("tattered_leather_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1043, weight(12.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(46)|leg_armor(12), imodbits_cloth], 
["duanxiu_lianjiapao", "duanxiu_lianjiapao", [("maille_studded", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2878, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(51)|leg_armor(46), imodbits_armor], 
["quanshen_lianjai", "quanshen_lianjai", [("long_mail_coat_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2483, weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(55)|leg_armor(46), imodbits_armor], 
["mail_hauberk", "Mail_Hauberk", [("hauberk_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1332, weight(20.000000)|abundance(100)|difficulty(7)|head_armor(0)|body_armor(55)|leg_armor(47), imodbits_armor], 
["linjiapijian_dingshijia", "linjiapijian_dingshijia", [("rough_spiked_plainring", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 2950, weight(19.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(58)|leg_armor(29), imodbits_armor], 
["dingshi_fupi_duanlianjia", "dingshi_fupi_duanlianjia", [("brigandine_black", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3045, weight(20.000000)|abundance(30)|difficulty(9)|head_armor(0)|body_armor(58)|leg_armor(42), imodbits_armor], 
["brigandine_red", "Brigandine", [("brigandine_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1830, weight(20.000000)|abundance(100)|difficulty(9)|head_armor(0)|body_armor(58)|leg_armor(42), imodbits_armor], 
["lvzhu_lianjiashan", "lvzhu_lianjiashan", [("armor_arena_green", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 3400, weight(21.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(59)|leg_armor(33), imodbits_armor], 
["hongkulou_lianjiashan", "hongkulou_lianjiashan", [("armor_arena_red", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 3400, weight(21.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(59)|leg_armor(33), imodbits_armor], 
["huangren_lianjaishan", "huangren_lianjaishan", [("armor_arena_yellow", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 3400, weight(21.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(59)|leg_armor(33), imodbits_armor], 
["lanmiu_lianjiashan", "lanmiu_lianjiashan", [("armor_arena_blue", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_covers_legs, 0, 3400, weight(21.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(59)|leg_armor(33), imodbits_armor], 
["wulaizhe_lianjia", "wulianzhe_lianjia", [("galloglass_mail", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 3400, weight(21.000000)|abundance(40)|difficulty(11)|head_armor(0)|body_armor(60)|leg_armor(32), imodbits_armor], 
["maopipijia_linjia", "maopipijia_linjia", [("rough_macle_fured", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 3778, weight(20.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(60)|leg_armor(34), imodbits_armor], 

["mail_with_tunic_red", "Red Mail with Tunic", [("arena_armorR_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3452, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor], 
["mail_with_tunic_green", "Green Mail with Tunic", [("arena_armorG_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3452, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor], 
["mail_with_tunic_yellow", "Yellow Mail with Tunic", [("arena_armorY_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3452, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor], 
["mail_with_tunic_white", "White Mail with Tunic", [("arena_armorW_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3452, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor], 

#Breastplates
["heibai_xiongjia", "heibai_xiongjia", [("breastplate_on_black", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2573, weight(19.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["lanse_xiongjia", "lanse_xiongjia", [("breastplate_on_blue", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2573, weight(19.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["huanghei_xiongjia", "huanghei_xiongjia", [("breastplate_on_empire", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2573, weight(19.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["lvse_xiongjia", "lvse_xiongjia", [("breastplate_on_green", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2573, weight(19.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["baise_xiongjia", "baise_xiongjia", [("breastplate_on_plain", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2573, weight(19.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["hongse_xiongjia", "hongse_xiongjia", [("breastplate_on_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2573, weight(19.000000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(27), imodbits_armor], 
["heavy_red_breastplate", "Heavy Red Breastplate", #红色重型胸甲
   [("red_gambeson_armored", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3273, 
   weight(21)|abundance(100)|difficulty(10)|head_armor(0)|body_armor(55)|leg_armor(27), 
   imodbits_armor], 
["mercenary_three_quarter_armour", "Mercenary Three Quarter Armour", #佣兵四分之三甲
   [("bnw_armour_slashed", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7273, 
   weight(24)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(80)|leg_armor(37), 
   imodbits_armor], 

#Westcoast Style Armors
["studded_leather_coat", "Studded_Leather_Coat", [("leather_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 692, weight(17.000000)|abundance(100)|difficulty(7)|head_armor(0)|body_armor(48)|leg_armor(30), imodbits_armor], 
["byrnie", "Byrnie", [("byrnie_a_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 792, weight(19.000000)|abundance(100)|difficulty(7)|head_armor(0)|body_armor(52)|leg_armor(36), imodbits_armor], 
["mail_shirt", "Mail_Shirt", [("mail_shirt_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1041, weight(19.000000)|abundance(100)|difficulty(6)|head_armor(0)|body_armor(53)|leg_armor(43), imodbits_armor], 
["zongselianjia_shan", "zongselianjia_shan", [("mail_coat_f", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 3361, weight(20.000000)|abundance(100)|difficulty(10)|head_armor(0)|body_armor(54)|leg_armor(40), imodbits_armor], 
["haubergeon", "Haubergeon", [("haubergeon_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 862, weight(18.000000)|abundance(100)|difficulty(9)|head_armor(0)|body_armor(55)|leg_armor(26), imodbits_armor], 
["scale_armor", "Scale_Armor", [("lamellar_armor_e", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2560, weight(25.000000)|abundance(100)|difficulty(12)|head_armor(0)|body_armor(56)|leg_armor(23), imodbits_armor], 
["lingjia_pao", "lingjia_pao", [("byrnieblack", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4214, weight(24.000000)|abundance(40)|difficulty(14)|head_armor(0)|body_armor(67)|leg_armor(48), imodbits_armor], 
["lianjia_pijian_linjia", "lianjia_pijian_linjia", [("ar_vae_t5_lamellar_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6000, weight(30.000000)|abundance(40)|difficulty(18)|head_armor(0)|body_armor(69)|leg_armor(40), imodbits_armor], 
["diecengpilian_jia", "diecengpilian_jia", [("nord_coat_of_plates", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 5287, weight(24.000000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(70)|leg_armor(30), imodbits_armor], 
["hongse_zhabanjia", "hongse_zhabanjia", [("huscarl_armour", 0)], itp_type_body_armor|itp_covers_legs, 0, 7319, weight(28.000000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(83)|leg_armor(45), imodbits_armor], 

#Steppe Style Armors
["lamellar_armor", "Lamellar_Armor", [("lamellar_armor_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2415, weight(25.000000)|abundance(100)|difficulty(10)|head_armor(0)|body_armor(52)|leg_armor(46), imodbits_armor], 
["reroupijia", "reroupijia", [("wei_xiadi_lamellar_armor02", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 2278, weight(18.000000)|abundance(60)|difficulty(12)|head_armor(0)|body_armor(55)|leg_armor(30), imodbits_armor], 
["linlianfuhe_jia", "linlianfuhe_jia", [("ragged_scale_b", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 7678, weight(26.000000)|abundance(30)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(48), imodbits_armor], 
["zhongxing_zhajia", "zhongxing_zhajia", [("rus_scale", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 8300, weight(29.000000)|abundance(30)|difficulty(17)|head_armor(0)|body_armor(81)|leg_armor(47), imodbits_armor], 

#Chain Armor Robes
["heraldic_mail_with_surcoat", "Heraldic_Mail_with_Surcoat", [("heraldic_armor_new_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(7)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":var_0", ":var_1"),
    ]),
]], 
["heraldic_mail_with_tabard", "Heraldic_Mail_with_Tabard", [("heraldic_armor_new_d", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3452, weight(21.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":var_0", ":var_1"),
    ]),
]], 
["heraldic_mail_with_tunic", "Heraldic_Mail", [("heraldic_armor_new_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3452, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(36), imodbits_armor, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":var_0", ":var_1"),
    ]),
]], 
["heraldic_mail_with_tunic_b", "Heraldic_Mail", [("heraldic_armor_new_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3616, weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(57), imodbits_armor, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":var_0", ":var_1"),
    ]),
]], 
["mail_with_surcoat", "Mail_with_Surcoat", [("mail_long_surcoat_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["surcoat_over_mail", "Surcoat_over_Mail", [("surcoat_over_mail_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["shenlan_lianjiazhaopao", "shenlan_lianjiazhaopao", [("swangarde_surcoat_4", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["lanse_lianjiazhaopao", "lanse_lianjiazhaopao", [("aqs_surcoat3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["lianghuang_lianjiazhaopao", "lianghuang_lianjiazhaopao", [("aqs_surcoat1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["qingse_lianjiazhaopao", "qingse_lianjiazhaopao", [("aqs_surcoat2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["dahong_lianjiazhaopao", "dahong_lianjiazhaopao", [("aqs_surcoat5", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["honghua_lianjia", "honghua_lianjia", [("teu_huogedoujia", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["lvbai_lianjiazhaopao", "lvbai_lianjiazhaopao", [("surcoat_com_021", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["lvjian_lianjiazhaopao", "lvjian_lianjiazhaopao", [("surcoat_com_031", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["jinhua_lianjiazhaopao", "jinhua_lianjiazhaopao", [("surcoat_mmx_291", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["hongtiepi_lianjiashan", "hongtiepi_lianjiashan", [("surcoat_mmx_303", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3332, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(55)|leg_armor(45), imodbits_armor], 
["gongniu_lianjiazhaopao", "gongniu_lianjiazhaopao", [("surcoat_mtw_111", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 
["heibai_lianjiazhaopao", "heibai_lianjiazhaopao", [("surcoat_mtw_131", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3562, weight(22.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(61)|leg_armor(54), imodbits_armor], 

#Light Plate Chain Composite Armors
["jianyi_qingxing_banlianjia", "jianyi_qingxing_banlianjia", [("long_platemail_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5817, weight(22.000000)|abundance(40)|difficulty(10)|head_armor(0)|body_armor(69)|leg_armor(40), imodbits_armor], 
["baimian_banlianjia", "baimian_banlianjia", [("transitional_plate_harness_06", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5817, weight(22.000000)|abundance(50)|difficulty(10)|head_armor(0)|body_armor(69)|leg_armor(40), imodbits_armor], 
["mail_and_plate", "Mail_and_Plate", [("mail_and_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5563, weight(22.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(42), imodbits_armor], 
["heise_lianxiongjia", "heise_lianxiongjia", [("blackmailplate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5563, weight(22.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(42), imodbits_armor], 
["zongse_lianxiongjia", "zongse_lianxiongjia", [("brownmailplate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5563, weight(22.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(72)|leg_armor(42), imodbits_armor], 
["jianyi_gouheng_zhongxing_banlianjia", "jianyi_gouheng_zhongxing_banlianjia", [("transitional_plate_harness_09", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5294, weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(73)|leg_armor(44), imodbits_armor], 
["gouheng_zhongxing_banlianjia", "gouheng_zhongxing_banlianjia", [("transitional_plate_harness_07", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6360, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 

#Plate Chain Composite Armors
["huisejianyi_banlianjia", "huisejianyi_banlianjia", [("corrazina_grey", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 5294, weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(73)|leg_armor(44), imodbits_armor], 
["lvsejianyi_banlianjia", "lvsejianyi_banlianjia", [("corrazina_green", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 5294, weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(73)|leg_armor(44), imodbits_armor], 
["hongsejianyi_banlianjia", "hongsejianyi_banlianjia", [("corrazina_red", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 5294, weight(23.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(73)|leg_armor(44), imodbits_armor], 
["dingshi_fupi_qingbanlian", "dingshi_fupi_qingbanlian", [("brig_plate_black", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5287, weight(23.000000)|abundance(30)|difficulty(12)|head_armor(0)|body_armor(76)|leg_armor(50), imodbits_armor], 
["honglanpao_banlian", "honglanpao_banlian", [("early_transitional_blue", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 6360, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 
["baipao_banlian", "baipao_banlian", [("early_transitional_heraldic", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 6360, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 
["honghuangpao_banlian", "honghuangpao_banlian", [("early_transitional_orange", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 6360, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_armor], 
["shenlan_pilianjia", "shenlan_pilianjia", [("dark_hard_lthr", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7810, weight(26.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(84)|leg_armor(58), imodbits_armor], 
["guizu_banlianfuhejia", "guizu_banlianfuhejia", [("armor23", 0), ("armor23.1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7113, weight(25.000000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(85)|leg_armor(55), imodbits_armor], 

#Coat of Plates
["heibai_banjiayi", "heibai_banjiayi", [("coat_of_platesblack", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6827, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(44), imodbits_armor], 
["lanbai_banjiayi", "lanbai_banjiayi", [("coat_of_platesblue", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6827, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(44), imodbits_armor], 
["lvbai_banjiayi", "lvbai_banjiayi", [("coat_of_platesgreen", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6827, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(44), imodbits_armor], 
["hongbai_banjiayi", "hongbai_banjiayi", [("coat_of_platesred", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6827, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(44), imodbits_armor], 
["huangbai_banjiayi", "huangbai_banjiayi", [("coat_of_platesyellow", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6827, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(44), imodbits_armor], 
["coat_of_plates", "Coat_of_Plates", [("coat_of_plates_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6830, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(45), imodbits_armor], 
["coat_of_plates_red", "Coat_of_Plates", [("coat_of_plates_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6830, weight(26.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(75)|leg_armor(45), imodbits_armor], 

#Simple Plate Armors
["plate_armor", "Plate_Armor", [("full_plate_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6360, weight(25.000000)|abundance(50)|difficulty(14)|head_armor(0)|body_armor(78)|leg_armor(54), imodbits_plate], 
["tiesezhongxingbanjia", "tiesezhongxingbanjia", [("mtw_pplate_iron", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 7600, weight(27.000000)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(82)|leg_armor(46), imodbits_armor], 
["iron_chest_plate", "Iron Chest Plate", #铁色胸板甲
   [("plate_armor3", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7000, 
   weight(24)|abundance(25)|difficulty(14)|head_armor(0)|body_armor(83)|leg_armor(50), 
   imodbits_armor], 
["rogue_iron_chest_plate", "Rogue Iron Chest Plate", #无赖骑士胸板甲
   [("plate_armor3_rogue", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7300, 
   weight(25)|abundance(20)|difficulty(15)|head_armor(0)|body_armor(85)|leg_armor(50), 
   imodbits_armor], 
["heise_zaoqi_banjia", "heise_zaoqi_banjia", [("transitional_plate_harness_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7681, weight(30.000000)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(84)|leg_armor(54), imodbits_armor], 
["heibai_zaoqi_banjia", "heibai_zaoqi_banjia", [("transitional_plate_harness_02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7681, weight(30.000000)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(84)|leg_armor(54), imodbits_armor], 
["lanse_zaoqi_banjia", "lanse_zaoqi_banjia", [("transitional_plate_harness_03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7681, weight(30.000000)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(84)|leg_armor(54), imodbits_armor], 
["hongse_zaoqi_banjia", "hongse_zaoqi_banjia", [("transitional_plate_harness_04", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 7681, weight(30.000000)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(84)|leg_armor(54), imodbits_armor], 

#Plate Armors
["roam_knight_plate", "Roam Knight Plate", [("fahan_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8010, weight(24.000000)|abundance(20)|difficulty(17)|head_armor(1)|body_armor(90)|leg_armor(28), imodbits_armor], 
["black_armor", "Black_Armor", [("black_armor", 0)], itp_type_body_armor|itp_covers_legs, 0, 9000, weight(23.000000)|abundance(25)|difficulty(16)|head_armor(0)|body_armor(86)|leg_armor(54), imodbits_plate], 
["zaoqi_zhongbanjia", "zaoqi_zhongbanjia", [("xenoargh_metal_leather01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8281, weight(32.000000)|abundance(20)|difficulty(17)|head_armor(0)|body_armor(87)|leg_armor(60), imodbits_armor], 
["tiesezhongxing_banjia", "tiesezhongxing_banjia", [("mtw2_armor_steel", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 8600, weight(28.000000)|abundance(20)|difficulty(16)|head_armor(0)|body_armor(87)|leg_armor(60), imodbits_armor], 
["chivalric_knight_plate", "Chivalric Knights Plate", [("akatosh", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8810, weight(28.000000)|abundance(20)|difficulty(18)|head_armor(1)|body_armor(90)|leg_armor(60), imodbits_armor], 
["wangguo_banjia", "wangguo_banjia", [("milanese_armour", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["baise_quanshenbanjia", "baise_quanshenbanjia", [("plate_harness_white", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["huangse_quanshenbanjia", "huangse_quanshenbanjia", [("plate_harness_yellow", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["lanse_quanshenbanjia", "lanse_quanshenbanjia", [("plate_harness_blue", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["hongse_quanshenbanjia", "hongse_quanshenbanjia", [("plate_harness_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["baimian_quanshenbanjia", "baimian_quanshenbanjia", [("plate_harness_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["jili_quanshenbanjia", "jili_quanshenbanjia", [("plate_harness_02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["jinjiu_quanshenbanjia", "jinjiu_quanshenbanjia", [("plate_harness_03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["heibai_quanshenbanjia", "heibai_quanshenbanjia", [("plate_harness_04", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["jinlong_quanshenbanjia", "jinlong_quanshenbanjia", [("plate_harness_06", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["jiaoma_quanshenbanjia", "jiaoma_quanshenbanjia", [("plate_harness_unicorn", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9000, weight(29.000000)|abundance(25)|difficulty(16)|head_armor(1)|body_armor(90)|leg_armor(68), imodbits_armor], 
["zisejingzhi_banjia", "zisejingzhi_banjia", [("gothic_plate2", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 9100, weight(29.000000)|abundance(20)|difficulty(16)|head_armor(1)|body_armor(92)|leg_armor(68), imodbits_armor], 
["heisejinzhibanjia", "heisejinzhibanjia", [("gothic_plate", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 9100, weight(29.000000)|abundance(20)|difficulty(16)|head_armor(1)|body_armor(92)|leg_armor(68), imodbits_armor], 
["gorgeous_tight_plate_armor", "Gorgeous Tight Plate Armor", #华丽紧致板甲
   [("powell_lifeguard_plate_light", 0)], 
   itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9200, 
   weight(29)|abundance(20)|difficulty(16)|head_armor(1)|body_armor(92)|leg_armor(68), 
   imodbits_armor], 
["jiaqianglengshi_jia", "jiaqianglengshi_jia", [("pa_plate", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 9400, weight(30.000000)|abundance(20)|difficulty(17)|head_armor(2)|body_armor(93)|leg_armor(68), imodbits_armor], 
["guizu_banjia", "guizu_banjia", [("armor11", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 10410, weight(28.000000)|abundance(10)|difficulty(19)|head_armor(3)|body_armor(93)|leg_armor(68), imodbits_armor], 

#Heavy Plate Armors
["baimian_jiahzong_banjia", "baimian_jiahzong_banjia", [("platemail_harness_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9670, weight(31.000000)|abundance(15)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(73), imodbits_armor], 
["huawen_jiahzong_banjia", "huawen_jiahzong_banjia", [("platemail_harness_02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9670, weight(31.000000)|abundance(15)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(73), imodbits_armor], 
["huanghei_jiazhong_banjia", "huanghei_jiazhong_banjia", [("platemail_harness_04", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9670, weight(31.000000)|abundance(15)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(73), imodbits_armor], 
["hongbai_jiazhong_banjia", "hongbai_jiazhong_banjia", [("platemail_harness_05", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9670, weight(31.000000)|abundance(15)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(73), imodbits_armor], 
["lanbai_jiazhong_banjia", "lanbai_jiazhong_banjia", [("platemail_harness_06", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9670, weight(31.000000)|abundance(15)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(73), imodbits_armor], 
["lvbai_jiazhong_banjia", "lvbai_jiazhong_banjia", [("platemail_harness_07", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9670, weight(31.000000)|abundance(15)|difficulty(18)|head_armor(2)|body_armor(95)|leg_armor(73), imodbits_armor], 
["qingjin_banjia", "qingjin_banjia", [("hm_arm_masU", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 10500, weight(30.000000)|abundance(5)|difficulty(18)|head_armor(5)|body_armor(102)|leg_armor(75), imodbits_armor], 
["baitie_banjia", "baitie_banjia", [("hm_arm_masV", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9500, weight(28.000000)|abundance(5)|difficulty(18)|head_armor(2)|body_armor(92)|leg_armor(68), imodbits_armor], 
["heijin_banjia", "heijin_banjia", [("hm_arm_masW", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 9800, weight(29.000000)|abundance(5)|difficulty(18)|head_armor(3)|body_armor(95)|leg_armor(70), imodbits_armor], 
["duangang_banjia", "duangang_banjia", [("hm_arm_masX", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 11000, weight(38.000000)|abundance(5)|difficulty(21)|head_armor(10)|body_armor(116)|leg_armor(20), imodbits_armor], 
["huxinzhongxin_banjia", "huxinzhongxin_banjia", [("full_plate", 0)], itp_type_body_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_covers_legs, 0, 9800, weight(31.000000)|abundance(15)|difficulty(19)|head_armor(1)|body_armor(95)|leg_armor(68), imodbits_armor], 

#Special Armors
["dancer_body", "Dancer Body", #舞女亵衣
   [("dancer_body", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 500, 
   weight(0.5)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(2), 
   imodbits_cloth], 
["bride_dress", "Bride_Dress", #婚纱
   [("bride_dress", 0)], 
   itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 500, 
   weight(3)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(10), 
   imodbits_cloth], 
["heise_chaoqing_banjia", "heise_chaoqing_banjia", [("plate_falcon_armor_black", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 8211, weight(19.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(70)|leg_armor(48), imodbits_armor], 
["female_light_plate", "Female Light Plate", #女式轻板甲
   [("cw_armor", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8900, 
   weight(27)|abundance(10)|difficulty(16)|head_armor(0)|body_armor(84)|leg_armor(57), 
   imodbits_armor], 
["adventure_knight_armor", "Adventure Knight Armor", #历险骑士的铠甲
   [("Oscar", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 7410, 
   weight(27)|abundance(1)|difficulty(17)|head_armor(2)|body_armor(87)|leg_armor(68), 
   imodbits_none], 
["roam_knight_plate_with_shawl", "Roam Knight Plate With Shawl", #带披肩云游骑士胸板甲
   [("fahan", 0)], 
   itp_type_body_armor|itp_covers_legs, 0, 8710, 
   weight(25)|abundance(1)|difficulty(17)|head_armor(3)|body_armor(92)|leg_armor(28), 
   imodbits_none], 




#SHIELD WEAPON
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["shield_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######POWELL SHIELD#########
["powell_fan_shaped_shield", "Powell Fan-shaped Shield", #普威尔徽章盾
   [("shield_heater_217", 0)], 
   itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 1060, 
   weight(3.500000)|abundance(10)|difficulty(4)|hit_points(620)|body_armor(35)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["powell_coat_of_arms", "Powell Coat of Arms", #普威尔国徽巨盾
   [("duyaqishidun", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_kite_shield, 1960, 
   weight(6.500000)|abundance(1)|difficulty(5)|hit_points(820)|body_armor(41)|spd_rtng(70)|shield_width(38)|shield_height(49), 
   imodbits_shield, [shield_hit_point_trigger]], 

#普威尔王室
["pride_fan_shaped_shield", "Pride Fan-shape Shield", #狮群扇形盾，士兵用
   [("shield_heater_317", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.500000)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["dark_lion_fan_shaped_shield", "Dark Lion Fan Shaped Shield", #暗狮菱形盾，隐秘行动者用
   [("shield_heater_c", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2)|abundance(10)|difficulty(3)|hit_points(450)|body_armor(24)|spd_rtng(97)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 
["blue_lion_fan_shaped_shield", "Blue Lion Fan-shape Shield", #蓝狮扇形盾，各地投奔王室者用
   [("shield_heater_214", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["red_yellow_lion_fan_shaped_shield", "Red Yellow Lion Fan Shaped Shield", #红黄狮扇形盾，骑士用
   [("shield_heater_410", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.500000)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["yellow_lion_fan_shaped_shield", "Red Lion Fan-shape Shield", #黄狮菱形盾，王室近卫用
   [("shield_battle103", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 460, 
   weight(3)|abundance(100)|difficulty(2)|hit_points(500)|body_armor(25)|spd_rtng(91)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 
["red_lion_iron_fan_shaped_shield", "Red Lion Iron Fan-shape Shield", #赤狮钢面菱形盾，高级骑士用
   [("shield_battle106", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 840, 
   weight(4.5)|abundance(20)|difficulty(4)|hit_points(550)|body_armor(32)|spd_rtng(85)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 

#拜龙教
["simple_red_dragon_skoutarion", "Simple Red Dragon Skoutarion", #简易红龙泪形盾
   [("norman_shield_3", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(100)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["silver_dragon_fan_shaped_shield", "Silver Dragon Fan Shaped Shield", #银龙扇形盾
   [("shield_heater_210", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["white_dragon_fan_shaped_shield", "White Dragon Fan Shaped Shield", #白龙扇形盾
   [("shield_heater_403", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

["blue_dragon_skoutarion", "Blue Dragon Skoutarion", #蓝龙泪形盾
   [("shield_tear_24", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 1050, 
   weight(3.5)|abundance(30)|difficulty(4)|hit_points(620)|body_armor(23)|spd_rtng(80)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["blue_dragon_large_shield", "Blue Dragon Large Shield", #蓝龙扇形塔盾
   [("House_of_Borguen_Heater4", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_kite_shield, 1744, 
   weight(5.000000)|abundance(10)|difficulty(4)|hit_points(630)|body_armor(30)|spd_rtng(70)|shield_width(36)|shield_height(54), 
   imodbits_shield, [shield_hit_point_trigger]], 

["dragon_god_black_shield", "Dragon God Black Shield", #龙神黑纹盾
   [("fix_EOS_knight_shield", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 3444, 
   weight(4)|abundance(2)|difficulty(5)|hit_points(630)|body_armor(35)|spd_rtng(95)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["holy_dragoon_knight_shield", "Holy Dragoon Knight Shield", #圣龙骑士盾
   [("fix_EOS_knight_shield_powell", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 3444, 
   weight(4)|abundance(2)|difficulty(5)|hit_points(630)|body_armor(35)|spd_rtng(95)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

#罗德里格斯公国
["simple_blue_flower_fan_shaped_shield", "Simple Blue Flower Fan-Shaped Shield", #简易蓝花扇形盾
   [("shield_heater_206", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, 
   weight(2)|abundance(100)|difficulty(1)|hit_points(380)|body_armor(20)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 
["wildboar_fan_shaped_shield", "Wildboar Fan-shape Shield", #野猪扇形盾，佣兵团用
   [("shield_heater_203", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["red_blue_fan_shaped_shield", "Red Blue Fan-shaped Shield", #红蓝四分扇形盾
   [("shield_heater_202", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["blue_flower_fan_shaped_shield", "Blue Flower Fan-Shaped Shield", #蓝花菱形盾
   [("shield_battle107", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 460, 
   weight(3)|abundance(100)|difficulty(2)|hit_points(500)|body_armor(25)|spd_rtng(91)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 
["blue_flower_skoutarion", "Blue Flower Skoutarion", #蓝花泪形盾
   [("shield_tear_28", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 550, 
   weight(3.5)|abundance(100)|difficulty(4)|hit_points(580)|body_armor(22)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

["shield_heater_of_element", "Shield Heater of Element", #元素骑士扇形盾
   [("shield_heater_element", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 660, 
   weight(2.5)|abundance(10)|difficulty(3)|hit_points(520)|body_armor(27)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

#普属自由城邦/普威尔正教
["yellow_black_fan_shaped_shield", "Yellow Black Fan-Shaped Shield", #黄黑八分扇形盾
   [("shield_heater_319", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, 
   weight(2)|abundance(100)|difficulty(1)|hit_points(380)|body_armor(20)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 
["strengthen_yellow_black_fan_shaped_shield", "Strengthen Yellow Black Fan-Shaped Shield", #加强黄黑扇形盾
   [("shield_heater_315", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 320, 
   weight(2)|abundance(100)|difficulty(1)|hit_points(390)|body_armor(21)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 

["preist_fan_shaped_shield", "Preist Fan Shaped Shield", #奉神城扇形盾
   [("ibelin_shield_knight_a", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(3)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["honeysuckle_fan_shaped_shield", "Honeysuckle Fan-shaped Shield", #金银花扇形盾
   [("shield_heater_514", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 420, 
   weight(2.5)|abundance(80)|difficulty(3)|hit_points(420)|body_armor(26)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["black_yellow_skoutarion", "Black Yellow Skoutarion", #黑黄筝形盾
   [("shield_kite112", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 440, 
   weight(3)|abundance(90)|difficulty(3)|hit_points(480)|body_armor(22)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]],
["red_yellow_skoutarion", "Red Yellow Skoutarion", #红黄筝形盾
   [("shield_kite109", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(90)|difficulty(3)|hit_points(480)|body_armor(23)|spd_rtng(83)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]],  
["yellow_black_skoutarion", "Yellow Black Skoutarion", #黄黑泪形盾
   [("shield_tear_27", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 550, 
   weight(3.5)|abundance(100)|difficulty(4)|hit_points(580)|body_armor(22)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

["golden_red_round_shield", "Golden Red Round Shield", #金红圆盾
   [("saracin_shield_v", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 560, 
   weight(3)|abundance(40)|difficulty(3)|hit_points(410)|body_armor(31)|spd_rtng(81)|shield_width(28), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 4),#完美格挡时限0.4秒
    ]),
   ]], 
["esoteric_Painted_round_shield", "Esoteric Painted Round Shield", #奥纹圆盾
   [("saracin_shield_p", 0)], 
   itp_type_shield, itcf_carry_round_shield, 940, 
   weight(3)|abundance(20)|difficulty(4)|hit_points(410)|body_armor(37)|spd_rtng(81)|shield_width(28), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 4),#完美格挡时限0.4秒
    ]),
   ]], 

#南沙公国
["powell_red_round_shield", "Powell Red Round Shield", #普威尔红圆盾
   [("roman_shield_velite", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 340, 
   weight(2.5)|abundance(100)|difficulty(3)|hit_points(410)|body_armor(21)|spd_rtng(21)|shield_width(29), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 3),#完美格挡时限0.3秒
    ]),
   ]], 
["lion_decorative_shield", "Lion Decorative Shield", #狮纹浮饰盾
   [("saracin_shield_test", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 540, 
   weight(3)|abundance(40)|difficulty(3)|hit_points(410)|body_armor(26)|spd_rtng(108)|shield_width(20)|shield_height(44), 
   imodbits_shield, [shield_hit_point_trigger]], 

#狮鹫佣兵团
["griffon_hunting_fan_shaped_shield", "Griffon Hunting Fan Shaped Shield", #狮鹫狩猎扇形盾
   [("shield_heater_502", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["simple_griffon_skoutarion", "Simple Griffon Skoutarion", #简易狮鹫泪形盾
   [("norman_shield_8", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(100)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["griffon_skoutarion", "Griffon Skoutarion", #狮鹫泪形盾
   [("shield_tear_17", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 550, 
   weight(3.5)|abundance(100)|difficulty(4)|hit_points(580)|body_armor(22)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

#飞马商会
["simple_pegasus_skoutarion", "Simple Pegasus Skoutarion", #简易飞马泪形盾
   [("norman_shield_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(100)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######YISHITH SHIELD#########
["clover_fan_shaped_shield", "Clover Fan-shaped Shield", #三叶草扇形盾
   [("shield_heater_810",0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,  277 , 
   weight(1.5)|abundance(80)|difficulty(0)|hit_points(320)|body_armor(20)|spd_rtng(94)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]],
["double_deer_fan_shaped_shield", "Double Deer Fan-shaped Shield", #双鹿扇形盾
   [("shield_heater_513", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(100)|shield_width(28)|shield_height(39), 
    imodbits_shield, [shield_hit_point_trigger]], 
["ranger_horn_fan_shaped_shield", "Ranger Horn Fan-shaped Shield", #巡林号角扇形盾
   [("shield_heater_516", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 420, 
   weight(2.5)|abundance(80)|difficulty(3)|hit_points(420)|body_armor(26)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["rose_knight_shield", "Rose Knight Shield", #蔷薇骑士盾
   [("cw_shield_tex", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 400, 
   weight(1.5)|abundance(100)|difficulty(3)|hit_points(470)|body_armor(23)|spd_rtng(104)|shield_width(18)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["king_deer_fan_shaped_shield", "King Deer Fan Shaped Shield", #王鹿扇形盾
   [("shield_heater_722", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 500, 
   weight(2.5)|abundance(60)|difficulty(2)|hit_points(490)|body_armor(27)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

["elf_light_shield", "Elf Light Shield", #精灵轻盾
   [("misidelong1dun", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 3800, 
   weight(0.5)|abundance(2)|difficulty(5)|hit_points(300)|body_armor(26)|spd_rtng(120)|shield_width(27)|shield_height(100), 
   imodbits_shield, [shield_hit_point_trigger]], 
["full_elf_knight_shield", "Full Elf Knight Shield", #高精灵骑士盾
   [("silvan_shield", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 5610, 
   weight(0.75)|abundance(1)|difficulty(7)|hit_points(1000)|body_armor(41)|spd_rtng(103)|shield_width(27)|shield_height(90), 
   imodbits_shield, [shield_hit_point_trigger]], 

["ice_knight_shield", "Ice Knight Shield", #急冻盾
   [("ice_knight_shield", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 30610, 
   weight(3.5)|abundance(1)|difficulty(8)|hit_points(1000)|body_armor(56)|spd_rtng(93)|shield_width(27)|shield_height(50), 
   imodbits_none, [shield_hit_point_trigger]], 

#伊希斯人类精英
["northern_cavalry_shield", "Northern Cavalry Shield", #北方骑兵盾
   [("mirkwood_med_shield", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 750, 
   weight(3)|abundance(50)|difficulty(3)|hit_points(400)|body_armor(24)|spd_rtng(86)|shield_width(27)|shield_height(45), 
   imodbits_shield, [shield_hit_point_trigger]], 
["northern_infantry_shield", "Northern Infantry Shield", #北方步兵大盾
   [("mirkwood_spear_shield", 0)], 
   itp_type_shield|itp_merchandise|itp_cant_use_on_horseback, itcf_carry_round_shield, 750, 
   weight(4.5)|abundance(50)|difficulty(4)|hit_points(500)|body_armor(25)|spd_rtng(70)|shield_width(27)|shield_height(81), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######STEPPE SHIELD#########
#格斗小圆盾
["stud_decorated_skin_battle_shield", "Stud Decorated Skin Battle Shield", #钉饰蒙皮格斗盾
   [("talak_buckler", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_buckler_left, 300, 
   weight(1)|abundance(100)|difficulty(2)|hit_points(410)|body_armor(21)|spd_rtng(110)|shield_width(15), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 6),#完美格挡时限0.6秒
    ]),
   ]], 
["spike_skin_battle_shield", "Spike Skin Battle Shield", #尖刺蒙皮格斗盾
   [("s_h1_1", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 520, 
   weight(1.5)|abundance(50)|difficulty(4)|hit_points(410)|body_armor(21)|spd_rtng(101)|shield_width(24), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),#完美格挡时限0.5秒
    ]),
   ]], 
["gorgeous_battle_shield", "kelutuohuali_yuandun", #华丽格斗盾
   [("dal_turkiv", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_buckler_left, 820, 
   weight(1.5)|abundance(40)|difficulty(4)|hit_points(450)|body_armor(23)|spd_rtng(115)|shield_width(15), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 6),#完美格挡时限0.6秒
    ]),
   ]], 

#大圆盾
["kouruto_round_shield", "Kouruto Round Shield", #科鲁托大圆盾
   [("round_shield_big_1", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 687, 
   weight(4.5)|abundance(100)|difficulty(4)|hit_points(410)|body_armor(23)|spd_rtng(81)|shield_width(45), 
   imodbits_shield, [shield_hit_point_trigger]], 
["beast_ancestor_totem_shield", "Beast Ancestor Totem Shield", #兽王图腾浮饰盾
   [("hermitage_shield_5", 0)], 
   itp_type_shield, itcf_carry_round_shield, 1600, 
   weight(4)|abundance(4)|difficulty(4)|hit_points(430)|body_armor(31)|spd_rtng(88)|shield_width(35), 
   imodbits_shield, [shield_hit_point_trigger]], 

#阔盾
["leather_broad_shield", "Leather Broad Shield", #皮制阔盾
   [("lithuanian_shield7", 0)], 
   itp_type_shield|itp_merchandise|itp_cant_use_on_horseback, itcf_carry_board_shield, 140, 
   weight(4)|abundance(100)|difficulty(3)|hit_points(430)|body_armor(15)|spd_rtng(78)|shield_width(25)|shield_height(55), 
   imodbits_shield, [shield_hit_point_trigger]], 
["leather_patterned_broad_shield", "Leather Patterned Broad Shield", #皮制花纹阔盾
   [("lithuanian_shield4", 0)], 
   itp_type_shield|itp_merchandise|itp_cant_use_on_horseback, itcf_carry_board_shield, 340, 
   weight(4.5)|abundance(100)|difficulty(3)|hit_points(430)|body_armor(17)|spd_rtng(78)|shield_width(25)|shield_height(55), 
   imodbits_shield, [shield_hit_point_trigger]], 
["kouruto_tower_shield", "Kouruto Tower Shield", #科鲁托塔盾
   [("shield_pavisei", 0)], 
   itp_type_shield|itp_merchandise|itp_cant_use_on_horseback, itcf_carry_board_shield, 480, 
   weight(5)|abundance(80)|difficulty(4)|hit_points(550)|body_armor(22)|spd_rtng(68)|shield_width(32)|shield_height(88), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######CONFEDERATION SHIELD#########
["slave_rotten_wooden_shield", "Slave Rotten Wooden Shield", #奴隶破木盾
   [("ad_viking_shield_round_07", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 35, 
   weight(3)|abundance(100)|difficulty(0)|hit_points(260)|body_armor(8)|spd_rtng(61)|shield_width(35), 
   imodbits_shield, [shield_hit_point_trigger]], 

["half_bird_fan_shaped_shield", "Half Bird Fan Shaped Shield", #半鸟扇形盾
   [("shield_heater_213", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 330, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(400)|body_armor(21)|spd_rtng(88)|shield_width(52)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 
["haze_crow_fan_shaped_shield", "Haze Crow Fan Shaped Shield", #霾鸦扇形盾
   [("shield_heater_412", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["phoenix_fan_shaped_shield", "Phoenix Fan Shaped Shield", #神鸟扇形盾
   [("shield_heater_501", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 600, 
   weight(2.5)|abundance(40)|difficulty(4)|hit_points(480)|body_armor(29)|spd_rtng(92)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

["thunderwing_fan_shaped_shield", "Thunderwing Fan Shaped Shield", #雷翼扇形盾，落雷特效
   [("shield_heater_304", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 2360, 
   weight(2.5)|abundance(5)|difficulty(5)|hit_points(520)|body_armor(30)|spd_rtng(70)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

["aquila_relief_shield", "Aquila Relief Shield", #翼佑椭圆盾
   [("saracin_shield_test_1", 0)], 
   itp_type_shield, itcf_carry_round_shield, 440, 
   weight(2.500000)|abundance(100)|difficulty(2)|hit_points(410)|body_armor(24)|spd_rtng(90)|shield_width(20)|shield_height(50), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 10),#完美格挡时限1秒
    ]),
   ]],

["winged_board_shield", "Winged Board Shield", #翼纹阔盾
   [("roman_shield_square", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 780, 
   weight(5)|abundance(70)|difficulty(4)|hit_points(600)|body_armor(28)|spd_rtng(63)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["winged_elliptical_tower_shield", "Winged Elliptical Tower Shield", #翼纹椭圆塔盾
   [("roman_shield_oval", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 480, 
   weight(5)|abundance(100)|difficulty(4)|hit_points(600)|body_armor(20)|spd_rtng(63)|shield_width(30)|shield_height(83), 
   imodbits_shield, [shield_hit_point_trigger]], 
["winged_tower_shield", "Winged Tower Shield", #翼纹塔盾
   [("roman_shield_cav_2", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 480, 
   weight(5)|abundance(20)|difficulty(5)|hit_points(650)|body_armor(21)|spd_rtng(60)|shield_width(32)|shield_height(101), 
   imodbits_shield, [shield_hit_point_trigger]], 

#净世军
["crow_hunting_fan_shaped_shield", "Crow Hunting Fan Shaped Shield", #猎鸦扇形盾
   [("shield_heater_517", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2.500000)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["aquila_guard_shield", "Aquila Guard Shield", #翼卫扇形盾
   [("shield_heater_404", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 430, 
   weight(2.5)|abundance(70)|difficulty(3)|hit_points(440)|body_armor(26)|spd_rtng(91)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["aquila_skoutarion", "Aquila Skoutarion", #翼卫三角盾
   [("shield_kite_k", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 540, 
   weight(3)|abundance(70)|difficulty(3)|hit_points(480)|body_armor(27)|spd_rtng(86)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 

["blue_gliding_eagle_shield", "Blue Gliding Eagle Shield", #蓝色鹰雕仪式盾
   [("xuexiaojdun", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_kite_shield, 1040, 
   weight(5.500000)|abundance(1)|difficulty(4)|hit_points(510)|body_armor(28)|spd_rtng(65)|shield_width(37)|shield_height(71), 
   imodbits_shield, [shield_hit_point_trigger]], 
["iron_eagle_shield", "Iron Eagle Shield", #鹰隼纯铁大骑盾
   [("corprus_falcon_kite_shield", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 840, 
   weight(4.000000)|abundance(100)|difficulty(5)|hit_points(710)|body_armor(44)|spd_rtng(80)|shield_width(27)|shield_height(58), 
   imodbits_shield, [shield_hit_point_trigger]], 

["purifier_eagle_tower_shield", "Purifier Eagle Tower Shield", #净世军鹰塔盾
   [("spak_pavise_1", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 1670, 
   weight(6.000000)|abundance(10)|difficulty(4)|hit_points(1000)|body_armor(23)|spd_rtng(40)|shield_width(34)|shield_height(76), 
   imodbits_shield, [shield_hit_point_trigger]], 

["purifier_fan_shaped_shield", "Purifier Fan Shaped Shield", #净世军扇形盾
   [("shield_knight_tevton_c", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(60)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["purifier_skoutarion", "Purifier Skoutarion", #净世军三角盾
   [("shield_veteran_tevton_b", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 540, 
   weight(3)|abundance(30)|difficulty(3)|hit_points(480)|body_armor(27)|spd_rtng(86)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 
["purifier_winged_knight_skoutarion", "Purifier Winged Knight Skoutarion", #净世翼军骑士盾
   [("shield_veteran_tevton_c", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 1240, 
   weight(3)|abundance(5)|difficulty(4)|hit_points(600)|body_armor(34)|spd_rtng(93)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 

#春之女神教
["nameless_goddess_shield", "Nameless Goddess Shield", #银色无名女神扇形盾
   [("chuncdun", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 750, 
   weight(3.500000)|abundance(1)|difficulty(4)|hit_points(580)|body_armor(32)|spd_rtng(82)|shield_width(28)|shield_height(42), 
   imodbits_shield, [
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_agent_no"),
        (store_agent_hit_points, ":hit_point", ":defender_agent_no", 1),
        (val_add, ":hit_point", 1),
        (agent_set_hit_points, ":defender_agent_no", ":hit_point",1),
    ]),
    shield_hit_point_trigger
   ]], 
["gliding_nameless_goddess_large_shield", "Gliding Nameless Goddess Large Shield", #金色无名女神扇形盾
   [("KTS1234", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 750, 
   weight(3.500000)|abundance(100)|difficulty(4)|hit_points(580)|body_armor(32)|spd_rtng(82)|shield_width(28)|shield_height(42), 
   imodbits_shield, [
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_agent_no"),
        (store_agent_hit_points, ":hit_point", ":defender_agent_no", 1),
        (val_add, ":hit_point", 2),
        (agent_set_hit_points, ":defender_agent_no", ":hit_point",1),
    ]),
    shield_hit_point_trigger
   ]], 


#######PAPAL SHIELD#########
["simple_papal_fan_shaped_shield", "Simple Papal Fan Shaped Shield", #简易教国扇形盾
   [("shield_heater_207", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, 
   weight(2)|abundance(100)|difficulty(1)|hit_points(380)|body_armor(20)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 
["papal_blue_skoutarion", "Papal Blue Skoutarion", #教国蓝色泪形盾
   [("shield_tear_14", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 550, 
   weight(3.5)|abundance(100)|difficulty(4)|hit_points(580)|body_armor(22)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["steel_bar_skoutarion", "Steel Bar Skoutarion", #钢条三角盾
   [("shield_kite_i", 0)], 
   itp_type_shield|itp_merchandise,itcf_carry_kite_shield, 510, 
   weight(3)|abundance(90)|difficulty(3)|hit_points(480)|body_armor(24)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

["papal_dagger", "Papal Dagger", #教国匕首
   [("knife_4_1", 0), ("knife_4_2", ixmesh_carry)], 
   itp_type_shield|itp_merchandise|itp_left_hand_weapon|itp_force_attach_left_hand, itcf_carry_dagger_front_right, 857, 
   weight(0.4)|abundance(10)|difficulty(1)|hit_points(300)|body_armor(26)|spd_rtng(125)|shield_width(20)|shield_height(5), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 4),#完美格挡时限0.4秒
    ]),

    (ti_on_shield_hit, [#反箭
        (store_trigger_param_1, ":defender_agent_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (store_trigger_param, ":missile_weapon_no", 5),

        (gt, ":missile_weapon_no", 0),#远程击中
        (call_script, "script_get_state_count", ":defender_agent_no", "itm_state_left_hand_block_arrow"),
        (gt, reg1, 0),#启动了反箭的状态

        (set_fixed_point_multiplier, 100),
        (item_get_weight, ":value_no", ":missile_weapon_no"),
        (item_get_max_ammo, ":missile_num", ":missile_weapon_no"),
        (val_sub, ":value_no", ":missile_num"),
        (le, ":value_no", 100),#投射物不重于一公斤（几乎所有的弓箭，排除了绝大部分投掷）

        (position_rotate_x, pos1, 180),
        (position_move_y, pos1, 10),
        (add_missile, ":defender_agent_no", pos1, 2000, ":attacker_weapon_no", 0, ":missile_weapon_no", 0),

        (agent_set_animation, ":defender_agent_no", "anim_left_hand_block_arrow", 1),
        (agent_get_wielded_item, ":weapon_no", ":defender_agent_no", 1),
        (agent_unequip_item, ":defender_agent_no", ":weapon_no", 2),
        (agent_equip_item, ":defender_agent_no", ":weapon_no", 2),
        (agent_set_wielded_item, ":defender_agent_no", ":weapon_no"),#清除箭矢
    ]),

    (ti_on_shield_hit, [#反击
        (store_trigger_param, ":defender_agent_no", 1),
        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
        (store_trigger_param, ":attacker_weapon", 4),

        (le, ":damage_count", 60),#伤害少于60
        (item_get_type, ":type_no", ":attacker_weapon"),
        (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type_no", itp_type_two_handed_wpn),
        (eq, ":type_no", itp_type_polearm),                                   #是近战武器
        (agent_is_human, ":attacker_agent_no"),#攻击者是人
        (agent_is_alive, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (item_get_weight, ":value_no", ":attacker_weapon"),
        (le, ":value_no", 180),#进攻武器小于1.8公斤
        (item_get_weapon_length, ":value_no", ":attacker_weapon"),
        (le, ":value_no", 130),#进攻武器小于130cm

        (agent_set_animation, ":defender_agent_no", "anim_left_hand_counterattack", 1),
        (agent_deliver_damage_to_agent, ":defender_agent_no", ":attacker_agent_no", 30),#造成伤害
    ]),
   ]], 

["papal_soldier_tower_shield", "Papal Soldier Tower Shield", #教国士兵塔盾
   [("spak_pavise_papal", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 1770, 
   weight(6.000000)|abundance(10)|difficulty(4)|hit_points(1000)|body_armor(23)|spd_rtng(40)|shield_width(34)|shield_height(76), 
   imodbits_shield, [shield_hit_point_trigger]], 
["papal_iron_tower_shield", "Papal Iron Tower Shield", #教国纯钢塔盾
   [("spak_pavise_iron", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 3970, 
   weight(20)|abundance(3)|difficulty(8)|hit_points(2000)|body_armor(63)|spd_rtng(10)|shield_width(34)|shield_height(76), 
   imodbits_shield, [shield_hit_point_trigger]], 

["papal_holy_cavalry_shield", "Papal Holy Cavalry Shield", #教国圣骑兵盾
   [("spak_knightsh", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 6870, 
   weight(2.5)|abundance(1)|difficulty(8)|hit_points(600)|body_armor(55)|spd_rtng(100)|shield_width(26)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["paladin_shield", "Paladin Shield", #圣骑士盾
   [("gd_shield", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 14870, 
   weight(2.5)|abundance(1)|difficulty(9)|hit_points(1000)|body_armor(75)|spd_rtng(100)|shield_width(20)|shield_height(49), 
   imodbits_shield, [shield_hit_point_trigger]], 

#证信宗
["exorcist_battle_shield", "Exorcist Battle Shield", #猎魔人格斗盾
   [("shields_archer_templar_b", 0)], 
   itp_type_shield, itcf_carry_round_shield, 340, 
   weight(2.5)|abundance(100)|difficulty(3)|hit_points(410)|body_armor(21)|spd_rtng(81)|shield_width(26)|shield_height(39), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 6),#完美格挡时限0.6秒
    ]),
   ]], 

["verification_fan_shaped_shield", "Verification Fan Shaped Shield", #证信宗扇形盾
   [("shield_knight_templar_e", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(70)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["exorcist_kite_shield", "Exorcist Kite Shield", #猎魔者鸢盾
   [("templar_shield_d", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 460, 
   weight(2.5)|abundance(60)|difficulty(2)|hit_points(400)|body_armor(25)|spd_rtng(100)|shield_width(21)|shield_height(53), 
   imodbits_shield, [shield_hit_point_trigger]], 
["exorcist_skoutarion", "Exorcist Skoutarion", #猎魔者三角盾
   [("shield_veteran_templar_e", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 540, 
   weight(3)|abundance(30)|difficulty(3)|hit_points(480)|body_armor(27)|spd_rtng(86)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 
["jugde_fan_shaped_shield", "Jugde Fan Shaped Shield", #审判者扇形盾
   [("shield_knight_templar_k", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 800, 
   weight(2.5)|abundance(20)|difficulty(4)|hit_points(540)|body_armor(29)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

#真信施洗会
["baptism_fan_shaped_shield", "Baptism Fan Shaped Shield", #施洗城黑白扇形盾
   [("shield_heater_305", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 330, 
   weight(2.5)|abundance(90)|difficulty(2)|hit_points(400)|body_armor(21)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 
["baptism_noble_fan_shaped_shield", "Baptism Noble Fan Shaped Shield", #施洗城贵族扇形盾
   [("shield_heater_405", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(70)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["baptism_soldier_fan_shaped_shield", "Baptism Soldier Fan Shaped Shield", #真信会士兵扇形盾
   [("shield_knight_tevton_b", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 400, 
   weight(2.5)|abundance(60)|difficulty(2)|hit_points(440)|body_armor(24)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["baptism_knight_fan_shaped_shield", "Baptism Knight Fan Shaped Shield", #真信会骑士扇形盾
   [("shield_knight_tevton_g", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 430, 
   weight(2.5)|abundance(50)|difficulty(3)|hit_points(440)|body_armor(26)|spd_rtng(91)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

["simple_baptism_skoutarion", "Simple Baptism Skoutarion", #施洗城简易泪形盾
   [("norman_shield_4", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(90)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["baptism_skoutarion", "Baptism Skoutarion", #施洗城三角盾
   [("shield_veteran_tevton_a", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 540, 
   weight(3)|abundance(30)|difficulty(3)|hit_points(480)|body_armor(27)|spd_rtng(86)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 

["eliminating_demon_tower_shield", "Eliminating Demon Tower Shield", #伐魔塔盾
   [("spak_pavise_eliminating", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 1770, 
   weight(6.000000)|abundance(10)|difficulty(4)|hit_points(1000)|body_armor(23)|spd_rtng(40)|shield_width(34)|shield_height(76), 
   imodbits_shield, [shield_hit_point_trigger]], 
["patron_tower_shield", "Patron Tower Shield", #庇护者塔盾
   [("KTSm128", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 7770, 
   weight(30)|abundance(2)|difficulty(9)|hit_points(1000)|body_armor(83)|spd_rtng(40)|shield_width(39)|shield_height(119), 
   imodbits_shield, [shield_hit_point_trigger]], 

#神哲修道宗
["theologian_small_shield", "Theologian Small Shield", #神学家小盾
   [("shields_archer_templar_a", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 340, 
   weight(3.000000)|abundance(100)|difficulty(3)|hit_points(410)|body_armor(21)|spd_rtng(81)|shield_width(26)|shield_height(39), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),#完美格挡时限0.5秒
    ]),
   ]], 
["deism_skoutarion", "Deism Skoutarion", #理神三角盾
   [("shield_veteran_templar_f", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 540, 
   weight(3)|abundance(30)|difficulty(3)|hit_points(480)|body_armor(27)|spd_rtng(86)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 
["deism_round_shield", "Deism Round Shield", #哲神圆盾
   [("dunpai4", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 1640, 
   weight(2.5)|abundance(4)|difficulty(5)|hit_points(480)|body_armor(45)|spd_rtng(84)|shield_width(32), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 4),#完美格挡时限0.4秒
    ]),
   ]], 

#圣别渴求者
["saints_painting_fan_shaped_shield", "Saints Painting Fan Shaped Shield", #圣徒绘面扇形盾
   [("shield_heater_707", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 330, 
   weight(2.5)|abundance(90)|difficulty(2)|hit_points(400)|body_armor(21)|spd_rtng(88)|shield_width(26)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["sanctification_seeker_skoutarion", "Sanctification Seeker Skoutarion", #圣别渴求三角盾
   [("shield_veteran_templar_b", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 540, 
   weight(3)|abundance(30)|difficulty(3)|hit_points(480)|body_armor(27)|spd_rtng(86)|shield_width(26)|shield_height(52), 
   imodbits_shield, [shield_hit_point_trigger]], 
["divine_right_round_shield", "Divine Right Round Shield", #神授圆盾
   [("shield_greek", 0)], 
   itp_type_shield, itcf_carry_round_shield, 1196, 
   weight(2.5)|abundance(10)|difficulty(4)|hit_points(500)|body_armor(24)|spd_rtng(84)|shield_width(32), 
   imodbits_shield, [shield_hit_point_trigger]], 

["sanctification_seeker_shield", "Sanctification Seeker Shield", #圣别渴求浮饰盾
   [("gaoduan1d", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 3844, 
   weight(4.5)|abundance(1)|difficulty(5)|hit_points(610)|body_armor(36)|spd_rtng(87)|shield_width(25)|shield_height(48), 
   imodbits_shield, [shield_hit_point_trigger]], 
["decorated_towers_shield", "Decorated Tower Shield", #鎏饰塔盾    
   [("towershield_steel", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 4600, 
   weight(14)|abundance(2)|difficulty(6)|hit_points(700)|body_armor(37)|spd_rtng(65)|shield_width(32)|shield_height(108), 
   imodbits_shield, [shield_hit_point_trigger]], 

#特殊盾牌
["sadi_dagger", "Sadi's Dagger", #萨蒂的匕首
   [("dirk", 0), ("dirk_scabbard", ixmesh_carry)],  
   itp_type_shield|itp_unique|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_dagger_front_right, 3560, 
   weight(0.5)|abundance(1)|difficulty(2)|hit_points(1000)|body_armor(30)|spd_rtng(155)|shield_width(5)|shield_height(30), 
   imodbits_none, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),#完美格挡时限0.5秒
    ]),

    (ti_on_shield_hit, [#反箭
        (store_trigger_param_1, ":defender_agent_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (store_trigger_param, ":missile_weapon_no", 5),

        (gt, ":missile_weapon_no", 0),#远程击中
        (call_script, "script_get_state_count", ":defender_agent_no", "itm_state_left_hand_block_arrow"),
        (gt, reg1, 0),#启动了反箭的状态

        (set_fixed_point_multiplier, 100),
        (item_get_weight, ":value_no", ":missile_weapon_no"),
        (item_get_max_ammo, ":missile_num", ":missile_weapon_no"),
        (val_sub, ":value_no", ":missile_num"),
        (le, ":value_no", 100),#投射物不重于一公斤（几乎所有的弓箭，排除了绝大部分投掷）

        (position_rotate_x, pos1, 180),
        (position_move_y, pos1, 10),
        (add_missile, ":defender_agent_no", pos1, 4000, ":attacker_weapon_no", 0, ":missile_weapon_no", 0),

        (agent_set_animation, ":defender_agent_no", "anim_left_hand_block_arrow", 1),
        (agent_get_wielded_item, ":weapon_no", ":defender_agent_no", 1),
        (agent_unequip_item, ":defender_agent_no", ":weapon_no", 2),
        (agent_equip_item, ":defender_agent_no", ":weapon_no", 2),
        (agent_set_wielded_item, ":defender_agent_no", ":weapon_no"),#清除箭矢
    ]),

    (ti_on_shield_hit, [#反击
        (store_trigger_param, ":defender_agent_no", 1),
        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
        (store_trigger_param, ":attacker_weapon", 4),

        (le, ":damage_count", 80),#伤害少于80
        (item_get_type, ":type_no", ":attacker_weapon"),
        (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type_no", itp_type_two_handed_wpn),
        (eq, ":type_no", itp_type_polearm),                                   #是近战武器
        (agent_is_human, ":attacker_agent_no"),#攻击者是人
        (agent_is_alive, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (item_get_weight, ":value_no", ":attacker_weapon"),
        (le, ":value_no", 200),#进攻武器小于两公斤
        (item_get_weapon_length, ":value_no", ":attacker_weapon"),
        (le, ":value_no", 140),#进攻武器小于140cm

        (agent_set_animation, ":defender_agent_no", "anim_left_hand_counterattack", 1),
        (agent_deliver_damage_to_agent, ":defender_agent_no", ":attacker_agent_no", 40),#造成伤害
    ]),
   ]], 

["exorcist_steel_shield", "Exorcist Steel Shield", #猎魔钢盾
   [("shield_crossbow", 0)], 
   itp_type_shield, itcf_carry_round_shield, 6597, 
   weight(7.25)|abundance(3)|difficulty(5)|hit_points(690)|body_armor(46)|spd_rtng(84)|shield_width(20), 
   imodbits_shield, [
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 3),#完美格挡时限0.3秒
    ]),
    shield_hit_point_trigger, 
   ]], 

["celestial_circle_white_shield", "Celestial Circle White Shield", #天环白盾
   [("shield_nord", 0)], 
   itp_type_shield|itp_unique|itp_left_hand_weapon, itcf_carry_buckler_left, 1700, 
   weight(1.5)|abundance(1)|difficulty(8)|hit_points(400)|body_armor(25)|spd_rtng(105)|shield_width(20), 
   imodbits_shield, [shield_hit_point_trigger]], 
["celestial_circle_black_shield", "Crossing Blade Black Shield", #天环黑盾
   [("shield_cross", 0)], 
   itp_type_shield|itp_unique|itp_left_hand_weapon, itcf_carry_buckler_left, 1700, 
   weight(1.5)|abundance(20)|difficulty(5)|hit_points(200)|body_armor(25)|spd_rtng(125)|shield_width(20), 
   imodbits_shield, [shield_hit_point_trigger]], 

["divine_lingering_light", "Divine Lingering Light", #神国的留光
   [("limingqishidun", 0)], 
   itp_type_shield|itp_unique, itcf_carry_kite_shield, 100000, 
   weight(2.5)|abundance(1)|difficulty(12)|hit_points(1000)|body_armor(140)|spd_rtng(130)|shield_width(38)|shield_height(49), 
   imodbits_none, [shield_hit_point_trigger]], 



#######EASTERN SHIELD#########
["ghost_cane_shield", "Ghost Cane Shield", #鬼面藤牌
   [("DaMing_tengpai", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 497, 
   weight(3.5)|abundance(100)|difficulty(3)|hit_points(480)|body_armor(22)|spd_rtng(84)|shield_width(42), 
   imodbits_shield, [shield_hit_point_trigger]], 
["loong_round_shield", "Loong Round Shield", #龙纹圆盾
   [("round01", 0)], 
   itp_type_shield, itcf_carry_round_shield, 670, 
   weight(4)|abundance(20)|difficulty(3)|hit_points(530)|body_armor(28)|spd_rtng(80)|shield_width(35), 
   imodbits_shield, [shield_hit_point_trigger]], 
["loong_shield", "Loong Shield", #龙腾盾
   [("heavy_shield2", 0)], 
   itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 700, 
   weight(2.5)|abundance(20)|difficulty(4)|hit_points(400)|body_armor(25)|spd_rtng(93)|shield_width(26)|shield_height(51), 
   imodbits_shield, [shield_hit_point_trigger]], 
["gliding_loong_round_shield", "Gliding Loong Round Shield", #金饰雕龙圆盾
   [("round_dragon_shield2", 0)], 
   itp_type_shield, itcf_carry_round_shield, 844, 
   weight(3.5)|abundance(10)|difficulty(4)|hit_points(610)|body_armor(31)|spd_rtng(81)|shield_width(30), 
   imodbits_shield, [shield_hit_point_trigger]], 
["eastern_tower_shield", "Easter Tower Shield", #东方塔盾
   [("caledonian_shield", 0)], 
   itp_type_shield|itp_merchandise|itp_cant_use_on_horseback, itcf_carry_board_shield, 750, 
   weight(4.5)|abundance(100)|difficulty(5)|hit_points(550)|body_armor(24)|spd_rtng(78)|shield_width(28)|shield_height(75), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######STARKHOOK SHIELD#########
["viola_shape_shield", "Viola Shape Shield", #琴形盾
   [("tarch_a", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, 
   itcf_carry_round_shield, 500, 
   weight(2.8)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(18)|spd_rtng(100)|shield_width(24)|shield_height(51), 
   imodbits_shield, [shield_hit_point_trigger]], 

#绯世
["blood_shell", "Blood Shell", #血壳
   [("crimson_round_shield", 0)], 
   itp_type_shield|itp_unique, 
   itcf_carry_round_shield, 5000, 
   weight(1.2)|abundance(1)|difficulty(3)|hit_points(820)|body_armor(38)|spd_rtng(100)|shield_width(32), 
   imodbits_none, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),#完美格挡时限0.5秒
    ]),
   ]], 
["blood_crow_claw_shield", "Blood Crow Claw", #血鸦钝爪
   [("crimson_gallic_shield", 0)], 
   itp_type_shield|itp_unique|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_dagger_front_right, 5745, 
   weight(0.3)|abundance(1)|difficulty(4)|hit_points(620)|body_armor(48)|shield_width(5)|shield_height(18), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["crimson_curtain", "Crimson Curtain", #猩红之幕
   [("crimson_shield", 0)], 
   itp_type_shield|itp_unique, 
   itcf_carry_round_shield, 10000, 
   weight(2.5)|abundance(1)|difficulty(4)|hit_points(1020)|body_armor(68)|shield_width(25)|shield_height(48), 
   imodbits_none, [shield_hit_point_trigger]], 


#######STATE SHIELD#########
["sire_bond_noble_shield", "Sire Bond Noble Shield", #归宗者扇形盾
   [("gaoduand", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 2844, 
   weight(4.5)|abundance(10)|difficulty(5)|hit_points(610)|body_armor(30)|spd_rtng(84)|shield_width(25)|shield_height(48), 
   imodbits_shield, [shield_hit_point_trigger]], 
["scepter_tower_shield", "Scepter Tower Shield", #束杖塔盾
   [("scepter_shield", 0)], 
   itp_type_shield, itcf_carry_board_shield, 4300, 
   weight(12.5)|abundance(4)|difficulty(6)|hit_points(650)|body_armor(34)|spd_rtng(75)|shield_width(29)|shield_height(112), 
   imodbits_shield, [shield_hit_point_trigger]], 


#######Libra SHIELD#########
["libra_fan_shaped_shield", "Libra Fan Shaped Shield", #权厄之秤扇形盾
   [("shield_heater_libra", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, 
   weight(2)|abundance(100)|difficulty(1)|hit_points(380)|body_armor(20)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 


#######UNDEAD SHIELD#########
#Necromancer Shields
["busizhe_shanxingdun", "busizhe_shanxingdun", #不死者扇形盾
   [("shield_heater_515", 0)], 
   itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(20)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(49), 
   imodbits_shield, [shield_hit_point_trigger]], 
["necro_tower_shield", "Necro Tower Shield", #死灵重塔盾
   [("shield_of_grey_knight", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 4001, 
   weight(14.5)|abundance(1)|difficulty(5)|hit_points(600)|body_armor(24)|spd_rtng(60)|shield_width(35)|shield_height(125), 
   imodbits_shield, [shield_hit_point_trigger]], 

#Zombie Shields
["ancient_papal_tower_shield", "Ancient Papal Tower Shield", #古教皇国塔盾
   [("ancient_papal_shield", 0)], 
   itp_type_shield, itcf_carry_round_shield, 6705, 
   weight(19.5)|abundance(1)|difficulty(8)|hit_points(700)|body_armor(73)|spd_rtng(40)|shield_width(35)|shield_height(125), 
   imodbits_shield, [shield_hit_point_trigger]], 

#Skeleton Shields
["bone_mound_fan_shaped_shield", "Bone Mound Fan Shaped Shield", #骨冢扇形盾
   [("pa_pop_shield_07_heretics", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 2005, 
   weight(2.5)|abundance(1)|difficulty(3)|hit_points(500)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(49), 
   imodbits_shield, [shield_hit_point_trigger]], 
["burial_unicorn_large_shield", "Burial Unicorn Large Shield", #陪葬品独角兽大盾
   [("RTY", 0)], itp_type_shield, itcf_carry_kite_shield, 1590, 
   weight(4.5)|abundance(1)|difficulty(4)|hit_points(420)|body_armor(39)|spd_rtng(77)|shield_width(32)|shield_height(42), 
   imodbits_shield, [shield_hit_point_trigger]], 

#Walker Shields
["stale_undead_shield", "Stale Undead Shield", #朽烂不死者扇形盾
   [("old_death_shield", 0)], 
   itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 3060, 
   weight(1.5)|abundance(1)|difficulty(3)|hit_points(120)|body_armor(7)|spd_rtng(20)|shield_width(28)|shield_height(49), 
   imodbits_none, [shield_hit_point_trigger]], 



#######DEMON SHIELD#########
["demon_fan_shaped_shield", "Demon Fan-shape Shield", #魔族肖像菱形盾
   [("shield_battle111", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 840, 
   weight(4.5)|abundance(1)|difficulty(4)|hit_points(550)|body_armor(32)|spd_rtng(85)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 

["lota_shield", "Lota Shield", #约塔立场盾
   [("banshen_shield", 0)], 
   itp_type_shield|itp_unique, itcf_carry_round_shield, 44444, 
   weight(13)|abundance(1)|difficulty(4)|hit_points(1000)|body_armor(170)|spd_rtng(90)|shield_width(1000), 
   imodbits_none, [shield_hit_point_trigger]], 


#######WITCHCRAFT SHIELD#########
["poison_spike_skin_battle_shield", "Poison Spike Skin Battle Shield", #毒刺蒙皮格斗盾
   [("s_h1_2", 0)], 
   itp_type_shield, itcf_carry_round_shield, 1420, 
   weight(1.5)|abundance(6)|difficulty(4)|hit_points(410)|body_armor(21)|spd_rtng(101)|shield_width(24), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),#完美格挡时限0.5秒
    ]),
   ]], 
["poison_fang_battle_shield", "Poison Fang Battle Shield", #毒牙格斗盾
   [("AYZDB", 0)], 
   itp_type_shield, itcf_carry_buckler_left, 2697, 
   weight(0.5)|abundance(100)|difficulty(4)|hit_points(420)|body_armor(22)|spd_rtng(110)|shield_width(8)|shield_height(42), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 7),#完美格挡时限0.7秒
    ]),
   ]], 

#各家族特殊盾牌
["white_tailed_dog_skoutarion", "White Tailed Dog Skoutarion", #白尾犬泪形盾
   [("norman_shield_6", 0)], 
   itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 550, 
   weight(3)|abundance(10)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["double_lizards_skoutarion", "Double Lizards Skoutarion", #双蜥泪形盾
   [("norman_shield_7", 0)], 
   itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 550, 
   weight(3)|abundance(10)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

["snake_large_round_shield", "Snake Large Round Shield", #游蛇大圆盾
   [("snakehoplon", 0)], 
   itp_type_shield, itcf_carry_round_shield, 1400, 
   weight(5)|abundance(10)|difficulty(4)|hit_points(510)|body_armor(21)|spd_rtng(71)|shield_width(45), 
   imodbits_shield, [shield_hit_point_trigger]], 
["snake_fan_shaped_shield", "Snake Fan Shaped Shield", #毒蛇扇形盾
   [("shield_heater_hc203", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 1560, 
   weight(2.5)|abundance(5)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 

["witchcraft_scorpion_shield", "Witchcraft Scorpion Shield", #巫蛊蝎塔盾
   [("witchcraft_scorpion_shield", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 3280, 
   weight(5)|abundance(1)|difficulty(5)|hit_points(650)|body_armor(40)|spd_rtng(60)|shield_width(32)|shield_height(101), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######ECLIPSE SHIELD#########
["copper_nail_round_shield", "Copper Nail Round Shield", #铜钉圆盾
   [("saracin_shield_s", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 640, 
   weight(3.5)|abundance(90)|difficulty(4)|hit_points(410)|body_armor(30)|spd_rtng(37)|shield_width(8), 
   imodbits_shield, [shield_hit_point_trigger]], 
["copper_flower_round_shield", "Copper Flower Round Shield", #铜花圆盾
   [("saracin_shield_g", 0)], 
   itp_type_shield, itcf_carry_round_shield, 740, 
   weight(3.5)|abundance(80)|difficulty(4)|hit_points(420)|body_armor(31)|spd_rtng(37)|shield_width(8), 
   imodbits_shield, [shield_hit_point_trigger]], 
["copper_painted_round_shield", "Copper Painted Round Shield", #铜纹圆盾
   [("bandit_shield_e", 0)], 
   itp_type_shield, itcf_carry_round_shield, 840, 
   weight(3.7)|abundance(70)|difficulty(4)|hit_points(440)|body_armor(33)|spd_rtng(37)|shield_width(8), 
   imodbits_shield, [shield_hit_point_trigger]], 

["brass_solar_tower_shield", "Brass Solar Tower Shield", #黄铜日耀塔盾
   [("lamtc", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield, 5000, 
   weight(20)|abundance(1)|difficulty(8)|hit_points(720)|body_armor(55)|spd_rtng(25)|shield_width(35)|shield_height(88), 
   imodbits_shield, [shield_hit_point_trigger]], 

["febrilagma_shield", "Febrilagma Shield", #浊热之影
   [("shield22_a", 0)], 
   itp_type_shield|itp_unique, itcf_carry_kite_shield, 80000, 
   weight(3.5)|abundance(1)|difficulty(6)|hit_points(1310)|body_armor(71)|spd_rtng(71)|shield_width(26)|shield_height(56), 
   imodbits_none, [shield_hit_point_trigger]], 



#######ABYSS SHIELD#########
["nordic_shield", "Wsetcoast Wooden Shield", #西海木圆盾 
   [("shield_round_b", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 50,  
   weight(3.5)|abundance(100)|difficulty(2)|hit_points(440)|body_armor(9)|spd_rtng(80)|shield_width(30), 
   imodbits_shield, [shield_hit_point_trigger]], 
["round_shield", "Westcoast Round Shield", #西海圆盾
   [("shield_round_c",0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 150,  
   weight(4)|abundance(100)|difficulty(3)|hit_points(440)|body_armor(15)|spd_rtng(80)|shield_width(30), 
   imodbits_shield, [shield_hit_point_trigger]], 
["blue_breeze_round_shield", "Blue Breeze Round Shield", #青风圆盾
   [("round617", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 444, 
   weight(3)|abundance(100)|difficulty(4)|hit_points(410)|body_armor(24)|spd_rtng(81)|shield_width(30), 
   imodbits_shield, [
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 3),  #完美格挡时限0.3秒
    ]),
    shield_hit_point_trigger
   ]], 

["sea_monster_fan_shaped_shield", "Sea Monster Fan Shaped Shield", #海怪扇形盾
   [("shield_heater_605", 0)], 
   itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 330, 
   weight(2.5)|abundance(90)|difficulty(2)|hit_points(400)|body_armor(21)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 
["hippocampus_skoutarion", "Hippocampus Skoutarion", #海马筝形盾
   [("shield_kite102", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(90)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

["simple_green_wind_skoutarion", "Simple Green Wind Skoutarion", #简易绿四风泪形盾
   [("norman_shield_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(100)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 
["simple_red_wind_skoutarion", "Simple Red Wind Skoutarion", #简易红四风泪形盾
   [("norman_shield_5", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 450, 
   weight(3)|abundance(100)|difficulty(3)|hit_points(480)|body_armor(21)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]], 

["sea_apostle_round_shield", "Sea Apostle Round Shield", #海神使徒圆盾
   [("round_dragon_shield", 0)], 
   itp_type_shield|itp_unique, itcf_carry_round_shield, 2460, 
   weight(3.5)|abundance(1)|difficulty(4)|hit_points(420)|body_armor(39)|spd_rtng(75)|shield_width(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["pectoral_shield", "Pectoral Shield", #鳍状盾
   [("deep_diver_shield", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 2050, 
   weight(2.5)|abundance(10)|difficulty(3)|hit_points(400)|body_armor(28)|spd_rtng(87)|shield_width(32)|shield_height(40), 
   imodbits_shield, [shield_hit_point_trigger]], 

["deep_one_knife_shield", "Deep One Knife Shield", #鱼人匕首
   [("backhand_knife_shield", 0)], 
   itp_type_shield|itp_merchandise|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_dagger_front_right, 400, 
   weight(0.5)|abundance(50)|difficulty(1)|hit_points(400)|body_armor(23)|spd_rtng(86)|shield_width(13)|shield_height(1), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 2),#完美格挡时限0.2秒
    ]),
    (ti_on_shield_hit, [#反击
        (store_trigger_param, ":defender_agent_no", 1),
        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
        (store_trigger_param, ":attacker_weapon", 4),

        (le, ":damage_count", 25),#伤害少于25
        (item_get_type, ":type_no", ":attacker_weapon"),
        (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type_no", itp_type_two_handed_wpn),
        (eq, ":type_no", itp_type_polearm),                                   #是近战武器
        (agent_is_human, ":attacker_agent_no"),#攻击者是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_set_animation, ":defender_agent_no", "anim_left_hand_counterattack", 1),
        (agent_deliver_damage_to_agent, ":defender_agent_no", ":attacker_agent_no", 25),#造成伤害
    ]),
   ]], 
["backhand_sabre_shield", "Backhand Sabre Shield", #反手剑
   [("backhand_sabre_shield", 0)], 
   itp_type_shield|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_quiver_right_vertical, 1000, 
   weight(2)|abundance(20)|difficulty(2)|hit_points(800)|body_armor(30)|spd_rtng(80)|shield_width(37)|shield_height(1), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 3),#完美格挡时限0.3秒
    ]),
    (ti_on_shield_hit, [#反击
        (store_trigger_param, ":defender_agent_no", 1),
        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
        (store_trigger_param, ":attacker_weapon", 4),

        (le, ":damage_count", 40),#伤害少于40
        (item_get_type, ":type_no", ":attacker_weapon"),
        (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type_no", itp_type_two_handed_wpn),
        (eq, ":type_no", itp_type_polearm),                                   #是近战武器
        (agent_is_human, ":attacker_agent_no"),#攻击者是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_set_animation, ":defender_agent_no", "anim_left_hand_counterattack", 1),
        (agent_deliver_damage_to_agent, ":defender_agent_no", ":attacker_agent_no", 40),#造成伤害
    ]),
   ]], 

["backhand_blade_shield", "Backhand Blade Shield", #拐刀
   [("backhand_blade_shield", 0)], 
   itp_type_shield|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_kite_shield, 1770, 
   weight(1)|abundance(10)|difficulty(3)|hit_points(900)|body_armor(33)|spd_rtng(96)|shield_width(30)|shield_height(10), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 4),#完美格挡时限0.4秒
    ]),
    (ti_on_shield_hit, [#反击
        (store_trigger_param, ":defender_agent_no", 1),
        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
        (store_trigger_param, ":attacker_weapon", 4),

        (le, ":damage_count", 60),#伤害少于60
        (item_get_type, ":type_no", ":attacker_weapon"),
        (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type_no", itp_type_two_handed_wpn),
        (eq, ":type_no", itp_type_polearm),                                   #是近战武器
        (agent_is_human, ":attacker_agent_no"),#攻击者是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_set_animation, ":defender_agent_no", "anim_left_hand_counterattack", 1),
        (agent_deliver_damage_to_agent, ":defender_agent_no", ":attacker_agent_no", 60),#造成伤害
    ]),
   ]], 
["ocean_cleaver_shield", "Ocean Cleaver Shield", #分海刃
   [("backhand_blade_2_shield", 0)], 
   itp_type_shield|itp_unique|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_kite_shield, 8260, 
   weight(2)|abundance(1)|difficulty(6)|hit_points(1000)|body_armor(40)|spd_rtng(92)|shield_width(35)|shield_height(12), 
   imodbits_shield, [
    shield_hit_point_trigger,
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),#完美格挡时限0.5秒
    ]),
    (ti_on_shield_hit, [#反击
        (store_trigger_param, ":defender_agent_no", 1),
        (store_trigger_param, ":attacker_agent_no", 2),
        (store_trigger_param, ":damage_count", 3),
        (store_trigger_param, ":attacker_weapon", 4),

        (le, ":damage_count", 80),#伤害少于80
        (item_get_type, ":type_no", ":attacker_weapon"),
        (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type_no", itp_type_two_handed_wpn),
        (eq, ":type_no", itp_type_polearm),                                   #是近战武器
        (agent_is_human, ":attacker_agent_no"),#攻击者是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_set_animation, ":defender_agent_no", "anim_left_hand_counterattack", 1),
        (agent_deliver_damage_to_agent, ":defender_agent_no", ":attacker_agent_no", 80),#造成伤害
    ]),
   ]], 



#######DESERT SHIELD#########
["malformation_shield", "Malformation Shield", #畸形盾
   [("adargag", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 330, 
   weight(2.5)|abundance(100)|difficulty(3)|hit_points(400)|body_armor(21)|spd_rtng(81)|shield_width(33)|shield_height(27), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######SABIANISM SHIELD#########
["bright_moon_small_shield", "Bright Moon Small Shield", #清月小盾
   [("roman_shield_round", 0)], 
   itp_type_shield, itcf_carry_round_shield, 640, 
   weight(1.5)|abundance(4)|difficulty(3)|hit_points(410)|body_armor(21)|spd_rtng(100)|shield_width(26), 
   imodbits_shield, [
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 5),  #完美格挡时限0.5秒
    ]),
    shield_hit_point_trigger
   ]], 



#######BARBARIAN SHIELD#########
["beast_skin_round_shield", "Beast Skin Round Shield", #兽皮小盾
   [("shield_round_f", 0)], 
   itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 40, 
   weight(2.000000)|abundance(100)|difficulty(0)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(23), 
   imodbits_shield, [
    (ti_on_shield_hit, [#完美格挡
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 1),  #完美格挡时限0.1秒
    ]),
    shield_hit_point_trigger
   ]], 
["fur_covered_shield", "Fur Covered Shield", #蒙皮盾
   [("shield_kite_m", 0)], 
   itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield, 110, 
   weight(3.500000)|abundance(100)|difficulty(0)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(24)|shield_height(68), 
   imodbits_shield, [shield_hit_point_trigger]], 



#######GILDING SHIELD#########
["gliding_round_shield", "Gliding Round Shield", #金饰圆盾
   [("lorien_round_shield", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 644, 
   weight(3.5)|abundance(30)|difficulty(3)|hit_points(410)|body_armor(25)|spd_rtng(81)|shield_width(32), 
   imodbits_shield, [shield_hit_point_trigger]], 
["gliding_fan_shaped_shield", "Gliding Fan-shaped Shield", #金饰菱形盾
   [("lorien_kite", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 700, 
   weight(3.5)|abundance(30)|difficulty(3)|hit_points(470)|body_armor(27)|spd_rtng(90)|shield_width(28)|shield_height(64), 
   imodbits_shield, [shield_hit_point_trigger]], 
["gliding_knight_fan_shaped_shield", "Gliding Knight Fan-shaped Shield", #金饰骑士扇形盾
   [("lorien_kite_small", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 760, 
   weight(3)|abundance(30)|difficulty(3)|hit_points(480)|body_armor(30)|spd_rtng(92)|shield_width(27)|shield_height(51), 
   imodbits_shield, [shield_hit_point_trigger]], 

["yellow_gorgeous_fanshaped_shield", "Yellow Gorgeous Fanshaped Shield", #黄色繁华扇形盾
   [("jdun", 0)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 2174, 
   weight(4.5)|abundance(5)|difficulty(4)|hit_points(510)|body_armor(31)|spd_rtng(78)|shield_width(28)|shield_height(58), 
   imodbits_none, [shield_hit_point_trigger]], 
["blue_gorgeous_large_fanshaped_shield", "Blue Gorgeous Large Fanshaped Shield", #蓝色繁华扇形大盾
   [("jdun0", 0)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 2204, 
   weight(5)|abundance(5)|difficulty(5)|hit_points(510)|body_armor(31)|spd_rtng(70)|shield_width(35)|shield_height(64), 
   imodbits_none, [shield_hit_point_trigger]], 


#######COMMON SHIELD#########
#平民物品
["lyre", "Lyre", #里拉琴
   [("lyre", 0)], 
   itp_type_shield|itp_wooden_parry|itp_civilian|itp_merchandise, itcf_carry_bow_back, 108, 
   weight(2.5)|abundance(100)|difficulty(0)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(9)|shield_height(63), 
   imodbits_none, [shield_hit_point_trigger]], 
["lute", "Lute", #鲁特琴
   [("lute", 0)], 
   itp_type_shield|itp_wooden_parry|itp_civilian|itp_merchandise, itcf_carry_bow_back, 118, 
   weight(2.5)|abundance(100)|difficulty(0)|hit_points(480)|body_armor(1)|spd_rtng(12)|shield_width(63), 
   imodbits_none, [shield_hit_point_trigger]], 

["claw_blade", "Claw Blade", #钩爪
   [("claw_blade", 0)],  
   itp_type_shield|itp_left_hand_weapon|itp_force_attach_left_hand, 
   itcf_carry_dagger_front_right, 2060, 
   weight(1)|abundance(1)|difficulty(4)|hit_points(1000)|body_armor(30)|spd_rtng(155)|shield_width(5)|shield_height(20), 
   imodbits_none, [shield_hit_point_trigger]], 

#圆盾
["wooden_shield", "Wooden Round Shield",#木圆盾
   [("shield_round_a", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 42, 
   weight(2)|abundance(100)|difficulty(0)|hit_points(360)|body_armor(1)|spd_rtng(80)|shield_width(35), 
   imodbits_shield, [shield_hit_point_trigger]], 

["leather_covered_round_shield", "Leather Covered Round Shield",#蒙皮圆盾 
   [("shield_round_d", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 240, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(310)|body_armor(26)|spd_rtng(96)|shield_width(28), 
   imodbits_shield, [
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 2),  #完美格挡时限0.2秒
    ]),
    shield_hit_point_trigger,
   ]],
["plate_covered_round_shield", "Plate Covered Round Shield", #覆板圆盾
   [("shield_round_e", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 440, 
   weight(4)|abundance(100)|difficulty(3)|hit_points(330)|body_armor(36)|spd_rtng(90)|shield_width(28), 
   imodbits_shield, [
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 3),  #完美格挡时限0.3秒
    ]),
    shield_hit_point_trigger,
   ]], 
["steel_shield", "Steel Shield", #钢盾
   [("shield_dragon", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 697, 
   weight(4.5)|abundance(70)|difficulty(4)|hit_points(700)|body_armor(47)|spd_rtng(91)|shield_width(20), 
   imodbits_shield, [
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 3),#完美格挡时限0.3秒
    ]),
    shield_hit_point_trigger, 
   ]], 

["tab_shield_round_a", "Old Round Shield",#破圆盾
   [("tableau_shield_round_5", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 26, 
   weight(2.5)|abundance(100)|difficulty(0)|hit_points(195)|body_armor(4)|spd_rtng(81)|shield_width(35), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 
["tab_shield_round_b", "Plain Round Shield", #粗制圆盾
   [("tableau_shield_round_3", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 85, 
   weight(3)|abundance(100)|difficulty(0)|hit_points(260)|body_armor(8)|spd_rtng(81)|shield_width(35), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 

["tab_shield_small_round_a", "Plain Pider Round Shield",#简易骑手圆盾 
   [("tableau_shield_small_round_3", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 96, 
   weight(2)|abundance(100)|difficulty(0)|hit_points(160)|body_armor(8)|spd_rtng(85)|shield_width(30), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 
["tab_shield_round_c", "Painted Round Shield", #绘面圆盾
   [("tableau_shield_round_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 160, 
   weight(3.5)|abundance(100)|difficulty(2)|hit_points(310)|body_armor(12)|spd_rtng(81)|shield_width(35), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 
["tab_shield_small_round_b", "Cavalry Round Shield", #骑兵圆盾
   [("tableau_shield_small_round_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 260, 
   weight(2.5)|abundance(100)|difficulty(0)|hit_points(200)|body_armor(16)|spd_rtng(83)|shield_width(33), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 
["tab_shield_small_round_c", "Elite Cavalry Round Shield", #精锐骑兵圆盾
   [("tableau_shield_small_round_2", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_round_shield, 420, 
   weight(3)|abundance(100)|difficulty(0)|hit_points(350)|body_armor(22)|spd_rtng(85)|shield_width(33), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 

["tab_shield_round_d", "Heavy Round Shield",#重型圆盾 
   [("tableau_shield_round_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_round_shield, 300, 
   weight(4.5)|abundance(100)|difficulty(4)|hit_points(350)|body_armor(18)|spd_rtng(81)|shield_width(40), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":var_0", ":var_1"),
    ]),
   shield_hit_point_trigger
   ]], 
["tab_shield_round_e", "Warrior Round Shield",#武卫圆盾
   [("tableau_shield_round_4", 0)], 
   itp_type_shield|itp_cant_use_on_horseback, itcf_carry_round_shield, 610, 
   weight(4.5)|abundance(100)|difficulty(4)|hit_points(410)|body_armor(27)|spd_rtng(81)|shield_width(45), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":var_0", ":var_1"),
    ]),
    (ti_on_shield_hit, [
        (store_trigger_param_1, ":defender_no"),
        (store_trigger_param_2, ":attacker_no"),
        (store_trigger_param, ":attacker_weapon_no", 4),
        (call_script, "script_cf_shield_against_common", ":defender_no", ":attacker_no", ":attacker_weapon_no", 1),#完美格挡时限0.1秒
    ]),
    shield_hit_point_trigger,
   ]], 


#扇形盾
["tab_shield_heater_a", "Old Heater Shield",#粗制扇形盾 
   [("tableau_shield_heater_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 36, 
   weight(2)|abundance(100)|difficulty(0)|hit_points(280)|body_armor(6)|spd_rtng(96)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger
   ]], 
["tab_shield_heater_b", "Plain_Heater_Shield", #简易扇形盾
   [("tableau_shield_heater_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 70, 
   weight(2.5)|abundance(100)|difficulty(0)|hit_points(360)|body_armor(11)|spd_rtng(93)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_heater_c", "Heater_Shield", #绘面扇形盾
   [("tableau_shield_heater_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 160, 
   weight(3)|abundance(100)|difficulty(0)|hit_points(430)|body_armor(14)|spd_rtng(90)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_heater_d", "Heavy_Heater_Shield", #重扇形盾
   [("tableau_shield_heater_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 160, 
   weight(3.500000)|abundance(100)|difficulty(0)|hit_points(510)|body_armor(19)|spd_rtng(87)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_heater_cav_a", "Horseman's_Heater_Shield", #骑兵扇形盾
   [("tableau_shield_heater_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 110, 
   weight(2.000000)|abundance(100)|difficulty(0)|hit_points(300)|body_armor(16)|spd_rtng(103)|shield_width(22)|shield_height(50), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_heater_cav_b", "Knightly_Heater_Shield", #骑士扇形盾
   [("tableau_shield_heater_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 360, 
   weight(2.500000)|abundance(100)|difficulty(0)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(22)|shield_height(50), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 

["simple_black_white_fan_shaped_shield", "Simple Black White Fan Shaped Shield", #简易黑白扇形盾
   [("shield_heater_306", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, 
   weight(2)|abundance(100)|difficulty(1)|hit_points(380)|body_armor(20)|spd_rtng(88)|shield_width(26)|shield_height(37), 
   imodbits_shield, [shield_hit_point_trigger]], 
["black_white_fan_shaped_shield", "Black White Fan Shaped Shield", #黑白扇形盾
   [("shield_knight_templar_a", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(28)|shield_height(39), 
   imodbits_shield, [shield_hit_point_trigger]], 
["black_white_kite_shield", "Black White Kite Shield", #黑白鸢盾
   [("templar_shield_a", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 360, 
   weight(2.5)|abundance(100)|difficulty(2)|hit_points(420)|body_armor(23)|spd_rtng(90)|shield_width(21)|shield_height(53), 
   imodbits_shield, [shield_hit_point_trigger]], 
["knight_black_white_fan_shaped_shield", "Knight Black White Fan Shaped Shield", #骑士黑白菱形盾
   [("shield_battle109", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 460, 
   weight(3)|abundance(100)|difficulty(2)|hit_points(500)|body_armor(25)|spd_rtng(91)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 
["black_and_white_skoutarion", "Black and White Skoutarion", #黑白泪形盾
   [("shield_kite_h", 0)], 
   itp_type_shield|itp_merchandise, itcf_carry_kite_shield, 550, 
   weight(3)|abundance(100)|difficulty(4)|hit_points(580)|body_armor(26)|spd_rtng(82)|shield_width(21)|shield_height(53), 
   imodbits_shield, [shield_hit_point_trigger]], 

["rune_fan_shaped_shield", "Rune Fan-shaped Shield", #符文菱形盾
   [("aqs_shield6", 0)], 
   itp_type_shield, itcf_carry_kite_shield, 8840, 
   weight(4.5)|abundance(1)|difficulty(6)|hit_points(850)|body_armor(62)|spd_rtng(95)|shield_width(20)|shield_height(32), 
   imodbits_shield, [shield_hit_point_trigger]], 



#筝形盾
["tab_shield_kite_a", "Old Kite Shield", #破筝形盾
   [("tableau_shield_kite_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 33, 
   weight(2)|abundance(100)|difficulty(0)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_kite_b", "Plain Kite Shield",#粗制筝形盾 
   [("tableau_shield_kite_3", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 70, 
   weight(2.5)|abundance(100)|difficulty(0)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_kite_c", "Kite Shield", #绘面筝形盾
   [("tableau_shield_kite_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 80, 
   weight(3)|abundance(100)|difficulty(2)|hit_points(350)|body_armor(14)|spd_rtng(100)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_kite_d", "Heavy_Kite_Shield", #筝形盾
   [("tableau_shield_kite_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 160, 
   weight(3.5)|abundance(100)|difficulty(3)|hit_points(515)|body_armor(18)|spd_rtng(87)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_kite_cav_a", "Horseman's_Kite_Shield", #骑兵筝形盾
   [("tableau_shield_kite_4", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 300, 
   weight(2.500000)|abundance(100)|difficulty(4)|hit_points(450)|body_armor(18)|spd_rtng(90)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_kite_cav_b", "Knightly_Kite_Shield", #骑士筝形盾
   [("tableau_shield_kite_4", 0)], 
   itp_type_shield|itp_merchandise,itcf_carry_kite_shield, 400, 
   weight(2.5)|abundance(100)|difficulty(4)|hit_points(470)|body_armor(25)|spd_rtng(90)|shield_width(18)|shield_height(52), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 

["gorgeous_skoutarion", "Gorgeous Skoutarion", #华丽筝形盾
   [("shield_kite113", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 950, 
   weight(3.5)|abundance(30)|difficulty(4)|hit_points(780)|body_armor(31)|spd_rtng(83)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]],  
["blue_purple_triangular_shield", "Blue Purple Triangular Shield", #蓝紫筝形盾
   [("shield_kite_g",0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry,itcf_carry_kite_shield, 400, 
   weight(3)|abundance(100)|difficulty(3)|hit_points(420)|body_armor(20)|spd_rtng(82)|shield_width(20)|shield_height(72), 
   imodbits_shield, [shield_hit_point_trigger]],


#阔盾
["wooden_board_shield", "Wooden Board Shield", #木板阔盾
   [("wooden_bari", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_round_shield, 30, 
   weight(3)|abundance(100)|difficulty(0)|hit_points(200)|body_armor(8)|spd_rtng(78)|shield_width(26)|shield_height(54), 
   imodbits_shield, [shield_hit_point_trigger]], 
["tab_shield_pavise_a", "Old Board Shield", #破阔盾
   [("tableau_shield_pavise_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 60, 
   weight(3.5)|abundance(100)|difficulty(1)|hit_points(280)|body_armor(10)|spd_rtng(78)|shield_width(32)|shield_height(68), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_pavise_b", "Plain Board Shield", #粗制阔盾
   [("tableau_shield_pavise_2", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 170, 
   weight(4)|abundance(100)|difficulty(2)|hit_points(360)|body_armor(14)|spd_rtng(78)|shield_width(32)|shield_height(68), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_pavise_c", "Board_Shield", #绘面阔盾
   [("tableau_shield_pavise_1", 0)], 
   itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 300, 
   weight(4.5)|abundance(100)|difficulty(3)|hit_points(430)|body_armor(21)|spd_rtng(78)|shield_width(32)|shield_height(68), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 
["tab_shield_pavise_d", "Heavy_Board_Shield", #重阔盾
   [("tableau_shield_pavise_1", 0)], 
   itp_type_shield|itp_merchandise|itp_cant_use_on_horseback, itcf_carry_board_shield, 480, 
   weight(6)|abundance(100)|difficulty(4)|hit_points(550)|body_armor(27)|spd_rtng(78)|shield_width(32)|shield_height(68), 
   imodbits_shield, [
    (ti_on_init_item, [
        (store_trigger_param_1, ":var_0"),
        (store_trigger_param_2, ":var_1"),
        (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":var_0", ":var_1"),
    ]),
    shield_hit_point_trigger,
   ]], 





#ONEHAND / TWOHAND WEAPON
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["hand_weapon_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######POWELL WEAPON#########
#Powell Swords
["powell_noble_sword", "Powell Noble Sword", #普威尔贵胄剑
   [("vikingswordf", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 700, 
   weight(1.5)|abundance(40)|difficulty(0)|weapon_length(102)|spd_rtng(109)|swing_damage(34, cut)|thrust_damage(27, pierce), 
   imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_get_troop_id, ":troop_no", ":attacker_agent_no"),
        (troop_is_hero, ":troop_no"),
        (store_random_in_range, ":count_no", 0, 5),#五分之一机率
        (eq, ":count_no", 1),
        (call_script, "script_dragon_power_add", ":troop_no", 1, 0, 2),
    ]),
   ]], 
["powell_noble_hand_and_a_half_sword", "Powell Noble Hand and a Half Sword", #普威尔贵胄手半剑
   [("scottish_claymore", 0)], 
   itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_back, 1037, 
   weight(3)|abundance(20)|difficulty(12)|weapon_length(141)|spd_rtng(104)|swing_damage(37, cut)|thrust_damage(30, pierce), 
   imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_get_troop_id, ":troop_no", ":attacker_agent_no"),
        (troop_is_hero, ":troop_no"),
        (store_random_in_range, ":count_no", 0, 3),#三分之一机率
        (eq, ":count_no", 1),
        (call_script, "script_dragon_power_add", ":troop_no", 1, 0, 3),
    ]),
   ]], 
["powell_knight_sword", "Powell Knight Sword", #普威尔骑士剑
   [("knight_sword", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 
   itc_longsword|itcf_carry_sword_left_hip, 1955, 
   weight(2.25)|abundance(20)|difficulty(11)|weapon_length(105)|spd_rtng(98)|swing_damage(38, cut)|thrust_damage(21, pierce), 
   imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (agent_get_troop_id, ":troop_no", ":attacker_agent_no"),
        (troop_is_hero, ":troop_no"),
        (call_script, "script_dragon_power_add", ":troop_no", 1, 0, 4),
    ]),
   ]], 
["nanfang_cijian", "nanfang_cijian", [("mackie_swordcane_blade", 0), ("mackie_swordcane_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_thrust_onehanded|itcf_horseback_thrust_onehanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 826, weight(1.000000)|abundance(20)|difficulty(15)|weapon_length(83)|spd_rtng(120)|swing_damage(0, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Powell Hoes
["fighting_pick", "Fighting_Pick", [("fighting_pick_new", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_mace_left_hip, 50, weight(1.000000)|abundance(100)|difficulty(0)|weapon_length(70)|spd_rtng(98)|swing_damage(25, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["military_sickle_a", "Military_Sickle", [("military_sickle_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary,  itc_scimitar|itcf_carry_axe_left_hip, 224, weight(1.000000)|abundance(100)|difficulty(9)|weapon_length(75)|spd_rtng(100)|swing_damage(26, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["military_pick", "Military_Pick", [("steel_pick_new", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_mace_left_hip, 175, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(70)|spd_rtng(97)|swing_damage(32, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["mogang_duanlian", "mogang_duanlian", [("AN_whammer02b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through, itc_scimitar|itcf_carry_axe_back, 896, weight(3.250000)|abundance(30)|difficulty(12)|weapon_length(77)|spd_rtng(103)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["zhanshi_chu", "zhanshi_chu", [("steel_pick_ex", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 743, weight(2.000000)|abundance(50)|difficulty(10)|weapon_length(62)|spd_rtng(90)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["qishi_chu", "qishi_chu", [("QSJC", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_extra_penetration, itc_scimitar|itcf_carry_axe_left_hip, 1290, weight(2.250000)|abundance(40)|difficulty(13)|weapon_length(100)|spd_rtng(86)|swing_damage(40, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["heavy_mattock", "Heavy Mattock", [("crow_molot", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through, itc_greatsword|itcf_carry_axe_back, 823, weight(4.750000)|abundance(40)|difficulty(17)|weapon_length(114)|spd_rtng(84)|swing_damage(40, pierce)|thrust_damage(18, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Powell Axes
["qishi_dingtouchui", "qishi_dingtouchui", [("QSDC", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_back, 2550, weight(4.000000)|abundance(20)|difficulty(18)|weapon_length(134)|spd_rtng(80)|swing_damage(38, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["qishi_danshouzhanfu", "qishi_danshouzhanfu", [("realknightaxe", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_axe_back, 610, weight(1.500000)|abundance(40)|difficulty(12)|weapon_length(86)|spd_rtng(105)|swing_damage(46, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["qishi_zhongfu", "qishi_zhongfu", [("JTZF", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_bastardsword|itcf_carry_sword_back, 1500, weight(2.250000)|abundance(40)|difficulty(15)|weapon_length(170)|spd_rtng(90)|swing_damage(45, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Powell Transcendent Weapons
["longshenjian", "longshenjian", [("SerpentSword", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_greatsword|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_carry_sword_left_hip, 100000, weight(2.500000)|abundance(1)|difficulty(10)|weapon_length(146)|spd_rtng(170)|swing_damage(127, pierce)|thrust_damage(127, pierce), imodbits_none, [weapon_visual_effect_trigger]], 


#######YISHITH WEAPON#########
#Elf Soldier Weapons
["yishith_dagger", "Yishith Dagger", #伊希斯匕首
   [("mirkwood_white_knife", 0), ("scab_mirkwood_white_knife", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_merchandise, 
   itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 136, 
   weight(0.5)|abundance(70)|difficulty(0)|weapon_length(52)|spd_rtng(117)|swing_damage(24, cut)|thrust_damage(20, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["yixisi_qingliangjian", "yixisi_qingliangjian", [("bb_holed_blade_sword", 0), ("bb_holed_blade_sword_scabard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 346, weight(0.750000)|abundance(60)|difficulty(0)|weapon_length(93)|spd_rtng(117)|swing_damage(28, cut)|thrust_damage(20, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yixisi_wandao", "yixisi_wandao", [("pa_sword_02", 0), ("pa_sword_02_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 431, weight(1.000000)|abundance(30)|difficulty(0)|weapon_length(107)|spd_rtng(102)|swing_damage(34, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yixisi_qingliang_shoubanjian", "yixisi_qingliang_shoubanjian", [("pa_sword_03", 0), ("pa_sword_03_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 522, weight(1.750000)|abundance(30)|difficulty(9)|weapon_length(150)|spd_rtng(100)|swing_damage(32, cut)|thrust_damage(26, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yixisi_qingliang_shuangshoujian", "yixisi_qingliang_shuangshoujian", [("pa_sword_04", 0), ("pa_sword_04_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 547, weight(2.000000)|abundance(30)|difficulty(10)|weapon_length(147)|spd_rtng(97)|swing_damage(35, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yishith_dark_elf_sword", "Yishith Dark Elf Sword", #伊希斯暗精灵剑
   [("pa_sword_06", 0), ("pa_sword_06_scabbard", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 410, 
   weight(1.000000)|abundance(20)|difficulty(0)|weapon_length(102)|spd_rtng(113)|swing_damage(34, cut)|thrust_damage(25, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

#High Elf Weapons
["yishith_gorgeous_sword", "Yishith Gorgeous Sword", #伊希斯华丽剑
   [("misidelong1jianA", 0), ("misidelong1jianAjianshao", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 826, 
   weight(0.500000)|abundance(20)|difficulty(9)|weapon_length(113)|spd_rtng(110)|swing_damage(37, cut)|thrust_damage(24, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yishith_forest_blessing_sword", "Yishith Forest Blessing Sword", #伊希斯林佑剑
   [("misidelong1jianB", 0), ("misidelong1jianBjianshao", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 870, 
   weight(0.500000)|abundance(20)|difficulty(9)|weapon_length(109)|spd_rtng(110)|swing_damage(38, cut)|thrust_damage(24, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yishith_knight_sword", "Yishith Knight Sword", #伊希斯骑士剑
   [("mirkwood_sword", 0), ("scab_mirkwood_sword", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_primary, 
   itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1026, 
   weight(1.000000)|abundance(10)|difficulty(10)|weapon_length(105)|spd_rtng(105)|swing_damage(38, cut)|thrust_damage(38, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Rebel Elf Weapons
["frigid_sword", "Frigid Sword", #坚寒长剑
   [("pa_sword_05", 0), ("pa_sword_05_scabbard", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 713, 
   weight(2.0)|abundance(20)|difficulty(12)|weapon_length(153)|spd_rtng(100)|swing_damage(42, cut)|thrust_damage(24, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["snow_sabre", "Snow Sabre",#雪染战刀 
   [("gwilith_1h", 0), ("gwilith_1h_sheath", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_primary, 
   itc_morningstar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1562, 
   weight(1.000000)|abundance(10)|difficulty(10)|weapon_length(105)|spd_rtng(108)|swing_damage(48, cut)|thrust_damage(0, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_of_snow_owl", "Sword of Snow Owl", #雪枭之剑
   [("xuexiaojian", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 2410, 
   weight(1.000000)|abundance(1)|difficulty(14)|weapon_length(108)|spd_rtng(110)|swing_damage(42, pierce)|thrust_damage(32, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Yishith Special Weapons
["emerald_sword", "Emerald Sword", #翡翠剑
   [("Annu_sword", 0), ("Annu_swordscab", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2020, 
   weight(0.75)|abundance(5)|difficulty(12)|weapon_length(110)|spd_rtng(110)|swing_damage(45, cut)|thrust_damage(31, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["spirit_tree_god_selection_sword", "Spirit Tree God Selection Sword", #灵树神选剑
   [("6cfelves_sword", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 12020, 
   weight(0.5)|abundance(1)|difficulty(12)|weapon_length(117)|spd_rtng(118)|swing_damage(50, pierce)|thrust_damage(39, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["snow_sword", "Snow Sword", #悲雪剑
   [("ice_knight_sword", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 13020, 
   weight(2)|abundance(1)|difficulty(18)|weapon_length(140)|spd_rtng(102)|swing_damage(57, cut)|thrust_damage(42, cut), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["verdant_hammer", "Verdant Hammer", #青葱之锤
   [("mc_druid", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_couchable, 
   itc_scimitar|itcf_carry_sword_back, 4020, 
   weight(1.250000)|abundance(1)|difficulty(16)|weapon_length(130)|spd_rtng(93)|swing_damage(34, blunt)|thrust_damage(0, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######STEPPE WEAPON#########
["therianthropy_claw", "Therianthropy Claw", #兽爪
   [("cw_no_head", 0), ("beast_tail", ixmesh_carry), ("beast_tail", ixmesh_inventory)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 0, 
   weight(10)|abundance(0)|difficulty(0)|weapon_length(10)|spd_rtng(104)|swing_damage(32, cut)|thrust_damage(24, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 

#One Hand Weapons
["kouruto_handmade_desert_sword", "Kouruto Handmade Desert Sword", #科鲁托土质沙漠剑
   [("arabian_sword_c", 0)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_primary, 
   itc_bastardsword|itcf_carry_sword_back, 116, 
   weight(4)|abundance(100)|difficulty(10)|weapon_length(123)|spd_rtng(90)|swing_damage(27, cut)|thrust_damage(19, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["kouruto_handmade_sword", "Kouruto Handmade Sword", #科鲁托土质剑
   [("andalusian_sword", 0), ("andalusian_sword_scabbard", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_primary, 
   itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 120, 
   weight(4)|abundance(100)|difficulty(0)|weapon_length(100)|spd_rtng(94)|swing_damage(28, cut)|thrust_damage(19, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 

["sword_khergit_1", "Nomad_Sabre", [("khergit_sword_b", 0), ("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 120, weight(1.250000)|abundance(100)|difficulty(0)|weapon_length(86)|spd_rtng(100)|swing_damage(29, cut)|thrust_damage(0, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_khergit_2", "Sabre", [("khergit_sword_c", 0), ("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 191, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(91)|spd_rtng(99)|swing_damage(30, cut)|thrust_damage(0, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_khergit_3", "Sabre", [("khergit_sword_a", 0), ("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 200, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(91)|spd_rtng(99)|swing_damage(31, cut)|thrust_damage(0, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_khergit_4", "Heavy_Sabre", [("khergit_sword_d", 0), ("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 233, weight(1.750000)|abundance(100)|difficulty(0)|weapon_length(88)|spd_rtng(90)|swing_damage(33, cut)|thrust_damage(0, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["kouruto_beast_sabre_simple", "Kouruto Beast Sabre Simple", #简易科鲁托猛兽剑
   [("dragondao", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_scimitar|itcf_carry_sword_left_hip, 800, 
   weight(1.5)|abundance(10)|difficulty(15)|weapon_length(83)|spd_rtng(95)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_get_horse, ":agent_horse_no", ":attacker_agent_no"),#不是骑兵
        (lt, ":agent_horse_no", 0),
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_casual_attack"),#盲击
    ]),
   ]], 

#Two Hand Swords
["duangang_shourendao", "duangang_shourendao", [("AN_warswordb", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced, itc_nodachi|itcf_carry_sword_back, 671, weight(3.750000)|abundance(70)|difficulty(17)|weapon_length(140)|spd_rtng(80)|swing_damage(41, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["mogang_shourendao", "mogang_shourendao", [("AN_warswordc", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced, itc_nodachi|itcf_carry_sword_back, 721, weight(4.000000)|abundance(70)|difficulty(17)|weapon_length(140)|spd_rtng(80)|swing_damage(42, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["kouruto_beast_sabre", "Kouruto Beast Sabre", #科鲁托猛兽剑
   [("dragondao_large", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down, 
   itc_nodachi|itcf_carry_sword_back, 2800, 
   weight(4.5)|abundance(4)|difficulty(24)|weapon_length(178)|spd_rtng(85)|swing_damage(44, cut)|thrust_damage(0, pierce), imodbits_axe, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_get_horse, ":agent_horse_no", ":attacker_agent_no"),#不是骑兵
        (lt, ":agent_horse_no", 0),
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_heavy_casual_attack"),#野盲击
    ]),
   ]], 

#Hammers
["crushing_hammer", "Crushing Hammer", #粉碎重锤
   [("BLNDC", 0)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down, 
   itc_nodachi|itcf_carry_sword_back, 926, 
   weight(4.500000)|abundance(30)|difficulty(15)|weapon_length(151)|spd_rtng(90)|swing_damage(41, pierce)|thrust_damage(0, pierce), 
   imodbits_pick, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_get_horse, ":agent_horse_no", ":attacker_agent_no"),#不是骑兵
        (lt, ":agent_horse_no", 0),
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_leap_attack"),#跳劈
    ]),
]], 
["stone_hammer", "Stone Hammer", #石重锤
   [("stonemaul", 0)], 
   itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_crush_through|itp_unbalanced, 
   itc_bastardsword|itcf_carry_axe_back, 8873, 
   weight(10)|abundance(1)|difficulty(30)|weapon_length(90)|spd_rtng(47)|swing_damage(54, blunt)|thrust_damage(0, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 


#######CONFEDERATION WEAPON#########
#Swords
["silver_winged_sword", "Silver Winged Sword", #银翼单手剑
   [("DA_sword_a", 0), ("scab_DA_sword_a", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 431, 
   weight(1.5)|abundance(40)|difficulty(0)|weapon_length(98)|spd_rtng(108)|swing_damage(31, cut)|thrust_damage(21, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_winged_long_sword", "Silver Winged Long Sword", #银翼长剑
   [("DA_sword_a_long", 0), ("scab_DA_sword_a", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 445, 
   weight(1.75)|abundance(40)|difficulty(11)|weapon_length(128)|spd_rtng(98)|swing_damage(32, cut)|thrust_damage(23, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_winged_knight_sword", "Silver Winged Knight Sword", #银翼骑士剑
   [("DA_bastard", 0), ("scab_DA_bastard", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 488, 
   weight(1.75)|abundance(40)|difficulty(10)|weapon_length(110)|spd_rtng(100)|swing_damage(34, cut)|thrust_damage(22, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_winged_noble_sword", "Silver Winged Noble Sword", #银翼贵胄剑
   [("DA_sword_b", 0), ("scab_DA_sword_b", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 523, 
   weight(1.5)|abundance(40)|difficulty(10)|weapon_length(100)|spd_rtng(113)|swing_damage(35, cut)|thrust_damage(21, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_winged_great_sword", "Silver Winged Great Sword", #银翼双手剑
   [("DA_sword_b_long", 0), ("scab_DA_sword_b", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 713, 
   weight(2.75)|abundance(40)|difficulty(12)|weapon_length(129)|spd_rtng(96)|swing_damage(38, cut)|thrust_damage(24, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

["medal_sword", "Medal Sword", #授勋剑
   [("zipaojwjian", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 523, 
   weight(1.75)|abundance(10)|difficulty(12)|weapon_length(107)|spd_rtng(98)|swing_damage(37, cut)|thrust_damage(30, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["divine_beak", "Divine Beak", #神之喙
   [("yongquanjian", 0), ("yongquanjianshao", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 523, 
   weight(2.75)|abundance(10)|difficulty(18)|weapon_length(127)|spd_rtng(98)|swing_damage(38, cut)|thrust_damage(30, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["falcon_sword", "Falcon Sword", #鹰爪单刃剑
   [("limingjian", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_back, 923, 
   weight(1.25)|abundance(1)|difficulty(14)|weapon_length(127)|spd_rtng(138)|swing_damage(40, cut)|thrust_damage(29, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

["diemer_authority_sword", "Diemer Authority Sword", #迪默权柄剑
   [("beiouwuqi3", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_unique, 
   itc_longsword|itcf_carry_sword_left_hip, 100000, 
   weight(1.5)|abundance(1)|difficulty(0)|weapon_length(114)|spd_rtng(100)|swing_damage(33, blunt)|thrust_damage(21, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 

#斧头
["carved_mattock_hammer", "Carved Mattock Hammer", #刻花鸦嘴锤
   [("xeno_war_pick01", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, 
   itc_scimitar|itcf_carry_mace_left_hip, 580, 
   weight(3.75)|abundance(40)|difficulty(14)|weapon_length(77)|spd_rtng(74)|swing_damage(33, pierce)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["simple_carving_axe", "Simple Carving Axe", #简易刻花斧
   [("vikingaxeb", 0)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_primary, 
   itc_morningstar|itcf_carry_axe_back, 500, 
   weight(3.5)|abundance(100)|difficulty(10)|weapon_length(108)|spd_rtng(90)|swing_damage(34, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["carved_one_handed_axe", "Carved One-handed Axe", #刻花单手斧
   [("AN_WarAxe", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, 
   itc_scimitar|itcf_carry_axe_left_hip, 477, 
   weight(2.75)|abundance(80)|difficulty(10)|weapon_length(69)|spd_rtng(90)|swing_damage(36, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["carved_one_handed_double_edged_axe", "Carved One-handed Double-edged Axe", #刻花单手双刃斧
   [("AN_WornDoubleAxe", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, 
   itc_scimitar|itcf_carry_sword_back, 490, 
   weight(3)|abundance(80)|difficulty(11)|weapon_length(81)|spd_rtng(82)|swing_damage(37, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["carved_double_edged_axe", "Carved Double-edged Axe", #刻花双刃斧
   [("silverruneaxe1", 0)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_primary, 
   itc_morningstar|itcf_carry_axe_back, 1000, 
   weight(4)|abundance(100)|difficulty(12)|weapon_length(103)|spd_rtng(90)|swing_damage(41, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["carved_knight_axe", "Carved Knight Axe", #刻花骑士斧
   [("AN_axe01", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, 
   itc_scimitar|itcf_carry_axe_left_hip, 823, 
   weight(3.5)|abundance(30)|difficulty(12)|weapon_length(80)|spd_rtng(88)|swing_damage(40, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["ceremonial_axe", "Ceremonial Axe", #仪仗斧
   [("beiouwuqi00", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 
   itc_scimitar|itcf_carry_axe_back, 977, 
   weight(2.75)|abundance(80)|difficulty(10)|weapon_length(79)|spd_rtng(90)|swing_damage(42, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["silver_carving_axe", "Silver Carving Axe", #银刻斧
   [("vanity413", 0)], 
   itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield, 
   itc_morningstar|itcf_carry_axe_back, 1400, 
   weight(4.25)|abundance(10)|difficulty(15)|weapon_length(152)|spd_rtng(91)|swing_damage(46, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["ancient_axe_of_phoenix", "Ancient Axe of Phoenix", #风鸟神古斧
   [("AN_axe03", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down,
   itc_nodachi|itcf_carry_axe_back, 9113, 
   weight(4.75)|abundance(10)|difficulty(17)|weapon_length(108)|spd_rtng(96)|swing_damage(50, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 


#######PAPAL WEAPON#########
#Normal Weapons
["papal_epee", "Papal Epee", #教国配重剑
   [("celtic_scabbard3", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, 
   itc_longsword|itcf_carry_sword_left_hip, 310, 
   weight(1.75)|abundance(100)|difficulty(10)|weapon_length(99)|spd_rtng(106)|swing_damage(32, cut)|thrust_damage(21, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["papal_hand_and_half_sword", "Papal Hand and Half Sword", #教国手半剑
   [("AN_sword07", 0)], 
   itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through, 
   itc_bastardsword|itcf_carry_sword_back, 2310, 
   weight(3.5)|abundance(30)|difficulty(15)|weapon_length(144)|spd_rtng(94)|swing_damage(47, cut)|thrust_damage(33, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

["papal_axe", "Papal Axe", #教国单手斧
   [("realaxea", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_scimitar|itcf_carry_axe_left_hip, 520, 
   weight(1.5)|abundance(40)|difficulty(10)|weapon_length(80)|spd_rtng(100)|swing_damage(39, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["papal_double_blade_axe", "Papal Double Blade Axe", #教国双刃斧
   [("2dblhead_ax", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, 
   itc_morningstar|itcf_carry_axe_back, 633, 
   weight(3.75)|abundance(60)|difficulty(14)|weapon_length(110)|spd_rtng(86)|swing_damage(40, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["silver_plated_sword", "Silver Plated Sword", #镀银单手剑
   [("silversword1", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 500, 
   weight(1.75)|abundance(100)|difficulty(9)|weapon_length(106)|spd_rtng(104)|swing_damage(33, cut)|thrust_damage(25, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["silver_plated_battle_sword", "Silver Plated Battle Sword", #镀银战剑
   [("boromir_sword", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 483, 
   weight(1.5)|abundance(70)|difficulty(9)|weapon_length(111)|spd_rtng(100)|swing_damage(34, cut)|thrust_damage(23, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["silver_plated_sabre", "Silver Plated Sabre", #镀银军刀
   [("Katana_New_med", 0), ("Katana_New_med_scabb", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_scimitar|itcf_carry_sword_left_hip, 734, 
   weight(2)|abundance(30)|difficulty(12)|weapon_length(104)|spd_rtng(98)|swing_damage(35, cut)|thrust_damage(0, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_plated_hand_and_half_sword", "Silver Plated Hand and Half Sword", #镀银手半剑
   [("vik1prepped3", 0)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_primary, 
   itc_bastardsword|itcf_carry_sword_back, 820, 
   weight(2.75)|abundance(50)|difficulty(10)|weapon_length(140)|spd_rtng(94)|swing_damage(37, cut)|thrust_damage(27, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_plated_exorcist_sword", "Silver Plated Exorcist Sword", #镀银狩魔剑
   [("scottish_sword_h3", 0), ("scottish_sword_scabbard_h3", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 400, 
   weight(1.25)|abundance(20)|difficulty(9)|weapon_length(76)|spd_rtng(95)|swing_damage(38, cut)|thrust_damage(32, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_great_sowrd", "Silver Great Sowrd", #镀银双手剑
   [("scottish_great_sword", 0), ("scottish_great_sword_scabbard", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1747, 
   weight(4.25)|abundance(20)|difficulty(12)|weapon_length(155)|spd_rtng(90)|swing_damage(40, cut)|thrust_damage(33, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["silver_beast_sabre", "Silver Beast Sabre", #镀银兽曲剑
   [("silver_beast_sword", 0)], 
   itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down, 
   itc_bastardsword|itcf_carry_sword_back, 2800, 
   weight(4)|abundance(15)|difficulty(19)|weapon_length(178)|spd_rtng(85)|swing_damage(41, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["silver_extra_great_sowrd", "Silver Extra Great Sowrd", #镀银特大剑
   [("boromir_great_sword", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down|itp_couchable, 
   itc_greatsword|itcf_carry_spear, 3547, 
   weight(10)|abundance(10)|difficulty(23)|weapon_length(237)|spd_rtng(67)|swing_damage(43, cut)|thrust_damage(31, blunt), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

["silver_one_handed_hammer", "Silver One Handed Hammer", #包银单手锤
   [("maul_h4", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, 
   itc_scimitar|itcf_carry_sword_back, 501, 
   weight(3)|abundance(30)|difficulty(13)|weapon_length(77)|spd_rtng(100)|swing_damage(38, blunt)|thrust_damage(0, pierce), 
   imodbits_pick, [weapon_visual_effect_trigger]], 

#Special Weapons
["heresy_hunter_sting", "Heresy Hunter Sting", #异端猎手刺刃
   [("knife_10_1", 0)], 
   itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_offset_lance, 
   itcf_thrust_onehanded|itcf_horseback_thrust_onehanded, 917, 
   weight(0.25)|abundance(20)|difficulty(0)|weapon_length(110)|spd_rtng(145)|swing_damage(0, cut)|thrust_damage(42, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["special_agent_sword", "Special Agent Sword", #特务配重剑
   [("arming_sword_h4", 0), ("arming_sword_scabbard_h4", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_can_knock_down, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 610, 
   weight(2)|abundance(20)|difficulty(11)|weapon_length(99)|spd_rtng(109)|swing_damage(37, cut)|thrust_damage(21, pierce), 
   imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_get_horse, ":agent_horse_no", ":attacker_agent_no"),#不是骑兵
        (lt, ":agent_horse_no", 0),
        (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 1),
        (gt, ":weapon_no", 0),
        (item_has_property, ":weapon_no", itp_left_hand_weapon),#左手装备左手武器
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_undercover_slash"),#潜身斩
    ]),
   ]], 
["baptized_demon_hunting_sword", "Baptized Demon Hunting Sword", #受洗猎魔剑
   [("trscs", 0), ("trscsscab", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1200, 
   weight(2)|abundance(10)|difficulty(15)|weapon_length(102)|spd_rtng(101)|swing_damage(42, cut)|thrust_damage(32, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["hymn_great_sword", "Hymn Great Sword", #圣歌双手剑
   [("Angeleron", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_greatsword|itcf_carry_sword_back, 1092, 
   weight(3)|abundance(10)|difficulty(15)|weapon_length(160)|spd_rtng(100)|swing_damage(45, cut)|thrust_damage(33, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["saint_cutter", "Saint Cutter", #剁圣刀
   [("mat2_papal", 0)], 
   itp_type_two_handed_wpn|itp_primary, 
   itc_morningstar|itcf_carry_sword_back, 7260, 
   weight(5.25)|abundance(1)|difficulty(22)|weapon_length(139)|spd_rtng(85)|swing_damage(51, pierce)|thrust_damage(0, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["paladin_sword", "Paladin Sword", #圣骑士剑
   [("guowangzhijian", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip, 8200, 
   weight(2.5)|abundance(1)|difficulty(15)|weapon_length(120)|spd_rtng(170)|swing_damage(55, pierce)|thrust_damage(52, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Papal Transcendent Weapons
["holy_sword_of_pope", "Holy Sword of Pope", #教皇之圣剑
   [("new_sword", 0), ("scab_new", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_unique|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 100000, 
   weight(1.5)|abundance(1)|difficulty(18)|weapon_length(108)|spd_rtng(120)|swing_damage(87, cut)|thrust_damage(43, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_revolt", "Holy Sword of Revolt", #首义之圣剑
   [("Aurorablade", 0)], 
   itp_type_two_handed_wpn|itp_unique|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down|itp_extra_penetration, 
   itc_greatsword|itcf_carry_sword_back, 100000, 
   weight(2.75)|abundance(1)|difficulty(21)|weapon_length(156)|spd_rtng(110)|swing_damage(77, pierce)|thrust_damage(45, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_kindness", "Holy Sword of Kindness", #慈爱之圣剑
   [("mothers_sword", 0), ("scab_mothers", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_unique|itp_primary|itp_bonus_against_shield|itp_no_pick_up_from_ground, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 100000, 
   weight(1.75)|abundance(1)|difficulty(15)|weapon_length(123)|spd_rtng(118)|swing_damage(70, cut)|thrust_damage(41, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_vanguard", "Holy Sword of Vanguard", #阵锋之圣剑
   [("Copperthorn", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_unique|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down,
   itc_greatsword|itcf_carry_sword_back, 100000, 
   weight(3.000000)|abundance(1)|difficulty(18)|weapon_length(162)|spd_rtng(108)|swing_damage(81, cut)|thrust_damage(56, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_adventure", "Holy Sword of Adventure", #历险之圣剑
   [("angeljian", 0)], 
   itp_type_two_handed_wpn|itp_unique|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down,
   itc_bastardsword|itcf_carry_sword_back, 100000, 
   weight(5)|abundance(1)|difficulty(30)|weapon_length(138)|spd_rtng(109)|swing_damage(90, pierce)|thrust_damage(50, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_gospel", "Holy Sword of Gospel", #
   [("templar_sword", 0)], 
   itp_type_one_handed_wpn|itp_unique|itp_primary|itp_can_penetrate_shield|itp_no_pick_up_from_ground, 
   itc_longsword|itcf_carry_sword_left_hip, 100000, 
   weight(1.25)|abundance(1)|difficulty(14)|weapon_length(114)|spd_rtng(123)|swing_damage(80, pierce)|thrust_damage(58, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_saintess", "Holy Sword of Saintess", #圣女之圣剑
   [("sabre_hithlain", 0), ("sabre_hithlain_scab", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_unique|itp_primary|itp_can_penetrate_shield|itp_penalty_with_shield|itp_no_pick_up_from_ground, 
   itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 100000, 
   weight(1.75)|abundance(1)|difficulty(12)|weapon_length(111)|spd_rtng(118)|swing_damage(79, cut)|thrust_damage(0, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["holy_sword_of_sniper", "Holy Sword of Sniper", #阻猎之圣剑
   [("FFVIICCSwordGenesis_ex", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_unique|itp_primary|itp_can_penetrate_shield|itp_penalty_with_shield|itp_no_pick_up_from_ground, 
   itc_greatsword|itcf_carry_sword_back, 100000, 
   weight(2.5)|abundance(1)|difficulty(17)|weapon_length(147)|spd_rtng(112)|swing_damage(80, cut)|thrust_damage(50, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 


#######EASTERN WEAPON#########
#One Hand Swords
["strange_short_sword", "Strange_Short_Sword", [("wakizashi", 0), ("wakizashi_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 430, weight(1.250000)|abundance(15)|difficulty(10)|weapon_length(65)|spd_rtng(108)|swing_damage(29, pierce)|thrust_damage(24, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["dongfang_jian", "dongfang_jian", [("fysg_weapon_jian03", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 400, weight(1.500000)|abundance(100)|difficulty(3)|weapon_length(102)|spd_rtng(110)|swing_damage(31, cut)|thrust_damage(21, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["dongfang_youxiajian", "dongfang_youxiajian", [("yuchang_jian_2", 0), ("yuchang_jianku_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 545, weight(1.750000)|abundance(60)|difficulty(9)|weapon_length(97)|spd_rtng(102)|swing_damage(33, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["huanshou_dao", "huanshou_dao", [("china_50huanshou", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1200, weight(1.800000)|abundance(100)|difficulty(9)|weapon_length(82)|spd_rtng(115)|swing_damage(37, cut)|thrust_damage(20, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["strange_sword", "Strange_Sword", [("katana", 0), ("katana_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 474, weight(2.000000)|abundance(20)|difficulty(19)|weapon_length(95)|spd_rtng(108)|swing_damage(40, cut)|thrust_damage(18, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["graghite_steel_katana", "Graghite Steel Katana", [("katana", 0), ("katana_scabbard", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_penalty_with_shield, itc_scimitar|itcf_carry_katana|itcf_show_holster_when_drawn, 1097, weight(2.250000)|abundance(30)|difficulty(15)|weapon_length(98)|spd_rtng(112)|swing_damage(41, cut)|thrust_damage(0, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Blunts
["dongfang_zhongjian", "dongfang_zhongjian", [("china_blunt", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_sword_left_hip, 1180, weight(3.250000)|abundance(20)|difficulty(15)|weapon_length(82)|spd_rtng(90)|swing_damage(38, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["guduo", "guduo", [("DaMing_guduo", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_axe_back, 590, weight(4.000000)|abundance(100)|difficulty(12)|weapon_length(94)|spd_rtng(109)|swing_damage(40, blunt)|thrust_damage(0, blunt), imodbits_pick, [weapon_visual_effect_trigger]], 

#Two Hand Swords
["sakulano_nodachi ", "Sakulano Nodachi", [("mackie_nodachi", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_bastardsword|itcf_carry_sword_back, 1694, weight(2.500000)|abundance(10)|difficulty(15)|weapon_length(125)|spd_rtng(102)|swing_damage(36, pierce)|thrust_damage(16, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["strange_great_sword", "Strange_Great_Sword", [("no_dachi", 0), ("no_dachi_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 707, weight(3.500000)|abundance(15)|difficulty(15)|weapon_length(125)|spd_rtng(98)|swing_damage(43, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["forged_steel_nodachi", "Forged Steel Nodachi", [("Katana_BIG_New_tex", 0), ("Katana_BIG_New_scabb", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 1312, weight(3.250000)|abundance(20)|difficulty(15)|weapon_length(133)|spd_rtng(94)|swing_damage(44, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_dongfanfzhanmajian", "mogang_dongfanfzhanmajian", [("Txz_td", 0), ("Txz_tdQ", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 2455, weight(2.250000)|abundance(10)|difficulty(16)|weapon_length(138)|spd_rtng(80)|swing_damage(50, cut)|thrust_damage(32, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["zhanma_dao", "zhanma_dao", [("modao", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_can_knock_down, itc_nodachi|itcf_carry_spear, 1785, weight(3.000000)|abundance(20)|difficulty(16)|weapon_length(255)|spd_rtng(93)|swing_damage(50, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Special Weapons
["prophase_enchanter_sword", "Prophase Enchanter Sword", [("fysg_weapon_mozhang", 0)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground, itc_morningstar|itcf_carry_sword_left_hip, 10000, weight(1.500000)|abundance(10)|difficulty(25)|weapon_length(150)|spd_rtng(120)|swing_damage(45, pierce)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["enchanter_sword", "Enchanter Sword", [("hanguangjian", 0), ("hanguangjian", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down|itp_extra_penetration|itp_ignore_friction, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 10000, weight(0.500000)|abundance(5)|difficulty(22)|weapon_length(200)|spd_rtng(120)|swing_damage(48, pierce)|thrust_damage(40, pierce), imodbit_well_made|imodbit_deadly|imodbit_masterwork, [weapon_visual_effect_trigger]], 
["jinjun_jian", "jinjun_jian", [("fysg_weapon_jian01", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip, 2800, weight(3.500000)|abundance(10)|difficulty(18)|weapon_length(120)|spd_rtng(120)|swing_damage(67, cut)|thrust_damage(36, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["blood_quenching", "Blood Quenching", [("uhtc", 0)], itp_type_two_handed_wpn|itp_unique|itp_no_parry|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down|itp_extra_penetration, itc_cut_two_handed|itcf_carry_katana, 30000, weight(2.250000)|abundance(1)|difficulty(30)|weapon_length(149)|spd_rtng(134)|swing_damage(74, pierce)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["sword_of_black_hair", "Sword of Black Hair", [("FC_sword", 0)], itp_type_two_handed_wpn|itp_unique|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_extra_penetration, itc_bastardsword|itcf_carry_sword_left_hip, 30000, weight(0.100000)|abundance(1)|difficulty(0)|weapon_length(123)|spd_rtng(134)|swing_damage(34, pierce)|thrust_damage(90, pierce), imodbits_none, [weapon_visual_effect_trigger]], 


#######STARKHOOK WEAPON#########
#Soldier Weapons
["longshoujian", "longshoujian", [("highlad_broadsword", 0), ("highlad_broadsword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 577, weight(1.750000)|abundance(30)|difficulty(10)|weapon_length(96)|spd_rtng(112)|swing_damage(27, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_viking_1", "Nordic_Sword", [("sword_viking_c", 0), ("sword_viking_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 171, weight(1.500000)|abundance(100)|difficulty(6)|weapon_length(96)|spd_rtng(109)|swing_damage(28, cut)|thrust_damage(20, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_viking_2_small", "Nordic_Short_Sword", [("sword_viking_b_small", 0), ("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 162, weight(1.250000)|abundance(100)|difficulty(6)|weapon_length(81)|spd_rtng(113)|swing_damage(28, cut)|thrust_damage(21, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_viking_3_small", "Nordic_Short_War_Sword", [("sword_viking_a_small", 0), ("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 191, weight(1.250000)|abundance(100)|difficulty(6)|weapon_length(81)|spd_rtng(113)|swing_damage(29, cut)|thrust_damage(21, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_viking_2", "Nordic_Sword", [("sword_viking_b", 0), ("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 192, weight(1.500000)|abundance(100)|difficulty(7)|weapon_length(95)|spd_rtng(107)|swing_damage(30, cut)|thrust_damage(21, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_viking_3", "Nordic_War_Sword", [("sword_viking_a", 0), ("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 201, weight(1.500000)|abundance(100)|difficulty(6)|weapon_length(95)|spd_rtng(109)|swing_damage(30, cut)|thrust_damage(21, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sergeant_sword", "Sergeant Sword", [("hlongsword", 0), ("hlongsword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1077, weight(1.500000)|abundance(30)|difficulty(10)|weapon_length(100)|spd_rtng(118)|swing_damage(31, blunt)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["jainyi_xifangfu", "jainyi_xifangfu", [("mackie_celtic_axe", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 740, weight(3.000000)|abundance(30)|difficulty(13)|weapon_length(100)|spd_rtng(86)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["lianren_fu", "lianren_fu", [("pa_axe_01", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_back, 546, weight(3.500000)|abundance(70)|difficulty(12)|weapon_length(80)|spd_rtng(90)|swing_damage(38, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["duangang_lianrenfu", "duangang_lianrenfu", [("new_axe", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 475, weight(2.750000)|abundance(80)|difficulty(12)|weapon_length(72)|spd_rtng(100)|swing_damage(39, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["garrison_sickle_axe", "Garrison Sickle Axe", #卫戍镰刃斧
   [("pa_axe_05", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 
   itc_scimitar|itcf_carry_axe_left_hip, 2243, 
   weight(3.5)|abundance(60)|difficulty(13)|weapon_length(70)|spd_rtng(94)|swing_damage(44, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_blood_strike"),#血星冲击
    ]),
   ]], 
["qubing_lianrenfu", "qubing_lianrenfu", [("pa_axe_06", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 866, weight(4.250000)|abundance(60)|difficulty(14)|weapon_length(105)|spd_rtng(87)|swing_damage(41, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#High Grade Weapons
["waverage_axe", "Waverage Axe", #怒涛斧
   [("butterfly_axe", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, 
   itc_nodachi|itcf_carry_sword_back, 3200, 
   weight(6.250000)|abundance(20)|difficulty(18)|weapon_length(173)|spd_rtng(83)|swing_damage(48, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["bloodburst_sword", "Bloodburst Sword", #血涌剑
   [("celtic2h3", 0)], 
   itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, 
   itc_bastardsword|itcf_carry_sword_back, 1231, 
   weight(3.750000)|abundance(20)|difficulty(16)|weapon_length(136)|spd_rtng(92)|swing_damage(49, cut)|thrust_damage(23, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["scaffold_axe", "Scaffold Axe", #手持断头台
   [("dargor_axe", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, 
   itc_nodachi|itcf_carry_axe_back, 3220, 
   weight(5.000000)|abundance(10)|difficulty(18)|weapon_length(116)|spd_rtng(86)|swing_damage(52, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["axe_of_bloddhonor", "Axe of Bloddhonor", #血勋重斧
   [("trgba", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, 
   itc_nodachi|itcf_carry_axe_back, 10220, 
   weight(8)|abundance(1)|difficulty(28)|weapon_length(122)|spd_rtng(82)|swing_damage(60, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

#绯世
["crimson_thorn", "Crimson Thorn", #绯红荆棘
   [("crimson_dragoncrusade3", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_unique, 
   itc_longsword|itcf_carry_sword_left_hip, 4474, 
   weight(0.8)|abundance(1)|difficulty(0)|weapon_length(93)|spd_rtng(104)|swing_damage(38, pierce)|thrust_damage(37, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["blood_crow_claw", "Blood Crow Claw", #血鸦利爪
   [("crimson_gallic", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_crush_through|itp_unique, 
   itc_scimitar|itcf_carry_sword_left_hip, 5745, 
   weight(0.3)|abundance(1)|difficulty(0)|weapon_length(63)|spd_rtng(144)|swing_damage(40, pierce)|thrust_damage(0, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["bloodstar", "Bloodstar", #血星
   [("crimson_gallic", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_crush_through|itp_unique|itp_bonus_against_shield|itp_can_knock_down, 
   itc_scimitar|itcf_carry_axe_left_hip, 7774, 
   weight(2.7)|abundance(1)|difficulty(0)|weapon_length(91)|spd_rtng(94)|swing_damage(44, pierce)|thrust_damage(0, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["scarlet_flame_sword", "Scarlet Flame Sword", #猩焰大剑
   [("crimson_darkzweihander1", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_crush_through|itp_unique|itp_bonus_against_shield|itp_can_knock_down, 
   itc_greatsword|itcf_carry_sword_back, 12013, 
   weight(3)|abundance(0)|difficulty(0)|weapon_length(150)|spd_rtng(98)|swing_damage(50, pierce)|thrust_damage(42, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 


#######STATE WEAPON#########
["qijing_lengtouchui", "qijing_lengtouchui", [("macear", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_sword_left_hip, 518, weight(3.250000)|abundance(100)|difficulty(12)|weapon_length(78)|spd_rtng(94)|swing_damage(34, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 


#######UNDEAD WEAPON#########
["gulou_shouzhang", "gulou_shouzhang", [("skull_club", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_sword_left_hip, 560, weight(3.500000)|abundance(10)|difficulty(12)|weapon_length(85)|spd_rtng(100)|swing_damage(31, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sword_of_ancient_knight", "Sword of Ancient Knight", [("heiyeqsword", 0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 600, weight(1.750000)|abundance(1)|difficulty(13)|weapon_length(112)|spd_rtng(91)|swing_damage(30, cut)|thrust_damage(22, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["life_divine_talisman_sword", "Life Divine Talisman Sword", [("shengguangjsjian", 0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 653, weight(1.500000)|abundance(1)|difficulty(12)|weapon_length(105)|spd_rtng(93)|swing_damage(34, cut)|thrust_damage(26, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["busi_diexuefu", "busi_diexuefu", [("wickedscythe3", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_axe_back, 3000, weight(4.000000)|abundance(10)|difficulty(18)|weapon_length(155)|spd_rtng(97)|swing_damage(47, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#僵尸武器
["burial_blunt_sword", "Burial Blunt Sword", #陪葬钝剑
   [("mirkwood_longsword", 0), ("scab_mirkwood_longsword", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 677, 
   weight(1.750000)|abundance(1)|difficulty(13)|weapon_length(80)|spd_rtng(82)|swing_damage(27, blunt)|thrust_damage(24, blunt), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

#骷髅武器
["bone_waraxe", "Bone Waraxe", [("dragonbonewaraxe", 0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 500, weight(3.500000)|abundance(10)|difficulty(12)|weapon_length(84)|spd_rtng(73)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["bone_sword", "Bone Sword", [("dragonbonesword", 0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 500, weight(2.000000)|abundance(10)|difficulty(12)|weapon_length(105)|spd_rtng(93)|swing_damage(38, cut)|thrust_damage(30, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["bone_katana", "Bone Katana", [("dragonbonekatana", 0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_katana, 500, weight(1.750000)|abundance(10)|difficulty(12)|weapon_length(108)|spd_rtng(98)|swing_damage(39, cut)|thrust_damage(27, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["bone_cutter", "Bone Cutter", [("dragonbonedaikatana", 0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 700, weight(2.000000)|abundance(10)|difficulty(14)|weapon_length(118)|spd_rtng(90)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["bone_sabre", "Bone Sabre", [("dragonbonenodachi", 0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_back, 700, weight(3.500000)|abundance(10)|difficulty(15)|weapon_length(140)|spd_rtng(83)|swing_damage(46, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["shihai_liaoyajian", "shihai_liaoyajian", [("dragonfang3", 0)], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_back, 2000, weight(4.500000)|abundance(10)|difficulty(19)|weapon_length(140)|spd_rtng(93)|swing_damage(50, cut)|thrust_damage(32, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["bone_great_sword", "Bone Great Sword", [("dragonbonegreatsword", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1000, weight(4.000000)|abundance(10)|difficulty(20)|weapon_length(138)|spd_rtng(87)|swing_damage(47, cut)|thrust_damage(35, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["busi_guzhuangjian", "busi_guzhuangjian", [("flat_sword", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 2526, weight(4.250000)|abundance(1)|difficulty(27)|weapon_length(215)|spd_rtng(93)|swing_damage(57, blunt)|thrust_damage(37, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#幽灵武器
["ghost_knife", "Ghost Knife", #灵体匕首
   [("ghost_peasant_knife", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_longsword, 100, 
   weight(0)|abundance(1)|difficulty(0)|weapon_length(45)|spd_rtng(113)|swing_damage(23, pierce)|thrust_damage(25, pierce), 
   imodbits_none, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (call_script, "script_cf_grab_skill_technique", ":attacker_agent_no", "itm_active_cutthroat"),#割喉
    ]),
   ]], 
["ghost_dagger", "Ghost Dagger", #彻骨短剑
   [("ghost_dagger", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_longsword, 400, 
   weight(0)|abundance(1)|difficulty(0)|weapon_length(49)|spd_rtng(104)|swing_damage(26, pierce)|thrust_damage(30, pierce), 
   imodbits_none, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (store_random_in_range, ":count_no", 0, 10),#十分之一概率
        (eq, ":count_no", 5),
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (agent_get_bone_position, pos1, ":attacker_agent_no", hb_item_r, 1),#右手武器处
        (agent_get_position, pos2, ":attacker_agent_no"),
        (call_script, "script_pos_copy_rotation_from_pos", pos1, pos2),#复制旋转角
        (position_move_y, pos1, -30),
        (copy_position, pos2, pos1),#向前射击
        (position_move_y, pos2, 10),
        (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
        (add_missile, ":attacker_agent_no", pos1, 1000, "itm_ghost_dagger", 0, "itm_spectre", 0),
    ]),
   ]], 
["ghost_long_sword", "Ghost Long Sword", #彻骨长剑
   [("ghost_long_sword", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_longsword, 800, 
   weight(0)|abundance(1)|difficulty(0)|weapon_length(101)|spd_rtng(94)|swing_damage(32, pierce)|thrust_damage(31, pierce), 
   imodbits_none, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (store_random_in_range, ":count_no", 0, 5),#五分之一概率
        (eq, ":count_no", 3),
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (agent_get_bone_position, pos1, ":attacker_agent_no", hb_item_r, 1),#右手武器处
        (agent_get_position, pos2, ":attacker_agent_no"),
        (call_script, "script_pos_copy_rotation_from_pos", pos1, pos2),#复制旋转角
        (position_move_y, pos1, -30),
        (copy_position, pos2, pos1),#向前射击
        (position_move_y, pos2, 10),
        (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
        (add_missile, ":attacker_agent_no", pos1, 1000, "itm_ghost_long_sword", 0, "itm_spectre", 0),
    ]),
   ]], 
["ghost_sickle", "Ghost Sickle", #午夜割喉之镰
   [("ghost_sickle", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_scimitar, 700, 
   weight(0)|abundance(1)|difficulty(0)|weapon_length(56)|spd_rtng(103)|swing_damage(29, pierce)|thrust_damage(0, pierce), 
   imodbits_none, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (call_script, "script_cf_grab_skill_technique", ":attacker_agent_no", "itm_active_cutthroat"),#割喉
    ]),
   ]], 
["ghost_steel_pick", "Ghost Steel Pick", #仇生战锄
   [("ghost_steel_pick", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_scimitar, 900, 
   weight(0)|abundance(1)|difficulty(0)|weapon_length(64)|spd_rtng(93)|swing_damage(34, pierce)|thrust_damage(0, pierce), 
   imodbits_none, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger
   ]], 

#Walker Weapons
["tuzai_zhandao", "tuzai_zhandao", [("butcher", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_sword_left_hip, 1067, weight(2.750000)|abundance(10)|difficulty(12)|weapon_length(99)|spd_rtng(98)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yanlun_kongnvefu", "yanlun_kongnvefu", [("CharonsCall", 0)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itc_bastardsword|itcf_carry_axe_back, 2345, weight(5.000000)|abundance(10)|difficulty(21)|weapon_length(113)|spd_rtng(98)|swing_damage(55, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 


#######DEMON WEAPON#########
#Worshipper Weapons
["simple_cruel_morningstar_hammer", "Simple Cruel Morningstar Hammer", #简易残虐者钉锤
   [("morningstar_3", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_unbalanced, 
   itc_scimitar|itcf_carry_axe_left_hip, 528, 
   weight(3.5)|abundance(20)|difficulty(13)|weapon_length(76)|spd_rtng(82)|swing_damage(32, pierce)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["cruel_morningstar_hammer", "Cruel Morningstar Hammer", #残虐者钉锤
   [("AN_mace02b", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 
   itc_scimitar|itcf_carry_axe_left_hip, 600, 
   weight(4)|abundance(10)|difficulty(12)|weapon_length(80)|spd_rtng(98)|swing_damage(35, pierce)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

#Demons One Hand Swords
["goblin_ancestor_sabre", "Goblin Ancestor Sabre", [("YDSWD", 0), ("YDSWDB", 0)], itp_type_one_handed_wpn|itp_unique|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 13000, weight(2.000000)|abundance(1)|difficulty(12)|weapon_length(112)|spd_rtng(105)|swing_damage(50, cut)|thrust_damage(28, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["yeyi_zhandao", "yeyi_zhandao", [("DreadweaveSword", 0)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield, itc_bastardsword|itcf_carry_katana, 12034, weight(3.000000)|abundance(5)|difficulty(21)|weapon_length(147)|spd_rtng(100)|swing_damage(45, pierce)|thrust_damage(37, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["havathang", "Havathang", [("an_sword01", 0), ("an_sword01_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 41016, weight(3.000000)|abundance(10)|difficulty(12)|weapon_length(117)|spd_rtng(120)|swing_damage(54, cut)|thrust_damage(40, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mozujundao", "mozujundao", [("AYCJ", 0), ("AYCJB", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 19025, weight(2.500000)|abundance(10)|difficulty(22)|weapon_length(125)|spd_rtng(110)|swing_damage(60, pierce)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 

#Demons Two Hand Swords
["mozu_changjian", "mozu_changjian", [("sartheron3", 0)], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_back, 10260, weight(3.250000)|abundance(10)|difficulty(18)|weapon_length(147)|spd_rtng(110)|swing_damage(53, cut)|thrust_damage(37, pierce), imodbits_sword_high, [
    (ti_on_weapon_attack, [
        (set_position_delta, 0, 75, 0),
        (particle_system_add_new, "psys_sword_magic_fire_1"),
        (particle_system_add_new, "psys_sword_magic_fire_2"),
        (set_current_color, 72, 40, 97),
        (add_point_light, 10, 30),
    ]),
    weapon_visual_effect_trigger,
]], 


#######WITCHCRAFT WEAPON#########
["dureng_jian", "dureng_jian", [("viking2h", 0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 750, weight(1.250000)|abundance(10)|difficulty(11)|weapon_length(110)|spd_rtng(112)|swing_damage(26, cut)|thrust_damage(29, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["man_cutter", "Man Cutter", #切人长刀
   [("mangshedao", 0)], 
   itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_back, 2260, 
   weight(5.25)|abundance(1)|difficulty(21)|weapon_length(139)|spd_rtng(80)|swing_damage(50, cut)|thrust_damage(0, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

["sword_of_the_insect", "Sword of the Insect", [("skycutter", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unique, itc_greatsword|itcf_carry_sword_back, 80000, weight(2.250000)|abundance(1)|difficulty(20)|weapon_length(120)|spd_rtng(93)|swing_damage(55, cut)|thrust_damage(34, pierce), imodbits_none, [weapon_visual_effect_trigger]], 


#######ECLIPSE WEAPON#########
#One Hand Swords
["copper_short_sword", "Copper Short Sword", #铜刃短剑
   [("rohansword", 0), ("rohanswordscab", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
   itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 426, 
   weight(1.25)|abundance(30)|difficulty(9)|weapon_length(96)|spd_rtng(102)|swing_damage(28, cut)|thrust_damage(19, pierce), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["duutong_goulianjian", "duutong_goulianjian", [("khopesh_1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 426, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(87)|spd_rtng(100)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 

#Two Hand Swords
["tongtie_zhongzhandao", "tongtie_zhongzhandao", [("war_concept_may09_03_03", 0), ("war_concept_may09_03_03_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_sword_back, 911, weight(4.000000)|abundance(20)|difficulty(14)|weapon_length(145)|spd_rtng(80)|swing_damage(47, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["tongtie_zhongwandao", "tongtie_zhongwandao", [("war_concept_may09_04_01_2", 0), ("war_concept_may09_04_01_scabbard_2", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, itp_type_two_handed_wpn|itcf_carry_sword_left_hip, 900, weight(3.500000)|abundance(20)|difficulty(15)|weapon_length(121)|spd_rtng(83)|swing_damage(45, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Blunt
["tongshi_juchui", "tongshi_juchui", [("mallet_h4", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_axe_back, 663, weight(6.500000)|abundance(30)|difficulty(14)|weapon_length(74)|spd_rtng(98)|swing_damage(42, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 

#Special
["sun_sword", "Sun Sword", #太阳之圣剑
   [("retribution1", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unique, 
   itc_greatsword|itcf_carry_sword_back, 100000, 
   weight(3)|abundance(1)|difficulty(20)|weapon_length(148)|spd_rtng(98)|swing_damage(35, cut)|thrust_damage(26, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["prominence", "Prominence", #日珥
   [("retribution1h", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unique|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, 
   itc_greatsword|itcf_carry_board_shield, 100000, 
   weight(3)|abundance(1)|difficulty(20)|weapon_length(148)|spd_rtng(98)|swing_damage(45, cut)|thrust_damage(30, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 


#######BARBARIAN WEAPON#########
["babarian_stone_sword", "Babarian Stone Sword", #蛮族石剑
   [("maquahuitl", 0)], 
   itp_type_two_handed_wpn|itp_primary|itp_merchandise|itp_bonus_against_shield|itp_unbalanced, 
   itc_bastardsword|itcf_carry_sword_left_hip, 694, 
   weight(4.)|abundance(30)|difficulty(12)|weapon_length(105)|spd_rtng(95)|swing_damage(33, blunt)|thrust_damage(19, blunt), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["shashijian", "shashijian", [("mackie_basehuitl_onehand", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down, itc_morningstar|itcf_carry_mace_left_hip, 928, weight(3.500000)|abundance(20)|difficulty(15)|weapon_length(69)|spd_rtng(90)|swing_damage(39, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["manzu_chui", "manzu_chui", [("pa_pop_meteoclub", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_sword_back, 756, weight(6.000000)|abundance(30)|difficulty(11)|weapon_length(68)|spd_rtng(84)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 

["barbarian_small_axe", "Barbarian Small Axe", [("h_hatchet", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_left_hip, 48, weight(2.150000)|abundance(20)|difficulty(12)|weapon_length(30)|spd_rtng(90)|swing_damage(29, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["manzushoufu", "manzushoufu", [("h_axe", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 186, weight(2.750000)|abundance(20)|difficulty(12)|weapon_length(60)|spd_rtng(87)|swing_damage(32, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]],
["manzu_gangfu", "manzu_gangfu", [("dk_lance", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 700, weight(2.250000)|abundance(40)|difficulty(14)|weapon_length(75)|spd_rtng(97)|swing_damage(45, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 


#######DESERT WEAPON#########
["arabian_sword_a", "Sarranid_Sword", [("arabian_sword_a", 0), ("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 100, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(97)|spd_rtng(109)|swing_damage(26, cut)|thrust_damage(19, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["arabian_sword_b", "Sarranid_Arming_Sword", [("arabian_sword_b", 0), ("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 210, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(97)|spd_rtng(109)|swing_damage(28, cut)|thrust_damage(19, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sarranid_cavalry_sword", "Sarranid_Cavalry_Sword", [("arabian_sword_c", 0), ("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 310, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(105)|spd_rtng(108)|swing_damage(28, cut)|thrust_damage(19, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["arabian_sword_d", "Sarranid_Guard_Sword", [("arabian_sword_d", 0), ("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 420, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(97)|spd_rtng(109)|swing_damage(30, cut)|thrust_damage(20, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["nanfang_duanjian", "nanfang_duanjian", [("shortsword1", 0), ("shortsword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 473, weight(1.250000)|abundance(30)|difficulty(9)|weapon_length(70)|spd_rtng(104)|swing_damage(31, cut)|thrust_damage(30, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["danshou_hudiedao", "danshou_hudiedao", [("mackie_falcata01", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 416, weight(1.250000)|abundance(30)|difficulty(0)|weapon_length(80)|spd_rtng(100)|swing_damage(32, cut)|thrust_damage(27, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["sand_king_guard_blade", "Sand King Guard Blade", [("mackie_godenak", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 447, weight(1.750000)|abundance(30)|difficulty(12)|weapon_length(110)|spd_rtng(90)|swing_damage(35, cut)|thrust_damage(25, cut), imodbits_sword, [weapon_visual_effect_trigger]], 

["nanfang_shuangshoujian", "nanfang_shuangshoujian", [("mackie_kriegsmesser", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back, 895, weight(3.000000)|abundance(30)|difficulty(13)|weapon_length(145)|spd_rtng(93)|swing_damage(38, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["hierarch_sword", "Hierarch Sword", [("Templarjian", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back, 30000, weight(3.250000)|abundance(1)|difficulty(20)|weapon_length(133)|spd_rtng(78)|swing_damage(44, cut)|thrust_damage(34, pierce), imodbits_none, [weapon_visual_effect_trigger]], 


#######ABYSS ORDER WEAPON#########
["haishenfu", "haishenfu", [("moghol_axe", 0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_mace_left_hip, 813, weight(3.000000)|abundance(10)|difficulty(18)|weapon_length(68)|spd_rtng(101)|swing_damage(44, cut)|thrust_damage(22, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jixingfu", "jixingfu", [("axe36", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_axe_back, 1324, weight(3.750000)|abundance(20)|difficulty(15)|weapon_length(145)|spd_rtng(92)|swing_damage(44, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["tectogene_great_sword", "Tectogene Great Sword", [("FD_sword", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unique|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back, 80000, weight(6.000000)|abundance(1)|difficulty(30)|weapon_length(183)|spd_rtng(75)|swing_damage(59, cut)|thrust_damage(40, pierce), imodbits_none, [weapon_visual_effect_trigger]], 

#反手剑
["deep_one_knife", "Deep One Knife", #鱼人匕首
   [("backhand_knife_shield", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary, 
    itc_scimitar|itcf_carry_dagger_front_left, 400, 
   weight(0.5)|abundance(50)|difficulty(0)|weapon_length(37)|spd_rtng(103)|swing_damage(28, cut), 
   imodbits_sword, [weapon_visual_effect_trigger]], 
["backhand_sabre", "Backhand Sabre", #反手剑
   [("backhand_sabre", 0), ("backhand_sabre_carry", ixmesh_carry)], 
   itp_type_one_handed_wpn|itp_primary, 
    itc_scimitar|itcf_carry_sword_left_hip, 1000, 
   weight(2)|abundance(20)|difficulty(9)|weapon_length(78)|spd_rtng(95)|swing_damage(33, cut), 
   imodbits_sword, [weapon_visual_effect_trigger]], 

["backhand_blade", "Backhand Blade", #拐刀
   [("backhand_blade", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
    itc_scimitar|itcf_carry_sword_back, 1770, 
   weight(1)|abundance(10)|difficulty(11)|weapon_length(37)|spd_rtng(108)|swing_damage(37, cut), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["ocean_cleaver", "Ocean Cleaver", #分海刃
   [("backhand_blade_2", 0)], 
   itp_type_one_handed_wpn|itp_primary, 
   itc_longsword|itcf_carry_sword_back, 8260, 
   weight(2)|abundance(1)|difficulty(16)|weapon_length(43)|spd_rtng(102)|swing_damage(43, cut), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######ADVENTURER WEAPON#########
["maoxianzhe_dajian", "maoxianzhe_dajian", [("AN_TwoHandedSword", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_bastardsword|itcf_carry_sword_back, 1544, weight(3.500000)|abundance(40)|difficulty(14)|weapon_length(150)|spd_rtng(91)|swing_damage(41, cut)|thrust_damage(31, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######JUDGMENT HAMMER WEAPON#########
["judgment_hammer", "judgment_hammer", [("YJZC", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_sword_back, 1400, weight(6.250000)|abundance(20)|difficulty(9)|weapon_length(157)|spd_rtng(123)|swing_damage(37, blunt)|thrust_damage(27, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 


#######ANCIENT WORRIER WEAPON#########
["gushi_jian", "gushi_jian", [("mackie_bastard_ori", 0), ("scab_mackie_bastard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 180, weight(1.500000)|abundance(20)|difficulty(0)|weapon_length(103)|spd_rtng(100)|swing_damage(29, cut)|thrust_damage(20, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["gushi_goujian", "gushi_goujian", [("truhs", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_left_hip, 372, weight(2.000000)|abundance(30)|difficulty(9)|weapon_length(82)|spd_rtng(110)|swing_damage(34, cut)|thrust_damage(0, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 


#######FORGED STEEL WEAPON#########
#One Hand Swords
["duangang_duanjian", "duangang_duanjian", [("short_steel_sword", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 480, weight(1.500000)|abundance(70)|difficulty(9)|weapon_length(98)|spd_rtng(108)|swing_damage(32, cut)|thrust_damage(29, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["duangang_youxiajian", "duangang_youxiajian", [("rangersword", 0), ("rangerswordscaba", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 430, weight(1.750000)|abundance(100)|difficulty(10)|weapon_length(110)|spd_rtng(106)|swing_damage(33, cut)|thrust_damage(25, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["duangang_danshoujian", "duangang_danshoujian", [("steelsword1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 640, weight(1.750000)|abundance(70)|difficulty(9)|weapon_length(114)|spd_rtng(102)|swing_damage(34, cut)|thrust_damage(27, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["duangang_youmudao", "duangang_youmudao", [("Txz_myd", 0), ("Txz_mydQ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 320, weight(1.500000)|abundance(80)|difficulty(0)|weapon_length(92)|spd_rtng(100)|swing_damage(34, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["duangang_wenshi_kuojian", "duangang_wenshi_kuojian", [("WolvenGladius", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip, 332, weight(2.000000)|abundance(30)|difficulty(9)|weapon_length(72)|spd_rtng(100)|swing_damage(36, cut)|thrust_damage(22, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["duangang_liaoyajian", "duangang_liaoyajian", [("dragoncrusade3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 640, weight(1.750000)|abundance(50)|difficulty(10)|weapon_length(101)|spd_rtng(102)|swing_damage(34, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["duangang_changjian", "duangang_changjian", [("bretonclaymore", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back, 637, weight(2.250000)|abundance(60)|difficulty(12)|weapon_length(141)|spd_rtng(98)|swing_damage(36, cut)|thrust_damage(25, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["duangang_shoubanjian", "duangang_shoubanjian", [("henrysword", 0), ("henrysword_sc", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 860, weight(3.250000)|abundance(40)|difficulty(12)|weapon_length(130)|spd_rtng(95)|swing_damage(38, cut)|thrust_damage(23, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["zhiren_duangangdao", "zhiren_duangangdao", [("katana_long", 0), ("katana_long_scabb", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 947, weight(2.000000)|abundance(20)|difficulty(14)|weapon_length(91)|spd_rtng(98)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Two Hand Swords
["duangang_zhandao", "duangang_zhandao", [("rhodocksword", 0), ("rhodockswordscaba", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 450, weight(1.750000)|abundance(100)|difficulty(10)|weapon_length(122)|spd_rtng(98)|swing_damage(35, cut)|thrust_damage(22, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["duangang_kuanrengzhandao", "duangang_kuanrengzhandao", [("rhodockswordb", 0), ("rhodockswordscaba", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 510, weight(2.000000)|abundance(100)|difficulty(11)|weapon_length(142)|spd_rtng(97)|swing_damage(36, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Axes
["duangang_shuangshoufu", "duangang_shuangshoufu", [("first_axe", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_morningstar|itcf_carry_axe_back, 945, weight(2.750000)|abundance(30)|difficulty(12)|weapon_length(96)|spd_rtng(93)|swing_damage(49, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jianyi_duangang_fu", "jianyi_duangang_fu", [("realbattleaxe", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary, itc_nodachi|itcf_carry_sword_back, 850, weight(4.750000)|abundance(100)|difficulty(12)|weapon_length(148)|spd_rtng(93)|swing_damage(43, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######GRAGHITE STEEL WEAPON#########
#One Hand Swords
["mogang_hushoujian", "mogang_hushoujian", [("darksword2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 611, weight(1.750000)|abundance(10)|difficulty(16)|weapon_length(100)|spd_rtng(113)|swing_damage(38, cut)|thrust_damage(30, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_zhanshijian", "mogang_zhanshijian", [("darksword3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 693, weight(2.000000)|abundance(10)|difficulty(18)|weapon_length(119)|spd_rtng(115)|swing_damage(41, cut)|thrust_damage(29, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_guizujian", "mogang_guizujian", [("darkbastardsword1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 631, weight(1.750000)|abundance(10)|difficulty(14)|weapon_length(102)|spd_rtng(121)|swing_damage(40, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_yizhangjian", "mogang_yizhangjian", [("darkbastardsword2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 611, weight(2.500000)|abundance(10)|difficulty(15)|weapon_length(120)|spd_rtng(110)|swing_damage(40, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_junyongjian", "mogang_junyongjian", [("darksword1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 661, weight(2.250000)|abundance(10)|difficulty(16)|weapon_length(117)|spd_rtng(117)|swing_damage(42, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_jundao", "mogang_jundao", [("demon_sword", 0), ("demon_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 781, weight(2.000000)|abundance(40)|difficulty(16)|weapon_length(100)|spd_rtng(112)|swing_damage(44, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_liaoyajian", "mogang_liaoyajian", [("darksword4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 971, weight(2.250000)|abundance(10)|difficulty(16)|weapon_length(124)|spd_rtng(118)|swing_damage(45, cut)|thrust_damage(30, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["mogang_shuangshoujian", "mogang_shuangshoujian", [("sp_2hsw", 0), ("sp_2hsw_sh", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 813, weight(3.000000)|abundance(20)|difficulty(17)|weapon_length(120)|spd_rtng(95)|swing_damage(48, cut)|thrust_damage(32, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Two Hand Swords
["mogang_changbingzhandao", "mogang_changbingzhandao", [("mackie_strange_sword", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_sword_back, 931, weight(3.250000)|abundance(20)|difficulty(15)|weapon_length(140)|spd_rtng(90)|swing_damage(43, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["graghite_steel_sabre", "Graghite Steel Sabre", [("asmoday_sword", 0), ("asmoday_sword_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 1500, weight(3.000000)|abundance(40)|difficulty(12)|weapon_length(175)|spd_rtng(92)|swing_damage(45, cut)|thrust_damage(31, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["mogang_pohuaijian", "mogang_pohuaijian", [("darkzweihander1", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through, itc_greatsword|itcf_carry_sword_back, 1013, weight(3.500000)|abundance(10)|difficulty(18)|weapon_length(150)|spd_rtng(85)|swing_damage(52, cut)|thrust_damage(36, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######GILDING WEAPON#########
#One Hand Swords
["jinshi_bishou", "jinshi_bishou", [("dagger_h4", 0), ("dagger_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 400, weight(1.000000)|abundance(20)|difficulty(0)|weapon_length(42)|spd_rtng(123)|swing_damage(28, cut)|thrust_damage(27, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["jinse_shizirengxingjian", "jinse_shizirengxingjian", [("bar_mace_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back, 714, weight(2.000000)|abundance(20)|difficulty(12)|weapon_length(158)|spd_rtng(98)|swing_damage(37, cut)|thrust_damage(31, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["jinshi_cejian", "jinshi_cejian", [("side_sword_h4", 0), ("side_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 530, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(95)|spd_rtng(111)|swing_damage(33, cut)|thrust_damage(28, pierce), imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_get_horse, ":agent_horse_no", ":attacker_agent_no"),#不是骑兵
        (lt, ":agent_horse_no", 0),
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_lunge"),#穿刺
    ]),
]], 
["jinse_minwenjian", "jinse_minwenjian", [("german_greatsword_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 873, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(121)|spd_rtng(110)|swing_damage(33, cut)|thrust_damage(22, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_changjian", "jinse_changjian", [("danish_greatsword_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 589, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(120)|spd_rtng(104)|swing_damage(34, cut)|thrust_damage(25, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_nanfangjian", "jinshi_nanfangjian", [("espada_eslavona_h4", 0), ("espada_eslavona_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 498, weight(1.500000)|abundance(20)|difficulty(0)|weapon_length(93)|spd_rtng(109)|swing_damage(34, cut)|thrust_damage(26, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_fanhuajian", "jinshi_fanhuajian", [("broad_short_sword_h4", 0), ("broad_short_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 637, weight(1.250000)|abundance(20)|difficulty(0)|weapon_length(88)|spd_rtng(118)|swing_damage(34, cut)|thrust_damage(29, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_hushoujian", "jinse_hushoujian", [("bastard_sword_h4", 0), ("bastard_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 540, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(100)|spd_rtng(108)|swing_damage(35, cut)|thrust_damage(23, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_guizujian", "jinse_guizujian", [("highland_claymore_h4", 0), ("highland_claymore_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 735, weight(1.500000)|abundance(20)|difficulty(10)|weapon_length(118)|spd_rtng(113)|swing_damage(35, cut)|thrust_damage(25, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_shamojian", "jinshi_shamojian", [("arabian_straight_sword_h4", 0), ("arabian_straight_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 509, weight(1.500000)|abundance(20)|difficulty(10)|weapon_length(102)|spd_rtng(110)|swing_damage(35, cut)|thrust_damage(21, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_huweijian", "jinshi_huweijian", [("italian_sword_h4", 0), ("italian_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 533, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(100)|spd_rtng(105)|swing_damage(35, cut)|thrust_damage(22, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_longshoujian", "jinshi_longshoujian", [("long_espada_eslavona_h4", 0), ("long_espada_eslavona_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 555, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(103)|spd_rtng(110)|swing_damage(36, cut)|thrust_damage(24, pierce), imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_get_horse, ":agent_horse_no", ":attacker_agent_no"),#不是骑兵
        (lt, ":agent_horse_no", 0),
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_double_lunge"),#二连穿刺
    ]),
]], 
["jinshi_qibingjian", "jinshi_qibingjian", [("longsword_h4", 0), ("practice_longsword_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 607, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(102)|spd_rtng(110)|swing_damage(36, cut)|thrust_damage(26, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_bubingjian", "jinse_bubingjian", [("heavy_bastard_sword_h4", 0), ("heavy_bastard_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 614, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(104)|spd_rtng(110)|swing_damage(37, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_qishijian", "jinshi_qishijian", [("arabian_guard_sword_h4", 0), ("arabian_guard_sword_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 634, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(100)|spd_rtng(113)|swing_damage(38, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["jinshi_youmudao", "jinshi_youmudao", [("Txz_qyd", 0), ("Txz_qydQ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 400, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(88)|spd_rtng(110)|swing_damage(32, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_duandao", "jinshi_duandao", [("wakizashi_h3", 0), ("wakizashi_scabbard_h3", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 387, weight(1.000000)|abundance(20)|difficulty(0)|weapon_length(71)|spd_rtng(118)|swing_damage(33, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshiwandao", "jinshiwandao", [("elite_scimitar_h4", 0), ("elite_scimitar_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 475, weight(1.500000)|abundance(20)|difficulty(9)|weapon_length(107)|spd_rtng(110)|swing_damage(33, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_wudao", "jinse_wudao", [("katana_h4", 0), ("katana_scabbard_h4", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_katana|itcf_show_holster_when_drawn, 627, weight(2.000000)|abundance(20)|difficulty(11)|weapon_length(110)|spd_rtng(110)|swing_damage(36, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_zhirengzhandao", "jinshi_zhirengzhandao", [("trtd", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_left_hip, 465, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(101)|spd_rtng(96)|swing_damage(36, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_madao", "jinshi_madao", [("miaodao_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 561, weight(1.750000)|abundance(20)|difficulty(10)|weapon_length(113)|spd_rtng(110)|swing_damage(37, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["jinse_zhanjian", "jinse_zhanjian", [("great_sword_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back, 713, weight(2.000000)|abundance(20)|difficulty(10)|weapon_length(130)|spd_rtng(100)|swing_damage(36, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_zhongjian", "jinse_zhongjian", [("heavy_great_sword_h4", 0), ("heavy_great_sword_scabbard_h4", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 734, weight(2.250000)|abundance(20)|difficulty(12)|weapon_length(115)|spd_rtng(97)|swing_damage(38, cut)|thrust_damage(22, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinshi_yizhangjian", "jinshi_yizhangjian", [("sword_of_war_h4", 0), ("sword_of_war_scabbard_h4", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 771, weight(2.000000)|abundance(20)|difficulty(10)|weapon_length(127)|spd_rtng(100)|swing_damage(39, cut)|thrust_damage(25, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinseshoubanjian", "jinseshoubanjian", [("flamberge_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_covers_head, itc_bastardsword|itcf_carry_sword_back, 1078, weight(3.000000)|abundance(20)|difficulty(12)|weapon_length(170)|spd_rtng(99)|swing_damage(42, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Blunt
["jinshi_tuntouzhang", "jinshi_tuntouzhang", [("studded_warclub_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_scimitar|itcf_carry_sword_left_hip, 500, weight(2.750000)|abundance(20)|difficulty(11)|weapon_length(100)|spd_rtng(90)|swing_damage(33, blunt)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["jinse_sichui", "jinse_sichui", [("great_maul_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 537, weight(2.500000)|abundance(20)|difficulty(11)|weapon_length(72)|spd_rtng(75)|swing_damage(39, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 

["jinshi_langtouchui", "jinshi_langtouchui", [("long_iron_mace_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_morningstar|itcf_carry_sword_left_hip, 826, weight(3.000000)|abundance(20)|difficulty(12)|weapon_length(100)|spd_rtng(100)|swing_damage(36, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["jinshi_lengtouchui", "jinshi_lengtouchui", [("flanged_mace_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_morningstar|itcf_carry_axe_back, 735, weight(3.000000)|abundance(20)|difficulty(14)|weapon_length(124)|spd_rtng(92)|swing_damage(38, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 

#Powerful Weapons
["jinshi_dingtouchui", "jinshi_dingtouchui", [("morningstar_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, itc_scimitar|itcf_carry_axe_left_hip, 528, weight(3.500000)|abundance(20)|difficulty(13)|weapon_length(91)|spd_rtng(85)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["jinshizhanfu", "jinshizhanfu", [("persian_war_axe_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_morningstar|itcf_carry_axe_back, 553, weight(2.250000)|abundance(20)|difficulty(12)|weapon_length(100)|spd_rtng(104)|swing_damage(37, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jinshi_kuorenfu", "jinshi_kuorenfu", [("shortened_voulge_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced, itc_morningstar|itcf_carry_axe_back, 690, weight(3.500000)|abundance(20)|difficulty(12)|weapon_length(109)|spd_rtng(94)|swing_damage(40, cut)|thrust_damage(27, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Two Hand Swords
["jinshi_zhanlian", "jinshi_zhanlian", [("shortened_military_scythe_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_spear, 877, weight(2.500000)|abundance(20)|difficulty(12)|weapon_length(120)|spd_rtng(98)|swing_damage(38, cut)|thrust_damage(30, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jinshi_shuanshoufu", "jinshi_shuanshoufu", [("persian_battle_axe_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_nodachi|itcf_carry_axe_back, 526, weight(3.000000)|abundance(100)|difficulty(12)|weapon_length(97)|spd_rtng(96)|swing_damage(41, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jinshi_shuangshou", "jinshi_shuangshou", [("two_handed_sword_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back, 656, weight(2.250000)|abundance(20)|difficulty(12)|weapon_length(110)|spd_rtng(100)|swing_damage(39, cut)|thrust_damage(27, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["gilding_nodachi", "Gilding Nodachi", [("nodachi_h4", 0), ("nodachi_scabbard_h4", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 705, weight(2.250000)|abundance(20)|difficulty(12)|weapon_length(138)|spd_rtng(100)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######PIGGING WEAPON#########
#One Hand Weapons
["shengtie_jianyi_fanqudao", "shengtie_jianyi_fanqudao", [("gallic_short_weapon_1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_can_penetrate_shield|itp_crush_through, itc_scimitar|itcf_carry_sword_left_hip, 45, weight(1.000000)|abundance(20)|difficulty(0)|weapon_length(63)|spd_rtng(94)|swing_damage(20, cut)|thrust_damage(0, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["shengtie_kuoren_fanqudao", "shengtie_kuoren_fanqudao", [("gallic_short_weapon_2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_can_penetrate_shield|itp_crush_through, itc_scimitar|itcf_carry_sword_left_hip, 62, weight(1.500000)|abundance(20)|difficulty(10)|weapon_length(67)|spd_rtng(98)|swing_damage(23, cut)|thrust_damage(0, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 

["shentie_goujian", "shentie_goujian", [("bb_hooked_sword", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through, itc_longsword|itcf_carry_sword_left_hip, 172, weight(1.750000)|abundance(30)|difficulty(9)|weapon_length(95)|spd_rtng(100)|swing_damage(29, cut)|thrust_damage(14, cut), imodbits_sword, [weapon_visual_effect_trigger]], 
["shengtie_dao", "shengtie_dao", [("NINJATO", 0), ("NINJATO_scabb_carry_back", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_katana|itcf_show_holster_when_drawn, 262, weight(2.250000)|abundance(30)|difficulty(14)|weapon_length(100)|spd_rtng(90)|swing_damage(30, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["shengtie_kuojian", "shengtie_kuojian", [("gladiush", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip, 226, weight(2.250000)|abundance(20)|difficulty(0)|weapon_length(71)|spd_rtng(100)|swing_damage(31, cut)|thrust_damage(15, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["shengtie_kuojian2", "shengtie_kuojian2", [("Italianxiphos", 0), ("Italianxiphos_sc", ixmesh_carry), ("Italianxiphos_sc.1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 298, weight(2.250000)|abundance(20)|difficulty(9)|weapon_length(70)|spd_rtng(100)|swing_damage(32, cut)|thrust_damage(17, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["shentie_shuangshoufu", "shentie_shuangshoufu", [("great_scimitar", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_morningstar|itcf_carry_sword_left_hip, 678, weight(3.500000)|abundance(30)|difficulty(15)|weapon_length(120)|spd_rtng(86)|swing_damage(33, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Two Hand Weapons
["shengtieshuangshoujian", "shengtieshuangshoujian", [("2h_claymore", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back, 381, weight(3.500000)|abundance(30)|difficulty(12)|weapon_length(113)|spd_rtng(85)|swing_damage(34, cut)|thrust_damage(29, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["shengtie_changbingfu", "shengtie_changbingfu", [("realbastardaxe", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_nodachi|itcf_carry_axe_back, 350, weight(3.000000)|abundance(100)|difficulty(10)|weapon_length(112)|spd_rtng(95)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

["shengtie_kaungbaodao", "shengtie_kaungbaodao", [("vorpal_s", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_sword_back, 425, weight(3.750000)|abundance(30)|difficulty(15)|weapon_length(137)|spd_rtng(83)|swing_damage(37, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 


#######COMMON WEAPON#########
#Peasent Weapons
["sickle", "Sickle", [("sickle", 0)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itc_cleaver|itcf_carry_sword_left_hip, 9, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(40)|spd_rtng(99)|swing_damage(20, cut)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["knife", "Knife", [("peasant_knife_new", 0)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_right, 18, weight(0.500000)|abundance(100)|difficulty(0)|weapon_length(40)|spd_rtng(110)|swing_damage(21, cut)|thrust_damage(13, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["cleaver", "Cleaver", [("cleaver_new", 0)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itc_cleaver|itcf_carry_dagger_front_right, 14, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(35)|spd_rtng(103)|swing_damage(24, cut)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["butchering_knife", "Butchering_Knife", [("khyber_knife_new", 0)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_right, 23, weight(0.750000)|abundance(100)|difficulty(0)|weapon_length(60)|spd_rtng(108)|swing_damage(24, cut)|thrust_damage(17, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["dagger", "Dagger", #匕首
   [("dagger_b", 0), ("dagger_b_scabbard", ixmesh_carry), ("dagger_b", 251658240), ("dagger_b_scabbard", 3458764514072199168)], 
   itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, 
   itc_dagger|itcf_carry_dagger_front_right, 37, 
   weight(0.75)|abundance(100)|difficulty(0)|weapon_length(47)|spd_rtng(109)|swing_damage(22, cut)|thrust_damage(19, pierce), 
   imodbits_sword_high, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (call_script, "script_cf_grab_skill_technique", ":attacker_agent_no", "itm_active_cutthroat"),#割喉
    ]),
   ]], 

#Swords
["jianyi_peizhongjian", "jianyi_peizhongjian", [("celticlongsword3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip, 260, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(106)|spd_rtng(100)|swing_damage(29, cut)|thrust_damage(20, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["hushou_duanjian", "hushou_duanjian", [("celtic3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 300, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(107)|spd_rtng(100)|swing_damage(30, cut)|thrust_damage(21, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["sword_medieval_c_small", "Short_Arming_Sword", [("sword_medieval_c_small", 0), ("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 123, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(86)|spd_rtng(113)|swing_damage(26, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_medieval_a", "Sword", [("sword_medieval_a", 0), ("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 80, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(95)|spd_rtng(109)|swing_damage(27, cut)|thrust_damage(22, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_medieval_b", "Sword", [("sword_medieval_b", 0), ("sword_medieval_b_scabbard", ixmesh_carry), ("sword_rusty_a", 4), ("sword_rusty_a_scabbard", 3458764513820540932)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 120, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(97)|spd_rtng(109)|swing_damage(28, cut)|thrust_damage(23, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_medieval_b_small", "Short_Sword", [("sword_medieval_b_small", 0), ("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 100, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(85)|spd_rtng(112)|swing_damage(29, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_medieval_c", "Arming_Sword", [("sword_medieval_c", 0), ("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 140, weight(1.500000)|abundance(100)|difficulty(7)|weapon_length(95)|spd_rtng(109)|swing_damage(29, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_medieval_c_long", "Arming_Sword", [("sword_medieval_c_long", 0), ("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 162, weight(1.500000)|abundance(100)|difficulty(7)|weapon_length(100)|spd_rtng(109)|swing_damage(29, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["peizhong_jian", "peizhong_jian", [("clansmanswordc", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip, 370, weight(2.000000)|abundance(100)|difficulty(9)|weapon_length(119)|spd_rtng(99)|swing_damage(31, cut)|thrust_damage(24, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["qinse_danshoujian", "qinse_danshoujian", [("silverzweihander1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 510, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(130)|spd_rtng(98)|swing_damage(32, cut)|thrust_damage(26, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["sword_medieval_d_long", "Long_Arming_Sword", [("sword_medieval_d_long", 0), ("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 250, weight(1.500000)|abundance(100)|difficulty(8)|weapon_length(105)|spd_rtng(106)|swing_damage(33, cut)|thrust_damage(28, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["tiehuan_danshoujian", "tiehuan_danshoujian", [("kingslayer", 0), ("kingslayer_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 740, weight(1.750000)|abundance(20)|difficulty(12)|weapon_length(124)|spd_rtng(97)|swing_damage(36, cut)|thrust_damage(24, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["zhereng_wandao", "zhereng_wandao", [("raptorsword", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip, 560, weight(2.000000)|abundance(100)|difficulty(11)|weapon_length(131)|spd_rtng(102)|swing_damage(35, cut)|thrust_damage(23, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["bastard_sword_a", "Bastard_Sword", [("bastard_sword_a", 0), ("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 305, weight(2.000000)|abundance(100)|difficulty(10)|weapon_length(101)|spd_rtng(108)|swing_damage(35, cut)|thrust_damage(26, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["bastard_sword_b", "Heavy_Bastard_Sword", [("bastard_sword_b", 0), ("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 526, weight(2.250000)|abundance(100)|difficulty(9)|weapon_length(105)|spd_rtng(97)|swing_damage(37, cut)|thrust_damage(27, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["sword_two_handed_b", "Two_Handed_Sword", [("sword_two_handed_b", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 470, weight(2.750000)|abundance(100)|difficulty(10)|weapon_length(110)|spd_rtng(97)|swing_damage(38, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["sword_two_handed_a", "Great_Sword", [("sword_two_handed_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 523, weight(2.750000)|abundance(100)|difficulty(10)|weapon_length(120)|spd_rtng(96)|swing_damage(42, cut)|thrust_damage(29, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["great_sword", "Great_Sword", [("b_bastard_sword", 0), ("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 437, weight(3.250000)|abundance(100)|difficulty(10)|weapon_length(120)|spd_rtng(90)|swing_damage(43, cut)|thrust_damage(31, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Sabres
["wanren_jian", "wanren_jian", [("saber13", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 460, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(101)|spd_rtng(106)|swing_damage(30, cut)|thrust_damage(21, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["falchion", "Falchion", [("falchion_new", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 53, weight(2.500000)|abundance(100)|difficulty(8)|weapon_length(73)|spd_rtng(96)|swing_damage(30, cut)|thrust_damage(0, pierce), imodbits_sword, [weapon_visual_effect_trigger]], 
["scimitar", "Scimitar", [("scimitar_a", 0), ("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 213, weight(1.500000)|abundance(100)|difficulty(8)|weapon_length(97)|spd_rtng(101)|swing_damage(30, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["fanquwanren_jian", "fanquwanren_jian", [("saber23", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 430, weight(1.250000)|abundance(100)|difficulty(9)|weapon_length(97)|spd_rtng(110)|swing_damage(31, cut)|thrust_damage(21, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["zhiren_zhandao", "zhiren_zhandao", [("sabre1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 300, weight(1.250000)|abundance(100)|difficulty(9)|weapon_length(93)|spd_rtng(100)|swing_damage(31, cut)|thrust_damage(19, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["scimitar_b", "Elite_Scimitar", [("scimitar_b", 0), ("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 294, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(103)|spd_rtng(100)|swing_damage(32, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["shortened_military_scythe", "Shortened_Military_Scythe", [("two_handed_battle_scythe_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 275, weight(3.000000)|abundance(100)|difficulty(10)|weapon_length(112)|spd_rtng(90)|swing_damage(37, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["khergit_sword_two_handed_a", "Two_Handed_Sabre", [("khergit_sword_two_handed_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 390, weight(2.750000)|abundance(100)|difficulty(11)|weapon_length(120)|spd_rtng(96)|swing_damage(37, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["khergit_sword_two_handed_b", "Two_Handed_Sabre", [("khergit_sword_two_handed_b", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 450, weight(3.000000)|abundance(100)|difficulty(10)|weapon_length(120)|spd_rtng(96)|swing_damage(39, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["military_cleaver_b", "Soldier's_Cleaver", [("military_cleaver_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 294, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(95)|spd_rtng(96)|swing_damage(31, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["military_cleaver_c", "Military_Cleaver", [("military_cleaver_c", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 363, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(95)|spd_rtng(96)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["two_handed_cleaver", "War_Cleaver", [("military_cleaver_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 548, weight(2.750000)|abundance(100)|difficulty(13)|weapon_length(120)|spd_rtng(93)|swing_damage(45, cut)|thrust_damage(0, cut), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["zhiren_changbing_zhandao", "zhiren_changbing_zhandao", [("mackie_nagamaki", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_morningstar|itcf_carry_sword_back, 835, weight(3.000000)|abundance(30)|difficulty(15)|weapon_length(135)|spd_rtng(93)|swing_damage(41, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["changbing_zhandao", "changbing_zhandao", [("Txz_zmd", 0), ("Txz_zmdQ", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 922, weight(2.000000)|abundance(40)|difficulty(12)|weapon_length(146)|spd_rtng(97)|swing_damage(42, cut)|thrust_damage(0, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

#Blunts and Hmmers
["wooden_stick", "Wooden_Stick", [("wooden_stick", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 4, weight(0.500000)|abundance(100)|difficulty(0)|weapon_length(63)|spd_rtng(99)|swing_damage(13, blunt)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["torch", "Torch", [("club", 0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(95)|spd_rtng(95)|swing_damage(11, blunt)|thrust_damage(0, pierce), imodbits_none, [
    (ti_on_init_item, [
        (set_position_delta, 0, 60, 0),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (set_current_color, 150, 130, 70),
        (add_point_light, 10, 30),
    ]),
    weapon_visual_effect_trigger,
]], 
["cudgel", "Cudgel", [("club", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 4, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(70)|spd_rtng(99)|swing_damage(13, blunt)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["club", "Club", [("club", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_sword_left_hip, 11, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(70)|spd_rtng(98)|swing_damage(20, blunt)|thrust_damage(0, pierce), imodbits_none, [weapon_visual_effect_trigger]], 
["hammer", "Hammer", [("iron_hammer_new", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 7, weight(2.000000)|abundance(100)|difficulty(0)|weapon_length(55)|spd_rtng(100)|swing_damage(24, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["mace_2", "Knobbed_Mace", [("mace_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 98, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(75)|spd_rtng(98)|swing_damage(24, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sarranid_mace_1", "Iron_Mace", [("mace_small_d", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 350, weight(2.000000)|abundance(100)|difficulty(0)|weapon_length(73)|spd_rtng(99)|swing_damage(25, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["mace_4", "Winged_Mace", [("mace_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 180, weight(2.750000)|abundance(100)|difficulty(0)|weapon_length(60)|spd_rtng(98)|swing_damage(26, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["military_hammer", "Military_Hammer", [("military_hammer", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 155, weight(2.000000)|abundance(100)|difficulty(0)|weapon_length(70)|spd_rtng(95)|swing_damage(31, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["zhanshi_chui", "zhanshi_chui", [("luc_warhammer_s_v1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 323, weight(3.000000)|abundance(60)|difficulty(12)|weapon_length(72)|spd_rtng(95)|swing_damage(34, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["handguard_hammer", "Handguard Hammer", [("wqheji21", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_sword_left_hip, 423, weight(2.000000)|abundance(50)|difficulty(15)|weapon_length(106)|spd_rtng(95)|swing_damage(34, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["jinse_duanchui", "jinse_duanchui", [("talak_warhammer", 0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_mace_left_hip, 700, weight(2.500000)|abundance(20)|difficulty(12)|weapon_length(66)|spd_rtng(100)|swing_damage(35, blunt)|thrust_damage(17, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 

["winged_mace", "Flanged_Mace", [("flanged_mace", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 60, weight(3.500000)|abundance(100)|difficulty(0)|weapon_length(85)|spd_rtng(90)|swing_damage(25, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jianyi_lengtouchui", "jianyi_lengtouchui", [("winged_mace_3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 676, weight(2.750000)|abundance(70)|difficulty(13)|weapon_length(76)|spd_rtng(87)|swing_damage(32, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["qinliang_lengtouchui", "qinliang_lengtouchui", [("pa_maul_02", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 734, weight(3.000000)|abundance(80)|difficulty(12)|weapon_length(105)|spd_rtng(100)|swing_damage(33, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["qinse_lengtouchui", "qinse_lengtouchui", [("doomguidemace3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 710, weight(3.750000)|abundance(20)|difficulty(13)|weapon_length(116)|spd_rtng(100)|swing_damage(36, blunt)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 

["sarranid_two_handed_mace_1", "Iron_Mace", [("mace_long_d", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_axe_back, 477, weight(4.500000)|abundance(100)|difficulty(12)|weapon_length(95)|spd_rtng(90)|swing_damage(35, blunt)|thrust_damage(22, blunt), imodbits_axe, [weapon_visual_effect_trigger]], 
["maul", "Maul", [("maul_b", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_spear, 56, weight(6.000000)|abundance(100)|difficulty(11)|weapon_length(79)|spd_rtng(83)|swing_damage(36, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sledgehammer", "Sledgehammer", [("maul_c", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down,  itc_nodachi|itcf_carry_spear, 57, weight(7.000000)|abundance(100)|difficulty(12)|weapon_length(82)|spd_rtng(81)|swing_damage(39, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["warhammer", "Great_Hammer", [("maul_d", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_unbalanced|itp_can_knock_down,  itc_nodachi|itcf_carry_spear, 159, weight(9.000000)|abundance(100)|difficulty(14)|weapon_length(75)|spd_rtng(79)|swing_damage(45, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

["mace_1", "Spiked_Club", [("mace_d", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 45, weight(1.500000)|abundance(100)|difficulty(0)|weapon_length(62)|spd_rtng(99)|swing_damage(19, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["spiked_club", "Spiked_Club", [("spiked_club", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 50, weight(3.000000)|abundance(100)|difficulty(0)|weapon_length(89)|spd_rtng(97)|swing_damage(21, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["spiked_mace", "Spiked_Mace", [("spiked_mace_new", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_axe_left_hip, 90, weight(3.500000)|abundance(100)|difficulty(0)|weapon_length(98)|spd_rtng(90)|swing_damage(23, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["mace_3", "Spiked_Mace", [("mace_c", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 152, weight(2.750000)|abundance(100)|difficulty(0)|weapon_length(70)|spd_rtng(98)|swing_damage(23, blunt)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jianyi_langyabang", "jianyi_langyabang", [("spikemace3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_axe_left_hip, 330, weight(2.750000)|abundance(100)|difficulty(9)|weapon_length(94)|spd_rtng(87)|swing_damage(27, pierce)|thrust_damage(16, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["dingci_lengtouchui", "dingci_lengtouchui", [("mace_h4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 428, weight(2.750000)|abundance(30)|difficulty(11)|weapon_length(76)|spd_rtng(100)|swing_damage(34, pierce)|thrust_damage(0, pierce), imodbits_pick, [weapon_visual_effect_trigger]], 
["morningstar", "Morningstar", [("mace_morningstar_new", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_unbalanced, itc_morningstar|itcf_carry_axe_left_hip, 428, weight(4.500000)|abundance(100)|difficulty(13)|weapon_length(85)|spd_rtng(85)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Goedendag
["club_with_spike_head", "Spiked_Staff", [("mace_e", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_bastardsword|itcf_carry_axe_back, 94, weight(2.750000)|abundance(100)|difficulty(9)|weapon_length(117)|spd_rtng(95)|swing_damage(24, blunt)|thrust_damage(20, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Axes
["hatchet", "Hatchet", [("hatchet", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 13, weight(2.000000)|abundance(100)|difficulty(0)|weapon_length(48)|spd_rtng(97)|swing_damage(23, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["hand_axe", "Hand_Axe", [("hatchet", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 24, weight(2.000000)|abundance(100)|difficulty(7)|weapon_length(60)|spd_rtng(95)|swing_damage(27, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["fighting_axe", "Fighting_Axe", [("fighting_ax", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 74, weight(2.500000)|abundance(100)|difficulty(9)|weapon_length(91)|spd_rtng(92)|swing_damage(31, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["one_handed_war_axe_a", "One_Handed_Axe", [("one_handed_war_axe_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 87, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(60)|spd_rtng(91)|swing_damage(34, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["one_handed_battle_axe_a", "One_Handed_Battle_Axe", [("one_handed_battle_axe_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 142, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(63)|spd_rtng(98)|swing_damage(34, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["one_handed_war_axe_b", "One_Handed_War_Axe", [("one_handed_war_axe_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 190, weight(1.500000)|abundance(100)|difficulty(9)|weapon_length(76)|spd_rtng(98)|swing_damage(34, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sarranid_axe_a", "Iron_Battle_Axe", [("one_handed_battle_axe_g", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 254, weight(1.750000)|abundance(100)|difficulty(9)|weapon_length(71)|spd_rtng(97)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["one_handed_battle_axe_b", "One_Handed_Battle_Axe", [("one_handed_battle_axe_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 230, weight(1.750000)|abundance(100)|difficulty(9)|weapon_length(72)|spd_rtng(98)|swing_damage(36, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jianyi_danshoufu", "jianyi_danshoufu", [("mackie_tomahawk", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 378, weight(2.500000)|abundance(80)|difficulty(10)|weapon_length(58)|spd_rtng(90)|swing_damage(36, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["one_handed_battle_axe_c", "One_Handed_Battle_Axe", [("one_handed_battle_axe_c", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 350, weight(2.000000)|abundance(100)|difficulty(9)|weapon_length(76)|spd_rtng(98)|swing_damage(37, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sarranid_axe_b", "Iron_War_Axe", [("one_handed_battle_axe_h", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 364, weight(1.750000)|abundance(100)|difficulty(9)|weapon_length(71)|spd_rtng(97)|swing_damage(38, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jainyi_shuangrenfu", "jainyi_shuangrenfu", [("mackie_double_axe", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 347, weight(2.500000)|abundance(30)|difficulty(11)|weapon_length(70)|spd_rtng(90)|swing_damage(41, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["danshou_biantoufu", "danshou_biantoufu", [("mackie_short_voulge", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_axe_left_hip, 326, weight(2.750000)|abundance(40)|difficulty(12)|weapon_length(78)|spd_rtng(90)|swing_damage(40, cut)|thrust_damage(23, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["danshou_chanfu", "danshou_chanfu", [("mackie_pendulum_axe", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_scimitar|itcf_carry_axe_left_hip, 314, weight(2.250000)|abundance(30)|difficulty(11)|weapon_length(76)|spd_rtng(91)|swing_damage(43, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

["axe", "Axe", [("iron_ax", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 63, weight(4.000000)|abundance(100)|difficulty(8)|weapon_length(93)|spd_rtng(91)|swing_damage(32, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["voulge", "Voulge", [("voulge", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 124, weight(4.500000)|abundance(100)|difficulty(9)|weapon_length(119)|spd_rtng(87)|swing_damage(35, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jainyi_changbingfu", "jainyi_changbingfu", [("mackie_bearded_axe", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_carry_axe_back, 680, weight(3.750000)|abundance(39)|difficulty(14)|weapon_length(140)|spd_rtng(81)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["two_handed_axe", "Two_Handed_Axe", [("two_handed_battle_axe_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 216, weight(4.000000)|abundance(100)|difficulty(11)|weapon_length(90)|spd_rtng(90)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jianyi_shuangshoufu", "jianyi_shuangshoufu", [("mackie_varangian_axe", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_morningstar|itcf_carry_axe_left_hip, 700, weight(3.750000)|abundance(50)|difficulty(13)|weapon_length(75)|spd_rtng(84)|swing_damage(40, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["qinliang_shuangshoufu", "qinliang_shuangshoufu", [("trgwa", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_spear, 1190, weight(4.000000)|abundance(100)|difficulty(14)|weapon_length(171)|spd_rtng(82)|swing_damage(41, pierce)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["battle_axe", "Battle_Axe", [("battle_ax", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 244, weight(5.000000)|abundance(100)|difficulty(9)|weapon_length(92)|spd_rtng(93)|swing_damage(41, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["war_axe", "War_Axe", [("war_ax", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 265, weight(5.000000)|abundance(100)|difficulty(10)|weapon_length(115)|spd_rtng(91)|swing_damage(43, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["fangxing_fu", "fangxing_fu", [("voulge_h4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 1100, weight(4.000000)|abundance(100)|difficulty(15)|weapon_length(143)|spd_rtng(91)|swing_damage(44, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

["shortened_voulge", "Shortened_Voulge", [("two_handed_battle_axe_c", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 228, weight(4.500000)|abundance(100)|difficulty(10)|weapon_length(100)|spd_rtng(92)|swing_damage(45, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sarranid_two_handed_axe_b", "Sarranid_War_Axe", [("two_handed_battle_axe_h", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 287, weight(3.000000)|abundance(100)|difficulty(12)|weapon_length(90)|spd_rtng(90)|swing_damage(46, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["gangpian_fu", "gangpian_fu", [("ax_indian", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 733, weight(4.750000)|abundance(70)|difficulty(12)|weapon_length(103)|spd_rtng(86)|swing_damage(46, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["bardiche", "Bardiche", [("two_handed_battle_axe_d", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 316, weight(4.500000)|abundance(100)|difficulty(11)|weapon_length(102)|spd_rtng(91)|swing_damage(47, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["two_handed_battle_axe_2", "Two_Handed_War_Axe", [("two_handed_battle_axe_b", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 308, weight(4.500000)|abundance(100)|difficulty(13)|weapon_length(92)|spd_rtng(92)|swing_damage(47, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["sarranid_two_handed_axe_a", "Sarranid_Battle_Axe", [("two_handed_battle_axe_g", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 358, weight(3.000000)|abundance(100)|difficulty(13)|weapon_length(95)|spd_rtng(94)|swing_damage(49, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["great_bardiche", "Great_Bardiche", [("two_handed_battle_axe_f", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 617, weight(5.500000)|abundance(100)|difficulty(12)|weapon_length(116)|spd_rtng(89)|swing_damage(50, cut)|thrust_damage(0, pierce), imodbits_axe], 
["great_axe", "Great_Axe", [("two_handed_battle_axe_e", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 316, weight(5.500000)|abundance(100)|difficulty(13)|weapon_length(90)|spd_rtng(80)|swing_damage(51, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["jinse_jufu", "jinse_jufu", [("runeaxe3", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 2000, weight(5.000000)|abundance(20)|difficulty(15)|weapon_length(154)|spd_rtng(85)|swing_damage(55, cut)|thrust_damage(0, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 

#Special Weapons
["yansha_danshoujian", "yansha_danshoujian", [("criss_1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_left_hip, 420, weight(1.250000)|abundance(30)|difficulty(12)|weapon_length(70)|spd_rtng(100)|swing_damage(40, cut)|thrust_damage(23, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 
["yansha_shuangshoujian", "yansha_shuangshoujian", [("flamberge", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_can_knock_down, itc_bastardsword|itcf_carry_sword_back, 1432, weight(2.750000)|abundance(10)|difficulty(10)|weapon_length(164)|spd_rtng(89)|swing_damage(52, cut)|thrust_damage(28, pierce), imodbits_sword_high, [weapon_visual_effect_trigger]], 

["whip", "Whip", #鞭子
   [("whip", 0)], 
   itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_can_penetrate_shield, 
   itc_scimitar|itcf_carry_sword_left_hip, 212, 
   weight(1.5)|abundance(20)|difficulty(0)|weapon_length(95)|spd_rtng(113)|swing_damage(17, blunt)|thrust_damage(0, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["lamp_stand_hammer", "Lamp Stand Hammer", #灯台锤
   [("candle_sword", 0)], 
   itp_type_one_handed_wpn|itp_primary|itp_can_penetrate_shield, 
   itc_longsword|itcf_carry_sword_left_hip, 2612, 
   weight(2.5)|abundance(1)|difficulty(11)|weapon_length(75)|spd_rtng(73)|swing_damage(27, pierce)|thrust_damage(29, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["anti_cavalry_great_sword", "Anti-cavalry Great Sword", #反骑巨剑
   [("copy_arabian_sword_d.1", 0)], 
   itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_cant_use_on_horseback|itp_can_knock_down, 
   itc_greatsword|itcf_carry_spear, 2316, 
   weight(6.5)|abundance(40)|difficulty(18)|weapon_length(235)|spd_rtng(74)|swing_damage(51, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["noble_black_sword", "Noble Black Sword", #煌黑大剑
   [("FF_sword", 0), ("FF_sword_scrabed", ixmesh_carry)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary, 
   itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 1437, 
   weight(3.75)|abundance(5)|difficulty(10)|weapon_length(124)|spd_rtng(88)|swing_damage(49, cut)|thrust_damage(37, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 




#HELMET
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["helmet_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["no_head", "No Head", #透明盔
   [("cw_no_head", 0)], 
   itp_type_head_armor|itp_unique|itp_doesnt_cover_hair, 0, 1, 
   weight(0.25)|abundance(1)|difficulty(6)|head_armor(50)|body_armor(0)|leg_armor(0), 
   imodbits_none], 


#######KING HELMET#########
["luxury_crown", "Luxury Crown", #倾国王冠
   [("aqs_crown_new", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0, 79981, 
   weight(0.25)|abundance(1)|difficulty(0)|head_armor(24)|body_armor(0)|leg_armor(0), 
   imodbits_none], 
["wangguan_toujinkui", "wangguan_toujinkui", [("andalusian_helmet_f", 0)], itp_type_head_armor|itp_fit_to_head, 0, 10078, weight(1.000000)|abundance(1)|difficulty(7)|head_armor(41)|body_armor(0)|leg_armor(0), imodbits_plate], 
["wangguan_lianjiatoukui", "wangguan_lianjiatoukui", [("coif_crown_b", 0)], itp_type_head_armor|itp_fit_to_head, 0, 12278, weight(2.250000)|abundance(1)|difficulty(8)|head_armor(49)|body_armor(0)|leg_armor(0), imodbits_plate], 
["wangguan_lianjiakui", "wangguan_lianjiakui", [("crown_helm_mail", 0)], itp_type_head_armor, 0, 11000, weight(2.250000)|abundance(1)|difficulty(10)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_plate], 
["wangguan_lianjiatoujin", "wangguan_lianjiatoujin", [("crown_coif", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 10315, weight(1.500000)|abundance(1)|difficulty(7)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_plate], 
["wangguan_tongkui", "wangguan_tongkui", [("crown_helm", 0)], itp_type_head_armor, 0, 13000, weight(3.250000)|abundance(1)|difficulty(14)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 


#######POWELL HELMET#########
#Powell Helmet
["flat_topped_helmet", "Flat_Topped_Helmet", [("flattop_helmet_new", 0)], itp_type_head_armor|itp_merchandise, 0, 413, weight(2.000000)|abundance(100)|difficulty(8)|head_armor(44)|body_armor(0)|leg_armor(0), imodbits_plate], 
["hubi_gangkui", "hubi_gangkui", [("realbarbutteb", 0)], itp_type_head_armor|itp_merchandise, 0, 500, weight(2.000000)|abundance(60)|difficulty(0)|head_armor(57)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaqiang_hubi_gangkui", "jiaqiang_hubi_gangkui", [("realbarbuttec", 0)], itp_type_head_armor|itp_merchandise, 0, 505, weight(2.000000)|abundance(60)|difficulty(10)|head_armor(58)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nanfang_chaozhongkui", "nanfang_chaozhongkui", [("osp_greathelm_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 998, weight(4.000000)|abundance(20)|difficulty(15)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Dragon Worship Helmet
["longshen_jiaoshitouhuan", "longshen_jiaoshitouhuan", [("wizard_circelet_1", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 662, weight(0.500000)|abundance(40)|difficulty(0)|head_armor(24)|body_armor(0)|leg_armor(0), imodbits_plate], 
["longshen_silitouhuan", "longshen_silitouhuan", [("wizard_circelet_2", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1862, weight(0.750000)|abundance(10)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#罗德里格斯公国
["rodriguez_bucket_helmet", "Rodriguez Bucket Helmet", #罗德里格斯桶盔
   [("col1_crusaderbucket1", 0)], 
   itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 834, 
   weight(3)|abundance(10)|difficulty(11)|head_armor(63)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 

#自由城邦
["state_great_helmet", "State Great Helmet", #自由城邦巨盔
   [("col1_madelnbucket2", 0)], 
   itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 914, 
   weight(3.25)|abundance(10)|difficulty(12)|head_armor(66)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 


#######ELF HELMET#########
#Corollas
["silver_crown", "Silver Crown", #银色花冠
   [("laurel_silver", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0, 2078, 
   weight(0.250000)|abundance(5)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["golden_crown", "Golden Crown", #金色花冠
   [("laurel_gold", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0, 3078, 
   weight(0.250000)|abundance(5)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 

#Elf Helmets
["ranger_hood", "Ranger Hood", #游侠风帽
   [("greehat1", 0)], 
   itp_type_head_armor|itp_merchandise, 0, 308, 
   weight(0.25)|abundance(30)|difficulty(0)|head_armor(38)|body_armor(0)|leg_armor(0), 
   imodbits_cloth],  
["ranger_helmet", "Ranger Helmet", #游侠面罩盔
   [("greehat", 0)], 
   itp_type_head_armor|itp_merchandise, 0, 408, 
   weight(0.5)|abundance(30)|difficulty(0)|head_armor(44)|body_armor(0)|leg_armor(0), 
   imodbits_cloth],  
["elf_dome_helmet", "Elf Dome Helmet", #精灵圆顶盔
   [("misidelong1tou", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 464, 
   weight(0.75)|abundance(20)|difficulty(0)|head_armor(50)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["elf_pointed_helmet", "Elf Pointed Helmet", #精灵尖顶盔
   [("misidelong2tou", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 484, 
   weight(0.75)|abundance(20)|difficulty(0)|head_armor(52)|body_armor(0)|leg_armor(0), 
   imodbits_plate],

["graghite_steel_small_helmet", "Graghite Steel Small Helmet", #墨钢小盔
   [("mirkwood_helm", 0)], 
   itp_type_head_armor, 0, 1540, 
   weight(4)|abundance(10)|difficulty(15)|head_armor(53)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["yishith_knight_helmet", "Yishith Knight Helmet", #伊希斯骑士盔
   [("mirkwoodnormalspearman", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 1684, 
   weight(2.75)|abundance(10)|difficulty(0)|head_armor(56)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["yishith_knight_strengthen_helmet", "Yishith Knight Strengthen Helmet", #伊希斯骑士加强盔
   [("mirkwoodroyalspearman", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 2084, 
   weight(3)|abundance(10)|difficulty(0)|head_armor(60)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 

["selected_champion_headcrown", "Selected Champion Headcrown", #神选冠军头冠
   [("glasshelmet", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair, 0, 12000, 
   weight(0.15)|abundance(1)|difficulty(20)|head_armor(70)|body_armor(20)|leg_armor(20), 
   imodbits_plate], 
["selected_champion_helmet", "Selected Champion Helmet", #神选冠军头盔
   [("glasshelmet_m", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 17000, 
   weight(0.75)|abundance(1)|difficulty(20)|head_armor(90)|body_armor(20)|leg_armor(20), 
   imodbits_plate], 

["ice_knight_helmet", "Ice Knight Helmet", #苦寒冰盔
   [("ice_knight_helmet", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0, 16000, 
   weight(2)|abundance(1)|difficulty(22)|head_armor(87)|body_armor(10)|leg_armor(10), 
   imodbits_plate], 

#灵芽
["seedlined_head", "Seedlined Head", #灵苗
   [("seedlined_head", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_covers_head|itp_civilian, 0, 3408, 
   weight(3.000000)|abundance(1)|difficulty(0)|head_armor(50)|body_armor(30)|leg_armor(30), 
   imodbits_none], 
["seedlined_flower_head", "Seedlined Flower Head", #灵花
   [("seedlined_flower_head", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_covers_head|itp_civilian, 0, 11408, 
   weight(3.000000)|abundance(1)|difficulty(0)|head_armor(60)|body_armor(40)|leg_armor(40), 
   imodbits_none], 
["seedlined_red_flower_head", "Seedlined Red Flower Head", #红色灵花
   [("seedlined_red_flower_head", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_covers_head|itp_civilian, 0, 31408, 
   weight(3.000000)|abundance(1)|difficulty(0)|head_armor(60)|body_armor(40)|leg_armor(40), 
   imodbits_none], 


#######STEPPE HELMET#########
#Therianthropy Head
["shitou", "shitou", [("nemean_helm", 0)], itp_type_head_armor|itp_unique|itp_attach_armature|itp_attachment_mask|itp_covers_head, 0, 1408, weight(50.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["xiongtou", "xiongtou", [("Bear_helmet", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 1408, weight(55.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none],
["langtou", "langtou", [("wolfhead", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 1408, weight(45.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none],  

["beast_ancestor_headgear", "Beast Ancestor Headgear", [("beast_helmet", 0)], itp_type_head_armor|itp_covers_head, 0, 1408, weight(8.000000)|abundance(1)|difficulty(20)|head_armor(63)|body_armor(3)|leg_armor(0), imodbits_none],  
["beast_king_helmet", "Beast King Helmet", [("dragonhelmet", 0)], itp_type_head_armor|itp_covers_head, 0, 4000, weight(10.500000)|abundance(1)|difficulty(30)|head_armor(78)|body_armor(10)|leg_armor(0), imodbits_plate], 

#Kouruto Human Helmet
["khergit_lady_hat", "Khergit_Lady_Hat", [("khergit_lady_hat", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_fit_to_head, 0, 20, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["khergit_lady_hat_b", "Khergit_Lady_Leather_Hat", [("khergit_lady_hat_b", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 20, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["nomad_cap", "Nomad_Cap", [("nomad_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 6, weight(0.750000)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["leather_steppe_cap_a", "Steppe_Cap", [("leather_steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 24, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(12)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["nomad_cap_b", "Nomad_Cap", [("nomad_cap_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 6, weight(0.750000)|abundance(100)|difficulty(0)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["leather_steppe_cap_b", "Steppe_Cap_", [("tattered_steppe_cap_b_new", 0)], itp_type_head_armor|itp_merchandise, 0, 36, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["leather_steppe_cap_c", "Steppe_Cap", [("steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 51, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["vaegir_fur_cap", "Cap_with_Fur", [("vaeg_helmet3", 0)], itp_type_head_armor|itp_merchandise, 0, 50, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(21)|body_armor(0)|leg_armor(0), imodbits_plate], 
["felt_steppe_cap", "Felt_Steppe_Cap", [("felt_steppe_cap", 0)], itp_type_head_armor, 0, 150, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["khergit_war_helmet", "Khergit_War_Helmet", [("tattered_steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 160, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(29)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["vaegir_fur_helmet", "Vaegir_Helmet", [("vaeg_helmet2", 0)], itp_type_head_armor|itp_merchandise, 0, 111, weight(2.000000)|abundance(100)|difficulty(6)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_plate], 
["khergit_helmet", "Khergit_Helmet", [("khergit_guard_helmet", 0)], itp_type_head_armor, 0, 201, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["vaegir_spiked_helmet", "Spiked_Cap", [("vaeg_helmet1", 0)], itp_type_head_armor|itp_merchandise, 0, 232, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(34)|body_armor(0)|leg_armor(0), imodbits_plate], 
["vaegir_lamellar_helmet", "Helmet_with_Lamellar_Guard", [("vaeg_helmet4", 0)], itp_type_head_armor|itp_merchandise, 0, 362, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_plate], 
["khergit_guard_helmet", "Khergit_Guard_Helmet", [("lamellar_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0, 533, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["khergit_cavalry_helmet", "Khergit_Cavalry_Helmet", [("lamellar_helmet_b", 0)], itp_type_head_armor|itp_merchandise, 0, 533, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["kelutuo_heikui", "kelutuo_heikui", [("dorn_squire_helm", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 678, weight(3.000000)|abundance(20)|difficulty(0)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["linshi_zhongkui", "linshi_zhongkui", [("Norman_phyrgian_faceplate_j", 0), ("Norman_phyrgian_faceplate_j.1", 0)], itp_type_head_armor|itp_merchandise, 0, 410, weight(3.000000)|abundance(10)|difficulty(18)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_plate], 
["kelutuo_duizhangkui", "kelutuo_duizhangkui", [("zztk", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 677, weight(2.250000)|abundance(20)|difficulty(9)|head_armor(43)|body_armor(1)|leg_armor(0), imodbits_plate], 
["nanfang_lianjiatoukui", "nanfang_lianjiatoukui", [("inv_gnezdovo_helm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 660, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(47)|body_armor(0)|leg_armor(0), imodbits_plate], 
["kelutuo_hongyukui", "kelutuo_hongyukui", [("Rathos_Spangenhelm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 579, weight(2.000000)|abundance(40)|difficulty(9)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 


#######CONFEDERATION HELMET#########
#Normal Used Helmets
["vaegir_noble_helmet", "Vaegir_Nobleman_Helmet", [("vaeg_helmet7", 0)], itp_type_head_armor|itp_merchandise, 0, 614, weight(2.000000)|abundance(100)|difficulty(9)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_plate], 
["vaegir_war_helmet", "Vaegir_War_Helmet", [("vaeg_helmet6", 0)], itp_type_head_armor|itp_merchandise, 0, 624, weight(2.000000)|abundance(100)|difficulty(9)|head_armor(47)|body_armor(0)|leg_armor(0), imodbits_plate], 
["vaegir_mask", "Vaegir_War_Mask", [("vaeg_helmet9", 0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 757, weight(2.000000)|abundance(100)|difficulty(12)|head_armor(52)|body_armor(0)|leg_armor(0), imodbits_plate], 
["wumiankui", "wumiankui", [("byzantine", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 745, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heizong_wumiankui", "heizong_wumiankui", [("cataphract", 0), ("cataphract.1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 745, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_plate], 
["hongzong_wumiankui", "hongzong_wumiankui", [("facecovermail_plume", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 745, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangpian_wumainkui", "gangpian_wumainkui", [("helm9", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 766, weight(2.250000)|abundance(20)|difficulty(10)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["yuanpian_humiankui", "yuanpian_humiankui", [("helmet_4", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 720, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_plate], 
["guizu_wumainkui", "guizu_wumainkui", [("inv_litchina_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 710, weight(2.250000)|abundance(20)|difficulty(11)|head_armor(57)|body_armor(0)|leg_armor(0), imodbits_plate], 
["yaunding_wumiankui", "yaunding_wumiankui", [("inv_nikolskoe_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 713, weight(2.250000)|abundance(20)|difficulty(11)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_plate], 
["shouling_wumiankui", "shouling_wumiankui", [("inv_novogrod_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 724, weight(2.500000)|abundance(20)|difficulty(12)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["lianjia_hubikui", "lianjia_hubikui", [("inv_rus_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 476, weight(2.000000)|abundance(20)|difficulty(8)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_plate], 
["shouling_lianjia_hubikui", "shouling_lianjia_hubikui", [("inv_tagancha_helm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 489, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(47)|body_armor(0)|leg_armor(0), imodbits_plate], 
["shouling_hubi_wumiankui", "shouling_hubi_wumiankui", [("inv_tagancha_helm_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 501, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(49)|body_armor(0)|leg_armor(0), imodbits_plate], 

["beak_mask", "Beak Mask", #鸟嘴面具
   [("witcher_mask_1", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair, 0, 140, 
   weight(1.75)|abundance(5)|difficulty(0)|head_armor(19)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["beak_hood", "Beak Hood", #鸟嘴兜帽
   [("witcher_mask_1_wear", 0)], 
   itp_type_head_armor, 0, 200, 
   weight(2.25)|abundance(5)|difficulty(0)|head_armor(25)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["beak_dome_hat", "Beak Dome Hat", #鸟嘴圆顶帽
   [("ouzhwytopper", 0)], 
   itp_type_head_armor, 0, 400, 
   weight(2.5)|abundance(5)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["beak_helmet", "Beak Helmet", #鸟嘴盔
   [("trainer_coap", 0)], 
   itp_type_head_armor, 0, 700, 
   weight(3.5)|abundance(5)|difficulty(13)|head_armor(44)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["white_beak_helmet", "White Beak Helmet", #白影鸟嘴盔
   [("beak_white", 0)], 
   itp_type_head_armor, 0, 700, 
   weight(3.5)|abundance(5)|difficulty(13)|head_armor(44)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 

#光瘴学派
["marsh_knight_helmet", "Marsh Knight Helmet", #噩沼骑士盔
   [("gondor_dolamroth_knight_helm", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 1676, 
   weight(2.5)|abundance(30)|difficulty(13)|head_armor(54)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 

["the_fault", "The Fault", #秘史面纱
   [("smoke_head_white", 0)], 
   itp_type_head_armor|itp_covers_head|itp_civilian, 0, 5000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), 
   imodbits_none, [
    (ti_on_init_item, [
        (set_position_delta, 0, 10, 0),
        (particle_system_add_new, "psys_history_mist_white"),
        (set_current_color, 150, 130, 70),
    ]),
  ]], 
["the_absurd", "The Absurd", #谬史之雾
   [("smoke_head_black", 0)], 
   itp_type_head_armor|itp_covers_head|itp_civilian, 0, 5000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), 
   imodbits_none, [
    (ti_on_init_item, [
        (set_position_delta, 0, 10, 0),
        (particle_system_add_new, "psys_history_mist_black"),
        (set_current_color, 150, 130, 70),
    ]),
  ]], 
["optihazation_knight_helmet", "Optihazation Knight Helmet", #光瘴骑士盔
   [("optization_knight_helm", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0, 10000, 
   weight(2.5)|abundance(30)|difficulty(13)|head_armor(54)|body_armor(0)|leg_armor(0), 
   imodbits_plate, [
    (ti_on_init_item, [
        (set_position_delta, 0, 10, 0),
        (particle_system_add_new, "psys_history_mist_white"),
        (set_current_color, 150, 130, 70),
#        (add_point_light, 10, 30),
    ]),
  ]], 

#Special Knight Helmets
["wing_guard_helmet", "Wing Guard Helmet", #翼侍头盔
   [("mirkwoodroyalarcher", 0)], 
   itp_type_head_armor, 0, 1340, 
   weight(3)|abundance(20)|difficulty(12)|head_armor(49)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["gorgeous_eagle_helmet", "Gorgeous Eagle Helmet", #华丽神鸟盔
   [("swanhead", 0)], 
   itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 2010, 
   weight(3.5)|abundance(10)|difficulty(18)|head_armor(62)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 

#Purification Helmets
["divinecusp_knight_helmet", "Divinecusp Knight Helmet", #神牙骑士盔
   [("gondor_citadel_knight_helm", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1740, 
   weight(3.500000)|abundance(10)|difficulty(14)|head_armor(57)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["tempestminion_helmet", "Tempestminion Helmet", #风暴仆从盔
   [("storm_troop_simple", 0)], 
   itp_type_head_armor|itp_covers_head, 0, 2140, 
   weight(4)|abundance(10)|difficulty(15)|head_armor(69)|body_armor(3)|leg_armor(0), 
   imodbits_plate], 
["tempestbringer_helmet", "Tempestbringer Helmet", #风暴使者盔
   [("storm_troop", 0)], 
   itp_type_head_armor|itp_covers_head, 0, 2740, 
   weight(4.5)|abundance(10)|difficulty(17)|head_armor(72)|body_armor(3)|leg_armor(0), 
   imodbits_plate], 

["death_eagle_helmet", "Death Eagle Helmet", #死鹰头壳
   [("griffith_helmUV", 0)], 
   itp_type_head_armor, 0, 3040, 
   weight(5)|abundance(1)|difficulty(22)|head_armor(75)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 


#######PAPAL HELMET#########
#Light Helmets Used by Priest
["penance_blinder", "Penance Blinder", #苦修者眼罩
   [("blinder", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_fit_to_head, 0, 2, 
   weight(0.05)|abundance(70)|difficulty(0)|head_armor(2)|body_armor(0)|leg_armor(0), 
   imodbits_none], 
["pilgrim_hood", "Pilgrim_Hood", #朝圣者兜帽
   [("pilgrim_hood", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 25, 
   weight(1.250000)|abundance(100)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["shengnv_tiejin", "shengnv_tiejin", [("french_crown", 0)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3035, weight(0.250000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["xiunv_toujin", "xiunv_toujin", [("habit_white", 0)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 16, weight(0.250000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["xiunv_tiemian", "xiunv_tiemian", [("wimple_helm", 0)], itp_type_head_armor|itp_covers_head, 0, 986, weight(1.500000)|abundance(10)|difficulty(12)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_plate], 
["zhujiao_mao", "zhujiao_mao", [("bishop_mitre", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0, 2135, weight(1.500000)|abundance(1)|difficulty(0)|head_armor(44)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Soldier Helmets
["papal_hood", "Papal Hood", #教国兜帽
   [("papal_hood_black_light", 0)], 
   itp_type_head_armor|itp_merchandise, 0, 100, 
   weight(0.2)|abundance(30)|difficulty(0)|head_armor(25)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["papal_chain_hood", "Papal Chain Hood", #教国链甲兜帽
   [("papal_hood_black", 0)], 
   itp_type_head_armor|itp_merchandise, 0, 600, 
   weight(1)|abundance(20)|difficulty(12)|head_armor(45)|body_armor(5)|leg_armor(0), 
   imodbits_cloth], 
["papal_believer_hood", "Papal Believer Hood", #教国信徒兜帽
   [("papal_hood_white_light", 0)], 
   itp_type_head_armor, 0, 105, 
   weight(0.2)|abundance(30)|difficulty(0)|head_armor(26)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["papal_believer_chain_hood", "Papal Believer Chain Hood", #教国信徒链甲兜帽
   [("papal_hood_white", 0)], 
   itp_type_head_armor, 0, 620, 
   weight(1)|abundance(20)|difficulty(12)|head_armor(46)|body_armor(5)|leg_armor(0), 
   imodbits_cloth], 

["penance_hood", "Penance Hood", #苦修者兜帽
   [("papal_hood_penance_light", 0)], 
   itp_type_head_armor, 0, 109, 
   weight(0.2)|abundance(25)|difficulty(0)|head_armor(28)|body_armor(5)|leg_armor(0), 
   imodbits_cloth], 
["penance_chain_hood", "Penance Chain Hood", #苦修者链甲兜帽
   [("papal_hood_penance", 0)], 
   itp_type_head_armor, 0, 624, 
   weight(1)|abundance(15)|difficulty(12)|head_armor(47)|body_armor(5)|leg_armor(0), 
   imodbits_cloth], 
["iron_sister_chain_hood", "Iron Sister Chain Hood", #铁修女链甲兜帽
   [("papal_hood_nun", 0)], 
   itp_type_head_armor, 0, 1020, 
   weight(1)|abundance(5)|difficulty(14)|head_armor(58)|body_armor(5)|leg_armor(0), 
   imodbits_cloth], 

["jiaoguo_sheshoukui", "jiaoguo_sheshoukui", [("kettle_hat_ca", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 880, weight(2.750000)|abundance(70)|difficulty(12)|head_armor(57)|body_armor(1)|leg_armor(0), imodbits_plate], 
["shengeqishi_fumiankui", "shengeqishi_fumiankui", [("helm16", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1047, weight(3.000000)|abundance(10)|difficulty(15)|head_armor(62)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Great Helmets
["great_helmet", "Great_Helmet", [("great_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 936, weight(2.750000)|abundance(100)|difficulty(11)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_tongkui", "gangshizi_tongkui", [("great_helm_1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_head, 0, 1085, weight(3.000000)|abundance(40)|difficulty(12)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_dakui", "gangshizi_dakui", [("great_helm_2", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.000000)|abundance(40)|difficulty(12)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_jukui", "gangshizi_jukui", [("great_helm_3", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1085, weight(3.000000)|abundance(40)|difficulty(12)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_niujiao_dakui", "gangshizi_niujiao_dakui", [("great_horned_helm_1", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.250000)|abundance(30)|difficulty(12)|head_armor(71)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_niujiao_dakui2", "gangshizi_niujiao_dakui2", [("great_horned_helm_2", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.250000)|abundance(30)|difficulty(12)|head_armor(71)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_niujiao_dakui3", "gangshizi_niujiao_dakui3", [("great_horned_helm_3", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.250000)|abundance(30)|difficulty(12)|head_armor(71)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_yi_dakui", "gangshizi_yi_dakui", [("great_winged_helm_1", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.250000)|abundance(30)|difficulty(12)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_yi_tongkui", "gangshizi_yi_tongkui", [("great_winged_helm_2", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.000000)|abundance(30)|difficulty(12)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangshizi_yi_jukui", "gangshizi_yi_jukui", [("great_winged_helm_3", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1085, weight(3.250000)|abundance(30)|difficulty(12)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaoguo_zhongkui", "jiaoguo_zhongkui", [("maciejowskihelm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 978, weight(3.000000)|abundance(30)|difficulty(14)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaoguo_guzhi_chaozhongkui", "jiaoguo_guzhi_chaozhongkui", [("helmet_20", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1008, weight(4.000000)|abundance(20)|difficulty(16)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaoguo_guzhi_chaozhongjiaokui", "jiaoguo_guzhi_chaozhongjiaokui", [("helmet_21", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 1008, weight(4.250000)|abundance(20)|difficulty(16)|head_armor(74)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaoguo_tongkui", "jiaoguo_tongkui", [("crusader_great_helmet2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 946, weight(3.000000)|abundance(20)|difficulty(11)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Special Helmet
["shield_angel", "Shield Angel", #盾天使
   [("shield_angel_head", 0)], 
   itp_type_head_armor|itp_unique|itp_covers_head|itp_attachment_mask, 0, 50000, 
   weight(4)|abundance(1)|difficulty(0)|head_armor(120)|body_armor(0)|leg_armor(0), 
   imodbits_none], 
["key_of_all_doors", "Key of All Doors", #门之钥
   [("firekeeper_4", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_fit_to_head, 0, 20000, 
   weight(0.5)|abundance(1)|difficulty(0)|head_armor(58)|body_armor(0)|leg_armor(0), 
   imodbits_none], 
["treacherous_halo", "Treacherous Halo", #诡秘光环
   [("treacherous_halo", 0)], 
   itp_type_head_armor|itp_unique|itp_doesnt_cover_hair|itp_civilian|itp_attachment_mask, 0, 40000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(80)|body_armor(25)|leg_armor(25), 
   imodbits_none], 

["halo", "Halo", #光环
   [("halo", 0)], 
   itp_type_head_armor|itp_unique|itp_doesnt_cover_hair|itp_civilian|itp_attachment_mask, 0, 30000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(70)|body_armor(30)|leg_armor(30), 
   imodbits_none], 
["paladin_halo_helmet", "Paladin Halo Helmet", #圣骑士光环盔
   [("paladin_halo", 0)], 
   itp_type_head_armor|itp_covers_head, 0, 42000, 
   weight(2.5)|abundance(1)|difficulty(12)|head_armor(130)|body_armor(30)|leg_armor(30), 
   imodbits_plate], 
["fragment_of_heaven", "Fragment of Heaven", #无垢天垣的一角
   [("zhujiaotk", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0, 60000, 
   weight(2)|abundance(1)|difficulty(10)|head_armor(100)|body_armor(40)|leg_armor(40), 
   imodbits_none], 


#######EASTERN HELMET#########
#Militia Helmets
["buba_kui", "buba_kui", [("DaMing_helmet_05", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 380, weight(2.000000)|abundance(100)|difficulty(6)|head_armor(32)|body_armor(2)|leg_armor(0), imodbits_cloth], 

#Soldier Helmets
["jiji_kui", "jiji_kui", [("mon_h_from12th", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 650, weight(2.500000)|abundance(100)|difficulty(8)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["strange_helmet", "Strange_Helmet", [("samurai_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 1224, weight(3.000000)|abundance(10)|difficulty(9)|head_armor(54)|body_armor(2)|leg_armor(0), imodbits_plate], 
["ruishi_kui", "ruishi_kui", [("DaMing_helmet_02", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1100, weight(3.000000)|abundance(10)|difficulty(15)|head_armor(60)|body_armor(6)|leg_armor(0), imodbits_cloth], 
["gauizima_kui", "gauizima_kui", [("DaMing_helmet_07", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1000, weight(3.000000)|abundance(10)|difficulty(13)|head_armor(62)|body_armor(7)|leg_armor(0), imodbits_cloth], 
["jicha_kui", "jicha_kui", [("fysg_toukui03", 0)], itp_type_head_armor|itp_merchandise, 0, 1000, weight(3.000000)|abundance(10)|difficulty(12)|head_armor(65)|body_armor(7)|leg_armor(0), imodbits_cloth], 

#Officer Helmets
["dongfangjunguan_kui", "dongfangjunguan_kui", [("DaMing_helmet", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1300, weight(3.000000)|abundance(10)|difficulty(15)|head_armor(65)|body_armor(8)|leg_armor(0), imodbits_cloth], 
["tielinjun_kui", "tielinjun_kui", [("DaMing_helmet_20", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 1300, weight(3.000000)|abundance(10)|difficulty(21)|head_armor(80)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["baiganjun_kui", "baiganjun_kui", [("DaMing_helmet_19", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1300, weight(3.000000)|abundance(10)|difficulty(15)|head_armor(65)|body_armor(8)|leg_armor(0), imodbits_cloth], 
["cangtoujun_kui", "cangtoujun_kui", [("DaMing_helmet_14", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1300, weight(3.000000)|abundance(20)|difficulty(15)|head_armor(65)|body_armor(8)|leg_armor(0), imodbits_cloth], 

#Elite Troop Helmets
["longxiang_kui", "longxiang_kui", [("helm_vijaynagri_royal", 0)], itp_type_head_armor|itp_merchandise, 0, 1650, weight(3.000000)|abundance(20)|difficulty(15)|head_armor(65)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["gulamu_kui", "gulamu_kui", [("kabuto", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1650, weight(3.500000)|abundance(10)|difficulty(15)|head_armor(65)|body_armor(8)|leg_armor(0), imodbits_cloth], 
["eastern_knight_helmet", "Eastern Knight Helmet", [("strom_troopshm1", 0)], itp_type_head_armor, 0, 1000, weight(3.000000)|abundance(1)|difficulty(13)|head_armor(63)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Kouruto Refugee
["dong_kelutuo_hongyukui", "dong_kelutuo_hongyukui", [("spangenhelm_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 579, weight(2.000000)|abundance(40)|difficulty(9)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 
["kelutuolangren_kui", "kelutuolangren_kui", [("DaMing_helmet_19_combined", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 535, weight(2.000000)|abundance(40)|difficulty(10)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["kelutuolangren_tonglingkui", "kelutuolangren_tonglingkui", [("cvcopy_Han_g_head21", 0)], itp_type_head_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 878, weight(2.000000)|abundance(40)|difficulty(0)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_cloth], 


#######WEST COAST HELMET#########
#Daily Hats
["xihai_guizumao", "xihai_guizumao", [("tricorne_goldlace_cockade_white", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 123, weight(0.750000)|abundance(20)|difficulty(0)|head_armor(25)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["xihai_guizumao2", "xihai_guizumao2", [("tricorne_whitelace_nocockade", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 123, weight(0.750000)|abundance(100)|difficulty(0)|head_armor(25)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Pirate Style
["nasal_helmet", "Nasal_Helmet", [("nasal_helmet_b", 0)], itp_type_head_armor|itp_merchandise, 0, 242, weight(1.250000)|abundance(100)|difficulty(7)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_plate], 
["spiked_helmet", "Spiked_Helmet", [("spiked_helmet_new", 0)], itp_type_head_armor|itp_merchandise, 0, 392, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_archer_helmet", "Nordic_Leather_Helmet", [("Helmet_A_vs2", 0)], itp_type_head_armor|itp_merchandise, 0, 40, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(23)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_veteran_archer_helmet", "Nordic_Leather_Helmet", [("Helmet_A", 0)], itp_type_head_armor|itp_merchandise, 0, 71, weight(1.250000)|abundance(100)|difficulty(6)|head_armor(28)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_footman_helmet", "Nordic_Footman_Helmet", [("Helmet_B_vs2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 352, weight(1.250000)|abundance(100)|difficulty(7)|head_armor(37)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_fighter_helmet", "Nordic_Fighter_Helmet", [("Helmet_B", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 542, weight(1.250000)|abundance(100)|difficulty(7)|head_armor(38)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_helmet", "Nordic_Helmet", [("helmet_w_eyeguard_new", 0)], itp_type_head_armor|itp_merchandise, 0, 412, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_huscarl_helmet", "Nordic_Huscarl's_Helmet", [("Helmet_C_vs2", 0)], itp_type_head_armor|itp_merchandise, 0, 694, weight(1.500000)|abundance(100)|difficulty(9)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_plate], 
["nordic_warlord_helmet", "Nordic_Warlord_Helmet", [("Helmet_C", 0)], itp_type_head_armor|itp_merchandise, 0, 787, weight(1.750000)|abundance(100)|difficulty(12)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 
["xihan_lingjiamao", "xihan_lingjiamao", [("copy_Helmet_C", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 781, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 
["xihai_dingshikui", "xihai_dingshikui", [("dux_ridge_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 766, weight(2.000000)|abundance(30)|difficulty(10)|head_armor(52)|body_armor(0)|leg_armor(0), imodbits_plate], 
["xihai_shoulingkui", "xihai_shoulingkui", [("valsgarde", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 800, weight(2.500000)|abundance(10)|difficulty(12)|head_armor(58)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jianyixihai_shoulingkui", "jianyixihai_shoulingkui", [("vendel", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 750, weight(2.250000)|abundance(10)|difficulty(11)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_plate], 
["xihai_wenshikui", "xihai_wenshikui", [("barf_helm", 0)], itp_type_head_armor|itp_merchandise, 0, 832, weight(2.000000)|abundance(30)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["xihai_niujiaokui", "xihai_niujiaokui", [("horned_helm_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 887, weight(2.750000)|abundance(50)|difficulty(10)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["kuangzhanshi_kui", "kuangzhanshi_kui", [("acb1_helm", 0)], itp_type_head_armor|itp_merchandise, 0, 1650, weight(3.000000)|abundance(20)|difficulty(0)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Diemer Style
["xihai_yuandingkui", "xihai_yuandingkui", [("norman", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 734, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate], 
["xihai_fumiankui", "xihai_fumiankui", [("norman_mask", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 744, weight(2.250000)|abundance(20)|difficulty(10)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["banmian_lianjiakui", "banmian_lianjiakui", [("vaeg_helmet81", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 567, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jianhu_lianjiakui", "jianhu_lianjiakui", [("vaeg_helmet51", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 588, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(48)|body_armor(1)|leg_armor(0), imodbits_plate], 
["jianhu_hualifuhe_kui", "jianhu_hualifuhe_kui", [("wjyfbzmk", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 889, weight(2.500000)|abundance(20)|difficulty(0)|head_armor(54)|body_armor(1)|leg_armor(0), imodbits_plate], 
["wumian_lianjiakui", "wumian_lianjiakui", [("face_cover_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 843, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(48)|body_armor(2)|leg_armor(0), imodbits_plate], 
["xihai_guizukui", "xihai_guizukui", [("inv_nord_ornate_visored_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1014, weight(2.250000)|abundance(20)|difficulty(10)|head_armor(59)|body_armor(0)|leg_armor(0), imodbits_plate], 

#巨盔
["scarlet_heavy_helmet", "Scarlet Heavy Helmet", #猩红重盔
   [("col2_bolzanobucket", 0)], 
   itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 844, 
   weight(3.25)|abundance(10)|difficulty(11)|head_armor(64)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 
["blood_angel_heavy_helmet", "Blood Angel Heavy Helmet", #血天使重盔
   [("col2_gotlandbucket", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 1434, 
   weight(3.25)|abundance(5)|difficulty(13)|head_armor(67)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 

#绯世
["blood_veil", "Blood Veil", #血丝面纱
   [("crimson_helmet_1", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_unique, 0, 3844, 
   weight(0.25)|abundance(1)|difficulty(0)|head_armor(54)|body_armor(7)|leg_armor(0), 
   imodbits_none], 
["hood_of_the_red_raven", "Hood of the Red Raven", #红鸦之兜
   [("crimson_helmet_2", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_unique, 0, 5584, 
   weight(0.5)|abundance(1)|difficulty(0)|head_armor(64)|body_armor(13)|leg_armor(0), 
   imodbits_none], 
["red_dream_heavy_crown", "Red Dream Heavy Crown", #赤梦重冠
   [("crimson_helmet_4", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_unique, 0, 9584, 
   weight(1)|abundance(1)|difficulty(0)|head_armor(77)|body_armor(3)|leg_armor(0), 
   imodbits_none], 
["blood_tide_ironclad", "Blood Tide Ironclad", #血潮铁壁
   [("crimson_helmet_3", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_unique, 0, 12841, 
   weight(1.25)|abundance(1)|difficulty(0)|head_armor(84)|body_armor(3)|leg_armor(0), 
   imodbits_none], 
["bloody_moon_halo", "Bloody Moon Halo", #血月
   [("moon_halo", 0)], 
   itp_type_head_armor|itp_unique|itp_covers_head|itp_civilian|itp_attachment_mask, 0, 35000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(60)|body_armor(15)|leg_armor(15), 
   imodbits_none], 


#######STATE HELMET#########
#Daily Hats
["heise_gongmingmao", "heise_gongmingmao", [("officerhatblack", 0), ("officerhatblack.1", 0)], itp_type_head_armor|itp_merchandise, 0, 78, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(21)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["lanse_gongmingmao", "lanse_gongmingmao", [("officerhatblue", 0), ("officerhatblue.1", 0)], itp_type_head_armor|itp_merchandise, 0, 78, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(21)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["zongse_gongmingmao", "zongse_gongmingmao", [("officerhatbrown", 0), ("officerhatbrown.1", 0)], itp_type_head_armor|itp_merchandise, 0, 78, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(21)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["shenhong_gongmingmao", "shenhong_gongmingmao", [("brownhat1", 0)], itp_type_head_armor|itp_merchandise, 0, 78, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(21)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["yuanding_limao", "yuanding_limao", [("brownhat2", 0)], itp_type_head_armor|itp_merchandise, 0, 68, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["heise_limao", "heise_limao", [("blackhat2", 0)], itp_type_head_armor|itp_merchandise, 0, 68, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["lanse_limao", "lanse_limao", [("bluehat1", 0)], itp_type_head_armor|itp_merchandise, 0, 68, weight(0.500000)|abundance(50)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Soldier Helmets 
["qianse_longxikui", "qianse_longxikui", [("lobster2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 466, weight(1.500000)|abundance(30)|difficulty(7)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_plate], 
["shense_longxikui", "shense_longxikui", [("lobster1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 466, weight(1.500000)|abundance(30)|difficulty(7)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Knight Helmets 
["duangang_qishikui", "duangang_qishikui", [("ds_knighta", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 949, weight(2.250000)|abundance(10)|difficulty(12)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["duanggang_qishizhangkui", "duanggang_qishizhangkui", [("ds_royal", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1232, weight(4.000000)|abundance(10)|difficulty(18)|head_armor(73)|body_armor(2)|leg_armor(0), imodbits_plate], 


#######UNDEAD HELMET#########
#Necromancer Helmet
["apprentice_pack_helmet", "Apprentice Pack Helmet", #学徒包头盔
   [("necro_skullcap_black", 0)], 
   itp_type_head_armor, 0, 70, 
   weight(0.2)|abundance(10)|difficulty(0)|head_armor(24)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["guguan", "guguan", [("nekromantahead1", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 11000, weight(0.500000)|abundance(1)|difficulty(0)|head_armor(36)|body_armor(0)|leg_armor(0), imodbits_none], 
["guguan_lianjiaxue", "guguan_lianjiaxue", [("nekromantahead2", 0)], itp_type_head_armor, 0, 11278, weight(1.500000)|abundance(1)|difficulty(0)|head_armor(43)|body_armor(0)|leg_armor(0), imodbits_none], 
["gu_wanguan", "gu_wanguan", [("nekromantahead3", 0)], itp_type_head_armor, 0, 12200, weight(2.000000)|abundance(1)|difficulty(0)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_none], 
["silingqishi_kui", "silingqishi_kui", [("deathknight", 0), ("deathknight.1", 0)], itp_type_head_armor, 0, 5034, weight(2.750000)|abundance(10)|difficulty(25)|head_armor(65)|body_armor(3)|leg_armor(0), imodbits_cloth], 
["silingzhujiao_kui", "silingzhujiao_kui", [("deathmaster", 0), ("deathmaster.1", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0, 5034, weight(2.750000)|abundance(10)|difficulty(25)|head_armor(65)|body_armor(3)|leg_armor(0), imodbits_cloth], 
["silingshuhsi_doumao", "silingshuhsi_doumao", [("demon_hood", 0)], itp_type_head_armor, 0, 980, weight(1.000000)|abundance(10)|difficulty(14)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["necro_helmet_female", "Necro Helmet Female", [("necro_helmet_female", 0)], itp_type_head_armor|itp_covers_head, 0, 1480, weight(3.250000)|abundance(1)|difficulty(15)|head_armor(64)|body_armor(6)|leg_armor(0), imodbits_plate], 
["necro_helmet", "Necro Helmet", [("necro_helmet", 0)], itp_type_head_armor|itp_covers_head, 0, 1380, weight(3.000000)|abundance(1)|difficulty(15)|head_armor(64)|body_armor(3)|leg_armor(0), imodbits_plate], 

#Zombie Helmet
["jiangshi_kui", "jiangshi_kui", [("bascinet_padded_01", 0)], itp_type_head_armor, 0, 827, weight(2.750000)|abundance(10)|difficulty(12)|head_armor(62)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Skeleton Helmet
["kuloutou", "kuloutou", [("barf_skull", 0)], itp_type_head_armor|itp_covers_head, 0, 1, weight(0.500000)|abundance(20)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["duangang_xiugaiqi", "duangang_xiugaiqi", [("scullhead4", 0)], itp_type_head_armor, 0, 980, weight(2.750000)|abundance(10)|difficulty(30)|head_armor(70)|body_armor(10)|leg_armor(0), imodbits_plate], 
["skeleton_king_chain_helmet", "Skeleton King Chain Helmet", [("DM_crown_helm_mail_demon", 0)], itp_type_head_armor, 0, 5480, weight(2.000000)|abundance(1)|difficulty(14)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate], 

["skull_unburned", "skull_unburned", [("barf_skull_unburned", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 1, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["skull_candle", "skull_candle", [("barf_skull_candle", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 1, weight(50.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["skeleton_blazing_thing_skull", "skeleton_blazing_thing_skull", [("barf_skeleton_blazing_thing_skull", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 1, weight(50.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["eternalflame_unburned_skull", "eternalflame_unburned_skull", [("eternalflame_unburned_skull", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 1, weight(50.000000)|abundance(1)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 

#Ghost Helmet
["ghost_tulbent", "Ghost Tulbent", [("ghost_tulbent", 0)], itp_type_head_armor|itp_unique|itp_covers_head|itp_attach_armature, 0, 10, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_none], 
["ghost_hood", "Ghost Hood", [("ghost_hood", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 50, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), imodbits_none], 
["ghost_leather_cap", "Ghost Leather Hood", [("ghost_leather_cap", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 90, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(18)|body_armor(0)|leg_armor(0), imodbits_none], 
["ghost_padded_coif", "Ghost Padded Coif", [("ghost_padded_coif", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 150, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_none], 
["ghost_mail_coif", "Ghost Mail Coif", [("ghost_mail_coif", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 600, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(29)|body_armor(0)|leg_armor(0), imodbits_none], 
["ghost_flattop_helmet", "Ghost Flattop Helmet", [("ghost_flattop_helmet", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0, 700, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_none], 
["ghost_bride_crown", "Ghost Bride Crown", [("ghost_bride_crown", 0)], itp_type_head_armor|itp_unique|itp_covers_head|itp_attach_armature, 0, 10, weight(0.000000)|abundance(1)|difficulty(0)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_none], 

#Walker
["jiangshitou_1", "jiangshitou_1", [("wight_face_1_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_head, 0, 1, weight(0.500000)|abundance(60)|difficulty(10)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["jiangshitou_2", "jiangshitou_2", [("wight_face_1_2", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_head, 0, 1, weight(0.500000)|abundance(60)|difficulty(10)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["jiangshitou_3", "jiangshitou_3", [("wight_face_helmet_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_head, 0, 1, weight(0.500000)|abundance(60)|difficulty(10)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 
["jiangshitou_4", "jiangshitou_4", [("wight_face_helmet_4", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_head, 0, 1, weight(0.500000)|abundance(60)|difficulty(10)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none], 


#######DEMON HELMET#########
["forsaken_hood", "Forsaken Hood", #弃世兜帽
   [("toutao_black_light", 0)], 
   itp_type_head_armor, 0, 100, 
   weight(0.2)|abundance(1)|difficulty(0)|head_armor(25)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["forsaken_chain_hood", "Forsaken Chain Hood", #弃世链甲兜帽
   [("toutao_black", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 600, 
   weight(1)|abundance(1)|difficulty(12)|head_armor(45)|body_armor(5)|leg_armor(0), 
   imodbits_plate], 
["devil_rider_hood", "Devil Rider Hood", #魔骑士盔
   [("DM_dragonrider_helmet", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 2500, 
   weight(3.000000)|abundance(1)|difficulty(14)|head_armor(63)|body_armor(2)|leg_armor(0), 
   imodbits_plate], 
["inhuman_helmet", "Inhuman Helmet", 
   [("inhuman_helmet", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 4500, 
   weight(5.250000)|abundance(1)|difficulty(25)|head_armor(73), 
   imodbits_plate], 
["bullhorn_inhuman_helmet", "Bullhorn Inhuman Helmet", 
   [("bullhorn_inhuman_helmet", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 4700, 
   weight(5.750000)|abundance(1)|difficulty(26)|head_armor(76), 
   imodbits_plate], 
["demon_berserker_helmet", "Demon Berserker Helmet", [("demon_berserker_helmet", 0)], itp_type_head_armor|itp_fit_to_head, 0, 8500, weight(5.500000)|abundance(1)|difficulty(30)|head_armor(85)|body_armor(0)|leg_armor(0), imodbits_plate], 
["mad_demon_helmet", "Mad Demon Helmet", #狂魔巨盔
   [("helmet_orc_skull", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 12500, 
   weight(6)|abundance(1)|difficulty(23)|head_armor(93)|body_armor(2)|leg_armor(0), 
   imodbits_plate], 
["dark_oath_helmet", "Dark Oath Helmet", #黑誓头盔
   [("Black_Knighth", 0)], 
   itp_type_head_armor|itp_covers_head, 0, 40078, 
   weight(5)|abundance(1)|difficulty(18)|head_armor(100)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 

["lemure_head", "Lemure Head", #劣魔头
   [("krag_bloodhowler_head", 0)], 
   itp_type_head_armor|itp_unique|itp_covers_head|itp_attachment_mask, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(60)|body_armor(0)|leg_armor(0), 
   imodbits_none], 


#######ABYSS HELMET#########
["abyss_cultist_hood", "Abyss Cultist Hood", #渊海信徒兜帽
   [("abyss_cultist_hood", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 70, 
   weight(0.25)|abundance(40)|difficulty(0)|head_armor(18)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["abyss_chain_hood", "Abyss Chain Hood", #渊海链甲兜帽
   [("abyss_cultist_hood_2", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 370, 
   weight(1)|abundance(40)|difficulty(8)|head_armor(37)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 
["deep_one_small_helmet", "Deep One Small Helmet", #渊海小盔
   [("abyss_helmet_1", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 580, 
   weight(2)|abundance(30)|difficulty(9)|head_armor(41)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["deep_one_strengthen_helmet", "Deep One Strengthen Helmet", #渊海加强盔
   [("abyss_helmet_2", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 900, 
   weight(2.5)|abundance(20)|difficulty(10)|head_armor(47)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 
["deep_one_jaw_protection_helmet", "Deep One Jaw Protection Helmet", #渊海护颚盔
   [("abyss_helmet_3", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 1130, 
   weight(2.5)|abundance(15)|difficulty(11)|head_armor(49)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 
["deep_one_simple_heavy_helmet", "Deep One Simple Heavy Helmet", #渊海简易重盔
   [("abyss_heavy_helmet", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 1230, 
   weight(2.75)|abundance(30)|difficulty(13)|head_armor(53)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["deep_one_elite_helmet", "Deep One Elite Helmet", #渊海精锐盔
   [("abyss_helmet_4", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 1800, 
   weight(3)|abundance(10)|difficulty(13)|head_armor(58)|body_armor(2)|leg_armor(0), 
   imodbits_plate], 
["deep_one_heavy_helmet", "Deep One Heavy Helmet", #渊海重盔
   [("abyss_heavy_helmet_2", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 2210, 
   weight(3.5)|abundance(15)|difficulty(17)|head_armor(62)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 

["phobia_facemask", "Phobia Facemask", #惧海面具
   [("abyss_facemask", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair|itp_civilian, 0, 2400, 
   weight(1.75)|abundance(5)|difficulty(12)|head_armor(40)|body_armor(1)|leg_armor(0), 
   imodbits_plate], 
["rip_current_assassin_helmet", "Rip Current Assassin Helmet", #裂流刺客盔
   [("abyss_assassin_hood", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 4244, 
   weight(2.5)|abundance(1)|difficulty(16)|head_armor(56)|body_armor(2)|leg_armor(0), 
   imodbits_plate], 
["tide_oracle_helmet", "Tide Oracle Helmet", #潮汐神谕盔
   [("abyss_helmet_5", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 9237, 
   weight(3.5)|abundance(1)|difficulty(18)|head_armor(70)|body_armor(3)|leg_armor(0), 
   imodbits_plate], 


#######SABIANISM HELMET#########
["shengnv_guan", "shengnv_guan", [("iron_crown_fem", 0), ("iron_crown_fem.1", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 770, weight(0.000000)|abundance(50)|difficulty(0)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["chunbaimiansha", "chunbaimiansha", [("sh_veil", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 370, weight(0.000000)|abundance(10)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth], 


#######ECLIPSE HELMET#########
["red_half_sallet", "Red Half Sallet", [("ashen_phoe_helmet_5", 0)], itp_type_head_armor|itp_merchandise, 0, 685, weight(1.750000)|abundance(10)|difficulty(0)|head_armor(49)|body_armor(0)|leg_armor(0), imodbits_plate], 
["red_half_sallet_open", "Red Half Sallet Open", [("ashen_phoe_helmet_11", 0)], itp_type_head_armor|itp_merchandise, 0, 685, weight(1.750000)|abundance(10)|difficulty(0)|head_armor(49)|body_armor(0)|leg_armor(0), imodbits_plate], 
["red_camail_sallet", "Red Camail Sallet", [("ashen_phoe_helmet_4", 0)], itp_type_head_armor|itp_merchandise, 0, 735, weight(2.000000)|abundance(10)|difficulty(0)|head_armor(55)|body_armor(1)|leg_armor(0), imodbits_plate], 
["red_camail_sallet_open", "Red Camail Sallet Open", [("ashen_phoe_helmet_13", 0)], itp_type_head_armor|itp_merchandise, 0, 735, weight(2.000000)|abundance(10)|difficulty(0)|head_armor(55)|body_armor(1)|leg_armor(0), imodbits_plate], 
["red_full_sallet", "Red Full Sallet", [("ashen_phoe_helmet_3", 0)], itp_type_head_armor|itp_merchandise, 0, 785, weight(2.250000)|abundance(10)|difficulty(0)|head_armor(60)|body_armor(1)|leg_armor(0), imodbits_plate], 
["red_full_sallet_open", "Red Full Sallet Open", [("ashen_phoe_helmet_9", 0)], itp_type_head_armor|itp_merchandise, 0, 785, weight(2.250000)|abundance(10)|difficulty(0)|head_armor(60)|body_armor(1)|leg_armor(0), imodbits_plate], 


#######DESERT HELMET#########
#Desert Women Headwearings
["sarranid_head_cloth", "Lady_Head_Cloth", [("tulbent", 0)], itp_type_head_armor|itp_attach_armature|itp_doesnt_cover_hair|itp_civilian|itp_next_item_as_melee, 0, 1, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["sarranid_head_cloth_b", "Lady_Head_Cloth", [("tulbent_b", 0)], itp_type_head_armor|itp_attach_armature|itp_doesnt_cover_hair|itp_civilian|itp_next_item_as_melee, 0, 1, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["sarranid_felt_head_cloth", "Head_Cloth", [("common_tulbent", 0)], itp_type_head_armor|itp_attach_armature|itp_civilian|itp_next_item_as_melee, 0, 1, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["sarranid_felt_head_cloth_b", "Head_Cloth", [("common_tulbent_b", 0)], itp_type_head_armor|itp_attach_armature|itp_civilian|itp_next_item_as_melee, 0, 1, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Desert Soldier Helmets
["sarranid_felt_hat", "Sarranid_Felt_Hat", [("sar_helmet3", 0)], itp_type_head_armor|itp_merchandise, 0, 16, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(5)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["turban", "Turban", [("tuareg_open", 0)], itp_type_head_armor|itp_merchandise, 0, 28, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(16)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["desert_turban", "Desert_Turban", [("tuareg", 0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 38, weight(1.500000)|abundance(100)|difficulty(0)|head_armor(18)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["sarranid_warrior_cap", "Sarranid_Warrior_Cap", [("tuareg_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 90, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate], 
["shahi", "Shahi", [("shahi", 0)], itp_type_head_armor|itp_merchandise, 0, 234, weight(1.000000)|abundance(100)|difficulty(6)|head_armor(27)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["sarranid_horseman_helmet", "Horseman_Helmet", [("sar_helmet2", 0)], itp_type_head_armor|itp_merchandise, 0, 180, weight(2.750000)|abundance(100)|difficulty(7)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["sarranid_helmet1", "Sarranid_Keffiyeh_Helmet", [("sar_helmet1", 0)], itp_type_head_armor|itp_merchandise, 0, 290, weight(2.500000)|abundance(100)|difficulty(7)|head_armor(35)|body_armor(0)|leg_armor(0), imodbits_plate], 
["rus_helmet_a", "Rus_Helmet", [("rus_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0, 337, weight(1.5)|abundance(100)|difficulty(0)|head_armor(37)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["sarranid_mail_coif", "Sarranid_Mail_Coif", [("tuareg_helmet2", 0)], itp_type_head_armor|itp_merchandise, 0, 430, weight(3.000000)|abundance(100)|difficulty(7)|head_armor(41)|body_armor(0)|leg_armor(0), imodbits_plate], 
["sarranid_veiled_helmet", "Sarranid_Veiled_Helmet", [("sar_helmet4", 0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 610, weight(3.500000)|abundance(100)|difficulty(8)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_plate], 
["sipahi_helmet_a", "Sipahi_Helmet", [("sipahi_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0, 372, weight(1.5)|abundance(100)|difficulty(7)|head_armor(43)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["rabati", "Rabati", [("rabati", 0)], itp_type_head_armor|itp_merchandise, 0, 635, weight(1.75)|abundance(100)|difficulty(0)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_cloth], 


#######BARBARIAN HELMET#########
["saman_kui", "saman_kui", [("white_headress", 0)], itp_type_head_armor|itp_merchandise, 0, 250, weight(3.000000)|abundance(20)|difficulty(6)|head_armor(35)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["bull_bone_helmet", "Bull Bone Helmet", #牛骨盔
   [("cow_helm", 0)], 
   itp_type_head_armor, 0, 280, 
   weight(8)|abundance(20)|difficulty(13)|head_armor(40)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 


#######DEATHBELL HELMET#########
#Basic Hoods
["professional_assassin_hood", "professional_assassin_hood", [("youhou_assassin_hood", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 280, weight(1.000000)|abundance(10)|difficulty(0)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["high_assassin_hood", "high_assassin_hood", [("drow_hood_b", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 434, weight(0.500000)|abundance(10)|difficulty(10)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_armor], 

#Special Troop Hoods
["war_assassin_hood", "war_assassin_hood", [("Saracen_Masked_helmet_d", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 631, weight(1.500000)|abundance(10)|difficulty(9)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 
["knell_assassin_hood", "knell_assassin_hood", [("drow_hood", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 434, weight(0.500000)|abundance(10)|difficulty(10)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_armor], 
["dancer_veil", "dancer_veil", [("belly_dancer_veil", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 381, weight(0.250000)|abundance(5)|difficulty(0)|head_armor(34)|body_armor(0)|leg_armor(0), imodbits_cloth], 


#######WITHCRAFT HELMET#########
["serpent_witchcraft_hat", "Serpent Witchcraft Hat", #蛇冠术士帽
   [("krag_kemmler_hat", 0)], 
   itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0, 1000, 
   weight(1.2)|abundance(1)|difficulty(0)|head_armor(38)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["snake_helmet", "Snake Helmet", #蟒革异形盔
   [("snake_helmet", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 2211, 
   weight(1.75)|abundance(1)|difficulty(16)|head_armor(50)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["venomblood_knight_helmet", "Venomblood Knight Helmet", #毒血骑士头盔
   [("duxue_fumiankui", 0)], 
   itp_type_head_armor|itp_fit_to_head, 0, 3211, 
   weight(2)|abundance(1)|difficulty(25)|head_armor(75)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 


#######ADVENTURER HELMET#########
["maoxianzhe_quankui", "maoxianzhe_quankui", [("haume1_balder", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 894, weight(2.750000)|abundance(30)|difficulty(9)|head_armor(63)|body_armor(0)|leg_armor(0), imodbits_plate], 
["maoxianzhe_shizikui", "maoxianzhe_shizikui", [("haume3_balder", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 988, weight(2.750000)|abundance(30)|difficulty(9)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 
["whitegold_helmet", "Whitegold Helmet", [("inhuman_helmet_2", 0)], itp_type_head_armor|itp_merchandise, 0, 3500, weight(3.250000)|abundance(1)|difficulty(18)|head_armor(65)|body_armor(0)|leg_armor(0), imodbits_plate], 
["bullhorn_whitegold_helmet", "Bullhorn Whitegold Helmet", [("bullhorn_inhuman_helmet_2", 0)], itp_type_head_armor, 0, 3700, weight(3.750000)|abundance(1)|difficulty(20)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 


#######MERCENARY HELMET#########
["guyongbing_tiekui", "guyongbing_tiekui", [("sarg_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 777, weight(1.750000)|abundance(70)|difficulty(9)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_plate], 
["guyongbing_zhongkui", "guyongbing_zhongkui", [("leduc_closed", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 877, weight(3.000000)|abundance(40)|difficulty(12)|head_armor(52)|body_armor(0)|leg_armor(0), imodbits_plate], 
["guyongbing_quankui", "guyongbing_quankui", [("qsk", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 805, weight(2.750000)|abundance(10)|difficulty(12)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["mercenary_knight_helmet", "Mercenary Knight Helmet", [("toukui", 0)], itp_type_head_armor, 0, 1000, weight(3.000000)|abundance(5)|difficulty(14)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 


#######COMMON HELMET#########
#Peasant Hat
["straw_hat", "Straw_Hat", [("straw_hat_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 9, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(2)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["head_wrappings", "Head_Wrapping", [("head_wrapping", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 16, weight(0.250000)|abundance(100)|difficulty(0)|head_armor(3)|body_armor(0)|leg_armor(0), imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick], 
["headcloth", "Headcloth", [("headcloth_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 1, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["wimple_a", "Wimple", [("wimple_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 10, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["wimple_with_veil", "Wimple_with_Veil", [("wimple_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 10, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["woolen_cap", "Woolen_Cap", [("woolen_cap_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 2, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["felt_hat", "Felt_Hat", [("felt_hat_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 4, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["felt_hat_b", "Felt_Hat", [("felt_hat_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 4, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["turret_hat_ruby", "Turret_Hat", [("turret_hat_r", 0)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 70, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["turret_hat_blue", "Turret_Hat", [("turret_hat_b", 0)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 80, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["turret_hat_green", "Barbette", [("barbette_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 70, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(6)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["court_hat", "Turret_Hat", [("court_hat", 0)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 80, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["female_hood", "Lady's_Hood", [("ladys_hood_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 9, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["common_hood", "Hood", [("hood_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 9, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["hood_b", "Hood", [("hood_b", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 9, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["hood_c", "Hood", [("hood_c", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 9, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["hood_d", "Hood", [("hood_d", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 9, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["woolen_hood", "Woolen_Hood", [("woolen_hood", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 4, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(13)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["leather_cap", "Leather_Cap", [("leather_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 6, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["black_hood", "Black_Hood", [("hood_black", 0)], itp_type_head_armor|itp_merchandise, 0, 33, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(18)|body_armor(0)|leg_armor(0), imodbits_cloth], 

#Soldier Helmets
["arming_cap", "Arming_Cap", [("arming_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 5, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(7)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["fur_hat", "Fur_Hat", [("fur_hat_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 4, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["padded_coif", "Padded_Coif", [("padded_coif_a_new", 0)], itp_type_head_armor|itp_merchandise, 0, 6, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(11)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["leather_warrior_cap", "Leather_Warrior_Cap", [("skull_cap_new_b", 0)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 14, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(21)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["skullcap", "Skullcap", [("skull_cap_new_a", 0)], itp_type_head_armor|itp_merchandise, 0, 120, weight(1.250000)|abundance(100)|difficulty(0)|head_armor(27)|body_armor(0)|leg_armor(0), imodbits_plate], 
["baotie_toujin", "baotie_toujin", [("cervelliere", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 118, weight(1.000000)|abundance(50)|difficulty(6)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate], 
["footman_helmet", "Footman's_Helmet", [("skull_cap_new", 0)], itp_type_head_armor|itp_merchandise, 0, 292, weight(1.500000)|abundance(100)|difficulty(7)|head_armor(31)|body_armor(0)|leg_armor(0), imodbits_plate], 
["segmented_helmet", "Segmented_Helmet", [("segmented_helm_new", 0)], itp_type_head_armor|itp_merchandise, 0, 343, weight(1.250000)|abundance(100)|difficulty(8)|head_armor(31)|body_armor(0)|leg_armor(0), imodbits_plate], 
["mail_coif", "Mail_Coif", [("mail_coif_new", 0)], itp_type_head_armor|itp_merchandise, 0, 142, weight(1.250000)|abundance(100)|difficulty(7)|head_armor(32)|body_armor(0)|leg_armor(0), imodbits_armor], 
["helmet_with_neckguard", "Helmet_with_Neckguard", [("neckguard_helm_new", 0)], itp_type_head_armor|itp_merchandise, 0, 372, weight(1.750000)|abundance(100)|difficulty(7)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_plate], 
["magyar_helmet_a", "Magyar_Helmet", [("magyar_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0, 221, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["ban_guokui", "ban_guokui", [("maciejowski_kettle", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 378, weight(1.250000)|abundance(40)|difficulty(7)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_plate], 
["wozhuangkui", "wozhuangkui", [("chapel-de-fer", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 389, weight(2.000000)|abundance(40)|difficulty(0)|head_armor(43)|body_armor(0)|leg_armor(0), imodbits_plate], 
["byzantion_helmet_a", "Byzantion_Helmet", [("byzantion_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0, 478, weight(2.000000)|abundance(100)|difficulty(0)|head_armor(41)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["jiushi_yuandingkui", "jiushi_yuandingkui", [("old_spangenhelmaven", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 478, weight(1.750000)|abundance(20)|difficulty(9)|head_armor(43)|body_armor(0)|leg_armor(0), imodbits_plate], 
["norman_helmet", "Helmet_with_Cap", [("norman_helmet_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 293, weight(1.250000)|abundance(100)|difficulty(8)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_plate], 
["bascinet", "Bascinet", [("bascinet_avt_new", 0)], itp_type_head_armor|itp_merchandise, 0, 474, weight(2.250000)|abundance(100)|difficulty(9)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_plate], 
["guard_helmet", "Guard_Helmet", [("reinf_helmet_new", 0)], itp_type_head_armor|itp_merchandise, 0, 554, weight(2.500000)|abundance(100)|difficulty(9)|head_armor(47)|body_armor(0)|leg_armor(0), imodbits_plate], 
["bascinet_2", "Bascinet_with_Aventail", [("bascinet_new_a", 0)], itp_type_head_armor|itp_merchandise, 0, 474, weight(2.250000)|abundance(100)|difficulty(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate], 
["bascinet_3", "Bascinet_with_Nose_Guard", [("bascinet_new_b", 0)], itp_type_head_armor|itp_merchandise, 0, 474, weight(2.250000)|abundance(100)|difficulty(9)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_plate], 
["black_helmet", "Black_Helmet", [("black_helm", 0)], itp_type_head_armor, 0, 638, weight(2.750000)|abundance(100)|difficulty(10)|head_armor(54)|body_armor(0)|leg_armor(0), imodbits_plate], 

["ban_qingbiankui", "ban_qingbiankui", [("visored_sallet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 685, weight(1.750000)|abundance(50)|difficulty(0)|head_armor(49)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmain_qingbiankui", "changmain_qingbiankui", [("open_sallet_coif", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 706, weight(2.000000)|abundance(40)|difficulty(10)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaqiang_qingbiankui", "jiaqiang_qingbiankui", [("new_sallet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 781, weight(2.250000)|abundance(30)|difficulty(12)|head_armor(63)|body_armor(3)|leg_armor(0), imodbits_plate], 

["yuanding_lianjiakui", "yuanding_lianjiakui", [("rhodok_pot_helmet_c", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 723, weight(2.500000)|abundance(40)|difficulty(0)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate], 
["baotou_lianjiakui", "baotou_lianjiakui", [("helmet_8", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 733, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate], 

["jianyia_jixingkui", "jianyia_jixingkui", [("toukui2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 710, weight(2.250000)|abundance(20)|difficulty(10)|head_armor(57)|body_armor(0)|leg_armor(0), imodbits_plate], 
["dingshi_lulmiankui", "dingshi_lulmiankui", [("steel_barbutte", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 723, weight(2.000000)|abundance(30)|difficulty(9)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Bandit Helmets
["baotu_tiekui", "baotu_tiekui", [("toukui1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 722, weight(2.000000)|abundance(20)|difficulty(10)|head_armor(56)|body_armor(0)|leg_armor(0), imodbits_plate], 
["baotu_jiaokui", "baotu_jiaokui", [("2kettle_hat_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 950, weight(3.500000)|abundance(30)|difficulty(14)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Pot Helmet
["lianjia_guokui", "lianjia_guokui", [("kettle_helm_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 454, weight(2.000000)|abundance(40)|difficulty(8)|head_armor(49)|body_armor(0)|leg_armor(0), imodbits_plate], 
["lianjia_quanfu_guokui", "lianjia_quanfu_guokui", [("masked_kettle_helm_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 512, weight(2.250000)|abundance(40)|difficulty(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate], 
["mao_guokui", "mao_guokui", [("helmet_10", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 454, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 
["mao_guokui2", "mao_guokui2", [("helmet_11", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 454, weight(2.000000)|abundance(20)|difficulty(9)|head_armor(46)|body_armor(0)|leg_armor(0), imodbits_plate], 
["kettle_hat", "Kettle_Hat", [("kettle_hat_new", 0)], itp_type_head_armor|itp_merchandise, 0, 402, weight(2.000000)|abundance(100)|difficulty(7)|head_armor(48)|body_armor(0)|leg_armor(0), imodbits_plate], 
["fuhe_guokui", "fuhe_guokui", [("prato_chapel-de-fer", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 783, weight(2.500000)|abundance(30)|difficulty(11)|head_armor(57)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaqiang_guokui", "jiaqiang_guokui", [("osp_kettle_hat_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 765, weight(2.250000)|abundance(40)|difficulty(11)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jiaqiang_guokui2", "jiaqiang_guokui2", [("osp_kettle_hat_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 765, weight(2.250000)|abundance(40)|difficulty(11)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate], 

["qinxing_jixingkui1", "qinxing_jixingkui1", [("classichelm_plume", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 767, weight(2.500000)|abundance(20)|difficulty(10)|head_armor(61)|body_armor(1)|leg_armor(0), imodbits_plate], 
["qinxing_jixingkui2", "qinxing_jixingkui2", [("classichelm_open", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 767, weight(2.500000)|abundance(20)|difficulty(10)|head_armor(61)|body_armor(1)|leg_armor(0), imodbits_plate], 

["zhuxing_fumiankui", "zhuxing_fumiankui", [("klappvisier", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 842, weight(2.000000)|abundance(10)|difficulty(11)|head_armor(59)|body_armor(0)|leg_armor(0), imodbits_plate], 
["goucao_fumainkui", "goucao_fumainkui", [("milanese_sallet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 851, weight(2.000000)|abundance(10)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Orthodox Knight Helmets
["full_helm", "Full_Helm", [("great_helmet_new_b", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 815, weight(2.500000)|abundance(100)|difficulty(10)|head_armor(57)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jinwen_fanmian_jianzuikui", "jinwen_fanmian_jianzuikui", [("hounskull", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["yuanding_fangmiankui", "yuanding_fangmiankui", [("visored_bascinet_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 855, weight(2.750000)|abundance(20)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heiyu_yuanding_fangmiankui", "heiyu_yuanding_fangmiankui", [("visored_bascinet_02", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 855, weight(2.750000)|abundance(20)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heizhong_yuanding_fangmiankui1", "heizhong_yuanding_fangmiankui1", [("visored_bascinet_03", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 855, weight(2.750000)|abundance(20)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmian_yuanding_fangmiankui", "changmian_yuanding_fangmiankui", [("visored_bascinet_04", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 855, weight(2.750000)|abundance(20)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["lanzong_yuanding_fangmiankui", "lanzong_yuanding_fangmiankui", [("ravenstern_bascinet_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 278, weight(2.750000)|abundance(100)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmian_lanzong_yuanding_fangmiankui", "changmian_lanzong_yuanding_fangmiankui", [("ravenstern_bascinet_02", 0)], itp_type_head_armor|itp_merchandise, 0, 855, weight(2.000000)|abundance(20)|difficulty(0)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["lianjia_qingbiankui", "lianjia_qingbiankui", [("sallet_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 760, weight(2.000000)|abundance(35)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["hue_qingbiankui", "hue_qingbiankui", [("sallet_02", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 785, weight(2.250000)|abundance(35)|difficulty(10)|head_armor(62)|body_armor(0)|leg_armor(0), imodbits_plate], 
["huangyu_lianjia_qingbiankui", "huangyu_lianjia_qingbiankui", [("sallet_03", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 760, weight(2.250000)|abundance(35)|difficulty(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jianliang_qingbiankui", "jianliang_qingbiankui", [("sallet_05", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 700, weight(1.750000)|abundance(35)|difficulty(9)|head_armor(58)|body_armor(0)|leg_armor(0), imodbits_plate], 
["hongyu_hue_qingbiankui", "hongyu_hue_qingbiankui", [("sallet_sarleon_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 785, weight(2.250000)|abundance(35)|difficulty(10)|head_armor(62)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jianzuikui", "jianzuikui", [("hounskull_bascinet_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmian_lanyu_jianzuikui", "changmian_lanyu_jianzuikui", [("ravenstern_bascinet_04", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(10)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heiyu_jianzuikui", "heiyu_jianzuikui", [("hounskull_bascinet_02", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["zhumiankui", "zhumiankui", [("hounskull_bascinet_03", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heiyu_zhumiankui", "heiyu_zhumiankui", [("hounskull_bascinet_04", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["fangmian_jianzuikui", "fangmian_jianzuikui", [("hounskull_bascinet_05", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmian_fangmian_jianzuikui", "changmian_fangmian_jianzuikui", [("hounskull_bascinet_06", 0)], itp_type_head_armor|itp_merchandise, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmian_jianzuikui", "changmian_jianzuikui", [("hounskull_bascinet_07", 0)], itp_type_head_armor|itp_merchandise, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heiyu_changmian_jianzuikui", "heiyu_changmian_jianzuikui", [("hounskull_bascinet_08", 0)], itp_type_head_armor|itp_merchandise, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmian_zhumiankui1", "changmian_zhumiankui1", [("hounskull_bascinet_09", 0)], itp_type_head_armor|itp_merchandise, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["mogang_zhumiankui", "mogang_zhumiankui", [("hounskull_black_01", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heiyu_mogang_zhumiankui", "heiyu_mogang_zhumiankui", [("hounskull_black_02", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["hongyu_zhumiankui", "hongyu_zhumiankui", [("hounskull_sarleon_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmain_hongyu_zhumiankui", "changmain_hongyu_zhumiankui", [("hounskull_sarleon_02", 0)], itp_type_head_armor|itp_merchandise, 0, 1100, weight(2.750000)|abundance(50)|difficulty(12)|head_armor(69)|body_armor(0)|leg_armor(0), imodbits_plate], 
["huodong_yuantikui", "huodong_yuantikui", [("flemish_armet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 876, weight(2.000000)|abundance(40)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["yuanti_kui", "yuanti_kui", [("armet_01", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 876, weight(2.000000)|abundance(40)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["baiyu_yuantikui", "baiyu_yuantikui", [("armet_02", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 876, weight(2.000000)|abundance(40)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmain_yuantikui", "changmain_yuantikui", [("armet_03", 0)], itp_type_head_armor|itp_merchandise, 0, 876, weight(2.000000)|abundance(40)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changmain_baiyu_yuantikui", "changmain_baiyu_yuantikui", [("armet_04", 0)], itp_type_head_armor|itp_merchandise, 0, 876, weight(2.000000)|abundance(40)|difficulty(11)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["fumain_kui", "fumain_kui", [("early_great_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 956, weight(2.750000)|abundance(20)|difficulty(12)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 
["jainyi_mogangkui", "jainyi_mogangkui", [("blackhelm", 0)], itp_type_head_armor|itp_merchandise, 0, 813, weight(3.000000)|abundance(30)|difficulty(12)|head_armor(65)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Special Knight Helmets
["wolf_knight_helmet", "Wolf Knight Helmet", [("wolfkinghthelmet", 0)], itp_type_head_armor|itp_covers_head, 0, 1000, weight(2.500000)|abundance(1)|difficulty(12)|head_armor(52)|body_armor(0)|leg_armor(0), imodbits_plate], 
["rogue_knight_helmet", "Rogue Knight Helmet", [("akatoshhelmet", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 800, weight(2.750000)|abundance(5)|difficulty(15)|head_armor(62)|body_armor(0)|leg_armor(0), imodbits_plate], 
["compassionate_knight_helmet", "Compassionate Knight Helmet", [("compassionate_knight_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 850, weight(2.750000)|abundance(5)|difficulty(15)|head_armor(63)|body_armor(0)|leg_armor(0), imodbits_plate], 
["curved_deformed_helmet", "Curved Deformed Helmet", [("tiltin_helmet", 0)], itp_type_head_armor|itp_merchandise, 0, 1280, weight(3.000000)|abundance(5)|difficulty(18)|head_armor(70)|body_armor(1)|leg_armor(0), imodbits_plate], 

["gliding_hero_helmet", "Gliding Hero Helmet", [("wangguo_shibing_kuiht", 0)], itp_type_head_armor, 0, 1500, weight(2.500000)|abundance(5)|difficulty(12)|head_armor(61)|body_armor(0)|leg_armor(0), imodbits_plate], 
["forged_hero_helmet", "Forged Hero Helmet", [("fahanhelmet", 0)], itp_type_head_armor|itp_covers_head, 0, 1100, weight(3.000000)|abundance(5)|difficulty(16)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 
["graghite_hero_helmet", "Graghite Hero Helmet", [("strom_troopshm2", 0)], itp_type_head_armor|itp_covers_head, 0, 2600, weight(3.500000)|abundance(5)|difficulty(20)|head_armor(75)|body_armor(8)|leg_armor(0), imodbits_plate], 

["red_bustling_helmet", "Red Bustling Helmet", [("gorieushelmetred", 0)], itp_type_head_armor|itp_covers_head|itp_merchandise, 0, 2000, weight(2.500000)|abundance(1)|difficulty(12)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["black_bustling_helmet", "Black Bustling Helmet", [("gorieushelmetebony", 0)], itp_type_head_armor|itp_covers_head|itp_merchandise, 0, 2000, weight(2.500000)|abundance(1)|difficulty(12)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["white_bustling_helmet", "White Bustling Helmet", [("gorieushelmet", 0)], itp_type_head_armor|itp_covers_head|itp_merchandise, 0, 2000, weight(2.500000)|abundance(1)|difficulty(12)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 

["qinse_qishikui", "qinse_qishikui", [("hm_hlf_s01X", 0)], itp_type_head_armor|itp_covers_head, 0, 1000, weight(2.500000)|abundance(5)|difficulty(15)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["baitie_qishikui", "baitie_qishikui", [("hm_hlf_s01Y", 0)], itp_type_head_armor|itp_covers_head, 0, 1000, weight(2.500000)|abundance(5)|difficulty(15)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["heijin_qishikui", "heijin_qishikui", [("hm_hlf_s01Z", 0)], itp_type_head_armor|itp_covers_head, 0, 1000, weight(2.500000)|abundance(5)|difficulty(18)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["duangang_yuanti_qishikui", "duangang_yuanti_qishikui", [("hm_hlf_s02U", 0)], itp_type_head_armor|itp_covers_head, 0, 1000, weight(2.500000)|abundance(5)|difficulty(15)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Great Helmets
["zhongxing_yuantikui", "zhongxing_yuantikui", [("classichelm_v_2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 800, weight(3.000000)|abundance(20)|difficulty(14)|head_armor(60)|body_armor(2)|leg_armor(0), imodbits_plate], 
["zhongxing_jixingkui", "zhongxing_jixingkui", [("UrscaHalfFace", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 810, weight(2.500000)|abundance(20)|difficulty(12)|head_armor(60)|body_armor(4)|leg_armor(0), imodbits_plate], 
["chaozhong_jixingkui", "chaozhong_jixingkui", [("spanishsallet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, weight(3.500000)|abundance(20)|difficulty(14)|head_armor(64)|body_armor(10)|leg_armor(0), imodbits_plate], 
["zhongxing_zhumiankui", "zhongxing_zhumiankui", [("greatbascinet1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 900, weight(3.000000)|abundance(10)|difficulty(13)|head_armor(63)|body_armor(1)|leg_armor(0), imodbits_plate], 
["winged_great_helmet", "Winged_Great_Helmet", [("maciejowski_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 947, weight(3.750000)|abundance(100)|difficulty(12)|head_armor(65)|body_armor(0)|leg_armor(0), imodbits_plate], 
["zhongxing_fangmainkui", "zhongxing_fangmainkui", [("french_helm_closed", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 899, weight(3.500000)|abundance(20)|difficulty(15)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["zhongxing_fangmainkui1", "zhongxing_fangmainkui1", [("french_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 899, weight(3.500000)|abundance(20)|difficulty(15)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_plate], 
["guiwen_zhongkui", "guiwen_zhongkui", [("sxn_great_helm", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1290, weight(3.000000)|abundance(10)|difficulty(13)|head_armor(74)|body_armor(0)|leg_armor(0), imodbits_plate], 
["gangtiao_tongkui", "gangtiao_tongkui", [("rhodok_great_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1030, weight(3.000000)|abundance(30)|difficulty(12)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 

["chaozhongkui", "chaozhongkui", [("osp_greathelm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0, 998, weight(4.000000)|abundance(20)|difficulty(15)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 
["changtongkui", "changtongkui", [("crusader_great_helmet", 0)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 946, weight(3.000000)|abundance(20)|difficulty(11)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 

#Special Headwearings
["dark_small_hood", "Dark Small Hood", #漆黑小兜帽
   [("hood_5", 0)], 
   itp_type_head_armor|itp_civilian, 0, 4, 
   weight(0.1)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["dark_hood", "Dark Hood", #漆黑兜帽
   [("hood_1", 0)], 
   itp_type_head_armor|itp_civilian, 0, 7, 
   weight(0.1)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["white_small_hood", "White Small Hood", #白色小兜帽
   [("hood_5", 0)], 
   itp_type_head_armor|itp_civilian, 0, 4, 
   weight(0.1)|abundance(100)|difficulty(0)|head_armor(8)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["white_hood", "White Hood", #白色兜帽
   [("hood_2", 0)], 
   itp_type_head_armor|itp_civilian, 0, 7, 
   weight(0.1)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["red_hood", "Red Hood", #暗红兜帽
   [("hood_3", 0)], 
   itp_type_head_armor|itp_civilian, 0, 7, 
   weight(0.1)|abundance(100)|difficulty(0)|head_armor(10)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["red_hood_mask", "Red Hood Mask", #暗红兜帽面罩
   [("hood_3b", 0)], 
   itp_type_head_armor|itp_civilian, 0, 11, 
   weight(0.2)|abundance(100)|difficulty(0)|head_armor(12)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["pale_mask", "Pale Mask", #苍白加厚兜帽
   [("hood_4", 0)], 
   itp_type_head_armor|itp_civilian, 0, 13, 
   weight(0.3)|abundance(100)|difficulty(0)|head_armor(13)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["faceless_mask", "Faceless Mask", #无面兜帽
   [("hood_4b", 0)], 
   itp_type_head_armor|itp_civilian|itp_covers_head, 0, 36, 
   weight(0.3)|abundance(100)|difficulty(0)|head_armor(18)|body_armor(2)|leg_armor(0), 
   imodbits_cloth], 

["party_mask", "Party Mask", #宴会假面
   [("Golden_Mask", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair|itp_civilian, 0, 65, 
   weight(0.2)|abundance(1)|difficulty(0)|head_armor(14)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["steel_mask", "Steel Mask", #铁假面
   [("Steel_Mask", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair|itp_civilian, 0, 45, 
   weight(1)|abundance(1)|difficulty(7)|head_armor(34)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 
["steel_veil", "Steel Veil", #铁面纱
   [("Steel_Veil", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair|itp_civilian, 0, 130, 
   weight(2)|abundance(1)|difficulty(11)|head_armor(48)|body_armor(0)|leg_armor(0), 
   imodbits_plate], 

["bride_crown", "Crown_of_Flowers", #新娘花冠
   [("bride_crown", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_doesnt_cover_hair|itp_civilian, 0, 1, 
   weight(0.5)|abundance(100)|difficulty(0)|head_armor(4)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["valkyrie_helmet", "Valkyrie Helmet", #女武神头盔
   [("valkyrie_head", 0)], 
   itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair|itp_unique, 0, 5, 
   weight(1.000000)|abundance(1)|difficulty(0)|head_armor(70)|body_armor(0)|leg_armor(0), 
   imodbits_none], 

["silver_glass", "Silver Glass", #银框眼镜
   [("h_mekane_c", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_doesnt_cover_hair|itp_civilian, 0, 1, 
   weight(0.5)|abundance(100)|difficulty(0)|head_armor(2)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 

["chains_hand", "Chains Hand", #颈手铐
   [("chains_hands", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_doesnt_cover_hair|itp_civilian, 0, 25, 
   weight(8)|abundance(20)|difficulty(0)|head_armor(12)|body_armor(2)|leg_armor(0), 
   imodbits_plate], 
["chains_full", "Chains Full", #全副镣铐
   [("chains_full", 0)], 
   itp_type_head_armor|itp_attachment_mask|itp_doesnt_cover_hair|itp_civilian, 0, 30, 
   weight(10)|abundance(20)|difficulty(0)|head_armor(12)|body_armor(2)|leg_armor(2), 
   imodbits_plate], 




#BOOT
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["boot_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5),imodbits_none],
#######PAPAL BOOT#########
["sedative_physician_high_heeled_boot", "Sedative Physician High Heeled Boot", #镇静医师高跟靴
   [("sedative_physician_boots", 0)], 
   itp_type_foot_armor|itp_civilian, 0, 600, 
   weight(2)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(26), 
   imodbits_cloth], 
["sedative_knight_high_heeled_boot", "Sedative Knight High Heeled Boot", #镇静骑士高跟靴
   [("sedative_knight_boots", 0)], 
   itp_type_foot_armor, 0, 2870, 
   weight(3)|abundance(1)|difficulty(10)|head_armor(0)|body_armor(0)|leg_armor(48), 
   imodbits_plate], 
["saint_dragon_knight_boot", "Saint Dragon Knight Boot", #圣龙骑士靴
   [("saint_dragon_knight_boot", 0)], 
   itp_type_foot_armor, 0, 3400, 
   weight(3.5)|abundance(1)|difficulty(20)|head_armor(0)|body_armor(0)|leg_armor(60), 
   imodbits_none], 

#龙孽
["dragon_abomination_leg", "Dragon Abomination Leg", #龙孽腿
   [("dragonmonster_boots", 0)], 
   itp_type_foot_armor|itp_unique, 0, 5000, 
   weight(6)|abundance(1)|difficulty(20)|head_armor(0)|body_armor(0)|leg_armor(63), 
   imodbits_none], 


#######YISHITH BOOT#########
["beifang_bangtui", "beifang_bangtui", [("dol_shoes", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 24, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(18), imodbits_cloth], 
["jingling_lieren_mianku", "jingling_lieren_mianku", [("gallic_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 54, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(15), imodbits_cloth], 
["beifang_mianku", "beifang_mianku", [("inca_boot", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 54, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(15), imodbits_cloth], 

["elf_knight_boot", "Elf Knight Boot", #精灵骑士靴
   [("DELFbody2_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 2840, 
   weight(0.75)|abundance(15)|difficulty(9)|head_armor(0)|body_armor(0)|leg_armor(39), 
   imodbits_plate], 
["emerald_boot", "Emerald Boot", #翡翠靴
   [("DELFbody1_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 3740, 
   weight(0.75)|abundance(10)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(47), 
   imodbits_plate], 
["elf_valkyrie_boot", "Elf Valkyrie Boot", #精灵女武神靴
   [("elf_knight_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 1000, 
   weight(0.75)|abundance(11)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(49), 
   imodbits_none],
["spiritual_boot", "Spiritual Boot", #灵树重靴
   [("lorien_palace_greaves", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 4040, 
   weight(1)|abundance(1)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(50), 
   imodbits_plate],  

["ice_knight_boot", "Ice Knight Boot", #寒冰骑士靴
   [("ice_knight_boots", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 8840, 
   weight(2.75)|abundance(1)|difficulty(16)|head_armor(0)|body_armor(20)|leg_armor(69), 
   imodbits_plate], 

["root_borning_one_foot", "Root Borning One Foot", #根生者腿
   [("root_foot", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 0, 
   weight(5.000000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(20), 
   imodbits_none],  


#######STEPPE BOOT#########
["khergit_leather_boots", "Khergit_Leather_Boots", [("khergit_leather_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian, 0, 120, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(18), imodbits_cloth], 
["khergit_guard_boots", "Khergit_Guard_Boots", [("lamellar_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 254, weight(2.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(25), imodbits_cloth], 

["kouruto_copper_boot", "Kouruto Copper Boot", #科鲁托赤铜靴
   [("dorn_guardsun_boots", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 1800, 
   weight(4)|abundance(1)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(47), 
   imodbits_plate], 


#######CONFEDERATION BOOT#########
["marsh_knight_boot", "Marsh Knight Boot", #噩沼骑士靴
   [("plate_boots_dthun", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 1500, 
   weight(3)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(35), 
   imodbits_plate], 
["spotless_plate_boot", "Spotless Plate Boot", #无垢板甲靴
   [("spotless_armor_boots", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2000, 
   weight(3)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(53), 
   imodbits_plate], 
["spotless_shadow_boot", "Spotless Shadow Boot", #无垢影袭板甲靴
   [("shadow_spotless_armor_boots", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2400, 
   weight(2.5)|abundance(10)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(50), 
   imodbits_plate], 

#谬史
["light_boot_of_soldiers", "Light Boot of Soldiers", #士兵们的轻靴
   [("history_boot_light", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 100, 
   weight(1.5)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(20), 
   imodbits_armor], 
["middle_boot_of_sergeants", "Middle Boot of Sergeants", #军士们的厚靴
   [("history_boot_middle", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 1100, 
   weight(2.5)|abundance(1)|difficulty(8)|head_armor(0)|body_armor(0)|leg_armor(37), 
   imodbits_armor], 
["heavy_boot_of_knights", "Heavy Boot of Knights", #骑士们的铁靴
   [("history_boot_heavy", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 2400, 
   weight(3)|abundance(1)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(52), 
   imodbits_plate], 


#######PAPAL BOOT#########
["papal_iron_boot", "Papal Iron Boot", #教国铁靴
   [("papal_iron_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_merchandise, 0, 900, 
   weight(3)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(52), 
   imodbits_plate], 
["saintess_boot", "Saintess Boot", #铁修女护膝靴
   [("saintess_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 1800, 
   weight(2.25)|abundance(5)|difficulty(11)|head_armor(0)|body_armor(3)|leg_armor(54), 
   imodbits_plate], 
["hymn_knight_boot", "Hymn Knight Boot", #讴歌者铁靴
   [("guanghui_zhanxue", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 2200, 
   weight(2.5)|abundance(1)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(57), 
   imodbits_plate], 
["reaper_knight_boot", "Reaper Knight Boot", #狩魔板甲靴
   [("heiyeqs_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature, 0, 1844, 
   weight(1.5)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(51), 
   imodbits_plate], 
["papal_elite_knight_boot", "Papal Elite Knight Boot", #教国精锐骑士靴
   [("arcene_boot", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_merchandise, 0, 1644, 
   weight(3.75)|abundance(10)|difficulty(19)|head_armor(0)|body_armor(0)|leg_armor(57), 
   imodbits_plate], 
["heroic_incarnation_stone_boot", "Heroic Incarnation Stone Boot", #英灵靴
   [("zhanshenxue", 0)], 
   itp_type_foot_armor|itp_unique|itp_attach_armature, 0, 10000, 
   weight(4)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(51), 
   imodbits_plate], 


#######EASTERN BOOT#########
["tuhuang_langrenxue", "tuhuang_langrenxue", [("mgj_boots_yunxue", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 230, weight(1.000000)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(27), imodbits_cloth], 
["langren_shoulinxue", "langren_shoulinxue", [("juanjia_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 230, weight(1.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(27), imodbits_cloth], 
["strange_boots", "Strange_Boots", [("samurai_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 965, weight(2.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(31), imodbits_cloth], 

["jiantouqibing_xue", "jiantouqibing_xue", [("DaMing_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise, 0, 570, weight(1.750000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(45), imodbits_cloth], 
["eastern_knight_boot", "Eastern Knight Boot", [("eastern_knight_boot", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise, 0, 3000, weight(3.000000)|abundance(10)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(56), imodbits_none], 
["shenwu_xue", "shenwu_xue", [("ylyq_zaoyun_xie1", 0)], itp_type_foot_armor|itp_attach_armature, 0, 5000, weight(3.500000)|abundance(10)|difficulty(25)|head_armor(0)|body_armor(00)|leg_armor(60), imodbits_none], 


#######STARKHOOK BOOT#########
["xihai_pixue", "xihai_pixue", [("infantry_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 120, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(18), imodbits_cloth], 
["westcoast_guard_boot", "Westcoast Guard Boot", [("drow_elite_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 2530, weight(1.000000)|abundance(10)|difficulty(15)|head_armor(0)|body_armor(0)|leg_armor(36), imodbits_plate], 
["kuangzhanshi_xue", "kuangzhanshi_xue", [("acb1_boo", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1560, weight(3.000000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(50), imodbits_cloth], 

#绯世
["crimson_foot", "Crimson Foot", #绯影之足
   [("crimson_foot", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(10), 
   imodbits_none],  
["crimson_flow_swiftstep", "Crimson Flow Swiftstep", #赤流疾步
   [("crimson_boot_1", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 4700, 
   weight(1)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(46), 
   imodbits_none],  
["veinnet_agility", "Veinnet Agility", #血网轻灵
   [("crimson_boot_2", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 5892, 
   weight(0.5)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(50), 
   imodbits_none],  
["sea_treading_blood_boot", "Sea Treading Blood Boot", #履海血靴
   [("crimson_boot_3", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 9000, 
   weight(1.5)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(70), 
   imodbits_none],  
["red_apostle_boot", "Red Apostle Boot", #红使徒靴
   [("crimson_boot_4", 0)], 
   itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 9200, 
   weight(2.5)|abundance(1)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(72), 
   imodbits_none],  


#######STATE BOOT#########
["state_knight_boot", "State Elite Knight Boot", #城邦骑士靴
   [("scepter_boot", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 2114, 
   weight(4)|abundance(10)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(63), 
   imodbits_plate], 
["consul_heavy_boot", "Consul Heavy Boot", #执政官重靴
   [("fasces_boot", 0)], 
   itp_type_foot_armor, 0, 4143, 
   weight(5)|abundance(1)|difficulty(20)|head_armor(0)|body_armor(0)|leg_armor(70), 
   imodbits_plate], 


#######UNDEAD BOOT#########
["necromancer_boot", "Necromancer Boot", [("necro_boot", 0)], itp_type_foot_armor|itp_attach_armature, 0, 1644, weight(3.750000)|abundance(1)|difficulty(19)|head_armor(0)|body_armor(0)|leg_armor(57), imodbits_plate], 

["skeleton_unburned_calf", "skeleton_unburned_calf", [("barf_skeleton_unburned_calf", 0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 1, weight(0.150000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(5), imodbits_none], 
["skeleton_candle_calf", "skeleton_candle_calf", [("barf_skeleton_candle_calf", 0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 1, weight(0.150000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(5), imodbits_none], 
["skeleton_blazing_thing_calf", "skeleton_blazing_thing_calf", [("barf_skeleton_blazing_thing_calf", 0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 1, weight(0.150000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(5), imodbits_none], 
["eternalflame_unburned_boot", "eternalflame_unburned_boot", [("eternalflame_unburned_boot", 0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 1, weight(0.150000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(5), imodbits_none], 

["ghost_boot", "ghost_boot", [("cw_no_head", 0)], itp_type_foot_armor|itp_unique, 0, 300, weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(25), imodbits_none], 

["victim_leg", "Victim Leg", #受难者腿
   [("zombie_calf", 0)], 
   itp_type_foot_armor|itp_unique, 0, 1, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(5), 
   imodbits_none], 


#######DEMON BOOT#########
["renmowushi_boot", "renmowushi_glove", [("knight_of_molag_bal_boots", 0)], itp_type_foot_armor|itp_attach_armature, 0, 5000, weight(3.000000)|abundance(10)|difficulty(20)|head_armor(0)|body_armor(0)|leg_armor(65), imodbits_armor], 
["dark_plate_boot", "dark_plate_boot", [("dark_plate_boot", 0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 6000, weight(3.000000)|abundance(1)|difficulty(25)|head_armor(0)|body_armor(0)|leg_armor(68), imodbits_none], 
["demon_knight_boot", "Demon Knight Boot", [("demon_knight_boot", 0)], itp_type_foot_armor|itp_attach_armature, 0, 8000, weight(3.500000)|abundance(1)|difficulty(25)|head_armor(0)|body_armor(10)|leg_armor(73), imodbits_armor], 
["dark_oath_shoe", "Dark Oath Shoe", #黑誓铁靴
   [("Black_Knightt", 0)], 
   itp_type_foot_armor, 0, 30000, 
   weight(7)|abundance(1)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(86), 
   imodbits_armor], 

["lemure_leg", "Lemure Leg", #劣魔腿
   [("krag_bloodhowler_foot", 0)], 
   itp_type_foot_armor|itp_unique, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(15), 
   imodbits_none], 


#######WITCHCRAFT BOOT#########
["snake_armor_boot", "Snake Armor Boot", [("snake_armor_boot", 0)], itp_type_foot_armor|itp_attach_armature, 0, 1043, weight(2.000000)|abundance(1)|difficulty(11)|head_armor(0)|body_armor(0)|leg_armor(46), imodbits_cloth], 


#######SABIANISM BOOT#########
["yinse_xue", "yinse_xue", [("bolster_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 1743, weight(1.000000)|abundance(20)|difficulty(6)|head_armor(0)|body_armor(0)|leg_armor(31), imodbits_cloth], 


#######ECLIPSE BOOT#########
["tongban_bangtui", "tongban_bangtui", [("brgreaves2", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 178, weight(3.000000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(28), imodbits_plate], 
["copper_noble_boot", "Copper Noble Boot", [("maserainnean_plate_1", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise, 0, 1178, weight(3.500000)|abundance(10)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(52), imodbits_plate], 


#######DESERT BOOT#########
["sarranid_boots_a", "Sarranid_Shoes", [("sarranid_shoes", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_civilian|itp_next_item_as_melee, 0, 30, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(12), imodbits_cloth], 
["sarranid_boots_b", "Sarranid_Leather_Boots", [("sarranid_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 120, weight(1.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(16), imodbits_cloth], 
["sarranid_boots_c", "Plated_Boots", [("sarranid_camel_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 280, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(25), imodbits_plate], 
["sarranid_boots_d", "Sarranid_Mail_Boots", [("sarranid_mail_chausses", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 320, weight(3.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(36), imodbits_armor], 


#######BARBARIAN BOOT#########
["wailai_manzuxue", "wailai_manzuxue", [("b_h2", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 483, weight(1.500000)|abundance(30)|difficulty(10)|head_armor(0)|body_armor(0)|leg_armor(28), imodbits_cloth], 
["manzu_pixue", "manzu_pixue", [("b_h1", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 783, weight(1.500000)|abundance(30)|difficulty(11)|head_armor(0)|body_armor(0)|leg_armor(31), imodbits_cloth], 



#######COMMON BOOT#########
#Peasant shoes
["bride_shoes", "Bride Shoes", #新娘鞋
   [("bride_shoes", 0)],    
   itp_type_foot_armor|itp_civilian, 0, 30, 
   weight(1)|abundance(100)|leg_armor(2), 
   imodbits_cloth], 
["wrapping_boots", "Wrapping Boots", #绑腿
   [("wrapping_boots_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 5, 
   weight(1)|abundance(100)|leg_armor(3), 
   imodbits_cloth], 
["woolen_hose", "Woolen Hose", #羊毛裤
   [("woolen_hose_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 10, 
   weight(1)|abundance(100)|leg_armor(5), 
   imodbits_cloth], 
["blue_hose", "Blue Hose", #蓝羊毛裤
   [("blue_hose_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 15, 
   weight(1)|abundance(100)|leg_armor(5), 
   imodbits_cloth], 
["ankle_boots", "Ankle Boots", #短靴
   [("ankle_boots_a_new", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 35, 
   weight(1)|abundance(100)|leg_armor(9), 
   imodbits_cloth], 
["hunter_boots", "Hunter Boots", 
   [("hunter_boots_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 20, 
   weight(1.25)|abundance(100)|leg_armor(9), 
   imodbits_cloth], 
["hide_boots", "Hide Boots", 
   [("hide_boots_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 25, 
   weight(1)|abundance(100)|leg_armor(13), 
   imodbits_cloth], 
["nomad_boots", "Nomad Boots", #游牧靴
   [("nomad_boots_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 70, 
   weight(1.25)|abundance(100)|leg_armor(14), 
   imodbits_cloth], 

#Light Boots
["light_leather_boots", "Light Leather Boots", #轻皮靴
   [("light_leather_boots", 0)],    
   itp_type_foot_armor|itp_merchandise, 0, 120, 
   weight(1)|abundance(100)|leg_armor(15), 
   imodbits_cloth], 
["leather_boots", "Leather Boots", #皮靴
   [("leather_boots_a", 0)], 
   itp_type_foot_armor|itp_merchandise|itp_civilian, 0, 200, 
   weight(1.25)|abundance(100)|leg_armor(17), 
   imodbits_cloth], 
["splinted_leather_greaves", "Splinted Leather Greaves", #夹板皮护腿
   [("splinted_greaves_a", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 250, 
   weight(2)|abundance(100)|leg_armor(21), 
   imodbits_armor], 
["female_ranger_leather_boot", "Female Ranger Leather Boot", #女游侠皮靴
   [("FKamael_m", 0)], 
   itp_type_foot_armor|itp_civilian, 0, 300, 
   weight(2)|abundance(5)|leg_armor(25), 
   imodbits_armor], 
["iron_leather_greave", "Iron Leather Greaves", #铁板护腿
   [("Annu_shoes", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 366, 
   weight(2)|abundance(50)|difficulty(7)|leg_armor(28), 
   imodbits_armor], 
["mail_chausses", "Mail Chausses", #链甲护腿
   [("mail_chausses_a", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 430, 
   weight(3)|abundance(100)|leg_armor(35), 
   imodbits_armor], 
["iron_leather_boot", "Iron Leather Boot", #铁板皮靴
   [("nord_splinted_greaves", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 500, 
   weight(2.5)|abundance(50)|leg_armor(31), 
   imodbits_armor], 
["nailed_iron_leather_boot", "Nailed Iron Leather Boot", #钉饰铁板皮靴
   [("splinted_greaves_nospurs", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 524, 
   weight(3)|abundance(30)|difficulty(11)|leg_armor(36), 
   imodbits_plate], 
["steel_leather_boot", "Steel Leather Boot", #钢皮靴
   [("steel_boots_inf", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 570, 
   weight(3.25)|abundance(30)|difficulty(13)|leg_armor(39), 
   imodbits_plate], 

#Ligature Nail Boots and Chain Boots
["splinted_greaves", "Splinted Greaves", #夹板链甲护腿
   [("leather_greaves_a", 0)], 
   itp_type_foot_armor|itp_merchandise, 0, 582, 
   weight(3.50)|abundance(100)|difficulty(7)|leg_armor(41), 
   imodbits_armor], 
["mail_boots", "Mail_Boots", [("mail_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 603, weight(3.500000)|abundance(100)|difficulty(8)|head_armor(0)|body_armor(0)|leg_armor(45), imodbits_armor], 
["iron_greaves", "Iron_Greaves", [("iron_greaves_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 844, weight(3.500000)|abundance(100)|difficulty(9)|head_armor(0)|body_armor(0)|leg_armor(51), imodbits_armor], 
["black_greaves", "Black_Greaves", [("black_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 1160, weight(3.750000)|abundance(100)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(55), imodbits_armor], 
["heise_banlianjiaxue", "heise_banlianjiaxue", [("shynbaulds_bk", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1000, weight(3.250000)|abundance(20)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(57), imodbits_plate], 
["lingjia_xue", "lingjia_xue", [("iron_greaves_a_j", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 632, weight(2.500000)|abundance(30)|difficulty(8)|head_armor(0)|body_armor(0)|leg_armor(43), imodbits_plate], 
["yinse_lianjiaxue", "yinse_lianjiaxue", [("gondor_heavy_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 470, weight(3.000000)|abundance(20)|difficulty(8)|head_armor(0)|body_armor(0)|leg_armor(37), imodbits_plate], 
["yinse_banlianxue", "yinse_banlianxue", [("dol_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 800, weight(3.000000)|abundance(20)|difficulty(9)|head_armor(0)|body_armor(0)|leg_armor(40), imodbits_plate], 

#Plate Boots
["shengtie_banjiaxue", "shengtie_banjiaxue", [("steel_greaves1", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 830, weight(3.500000)|abundance(30)|difficulty(13)|head_armor(0)|body_armor(0)|leg_armor(48), imodbits_plate], 
["guanze_banjiaxue", "guanze_banjiaxue", [("steel_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 947, weight(3.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(51), imodbits_plate], 
["wenli_banjiaxue", "wenli_banjiaxue", [("mtw2_greaves1", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 947, weight(3.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(51), imodbits_plate], 
["longwen_banjiaxue", "longwen_banjiaxue", [("plate_boots2", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 805, weight(2.750000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(50), imodbits_plate], 
["plate_boots", "Plate Boot", [("plate_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 805, weight(2.750000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(50), imodbits_plate], 
["duangang_banjiaxue", "duangang_banjiaxue", [("shynbaulds", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1045, weight(3.000000)|abundance(30)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(53), imodbits_plate], 
["huali_banjiaxue", "huali_banjiaxue", [("sxd_ornate_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1047, weight(3.000000)|abundance(50)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(51), imodbits_plate], 
["zhengshi_banjiaxue", "zhengshi_banjiaxue", [("boot3", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1134, weight(3.250000)|abundance(30)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(54), imodbits_plate], 
["zhongxing_banjiaxue", "zhongxing_banjiaxue", [("xie1", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 1567, weight(3.500000)|abundance(20)|difficulty(14)|head_armor(0)|body_armor(0)|leg_armor(56), imodbits_plate], 
["heise_gangbanxue", "heise_gangbanxue", [("black_steel_boots_01", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise, 0, 844, weight(3.750000)|abundance(80)|difficulty(12)|head_armor(0)|body_armor(0)|leg_armor(51), imodbits_plate], 

#Special Knight Boots
["valkyrie_boot", "Valkyrie Boot", [("valkyrie_boot", 0)], itp_type_foot_armor|itp_attach_armature, 0, 1000, weight(2.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(60), imodbits_none], 
["qinse_banjiaxue", "qinse_banjiaxue", [("hm_boo_masU", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 2000, weight(3.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(60), imodbits_plate], 
["qinse_banjiaxue", "qinse_banjiaxue", [("hm_boo_masU", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 2000, weight(3.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(60), imodbits_plate], 
["baitie_qishixue", "baitie_qishixue", [("hm_boo_masV", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 2000, weight(3.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(60), imodbits_plate], 
["heijin_qishixue", "heijin_qishixue", [("hm_boo_masW", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 1400, weight(2.750000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(56), imodbits_plate], 
["duangang_qishixue", "duangang_qishixue", [("hm_boo_masX", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm, 0, 1800, weight(3.000000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(0)|leg_armor(58), imodbits_plate], 
["wuzhe_pixue", "wuzhe_pixue", [("xena_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_force_attach_left_hand|itp_force_attach_right_hand|itp_force_attach_left_forearm|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 447, weight(1.000000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(32), imodbits_cloth], 




#GLOVES
#_______________________________________________________________________________________________________________________________________________________________________________
#Gloves are usually leather-made or textile-made, having less armor. Brassarts are always more solid and heavy, more militarized.
 ["glove_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
#######POWELL BRASSART#########
["perfumer_glove", "Perfumer Glove", #调香手套
   [("perfumer_glove_L", 0)], 
   itp_type_hand_armor|itp_merchandise|itp_civilian, 0, 200, 
   weight(0.25)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(1)|leg_armor(0), 
   imodbits_cloth], 
["sedative_gauntlet", "Sedative Gauntlet", #镇静护腕
   [("sedative_physician_hands_L", 0)], 
   itp_type_hand_armor, 0, 800, 
   weight(1.5)|abundance(1)|difficulty(10)|head_armor(0)|body_armor(11)|leg_armor(0), 
   imodbits_plate], 

["christer_hand", "Christer Hand", #克莉斯特手
   [("christer_hand_L", 0)], 
   itp_type_hand_armor|itp_unique|itp_civilian, 0, 0, 
   weight(1.5)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(15)|leg_armor(0), 
   imodbits_none], 
["dragon_abomination_hand", "Dragon Abomination Hand", #龙孽爪
   [("dragonmonster_handL", 0)], 
   itp_type_hand_armor|itp_unique|itp_civilian, 0, 8000, 
   weight(3)|abundance(1)|difficulty(24)|head_armor(0)|body_armor(30)|leg_armor(0), 
   imodbits_none], 
["dragon_abomination_gauntlet", "Dragon Abomination Gauntlet", #龙孽臂铠
   [("dragonmonster_heavy_handL", 0)], 
   itp_type_hand_armor|itp_unique|itp_civilian, 0, 12000, 
   weight(3.5)|abundance(1)|difficulty(32)|head_armor(0)|body_armor(34)|leg_armor(0), 
   imodbits_none], 

#######YSHITH BRASSART#########
["root_borning_one_hand", "Root Borning One Hand", #根生者手
   [("root_handL", 0)], 
   itp_type_hand_armor|itp_unique, 0, 0, 
   weight(3)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), 
   imodbits_none], 
["molting_failer_hand", "Molting Failer Hand", #蜕生失败者手
   [("human_apple_handL", 0)], 
   itp_type_hand_armor|itp_unique, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(2)|leg_armor(0), 
   imodbits_none], 

["ice_knight_hand", "Ice Knight Hand", #坚寒臂铠
  [("ice_knight_handL", 0)], 
  itp_type_hand_armor, 0, 4700, 
  weight(1.5)|abundance(1)|difficulty(14)|head_armor(0)|body_armor(18)|leg_armor(0), 
  imodbits_plate], 

#######CONFEDERATION BRASSART#########
["glove_of_soldiers", "Glove of Soldiers", #士兵们的手套
   [("history_hand_light_L", 0)], 
   itp_type_hand_armor, 0, 30, 
   weight(0.5)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(1)|leg_armor(0), 
   imodbits_armor], 
["gauntlet_of_sergeants", "Gauntlet of Sergeants", #军士们的护手
   [("history_hand_middle_L", 0)], 
   itp_type_hand_armor, 0, 210, 
   weight(2.0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(0), 
   imodbits_armor], 
["gauntlet_of_knights", "Gauntlet of Knights", #骑士们的臂铠
   [("history_hand_heavy_L", 0)], 
   itp_type_hand_armor, 0, 540, 
   weight(3.0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), 
   imodbits_plate], 

#######PAPAL BRASSART#########
["incarnation_stone_carving_glove", "Incarnation Stone Carving Glove", #英灵石刻手
   [("zhanshentouying_L", 0)], 
   itp_type_hand_armor|itp_unique, 0, 10000, 
   weight(2)|abundance(1)|difficulty(18)|head_armor(0)|body_armor(30)|leg_armor(0), 
   imodbits_none], 


#######STARKHOOK BRASSART#########
["westcoast_black_glove", "Westcoast Black Glove", [("drow_elite_gloves_L", 0)], itp_type_hand_armor, 0, 230, weight(0.250000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(3)|leg_armor(0), imodbits_cloth], 

["crimson_hand", "Crimson Hand", #猩红之手
   [("crimson_handL", 0)], 
   itp_type_hand_armor|itp_unique, 0, 13000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(3)|leg_armor(0), 
   imodbits_none], 
["grip_of_crimson_flow", "Grip of Crimson Flow", #赤流一握
   [("crimson_hand1_L", 0)], 
   itp_type_hand_armor|itp_unique, 0, 50000, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(14)|leg_armor(0), 
   imodbits_none], 


#######STATE BRASSART#########
["scepter_gauntlet", "Scepter Gauntlet", #权杖护手
   [("scepter_hand_L", 0)], 
   itp_type_hand_armor, 0, 1010, 
   weight(2)|abundance(10)|difficulty(14)|head_armor(0)|body_armor(14)|leg_armor(0), 
   imodbits_armor], 


#######UNDEAD HAND#########
["victim_hand", "Victim Hand", #受难者手
   [("z_handL", 0)], 
   itp_type_hand_armor, 0, 1, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(1)|leg_armor(0), 
   imodbits_none], 
["kulou_shou", "kulou_shou", [("barf_skeleton_handL", 0)], itp_type_hand_armor, 0, 1, weight(0.500000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(0), imodbits_cloth], 

["skeleton_unburned_hand", "skeleton_unburned_hand", [("barf_skeleton_unburned_handL", 0)], itp_type_hand_armor, 0, 1, weight(0.500000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(0), imodbits_cloth], 
["skeleton_candle_hand", "skeleton_candle_hand", [("barf_skeleton_candle_handL", 0)], itp_type_hand_armor, 0, 1, weight(0.500000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(0), imodbits_cloth], 
["skeleton_blazing_thing_hand", "skeleton_blazing_thing_hand", [("barf_skeleton_blazing_thing_handL", 0)], itp_type_hand_armor, 0, 1, weight(0.500000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(0), imodbits_cloth], 

["ghost_lthr_glove", "Ghost Lthr Glove", [("ghost_lthr_glove_L", 0)], itp_type_hand_armor, 0, 30, weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(1)|leg_armor(0), imodbits_cloth], 
["ghost_mail_mitten", "Ghost Mail Mitten", [("ghost_mail_mitten_L", 0)], itp_type_hand_armor, 0, 70, weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(3)|leg_armor(0), imodbits_cloth], 
["ghost_gauntlet", "Ghost Gauntlet", [("ghost_gauntlet_a_L", 0)], itp_type_hand_armor, 0, 110, weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(5)|leg_armor(0), imodbits_cloth], 


#######BARBARIAN BRASSART#########
["manzu_shoutao", "manzu_shoutao", [("beargauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 550, weight(3.000000)|abundance(10)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_plate], 


#######DEMON BRASSART#########
["renmowushi_glove", "renmowushi_glove", [("knight_of_molag_bal_hand_L", 0)], itp_type_hand_armor, 0, 3400, weight(3.000000)|abundance(10)|difficulty(21)|head_armor(0)|body_armor(20)|leg_armor(0), imodbits_armor], 
["dark_oath_hand", "Dark Oath Hand", #黑誓臂铠
   [("Black_Knight-L", 0)], 
   itp_type_hand_armor, 0, 34000, 
   weight(3)|abundance(1)|difficulty(18)|head_armor(0)|body_armor(60)|leg_armor(0), 
   imodbits_armor], 

["lemure_hand", "Lemure Hand", #劣魔手
   [("krag_belakor_handL", 0)], 
   itp_type_hand_armor|itp_unique, 0, 0, 
   weight(0)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), 
   imodbits_none], 


#######COMMON BRASSART#########
#Common Glove
["dancer_hand", "Dancer Hand", #舞女手纱
   [("dancer_handL", 0)], 
   itp_type_hand_armor|itp_civilian, 0, 3, 
   weight(0.1)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["luzhi_shoutao", "luzhi_shoutao", [("st_leatherglove_L", 0)], itp_type_hand_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 80, weight(0.250000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(1)|leg_armor(0), imodbits_cloth], 
["nvshi_shoutao", "nvshi_shoutao", [("female_gloveL", 0)], itp_type_hand_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 80, weight(0.250000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(1)|leg_armor(0), imodbits_cloth], 
["nvshi_shoujia", "nvshi_shoujia", [("lithe_L", 0)], itp_type_hand_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 20, weight(0.500000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(2)|leg_armor(0), imodbits_cloth], 
["leather_gloves", "Leather_Gloves", [("leather_gloves_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 150, weight(0.250000)|abundance(120)|difficulty(0)|head_armor(0)|body_armor(2)|leg_armor(0), imodbits_cloth], 
["fenzhi_pishoutao", "fenzhi_pishoutao", [("tld_lthr_glove_L", 0)], itp_type_hand_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 100, weight(0.250000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(4)|leg_armor(0), imodbits_cloth], 
["luzhi_bikai", "luzhi_bikai", [("glovevambrace_set1_L", 0)], itp_type_hand_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 300, weight(1.000000)|abundance(20)|difficulty(7)|head_armor(0)|body_armor(5)|leg_armor(0), imodbits_cloth], 


#Common Brassart
["fenzhi_jiaqiangshoutao", "fenzhi_jiaqiangshoutao", [("tld_gauntlet_b_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 360, weight(0.250000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(6)|leg_armor(0), imodbits_cloth], 
["scale_gauntlets", "Scale_Gauntlets", [("scale_gauntlets_b_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 910, weight(0.750000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(7)|leg_armor(0), imodbits_armor], 
["fenzhi_huzhishoutao", "fenzhi_huzhishoutao", [("tld_gauntlet_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 460, weight(0.500000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(8)|leg_armor(0), imodbits_plate], 
["lamellar_gauntlets", "Lamellar_Gauntlets", [("scale_gauntlets_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 910, weight(0.750000)|abundance(100)|difficulty(9)|head_armor(0)|body_armor(8)|leg_armor(0), imodbits_armor], 
["mail_mittens", "Mail_Mittens", [("mail_mittens_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 550, weight(0.500000)|abundance(100)|difficulty(7)|head_armor(0)|body_armor(9)|leg_armor(0), imodbits_armor], 
["fenzhi_lianjiashoutao", "fenzhi_lianjiashoutao", [("tld_mail_mitten_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 560, weight(1.000000)|abundance(50)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_plate], 
["fenzhi_dingshishoutao", "fenzhi_dingshishoutao", [("wisby_gauntlets_black_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 700, weight(1.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_plate], 
["fenzhi_fulianshoutao", "fenzhi_fulianshoutao", [("mail_gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 770, weight(1.000000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(11)|leg_armor(0), imodbits_plate], 
["shnegtie_shoutao", "shnegtie_shoutao", [("swanhandL", 0)], itp_type_hand_armor|itp_merchandise, 0, 500, weight(1.000000)|abundance(40)|difficulty(12)|head_armor(0)|body_armor(11)|leg_armor(0), imodbits_plate], 
["fenzhi_fubanshoutao", "fenzhi_fubanshoutao", [("wisby_gauntlets_red_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 780, weight(1.250000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(12)|leg_armor(0), imodbits_plate], 
["gauntlets", "Gauntlets", [("gauntlets_L", 0), ("gauntlets_L", 134217728)], itp_type_hand_armor|itp_merchandise, 0, 1100, weight(1.000000)|abundance(100)|difficulty(10)|head_armor(0)|body_armor(12)|leg_armor(0), imodbits_armor], 

["yinse_bikai", "yinse_bikai", [("hourglass_gauntlets_white_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 700, weight(1.500000)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(14)|leg_armor(0), imodbits_plate], 
["qinse_banjiabikai", "qinse_banjiabikai", [("hm_glv_masU_L", 0)], itp_type_hand_armor, 0, 1500, weight(1.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(20)|leg_armor(0), imodbits_plate], 
["shengtie_banjiabikai", "shengtie_banjiabikai", [("hm_glv_masV_L", 0)], itp_type_hand_armor, 0, 800, weight(1.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(15)|leg_armor(0), imodbits_plate], 
["heijin_banjaibikai", "heijin_banjaibikai", [("hm_glv_masW_L", 0)], itp_type_hand_armor, 0, 1000, weight(1.500000)|abundance(5)|difficulty(18)|head_armor(0)|body_armor(18)|leg_armor(0), imodbits_plate], 
["duangang_banjiabikai", "duangang_banjiabikai", [("hm_glv_masX_L", 0)], itp_type_hand_armor, 0, 2000, weight(1.500000)|abundance(5)|difficulty(21)|head_armor(0)|body_armor(21)|leg_armor(0), imodbits_plate], 
["kongju_bikai", "kongju_bikai", [("zuoshou1_L", 0)], itp_type_hand_armor, 0, 800, weight(2.500000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(18)|leg_armor(0), imodbits_plate], 
["heiguang_bikai", "heiguang_bikai", [("twilight_gloves_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 900, weight(1.500000)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(17)|leg_armor(0), imodbits_plate], 
["fangxing_bikai", "fangxing_bikai", [("steel_gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 900, weight(1.500000)|abundance(20)|difficulty(0)|head_armor(0)|body_armor(17)|leg_armor(0), imodbits_plate], 
["yuanzhi_bikai", "yuanzhi_bikai", [("steel_mittens_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 800, weight(1.500000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(16)|leg_armor(0), imodbits_plate], 
["mogang_fangxing_bikai", "mogang_fangxing_bikai", [("black_steel_gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 900, weight(1.500000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(17)|leg_armor(0), imodbits_plate], 
["mogang_yuanzhi_bikai", "mogang_yuanzhi_bikai", [("black_steel_mittens_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 800, weight(1.500000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(16)|leg_armor(0), imodbits_plate], 
["shepi_shoutao", "shepi_shoutao", [("kote_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 450, weight(0.250000)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(8)|leg_armor(0), imodbits_cloth], 
["suozi_bikai", "suozi_bikai", [("kote_arms_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 560, weight(0.750000)|abundance(30)|difficulty(0)|head_armor(0)|body_armor(11)|leg_armor(0), imodbits_plate], 
["duangang_shalouhushou", "duangang_shalouhushou", [("hourglass_gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 906, weight(1.750000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(18)|leg_armor(0), imodbits_plate], 
["mogang_shalouhushou", "mogang_shalouhushou", [("hourglass_gauntlets_black_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 906, weight(1.750000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(18)|leg_armor(0), imodbits_plate], 
["huali_shalouhushou", "huali_shalouhushou", [("hourglass_gauntlets_ornate_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 906, weight(1.750000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(18)|leg_armor(0), imodbits_plate], 
["heibai_banjia_bikai", "heibai_banjia_bikai", [("bnw_gauntlet_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 800, weight(1.000000)|abundance(10)|difficulty(22)|head_armor(0)|body_armor(16)|leg_armor(0), imodbits_plate], 
["gouwen_tieshoutao", "gouwen_tieshoutao", [("amade_steel_gauntlet_L", 0)], itp_type_hand_armor|itp_merchandise, 0, 743, weight(1.000000)|abundance(20)|difficulty(12)|head_armor(0)|body_armor(14)|leg_armor(0), imodbits_plate], 




#POLEARM
#_______________________________________________________________________________________________________________________________________________________________________________
#Spears can only be used to thrust, while halberds are usually used to swing. Lances are a cavalry weapon.
 ["polearm_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######POWELL POLEARM#########
#Powell Sorcery-spears
["sorcery_lance", "Sorcery Lance", [("MAO", 0)], itp_type_polearm|itp_two_handed|itp_primary|itp_couchable, itc_shieldless_slashable_spear|itcf_carry_spear, 1700, weight(5.250000)|abundance(80)|difficulty(14)|weapon_length(181)|spd_rtng(90)|swing_damage(35, cut)|thrust_damage(27, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["dragon_blood_sorcery_lance", "Dragon Blood Sorcery Lance", [("ylyq_zaoyun_qiang", 0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_couchable, itc_shieldlimit_slashable_spear|itcf_carry_spear, 5400, weight(6.000000)|abundance(100)|difficulty(14)|weapon_length(203)|spd_rtng(95)|swing_damage(50, cut)|thrust_damage(40, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["bec_de_corbin_a", "War_Hammer", [("bec_de_corbin_a", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_mountless_halberd|itcf_carry_spear, 425, weight(8.000000)|abundance(100)|difficulty(15)|weapon_length(120)|spd_rtng(81)|swing_damage(38, pierce)|thrust_damage(30, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#Powell Knight Lances
["gangying_qishiqiang", "gangying_qishiqiang", [("w_emberlance", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 1891, weight(7.500000)|abundance(10)|difficulty(16)|weapon_length(230)|spd_rtng(100)|swing_damage(0, blunt)|thrust_damage(34, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["shield_handed_knight_lance", "Shield Handed Knight Lance", #护手盾骑士枪
   [("KTS444FS", 0)], 
   itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_couchable, 
   itc_parryable_greatlance|itcf_carry_spear, 2211, 
   weight(10.000000)|abundance(5)|difficulty(15)|weapon_length(384)|spd_rtng(90)|swing_damage(0, blunt)|thrust_damage(35, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["nameless_goddess_silverwing_lance", "Nameless Goddess Silverwing Lance", #无名天使肖像枪
   [("chuncqiang", 0)], 
   itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_couchable, 
   itc_parryable_greatlance|itcf_carry_spear, 4491, 
   weight(8.25)|abundance(1)|difficulty(14)|weapon_length(327)|spd_rtng(90)|swing_damage(0, blunt)|thrust_damage(35, pierce), 
   imodbits_polearm, [
    (ti_on_weapon_attack, [
        (store_trigger_param_1, ":agent_no"),
        (store_random_in_range, ":count_no", 0, 5),#五分之一概率
        (eq, ":count_no", 3),
        (store_agent_hit_points, ":hit_point", ":agent_no", 1),
        (val_add, ":hit_point", 1),
        (agent_set_hit_points, ":agent_no", ":hit_point",1),
    ]),
    weapon_visual_effect_trigger,
   ]], 
["harvest_goddess_portrait_lance", "Harvest Goddess Portrait Lance", #丰收女神肖像枪
   [("KTS1234q", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable|itp_unique, 
   itc_parryable_greatlance|itcf_carry_spear, 5101, 
   weight(8.25)|abundance(1)|difficulty(14)|weapon_length(327)|spd_rtng(90)|swing_damage(0, blunt)|thrust_damage(36, pierce), 
   imodbits_polearm, [
    (ti_on_weapon_attack, [
        (store_trigger_param_1, ":agent_no"),
        (store_agent_hit_points, ":hit_point", ":agent_no", 1),
        (val_add, ":hit_point", 1),
        (agent_set_hit_points, ":agent_no", ":hit_point",1),
    ]),
    weapon_visual_effect_trigger,
   ]], 

#Powell Orthodox Weapons
["noble_ornamentation_lance", "Noble Ornamentation Lance", #贵胄浮饰枪
   [("gaoduanq", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable, 
   itc_parryable_greatlance|itcf_carry_spear, 2691, 
   weight(7.250000)|abundance(10)|difficulty(15)|weapon_length(255)|spd_rtng(90)|swing_damage(0, blunt)|thrust_damage(35, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["sickle_of_eliminater", "Sickle of Eliminater", #肃正之镰
   [("eliminater", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_couchable|itp_crush_through|itp_can_knock_down|itp_extra_penetration, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 15000, 
   weight(8.50)|abundance(1)|difficulty(24)|weapon_length(245)|spd_rtng(94)|swing_damage(46, pierce)|thrust_damage(30, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 


#######YISHITH POLEARM#########
#Yishith Human Spears
["jianyi_yejianqiang", "jianyi_yejianqiang", [("ashwood_pike_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 879, weight(6.250000)|abundance(30)|difficulty(10)|weapon_length(165)|spd_rtng(80)|swing_damage(28, cut)|thrust_damage(25, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["yejian_qiang", "yejian_qiang", [("rohanspear", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 934, weight(7.000000)|abundance(30)|difficulty(12)|weapon_length(230)|spd_rtng(81)|swing_damage(30, cut)|thrust_damage(26, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#Elf Spears
["elf_halberd", "Elf Halberd", #精灵枪刃
   [("silvan_spear", 0)], 
   itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_currency_slashable_spear|itcf_carry_spear, 3155, 
   weight(2.500000)|abundance(25)|difficulty(9)|weapon_length(245)|spd_rtng(110)|swing_damage(37, cut)|thrust_damage(30, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["spirit_tree_halberd", "Spirit Tree Halberd", #灵树枪刃
   [("6cfelves_lance", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_couchable, 
   itc_currency_slashable_spear|itcf_carry_spear, 7155, 
   weight(3.5)|abundance(8)|difficulty(12)|weapon_length(225)|spd_rtng(106)|swing_damage(40, pierce)|thrust_damage(34, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

#Rebel Elf Spears
["frigid_spear", "Frigid Spear", #苦寒枪
   [("WAoRStaffB", 0)], 
   itp_type_polearm|itp_primary|itp_offset_lance|itp_couchable, 
   itc_currency_slashable_spear|itcf_carry_spear, 3778, 
   weight(4.000000)|abundance(20)|difficulty(12)|weapon_length(201)|spd_rtng(83)|swing_damage(32, cut)|thrust_damage(34, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 


#######STEPPE POLEARM#########
["nanfang_jichangmao", "nanfang_jichangmao", [("spear_e_3-25m", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_offset_lance, itc_pike|itcf_carry_spear, 885, weight(7.000000)|abundance(30)|difficulty(12)|weapon_length(228)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]],


#######CONFEDERATION POLEARM#########
#鱼人
["trident_spear", "Trident Spear", #三尖叉
   [("trident", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 75, 
   weight(4)|abundance(40)|difficulty(0)|weapon_length(154)|spd_rtng(84)|swing_damage(17, cut)|thrust_damage(23, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["bend_blade_trident", "Bend Blade Trident", #弯刃三叉戟
   [("changgan09", 0)], 
   itp_type_polearm|itp_merchandise|itp_primary|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 650, 
   weight(6)|abundance(30)|difficulty(8)|weapon_length(211)|spd_rtng(86)|swing_damage(28, cut)|thrust_damage(30, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["straight_blade_trident", "Straight Blade Trident", #直刃三叉戟
   [("changgan08", 0)], 
   itp_type_polearm|itp_merchandise|itp_primary|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 660, 
   weight(6)|abundance(30)|difficulty(8)|weapon_length(211)|spd_rtng(86)|swing_damage(26, cut)|thrust_damage(31, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["tide_ceremonial_spear", "Tide Ceremonial Spear", #潮汐仪式矛
   [("chazi", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 9000, 
   weight(7.5)|abundance(1)|difficulty(16)|weapon_length(173)|spd_rtng(89)|swing_damage(386, cut)|thrust_damage(40, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

["fake_halberd", "Fake Halberd", #纸壳斧枪
   [("ji", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_no_parry, 
   itc_mountless_halberd|itcf_carry_spear, 14, 
   weight(3.5)|abundance(1)|difficulty(0)|weapon_length(250)|spd_rtng(36)|swing_damage(1, blunt)|thrust_damage(1, blunt), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["divinecusp_spear", "Divinecusp Spear", #神牙枪
   [("QJQ", 0)], 
   itp_type_polearm|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_extra_penetration|itp_offset_lance, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 3250, 
   weight(8)|abundance(10)|difficulty(18)|weapon_length(300)|spd_rtng(86)|swing_damage(40, pierce)|thrust_damage(41, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["phoenix_wand_lance", "Phoenix Wand Lance", #不死鸟权杖枪
   [("WAoRStaffD", 0)], 
   itp_type_polearm|itp_unique|itp_primary|itp_bonus_against_shield, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 15000, 
   weight(7.25)|abundance(1)|difficulty(18)|weapon_length(202)|spd_rtng(78)|swing_damage(50, cut)|thrust_damage(40, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["aquila_wand_lance", "Aquila Wand Lance", #天鹰权杖枪
   [("eagle_guard_spear", 0)], 
   itp_type_polearm|itp_unique|itp_primary|itp_bonus_against_shield, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 15000, 
   weight(7.5)|abundance(1)|difficulty(17)|weapon_length(148)|spd_rtng(83)|swing_damage(51, pierce)|thrust_damage(42, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 


#######PAPAL POLEARM#########
#Soldier Spear
["jianyi_jiantiqiang", "jianyi_jiantiqiang", [("bamboo_lance", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itc_shieldlimit_slashable_spear|itcf_carry_spear, 695, weight(6.250000)|abundance(40)|difficulty(11)|weapon_length(166)|spd_rtng(86)|swing_damage(31, cut)|thrust_damage(25, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["jiantou_qiang1", "jiantou_qiang1", [("tonbogiri", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_covers_head, itc_shieldlimit_slashable_spear|itcf_carry_spear, 855, weight(6.250000)|abundance(50)|difficulty(12)|weapon_length(185)|spd_rtng(80)|swing_damage(32, cut)|thrust_damage(26, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["buqiang_jiantiqiang", "buqiang_jiantiqiang", [("yari_spear_crimson", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield, itc_mounted_slashable_spear|itcf_carry_spear, 925, weight(7.000000)|abundance(40)|difficulty(15)|weapon_length(204)|spd_rtng(87)|swing_damage(34, cut)|thrust_damage(27, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#High Knight Polearm
["jiaoguo_hong_qizhiqiang", "jiaoguo_hong_qizhiqiang", [("banner_lance", 0)], itp_type_polearm|itp_merchandise|itp_no_parry|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 910, weight(7.250000)|abundance(40)|difficulty(10)|weapon_length(245)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(32, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["jiaoguo_hei_qizhiqiang", "jiaoguo_hei_qizhiqiang", [("black_lance", 0)], itp_type_polearm|itp_merchandise|itp_no_parry|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 910, weight(7.250000)|abundance(40)|difficulty(10)|weapon_length(245)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(32, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["asterisk_staff", "Asterisk Staff", #星字杖
   [("jumonji_yari_l", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable|itp_can_knock_down|itp_extra_penetration|itp_ignore_gravity, 
   itc_currency_slashable_spear|itcf_carry_spear, 5000, 
   weight(7)|abundance(10)|difficulty(15)|weapon_length(217)|spd_rtng(108)|swing_damage(48, pierce)|thrust_damage(36, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["steel_asterisk_staff", "Steel Asterisk Staff", #锻钢星字杖
   [("sjj", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable|itp_can_knock_down|itp_extra_penetration|itp_ignore_gravity, 
   itc_currency_slashable_spear|itcf_carry_spear, 9500, 
   weight(8)|abundance(1)|difficulty(18)|weapon_length(179)|spd_rtng(108)|swing_damage(49, pierce)|thrust_damage(36, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

["shouhuzhe_changqiang", "shouhuzhe_changqiang", [("spear_a_4m", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, itc_greatlance|itcf_carry_spear, 1925, weight(8.700000)|abundance(10)|difficulty(10)|weapon_length(407)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(36, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["shouhuzhe_chaochangqiang", "shouhuzhe_chaochangqiang", [("asd4", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, itc_greatlance|itcf_carry_spear, 2325, weight(9.000000)|abundance(10)|difficulty(14)|weapon_length(503)|spd_rtng(61)|swing_damage(0, blunt)|thrust_damage(35, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#Papal Special Polearm
["zhujian_xinzhang", "zhujian_xinzhang", [("bishop_staff", 0)], itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_couchable, itc_currency_slashable_spear|itcf_carry_spear, 8500, weight(5.000000)|abundance(1)|difficulty(12)|weapon_length(118)|spd_rtng(80)|swing_damage(32, blunt)|thrust_damage(24, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 
["zhujaio_quanzhang", "zhujaio_quanzhang", [("shepard_crook", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_currency_slashable_spear|itcf_carry_spear, 9000, weight(6.000000)|abundance(1)|difficulty(12)|weapon_length(165)|spd_rtng(83)|swing_damage(33, blunt)|thrust_damage(33, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["jiaohuang_quanzhang", "jiaohuang_quanzhang", [("cleric_staff", 0)], itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced, itc_currency_slashable_spear|itcf_carry_spear, 30000, weight(7.750000)|abundance(1)|difficulty(14)|weapon_length(163)|spd_rtng(84)|swing_damage(37, blunt)|thrust_damage(25, blunt), imodbits_none, [weapon_visual_effect_trigger]], 
["holy_selected_lance", "Holy Selected Lance", #圣选枪
   [("xuexiaoqiqiang", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable|itp_unique, 
   itc_parryable_greatlance|itcf_carry_spear, 15101, 
   weight(9.5)|abundance(1)|difficulty(17)|weapon_length(227)|spd_rtng(87)|swing_damage(0, blunt)|thrust_damage(45, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["holy_selected_great_lance", "Holy Selected Great Lance", #圣选超长枪
   [("lanse1q", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable|itp_unique, 
   itc_parryable_greatlance|itcf_carry_spear, 16101, 
   weight(11)|abundance(1)|difficulty(18)|weapon_length(427)|spd_rtng(87)|swing_damage(0, blunt)|thrust_damage(42, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

#Papal Transcendent Poleam
["holy_spear_of_hunting", "Holy Spear of Hunting", 
   [("lielongqiang", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_unique, 
   itc_currency_slashable_spear|itcf_carry_spear, 100000, 
   weight(8)|abundance(100)|difficulty(0)|weapon_length(263)|spd_rtng(95)|swing_damage(50, blunt)|thrust_damage(53, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 


#######EASTERN POLEARM#########
["bamboo_spear", "Bamboo_Spear", #竹矛
   [("arabian_spear_a_3m", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 80, 
   weight(5.75)|abundance(100)|difficulty(0)|weapon_length(200)|spd_rtng(88)|swing_damage(15, blunt)|thrust_damage(20, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["jingzhi_zhumao", "jingzhi_zhumao", [("bamboo_spear_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear|itcf_carry_spear, 385, weight(6.000000)|abundance(100)|difficulty(12)|weapon_length(200)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["ji", "ji", [("DaMing_ji", 0)], itp_type_polearm|itp_merchandise|itp_primary|itp_offset_lance|itp_couchable|itp_crush_through, itc_mounted_slashable_spear|itcf_carry_spear, 1860, weight(8.000000)|abundance(100)|difficulty(17)|weapon_length(230)|spd_rtng(100)|swing_damage(54, cut)|thrust_damage(37, pierce), imodbits_polearm, [weapon_visual_effect_trigger]],
["dongfang_yinqiang", "dongfang_yinqiang", [("ylyq_zaoyun_qiang1", 0)], itp_type_polearm|itp_merchandise|itp_primary|itp_couchable|itp_offset_lance, itc_mounted_slashable_spear|itcf_carry_spear, 3548, weight(6.500000)|abundance(1)|difficulty(15)|weapon_length(98)|spd_rtng(90)|swing_damage(38, cut)|thrust_damage(37, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["dongfang_longyaqiang", "dongfang_longyaqiang", [("dragonspear", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 1900, weight(7.500000)|abundance(20)|difficulty(18)|weapon_length(277)|spd_rtng(72)|swing_damage(0, blunt)|thrust_damage(38, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["snake_spear", "Snake Spear", #蛇矛
   [("changgan05", 0)], 
    itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_penalty_with_shield, 
   itc_mounted_slashable_spear|itcf_carry_spear, 580, 
   weight(5.75)|abundance(100)|difficulty(10)|weapon_length(235)|spd_rtng(93)|swing_damage(35, cut)|thrust_damage(34, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["hafted_blade_b", "Hafted_Blade", [("khergit_pike_b", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_mounted_slashable_spear|itcf_carry_spear, 582, weight(7.250000)|abundance(100)|difficulty(9)|weapon_length(135)|spd_rtng(95)|swing_damage(37, cut)|thrust_damage(21, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["yanyue_dao", "yanyue_dao", [("naginata", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary, itc_mounted_slashable_spear|itcf_carry_spear, 841, weight(7.750000)|abundance(20)|difficulty(15)|weapon_length(197)|spd_rtng(88)|swing_damage(38, cut)|thrust_damage(23, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######STARKHOOK POLEARM#########
["mangler_halberd", "Mangler Halberd", #厉海斧枪
   [("ji", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, 
   itc_mountless_halberd|itcf_carry_spear, 4474, 
   weight(7.500000)|abundance(10)|difficulty(18)|weapon_length(250)|spd_rtng(86)|swing_damage(47, cut)|thrust_damage(30, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["heroic_halberd", "Heroic Halberd", #盛勇斧枪
   [("FB_halberd", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_unbalanced, 
   itc_mountless_halberd|itcf_carry_spear, 6174, 
   weight(9.5)|abundance(1)|difficulty(25)|weapon_length(248)|spd_rtng(82)|swing_damage(50, cut)|thrust_damage(33, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 
["heroic_halberd_alt", "Heroic Halberd", #盛勇斧枪
   [("FB_halberd", 0)], 
   itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, 
   itc_mountless_halberd|itcf_carry_spear, 6174, 
   weight(9.5)|abundance(1)|difficulty(25)|weapon_length(248)|spd_rtng(82)|swing_damage(50, cut)|thrust_damage(33, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 

["blood_short_spear", "Blood Short Spear", #铩血短矛
   [("new_xueqiang", 0)], 
   itp_type_polearm|itp_unique|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_couchable, 
   itc_mounted_slashable_spear|itcf_carry_spear, 10000, 
   weight(5.25)|abundance(1)|difficulty(18)|weapon_length(155)|spd_rtng(95)|swing_damage(40, cut)|thrust_damage(39, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["scarlet_heavy_lance", "Scarlet Heavy Lance", #猩红重骑枪
   [("pol_gusar_lansa_c", 0)], 
   itp_type_polearm|itp_primary|itp_no_parry|itp_bonus_against_shield|itp_couchable, 
   itc_greatlance|itcf_carry_spear, 13840, 
   weight(7)|abundance(1)|difficulty(16)|weapon_length(276)|spd_rtng(84)|swing_damage(0, blunt)|thrust_damage(37, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

#绯世
["blood_thorn", "Blood thorn", #血荆条
   [("crimson_spear", 0)], 
   itp_type_polearm|itp_unique|itp_primary, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 3776, 
   weight(1.5)|abundance(1)|difficulty(0)|weapon_length(163)|spd_rtng(100)|swing_damage(33, pierce)|thrust_damage(35, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 
["blood_snatcher", "Blood Snatcher", #夺血者
   [("crimson_sgzl", 0)], 
   itp_type_polearm|itp_unique|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, 
   itc_parry_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear, 11370, 
   weight(3.5)|abundance(1)|difficulty(0)|weapon_length(218)|spd_rtng(82)|swing_damage(43, pierce)|thrust_damage(0, pierce), 
   imodbits_none, [weapon_visual_effect_trigger]], 


#######STATE POLEARM#########
["dismounted_knight_halberd", "Dismounted Knight Halberd", #下马骑士斧枪
   [("scepter_halberd", 0)], 
   itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, 
   itc_mountless_halberd|itcf_carry_spear, 4040, 
   weight(6.5)|abundance(10)|difficulty(18)|weapon_length(137)|spd_rtng(94)|swing_damage(44, cut)|thrust_damage(32, pierce), 
   imodbits_sword_high, [weapon_visual_effect_trigger]], 


#######UNDEAD POLEARM#########
["skull_staff", "skull Staff", [("skull_staff", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_mounted_slashable_spear|itcf_carry_spear, 2058, weight(7.500000)|abundance(5)|difficulty(14)|weapon_length(155)|spd_rtng(70)|swing_damage(33, blunt)|thrust_damage(26, blunt), imodbits_polearm, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_set_animation, ":attacker_agent_no", "anim_active_enchant_5", 1),

        (set_fixed_point_multiplier, 100),
        (agent_get_position, pos1, ":attacker_agent_no"),
        (position_move_y, pos1, 150),#身前1.5米
        (set_spawn_position, pos1),
        (spawn_item, "itm_skeleton_spear_anim", 0, 2),
        (assign, ":cur_instance", reg0),
        (scene_prop_set_slot, ":cur_instance", slot_instance_agent_used, ":attacker_agent_no"),
        (scene_prop_set_slot, ":cur_instance", slot_instance_item, "itm_skeleton_spear_anim"),
        (prop_instance_deform_in_range, ":cur_instance", 0, 600, 2300),
        (call_script, "script_mission_create_timer", -1, ":cur_instance", 180, 1),#计时器
    ]),
]], 
["bone_thruncheon", "Bone Thruncheon", [("dragonbonestaff", 0)], itp_type_polearm|itp_two_handed|itp_primary|itp_offset_lance, itc_mounted_slashable_spear|itcf_carry_spear, 6058, weight(4.500000)|abundance(5)|difficulty(12)|weapon_length(145)|spd_rtng(94)|swing_damage(38, cut)|thrust_damage(0, pierce), imodbits_polearm, [
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (agent_set_animation, ":attacker_agent_no", "anim_active_enchant_5", 1),

        (set_fixed_point_multiplier, 100),
        (agent_get_position, pos1, ":attacker_agent_no"),
        (position_move_y, pos1, 150),#身前1.5米
        (position_move_x, pos1, -50),
        (try_for_range, reg1, 0, 3),
           (set_spawn_position, pos1),
           (spawn_item, "itm_skeleton_spear_anim", 0, 2),
           (assign, ":cur_instance", reg0),
           (scene_prop_set_slot, ":cur_instance", slot_instance_agent_used, ":attacker_agent_no"),
           (scene_prop_set_slot, ":cur_instance", slot_instance_item, "itm_skeleton_spear_anim"),
           (prop_instance_deform_in_range, ":cur_instance", 0, 600, 2300),
           (call_script, "script_mission_create_timer", -1, ":cur_instance", 180, 1),#计时器
           (position_move_x, pos1, 50),
        (try_end),
    ]),
]], 

["powell_burial_spear", "Powell Burial Spear", [("Fa_spear", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_offset_lance|itp_couchable, itc_greatlance|itcf_carry_spear, 1008, weight(7.500000)|abundance(30)|difficulty(14)|weapon_length(237)|spd_rtng(80)|swing_damage(0, cut)|thrust_damage(36, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["bone_scythe", "Bone Scythe", [("dragonbonescythe", 0)], itp_type_polearm|itp_unique|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_couchable|itp_crush_through|itp_can_knock_down, itc_shieldless_slashable_spear|itcf_carry_sword_back, 3000, weight(7.250000)|abundance(1)|difficulty(19)|weapon_length(179)|spd_rtng(77)|swing_damage(37, pierce)|thrust_damage(32, pierce), imodbits_none, [weapon_visual_effect_trigger]], 

#Ghost Weapon
["ghost_battle_fork", "Ghost Battle Fork", [("ghost_battle_fork", 0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 182, weight(0)|abundance(1)|difficulty(0)|weapon_length(140)|spd_rtng(98)|swing_damage(19, blunt)|thrust_damage(30, pierce), imodbits_polearm, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger]], 
["duagang_liandao", "duagang_liandao", [("dk_steel", 0)], itp_type_polearm|itp_unique|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_couchable|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_shieldless_slashable_spear|itcf_carry_spear, 11000, weight(0)|abundance(1)|difficulty(15)|weapon_length(241)|spd_rtng(130)|swing_damage(40, pierce)|thrust_damage(30, pierce), imodbits_polearm, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger]], 
["death_omen", "Death Omen", [("dk_ebony", 0)], itp_type_polearm|itp_unique|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_couchable|itp_crush_through|itp_no_pick_up_from_ground|itp_can_knock_down|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction, itc_shieldless_slashable_spear|itcf_carry_spear, 15000, weight(0)|abundance(1)|difficulty(15)|weapon_length(245)|spd_rtng(130)|swing_damage(40, pierce)|thrust_damage(30, pierce), imodbits_none, [
    ghost_weapon_trigger,
    weapon_visual_effect_trigger,
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_spectre_burst"),#灵爆
    ]),
]], 


#######DEMON POLEARM#########
["long_cruel_morningstar_hammer", "Long Cruel Morningstar Hammer", #长柄残虐者钉锤
   [("AN_mace02b_long", 0)], 
   itp_type_polearm|itp_primary|itp_can_knock_down|itp_bonus_against_shield, 
   itc_currency_slashable_spear|itcf_carry_spear, 1910, 
   weight(6.75)|abundance(5)|difficulty(14)|weapon_length(190)|spd_rtng(74)|swing_damage(37, pierce)|thrust_damage(30, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["demon_knight_lance", "Demon Knight Lance", #魔骑士枪
   [("lance22_b", 0)], 
   itp_type_polearm|itp_no_parry|itp_primary|itp_couchable, 
   itc_greatlance|itcf_carry_spear, 8000, 
   weight(7)|abundance(1)|difficulty(21)|weapon_length(227)|spd_rtng(85)|swing_damage(0, blunt)|thrust_damage(44, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 


#######SABIANISM POLEARM#########
["xinhua_qiqiang", "xinhua_qiqiang", [("Annu_spear", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_couchable,  itc_greatlance|itcf_carry_spear, 1300, weight(7.000000)|abundance(10)|difficulty(15)|weapon_length(320)|spd_rtng(79)|swing_damage(0, blunt)|thrust_damage(30, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["xinyue_qiqiang", "xinyue_qiqiang", [("we_sar_spear_pike", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_couchable,  itc_greatlance|itcf_carry_spear, 4400, weight(7.500000)|abundance(20)|difficulty(18)|weapon_length(355)|spd_rtng(74)|swing_damage(0, blunt)|thrust_damage(35, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######WITCHCRAFT POLEARM#########
["kaitang_qiang", "kaitang_qiang", [("melitine_lance3", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, itc_pike|itcf_carry_spear, 1008, weight(7.000000)|abundance(30)|difficulty(0)|weapon_length(200)|spd_rtng(80)|swing_damage(0, cut)|thrust_damage(34, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["changliu_duanqiang", "changliu_duanqiang", [("melitine_short_spear3", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary, itc_shieldlimit_slashable_spear|itcf_carry_spear, 980, weight(6.250000)|abundance(30)|difficulty(11)|weapon_length(150)|spd_rtng(90)|swing_damage(22, cut)|thrust_damage(32, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["podu_qiang", "podu_qiang", [("melitine_lance2", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield, itc_pike|itcf_carry_spear, 985, weight(8.000000)|abundance(30)|difficulty(12)|weapon_length(210)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(33, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["scorpion_stinger", "Scorpion Stinger", [("gaoduan1q", 0)], itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_couchable|itp_unique, itc_spear|itcf_carry_spear, 6300, weight(7.750000)|abundance(1)|difficulty(21)|weapon_length(260)|spd_rtng(70)|swing_damage(0, blunt)|thrust_damage(33, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######ECLIPSE POLEARM#########
["copper_spear", "Copper Spear", [("spear1", 0)], itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_offset_lance, itc_spear|itcf_carry_spear, 600, weight(8.000000)|abundance(20)|difficulty(15)|weapon_length(167)|spd_rtng(70)|swing_damage(0, blunt)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["febrilagma_diffusion_lance", "Febrilagma Diffusion Lance", [("lance22_a", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_bonus_against_shield|itp_couchable|itp_unique, itc_greatlance|itcf_carry_spear, 100000, weight(12.500000)|abundance(10)|difficulty(0)|weapon_length(270)|spd_rtng(100)|swing_damage(0, blunt)|thrust_damage(34, pierce), imodbits_none, [weapon_visual_effect_trigger]], 


#######MAMMONIST POLEARM#########
["mojin_quanzhangqiang", "mojin_quanzhangqiang", [("WAoRStaffF", 0)], itp_type_polearm|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_couchable|itp_crush_through|itp_can_knock_down, itc_mounted_slashable_spear|itcf_carry_spear, 17000, weight(8.000000)|abundance(1)|difficulty(21)|weapon_length(192)|spd_rtng(87)|swing_damage(40, cut)|thrust_damage(42, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######BARBARIAN POLEARM#########
["manzu_shiqiang", "manzu_shiqiang", [("h_spear", 0)], itp_type_polearm|itp_no_parry|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_couchable|itp_unbalanced, itc_pike|itcf_carry_spear, 386, weight(7.750000)|abundance(30)|difficulty(12)|weapon_length(132)|spd_rtng(70)|swing_damage(0, cut)|thrust_damage(27, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 
["shashi_mao", "shashi_mao", [("mackie_tepoztopilli", 0)], itp_type_polearm|itp_two_handed|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_couchable|itp_unbalanced, itc_shieldless_slashable_spear|itcf_carry_spear, 1055, weight(8.500000)|abundance(20)|difficulty(14)|weapon_length(158)|spd_rtng(72)|swing_damage(27, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######ANCIENT WORRIER POLEARM#########
["halberd_for_the_end_of_glory", "Halberd for the End of Glory", [("heiqishiji", 0)], itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_currency_slashable_spear|itcf_carry_spear, 7085, weight(7.750000)|abundance(1)|difficulty(25)|weapon_length(269)|spd_rtng(80)|swing_damage(43, cut)|thrust_damage(34, pierce), imodbits_polearm, [weapon_visual_effect_trigger]],


#######SILVERING POLEARM#########
#Cant use on horseback
["duyin_duangzhandouqiang", "duyin_duangzhandouqiang", [("war_spear_h4", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike|itcf_carry_spear, 816, weight(6.000000)|abundance(20)|difficulty(12)|weapon_length(150)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(35, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["duyin_zhandouqiang", "duyin_zhandouqiang", [("pike_h4", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike|itcf_carry_spear, 1185, weight(7.500000)|abundance(20)|difficulty(14)|weapon_length(302)|spd_rtng(78)|swing_damage(0, blunt)|thrust_damage(34, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#lance
["duying_hushouqiang", "duying_hushouqiang", [("awlpike_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_couchable, itc_spear|itcf_carry_spear, 1054, weight(6.250000)|abundance(30)|difficulty(11)|weapon_length(168)|spd_rtng(85)|swing_damage(0, blunt)|thrust_damage(33, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["duyin_shuangtouqiang", "duyin_shuangtouqiang", [("double_sided_lance_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_couchable, itc_mounted_slashable_spear|itcf_carry_spear, 774, weight(5.250000)|abundance(20)|difficulty(11)|weapon_length(126)|spd_rtng(80)|swing_damage(25, cut)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["duyin_zhandoucha", "duyin_zhandoucha", [("battle_fork_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 719, weight(5.750000)|abundance(20)|difficulty(9)|weapon_length(140)|spd_rtng(83)|swing_damage(18, blunt)|thrust_damage(24, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["duyin_duanqiang", "duyin_duanqiang", [("boar_spear_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary, itc_shieldlimit_slashable_spear|itcf_carry_spear, 770, weight(5.500000)|abundance(20)|difficulty(0)|weapon_length(143)|spd_rtng(87)|swing_damage(27, cut)|thrust_damage(24, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["duyin_fuheqiang", "duyin_fuheqiang", [("elegant_poleaxe_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itc_mountless_halberd|itcf_carry_spear, 885, weight(5.750000)|abundance(20)|difficulty(12)|weapon_length(134)|spd_rtng(82)|swing_damage(35, cut)|thrust_damage(26, pierce), imodbits_axe, [weapon_visual_effect_trigger]], 
["duyin_kuotouqiang", "duyin_kuotouqiang", [("english_bill_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itc_mountless_halberd|itcf_carry_spear, 825, weight(7.000000)|abundance(20)|difficulty(12)|weapon_length(180)|spd_rtng(83)|swing_damage(34, cut)|thrust_damage(26, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["duyin_goulianqiang", "duyin_goulianqiang", [("fauchard_h4", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_mountless_halberd|itcf_carry_spear, 743, weight(6.750000)|abundance(20)|difficulty(8)|weapon_length(142)|spd_rtng(79)|swing_damage(21, cut)|thrust_damage(18, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######FORGED STEEL WEAPON#########
["duangang_zhuixingqiang", "duangang_zhuixingqiang", [("gothic_lance", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 1800, weight(7.750000)|abundance(10)|difficulty(15)|weapon_length(235)|spd_rtng(85)|swing_damage(0, blunt)|thrust_damage(38, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 


#######GRAGHITE STEEL WEAPON#########
["mogang_qiang", "mogang_qiang", [("cross_spear", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 1385, weight(7.500000)|abundance(30)|difficulty(11)|weapon_length(215)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(33, pierce), imodbits_polearm, [weapon_visual_effect_trigger]],
["mogang_zhuixingqiang", "mogang_zhuixingqiang", [("we_swa_spear_lance_iron", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_couchable, itc_pike|itcf_carry_spear, 2300, weight(8.250000)|abundance(10)|difficulty(15)|weapon_length(315)|spd_rtng(93)|swing_damage(0, blunt)|thrust_damage(38, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["mogang_changzhuiqiang", "mogang_changzhuiqiang", [("roman_pilum_3", 0)], itp_type_polearm|itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_mountless_halberd|itcf_carry_spear, 1200, weight(7.250000)|abundance(20)|difficulty(15)|weapon_length(174)|spd_rtng(92)|swing_damage(20, blunt)|thrust_damage(38, pierce), imodbits_polearm, [weapon_visual_effect_trigger]],  


#######COMMON POLEARM#########
#Common Bayonet
["pitch_fork", "Pitch_Fork", [("pitch_fork", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 59, weight(5.000000)|abundance(100)|difficulty(0)|weapon_length(154)|spd_rtng(83)|swing_damage(16, blunt)|thrust_damage(22, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["military_fork", "Military_Fork", [("military_fork", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 153, weight(5.250000)|abundance(100)|difficulty(0)|weapon_length(132)|spd_rtng(90)|swing_damage(15, blunt)|thrust_damage(28, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["battle_fork", "Battle_Fork", [("battle_fork", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 282, weight(5.500000)|abundance(100)|difficulty(9)|weapon_length(140)|spd_rtng(90)|swing_damage(15, blunt)|thrust_damage(32, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["boar_spear", "Boar_Spear", [("spear", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield, itc_shieldlimit_slashable_spear|itcf_carry_spear, 76, weight(4.500000)|abundance(100)|difficulty(0)|weapon_length(157)|spd_rtng(90)|swing_damage(26, cut)|thrust_damage(23, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["kuotou_qiang", "kuotou_qiang", [("gallic_spear_2", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 700, weight(4.150000)|abundance(30)|difficulty(8)|weapon_length(127)|spd_rtng(90)|swing_damage(28, cut)|thrust_damage(27, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["jiachang_kuotou_qiang", "jiachang_kuotou_qiang", [("gallic_spear_2_uniq", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_offset_lance, itc_pike|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear, 831, weight(5.000000)|abundance(30)|difficulty(12)|weapon_length(203)|spd_rtng(84)|swing_damage(28, cut)|thrust_damage(26, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["citou_qiang", "citou_qiang", [("gallic_spear_1", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear|itcf_carry_spear, 731, weight(4.500000)|abundance(30)|difficulty(8)|weapon_length(129)|spd_rtng(89)|swing_damage(0, blunt)|thrust_damage(27, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["jiantou_qiang", "jiantou_qiang", [("gallic_spear_3", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear|itcf_carry_spear, 767, weight(4.750000)|abundance(30)|difficulty(10)|weapon_length(154)|spd_rtng(82)|swing_damage(0, blunt)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["lengtou_qiang", "lengtou_qiang", [("gallic_spear_4b", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear|itcf_carry_spear, 767, weight(4.900000)|abundance(30)|difficulty(10)|weapon_length(163)|spd_rtng(82)|swing_damage(0, blunt)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#Common Spears
["shortened_spear", "Shortened_Spear", [("spear_g_1-9m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 53, weight(4.250000)|abundance(100)|difficulty(0)|weapon_length(120)|spd_rtng(102)|swing_damage(19, blunt)|thrust_damage(25, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["spear", "Spear", [("spear_h_2-15m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 85, weight(4.500000)|abundance(100)|difficulty(0)|weapon_length(135)|spd_rtng(98)|swing_damage(9, blunt)|thrust_damage(26, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["war_spear", "War_Spear", [("spear_i_2-3m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 140, weight(4.600000)|abundance(100)|difficulty(0)|weapon_length(150)|spd_rtng(95)|swing_damage(12, blunt)|thrust_damage(27, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["ashwood_pike", "Ashwood_Pike", [("pike", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_shieldless_slashable_spear|itcf_carry_spear, 205, weight(4.750000)|abundance(100)|difficulty(9)|weapon_length(170)|spd_rtng(90)|swing_damage(14, blunt)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["pike", "Pike", [("spear_a_3m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_mountless_halberd|itcf_carry_spear, 227, weight(5.750000)|abundance(100)|difficulty(12)|weapon_length(245)|spd_rtng(81)|swing_damage(12, blunt)|thrust_damage(30, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["sanjian_qiang", "sanjian_qiang", [("yongquanspear", 0)], itp_type_polearm|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable,  itc_shieldlimit_slashable_spear|itcf_carry_spear, 1085, weight(7.000000)|abundance(30)|difficulty(12)|weapon_length(238)|spd_rtng(83)|swing_damage(29, cut)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["changren_qiang", "changren_qiang", [("bretonspear", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_couchable, itc_spear|itcf_carry_spear, 1002, weight(7.150000)|abundance(30)|difficulty(15)|weapon_length(231)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["awlpike", "Awlpike", [("awl_pike_b", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 277, weight(4.500000)|abundance(100)|difficulty(12)|weapon_length(165)|spd_rtng(95)|swing_damage(20, blunt)|thrust_damage(33, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["awlpike_long", "Long_Awlpike", [("awl_pike_a", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_shieldlimit_slashable_spear|itcf_carry_spear, 385, weight(4.750000)|abundance(100)|difficulty(18)|weapon_length(185)|spd_rtng(89)|swing_damage(17, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#Common Lance
["jousting_lance", "Jousting Lance", #练习骑枪
   [("joust_of_peace", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, 
   itc_spear|itcf_carry_spear, 377, 
   weight(6)|abundance(100)|difficulty(0)|weapon_length(225)|spd_rtng(61)|swing_damage(0, cut)|thrust_damage(22, blunt), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["double_sided_lance", "Double Sided Lance", #双头骑枪
   [("lance_dblhead", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance|itp_couchable, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 374, 
   weight(4.25)|abundance(100)|difficulty(0)|weapon_length(130)|spd_rtng(80)|swing_damage(25, cut)|thrust_damage(27, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["light_lance", "Light Lance", #轻骑枪
   [("spear_b_2-75m", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, 
   itc_spear|itcf_carry_spear, 180, 
   weight(4.5)|abundance(100)|difficulty(9)|weapon_length(175)|spd_rtng(90)|swing_damage(0, blunt)|thrust_damage(34, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["lance", "Lance", #骑枪
   [("spear_d_2-8m", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, 
   itc_spear|itcf_carry_spear, 270, 
   weight(4.5)|abundance(100)|difficulty(10)|weapon_length(180)|spd_rtng(80)|swing_damage(0, blunt)|thrust_damage(33, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["heavy_lance", "Heavy Lance", #重骑枪
   [("spear_f_2-9m", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, 
   itc_spear|itcf_carry_spear, 360, 
   weight(4.75)|abundance(100)|difficulty(11)|weapon_length(190)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["great_lance", "Great Lance", #巨型骑枪
   [("heavy_lance", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, 
   itc_spear|itcf_carry_spear, 410, 
   weight(6)|abundance(100)|difficulty(12)|weapon_length(240)|spd_rtng(75)|swing_damage(0, cut)|thrust_damage(28, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

["hongwen_qiqiang", "hongwen_qiqiang", [("lance_3", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 1567, weight(8.500000)|abundance(20)|difficulty(16)|weapon_length(351)|spd_rtng(72)|swing_damage(0, blunt)|thrust_damage(29, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["baiwen_qiqiang", "baiwen_qiqiang", [("lance_4", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 500, weight(7.500000)|abundance(30)|difficulty(15)|weapon_length(271)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["lanwen_qiqiang", "lanwen_qiqiang", [("lance_6", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 500, weight(7.500000)|abundance(30)|difficulty(15)|weapon_length(276)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["heibai_wenqiqiang", "heibai_wenqiqiang", [("we_swa_spear_lance_colouredbw", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 500, weight(7.500000)|abundance(30)|difficulty(15)|weapon_length(276)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["lvbai_wenqiqiang", "lvbai_wenqiqiang", [("we_swa_spear_lance_colouredby", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 500, weight(7.500000)|abundance(30)|difficulty(15)|weapon_length(276)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["honghei_wenqiqiang", "honghei_wenqiqiang", [("we_swa_spear_lance_colouredrb", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_couchable,itc_greatlance|itcf_carry_spear, 500, weight(7.500000)|abundance(30)|difficulty(15)|weapon_length(276)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["honghuang_wenqiqiang", "honghuang_wenqiqiang", [("we_swa_spear_lance_colouredry", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_couchable, itc_greatlance|itcf_carry_spear, 500, weight(7.500000)|abundance(30)|difficulty(15)|weapon_length(276)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(31, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

["ellite_lance", "Elite Lance", [("lrqq1", 0)], itp_type_polearm|itp_no_parry|itp_merchandise|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 1400, weight(8.000000)|abundance(30)|difficulty(18)|weapon_length(309)|spd_rtng(75)|swing_damage(0, blunt)|thrust_damage(35, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 
["knight_lance", "Knight Lance", [("lance22_c", 0)], itp_type_polearm|itp_no_parry|itp_primary|itp_couchable, itc_greatlance|itcf_carry_spear, 1900, weight(7.750000)|abundance(10)|difficulty(19)|weapon_length(225)|spd_rtng(78)|swing_damage(0, blunt)|thrust_damage(36, pierce), imodbits_polearm, [weapon_visual_effect_trigger]], 

#Long Hammers
["staff", "Staff", [("wooden_staff", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_staff|itcf_carry_spear, 36, weight(2.500000)|abundance(100)|difficulty(0)|weapon_length(130)|spd_rtng(90)|swing_damage(18, blunt)|thrust_damage(19, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 
["quarter_staff", "Quarter_Staff", [("quarter_staff", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 50, weight(3.000000)|abundance(100)|difficulty(0)|weapon_length(138)|spd_rtng(104)|swing_damage(20, blunt)|thrust_damage(20, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 
["iron_staff", "Iron_Staff", [("iron_staff", 0)], itp_type_polearm|itp_merchandise|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 101, weight(4.500000)|abundance(100)|difficulty(6)|weapon_length(128)|spd_rtng(97)|swing_damage(25, blunt)|thrust_damage(26, blunt), imodbits_polearm, [weapon_visual_effect_trigger]], 

["long_spiked_club", "Long_Spiked_Club", [("mace_long_c", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_currency_slashable_spear|itcf_carry_spear, 264, weight(3.500000)|abundance(100)|difficulty(9)|weapon_length(126)|spd_rtng(96)|swing_damage(25, pierce)|thrust_damage(22, blunt), imodbits_axe, [weapon_visual_effect_trigger]], 
["long_hafted_knobbed_mace", "Long_Hafted_Knobbed_Mace", [("mace_long_a", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_currency_slashable_spear|itcf_carry_spear, 324, weight(3.750000)|abundance(100)|difficulty(0)|weapon_length(133)|spd_rtng(95)|swing_damage(27, blunt)|thrust_damage(23, blunt), imodbits_axe, [weapon_visual_effect_trigger]], 
["long_hafted_spiked_mace", "Long Hafted Spiked Mace", #长柄尖头杖
   [("mace_long_b", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, 
   itc_currency_slashable_spear|itcf_carry_spear, 310, 
   weight(3.750000)|abundance(100)|difficulty(0)|weapon_length(140)|spd_rtng(94)|swing_damage(29, pierce)|thrust_damage(26, blunt), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["polehammer", "Polehammer", #长柄锤
   [("pole_hammer", 0)], 
   itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 403, 
   weight(7)|abundance(100)|difficulty(18)|weapon_length(126)|spd_rtng(64)|swing_damage(37, blunt)|thrust_damage(30, blunt), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

#Common Halberds
["scythe", "Scythe", #长柄镰刀
   [("scythe", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 43, 
   weight(2.75)|abundance(100)|difficulty(0)|weapon_length(182)|spd_rtng(79)|swing_damage(19, cut)|thrust_damage(14, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["long_pole_machete", "Long Pole Machete", #长杆砍刀
   [("glaive1", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 785, 
   weight(3.25)|abundance(30)|difficulty(10)|weapon_length(197)|spd_rtng(88)|swing_damage(25, cut)|thrust_damage(23, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["military_scythe", "Military_Scythe", #军用镰
   [("spear_e_2-5m", 0), ("spear_c_2-5m", 6291486)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 155, 
   weight(3.5)|abundance(100)|difficulty(0)|weapon_length(155)|spd_rtng(90)|swing_damage(31, cut)|thrust_damage(25, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["flat_head_axe", "Flat Head Axe", #扁头斧
   [("mackie_voulge", 0)], 
   itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 834, 
   weight(5.75)|abundance(70)|difficulty(15)|weapon_length(187)|spd_rtng(85)|swing_damage(32, cut)|thrust_damage(23, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["glaive", "Glaive", #长柄大刀
   [("glaive_b", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 257, 
   weight(6.5)|abundance(100)|difficulty(16)|weapon_length(244)|spd_rtng(75)|swing_damage(33, cut)|thrust_damage(22, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["hafted_blade_a", "Hafted_Blade", #宽刃刀
   [("khergit_pike_a", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 353, 
   weight(7.75)|abundance(100)|difficulty(15)|weapon_length(153)|spd_rtng(78)|swing_damage(34, cut)|thrust_damage(17, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["poleaxe", "Poleaxe", #长柄斧
   [("pole_ax", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 360, 
   weight(6)|abundance(100)|difficulty(16)|weapon_length(180)|spd_rtng(78)|swing_damage(36, cut)|thrust_damage(15, blunt), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["voulge", "Voulge", #长枪斧
   [("two_handed_battle_long_axe_a", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 420, 
   weight(7.75)|abundance(100)|difficulty(16)|weapon_length(175)|spd_rtng(78)|swing_damage(37, cut)|thrust_damage(18, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["long_bardiche", "Long_Bardiche", #长月刃斧
   [("two_handed_battle_long_axe_b", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 497, 
   weight(8)|abundance(100)|difficulty(17)|weapon_length(140)|spd_rtng(76)|swing_damage(38, cut)|thrust_damage(17, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["extra_long_shovel_axe", "Extra Long Shovel Axe", #超长铲斧
   [("mackie_pendulum", 0)], 
   itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_couchable|itp_unbalanced|itp_can_knock_down, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 520, 
   weight(8.25)|abundance(50)|difficulty(17)|weapon_length(180)|spd_rtng(77)|swing_damage(39, cut)|thrust_damage(26, cut), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["great_long_bardiche", "Great Long Bardiche", #巨型长月刃斧
   [("two_handed_battle_long_axe_c", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 668, 
   weight(8.5)|abundance(100)|difficulty(16)|weapon_length(155)|spd_rtng(79)|swing_damage(40, cut)|thrust_damage(17, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["steel_bardiche", "Steel Bardiche", #钢片月刃斧
   [("bardiche_ex", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced, 
   itc_shieldless_slashable_spear|itcf_carry_spear, 1000, 
   weight(7.5)|abundance(70)|difficulty(15)|weapon_length(125)|spd_rtng(83)|swing_damage(44, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["long_axe", "Long Axe", #长斧
   [("long_axe_a", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee|itp_unbalanced,
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 297, 
   weight(4.5)|abundance(100)|difficulty(12)|weapon_length(120)|spd_rtng(93)|swing_damage(35, cut)|thrust_damage(19, blunt), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["long_axe_alt", "Long Axe", #长斧
   [("long_axe_a", 0)], 
   itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, 
   itc_nodachi|itcf_carry_spear, 297, 
   weight(4.5)|abundance(100)|difficulty(12)|weapon_length(120)|spd_rtng(88)|swing_damage(35, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["long_axe_b", "Long War Axe", #长战斧
   [("long_axe_b", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee|itp_unbalanced, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 418, 
   weight(5.5)|abundance(100)|difficulty(13)|weapon_length(125)|spd_rtng(92)|swing_damage(39, cut)|thrust_damage(18, blunt), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["long_axe_b_alt", "Long_War_Axe", #长战斧
   [("long_axe_b", 0)], 
   itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, 
   itc_nodachi|itcf_carry_spear, 418, 
   weight(5.5)|abundance(100)|difficulty(13)|weapon_length(125)|spd_rtng(87)|swing_damage(39, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["long_axe_c", "Great Long Axe", #巨型长斧
   [("long_axe_c", 0)], 
   itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee|itp_unbalanced,
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 660, 
   weight(5.5)|abundance(100)|difficulty(14)|weapon_length(127)|spd_rtng(91)|swing_damage(42, cut)|thrust_damage(19, blunt), 
   imodbits_axe, [weapon_visual_effect_trigger]], 
["long_axe_c_alt", "Great Long Axe", #巨型长斧
   [("long_axe_c", 0)], 
   itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, 
   itc_nodachi|itcf_carry_spear, 660, 
   weight(5.5)|abundance(100)|difficulty(14)|weapon_length(127)|spd_rtng(85)|swing_damage(42, cut)|thrust_damage(0, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]], 

["great_scythe", "Great Scythe", #巨镰
   [("Txz_sgzl", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down|itp_cant_use_on_horseback, 
   itc_parry_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear, 2370, 
   weight(6.5)|abundance(30)|difficulty(18)|weapon_length(218)|spd_rtng(82)|swing_damage(33, pierce)|thrust_damage(0, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 
["short_blade_great_scythe", "Short Blade Great Scythe", #短刃巨镰
   [("Txz_cgf", 0)], 
   itp_type_polearm|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down, 
   itc_mountless_halberd|itcf_carry_spear, 2170, 
   weight(5.25)|abundance(30)|difficulty(18)|weapon_length(155)|spd_rtng(85)|swing_damage(34, pierce)|thrust_damage(0, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

["flail_spear", "Flail Spear", #连枷枪
   [("chandelier_lancer", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_unbalanced|itp_can_knock_down, 
   itc_parry_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear, 2070, 
   weight(6)|abundance(30)|difficulty(18)|weapon_length(268)|spd_rtng(92)|swing_damage(36, pierce)|thrust_damage(0, pierce), 
   imodbits_polearm, [weapon_visual_effect_trigger]], 

["luen_halberd", "Luen Halberd", #铭文斧枪
   [("halbert_hypocritical", 0)], 
   itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, 
   itc_mountless_halberd|itcf_carry_spear, 9985, 
   weight(7.5)|abundance(10)|difficulty(18)|weapon_length(178)|spd_rtng(80)|swing_damage(54, cut)|thrust_damage(34, pierce), 
   imodbits_axe, [weapon_visual_effect_trigger]],




#BOW
#_______________________________________________________________________________________________________________________________________________________________________________
#Elf bows cannot be used by motal because they actually use magic when pulling the bow. Even if a mortal meets the power draw requirements, forceful pulling can cause it to permanently break.
 ["bow_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######POWELL BOW#########
#短弓
["dragon_hunting_short_bow", "Dragon Hunting Short Bow", #猎龙短弓
   [("dargon_hunting_short_bow", 0), ("dargon_hunting_short_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 
   itcf_shoot_bow|itcf_carry_bow_back, 2745, 
   weight(1.75)|abundance(10)|difficulty(6)|accuracy(57)|spd_rtng(50)|shoot_speed(87)|max_ammo(0)|thrust_damage(31, pierce)|weapon_length(0), 
   imodbits_bow], 
#长弓
["dragon_hunting_bow", "Dragon Hunting Bow", #猎龙大弓
   [("txz_weapon_a03_03", 0), ("txz_weapon_a03_03_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 3145, 
   weight(4.5)|abundance(10)|difficulty(6)|accuracy(65)|spd_rtng(40)|shoot_speed(97)|max_ammo(0)|thrust_damage(33, pierce)|weapon_length(0), 
   imodbits_bow], 


#######ELF BOW#########
#以下是精灵军队的基础弓，各地出身普通的精灵士官（主要是半精灵）大多采用巡林长弓和巡狩短弓。
#长弓
["elf_simple_bow", "Elf Simple Bow",#精灵素弓
   [("mirkwood_bow", 0), ("mirkwood_bow_carry", ixmesh_carry)],
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1628,
   weight(0.5)|abundance(20)|difficulty(1)|accuracy(62)|spd_rtng(54)|shoot_speed(63)|max_ammo(0)|thrust_damage(25, pierce)|weapon_length(97),
   imodbits_bow, [elf_bow_trigger]], 
["elf_woodguard_longbow", "Elf Woodguard Longbow",#精灵巡林长弓
   [("aqs_magbow_fourth", 0), ("aqs_magbow_fourth_carry", ixmesh_carry)],
   itp_type_bow|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 2500, 
   weight(1.5)|abundance(15)|difficulty(3)|accuracy(78)|spd_rtng(57)|shoot_speed(77)|max_ammo(0)|thrust_damage(32, pierce)|weapon_length(105), 
   imodbits_bow, [elf_bow_trigger]], 
["elf_ornamentation_bow", "Elf Ornamentation Bow",#精灵纹饰弓
   [("Elfbow", 0), ("Elfbow_carry", ixmesh_carry)],
   itp_type_bow|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1628,
   weight(1.5)|abundance(15)|difficulty(3)|accuracy(82)|spd_rtng(60)|shoot_speed(80)|max_ammo(0)|thrust_damage(34, pierce)|weapon_length(80),
   imodbits_bow, [elf_bow_trigger]], 
#短弓
["elf_hunter_bow", "Elf hunter Bow",#精灵猎弓
   [("dedal_bow_tatar_c", 0), ("dedal_bowcase_tatar_c", ixmesh_carry), ("dedal_bow_tatar_c_icon", ixmesh_inventory)],
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 2034,
   weight(0.25)|abundance(20)|difficulty(2)|accuracy(56)|spd_rtng(60)|shoot_speed(57)|max_ammo(0)|thrust_damage(26, pierce)|weapon_length(70),
   imodbits_bow, [elf_bow_trigger]], 
["elf_outrider_bow", "Elf Outrider Bow", #精灵巡狩短弓
   [("short_imperial_bow", 0), ("short_imperial_bow_case", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 2761, 
   weight(0.5)|abundance(15)|difficulty(3)|accuracy(69)|spd_rtng(65)|shoot_speed(70)|max_ammo(0)|thrust_damage(30, pierce)|weapon_length(50), 
   imodbits_bow, [elf_bow_trigger]], 

#精锐纯血精灵士兵使用的弓
#短弓
["forestwarden_bow", "Forestwarden bow", #灵森守护弓
   [("imperial_bow", 0), ("imperial_bow_case", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 3944, 
   weight(0.75)|abundance(2)|difficulty(4)|accuracy(74)|spd_rtng(68)|shoot_speed(75)|max_ammo(0)|thrust_damage(34, pierce)|weapon_length(72), 
   imodbits_bow, [elf_bow_trigger]], 
["yishith_elite_ridebow", "Yishith Elite Ridebow", #伊希斯精锐骑弓
   [("imperial_bow_2", 0), ("imperial_bow_case_2", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 3700, 
   weight(0.75)|abundance(1)|difficulty(4)|accuracy(75)|spd_rtng(70)|shoot_speed(76)|max_ammo(0)|thrust_damage(33, pierce)|weapon_length(72), 
   imodbits_bow, [elf_bow_trigger]], 
#长弓
["string_of_elegy", "String of Elegy", #挽歌之弦
   [("aidagong", 0), ("aidagong_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 4633, 
   weight(1.75)|abundance(10)|difficulty(4)|accuracy(85)|spd_rtng(63)|shoot_speed(82)|max_ammo(0)|thrust_damage(36, pierce)|weapon_length(105), 
   imodbits_bow, [elf_bow_trigger]], 
["seawind_speaker", "Seawind Speaker", #海风语者
   [("Duskfall", 0), ("Duskfall_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 4033, 
   weight(1.4)|abundance(10)|difficulty(4)|accuracy(82)|spd_rtng(66)|shoot_speed(80)|max_ammo(0)|thrust_damage(35, pierce)|weapon_length(75), 
   imodbits_bow, [elf_bow_trigger]], 

#骑士团弓，除了供应给骑士团使用外，还是非神选的本派系领主和部分超级兵的装备。多少都有点特殊效果。
#短弓
["spirittree_knight_bow", "Spirittree Knight Bow", #灵树骑士弓，标准高级骑弓，可佩盾
   [("imperial_bow_1", 0), ("imperial_bow_case_1", ixmesh_carry)], 
   itp_type_bow|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 7750, 
   weight(0.5)|abundance(1)|difficulty(5)|accuracy(90)|spd_rtng(80)|shoot_speed(90)|max_ammo(0)|thrust_damage(39, pierce)|weapon_length(72), 
   imodbits_bow, [elf_bow_trigger]], 
["spiritwind_cavalry_bow", "Spiritwind Cavalry Bow", #灵风游骑弓，速射骑弓
   [("imperial_bow_3", 0), ("imperial_bow_case_3", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 7500, 
   weight(0.5)|abundance(1)|difficulty(5)|accuracy(88)|spd_rtng(90)|shoot_speed(89)|max_ammo(0)|thrust_damage(38, pierce)|weapon_length(72), 
   imodbits_bow, []], 
#长弓
["spiritrain_ranger_bow", "Spiritrain Ranger Bow", #灵雨大弓，速射步弓，可切换近战
   [("WJJTZG", 0), ("WJJTZGcarry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_cant_use_on_horseback|itp_next_item_as_melee, 
   itcf_shoot_bow|itcf_carry_bow_back, 8000, 
   weight(1.9)|abundance(1)|difficulty(5)|accuracy(89)|spd_rtng(120)|shoot_speed(80)|max_ammo(0)|thrust_damage(41, pierce)|weapon_length(151), 
   imodbits_bow, [elf_bow_trigger]], 
["spiritrain_ranger_bow_melee", "Spiritrain Ranger Bow",
    [("WJJTZG", 0)],
    itp_type_polearm|itp_primary|itp_two_handed|itp_offset_lance|itp_cant_use_on_horseback,
    itc_shieldless_slashable_spear|itcf_carry_spear, 8000,
    weight(1.9)|abundance(1)|difficulty(12)|weapon_length(151)|spd_rtng(86)|swing_damage(40, pierce)|thrust_damage(30, pierce),
    imodbits_polearm, [weapon_visual_effect_trigger]], 
["immortal_soul_bow", "Immortal Soul Bow", #永世者狙杀弓，狙击步弓
   [("6cfelves_bow", 0), ("6cfelves_bow_low", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 8100, 
   weight(2.25)|abundance(5)|difficulty(6)|accuracy(100)|spd_rtng(27)|shoot_speed(99)|max_ammo(0)|thrust_damage(50, pierce)|weapon_length(137), 
   imodbits_bow, [elf_bow_trigger]], 

#High Elf Bows
["eternal_inheritance_bow", "Eternal Inheritance Bow", #永世传承弓
   [("elvenbow", 0), ("elvenbow", ixmesh_carry)], 
   itp_type_bow|itp_unique|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 
   itcf_shoot_bow|itcf_carry_bow_back, 15000, 
   weight(0.5)|abundance(1)|difficulty(0)|accuracy(100)|spd_rtng(130)|shoot_speed(100)|max_ammo(0)|thrust_damage(50, pierce)|weapon_length(77), 
   imodbits_bow, [elf_bow_trigger]], 

#Dark Elf Bows
["dark_elf_longbow", "Dark Elf Longbow", #暗精灵长弓
   [("painted_bow", 0), ("painted_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 7894, 
   weight(1.7)|abundance(5)|difficulty(4)|accuracy(80)|spd_rtng(65)|shoot_speed(76)|max_ammo(0)|thrust_damage(35, pierce)|weapon_length(104), 
   imodbits_bow, [elf_bow_trigger]], 

#Rebel Elf Bows
["firm_ice_bow", "Firm Ice Bow", #坚寒大弓
   [("stahlrimbow", 0)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_extra_penetration|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 3633, 
   weight(3.25)|abundance(5)|difficulty(4)|accuracy(77)|spd_rtng(59)|shoot_speed(74)|max_ammo(0)|thrust_damage(28, pierce)|weapon_length(122), 
   imodbits_bow], 


#######STEPPE BOW#########
["slingshot", "Slingshot", #弹弓
   [("slingshot", 0)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_revolver_right, 56, 
   weight(0.5)|abundance(20)|difficulty(2)|accuracy(43)|spd_rtng(70)|shoot_speed(20)|max_ammo(0)|thrust_damage(27, blunt)|weapon_length(0), 
   imodbits_bow], 

#steppe bow
["nomad_bow", "Nomad Bow", #游牧弓
   [("nomad_bow", 0), ("nomad_bow_case", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 164, 
   weight(1.25)|abundance(100)|difficulty(2)|accuracy(52)|spd_rtng(50)|shoot_speed(42)|max_ammo(0)|thrust_damage(23, cut)|weapon_length(0), 
   imodbits_bow], 
["kouruto_bow", "Kouruto Bow", [("khergit_bow", 0), ("khergit_bow_case", ixmesh_carry)], #草原弓
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 269, 
   weight(1.25)|abundance(100)|difficulty(3)|accuracy(57)|spd_rtng(55)|shoot_speed(44)|max_ammo(0)|thrust_damage(26, cut)|weapon_length(0), 
   imodbits_bow], 
["southern_horn_bow", "Southern Horn Bow", #南方角弓
   [("mongolian_bow", 0), ("mongolian_bow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 454, 
   weight(1.75)|abundance(30)|difficulty(4)|accuracy(64)|spd_rtng(61)|shoot_speed(49)|max_ammo(0)|thrust_damage(31, cut)|weapon_length(0), 
   imodbits_bow], 
["elite_horn_bow", "Elite Horn Bow", #精锐角弓
   [("tatar_bow_h4", 0), ("tatar_bow_scabbard_h4", ixmesh_carry), ("tatar_bow_scabbard_h4.1", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left, 963, 
   weight(2)|abundance(30)|difficulty(4)|accuracy(69)|spd_rtng(66)|shoot_speed(54)|max_ammo(0)|thrust_damage(32, cut)|weapon_length(0), 
   imodbits_bow], 
["kouruto_auxiliary_bow", "Kouruto Auxiliary Bow", #科鲁托辅军弓
   [("amazon_bow", 0), ("amazon_bow_case", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left, 841, 
   weight(1.75)|abundance(40)|difficulty(4)|accuracy(70)|spd_rtng(73)|shoot_speed(60)|max_ammo(0)|thrust_damage(35, cut)|weapon_length(0), 
   imodbits_bow], 
["southern_knight_bow", "Southern Knight Bow", #南方骑士弓
   [("txz_weapon_a03_01", 0), ("txz_weapon_a03_01_case", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left, 1724, 
   weight(1.75)|abundance(30)|difficulty(6)|accuracy(73)|spd_rtng(77)|shoot_speed(70)|max_ammo(0)|thrust_damage(37, cut)|weapon_length(0), 
   imodbits_bow], 

# Steppe Longbow
["kouruto_homemade_longbow", "Kouruto Homemade Longbow", #科鲁托土制长弓
   [("aqs_magbow_first", 0), ("aqs_magbow_first_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1000, 
   weight(3.25)|abundance(30)|difficulty(3)|accuracy(68)|spd_rtng(42)|shoot_speed(60)|max_ammo(0)|thrust_damage(28, cut)|weapon_length(0), 
   imodbits_bow], 


#######CONFEDERATION BOW#########
#短弓
["hippogriff_short_bow", "Hippogriff Short Bow", #鹰猎骑弓
   [("elven_bow_short", 0), ("elven_bow_short", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 5052, 
   weight(1.5)|abundance(5)|difficulty(4)|accuracy(70)|spd_rtng(70)|shoot_speed(65)|max_ammo(0)|thrust_damage(30, blunt)|weapon_length(0), 
   imodbits_bow], 
["phoenix_splendid_bow", "Phoenix Splendid Bow", #神鸟绚烂弓
   [("lonely", 0), ("lonely_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 6145, 
   weight(1.5)|abundance(10)|difficulty(5)|accuracy(76)|spd_rtng(71)|shoot_speed(71)|max_ammo(0)|thrust_damage(31, pierce)|weapon_length(0), 
   imodbits_bow], 
#长弓
["hippogriff_recurve_bow", "Hippogriff Recurve Bow", #骏鹰反曲大弓
   [("elven_bow", 0), ("elven_bow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 7154, 
   weight(4)|abundance(20)|difficulty(5)|accuracy(83)|spd_rtng(63)|shoot_speed(82)|max_ammo(0)|thrust_damage(39, cut)|weapon_length(0), 
   imodbits_bow], 


#######PAPAL BOW#########
["papal_longbow", "Papal Longbow", #教国长弓
   [("aqs_magbow_third", 0), ("aqs_magbow_third_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1961, 
   weight(3.5)|abundance(100)|difficulty(4)|accuracy(74)|spd_rtng(64)|shoot_speed(70)|max_ammo(0)|thrust_damage(35, cut)|weapon_length(0), 
   imodbits_bow], 


#######EASTERN BOW#########
["tielin_bow", "Tielin Bow", #铁林弓
   [("hangong", 0), ("hangong", ixmesh_carry)], 
   itp_type_bow|itp_primary|itp_penalty_with_shield, 
   itcf_shoot_bow|itcf_carry_bow_back, 2100, 
   weight(2.5)|abundance(5)|difficulty(5)|accuracy(72)|spd_rtng(71)|shoot_speed(71)|max_ammo(0)|thrust_damage(38, cut)|weapon_length(0), 
   imodbits_bow], 
["eastern_cavalry_bow", "Eastern Cavalry Bow", #东方骑将弓
   [("jarl_Bow", 0), ("jarl_Bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_bonus_against_shield, 
   itcf_shoot_bow|itcf_carry_bow_back, 3025, 
   weight(1.75)|abundance(5)|difficulty(5)|accuracy(75)|spd_rtng(70)|shoot_speed(68)|max_ammo(0)|thrust_damage(39, pierce)|weapon_length(0), 
   imodbits_bow], 

#Eastern Longbow
["bogy_spur", "Bogy Spur", #妖邪之刺
   [("forswornbow", 0), ("forswornbow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 4754, 
   weight(3.5)|abundance(1)|difficulty(4)|accuracy(82)|spd_rtng(59)|shoot_speed(76)|max_ammo(0)|thrust_damage(36, cut)|weapon_length(0), 
   imodbits_bow], 
["conceal_bow", "Conceal Bow", #秘卫长弓
   [("dwarvenbowkarztev", 0), ("dwarvenbowkarztev", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 7000, 
   weight(3.75)|abundance(1)|difficulty(5)|accuracy(96)|spd_rtng(60)|shoot_speed(82)|max_ammo(0)|thrust_damage(34, pierce)|weapon_length(0), 
   imodbits_bow], 
["iron_adepti_bow", "Iron Adepti Bow", #铁仙弓
   [("nightingalebow", 0), ("nightingalebow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 9000, 
   weight(5)|abundance(3)|difficulty(6)|accuracy(87)|spd_rtng(65)|shoot_speed(89)|max_ammo(0)|thrust_damage(43, cut)|weapon_length(0), 
   imodbits_bow], 

["yumi", "Yumi", #和弓
   [("bogmir_yumi", 0), ("bogmir_yumi_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 3761, 
   weight(4)|abundance(30)|difficulty(6)|accuracy(79)|spd_rtng(64)|shoot_speed(74)|max_ammo(0)|thrust_damage(34, cut)|weapon_length(0), 
   imodbits_bow], 
["gorgeous_eastern_greatbow", "Gorgeous Eastern Greatbow", #华丽东方大弓
   [("yumi_h4", 0), ("yumi_carry_h4", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 6555, 
   weight(4.25)|abundance(20)|difficulty(4)|accuracy(84)|spd_rtng(70)|shoot_speed(82)|max_ammo(0)|thrust_damage(41, cut)|weapon_length(0), 
   imodbits_bow], 
["general_greatbow", "General Greatbow", #将军大弓
   [("long_bow_h4", 0), ("long_bow_carry_h4", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 7962, 
   weight(4.75)|abundance(10)|difficulty(7)|accuracy(88)|spd_rtng(74)|shoot_speed(80)|max_ammo(0)|thrust_damage(45, cut)|weapon_length(0), 
   imodbits_bow], 


#######STARKHOOK BOW#########
["simple_archipelagic_short_bow", "Simple Archipelagic Short Bow", #简易外岛短弓
   [("nordherobow_simple", 0), ("nordherobow_simple", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1054, 
   weight(1.5)|abundance(10)|difficulty(3)|accuracy(46)|spd_rtng(65)|shoot_speed(39)|max_ammo(0)|thrust_damage(33, cut)|weapon_length(63), 
   imodbits_bow], 
["archipelagic_short_bow", "Archipelagic Short Bow", #外岛短弓
   [("nordherobow", 0), ("nordherobow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1154, 
   weight(1.75)|abundance(20)|difficulty(4)|accuracy(50)|spd_rtng(65)|shoot_speed(42)|max_ammo(0)|thrust_damage(35, cut)|weapon_length(63), 
   imodbits_bow], 
["red_short_bow", "Red Short Bow", #赤红短弓
   [("spak_bow6", 0), ("spak_bow6_case", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 3154, 
   weight(1.75)|abundance(1)|difficulty(4)|accuracy(55)|spd_rtng(69)|shoot_speed(46)|max_ammo(0)|thrust_damage(27, pierce)|weapon_length(53), 
   imodbits_bow], 

["westcoast_longbow", "Westcoast Longbow", #西海长弓
   [("gondor_bow", 0), ("gondor_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1633, 
   weight(3.25)|abundance(50)|difficulty(3)|accuracy(72)|spd_rtng(69)|shoot_speed(65)|max_ammo(0)|thrust_damage(30, cut)|weapon_length(0), 
   imodbits_bow], 
["simple_archipelagic_long_bow", "Simple Archipelagic Long Bow", #简易外岛长弓
   [("nordherobow_long_simple", 0), ("nordherobow_long_simple", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1754, 
   weight(3.75)|abundance(10)|difficulty(3)|accuracy(56)|spd_rtng(49)|shoot_speed(69)|max_ammo(0)|thrust_damage(33, cut)|weapon_length(110), 
   imodbits_bow], 
["archipelagic_long_bow", "Archipelagic Long Bow", #外岛长弓
   [("nordherobow_long", 0), ("nordherobow_long", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1854, 
   weight(4)|abundance(20)|difficulty(4)|accuracy(60)|spd_rtng(49)|shoot_speed(73)|max_ammo(0)|thrust_damage(35, cut)|weapon_length(110), 
   imodbits_bow], 
["veinshade_wing", "Veinshade Wing", #血影之翼
   [("crimson_bow", 0), ("crimson_bow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_unique, 
   itcf_shoot_bow|itcf_carry_bow_back, 37154, 
   weight(0)|abundance(1)|difficulty(0)|accuracy(83)|spd_rtng(63)|shoot_speed(92)|max_ammo(0)|thrust_damage(40, pierce)|weapon_length(83), 
   imodbits_none], 


#######UNDEAD BOW#########
#短弓
["osteotomy_bow", "Osteotomy Bow", #截骨弓
   [("dragonbonebow_short", 0), ("dragonbonebow_short", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1094, 
   weight(2.6)|abundance(1)|difficulty(2)|accuracy(60)|spd_rtng(66)|shoot_speed(58)|max_ammo(0)|thrust_damage(31, cut)|weapon_length(75), 
   imodbits_bow], 
["drowning_bow", "Drowning Bow", #溺死鬼复合弓
   [("draugrbow_simple", 0), ("draugrbow_simple", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1954, 
   weight(2)|abundance(1)|difficulty(3)|accuracy(52)|spd_rtng(56)|shoot_speed(46)|max_ammo(0)|thrust_damage(34, cut)|weapon_length(80), 
   imodbits_bow], 
["tidal_revival_bow", "Tidal Revival Bow", #潮汐复生之弓
   [("draugrbow", 0), ("draugrbow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 2754, 
   weight(2.25)|abundance(1)|difficulty(4)|accuracy(55)|spd_rtng(57)|shoot_speed(50)|max_ammo(0)|thrust_damage(37, cut)|weapon_length(80), 
   imodbits_bow], 
["undead_hateful_bow", "Undead Hateful Bow", #不死憎恶弓
   [("noldor_bow", 0), ("noldor_bow_case", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 6214, 
   weight(1.5)|abundance(1)|difficulty(6)|accuracy(80)|spd_rtng(70)|shoot_speed(80)|max_ammo(0)|thrust_damage(36, pierce)|weapon_length(0), 
   imodbits_bow], 

#长弓
["vestigial_bow", "Vestigial Bow", #残存之弓
   [("orcishbow", 0), ("orcishbow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 4021, 
   weight(4)|abundance(1)|difficulty(5)|accuracy(82)|spd_rtng(50)|shoot_speed(76)|max_ammo(0)|thrust_damage(37, cut)|weapon_length(0), 
   imodbits_bow], 
["osteotomy_longbow", "Osteotomy Longbow", #刺骨长弓
   [("dragonbonebow", 0), ("dragonbonebow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 4094, 
   weight(4.6)|abundance(1)|difficulty(2)|accuracy(85)|spd_rtng(52)|shoot_speed(78)|max_ammo(0)|thrust_damage(39, cut)|weapon_length(120), 
   imodbits_bow], 
["walker_flesh_greatbow", "Walker Flesh Greatbow", #丧尸血肉大弓
   [("ullrvetr3", 0), ("ullrvetr3", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 8961, 
   weight(4.25)|abundance(1)|difficulty(4)|accuracy(57)|spd_rtng(38)|shoot_speed(20)|max_ammo(0)|thrust_damage(20, cut)|weapon_length(0), 
   imodbits_bow], 


#######DEMON BOW#########
#短弓
["demon_reverse_bow", "Demon Reverse Bow", #魔族反曲弓
   [("dwarvenbowkarztev", 0), ("dwarvenbowkarztev", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 9045, 
   weight(2.75)|abundance(1)|difficulty(8)|accuracy(89)|spd_rtng(81)|shoot_speed(86)|max_ammo(0)|thrust_damage(39, pierce)|weapon_length(0), 
   imodbits_bow], 
["manhunter_short_bow", "Manhunter Short Bow", #猎杀人类短弓
   [("ebonybow", 0), ("ebonybow", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 10700, 
   weight(3)|abundance(1)|difficulty(9)|accuracy(96)|spd_rtng(81)|shoot_speed(92)|max_ammo(0)|thrust_damage(40, pierce)|weapon_length(0), 
   imodbits_bow], 
["demon_knight_bow", "Demon Knight Bow", #魔骑士弓
   [("daedricbow", 0), ("daedricbow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 11055, 
   weight(2.5)|abundance(1)|difficulty(10)|accuracy(95)|spd_rtng(84)|shoot_speed(96)|max_ammo(0)|thrust_damage(47, pierce)|weapon_length(0), 
   imodbits_bow], 


#######SABIANISM BOW#########
["meteorite_bow", "Meteorite Bow", #星陨弓
   [("aqs_magbow_second", 0), ("aqs_magbow_second_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 6069, 
   weight(3.75)|abundance(10)|difficulty(7)|accuracy(99)|spd_rtng(70)|shoot_speed(100)|max_ammo(0)|thrust_damage(33, pierce)|weapon_length(0), 
   imodbits_bow], 


#######WITCHCRAFT BOW#########
#短弓
["witchcraft_poinson_bow", "Witchcraft Poinson Bow", #巫蛊毒弓
   [("melitine_bow4", 0), ("melitine_bow4_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 2143, 
   weight(1.25)|abundance(3)|difficulty(2)|accuracy(80)|spd_rtng(65)|shoot_speed(66)|max_ammo(0)|thrust_damage(24, pierce)|weapon_length(0), 
   imodbits_bow], 
["witchcraft_poinson_composite_bow", "Witchcraft Poinson Composite Bow", #巫蛊毒复合弓
   [("melitine_bow3", 0), ("melitine_bow3_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 3742, 
   weight(1.5)|abundance(2)|difficulty(4)|accuracy(83)|spd_rtng(72)|shoot_speed(67)|max_ammo(0)|thrust_damage(27, pierce)|weapon_length(0), 
   imodbits_bow], 
["eroding_green_bow", "Eroding Green Bow", #翠蚀弓
   [("glassbo", 0), ("glassbo", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 8754, 
   weight(2)|abundance(1)|difficulty(5)|accuracy(86)|spd_rtng(78)|shoot_speed(72)|max_ammo(0)|thrust_damage(30, pierce)|weapon_length(0), 
   imodbits_bow], 

#长弓
["snake_spot_longbow", "Snake Spot Longbow", #蛇斑长弓
   [("bogmir_yumi_final", 0), ("bogmir_yumi_final_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 6761, 
   weight(3.25)|abundance(1)|difficulty(6)|accuracy(90)|spd_rtng(54)|shoot_speed(74)|max_ammo(0)|thrust_damage(34, cut)|weapon_length(0), 
   imodbits_bow], 
["abscess_bow", "Abscess Bow", #肿胀大弓
   [("falmerbow", 0), ("falmerbow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 9704, 
   weight(5)|abundance(1)|difficulty(8)|accuracy(52)|spd_rtng(35)|shoot_speed(55)|max_ammo(95)|thrust_damage(29, pierce)|weapon_length(0), 
   imodbits_bow], 


#######ECLIPSE BOW#########
["copper_bow_simple", "Copper Bow Simple", #简易铜饰弓
   [("dwarvenbow_simple", 0), ("dwarvenbow_simple", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1054, 
   weight(7)|abundance(10)|difficulty(3)|accuracy(62)|spd_rtng(80)|shoot_speed(69)|max_ammo(0)|thrust_damage(30, cut)|weapon_length(0), 
   imodbits_bow], 
["copper_bow", "Copper Bow", #铜饰弓
   [("dwarvenbow", 0), ("dwarvenbow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1450, 
   weight(7.25)|abundance(10)|difficulty(4)|accuracy(65)|spd_rtng(84)|shoot_speed(74)|max_ammo(0)|thrust_damage(33, cut)|weapon_length(0), 
   imodbits_bow], 
["lava_great_bow", "Lava Great Bow", #浊热巨弓
   [("lava_bow", 0), ("lava_bow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 1450, 
   weight(10)|abundance(10)|difficulty(6)|accuracy(50)|spd_rtng(84)|shoot_speed(34)|max_ammo(0)|thrust_damage(33, blunt)|weapon_length(130), 
   imodbits_bow], 


#######ANCIENT WORRIER BOW#########
["relic_bow", "Relic Bow", #遗迹大弓
   [("aurielsbow", 0), ("aurielsbow", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 9954, 
   weight(15)|abundance(1)|difficulty(7)|accuracy(78)|spd_rtng(31)|shoot_speed(86)|max_ammo(0)|thrust_damage(50, cut)|weapon_length(0), 
   imodbits_bow], 


#######COMMON BOW#########
#Longbows
["practice_bow_2", "Practice Long Bow", #练习弓
   [("hunting_bow", 0), ("hunting_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 50, 
   weight(2)|abundance(100)|difficulty(0)|accuracy(35)|spd_rtng(20)|shoot_speed(30)|max_ammo(0)|thrust_damage(21, blunt)|weapon_length(0), 
   imodbits_bow], 
["simple_long_bow", "Simple Long Bow", #简陋长弓
   [("woodenbow_long", 0), ("woodenbow_long", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 85, 
   weight(2.5)|abundance(100)|difficulty(0)|accuracy(58)|spd_rtng(34)|shoot_speed(45)|max_ammo(0)|thrust_damage(23, cut)|weapon_length(0), 
   imodbits_bow], 
["long_bow", "Long Bow", #长弓
   [("long_bow", 0), ("long_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 145, 
   weight(2.75)|abundance(100)|difficulty(3)|accuracy(64)|spd_rtng(39)|shoot_speed(60)|max_ammo(0)|thrust_damage(27, cut)|weapon_length(0), 
   imodbits_bow], 
["war_bow", "War Bow", #长复合弓
   [("war_bow", 0), ("war_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 728, 
   weight(3.5)|abundance(100)|difficulty(4)|accuracy(69)|spd_rtng(44)|shoot_speed(65)|max_ammo(0)|thrust_damage(31, cut)|weapon_length(0), 
   imodbits_bow], 
["archer_longbow", "Archer Longbow", #射手长弓
   [("Archer_Bow", 0), ("Archer_Bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 2245, 
   weight(4)|abundance(30)|difficulty(5)|accuracy(74)|spd_rtng(49)|shoot_speed(70)|max_ammo(0)|thrust_damage(36, cut)|weapon_length(0), 
   imodbits_bow], 
["strengthen_archer_longbow", "Strengthen Archer Longbow", #加强射手长弓
   [("Archer_Bow2", 0), ("Archer_Bow2_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 2400, 
   weight(4.25)|abundance(30)|difficulty(5)|accuracy(80)|spd_rtng(52)|shoot_speed(73)|max_ammo(0)|thrust_damage(38, cut)|weapon_length(0), 
   imodbits_bow],
["gorgeous_recurve_bow", "Gorgeous Recurve Bow", #华丽反曲大弓
   [("latticed_flatbow", 0), ("latticed_flatbow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, 
   itcf_shoot_bow|itcf_carry_bow_back, 3100, 
   weight(3.25)|abundance(15)|difficulty(6)|accuracy(84)|spd_rtng(57)|shoot_speed(74)|max_ammo(0)|thrust_damage(40, pierce)|weapon_length(97), 
   imodbits_bow], 

#Shortbows
["simple_bow", "Simple Bow", #简陋弓
   [("woodenbow", 0), ("woodenbow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 5, 
   weight(1)|abundance(100)|difficulty(0)|accuracy(34)|spd_rtng(39)|shoot_speed(30)|max_ammo(0)|thrust_damage(16, cut)|weapon_length(0), 
   imodbits_bow], 
["hunting_bow", "Hunting Bow", #猎弓
   [("hunting_bow", 0), ("hunting_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 17, 
   weight(1)|abundance(100)|difficulty(0)|accuracy(40)|spd_rtng(45)|shoot_speed(35)|max_ammo(0)|thrust_damage(18, cut)|weapon_length(0), 
   imodbits_bow], 
["short_bow", "Short Bow", #短弓
   [("short_bow", 0), ("short_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 58, 
   weight(1.25)|abundance(100)|difficulty(1)|accuracy(47)|spd_rtng(47)|shoot_speed(40)|max_ammo(0)|thrust_damage(22, cut)|weapon_length(0), 
   imodbits_bow], 

["strong_bow", "Strong Bow", #短复合弓
   [("strong_bow", 0), ("strong_bow_case", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 437, 
   weight(1.25)|abundance(100)|difficulty(3)|accuracy(52)|spd_rtng(49)|shoot_speed(45)|max_ammo(0)|thrust_damage(27, cut)|weapon_length(0), 
   imodbits_crossbow], 
["noble_practice_bow", "Noble Practice Bow", #贵族练习短弓
   [("spak_bow7", 0), ("spak_bow7_case", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 587, 
   weight(1.5)|abundance(5)|difficulty(3)|accuracy(65)|spd_rtng(52)|shoot_speed(46)|max_ammo(0)|thrust_damage(26, blunt)|weapon_length(0), 
   imodbits_crossbow], 

["simple_recurve_bow", "Simple Recurve Bow", #简易反曲弓
   [("my_bow", 0), ("my_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 645, 
   weight(1.75)|abundance(100)|difficulty(3)|accuracy(60)|spd_rtng(57)|shoot_speed(50)|max_ammo(0)|thrust_damage(29, cut)|weapon_length(0), 
   imodbits_bow], 
["gorgeous_composite_bow", "Gorgeous Composite Bow", #华丽复合弓
   [("bow_h4", 0), ("bow_carry_h4", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1754, 
   weight(2)|abundance(20)|difficulty(5)|accuracy(66)|spd_rtng(61)|shoot_speed(55)|max_ammo(0)|thrust_damage(33, cut)|weapon_length(0), 
   imodbits_bow], 
["knight_recurve_bow", "Knight Recurve Bow", #骑士反曲弓
   [("new_bow", 0), ("new_bow_carry", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 835, 
   weight(2.25)|abundance(70)|difficulty(4)|accuracy(71)|spd_rtng(65)|shoot_speed(60)|max_ammo(0)|thrust_damage(36, cut)|weapon_length(0), 
   imodbits_bow], 

["iron_bow", "Iron Bow", #铁箍弓
   [("ironbow", 0), ("ironbow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 754, 
   weight(2.5)|abundance(80)|difficulty(3)|accuracy(73)|spd_rtng(56)|shoot_speed(68)|max_ammo(0)|thrust_damage(40, cut)|weapon_length(0), 
   imodbits_bow], 
["steel_bow", "Steel Bow", #钢轮弓
   [("steelbow", 0), ("steelbow", ixmesh_carry)], 
   itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, 
   itcf_shoot_bow|itcf_carry_bow_back, 1078, 
   weight(2.75)|abundance(20)|difficulty(4)|accuracy(78)|spd_rtng(60)|shoot_speed(72)|max_ammo(0)|thrust_damage(43, cut)|weapon_length(0), 
   imodbits_bow], 

["heroic_composite_bow", "Heroic Composite Bow", #英雄复合弓
   [("bow_nordic", 0), ("bow_nordic_carry", ixmesh_carry)], 
   itp_type_bow|itp_two_handed|itp_primary|itp_unique, 
   itcf_shoot_bow|itcf_carry_bow_back, 18035, 
   weight(3)|abundance(1)|difficulty(11)|accuracy(89)|spd_rtng(93)|shoot_speed(99)|max_ammo(0)|thrust_damage(36, pierce)|weapon_length(0), 
   imodbits_bow], 




#ARROWS
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["arrow_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######POWELL ARROW#########
["wangguo_jian", "wangguo_jian", [("gondor_arrow", 0), ("gondor_quiver", ixmesh_inventory), ("gondor_arrow_flying", ixmesh_flying_ammo), ("gondor_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 260, weight(3.000000)|abundance(10)|weapon_length(98)|max_ammo(76)|thrust_damage(4, pierce), imodbits_missile], 
["wangguo_lierenjian", "wangguo_lierenjian", [("spak_ar", 0), ("spak_ar_bag", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("spak_ar_bag", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 500, weight(3.500000)|abundance(50)|weapon_length(95)|max_ammo(75)|thrust_damage(6, pierce), imodbits_missile], 
["dragon_hunter_arrow", "dragon_hunter_arrow", [("WJJTZGPJJ", 0), ("WJJTZGPJJB", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("WJJTZGPJJB", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3500, weight(3.000000)|abundance(30)|weapon_length(120)|max_ammo(15)|thrust_damage(20, pierce), imodbits_missile], 


#######ELF ARROW#########
#Normal Elf Arrows
["jingling_lierenjian1", "jingling_lierenjian1", [("ilithien_arrow", 0), ("ithilien_quiver", ixmesh_inventory), ("ilithien_arrow_flying", ixmesh_flying_ammo), ("ithilien_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 500, weight(2.000000)|abundance(10)|weapon_length(95)|max_ammo(64)|thrust_damage(6, pierce), imodbits_missile], 

#Elf Soldier Arrows
["green_arrow", "Green Arrow", #青葱箭
   [("6cfelves_bowgong", 0), ("6cfelves_bowgong_qiao", ixmesh_inventory), ("6cfelves_bowgong_fly", ixmesh_flying_ammo), ("6cfelves_bowgong_qiao", ixmesh_carry)], 
   itp_type_arrows|itp_merchandise|itp_bonus_against_shield|itp_extra_penetration, 
   itcf_carry_quiver_back_right, 2200, weight(2)|abundance(5)|weapon_length(95)|max_ammo(40)|thrust_damage(8, pierce), 
   imodbits_missile], 
["jingling_sanbingjian", "jingling_sanbingjian", [("w_arr", 0), ("w_qui", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("w_qui", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3000, weight(2.000000)|abundance(5)|weapon_length(95)|max_ammo(40)|thrust_damage(10, pierce), imodbits_missile], 
["jingling_shuyongjian", "jingling_shuyongjian", [("mirkwood_arrow", 0), ("sldequiver", ixmesh_inventory), ("mirkwood_arrow_flying", ixmesh_flying_ammo), ("sldequiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3431, weight(1.500000)|abundance(5)|weapon_length(105)|max_ammo(76)|thrust_damage(12, pierce), imodbits_missile], 
["jingling_youxiajian", "jingling_youxiajian", [("silvan_arrow", 0), ("silvan_arrowquiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("silvan_arrowquiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3800, weight(1.500000)|abundance(20)|weapon_length(95)|max_ammo(35)|thrust_damage(13, pierce), imodbits_missile], 

#Elf Advanced Arrow
["daoye_jian", "daoye_jian", [("lonely_ar", 0), ("lonely_quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("lonely_quiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3500, weight(1.500000)|abundance(5)|weapon_length(91)|max_ammo(38)|thrust_damage(14, pierce), imodbits_missile],  
["jingling_liulijian", "jingling_liulijian", [("glassarrow", 0), ("glassarrow_quiver", ixmesh_inventory), ("flying_glassarrow", ixmesh_flying_ammo), ("glassarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3729, weight(1.250000)|abundance(5)|weapon_length(95)|max_ammo(55)|thrust_damage(18, pierce), imodbits_missile],

#High Elf Arrows
["gaojingling_xuejian", "gaojingling_xuejian", [("e_arrow", 0), ("Equiver_b", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("Equiver_b", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 5900, weight(1.500000)|abundance(5)|weapon_length(95)|max_ammo(70)|thrust_damage(21, pierce), imodbits_missile], 

#Rebel Elf Arrows
["jianhan_jian", "jianhan_jian", [("stahlrimarrow", 0), ("stahlrimarrow_quiver", ixmesh_inventory), ("flying_stahlrimarrow", ixmesh_flying_ammo), ("stahlrimarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 3142, weight(2.000000)|abundance(5)|weapon_length(91)|max_ammo(27)|thrust_damage(10, pierce), imodbits_missile], 


#######STEPPE ARROW#########
["slingshot_stones", "Slingshot Stones", #石弹
   [("throwing_stone", 0)], 
   itp_type_arrows|itp_merchandise, 0, 1, 
   weight(4)|abundance(100)|max_ammo(36)|thrust_damage(0, blunt), 
   imodbit_large_bag], 

["caoyuan_youliejian", "caoyuan_youliejian", [("orcisharrow", 0), ("orcisharrow_quiver", ixmesh_inventory), ("flying_orcisharrow", ixmesh_flying_ammo), ("orcisharrow_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 220, weight(2.500000)|abundance(50)|weapon_length(91)|max_ammo(60)|thrust_damage(2, pierce), imodbits_missile], 
["khergit_arrows", "Khergit_Arrows", [("arrow_b", 0), ("quiver_b", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 400, weight(3.500000)|abundance(20)|weapon_length(95)|max_ammo(68)|thrust_damage(4, cut), imodbits_missile], 
["nanfang_jian", "nanfang_jian", [("tatar_arrows_h4", 0), ("tatar_arrows_quiver_h4", ixmesh_inventory), ("tatar_arrows_flying_h4", ixmesh_flying_ammo), ("tatar_arrows_quiver_h4", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 900, weight(3.500000)|abundance(30)|weapon_length(95)|max_ammo(70)|thrust_damage(5, pierce), imodbits_missile], 

#Kouruto Refugee Arrows
["kouruto_refugee_arrow", "Kouruto Refugee Arrow", [("txz_weapon_a03_02", 0), ("txz_weapon_a03_02_case", ixmesh_inventory), ("txz_weapon_a03_02_fly", ixmesh_flying_ammo), ("txz_weapon_a03_02_case", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 300, weight(3.500000)|abundance(100)|weapon_length(95)|max_ammo(70)|thrust_damage(4, pierce), imodbits_missile], 


#######CONFEDERATION ARROW#########
["banglian_shenniaojian", "banglian_shenniaojian", [("spak_arrow", 0), ("spak_quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("spak_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 1700, weight(3.000000)|abundance(10)|weapon_length(82)|max_ammo(28)|thrust_damage(7, pierce), imodbits_missile], 
["fengniao_jian", "fengniao_jian", [("3steel_arrow", 0), ("phoenix_quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("phoenix_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 2350, weight(3.500000)|abundance(20)|weapon_length(91)|max_ammo(34)|thrust_damage(9, pierce), imodbits_missile], 


#######EASTERN ARROW#########
["dongfang_gangjian", "dongfang_gangjian", [("steelarrow", 0), ("steelarrow_quiver", ixmesh_inventory), ("flying_steelarrow", ixmesh_flying_ammo), ("steelarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 800, weight(4.500000)|abundance(50)|weapon_length(95)|max_ammo(80)|thrust_damage(7, pierce), imodbits_missile], 
["dongfangjingjunjian", "dongfangjingjunjian", [("aidaarrow", 0), ("aidaarrowtao", ixmesh_inventory), ("aidaarrow_fly", ixmesh_flying_ammo), ("aidaarrowtao", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 600, weight(3.500000)|abundance(30)|weapon_length(95)|max_ammo(60)|thrust_damage(9, pierce), imodbits_missile], 


#######STARKHOOK ARROW#########
["blood_extinguish_arrow", "Blood Extinguish Arrow", #熄血箭
   [("nordheroarrow", 0), ("nordheroarrow_quiver", ixmesh_inventory), ("flying_nordheroarrow", ixmesh_flying_ammo), ("nordheroarrow_quiver", ixmesh_carry)], 
   itp_type_arrows|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 1122, 
   weight(3.5)|abundance(10)|weapon_length(94)|max_ammo(35)|thrust_damage(8, pierce), imodbits_missile], 
["weeping_blood_arrow", "Weeping Blood Arrow", #泣血箭
   [("spak_bow6_arrow", 0), ("spak_bow6_quiver", ixmesh_inventory), ("flying_nordheroarrow", ixmesh_flying_ammo), ("spak_bow6_quiver", ixmesh_carry)],
   itp_type_arrows|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 2225, 
   weight(3.7)|abundance(1)|weapon_length(94)|max_ammo(33)|thrust_damage(9, pierce), imodbits_missile], 
["curse_blood_evil_arrow", "Curse Blood Evil Arrow", #咒血恶箭
   [("spak_ar2", 0), ("spak_ar2bag", ixmesh_inventory), ("flying_nordheroarrow", ixmesh_flying_ammo), ("spak_ar2bag", ixmesh_carry)],
   itp_type_arrows|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 2825, 
   weight(3.7)|abundance(1)|weapon_length(94)|max_ammo(30)|thrust_damage(10, pierce), imodbits_missile], 

["red_thread_whisperer", "Red Thread Whisperer", #低语赤线
   [("crimson_arrow", 0), ("crimson_arrow_quiver", ixmesh_inventory), ("flying_crimson_arrow", ixmesh_flying_ammo), ("crimson_arrow_quiver", ixmesh_carry)],
   itp_type_arrows|itp_bonus_against_shield|itp_extra_penetration|itp_unique, itcf_carry_quiver_back_right, 7225, 
   weight(0.5)|abundance(1)|weapon_length(94)|max_ammo(23)|thrust_damage(11, pierce), imodbits_none], 


#######UNDEAD ARROW#########
["busi_jiayuanjian", "busi_jiayuanjian", [("scull_arrow", 0), ("scull_quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("scull_quiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 8000, weight(3.500000)|abundance(10)|weapon_length(95)|max_ammo(75)|thrust_damage(11, pierce), imodbits_missile], 


#######SABIANISM ARROW#########
["yinyue_jian", "yinyue_jian", [("silvermoon_arrow", 0), ("silvermoon_bag", ixmesh_inventory), ("silvermoon_arrow_fly", ixmesh_flying_ammo), ("silvermoon_bag", ixmesh_carry)], itp_type_arrows|itp_bonus_against_shield|itp_extra_penetration, itcf_carry_quiver_back_right, 2200, weight(3.000000)|abundance(5)|weapon_length(91)|max_ammo(70)|thrust_damage(12, pierce), imodbits_missile], 


#######WITCHCRAFT ARROW#########
["wugu_jian1", "wugu_jian1", [("melitine_bow3_arrow", 0), ("melitine_bow3_quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("melitine_bow3_quiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_back_right, 3700, weight(3.500000)|abundance(10)|weapon_length(95)|max_ammo(60)|thrust_damage(8, pierce), imodbits_missile], 
["witchcraft_toxic_arrow", "witchcraft_toxic_arrow", [("melitine_bow4_arrow", 0), ("melitine_bow4_quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("melitine_bow4_quiver", ixmesh_carry)], itp_type_arrows|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_back_right, 2400, weight(3.000000)|abundance(10)|weapon_length(91)|max_ammo(80)|thrust_damage(4, pierce), imodbits_missile], 
["dim_light_arrow", "dim_light_arrow", [("elvenarrow", 0), ("elvenarrow_quiver", ixmesh_inventory), ("flying_elvenarrow", ixmesh_flying_ammo), ("elvenarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 2453, weight(3.500000)|abundance(10)|weapon_length(91)|max_ammo(25)|thrust_damage(15, pierce), imodbits_missile], 


#######ADVENTURER ARROW#########
["maoxianzhe_buqiangjian", "maoxianzhe_buqiangjian", [("gromitearrow", 0), ("gromiteq", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("gromiteq", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 905, weight(3.000000)|abundance(30)|weapon_length(93)|max_ammo(32)|thrust_damage(9, pierce), imodbits_missile], 


#######GRAGHITE STEEL ARROW#########
["mogang_jian", "mogang_jian", [("ebonyarrow", 0), ("ebonyarrow_quiver", ixmesh_inventory), ("flying_ebonyarrow", ixmesh_flying_ammo), ("ebonyarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 1330, weight(3.500000)|abundance(20)|weapon_length(95)|max_ammo(44)|thrust_damage(12, pierce), imodbits_missile], 
["mogang_zhongjian", "mogang_zhongjian", [("nordicarrow", 0), ("nordicarrow_quiver", ixmesh_inventory), ("flying_nordicarrow", ixmesh_flying_ammo), ("nordicarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 1673, weight(3.750000)|abundance(20)|weapon_length(95)|max_ammo(44)|thrust_damage(13, pierce), imodbits_missile], 


#######GILDING ARROW#########
["gilding_arrow", "gilding_arrow", [("jin_arrow", 0), ("arrowcase", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("arrowcase", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 550, weight(3.000000)|abundance(100)|weapon_length(95)|max_ammo(60)|thrust_damage(5, pierce), imodbits_missile], 


#######COMMON ARROW#########
["practice_arrows_2", "Practice_Arrows", [("arena_arrow", 0), ("quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows, 2147483648, 0, weight(1.500000)|abundance(100)|weapon_length(95)|max_ammo(80)|thrust_damage(0, cut), imodbits_missile], 
["arrows", "Arrows", [("arrow", 0), ("quiver", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, 2147483648, 50, weight(3.000000)|abundance(100)|weapon_length(95)|max_ammo(80)|thrust_damage(1, cut), imodbits_missile], 
["barbed_arrows", "Barbed_Arrows", [("barbed_arrow", 0), ("quiver_d", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 100, weight(3.000000)|abundance(70)|weapon_length(95)|max_ammo(76)|thrust_damage(2, cut), imodbits_missile], 
["bodkin_arrows", "Bodkin_Arrows", [("piercing_arrow", 0), ("quiver_c", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 200, weight(3.000000)|abundance(50)|weapon_length(91)|max_ammo(72)|thrust_damage(3, pierce), imodbits_missile], 
["hongyu_sheshoujian", "hongyu_sheshoujian", [("arrows_h4", 0), ("arrows_quiver_h4", ixmesh_inventory), ("arrows_flying_h4", ixmesh_flying_ammo), ("arrows_quiver_h4", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 633, weight(3.500000)|abundance(40)|weapon_length(100)|max_ammo(36)|thrust_damage(6, pierce), imodbits_missile], 
["noble_hunting_arrow", "noble_hunting_arrow", [("barbed_arrows_h4", 0), ("barbed_arrows_quiver_h4", ixmesh_inventory), ("barbed_arrows_flying_h4", ixmesh_flying_ammo), ("barbed_arrows_quiver_h4", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 722, weight(3.000000)|abundance(30)|weapon_length(91)|max_ammo(40)|thrust_damage(7, pierce), imodbits_missile], 
["hongyu_zhuitoujian", "hongyu_zhuitoujian", [("bodkin_arrows_h4", 0), ("bodkin_arrows_quiver_h4", ixmesh_inventory), ("bodkin_arrows_flying_h4", ixmesh_flying_ammo), ("bodkin_arrows_quiver_h4", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 1000, weight(3.500000)|abundance(10)|weapon_length(95)|max_ammo(30)|thrust_damage(8, pierce), imodbits_missile], 

["jianliang_jian", "jianliang_jian", [("ironarrow", 0), ("ironarrow_quiver", ixmesh_inventory), ("flying_ironarrow", ixmesh_flying_ammo), ("ironarrow_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 240, weight(3.000000)|abundance(20)|weapon_length(98)|max_ammo(52)|thrust_damage(3, pierce), imodbits_missile], 
["gangjian", "gangjian", [("3steel_arrow", 0), ("3steel_arrow_bag", ixmesh_inventory), ("flying_missile", ixmesh_flying_ammo), ("3steel_arrow_bag", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, itcf_carry_quiver_back_right, 800, weight(4.500000)|abundance(50)|weapon_length(95)|max_ammo(80)|thrust_damage(7, pierce), imodbits_missile], 

#特效箭
["power_shot_special_effect", "Power Shot Special Effect", #强力射击
   [("cw_no_head", 0), ("power_shot_flying", ixmesh_flying_ammo)], 
   itp_type_arrows|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction|itp_no_pick_up_from_ground, 0, 0, 
   weight(4.5)|abundance(1)|weapon_length(95)|max_ammo(1)|thrust_damage(35, pierce), 
   imodbits_none], 




#CROSSBOW
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["crossbow_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######STEPPE CROSSBOW#########
["steppe_crossbow", "Steppe Crossbow", [("crossbow_c", 0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 503, weight(2.750000)|abundance(100)|difficulty(9)|accuracy(65)|spd_rtng(49)|shoot_speed(65)|max_ammo(1)|thrust_damage(64, cut)|weapon_length(0), imodbits_crossbow], 


#######CONFEDERATION CROSSBOW#########
["blowgun", "Blowgun", #吹箭筒
   [("blowgun", 0)], 
   itp_type_crossbow|itp_merchandise|itp_primary, 
   itcf_shoot_crossbow|itcf_carry_crossbow_back, 271, 
   weight(1.75)|abundance(30)|difficulty(18)|accuracy(0)|spd_rtng(46)|shoot_speed(40)|max_ammo(1)|thrust_damage(30, cut)|weapon_length(0), 
   imodbits_crossbow], 
["poison_blowgun", "Poison Blowgun", #毒吹箭筒
   [("poison_blowgun", 0)], 
   itp_type_crossbow|itp_primary, 
   itcf_shoot_crossbow|itcf_carry_crossbow_back, 2311, 
   weight(1.75)|abundance(5)|difficulty(19)|accuracy(0)|spd_rtng(46)|shoot_speed(40)|max_ammo(1)|thrust_damage(32, cut)|weapon_length(0), 
   imodbits_crossbow, [
    (ti_on_weapon_attack, [
        (store_random_in_range, ":count_no", 0, 5),#五分之一概率
        (eq, ":count_no", 3),
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),

        (set_fixed_point_multiplier, 100),
        (agent_get_bone_position, pos1, ":attacker_agent_no", hb_item_r, 1),#右手武器处
        (agent_get_position, pos2, ":attacker_agent_no"),
        (call_script, "script_pos_copy_rotation_from_pos", pos1, pos2),#复制旋转角
        (position_move_y, pos1, -30),
        (copy_position, pos2, pos1),#向前射击
        (position_move_y, pos2, 10),
        (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
        (add_missile, ":attacker_agent_no", pos1, 1000, "itm_poison_blowgun", 0, "itm_weak_toxin_liquid", 0),#发射弱毒液
    ]),
    (ti_on_weapon_attack, [
        (key_is_down, key_e),#武器特技键按下
        (store_trigger_param_1, ":attacker_agent_no"),
        (agent_is_human, ":attacker_agent_no"),#是人
        (agent_is_alive, ":attacker_agent_no"),
        (neg|agent_is_non_player, ":attacker_agent_no"),#是玩家
        (call_script, "script_cf_close_combat_technique", ":attacker_agent_no", "itm_active_release_toxin_fog"),#释放毒雾
    ]),
]],


#######EASTERN CROSSBOW#########
["dongfang_nu", "dongfang_nu", [("liannu", 0)], itp_type_crossbow|itp_merchandise|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 4683, weight(3.750000)|abundance(100)|difficulty(10)|accuracy(70)|spd_rtng(67)|shoot_speed(99)|max_ammo(10)|thrust_damage(82, cut)|weapon_length(0), imodbits_crossbow], 


#######STATE CROSSBOW#########
#步弩
["sanbing_nu", "sanbing_nu", [("crossbow_h4", 0)], itp_type_crossbow|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 7000, weight(3.500000)|abundance(10)|difficulty(12)|accuracy(90)|spd_rtng(40)|shoot_speed(75)|max_ammo(10)|thrust_damage(88, cut)|weapon_length(0), imodbits_crossbow], 
["baolei_tiebinu", "baolei_tiebinu", [("arbalest_h4", 0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_extra_penetration, itcf_shoot_crossbow|itcf_carry_crossbow_back, 8000, weight(5.500000)|abundance(10)|difficulty(20)|accuracy(93)|spd_rtng(50)|shoot_speed(85)|max_ammo(7)|thrust_damage(95, cut)|weapon_length(0), imodbits_crossbow], 
["winch_crossbow", "Winch Crossbow", [("spak_crsb02", 0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_extra_penetration, itcf_shoot_crossbow|itcf_carry_crossbow_back, 12355, weight(8.000000)|abundance(3)|difficulty(24)|accuracy(92)|spd_rtng(60)|shoot_speed(48)|max_ammo(1)|thrust_damage(81, pierce)|weapon_length(0), imodbits_crossbow], 

#骑弩
["jiqiao_nu", "jiqiao_nu", [("van_helsing_crossbow_01", 0), ("van_helsing_crossbow_scabbard", ixmesh_carry)], itp_type_crossbow|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 10000, weight(3.500000)|abundance(5)|difficulty(20)|accuracy(90)|spd_rtng(50)|shoot_speed(85)|max_ammo(7)|thrust_damage(85, cut)|weapon_length(0), imodbits_crossbow], 


#######WITCHCRAFT CROSSBOW#########
["shexie_nu", "shexie_nu", [("txz_weapon_a03_06", 0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 7394, weight(2.750000)|abundance(10)|difficulty(15)|accuracy(95)|spd_rtng(75)|shoot_speed(85)|max_ammo(2)|thrust_damage(65, pierce)|weapon_length(0), imodbits_crossbow], 


#######COMMON CROSSBOW#########
#骑弩
["hunting_crossbow", "Hunting_Crossbow", [("crossbow_a", 0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 221, weight(2.250000)|abundance(10)|difficulty(6)|accuracy(87)|spd_rtng(47)|shoot_speed(60)|max_ammo(1)|thrust_damage(50, cut)|weapon_length(0), imodbits_crossbow], 
["light_crossbow", "Light_Crossbow", [("crossbow_b", 0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1365, weight(2.500000)|abundance(10)|difficulty(10)|accuracy(87)|spd_rtng(45)|shoot_speed(70)|max_ammo(1)|thrust_damage(60, cut)|weapon_length(0), imodbits_crossbow], 
["birch_crossbow", "Birch Crossbow", [("light_crossbow_h4", 0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 3065, weight(2.500000)|abundance(20)|difficulty(15)|accuracy(88)|spd_rtng(55)|shoot_speed(78)|max_ammo(1)|thrust_damage(66, cut)|weapon_length(0), imodbits_crossbow], 
["lightweight_winch_crossbow", "Lightweight Winch Crossbow", [("spak_crsb02_small", 0)], itp_type_crossbow|itp_merchandise|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 4355, weight(3.000000)|abundance(5)|difficulty(15)|accuracy(89)|spd_rtng(82)|shoot_speed(68)|max_ammo(1)|thrust_damage(71, cut)|weapon_length(0), imodbits_crossbow], 
["guizu_qinnu", "guizu_qinnu", [("heavy_crossbow_h4", 0)], itp_type_crossbow|itp_merchandise|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 5355, weight(2.000000)|abundance(5)|difficulty(16)|accuracy(90)|spd_rtng(85)|shoot_speed(65)|max_ammo(1)|thrust_damage(75, cut)|weapon_length(0), imodbits_crossbow], 

["assassination_sniper_crossbow", "Assassination Sniper Crossbow", [("mortis_crossbow", 0), ("mortis_crossbow_close", ixmesh_carry)], itp_type_crossbow|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 8355, weight(3.000000)|abundance(10)|difficulty(16)|accuracy(99)|spd_rtng(15)|shoot_speed(80)|max_ammo(1)|thrust_damage(100, pierce)|weapon_length(0), imodbits_crossbow], 
["assassination_crossbow", "Assassination Crossbow", [("mortis_crossbow_small", 0), ("mortis_crossbow_small_close", ixmesh_carry)], itp_type_crossbow|itp_primary|itp_bonus_against_shield, itcf_shoot_pistol|itcf_carry_crossbow_back, 8355, weight(2.500000)|abundance(10)|difficulty(16)|accuracy(99)|spd_rtng(95)|shoot_speed(80)|max_ammo(9)|thrust_damage(53, pierce)|weapon_length(0), imodbits_crossbow], 
["sniper_crossbow", "Sniper Crossbow", #狙击步弩
   [("hejin_nu", 0)], 
   itp_type_crossbow|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 28355, 
   weight(5)|abundance(10)|difficulty(16)|accuracy(99)|spd_rtng(55)|shoot_speed(99)|max_ammo(1)|thrust_damage(110, pierce)|weapon_length(0), 
   imodbits_crossbow], 

#步弩
["crossbow", "Crossbow", [("crossbow_a", 0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 987, weight(3.000000)|abundance(10)|difficulty(12)|accuracy(86)|spd_rtng(43)|shoot_speed(75)|max_ammo(1)|thrust_damage(70, cut)|weapon_length(0), imodbits_crossbow], 
["heavy_crossbow", "Heavy_Crossbow", [("crossbow_c", 0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1460, weight(3.500000)|abundance(10)|difficulty(15)|accuracy(86)|spd_rtng(41)|shoot_speed(75)|max_ammo(1)|thrust_damage(80, cut)|weapon_length(0), imodbits_crossbow], 
["oak_corssbow", "Oak Corssbow", [("hunting_crossbow_h4", 0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 3965, weight(3.000000)|abundance(20)|difficulty(17)|accuracy(88)|spd_rtng(45)|shoot_speed(80)|max_ammo(1)|thrust_damage(83, cut)|weapon_length(0), imodbits_crossbow], 
["tiegu_nu", "tiegu_nu", [("xenoargh_arbalest", 0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 6965, weight(4.750000)|abundance(10)|difficulty(19)|accuracy(89)|spd_rtng(41)|shoot_speed(85)|max_ammo(2)|thrust_damage(90, cut)|weapon_length(0), imodbits_crossbow], 





#CROSSBOW BOLT
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["bolt_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######CONFEDERATION WEAPON#########
["blowgun_arrow", "Blowgun Arrow", #吹箭镖
   [("blowgun_arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("blowgun_arrow_carry", ixmesh_carry), ("blowgun_arrow_carry", ixmesh_inventory)], 
   itp_type_bolts|itp_merchandise, 
   itcf_carry_quiver_right_vertical, 100, 
   weight(0.5)|abundance(10)|weapon_length(5)|max_ammo(60)|thrust_damage(0, pierce), 
   imodbits_missile], 

#######PAPAL WEAPON#########
["silver_bolts", "Silver Steel Bolts", #镀银弩矢
   [("van_helsing_crossbow_bolt_silver", 0), ("van_helsing_crossbow_bolt_silver_fly", ixmesh_flying_ammo), ("van_helsing_crossbow_bolt_bag", ixmesh_carry)], 
   itp_type_bolts|itp_can_penetrate_shield|itp_bonus_against_shield, 
   itcf_carry_quiver_right_vertical, 4800, 
   weight(2.55)|abundance(25)|weapon_length(25)|max_ammo(28)|thrust_damage(8, pierce), 
   imodbits_missile], 

#######GRAGHITE STEEL WEAPON#########
["graghite_steel_bolts", "Graghite Steel Bolts", #墨钢弩矢
   [("van_helsing_crossbow_bolt", 0), ("van_helsing_crossbow_bolt_fly", ixmesh_flying_ammo), ("van_helsing_crossbow_bolt_bag", ixmesh_carry)], 
   itp_type_bolts|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 
   itcf_carry_quiver_right_vertical, 5000, 
   weight(2.6)|abundance(1)|weapon_length(25)|max_ammo(30)|thrust_damage(10, pierce), 
   imodbits_missile], 


#######COMMON BOLT#########
["bolts", "Bolts", #弩矢
   [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag", ixmesh_carry), ("bolt_bag_b", 3458768911867052032)], 
   itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, 
   itcf_carry_quiver_right_vertical, 60, 
   weight(2.25)|abundance(90)|weapon_length(63)|max_ammo(60)|thrust_damage(3, cut), 
   imodbits_missile], 
["steel_bolts", "Steel Bolts", #钢弩矢
   [("bolt", 0), ("flying_missile", ixmesh_flying_ammo), ("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 
   itcf_carry_quiver_right_vertical, 200, 
   weight(2.5)|abundance(20)|weapon_length(63)|max_ammo(56)|thrust_damage(5, cut), 
   imodbits_missile], 
["heiyu_nushi", "heiyu_nushi", [("bolts_h3", 0), ("bolts_flying_h3", ixmesh_flying_ammo), ("bolts_quiver_h3", ixmesh_carry), ("bolts_quiver_h3.1", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_quiver_right_vertical, 950, weight(2.600000)|abundance(30)|weapon_length(25)|max_ammo(34)|thrust_damage(7, pierce), imodbits_missile], 
["hongyu_nushi", "hongyu_nushi", [("bolts_h4", 0), ("bolts_flying_h4", ixmesh_flying_ammo), ("bolts_quiver_h4", ixmesh_carry), ("bolts_quiver_h4.1", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_quiver_right_vertical, 950, weight(2.600000)|abundance(30)|weapon_length(25)|max_ammo(35)|thrust_damage(7, pierce), imodbits_missile], 
["baiyu_nushi", "baiyu_nushi", [("steel_bolts_h3", 0), ("steel_bolts_flying_h3", ixmesh_flying_ammo), ("steel_bolts_quiver_h3", ixmesh_carry), ("steel_bolts_quiver_h3.1", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_quiver_right_vertical, 950, weight(2.600000)|abundance(30)|weapon_length(25)|max_ammo(33)|thrust_damage(7, pierce), imodbits_missile], 
["heibaiyu_nushi", "heibaiyu_nushi", [("steel_bolts_h4", 0), ("steel_bolts_flying_h4", ixmesh_flying_ammo), ("steel_bolts_quiver_h4", ixmesh_carry), ("steel_bolts_quiver_h4.1", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_quiver_right_vertical, 950, weight(2.600000)|abundance(30)|weapon_length(25)|max_ammo(35)|thrust_damage(7, pierce), imodbits_missile], 




#FIREARM
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["firearm_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["flintlock_pistol", "Flintlock Pistol", #早期魔导火枪
   [("flintlock_pistol", 0)], 
   itp_type_pistol|itp_merchandise|itp_primary, 481036795904, 7300, 
   weight(1.5)|abundance(1)|difficulty(0)|accuracy(88)|spd_rtng(32)|shoot_speed(125)|max_ammo(2)|thrust_damage(80, pierce)|weapon_length(0), 
   imodbits_none, [
    (ti_on_weapon_attack, [
        (store_trigger_param, ":attacker_no", 1),
        (agent_get_ammo, ":ammo_number", ":attacker_no", 1),
        (gt, ":ammo_number", 0),
        (play_sound, "snd_pistol_shot"),
        (position_move_x, pos1, 27),
        (position_move_y, pos1, 36),
        (particle_system_burst, "psys_pistol_smoke", pos1, 15),
    ]),
]], 
["flintlock_pistol_elite", "Elite Flintlock Pistol", 
   [("flintlock_pistol_1", 0)], itp_type_pistol|itp_primary|itp_ignore_gravity, 483721150464, 10300, weight(1.500000)|abundance(1)|difficulty(0)|accuracy(98)|spd_rtng(48)|shoot_speed(135)|max_ammo(6)|thrust_damage(88, pierce)|weapon_length(0), imodbits_none, [
    (ti_on_weapon_attack, [
        (store_trigger_param, ":attacker_no", 1),
        (agent_get_ammo, ":ammo_number", ":attacker_no", 1),
        (gt, ":ammo_number", 0),
        (play_sound, "snd_pistol_shot"),
        (position_move_x, pos1, 27),
        (position_move_y, pos1, 36),
        (particle_system_burst, "psys_pistol_smoke", pos1, 15),
    ]),
  ]], 
["arquebus", "arquebus", [("arquebus", 0), ("arquebus", ixmesh_carry)], itp_type_musket|itp_primary|itp_bonus_against_shield|itp_ignore_gravity|itp_has_bayonet, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket|itc_musket_melee, 10062, weight(3.750000)|abundance(1)|difficulty(0)|accuracy(100)|spd_rtng(45)|shoot_speed(140)|max_ammo(3)|thrust_damage(120, pierce)|weapon_length(0), imodbits_none, [
    (ti_on_weapon_attack, [
        (store_trigger_param, ":attacker_no", 1),
        (agent_get_ammo, ":ammo_number", ":attacker_no", 1),
        (gt, ":ammo_number", 0),
        (play_sound, "snd_pistol_shot"),
        (position_move_x, pos1, 27),
        (position_move_y, pos1, 36),
        (particle_system_burst, "psys_pistol_smoke", pos1, 15),
    ]),
  ]], 




#BULLET
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["bullet_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["cartridges", "Cartridges", [("cartridge_a", 0)], itp_type_bullets|itp_default_ammo|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_ignore_gravity, 0, 41000, weight(2.250000)|abundance(1)|weapon_length(3)|max_ammo(100)|thrust_damage(50, pierce), imodbits_missile], 
["bullet_barrel", "Bullet Barrels", [("DaMing_zidantong", 0), ("huojian_fly3", ixmesh_flying_ammo)], itp_type_bullets|itp_default_ammo, 0, 41000, weight(2.250000)|abundance(1)|weapon_length(3)|max_ammo(100)|thrust_damage(50, pierce), imodbits_missile], 




#THROWING
#_______________________________________________________________________________________________________________________________________________________________________________
#Some throwing things can be used as melee weapon.
 ["throwing_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######POWELL THROWING#########
["touguan_toumao", "touguan_toumao", [("txz_weapon_a03_08", 0), ("txz_weapon_a03_08_quiver", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 36507484160, 1482, weight(4.000000)|abundance(25)|difficulty(7)|accuracy(0)|spd_rtng(85)|shoot_speed(70)|max_ammo(4)|thrust_damage(45, pierce)|weapon_length(65), imodbits_thrown], 

["fire_arrow", "Fire Arrow", #火矢
   [("cw_no_head", 0), ("sorceror", ixmesh_inventory), ("sorceror", ixmesh_flying_ammo)], 
   itp_type_thrown|itp_can_penetrate_shield|itp_no_pick_up_from_ground|itp_ignore_gravity, 
   0, 0, 
   weight(0)|abundance(1)|spd_rtng(60)|shoot_speed(60)|max_ammo(1)|thrust_damage(18, cut)|weapon_length(0), 
   imodbits_none], 

["ice_arrow", "Ice Arrow", #冰矢
   [("ice_arrow", 0)], 
   itp_type_thrown|itp_no_pick_up_from_ground, 
   0, 0, 
   weight(1)|abundance(1)|spd_rtng(60)|shoot_speed(60)|max_ammo(1)|thrust_damage(23, pierce)|weapon_length(30), 
   imodbits_none], 

["wind_blade", "Wind Blade", #风刃
   [("cw_no_head", 0), ("wind_blast_v", ixmesh_inventory), ("wind_blast_flying", ixmesh_flying_ammo)], 
   itp_type_thrown|itp_ignore_gravity|itp_ignore_friction|itp_no_pick_up_from_ground, 
   0, 0, 
   weight(0)|abundance(1)|spd_rtng(60)|shoot_speed(60)|max_ammo(1)|thrust_damage(14, blunt)|weapon_length(0), 
   imodbits_none], 
["wind_whip", "Wind Whip", #风鞭
   [("cw_no_head", 0), ("wind_blast_h", ixmesh_inventory), ("wind_blast_h", ixmesh_flying_ammo)], 
   itp_type_thrown|itp_ignore_gravity|itp_ignore_friction|itp_no_pick_up_from_ground, 
   0, 0, 
   weight(0)|abundance(1)|spd_rtng(60)|shoot_speed(60)|max_ammo(1)|thrust_damage(25, blunt)|weapon_length(0), 
   imodbits_none], 

["stone_snag", "Stone Snag", #岩刺
   [("stone_bullet", 0)], 
   itp_type_thrown|itp_no_pick_up_from_ground, 
   0, 0, 
   weight(1)|abundance(1)|spd_rtng(30)|shoot_speed(30)|max_ammo(1)|thrust_damage(23, blunt)|weapon_length(15), 
   imodbits_none], 


#######CONFEDERATION THROWING#########
["weak_toxin_liquid", "Weak Toxin Liquid", #弱毒液
   [("cw_no_head", 0), ("weak_toxin_liquid", ixmesh_inventory), ("weak_toxin_liquid_flying", ixmesh_flying_ammo)], 
   itp_type_thrown|itp_can_penetrate_shield|itp_no_pick_up_from_ground, 
   itcf_throw_stone, 600, 
   weight(3)|abundance(1)|difficulty(1)|accuracy(0)|spd_rtng(80)|shoot_speed(30)|max_ammo(30)|thrust_damage(7, blunt)|weapon_length(8), 
   imodbits_none, [
    (ti_on_missile_hit, [
        (store_trigger_param_1, ":attacker_agent_no"),
        (call_script, "script_proceed_state", ":attacker_agent_no", "itm_state_weak_toxin", 30),#使用者弱毒＋30
        (particle_system_burst, "psys_toxin_fog", pos1, 20),#烟雾特效
        (set_fixed_point_multiplier, 100),
        (try_for_agents, ":beattacked_agent_no", pos1, 100),#一米内
           (agent_is_active, ":beattacked_agent_no"),
           (agent_is_alive, ":beattacked_agent_no"),
           (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_weak_toxin", 40),#命中一米内弱毒＋40
        (try_end),
    ]),
]],  


#######PAPAL THROWING#########
["chumei_heijian", "chumei_heijian", [("heijian", 0), ("heijian_bag", ixmesh_carry), ("heijian_fly", ixmesh_flying_ammo)], itp_type_thrown|itp_primary, 2952921088, 1280, weight(5.000000)|abundance(5)|difficulty(5)|accuracy(0)|spd_rtng(119)|shoot_speed(32)|max_ammo(16)|thrust_damage(35, pierce)|weapon_length(45), imodbits_none], 


#######STARKHOOK THROWING#########
["bloodthirsty_javelin", "Bloodthirsty Javelin", #西海嗜血投枪
   [("toumao", 0), ("toumao_quiver", ixmesh_carry)], 
   itp_type_thrown|itp_primary|itp_bonus_against_shield, 
   itcf_throw_javelin|itcf_carry_quiver_back, 3800, 
   weight(6)|abundance(5)|difficulty(6)|accuracy(0)|spd_rtng(92)|shoot_speed(48)|max_ammo(9)|thrust_damage(42, pierce)|weapon_length(90), 
   imodbits_none], 
["crimson_lunar_flowing_light", "Crimson Lunar Flowing Light", #血月流光
   [("crimson_toumao", 0), ("crimson_toumao_quiver", ixmesh_carry)], 
   itp_type_thrown|itp_primary|itp_bonus_against_shield|itp_unique, 
   itcf_throw_javelin|itcf_carry_quiver_back, 15800, 
   weight(4)|abundance(1)|difficulty(4)|accuracy(0)|spd_rtng(99)|shoot_speed(68)|max_ammo(9)|thrust_damage(50, pierce)|weapon_length(90), 
   imodbits_none], 


#######DEATH THROWING#########
["rib_spear", "Rib Spear", #骨矛
   [("skeleton_spear", 0), ("skeleton_spear", ixmesh_carry)], itp_type_thrown|itp_primary|itp_next_item_as_melee, 
   36507484160, 1500, 
   weight(3)|abundance(1)|difficulty(4)|accuracy(0)|spd_rtng(91)|shoot_speed(25)|max_ammo(1)|thrust_damage(30, cut)|weapon_length(205), 
   imodbits_thrown], 
["rib_spear_melee", "Rib Spear", #骨矛
   [("skeleton_spear", 0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_couchable, 
   itc_shieldlimit_slashable_spear|itcf_carry_spear, 1500, 
   weight(3)|abundance(1)|difficulty(12)|weapon_length(205)|spd_rtng(95)|swing_damage(22, cut)|thrust_damage(36, pierce), 
   imodbits_polearm], 
["spectre", "Spectre", #屑灵
   [("cw_no_head", 0), ("barf_skull_ghost", ixmesh_inventory), ("barf_skull_ghost", ixmesh_flying_ammo)], 
   itp_type_thrown|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_ignore_gravity|itp_ignore_friction|itp_no_pick_up_from_ground, 
   0, 6000, 
   weight(0)|abundance(1)|spd_rtng(100)|shoot_speed(25)|max_ammo(1)|thrust_damage(30, blunt)|weapon_length(55), 
   imodbits_none], 


#######CHAOS THROWING#########
["shichumei", "shichumei", [("stones_h4", 0), ("stones_h4", ixmesh_carry)], itp_type_thrown|itp_primary, 805371904, 100000, weight(4.000000)|abundance(1)|difficulty(15)|accuracy(0)|spd_rtng(66)|shoot_speed(50)|max_ammo(6)|thrust_damage(40, blunt)|weapon_length(8), imodbits_none], 


#######DEATHBELL THROWING#########
["zhanzheng_feiren", "zhanzheng_feiren", [("4point_shuriken_h4", 0)], itp_type_thrown|itp_unique|itp_primary, 131072, 30000, weight(0.250000)|abundance(1)|difficulty(10)|accuracy(0)|spd_rtng(121)|shoot_speed(30)|max_ammo(1000000)|thrust_damage(46, pierce)|weapon_length(0), imodbits_none, [
    (ti_on_missile_hit, [
        (store_trigger_param_1, ":hit_position"),
        (agent_set_position, ":hit_position", pos1),
    ]),
]], 
["qizhi_feidao", "qizhi_feidao", [("6point_shuriken_h4", 0)], itp_type_thrown|itp_unique|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 131072, 30000, weight(0.250000)|abundance(1)|difficulty(10)|accuracy(0)|spd_rtng(131)|shoot_speed(30)|max_ammo(100000)|thrust_damage(49, cut)|weapon_length(0), imodbits_none, [
    (ti_on_missile_hit, [
        (store_trigger_param_1, ":hit_position"),
        (agent_set_position, ":hit_position", pos1),
    ]),
]], 
["sizhong", "sizhong", [("snowflake_h4", 0)], itp_type_thrown|itp_unique|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 131072, 30000, weight(0.250000)|abundance(1)|difficulty(10)|accuracy(0)|spd_rtng(110)|shoot_speed(37)|max_ammo(100000)|thrust_damage(50, pierce)|weapon_length(0), imodbits_none, [
    (ti_on_missile_hit, [
        (store_trigger_param_1, ":hit_position"),
        (agent_set_position, ":hit_position", pos1),
    ]),
]], 
["jinshi_zhanbiao", "jinshi_zhanbiao", [("war_darts_h4", 0), ("war_darts_quiver_h4", ixmesh_carry), ("war_darts_quiver_h4.1", ixmesh_carry)], itp_type_thrown|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, 2147745792, 1301, weight(3.000000)|abundance(20)|difficulty(5)|accuracy(0)|spd_rtng(91)|shoot_speed(15)|max_ammo(10)|thrust_damage(40, cut)|weapon_length(36), imodbits_thrown_minus_heavy], 


#######GILDING WEAPON#########
["jinshi_feidao", "jinshi_feidao", [("throwing_knives_h4", 0)], itp_type_thrown|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_extra_penetration, 131072, 870, weight(2.500000)|abundance(20)|difficulty(4)|accuracy(0)|spd_rtng(121)|shoot_speed(25)|max_ammo(28)|thrust_damage(34, cut)|weapon_length(10), imodbits_thrown_minus_heavy], 
["jinshi_toumao", "jinshi_toumao", [("throwing_spear_h4", 0), ("throwing_spear_quiver_h4", ixmesh_carry), ("throwing_spear_quiver_h4.1", ixmesh_carry)], itp_type_thrown|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, 2147745792, 1262, weight(3.750000)|abundance(10)|difficulty(5)|accuracy(0)|spd_rtng(90)|shoot_speed(33)|max_ammo(10)|thrust_damage(40, pierce)|weapon_length(65), imodbits_thrown_minus_heavy], 
["jinshi_touqiang", "jinshi_touqiang", [("jarid_h4", 0), ("jarid_quiver_h4", ixmesh_carry), ("jarid_quiver_h4.1", ixmesh_carry)], itp_type_thrown|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, 2147745792, 1282, weight(4.000000)|abundance(10)|difficulty(5)|accuracy(0)|spd_rtng(85)|shoot_speed(45)|max_ammo(9)|thrust_damage(42, pierce)|weapon_length(75), imodbits_thrown], 
["jinshi_feishui", "jinshi_feishui", [("throwing_hammer_h4", 0)], itp_type_thrown|itp_primary|itp_bonus_against_shield, 196608, 2362, weight(5.000000)|abundance(10)|difficulty(6)|accuracy(0)|spd_rtng(110)|shoot_speed(12)|max_ammo(8)|thrust_damage(35, blunt)|weapon_length(53), imodbits_thrown], 


#######COMMON WEAPON#########
#Junk Throwings
["stones", "Stones", [("throwing_stone", 0)], itp_type_thrown|itp_merchandise|itp_primary, 65536, 1, weight(4.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(97)|shoot_speed(30)|max_ammo(36)|thrust_damage(11, blunt)|weapon_length(8), imodbit_large_bag], 

#Throwing Knifes
["throwing_knives", "Throwing_Knives", [("throwing_knife", 0)], itp_type_thrown|itp_merchandise|itp_primary, 131072, 76, weight(3.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(121)|shoot_speed(25)|max_ammo(28)|thrust_damage(19, cut)|weapon_length(0), imodbits_thrown], 
["throwing_daggers", "Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_merchandise|itp_primary, 131072, 193, weight(3.500000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(110)|shoot_speed(24)|max_ammo(26)|thrust_damage(25, cut)|weapon_length(0), imodbits_thrown], 

#Javelins
["darts", "Darts", [("dart_b", 0), ("dart_b_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary, 36239048704, 155, weight(2.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(95)|shoot_speed(42)|max_ammo(15)|thrust_damage(28, cut)|weapon_length(32), imodbits_thrown], 
["war_darts", "War_Darts", [("dart_a", 0), ("dart_a_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary, 36507484160, 280, weight(2.350000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(93)|shoot_speed(30)|max_ammo(12)|thrust_damage(35, cut)|weapon_length(45), imodbits_thrown], 

["javelin", "Javelins", [("javelin", 0), ("javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, 36507484160, 300, weight(5.000000)|abundance(100)|difficulty(2)|accuracy(0)|spd_rtng(91)|shoot_speed(25)|max_ammo(5)|thrust_damage(27, cut)|weapon_length(75), imodbits_thrown], 
["javelin_melee", "Javelin", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary, 4222124851990272, 300, weight(1.000000)|abundance(100)|difficulty(0)|weapon_length(75)|spd_rtng(95)|swing_damage(12, cut)|thrust_damage(14, pierce), imodbits_polearm], 

["throwing_spears", "Throwing_Spears", [("jarid_new_b", 0), ("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, 36507484160, 262, weight(3.000000)|abundance(100)|difficulty(2)|accuracy(0)|spd_rtng(90)|shoot_speed(29)|max_ammo(4)|thrust_damage(44, cut)|weapon_length(65), imodbits_thrown], 
["throwing_spear_melee", "Throwing_Spear", [("jarid_new_b", 0), ("javelins_quiver", ixmesh_carry)], itp_type_polearm|itp_wooden_parry|itp_primary, 4222124851990272, 262, weight(1.000000)|abundance(100)|difficulty(1)|weapon_length(75)|spd_rtng(91)|swing_damage(18, cut)|thrust_damage(23, pierce), imodbits_thrown], 

["jarid", "Jarids", [("jarid_new", 0), ("jarid_quiver", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, 36507484160, 282, weight(4.000000)|abundance(100)|difficulty(2)|accuracy(0)|spd_rtng(89)|shoot_speed(30)|max_ammo(4)|thrust_damage(45, cut)|weapon_length(65), imodbits_thrown], 
["jarid_melee", "Jarid", [("jarid_new", 0), ("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_wooden_parry|itp_primary, 4222124851990272, 282, weight(1.000000)|abundance(100)|difficulty(2)|weapon_length(65)|spd_rtng(93)|swing_damage(16, cut)|thrust_damage(20, pierce), imodbits_thrown], 

#Throwing Axes
["light_throwing_axes", "Light_Throwing_Axes", [("francisca", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, 196608, 360, weight(5.000000)|abundance(100)|difficulty(2)|accuracy(0)|spd_rtng(99)|shoot_speed(18)|max_ammo(4)|thrust_damage(35, cut)|weapon_length(53), imodbits_thrown_minus_heavy], 
["light_throwing_axes_melee", "Light_Throwing_Axe", [("francisca", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 9223388529554358286, 360, weight(1.000000)|abundance(100)|difficulty(2)|weapon_length(53)|spd_rtng(99)|swing_damage(26, cut)|thrust_damage(0, cut), imodbits_thrown_minus_heavy], 

["throwing_axes", "Throwing_Axes", [("throwing_axe_a", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, 196608, 490, weight(5.000000)|abundance(100)|difficulty(3)|accuracy(0)|spd_rtng(98)|shoot_speed(18)|max_ammo(4)|thrust_damage(39, cut)|weapon_length(53), imodbits_thrown_minus_heavy], 
["throwing_axes_melee", "Throwing_Axe", [("throwing_axe_a", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 9223388529554358286, 490, weight(1.000000)|abundance(100)|difficulty(3)|weapon_length(53)|spd_rtng(98)|swing_damage(29, cut)|thrust_damage(0, cut), imodbits_thrown_minus_heavy], 

["heavy_throwing_axes", "Heavy_Throwing_Axes", [("throwing_axe_b", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, 196608, 620, weight(5.000000)|abundance(100)|difficulty(4)|accuracy(0)|spd_rtng(97)|shoot_speed(18)|max_ammo(4)|thrust_damage(44, cut)|weapon_length(53), imodbits_thrown_minus_heavy], 
["heavy_throwing_axes_melee", "Heavy_Throwing_Axe", [("throwing_axe_b", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 9223388529554358286, 620, weight(1.000000)|abundance(100)|difficulty(4)|weapon_length(53)|spd_rtng(97)|swing_damage(32, cut)|thrust_damage(0, cut), imodbits_thrown_minus_heavy],




#HORSE
#_______________________________________________________________________________________________________________________________________________________________________________
#basic status         value         hp        difficulty     body_armor      speed     maneuver      scale      charge    abundance
#steppe horse        832         200            2                  30                  50              39              110          36             80
#desert horse         850         225            2                  33                  48              44              112          32             80
#plain horse           800         210            2                  27                  49              44              106          33             80
#mountain horse   820         230            2                  29                  45              54               95           28             80
#hunter horse       1310        260            3                  27                  52              44              108          24             60
#dragonblood       3105        420            4                  40                  52              30              118          45             30
#spiritual horse     4983        500            5                  50                  65              38              100          50             10
#demon horse      4983        600            6                  49                  45              39              108          42              5

#leather armor     +1130        0              0                 +25                 -5              -5                0             0              -40
#chain armor        +3000        0             +2               +45                 -8               0                 0             0             -40
#ligature armor    +2662        0             +2               +38                -10               0                0             0             -40
#plate mail armor +3968        0             +2               +47                -14             +5               0             0             -60
#plate armor         +4936        0             +4               +60                -17              0                0             0             -10
#full plate armor   +5946        0             +4               +90                -22              0                0             0             -20
 ["horse_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#######RIDEABLE MONSTER#########
#Special Creature
["great_lizard", "Great Lizard", #无甲骑龙
   [("Dark_Basilisk_2", 0)], 
   itp_type_horse|itp_merchandise, 0, 7500, 
   abundance(20)|difficulty(7)|hit_points(1000)|body_armor(28)|horse_speed(35)|horse_maneuver(10)|horse_charge(42)|horse_scale(140), 
   imodbits_horse_basic|imodbit_champion], 
["armed_great_lizard", "Armed Great Lizard", #披甲骑龙
   [("dark_basilisk", 0)], 
   itp_type_horse|itp_merchandise, 0, 12000, 
   abundance(15)|difficulty(7)|hit_points(1000)|body_armor(40)|horse_speed(25)|horse_maneuver(10)|horse_charge(42)|horse_scale(140), 
   imodbits_horse_basic|imodbit_champion], 

["unicorn", "Unicorn", #独角兽
   [("unicorn", 0)], 
   itp_type_horse, 0, 10000, 
   abundance(1)|difficulty(7)|hit_points(900)|body_armor(50)|horse_speed(70)|horse_maneuver(56)|horse_charge(60)|horse_scale(112), 
   imodbits_horse_basic|imodbit_champion], 
["leather_armor_unicorn", "Leather Armor Unicorn", #皮甲罩袍独角兽
   [("leather_armor_unicorn", 0)], 
   itp_type_horse, 0, 11500, 
   abundance(1)|difficulty(7)|hit_points(900)|body_armor(75)|horse_speed(65)|horse_maneuver(56)|horse_charge(60)|horse_scale(112), 
   imodbits_horse_basic|imodbit_champion], 
["full_armor_unicorn", "Full Armor Unicorn", #重装独角兽
   [("full_armor_unicorn", 0)], 
   itp_type_horse, 0, 16000, 
   abundance(1)|difficulty(11)|hit_points(900)|body_armor(130)|horse_speed(61)|horse_maneuver(56)|horse_charge(60)|horse_scale(112), 
   imodbits_horse_basic|imodbit_champion], 

["spider", "Spider", [("spider", 0)], #魔蛛
   itp_type_horse|itp_merchandise, 0, 37000, 
   abundance(1)|difficulty(6)|hit_points(2300)|body_armor(42)|horse_speed(64)|horse_maneuver(15)|horse_charge(65)|horse_scale(115), 
   imodbits_horse_basic|imodbit_champion], 
["febrilagma_beast", "Febrilagma Beast", #浊热病怪兽
   [("rongyang", 0)], 
   itp_type_horse|itp_merchandise, 0, 50000, 
   abundance(1)|difficulty(7)|hit_points(3000)|body_armor(90)|horse_speed(44)|horse_maneuver(35)|horse_charge(110)|horse_scale(110), 
   imodbits_horse_basic|imodbit_champion], 

["demon_sheep_horn_horse", "Demon Sheep Horn Horse", #恶魔羊角马
   [("arhar_armor_light", 0)], 
   itp_type_horse|itp_merchandise, 0, 17000, 
   abundance(1)|difficulty(8)|hit_points(900)|body_armor(80)|horse_speed(68)|horse_maneuver(50)|horse_charge(57)|horse_scale(130), 
   imodbits_none], 
["golden_demon_sheep_horn_horse", "Golden Demon Sheep Horn Horse", #金饰恶魔羊角马
   [("arhar_armor", 0)], 
   itp_type_horse|itp_merchandise, 0, 17000, 
   abundance(1)|difficulty(9)|hit_points(900)|body_armor(120)|horse_speed(58)|horse_maneuver(50)|horse_charge(57)|horse_scale(130), 
   imodbits_none], 

#Camel
["luotuo", "luotuo", [("camel", 0)], itp_type_horse|itp_merchandise, 0, 1011, abundance(40)|difficulty(4)|hit_points(365)|body_armor(35)|horse_speed(36)|horse_maneuver(32)|horse_charge(15)|horse_scale(120), imodbits_horse_basic], 

#Demon Horse
["demon_horse", "demon_horse", [("DM_snouz_horse_d_01_demon", 0)], itp_type_horse, 0, 14000, abundance(5)|difficulty(6)|hit_points(600)|body_armor(49)|horse_speed(45)|horse_maneuver(39)|horse_charge(42)|horse_scale(108), imodbits_horse_basic|imodbit_champion], 
["anhei_qingshi_moshouma1", "anhei_qingshi_moshouma1", [("Annu_horse", 0)], itp_type_horse, 0, 42000, abundance(1)|difficulty(8)|hit_points(700)|body_armor(120)|horse_speed(78)|horse_maneuver(38)|horse_charge(65)|horse_scale(112), imodbits_horse_basic|imodbit_champion], 
["anhei_qingshi_moshouma", "anhei_qingshi_moshouma", [("charger_dark", 0)], itp_type_horse, 0, 21000, abundance(5)|difficulty(7)|hit_points(600)|body_armor(110)|horse_speed(37)|horse_maneuver(39)|horse_charge(53)|horse_scale(108), imodbits_horse_basic|imodbit_champion], 
["horn_dark_warhorse", "horn_dark_warhorse", [("DM_dark_charger_c2", 0)], itp_type_horse, 0, 21500, abundance(5)|difficulty(7)|hit_points(600)|body_armor(110)|horse_speed(37)|horse_maneuver(39)|horse_charge(61)|horse_scale(108), imodbits_horse_basic|imodbit_champion], 

#Undead Horse
["necromancer_horse", "necromancer_horse", #死灵统御军马
   [("necromancer_horse", 0)], 
   itp_type_horse, 0, 12050, 
   abundance(1)|difficulty(6)|hit_points(700)|body_armor(118)|horse_speed(43)|horse_maneuver(46)|horse_charge(46)|horse_scale(105), 
   imodbits_none], 

["jiangshi_ma", "jiangshi_ma", [("zombie_horse", 0)], itp_type_horse, 0, 2050, abundance(1)|difficulty(5)|hit_points(400)|body_armor(63)|horse_speed(36)|horse_maneuver(40)|horse_charge(40)|horse_scale(112), imodbits_none], 
["jiangshi_charger", "jiangshi_charger", [("armored_zombie_warhorse", 0)], itp_type_horse, 0, 4350, abundance(1)|difficulty(5)|hit_points(200)|body_armor(85)|horse_speed(52)|horse_maneuver(40)|horse_charge(40)|horse_scale(112), imodbits_none], 
["zhongjia_jiangshi_ma", "zhongjia_jiangshi_ma", [("armored_zombie_warhorse1", 0)], itp_type_horse, 0, 7050, abundance(1)|difficulty(6)|hit_points(200)|body_armor(110)|horse_speed(22)|horse_maneuver(40)|horse_charge(44)|horse_scale(112), imodbits_none], 
["quanjia_jiangshi_ma", "quanjia_jiangshi_ma", [("armored_zombie_warhorse2", 0)], itp_type_horse, 0, 8920, abundance(1)|difficulty(7)|hit_points(200)|body_armor(121)|horse_speed(19)|horse_maneuver(40)|horse_charge(44)|horse_scale(112), imodbits_none], 
["powell_jiangshi_ma", "powell_jiangshi_ma", [("powell_zombie_warhorse", 0)], itp_type_horse, 0, 11030, abundance(1)|difficulty(6)|hit_points(400)|body_armor(145)|horse_speed(17)|horse_maneuver(40)|horse_charge(40)|horse_scale(112), imodbits_none], 
["kouruto_jiangshi_ma", "kouruto_jiangshi_ma", [("kouruto_zombie_warhorse", 0)], itp_type_horse, 0, 9050, abundance(1)|difficulty(6)|hit_points(400)|body_armor(116)|horse_speed(21)|horse_maneuver(40)|horse_charge(40)|horse_scale(112), imodbits_none], 
["papal_jiangshi_ma", "papal_jiangshi_ma", [("papal_zombie_warhorse", 0)], itp_type_horse, 0, 11830, abundance(1)|difficulty(6)|hit_points(400)|body_armor(146)|horse_speed(17)|horse_maneuver(40)|horse_charge(40)|horse_scale(112), imodbits_none], 
["knight_jiangshi_ma", "knight_jiangshi_ma", [("knight_zombie_warhorse", 0)], itp_type_horse, 0, 11030, abundance(1)|difficulty(6)|hit_points(400)|body_armor(145)|horse_speed(17)|horse_maneuver(40)|horse_charge(40)|horse_scale(112), imodbits_none], 

["kulouma", "kulouma", [("barf_skeletal_horse", 0)], itp_type_horse, 0, 2134, abundance(1)|difficulty(5)|hit_points(800)|body_armor(26)|horse_speed(58)|horse_maneuver(45)|horse_charge(30)|horse_scale(112), imodbits_none], 
["kulouma_charger", "kulouma_charger", [("skeletal_charger", 0)], itp_type_horse, 0, 4434, abundance(1)|difficulty(6)|hit_points(800)|body_armor(36)|horse_speed(55)|horse_maneuver(45)|horse_charge(30)|horse_scale(112), imodbits_none], 
["powell_kulouma", "powell_kulouma", [("powell_skeletal_horse", 0)], itp_type_horse, 0, 5012, abundance(1)|difficulty(7)|hit_points(800)|body_armor(43)|horse_speed(53)|horse_maneuver(45)|horse_charge(30)|horse_scale(112), imodbits_none], 
["steppe_kulouma", "steppe_kulouma", [("steppe_skeletal_horse", 0)], itp_type_horse, 0, 5692, abundance(1)|difficulty(6)|hit_points(800)|body_armor(64)|horse_speed(50)|horse_maneuver(45)|horse_charge(30)|horse_scale(112), imodbits_none], 
["knight_kulouma", "knight_kulouma", [("knight_skeletal_horse", 0)], itp_type_horse, 0, 7635, abundance(1)|difficulty(7)|hit_points(800)|body_armor(82)|horse_speed(41)|horse_maneuver(45)|horse_charge(30)|horse_scale(112), imodbits_none], 
["death_kulouma", "death_kulouma", [("death_skeletal_horse", 0)], itp_type_horse, 0, 22651, abundance(1)|difficulty(8)|hit_points(1300)|body_armor(85)|horse_speed(60)|horse_maneuver(40)|horse_charge(60)|horse_scale(112), imodbits_none], 

["ghost_horse", "ghost_horse", [("ghost_horse", 0)], itp_type_horse|itp_unique, 0, 3000, abundance(1)|difficulty(2)|hit_points(80)|body_armor(0)|horse_speed(60)|horse_maneuver(50)|horse_charge(0)|horse_scale(102), imodbits_none], 
["fantom_nightmare", "fantom_nightmare", [("nightmare2", 0)], itp_type_horse|itp_unique, 0, 9000, abundance(1)|difficulty(4)|hit_points(200)|body_armor(1)|horse_speed(70)|horse_maneuver(55)|horse_charge(0)|horse_scale(114), imodbits_none], 

["walker_short_chain_warhorse_1", "walker_short_chain_warhorse", [("undead_horse_3", 0)], itp_type_horse, 0, 6000, abundance(1)|difficulty(5)|hit_points(2000)|body_armor(23)|horse_speed(38)|horse_maneuver(15)|horse_charge(30)|horse_scale(112), imodbits_none], 
["walker_short_chain_warhorse_2", "walker_short_chain_warhorse", [("undead_horse_2", 0)], itp_type_horse, 0, 6000, abundance(1)|difficulty(5)|hit_points(2000)|body_armor(23)|horse_speed(38)|horse_maneuver(15)|horse_charge(30)|horse_scale(112), imodbits_none], 
["walker_chain_warhorse", "walker_chain_warhorse", [("undead_horse_1", 0)], itp_type_horse, 0, 6500, abundance(1)|difficulty(5)|hit_points(2000)|body_armor(27)|horse_speed(37)|horse_maneuver(15)|horse_charge(30)|horse_scale(112), imodbits_none], 
["walker_full_plate_warhorse", "walker_full_plate_warhorse", [("dark_charger_a", 0)], itp_type_horse, 0, 11000, abundance(1)|difficulty(6)|hit_points(2000)|body_armor(66)|horse_speed(31)|horse_maneuver(15)|horse_charge(30)|horse_scale(112), imodbits_none], 

#根生者
["root_horse", "Root Horse", #根生马
   [("root_horse", 0)],
   itp_type_horse|itp_unique, 0, 5050, 
   abundance(1)|difficulty(3)|hit_points(700)|body_armor(43)|horse_speed(30)|horse_maneuver(30)|horse_charge(40)|horse_scale(102), 
   imodbits_none], 
["root_lizard", "Root Lizard", #根生蜥龙
   [("root_lizard", 0)], 
   itp_type_horse|itp_merchandise, 0, 9500, 
   abundance(20)|difficulty(4)|hit_points(1200)|body_armor(58)|horse_speed(25)|horse_maneuver(20)|horse_charge(42)|horse_scale(106), 
   imodbits_none], 

#绯世
["crimson_monster", "Crimson Monster", #绯红铁蹄
   [("crimson_horse", 0)],
   itp_type_horse|itp_unique, 0, 25050, 
   abundance(1)|difficulty(0)|hit_points(1000)|body_armor(43)|horse_speed(56)|horse_maneuver(70)|horse_charge(30)|horse_scale(100), 
   imodbits_none], 
["shadow_of_blood_invasion", "Shadow of Blood Invasion", #侵血之影
   [("crimson_nightmare", 0)],
   itp_type_horse|itp_unique, 0, 50500, 
   abundance(1)|difficulty(0)|hit_points(1200)|body_armor(63)|horse_speed(66)|horse_maneuver(70)|horse_charge(50)|horse_scale(107), 
   imodbits_none], 


#######DRAGONBLOOD HORSE#########
#Dragonblood Horse is a powerful breed of horse mixed with dragon blood, with extremely high endurance and courage, but also correspondingly very irritable and difficult to control. Usually used to carry heavy plate armor that ordinary horses cannot afford, it gallops on the battlefield like a tank.
#Dragonblood Horse in Plate
["heisebanjia_ma", "heisebanjia_ma", [("WPlatedCharger9", 0)], itp_type_horse|itp_merchandise, 0, 8041, abundance(20)|difficulty(6)|hit_points(420)|body_armor(100)|horse_speed(35)|horse_maneuver(30)|horse_charge(45)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 
["yinsebanjia_ma", "yinsebanjia_ma", [("WPlatedCharger2", 0)], itp_type_horse|itp_merchandise, 0, 8041, abundance(20)|difficulty(6)|hit_points(420)|body_armor(100)|horse_speed(35)|horse_maneuver(30)|horse_charge(45)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 
["hongbanjia_longxuama", "hongbanjia_longxuama", [("WPlatedCharger7", 0)], itp_type_horse|itp_merchandise, 0, 8041, abundance(20)|difficulty(6)|hit_points(420)|body_armor(100)|horse_speed(35)|horse_maneuver(30)|horse_charge(45)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 

#Dragonblood Horse in Full Plate
["hongsequanbanjia_ma", "hongsequanbanjia_ma", [("charger_plate_white", 0)], itp_type_horse|itp_merchandise, 0, 9051, abundance(10)|difficulty(6)|hit_points(420)|body_armor(130)|horse_speed(33)|horse_maneuver(30)|horse_charge(45)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 
["zongsequanbangjia_ma", "zongsequanbangjia_ma", [("charger_plate_brown", 0)], itp_type_horse|itp_merchandise, 0, 9051, abundance(10)|difficulty(6)|hit_points(420)|body_armor(130)|horse_speed(33)|horse_maneuver(30)|horse_charge(45)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 
["heisequanbangjia_ma", "heisequanbangjia_ma", [("charger_plate", 0)], itp_type_horse|itp_merchandise, 0, 9051, abundance(10)|difficulty(6)|hit_points(420)|body_armor(130)|horse_speed(33)|horse_maneuver(30)|horse_charge(45)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 

#Dragonblood Horse in Super Plate
["dark_super_dragonblood_horse", "dark_super_dragonblood_horse", [("special_horse_1", 0)], itp_type_horse|itp_merchandise, 0, 12051, abundance(5)|difficulty(7)|hit_points(420)|body_armor(160)|horse_speed(30)|horse_maneuver(30)|horse_charge(53)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 
["silver_super_dragonblood_horse", "silver_super_dragonblood_horse", [("plated_horse_5", 0)], itp_type_horse|itp_merchandise, 0, 12051, abundance(5)|difficulty(7)|hit_points(420)|body_armor(160)|horse_speed(30)|horse_maneuver(30)|horse_charge(53)|horse_scale(118), imodbits_horse_basic|imodbit_champion], 


#######EASTERN HORSE#########
["donfang_liema", "donfang_liema", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0, 1310, abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["donfang_liema2", "donfang_liema2", [("roman_horse_2", 0)], itp_type_horse|itp_merchandise, 0, 1310, abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 

#The East has a magical breed of horses called 'Silver Horses', and for some unknown reason, the blood flowing through their bodies will present a wonderful metallic color under light. After breeding and training, these horses will become strong fighting horses called "Ironblood Horses".
#Silver Horse
["xueyin_ma", "xueyin_ma", [("rus_horse", 0)], itp_type_horse|itp_merchandise, 0, 2700, abundance(20)|difficulty(4)|hit_points(270)|body_armor(33)|horse_speed(60)|horse_maneuver(50)|horse_charge(42)|horse_scale(112), imodbits_horse_basic|imodbit_champion], 
["gauizi_ma", "gauizi_ma", [("zhanma", 0)], itp_type_horse|itp_merchandise, 0, 5740, abundance(20)|difficulty(6)|hit_points(450)|body_armor(34)|horse_speed(58)|horse_maneuver(40)|horse_charge(40)|horse_scale(120), imodbits_horse_basic|imodbit_champion], 
["shenwu_ma", "shenwu_ma", [("wushuang_horse_jueying", 0)], itp_type_horse, 0, 13000, abundance(10)|difficulty(7)|hit_points(450)|body_armor(80)|horse_speed(68)|horse_maneuver(40)|horse_charge(40)|horse_scale(120), imodbits_none], 


# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger, 
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
#######INFERIOR HORSE#########
["sumpter_horse", "Sumpter_Horse", [("sumpter_horse", 0)], itp_type_horse|itp_merchandise, 0, 431, weight(0.000000)|abundance(90)|difficulty(1)|hit_points(160)|body_armor(17)|horse_speed(34)|horse_maneuver(33)|horse_charge(9)|horse_scale(100), imodbits_horse_basic], 
["saddle_horse", "Saddle_Horse", [("saddle_horse", 0), ("horse_c", 34360000512)], itp_type_horse|itp_merchandise, 0, 481, weight(0.000000)|abundance(90)|difficulty(1)|hit_points(130)|body_armor(20)|horse_speed(39)|horse_maneuver(36)|horse_charge(8)|horse_scale(100), imodbits_horse_basic], 


#######HUNTER HORSE#########
#Horse hunting is a type of horse widely used in military operations, and its source is no longer traceable. It is cultivated in various parts of the human world. This type of harness has faster speed and better protection than regular horses, and is used by various types of troops that pursue speed, such as rangers and scouts. However, hunting horses also has the disadvantage of insufficient carrying capacity and cannot be paired with overly heavy horse armor.
#Armorless Hunter
["hunter", "Hunter", [("hunting_horse", 0), ("hunting_horse", 34360000512)], itp_type_horse|itp_merchandise, 0, 1310, weight(0.000000)|abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["zase_ma", "zase_ma", [("normal_horse14", 0)], itp_type_horse|itp_merchandise, 0, 1310, abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huise_ma", "huise_ma", [("normal_horse13", 0)], itp_type_horse|itp_merchandise, 0, 1310, abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["heise_ma", "heise_ma", [("normal_horse12", 0)], itp_type_horse|itp_merchandise, 0, 1310, abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["shenseliema", "shenseliema", [("normal_horse11", 0)], itp_type_horse|itp_merchandise, 0, 1310, abundance(60)|difficulty(3)|hit_points(260)|body_armor(27)|horse_speed(52)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 

#Hunter Horse in Leather Armor
["lanbai_pijia_liema", "lanbai_pijia_liema", [("war_horse_blue", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["pitie_liema", "pitie_liema", [("WPlated4", 0)], itp_type_horse|itp_merchandise, 0, 2800, abundance(30)|difficulty(4)|hit_points(260)|body_armor(61)|horse_speed(45)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huilan_pijia_liema", "huilan_pijia_liema", [("war_horse_grey", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jinhong_pijia_liema", "jinhong_pijia_liema", [("war_horse_red", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huangbai_pijia_liema", "huangbai_pijia_liema", [("war_horse_yellow", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["zongse_pijia_liema", "zongse_pijia_liema", [("warhorse_hu2_rtw2", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["zongse_dingshi_pijia_liema", "zongse_dingshi_pijia_liema", [("warhorse_me3_rtw2", 0)], itp_type_horse|itp_merchandise, 0, 2600, abundance(40)|difficulty(3)|hit_points(260)|body_armor(57)|horse_speed(46)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion], 
["lanwen_pijia_liema", "lanwen_pijia_liema", [("caparisoned_horse_blue", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jiuhong_pijia_liema", "jiuhong_pijia_liema", [("caparisoned_horse_burgundy", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jinyang_pijia_liema", "jinyang_pijia_liema", [("caparisoned_horse_green", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["honghua_pijia_liema", "honghua_pijia_liema", [("caparisoned_horse_red", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["baijin_pijia_liema", "baijin_pijia_liema", [("caparisoned_horse_white", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["linjia_pijia_liema", "linjia_pijia_liema", [("caparisoned_horse_yellow", 0)], itp_type_horse|itp_merchandise, 0, 3600, abundance(20)|difficulty(4)|hit_points(260)|body_armor(68)|horse_speed(42)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongbai_pijia_liema", "hongbai_pijia_liema", [("charger_x_maw", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["yanghua_pijia_liema", "yanghua_pijia_liema", [("aqs_horse2", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lvyipijia_ma", "lvyipijia_ma", [("new_horse_1", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongyipijia_ma", "hongyipijia_ma", [("new_horse_10", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["baiyipijia_ma", "baiyipijia_ma", [("new_horse_11", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongheipijia_ma", "hongheipijia_ma", [("new_horse_2", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(52)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["heiyipijia_ma", "heiyipijia_ma", [("new_horse_3", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lanyipijia_ma", "lanyipijia_ma", [("new_horse_4", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huangyipijia_ma", "huangyipijia_ma", [("new_horse_5", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["chenyipijia_ma", "chenyipijia_ma", [("new_horse_6", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huangshizipijia_ma", "huangshizipijia_ma", [("new_horse_7", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huanghiepijia_ma", "huanghiepijia_ma", [("new_horse_8", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(47)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["heibaitiaopijia_ma", "heibaitiaopijia_ma", [("new_horse_9", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(522)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["shiwenpijia_ma", "shiwenpijia_ma", [("new_horse_cas", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jinhongpijia_ma", "jinhongpijia_ma", [("new_horse_eng", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jinhuapijia_ma", "jinhuapijia_ma", [("new_horse_fra", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lanlvshipijia_ma", "lanlvshipijia_ma", [("new_horse_gal", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jinyinpijia_ma", "jinyinpijia_ma", [("new_horse_ger", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["baishizipijia_ma", "baishizipijia_ma", [("new_horse_hos", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongbaipijia_ma", "hongbaipijia_ma", [("new_horse_hun", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lvqinpijia_ma", "lvqinpijia_ma", [("new_horse_ire", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["jinshizi_ma", "jinshizi_ma", [("new_horse_jer", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lanjinpijia_ma", "lanjinpijia_ma", [("new_horse_kiv", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["shifupijia_ma", "shifupijia_ma", [("new_horse_nor", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["qinlvpijia_ma", "qinlvpijia_ma", [("new_horse_nov", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongbaiyinpijia_ma", "hongbaiyinpijia_ma", [("new_horse_pol", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lanshizipijia_ma", "lanshizipijia_ma", [("new_horse_por", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["lanhuangyingpijia_ma", "lanhuangyingpijia_ma", [("new_horse_sco", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["languanpijia_ma", "languanpijia_ma", [("new_horse_swe", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongshizipijia_ma", "hongshizipijia_ma", [("new_horse_tem", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huanglvwenpijia_ma", "huanglvwenpijia_ma", [("new_horse_den", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["huangyingpijia_ma", "huangyingpijia_ma", [("new_horse_sic", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["hongbaishipijia_ma", "hongbaishipijia_ma", [("new_horse_leo", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["honghuangwenpijia_ma", "honghuangwenpijia_ma", [("new_horse_ara", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["heishizipijia_ma", "heishizipijia_ma", [("heraldic_horse_3", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 
["kelutuo_pijia_liema", "kelutuo_pijia_liema", [("aqs_horse4", 0)], itp_type_horse|itp_merchandise, 0, 2440, abundance(40)|difficulty(3)|hit_points(260)|body_armor(52)|horse_speed(47)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 

#Hunter Horse in Simple Plate Mail Armor
["pilianjai_liema", "pilianjai_liema", [("war_horse_brown", 0)], itp_type_horse|itp_merchandise, 0, 3240, abundance(20)|difficulty(4)|hit_points(260)|body_armor(65)|horse_speed(43)|horse_maneuver(39)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 

#Hunter Horse in Ligature Armor
["tiesezhajia_liema", "tiesezhajia_liema", [("lamellar_armor_horse_2", 0)], itp_type_horse|itp_merchandise, 0, 4540, abundance(30)|difficulty(4)|hit_points(260)|body_armor(75)|horse_speed(38)|horse_maneuver(39)|horse_charge(33)|horse_scale(108), imodbits_horse_basic], 

#Hunter Horse in Full Armor
["full_armor_hunter_horse", "full_armor_hunter_horse", [("aqs_horse1_cape", 0)], itp_type_horse|itp_merchandise, 0, 7810, abundance(20)|difficulty(5)|hit_points(260)|body_armor(107)|horse_speed(30)|horse_maneuver(39)|horse_charge(50)|horse_scale(108), imodbits_horse_basic], 


#######STEPPE HORSE#########
#The official name of Steppe horse is Kouruto Shob horse, which was bred by the Kouruto people and has a higher body size and faster speed compared to other ordinary horses.
#Armorless Steppe Horse
["steppe_horse", "Steppe_Horse", [("steppe_horse", 0)], itp_type_horse|itp_merchandise, 0, 832, weight(0.000000)|abundance(80)|difficulty(2)|hit_points(200)|body_armor(30)|horse_speed(50)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 

#Steppe Horse in Plate Mail Armor
["charger", "Charger", [("charger_new", 0)], itp_type_horse|itp_merchandise, 0, 4800, weight(0.000000)|abundance(20)|difficulty(4)|hit_points(200)|body_armor(80)|horse_speed(36)|horse_maneuver(44)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["tiesebanlian_ma", "tiesebanlian_ma", [("charger_new_steel", 0)], itp_type_horse|itp_merchandise, 0, 4800, abundance(20)|difficulty(4)|hit_points(200)|body_armor(80)|horse_speed(36)|horse_maneuver(44)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["zongsebanlian_ma", "zongsebanlian_ma", [("charger_new_brown", 0)], itp_type_horse|itp_merchandise, 0, 4800, abundance(20)|difficulty(4)|hit_points(200)|body_armor(80)|horse_speed(36)|horse_maneuver(44)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["heisebanlian_ma", "heisebanlian_ma", [("charger_new_black", 0)], itp_type_horse|itp_merchandise, 0, 4800, abundance(20)|difficulty(4)|hit_points(200)|body_armor(80)|horse_speed(36)|horse_maneuver(44)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 

#Steppe Horse in Ligature Armor
["warhorse_steppe", "Steppe_Charger", [("warhorse_steppe", 0)], itp_type_horse|itp_merchandise, 0, 3494, weight(0.000000)|abundance(40)|difficulty(4)|hit_points(200)|body_armor(68)|horse_speed(40)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["hualizhajia_ma", "hualizhajia_ma", [("warhorse_lamellar_c", 0)], itp_type_horse|itp_merchandise, 0, 3494, abundance(40)|difficulty(4)|hit_points(200)|body_armor(68)|horse_speed(40)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["tiesezhajia_ma", "tiesezhajia_ma", [("warhorse_lamellar_b", 0)], itp_type_horse|itp_merchandise, 0, 3494, abundance(40)|difficulty(4)|hit_points(200)|body_armor(68)|horse_speed(40)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["jingzhizhajia_ma", "jingzhizhajia_ma", [("warhorse_lamellar_a", 0)], itp_type_horse|itp_merchandise, 0, 3494, abundance(40)|difficulty(4)|hit_points(200)|body_armor(68)|horse_speed(40)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic|imodbit_champion], 

#Steppe Horse in Half Ligature Armor
["shense_banzhajia_caoyuanma", "shense_banzhajia_caoyuanma", [("ho_khe_cata_black", 0)], itp_type_horse|itp_merchandise, 0, 3094, abundance(40)|difficulty(4)|hit_points(200)|body_armor(60)|horse_speed(44)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["qianse_banzhajia_caoyuanma", "qianse_banzhajia_caoyuanma", [("ho_khe_cata_yellow", 0)], itp_type_horse|itp_merchandise, 0, 3094, abundance(40)|difficulty(4)|hit_points(200)|body_armor(60)|horse_speed(44)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 

#Steppe Horse in Chain Armor
["warhorse", "War_Horse", [("warhorse_chain", 0)], itp_type_horse|itp_merchandise, 0, 3714, weight(0.000000)|abundance(40)|difficulty(4)|hit_points(200)|body_armor(61)|horse_speed(41)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["tuselianjia_ma", "tuselianjia_ma", [("warhorse_chain_brass", 0)], itp_type_horse|itp_merchandise, 0, 3714, abundance(40)|difficulty(4)|hit_points(200)|body_armor(61)|horse_speed(41)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 

#Steppe Horse in Chain Armor Frock
["tiese_lianjia_caoyuanma", "tiese_lianjia_caoyuanma", [("mailled_horse_1", 0)], itp_type_horse|itp_merchandise, 0, 3804, abundance(35)|difficulty(4)|hit_points(200)|body_armor(74)|horse_speed(42)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 
["tuhuang_lianjia_caoyuanma", "tuhuang_lianjia_caoyuanma", [("mailled_horse_2", 0)], itp_type_horse|itp_merchandise, 0, 3804, abundance(35)|difficulty(4)|hit_points(200)|body_armor(74)|horse_speed(42)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 

#Steppe Horse in Scale and Shell
["linjia_zhaopaozhanma", "linjia_zhaopaozhanma", [("ho_sar_long_sarranid", 0)], itp_type_horse|itp_merchandise, 0, 3400, abundance(40)|difficulty(4)|hit_points(200)|body_armor(70)|horse_speed(41)|horse_maneuver(39)|horse_charge(36)|horse_scale(110), imodbits_horse_basic], 


#######PLAIN HORSE#########
#The plain horse is a horse breed bred by the Powell people, officially known as the Cheval horse. This horse has a relatively mediocre and reliable characteristics, and has been on the offensive with Powell's knights for hundreds of years.
#Armorless Plain Horse
["courser", "Courser", [("courser", 0)], itp_type_horse|itp_merchandise, 0, 800, weight(0.000000)|abundance(80)|difficulty(2)|hit_points(210)|body_armor(27)|horse_speed(49)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 

#Plain Horse in Chain Armor Frock
["dolphin_chain_armor_plain_horse", "Dolphin Chain Armor Plain Horse", [("war_horse_dolphin", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["lvhua_lianjia_pinyuanma", "lvhua_lianjia_pinyuanma", [("WLONG3", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["julu_ianjia_pingyuanma", "julu_ianjia_pingyuanma", [("WLONG6", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["jiaoma_ianjia_pingyuanma", "jiaoma_ianjia_pingyuanma", [("WLONG11", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["jinjiu_lianjia_pingyuanma", "jinjiu_lianjia_pingyuanma", [("WLONG14", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["honghei_lianjia_pingyuanma", "honghei_lianjia_pingyuanma", [("WLONG15", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(52)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["ziying_lianjia_pingyuanma", "ziying_lianjia_pingyuanma", [("WLONG20", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["honglong_lianjia_pingyuanma", "honglong_lianjia_pingyuanma", [("WLONG23", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["yinsun_lianjia_pingyuanma", "yinsun_lianjia_pingyuanma", [("WLONG24", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["jinyang_lianjia_pinyuanma", "jinyang_lianjia_pinyuanma", [("war_horse_green", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["xunlu_lianjia_pinyuanma", "xunlu_lianjia_pinyuanma", [("war_horse_ravenstern", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["ziyi_lianjia_pinyuanma", "ziyi_lianjia_pinyuanma", [("war_horse_burgundy", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["baiyang_lianjia_pinyuanma", "baiyang_lianjia_pinyuanma", [("war_horse_white", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["hongshi_lianjia_pinyuanma", "hongshi_lianjia_pinyuanma", [("rampant_lion_red2", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["lanying_lianjia_pinyuanma", "lanying_lianjia_pinyuanma", [("eagle_on_yellow", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["heishu_lianjia_pinyuanma", "heishu_lianjia_pinyuanma", [("war_horse_black", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 
["qiangwei_lianjia_pingyuanma", "qiangwei_lianjia_pingyuanma", [("cw_horse", 0)], itp_type_horse|itp_merchandise, 0, 3800, abundance(40)|difficulty(4)|hit_points(210)|body_armor(72)|horse_speed(41)|horse_maneuver(44)|horse_charge(33)|horse_scale(106), imodbits_horse_basic], 

#Plain Horse in Simple Plate
["iron_knight_warhorse", "iron_knight_warhorse", [("iron_knight_warhorse", 0)], itp_type_horse|itp_merchandise, 0, 6700, abundance(30)|difficulty(6)|hit_points(210)|body_armor(100)|horse_speed(34)|horse_maneuver(44)|horse_charge(38)|horse_scale(106), imodbits_horse_basic], 
["powell_knight_warhorse", "powell_knight_warhorse", [("horse10_c", 0)], itp_type_horse|itp_merchandise, 0, 6900, abundance(30)|difficulty(6)|hit_points(210)|body_armor(102)|horse_speed(34)|horse_maneuver(44)|horse_charge(38)|horse_scale(106), imodbits_horse_basic, [], [fac_kingdom_1]], 


#######MOUNTAINIC HORSE#########
#Mountainic horses, also known as the Piedmont Pony, are the most abundant horse breeds in the Papal. Although smaller in size and slower in speed than other horse breeds, mountain horses have a gentle and easy to handle personality, and are quite capable of carrying heavy armor.
#Armorless Mountanic Horse
["mountain_horse", "Mountain_Horse", #山地马
   [("arabian_horse_b", 0)], 
   itp_type_horse|itp_merchandise, 0, 820, 
   weight(0.000000)|abundance(80)|difficulty(2)|hit_points(230)|body_armor(29)|horse_speed(45)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic], 

#Papal Mountanic Horse in Chain Armor Frock
["papal_chain_armor_mountain_horse", "Papal Chain Armor Mountain Horse", #教国链甲山地马
   [("charge_teuton", 0)], 
   itp_type_horse|itp_merchandise, 0, 3820, 
   weight(0.000000)|abundance(30)|difficulty(3)|hit_points(230)|body_armor(74)|horse_speed(37)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic], 
["purifier_chain_armor_mountain_horse", "Purifier Chain Armor Mountain Horse", #净世军链甲山地马
   [("long_cross_horse_a", 0)], 
   itp_type_horse, 0, 3820, 
   abundance(30)|difficulty(3)|hit_points(230)|body_armor(74)|horse_speed(37)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic|imodbit_champion], 
["veteran_chain_armor_mountain_horse", "Veteran Chain Armor Mountain Horse", #历战链甲山地马
   [("long_templar_horse", 0)], 
   itp_type_horse|itp_merchandise, 0, 3850, 
   abundance(20)|difficulty(3)|hit_points(225)|body_armor(76)|horse_speed(36)|horse_maneuver(60)|horse_charge(29)|horse_scale(95), 
   imodbits_horse_basic], 
["exorcist_chain_armor_mountain_horse", "Exorcist Chain Armor Mountain Horse", #狩魔链甲山地马
   [("long_hospitaller_horse", 0)], 
   itp_type_horse, 0, 4020, 
   abundance(13)|difficulty(3)|hit_points(245)|body_armor(76)|horse_speed(40)|horse_maneuver(54)|horse_charge(32)|horse_scale(95), 
   imodbits_horse_basic|imodbit_champion], 
["theologian_chain_armor_mountain_horse", "Theologian Chain Armor Mountain Horse", #神学家短链甲山地马
   [("jerusalem_horse_a", 0)], 
   itp_type_horse, 0, 3920, 
   abundance(15)|difficulty(3)|hit_points(260)|body_armor(75)|horse_speed(39)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic|imodbit_champion], 
["papal_plate_armor_mountain_horse", "Papal Plate Armor Mountain Horse", #教国铁甲山地马
   [("aqs_horse3", 0)], 
   itp_type_horse, 0, 6000, 
   abundance(10)|difficulty(5)|hit_points(230)|body_armor(90)|horse_speed(30)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic], 

#Mountanic Horse in Simple Plate
["simple_plate_mountanic_horse_iron", "Simple Plate Mountanic Horse Iron", #铁色轻板甲山地马
   [("plated_horse_1", 0)], 
   itp_type_horse|itp_merchandise, 0, 5734, 
   abundance(15)|difficulty(5)|hit_points(230)|body_armor(87)|horse_speed(31)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic], 
["simple_plate_mountanic_horse_yellow", "simple_plate_mountanic_horse_yellow", #铁黄轻板甲山地马
   [("plated_horse_2", 0)], 
   itp_type_horse|itp_merchandise, 0, 5734, 
   abundance(15)|difficulty(5)|hit_points(230)|body_armor(87)|horse_speed(31)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic], 
["simple_plate_mountanic_horse_luxurious", "simple_plate_mountanic_horse_luxurious", #华丽轻板甲山地马
   [("plated_horse_3", 0)], 
   itp_type_horse|itp_merchandise, 0, 6334, 
   abundance(12)|difficulty(5)|hit_points(240)|body_armor(88)|horse_speed(32)|horse_maneuver(54)|horse_charge(30)|horse_scale(95), 
   imodbits_horse_basic], 
["simple_plate_mountanic_horse_ancient", "simple_plate_mountanic_horse_ancient", #古轻板甲山地马
   [("plated_horse_4", 0)], 
   itp_type_horse|itp_merchandise, 0, 6734, 
   abundance(2)|difficulty(5)|hit_points(250)|body_armor(90)|horse_speed(34)|horse_maneuver(54)|horse_charge(28)|horse_scale(95), 
   imodbits_horse_basic], 


#######WHITESPRING HORSE#########
#The Whitespring Horse is one of the extraordinary horse breeds, transformed from the mountanic horse that drank the miracle of the White Spring.
["highknight_warhorse", "Highknight Warhorse", #高洁骑士战马
   [("DGsqma2_tiehuan", 0)], 
   itp_type_horse, 0, 9700, 
   abundance(10)|difficulty(5)|hit_points(800)|body_armor(83)|horse_speed(50)|horse_maneuver(54)|horse_charge(44)|horse_scale(102), 
   imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_5]], 
["whitespring_warhorse_in_simple_plate", "whitespring_warhorse_in_simple_plate", #轻板甲洗礼马
   [("hero_horse5_5_t", 0)], 
   itp_type_horse, 0, 13700, 
   abundance(10)|difficulty(6)|hit_points(1200)|body_armor(113)|horse_speed(50)|horse_maneuver(54)|horse_charge(50)|horse_scale(102), 
   imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_5]], 
["divine_iron_warhorse", "divine_iron_warhorse", #天铁加护马
   [("DGsqma", 0)], 
   itp_type_horse, 0, 32100, 
   abundance(1)|difficulty(7)|hit_points(1500)|body_armor(153)|horse_speed(50)|horse_maneuver(54)|horse_charge(60)|horse_scale(102), 
   imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_5]], 
["palatin_warhorse", "palatin_warhorse", #圣别马
   [("limingma20", 0)], 
   itp_type_horse, 0, 50000, 
   abundance(1)|difficulty(8)|hit_points(2000)|body_armor(170)|horse_speed(57)|horse_maneuver(54)|horse_charge(60)|horse_scale(102), 
   imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_5]], 


#######DESERT HORSE#########
#Armorless Desert Horse
["arabian_horse_a", "Desert_Horse", [("arabian_horse_a", 0)], itp_type_horse|itp_merchandise, 0, 850, weight(0.000000)|abundance(80)|difficulty(2)|hit_points(225)|body_armor(33)|horse_speed(48)|horse_maneuver(44)|horse_charge(32)|horse_scale(112), imodbits_horse_basic, [], [fac_kingdom_3, fac_kingdom_6]], 

#The desert horse originated from the Ramen Sand Horse raised by the descendants of the Sand King, which adapts to desert environments and is quite resilient. But after the collapse of the Sand People, the use of this type of horse became increasingly scarce.
#Desert Horse in Ligature Armor
["desert_horse_leather_1", "desert_horse_leather", [("lamellar_horse_1", 0)], itp_type_horse|itp_merchandise, 0, 3492, abundance(40)|difficulty(4)|hit_points(225)|body_armor(71)|horse_speed(38)|horse_maneuver(44)|horse_charge(32)|horse_scale(112), imodbits_horse_basic, [], [fac_kingdom_3, fac_kingdom_6]], 
["desert_horse_leather_2", "desert_horse_leather", [("lamellar_horse_2", 0)], itp_type_horse|itp_merchandise, 0, 3492, abundance(40)|difficulty(4)|hit_points(225)|body_armor(71)|horse_speed(38)|horse_maneuver(44)|horse_charge(32)|horse_scale(112), imodbits_horse_basic, [], [fac_kingdom_3, fac_kingdom_6]], 
["warhorse_sarranid", "Sarranian_War_Horse", [("warhorse_sarranid", 0)], itp_type_horse|itp_merchandise, 0, 3814, weight(0.000000)|abundance(40)|difficulty(4)|hit_points(225)|body_armor(71)|horse_speed(38)|horse_maneuver(44)|horse_charge(32)|horse_scale(112), imodbits_horse_basic], 


#######SPIRITUAL HORSE#########
#Like elves, Spiritual Horses are also minions created by the Spirit Tree, possessing unparalleled physical fitness. However, they do not allow any characters outside the Spirit Tree minions to ride them, and they strongly dislike any horse armor.
#杂交灵性马
["silver_mane_steed", "Silver Mane Steed", #银粽骏马，灵性马血脉稀薄的后裔
   [("courser_white", 0)], 
   itp_type_horse|itp_merchandise, 0, 2700, 
   abundance(20)|difficulty(4)|hit_points(270)|body_armor(33)|horse_speed(60)|horse_maneuver(50)|horse_charge(42)|horse_scale(105), 
   imodbits_horse_basic|imodbit_champion], 
["variegated_spiritual_horse", "Variegated Spiritual Horse", #杂色灵性马，平原马杂交
   [("pinto", 0)], 
   itp_type_horse|itp_merchandise, 0, 4383, 
   abundance(5)|difficulty(4)|hit_points(480)|body_armor(47)|horse_speed(60)|horse_maneuver(42)|horse_charge(45)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 
["south_spiritual_horse", "South Spiritual Horse", #南方灵性马，草原马和沙漠马杂交
   [("aqs_horse5", 0)], 
   itp_type_horse|itp_merchandise, 0, 4383, 
   abundance(5)|difficulty(4)|hit_points(460)|body_armor(45)|horse_speed(63)|horse_maneuver(40)|horse_charge(40)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 
["grey_spiritual_horse", "Grey Spiritual Horse", #灰色灵性马，山地马杂交
   [("greyflame", 0)], 
   itp_type_horse|itp_merchandise, 0, 4383, 
   abundance(5)|difficulty(4)|hit_points(500)|body_armor(45)|horse_speed(56)|horse_maneuver(58)|horse_charge(38)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 

#纯种灵性马
["white_spiritual_horse", "White Spiritual Horse", #白色灵性马
   [("moondance", 0)], 
   itp_type_horse, 0, 4983, 
   abundance(2)|difficulty(5)|hit_points(500)|body_armor(50)|horse_speed(65)|horse_maneuver(38)|horse_charge(50)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 
["black_spiritual_horse", "Black Spiritual Horse", #黑色灵性马
   [("blackdapple", 0)], 
   itp_type_horse, 0, 4983, 
   abundance(2)|difficulty(5)|hit_points(500)|body_armor(50)|horse_speed(65)|horse_maneuver(38)|horse_charge(50)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 

["leather_armor_spiritual_horse", "Leather Armor Spiritual Horse", #罩袍灵性马
   [("moondance_leather", 0)], 
   itp_type_horse, 0, 6083, 
   abundance(1)|difficulty(5)|hit_points(500)|body_armor(75)|horse_speed(60)|horse_maneuver(30)|horse_charge(50)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 
["scale_armor_spiritual_horse", "Scale Armor Spiritual Horse", #扎甲灵性马
   [("blackapple_scale", 0)], 
   itp_type_horse, 0, 7533, 
   abundance(1)|difficulty(7)|hit_points(500)|body_armor(88)|horse_speed(55)|horse_maneuver(30)|horse_charge(50)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 
["plate_armor_spiritual_horse", "Plate Armor Spiritual Horse", #板甲灵性马
   [("moondance_plate", 0)], 
   itp_type_horse, 0, 9911, 
   abundance(1)|difficulty(9)|hit_points(500)|body_armor(110)|horse_speed(48)|horse_maneuver(30)|horse_charge(50)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 

#异化灵性马
["magic_spiritual_horse", "Magic Spiritual Horse", #魔堕灵性马
   [("aqs_horse1", 0)], 
   itp_type_horse, 0, 9983, 
   abundance(1)|difficulty(7)|hit_points(700)|body_armor(60)|horse_speed(65)|horse_maneuver(38)|horse_charge(60)|horse_scale(100), 
   imodbits_horse_basic|imodbit_champion], 


#######SPECIAL HORSE#########
["guizu_ma", "guizu_ma", [("warhorse_08y", 0)], itp_type_horse|itp_merchandise, 0, 6310, abundance(20)|difficulty(4)|hit_points(260)|body_armor(85)|horse_speed(40)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic], 

["darkflame_warhorse", "darkflame_warhorse", [("ma0", 0)], itp_type_horse|itp_merchandise, 0, 26300, abundance(5)|difficulty(7)|hit_points(900)|body_armor(125)|horse_speed(43)|horse_maneuver(42)|horse_charge(44)|horse_scale(111), imodbits_horse_basic], 
["ancient_warrior_warhorse", "ancient_warrior_warhorse", [("ljmaaa", 0)], itp_type_horse, 0, 31330, abundance(1)|difficulty(7)|hit_points(1250)|body_armor(160)|horse_speed(45)|horse_maneuver(42)|horse_charge(47)|horse_scale(111), imodbits_horse_basic], 
["ancient_king_warhorse", "ancient_king_warhorse", [("dyzmmm", 0)], itp_type_horse, 0, 57400, abundance(1)|difficulty(8)|hit_points(1600)|body_armor(185)|horse_speed(48)|horse_maneuver(46)|horse_charge(50)|horse_scale(111), imodbits_horse_basic], 



#CAPE
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["cape_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["powell_red_cape", "Powell Red Cape", #普威尔红披风
   [("powell_lifeguard_plate.3", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["flower_red_cape", "Flower Red Cape", #红花披风
   [("cw_armor.1", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["luxurious_cape", "Luxurious Cape", #华贵披风
   [("Sangrail_maserainnean_plate_1.2", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["deep_blue_cape", "Deep Blue Cape", #深蓝披风
   [("gorieusred.2", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["knight_white_cape", "Knight White Cape", #骑士白披风
   [("knight_surcoat_01_with-mantle.1", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["experienced_cape", "Experienced Cape", #历战者披风
   [("armor11.1", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["experienced_knight_cape", "Experienced Knight Cape", #历战骑士披风
   [("dragon_armor.4", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["coarse_cape", "Coarse Cape", #粗布披风
   [("pink_gray_cloak", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["papal_knight_cape", "Papal Knight Cape", #教国骑士披风
   [("shengdian_qishi.2", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 
["winged_saint_cape", "Winged Saint Cape", #翼圣披风
   [("heavy_spotless_armor.1", 0)], 
   itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_doesnt_cover_hair, 0, 312, 
   weight(1)|abundance(40)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), 
   imodbits_cloth], 



#TALISMAN护符
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["talisman_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3, 0, imodbits_none],

["small_life_talisman", "Small Life Talisman", #残破命脉护符
   [("cross_normal", 0)], 
   itp_type_goods|itp_accessorise, 0, 1000, 
   weight(0.05)|abundance(40)|max_ammo(0)|food_quality(0), 
   imodbits_none], 
["mark_of_scars", "Mark of Scars", #伤痕印记
   [("GoldRing", 0)], 
   itp_type_goods|itp_accessorise, 0, 2700, 
   weight(0.05)|abundance(10)|max_ammo(0)|food_quality(0), 
   imodbits_none], 
["holy_sand_talisman", "Holy Sand Talisman", #圣沙护符
   [("papal_logo", 0)], 
   itp_type_goods|itp_accessorise, 0, 1000, 
   weight(0.05)|abundance(1)|max_ammo(0)|food_quality(0), 
   imodbits_none], 
["gold_dung_beetle_talisman", "Gold Dung Beetle Talisman", #金色粪金龟护符
   [("Goldbug", 0)], 
   itp_type_goods|itp_accessorise, 0, 1000, 
   weight(0.05)|abundance(1)|max_ammo(0)|food_quality(0), 
   imodbits_none], 



#MATERIALS物资
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["material_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3, 0, imodbits_none],

["mubingling", "Pottery", [("round01", 0)], itp_type_goods|itp_always_loot, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 

["highly_toxin", "Highly Toxin", #剧毒油脂
   [("raw_dye_blue", 0)], 
   itp_type_goods|itp_small_tool, 0, 1000, 
   weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), 
   imodbits_none], 

["silver_bullion", "Silver Bullion", #银条
   [("Silver2", 0)], 
   itp_type_goods, 0, 800, weight(0.15)|abundance(100), imodbits_none], 
["gold_bullion", "Gold Bullion", #金条
   [("Gold2", 0)], 
   itp_type_goods, 0, 1500, weight(0.2)|abundance(100), imodbits_none], 
["booty", "Booty", #战利品
   [("chest_simple", 0)], 
   itp_type_goods, 0, 5000, weight(40)|abundance(100), imodbits_none], 

["great_apple", "Great Apple", #嘉果
   [("great_apple", 0)], 
   itp_type_goods, 0, 50000, weight(50)|abundance(1)|max_ammo(0)|food_quality(0), imodbits_none], 


#龙相关
#hit_points表示增加的龙力，food_quality表示侵蚀，max_ammo表示最高适用的阶段。
["raw_dragonblood", "Raw Dragonblood", #生龙血
   [("health_bottle_s", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 70, weight(0.1)|abundance(15)|hit_points(7)|food_quality(4)|max_ammo(3), imodbits_none], 
["inferior_dragonblood_wine", "Inferior Dragonblood Wine", #劣等龙血酒
   [("health_bottle_m", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 100, weight(0.1)|abundance(15)|hit_points(7)|food_quality(1)|max_ammo(3), imodbits_none], 
["superior_dragonblood_wine", "Superior Dragonblood Wine", #优质龙血酒
   [("health_bottle_multi", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 200, weight(0.1)|abundance(10)|hit_points(18)|food_quality(1)|max_ammo(3), imodbits_none], 
["raw_dragon_meat", "Raw Dragon Meat", #生龙肉
   [("raw_meat", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 700, weight(0.5)|abundance(5)|hit_points(100)|food_quality(5)|max_ammo(4), imodbits_none], 
["cooked_dragon_steak", "Cooked Dragon Steak", #熟龙肉排
   [("smoked_meat", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 1000, weight(0.5)|abundance(3)|hit_points(100)|food_quality(2)|max_ammo(4), imodbits_none], 
["dragon_marrow", "Dragon Marrow", #龙髓液
   [("bloodbottle", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 3000, weight(0.5)|abundance(5)|hit_points(300)|food_quality(4)|max_ammo(5), imodbits_none], 
["dragon_heart", "Dragon Heart", #龙心
   [("dragonheart", 0)], 
   itp_type_goods|itp_expendable|itp_merchandise, 0, 10000, weight(0.5)|abundance(5)|hit_points(1000)|food_quality(10)|max_ammo(5), imodbits_none], 


#尸体
["bad_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["normal_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["good_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["excellent_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["elf_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["demon_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 
["highest_corpse", "Pottery", [("round01", 0)], itp_type_goods, 0, 1000, weight(10.000000)|abundance(10)|max_ammo(0)|food_quality(0), imodbits_none], 




#OTHERS
#_______________________________________________________________________________________________________________________________________________________________________________
#
 ["other_item","INVALID ITEM", [("invalid_item",0)], 0, 0, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


["fragment_of_ancient_king_sword", "Fragment of Ancient King Sword", [("WAoRSwordA.2", 0), ("WAoRSwordA.1", 0)], itp_type_goods|itp_unique, 4589617167, 15000, weight(0.750000)|abundance(1)|max_ammo(0)|food_quality(0), imodbits_none], 

["blood_overflow", "Blood Overflow", #血溢
   [("corprus_scepter_dark", 0)], 
   itp_type_goods|itp_no_pick_up_from_ground, 0, 0, 0, 
   imodbits_none], 
["blood_explosion", "Blood Explosion", #血爆
   [("corprus_scepter_dark_huge", 0)], 
   itp_type_goods|itp_no_pick_up_from_ground, 0, 0, 0, imodbits_none], 
["skeleton_giant", "Skeleton Giant", #不死组合巨人
   [("skeleton_giant_hit_1", 0)], 
  itp_type_goods|itp_no_pick_up_from_ground, 0, 0, 0, 
  imodbits_none], 
["skeleton_giant_sword", "Skeleton Giant Sword", #剑骸组合巨人
   [("skeleton_giant_hit_2", 0)], 
   itp_type_goods|itp_no_pick_up_from_ground, 0, 0, 0, 
   imodbits_none], 
["skeleton_spear_anim", "Skeleton Spear Anim", #骨矛动画
   [("skeleton_spear_anim", 0)], 
   itp_type_goods|itp_no_pick_up_from_ground, 0, 0, 0, 
   imodbits_none], 
["carrion", "Carrion", #烂泥
   [("carrion", 0)], 
   itp_type_goods|itp_no_pick_up_from_ground, 0, 0, abundance(0)|max_ammo(0)|food_quality(0), 
   imodbits_none],


#######QUEST ITEM#########
["siege_supply", "Supplies", [("ale_barrel", 0)], itp_type_goods, 0, 96, weight(40.000000)|abundance(70)|max_ammo(0)|food_quality(0), imodbits_none], 
["quest_wine", "Wine", [("amphora_slim", 0)], itp_type_goods, 0, 46, weight(40.000000)|abundance(60)|max_ammo(50)|food_quality(0), imodbits_none], 
["quest_ale", "Ale", [("ale_barrel", 0)], itp_type_goods, 0, 31, weight(40.000000)|abundance(70)|max_ammo(50)|food_quality(0), imodbits_none], 

["keys", "Ring_of_Keys", [("throwing_axe_a", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, 9223388529554358286, 240, weight(5.000000)|abundance(100)|difficulty(0)|weapon_length(53)|spd_rtng(98)|swing_damage(29, cut)|thrust_damage(0, cut), imodbits_thrown], 




["firekeeper_body", "firekeeper_body", [("firekeeper_2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee|itp_covers_head, 0, 1, weight(1.000000)|abundance(1)|difficulty(0)|head_armor(23)|body_armor(178)|leg_armor(175), imodbits_none], 
["firekeeper_eyes", "firekeeper_eyes", [("firekeeper_4", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_fit_to_head, 0, 20000, weight(0.500000)|abundance(3)|difficulty(0)|head_armor(68)|body_armor(0)|leg_armor(0), imodbits_none], 
["firekeeper_gloves", "firekeeper_gloves", [("female_gloveL", 0)], itp_type_hand_armor|itp_civilian|itp_next_item_as_melee|itp_covers_head, 0, 1, weight(0.250000)|abundance(1)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_none], 
["firekeeper_head", "firekeeper_head", [("firekeeper_1", 0)], itp_type_foot_armor|itp_civilian|itp_next_item_as_melee|itp_covers_head, 0, 1, weight(0.100000)|abundance(1)|difficulty(0)|head_armor(100)|body_armor(0)|leg_armor(0), imodbits_none], 


["items_end", "Items End", [("invalid_item",0)], 0, 0, 1, 0, 0],
]


items = items + picture_items + faction_items