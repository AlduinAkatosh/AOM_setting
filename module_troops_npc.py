# -*- coding: UTF-8 -*-

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *
from ID_attributes import *

from module_troops import *


####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

powell_knight_attrib_1 =    str_30 | agi_30 | int_18 | cha_36|level(45)
powell_knight_skills_1 = knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_12|knows_trade_3
#four biggest lords


powell_knight_attrib_2 =    str_27 | agi_26 | int_18 | cha_30|level(42)
powell_knight_skills_2 = knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_8|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_7|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_5|knows_prisoner_management_4|knows_leadership_10|knows_trade_3
#old lords

powell_knight_attrib_3 =    str_26 | agi_22 | int_15 | cha_24|level(40)
powell_knight_skills_3 = knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_5|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_3|knows_prisoner_management_3|knows_leadership_8|knows_trade_2
#young lords

yishith_knight_attrib_1 =   str_25 | agi_50 | int_60 | cha_60|level(55)
yishith_knight_skills_1 = knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_15|knows_weapon_master_10|knows_shield_4|knows_athletics_15|knows_riding_9|knows_horse_archery_10|knows_looting_6|knows_trainer_8|knows_tracking_4|knows_tactics_10|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_8|knows_persuasion_8|knows_prisoner_management_8|knows_leadership_15|knows_trade_3

yishith_knight_attrib_2 =   str_22 | agi_47 | int_48 | cha_60|level(48)
yishith_knight_skills_2 = knows_ironflesh_7|knows_power_strike_6|knows_power_throw_1|knows_power_draw_12|knows_weapon_master_9|knows_shield_3|knows_athletics_14|knows_riding_8|knows_horse_archery_8|knows_looting_5|knows_trainer_7|knows_tracking_3|knows_tactics_8|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_6|knows_persuasion_6|knows_prisoner_management_6|knows_leadership_12|knows_trade_3

yishith_knight_attrib_3 =   str_20 | agi_42 | int_45 | cha_50|level(42)
yishith_knight_skills_3 = knows_ironflesh_7|knows_power_strike_6|knows_power_throw_1|knows_power_draw_10|knows_weapon_master_7|knows_shield_3|knows_athletics_12|knows_riding_7|knows_horse_archery_7|knows_looting_5|knows_trainer_7|knows_tracking_3|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_5|knows_persuasion_6|knows_prisoner_management_4|knows_leadership_9|knows_trade_3

korouto_knight_attrib_1 =   str_53 | agi_15 | int_15 | cha_15|level(45)
korouto_knight_skills_1 = knows_ironflesh_15|knows_power_strike_14|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_7|knows_horse_archery_1|knows_looting_10|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_1|knows_prisoner_management_4|knows_leadership_7|knows_trade_1

korouto_knight_attrib_2 =   str_50 | agi_15 | int_12 | cha_12|level(42)
korouto_knight_skills_2 = knows_ironflesh_15|knows_power_strike_14|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_4|knows_shield_3|knows_athletics_3|knows_riding_7|knows_horse_archery_1|knows_looting_8|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_1

korouto_knight_attrib_3 =   str_47 | agi_14 | int_9 | cha_9|level(40)
korouto_knight_skills_3 = knows_ironflesh_14|knows_power_strike_14|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_7|knows_horse_archery_1|knows_looting_7|knows_trainer_1|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_1|knows_prisoner_management_3|knows_leadership_3|knows_trade_1

conferderation_knight_attrib_1 =   str_28 | agi_20 | int_21 | cha_18|level(45)
conferderation_knight_skills_1 = knows_ironflesh_8|knows_power_strike_7|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_5|knows_looting_6|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_4|knows_persuasion_8|knows_prisoner_management_6|knows_leadership_12|knows_trade_2

conferderation_knight_attrib_2 =   str_27 | agi_19 | int_18 | cha_17|level(42)
conferderation_knight_skills_2 = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_power_draw_2|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_4|knows_looting_5|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_4|knows_persuasion_8|knows_prisoner_management_5|knows_leadership_9|knows_trade_2

conferderation_knight_attrib_3 =   str_26 | agi_18 | int_14 | cha_15|level(40)
conferderation_knight_skills_3 = knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_5|knows_horse_archery_4|knows_looting_5|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_4|knows_persuasion_5|knows_prisoner_management_3|knows_leadership_7|knows_trade_1

papal_knight_attrib_1 =   str_33 | agi_28 | int_24 | cha_21|level(45)
papal_knight_skills_1 = knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_9|knows_shield_9|knows_athletics_7|knows_riding_4|knows_horse_archery_1|knows_looting_3|knows_trainer_8|knows_tracking_3|knows_tactics_7|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_5|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_12|knows_trade_2

papal_knight_attrib_2 =   str_30 | agi_26 | int_22 | cha_19|level(42)
papal_knight_skills_2 = knows_ironflesh_9|knows_power_strike_9|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_8|knows_shield_8|knows_athletics_7|knows_riding_4|knows_horse_archery_1|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_7|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_10|knows_trade_2

papal_knight_attrib_3 =   str_27 | agi_23 | int_19 | cha_16|level(40)
papal_knight_skills_3 = knows_ironflesh_8|knows_power_strike_8|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_7|knows_shield_7|knows_athletics_6|knows_riding_3|knows_horse_archery_1|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_4|knows_prisoner_management_5|knows_leadership_9|knows_trade_1

longshu_knight_attrib_1 =   str_45 | agi_35 | int_25 | cha_34|level(50)
longshu_knight_skills_1 = knows_ironflesh_13|knows_power_strike_14|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_8|knows_athletics_8|knows_riding_9|knows_horse_archery_8|knows_looting_9|knows_trainer_10|knows_tracking_3|knows_tactics_8|knows_pathfinding_6|knows_spotting_3|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_5|knows_persuasion_4|knows_prisoner_management_5|knows_leadership_12|knows_trade_3

longshu_knight_attrib_2 =   str_42 | agi_32 | int_21 | cha_30|level(48)
longshu_knight_skills_2 = knows_ironflesh_11|knows_power_strike_11|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_8|knows_shield_7|knows_athletics_7|knows_riding_8|knows_horse_archery_8|knows_looting_7|knows_trainer_10|knows_tracking_3|knows_tactics_7|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_5|knows_persuasion_4|knows_prisoner_management_5|knows_leadership_11|knows_trade_3

longshu_knight_attrib_3 =   str_40 | agi_30 | int_18 | cha_27|level(45)
longshu_knight_skills_3 = knows_ironflesh_10|knows_power_strike_10|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_6|knows_athletics_6|knows_riding_7|knows_horse_archery_7|knows_looting_5|knows_trainer_8|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_5|knows_persuasion_4|knows_prisoner_management_5|knows_leadership_10|knows_trade_2

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

#科鲁托人类脸
kouruto_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
kouruto_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
kouruto_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
kouruto_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
kouruto_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

kouruto_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
kouruto_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
kouruto_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
kouruto_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
kouruto_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

kouruto_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
kouruto_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

#科鲁托兽人脸
kouruto_lion_face_1 = 0x0000000000000041124924924a49224900000000001ca2920000000000000000
kouruto_lion_face_2 = 0x0000000dff00104d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_bear_face_1 = 0x0000000000002081124924924a49224900000000001ca2920000000000000000
kouruto_bear_face_2 = 0x0000000dff00308d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_wolf_face_1 = 0x00000000000040c1124924924a49224900000000001ca2920000000000000000
kouruto_wolf_face_2 = 0x0000000dff0050cd5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_tiger_face_1 = 0x0000000000006101124924924a49224900000000001ca2920000000000000000
kouruto_tiger_face_2 = 0x0000000dff00610d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_cow_face_1 = 0x0000000000007141124924924a49224900000000001ca2920000000000000000
kouruto_cow_face_2 = 0x0000000dff00814d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_sheep_face_1 = 0x0000000000009181124924924a49224900000000001ca2920000000000000000
kouruto_sheep_face_2 = 0x0000000dff00918d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_deer_face_1 = 0x000000000000a1c1124924924a49224900000000001ca2920000000000000000
kouruto_deer_face_2 = 0x0000000dff00b1cd5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_rabbit_face_1 = 0x000000000000c201124924924a49224900000000001ca2920000000000000000
kouruto_rabbit_face_2 = 0x0000000dff00d20d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_dog_face_1 = 0x000000000000e241124924924a49224900000000001ca2920000000000000000
kouruto_dog_face_2 = 0x0000000ebf00f24d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_fox_face_1 = 0x0000000000010281124924924a49224900000000001ca2920000000000000000
kouruto_fox_face_2 = 0x0000000ebf01128d5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_cat_face_1 = 0x00000000000122c1124924924a49224900000000001ca2920000000000000000
kouruto_cat_face_2 = 0x0000000ebf0132cd5b75d2db6dd6db6500000000001eedad0000000000000000

kouruto_lion_woman_face_1 = 0x00000000000000410000000000000e0000000000000000000000000000000000
kouruto_lion_woman_face_2 = 0x000000003f0010710000000000000fff00000000000000000000000000000000

kouruto_bear_woman_face_1 = 0x00000000000020810000000000000e0000000000000000000000000000000000
kouruto_bear_woman_face_2 = 0x000000003f0030b10000000000000fff00000000000000000000000000000000

kouruto_wolf_woman_face_1 = 0x00000000000040c10000000000000e0000000000000000000000000000000000
kouruto_wolf_woman_face_2 = 0x000000003f0050f10000000000000fff00000000000000000000000000000000

kouruto_tiger_woman_face_1 = 0x00000000000061010000000000000e0000000000000000000000000000000000
kouruto_tiger_woman_face_2 = 0x000000003f0061310000000000000fff00000000000000000000000000000000

kouruto_cow_woman_face_1 = 0x00000000000071410000000000000e0000000000000000000000000000000000
kouruto_cow_woman_face_2 = 0x000000003f0081710000000000000fff00000000000000000000000000000000

kouruto_sheep_woman_face_1 = 0x00000000000091810000000000000e0000000000000000000000000000000000
kouruto_sheep_woman_face_2 = 0x000000003f0091b10000000000000fff00000000000000000000000000000000

kouruto_deer_woman_face_1 = 0x000000000000a1c10000000000000e0000000000000000000000000000000000
kouruto_deer_woman_face_2 = 0x000000003f00b1f10000000000000fff00000000000000000000000000000000

kouruto_rabbit_woman_face_1 = 0x000000000000c2010000000000000e0000000000000000000000000000000000
kouruto_rabbit_woman_face_2 = 0x000000003f00d2310000000000000fff00000000000000000000000000000000

kouruto_dog_woman_face_1 = 0x000000000000e2410000000000000e0000000000000000000000000000000000
kouruto_dog_woman_face_2 = 0x000000003f00f2710000000000000fff00000000000000000000000000000000

kouruto_fox_woman_face_1 = 0x00000000000102810000000000000e0000000000000000000000000000000000
kouruto_fox_woman_face_2 = 0x000000003f0112b10000000000000fff00000000000000000000000000000000

kouruto_cat_woman_face_1 = 0x00000000000122c10000000000000e0000000000000000000000000000000000
kouruto_cat_woman_face_2 = 0x000000003f0132f10000000000000fff00000000000000000000000000000000


nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

east_face_younger_1 = 0x000000003f00c01436db8db6db61b6db00000000001c36db0000000000000000
east_face_young_1   = 0x00000007ff00c01436db8d96dd61b86300000000001c36db0000000000000000
east_face_middle_1  = 0x000000003f00900f36db8db6db61b6db00000000001c36db0000000000000000
east_face_old_1     = 0x0000000fff00a00436db8d96dd61b86300000000001c36db0000000000000000
east_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

east_face_younger_2 = 0x000000003f00c0c136db8db6db61b6db00000000001c36db0000000000000000
east_face_young_2   = 0x00000007ff00c14536db8d96dd61b86300000000001c36db0000000000000000
east_face_middle_2  = 0x000000003f00900836db8db6db61b6db00000000001c36db0000000000000000
east_face_old_2     = 0x000000003f00a5c136db8db6db61b6db00000000001c36db0000000000000000
east_face_older_2   = 0x0000000fff00b14536db8d96dd61b86300000000001c36db0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops_npc = [
   ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END




#######################################################通用NPC体系##########################################
##
####这个体系内的NPC包括玩家和领主的部队NPC，野怪领主，佣兵团长和剧情角色等，所有人共用一套系统，能在不同身份间互相转化。

########骑士团人物
##
#骑士团团长
  ["knight_master_1_1",  "Margot Adler",  "Margot Adler",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_1_2",  "Sandnan Carson",  "Sandnan Carson",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_1_3",  "Terjed Bach",  "Terjed Bach",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_1_4",  "Rachel Cannon",  "Rachel Cannon",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_1_5",  "Lavahan Parks",  "Lavahan Parks",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_master_2_1",  "Enid",  "Enid",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_2_2",  "Gargastaff",  "Gargastaff",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_2_3",  "Otiret",  "Otiret",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_2_4",  "Leticia",  "Leticia",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_master_3_1",  "Schimbari",  "Schimbari",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_3_2",  "Minganwendus",  "Minganwendus",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_master_4_1",  "Nickles Hagelberg",  "Nickles Hagelberg",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_4_2",  "Hardy Jonson",  "Hardy Jonson",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_master_5_1",  "Alianrod Leu",  "Alianrod Leu",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_5_2",  "dual-door",  "dual-door",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_5_3",  "Ruthra Chaney",  "Ruthra Chaney",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_5_4",  "Thomson Reard",  "Thomson Reard",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_master_5_5",  "Samatino Edwards",  "Samatino Edwards",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],


  ["knight_master_7_1",  "Zachary Iverson",  "Zachary Iverson",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_master_8_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],


#骑士团队长
  ["knight_captain_1_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_1_2",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_1_3",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_1_4",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_1_5",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_captain_2_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_2_2",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_2_3",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_2_4",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_captain_3_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_3_2",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_captain_4_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_4_2",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_captain_5_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_5_2",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_5_3",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_5_4",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["knight_captain_5_5",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],


  ["knight_captain_7_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],

  ["knight_captain_8_1",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],



########冒险者协会人物
##
  ["sterling_branch_president","Sterling Branch President","Sterling Branch President", #斯特林分会长
   tf_hero,
   0,reserved, fac_adventurers_association,
   [itm_nanfang_cijian, itm_nobleman_outfit, itm_leather_boots, itm_leather_gloves],
   str_23 | agi_26 | int_49 | cha_17|level(48),wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (420) | wp_crossbow (420) | wp_throwing (420),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_7|knows_athletics_6|knows_riding_8|knows_horse_archery_8|knows_looting_8|knows_trainer_9|knows_tracking_8|knows_tactics_9|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_14|knows_wound_treatment_9|knows_surgery_9|knows_first_aid_10|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_12|knows_study_7|knows_prisoner_management_9|knows_leadership_10|knows_trade_10,
   0x0000000fe20415c5545c91e6e38d2d1a00000000001daadd0000000000000000],

  ["matton_adams","Matton Adams","Matton Adams", #马顿·亚当斯
   tf_hero,
   0,reserved, fac_adventurers_association,
   [itm_stud_decorated_skin_battle_shield, itm_silver_plated_sword, itm_hunting_crossbow, itm_bolts, itm_jugdement_light_armor, itm_leather_boots, itm_leather_gloves, itm_heise_ma],
   str_17 | agi_14 | int_14 | cha_11|level(25),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (150) | wp_crossbow (200) | wp_throwing (150),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_3|knows_looting_2|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_6|knows_devout_3|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   0x000000003f08300f545e71190a25328a00000000001d34940000000000000000],



########权厄之秤人物
##
  ["anne_laure_deschamps","Anne Laure Deschamps","Baron Anne Laure Deschamps", #安妮-洛尔·德尚男爵
   tf_hero|tf_female,
   0,reserved, fac_outlaws_libra,
   [itm_libra_fan_shaped_shield, itm_powell_noble_sword, itm_hongjing_qingbanlianfuhe_jia, itm_steel_leather_boot, itm_nvshi_shoutao, itm_red_noble_shirt, itm_leather_boots],
   str_21 | agi_20 | int_22 | cha_18|level(40), wp_one_handed (270) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_8|knows_trainer_6|knows_tracking_8|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_8|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_7|knows_array_arrangement_4|knows_memory_9|knows_study_3|knows_devout_1|knows_prisoner_management_10|knows_leadership_10|knows_trade_10,
   0x000000001d04000418dcb21d0bc9a72600000000000dbaf20000000000000000],

  ["marcel_chansonier","Marcel Chansonier","Marcel Chansonier", #马塞尔·夏索尼埃
   tf_hero,
   0,reserved, fac_outlaws_libra,
   [itm_libra_fan_shaped_shield, itm_powell_noble_sword, itm_hongjing_qingbanlianfuhe_jia, itm_steel_leather_boot, itm_nvshi_shoutao, itm_red_noble_shirt, itm_leather_boots],
   str_21 | agi_20 | int_22 | cha_18|level(40), wp_one_handed (270) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_8|knows_trainer_6|knows_tracking_8|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_8|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_7|knows_array_arrangement_4|knows_memory_9|knows_study_3|knows_devout_1|knows_prisoner_management_10|knows_leadership_10|knows_trade_10,
   0x000000001d04000418dcb21d0bc9a72600000000000dbaf20000000000000000],






  ["dark_owl_eloise","Dark Owl Eloise","Eloise", #暗枭埃洛伊斯
   tf_hero|tf_female,
   0,reserved, fac_kingdom_4,
   [itm_tempestminion_helmet, itm_saintess_boot, itm_fenzhi_huzhishoutao, itm_phoenix_splendid_bow, itm_weeping_blood_arrow, itm_aquila_relief_shield, itm_silver_winged_noble_sword, itm_confederation_female_cavalry_armor],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3, 
   0x00000001b600001e2ca1cd6d136a24b600000000001c928c0000000000000000],

  ["zela","Zela","Zela", #泽拉
   tf_hero|tf_female,
   0, 0, fac_slavers,
   [itm_extra_long_shovel_axe, itm_great_long_bardiche, itm_battle_axe, itm_war_axe, itm_xihai_dingshikui, itm_westcoast_covered_chain_armor_robe, itm_mail_chausses, itm_leather_gloves, itm_long_bardiche],
   str_32 | agi_29 | int_14 | cha_15|level(45), wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (430) | wp_crossbow (430) | wp_throwing (430),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_6|knows_athletics_8|knows_riding_4|knows_horse_archery_6|knows_looting_5|knows_trainer_5|knows_tracking_4|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_2, 
   0x00000001870c10244b1986371b8cb4d400000000001db8930000000000000000],

  ["tailless_aruna","Tailless Aruna","Aruna", #“无尾斗士”阿茹娜
   tf_hero|tf_female,
   0, 0, fac_slavers,
   [itm_extra_long_shovel_axe, itm_great_long_bardiche, itm_battle_axe, itm_war_axe, itm_xihai_dingshikui, itm_westcoast_covered_chain_armor_robe, itm_mail_chausses, itm_leather_gloves, itm_long_bardiche],
   str_32 | agi_29 | int_14 | cha_15|level(45), wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (430) | wp_crossbow (430) | wp_throwing (430),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_6|knows_athletics_8|knows_riding_4|knows_horse_archery_6|knows_looting_5|knows_trainer_5|knows_tracking_4|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_2, 
   0x00000001b600001e2ca1cd6d136a24b600000000001c928c0000000000000000],

  ["lance_protector_francois_beaumont","Lance Protector Francois Beaumont","Francois Beaumonts", #护枪官弗朗索瓦·博蒙
   tf_hero,
   0, 0, fac_kingdom_1,
   [itm_blue_flower_skoutarion, itm_nameless_goddess_silverwing_lance, itm_qishi_dingtouchui, itm_qishi_danshouzhanfu, itm_rodriguez_bucket_helmet, itm_dolphin_plate_chain_composite_armor, itm_iron_greaves, itm_gauntlets, itm_dolphin_chain_armor_plain_horse, itm_nobleman_outfit, itm_woolen_hose, itm_leather_gloves],
   str_31 | agi_26 | int_15 | cha_15|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_6|knows_tracking_2|knows_tactics_7|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_1|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   0x000000018e04240f5365b1565d642b5500000000001dc51b0000000000000000],

  ["lance_protector_antoine_moro","Lance Protector Antoine Moro","Antoine Moro", #护枪官安托万.莫罗
   tf_hero,
   0, 0, fac_commoners,
   [itm_qishi_danshouzhanfu, itm_harvest_goddess_portrait_lance, itm_blue_flower_skoutarion, itm_rodriguez_bucket_helmet, itm_lanse_zaoqi_banjia, itm_plate_boots, itm_scale_gauntlets, itm_dolphin_chain_armor_plain_horse],
   str_56 | agi_50 | int_37 | cha_33|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_11|knows_riding_12|knows_horse_archery_13|knows_looting_6|knows_trainer_10|knows_tracking_7|knows_tactics_9|knows_pathfinding_7|knows_spotting_8|knows_inventory_management_9|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_5|knows_persuasion_9|knows_array_arrangement_6|knows_memory_12|knows_study_7|knows_devout_8|knows_prisoner_management_9|knows_leadership_12|knows_trade_6,
   0x00000001850030073cda72432c8934dc00000000001db4a40000000000000000],

  ["yannick_village_elder", "Yannick", "Yannick", #扬尼克村长
   tf_hero,
   0, 0, fac_commoners,
   [itm_nanfang_duanjian, itm_robe, itm_ankle_boots],
   str_30 | agi_26 | int_17 | cha_18|level(46),wp_one_handed (425) | wp_two_handed (425) | wp_polearm (425) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_7|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_7|knows_trade_5,
   0x00000001bc00324855638cc965a938af00000000001d49ac0000000000000000],


  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],

  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],


##_____________________________________________________________________undead related_________________________________________________________________________________
  ["beheading_necromancer","Beheading Necromancer Rita ZenI","Rita ZenI",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],#for mozu charpter two and undead prologue
  ["inflammation_necromancer","Inflammation Necromancer Fernan Dubois","Fernan Dubois",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["cyan_necromancer","Cyan Necromancer Leng Zhushu","Leng Zhushu",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["armor_necromancer","Armor Necromancer Federico Tonatore","Federico Tonatore",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["shower_necromancer","Shower Necromancer Ashley Nessa","Ashley Nessa",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["shattered_necromancer","Shattered Necromancer Lild Hansen","Lild Hansen",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["element_necromancer","Element Necromancer Jacques Duran","Jacques Duran",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["power_necromancer","Power Necromancer Calvin bilbohm","Calvin bilbohm",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["shadow_necromancer","Shadow Necromancer Xazo Broder","Xazo Broder",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["storm_necromancer","Storm Necromancer Dave Bruno","Dave Bruno",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["defend_necromancer","Defend Necromancer Dariachi","Dariachi",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],

#walker clique
  ["turbid_necromancer","Turbid Necromancer Bazel Babbitt","Bazel Babbitt",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_80 | agi_80 | int_47 | cha_12|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_9|knows_power_draw_4|knows_weapon_master_10|knows_shield_5|knows_athletics_8|knows_riding_10|knows_horse_archery_6,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],

  ["assistant_1","Assistant Chechen","Chechen",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_2","Assistant Carter","Carter",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_3","Assistant Bizier","Bizier",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_4","Assistant Bowen","Bowen",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_5","Assistant Azir","Azir",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_6","Assistant Bradleyk","Bradleyk",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_7","Assistant Osmon","Osmon",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["assistant_8","Assistant Luo Ping","Luo Ping",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],

  ["apprentice_1","Apprentice Aifen","Aifen",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_2","Apprentice Steven","Steven",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_3","Apprentice Biyole","Biyole",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_4","Apprentice Fay","Fay",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_5","Apprentice Zhang Jing","Zhang Jing",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_6","Apprentice Milian","Milian",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_7","Apprentice Nimisis","Nimisis",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_8","Apprentice Shendemet","Shendemet",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_9","Apprentice Andy","Andy",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_10","Apprentice Gaby","Gaby",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_11","Apprentice Jimmy","Jimmy",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_12","Apprentice Liu Senmiao","Liu Senmiao",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_13","Apprentice Nusanha","Nusanha",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_14","Apprentice Tumen Wure","Tumen Wure",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_15","Apprentice IL","IL",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],
  ["apprentice_16","Apprentice Crius","Crius",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],

  ["reception","Reception Chagan","Chagan",tf_pretty_female|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_pilgrim_disguise, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2],
   str_16 | agi_21 | int_19 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000, 
0x00000001f20c958f1916d632e271ead800000000001eb8e30000000000000000],#for undead base



  ["simple_npc_end","simple_npc_end","simple_npc_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     


############################################简单NPC结束#####################################


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],


#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra



#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Enghe","Enghe",tf_hero|tf_female, 0, reserved, fac_commoners,[],
   str_21|agi_18|int_9|cha_12|level(25),wp_one_handed (270) | wp_two_handed (210) | wp_polearm (210) | wp_archery (330) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_7|knows_power_strike_6|knows_power_draw_7|knows_weapon_master_3|knows_shield_3|knows_athletics_4|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_2|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_1|knows_persuasion_2|knows_prisoner_management_3|knows_leadership_4|knows_trade_3, 
   0x00000005800C300636998314E3A5E75C00000000001D468B0000000000000000],
  ["npc2","Amily","Amily", tf_pretty_female|tf_hero, 0,reserved, fac_commoners,[],
   str_21 | agi_27 | int_30 | cha_19|level(30),wp_one_handed (270) | wp_two_handed (230) | wp_polearm (270) | wp_archery (270) | wp_crossbow (300) | wp_throwing (175),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_4|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_5|knows_trainer_1|knows_tracking_2|knows_tactics_2|knows_spotting_5|knows_leadership_3,
   0x0000000F400020050000000000000EDB00000000000000000000000000000000],
  ["npc3","Apry","Apry",tf_hero|tf_female, 0, reserved, fac_commoners,[],
   str_13 | agi_10 | int_15 | cha_12|level(5),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_3|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_leadership_2|knows_trade_8,
   0x00000000000010044348A9371280B28D00000000001D28810000000000000000],
  ["npc4","Fanlentina","Fanlentina", #范伦汀娜
   tf_hero|tf_special_female, 
   0, reserved,  fac_commoners,
   [itm_powell_noble_sword, itm_red_dress, itm_leather_boots, itm_nvshi_shoutao],
   str_6|agi_5|int_54|cha_37|level(5), wp_one_handed (30) | wp_two_handed (20) | wp_polearm (20) | wp_archery (20) | wp_crossbow (30) | wp_throwing (20),
   knows_ironflesh_1|knows_weapon_master_1|knows_riding_1|knows_horse_archery_1|knows_tactics_4|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_5|knows_persuasion_4|knows_array_arrangement_3|knows_memory_15|knows_study_8,
   0x0000000000001082000000000000000000000000000000000000000000000000],
  ["npc5","Sadi","Sadi",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_21 | agi_32 | int_17 | cha_10|level(30),wp_one_handed (370) | wp_two_handed (75) | wp_polearm (240) | wp_archery (75) | wp_crossbow (75) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_8|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_7|knows_shield_7|knows_athletics_7|knows_riding_4|knows_horse_archery_2|knows_looting_2|knows_trainer_2|knows_tracking_10|knows_tactics_2|knows_pathfinding_5|knows_spotting_8|knows_inventory_management_2|knows_persuasion_7|knows_prisoner_management_3|knows_leadership_8|knows_trade_3,
   0x00000000000C000102D98315DB61E45C00000000001C468B0000000000000000],
  ["npc6","Odungova","Odungova",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_26 | agi_18 | int_12 | cha_15 |level(30),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_7|knows_looting_9|knows_trainer_2|knows_tracking_6|knows_tactics_2|knows_pathfinding_8|knows_spotting_6|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_1|knows_leadership_4|knows_trade_2,
  0x000000001E10300428E3842D1C61369500000000001D28FC0000000000000000],
  ["npc7","Qester","Qester",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_30 | agi_28 | int_18 | cha_16 |level(35), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_9|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_7|knows_shield_7|knows_athletics_6|knows_riding_7|knows_horse_archery_7|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_2|knows_persuasion_3|knows_prisoner_management_3|knows_leadership_4|knows_trade_1,
   0x0000000034042006668965A515224A8D00000000001E589A0000000000000000],
  ["npc8","Caisiale","Caisiale",tf_hero|tf_pretty_female, 0, reserved,  fac_commoners,[],
   str_28|agi_21|int_21|cha_16|level(35),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100) | wp_firearm (350),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_7|knows_athletics_6|knows_riding_7|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_5|knows_engineer_5|knows_persuasion_4|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   0x000000003F0040030000000000000E3800000000000000000000000000000000],
  ["npc9","Alexia","Alexia",tf_hero|tf_pretty_female, 0, reserved,  fac_commoners,[],
   str_24|agi_35|int_18|cha_30|level(35),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_10|knows_power_strike_9|knows_power_draw_9|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_2|knows_horse_archery_3|knows_trainer_3|knows_tracking_2|knows_tactics_2|knows_pathfinding_5|knows_spotting_4|knows_persuasion_2|knows_prisoner_management_4|knows_leadership_3|knows_trade_1,
   0x00000000000010060000000000000F3300000000000000000000000000000000],
  ["npc10","Laurie","Laurie",#劳瑞
   tf_hero|tf_special_female, 
   0, reserved,  fac_commoners,
   [itm_fighting_pick, itm_tabard, itm_leather_boots, itm_silver_glass],
   str_26 | agi_25 | int_24 | cha_18|level(45), wp_one_handed (400) | wp_two_handed (300) | wp_polearm (300) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_6|knows_athletics_11|knows_riding_11|knows_horse_archery_12|knows_looting_10|knows_trainer_5|knows_tracking_12|knows_tactics_4|knows_pathfinding_12|knows_spotting_13|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_5|knows_persuasion_6|knows_array_arrangement_5|knows_memory_8|knows_study_4|knows_devout_2|knows_prisoner_management_10|knows_leadership_4|knows_trade_10,
   0x000000000c003104000000000000000000000000000000000000000000000000],
  ["npc11","Lilian","Lilian",#丽莲
   tf_hero|tf_special_female, 
   0, reserved,  fac_commoners,
   [itm_shield_heater_of_element, itm_dragon_blood_sorcery_lance, itm_elemental_ranger_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai],
   str_33 | agi_30 | int_38 | cha_24|level(48),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_8|knows_persuasion_8|knows_array_arrangement_8|knows_memory_11|knows_study_12|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x000000000b0020c3000000000000000000000000000000000000000000000000, 0x000000000b0020c3000000000000000000000000000000000000000000000000],
  ["npc12","Su Budao","Su Budao",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_38 | agi_18 | int_9 | cha_7|level(25),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_2|knows_athletics_2|knows_shield_1|knows_riding_4|knows_horse_archery_3|knows_trainer_3|knows_spotting_1|knows_prisoner_management_2|knows_leadership_5,
   0x00000000280C4007171689C51DA122AD00000000001CE8630000000000000000],
  ["npc13","Meroy","Meroy",tf_hero|tf_pretty_female, 0, reserved,  fac_commoners,[itm_strange_great_sword, itm_siwangwuzhejia, itm_dancer_veil, itm_fenzhi_jiaqiangshoutao, itm_wuzhe_pixue, itm_qizhi_feidao],
   str_57 | agi_63 | int_30 | cha_60|level(40),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_11|knows_power_strike_14|knows_power_throw_13|knows_weapon_master_10|knows_shield_5|knows_athletics_10|knows_riding_4|knows_horse_archery_4|knows_looting_2|knows_trainer_3|knows_tracking_10|knows_tactics_4|knows_spotting_10|knows_persuasion_10,
   0x000000090F0030020000000000000F3300000000000000000000000000000000],
  ["npc14","Pelop","Pelop",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_23|agi_28|int_27|cha_20|level(35),wp(350),
   knows_ironflesh_9|knows_power_strike_10|knows_power_throw_9|knows_power_draw_7|knows_weapon_master_7|knows_shield_6|knows_athletics_4|knows_riding_5|knows_horse_archery_6|knows_trainer_5|knows_tactics_3|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_2|knows_persuasion_1|knows_prisoner_management_1|knows_leadership_5,
   0x00000000000010017348A9371280B28D00000000001D28810000000000000000],
  ["npc15","Vivian","Vivian",tf_hero|tf_zombie, 0, reserved,  fac_commoners,[],
   str_35 | agi_35 | int_19 | cha_17|level(35),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (450) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_7|knows_shield_7|knows_athletics_7|knows_looting_3|knows_trainer_2|knows_tracking_1|knows_tactics_4|knows_pathfinding_1|knows_spotting_1|knows_wound_treatment_8|knows_surgery_7|knows_first_aid_8|knows_persuasion_4|knows_prisoner_management_1|knows_leadership_5,
   0x0000000F2E1021862B4B9123594EAB5300000000001D55360000000000000000],
  ["npc16","Lei Lisi","Lei Lisi",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_21 | agi_18 | int_10 | cha_10|level(20),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (280) | wp_archery (150) | wp_crossbow (280) | wp_throwing (120) | wp_firearm (530),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_2|knows_horse_archery_1|knows_looting_4|knows_trainer_1|knows_tracking_8|knows_tactics_4|knows_pathfinding_2|knows_spotting_7|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_2|knows_persuasion_4|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   0x00000000000060027308A9501289B28D00000000001C24810000000000000000],
  ["npc17","Michelia","Michelia",tf_hero|tf_pretty_female, 0, reserved,  fac_commoners,[],
   str_28 | agi_30 | int_12 | cha_16|level(35),wp_one_handed (350) | wp_two_handed (200) | wp_polearm (200) | wp_archery (100) | wp_crossbow (500) | wp_throwing (200),
   knows_ironflesh_10|knows_power_strike_9|knows_weapon_master_7|knows_shield_8|knows_athletics_6|knows_trainer_4|knows_tactics_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_6|knows_prisoner_management_1|knows_leadership_6|knows_trade_1,
   0x00000000000020030000000000000F3300000000000000000000000000000000],
  ["npc18","Isidor","Isidor",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_15 | agi_12 | int_6 | cha_6|level(10),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_1|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_2|knows_spotting_1|knows_inventory_management_4|knows_first_aid_2|knows_trade_2,
   0x00000000330010027308A9501285B28D00000000001E24810000000000000000],
  ["npc19","Mayvis","Mayvis",tf_hero|tf_female, 0, reserved,  fac_commoners,[itm_pilgrim_disguise, itm_yinse_xue, itm_faceless_mask],
   str_38 | agi_25 | int_23 | cha_30|level(35),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_8|knows_power_draw_10|knows_weapon_master_8|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_7|knows_trainer_3|knows_spotting_5|knows_persuasion_5|knows_prisoner_management_2|knows_leadership_6,
   0x00000000330000017308A9501281B28D00000000001E24810000000000000000],
  ["npc20","Sabina","Sabina",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_26| agi_18 | int_14 | cha_15|level(30),wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (120) | wp_crossbow (95) | wp_throwing (260),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_4|knows_riding_7|knows_athletics_7|knows_horse_archery_4|knows_shield_3|knows_looting_5|knows_trainer_2|knows_tactics_4|knows_prisoner_management_5|knows_leadership_4,
   0x00000000330020017048A954168412BC00000000001D24810000000000000000],
  ["npc21","Ouyang Mingna","Ouyang Mingna",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_27 | agi_19 | int_12 | cha_21|level(35),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (500) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (350),
   knows_ironflesh_10|knows_power_strike_11|knows_weapon_master_8|knows_shield_6|knows_athletics_5|knows_horse_archery_4|knows_riding_7|knows_trainer_4|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_4|knows_persuasion_8|knows_prisoner_management_3|knows_leadership_8|knows_trade_3,
   0x00000000000050014308A9501280B28D00000000001C24810000000000000000],
  ["npc22","Ai Miye","Ai Miye",tf_hero|tf_female, 0, reserved,  fac_commoners,[],
   str_14 | agi_15 | int_30 | cha_24|level(10),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180) | wp_firearm (180),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_2|knows_shield_2|knows_athletics_4|knows_horse_archery_2|knows_riding_2|knows_trainer_1|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_7|knows_persuasion_10|knows_prisoner_management_2|knows_leadership_6|knows_trade_1,
   0x00000000330070030048A9541480921000000000001DA4810000000000000000],


#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Krorons Seventh",  "Krorons Seventh",  tf_hero, 0,reserved,  fac_kingdom_1,
[],
   str_30 | agi_30 | int_18 | cha_36|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_3|knows_looting_6|knows_trainer_7|knows_tracking_4|knows_tactics_9|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_6|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000, 0x000000018000300136db91b6db41b6db00000000001cb69b0000000000000000],
  ["kingdom_2_lord",  "Proloc Sir Sinzion",  "Sir Sinzion",  tf_hero|tf_elf, 0,reserved,  fac_kingdom_2,
[], 
      str_25 | agi_50 | int_60 | cha_60|level(55),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (800) | wp_crossbow (100) | wp_throwing (100), knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_15|knows_weapon_master_10|knows_shield_4|knows_athletics_15|knows_riding_9|knows_horse_archery_10|knows_looting_6|knows_trainer_8|knows_tracking_4|knows_tactics_10|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_8|knows_persuasion_8|knows_prisoner_management_8|knows_leadership_15|knows_trade_3,
0x0000000FD60000010000000000000E6F00000000000000000000000000000000, 0x0000000FD60000010000000000000E6F00000000000000000000000000000000],
  ["kingdom_3_lord",  "Agudamu Khan",  "Agudamu",  tf_hero, 0,reserved,  fac_kingdom_3,
[],
         str_53 | agi_15 | int_15 | cha_15|level(45),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (120) | wp_crossbow (50) | wp_throwing (50), knows_ironflesh_15|knows_power_strike_14|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_7|knows_horse_archery_1|knows_looting_10|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_1|knows_prisoner_management_4|knows_leadership_7|knows_trade_1,
0x0000000CEE0051CC44BE2D14D370C65C00000000001ED6DF0000000000000000, 0x0000000B3F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000],
  ["kingdom_4_lord",  "Emperor Evanjielin Queentin",  "Evanjielin Queentin",  tf_hero|tf_female, 0,reserved,  fac_kingdom_4,
[],
                     str_28 | agi_20 | int_21 | cha_18|level(45),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (120) | wp_crossbow (100) | wp_throwing (280), knows_ironflesh_8|knows_power_strike_7|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_5|knows_looting_6|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_4|knows_persuasion_8|knows_prisoner_management_6|knows_leadership_12|knows_trade_2,
0x00000005ec10000106666a172c66173500000000001cd5260000000000000000, 0x00000005ec10000106666a172c66173500000000001cd5260000000000000000],
  ["kingdom_5_lord",  "Pontiff Consus Third",  "Consus Third",  tf_hero, 0,reserved,  fac_kingdom_5,
[],
                     str_63 | agi_54 | int_50 | cha_63|level(60),wp_one_handed (700) | wp_two_handed (700) | wp_polearm (700) | wp_archery (700) | wp_crossbow (700) | wp_throwing (700), knows_ironflesh_15|knows_power_strike_14|knows_power_throw_14|knows_power_draw_14|knows_weapon_master_15|knows_shield_15|knows_athletics_15|knows_riding_14|knows_horse_archery_13|knows_looting_7|knows_trainer_10|knows_tracking_10|knows_tactics_10|knows_pathfinding_10|knows_spotting_10|knows_inventory_management_10|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_8|knows_engineer_10|knows_persuasion_8|knows_prisoner_management_10|knows_leadership_15|knows_trade_6,
0x0000000E80044004368D4D490A85A6DA00000000001CC6EC0000000000000000, 0x0000000E80044004368D4D490A85A6DA00000000001CC6EC0000000000000000],
  ["kingdom_6_lord",  "Emperor Ouyang Chongming",  "Ouyang Chongming",  tf_hero, 0,reserved,  fac_kingdom_6,
[],
                      str_45 | agi_35 | int_25 | cha_34|level(50),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500), knows_ironflesh_13|knows_power_strike_14|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_8|knows_athletics_8|knows_riding_9|knows_horse_archery_8|knows_looting_9|knows_trainer_10|knows_tracking_3|knows_tactics_8|knows_pathfinding_6|knows_spotting_3|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_5|knows_persuasion_4|knows_prisoner_management_5|knows_leadership_15|knows_trade_3,
0x00000006FF04910844DBB5692501469D00000000001CD4630000000000000000, 0x00000006FF04910844DBB5692501469D00000000001CD4630000000000000000],
  ["kingdom_7_lord", "Grand Duke Siegfried Starkhook", "Siegfried Starkhook", tf_hero, 0,reserved, fac_kingdom_7,
[],
                      str_45 | agi_30 | int_25 | cha_27|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (100) | wp_crossbow (200) | wp_throwing (450), knows_ironflesh_10|knows_power_strike_12|knows_power_throw_9|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_11|knows_riding_3|knows_horse_archery_3|knows_looting_7|knows_trainer_7|knows_tracking_2|knows_tactics_5|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_4|knows_persuasion_3|knows_prisoner_management_3|knows_leadership_15|knows_trade_10,
0x00000006FF0430474D58B5692595469D00000000001CD4630000000000000000, 0x00000006FF0430474D58B5692595469D00000000001CD4630000000000000000],
  ["kingdom_8_lord", "Consul Batista", "Batista", tf_hero, 0,reserved, fac_kingdom_8,
[],  
                     str_30 | agi_32 | int_25 | cha_27|level(45),wp_one_handed (400) | wp_two_handed (200) | wp_polearm (200) | wp_archery (100) | wp_crossbow (550) | wp_throwing (200), knows_ironflesh_10|knows_power_strike_9|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_7|knows_shield_9|knows_athletics_7|knows_riding_3|knows_horse_archery_3|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_6|knows_persuasion_4|knows_prisoner_management_3|knows_leadership_12|knows_trade_1,
0x00000001C00443854D5BB5692289469D00000000001CD4630000000000000000, 0x00000001C00443854D5BB5692289469D00000000001CD4630000000000000000],


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top


##########################################################普威尔联合王国##########################################################
##
  ["knight_1_1", "Duke Edmond Rodriguez", "Edmond Rodriguez", #埃德蒙德·罗德里格斯公爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_dragon_blood_sorcery_lance, itm_shield_heater_of_element, itm_changmian_lanyu_jianzuikui, itm_element_plate_chain_composite_armor, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_dolphin_chain_armor_plain_horse, itm_blue_noble_shirt, itm_leather_boots],
   str_35 | agi_28 | int_21 | cha_19|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x0000000abf08a1cf42ab76db357ac31200000000001da3690000000000000000],
  ["knight_1_2", "Duke Jeremie Ignaz", "Jeremie Ignaz", #伊格纳兹公爵
   tf_hero, 
   0, reserved,  fac_kingdom_1,
   [itm_qishi_dingtouchui, itm_dragon_god_black_shield, itm_mogang_zhuixingqiang, itm_hongyu_zhumiankui, itm_dragonblood_knight_plate, itm_duangang_banjiaxue, itm_mogang_shalouhushou, itm_hongbanjia_longxuama, itm_red_noble_shirt, itm_leather_boots],
   str_43 | agi_34 | int_20 | cha_19|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_2|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   0x0000000c000c32c62762d6acdcd6559400000000001cb73d0000000000000000],
  ["knight_1_3", "Duke Olivier Patrick", "Olivier Patrick", #派崔克公爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield, itm_courtly_outfit, itm_leather_boots],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x0000000cb7002284330e8b5b276aa2f400000000001c58780000000000000000],
  ["knight_1_4", "Duke Raoul Mahmoud", "Raoul Mahmoud", #马哈茂德公爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield, itm_rich_outfit, itm_leather_boots],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c370c13544464a9ca5f4e453600000000001f3ac30000000000000000],
  ["knight_1_5", "Marquis Valentin Garcia", "Valentin Garcia", #瓦伦汀·加西亚侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_gangying_qishiqiang, itm_dark_oath_plate, itm_havathang, itm_dark_oath_helmet, itm_dark_oath_shoe, itm_anhei_qingshi_moshouma1, itm_mozujundao, itm_demon_fan_shaped_shield,itm_dark_oath_hand, itm_red_noble_shirt, itm_leather_boots],
   str_50 | agi_43 | int_30 | cha_3|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_14|knows_power_draw_14|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_9|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_7|knows_tactics_7|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_7|knows_array_arrangement_7|knows_memory_12|knows_study_12|knows_devout_12|knows_prisoner_management_9|knows_leadership_9|knows_trade_7,
    0x0000000c000064856b2b6e2ae291992b00000000001da6620000000000000000],
  ["knight_1_6", "Count Julian Thorne", "Julian Thorne", #于里安·索恩德伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield, itm_rich_outfit, itm_leather_boots],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c00080387184374c6a396a8e500000000001d57e20000000000000000],
  ["knight_1_7", "Marquis Stefan Exupery", "Stefan Exupery", #斯特凡·埃克苏佩里侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield, itm_leather_noble_gown, itm_leather_boots],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x0000000b8000028458d4ae9a9bae5b1400000000001cd8940000000000000000],
  ["knight_1_8", "Count Rosa Manpatton", "Rosa Manpatton", #萝萨·曼帕顿伯爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000007f10000034cc8ab5a4dcd9c8b00000000001cc1090000000000000000],
  ["knight_1_9", "Count Cantan Wallov", "Cantan Wallov", #康坦·华洛夫伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_qishi_dingtouchui, itm_dragon_god_black_shield, itm_mogang_zhuixingqiang, itm_hongyu_zhumiankui, itm_dragonblood_knight_plate, itm_duangang_banjiaxue, itm_mogang_shalouhushou, itm_hongbanjia_longxuama, itm_red_noble_shirt, itm_leather_boots],
   str_43 | agi_34 | int_20 | cha_19|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_2|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   0x0000000c0f0803c458739a9a1576199800000000001dc8ab0000000000000000],
  ["knight_1_10", "Marquis Filibel Wincard", "Filibel Wincard", #菲利贝尔·温卡德伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_qishi_dingtouchui, itm_dragon_god_black_shield, itm_mogang_zhuixingqiang, itm_hongyu_zhumiankui, itm_dragonblood_knight_plate, itm_duangang_banjiaxue, itm_mogang_shalouhushou, itm_hongbanjia_longxuama, itm_leather_noble_gown, itm_leather_boots],
   str_43 | agi_34 | int_20 | cha_19|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_2|knows_prisoner_management_6|knows_leadership_8|knows_trade_2,
   0x0000000c0000351027632536dd7236cd00000000001d62f30000000000000000],
  ["knight_1_11", "Marquis Martin Rolschard", "Martin Rolschard", #马丁·罗尔斯查德侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield, itm_rich_outfit, itm_leather_boots],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x00000009010044903a09c54592a196ab00000000001d34dc0000000000000000],
  ["knight_1_12", "Count Waldo Vanderbilt", "Waldo Vanderbilt", #瓦尔多·范德比尔特侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield, itm_courtly_outfit, itm_leather_boots],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c2a0805442b9e71498c8dbaac00000000001d389b0000000000000000],
  ["knight_1_13", "Count Savinian Jurbury", "Savinian Jurbury", #萨维尼安·尤尔伯利伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_sorcery_lance, itm_huijing_qingbanlianfuhe_jia, itm_changmain_hongyu_zhumiankui, itm_red_blue_fan_shaped_shield, itm_yuanzhi_bikai, itm_mail_boots, itm_blue_noble_shirt, itm_leather_boots],
   str_27 | agi_26 | int_18 | cha_19|level(42),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (420) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),    knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_3|knows_memory_7|knows_study_6|knows_devout_3|knows_prisoner_management_7|knows_leadership_8|knows_trade_4, 
   0x0000000c000c30c13928b1c322a5392c00000000001d4c620000000000000000],
  ["knight_1_14", "Marquis Rene Vuitton", "Rene Vuitton", #勒内·威登伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_dragon_blood_sorcery_lance, itm_shield_heater_of_element, itm_changmian_lanyu_jianzuikui, itm_element_plate_chain_composite_armor, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_dolphin_chain_armor_plain_horse, itm_hongse_dianchengpao, itm_leather_boots],
   str_35 | agi_28 | int_21 | cha_19|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x0000000c3f00130532d45213918e25bb00000000001e37630000000000000000],
  ["knight_1_15", "Marquis Raymond Hilton", "Raymond Hilton", #雷蒙·希尔顿侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_qishi_dingtouchui, itm_red_lion_iron_fan_shaped_shield, itm_dragon_blood_sorcery_lance, itm_changmain_hongyu_zhumiankui, itm_crown_knight_plate, itm_zhengshi_banjiaxue, itm_huali_shalouhushou, itm_powell_knight_warhorse, itm_courtly_outfit, itm_leather_boots],
   str_39 | agi_34 | int_25 | cha_30|level(55), wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_13|knows_shield_7|knows_athletics_8|knows_riding_11|knows_horse_archery_11|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_7|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_8|knows_devout_1|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   0x0000000c5c0843034895653b6565886c00000000001e34530000000000000000],


  ["knight_1_16", "Viscount Odile Phoebe", "Odile Phoebe", #奥迪莱·菲比子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_jinshi_zhanbiao, itm_jinshi_zhanbiao, itm_nanfang_shuangshoujian, itm_sarranid_veiled_helmet, itm_powell_south_ligature_plate, itm_sarranid_boots_d, itm_lamellar_gauntlets, itm_red_noble_shirt, itm_leather_boots],
   str_33 | agi_22 | int_17 | cha_18|level(47),wp_one_handed (470) | wp_two_handed (470) | wp_polearm (470) | wp_archery (470) | wp_crossbow (470) | wp_throwing (470),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_7|knows_athletics_7|knows_riding_4|knows_horse_archery_8|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   0x000000095108144663a1ba3ad456e8fb00000000001eb25a0000000000000000],
  ["knight_1_17", "Count Lafarge Rex", "Lafarge Rex", #拉法齐·雷克斯伯爵
   tf_hero, 
   0, reserved, fac_kingdom_1, 
   [itm_dragon_hunter_arrow, itm_dragon_hunting_bow, itm_mogang_duanlian, itm_gangshizi_niujiao_dakui, itm_baipao_banlian, itm_iron_greaves, itm_yuanzhi_bikai, itm_hongbaishipijia_ma, itm_black_and_white_skoutarion, itm_hongshizipijia_ma, itm_blue_noble_shirt, itm_leather_boots],
   str_30|agi_27|int_19|cha_19|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_9|knows_power_throw_3|knows_power_draw_7|knows_weapon_master_8|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_7|knows_looting_4|knows_trainer_3|knows_tracking_6|knows_tactics_6|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_8|knows_prisoner_management_5|knows_leadership_7|knows_trade_3,
   0x0000000c010c42c14d9d6918bdb336e200000000001ed6a30000000000000000],
  ["knight_1_18", "Count Justina Rochebas", "Justina Rochebas", #朱斯蒂纳·罗车巴斯伯爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_heavy_lance, itm_gauntlets, itm_hongsejianyi_banlianjia, itm_puweier_lianjia, itm_hongyu_hue_qingbiankui, itm_hongyu_zhumiankui, itm_jinhong_pijia_liema, itm_lance, itm_mail_boots, itm_leather_noble_gown, itm_leather_boots],
   str_26 | agi_22 | int_12 | cha_15|level(40),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_6|knows_devout_3|knows_prisoner_management_7|knows_leadership_8|knows_trade_5, 
   0x00000001ff040030285069beeda1c55c00000000001d45050000000000000000],
  ["knight_1_19", "Viscount Gabrielle Despin", "Gabrielle Despin", #加布里埃勒·迪斯平子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_tab_shield_heater_cav_a, itm_tab_shield_heater_cav_b, itm_tiehuan_danshoujian, itm_hongyu_hue_qingbiankui, itm_coat_of_plates_red, itm_mail_boots, itm_mail_mittens, itm_hongheipijia_ma, itm_heise_ma, itm_courtly_outfit, itm_leather_boots],
   str_26|agi_22|int_14|cha_16|level(40),wp_one_handed (325) | wp_two_handed (325) | wp_polearm (145) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_4|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   0x0000000a5b0012103d9b6d4ba2ada53c00000000001dc1180000000000000000],


#Powell younger knights  
  ["knight_1_20", "Lord Christer Rodriguez", "Christer Rodriguez", #克莉斯特·罗德里格斯勋爵
   tf_hero|tf_special_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_dragon_blood_sorcery_lance, itm_shield_heater_of_element, itm_changmian_lanyu_jianzuikui, itm_element_plate_chain_composite_armor, itm_guanze_banjiaxue, itm_christer_hand, itm_dolphin_chain_armor_plain_horse],
   str_35 | agi_28 | int_21 | cha_19|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x000000000b000041000000000000000000000000000000000000000000000000],
  ["knight_1_21", "Viscount Joachim Ignaz", "Joachim Ignaz", #若阿尚·伊格纳兹子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_heavy_lance, itm_gauntlets, itm_hongsejianyi_banlianjia, itm_puweier_lianjia, itm_hongyu_hue_qingbiankui, itm_hongyu_zhumiankui, itm_jinhong_pijia_liema, itm_lance, itm_mail_boots, itm_hongse_dianchengpao, itm_leather_boots],
   str_26 | agi_22 | int_12 | cha_15|level(40),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_6|knows_devout_3|knows_prisoner_management_7|knows_leadership_8|knows_trade_5, 
   0x0000000fcd0840d24a9b2ab4ac29b33c00000000001db4db0000000000000000],
  ["knight_1_22", "Lord Thierry Patrick", "Thierry Patrick", #蒂埃里·派崔克勋爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield, itm_red_noble_shirt, itm_leather_boots],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x0000000c370c1354546469ca6c4e453500000000001d3ac40000000000000000],
  ["knight_1_23", "Lord Yves Mahmoud", "Yves Mahmoud", #伊夫·马哈茂德勋爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_jinshi_zhanbiao, itm_jinshi_zhanbiao, itm_nanfang_shuangshoujian, itm_sarranid_veiled_helmet, itm_powell_south_ligature_plate, itm_sarranid_boots_d, itm_lamellar_gauntlets, itm_leather_noble_gown, itm_leather_boots],
   str_33 | agi_22 | int_17 | cha_18|level(47),wp_one_handed (470) | wp_two_handed (470) | wp_polearm (470) | wp_archery (470) | wp_crossbow (470) | wp_throwing (470),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_7|knows_athletics_7|knows_riding_4|knows_horse_archery_8|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   0x000000088c0064865ba34e2ae291993b00000000001daa720000000000000000],
  ["knight_1_24", "Lord Gerzavier Garcia", "Gerzavier Garcia", #格扎维埃·加西亚勋爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_mogang_zhuixingqiang, itm_tab_shield_round_e, itm_xihai_wenshikui, itm_lanse_lianjiazhaopao, itm_mail_chausses, itm_scale_gauntlets, itm_blue_noble_shirt, itm_leather_boots],
   str_27 | agi_20 | int_12 | cha_13|level(40),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (340) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_10|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_10|knows_athletics_4|knows_riding_2|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_7|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   0x0000000c0a08038736db74c6a396a8dd00000000001cb8eb0000000000000000],
  ["knight_1_25", "Baron Thomas Thorne", "Thomas Thorne", #托马·索恩德男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_jainyi_changbingfu, itm_fangmian_jianzuikui, itm_mail_boots, itm_gauntlets, itm_honglanpao_banlian, itm_blue_dragon_large_shield, itm_powell_noble_hand_and_a_half_sword, itm_one_handed_battle_axe_c, itm_leather_noble_gown, itm_leather_boots],
   str_26 | agi_23 | int_14 | cha_13|level(42),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (350),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   0x0000000c330855054823ab476449f39e00000000001e756b0000000000000000],
  ["knight_1_26", "Viscount Virgini Exupery", "Virgini Exupery", #维尔日妮·埃克苏佩里子爵
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_1, 
   [itm_birch_crossbow, itm_sorcery_lance, itm_steel_bolts, itm_state_great_helmet, itm_honghuangcheng_banlian, itm_wenli_banjiaxue, itm_yinse_bikai, itm_jinjiu_lianjia_pingyuanma, itm_strengthen_yellow_black_fan_shaped_shield, itm_leather_noble_gown, itm_leather_boots],
    str_25|agi_20|int_15|cha_15|level(41),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_9|knows_athletics_4|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_7|knows_trade_3,
   0x000000003c00001b25238a524ba5233400000000001e66b60000000000000000],
  ["knight_1_27", "Baron Simeon Manpatton", "Simeon Manpatton", #西梅翁·曼帕顿男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_hongyu_zhumiankui, itm_lvlong_lianjaizhaopao, itm_steel_leather_boot, itm_lamellar_gauntlets, itm_hongyipijia_ma, itm_zhanshi_chu, itm_hongwen_qiqiang, itm_shiwenpijia_ma, itm_leather_noble_gown, itm_leather_boots],
   str_26 | agi_23 | int_14 | cha_13|level(42),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   0x0000000ed50045c5365d8565932a8d6c00000000001ec6940000000000000000],
  ["knight_1_28", "Baron Prosper Wallov", "Prosper Wallov", #普罗斯佩耳·华洛夫男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_heavy_mattock, itm_dragon_hunting_bow, itm_fuhe_guokui, itm_puweier_lianjia, itm_mail_chausses, itm_fenzhi_dingshishoutao, itm_dragon_hunter_arrow, itm_dragon_hunter_arrow, itm_dragon_hunter_arrow, itm_dragon_hunter_arrow, itm_hongse_dianchengpao, itm_leather_boots],
   str_27 | agi_28 | int_23 | cha_18|level(43),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (250) | wp_archery (400) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_8|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_4|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_3|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   0x0000000fc0042291396552daa684b72b00000000001e529c0000000000000000],
  ["knight_1_29", "Baron Nathan wincard", "Nathan wincard", #纳坦·温卡德男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_heavy_mattock, itm_qishi_zhongfu, itm_throwing_spears, itm_touguan_toumao, itm_mercenary_knight_helmet, itm_jiaqianglengshi_jia, itm_shengtie_banjiaxue, itm_gauntlets, itm_jarid, itm_throwing_spears, itm_jarid, itm_hongse_dianchengpao, itm_leather_boots],
   str_33|agi_26|int_21|cha_18|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_8|knows_shield_4|knows_athletics_8|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_7|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_3|knows_prisoner_management_4|knows_leadership_7|knows_trade_3,
   0x0000000a000c438338e33238d555b6b300000000001dc91d0000000000000000],


  ["knight_1_30", "Count Louis Rolschard", "Louis Rolschard", #路易·罗尔斯查德伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_birch_crossbow, itm_sorcery_lance, itm_steel_bolts, itm_state_great_helmet, itm_honghuangcheng_banlian, itm_wenli_banjiaxue, itm_yinse_bikai, itm_jinjiu_lianjia_pingyuanma, itm_strengthen_yellow_black_fan_shaped_shield, itm_red_noble_shirt, itm_leather_boots],
    str_25|agi_20|int_15|cha_15|level(41),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_9|knows_athletics_4|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_7|knows_trade_3,
   0x000000096c0c4208395d6ea5118d2b6a00000000001d12db0000000000000000],
  ["knight_1_31", "Baron Audrey Vanderbilt", "Audrey Vanderbilt", #奥德蕾·范德比尔特男爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_arabian_sword_b, itm_stud_decorated_skin_battle_shield, itm_arabian_sword_a, itm_southern_horn_bow, itm_sarranid_mail_coif, itm_khergit_guard_armor, itm_sarranid_boots_c, itm_lamellar_gauntlets, itm_luotuo, itm_nanfang_jian, itm_nanfang_jian],
   str_34 | agi_22 | int_9 | cha_16|level(40),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_4|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_6|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   0x00000001ea081005495a86b64382a70c00000000001dc8c80000000000000000],
  ["knight_1_32", "Viscount Octaf Yulbury", "Octaf Yulbury", #奥克塔夫·尤尔伯利男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_lingjia_pao, itm_flat_topped_helmet, itm_fenzhi_jiaqiangshoutao, itm_one_handed_battle_axe_b, itm_sarranid_axe_a, itm_jianyi_danshoufu, itm_light_throwing_axes, itm_light_throwing_axes, itm_tab_shield_round_d, itm_tab_shield_round_c, itm_tab_shield_round_e, itm_blue_breeze_round_shield, itm_steel_leather_boot, itm_splinted_greaves, itm_leather_noble_gown, itm_leather_boots],
   str_25 | agi_18 | int_12 | cha_9|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (250) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_4|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_7|knows_looting_4|knows_trainer_4|knows_tracking_2|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   0x00000001c00c334568e1ae24c98596f300000000001d3c990000000000000000],
  ["knight_1_33", "Viscount Pivi Vuitton", "Pivi Vuitton", #皮维·威登子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_shield_heater_of_element, itm_dragon_blood_sorcery_lance, itm_changmian_lanyu_jianzuikui, itm_elemental_ranger_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_courtly_outfit, itm_leather_boots],
   str_33 | agi_30 | int_21 | cha_24|level(48),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x00000009c5001302361576cad450d9bc00000000001dc4ec0000000000000000],
  ["knight_1_34", "Lord Yvonne Hilton", "Yvonne Hilton", #伊冯娜·希尔顿勋爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_hongwen_qiqiang, itm_military_cleaver_c, itm_gorgeous_skoutarion, itm_two_handed_cleaver, itm_great_helmet, itm_zongse_lianxiongjia, itm_iron_greaves, itm_scale_gauntlets, itm_hongyipijia_ma],
   str_24|agi_22|int_16|cha_14|level(38),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_1|knows_trainer_4|knows_tracking_3|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_2|knows_prisoner_management_6|knows_leadership_6|knows_trade_3,
   0x00000009c10c00012ab2072a8cadcad300000000001cc5040000000000000000],

  ["knight_1_35", "Marquis Arthur Lefebvre", "Arthur Lefebvre", #亚瑟·莱菲布勒侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_qishi_dingtouchui, itm_dragon_god_black_shield, itm_mogang_zhuixingqiang, itm_hongyu_zhumiankui, itm_dragonblood_knight_plate, itm_duangang_banjiaxue, itm_mogang_shalouhushou, itm_hongbanjia_longxuama, itm_leather_noble_gown, itm_leather_boots],
   str_43 | agi_34 | int_20 | cha_19|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_2|knows_prisoner_management_6|knows_leadership_8|knows_trade_2,
   0x0000000b7800b3806889d3a9168ac73500000000001d52510000000000000000],
  ["knight_1_36", "Count Come Lepez", "Come Lepez", #科莫·洛佩兹伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_dragon_blood_sorcery_lance, itm_shield_heater_of_element, itm_changmian_lanyu_jianzuikui, itm_element_plate_chain_composite_armor, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_dolphin_chain_armor_plain_horse, itm_courtly_outfit, itm_leather_boots, itm_rich_outfit, itm_leather_boots],
   str_35 | agi_28 | int_21 | cha_19|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x00000001b808650e5763a6371c499f2e00000000001dbb130000000000000000],
  ["knight_1_37", "Count Syrius Castel", "Syrius Castel", #塞琉斯·卡斯特尔伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x0000000e3a0045c768ccaac91444c65f00000000001cb51c0000000000000000],
  ["knight_1_38", "Count Automne Mitterrand", "Automne Mitterrand", #奥托尼·密特朗伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield, itm_red_noble_shirt, itm_leather_boots],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x0000000fc000121269744dc8d446372500000000001d1b250000000000000000],
  ["knight_1_39", "Count Tlaloc Guerin", "Tlaloc Guerin", #特拉洛克·盖兰伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield, itm_red_noble_shirt, itm_leather_boots],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000e2704254f6c196d38dc50a53400000000001e36e30000000000000000],
  ["knight_1_40", "Count Alben Faure", "Alben Faure", #阿尔邦·福勒伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield, itm_red_noble_shirt, itm_leather_boots],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000e20000314685152cecbaddf3300000000001e335c0000000000000000],
  ["knight_1_41", "Count Gaston Roux", "Gaston Roux", #加斯东·鲁克斯伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_shield_heater_of_element, itm_dragon_blood_sorcery_lance, itm_changmian_lanyu_jianzuikui, itm_elemental_ranger_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_blue_noble_shirt, itm_leather_boots],
   str_33 | agi_30 | int_21 | cha_24|level(48),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x0000000a22000344271ba9a7af78f66b00000000001d4df30000000000000000],
  ["knight_1_42", "Count Godfrey Vincent", "Godfrey Vincent", #歌德弗鲁瓦·文森伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_yellow_lion_fan_shaped_shield, itm_powell_knight_sword, itm_qinxing_jixingkui1, itm_powell_plate, itm_plate_boots, itm_fangxing_bikai, itm_honghei_lianjia_pingyuanma, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_red_noble_shirt, itm_leather_boots],
   str_29 | agi_25 | int_18 | cha_20|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_7|knows_devout_4|knows_prisoner_management_7|knows_leadership_8|knows_trade_4, 
   0x0000000a270c539337198654d1692d1b00000000001cb6d90000000000000000],
  ["knight_1_43", "Count Guillaume Dupond", "Guillaume Dupond", #纪晓姆·杜朋伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_silver_dragon_fan_shaped_shield, itm_powell_lifeguard_plate, itm_changmain_hongyu_zhumiankui, itm_heise_banlianjiaxue, itm_heise_banlianjiaxue, itm_powell_noble_hand_and_a_half_sword, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_powell_fan_shaped_shield, itm_red_noble_shirt, itm_leather_boots],
   str_30 | agi_30 | int_18 | cha_24|level(45), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50), 
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_1|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_7|knows_devout_4|knows_prisoner_management_3|knows_leadership_7|knows_trade_1, 
   0x0000000e7200038e269c36d9632526f600000000001d32950000000000000000],
  ["knight_1_44", "Marquis Zoe Gautier", "Zoe Gautier", #佐尔·高提耶侯爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_voulge, itm_hongyu_hue_qingbiankui, itm_coat_of_plates_red, itm_mail_boots, itm_mail_mittens, itm_hongheipijia_ma, itm_heise_ma, itm_leather_noble_gown, itm_leather_boots],
   str_25|agi_22|int_14|cha_16|level(39),wp_one_handed (145) | wp_two_handed (145) | wp_polearm (315) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   0x00000001a200200259a450d6dba648cb00000000001e549d0000000000000000],
  ["knight_1_45", "Count Kevin Martinez", "Count Kevin Martinez", #基文·马丁内兹伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_qishi_dingtouchui, itm_red_lion_iron_fan_shaped_shield, itm_dragon_blood_sorcery_lance, itm_changmain_hongyu_zhumiankui, itm_crown_knight_plate, itm_zhengshi_banjiaxue, itm_huali_shalouhushou, itm_powell_knight_warhorse, itm_rich_outfit, itm_leather_boots],
   str_39 | agi_34 | int_25 | cha_30|level(55), wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_13|knows_shield_7|knows_athletics_8|knows_riding_11|knows_horse_archery_11|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_7|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_8|knows_devout_1|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   0x0000000a040063c464f590d6138a231a00000000001d69240000000000000000],
  ["knight_1_46", "Marquis Ronald Chevalier", "Ronald Chevalier", #罗纳尔·舍瓦利侯爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_sickle_of_eliminater, itm_gangshizi_yi_tongkui, itm_hongbai_jiazhong_banjia, itm_duangang_banjiaxue, itm_duangang_shalouhushou, itm_papal_plate_armor_mountain_horse, itm_courtly_outfit, itm_leather_boots],
   str_40|agi_32|int_24|cha_24|level(55),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),
   knows_ironflesh_10|knows_power_strike_11|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_4|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_7|knows_trainer_4|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_7|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_9|knows_prisoner_management_6|knows_leadership_7|knows_trade_1,
   0x000000053f0010143451646a75a944dc00000000001e3b130000000000000000],
  ["knight_1_47", "Count Rajiv Leroy", "Rajiv Leroy", #拉吉夫·勒罗伊伯爵
   tf_hero, 0, reserved,  fac_kingdom_1, 
   [itm_qishi_dingtouchui, itm_red_lion_iron_fan_shaped_shield, itm_dragon_blood_sorcery_lance, itm_changmain_hongyu_zhumiankui, itm_crown_knight_plate, itm_zhengshi_banjiaxue, itm_huali_shalouhushou, itm_powell_knight_warhorse, itm_courtly_outfit, itm_leather_boots],
   str_39 | agi_34 | int_25 | cha_30|level(55), wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_13|knows_shield_7|knows_athletics_8|knows_riding_11|knows_horse_archery_11|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_7|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_8|knows_devout_1|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   0x0000000a2e0043ce58dc9234ce69c77d00000000001d384d0000000000000000],
  ["knight_1_48", "Count Manon Joly", "Manon Joly", #玛尼翁·乔利伯爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_knight_recurve_bow, itm_wangguo_jian, itm_pride_fan_shaped_shield, itm_military_pick, itm_winged_great_helmet, itm_puweierguojiaqishi_jia, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_charger, itm_leather_noble_gown, itm_leather_boots],
   str_26 | agi_25 | int_24 | cha_18|level(45), wp_one_handed (400) | wp_two_handed (300) | wp_polearm (300) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_6|knows_athletics_11|knows_riding_11|knows_horse_archery_12|knows_looting_10|knows_trainer_5|knows_tracking_12|knows_tactics_4|knows_pathfinding_12|knows_spotting_13|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_5|knows_persuasion_6|knows_array_arrangement_5|knows_memory_8|knows_study_4|knows_devout_2|knows_prisoner_management_10|knows_leadership_4|knows_trade_10,
   0x0000000c800c10073364ce3adac6c29c00000000001da4a30000000000000000],
  ["knight_1_49", "Count Sotirios Mercier", "Sotirios Mercier", #苏蒂里奥斯·梅西耶伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_silver_dragon_fan_shaped_shield, itm_powell_lifeguard_plate, itm_changmain_hongyu_zhumiankui, itm_heise_banlianjiaxue, itm_heise_banlianjiaxue, itm_powell_noble_hand_and_a_half_sword, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_powell_fan_shaped_shield, itm_leather_noble_gown, itm_leather_boots],
   str_30 | agi_30 | int_18 | cha_24|level(45), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50), 
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_1|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_7|knows_devout_4|knows_prisoner_management_3|knows_leadership_7|knows_trade_1, 
   0x0000000a3a0823c242e325a96191aaf400000000001d491b0000000000000000],
  ["knight_1_50", "Marquis Donatas Dubois", "Donatas Dubois", #多纳塔斯·杜波依斯侯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_yansha_shuangshoujian, itm_changmain_hongyu_zhumiankui, itm_dragon_sword_master_plate, itm_longwen_banjiaxue, itm_fangxing_bikai, itm_leather_noble_gown, itm_leather_boots, itm_red_noble_shirt, itm_leather_boots],
   str_42 | agi_36 | int_24 | cha_20|level(56),wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_6|knows_athletics_11|knows_riding_6|knows_horse_archery_10|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3,
    0x000000066e08030144336644ae4930e400000000001c2b640000000000000000],
  ["knight_1_51", "Marquis Borch Moreau", "Borch Moreau", #博尔奇·摩勒欧伯爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_ellite_lance, itm_qishi_chu, itm_heavy_mattock, itm_steel_shield, itm_chaozhongkui, itm_baimian_banlianjia, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_huise_ma, itm_hongse_dianchengpao, itm_leather_boots],
   str_27|agi_23|int_15|cha_14|level(40),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360), 
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_5|knows_athletics_4|knows_riding_6|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_3|knows_devout_4|knows_prisoner_management_3|knows_leadership_5|knows_trade_2, 
   0x0000000e0b08458936f425548c7246fc00000000001e19320000000000000000],
  ["knight_1_52", "Count Lea Fantaine", "Lea Fantaine", #莉艾·方丹伯爵
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_1, 
   [itm_shield_heater_of_element, itm_dragon_blood_sorcery_lance, itm_changmian_lanyu_jianzuikui, itm_elemental_ranger_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai],
   str_33 | agi_30 | int_21 | cha_24|level(48),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   0x00000006440850313e9a75c2cba6c31400000000001cc8ca0000000000000000],

  ["knight_1_53", "Viscount Chandron Leander", "Chandron Leander", #尚德隆·里安德尔子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield, itm_red_noble_shirt, itm_leather_boots],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   0x00000003f80c130526d96649537748ac00000000001e24550000000000000000],
  ["knight_1_54", "Viscount Lochlann Marks", "Lochlann Marks", #罗克兰·马克斯子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_nameless_goddess_silverwing_lance, itm_rodriguez_bucket_helmet, itm_dolphin_plate_chain_composite_armor, itm_mail_boots, itm_dolphin_chain_armor_plain_horse, itm_fenzhi_fubanshoutao, itm_duangang_shalouhushou, itm_blue_flower_fan_shaped_shield, itm_powell_knight_sword, itm_rich_outfit, itm_leather_boots],
   str_31 | agi_26 | int_15 | cha_15|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_6|knows_tracking_2|knows_tactics_7|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_1|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   0x000000077800554348a3aa22de6da8ac00000000001dab2c0000000000000000],
  ["knight_1_55", "Lord Garrin Neil", "Garrin Neil", #巴伦·尼尔勋爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_heiyu_jianzuikui, itm_iron_greaves, itm_scale_gauntlets, itm_baipao_banlian, itm_heibai_wenqiqiang, itm_birch_crossbow, itm_bastard_sword_b, itm_steel_bolts, itm_hongshizipijia_ma, itm_preist_fan_shaped_shield, itm_courtly_outfit, itm_leather_boots],
   str_26 | agi_23 | int_14 | cha_13|level(42),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (340) | wp_archery (200) | wp_crossbow (340) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_devout_6|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   0x00000003ca08158734e68dd6c990a97400000000001cb5520000000000000000],
  ["knight_1_56", "Baron Dunstan Sidney", "Dunstan Sidney", #邓斯坦·史丹尼男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_papal_soldier_tower_shield, itm_jinshi_fanhuajian, itm_jinshi_shuangshou, itm_gangshizi_niujiao_dakui2, itm_baipao_banlian, itm_mail_boots, itm_gauntlets, itm_courtly_outfit, itm_leather_boots],
   str_26 | agi_19 | int_19 | cha_14|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_5|knows_devout_10|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   0x00000003d304320478ec9142fe6d45e400000000001cd2e30000000000000000],
  ["knight_1_57", "Baron Spencer Luke", "Spencer Luke", #史班瑟·路加男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_papal_soldier_tower_shield, itm_jinshi_fanhuajian, itm_jinshi_shuangshou, itm_gangshizi_niujiao_dakui2, itm_baipao_banlian, itm_mail_boots, itm_gauntlets, itm_rich_outfit, itm_leather_boots],
   str_26 | agi_19 | int_19 | cha_14|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_5|knows_devout_10|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   0x0000000a4e085512356bb51714866b2b00000000001d4b530000000000000000],
  ["knight_1_58", "Viscount Zephir Lee", "Zephir Lee", #泽菲尔·李子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_nameless_goddess_silverwing_lance, itm_rodriguez_bucket_helmet, itm_dolphin_plate_chain_composite_armor, itm_mail_boots, itm_dolphin_chain_armor_plain_horse, itm_fenzhi_fubanshoutao, itm_duangang_shalouhushou, itm_blue_flower_fan_shaped_shield, itm_powell_knight_sword, itm_rich_outfit, itm_leather_boots],
   str_31 | agi_26 | int_15 | cha_15|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_6|knows_tracking_2|knows_tactics_7|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_1|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   0x0000000c5d00321225e14f49517ac4fd00000000001e27720000000000000000],
  ["knight_1_59", "Baron Taavi Mueton", "Taavi Mueton", #塔维·缪顿男爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_graghite_steel_sabre, itm_heiyu_mogang_zhumiankui, itm_powell_knell_plate, itm_heise_banlianjiaxue, itm_heijin_banjaibikai, itm_heisebanjia_ma, itm_jinshi_zhanbiao, itm_jinshi_zhanbiao, itm_rich_outfit, itm_leather_boots],
   str_45 | agi_50| int_37 | cha_45|level(53), wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),
   knows_ironflesh_12|knows_power_strike_13|knows_power_throw_11|knows_power_draw_8|knows_weapon_master_12|knows_shield_6|knows_athletics_11|knows_riding_8|knows_horse_archery_14|knows_looting_7|knows_trainer_5|knows_tracking_7|knows_tactics_5|knows_pathfinding_7|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_5|knows_persuasion_7|knows_array_arrangement_4|knows_memory_11|knows_study_8|knows_devout_6|knows_prisoner_management_7|knows_leadership_7|knows_trade_4,
   0x00000009840c054429597093d26ec59d00000000001d5b590000000000000000],
  ["knight_1_60", "Viscount Surias Doyle", "Surias Doyle", #尚利亚·多伊尔子爵
   tf_hero, 
   0, reserved,  fac_kingdom_1, 
   [itm_heavy_lance, itm_gauntlets, itm_hongsejianyi_banlianjia, itm_puweier_lianjia, itm_hongyu_hue_qingbiankui, itm_hongyu_zhumiankui, itm_jinhong_pijia_liema, itm_lance, itm_mail_boots, itm_courtly_outfit, itm_leather_boots],
   str_26 | agi_22 | int_12 | cha_15|level(40),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_6|knows_devout_3|knows_prisoner_management_7|knows_leadership_8|knows_trade_5, 
   0x000000090c005187479a6e48e452477400000000001c94e50000000000000000],




##########################################################伊希斯公国##########################################################
##
  ["knight_2_1", "Acting Proloc Evelyn", "Evelyn", #伊芙琳·死亡代议长
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_light_armor, itm_elf_knight_boot, itm_kongju_bikai, itm_spirit_tree_god_selection_sword],
   str_41 | agi_81 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_11|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_13|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FC80010070000000000000E0700000000000000000000000000000000],
  ["knight_2_2", "Acting Proloc Frederica", "Frederica", #绯雷德翠卡·先祖代议长
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_god_selection_sword, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_graghite_armor, itm_black_greaves, itm_plate_armor_spiritual_horse, itm_heiguang_bikai],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_12|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000FC80020030000000000000FC500000000000000000000000000000000],
  ["knight_2_3", "Acting Proloc Jennifer", "Jennifer", #珍妮芙·生命代议长
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_qinliang_shuangshoufu, itm_steel_shield, itm_selected_champion_headcrown, itm_selected_champion_windbreaker, itm_elf_valkyrie_boot, itm_mogang_fangxing_bikai],
   str_39 | agi_77 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_9|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x00000001880010010000000000000FFD00000000000000000000000000000000],

  ["knight_2_4", "Assemblyman Yulia", "Yulia", #尤莱雅·生命议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_qinliang_shuangshoufu, itm_steel_shield, itm_selected_champion_headcrown, itm_selected_champion_windbreaker, itm_elf_valkyrie_boot, itm_mogang_fangxing_bikai],
   str_39 | agi_77 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_9|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000FCD0000010000000000000E0000000000000000000000000000000000],
  ["knight_2_5", "Assemblyman Gabriella", "Gabriella", #嘉比里拉·灵魂议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_spirit_tree_god_selection_sword, itm_selected_champion_headcrown, itm_selected_champion_glass_armor, itm_elf_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_eternal_inheritance_bow, itm_full_armor_unicorn],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (660) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_15|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FF00000060000000000000E3800000000000000000000000000000000],
  ["knight_2_6", "Assemblyman Octavel", "Octavel", #奥克塔薇·先祖议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_god_selection_sword, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_graghite_armor, itm_black_greaves, itm_plate_armor_spiritual_horse, itm_heiguang_bikai],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_12|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000FFF0000010000000000000E3F00000000000000000000000000000000],
  ["knight_2_7", "Assemblyman Juranos", "Juranos", #尤拉诺斯·死亡议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_light_armor, itm_elf_knight_boot, itm_kongju_bikai, itm_spirit_tree_god_selection_sword],
   str_41 | agi_81 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_11|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_13|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FFF0010030000000000000FD400000000000000000000000000000000],
  ["knight_2_8", "Assemblyman Vlan", "Vlan", #维兰·生命议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_qinliang_shuangshoufu, itm_steel_shield, itm_selected_champion_headcrown, itm_selected_champion_windbreaker, itm_elf_valkyrie_boot, itm_mogang_fangxing_bikai],
   str_39 | agi_77 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_9|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000EBF0020020000000000000FD400000000000000000000000000000000],
  ["knight_2_9", "Assemblyman Ekaterin", "Ekaterin", #埃卡捷琳·灵魂议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_spirit_tree_god_selection_sword, itm_selected_champion_headcrown, itm_selected_champion_glass_armor, itm_elf_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_eternal_inheritance_bow, itm_full_armor_unicorn],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (660) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_15|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000D980000010000000000000FD000000000000000000000000000000000],
  ["knight_2_10", "Assemblyman Nelag", "Garfield", #加菲尔德·先祖议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_god_selection_sword, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_graghite_armor, itm_black_greaves, itm_plate_armor_spiritual_horse, itm_heiguang_bikai],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_12|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000E880000050000000000000FF800000000000000000000000000000000],


  ["knight_2_11", "Assemblyman Edryder Elaine", "Edryder Elaine", #爱德莱德·伊莲恩议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_elf_light_shield, itm_yishith_knight_sword, itm_yishith_knight_strengthen_helmet, itm_spiritual_tree_armor, itm_elf_valkyrie_boot, itm_jingling_liulijian, itm_fenzhi_fulianshoutao, itm_leather_armor_unicorn, itm_spirittree_knight_bow],
   str_29 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (570),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_13|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000FC80010050000000000000FF800000000000000000000000000000000],
  ["knight_2_12", "Assemblyman Nebnil Sylvester", "Nebnil Sylvester", #奈伯尼尔·希尔维斯特议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_elf_light_shield, itm_yishith_knight_sword, itm_yishith_knight_strengthen_helmet, itm_spiritual_tree_armor, itm_elf_valkyrie_boot, itm_jingling_liulijian, itm_fenzhi_fulianshoutao, itm_leather_armor_unicorn, itm_spirittree_knight_bow],
   str_29 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (570),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_13|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x00000009080020050000000000000FE000000000000000000000000000000000],
  ["knight_2_13", "Assemblyman Noah Julius", "Noah Julius", #诺亚·朱莉尔思议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_qinliang_shuangshoufu, itm_seawind_speaker, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_xihai_wenshikui, itm_yishith_westcoast_chain_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   0x0000000FC80020060000000000000FE200000000000000000000000000000000],
  ["knight_2_14", "Assemblyman Helna Ingram", "Helna Ingram", #赫尔娜·因格拉谬议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_elf_light_shield, itm_yishith_knight_sword, itm_yishith_knight_strengthen_helmet, itm_spiritual_tree_armor, itm_elf_valkyrie_boot, itm_jingling_liulijian, itm_fenzhi_fulianshoutao, itm_leather_armor_unicorn, itm_spirittree_knight_bow],
   str_29 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (570),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_13|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],


#Yishith younger knights  
  ["knight_2_15", "Assemblyman Phyllis Evelyn", "Phyllis Evelyn", #菲丽斯·伊芙琳议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_jingling_liulijian, itm_elf_halberd, itm_spiritrain_ranger_bow, itm_jingling_liulijian, itm_yishith_knight_helmet, itm_spiritrain_plate_skirt, itm_heise_banlianjiaxue, itm_gauntlets],
   str_30 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_9|knows_weapon_master_12|knows_shield_8|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000C120020070000000000000FC700000000000000000000000000000000],
  ["knight_2_16", "Assemblyman Melissa Frederica", "Melissa Frederica", #孟莉萨·绯雷德翠卡议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_verdant_hammer, itm_jingling_liulijian, itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_graghite_steel_small_helmet, itm_immortal_plate_skirt, itm_valkyrie_boot, itm_mogang_yuanzhi_bikai],
   str_28 | agi_62 | int_38 | cha_64|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_10|knows_power_strike_7|knows_power_throw_4|knows_power_draw_11|knows_weapon_master_12|knows_shield_12|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_12|knows_trade_3, 
   0x0000000C120020010000000000000E8700000000000000000000000000000000],
  ["knight_2_17", "Assemblyman Olivetta Jennifer", "Olivetta Jennifer", #奥利维塔·珍妮芙议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_qishi_danshouzhanfu, itm_spiritwind_cavalry_bow, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_changmian_zhumiankui1, itm_spiritwind_light_plate, itm_spiritual_boot, itm_fenzhi_fulianshoutao, itm_leather_armor_spiritual_horse],
   str_28 | agi_59 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (580),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_7|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x00000000000020020000000000000E9800000000000000000000000000000000],
  ["knight_2_18", "Assemblyman Natyavida Yulia", "Natyavida Yulia", #娜提雅维达·尤莱雅议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_qishi_danshouzhanfu, itm_spiritwind_cavalry_bow, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_changmian_zhumiankui1, itm_spiritwind_light_plate, itm_spiritual_boot, itm_fenzhi_fulianshoutao, itm_leather_armor_spiritual_horse],
   str_28 | agi_59 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (580),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_7|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000FD50020040000000000000E9800000000000000000000000000000000],
  ["knight_2_19", "Assemblyman Helois Gabriella", "Helois Gabriella", #海洛伊斯·嘉比里拉议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_elf_light_shield, itm_yishith_knight_sword, itm_yishith_knight_strengthen_helmet, itm_spiritual_tree_armor, itm_elf_valkyrie_boot, itm_jingling_liulijian, itm_fenzhi_fulianshoutao, itm_leather_armor_unicorn, itm_spirittree_knight_bow],
   str_29 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (570),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_13|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000FD50020040000000000000EB800000000000000000000000000000000],
  ["knight_2_20", "Assemblyman Grisherda Octavel", "Grisherda Octavel", #葛丽歇尔达·奥克塔薇议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_verdant_hammer, itm_jingling_liulijian, itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_graghite_steel_small_helmet, itm_immortal_plate_skirt, itm_valkyrie_boot, itm_mogang_yuanzhi_bikai],
   str_28 | agi_62 | int_38 | cha_64|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_10|knows_power_strike_7|knows_power_throw_4|knows_power_draw_11|knows_weapon_master_12|knows_shield_12|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_12|knows_trade_3, 
   0x0000000FF10020040000000000000EA700000000000000000000000000000000],
  ["knight_2_21", "Assemblyman Zenia Juranos", "Zenia Juranos", #芝妮雅·尤拉诺斯议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_jingling_liulijian, itm_elf_halberd, itm_spiritrain_ranger_bow, itm_jingling_liulijian, itm_yishith_knight_helmet, itm_spiritrain_plate_skirt, itm_heise_banlianjiaxue, itm_gauntlets],
   str_30 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_9|knows_weapon_master_12|knows_shield_8|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x000000097F0020040000000000000E0700000000000000000000000000000000],
  ["knight_2_22", "Assemblyman Edwina Welland", "Edwina Welland", #爱德文娜·维兰议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_qishi_danshouzhanfu, itm_spiritwind_cavalry_bow, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_changmian_zhumiankui1, itm_spiritwind_light_plate, itm_spiritual_boot, itm_fenzhi_fulianshoutao, itm_leather_armor_spiritual_horse],
   str_28 | agi_59 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (580),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_7|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000FFF0020060000000000000E3F00000000000000000000000000000000],
  ["knight_2_23", "Assemblyman Antoniel Ekaterin", "Antoniel Ekaterin", #安东妮儿·埃卡捷琳议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_elf_light_shield, itm_yishith_knight_sword, itm_yishith_knight_strengthen_helmet, itm_spiritual_tree_armor, itm_elf_valkyrie_boot, itm_jingling_liulijian, itm_fenzhi_fulianshoutao, itm_leather_armor_unicorn, itm_spirittree_knight_bow],
   str_29 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (570),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_13|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   0x0000000FC00020060000000000000E1700000000000000000000000000000000],
  ["knight_2_24", "Assemblyman Chloe Garfield", "Chloe Garfield", #克洛怡·加菲尔德议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_verdant_hammer, itm_jingling_liulijian, itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_graghite_steel_small_helmet, itm_immortal_plate_skirt, itm_valkyrie_boot, itm_mogang_yuanzhi_bikai],
   str_28 | agi_62 | int_38 | cha_64|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_10|knows_power_strike_7|knows_power_throw_4|knows_power_draw_11|knows_weapon_master_12|knows_shield_12|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_12|knows_trade_3, 
   0x0000000D400020060000000000000E1000000000000000000000000000000000],


  ["knight_2_25", "Assemblyman Layla", "Layla", #莱伊拉·生命议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_qinliang_shuangshoufu, itm_steel_shield, itm_selected_champion_headcrown, itm_selected_champion_windbreaker, itm_elf_valkyrie_boot, itm_mogang_fangxing_bikai],
   str_39 | agi_77 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_9|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_26", "Assemblyman Junitha", "Junitha", #茱丽莎·死亡议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_light_armor, itm_elf_knight_boot, itm_kongju_bikai, itm_spirit_tree_god_selection_sword],
   str_41 | agi_81 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_11|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_13|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_27", "Assemblyman Seomis", "Seomis", #瑟欧密斯·先祖议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_god_selection_sword, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_graghite_armor, itm_black_greaves, itm_plate_armor_spiritual_horse, itm_heiguang_bikai],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_12|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_28", "Assemblyman Katia", "Katia", #凯缇亚·灵魂议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_spirit_tree_god_selection_sword, itm_selected_champion_headcrown, itm_selected_champion_glass_armor, itm_elf_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_eternal_inheritance_bow, itm_full_armor_unicorn],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (660) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_15|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_29", "Assemblyman Drina", "Drina", #戴瑞那·死亡议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_gaojingling_xuejian, itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_light_armor, itm_elf_knight_boot, itm_kongju_bikai, itm_spirit_tree_god_selection_sword],
   str_41 | agi_81 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_11|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_13|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_30", "Assemblyman Nesha", "Nesha", #内莎·灵魂议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_spirit_tree_god_selection_sword, itm_selected_champion_headcrown, itm_selected_champion_glass_armor, itm_elf_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_eternal_inheritance_bow, itm_full_armor_unicorn],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (660) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_15|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],


  ["knight_2_31", "Assemblyman Tabath Pelaeka", "Tabath Pelaeka", #塔芭斯·佩莱卡议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_jingling_youxiajian, itm_yejian_qiang, itm_string_of_elegy, itm_jingling_youxiajian, itm_elf_dome_helmet, itm_dark_chest_armor_shirt, itm_nailed_iron_leather_boot, itm_fenzhi_fulianshoutao],
   str_25 | agi_56 | int_37 | cha_60|level(50),wp_one_handed (50) | wp_two_handed (510) | wp_polearm (510) | wp_archery (530) | wp_crossbow (510) | wp_throwing (510),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_8|knows_athletics_13|knows_riding_10|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_32", "Assemblyman Haris Vayen", "Haris Vayen", #海瑞丝·法耶议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_qinliang_shuangshoufu, itm_seawind_speaker, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_xihai_wenshikui, itm_yishith_westcoast_chain_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_33", "Assemblyman Joaka Tejina", "Joaka Tejina", #乔卡·特吉娜议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_forestwarden_bow, itm_elf_light_shield, itm_yishith_gorgeous_sword, itm_jingling_youxiajian, itm_elf_dome_helmet, itm_unicorn_chain_armor, itm_emerald_boot, itm_fenzhi_lianjiashoutao, itm_leather_armor_spiritual_horse],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (470) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_8|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_34", "Assemblyman Olekseia Myntha", "Olekseia Myntha", #奥克莎·米萨议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_forestwarden_bow, itm_elf_light_shield, itm_yishith_gorgeous_sword, itm_jingling_youxiajian, itm_elf_dome_helmet, itm_unicorn_chain_armor, itm_emerald_boot, itm_fenzhi_lianjiashoutao, itm_leather_armor_spiritual_horse],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (470) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_8|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_35", "Assemblyman Akilina Audrey", "Akilina Audrey", #安吉丽娜·奥德瑞议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_daoye_jian, itm_yishith_elite_ridebow, itm_verdant_hammer, itm_rose_knight_shield, itm_changmian_jianzuikui, itm_verdant_light_plate_chain_composite_armor, itm_mail_boots, itm_gauntlets, itm_qiangwei_lianjia_pingyuanma],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (440),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_36", "Assemblyman Sepana Iarina", "Sepana Iarina", #雪帕·伊亚莉娜议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_qinliang_shuangshoufu, itm_seawind_speaker, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_xihai_wenshikui, itm_yishith_westcoast_chain_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_37", "Assemblyman Sihavan Erenchina", "Sihavan Erenchina", #斯哈维·艾瑞琦娜议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_jingling_youxiajian, itm_yejian_qiang, itm_string_of_elegy, itm_jingling_youxiajian, itm_elf_dome_helmet, itm_dark_chest_armor_shirt, itm_nailed_iron_leather_boot, itm_fenzhi_fulianshoutao],
   str_25 | agi_56 | int_37 | cha_60|level(50),wp_one_handed (50) | wp_two_handed (510) | wp_polearm (510) | wp_archery (530) | wp_crossbow (510) | wp_throwing (510),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_8|knows_athletics_13|knows_riding_10|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],
  ["knight_2_38", "Assemblyman Tamar Valka", "Tamar Valka", #塔玛尔·瓦尔卡议员
   tf_hero|tf_elf, 
   0, reserved,  fac_kingdom_2, 
   [itm_daoye_jian, itm_yishith_elite_ridebow, itm_verdant_hammer, itm_rose_knight_shield, itm_jiaqiang_guokui2, itm_verdant_light_plate_chain_composite_armor, itm_nailed_iron_leather_boot, itm_leather_gloves],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (440),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   0x0000000FF70020070000000000000FFA00000000000000000000000000000000],




##########################################################科鲁托酋长国##########################################################
##
  ["knight_3_1", "Great Chief Bagan", "Bagan", #大酋长“柱子”巴根
   tf_hero|tf_beast_man, #牛族
   0, 0, fac_kingdom_3,
   [itm_great_axe, itm_linshi_zhongkui, itm_kelutuo_lianjia, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_74 | agi_9 | int_5 | cha_5|level(45), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_1|knows_array_arrangement_1|knows_memory_1|knows_study_1|knows_devout_5|knows_prisoner_management_3|knows_leadership_3|knows_trade_1, 
   0x000000003904714738ac91385c665f1100000000001ea6440000000000000000],
  ["knight_3_2", "Great Chief Manduratu", "Manduratu", #大酋长“兴隆”满都拉图
   tf_hero|tf_beast_man, #狐族
   0, 0, fac_kingdom_3,
   [itm_beast_ancestor_totem_shield, itm_kouruto_beast_sabre_simple, itm_nanfang_lianjiatoukui, itm_zongse_lianxiongjia, itm_shengtie_banjiaxue, itm_lamellar_gauntlets, itm_tuselianjia_ma],
   str_70 | agi_15 | int_15 | cha_13|level(47), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x0000000004111289412458da1c6d951c00000000001db6660000000000000000],
  ["knight_3_3", "Great Chief Suhe", "Suhe", #大酋长“斧头”苏合
   tf_hero|tf_beast_man, #犬族
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_lance, itm_kouruto_beast_sabre_simple, itm_kelutuo_duizhangkui, itm_linlianfuhe_jia, itm_lingjia_xue, itm_scale_gauntlets, itm_warhorse_steppe],
   str_71 | agi_15 | int_10 | cha_7|level(47), wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (65) | wp_crossbow (5) | wp_throwing (65),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000003324f24b14c4adb6933a249b00000000001e55930000000000000000],

  ["knight_3_4", "Chief Temur", "Temur", #“铁块”特木尔酋长
   tf_hero|tf_beast_man, #熊族
   0, 0, fac_kingdom_3,
   [itm_warhammer, itm_kouruto_round_shield, itm_linshi_zhongkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_gauntlets, itm_heisebanlian_ma, itm_zongsebanlian_ma],
   str_80 | agi_11 | int_7 | cha_8|level(49), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_14|knows_power_strike_12|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x00000000251c30855aabae46ebadd92900000000001ed6e10000000000000000],
  ["knight_3_5", "Chief Halbara", "Halbara", #“黑虎”哈尔巴拉
   tf_hero|tf_beast_man, #猫族
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_war_darts, itm_nanfang_cijian, itm_kelutuo_heikui, itm_heise_lianxiongjia, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao, itm_shense_banzhajia_caoyuanma],
   str_71 | agi_15 | int_15 | cha_13|level(46), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_10|knows_power_draw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x000000003f1d22c1366472c4b34eb6e300000000001d48ab0000000000000000],
  ["knight_3_6", "Chief Chaolu", "Chaolu", #“石头”朝鲁
   tf_hero|tf_beast_man, #熊族
   0, 0, fac_kingdom_3,
   [itm_warhammer, itm_kouruto_tower_shield, itm_linshi_zhongkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_gauntlets],
   str_78 | agi_11 | int_7 | cha_8|level(47), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_14|knows_power_strike_11|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000090004208905646dd4dbd0e16400000000001e695b0000000000000000],
  ["knight_3_7", "Chief Bartel", "Bartel", #“英雄”巴特尔
   tf_hero|tf_beast_man, #狮族
   0, 0, fac_kingdom_3, 
   [itm_kouruto_beast_sabre, itm_beast_ancestor_headgear, itm_kouruto_sword_fighter_lamellar_armor, itm_shengtie_banjiaxue, itm_shengtie_banjiabikai, itm_tiesebanlian_ma],
   str_108 | agi_20 | int_18 | cha_30|level(60), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (80) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_7|knows_power_draw_4|knows_weapon_master_9|knows_shield_4|knows_athletics_7|knows_riding_7|knows_horse_archery_4|knows_looting_7|knows_trainer_6|knows_tracking_7|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13, 
   0x000000093228104152cb2e69898738ac00000000001dc8e90000000000000000],
  ["knight_3_8", "Chief Lakshen", "Lakshen", #“魁梧”拉克申
   tf_hero|tf_beast_man, #熊族
   0, 0, fac_kingdom_3,
   [itm_warhammer, itm_kouruto_round_shield, itm_linshi_zhongkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_gauntlets, itm_heisebanlian_ma, itm_zongsebanlian_ma],
   str_80 | agi_11 | int_7 | cha_8|level(49), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_14|knows_power_strike_12|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000091d1020832915d0a6e92a732100000000001e66e60000000000000000],
  ["knight_3_9", "Chief Suzhlehek", "Suzhlehek", #“威武”苏日勒和克
   tf_hero|tf_beast_man, #虎族
   0, 0, fac_kingdom_3,
   [itm_duangang_shourendao, itm_kelutuo_duizhangkui, itm_light_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_lamellar_gauntlets, itm_hualizhajia_ma],
   str_77| agi_13 | int_7 | cha_9|level(50), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (5) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_4|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_9, 
   0x0000000908006103289a90861352c45e00000000001f4b360000000000000000],
  ["knight_3_10", "Chief Izibis", "Izibis", #“金钱豹”伊日毕斯
   tf_hero|tf_beast_man, #鹿族
   0, 0, fac_kingdom_3,
   [itm_kouruto_beast_sabre_simple, itm_spike_skin_battle_shield, itm_nanfang_lianjiatoukui, itm_kelutuo_zhajia_pao, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_66 | agi_13 | int_9 | cha_8|level(43), wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (35) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   0x00000000161c21c446cd6d571592b4e200000000001df69c0000000000000000],
  ["knight_3_11", "Chief Jeddah", "Jeddah", #“长矛”吉达
   tf_hero|tf_beast_man, #狮族
   0, 0, fac_kingdom_3,
   [itm_mogang_shourendao, itm_beast_king_helmet, itm_kouruto_elite_lamellar_armor, itm_shengtie_banjiaxue, itm_lamellar_gauntlets, itm_charger],
   str_95 | agi_16 | int_10 | cha_3|level(57), wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (35) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_7|knows_power_draw_5|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_8|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_6|knows_leadership_11, 
   0x000000001e20004932ec8f276668a31500000000001dcb640000000000000000],
  ["knight_3_12", "Chief Nusangha", "Nusangha", #“邋遢”努桑哈
   tf_hero|tf_beast_man, #狮族
   0, 0, fac_kingdom_3,
   [itm_long_bardiche, itm_khergit_cavalry_helmet, itm_linlianfuhe_jia, itm_khergit_leather_boots, itm_leather_gloves, itm_steppe_horse],
   str_65 | agi_13 | int_8 | cha_12|level(42), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_5|knows_riding_6|knows_horse_archery_3|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000002728104d5494ce955d353a9400000000001ec4f60000000000000000],

  ["knight_3_13", "Chief Dresdger","Dresdger", #“竖耳”德勒德格日
   tf_hero|tf_beast_man, #兔族
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_slingshot, itm_slingshot_stones, itm_kelutuo_heikui, itm_khergit_elite_armor, itm_lingjia_xue, itm_fenzhi_jiaqiangshoutao],
   str_61 | agi_19 | int_9 | cha_9|level(42), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (80) | wp_crossbow (5) | wp_throwing (80),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   0x000000000014d205666529369369b4f000000000001d18db0000000000000000],
  ["knight_3_14", "Chief Habuchik", "Habuchik", #“扁头”哈布其克
   tf_hero|tf_beast_man, #狐族
   0, 0, fac_kingdom_3,
   [itm_double_sided_lance, itm_black_and_white_skoutarion, itm_vaegir_fur_helmet, itm_khergit_guard_armor, itm_splinted_greaves, itm_leather_gloves, itm_steppe_horse],
   str_42 | agi_13 | int_13 | cha_10|level(36), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_3|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_4|knows_looting_4|knows_trainer_1|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_prisoner_management_3|knows_leadership_5|knows_trade_4, 
   0x000000002309028c46da8c44d3c637b000000000001eb6060000000000000000],
  ["knight_3_15", "Chief Wengheri", "Wengheri", #“凹脸”翁和日
   tf_hero|tf_beast_man, #犬族
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_lance, itm_kouruto_beast_sabre_simple, itm_kelutuo_duizhangkui, itm_linlianfuhe_jia, itm_lingjia_xue, itm_scale_gauntlets, itm_warhorse_steppe],
   str_70 | agi_15 | int_10 | cha_7|level(47), wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (65) | wp_crossbow (5) | wp_throwing (65),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000001d14e2445d5379e9a47649aa00000000001e495c0000000000000000],
  ["knight_3_16", "Chief Boletherge", "Boletherge", #“凸目”波勒特和日
   tf_hero|tf_beast_man, #熊族
   0, 0, fac_kingdom_3, 
   [itm_polehammer, itm_kouruto_round_shield, itm_kelutuo_duizhangkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_iron_greaves, itm_gauntlets],
   str_72 | agi_10 | int_7 | cha_8|level(40), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_10|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000002b28308324ba36a5aa6e4b8900000000001efb540000000000000000],
  ["knight_3_17", "Chief Chaganfu", "Chaganfu", #“白小子”查干夫
   tf_hero|tf_beast_man, #猫族
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_silver_plated_sabre, itm_exorcist_battle_shield, itm_papal_believer_chain_hood, itm_lamellar_vest, itm_mail_chausses, itm_lamellar_gauntlets],
   str_63 | agi_14 | int_13 | cha_10|level(38), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_7|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_4|knows_looting_5|knows_trainer_2|knows_tracking_7|knows_tactics_3|knows_pathfinding_8|knows_spotting_9|knows_inventory_management_1|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_5|knows_devout_3|knows_prisoner_management_2|knows_leadership_5|knows_trade_2, 
   0x00000000000122c946a3a5e6a370cb2c00000000001ca7630000000000000000],
  ["knight_3_18", "Chief Huqitu", "Huqitu", #“大力”呼其图
   tf_hero|tf_beast_man, #熊族
   0, 0, fac_kingdom_3, 
   [itm_polehammer, itm_linshi_zhongkui, itm_linlianfuhe_jia, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_68 | agi_6 | int_7 | cha_8|level(52), wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_15|knows_power_strike_12|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x0000000007242083468dc547726a49e200000000001e17690000000000000000],
  ["knight_3_19", "Chief Timuribuh", "Timuribuh", #“硬铁”帖木日布赫
   tf_hero|tf_beast_man, #狮族
   0, 0, fac_kingdom_3, 
   [itm_mogang_shourendao, itm_nanfang_lianjiatoukui, itm_kouruto_sword_fighter_lamellar_armor, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_87 | agi_17 | int_11 | cha_17|level(56), wp_one_handed (50) | wp_two_handed (75) | wp_polearm (75) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),
   knows_ironflesh_13|knows_power_strike_14|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_5|knows_shield_2|knows_athletics_7|knows_riding_4|knows_horse_archery_2|knows_looting_5|knows_trainer_5|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_9, 
   0x000000002008004a67ab6a4a9b55258b00000000001e46ad0000000000000000],
  ["knight_3_20", "Chief Batubuch", "Batubuch", #“坚固”巴图布赫
   tf_hero|tf_beast_man, #熊族
   0, 0, fac_kingdom_3, 
   [itm_polehammer, itm_kouruto_round_shield, itm_kelutuo_duizhangkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_iron_greaves, itm_gauntlets],
   str_72 | agi_10 | int_7 | cha_8|level(40), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_10|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x000000000e18308645236a3692b0c6a300000000001ccd200000000000000000],

  ["knight_3_21", "Chief Daisendari","Daisendari", #“歼敌”岱森达日
   tf_hero|tf_beast_man, #狼族
   0, 0, fac_kingdom_3,
   [itm_gorgeous_battle_shield, itm_heavy_lance, itm_kouruto_beast_sabre_simple, itm_khergit_guard_helmet, itm_kouruto_elite_heavy_lamellar_armor, itm_khergit_guard_boots, itm_lamellar_gauntlets, itm_shense_banzhajia_caoyuanma, itm_great_lance, itm_heavy_lance, itm_heavy_lance, itm_great_lance, itm_qianse_banzhajia_caoyuanma],
   str_54 | agi_16 | int_10 | cha_7|level(48), wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (65) | wp_crossbow (5) | wp_throwing (65),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x0000000b992460c22651754d1b8e195300000000001d592d0000000000000000],
  ["knight_3_22", "Chief Nigsberg","Nigsberg", #“飞虎”尼格斯巴日
   tf_hero|tf_beast_man, #虎族
   0, 0, fac_kingdom_3,
   [itm_duangang_shourendao, itm_kelutuo_duizhangkui, itm_light_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_74 | agi_14 | int_7 | cha_9|level(48), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (5) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_4|knows_shield_1|knows_athletics_5|knows_riding_4|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_9, 
   0x00000005ff006101426d3a992b94f28b00000000001e0b330000000000000000],
  ["knight_3_23", "Chief Ningen","Ningen", #“好人”宁金
   tf_hero|tf_beast_woman, #兔族
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_slingshot, itm_slingshot_stones, itm_kelutuo_heikui, itm_khergit_elite_armor, itm_lingjia_xue, itm_fenzhi_jiaqiangshoutao],
   str_61 | agi_19 | int_9 | cha_9|level(42), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (80) | wp_crossbow (5) | wp_throwing (80),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   0x000000001e00d21e0000000000000fce00000000000000000000000000000000],
  ["knight_3_24", "Chief Agura","Agura", #“大山”阿古拉
   tf_hero|tf_beast_man, #牛族
   0, 0, fac_kingdom_3,
   [itm_sarranid_axe_b, itm_kouruto_round_shield, itm_linshi_zhongkui, itm_kelutuo_lianjia, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_70 | agi_8 | int_5 | cha_5|level(42), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_11|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_3|knows_shield_4|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_1|knows_array_arrangement_1|knows_memory_1|knows_study_1|knows_devout_5|knows_prisoner_management_3|knows_leadership_3|knows_trade_1, 
   0x00000005f32881452722512b1b4e671b00000000001eba460000000000000000],
  ["knight_3_25", "Chief Muren","Muren", #“河流”牧仁
   tf_hero|tf_beast_woman, #狼族
   0, 0, fac_kingdom_3,
   [itm_nanfang_jian, itm_kouruto_beast_sabre_simple, itm_gorgeous_battle_shield, itm_khergit_guard_helmet, itm_kouruto_elite_heavy_lamellar_armor, itm_khergit_guard_boots, itm_lamellar_gauntlets, itm_shense_banzhajia_caoyuanma, itm_southern_horn_bow, itm_qianse_banzhajia_caoyuanma],
   str_71 | agi_18 | int_10 | cha_7|level(44), wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (75) | wp_crossbow (5) | wp_throwing (75),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x00000000040050e90000000000000f1e00000000000000000000000000000000],
  ["knight_3_26", "Chief Thoabu","Thoabu", #“飞鹰”少布
   tf_hero|tf_beast_man, #狼族
   0, 0, fac_kingdom_3, 
   [itm_nanfang_jian, itm_mogang_shourendao, itm_kelutuo_heikui, itm_kelutuo_zhajia, itm_black_greaves, itm_mogang_shalouhushou, itm_tiese_lianjia_caoyuanma, itm_southern_knight_bow],
   str_83 | agi_20 | int_17 | cha_16|level(55), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (20) | wp_throwing (100),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_6|knows_power_draw_7|knows_weapon_master_7|knows_shield_4|knows_athletics_9|knows_riding_9|knows_horse_archery_5|knows_looting_9|knows_trainer_6|knows_tracking_10|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_7|knows_leadership_10|knows_trade_1, 
   0x00000005c01850c176dd6eb6709112b400000000001e66940000000000000000],
  ["knight_3_27", "Chief Giyasain","Giyasain", #“好运”吉雅赛音
   tf_hero|tf_beast_woman, #羊族
   0, 0, fac_kingdom_3,
   [itm_heibaiyu_nushi, itm_birch_crossbow, itm_crushing_hammer, itm_linshi_zhongkui, itm_furnace_light_copper_armor, itm_kouruto_copper_boot, itm_lamellar_gauntlets, itm_zongsebanlian_ma],
   str_64 | agi_13 | int_21 | cha_11|level(55), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_looting_4|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_9|knows_study_12|knows_devout_13|knows_prisoner_management_5|knows_leadership_11, 
   0x00000000370091a90000000000000f1e00000000000000000000000000000000],

  ["knight_3_28", "Chief Enhejin","Enhejin", #“和平”恩金
   tf_hero|tf_beast_man, #狼族
   0, 0, fac_kingdom_3, 
   [itm_war_darts, itm_kouruto_beast_sabre_simple, itm_spike_skin_battle_shield, itm_kelutuo_heikui, itm_kelutuo_zhajia, itm_black_greaves, itm_gauntlets],
   str_75 | agi_16 | int_10 | cha_7|level(50), wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (70) | wp_crossbow (5) | wp_throwing (70),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_9|knows_tactics_5|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   0x00000000fa0840c4635964159dc5d69600000000001db9630000000000000000],
  ["knight_3_29", "Chief Autunmuqi","Autunmuqi", #“星枝”奥敦木其尔
   tf_hero|tf_beast_woman, #羊族
   0, 0, fac_kingdom_3,
   [itm_khergit_arrows, itm_long_hafted_spiked_mace, itm_kelutuo_duizhangkui, itm_mamluke_mail, itm_lingjia_xue, itm_leather_gloves, itm_elite_horn_bow],
   str_67 | agi_13 | int_9 | cha_8|level(44), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (65) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_4|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   0x00000000370091a80000000000000e0000000000000000000000000000000000],
  ["knight_3_30", "Chief Taorihui","Taorihui", #“干眼睛”陶日崩
   tf_hero|tf_beast_man, #虎族
   0, 0, fac_kingdom_3,
   [itm_khergit_sword_two_handed_a, itm_vaegir_spiked_helmet, itm_sarranid_elite_armor, itm_khergit_leather_boots, itm_steppe_horse],
   str_58 | agi_11 | int_6 | cha_7|level(35), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (5) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_3|knows_weapon_master_2|knows_athletics_3|knows_riding_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_5, 
   0x00000000d120610147abb626d9ad476c00000000001d16540000000000000000],
  ["knight_3_31", "Chief Surilig","Surilig", #“威严”苏日立格
   tf_hero|tf_beast_man, #鹿族
   0, 0, fac_kingdom_3,
   [itm_steel_bolts, itm_light_crossbow, itm_khergit_sword_two_handed_a, itm_khergit_helmet, itm_red_colored_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_leather_gloves, itm_jingzhizhajia_ma],
   str_61 | agi_10 | int_17 | cha_9|level(42), wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_7|knows_study_7|knows_devout_9|knows_prisoner_management_2|knows_leadership_8, 
   0x00000000c000b1c1089e8d5a5b7162e900000000001f39580000000000000000],
  ["knight_3_32", "Chief Guuri","Guuri", #“全都要”古日
   tf_hero|tf_beast_man, #狼族
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_vaegir_lamellar_helmet, itm_lamellar_vest, itm_khergit_leather_boots, itm_leather_gloves, itm_kelutuo_pijia_liema, itm_southern_horn_bow, itm_khergit_arrows],
   str_53 | agi_16 | int_9 | cha_7|level(30), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (55) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_3|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   0x00000000ec1040c52563933a9c8db69300000000001cb92e0000000000000000],
  ["knight_3_33", "Chief Bayagin","Bayagin", #“暴富”巴亚金
   tf_hero|tf_beast_man, #虎族
   0, 0, fac_kingdom_3,
   [itm_khergit_sword_two_handed_a, itm_vaegir_spiked_helmet, itm_sarranid_elite_armor, itm_khergit_leather_boots],
   str_35 | agi_12 | int_6 | cha_7|level(32), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (5) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_weapon_master_2|knows_athletics_3|knows_riding_3|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_5, 
   0x000000084220610358d368a2b46446aa00000000001e34ab0000000000000000],
  ["knight_3_34", "Chief Agima","Agima", #“炎热”阿给玛
   tf_hero|tf_beast_man, #狼族
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_vaegir_lamellar_helmet, itm_lamellar_vest, itm_khergit_leather_boots, itm_leather_gloves, itm_kelutuo_pijia_liema, itm_southern_horn_bow, itm_khergit_arrows],
   str_33 | agi_16 | int_9 | cha_7|level(30), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (55) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_3|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   0x00000008532450cb46e4a73d2b71573200000000001f5a460000000000000000],

  ["knight_3_35", "Chief Sihendai","Sihendai", #女酋长“精明”司晨黛
   tf_hero|tf_female, #人类
   0, 0, fac_kingdom_3,
   [itm_nanfang_jian, itm_gorgeous_battle_shield, itm_sword_khergit_4, itm_kelutuo_duizhangkui, itm_kelutuo_zhajia_pao, itm_splinted_greaves, itm_lamellar_gauntlets, itm_linjia_zhaopaozhanma, itm_southern_knight_bow],
   str_25 | agi_23 | int_15 | cha_11|level(40), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (285) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_8|knows_horse_archery_8|knows_looting_8|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_4|knows_devout_1|knows_prisoner_management_8|knows_leadership_9|knows_trade_7,
   0x000000000f0830115b7472455e66aa9900000000001d36d40000000000000000],




########################################################乌-迪默-安基亚邦联########################################################
##
  ["knight_4_1", "Elector Eden Isaac", "Eden Isaac", #选帝侯伊登·艾萨克
   tf_hero|tf_deep_one_man, 
   0, reserved, fac_kingdom_4, 
   [itm_ocean_cleaver, itm_rip_current_assassin_helmet, itm_abyss_plate, itm_plate_boots, itm_kongju_bikai, itm_ocean_cleaver_shield, itm_armed_great_lizard],
   str_41 | agi_41 | int_28 | cha_24|level(55), wp_one_handed (520) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_12|knows_shield_11|knows_athletics_12|knows_riding_9|knows_horse_archery_12|knows_looting_8|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_8|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_7|knows_engineer_5|knows_persuasion_9|knows_array_arrangement_4|knows_memory_6|knows_study_14|knows_devout_12|knows_prisoner_management_9|knows_leadership_12|knows_trade_7, 
   0x0000000024002085084684b71a4b372a00000000000eb2dc0000000000000000],
  ["knight_4_2", "Elector Iaya Swandaster", "Iaya Swandaster", #选帝侯伊阿亚·斯旺达斯特
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_blue_gliding_eagle_shield, itm_silver_carving_axe, itm_death_eagle_helmet, itm_bloody_eagle_plate, itm_spotless_plate_boot, itm_yinse_bikai],
   str_59 | agi_48 | int_47 | cha_6|level(60),wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_8|knows_athletics_10|knows_riding_7|knows_horse_archery_8|knows_looting_6|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_10|knows_surgery_10|knows_first_aid_10|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_5|knows_memory_11|knows_study_15|knows_devout_15|knows_prisoner_management_11|knows_leadership_7,
   0x0000000d960023433ae29744e9a5986b00000000001dd2a10000000000000000],
  ["knight_4_3", "Elector Olaf Truilu", "Olaf Truilu", #选帝侯奥拉夫·特吕伊鲁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_phoenix_wand_lance, itm_medal_sword, itm_aquila_relief_shield, itm_black_bustling_helmet, itm_ancient_warrior_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_ancient_warrior_warhorse],
   str_47 | agi_44 | int_45 | cha_70|level(60), wp_one_handed (580) | wp_two_handed (580) | wp_polearm (580) | wp_archery (580) | wp_crossbow (580) | wp_throwing (580), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_8|knows_athletics_10|knows_riding_14|knows_horse_archery_10|knows_looting_9|knows_trainer_7|knows_tracking_8|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_5|knows_surgery_6|knows_first_aid_6|knows_engineer_5|knows_persuasion_12|knows_array_arrangement_5|knows_memory_14|knows_study_15|knows_prisoner_management_15|knows_leadership_11|knows_trade_5, 
   0x0000000ccd041309245ad14b744b30ac00000000001db2a90000000000000000],

  ["knight_4_4", "Marquis Rimald Shererson", "Rimald Shererson", #侯爵瑞马尔德·谢勒森
   tf_hero|tf_deep_one_woman, 
   0, reserved, fac_kingdom_4, 
   [itm_lanwen_qiqiang, itm_pectoral_shield, itm_carved_one_handed_double_edged_axe, itm_yaunding_wumiankui, itm_cormorant_light_plate_chain_composite_armor, itm_mail_boots, itm_fenzhi_huzhishoutao, itm_great_lizard],
   str_27 | agi_27 | int_18 | cha_14|level(40), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300), 
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x00000000010010880000000000000ff500000000000000000000000000000000],
  ["knight_4_5", "Marquis Tuya Tugesen", "Tuya Tugesen", #侯爵图亚·图热森
   tf_hero|tf_deep_one_woman, 
   0, reserved, fac_kingdom_4, 
   [itm_falcon_sword, itm_jinshi_touqiang, itm_divinecusp_spear, itm_divinecusp_knight_helmet, itm_heavy_spotless_plate, itm_spotless_plate_boot, itm_yinse_bikai, itm_iron_eagle_shield, itm_armed_great_lizard],
   str_42 | agi_37 | int_29 | cha_27|level(58), wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_6|knows_weapon_master_10|knows_shield_10|knows_athletics_8|knows_riding_9|knows_horse_archery_11|knows_looting_7|knows_trainer_7|knows_tracking_5|knows_tactics_7|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_5|knows_memory_13|knows_study_9|knows_devout_15|knows_prisoner_management_11|knows_leadership_8|knows_trade_4, 
   0x000000000e0000a40000000000000f1d00000000000000000000000000000000],
  ["knight_4_6", "Marquis Astrid Dolehoeg", "Astrid Dolehoeg", #侯爵阿斯特里德·度勒郝格
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_falcon_sword, itm_jinshi_touqiang, itm_divinecusp_spear, itm_divinecusp_knight_helmet, itm_heavy_spotless_plate, itm_spotless_plate_boot, itm_yinse_bikai, itm_iron_eagle_shield, itm_simple_plate_mountanic_horse_iron],
   str_42 | agi_37 | int_29 | cha_27|level(58), wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_6|knows_weapon_master_10|knows_shield_10|knows_athletics_8|knows_riding_9|knows_horse_archery_11|knows_looting_7|knows_trainer_7|knows_tracking_5|knows_tactics_7|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_5|knows_memory_13|knows_study_9|knows_devout_15|knows_prisoner_management_11|knows_leadership_8|knows_trade_4, 
   0x00000004400c10022ad96e38da892b2400000000001dcb3c0000000000000000],
  ["knight_4_7", "Count Harold Bershaus", "Harold Bershaus", #伯爵哈罗德·柏邵斯
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_silver_winged_knight_sword, itm_phoenix_fan_shaped_shield, itm_heavy_lance, itm_hongzong_wumiankui, itm_jinhua_lianjiazhaopao, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_heibaitiaopijia_ma],
   str_33 | agi_29 | int_35 | cha_24|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450), 
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_12|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_8|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_7|knows_devout_4|knows_prisoner_management_13|knows_leadership_9|knows_trade_5, 
   0x00000006690003073d9b6d4a92ada52500000000001de1180000000000000000],
  ["knight_4_8", "Count Rudd Hansen", "Rudd Hansen", #伯爵鲁德·汉森
   tf_hero|tf_deep_one_man, 
   0, reserved, fac_kingdom_4, 
   [itm_lanwen_qiqiang, itm_pectoral_shield, itm_carved_double_edged_axe, itm_guizu_wumainkui, itm_lanse_zaoqi_banjia, itm_iron_greaves, itm_gauntlets, itm_great_lizard],
   str_30 | agi_30 | int_20 | cha_17|level(45), wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380), 
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_10|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_5|knows_study_13|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x000000000700408136fc72b65daa48db00000000001d89910000000000000000],
  ["knight_4_9", "Count Hayda Ullerson", "Hayda Ullerson", #伯爵海达·乌勒森
   tf_hero|tf_deep_one_woman, 
   0, reserved, fac_kingdom_4, 
   [itm_lanwen_qiqiang, itm_pectoral_shield, itm_carved_double_edged_axe, itm_guizu_wumainkui, itm_lanse_zaoqi_banjia, itm_iron_greaves, itm_gauntlets, itm_great_lizard],
   str_30 | agi_30 | int_20 | cha_17|level(45), wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380), 
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_10|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_5|knows_study_13|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x00000000120010860000000000000fb700000000000000000000000000000000],
  ["knight_4_10", "Count Telge Hogan", "Telge Hogan", #伯爵特尔格·郝根
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_phoenix_wand_lance, itm_medal_sword, itm_aquila_relief_shield, itm_black_bustling_helmet, itm_ancient_hero_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_ancient_warrior_warhorse],
   str_52 | agi_49 | int_50 | cha_90|level(62), wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600), 
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_10|knows_athletics_12|knows_riding_15|knows_horse_archery_12|knows_looting_9|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_9|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_8|knows_engineer_6|knows_persuasion_13|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_prisoner_management_15|knows_leadership_12|knows_trade_6, 
   0x000000084b0002063d9b6d4492ada53500000000001db1180000000000000000],

  ["knight_4_11", "Viscount Rogerson Hagen", "Rogerson Hagen", #子爵罗格森·哈根
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_silver_winged_knight_sword, itm_phoenix_fan_shaped_shield, itm_heavy_lance, itm_hongzong_wumiankui, itm_jinhua_lianjiazhaopao, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_heibaitiaopijia_ma],
   str_33 | agi_29 | int_35 | cha_24|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450), 
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_12|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_8|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_7|knows_devout_4|knows_prisoner_management_13|knows_leadership_9|knows_trade_5, 
   0x000000002d000345471d4ac89dcacb2500000000001dca550000000000000000],
  ["knight_4_12", "Viscount Elric Jacobson", "Elric Jacobson", #子爵艾尔瑞克·雅各布森
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_banglian_shenniaojian, itm_crow_hunting_fan_shaped_shield, itm_jinshi_lengtouchui, itm_heijin_qishikui, itm_brilliant_silver_plate_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_great_lizard, itm_hippogriff_short_bow],
   str_31 | agi_27 | int_21 | cha_6|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_8|knows_shield_7|knows_athletics_8|knows_riding_11|knows_horse_archery_9|knows_looting_10|knows_trainer_7|knows_tracking_9|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_6|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_8|knows_persuasion_5|knows_array_arrangement_3|knows_memory_9|knows_study_4|knows_devout_5|knows_prisoner_management_15|knows_leadership_10|knows_trade_6, 
   0x0000000c1500000724936cc51c85b72500000000001dd4d80000000000000000],
  ["knight_4_13", "Viscount Farn Hallwatson", "Farn Hallwatson", #子爵法恩·哈勒沃森
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_silver_winged_noble_sword, itm_carved_double_edged_axe, itm_aquila_skoutarion, itm_tempestbringer_helmet, itm_huanghei_jiazhong_banjia, itm_iron_greaves, itm_gauntlets, itm_yinsun_lianjia_pingyuanma],
   str_31 | agi_27 | int_30 | cha_28|level(50), wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_9|knows_athletics_6|knows_riding_8|knows_horse_archery_10|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_10|knows_study_7|knows_devout_13|knows_prisoner_management_9|knows_leadership_7|knows_trade_4,
   0x0000000a3000130439233512e787392d00000000001ef7200000000000000000],
  ["knight_4_14", "Viscount Alva Berg", "Alva Berg", #子爵奥尔卡·贝尔格
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_ellite_lance, itm_silver_winged_noble_sword, itm_aquila_relief_shield, itm_jinshi_toumao, itm_marsh_knight_helmet, itm_optihaze_light_armor, itm_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_armed_great_lizard],
   str_26 | agi_22 | int_28 | cha_18|level(43), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_10|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_4|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_11|knows_leadership_8|knows_trade_4, 
   0x0000000bc70020042c69aa36ead0a69d00000000001d455c0000000000000000],

#conferderation younger knights  
  ["knight_4_15", "Baron Reyek Edenson", "Reyek Edenson", #男爵雷耶克·伊登森
   tf_hero|tf_deep_one_man, 
   0, reserved, fac_kingdom_4, 
   [itm_lanwen_qiqiang, itm_pectoral_shield, itm_carved_double_edged_axe, itm_guizu_wumainkui, itm_lanse_zaoqi_banjia, itm_iron_greaves, itm_gauntlets, itm_great_lizard],
   str_30 | agi_30 | int_20 | cha_17|level(45), wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380), 
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_10|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_5|knows_study_13|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x000000000b0010874594b2c71c86153b00000000001ed4b50000000000000000],
  ["knight_4_16", "Baron Dirigan Swandaster", "Dirigan Swandaster", #男爵迪里刚·斯旺达斯特
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_divinecusp_spear, itm_divine_beak, itm_divinecusp_knight_helmet, itm_spotless_plate, itm_spotless_plate_boot, itm_duangang_shalouhushou, itm_simple_plate_mountanic_horse_iron, itm_iron_eagle_shield],
   str_36 | agi_30 | int_24 | cha_22|level(52), wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_7|knows_riding_8|knows_horse_archery_10|knows_looting_6|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_12|knows_study_8|knows_devout_14|knows_prisoner_management_10|knows_leadership_7|knows_trade_4, 
   0x000000099700134439233512e287391d00000000001e37200000000000000000],
  ["knight_4_17", "Baron Lena Truilu", "Lena Truilu", #男爵勒纳·特吕伊鲁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_carved_knight_axe, itm_phoenix_fan_shaped_shield, itm_strong_bow, itm_bodkin_arrows, itm_guizu_wumainkui, itm_cormorant_light_plate_chain_composite_armor, itm_mail_chausses, itm_leather_gloves, itm_zongse_pijia_liema],
   str_26 | agi_23 | int_9 | cha_7|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_7|knows_riding_4|knows_horse_archery_5|knows_looting_7|knows_trainer_3|knows_tracking_7|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_4|knows_prisoner_management_5|knows_leadership_4|knows_trade_3, 
   0x0000000c2f0443837d198a2324b5b81400000000001e55a30000000000000000],
  ["knight_4_18", "Baron Giles Rimaldson", "Giles Rimaldson", #男爵吉尔丝·瑞马尔德森
   tf_hero|tf_deep_one_woman, 
   0, reserved, fac_kingdom_4, 
   [itm_ocean_cleaver, itm_rip_current_assassin_helmet, itm_abyss_plate_robe, itm_plate_boots, itm_kongju_bikai, itm_ocean_cleaver_shield],
   str_36 | agi_36 | int_25 | cha_21|level(49), wp_one_handed (450) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400), 
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_8|knows_power_draw_7|knows_weapon_master_12|knows_shield_10|knows_athletics_10|knows_riding_8|knows_horse_archery_10|knows_looting_7|knows_trainer_7|knows_tracking_8|knows_tactics_8|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_5|knows_study_14|knows_devout_11|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x00000000080000670000000000000f0a00000000000000000000000000000000],
  ["knight_4_19", "Baron Salton Tuyasen", "Salton Tuyasen", #男爵索尔顿·图亚森
   tf_hero|tf_deep_one_man, 
   0, reserved, fac_kingdom_4, 
   [itm_backhand_blade_shield, itm_backhand_blade, itm_yaunding_wumiankui, itm_mail_and_plate, itm_mail_boots, itm_fenzhi_huzhishoutao],
   str_28 | agi_28 | int_18 | cha_14|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330), 
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x000000002600004924e426c36f15b27300000000000dcaf20000000000000000],

  ["knight_4_20", "Baron Goleta Dolehogg", "Goleta Dolehogg", #男爵各勒塔·度勒郝格
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_4, 
   [itm_silver_winged_noble_sword, itm_carved_double_edged_axe, itm_aquila_skoutarion, itm_tempestbringer_helmet, itm_huanghei_jiazhong_banjia, itm_iron_greaves, itm_gauntlets, itm_yinsun_lianjia_pingyuanma],
   str_31 | agi_27 | int_30 | cha_28|level(50), wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_9|knows_athletics_6|knows_riding_8|knows_horse_archery_10|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_10|knows_study_7|knows_devout_13|knows_prisoner_management_9|knows_leadership_7|knows_trade_4,
   0x00000004870c10023adc6e38dcc92b2400000000001d3aec0000000000000000],
  ["knight_4_21", "Baron Eric Haroldson", "Eric Haroldson", #男爵俄丽克·哈罗德森
   tf_hero|tf_deep_one_woman, 
   0, reserved,  fac_kingdom_4, 
   [itm_heibaiyu_nushi, itm_birch_crossbow, itm_phoenix_fan_shaped_shield, itm_jinshi_langtouchui, itm_heizong_wumiankui, itm_confederation_female_cavalry_armor, itm_mail_boots, itm_scale_gauntlets],
   str_24| agi_16 | int_22 | cha_26|level(42), wp_one_handed (340) | wp_two_handed (340) | wp_polearm (310) | wp_archery (310) | wp_crossbow (310) | wp_throwing (310), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_6|knows_horse_archery_4|knows_looting_4|knows_trainer_8|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_6|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_5|knows_engineer_9|knows_persuasion_6|knows_array_arrangement_3|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_13|knows_leadership_6|knows_trade_5, 
   0x00000000020020590000000000000e5e00000000000000000000000000000000],
  ["knight_4_22", "Baron Lars Rudson", "Lars Rudson", #男爵拉尔斯·鲁德森
   tf_hero|tf_deep_one_man, 
   0, reserved, fac_kingdom_4, 
   [itm_backhand_blade_shield, itm_backhand_blade, itm_yaunding_wumiankui, itm_mail_and_plate, itm_mail_boots, itm_fenzhi_huzhishoutao],
   str_28 | agi_28 | int_18 | cha_14|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330), 
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x00000000140040812921ecad1c8db33c000000000011b5a50000000000000000],
  ["knight_4_23", "Baron Raffle Heidasen", "Raffle Heidasen", #男爵莱芙·海达森
   tf_hero|tf_deep_one_woman, 
   0, reserved, fac_kingdom_4, 
   [itm_blowgun_arrow, itm_poison_blowgun, itm_backhand_sabre, itm_backhand_sabre_shield, itm_yaunding_wumiankui, itm_cormorant_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets, itm_great_lizard],
   str_24 | agi_24 | int_16 | cha_13|level(39), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (320) | wp_throwing (280), 
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_8|knows_shield_7|knows_athletics_9|knows_riding_6|knows_horse_archery_8|knows_looting_7|knows_trainer_5|knows_tracking_6|knows_tactics_9|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   0x00000000040020a20000000000000f2300000000000000000000000000000000],

  ["knight_4_24", "Baron Knut Hogan", "Knut Hogan", #男爵克努特·郝根
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_double_sided_lance, itm_jarid, itm_jarid, itm_carved_one_handed_double_edged_axe, itm_heizong_wumiankui, itm_eagle_flock_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets, itm_huanghiepijia_ma],
   str_21 | agi_18 | int_10 | cha_10|level(36), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (200) | wp_crossbow (200) | wp_throwing (290), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_6|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3, 
   0x000000002204539057158d229b4e4ad400000000001db6940000000000000000],
  ["knight_4_25", "Marquis Harry Virtanen", "Harry Virtanen", #侯爵哈里·维尔塔宁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_carved_double_edged_axe, itm_silver_winged_great_sword, itm_purifier_winged_knight_skoutarion, itm_gorgeous_eagle_helmet, itm_huangbai_banjiayi, itm_iron_greaves, itm_yuanzhi_bikai],
   str_30 | agi_26 | int_16 | cha_14|level(48), wp_one_handed (470) | wp_two_handed (470) | wp_polearm (470) | wp_archery (470) | wp_crossbow (470) | wp_throwing (470),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_8|knows_shield_8|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_4|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_7|knows_devout_12|knows_prisoner_management_9|knows_leadership_6|knows_trade_4, 
   0x0000000195000387185cb16713b232d900000000001c73210000000000000000],
  ["knight_4_26", "Count Toivo Korhonen", "Toivo Korhonen", #伯爵托伊沃·科诺宁
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_medal_sword, itm_aquila_relief_shield, itm_fengniao_jian, itm_optihazation_knight_helmet, itm_optihaze_heavy_armor, itm_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_phoenix_splendid_bow, itm_armed_great_lizard],
   str_33 | agi_29 | int_35 | cha_24|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450), 
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_12|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_8|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_7|knows_devout_4|knows_prisoner_management_13|knows_leadership_9|knows_trade_5, 
   0x0000000240081005469289b9b2ae571c00000000001d44ec0000000000000000],
  ["knight_4_27", "Count Onni Pekkanen", "Onni Pekkanen", #伯爵翁尼·佩卡宁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_aquila_relief_shield, itm_jarid, itm_jarid, itm_carved_one_handed_axe, itm_wumiankui, itm_thunderwing_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets],
   str_22 | agi_18 | int_10 | cha_10|level(37), wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (200) | wp_crossbow (200) | wp_throwing (300), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_4|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3,  
   0x0000000fbf0463454ae379e56369c51c00000000001da4d30000000000000000],
  ["knight_4_28", "Count Hakan Makinen", "Hakan Makinen", #伯爵哈坎·梅基宁
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_medal_sword, itm_aquila_relief_shield, itm_fengniao_jian, itm_optihazation_knight_helmet, itm_optihaze_heavy_armor, itm_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_phoenix_splendid_bow, itm_armed_great_lizard],
   str_33 | agi_29 | int_35 | cha_24|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450), 
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_12|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_8|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_7|knows_devout_4|knows_prisoner_management_13|knows_leadership_9|knows_trade_5, 
   0x0000000e9308201133a22e672395f8ec00000000001d354a0000000000000000],
  ["knight_4_29", "Count Hans Nyblom", "Hans Nyblom", #伯爵汉斯·尼布鲁姆
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_silver_winged_knight_sword, itm_phoenix_fan_shaped_shield, itm_heavy_lance, itm_hongzong_wumiankui, itm_jinhua_lianjiazhaopao, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_heibaitiaopijia_ma],
   str_23 | agi_20 | int_13 | cha_12|level(38), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_6|knows_athletics_4|knows_riding_7|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3, 
   0x0000000e840043142ceec606e496b69b00000000001e56560000000000000000],

  ["knight_4_30", "Elector Nils Raikkonen", "Nils Raikkonen", #选帝侯尼尔斯·赖科宁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_phoenix_wand_lance, itm_medal_sword, itm_aquila_relief_shield, itm_black_bustling_helmet, itm_ancient_warrior_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_ancient_warrior_warhorse],
   str_47 | agi_44 | int_45 | cha_70|level(60), wp_one_handed (580) | wp_two_handed (580) | wp_polearm (580) | wp_archery (580) | wp_crossbow (580) | wp_throwing (580), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_8|knows_athletics_10|knows_riding_14|knows_horse_archery_10|knows_looting_9|knows_trainer_7|knows_tracking_8|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_5|knows_surgery_6|knows_first_aid_6|knows_engineer_5|knows_persuasion_12|knows_array_arrangement_5|knows_memory_14|knows_study_15|knows_prisoner_management_15|knows_leadership_11|knows_trade_5, 
   0x0000000e840845842d236b532e50dc9900000000000a9edc0000000000000000],

  ["knight_4_31", "Count Harden Walkpa", "Harden Walkpa", #伯爵哈登·瓦尔克帕
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_carved_one_handed_axe, itm_silver_winged_great_sword, itm_winged_elliptical_tower_shield, itm_vaegir_mask, itm_phoenix_plate_chain_composite_armor, itm_splinted_greaves, itm_scale_gauntlets],
   str_25 | agi_22 | int_13 | cha_12|level(40), wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_6|knows_shield_7|knows_athletics_5|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_2|knows_devout_4|knows_prisoner_management_7|knows_leadership_5|knows_trade_3, 
   0x0000000ea600154f29597ae68a4fa91200000000001e22cc0000000000000000],
  ["knight_4_32", "Count Augie Hamalanen", "Augie Hamalanen", #伯爵奥吉·哈马莱宁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_carved_knight_axe, itm_phoenix_fan_shaped_shield, itm_strong_bow, itm_bodkin_arrows, itm_guizu_wumainkui, itm_cormorant_light_plate_chain_composite_armor, itm_mail_chausses, itm_leather_gloves, itm_zongse_pijia_liema],
   str_26 | agi_23 | int_9 | cha_7|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_7|knows_riding_4|knows_horse_archery_5|knows_looting_7|knows_trainer_3|knows_tracking_7|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_4|knows_prisoner_management_5|knows_leadership_4|knows_trade_3, 
   0x0000000e820c52094a655ac52b7a3ad500000000001e34b30000000000000000],
  ["knight_4_33", "Marquis Helvi Valo", "Helvi Valo", #侯爵海尔维·瓦洛
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_carved_double_edged_axe, itm_phoenix_fan_shaped_shield, itm_ellite_lance, itm_shouling_wumiankui, itm_confederation_female_cavalry_armor, itm_marsh_knight_boot, itm_fenzhi_fubanshoutao, itm_great_lizard],
   str_23| agi_19 | int_12 | cha_13|level(40), wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260), 
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_8|knows_horse_archery_6|knows_looting_7|knows_trainer_3|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_5|knows_devout_1|knows_prisoner_management_10|knows_leadership_7|knows_trade_4, 
   0x0000000e4204400132ec31c6eaa9b6db00000000001e2a620000000000000000],
  ["knight_4_34", "Count Simo Niinisto", "Simo Niinisto", #伯爵西蒙·尼尼托斯
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_carved_knight_axe, itm_phoenix_fan_shaped_shield, itm_strong_bow, itm_bodkin_arrows, itm_guizu_wumainkui, itm_cormorant_light_plate_chain_composite_armor, itm_mail_chausses, itm_leather_gloves, itm_zongse_pijia_liema],
   str_26 | agi_23 | int_9 | cha_7|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_7|knows_riding_4|knows_horse_archery_5|knows_looting_7|knows_trainer_3|knows_tracking_7|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_4|knows_prisoner_management_5|knows_leadership_4|knows_trade_3, 
   0x0000000e8904154f285e91271b8cb91a00000000001e26e60000000000000000],
  ["knight_4_35", "Count Marja Haukio", "Marja Haukio", #伯爵莉雅·郝吉奥
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_ellite_lance, itm_silver_winged_noble_sword, itm_aquila_relief_shield, itm_jinshi_toumao, itm_marsh_knight_helmet, itm_optihaze_light_armor, itm_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_armed_great_lizard],
   str_26 | agi_22 | int_28 | cha_18|level(43), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_10|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_4|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_11|knows_leadership_8|knows_trade_4, 
   0x000000019908001d22538e3ae1a5ba5d00000000001ec8b30000000000000000],

  ["knight_4_36", "Viscount Marko Nieminen", "Marko Nieminen", #子爵马尔科·涅米宁
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_falcon_sword, itm_silver_plated_sabre, itm_jinshi_touqiang, itm_exorcist_battle_shield, itm_white_beak_helmet, itm_papal_knight_chain_armor, itm_mail_boots, itm_fenzhi_fubanshoutao],
   str_27 | agi_24 | int_30 | cha_26|level(42),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (235) | wp_crossbow (235) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_5|knows_trainer_5|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_9|knows_array_arrangement_3|knows_memory_9|knows_study_8|knows_devout_14|knows_prisoner_management_8|knows_leadership_6|knows_trade_3,
   0x0000000ea80c530e3ab2f1432372350b00000000001c48e40000000000000000],
  ["knight_4_37", "Viscount Oiva Ahtisaari", "Oiva Ahtisaari", #子爵奥伊瓦·阿赫蒂萨里
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_4, 
   [itm_polehammer, itm_jinshi_tuntouzhang, itm_half_bird_fan_shaped_shield, itm_hongzong_wumiankui, itm_huisejianyi_banlianjia, itm_mail_boots, itm_mail_mittens, itm_hongbaiyinpijia_ma],
   str_23 | agi_19 | int_10 | cha_8|level(40), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (310) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_8|knows_trainer_5|knows_tracking_8|knows_tactics_5|knows_pathfinding_5|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_6|knows_persuasion_3|knows_array_arrangement_3|knows_memory_5|knows_study_3|knows_devout_4|knows_prisoner_management_11|knows_leadership_6|knows_trade_5, 
   0x0000000ebd1000072862754971b624d400000000001d14930000000000000000],
  ["knight_4_38", "Baron Jean Marin", "Jean Marin", #男爵金·马林
   tf_hero, 
   0, reserved, fac_kingdom_4, 
   [itm_banglian_shenniaojian, itm_silver_winged_noble_sword, itm_crow_hunting_fan_shaped_shield, itm_vaegir_mask, itm_lanbai_banjiayi, itm_steel_leather_boot, itm_fenzhi_fulianshoutao, itm_archer_longbow],
   str_22 | agi_21 | int_13 | cha_12|level(38), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (310) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3, 
   0x0000000ea90063434af38998cdb226ca00000000001db8ec0000000000000000],




###########################################################教皇国###########################################################
##
  ["knight_5_1", "Archbishop Auguste Lazio", "Auguste Lazio", #都主教奥格斯特·拉齐奥
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jugde_fan_shaped_shield, itm_holy_selected_lance, itm_paladin_sword, itm_zhujiao_mao, itm_heavy_bishop_robe_armor, itm_papal_elite_knight_boot, itm_huali_shalouhushou, itm_divine_iron_warhorse],     
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000a1b0c00484cdcbaa5ac9a349200000000001ca4dc0000000000000000],
  ["knight_5_2", "Archbishop Amuri Sutton", "Amuri Sutton", #都主教阿蒙瑞·萨顿
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_shouhuzhe_chaochangqiang, itm_paladin_sword, itm_zhujiao_mao, itm_heavy_bishop_robe_armor, itm_papal_elite_knight_boot, itm_huali_shalouhushou, itm_patron_tower_shield],    
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000c390c659229136db45a75251300000000001f16930000000000000000],
  ["knight_5_3", "Archbishop Alatino Rossi", "Alatino Rossi", #都主教阿拉蒂诺·罗希
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_zhujian_xinzhang, itm_paladin_sword, itm_zhujiao_mao, itm_bishop_robe_armor, itm_papal_elite_knight_boot, itm_huali_shalouhushou, itm_deism_round_shield, itm_palatin_warhorse],    
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x00000000230000254829a534a465a45a00000000001d48d20000000000000000],
  ["knight_5_4", "Archbishop Ambrogio Parodi", "Ambrogio Parodi", #都主教安布罗吉奥·帕罗迪
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_zhujian_xinzhang, itm_paladin_sword, itm_zhujiao_mao, itm_bishop_robe_armor, itm_papal_elite_knight_boot, itm_huali_shalouhushou, itm_sanctification_seeker_shield, itm_palatin_warhorse],    
    str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000],
  ["knight_5_5", "Bishop Gianluca Colombo", "Gianluca Colombo", #主教詹卢卡·科伦坡
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_asterisk_staff, itm_silver_great_sowrd, itm_jiaoguo_zhongkui, itm_armed_priest_plate, itm_iron_greaves, itm_gauntlets, itm_papal_holy_cavalry_shield, itm_simple_plate_mountanic_horse_luxurious],
   str_36 | agi_30 | int_25 | cha_25|level(52),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_7|knows_athletics_6|knows_riding_7|knows_horse_archery_8|knows_looting_4|knows_trainer_8|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_12|knows_study_11|knows_devout_15|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000009ff0810051c5d57a46c8eb72100000000001d569b0000000000000000],
  ["knight_5_6", " Bishop Benedetto Ferrero", "Benedetto Ferrero", #主教贝内代托·费雷罗
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_hymn_great_sword, itm_sanctification_seeker_shield, itm_steel_asterisk_staff, itm_shengeqishi_fumiankui, itm_hymn_high_knight_plate, itm_hymn_knight_boot, itm_huali_shalouhushou, itm_palatin_warhorse],
   str_63 | agi_45 | int_57 | cha_50|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_15|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_14|knows_shield_12|knows_athletics_13|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_6|knows_tactics_8|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_7|knows_memory_13|knows_study_15|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_5, 
   0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000],
  ["knight_5_7", "Bishop Camilo Russo", "Camilo Russo", #主教卡米洛·鲁索
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_jingling_shuyongjian, itm_deism_round_shield, itm_knight_recurve_bow, itm_steel_asterisk_staff, itm_iron_sister_chain_hood, itm_arcane_eilte_plate, itm_saintess_boot, itm_yinse_bikai, itm_highknight_warhorse],
   str_58 | agi_55 | int_63 | cha_59|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_13|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_7|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_13|knows_prisoner_management_7|knows_leadership_12|knows_trade_4, 
   0x00000000030c20156b14c9d86c8ac69500000000001f69220000000000000000],
  ["knight_5_8", "Bishop Carmelo Fife", "Carmelo Fife", #主教卡梅罗·法夫
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jingling_shuyongjian, itm_deism_round_shield, itm_knight_recurve_bow, itm_steel_asterisk_staff, itm_gangshizi_yi_jukui, itm_high_theologian_chain_armor, itm_papal_elite_knight_boot, itm_yinse_bikai, itm_highknight_warhorse],
   str_58 | agi_55 | int_63 | cha_59|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_13|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_7|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_13|knows_prisoner_management_7|knows_leadership_12|knows_trade_4, 
   0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000],
  ["knight_5_9", "Bishop Aurelio Veneto", "Aurelio Veneto", #主教奥雷里奥·维尼托
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000],
  ["knight_5_10", "Bishop Emmanuel Waller", "Emmanuel Waller", #主教伊曼纽尔·瓦勒
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000],
  ["knight_5_11", "Bishop Federico Umbria", "Federico Umbria", #主教费德里科·翁布里亚
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000],
  ["knight_5_12", "Bishop Giancarlo Tuscany", "Giancarlo Tuscany", #主教詹卡洛·托斯卡纳
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000],
  ["knight_5_13", "Bishop Joshua Sicily", "Joshua Sicily", #主教约书亚·西西里
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000],
  ["knight_5_14", "Bishop Eliza Sadnia", "Eliza Sadnia", #主教伊莉莎·萨德尼亚
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_hymn_great_sword, itm_sanctification_seeker_shield, itm_steel_asterisk_staff, itm_shengeqishi_fumiankui, itm_hymn_high_knight_plate, itm_hymn_knight_boot, itm_huali_shalouhushou, itm_palatin_warhorse],
   str_63 | agi_45 | int_57 | cha_50|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_15|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_14|knows_shield_12|knows_athletics_13|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_6|knows_tactics_8|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_7|knows_memory_13|knows_study_15|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_5, 
   0x000000000308001c470c9636a54abae2000000000016b5240000000000000000],
  ["knight_5_15", "Pastor Eleonora Liguria", "Eleonora Liguria", #教长伊莱诺拉·利古里亚
   tf_hero|tf_female, 
   0, reserved,  fac_kingdom_5, 
   [itm_deism_round_shield, itm_iron_sister_chain_hood, itm_arcane_light_plate, itm_saintess_boot, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse, itm_steel_asterisk_staff, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_38 | agi_34 | int_51 | cha_44|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000000308301c352e49a81bb120b200000000000b36d90000000000000000],
  ["knight_5_16", "Pastor Katrina Friuli", "Katrina Friuli", #教长卡特琳娜·弗留利
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_deism_round_shield, itm_iron_sister_chain_hood, itm_arcane_light_plate, itm_saintess_boot, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse, itm_steel_asterisk_staff, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_38 | agi_34 | int_51 | cha_44|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000000510202c674c89bb6345311400000000001e28e20000000000000000],
  ["knight_5_17", "Pastor Simone Calabria", "Simone Calabria", #教长西蒙娜·卡拉布里亚
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_deism_round_shield, itm_iron_sister_chain_hood, itm_arcane_light_plate, itm_saintess_boot, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse, itm_steel_asterisk_staff, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_38 | agi_34 | int_51 | cha_44|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000000a002006478b2cab63615d1400000000001ec66c0000000000000000],
  ["knight_5_18", "Pastor Guglielmo Abruzzo", "Guglielmo Abruzzo", #教长古列尔莫·阿布鲁佐
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000],

#papal younger knights  
  ["knight_5_19", "Pastor Agnes Lazio", "Agnes Lazio", #教长阿格尼斯·拉齐奥
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_decorated_towers_shield, itm_steel_asterisk_staff, itm_hymn_great_sword, itm_shengeqishi_fumiankui, itm_hymn_knight_plate_armor, itm_hymn_knight_boot, itm_yuanzhi_bikai],
   str_42 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_11|knows_shield_12|knows_athletics_9|knows_riding_10|knows_horse_archery_11|knows_looting_5|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_10|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000],
  ["knight_5_20", "Pastor Manuela Sutton", "Manuela Sutton", #教长曼努埃拉·萨顿
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_deism_round_shield, itm_iron_sister_chain_hood, itm_arcane_light_plate, itm_saintess_boot, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse, itm_steel_asterisk_staff, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_38 | agi_34 | int_51 | cha_44|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000000000c202824d969bd5e90b74d00000000001ea1a50000000000000000],
  ["knight_5_21", "Pastor Samantha Rossi", "NealchaSamantha Rossi", #教长萨曼塔·罗希
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_decorated_towers_shield, itm_steel_asterisk_staff, itm_hymn_great_sword, itm_shengeqishi_fumiankui, itm_hymn_knight_plate_armor, itm_hymn_knight_boot, itm_yuanzhi_bikai],
   str_42 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_11|knows_shield_12|knows_athletics_9|knows_riding_10|knows_horse_archery_11|knows_looting_5|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_10|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000000d08301837526dab8eae6a6500000000001c571c0000000000000000],
  ["knight_5_22", "Pastor Virgilio Parodi", "Virgilio Parodi", #教长维吉利奥·帕罗迪
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_baiyu_nushi, itm_birch_crossbow, itm_asterisk_staff, itm_deism_skoutarion, itm_jianliang_qingbiankui, itm_sword_pairing_friar_chain_armor, itm_splinted_greaves, itm_fenzhi_dingshishoutao, itm_grey_spiritual_horse, itm_steel_bar_skoutarion],
   str_26 | agi_23 | int_33 | cha_31|level(42),wp_one_handed (380) | wp_two_handed (235) | wp_polearm (380) | wp_archery (235) | wp_crossbow (380) | wp_throwing (235),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_8|knows_shield_11|knows_athletics_6|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_11|knows_study_8|knows_devout_12|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   0x000000003f0c0003451a90d51a8d14f300000000001dc9ab0000000000000000],
  ["knight_5_23", "Pastor Robert Colombo", "Robert Colombo", #教长罗伯特·科伦坡
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_decorated_towers_shield, itm_steel_asterisk_staff, itm_hymn_great_sword, itm_shengeqishi_fumiankui, itm_hymn_knight_plate_armor, itm_hymn_knight_boot, itm_yuanzhi_bikai],
   str_42 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_11|knows_shield_12|knows_athletics_9|knows_riding_10|knows_horse_archery_11|knows_looting_5|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_10|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000],
  ["knight_5_24", "Pastor Rosario Ferrero", "Rosario Ferrero", #教长罗莎里奥·费雷罗
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_decorated_towers_shield, itm_steel_asterisk_staff, itm_hymn_great_sword, itm_shengeqishi_fumiankui, itm_hymn_knight_plate_armor, itm_hymn_knight_boot, itm_yuanzhi_bikai],
   str_42 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_11|knows_shield_12|knows_athletics_9|knows_riding_10|knows_horse_archery_11|knows_looting_5|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_10|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000000240c20193b9eb1239b69271c00000000001db8530000000000000000],
  ["knight_5_25", "Pastor Samuel Russo", "Samuel Russo", #教长苏缪勒·鲁索
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c060400c454826e471092299a00000000001d952d0000000000000000],
  ["knight_5_26", "Pastor Salvatore Fife", "Salvatore Fife", #教长萨瓦托·法夫
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000],
  ["knight_5_27", "Pastor Rafael Veneto", "Rafael Veneto", #教长拉法勒·维尼托
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000],
  ["knight_5_28", "Pastor Sadro Valle", "Sadro Valle", #教长萨德罗·瓦勒
   tf_hero, 0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000],
  ["knight_5_29", "Pastor Mikarangilo Umbria", "Mikarangilo Umbria", #教长米卡兰吉洛·翁布里亚
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000000070472d0388d91394a4948a100000000001db4e40000000000000000],
  ["knight_5_30", "Pastor Masmiliano Tuscany", "Masmiliano Tuscany", #教长马思米利安诺·托斯卡纳
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000001408800e2291cdc39d49a72100000000001cb3990000000000000000],
  ["knight_5_31", "Pastor Markron Sicily", "Markron Sicily", #教长马尔克龙·西西里
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000053f00359334a294d2ccb6884b00000000001e5a4b0000000000000000],
  ["knight_5_32", "Pastor Isabella Sadnia", "Isabella Sadnia", #教长伊莎贝拉·萨德尼亚
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_shouhuzhe_changqiang, itm_zhongxing_fangmainkui1, itm_patron_high_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse, itm_patron_tower_shield],
   str_35 | agi_27 | int_28 | cha_22|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_14|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   0x000000003f1000021c4b91cbaa51350d00000000001e42cb0000000000000000],
  ["knight_5_33", "Bishop Alfio Brindisi", "Alfio Brindisi", #主教阿尔菲奥·布林迪西
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x00000008330c044827924adba04da96a00000000001652a40000000000000000],
  ["knight_5_34", "Bishop Gogoli Palermo", "Gogoli Palermo", #主教果戈里·巴勒莫
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x00000008230435901ad46e330a8d005a00000000001e19350000000000000000],
  ["knight_5_35", "Bishop Lorenzo Bari", "Lorenzo Bari", #主教洛伦佐·巴里
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_hymn_great_sword, itm_sanctification_seeker_shield, itm_steel_asterisk_staff, itm_shengeqishi_fumiankui, itm_hymn_high_knight_plate, itm_hymn_knight_boot, itm_huali_shalouhushou, itm_palatin_warhorse],
   str_63 | agi_45 | int_57 | cha_50|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_15|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_14|knows_shield_12|knows_athletics_13|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_6|knows_tactics_8|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_7|knows_memory_13|knows_study_15|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_5, 
   0x000000018000300236db6db6db6db6db00000000001db6db0000000000000000],
  ["knight_5_36", "Bishop Matteo Turin", "Matteo Turin", #主教马特奥·都立
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_mogang_zhuixingqiang, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_high_knight_plate, itm_reaper_knight_boot, itm_mogang_shalouhushou, itm_divine_iron_warhorse],
   str_60 | agi_55 | int_40 | cha_37|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_12|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_9|knows_trainer_8|knows_tracking_10|knows_tactics_9|knows_pathfinding_8|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_14|knows_study_13|knows_devout_14|knows_prisoner_management_14|knows_leadership_13|knows_trade_6, 
   0x0000000cec1021845463cd16c529c68c00000000001e56cb0000000000000000],
  ["knight_5_37", "Bishop Omar Otranto", "Omar Otranto", #主教奥马尔·奥特兰托
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000ceb0830923b036ed4dc352484000000000016bcdc0000000000000000],
  ["knight_5_38", "Bishop Paolo Pisa", "Paolo Pisa", #主教保罗·比萨
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x000000001000b3c64af576950ed5d6de00000000001da8760000000000000000],
  ["knight_5_39", "Pastor Pasquale Aosta", "Pasquale Aosta", #主教帕斯夸尔·奥斯塔
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   0x0000000cee0054c83d2691366d28464a00000000001eb90a0000000000000000],
  ["knight_5_40", "Bishop Bruna Garda", "Bruna Garda", #主教布鲁娜·加尔达
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_mogang_zhuixingqiang, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_high_knight_plate, itm_reaper_knight_boot, itm_mogang_shalouhushou, itm_divine_iron_warhorse],
   str_60 | agi_55 | int_40 | cha_37|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_12|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_9|knows_trainer_8|knows_tracking_10|knows_tactics_9|knows_pathfinding_8|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_14|knows_study_13|knows_devout_14|knows_prisoner_management_14|knows_leadership_13|knows_trade_6, 
   0x000000019b042028296529b2e4b6eadb00000000001ddcec0000000000000000],
  ["knight_5_41", "Bishop Fulvio Bergamo", "Fulvio Bergamo", #主教富尔维奥·贝加莫
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_mogang_zhuixingqiang, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_high_knight_plate, itm_reaper_knight_boot, itm_mogang_shalouhushou, itm_divine_iron_warhorse],
   str_60 | agi_55 | int_40 | cha_37|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_12|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_9|knows_trainer_8|knows_tracking_10|knows_tactics_9|knows_pathfinding_8|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_14|knows_study_13|knows_devout_14|knows_prisoner_management_14|knows_leadership_13|knows_trade_6, 
   0x0000000cd3041492366c49476294c4de000000000015bd240000000000000000],
  ["knight_5_42", "Bishop Ilario Frascati", "Ilario Frascati", #主教伊拉里奥·弗雷斯卡蒂
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_mogang_zhuixingqiang, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_high_knight_plate, itm_reaper_knight_boot, itm_mogang_shalouhushou, itm_divine_iron_warhorse],
   str_60 | agi_55 | int_40 | cha_37|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_12|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_9|knows_trainer_8|knows_tracking_10|knows_tactics_9|knows_pathfinding_8|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_14|knows_study_13|knows_devout_14|knows_prisoner_management_14|knows_leadership_13|knows_trade_6, 
   0x0000000672081145606491cb195596cb00000000001df4ab0000000000000000],
  ["knight_5_43", "Bishop Aleanna Foggia", "Aleanna Foggia", #主教阿莱安娜·福贾
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_deism_round_shield, itm_silver_plated_sabre, itm_xiunv_tiemian, itm_arcane_nun_armor, itm_mail_boots, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse],
   str_26 | agi_24 | int_17 | cha_18|level(40),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_6|knows_shield_8|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_6|knows_devout_11|knows_prisoner_management_4|knows_leadership_8|knows_trade_7,
   0x00000001b810002d372169a913ad14dc00000000001cb3740000000000000000],
  ["knight_5_44", "Bishop Edward Chiscario", "Edward Chiscario", #主教爱德华·奇思里奥
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jingling_shuyongjian, itm_deism_round_shield, itm_knight_recurve_bow, itm_steel_asterisk_staff, itm_gangshizi_yi_tongkui, itm_high_theologian_chain_armor, itm_papal_elite_knight_boot, itm_yinse_bikai, itm_highknight_warhorse],
   str_58 | agi_55 | int_63 | cha_59|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_13|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_7|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_13|knows_prisoner_management_7|knows_leadership_12|knows_trade_4, 
   0x000000066e0435d015234639558f492500000000001e465c0000000000000000],
  ["knight_5_45", "Bishop Micro Dolomites", "Micro Dolomites", #主教米克罗·多洛米泰斯
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_jingling_shuyongjian, itm_deism_round_shield, itm_knight_recurve_bow, itm_steel_asterisk_staff, itm_iron_sister_chain_hood, itm_arcane_eilte_plate, itm_saintess_boot, itm_yinse_bikai, itm_highknight_warhorse],
   str_58 | agi_55 | int_63 | cha_59|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_13|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_7|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_13|knows_prisoner_management_7|knows_leadership_12|knows_trade_4, 
   0x00000006650c425148a46d351baa4b2400000000001e626a0000000000000000],

  ["knight_5_46", "Pastor Tiziano Calabria", "Tiziano Calabria", #教长蒂奇亚诺·卡拉布里亚
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_shouhuzhe_changqiang, itm_zhongxing_fangmainkui1, itm_patron_high_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse, itm_patron_tower_shield],
   str_35 | agi_27 | int_28 | cha_22|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_14|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   0x000000067600514536f39657146714da00000000001d6d190000000000000000],
  ["knight_5_47", "Bishop Stefano Trieste", "Stefano Trieste", #教长斯特凡诺·特里雅斯特
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_shouhuzhe_changqiang, itm_zhongxing_fangmainkui1, itm_patron_high_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse, itm_patron_tower_shield],
   str_35 | agi_27 | int_28 | cha_22|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_14|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   0x00000006470033c546da71b30e8d38e300000000001da9630000000000000000],
  ["knight_5_48", "Pastor Coloma Elba", "Coloma Elba", #教长科洛玛·埃尔巴
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_shouhuzhe_changqiang, itm_zhongxing_fangmainkui1, itm_patron_high_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse, itm_patron_tower_shield],
   str_35 | agi_27 | int_28 | cha_22|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_14|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   0x00000001970c002e3aa292465469c4a3000000000015371a0000000000000000],
  ["knight_5_49", "Pastor Samuele Asritoqin", "Samuele Asritoqin", #教长速穆勒·阿斯里托琴
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_decorated_towers_shield, itm_steel_asterisk_staff, itm_hymn_great_sword, itm_shengeqishi_fumiankui, itm_hymn_knight_plate_armor, itm_hymn_knight_boot, itm_yuanzhi_bikai],
   str_42 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_11|knows_shield_12|knows_athletics_9|knows_riding_10|knows_horse_archery_11|knows_looting_5|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_10|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000006451032415f8ccd391c7264f400000000001d29190000000000000000],
  ["knight_5_50", "Pastor Yanni Asti", "Yanni Asti", #教长扬尼·阿斯帝
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000006520014c5654b4dcc998db92900000000001f1c540000000000000000],
  ["knight_5_51", "Pastor Oz Veneto", "Oz Veneto", #教长奥兹·威尼托
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000022b0844c754ebaf4b3351f07400000000001dbb9b0000000000000000],
  ["knight_5_52", "Pastor Carlott Romagna", "Carlott Romagna", #教长卡洛特·罗马涅
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_5, 
   [itm_deism_round_shield, itm_iron_sister_chain_hood, itm_arcane_light_plate, itm_saintess_boot, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse, itm_steel_asterisk_staff, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_38 | agi_34 | int_51 | cha_44|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000000050c402e46dbd2491a2cd52c00000000001da5a40000000000000000],
  ["knight_5_53", "Pastor Ty Rovigo", "Ty Rovigo", #教长泰·罗戈维
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000002390443c528a379cb657248e400000000001dc4d80000000000000000],
  ["knight_5_54", "Pastor Aokes Purgatorio", "Aokes Purgatorio", #教长奥克斯·普尔加托里奥
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_shouhuzhe_changqiang, itm_zhongxing_fangmainkui1, itm_patron_high_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse, itm_patron_tower_shield],
   str_35 | agi_27 | int_28 | cha_22|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_14|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   0x00000002360c318650abb536a1bee20c00000000001cc2da0000000000000000],
  ["knight_5_55", "Pastor Dutch Campodimele", "Dutch Campodimele", #教长达奇·坎波迪梅莱
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000002340805c622e1495b267749a500000000001cb5690000000000000000],
  ["knight_5_56", "Pastor Rosco Lunamatrona", "Rosco Lunamatrona", #教长罗斯科·月玛德纳
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000002130c4154486369ca8932c80c00000000001d17540000000000000000],
  ["knight_5_57", "Pastor Dungeoff Ticino", "Dungeoff Ticino", #教长邓高夫·提契诺
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x000000020510314849236a36ad4f6771000000000005c95a0000000000000000],
  ["knight_5_58", "Pastor Joaquin Palma", "Joaquin Palma", #教长乔坤·帕尔马
   tf_hero, 
   0, reserved, fac_kingdom_5, 
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   0x00000002160034d436f457e52b49c93300000000001c28d50000000000000000],




###########################################################龙树###########################################################
##
  ["knight_6_1", "Commissioner Liyuede", "Liyuede", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x0000000f3f0c8284350c7254ccb646d900000000001c98d20000000000000000
],
  ["knight_6_2", "Commissioner Fanqisi", "Fanqisi", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x0000000f040c858f1aa670576593559d00000000001daaa40000000000000000
],
  ["knight_6_3", "Commissioner Penglaien", "Penglaien", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x000000029704b14439fa59e29d90e4d300000000001dc6aa0000000000000000
],
  ["knight_6_4", "Commissioner Lunadun", "Lunadun", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x00000002971082414c6e89c85a8b22da00000000000a489b0000000000000000
],
  ["knight_6_5", "Commissioner Xieqili", "Xieqili", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000
],
  ["knight_6_6", "Commissioner Songze", "Songze", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)|wp_firearm (500),longshu_knight_skills_1, 0x0000000d801081d2485d76c52377151b00000000001eed630000000000000000
],
  ["knight_6_7", "Commissioner_Tuoya", "Tuoya", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x000000019a10700339366958ec69d96200000000001d48d20000000000000000
],
  ["knight_6_8", "Commissioner Sakashizu", "Sakashizu", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 0x00000001bf00000236db6db6db6db6db00000000001db6db0000000000000000
],
  ["knight_6_9", "Commissioner Jinghaochen", "Jinghaochen", tf_hero, 0, reserved,  fac_kingdom_6, [],   longshu_knight_attrib_1,wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (200) | wp_crossbow (500) | wp_throwing (200)| wp_firearm (500),longshu_knight_skills_1, 
0x0000000dbf049347490a7536ae7246eb00000000001db75c0000000000000000, 0x0000000dbf049347490a7536ae7246eb00000000001db75c0000000000000000],

  ["knight_6_10", "Prefecture Huliansen", "Huliansen", tf_hero, 0, reserved,  fac_kingdom_6, [],  longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x0000000d9d103108581666d9ac3196d500000000001223740000000000000000
],
  ["knight_6_11", "Prefecture Wenqiereng", "Wenqiereng", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x0000000db71062d32963a5c766924c1a00000000001cb6a10000000000000000
],
  ["knight_6_12", "Prefecture Hujiannan", "Hujiannan", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x0000000dbf0ca28426edb5b6752b075d00000000001dab2a0000000000000000
],
  ["knight_6_13", "Prefecture Nangongzuoer", "Nangongzuoer", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x0000000bbf08000618a5ad249472d4d300000000001c29560000000000000000
],
  ["knight_6_14", "Prefecture Zhaoxinyi", "Zhaoxinyi", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x0000000bbf0c95c55a8bad292c6dab5400000000001f48d20000000000000000
],
  ["knight_6_15", "Prefecture Qianlian", "Qianlian", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], 
longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2,  0x000000019800600242a3a9991180ab1300000000001e22e40000000000000000
],
  ["knight_6_16", "Prefecture Yuweiwu", "Yuweiwu", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000067f00230e12d5ad4c8b69b8de00000000001cd79a0000000000000000
],
  ["knight_6_17", "Prefecture Xiongyin", "Xiongyin", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000067f00b3ce5931519c61564acc00000000001dca9b0000000000000000
],
  ["knight_6_18", "Prefecture Jihuafu", "Jihuafu", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000067f0c818608b56dc88dd719ab00000000001e2d930000000000000000
],
  ["knight_6_19", "Prefecture Ouyangwen", "Ouyangwen", tf_hero, 0, reserved,  fac_kingdom_6, [],   
longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000022f003104596392c5460ad0e400000000000a53650000000000000000
],
  ["knight_6_20", "Prefecture Xilongsheng", "Xilongsheng", tf_hero, 0, reserved,  fac_kingdom_6, [],  
longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023f0c954243a48a671592402c00000000001f29550000000000000000
],
  ["knight_6_21", "Prefecture Zhangde", "Zhangde", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x00000002141033481a9985525c92d8dc000000000012a8e20000000000000000
],
  ["knight_6_22", "Prefecture Zhuddan", "Zhuddan", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023f00b5c32752cda2a62d50cb00000000001e271c0000000000000000
],
  ["knight_6_23", "Prefecture Fangrenfeng", "Fangrenfeng", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023f08b08146958eab14793abe00000000001e2d4e0000000000000000
],
  ["knight_6_24", "Prefecture Sunqiu", "Sunqiu", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023f08b08146958eab14793abe00000000001e2d4e0000000000000000
],
  ["knight_6_25", "Prefecture Makaige", "Makaige", tf_hero, 0, reserved,  fac_kingdom_6, [], 
longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023f0cc1d13a9b5634dbd1a76300000000001dd70d0000000000000000
],
  ["knight_6_26", "Prefecture Weiwushuang", "Weiwushuang", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],    
longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x00000001ac1020034794b1469c6aa72400000000001fa96b0000000000000000
],
  ["knight_6_27", "Prefecture Meijianhan", "Meijianhan", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023d0c8004352cb0275a2e375a00000000001deb230000000000000000
],
  ["knight_6_28", "Magistrate Dingzhao", "Dingzhao", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023f00900133243639614a369200000000001edb640000000000000000
],
  ["knight_6_29", "Magistrate Wugao", "Wugao", tf_hero, 0, reserved,  fac_kingdom_6, [],   
longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023d08a00246edb916ca6e1aa5000000000007569a0000000000000000
],
  ["knight_6_30", "Magistrate Kangkai", "Kangkai", tf_hero, 0, reserved,  fac_kingdom_6, [],  longshu_knight_attrib_2,wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (200) | wp_crossbow (450) | wp_throwing (200)| wp_firearm (450),longshu_knight_skills_2, 0x000000023e1092482b34a94b33e5252d00000000001ed7840000000000000000
],


  ["knight_6_31", "Magistrate Daiyun", "Daiyun", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_32", "Magistrate Wangjinyan", "Wangjinyan", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x000000023f08238534a24ec4f58948ac00000000001e688d0000000000000000
],
  ["knight_6_33", "Magistrate Yeruyin", "Yeruyin", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x000000019a10700339366958ec69d96200000000001d48d20000000000000000
],
  ["knight_6_34", "Magistrate Tuxiaogu", "Tuxiaogu", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000eb700851038ec2d559b94969b00000000000cb5530000000000000000
],


#longshu younger knights  
  ["knight_6_35", "Magistrate Lishaungcang", "Lishaungcang", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002fe00925228538a254c7216db00000000001156950000000000000000
],  
  ["knight_6_36", "Magistrate Fanyouyou", "Fanyouyou", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002fe00920028538a254c7216db00000000001d56950000000000000000
],
  ["knight_6_37", "Magistrate Penghouyi", "Penghouyi", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff08821056d5acc60a5269a400000000001ef6e40000000000000000
],
  ["knight_6_38", "Magistrate luziyu", "luziyu", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff10c44f28eafa456346359300000000001de9650000000000000000
],
  ["knight_6_39", "Magistrate Xieluochang", "Xieluochang", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],   longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000183043003391d77366965caaa000000000015c85b0000000000000000
],
  ["knight_6_40", "Magistrate Songjiaxin", "Songjiaxin", tf_hero, 0, reserved,  fac_kingdom_6, [],  longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff04938f4d0c6932966912f500000000001d0a460000000000000000
],
  ["knight_6_41", "Magistrate Morigeng", "Morigeng", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff108492286599371c68d5ae00000000001e535f0000000000000000
],
  ["knight_6_42", "Magistrate Yeduowenchuan", "Yeduowenchuan", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000
],
  ["knight_6_43", "Magistrate Jingzaireng", "Jingzaireng", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff0c94c562e99d375b96951400000000001e29710000000000000000
],
  ["knight_6_44", "Magistrate Huhui", "Huhui", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002d91033cb58ad2e350b964b5800000000001224ac0000000000000000
],
  ["knight_6_45", "Magistrate Weneryi", "Weneryi", tf_hero, 0, reserved,  fac_kingdom_6, [], 
longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff008310591c6ab4dc6ca72400000000001dbacb0000000000000000
],
  ["knight_6_46", "Magistrate Hukuang", "Hukuang", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff10128a5b1269b36c91e2eb00000000001e39ac0000000000000000
],
  ["knight_6_47", "Magistrate Nangongpingjiang", "Nangongpingjiang", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff0c044536f4aa1bac49ca9400000000001e23640000000000000000
],
  ["knight_6_48", "Magistrate Zhaoyazi", "Zhaoyazi", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff10025019277398b47246ca00000000001e59730000000000000000
],
  ["knight_6_49", "Magistrate Qianshenglong", "Qianshenglong", tf_hero, 0, reserved,  fac_kingdom_6, [],   knight_attrib_4,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),knight_skills_4|knows_trainer_6, 0x00000002f90040c5352dd62aad49486b00000000001ca45b0000000000000000
],
  ["knight_6_50", "Magistrate Yuguangyuan", "Yuguangyuan", tf_hero, 0, reserved,  fac_kingdom_6, [],  longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff08b14237ab6ed914c8271c00000000001d42dc0000000000000000
],
  ["knight_6_51", "Magistrate Xiongfu", "Xiongfu", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff10b349531bd174e571aadb00000000001db96b0000000000000000
],
  ["knight_6_52", "Magistrate Jishengting", "Jishengting", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff0883d4295a6d2523b5c4a000000000001d585e0000000000000000
],
  ["knight_6_53", "Magistrate Ouyangtaoli", "Ouyangtaoli", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000001b80860076514b235a389472400000000000f5d230000000000000000
],
  ["knight_6_54", "Magistrate Xizhuguo", "Xizhuguo", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff0895c1295a6d2523b5c4a000000000001d585e0000000000000000
],
  ["knight_6_55", "Magistrate Zhangwuxun", "Zhangwuxun", tf_hero, 0, reserved,  fac_kingdom_6, [], 
longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002fb0825c346c2b2351b69595e00000000001db7150000000000000000
],
  ["knight_6_56", "Magistrate Zhujie", "Zhujie", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ef10558b355e58431c89a86100000000000e58d30000000000000000
],
  ["knight_6_57", "Magistrate Fangxun", "Fangxun", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002c3086350650546312a55c07000000000000e952c0000000000000000
],
  ["knight_6_58", "Magistrate Sunzhou", "Sunzhou", tf_hero, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff0c92c827214dc90e6ad8eb00000000001d3b0c0000000000000000
],
  ["knight_6_59", "Magistrate Mazhen", "Mazhen", tf_hero, 0, reserved,  fac_kingdom_6, [],   longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff102051486a67376bcac76b00000000001eb51c0000000000000000
],
  ["knight_6_60", "Magistrate Weihao", "Weihao", tf_hero, 0, reserved,  fac_kingdom_6, [],  longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff108492286599371c68d5ae00000000001e535f0000000000000000
],


  ["knight_6_61", "Magistrate Meifengyi", "Meifengyi", tf_hero, 0, reserved,  fac_kingdom_6, [],     longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002fe0041ca489e60b891a92b6c00000000001e390d0000000000000000
],
  ["knight_6_62", "Magistrate Dingxiaoyan", "Dingxiaoyan", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [],    longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000001bf1010013563e942a422b95c00000000001e9c5c0000000000000000
],
  ["knight_6_63", "Magistrate Wuji", "Wuji", tf_hero, 0, reserved,  fac_kingdom_6, [],   longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ff08631028f5b32c4c4ed96c00000000001d356e0000000000000000
],
  ["knight_6_64", "Magistrate Kangzhuang", "Kangzhuang", tf_hero, 0, reserved,  fac_kingdom_6, [],  
longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x00000002ec0040c12395aec94c52c72500000000001d9b730000000000000000
],


  ["knight_6_65", "Prefecture Ximuqiang", "Ximuqiang", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_66", "Prefecture Gangtang", "Gangtang", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_67", "Prefecture Hongdu", "Hongdu", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_68", "Prefecture Zhoudayou", "Zhoudayou", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_69", "Prefecture Qianbingshi", "Qianbingshi", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_70", "Prefecture Liubolu", "Liubolu", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_71", "Prefecture Qinbaopu", "Qinbaopu", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_72", "Prefecture Xiajingfeng", "Xiajingfeng", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_73", "Prefecture Zhumailun", "Zhumailun", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_74", "Prefecture Zhangzaizhen", "Zhangzaizhen", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_75", "Prefecture Yuleyong", "Yuleyong", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_76", "Prefecture Jingquanzhong", "Jingquanzhong", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_77", "Prefecture Maweizhuo", "Maweizhuo", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_78", "Prefecture Lixiuzhen", "Lixiuzhen", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_79", "Prefecture Jiangkai", "Jiangkai", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_80", "Prefecture Yinxien", "Yinxien", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_81", "Prefecture Tangpaoding", "Tangpaoding", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_82", "Prefecture Tajiro Okamoto", "Tajiro Okamoto", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_83", "Prefecture Weipeitian", "Weipeitian", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_84", "Prefecture Yokonoryo Wataru", "Yokonoryo Wataru", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_85", "Prefecture Kongyu", "Kongyu", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_86", "Prefecture Yuanbuqi", "Yuanbuqi", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_87", "Prefecture Leiqianguang", "Leiqianguang", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_88", "Prefecture Aoto Kyusyu", "Aoto Kyusyu", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_89", "Prefecture Fengbujue", "Fengbujue", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_90", "Prefecture Zhongyushi", "Zhongyushi", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_91", "Prefecture Matsuta Yoshiaki", "Matsuta Yoshiaki", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_92", "Prefecture Dingsanyou", "Dingsanyou", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_93", "Prefecture Jiangsongxiu", "Jiangsongxiu", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_94", "Prefecture Shibatomohi", "Shibatomohi", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_95", "Prefecture Huayue", "Huayue", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_96", "Prefecture Koyama kennosuke", "Koyama kennosuke", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_97", "Prefecture Murongke", "Murongke", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_98", "Prefecture Kumazaki Masaaki", "Kumazaki Masaaki", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_99", "Prefecture Okuyama Nanako", "Okuyama Nanako", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_100", "Prefecture Caiqiangjun", "Caiqiangjun", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_101", "Prefecture Dongweili", "Dongweili", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_102", "Prefecture Pioazhixin", "Pioazhixin", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_103", "Prefecture Yideri", "Yideri", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_104", "Prefecture Qiuxiaoman", "Qiuxiaoman", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_105", "Prefecture Degdu Bayar", "Degdu Bayar", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],


  ["knight_6_106", "Magistrate Baorongguang", "Baorongguang", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_107", "Magistrate Simakuaishi", "Simakuaishi", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_108", "Magistrate Shidan", "Shidan", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_109", "Magistrate Jiangqihui", "Jiangqihui", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_110", "Magistrate Qiaonasen", "Qiaonasen", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_111", "Magistrate Yankaiyuan", "Yankaiyuan", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_112", "Magistrate Takeyoshi Koji", "Takeyoshi Koji", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_113", "Magistrate Baikaixiao", "Baikaixiao", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_114", "Magistrate Hiturigu", "Hiturigu", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_115", "Magistrate Yansi", "Yansi", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],
  ["knight_6_116", "Magistrate Lizaifan", "Lizaifan", tf_hero, 0, reserved,  fac_kingdom_6, [], longshu_knight_attrib_3,wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (400) | wp_throwing (150)| wp_firearm (400),longshu_knight_skills_3, 
0x0000000ebf00834715254ee96b6544f200000000001e1b550000000000000000
],




##########################################################斯塔胡克大公国##########################################################
##
  ["knight_7_1", "Governor Norberu", "Norberu", #总督诺伯鲁侯爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_tab_shield_small_round_c, itm_scarlet_heavy_lance, itm_sergeant_sword, itm_starkhook_imported_plate_armor, itm_mail_boots, itm_scale_gauntlets, itm_julu_ianjia_pingyuanma, itm_scarlet_heavy_helmet],
   str_41 | agi_34 | int_19 | cha_21|level(48),wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (320) | wp_crossbow (200) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_7|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_9|knows_study_7|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x0000000c800430824461b2492114b92000000000001d9b990000000000000000],

  ["knight_7_2", "Governor Apuo", "Apuo", #提督阿普伯爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_huali_shalouhushou, itm_berserker_half_body_armor, itm_kuangzhanshi_kui, itm_kuangzhanshi_xue, itm_mangler_halberd],
   str_42 | agi_30 | int_15 | cha_12|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (410) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x0000000ca1045381452bb044cab4c50a00000000001dc90e0000000000000000],
  ["knight_7_3", "Governor Oden", "Oden", #提督奥登伯爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_jinshi_cejian, itm_sergeant_sword, itm_hippocampus_skoutarion, itm_sword_viking_3, itm_xihai_guizukui, itm_heise_lianxiongjia, itm_mail_boots, itm_gauntlets, itm_jiaoma_ianjia_pingyuanma, itm_lance, itm_heavy_lance, itm_lianren_fu],
   str_25 | agi_22 | int_14 | cha_13|level(40),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (340) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_8,
   0x0000000afe0c05c144de56e4a376a33100000000001e36ea0000000000000000],

  ["knight_7_4", "Governor Gunther", "Gunther", #提督冈瑟子爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_bloodthirsty_javelin, itm_kuangzhanshi_kui, itm_scarlet_bloodhonor_armor, itm_westcoast_guard_boot, itm_westcoast_black_glove, itm_bloodthirsty_javelin, itm_garrison_sickle_axe, itm_variegated_spiritual_horse, itm_steel_shield],
   str_42 | agi_35 | int_18 | cha_24|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_8|knows_shield_5|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_4|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_5|knows_leadership_7|knows_trade_4, 
   0x000000018600104d490b99dca45a58ab00000000001ee6e40000000000000000],
  ["knight_7_5", "Governor Bellamy", "Bellamy", #提督贝拉米子爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_jinshi_cejian, itm_hippocampus_skoutarion, itm_sword_viking_3, itm_xihai_guizukui, itm_heise_lianxiongjia, itm_mail_boots, itm_gauntlets, itm_lianren_fu, itm_red_short_bow, itm_weeping_blood_arrow],
   str_25 | agi_23 | int_14 | cha_13|level(41), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_8,
   0x000000053c080209291d55591b8cc99400000000001e28a50000000000000000],
  ["knight_7_6", "Governor Barnett", "Barnett", #提督巴内特子爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_sergeant_sword, itm_tab_shield_round_e, itm_qubing_lianrenfu, itm_starkhook_imported_plate_armor, itm_mail_boots, itm_scale_gauntlets, itm_scarlet_heavy_helmet],
   str_37 | agi_31 | int_18 | cha_20|level(45),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (300) | wp_crossbow (200) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_7|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_4, 
   0x00000005060063d1289b4b346c31872600000000001eb6d90000000000000000],


#starkhook younger knights  
  ["knight_7_7", "Governor Stepan", "Stepan", #提督斯捷潘男爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_jinshi_cejian, itm_sergeant_sword, itm_hippocampus_skoutarion, itm_sword_viking_3, itm_xihai_guizukui, itm_heise_lianxiongjia, itm_mail_boots, itm_gauntlets, itm_jiaoma_ianjia_pingyuanma, itm_lance, itm_heavy_lance, itm_lianren_fu],
   str_25 | agi_22 | int_14 | cha_13|level(40),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (340) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_8,
   0x00000001730021091975cdcd1bab471c00000000001199620000000000000000],
  ["knight_7_8", "Governor Heywood", "Heywood", #提督海伍德男爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_huali_shalouhushou, itm_berserker_half_body_armor, itm_kuangzhanshi_kui, itm_kuangzhanshi_xue, itm_mangler_halberd],
   str_42 | agi_30 | int_15 | cha_12|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (410) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x000000014f085441489c5356a5d638eb00000000001a2ce20000000000000000],

  ["knight_7_9", "Governor Soren", "Soren", #提督索伦伯爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_flintlock_pistol, itm_cartridges, itm_plate_covered_round_shield, itm_sergeant_sword, itm_xihai_guizumao, itm_grand_duchy_captain_half_plate, itm_steel_leather_boot, itm_fenzhi_huzhishoutao],
   str_23 | agi_18 | int_14 | cha_12|level(36),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300) | wp_firearm (100),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_6|knows_spotting_4|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_2|knows_prisoner_management_3|knows_leadership_6|knows_trade_8,
   0x000000022e0034d11b0d91a45e6db45d00000000001545550000000000000000],
  ["knight_7_10", "Governor Dineson", "Dineson", #提督迪内森伯爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_simple_archipelagic_short_bow, itm_duangang_lianrenfu, itm_blue_breeze_round_shield, itm_xihai_dingshikui, itm_gongguo_banshenjia, itm_mail_boots, itm_fenzhi_fubanshoutao, itm_julu_ianjia_pingyuanma, itm_blood_extinguish_arrow],
   str_40 | agi_33 | int_15 | cha_12|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (320) | wp_crossbow (200) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_7|knows_weapon_master_7|knows_shield_6|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_3|knows_trainer_7|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x00000002020c30024a936a2c9b731c9200000000001d231d0000000000000000],
  ["knight_7_11", "Governor Kierkegaard", "Kierkegaard", #提督克尔凯郭尔伯爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_throwing_axes, itm_heavy_throwing_axes, itm_simple_red_wind_skoutarion, itm_lianren_fu, itm_xihan_lingjiamao, itm_xuandoushi_jia, itm_mail_chausses, itm_mail_mittens, itm_huise_ma],
   str_30 | agi_28 | int_17 | cha_16|level(44),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (200) | wp_crossbow (200) | wp_throwing (440),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_6|knows_horse_archery_9|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x00000002060074d1192b94069c664a9300000000001d56930000000000000000],
  ["knight_7_12", "Governor Deepika", "Deepika", #提督迪皮卡伯爵
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_7, 
  [itm_lansexiongbanjia, itm_duangang_banjiaxue, itm_duangang_shalouhushou, itm_steel_shield, itm_jianyixihai_shoulingkui, itm_xihai_shoulingkui, itm_jinshi_shuanshoufu, itm_jinshizhanfu, itm_jinshi_toumao, itm_jinshi_touqiang],
   str_30|agi_18|int_21|cha_18|level(40),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_9|knows_power_throw_7|knows_power_draw_2|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_8|knows_tracking_2|knows_tactics_7|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_2|knows_memory_5|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_7,
   0x0000000229041091374c6e39523b34d3000000000005e9630000000000000000],


  ["knight_7_13", "Governor Luck", "Luck", #提督勒克子爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_heavy_throwing_axes, itm_tab_shield_round_e, itm_heavy_throwing_axes, itm_lianren_fu, itm_xihai_wenshikui, itm_gongguo_banshenjia2, itm_black_greaves, itm_gauntlets],
   str_40 | agi_38 | int_20 | cha_21|level(50),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (500),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_5|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x000000021b1021513c9bb5b5224637ce000000000011c7480000000000000000],
  ["knight_7_14", "Governor Rasmussen", "Rasmussen", #提督拉斯穆森子爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
  [itm_jinshi_zhanbiao, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_extra_long_shovel_axe, itm_xihai_fumiankui, itm_heise_zaoqi_banjia, itm_black_greaves, itm_mogang_yuanzhi_bikai, itm_heishu_lianjia_pinyuanma],
   str_40 | agi_38 | int_20 | cha_21|level(50),wp_one_handed (460) | wp_two_handed (460) | wp_polearm (460) | wp_archery (300) | wp_crossbow (400) | wp_throwing (480),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_8|knows_power_draw_5|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_7|knows_tracking_7|knows_tactics_6|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   0x0000000193008013491c4dc8136a38ec00000000001dd7630000000000000000],
  ["knight_7_15", "Governor Lars", "Lars", #提督拉尔斯男爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_bloodthirsty_javelin, itm_kuangzhanshi_kui, itm_bloodhonor_armor, itm_westcoast_guard_boot, itm_westcoast_black_glove, itm_heroic_halberd],
   str_43 | agi_36 | int_18 | cha_24|level(52),wp_one_handed (490) | wp_two_handed (490) | wp_polearm (490) | wp_archery (300) | wp_crossbow (300) | wp_throwing (490),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_9|knows_shield_6|knows_athletics_12|knows_riding_5|knows_horse_archery_10|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_5|knows_leadership_8|knows_trade_4, 
   0x0000000220082146315c6e271351d493000000000008ad220000000000000000],
  ["knight_7_16", "Governor Isaac", "Isaac", #提督伊萨克男爵
   tf_hero, 
   0, reserved, fac_kingdom_7, 
   [itm_bloodthirsty_javelin, itm_kuangzhanshi_kui, itm_scarlet_bloodhonor_armor, itm_westcoast_guard_boot, itm_westcoast_black_glove, itm_bloodthirsty_javelin, itm_garrison_sickle_axe, itm_variegated_spiritual_horse, itm_steel_shield],
   str_42 | agi_35 | int_18 | cha_24|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_8|knows_shield_5|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_4|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_5|knows_leadership_7|knows_trade_4, 
   0x00000001af0473c7431c6d68dd58e8cd00000000001d52ee0000000000000000],




##########################################################自由城邦##########################################################
##
  ["knight_8_1", "Consul Stafano", "Stafano", #执政官斯塔法诺爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x00000001be1035c3475eb254e45638e400000000000999190000000000000000],
  ["knight_8_2", "Consul Sylville", "Sylville", #执政官斯尔维尔爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x0000000c7f0c11853cde8ca52b726b1300000000001d26970000000000000000],
  ["knight_8_3", "Consul Tiziano", "Tiziano", #执政官提兹安诺爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x0000000c4d04348f351dad34d24ebee200000000001f68ed0000000000000000],
  ["knight_8_4", "Consul Vittorio", "Vittorio", #执政官维托里奥爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x0000000c630030c123236f44a4c9cf6900000000001eb31d0000000000000000],
  ["knight_8_5", "Consul Ricardo", "Ricardo", #执政官理卡多爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x0000000c4b10448819648d27a2aec76a00000000001e13110000000000000000],
  ["knight_8_6", "Consul Anastasia", "Anastasia", #执政官安娜施特希雅爵士
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x000000003f080020371a96b323d6b33600000000001dd7550000000000000000],

#state younger knights  
  ["knight_8_7", "Consul Nicolo", "Nicolo", #执政官尼可罗爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x00000004ff0053c8552b6d29215234a900000000001cd79e0000000000000000],
  ["knight_8_8", "Consul Luigi", "Luigi", #执政官路易吉爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x00000004ff10b3d11acd79d6db4e376100000000001f2d1b0000000000000000],

  ["knight_8_9", "Consul Farifanoo", "Farifanoo", #执政官法利法诺奥爵士
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x000000000008302d355451a6c4ce451c00000000001da51a0000000000000000],
  ["knight_8_10", "Consul Biancio", "Biancio", #执政官比安奇奥爵士
   tf_hero|tf_female, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x00000000040c001f46699a678b65ab9b00000000001cca540000000000000000],
  ["knight_8_11", "Consul Ticono", "Ticono", #执政官提可可诺爵士
   tf_hero, 
   0, reserved, fac_kingdom_8, 
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield], 
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   0x000000021b08250f4b5c3199002e492300000000001e56b30000000000000000],





  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000],
#of the family

  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],






#Royal family members

  ["knight_relatives_begin","Error - knight_relatives_begin should not appear in game","knight_relatives_begin", tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_1_wife", "Lady Anna Rodriguez", "Anna Rodriguez",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_2_wife", "Lady Nerda Ignaz", "Nerda Ignaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_1_2_daughter", "Lady Bena Ignaz", "Bena Ignaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_1_3_wife", "Lady Elena Patrick", "Elena Patrick",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_3_daughter", "Lady Constance Patrick", "Constance Patrick",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_4_wife", "Lady Vera Mahmoud", "Vera Mahmoud",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_4_daughter", "Lady Oberina Mahmoud", "Oberina Mahmoud",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_5_wife", "Lady Tiber Garcia", "Tiber Garcia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_6_wife", "Lady Marguerite Thorne","Marguerite Thorne", tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_6_daughter", "Lady Sonde Zhedosa", "Sonde Zhedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_7_wife", "Lady Melissa Exupery", "Melissa Exupery",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_7_daughter", "Lady Irina Exsuperi", "Irina Exsuperi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_1_8_daughter", "Lady Sonad Manpatton", "Sonad Manpatton",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_9_wife", "Lady Waldorf Pola", "Waldorf Pola",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_9_daughter", "Lady Alice wallov", "Alice wallov",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_10_wife", "Lady Joanna wincard", "Joanna wincard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_10_daughter", "Lady Bernatus winkard", "Bernatus winkard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_11_wife", "Lady Enrikata rolschard", "Enrikata rolschard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_11_daughter", "Lady Jaeta rolschard", "Jaeta rolschard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  ["kingdom_1_12_wife", "Lady Guy Vanderbilt", "Guy Vanderbilt",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001841010014762d6572c89a68b000000000010c9190000000000000000],
  ["kingdom_1_12_daughter", "Lady Manon Vanderbilt", "Manon Vanderbilt",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001be000003215daab4ca53d8f500000000001db86e0000000000000000],
  ["kingdom_1_13_wife", "Lady Clement ullbury", "Clement ullbury",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001bc0810023b5d95493a28fcd300000000001d55b40000000000000000],
  ["kingdom_1_13_daughter", "Lady Ann jurbury", "Ann jurbury",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a80c0002298c92629c11eba400000000001db28d0000000000000000],
  ["kingdom_1_14_wife", "Lady Adele Vuitton", "Adele Vuitton",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019610200136ab6eb30d48cd1400000000000e249b0000000000000000],
  ["kingdom_1_14_daughter", "Lady Antoinette Vuitton","Antoinette Vuitton",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001960c200346859a48eb6836dc00000000001649680000000000000000],
  ["kingdom_1_15_wife", "Lady Bert Hilton", "Bert Hilton",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000193101007395d45d7116549a4000000000011691a0000000000000000],
  ["kingdom_1_15_daughter", "Lady Charlotte Hilton", "Charlotte Hilton",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001bc0c10034d9271d5148245d200000000001d37930000000000000000],
  ["kingdom_1_16_sister", "Lady Gabrielle Phoebe", "Gabrielle Phoebe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b50400014b6d6ea8e9accda300000000001e22e40000000000000000],
  ["kingdom_1_17_sister", "Lady Mary Rex", "Mary Rex",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a70c200516a292c71a92385900000000001cc71e0000000000000000],
  ["kingdom_1_18_sister", "Lady Margaret Roberts", "Margaret Roberts",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019d0c1001405349fb94a5d75600000000001eb72b0000000000000000],  
  ["kingdom_1_19_sister", "Lady Jenna despin", "Jenna despin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018600100258a38e54e6b1129b00000000000ce8dc0000000000000000],  



  #Yishith ladies
  ["kingdom_2_1_daughter","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_2_daughter","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_3_daughter","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_4_daughter","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_5_daughter","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_6_daughter","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_7_daughter","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_8_daughter","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_9_daugter","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_10_daughter","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],



  ["kingdom_3_1_wife","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_1_daughter","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_2_wife","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_2_daughter","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_3_wife","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_3_daughter","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_4_wife","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_4_daughter","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_5_wife","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_5_daughter","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_6_wife","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_6_daughter","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_7_wife","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_7_daughter","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_8_wife","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_8_daughter","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_9_sister","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_10_sister","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_11_sister","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_12_sister","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],

  
  
  ["kingdom_4_1_wife","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_1_daughter","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_2_wife","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_2_daughter","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_3_wife","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_3_daughter","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_4_daughter","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_5_wife","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_5_daughter","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_6_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_7_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_7_daughter","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_8_wife","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_8_daughter","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_9_wife","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_9_daughter","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_10_wife","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_10_daughter","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_11_sister", "Lady Asta", "Asta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a20800042d56854af44e3cd800000000001deb640000000000000000],
  ["kingdom_4_12_sister", "Lady Freja", "Freja",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b004000154658dc79e3244e500000000001eca1d0000000000000000],
  ["kingdom_4_13_sister", "Lady Olivia", "Olivia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b810500718dfb1c524a2e8b300000000001da7220000000000000000],
  ["kingdom_4_14_sister", "Lady Sofie", "Sofie",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000181082004389b8ec5546e38cc00000000001da5110000000000000000],




  ["kingdom_5_15_sister", "Lady Ifar", "Ifar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001840810053459aab565ae37a200000000000a3d250000000000000000],
  ["kingdom_5_16_sister", "Lady Yasmin", "Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019a0400053d2c0950194da6e100000000001ecb110000000000000000],
  ["kingdom_5_17_sister", "Lady Dula", "Dula",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019f0c0007371bd9a6f28a556a00000000001eb8da0000000000000000],
  ["kingdom_5_18_sister", "Lady Ruwa", "Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c20075f2b27d55e4d957a000000000009b5510000000000000000],


  
#Sarranid ladies
  ["kingdom_6_1_wife", "Lady Jichang", "Jichang",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018700700747e32e4aa171430a00000000000db92c0000000000000000],
  ["kingdom_6_1_daughter", "Lady Lishuangjin", "Lishuangjin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a910600204ac35db946e575b0000000000173ae40000000000000000],
  ["kingdom_6_2_wife", "Lady Chengqifeng", "Chengqifeng",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001900860022ad326675c59439b000000000009ba920000000000000000],
  ["kingdom_6_2_daughter", "Lady fanyue", "fanyue",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a90060053d5ad1cabd4946e100000000000cb4e10000000000000000],
  ["kingdom_6_3_wife", "Lady Zhuangkexin", "Zhuangkexin",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000001ac047004549d69cd13a6223500000000001f40e40000000000000000],
  ["kingdom_6_3_daughter", "Lady Pengyingying", "Pengyingying",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   
0x00000001bf10200528da72c5ac89a65d00000000001da54d0000000000000000],
  ["kingdom_6_4_wife", "Lady Guanzhao", "Guanzhao",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000001a308700648eb7ddb2c71b31300000000001d6a650000000000000000],
  ["kingdom_6_4_daughter", "Lady Luju", "Luju",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019600600538e55a66d397d4ea00000000000aa6590000000000000000],
  ["kingdom_6_5_daughter", "Lady Xieshengnan", "Xieshengnan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   
0x0000000189085007551d7134d365271e000000000016274b0000000000000000],
  ["kingdom_6_6_wife", "Lady Peian", "Peian",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000001840850056b246dc9246d959400000000001db2e30000000000000000],
  ["kingdom_6_6_daughter", "Lady Songming", "Songming",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000019e0450023abe76632c19c6b400000000001e691d0000000000000000],
  ["kingdom_6_7_daughter", "Lady Shlinna", "Shlinna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_9_wife", "Lady Lisirong", "Lisirong",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001bc0460035bb4764d586ebd14000000000005b9340000000000000000],
  ["kingdom_6_9_daughter", "Lady Jingrongcan", "Jingrongcan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x000000019a10700469d4cdea7359b69300000000001cd2dd0000000000000000],
  ["kingdom_6_10_wife", "Lady Herou", "Herou",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001bf0020074eda8a655e54c69c00000000001e2b230000000000000000],
  ["kingdom_6_10_daughter", "Lady Huxi", "Huxi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000190106003595bad4b5f9a565c00000000000e22ea0000000000000000],
  ["kingdom_6_11_wife", "Lady Minwenrui", "Minwenrui",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001bf00000714e98d35646e4b3200000000001c354c0000000000000000],
  ["kingdom_6_11_daughter", "Lady Wenqiexian", "Wenqiexian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000001b8007002336d99c4dc14491b00000000000f16d10000000000000000],
  ["kingdom_6_12_wife", "Lady Luolan", "Luolan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a1087007331352949589d52b00000000000eb4ea0000000000000000],
  ["kingdom_6_12_daughter", "Lady Hulan", "Hulan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b90010036713cdc75c31945c00000000000e828b0000000000000000],
  ["kingdom_6_13_wife", "Lady Wuxian", "Wuxian",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000001820050073354545b46aab6a200000000001994fb0000000000000000],
  ["kingdom_6_13_daughter", "Lady Nangongpinjia", "Nangongpinjia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   
0x00000001a90060036ae9c95a4c9546aa00000000001e38920000000000000000],
  ["kingdom_6_14_wife", "Lady Luohesheng", "Luohesheng",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002fe10600136dc31c66399392500000000001ec4db0000000000000000],
  ["kingdom_6_14_daughter", "Lady Zhaoyalan", "Zhaoyalan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002f0105005375a95c6ac8950e300000000000627230000000000000000],
  ["kingdom_6_15_daughter", "Lady Qianshengxiang", "Qianshengxiang",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   
0x00000002ff00000436cb8db6994ea71b00000000001dcd240000000000000000],
  ["kingdom_6_16_wife", "Lady Mibei", "Mibei",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002ff0400063a5295d891599f1300000000001ca2dd0000000000000000],
  ["kingdom_6_16_daughter", "Lady Yuwenxin", "Yuwenxin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x00000002e804500646d28ec96e66d59200000000000d1b0b0000000000000000],
  ["kingdom_6_17_wife", "Lady Yinying", "Yinying",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002d504500132ae8f4aab79baee00000000001e3b090000000000000000],
  ["kingdom_6_17_daughter", "Lady Xiongmu", "Xiongmu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ec0c600556e60e28e466c4440000000000152b510000000000000000],
  ["kingdom_6_18_wife", "Lady Yaojinyu", "Yaojinyu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ff0c00035e6a4a58d2ad992200000000001dd8e10000000000000000],
  ["kingdom_6_18_daughter", "Lady Jihuashuang", "Jihuashuang",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002ff1000020713d1b75a76ab1a00000000001e9d250000000000000000],
  ["kingdom_6_19_wife", "Lady Guxinyi", "Guxinyi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002fa1000051bdab528b48e356a00000000000a1d5b0000000000000000],
  ["kingdom_6_19_daughter", "Lady Ouyangtaoyao", "Ouyangtaoyao",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002e00450033aaeac98dcae256600000000001968620000000000000000],
  ["kingdom_6_20_wife", "Lady Hankeqing", "Hankeqing",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002dd0c20063acd8a5b6c7a2a2400000000001959080000000000000000],
  ["kingdom_6_20_daughter", "Lady Xiweiwei", "Xiweiwei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002c90c5002454268e4dc956ce400000000001f24cd0000000000000000],
  ["kingdom_6_21_wife", "Lady Weiqing", "Weiqing",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002de10600548ab88c6db8676cb00000000000e44960000000000000000],
  ["kingdom_6_21_daughter", "Lady Zhangwenrui", "Zhangwenrui",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002d910600456e26a9d0b90150c00000000001e561b0000000000000000],
  ["kingdom_6_22_wife", "Lady Yanguanghua", "Yanguanghua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002d910700736d94e2cd45166e4000000000005c6740000000000000000],
  ["kingdom_6_22_daughter", "Lady Zhuyan", "Zhuyan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ff0400033b138e1662492b1c00000000001e309b0000000000000000],
  ["kingdom_6_23_daughter", "Lady Fangli", "Fangli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x00000002f9000002430b49a6dd4db549000000000019c50b0000000000000000],
  ["kingdom_6_24_wife", "Lady Yanjie", "Yanjie",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002ff04600138e889369c2944e500000000001d8eec0000000000000000],
  ["kingdom_6_24_daughter", "Lady Sunzhen", "Sunzhen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002c0087001389a92c312c8c89400000000000ab4d30000000000000000],
  ["kingdom_6_25_wife", "Lady Xueyue", "Xueyue",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002d60450072ca865f71db63714000000000012c5130000000000000000],
  ["kingdom_6_25_daughter", "Lady Maqingping", "Maqingping",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   
0x00000002ff08100148e4b1dea48da68900000000001dc4aa0000000000000000],
  ["kingdom_6_26_daughter", "Lady Weizhou", "Weizhou",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x00000002f90850033cca2dc9968ee96400000000001ddb8d0000000000000000],
  ["kingdom_6_27_wife", "Lady Jiangzhenzhu", "Jiangzhenzhu",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002e9047005372ce1e995cb4ce5000000000018a8690000000000000000],
  ["kingdom_6_27_daughter", "Lady Meiqingcheng", "Meiqingcheng",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002ff04100415519dd8a275588900000000001e38a40000000000000000],
  ["kingdom_6_28_wife", "Lady Shiliuse", "Shiliuse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ca0450023d9c69bddbceaa9300000000001ec51c0000000000000000],
  ["kingdom_6_28_daughter", "Lady Dingzhaojun", "Dingzhaojun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002c80c700428cd8a63231946a4000000000011c8f30000000000000000],
  ["kingdom_6_29_wife", "Lady Shendingxiang", "Shendingxiang",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 
0x00000002ff081003529a6935246a371b00000000001e1d1e0000000000000000],
  ["kingdom_6_29_daughter", "Lady Wujuan", "Wujuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002f810600228e978990db62a5d000000000011250c0000000000000000],
  ["kingdom_6_30_wife", "Lady Qingming", "Qingming",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002f30860075d24c73864b1d75b00000000000d5a310000000000000000],
  ["kingdom_6_30_daughter", "Lady Kangjinxi", "Kangjinxi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002f00c20063a549748e264db24000000000011bcd20000000000000000],

  ["kingdom_6_31_sister", "Lady Daiyuyu", "Daiyuyu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002fd08000738ac4dcb2ab1485d00000000001248ce0000000000000000],
  ["kingdom_6_32_sister", "Lady Wangyueyan", "Wangyueyan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ff1010063acc4ba29ecf18aa00000000001cd6d60000000000000000],
  ["kingdom_6_33_sister", "Lady Yeruhan", "Yeruhan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002f40c700224813264db6b2974000000000011531e0000000000000000],
  ["kingdom_6_34_sister", "Lady Changyuan", "Changyuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000002ff0400023b1c27d50c3534ea00000000001d23710000000000000000],



  ["kingdom_7_1_wife", "Lady Luqa", "Luqa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100457a6930ad49354e500000000001d56da0000000000000000],
  ["kingdom_7_1_daughter", "Lady Zandina", "Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001108100349dd84d72332356200000000001f39690000000000000000],
  ["kingdom_7_2_wife", "Lady Lulya", "Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001f0410043ab3514ad44dd44d00000000001db0520000000000000000],
  ["kingdom_7_2_daughter", "Lady Zahara", "Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000231010014ce590b11cb2352b00000000001e4d5d0000000000000000],
  ["kingdom_7_3_sister", "Lady Safiya", "Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000036082001576572385b92598200000000001cb75d0000000000000000],
  ["kingdom_7_4_sister", "Lady Khalisa", "Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000820054714a958f129995300000000001db76d0000000000000000],
  ["kingdom_7_5_sister", "Lady Janab", "Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001004200330ed673522514b0c00000000001d47990000000000000000],
  ["kingdom_7_6_sister", "Lady Sur", "Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000015100005269b70e4ea97552300000000001cab2b0000000000000000],



  ["kingdom_8_1_wife", "Lady Clara", "Clara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0830074333b5b65d52352a00000000001e4ad50000000000000000],
  ["kingdom_8_1_daughter", "Lady Cinzia", "Cinzia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002e1040054cdc6943a465324d00000000001e250c0000000000000000],
  ["kingdom_8_2_wife", "Lady Grazia", "Grazia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000321030072d54bb48e529c6ec00000000001db4620000000000000000],
  ["kingdom_8_2_daughter", "Lady Letizia", "Letizia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000040020034d26b1a86a52391400000000001e95a60000000000000000],
  ["kingdom_8_3_sister", "Lady Liliana", "Liliana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a102003375eb999136e6adc00000000000e92dc0000000000000000],
  ["kingdom_8_4_sister", "Lady Luana", "Luana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001108300435a2b8d52a71396300000000001e995d0000000000000000],
  ["kingdom_8_5_sister", "Lady Lucilla", "Lucilla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003f0810035892ae24e44ac2eb00000000001dd5510000000000000000],
  ["kingdom_8_6_sister", "Lady Noemi", "Noemi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001404300344d3763a9398969d00000000000d9bd10000000000000000],


  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_25_seneschal", "{!}Town 25 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_26_seneschal", "{!}Town 26 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_27_seneschal", "{!}Town 27 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_28_seneschal", "{!}Town 28 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_29_seneschal", "{!}Town 29 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_30_seneschal", "{!}Town 30 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_31_seneschal", "{!}Town 31 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_32_seneschal", "{!}Town 32 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_33_seneschal", "{!}Town 33 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_34_seneschal", "{!}Town 34 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],

  ["castle_1_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_1_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_1_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_1_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_1_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_1_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_1_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_1_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_1_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_1_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_11_seneschal", "{!}Castle 1_11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_12_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_13_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_14_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_15_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_16_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_17_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_18_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_19_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_20_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_22_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_23_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_1_24_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

  ["castle_2_1_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_2_2_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_2_3_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_2_4_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_2_5_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_2_6_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_2_7_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_2_8_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_10_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_11_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_12_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_13_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_14_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_15_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_2_16_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],

  ["castle_3_1_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_3_2_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_3_3_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_4_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_3_5_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_3_6_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_3_7_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_8_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_9_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_10_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_11_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_12_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_13_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_3_14_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],

  ["castle_4_1_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_4_2_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_4_3_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_4_4_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_4_5_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_4_6_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_4_7_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_8_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_4_9_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_10_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_11_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_12_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_13_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_14_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_4_16_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],

  ["castle_5_1_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_5_2_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_5_3_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_5_4_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_5_5_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_6_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_7_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_8_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_9_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_10_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_11_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_12_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_13_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_14_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_15_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_16_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_17_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_18_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_19_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_21_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_22_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_5_23_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

  ["castle_6_1_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_2_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_3_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_4_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_6_5_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_6_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_6_7_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_8_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_9_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_10_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_11_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_12_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_13_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_14_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_15_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_16_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_17_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_18_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_19_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_21_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_22_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_23_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_24_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_25_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_26_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_27_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_28_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_29_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_31_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_32_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_33_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_34_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_35_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_36_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_37_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_38_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_39_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_6_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

  ["castle_7_1_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_7_2_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_7_3_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_7_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_7_5_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],

  ["castle_8_1_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_8_2_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_8_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_8_4_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],



#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_23_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_24_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_25_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_26_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_26_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_27_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_27_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_28_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_28_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_29_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_29_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_30_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_30_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_31_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_31_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_32_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_32_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_33_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_33_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_34_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_34_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_23_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_24_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_25_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_29_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_30_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_31_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_32_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_33_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_34_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_23_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_24_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_25_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_26_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_27_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_28_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_29_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_30_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_31_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_32_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_33_weaponsmith","Weaponsmith",  "{!}Weaponsmith",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_34_weaponsmith","Weaponsmith",  "{!}Weaponsmith",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],


#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_23_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_23_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_24_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_24_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_25_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_25_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_26_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_26_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_27_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_27_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_28_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_28_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_29_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_29_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_30_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_30_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_31_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_31_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_32_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_32_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_33_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_33_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_34_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_34_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],


#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_woolen_dress,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_23_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_24_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_26_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_26_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_27_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_28_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_28_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_29_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_30_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_30_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_31_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_31_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_32_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_32_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_33_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_33_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_34_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_34_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_23_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_24_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_25_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_26_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_27_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_28_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_29_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_30_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_31_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_32_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_33_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_34_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_24_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_25_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_26_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_27_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_28_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_29_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_30_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_31_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_32_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_33_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_34_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_1_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_1_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_1_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_1_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_1_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_1_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_1_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_1_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_1_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_1_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_1_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_1_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_1_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_1_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_1_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_1_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_1_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_1_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_1_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_1_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_1_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_1_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_1_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_1_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_1_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],

  ["village_2_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_2_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_2_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_2_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_2_7_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_2_8_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_9_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_2_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_2_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_2_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_2_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_2_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_2_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_2_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],

  ["village_3_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_3_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_3_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_3_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_3_7_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_3_8_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_3_9_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_3_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],

  ["village_4_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_8_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_9_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_4_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],

  ["village_5_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_5_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_5_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_5_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_7_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_8_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_5_9_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_5_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_5_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_5_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_5_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_5_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_5_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_5_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_5_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_5_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],

  ["village_6_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_6_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_6_7_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_8_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_6_9_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_6_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_6_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_6_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_6_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_6_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_6_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],

  ["village_7_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_7_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_8_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_9_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_7_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],

  ["village_8_1_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_2_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_3_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_4_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_5_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_6_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_8_7_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],

# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  ["town_23_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_24_master_craftsman", "{!}Town 24 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_25_master_craftsman", "{!}Town 25 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_26_master_craftsman", "{!}Town 26 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_27_master_craftsman", "{!}Town 27 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_28_master_craftsman", "{!}Town 28 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_29_master_craftsman", "{!}Town 29 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_30_master_craftsman", "{!}Town 30 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_31_master_craftsman", "{!}Town 31 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_32_master_craftsman", "{!}Town 32 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_33_master_craftsman", "{!}Town 33 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_34_master_craftsman", "{!}Town 34 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],

# Chests
  ["player_additional_inventory_1","{!}Fiend Chest1","{!}Fiend Chest1",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dark_oath_helmet],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
  ["player_additional_inventory_2","{!}Fiend Chest1","{!}Fiend Chest1",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dark_oath_helmet],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],

  ["plot_chest_1","{!}Plot Chest1","{!}Plot Chest1",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dark_oath_helmet],def_attrib|level(18),wp(60),knows_common, 0],

  ["fiend_chest_1","{!}Fiend Chest1","{!}Fiend Chest1",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dark_oath_helmet],def_attrib|level(18),wp(60),knows_common, 0],
  ["fiend_chest_2","{!}Fiend Chest2","{!}Fiend Chest2",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_havathang],def_attrib|level(18),wp(60),knows_common, 0],
  ["fiend_chest_3","{!}Fiend Chest3","{!}Fiend Chest3",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dark_oath_shoe],def_attrib|level(18),wp(60),knows_common, 0],
  ["fiend_chest_4","{!}Fiend Chest4","{!}Fiend Chest4",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dark_oath_hand],def_attrib|level(18),wp(60),knows_common, 0],

  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  


##______________________________________________________________________quick battle related______________________________________________________________________________

  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", #下级骑士
   tf_hero,0,0,fac_kingdom_1,
   [itm_tab_shield_kite_c, itm_double_sided_lance, itm_sword_viking_2, itm_heibai_xiongjia, itm_splinted_leather_greaves, itm_leather_gloves, itm_changmain_yuantikui],
   str_14|agi_11|int_7|cha_7|level(1), wp_one_handed (100) | wp_two_handed (70) | wp_polearm (100) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_2|knows_shield_2|knows_athletics_1|knows_riding_3|knows_horse_archery_1|knows_trainer_1|knows_tactics_1|knows_leadership_1,
   0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000],

  ["quick_battle_troop_2","Usiatra","Usiatra", #军士
   tf_hero,0,0,fac_kingdom_1,
   [itm_bolts, itm_hunting_crossbow, itm_leather_warrior_cap, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_sword_two_handed_b],
   str_13|agi_9|int_7|cha_12|level(1), wp_one_handed (70) | wp_two_handed (100) | wp_polearm (70) | wp_archery (50) | wp_crossbow (100) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_2|knows_shield_1|knows_riding_1|knows_trainer_1|knows_tactics_2|knows_inventory_management_2|knows_prisoner_management_2|knows_leadership_3,
   0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000],

  ["quick_battle_troop_3","Hegen","Hegen", #侍女
   tf_hero|tf_female, 0,0,fac_kingdom_1,
   [itm_ghost_knife, itm_lute, itm_court_dress, itm_woolen_hose, itm_nvshi_shoutao, itm_book_wound_treatment_reference, itm_book_surgery_reference],
   str_8|agi_7|int_12|cha_14|level(1), wp_one_handed (50) | wp_two_handed (30) | wp_polearm (30) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),
   knows_ironflesh_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_persuasion_1|knows_memory_2,
   0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000],

  ["quick_battle_troop_4","Konrad","Konrad", #密探
   tf_hero,0,0,fac_kingdom_1,
   [itm_barbed_arrows, itm_short_bow, itm_stud_decorated_skin_battle_shield, itm_shentie_goujian, itm_padded_coif, itm_red_gambeson, itm_leather_boots, itm_leather_gloves],
   str_8|agi_14|int_12|cha_7|level(1), wp_one_handed (100) | wp_two_handed (50) | wp_polearm (50) | wp_archery (100) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_1|knows_power_strike_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_looting_2|knows_tracking_2|knows_pathfinding_1|knows_spotting_2,
   0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000],

  ["quick_battle_troop_5","Sverre","Sverre", #水手
   tf_hero,0,0,fac_kingdom_1,
   [itm_tab_shield_round_b, itm_hand_axe, itm_light_throwing_axes, itm_hongse_dianchengjia, itm_xihai_pixue, itm_leather_gloves],
   str_13|agi_7|int_11|cha_7|level(1), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (100),
   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_horse_archery_2|knows_looting_1|knows_spotting_1|knows_inventory_management_3|knows_prisoner_management_1|knows_trade_3,
   0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000],

  ["quick_battle_troop_6","Borislav","Borislav", #术士
   tf_hero,0,0,fac_kingdom_1,
   [itm_iron_staff, itm_penance_blinder, itm_leather_noble_gown, itm_blue_hose, itm_fenzhi_pishoutao],
   str_9|agi_10|int_15|cha_10|level(1), wp_one_handed (60) | wp_two_handed (60) | wp_polearm (80) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),
   knows_ironflesh_1|knows_athletics_1|knows_riding_2|knows_horse_archery_3|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_3|knows_devout_1|knows_leadership_1|knows_trade_1,
   0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000],

  ["quick_battle_troop_7","Stavros","Stavros", #公主
   tf_hero|tf_pretty_female,0,0,fac_kingdom_1,
   [itm_graghite_steel_bolts, itm_fengniao_jian, itm_papal_chain_hood, itm_vacuum_oath_armor, itm_dark_oath_shoe, itm_dark_oath_hand, itm_unicorn, itm_asterisk_staff, itm_jinshi_qishijian, itm_jiqiao_nu, itm_steel_shield, itm_phoenix_splendid_bow],
   str_20|agi_14|int_14|cha_22|level(1), wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_4|knows_study_5|knows_prisoner_management_2|knows_leadership_4|knows_trade_2,
   0x00000000000000270000000000000edb00000000000000000000000000000000],

  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [],
   str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,
   [],
   str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [],
   str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,kouruto_face_young_1, kouruto_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],



# These are used as arrays in the scripts.
  ["boss_array","{!}boss_array","{!}boss_array",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["boss_scene_array","{!}boss_scene_array","{!}boss_scene_array",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_ai","{!}temp_array_ai","{!}temp_array_ai",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["temp_array_new_map_1","{!}store natural feature","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_2","{!}for compression","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_3","{!}store center","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_4","{!}store map overlay id","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_5","{!}store map natural area name","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_6","{!}store map faction color","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_8","{!}store center overlay id","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_new_map_9","{!}store center id of overlay","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["temp_array_inflitration_sentry","{!}temp_array","{!}temp_array",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_inflitration_entry_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_inflitration_entry_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_inflitration_entry_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["temp_array_detachment","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0], #用于会战记录编队

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],


#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
   
]




