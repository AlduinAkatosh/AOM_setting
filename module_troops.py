# -*- coding: UTF-8 -*-

import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *
from ID_attributes import *

from module_troops_npc import *
from module_troops_multiplayer import *
from module_troops_mission import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): A list of items
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

#全技能模板
#knows_ironflesh_9|knows_power_strike_9|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_2|knows_trainer_2|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_desc_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_6|knows_study_4|knows_devout_1|knows_prisoner_management_3|knows_leadership_4|knows_trade_2



reserved = 0

no_scene = 0

#普威尔脸
powell_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
powell_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
powell_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
powell_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
powell_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

powell_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
powell_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
powell_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
powell_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
powell_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

#伊希斯脸
half_elf_face_key_1 = 0x00000000000000610000000000000e0000000000000000000000000000000000
half_elf_face_key_2 = 0x00000000000030710000000000000fff00000000000000000000000000000000

soul_elf_face_key_1 = 0x00000000000040810000000000000e0000000000000000000000000000000000
soul_elf_face_key_2 = 0x00000000000050b10000000000000fff00000000000000000000000000000000

demise_elf_face_key_1 = 0x00000000000060810000000000000e0000000000000000000000000000000000
demise_elf_face_key_2 = 0x00000000000070b10000000000000fff00000000000000000000000000000000

ancester_elf_face_key_1 = 0x00000000000080810000000000000e0000000000000000000000000000000000
ancester_elf_face_key_2 = 0x00000000000090b10000000000000fff00000000000000000000000000000000

vita_elf_face_key_1 = 0x000000000000a0810000000000000e0000000000000000000000000000000000
vita_elf_face_key_2 = 0x000000000000b0b10000000000000fff00000000000000000000000000000000

molter_elf_face_key_1 = 0x00000000000000010000000000000e0000000000000000000000000000000000
molter_elf_face_key_2 = 0x00000000000030200000000000000fff00000000000000000000000000000000

yishith_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
yishith_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
yishith_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
yishith_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
yishith_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

yishith_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
yishith_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
yishith_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
yishith_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
yishith_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

root_borning_one_face = 0x0000000000001000000000000000000000000000000000000000000000000000 #根生者

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
kouruto_lion_face_1 = 0x00000000000000410000000000000edb00000000001c00000000000000000000
kouruto_lion_face_2 = 0x0000000fff00104d5fffffffffffffff00000000001effff0000000000000000

kouruto_bear_face_1 = 0x00000000000020810000000000000edb00000000001c00000000000000000000
kouruto_bear_face_2 = 0x0000000fff00308d5fffffffffffffff00000000001effff0000000000000000

kouruto_wolf_face_1 = 0x00000000000040c10000000000000edb00000000001c00000000000000000000
kouruto_wolf_face_2 = 0x0000000fff0050cd5fffffffffffffff00000000001effff0000000000000000

kouruto_tiger_face_1 = 0x00000000000061010000000000000edb00000000001c00000000000000000000
kouruto_tiger_face_2 = 0x0000000fff00610d5fffffffffffffff00000000001effff0000000000000000

kouruto_cow_face_1 = 0x00000000000071410000000000000edb00000000001c00000000000000000000
kouruto_cow_face_2 = 0x0000000fff00814d5fffffffffffffff00000000001effff0000000000000000

kouruto_sheep_face_1 = 0x00000000000091810000000000000edb00000000001c00000000000000000000
kouruto_sheep_face_2 = 0x0000000fff00918d5fffffffffffffff00000000001effff0000000000000000

kouruto_deer_face_1 = 0x000000000000a1c10000000000000edb00000000001c00000000000000000000
kouruto_deer_face_2 = 0x0000000fff00b1cd5fffffffffffffff00000000001effff0000000000000000

kouruto_rabbit_face_1 = 0x000000000000c2010000000000000edb00000000001c00000000000000000000
kouruto_rabbit_face_2 = 0x0000000fff00d20d5fffffffffffffff00000000001effff0000000000000000

kouruto_dog_face_1 = 0x000000000000e2410000000000000edb00000000001c00000000000000000000
kouruto_dog_face_2 = 0x0000000fff00f24d5fffffffffffffff00000000001effff0000000000000000

kouruto_fox_face_1 = 0x00000000000102810000000000000edb00000000001c00000000000000000000
kouruto_fox_face_2 = 0x0000000fff01128d5fffffffffffffff00000000001effff0000000000000000

kouruto_cat_face_1 =0x00000000000122c10000000000000edb00000000001c00000000000000000000
kouruto_cat_face_2 = 0x0000000fff0132cd5fffffffffffffff00000000001effff0000000000000000

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


#迪默脸
diemer_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
diemer_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
diemer_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
diemer_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
diemer_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

diemer_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
diemer_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
diemer_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
diemer_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
diemer_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

#鱼人脸
deep_one_face_1 = 0x0000000000000041120000000000000800000000001c80400000000000000000
deep_one_face_2 = 0x000000003f00408d7bffffffffffffff00000000001effff0000000000000000

deep_one_woman_face_1 = 0x00000000000000410000000000000e0000000000000000000000000000000000
deep_one_woman_face_2 = 0x000000003f0020b10000000000000fff00000000000000000000000000000000

crimson_face = 0x0000000000002000000000000000000000000000000000000000000000000000 #绯世之影

#教国脸
papal_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
papal_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
papal_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
papal_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
papal_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

papal_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
papal_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
papal_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
papal_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
papal_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

#东方脸
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

powell_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
powell_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

yishith_face1  = yishith_face_young_1
yishith_face2  = yishith_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

zombie_face = 0x0000000000000000000000000000000000000000000000000000000000000000   #僵尸

#NAMES:
#

tf_guarantee_all = tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
tf_guarantee_infantry = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_pretty_female|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_7|agi_7|int_7|cha_7,wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50) | wp_firearm (400),0,0x00000000000000270000000000000edb00000000000000000000000000000000],
  ["temp_substitute","Substitute","Substitute",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [],
   str_64|agi_64|int_64|cha_64|level(63),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500) | wp_firearm (500),knows_ironflesh_15|knows_power_strike_15|knows_power_throw_15|knows_power_draw_15|knows_weapon_master_10|knows_shield_10|knows_athletics_15|knows_riding_10|knows_horse_archery_10|knows_looting_10|knows_trainer_10|knows_tracking_10|knows_tactics_10|knows_pathfinding_10|knows_spotting_10|knows_inventory_management_10|knows_wound_treatment_10|knows_surgery_10|knows_first_aid_10|knows_engineer_10|knows_persuasion_10|knows_prisoner_management_10|knows_leadership_10|knows_trade_10,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",#农民
   tf_guarantee_armor,
   no_scene,reserved,fac_commoners, 
   [itm_cleaver, itm_knife, itm_pitch_fork, itm_sickle, itm_club, itm_stones, itm_leather_cap, itm_felt_hat, itm_felt_hat, itm_linen_tunic, itm_coarse_tunic, itm_nomad_boots, itm_wrapping_boots], 
   str_7|agi_5|int_5|cha_5|level(2),wp(10),
   knows_ironflesh_1|knows_weapon_master_1|knows_inventory_management_1|knows_wound_treatment_1|knows_first_aid_1|knows_devout_1,
   man_face_middle_1, man_face_old_2, 0,
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["townsman","Townsman","Townsmen",#市民
   tf_guarantee_boots|tf_guarantee_armor,
   no_scene,reserved,fac_commoners,
    [itm_cleaver, itm_knife, itm_club, itm_quarter_staff, itm_dagger, itm_stones, itm_leather_cap, itm_linen_tunic, itm_coarse_tunic, itm_leather_apron, itm_nomad_boots, itm_wrapping_boots],  
   str_6|agi_6|int_5|cha_5|level(4), wp(30),
   knows_ironflesh_1|knows_inventory_management_2|knows_wound_treatment_1|knows_first_aid_1|knows_trade_1,
   mercenary_face_1, mercenary_face_2, 0,
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],

  ["watchman","Watchman","Watchmen",#眼线
   tf_guarantee_boots|tf_guarantee_armor,
   no_scene,reserved,fac_commoners,
   [itm_shirt, itm_linen_tunic, itm_burlap_tunic, itm_leather_apron, itm_tabard, itm_butchering_knife, itm_dagger, itm_sword_medieval_b_small, itm_sword_medieval_c, itm_straw_hat, itm_head_wrappings, itm_headcloth, itm_felt_hat, itm_felt_hat_b, itm_wrapping_boots, itm_woolen_hose, itm_blue_hose, itm_ankle_boots, itm_pitch_fork, itm_military_fork, itm_battle_fork, itm_boar_spear, itm_simple_bow, itm_practice_arrows_2, itm_arrows],  
   str_9|agi_7|int_5|cha_5|level(9), wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (70) | wp_crossbow (60) | wp_throwing (70), 
   knows_ironflesh_1|knows_power_draw_1|knows_athletics_1|knows_horse_archery_1|knows_looting_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_1|knows_first_aid_1|knows_trade_1, 
   mercenary_face_1, mercenary_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["hunter","Hunter","Hunter",#猎人
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,
   no_scene,reserved,fac_commoners,
   [itm_green_tunic, itm_tunic_with_green_cape, itm_ragged_outfit, itm_leather_vest, itm_rawhide_coat, itm_beast_skin_round_shield, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_leather_cap, itm_black_hood, itm_fur_hat, itm_padded_coif, itm_hunter_boots, itm_hide_boots, itm_nomad_boots, itm_leather_gloves, itm_leather_gloves, itm_fenzhi_pishoutao, itm_military_fork, itm_battle_fork, itm_boar_spear, itm_hunting_bow, itm_arrows, itm_arrows, itm_arrows], 
   str_12|agi_12|int_7|cha_7|level(16), wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (120) | wp_crossbow (110) | wp_throwing (120), 
   knows_ironflesh_3|knows_power_strike_1|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_1|knows_athletics_3|knows_riding_1|knows_horse_archery_2|knows_looting_3|knows_tracking_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_memory_1|knows_devout_1|knows_leadership_1|knows_trade_3, 
   mercenary_face_1, mercenary_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["mercenary_archer","Mercenary Archer","Mercenary Archer",#雇佣短弓手
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
   no_scene,reserved,fac_commoners,
   [itm_padded_leather, itm_leather_jacket, itm_pelt_coat, itm_aketon_green, itm_fur_covered_shield, itm_leather_covered_round_shield, itm_leather_warrior_cap, itm_skullcap, itm_baotie_toujin, itm_light_leather_boots, itm_leather_boots, itm_splinted_leather_greaves, itm_fenzhi_pishoutao, itm_fenzhi_jiaqiangshoutao, itm_kuotou_qiang, itm_jiachang_kuotou_qiang, itm_citou_qiang, itm_jiantou_qiang, itm_lengtou_qiang, itm_shortened_spear, itm_short_bow, itm_barbed_arrows, itm_bodkin_arrows, itm_arrows, itm_barbed_arrows, itm_barbed_arrows, itm_barbed_arrows],
   str_16|agi_14|int_8|cha_7|level(25), wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (180) | wp_crossbow (170) | wp_throwing (180), 
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_5|knows_weapon_master_3|knows_shield_2|knows_athletics_5|knows_riding_1|knows_horse_archery_2|knows_looting_6|knows_trainer_2|knows_tracking_6|knows_tactics_1|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_4|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_2|knows_trade_5,
   mercenary_face_1, mercenary_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["mercenary_skirmisher","Mercenary Skirmisher","Mercenary Skirmisher",#雇佣散兵
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   no_scene,reserved,fac_commoners,
   [itm_duanxiu_lianjiapao, itm_quanshen_lianjai, itm_ban_guokui, itm_iron_leather_greave, itm_mail_chausses, itm_fenzhi_jiaqiangshoutao, itm_spear, itm_war_spear, itm_ashwood_pike, itm_strong_bow, itm_bodkin_arrows, itm_wangguo_lierenjian],
   str_22|agi_20|int_12|cha_10|level(35),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (280) | wp_crossbow (270) | wp_throwing (280), 
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_2|knows_horse_archery_5|knows_looting_8|knows_trainer_4|knows_tracking_7|knows_tactics_3|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_6|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_5,
   mercenary_face_1, mercenary_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["blackguard_mercenary","Blackguard Mercenary","Blackguard Mercenaries",#无赖佣兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_outlaws,
  [itm_duanxiu_lianjiapao, itm_lingjia_pao, itm_heise_lianxiongjia, itm_zongse_lianxiongjia, itm_duanxiu_lianjiapao, itm_lingjia_pao, itm_duanxiu_lianjiapao, itm_splinted_leather_greaves, itm_mail_chausses, itm_mail_mittens, itm_footman_helmet, itm_nasal_helmet, itm_norman_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_flat_topped_helmet, itm_kettle_hat, itm_spiked_helmet, itm_scimitar, itm_arabian_sword_d, itm_war_axe, itm_sword_two_handed_a, itm_khergit_sword_two_handed_b, itm_shortened_voulge, itm_bardiche, itm_voulge, itm_sword_viking_3, itm_sword_viking_3_small, itm_ashwood_pike, itm_awlpike, itm_awlpike_long, itm_war_spear, itm_dark_lion_fan_shaped_shield, itm_simple_pegasus_skoutarion, itm_simple_green_wind_skoutarion, itm_simple_red_dragon_skoutarion, itm_simple_baptism_skoutarion, itm_simple_red_wind_skoutarion, itm_griffon_skoutarion, itm_tab_shield_round_a, itm_tab_shield_round_b, itm_throwing_spears, itm_throwing_knives, itm_jarid, itm_light_throwing_axes],
   str_18|agi_14|int_8|cha_8|level(25),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_1|knows_horse_archery_4|knows_looting_7|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_prisoner_management_2|knows_leadership_1|knows_trade_5,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["blackguard_sergeant","Blackguard Sergeant","Blackguard Sergeants",#无赖军士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_outlaws,
  [itm_huisejianyi_banlianjia, itm_lvsejianyi_banlianjia, itm_guyongbing_tiekui, itm_guyongbing_quankui, itm_zhuxing_fumiankui, itm_goucao_fumainkui, itm_xihai_fumiankui, itm_duangang_banjiaxue, itm_shengtie_banjiaxue, itm_fangxing_bikai, itm_yuanzhi_bikai, itm_duyin_kuotouqiang, itm_duyin_goulianqiang, itm_changliu_duanqiang, itm_podu_qiang, itm_kaitang_qiang],
   str_28|agi_19|int_10|cha_10|level(40),wp_one_handed (260) | wp_two_handed (260) | wp_polearm (330) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_7|knows_looting_12|knows_trainer_5|knows_tracking_6|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_3|knows_memory_6|knows_study_2|knows_prisoner_management_6|knows_leadership_6|knows_trade_9,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["kouruto_refugee_mercenary","Kouruto Refugee Mercenary","Kouruto Refugee Mercenarys",#科鲁托浪人雇佣兵
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged,
   0,0,fac_outlaws_kouruto_refugee,
   [],
   str_19 | agi_17 | int_10 | cha_10|level(30),wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (290) | wp_crossbow (290) | wp_throwing (290),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_6|knows_shield_5|knows_athletics_6|knows_riding_7|knows_horse_archery_7|knows_looting_10|knows_trainer_4|knows_tracking_7|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_4|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_5|knows_trade_2,
   kouruto_face_young_1, kouruto_face_old_2],

  ["roving_bandits","Roving Bandits","Roving Bandits",#武装流民
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_outlaws_robber_knight,
   [itm_arrows, itm_scimitar, itm_winged_mace, itm_spear, itm_padded_cloth, itm_aketon_green, itm_leather_jerkin, itm_ragged_outfit, itm_padded_leather, itm_leather_boots, itm_leather_gloves, itm_hunting_bow, itm_short_bow, itm_fur_hat, itm_padded_coif, itm_leather_warrior_cap, itm_skullcap, itm_sword_medieval_b, itm_sword_medieval_b_small],
   str_9 | agi_7 | int_6 | cha_5|level(8),wp_one_handed (75) | wp_two_handed (75) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_looting_3|knows_tracking_1|knows_pathfinding_1|knows_spotting_2|knows_first_aid_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_trade_2,
   bandit_face1, bandit_face2],

  ["mercenaries_end","mercenaries_end","mercenaries_end",tf_hero,no_scene,reserved,fac_no_faction,
   [],def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],



#######################################################普威尔联合王国########################################################

#——————————————————————————————联合王国通用部队————————————————————————————————
##
  ["powell_peasant","Powell Peasant","Powell Peasant",#普威尔平民
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_1,
   [itm_scythe, itm_fighting_pick, itm_club, itm_tab_shield_heater_a, itm_leather_cap, itm_felt_hat, itm_felt_hat, itm_wrapping_boots, itm_hongbai_pingmingyi, itm_hongbai_pingmingfu, itm_dahong_pingming_fu, itm_honghuang_pingmingfu, itm_pitch_fork],
   str_5|agi_5|int_4|cha_4|level(1),wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),
   knows_ironflesh_1|knows_inventory_management_1|knows_persuasion_1|knows_memory_1|knows_leadership_1|knows_trade_1,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["powell_militia","Powell Militia","Powell Militia",#普威尔民兵
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_1,
   [itm_fighting_pick, itm_boar_spear, itm_tab_shield_heater_a, itm_arming_cap, itm_hongse_dianchengpao, itm_wangguo_mingbin_mianjia, itm_zonghong_diancheng_jia, itm_zonghong_mianjia, itm_leather_warrior_cap, itm_fighting_pick, itm_shortened_spear, itm_leather_gloves, itm_leather_boots],
   str_7|agi_6|int_5|cha_4|level(5),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),
   knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_horse_archery_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_1|knows_memory_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["powell_footman","Powell Footman","Powell Footmen",#普威尔步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_fighting_pick, itm_tab_shield_heater_b, itm_mail_coif, itm_norman_helmet, itm_wangguobubing_jia, itm_leather_gloves, itm_leather_boots, itm_war_spear, itm_awlpike],
   str_13|agi_9|int_6|cha_6|level(15),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (135) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_1|knows_shield_1|knows_athletics_2|knows_riding_1|knows_horse_archery_2|knows_looting_1|knows_tactics_2|knows_spotting_1|knows_inventory_management_2|knows_surgery_1|knows_persuasion_3|knows_memory_3|knows_study_1|knows_prisoner_management_2|knows_leadership_1|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_conjuring_infantry","Powell Conjuring Infantry","Powell Conjuring Infantry",#普威尔术步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_leather_gloves, itm_sorcery_lance, itm_jiaqiang_hubi_gangkui, itm_shububing_jia, itm_mail_boots],
   str_24|agi_21|int_10|cha_6|level(30),wp_one_handed (185) | wp_two_handed (185) | wp_polearm (240) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_6|knows_power_strike_7|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_5|knows_riding_3|knows_horse_archery_2|knows_looting_3|knows_trainer_2|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_prisoner_management_2|knows_leadership_2|knows_trade_3,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["powell_horseman","Powell Horseman","Powell Horseman",#普威尔骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_segmented_helmet, itm_helmet_with_neckguard, itm_leather_gloves, itm_tab_shield_kite_a, itm_tab_shield_kite_b, itm_light_lance, itm_fighting_pick, itm_sumpter_horse, itm_saddle_horse, itm_red_gambeson, itm_leather_jerkin, itm_splinted_greaves],
   str_12|agi_10|int_6|cha_5|level(15),wp_one_handed (150) | wp_two_handed (100) | wp_polearm (150) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_surgery_1|knows_persuasion_2|knows_memory_3|knows_study_1|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["powell_conjuring_rider","Powell Conjuring Rider","Powell Conjuring Rider",#普威尔术骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_hunter, itm_mail_with_surcoat, itm_helmet_with_neckguard, itm_flat_topped_helmet, itm_leather_gloves, itm_sorcery_lance, itm_tab_shield_heater_cav_a, itm_military_pick, itm_mail_chausses],
   str_15|agi_12|int_9|cha_9|level(20),wp_one_handed (180) | wp_two_handed (50) | wp_polearm (180) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_4|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_1|knows_riding_3|knows_horse_archery_3|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_windscorching_lancer","Powell Windscorching Lancer","Powell Windscorching Lancer",#普威尔风炎枪骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_sorcery_lance, itm_leather_gloves, itm_hongshi_lianjia_pinyuanma, itm_pride_fan_shaped_shield, itm_hubi_gangkui, itm_shububing_jia, itm_iron_greaves],
   str_24|agi_21|int_10|cha_6|level(40),wp_one_handed (230) | wp_two_handed (50) | wp_polearm (300) | wp_archery (150) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_3|knows_athletics_3|knows_riding_4|knows_horse_archery_5|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_1|knows_prisoner_management_4|knows_leadership_4|knows_trade_3,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_rockglacier_ranger","Powell Rockglacier Ranger","Powell Rockglacier Ranger",#普威尔冰岩枪骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_sorcery_lance, itm_leather_gloves, itm_hubi_gangkui, itm_shububing_jia, itm_mail_boots, itm_shifupijia_ma, itm_languanpijia_ma],
   str_22 | agi_21 | int_10 | cha_10|level(40),wp_one_handed (230) | wp_two_handed (50) | wp_polearm (230) | wp_archery (270) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_1|knows_prisoner_management_4|knows_leadership_3|knows_trade_3, 
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["powell_huntsman","Powell Huntsman","Powell Huntsman",#普威尔猎人
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor,
   0,0,fac_kingdom_1,
   [itm_short_tunic, itm_red_tunic, itm_leather_gloves, itm_leather_boots, itm_arrows, itm_hunting_bow, itm_fighting_pick, itm_leather_warrior_cap, itm_skullcap, itm_arrows, itm_barbed_arrows, itm_arrows, itm_wangguo_jian],
   str_10 | agi_10 | int_6 | cha_6|level(12),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (570) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_1|knows_athletics_3|knows_riding_1|knows_horse_archery_2|knows_looting_3|knows_trainer_1|knows_tracking_3|knows_tactics_1|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_1|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["powell_skirmisher","Powell Skirmisher","Powell Skirmisher",#普威尔散兵
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_red_gambeson, itm_leather_jerkin, itm_mail_coif, itm_footman_helmet, itm_leather_gloves, itm_leather_boots, itm_fighting_pick, itm_long_bow, itm_arrows, itm_barbed_arrows, itm_barbed_arrows, itm_wangguo_jian, itm_wangguo_lierenjian],
   str_15 | agi_15 | int_8 | cha_7|level(24),wp_one_handed (120) | wp_two_handed (50) | wp_polearm (50) | wp_archery (200) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_4|knows_weapon_master_3|knows_shield_2|knows_athletics_4|knows_riding_1|knows_horse_archery_3|knows_looting_3|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["powell_nobility","Powell Nobility","Powell Nobility",#普威尔贵族
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,
   0,0,fac_kingdom_1,
   [itm_hunter, itm_red_noble_shirt, itm_leather_boots, itm_leather_gloves, itm_tab_shield_kite_cav_a, itm_tab_shield_heater_cav_a, itm_fighting_pick, itm_light_lance, itm_shortened_spear, itm_spear],
   str_15 | agi_12 | int_9 | cha_10|level(15),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_2|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["powell_noble_trainee","Powell Noble Trainee","Powell Noble Trainee",#普威尔贵族习武者
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_lance, itm_military_pick, itm_mail_chausses, itm_courser, itm_tab_shield_kite_cav_a, itm_tab_shield_kite_cav_b, itm_tab_shield_heater_cav_a, itm_tab_shield_heater_cav_b, itm_light_mail_and_plate, itm_mail_mittens, itm_segmented_helmet, itm_helmet_with_neckguard],
   str_19 | agi_15 | int_9 | cha_10|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_5|knows_devout_2|knows_prisoner_management_5|knows_leadership_5|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["powell_noble_knight","Powell Noble Knight","Powell Noble Knight",#普威尔贵胄骑士
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,
   0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_gauntlets, itm_hongsejianyi_banlianjia, itm_puweier_lianjia, itm_hongyu_hue_qingbiankui, itm_hongyu_zhumiankui, itm_jinhong_pijia_liema, itm_lance, itm_mail_boots],
   str_26 | agi_22 | int_12 | cha_15|level(40),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_6|knows_devout_3|knows_prisoner_management_7|knows_leadership_8|knows_trade_5, 
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_armored_conjurer","Powell Armored Conjurer","Powell Armored Conjurer",#普威尔铠甲术士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_sorcery_lance, itm_huijing_qingbanlianfuhe_jia, itm_changmain_hongyu_zhumiankui, itm_red_blue_fan_shaped_shield, itm_yuanzhi_bikai, itm_mail_boots],
   str_27 | agi_26 | int_18 | cha_19|level(42),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (420) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),    knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_3|knows_memory_7|knows_study_6|knows_devout_3|knows_prisoner_management_7|knows_leadership_8|knows_trade_4, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#————————————————————————————————普威尔王室—————————————————————————————————
##
  ["powell_kingcity_citizen","Powell Kingcity Citizen","Powell Kingcity Citizens",#普威尔王都市民
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_sword_medieval_a, itm_sword_medieval_c_small, itm_tab_shield_heater_b, itm_tab_shield_heater_a, itm_arming_cap, itm_hongse_dianchengjia, itm_blue_hose, itm_woolen_hose, itm_ankle_boots, itm_boar_spear, itm_military_fork, itm_throwing_knives, itm_hongbai_pingmingfu, itm_dahong_pingming_fu, itm_honghuang_pingmingfu],
   str_11|agi_7|int_6|cha_6|level(10),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_athletics_1|knows_riding_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_devout_1|knows_leadership_1|knows_trade_1,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["powell_armed_footman","Powell Armed Footman","Powell Armed Footmen",#普威尔武装步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_citou_qiang, itm_sword_medieval_b_small, itm_sword_medieval_b, itm_fighting_pick, itm_segmented_helmet, itm_wangguo_mingbin_mianjia, itm_leather_boots, itm_leather_gloves, itm_zonghong_mianjia, itm_wangguobubing_jia, itm_light_leather_boots, itm_hongse_dianchengpao, itm_tab_shield_heater_c, itm_tab_shield_heater_b, itm_military_sickle_a, itm_footman_helmet, itm_kuotou_qiang],
   str_15|agi_13|int_9|cha_9|level(20),wp_one_handed (145) | wp_two_handed (145) | wp_polearm (145) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_surgery_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["powell_strike_swordman","Powell Strike Swordman","Powell Strike Swordmen",#普威尔突击剑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_steel_shield, itm_bastard_sword_a, itm_ban_qingbiankui, itm_hongsejianyi_banlianjia, itm_mail_chausses, itm_mail_mittens],
   str_22|agi_17|int_10|cha_10|level(31),wp_one_handed (265) | wp_two_handed (265) | wp_polearm (145) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_2|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_4|knows_prisoner_management_2|knows_leadership_5|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_great_swordman","Powell Great Swordman","Powell Great Swordmen",#普威尔大剑师
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_jinseshoubanjian, itm_hongyu_hue_qingbiankui, itm_hongse_quanshenbanjia, itm_mail_chausses, itm_yuanzhi_bikai],
   str_29|agi_26|int_15|cha_17|level(45),wp_one_handed (385) | wp_two_handed (385) | wp_polearm (145) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_3|knows_athletics_6|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_7|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_sword_cavalry","Powell Sword Cavalry","Powell Sword Cavalries",#普威尔剑骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_tab_shield_heater_cav_a, itm_tab_shield_heater_cav_b, itm_tiehuan_danshoujian, itm_hongyu_hue_qingbiankui, itm_coat_of_plates_red, itm_mail_boots, itm_mail_mittens, itm_hongheipijia_ma, itm_heise_ma],
   str_26|agi_22|int_14|cha_16|level(40),wp_one_handed (325) | wp_two_handed (325) | wp_polearm (145) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_4|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["powell_heavy_infantry","Powell Heavy Infantry","Powell Heavy Infantries",#普威尔重步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_tab_shield_pavise_d, itm_bec_de_corbin_a, itm_ban_qingbiankui, itm_hongsejianyi_banlianjia, itm_mail_boots, itm_mail_mittens],
   str_21|agi_17|int_10|cha_10|level(30),wp_one_handed (145) | wp_two_handed (145) | wp_polearm (255) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_4|knows_prisoner_management_2|knows_leadership_5|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["powell_halberd_infantry","Powell Halberd Infantry","Powell Halberd Infantries",#普威尔戟兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_voulge, itm_hongyu_hue_qingbiankui, itm_hongse_zaoqi_banjia, itm_mail_boots, itm_fenzhi_dingshishoutao],
   str_28|agi_25|int_15|cha_17|level(43),wp_one_handed (145) | wp_two_handed (145) | wp_polearm (365) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_7|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["powell_halberd_cavalry","Powell Halberd Cavalry","Powell Halberd Cavalres",#普威尔戟骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_voulge, itm_hongyu_hue_qingbiankui, itm_coat_of_plates_red, itm_mail_boots, itm_mail_mittens, itm_hongheipijia_ma, itm_heise_ma],
   str_25|agi_22|int_14|cha_16|level(39),wp_one_handed (145) | wp_two_handed (145) | wp_polearm (315) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["powell_court_nobility","Powell Court Nobility","Powell Court Nobility",#普威尔宫廷贵族
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_red_noble_shirt, itm_leather_boots, itm_leather_gloves, itm_tab_shield_kite_cav_a, itm_tab_shield_heater_cav_a, itm_fighting_pick, itm_javelin, itm_javelin, itm_javelin],
   str_15 | agi_12 | int_9 | cha_10|level(15),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_2|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["powell_bodyguard","Powell Bodyguard","Powell Bodyguard",#普威尔近侍
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_bec_de_corbin_a, itm_pride_fan_shaped_shield, itm_powell_noble_hand_and_a_half_sword, itm_flat_topped_helmet, itm_shidun_lianjiazhaopao, itm_light_leather_boots, itm_scale_gauntlets, itm_saddle_horse, itm_throwing_spears, itm_throwing_spears, itm_throwing_spears],
   str_21 | agi_17 | int_15 | cha_12|level(28),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_5|knows_devout_3|knows_prisoner_management_5|knows_leadership_5|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["powell_court_knight","Powell Court Knight","Powell Court Knights",#普威尔内府骑士
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,
   0,0,fac_kingdom_1,
   [itm_yellow_lion_fan_shaped_shield, itm_powell_knight_sword, itm_qinxing_jixingkui1, itm_powell_plate, itm_plate_boots, itm_fangxing_bikai, itm_honghei_lianjia_pingyuanma, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao],
   str_29 | agi_25 | int_18 | cha_20|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_7|knows_devout_4|knows_prisoner_management_7|knows_leadership_8|knows_trade_4, 
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["powell_praetorian","Powell Praetorian","Powell Praetorian",#普威尔贵族禁卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_silver_dragon_fan_shaped_shield, itm_powell_lifeguard_plate, itm_changmain_hongyu_zhumiankui, itm_heise_banlianjiaxue, itm_heise_banlianjiaxue, itm_powell_noble_hand_and_a_half_sword, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_touguan_toumao, itm_powell_fan_shaped_shield],
   str_30 | agi_30 | int_18 | cha_24|level(45), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50), 
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_1|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_7|knows_devout_4|knows_prisoner_management_3|knows_leadership_7|knows_trade_1, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

#王冠骑士团
  ["crown_knight","Crown Knight","Crown Knights",#王冠骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_qishi_dingtouchui, itm_red_lion_iron_fan_shaped_shield, itm_dragon_blood_sorcery_lance, itm_changmain_hongyu_zhumiankui, itm_crown_knight_plate, itm_zhengshi_banjiaxue, itm_huali_shalouhushou, itm_powell_knight_warhorse],
   str_39 | agi_34 | int_25 | cha_30|level(55), wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_13|knows_shield_7|knows_athletics_8|knows_riding_11|knows_horse_archery_11|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_7|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_8|knows_devout_1|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
#国家骑士团
  ["king_spy","King Spy","King Spys",#普威尔密探
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_simple_recurve_bow, itm_wangguo_jian, itm_military_sickle_a, itm_jinshi_feidao, itm_professional_assassin_hood, itm_dingshi_fupi_duanlianjia, itm_black_greaves, itm_fenzhi_lianjiashoutao],
   str_18 | agi_23| int_17 | cha_11|level(30), wp_one_handed (300) | wp_two_handed (200) | wp_polearm (200) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_8|knows_riding_6|knows_horse_archery_6|knows_looting_7|knows_trainer_3|knows_tracking_9|knows_tactics_3|knows_pathfinding_9|knows_spotting_10|knows_inventory_management_3|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_6|knows_study_3|knows_devout_2|knows_prisoner_management_7|knows_leadership_2|knows_trade_8,
   man_face_young_1, man_face_young_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["national_knight","National Knight","National Knights",#国家骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_knight_recurve_bow, itm_wangguo_jian, itm_pride_fan_shaped_shield, itm_military_pick, itm_winged_great_helmet, itm_puweierguojiaqishi_jia, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_charger],
   str_26 | agi_25 | int_24 | cha_18|level(45), wp_one_handed (400) | wp_two_handed (300) | wp_polearm (300) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_6|knows_athletics_11|knows_riding_11|knows_horse_archery_12|knows_looting_10|knows_trainer_5|knows_tracking_12|knows_tactics_4|knows_pathfinding_12|knows_spotting_13|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_5|knows_persuasion_6|knows_array_arrangement_5|knows_memory_8|knows_study_4|knows_devout_2|knows_prisoner_management_10|knows_leadership_4|knows_trade_10,
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],

#戒钟禁卫队
  ["tocsin_attendant","Tocsin Atendant","Tocsin Atendants",#戒钟侍从
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_jinshi_feidao, itm_silver_dragon_fan_shaped_shield, itm_mogang_hushoujian, itm_flat_topped_helmet, itm_zhiyecike_jia, itm_iron_leather_greave, itm_fenzhi_lianjiashoutao],
   str_18 | agi_22| int_17 | cha_13|level(28), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_4|knows_horse_archery_6|knows_looting_3|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   man_face_young_1, man_face_young_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],
  ["tocsin_knight","Tocsin Knight","Tocsin Knights",#戒钟骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_graghite_steel_sabre, itm_heiyu_mogang_zhumiankui, itm_powell_knell_plate, itm_heise_banlianjiaxue, itm_heijin_banjaibikai, itm_heisebanjia_ma, itm_jinshi_zhanbiao, itm_jinshi_zhanbiao],
   str_45 | agi_50| int_37 | cha_45|level(53), wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),
   knows_ironflesh_12|knows_power_strike_13|knows_power_throw_11|knows_power_draw_8|knows_weapon_master_12|knows_shield_6|knows_athletics_11|knows_riding_8|knows_horse_archery_14|knows_looting_7|knows_trainer_5|knows_tracking_7|knows_tactics_5|knows_pathfinding_7|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_5|knows_persuasion_7|knows_array_arrangement_4|knows_memory_11|knows_study_8|knows_devout_6|knows_prisoner_management_7|knows_leadership_7|knows_trade_4,
   man_face_young_1, man_face_young_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],
  ["tocsin_assassin","Tocsin Assassin","Tocsin Assassins",#戒钟刺客
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_graghite_steel_sabre, itm_knell_assassin_hood, itm_powell_knell_plate, itm_heise_banlianjiaxue, itm_heijin_banjaibikai, itm_sizhong],
   str_60 | agi_70| int_45 | cha_40|level(61), wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_15|knows_power_throw_13|knows_power_draw_10|knows_weapon_master_15|knows_shield_8|knows_athletics_12|knows_riding_10|knows_horse_archery_15|knows_looting_10|knows_trainer_7|knows_tracking_10|knows_tactics_7|knows_pathfinding_10|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_8|knows_engineer_5|knows_persuasion_9|knows_array_arrangement_4|knows_memory_15|knows_study_10|knows_devout_6|knows_prisoner_management_9|knows_leadership_9|knows_trade_6,
   man_face_young_1, man_face_young_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#肃正之镰
  ["powell_headsman","Powell Headsman","Powell Headsmen",#普威尔刽子手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_blue_purple_triangular_shield, itm_military_cleaver_b, itm_gangpian_wumainkui, itm_hongkulou_lianjiashan, itm_splinted_leather_greaves, itm_leather_gloves],
   str_16|agi_12|int_8|cha_8|level(20),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_1|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_surgery_1|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_2|knows_study_1|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["powell_executioner","Powell Executioner","Powell Executioners",#普威尔行刑官
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_hongwen_qiqiang, itm_military_cleaver_c, itm_gorgeous_skoutarion, itm_two_handed_cleaver, itm_great_helmet, itm_zongse_lianxiongjia, itm_iron_greaves, itm_scale_gauntlets, itm_hongyipijia_ma],
   str_24|agi_22|int_16|cha_14|level(38),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_1|knows_trainer_4|knows_tracking_3|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_2|knows_prisoner_management_6|knows_leadership_6|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["eliminater_recruit","Eliminater Recruit","Eliminater Recruits",#肃正新兵
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_hunter_arrow, itm_steel_bow, itm_mogang_duanlian, itm_jiaoguo_sheshoukui, itm_baise_xiongjia, itm_iron_leather_boot, itm_scale_gauntlets],
   str_21|agi_18|int_12|cha_12|level(30),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),
   knows_ironflesh_6|knows_power_strike_7|knows_power_throw_2|knows_power_draw_5|knows_weapon_master_5|knows_shield_2|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_2|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_3|knows_devout_6|knows_prisoner_management_4|knows_leadership_3|knows_trade_1,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["eliminater_sergeant","Eliminater Sergeant","Eliminater Sergeants",#肃正军士
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_hunter_arrow, itm_dragon_hunting_bow, itm_mogang_duanlian, itm_gangshizi_niujiao_dakui, itm_baipao_banlian, itm_iron_greaves, itm_yuanzhi_bikai, itm_hongbaishipijia_ma, itm_black_and_white_skoutarion, itm_hongshizipijia_ma],
   str_30|agi_27|int_19|cha_19|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_9|knows_power_throw_3|knows_power_draw_7|knows_weapon_master_8|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_7|knows_looting_4|knows_trainer_3|knows_tracking_6|knows_tactics_6|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_8|knows_prisoner_management_5|knows_leadership_7|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["eliminater_vanguard","Eliminater Vanguard","Eliminater Vanguards",#肃正尖兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_great_scythe, itm_short_blade_great_scythe, itm_gangshizi_yi_dakui, itm_baipao_banlian, itm_iron_greaves, itm_yuanzhi_bikai],
   str_26|agi_24|int_16|cha_16|level(40),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_8|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_7|knows_shield_4|knows_athletics_4|knows_riding_6|knows_horse_archery_8|knows_looting_5|knows_trainer_4|knows_tracking_7|knows_tactics_6|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_6|knows_prisoner_management_4|knows_leadership_5|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["eliminater_knight","Eliminater Knight","Eliminater Knights",#肃正骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_sickle_of_eliminater, itm_gangshizi_yi_tongkui, itm_hongbai_jiazhong_banjia, itm_duangang_banjiaxue, itm_duangang_shalouhushou, itm_papal_plate_armor_mountain_horse],
   str_40|agi_32|int_24|cha_24|level(55),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),
   knows_ironflesh_10|knows_power_strike_11|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_4|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_7|knows_trainer_4|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_7|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_9|knows_prisoner_management_6|knows_leadership_7|knows_trade_1,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["purification_sickle","Purification Sickle","Purification Sickles",#净夜死镰
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_pretty_female,
   0,0,fac_kingdom_1,
   [itm_sickle_of_eliminater, itm_heise_banlianjiaxue, itm_mogang_shalouhushou, itm_night_eliminater_plate, itm_papal_chain_hood],
   str_44|agi_37|int_28|cha_28|level(58),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_4|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_7|knows_trainer_4|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_7|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_9|knows_prisoner_management_6|knows_leadership_7|knows_trade_1,
   0x00000000000010010000000000000e0000000000000000000000000000000000, 0x000000003f0020310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_assassin, #刺客
  ],


#————————————————————————————————罗德里格斯公国—————————————————————————————————
##
  ["red_dolphin_attendant","Red Dolphin Attendant","Red Dolphin Attendant",#红海豚侍从
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_iron_leather_greave, itm_leather_gloves, itm_dolphin_chest_armor, itm_tab_shield_pavise_c, itm_tab_shield_pavise_b, itm_baotie_toujin, itm_mail_coif, itm_helmet_with_neckguard, itm_leather_gloves, itm_spear, itm_war_spear],
   str_13 | agi_10 | int_9 | cha_9|level(19),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_1|knows_athletics_2|knows_riding_1|knows_horse_archery_3|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_2|knows_trade_1,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["red_dolphin_worrier","Red Dolphin Worrier","Red Dolphin Worrier",#红海豚卫士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_iron_leather_greave, itm_mail_chausses, itm_dolphin_chain_armor, itm_flat_topped_helmet, itm_ban_qingbiankui, itm_leather_gloves, itm_mail_mittens, itm_mail_mittens, itm_simple_blue_flower_fan_shaped_shield, itm_blue_flower_fan_shaped_shield, itm_sorcery_lance, itm_powell_noble_sword],
   str_18 | agi_13 | int_9 | cha_9|level(26),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_4|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_1|knows_prisoner_management_3|knows_leadership_4|knows_trade_2,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["red_dolphin_knight","Red Dolphin Knight","Red Dolphin Knight",#红海豚骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_sorcery_lance, itm_mail_chausses, itm_steel_leather_boot, itm_nailed_iron_leather_boot, itm_dolphin_mail_and_plate, itm_lanbai_pijia_liema, itm_languanpijia_ma, itm_yuanding_fangmiankui, itm_full_helm, itm_flat_topped_helmet, itm_mail_mittens, itm_fenzhi_fulianshoutao, itm_simple_blue_flower_fan_shaped_shield, itm_blue_flower_fan_shaped_shield, itm_powell_noble_sword, itm_powell_noble_hand_and_a_half_sword],
   str_23 | agi_18 | int_12 | cha_12|level(34),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_6|knows_horse_archery_7|knows_looting_2|knows_trainer_5|knows_tracking_1|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_2|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_1|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["red_dolphin_banneret","Red Dolphin Banneret","Red Dolphin Banneret",#红海豚方旗骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_nameless_goddess_silverwing_lance, itm_rodriguez_bucket_helmet, itm_dolphin_plate_chain_composite_armor, itm_mail_boots, itm_dolphin_chain_armor_plain_horse, itm_fenzhi_fubanshoutao, itm_duangang_shalouhushou, itm_blue_flower_fan_shaped_shield, itm_powell_knight_sword],
   str_31 | agi_26 | int_15 | cha_15|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_6|knows_tracking_2|knows_tactics_7|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_1|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["lesaff_armed_sailor","Lesaff Armed Sailor","Lesaff Armed Sailor",#勒塞夫武装水手
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_1,
   [itm_xihai_pixue, itm_hongse_dianchengjia, itm_leather_gloves, itm_hatchet, itm_hand_axe, itm_leather_warrior_cap, itm_light_throwing_axes, itm_wooden_shield],
   str_8 | agi_6 | int_9 | cha_9|level(7),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_looting_1|knows_spotting_1|knows_inventory_management_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_trade_1,
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["lesaff_shipboard_infantry","Lesaff Shipboard Infantry","Lesaff Shipboard Infantry",#勒塞夫船上步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_xihai_pixue, itm_wangguo_mingbin_mianjia, itm_fenzhi_pishoutao, itm_fighting_axe, itm_skullcap, itm_baotie_toujin, itm_leather_warrior_cap, itm_light_throwing_axes, itm_light_throwing_axes, itm_wooden_shield, itm_nordic_shield],
   str_13 | agi_9 | int_9 | cha_9|level(15),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (50) | wp_crossbow (50) | wp_throwing (90),
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_1|knows_shield_2|knows_athletics_3|knows_horse_archery_1|knows_looting_2|knows_trainer_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_2|knows_memory_3|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_trade_2,
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["lesaff_axe_warrior","Lesaff Axe Warrior","Lesaff Axe Warrior",#勒塞夫斧战士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_fenzhi_lianjiashoutao, itm_mail_chausses, itm_flat_topped_helmet, itm_segmented_helmet, itm_jianyi_qingxing_banlianjia, itm_qinliang_shuangshoufu, itm_light_throwing_axes, itm_light_throwing_axes, itm_light_throwing_axes, itm_nordic_shield, itm_nordic_shield],
   str_17 | agi_12 | int_9 | cha_9|level(25),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (130) | wp_archery (50) | wp_crossbow (50) | wp_throwing (130),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_6|knows_looting_4|knows_trainer_2|knows_tracking_2|knows_tactics_1|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_1|knows_trade_3,
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["lesaff_iron_axe_sergeant","Lesaff Iron Axe Sergeant","Lesaff Iron Axe Sergeant",#勒塞夫铁斧军士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_lingjia_pao, itm_flat_topped_helmet, itm_fenzhi_jiaqiangshoutao, itm_one_handed_battle_axe_b, itm_sarranid_axe_a, itm_jianyi_danshoufu, itm_light_throwing_axes, itm_light_throwing_axes, itm_tab_shield_round_d, itm_tab_shield_round_c, itm_tab_shield_round_e, itm_blue_breeze_round_shield, itm_steel_leather_boot, itm_splinted_greaves],
   str_25 | agi_18 | int_12 | cha_9|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (250) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_4|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_7|knows_looting_4|knows_trainer_4|knows_tracking_2|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["garcia_bodyguard","Garcia Bodyguard","Garcia Bodyguard",#加西亚亲卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_devil_rider_hood, itm_fenzhi_lianjiashoutao, itm_dark_apprentice_robe, itm_fenzhi_pishoutao, itm_xihai_pixue, itm_gauntlets, itm_cruel_morningstar_hammer, itm_steel_shield],
   str_40 | agi_29 | int_20 | cha_3|level(37),wp_one_handed (370) | wp_two_handed (370) | wp_polearm (370) | wp_archery (370) | wp_crossbow (370) | wp_throwing (370),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_7|knows_shield_7|knows_athletics_7|knows_riding_7|knows_horse_archery_7|knows_looting_5|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_5|knows_array_arrangement_5|knows_memory_7|knows_study_7|knows_devout_7|knows_prisoner_management_7|knows_leadership_7|knows_trade_5,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["faceless_cavalry","Faceless Cavalry","Faceless Cavalry",#无面骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_heisebanjia_ma, itm_heiguang_bikai, itm_black_greaves, itm_heijin_qishikui, itm_black_armor, itm_dingci_lengtouchui, itm_heise_banlianjiaxue, itm_demon_fan_shaped_shield, itm_gangying_qishiqiang],
   str_50 | agi_43 | int_30 | cha_3|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_14|knows_power_draw_14|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_9|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_7|knows_tactics_7|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_7|knows_array_arrangement_7|knows_memory_12|knows_study_12|knows_devout_12|knows_prisoner_management_9|knows_leadership_9|knows_trade_7,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#戈兰尼尔民兵自卫军
  ["grenier_militia","Grenier Militia","Grenier Militias",#戈兰尼尔民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_jianyi_peizhongjian, itm_tab_shield_pavise_a, itm_hood_d, itm_blue_gambeson, itm_blue_hose, itm_blue_tunic, itm_ankle_boots, itm_sword_medieval_c_small, itm_sword_medieval_a, itm_arming_cap, itm_quarter_staff, itm_staff, itm_stones, itm_throwing_knives, itm_pitch_fork, itm_boar_spear, itm_kuotou_qiang, itm_simple_long_bow, itm_practice_arrows_2, itm_arrows],
   str_9 | agi_7 | int_6 | cha_6|level(8),wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (55) | wp_crossbow (55) | wp_throwing (55),
   knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_trade_1,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["grenier_wellselected_militia","Grenier Wellselected Militia","Grenier Wellselected Militias",#戈兰尼尔精选民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_helmet_with_neckguard, itm_lanse_xiongjia, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet, itm_mail_coif, itm_fenzhi_pishoutao, itm_ashwood_pike, itm_shortened_spear, itm_citou_qiang, itm_blue_gambeson, itm_jiushi_yuandingkui, itm_splinted_leather_greaves, itm_tab_shield_pavise_b, itm_tab_shield_pavise_c, itm_long_bow, itm_simple_long_bow, itm_barbed_arrows, itm_arrows, itm_bodkin_arrows, itm_blue_gambeson],
   str_15 | agi_12 | int_9 | cha_8|level(20),wp_one_handed (175) | wp_two_handed (175) | wp_polearm (175) | wp_archery (175) | wp_crossbow (175) | wp_throwing (175),
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_1|knows_horse_archery_2|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_surgery_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["grenier_rider","Grenier Rider","Grenier Riders",#戈兰尼尔骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_simple_blue_flower_fan_shaped_shield, itm_lanwen_qiqiang, itm_qinse_danshoujian, itm_yuanding_lianjiakui, itm_dolphin_chain_armor, itm_iron_leather_greave, itm_mail_mittens, itm_languanpijia_ma, itm_blue_flower_fan_shaped_shield, itm_sword_medieval_d_long],
   str_21 | agi_15 | int_10 | cha_9|level(31),wp_one_handed (245) | wp_two_handed (245) | wp_polearm (245) | wp_archery (245) | wp_crossbow (245) | wp_throwing (245),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_4|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["grenier_longbow_archer","Grenier Longbow Archer","Grenier Longbow Archers",#戈兰尼尔长弓手
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_wangguo_jian, itm_simple_blue_flower_fan_shaped_shield, itm_awlpike_long, itm_war_bow, itm_yuanding_lianjiakui, itm_dolphin_chain_armor, itm_iron_leather_greave, itm_mail_mittens, itm_blue_flower_fan_shaped_shield, itm_changren_qiang],
   str_21 | agi_15 | int_10 | cha_9|level(32),wp_one_handed (245) | wp_two_handed (245) | wp_polearm (245) | wp_archery (245) | wp_crossbow (245) | wp_throwing (245),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_5|knows_weapon_master_5|knows_shield_4|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["grenier_chivalric_knight","Grenier Chivalric Knight","Grenier Chivalric Knights",#戈兰尼尔侠义骑士
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_qishi_danshouzhanfu, itm_blue_flower_skoutarion, itm_rodriguez_bucket_helmet, itm_lanse_zaoqi_banjia, itm_mail_boots, itm_gauntlets, itm_jinhuapijia_ma, itm_wangguo_lierenjian, itm_archer_longbow],
   str_30 | agi_26 | int_17 | cha_18|level(46),wp_one_handed (425) | wp_two_handed (425) | wp_polearm (425) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_7|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_7|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_7|knows_trade_5,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

#罗德里格斯盾卫队
  ["trade-wind_gulf_guard","Trade-wind Gulf Guard","Trade-wind Gulf Guard",#信风湾守卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_mogang_changzhuiqiang, itm_tab_shield_pavise_d, itm_lianjia_quanfu_guokui, itm_duanxiu_lianjiapao, itm_leather_boots, itm_leather_gloves],
   str_16 | agi_12 | int_10 | cha_10|level(20),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),
   knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_5|knows_athletics_2|knows_horse_archery_3|knows_trainer_2|knows_inventory_management_2|knows_surgery_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_5|knows_prisoner_management_1|knows_leadership_2,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["holding_guard","Holding Guard","Holding Guard",#扼守之盾
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_mogang_zhuixingqiang, itm_tab_shield_round_e, itm_xihai_wenshikui, itm_lanse_lianjiazhaopao, itm_mail_chausses, itm_scale_gauntlets],
   str_27 | agi_20 | int_12 | cha_13|level(40),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (340) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_10|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_10|knows_athletics_4|knows_riding_2|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_7|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

#元素骑士团
  ["elemental_knight","Elemental Knight","Elemental Knights",#元素骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_blood_sorcery_lance, itm_shield_heater_of_element, itm_changmian_lanyu_jianzuikui, itm_element_plate_chain_composite_armor, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_dolphin_chain_armor_plain_horse],
   str_35 | agi_28 | int_21 | cha_19|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_9|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["elemental_ranger","Elemental Ranger","Elemental Rangers",#元素游侠
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_shield_heater_of_element, itm_dragon_blood_sorcery_lance, itm_changmian_lanyu_jianzuikui, itm_elemental_ranger_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai],
   str_33 | agi_30 | int_21 | cha_24|level(48),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_2|knows_trainer_7|knows_tracking_2|knows_tactics_6|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_8|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_3, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["elemental_attendant","Elemental Attendant","Elemental Attendants",#元素侍从
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_powell_noble_sword, itm_shield_heater_of_element, itm_sorcery_lance, itm_yuanding_lianjiakui, itm_dolphin_chain_armor, itm_steel_leather_boot, itm_fenzhi_dingshishoutao],
   str_24 | agi_20 | int_15 | cha_15|level(35),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_6|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_1|knows_prisoner_management_3|knows_leadership_4|knows_trade_2,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
#血火佣兵团
  ["bloodfire_mercenary_corps_veteran","Bloodfire Mercenary Corps Veteran","Bloodfire Mercenary Corps Veteran",#血火佣兵团老手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_one_handed_battle_axe_b, itm_shield_heater_of_element, itm_fighting_axe, itm_one_handed_war_axe_a, itm_ban_guokui, itm_red_gambeson, itm_splinted_leather_greaves, itm_leather_gloves, itm_axe, itm_voulge, itm_light_throwing_axes, itm_sumpter_horse, itm_saddle_horse],
   str_17 | agi_12 | int_9 | cha_9|level(25),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_3|knows_tactics_1|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_2|knows_trade_4,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["bloodfire_vanguard","Bloodfire Vanguard","Bloodfire Vanguard",#血火先锋
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_shield_heater_of_element, itm_jianyi_shuangshoufu, itm_two_handed_axe, itm_guyongbing_tiekui, itm_hongkulou_lianjiashan, itm_mail_chausses, itm_fenzhi_fulianshoutao, itm_shenseliema, itm_throwing_axes, itm_light_lance, itm_double_sided_lance, itm_lance, itm_throwing_axes],
   str_25 | agi_22 | int_13 | cha_12|level(38),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_6|knows_shield_5|knows_athletics_8|knows_riding_6|knows_horse_archery_7|knows_looting_4|knows_trainer_5|knows_tracking_3|knows_tactics_7|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_2|knows_devout_1|knows_prisoner_management_5|knows_leadership_7|knows_trade_5,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["bloodfire_berserker_warrior","Bloodfire Berserker Warrior","Bloodfire Berserker Warrior",#血火狂战勇士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_war_axe, itm_guyongbing_zhongkui, itm_hongkulou_lianjiashan, itm_mail_chausses, itm_gauntlets],
   str_30 | agi_20 | int_17 | cha_16|level(40),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_7|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_2|knows_devout_1|knows_prisoner_management_5|knows_leadership_7|knows_trade_5,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],


#————————————————————————————————北境开拓领—————————————————————————————————
##
  ["northern_militia","Northern Militia","Northern Militia", #北境民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_plate_covered_round_shield, itm_arming_cap, itm_wangguo_mingbin_mianjia, itm_wrapping_boots, itm_skullcap, itm_zonghong_mianjia, itm_zonghong_diancheng_jia, itm_leather_warrior_cap, itm_hunter_boots, itm_boar_spear, itm_battle_fork, itm_kuotou_qiang, itm_jiachang_kuotou_qiang, itm_padded_leather, itm_red_gambeson],
   str_10|agi_8|int_8|cha_7|level(13),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (90) | wp_throwing (90), 
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_2|knows_riding_1|knows_tracking_1|knows_tactics_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_devout_1|knows_leadership_1|knows_trade_1, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["northern_infantry","Northern Infantry","Northern Infantry", #北境步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_military_pick, itm_bec_de_corbin_a, itm_steel_shield, itm_tab_shield_pavise_d, itm_wozhuangkui, itm_quanshen_lianjai, itm_mail_chausses, itm_mail_mittens, itm_duanxiu_lianjiapao, itm_mail_hauberk, itm_zhanshi_chu, itm_tab_shield_kite_cav_b],
   str_17|agi_14|int_11|cha_10|level(25),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200), 
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_1, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["northern_tower_shield_sergeant","Northern Tower Shield Sergeant","Northern Tower Shield Sergeants", #北境塔盾军士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_mogang_changzhuiqiang, itm_qishi_chu, itm_heavy_mattock, itm_papal_soldier_tower_shield, itm_chaozhongkui, itm_baimian_banlianjia, itm_steel_leather_boot, itm_leather_gloves],
   str_24|agi_20|int_14|cha_13|level(37),wp_one_handed (310) | wp_two_handed (310) | wp_polearm (310) | wp_archery (310) | wp_crossbow (310) | wp_throwing (310), 
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_7|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_2|knows_leadership_5|knows_trade_3, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["northern_cavalry","Northern Cavalry","Northern Cavalry", #北境枪骑兵
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,
   no_scene,reserved,fac_kingdom_1,
   [itm_ellite_lance, itm_qishi_chu, itm_heavy_mattock, itm_steel_shield, itm_chaozhongkui, itm_baimian_banlianjia, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_huise_ma],
   str_27|agi_23|int_15|cha_14|level(40),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360), 
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_5|knows_athletics_4|knows_riding_6|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_3|knows_devout_4|knows_prisoner_management_3|knows_leadership_5|knows_trade_2, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["northern_crossbowman","Northern Crossbowman","Northern Crossbowman", #北境弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   no_scene,reserved,fac_kingdom_1,
   [itm_crossbow, itm_bolts, itm_steel_bolts, itm_military_pick, itm_bec_de_corbin_a, itm_steel_shield, itm_tab_shield_pavise_d, itm_wozhuangkui, itm_quanshen_lianjai, itm_mail_chausses, itm_mail_mittens, itm_duanxiu_lianjiapao, itm_mail_hauberk, itm_zhanshi_chu, itm_tab_shield_kite_cav_b, ],
   str_16|agi_15|int_11|cha_20|level(25),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200), 
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_1, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["northern_heavy_crossbow_shooter","Northern Heavy Crossbow Shooter","Northern Heavy Crossbow Shooter", #北境强弩攻坚手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   no_scene,reserved,fac_kingdom_1,
   [itm_heavy_crossbow, itm_qishi_chu, itm_steel_bolts, itm_steel_shield, itm_bascinet_3, itm_quanshen_lianjai, itm_mail_chausses, itm_mail_mittens],
   str_23|agi_21|int_14|cha_13|level(37),wp_one_handed (310) | wp_two_handed (310) | wp_polearm (310) | wp_archery (310) | wp_crossbow (310) | wp_throwing (310), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_2|knows_leadership_5|knows_trade_3, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["northern_serf","Northern Serf","Northern Serf", #北境农奴
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_wooden_board_shield, itm_fighting_pick, itm_felt_hat, itm_burlap_tunic, itm_wrapping_boots, itm_coarse_tunic, itm_linen_tunic, itm_shirt, itm_head_wrappings, itm_headcloth, itm_straw_hat, itm_pitch_fork, itm_battle_fork, itm_boar_spear, itm_hunter_boots], 
   str_9|agi_9|int_7|cha_5|level(8),wp(70),
   knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_1|knows_inventory_management_1|knows_wound_treatment_1|knows_first_aid_1|knows_devout_3,
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["northern_serf_infantry","Northern Serf Infantry","Northern Serf Infantry", #北境农奴步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_simple_red_dragon_skoutarion, itm_mail_coif, itm_light_leather, itm_light_leather_boots, itm_leather_gloves, itm_hide_boots, itm_hunter_boots, itm_wooden_board_shield, itm_long_spiked_club, itm_flat_head_axe, itm_poleaxe, itm_tab_shield_pavise_a, itm_leather_jerkin, itm_maopipijia_pijia, itm_tab_shield_pavise_b, itm_military_pick, itm_military_sickle_a, itm_skullcap, itm_leather_warrior_cap, itm_baotie_toujin, itm_footman_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_long_hafted_spiked_mace],
    str_16|agi_13|int_6|cha_5|level(20),wp_one_handed (190) | wp_two_handed (190) | wp_polearm (190) | wp_archery (190) | wp_crossbow (190) | wp_throwing (190), 
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_3|knows_shield_1|knows_athletics_2|knows_riding_1|knows_horse_archery_3|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_2, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["northern_serf_rider","Northern Serf Rider","Northern Serf Rider", #北境农奴骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_flat_head_axe, itm_bascinet_2, itm_quanshen_lianjai, itm_splinted_greaves, itm_fenzhi_dingshishoutao, itm_heise_ma, itm_hongse_xiongjia, itm_leather_armor, itm_black_white_fan_shaped_shield, itm_linjiapijian_dingshijia, itm_dingshi_fupi_duanlianjia, itm_mail_hauberk, itm_duanxiu_lianjiapao, itm_tab_shield_heater_b, itm_tab_shield_heater_a, itm_tab_shield_heater_d, itm_tab_shield_heater_cav_a, itm_tab_shield_heater_c, itm_military_pick, itm_zhanshi_chu, itm_qishi_danshouzhanfu, itm_bastard_sword_b, itm_military_cleaver_c, itm_zhanshi_chui, itm_military_hammer, itm_sarranid_axe_b, itm_one_handed_battle_axe_c, itm_fenzhi_fulianshoutao, itm_mail_coif, itm_guard_helmet, itm_bascinet_3, itm_mail_mittens, itm_mail_chausses, itm_iron_leather_boot, itm_steel_leather_boot, itm_shenseliema, itm_zase_ma],
    str_27|agi_22|int_13|cha_12|level(34),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_4|knows_prisoner_management_3|knows_leadership_5|knows_trade_2, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["northern_ministeriales","Northern Ministeriales","Northern Ministeriales", #北境农奴骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_great_lance, itm_qishi_dingtouchui, itm_silver_dragon_fan_shaped_shield, itm_qishi_zhongfu, itm_gangshizi_jukui, itm_powell_patron_plate, itm_iron_greaves, itm_gauntlets, itm_pitie_liema],
    str_30|agi_29|int_19|cha_18|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (440) | wp_crossbow (440) | wp_throwing (440), 
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_5|knows_athletics_5|knows_riding_6|knows_horse_archery_7|knows_looting_1|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_3, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#龙血骑士团
  ["dragonblood_knight","Dragonblood Knight","Dragonblood Knights", #龙血骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_qishi_dingtouchui, itm_dragon_god_black_shield, itm_mogang_zhuixingqiang, itm_hongyu_zhumiankui, itm_dragonblood_knight_plate, itm_duangang_banjiaxue, itm_mogang_shalouhushou, itm_hongbanjia_longxuama],
   str_43 | agi_34 | int_20 | cha_19|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_2|knows_prisoner_management_6|knows_leadership_8|knows_trade_2, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["northern_hunter","Northern Hunter","Northern Hunter", #北境猎人
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged, 
   no_scene,reserved,fac_kingdom_1,
   [itm_military_sickle_a, itm_fighting_pick, itm_short_bow, itm_wangguo_jian, itm_helmet_with_neckguard, itm_leather_jerkin, itm_hunter_boots, itm_leather_gloves, itm_red_gambeson, itm_segmented_helmet, itm_footman_helmet, itm_splinted_leather_greaves, itm_hide_boots, itm_nomad_boots, itm_hammer, itm_sarranid_mace_1, itm_wangguo_jian, itm_wangguo_jian, itm_wangguo_jian],
    str_14|agi_11|int_12|cha_9|level(17),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150), 
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_2|knows_shield_1|knows_athletics_4|knows_horse_archery_4|knows_looting_1|knows_tracking_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_devout_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1, 
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["dragon_scout","Dragon Scout","Dragon Scout", #寻龙猎手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged, 
   no_scene,reserved,fac_kingdom_1,
   [itm_wangguo_lierenjian, itm_wangguo_lierenjian, itm_dragon_hunter_arrow, itm_wangguo_sheshoulianjia, itm_strengthen_archer_longbow, itm_leather_gloves, itm_splinted_leather_greaves, itm_flat_topped_helmet, itm_military_pick],
   str_20 | agi_22 | int_17 | cha_13|level(30),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (150) | wp_archery (280) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_6|knows_tactics_4|knows_pathfinding_5|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_3|knows_devout_4|knows_prisoner_management_2|knows_leadership_4|knows_trade_3, 
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["powell_dragon_archer","Powell Dragon Archer","Powell Dragon Archer", #普威尔猎龙射手
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_heavy_mattock, itm_dragon_hunting_bow, itm_fuhe_guokui, itm_puweier_lianjia, itm_mail_chausses, itm_fenzhi_dingshishoutao, itm_dragon_hunter_arrow, itm_dragon_hunter_arrow, itm_dragon_hunter_arrow, itm_dragon_hunter_arrow],
   str_27 | agi_28 | int_23 | cha_18|level(43),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (250) | wp_archery (400) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_8|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_4|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_3|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

#无乡骑士团
  ["revenge_iron_hoof","Revenge Iron Hoof","Revenge Iron Hoof", #复仇铁骑
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,
   no_scene,reserved,fac_kingdom_1,
   [itm_heavy_mattock, itm_voulge, itm_throwing_spears, itm_throwing_spears, itm_jiaqiang_qingbiankui, itm_zongselianjia_shan, itm_nailed_iron_leather_boot, itm_scale_gauntlets, itm_zase_ma, itm_great_lance, itm_long_bardiche, itm_heavy_lance, itm_huise_ma, itm_shenseliema],
   str_20|agi_14|int_13|cha_13|level(27),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_1,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["hometownless_knight","Hometownless Knight","Hometownless Knight", #无乡骑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
    no_scene,reserved,fac_kingdom_1,
   [itm_heavy_mattock, itm_qishi_zhongfu, itm_throwing_spears, itm_touguan_toumao, itm_mercenary_knight_helmet, itm_jiaqianglengshi_jia, itm_shengtie_banjiaxue, itm_gauntlets, itm_jarid, itm_throwing_spears, itm_jarid],
   str_33|agi_26|int_21|cha_18|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_8|knows_shield_4|knows_athletics_8|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_7|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_3|knows_prisoner_management_4|knows_leadership_7|knows_trade_3,
   powell_face_old_1, powell_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#龙狱
  ["brand_dragonmania","Brand Dragonmania","Brand Dragonmanias",#烙印龙癫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_slavers,
   [itm_dragon_abomination_body, itm_dragon_abomination_leg, itm_dragon_abomination_hand, itm_chains_full],
   str_45 | agi_41 | int_32 | cha_16|level(30), wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_8|knows_riding_1|knows_horse_archery_3|knows_looting_7|knows_trainer_2|knows_tracking_6|knows_tactics_4|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_9|knows_study_15|knows_devout_2|knows_prisoner_management_2|knows_leadership_8|knows_trade_1, 
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_monster, #敌意存在
  ],
  ["brand_dragonfrenzy","Brand Dragonfrenzy","Brand Dragonfrenzies",#烙印龙狂
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_slavers,
   [itm_dragon_abomination_body_with_armor, itm_dragon_abomination_leg, itm_dragon_abomination_hand, itm_chains_full],
   str_62 | agi_58 | int_44 | cha_23|level(40), wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_4|knows_shield_3|knows_athletics_11|knows_riding_3|knows_horse_archery_5|knows_looting_9|knows_trainer_3|knows_tracking_8|knows_tactics_6|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_2|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_12|knows_study_15|knows_devout_3|knows_prisoner_management_4|knows_leadership_10|knows_trade_2, 
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_monster, #敌意存在
  ],
  ["brand_dragon_abomination","Brand Dragon Abomination","Brand Dragon Abominations",#烙印龙孽
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_slavers,
   [itm_dragon_abomination_heavy_armor, itm_dragon_abomination_leg, itm_dragon_abomination_gauntlet, itm_chains_full],
   str_80 | agi_75 | int_55 | cha_29|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_10|knows_power_draw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_13|knows_riding_4|knows_horse_archery_7|knows_looting_10|knows_trainer_4|knows_tracking_10|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_3|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_4|knows_memory_14|knows_study_15|knows_devout_4|knows_prisoner_management_5|knows_leadership_12|knows_trade_3, 
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_monster, #敌意存在
  ],

  ["extinction_tornado","Extinction Tornado","Extinction Tornado",#灭绝龙卷
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_pretty_female,
   0,0,fac_slavers,
   [itm_dragon_abomination_heavy_armor_with_wing, itm_dragon_abomination_leg, itm_dragon_abomination_gauntlet, itm_chains_full],
   str_110 | agi_102 | int_78 | cha_45|level(60), wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_13|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_15|knows_riding_6|knows_horse_archery_8|knows_looting_10|knows_trainer_5|knows_tracking_10|knows_tactics_9|knows_pathfinding_10|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_10|knows_array_arrangement_5|knows_memory_15|knows_study_15|knows_devout_5|knows_prisoner_management_8|knows_leadership_15|knows_trade_4, 
   0x00000000000010010000000000000e0000000000000000000000000000000000, 0x000000003f0020310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_monster, #敌意存在
  ],



#————————————————————————————————普属自由城邦—————————————————————————————————
##
  ["preist_porter","Preist Porter","Preist Porters", #奉神城门卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   no_scene,reserved,fac_kingdom_1,
   [itm_tab_shield_pavise_b, itm_boar_spear, itm_baotie_toujin, itm_yellow_tunic, itm_woolen_hose],
    str_10|agi_9|int_8|cha_8|level(15), wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (90) | wp_throwing (90),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_1|knows_shield_3|knows_athletics_1|knows_riding_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_1|knows_memory_3|knows_study_2|knows_devout_4|knows_leadership_1|knows_trade_1,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["preist_infantry","Preist Infantry","Preist Infantries", #奉神城步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   no_scene,reserved,fac_kingdom_1,
   [itm_tab_shield_pavise_d, itm_jianyi_jiantiqiang, itm_flat_topped_helmet, itm_huanghei_xiongjia, itm_splinted_leather_greaves, itm_leather_gloves],
    str_17|agi_14|int_9|cha_8|level(28),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_3|knows_devout_5|knows_prisoner_management_1|knows_leadership_3|knows_trade_1,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["preist_horseback_crossbow_sergeant","Preist Horseback Crossbow Sergeant","Preist Horseback Crossbow Sergeant", #奉神城骑弩军士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   no_scene,reserved,fac_kingdom_1,
   [itm_hunting_crossbow, itm_preist_fan_shaped_shield, itm_bolts, itm_honghuang_wenqiqiang, itm_huangyu_lianjia_qingbiankui, itm_lianghuang_lianjiazhaopao, itm_mail_chausses, itm_scale_gauntlets, itm_huangyipijia_ma],
    str_24|agi_19|int_13|cha_12|level(40),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_8|knows_athletics_4|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_8|knows_study_3|knows_devout_7|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["preist_noble_crossbowman","Preist Noble Crossbowman","Preist Noble Crossbowmen", #奉神城贵胄弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   no_scene,reserved,fac_kingdom_1,
   [itm_oak_corssbow, itm_jiantou_qiang1, itm_bolts, itm_ban_qingbiankui, itm_mail_with_tunic_yellow, itm_iron_leather_boot, itm_mail_mittens, itm_yellow_black_fan_shaped_shield],
    str_16|agi_14|int_12|cha_12|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_6|knows_athletics_4|knows_riding_3|knows_horse_archery_6|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_5|knows_prisoner_management_1|knows_leadership_3|knows_trade_1,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["preist_noble_cavalry","Preist Noble Cavalry","Preist Noble Cavalries", #奉神城贵胄骑兵
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,
   no_scene,reserved,fac_kingdom_1,
   [itm_birch_crossbow, itm_sorcery_lance, itm_steel_bolts, itm_state_great_helmet, itm_honghuangcheng_banlian, itm_wenli_banjiaxue, itm_yinse_bikai, itm_jinjiu_lianjia_pingyuanma, itm_strengthen_yellow_black_fan_shaped_shield],
    str_25|agi_20|int_15|cha_15|level(41),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_9|knows_athletics_4|knows_riding_6|knows_horse_archery_8|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_8|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_7|knows_trade_3,
   powell_face_young_1, powell_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],


#奉神骑士团
  ["preist_knight","Preist Knight","Preist Knights",#奉神骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_guizu_qinnu, itm_jinseshoubanjian, itm_baiyu_nushi, itm_duangang_yuanti_qishikui, itm_powell_priest_plate_high, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_iron_knight_warhorse, itm_sorcery_lance, itm_honeysuckle_fan_shaped_shield],
   str_31 | agi_30 | int_20 | cha_24|level(47),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_9|knows_looting_2|knows_trainer_5|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_7|knows_devout_11|knows_prisoner_management_4|knows_leadership_9|knows_trade_3,
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["preist_attendant","Preist Attendant","Elemental Attendants",#奉神侍从
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_buqiang_jiantiqiang, itm_jinshi_cejian, itm_black_yellow_skoutarion, itm_fuhe_guokui, itm_priest_chain_armor, itm_mail_chausses, itm_fenzhi_dingshishoutao, itm_zase_ma],
   str_24 | agi_20 | int_15 | cha_15|level(35),wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (290) | wp_crossbow (290) | wp_throwing (290),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_6|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_4|knows_devout_8|knows_prisoner_management_3|knows_leadership_4|knows_trade_2,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],


#普威尔正教会
  ["powell_novice_divineguider","Powell Novice Divineguider","Powell Novice Divineguiders",#普威尔新手神术使
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_tab_shield_pavise_c, itm_jinshi_bishou, itm_boar_spear, itm_gambeson, itm_ankle_boots, itm_leather_gloves],
   str_8 | agi_8 | int_7 | cha_7|level(10),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_1|knows_power_strike_1|knows_shield_1|knows_horse_archery_1|knows_persuasion_3|knows_memory_4|knows_study_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["powell_conscripted_therapist","Powell Conscripted Therapist","Powell Conscripted Therapists",#普威尔治疗师
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_tab_shield_pavise_d, itm_jinse_minwenjian, itm_baotie_toujin, itm_splinted_leather_greaves, itm_leather_gloves, itm_light_crossbow, itm_bolts, itm_traveling_friar_cloth],
   str_15 | agi_12 | int_12 | cha_10|level(25),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_6|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_2|knows_trainer_1|knows_tracking_1|knows_tactics_3|knows_pathfinding_2|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_8|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_1,
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["powell_military_divineguider","Powell Military Divineguider","Powell Military Divineguiders",#普威尔军事神术使
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_jiantou_qiang1, itm_tab_shield_pavise_d, itm_jinse_changjian, itm_jianyia_jixingkui, itm_puweierzhanjiao_jia, itm_mail_chausses, itm_mail_mittens],
   str_20 | agi_15 | int_14 | cha_12|level(30),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_6|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_2|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_6|knows_prisoner_management_2|knows_leadership_4|knows_trade_2,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["powell_armour_divineguider","Powell Armour Divineguider","Powell Armour Divineguider",#普威尔圣军士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_papal_soldier_tower_shield, itm_jinshi_fanhuajian, itm_jinshi_shuangshou, itm_gangshizi_niujiao_dakui2, itm_baipao_banlian, itm_mail_boots, itm_gauntlets],
   str_26 | agi_19 | int_19 | cha_14|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_5|knows_devout_10|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["powell_orthodox_believer","Powell Orthodox Believer","Powell Orthodox Believers",#普威尔正教信徒
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_hammer, itm_simple_papal_fan_shaped_shield, itm_white_tunic, itm_woolen_hose],
   str_9 | agi_9 | int_5 | cha_7|level(10),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_riding_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_devout_6,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["powell_parishioner_warrier","Powell Parishioner Warrier","Powell Parishioner Warriers",#普威尔教友战士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_golden_red_round_shield, itm_military_hammer, itm_papal_believer_hood, itm_gambeson, itm_splinted_leather_greaves, itm_leather_gloves],
   str_16 | agi_12 | int_5 | cha_7|level(20),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_4|knows_shield_5|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_surgery_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_8|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_orthodox_zealot","Powell Orthodox Zealot","Powell Orthodox Zealots",#普威尔正教狂信徒
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_golden_red_round_shield, itm_jinshi_tuntouzhang, itm_papal_believer_chain_hood, itm_papal_chest_armor, itm_iron_leather_boot, itm_mail_mittens],
   str_25 | agi_20 | int_5 | cha_7|level(35),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_8|knows_athletics_6|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_5|knows_devout_12|knows_prisoner_management_3|knows_leadership_5|knows_trade_2,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["divine_swordsworn_cavalry","Divine Swordsworn Cavalry","Divine Swordsworn Cavalries",#奉剑圣骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_noble_ornamentation_lance, itm_jinseshoubanjian, itm_baiyu_yuantikui, itm_powell_priest_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_papal_chain_armor_mountain_horse, itm_sire_bond_noble_shield],
   str_34 | agi_22 | int_9 | cha_16|level(50),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_11|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_13|knows_prisoner_management_6|knows_leadership_8|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],


#—————————————————————————————————南沙公国—————————————————————————————————
##
  ["powell_rogue_farmer","Powell Rogue Farmer","Powell Rogue Farmer",#普威尔无赖农民
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_1,
   [itm_cleaver, itm_knife, itm_pitch_fork, itm_sickle, itm_club, itm_stones, itm_leather_cap, itm_felt_hat, itm_felt_hat, itm_linen_tunic, itm_coarse_tunic, itm_nomad_boots, itm_wrapping_boots], 
   str_8|agi_7|int_6|cha_5|level(6),wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_athletics_1|knows_horse_archery_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["sousanth_militia","Sousanth Militia","Sousanth Militia",#南沙民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_wangguo_jian, itm_tab_shield_heater_a, itm_nanfang_jichangmao, itm_hunting_bow, itm_segmented_helmet, itm_skirmisher_armor, itm_sarranid_boots_b, itm_leather_gloves, itm_jianliang_jian, itm_nanfang_cijian, itm_tab_shield_heater_b, itm_archers_vest, itm_mail_coif, itm_helmet_with_neckguard, itm_darts],
   str_14 | agi_11 | int_8 | cha_6|level(17),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_1|knows_athletics_3|knows_riding_1|knows_horse_archery_3|knows_looting_2|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_persuasion_1|knows_memory_1|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_1,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["sousanth_guard","Sousanth Guard","Sousanth Guards",#南沙城卫队
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_tab_shield_heater_d, itm_nanfang_jichangmao, itm_military_cleaver_b, itm_flat_topped_helmet, itm_sarranid_leather_armor, itm_mail_chausses, itm_leather_gloves, itm_sarranid_leather_armor, itm_sarranid_cavalry_robe, itm_fenzhi_jiaqiangshoutao, itm_nanfang_cijian, itm_tab_shield_heater_c, itm_archers_vest, itm_short_bow, itm_nanfang_jian, itm_darts, itm_darts],
   str_18 | agi_15 | int_10 | cha_9|level(29),wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_3|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["sousanth_elite_bowman","Sousanth Elite Bowman","Sousanth Elite Bowmen",#南沙精锐射手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_strong_bow, itm_awlpike, itm_powell_red_round_shield, itm_nanfang_cijian, itm_kettle_hat, itm_sarranid_elite_armor, itm_steel_leather_boot, itm_lamellar_gauntlets, itm_nanfang_jian],
   str_24 | agi_23 | int_13 | cha_12|level(39),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (360) | wp_archery (360) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_7|knows_weapon_master_7|knows_shield_4|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_3|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["sousanth_darts_sergeant","Sousanth Darts Sergeant","Sousanth Darts Sergeant",#南沙战镖军士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_nanfang_cijian, itm_pride_fan_shaped_shield, itm_war_darts, itm_war_darts, itm_hongyu_hue_qingbiankui, itm_khergit_elite_armor, itm_splinted_greaves, itm_mail_mittens, itm_sword_two_handed_a, itm_bastard_sword_a, itm_sword_two_handed_b, itm_bastard_sword_b],
   str_26 | agi_22 | int_15 | cha_14|level(40),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (360),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_7|knows_power_draw_5|knows_weapon_master_7|knows_shield_4|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_1|knows_prisoner_management_3|knows_leadership_7|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["sousanth_rider","Sousanth Rider","Sousanth Riders",#南沙骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_double_sided_lance, itm_great_lance, itm_military_cleaver_c, itm_jiaqiang_guokui2, itm_archers_vest, itm_splinted_greaves, itm_mail_mittens, itm_arabian_horse_a, itm_steppe_horse],
   str_18 | agi_15 | int_10 | cha_9|level(30),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_3|knows_riding_4|knows_horse_archery_5|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_3|knows_devout_2|knows_prisoner_management_1|knows_leadership_4|knows_trade_2,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["powell_rogue_attendant","Powell Rogue Attendant","Powell Rogue Attendants",#普威尔无赖扈从
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_flat_topped_helmet, itm_mail_with_tunic_red, itm_mail_chausses, itm_tab_shield_heater_a, itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a, itm_shicong_lianjiapao, itm_hongkulou_lianjiashan, itm_brigandine_red, itm_leather_jerkin, itm_fighting_pick, itm_military_sickle_a, itm_peizhong_jian, itm_sword_medieval_c_long, itm_spiked_mace, itm_jianyi_langyabang, itm_footman_helmet, itm_mail_coif, itm_segmented_helmet, itm_helmet_with_neckguard, itm_norman_helmet, itm_splinted_leather_greaves, itm_iron_leather_boot, itm_leather_gloves, itm_fenzhi_pishoutao, itm_light_lance, itm_lance, itm_heavy_lance, itm_hunter, itm_saddle_horse, itm_saddle_horse, itm_saddle_horse],
   str_16 | agi_14 | int_8 | cha_5|level(23),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_1|knows_athletics_3|knows_riding_4|knows_horse_archery_5|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_rogue_knight","Powell Rogue Knight","Powell Rogue Knights",#普威尔无赖骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_hongyu_zhumiankui, itm_lvlong_lianjaizhaopao, itm_steel_leather_boot, itm_lamellar_gauntlets, itm_hongyipijia_ma, itm_dahong_lianjiazhaopao, itm_mail_with_surcoat, itm_puweier_lianjia, itm_white_dragon_fan_shaped_shield, itm_blue_lion_fan_shaped_shield, itm_hongsejianyi_banlianjia, itm_military_pick, itm_zhanshi_chu, itm_military_cleaver_c, itm_bastard_sword_a, itm_bastard_sword_b, itm_bastard_sword_a, itm_bastard_sword_b, itm_sword_two_handed_b, itm_sword_medieval_d_long, itm_hongwen_qiqiang, itm_lianjia_qingbiankui, itm_fangmian_jianzuikui, itm_zhumiankui, itm_splinted_greaves, itm_mail_boots, itm_mail_chausses, itm_mail_mittens, itm_fenzhi_lianjiashoutao, itm_great_lance, itm_honghei_wenqiqiang, itm_hongheipijia_ma, itm_chenyipijia_ma, itm_jinhongpijia_ma, itm_shiwenpijia_ma, itm_hongbai_pijia_liema, itm_honghua_pijia_liema, itm_honghei_lianjia_pingyuanma],
   str_26 | agi_23 | int_14 | cha_13|level(42),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["rodriguez_rogue_attendant","Rodriguez Rogue Attendant","Rodriguez Rogue Attendants",#罗德里格斯无赖扈从
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_tab_shield_heater_a, itm_nordic_shield, itm_tab_shield_round_a, itm_tab_shield_round_d, itm_footman_helmet, itm_mail_shirt, itm_splinted_leather_greaves, itm_blue_gambeson, itm_lanmiu_lianjiashan, itm_lanse_xiongjia, itm_duanxiu_lianjiapao, itm_padded_leather, itm_wooden_shield, itm_tab_shield_heater_b, itm_tab_shield_heater_c, itm_military_cleaver_b, itm_sword_medieval_c_long, itm_peizhong_jian, itm_sword_medieval_d_long, itm_fighting_axe, itm_hand_axe, itm_one_handed_war_axe_a, itm_flat_topped_helmet, itm_segmented_helmet, itm_mail_coif, itm_leather_gloves, itm_helmet_with_neckguard, itm_baotie_toujin, itm_xihai_pixue, itm_leather_boots, itm_iron_leather_boot, itm_fenzhi_pishoutao, itm_fenzhi_fulianshoutao, itm_mail_mittens, itm_long_pole_machete, itm_military_scythe],
   str_16 | agi_14 | int_8 | cha_5|level(23),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (180),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_1|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["rodriguez_rogue_knight","Rodriguez Rogue Knight","Rodriguez Rogue Knights",#罗德里格斯无赖骑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_blue_purple_triangular_shield, itm_blue_flower_skoutarion, itm_jainyi_changbingfu, itm_fangmian_jianzuikui, itm_shenlan_lianjiazhaopao, itm_mail_boots, itm_gauntlets, itm_lanse_lianjiazhaopao, itm_honghua_lianjia, itm_simple_griffon_skoutarion, itm_mail_and_plate, itm_honglanpao_banlian, itm_blue_dragon_large_shield, itm_blue_lion_fan_shaped_shield, itm_red_blue_fan_shaped_shield, itm_powell_noble_hand_and_a_half_sword, itm_bastard_sword_b, itm_great_sword, itm_two_handed_cleaver, itm_voulge, itm_axe, itm_jainyi_shuangrenfu, itm_qinliang_shuangshoufu, itm_one_handed_battle_axe_c, itm_two_handed_axe, itm_jianyi_shuangshoufu, itm_heiyu_jianzuikui, itm_jianzuikui, itm_hue_qingbiankui, itm_lianjia_qingbiankui, itm_zhumiankui, itm_scale_gauntlets, itm_iron_greaves, itm_splinted_greaves, itm_fenzhi_fubanshoutao, itm_fenzhi_fulianshoutao],
   str_26 | agi_23 | int_14 | cha_13|level(42),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (350),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["city_rogue_attendant","City Rogue Attendant","City Rogue Attendants",#自由城邦无赖扈从
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_jiaoguo_sheshoukui, itm_baise_xiongjia, itm_aketon_green, itm_gambeson, itm_tab_shield_pavise_a, itm_padded_cloth, itm_tab_shield_pavise_b, itm_tab_shield_pavise_c, itm_mace_4, itm_sarranid_mace_1, itm_mace_2, itm_military_hammer, itm_handguard_hammer, itm_jianyi_lengtouchui, itm_qinliang_lengtouchui, itm_flat_topped_helmet, itm_wozhuangkui, itm_norman_helmet, itm_guard_helmet, itm_bascinet_2, itm_bascinet_3, itm_ban_qingbiankui, itm_mail_mittens, itm_fenzhi_lianjiashoutao, itm_jianyi_jiantiqiang, itm_pitch_fork, itm_boar_spear, itm_military_fork, itm_kuotou_qiang, itm_jiachang_kuotou_qiang, itm_citou_qiang, itm_jiantou_qiang, itm_crossbow, itm_bolts, itm_splinted_leather_greaves, itm_mail_chausses, itm_leather_boots],
   str_16 | agi_14 | int_8 | cha_5|level(23),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (170) | wp_archery (100) | wp_crossbow (170) | wp_throwing (100),
   knows_ironflesh_5|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_4|knows_athletics_3|knows_riding_3|knows_horse_archery_5|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_4|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["city_rogue_knight","City Rogue Knight","City Rogue Knights",#自由城邦无赖骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_heiyu_jianzuikui, itm_iron_greaves, itm_scale_gauntlets, itm_jinhua_lianjiazhaopao, itm_heibai_lianjiazhaopao, itm_baipao_banlian, itm_hue_qingbiankui, itm_zhumiankui, itm_jianzuikui, itm_fangmian_jianzuikui, itm_huodong_yuantikui, itm_heibai_wenqiqiang, itm_gauntlets, itm_fenzhi_fulianshoutao, itm_baiwen_qiqiang, itm_great_lance, itm_birch_crossbow, itm_bolts, itm_bastard_sword_a, itm_bastard_sword_b, itm_sword_medieval_d_long, itm_splinted_greaves, itm_mail_boots, itm_light_crossbow, itm_baiyu_nushi, itm_heibaiyu_nushi, itm_heiyu_nushi, itm_hongyu_nushi, itm_steel_bolts, itm_huise_ma, itm_zase_ma, itm_shenseliema, itm_baiyipijia_ma, itm_jinshizi_ma, itm_lanshizipijia_ma, itm_hongshizipijia_ma, itm_hongbaipijia_ma, itm_shiwenpijia_ma, itm_yellow_black_skoutarion, itm_black_yellow_skoutarion, itm_preist_fan_shaped_shield],
   str_26 | agi_23 | int_14 | cha_13|level(42),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (340) | wp_archery (200) | wp_crossbow (340) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_devout_6|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["araiharsa_mercenary_infantry","Araiharsa Mercenary Infantry","Araiharsa Mercenary Infantries",#阿利哈沙雇佣步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_kouruto_bow, itm_stud_decorated_skin_battle_shield, itm_kouruto_handmade_desert_sword, itm_nanfang_jichangmao, itm_sarranid_warrior_cap, itm_archers_vest, itm_sarranid_boots_a, itm_luzhi_bikai, itm_bodkin_arrows, itm_barbed_arrows],
   str_34 | agi_22 | int_9 | cha_16|level(20),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (170) | wp_crossbow (170) | wp_throwing (170),
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_2|knows_athletics_2|knows_riding_1|knows_horse_archery_2|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_4|knows_prisoner_management_1|knows_leadership_2|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["araiharsa_mercenary_rider","Araiharsa Mercenary Rider","Araiharsa Mercenary Riders",#阿利哈沙雇佣骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_arabian_sword_b, itm_stud_decorated_skin_battle_shield, itm_arabian_sword_a, itm_southern_horn_bow, itm_sarranid_mail_coif, itm_khergit_guard_armor, itm_sarranid_boots_c, itm_lamellar_gauntlets, itm_luotuo, itm_nanfang_jian, itm_nanfang_jian],
   str_34 | agi_22 | int_9 | cha_16|level(40),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_4|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_6|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

#沙舟骑士团
  ["sandboat_knight","Sandboat Knight","Sandboat Knights",#沙舟骑士
  tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
  0,0,fac_kingdom_1,
   [itm_southern_knight_bow, itm_nanfang_jian, itm_hongyu_sheshoujian, itm_duangang_changjian, itm_nanfang_chaozhongkui, itm_sandboat_knight_plate, itm_iron_greaves, itm_fenzhi_fubanshoutao, itm_warhorse_sarranid, itm_lion_decorative_shield],
   str_34 | agi_30 | int_21 | cha_20|level(49),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
  knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_11|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
  powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["sousanth_servant","Sousanth Servant","Sousanth Servants",#南沙仆从
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword, itm_spike_skin_battle_shield, itm_nanfang_jian, itm_southern_horn_bow, itm_sarranid_veiled_helmet, itm_sarranid_elite_armor, itm_sarranid_boots_d, itm_lamellar_gauntlets, itm_arabian_horse_a],
   str_23 | agi_23 | int_15 | cha_13|level(34),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (380) | wp_archery (320) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_5|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
#古洛隆卫队
  ["gurorrion_guard","Gurorrion Guard","Gurorrion Guards",#古洛隆卫士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_1,
   [itm_jinshi_zhanbiao, itm_jinshi_zhanbiao, itm_nanfang_shuangshoujian, itm_sarranid_veiled_helmet, itm_powell_south_ligature_plate, itm_sarranid_boots_d, itm_lamellar_gauntlets],
   str_33 | agi_22 | int_17 | cha_18|level(47),wp_one_handed (470) | wp_two_handed (470) | wp_polearm (470) | wp_archery (470) | wp_crossbow (470) | wp_throwing (470),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_7|knows_athletics_7|knows_riding_4|knows_horse_archery_8|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],


#—————————————————————————————————龙神教—————————————————————————————————
##
  ["dragon_power_worshipper","Dragon Power Worshipper","Dragon Power Worshippers",#龙力崇拜者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_1,
   [itm_jianyi_peizhongjian, itm_hushou_duanjian, itm_sword_medieval_c_small, itm_hongbai_pingmingyi, itm_leather_boots, itm_leather_gloves, itm_splinted_leather_greaves, itm_woolen_hose, itm_ankle_boots, itm_hunter_boots, itm_luzhi_shoutao, itm_pitch_fork, itm_military_fork, itm_boar_spear, itm_kuotou_qiang, itm_jiachang_kuotou_qiang, itm_honghuang_pingmingfu, itm_hongbai_pingmingfu, itm_dahong_pingming_fu, itm_red_noble_shirt, itm_rich_outfit, itm_short_tunic, itm_tab_shield_kite_b, itm_tab_shield_kite_a, itm_tab_shield_kite_c, itm_tab_shield_pavise_a],
   str_13 | agi_11 | int_8 | cha_6|level(15),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (110) | wp_crossbow (110) | wp_throwing (110),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_tactics_1|knows_pathfinding_1|knows_inventory_management_1|knows_wound_treatment_1|knows_persuasion_1|knows_memory_3|knows_study_2|knows_devout_4|knows_leadership_1|knows_trade_1,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["dragon_god_follower","Dragon God Follower","Dragon God Followers",#龙神追随者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_simple_red_dragon_skoutarion, itm_duangang_duanjian, itm_hushou_duanjian, itm_bec_de_corbin_a, itm_flat_topped_helmet, itm_hongse_xiongjia, itm_splinted_leather_greaves, itm_leather_gloves, itm_longshen_jiaoshitouhuan],
   str_17 | agi_13 | int_13 | cha_10|level(25),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_2|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_5|knows_prisoner_management_1|knows_leadership_3|knows_trade_1,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["dragon_blood_swordsman","Dragon Blood Swordsman","Dragon Blood Swordsmen",#龙血剑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_duangang_shoubanjian, itm_simple_red_dragon_skoutarion, itm_great_sword, itm_ban_qingbiankui, itm_lvlong_lianjaizhaopao, itm_mail_chausses, itm_mail_mittens],
   str_25 | agi_15 | int_17 | cha_15|level(35),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_4|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_5|knows_devout_6|knows_prisoner_management_2|knows_leadership_5|knows_trade_3,
   powell_face_young_1, powell_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["dragon_power_great_swordman","Dragon Power Great Swordman","Dragon Power Great Swordmen",#龙力大剑师
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_1,
   [itm_yansha_shuangshoujian, itm_changmain_hongyu_zhumiankui, itm_dragon_sword_master_plate, itm_longwen_banjiaxue, itm_fangxing_bikai],
   str_42 | agi_36 | int_24 | cha_20|level(56),wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_6|knows_athletics_11|knows_riding_6|knows_horse_archery_10|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["dragonwings_knight","Dragonwings Knight","Dragonwings Knights",#龙翼骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_blood_sorcery_lance, itm_silver_dragon_fan_shaped_shield, itm_hongyu_zhumiankui, itm_dragon_worshipper_plate, itm_guanze_banjiaxue, itm_fangxing_bikai, itm_hongbanjia_longxuama],
  str_39 | agi_36 | int_23 | cha_22|level(54),wp_one_handed (530) | wp_two_handed (530) | wp_polearm (530) | wp_archery (530) | wp_crossbow (530) | wp_throwing (530),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_6|knows_athletics_8|knows_riding_9|knows_horse_archery_10|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_11|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["dragonword_practitioner","Dragonword Practitioner","Dragonword Practitioners",#龙言修习者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_sorcery_lance, itm_blue_dragon_skoutarion, itm_zhanshi_chu, itm_powell_noble_sword, itm_longshen_jiaoshitouhuan, itm_lvlong_lianjaizhaopao, itm_mail_chausses, itm_mail_mittens, itm_hongyipijia_ma, itm_mogang_duanlian],
   str_21 | agi_17 | int_20 | cha_18|level(30),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_4|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_8|knows_study_3|knows_devout_5|knows_prisoner_management_2|knows_leadership_5|knows_trade_3,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["dragonword_great_presbyter","Dragonword Great Presbyter","Dragonword Great Presbyters",#龙吼大司祭
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_blood_sorcery_lance, itm_white_dragon_fan_shaped_shield, itm_powell_noble_hand_and_a_half_sword, itm_longshen_silitouhuan, itm_dragon_worshipper_robe, itm_heise_banlianjiaxue, itm_mogang_yuanzhi_bikai],
   str_33 | agi_29 | int_37 | cha_18|level(50),wp_one_handed (470) | wp_two_handed (470) | wp_polearm (470) | wp_archery (470) | wp_crossbow (470) | wp_throwing (470),
   knows_ironflesh_13|knows_power_strike_9|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_5|knows_first_aid_4|knows_engineer_2|knows_persuasion_9|knows_array_arrangement_2|knows_memory_12|knows_study_8|knows_devout_8|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_strategic_strength, #战略力量
  ],

  ["dragonhead_master","Dragonhead Master","Dragonhead Masters",#龙首大导师
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_blood_sorcery_lance, itm_qishi_danshouzhanfu, itm_whitegold_helmet, itm_dragon_sword_master_plate, itm_longwen_banjiaxue, itm_yinse_bikai, itm_holy_dragoon_knight_shield, itm_hongsequanbanjia_ma],
  str_60 | agi_54 | int_40 | cha_32|level(60),wp_one_handed (580) | wp_two_handed (580) | wp_polearm (580) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_7|knows_power_draw_9|knows_weapon_master_12|knows_shield_8|knows_athletics_11|knows_riding_11|knows_horse_archery_10|knows_looting_4|knows_trainer_10|knows_tracking_4|knows_tactics_8|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_9|knows_array_arrangement_3|knows_memory_13|knows_study_9|knows_devout_7|knows_prisoner_management_8|knows_leadership_12|knows_trade_5,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#镇静公馆
  ["sedative_pavilion_nurse","Sedative Pavilion Nurse","Sedative Pavilion Nurses",#镇静公馆护士
   tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor,
   0, 0, fac_kingdom_1,
   [itm_jinshi_bishou, itm_sedative_maid_cloth, itm_sedative_physician_high_heeled_boot],
   str_10 | agi_6 | int_14 | cha_17|level(12),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_1|knows_inventory_management_1|knows_wound_treatment_3|knows_surgery_2|knows_first_aid_2|knows_persuasion_1|knows_memory_2|knows_study_6|knows_trade_1,
   0x00000000000050010000000000000e0000000000000000000000000000000000, 0x000000003f0060310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["sedative_pavilion_maid","Sedative Pavilion Maid","Sedative Pavilion Maids",#镇静公馆侍女
   tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
   0, 0, fac_kingdom_1,
   [itm_wangguo_jian, itm_wangguo_jian, itm_jinshi_cejian, itm_noble_practice_bow, itm_sedative_maid_cloth, itm_sedative_physician_high_heeled_boot, itm_perfumer_glove],
  str_15 | agi_10 | int_19 | cha_24|level(24),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_2|knows_horse_archery_3|knows_trainer_2|knows_tactics_2|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_8|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   0x00000000000050010000000000000e0000000000000000000000000000000000, 0x000000003f0060310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["sedative_pavilion_physician","Sedative Pavilion Physician","Sedative Pavilion Physicians",#镇静公馆医师
   tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_1,
   [itm_jinshi_fanhuajian, itm_deep_one_knife_shield, itm_silver_crown, itm_sedative_physician_cloth, itm_sedative_physician_high_heeled_boot, itm_fenzhi_pishoutao, itm_gorgeous_composite_bow, itm_jingling_lierenjian1],
  str_23 | agi_17 | int_34 | cha_32|level(37),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_2|knows_trainer_4|knows_tracking_2|knows_tactics_3|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_4|knows_memory_9|knows_study_10|knows_prisoner_management_3|knows_leadership_6|knows_trade_4,
   0x00000000000050010000000000000e0000000000000000000000000000000000, 0x000000003f0060310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["tranquility_chief_physician","Tranquility Chief Physician","Tranquility Chief Physicians",#安宁主治
   tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_1,
   [itm_green_arrow, itm_backhand_sabre_shield, itm_jinshi_longshoujian, itm_no_head, itm_sedative_chief_physician_cloth, itm_sedative_knight_high_heeled_boot, itm_fenzhi_huzhishoutao, itm_knight_recurve_bow],
   str_28 | agi_22 | int_38 | cha_41|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (420) | wp_crossbow (420) | wp_throwing (420),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_7|knows_shield_6|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_5|knows_trainer_6|knows_tracking_3|knows_tactics_6|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_7|knows_wound_treatment_9|knows_surgery_9|knows_first_aid_8|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_6|knows_memory_11|knows_study_13|knows_prisoner_management_5|knows_leadership_9|knows_trade_5,
   0x00000000000050010000000000000e0000000000000000000000000000000000, 0x000000003f0060310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_assistance, #辅助
  ],

  ["liminal_physician","Liminal Physician","Liminal Physicians",#医界师
   tf_pretty_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_1,
   [itm_jingling_youxiajian, itm_backhand_sabre_shield, itm_jinshi_qishijian, itm_silver_crown, itm_sedative_knight_plate, itm_sedative_knight_high_heeled_boot, itm_sedative_gauntlet, itm_steel_bow, itm_white_spiritual_horse],
   str_37 | agi_32 | int_56 | cha_60|level(60),wp_one_handed (520) | wp_two_handed (520) | wp_polearm (520) | wp_archery (540) | wp_crossbow (540) | wp_throwing (540),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_6|knows_power_draw_9|knows_weapon_master_9|knows_shield_8|knows_athletics_9|knows_riding_8|knows_horse_archery_10|knows_looting_7|knows_trainer_7|knows_tracking_5|knows_tactics_8|knows_pathfinding_5|knows_spotting_6|knows_inventory_management_9|knows_wound_treatment_10|knows_surgery_10|knows_first_aid_10|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_8|knows_memory_13|knows_study_15|knows_prisoner_management_7|knows_leadership_11|knows_trade_6,
   0x00000000000050010000000000000e0000000000000000000000000000000000, 0x000000003f0060310000000000000fff00000000000000000000000000000000, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],


#—————————————————————————————————圣龙骑士团—————————————————————————————————
##
  ["holy_dragoon_knight","Holy Dragoon Knight","Holy Dragoon Knights",#圣龙骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_1,
   [itm_dragon_blood_sorcery_lance, itm_holy_dragoon_knight_shield, itm_paladin_halo_helmet, itm_holy_dragoon_armor, itm_longwen_banjiaxue, itm_huali_shalouhushou, itm_silver_super_dragonblood_horse],
   str_63 | agi_57 | int_45 | cha_56|level(62), wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_12|knows_power_draw_12|knows_weapon_master_13|knows_shield_9|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_6|knows_trainer_10|knows_tracking_6|knows_tactics_9|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_10|knows_array_arrangement_6|knows_memory_14|knows_study_12|knows_devout_7|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   powell_face_middle_1, powell_face_middle_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],


  ["powell_messenger","Powell Messenger","Powell Messengers", #普威尔信使
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_kingdom_1,
   [itm_zhanshi_chu, itm_powell_fan_shaped_shield, itm_hongwen_qiqiang, itm_flat_topped_helmet, itm_puweier_lianjia, itm_steel_leather_boot, itm_scale_gauntlets, itm_hunter],
   str_23 | agi_19 | int_16 | cha_10|level(35), wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_7|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_5|knows_trade_2,
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["powell_deserter","Powell Deserter","Powell Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,powell_face_young_1, powell_face_old_2],




##########################################################伊希斯公国##########################################################

#—————————————————————————————————公国通用—————————————————————————————————
##
  ["yishith_inferior_elf","Yishith Inferior Elf","Yishith Inferior Elf",#伊希斯劣等精灵
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_yishith_dagger, itm_barbed_arrows, itm_elf_simple_bow, itm_bodkin_arrows, itm_tint_elf_cloth, itm_woolen_hose, itm_nvshi_shoutao, itm_fusco_elf_cloth],
   str_3 | agi_14 | int_12 | cha_14|level(5),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (100) | wp_crossbow (50) | wp_throwing (50),
   knows_power_draw_1|knows_weapon_master_3|knows_shield_1|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_3|knows_array_arrangement_3|knows_memory_5|knows_study_8|knows_devout_12, 
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_elf_hunter","Yishith_elf_hunter","Yishith_elf_hunter",#伊希斯精灵猎户
   tf_elf|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_elf_hunter_bow, itm_yishith_dagger, itm_jingling_lierenjian1, itm_jingling_lierenjian1, itm_silver_crown, itm_elf_light_leather_armor, itm_splinted_leather_greaves, itm_fenzhi_jiaqiangshoutao],
   str_6 | agi_19 | int_15 | cha_19|level(10),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (150) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_1|knows_power_draw_3|knows_weapon_master_5|knows_shield_1|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_9|knows_devout_12|knows_leadership_1, 
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_elf_skirmisher","Yishith Elf Skirmisher","Yishith Elf Skirmisher",#伊希斯精灵散兵
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_elf_hunter_bow, itm_yixisi_qingliangjian, itm_jingling_sanbingjian, itm_jingling_sanbingjian, itm_ranger_hood, itm_elf_leather_armor, itm_iron_leather_boot, itm_fenzhi_pishoutao],
   str_9 | agi_26 | int_18 | cha_26|level(20),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (240) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_power_draw_5|knows_weapon_master_7|knows_shield_2|knows_athletics_8|knows_riding_4|knows_horse_archery_9|knows_looting_3|knows_trainer_4|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_8|knows_study_10|knows_devout_12|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_elf_woodguard","Yishith Elf Woodguard","Yishith Elf Woodguard",#伊希斯精灵巡林者
   tf_elf|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_elf_woodguard_longbow, itm_yejian_qiang, itm_jingling_sanbingjian, itm_jingling_sanbingjian, itm_ranger_helmet, itm_forest_guard_chain_armor, itm_iron_leather_greave, itm_fenzhi_jiaqiangshoutao],
   str_14 | agi_33 | int_21 | cha_33|level(30),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (330) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_7|knows_shield_3|knows_athletics_11|knows_riding_5|knows_horse_archery_11|knows_looting_6|knows_trainer_5|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_11|knows_devout_12|knows_prisoner_management_3|knows_leadership_4|knows_trade_1,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_jungleslaughterer","Yishith Jungleslaughterer","Yishith Jungleslaughterer",#伊希斯密林游猎
   tf_elf|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_elf_woodguard_longbow, itm_elf_halberd, itm_jingling_sanbingjian, itm_jingling_shuyongjian, itm_flower_red_cape, itm_elf_leaf_scale_armor, itm_nailed_iron_leather_boot, itm_fenzhi_jiaqiangshoutao],
   str_18 | agi_45 | int_26 | cha_45|level(42),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (450) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_10|knows_shield_4|knows_athletics_13|knows_riding_6|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_11|knows_study_12|knows_devout_13|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_elf_outrider","Yishith Elf Outrider","Yishith Elf Outrider",#伊希斯精灵巡狩
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_elf_outrider_bow, itm_yixisi_qingliang_shoubanjian, itm_jingling_sanbingjian, itm_jingling_shuyongjian, itm_ranger_helmet, itm_yishith_ranger_chest_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao, itm_lvqinpijia_ma],
   str_19 | agi_37 | int_24 | cha_45|level(38),wp_one_handed (240) | wp_two_handed (50) | wp_polearm (50) | wp_archery (400) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_10|knows_shield_4|knows_athletics_11|knows_riding_10|knows_horse_archery_13|knows_looting_7|knows_trainer_6|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_11|knows_study_11|knows_devout_12|knows_prisoner_management_6|knows_leadership_7|knows_trade_3,
    half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["yishith_human_resident","Yishith Human Resident","Yishith Human Resident",#伊希斯人类居民
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_butchering_knife, itm_tab_shield_pavise_a, itm_sword_medieval_c_small, itm_dagger, itm_felt_hat_b, itm_yixisirenlei_fu, itm_beifang_bangtui, itm_hood_d, itm_hood_c, itm_hood_b, itm_common_hood, itm_leather_cap, itm_sickle, itm_cleaver, itm_knife, itm_sword_medieval_a],
   str_7 | agi_7 | int_6 | cha_5|level(5),wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_athletics_1|knows_horse_archery_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1,
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["yishith_human_militia","Yishith Human Militia","Yishith Human Militia",#伊希斯征召民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_tab_shield_pavise_b, itm_jianyi_yejianqiang, itm_skullcap, itm_beifang_pijia, itm_beifang_mianku, itm_luzhi_shoutao, itm_leather_warrior_cap, itm_leather_gloves],
   str_10 | agi_8 | int_6 | cha_6|level(10),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_shield_2|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_looting_2|knows_tactics_1|knows_pathfinding_1|knows_inventory_management_2|knows_memory_1|knows_study_1|knows_devout_2|knows_leadership_1|knows_trade_1,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["yishith_human_infantry","Yishith Human Infantry","Yishith Human Infantry",#伊希斯人类步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_tab_shield_pavise_c, itm_jianyi_yejianqiang, itm_segmented_helmet, itm_beifang_pijia, itm_leather_boots, itm_leather_gloves, itm_splinted_leather_greaves, itm_helmet_with_neckguard],
   str_15 | agi_12 | int_7 | cha_6|level(20),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_3|knows_athletics_3|knows_riding_2|knows_horse_archery_3|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   yishith_face_middle_1, yishith_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["yishith_human_cavalry","Yishith Human Cavalry","Yishith Human Cavalry",#伊希斯人类马兵
   tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_bastard_sword_a, itm_sword_medieval_d_long, itm_tab_shield_kite_c, itm_jianyi_yejianqiang, itm_bascinet_2, itm_beifang_lingxiongjia, itm_iron_leather_greave, itm_mail_mittens, itm_lanwen_pijia_liema],
   str_17 | agi_14 | int_8 | cha_7|level(26),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_3|knows_leadership_3|knows_trade_3,
   yishith_face_middle_1, yishith_face_older_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["yishith_human_heavyinfantry","Yishith Human Heavyinfantry","Yishith Human Heavyinfantry",#伊希斯人类重步兵
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_yejian_qiang, itm_tab_shield_pavise_d, itm_bascinet_3, itm_beifang_lingxiongjia, itm_iron_leather_greave, itm_mail_mittens],
   str_16 | agi_13 | int_8 | cha_7|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_3|knows_leadership_3|knows_trade_3,
   yishith_face_middle_1, yishith_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["yishith_human_guard","Yishith Human Guard","Yishith Human Guard",#伊希斯盾兵
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_changren_qiang, itm_tab_shield_pavise_d, itm_lanzong_yuanding_fangmiankui, itm_heise_lianxiongjia, itm_steel_leather_boot, itm_gauntlets],
   str_21 | agi_16 | int_8 | cha_7|level(32),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   yishith_face_middle_1, yishith_face_older_2, 0, 
   0, 0, itm_function_defend, #防御
  ],


#—————————————————————————————————灵魄之灵树—————————————————————————————————
##
  ["soul_full_elf","Soul Full Elf","Soul Full Elf",#灵魄之树纯血精灵
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_elf_outrider_bow, itm_elf_light_shield, itm_yixisi_wandao, itm_jingling_shuyongjian, itm_silver_crown, itm_soul_full_elf_cloth, itm_splinted_leather_greaves, itm_fenzhi_jiaqiangshoutao, itm_silver_mane_steed],
   str_12 | agi_30 | int_24 | cha_34|level(20),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (270) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_6|knows_weapon_master_7|knows_shield_4|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_3|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_13|knows_devout_14|knows_prisoner_management_3|knows_leadership_5|knows_trade_1,
   soul_elf_face_key_1, soul_elf_face_key_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["yishith_equerry","Yishith Equerry","Yishith Equerry",#伊希斯骑士侍从
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_elf_outrider_bow, itm_elf_light_shield, itm_yishith_gorgeous_sword, itm_jingling_youxiajian, itm_ranger_helmet, itm_soul_elf_attendant_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao, itm_white_spiritual_horse],
   str_18 | agi_38 | int_28 | cha_42|level(30),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (360) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_7|knows_weapon_master_7|knows_shield_6|knows_athletics_11|knows_riding_9|knows_horse_archery_11|knows_looting_6|knows_trainer_6|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   soul_elf_face_key_1, soul_elf_face_key_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["yishith_spiritual_horse_knight","Yishith Spiritual Horse Knight","Yishith Spiritual Horse Knight",#伊希斯灵马骑士
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_forestwarden_bow, itm_elf_light_shield, itm_yishith_gorgeous_sword, itm_jingling_youxiajian, itm_elf_dome_helmet, itm_unicorn_chain_armor, itm_emerald_boot, itm_fenzhi_lianjiashoutao, itm_leather_armor_spiritual_horse],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (470) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_8|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   soul_elf_face_key_1, soul_elf_face_key_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["seddlined_thrall","Seddlined Thrall","Seddlined Thralls",#灵芽隶从
   tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_shortened_spear, itm_spear, itm_tab_shield_pavise_a, itm_felt_hat, itm_lvse_dianchengjia, itm_lvse_minbing_mianjia, itm_tab_shield_pavise_b, itm_felt_hat_b],
   str_13 | agi_10 | int_7 | cha_5|level(15),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_1|knows_athletics_3|knows_riding_1|knows_horse_archery_2|knows_looting_2|knows_trainer_1|knows_tracking_3|knows_tactics_1|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_2|knows_memory_3|knows_prisoner_management_1|knows_leadership_2|knows_trade_3,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["seddlined_puppet","Seddlined Puppet","Seddlined Puppets",#灵芽傀儡
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_sword_medieval_c_small, itm_jianyi_yejianqiang, itm_tab_shield_pavise_b, itm_jianyi_peizhongjian, itm_helmet_with_neckguard, itm_yixisirenlei_xiongjia, itm_beifang_bangtui, itm_footman_helmet, itm_segmented_helmet, itm_mail_coif, itm_jiushi_yuandingkui, itm_beifang_mianku],
   str_16 | agi_14 | int_7 | cha_7|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_3|knows_shield_2|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["seddlined_desperater","Seddlined Desperater","Seddlined Desperaters",#灵苗死士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_bastard_sword_a, itm_yejian_qiang, itm_seedlined_head, itm_lvse_xiongjia, itm_steel_leather_boot, itm_leather_gloves, itm_clover_fan_shaped_shield],
   str_29 | agi_24 | int_3 | cha_3|level(32),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (230),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_4|knows_tracking_5|knows_spotting_5,
   yishith_face_young_1, yishith_face_old_2],
  ["seddlined_dare_to_die_corp","Seddlined Dare-to-die Corp","Seddlined Dare-to-die Corps",#灵花决死剑士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_mogang_shuangshoujian, itm_seedlined_flower_head, itm_lvbai_jiazhong_banjia, itm_mail_boots, itm_kongju_bikai, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_red_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head],
   str_37 | agi_30 | int_3 | cha_30|level(48),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_5|knows_horse_archery_8|knows_looting_4|knows_tracking_5|knows_spotting_5,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["seddlined_crazy_cavalry","Seddlined Crazy Cavalry","Seddlined Crazy Cavalry",#灵苗狂骑兵
   tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,
   0,0,fac_kingdom_2,
   [itm_sword_two_handed_b, itm_seedlined_head, itm_mail_with_tunic_green, itm_splinted_greaves, itm_gauntlets, itm_heise_ma],
   str_29 | agi_24 | int_3 | cha_3|level(35),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_7|knows_horse_archery_7|knows_looting_4|knows_tracking_5|knows_spotting_5,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["seddlined_apostle","Seddlined Apostle","Seddlined Apostles",#灵花使徒
   tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_lvbai_wenqiqiang, itm_mogang_jundao, itm_seedlined_flower_head, itm_lvbai_jiazhong_banjia, itm_shengtie_banjiaxue, itm_kongju_bikai, itm_lvhua_lianjia_pinyuanma, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_red_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_seedlined_flower_head, itm_clover_fan_shaped_shield],
   str_37 | agi_30 | int_3 | cha_30|level(51),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (340) | wp_archery (340) | wp_crossbow (340) | wp_throwing (340),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_6|knows_athletics_6|knows_riding_8|knows_horse_archery_8|knows_looting_4|knows_tracking_5|knows_spotting_5,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["soul_selected_champion","Soul Selected Champion","Soul Selected Champions",#灵魄之树神选冠军
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_spirit_tree_god_selection_sword, itm_selected_champion_headcrown, itm_selected_champion_glass_armor, itm_elf_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_eternal_inheritance_bow, itm_full_armor_unicorn],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (660) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_15|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   soul_elf_face_key_1, soul_elf_face_key_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#灵树骑士团
  ["spirittree_knight","Spirittree Knight","Spirittree Knights",#灵树骑士
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_elf_light_shield, itm_yishith_knight_sword, itm_yishith_knight_strengthen_helmet, itm_spiritual_tree_armor, itm_elf_valkyrie_boot, itm_jingling_liulijian, itm_fenzhi_fulianshoutao, itm_leather_armor_unicorn, itm_spirittree_knight_bow],
   str_29 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (570),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_13|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   soul_elf_face_key_1, soul_elf_face_key_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],




#—————————————————————————————————死亡之灵树—————————————————————————————————
##
  ["demise_full_elf","Demise Full Elf","Demise Full Elf",#死亡之树纯血精灵
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_double_deer_fan_shaped_shield, itm_jianyi_yejianqiang, itm_elf_ornamentation_bow, itm_jingling_lierenjian1, itm_silver_crown, itm_dark_tight_leather_armor, itm_jingling_lieren_mianku, itm_fenzhi_pishoutao],
   str_12 | agi_30 | int_24 | cha_34|level(20),wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (250) | wp_crossbow (210) | wp_throwing (210),
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_5|knows_weapon_master_7|knows_shield_4|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_3|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_13|knows_devout_14|knows_prisoner_management_3|knows_leadership_5|knows_trade_1,
   demise_elf_face_key_1, demise_elf_face_key_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["hotbed_gatekeeper","Hotbed Gatekeeper","Hotbed Gatekeeper",#温床守门人
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_double_deer_fan_shaped_shield, itm_jianyi_yejianqiang, itm_elf_ornamentation_bow, itm_jingling_shuyongjian, itm_ranger_hood, itm_dark_tight_scale_armor, itm_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_17 | agi_35 | int_26 | cha_40|level(28),wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (330) | wp_crossbow (290) | wp_throwing (290),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_11|knows_riding_8|knows_horse_archery_11|knows_looting_6|knows_trainer_6|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   demise_elf_face_key_1, demise_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["hotbed_farmer","Hotbed Farmer","Hotbed Farmer",#温床护苗人
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_king_deer_fan_shaped_shield, itm_yejian_qiang, itm_string_of_elegy, itm_jingling_shuyongjian, itm_ranger_helmet, itm_dark_tight_composite_armor, itm_nailed_iron_leather_boot, itm_fenzhi_lianjiashoutao],
   str_21 | agi_44 | int_30 | cha_46|level(37),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (410) | wp_crossbow (380) | wp_throwing (380),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_12|knows_riding_9|knows_horse_archery_13|knows_looting_6|knows_trainer_6|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   demise_elf_face_key_1, demise_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["demise_gardener","Demise Gardener","Demise Gardener",#死亡园丁
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_jingling_youxiajian, itm_yejian_qiang, itm_string_of_elegy, itm_jingling_youxiajian, itm_elf_dome_helmet, itm_dark_chest_armor_shirt, itm_nailed_iron_leather_boot, itm_fenzhi_fulianshoutao],
   str_25 | agi_56 | int_37 | cha_60|level(50),wp_one_handed (50) | wp_two_handed (510) | wp_polearm (510) | wp_archery (530) | wp_crossbow (510) | wp_throwing (510),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_8|knows_athletics_13|knows_riding_10|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   demise_elf_face_key_1, demise_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["the_composted","the Composted","the Composted",#被堆肥者
   0,0,0,fac_slavers,
   [],
   str_9 | agi_6 | int_3 | cha_3|level(1),wp_one_handed (10) | wp_two_handed (10) | wp_polearm (10) | wp_archery (10) | wp_crossbow (10) | wp_throwing (10),
   knows_ironflesh_1|knows_study_4,
   diemer_face_younger_1, diemer_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["living_root","Living Root","Living Roots",#活根
   tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_2,
   [itm_root_borning_one_hand, itm_root_borning_one_foot, itm_root_borning_one_body, itm_butchering_knife],
   str_22 | agi_7 | int_3 | cha_3|level(15),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),
   knows_ironflesh_5|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_athletics_3|knows_riding_1|knows_horse_archery_2|knows_tracking_3|knows_study_4,
   root_borning_one_face, root_borning_one_face, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["root_borning_one","Root Borning One","Root Borning Ones",#根生者
   tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_silver_winged_sword, itm_haze_crow_fan_shaped_shield, itm_mail_coif, itm_root_borning_one_body, itm_root_borning_one_foot, itm_root_borning_one_hand, itm_pitch_fork, itm_boar_spear, itm_shortened_spear, itm_lengtou_qiang, itm_jiantou_qiang, itm_citou_qiang, itm_spear, itm_sword_medieval_c_small, itm_sword_medieval_a, itm_hushou_duanjian, itm_jianyi_peizhongjian, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_sword_medieval_c],
   str_27 | agi_12 | int_3 | cha_3|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_5|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_athletics_3|knows_riding_1|knows_horse_archery_2|knows_looting_3|knows_tracking_3|knows_pathfinding_1|knows_spotting_1|knows_study_4,
   root_borning_one_face, root_borning_one_face, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["humic_walker","Humic Walker","Humic Walkers",#腐殖行者
   tf_zombie|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_winged_board_shield, itm_vaegir_noble_helmet, itm_quanshen_lianjai, itm_root_borning_one_foot, itm_root_borning_one_hand, itm_awlpike_long, itm_ashwood_pike, itm_pike, itm_sanjian_qiang, itm_war_spear, itm_changren_qiang, itm_awlpike],
   str_34 | agi_14 | int_3 | cha_3|level(34),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_2|knows_shield_4|knows_athletics_4|knows_riding_1|knows_horse_archery_3|knows_looting_2|knows_tracking_3|knows_pathfinding_2|knows_spotting_2|knows_study_4,
   root_borning_one_face, root_borning_one_face, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["hotbed_hollow","Hotbed Hollow","Hotbed Hollows",#温床幽魂
   tf_zombie|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_yuanpian_humiankui, itm_diecengpilian_jia, itm_mail_chausses, itm_root_borning_one_hand, itm_military_scythe, itm_flat_head_axe, itm_glaive, itm_long_bardiche, itm_voulge, itm_hafted_blade_a, itm_great_long_bardiche, itm_poleaxe],
   str_42 | agi_24 | int_3 | cha_3|level(52),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_2|knows_shield_4|knows_athletics_7|knows_riding_2|knows_horse_archery_3|knows_looting_4|knows_tracking_5|knows_pathfinding_3|knows_spotting_3|knows_study_4,
   root_borning_one_face, root_borning_one_face, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["humic_vanguard","Humic Vanguard","Humic Vanguards",#腐殖先锋
   tf_zombie|tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_changren_qiang, itm_silver_winged_noble_sword, itm_silver_winged_long_sword, itm_half_bird_fan_shaped_shield, itm_vaegir_noble_helmet, itm_scale_armor, itm_mail_chausses, itm_root_borning_one_hand, itm_root_horse],
   str_33 | agi_14 | int_3 | cha_3|level(33),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_2|knows_shield_2|knows_athletics_4|knows_riding_3|knows_horse_archery_3|knows_looting_2|knows_tracking_3|knows_pathfinding_2|knows_spotting_2|knows_study_4,
   root_borning_one_face, root_borning_one_face, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["humus_lord","Humus Lord","Humus Lords",#腐土领主
   tf_zombie|tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_great_long_bardiche, itm_long_bardiche, itm_voulge, itm_aquila_skoutarion, itm_yuanpian_humiankui, itm_gouheng_zhongxing_banlianjia, itm_mail_boots, itm_root_borning_one_hand, itm_root_lizard, itm_silver_winged_great_sword, itm_silver_winged_noble_sword, itm_silver_winged_knight_sword],
   str_40 | agi_22 | int_3 | cha_3|level(50),wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (210) | wp_crossbow (210) | wp_throwing (210),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_2|knows_shield_2|knows_athletics_5|knows_riding_4|knows_horse_archery_4|knows_looting_4|knows_tracking_5|knows_pathfinding_3|knows_spotting_3|knows_study_4,
   root_borning_one_face, root_borning_one_face, 0, 
   0, 0, itm_function_combat, #格斗
  ],


  ["demise_selected_champion","Demise Selected Champion","Demise Selected Champions",#死亡之树神选冠军
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_gaojingling_xuejian, itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_light_armor, itm_elf_knight_boot, itm_kongju_bikai, itm_spirit_tree_god_selection_sword],
   str_41 | agi_81 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_11|knows_weapon_master_15|knows_shield_11|knows_athletics_14|knows_riding_13|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_4,
   demise_elf_face_key_1, demise_elf_face_key_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#灵雨游侠团
  ["spiritrain_ranger","Spiritrain Ranger","Spiritrain Ranger",#灵雨游侠
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_jingling_liulijian, itm_elf_halberd, itm_spiritrain_ranger_bow, itm_jingling_liulijian, itm_yishith_knight_helmet, itm_spiritrain_plate_skirt, itm_heise_banlianjiaxue, itm_gauntlets],
   str_30 | agi_60 | int_40 | cha_65|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_9|knows_weapon_master_12|knows_shield_8|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   demise_elf_face_key_1, demise_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],




#—————————————————————————————————先祖之灵树—————————————————————————————————
##
  ["ancester_full_elf","Ancester Full Elf","Ancester Full Elf",#先祖之树纯血精灵
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_jingling_sanbingjian, itm_yixisi_qingliang_shoubanjian, itm_ranger_horn_fan_shaped_shield, itm_silver_crown, itm_autumn_leather_armor, itm_leather_boots, itm_leather_gloves, itm_elf_woodguard_longbow],
   str_12 | agi_30 | int_24 | cha_34|level(20),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (230) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_4|knows_power_strike_2|knows_power_throw_1|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_3|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_13|knows_devout_14|knows_prisoner_management_3|knows_leadership_5|knows_trade_1,
   ancester_elf_face_key_1, ancester_elf_face_key_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["yishith_elf_sergeant","Yishith Elf Sergeant","Yishith Elf Sergeants",#伊希斯精灵军士
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_jingling_shuyongjian, itm_yixisi_qingliang_shuangshoujian, itm_honeysuckle_fan_shaped_shield, itm_ranger_hood, itm_autumn_scale_chest_armor, itm_iron_leather_boot, itm_scale_gauntlets, itm_elf_ornamentation_bow],
   str_18 | agi_38 | int_28 | cha_42|level(30),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (330) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_3|knows_power_draw_7|knows_weapon_master_7|knows_shield_8|knows_athletics_11|knows_riding_9|knows_horse_archery_11|knows_looting_6|knows_trainer_6|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   ancester_elf_face_key_1, ancester_elf_face_key_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["yishith_elf_heavy_cavalry","Yishith Elf Heavy Cavalry","Yishith Elf Heavy Cavalry",#伊希斯精灵重骑兵
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_daoye_jian, itm_yishith_elite_ridebow, itm_verdant_hammer, itm_rose_knight_shield, itm_changmian_jianzuikui, itm_verdant_light_plate_chain_composite_armor, itm_mail_boots, itm_gauntlets, itm_qiangwei_lianjia_pingyuanma],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (440),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   ancester_elf_face_key_1, ancester_elf_face_key_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["yishith_heavy_ranger","Yishith Heavy Ranger","Yishith Heavy Ranger",#伊希斯重甲游侠
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_daoye_jian, itm_yishith_elite_ridebow, itm_verdant_hammer, itm_rose_knight_shield, itm_jiaqiang_guokui2, itm_verdant_light_plate_chain_composite_armor, itm_nailed_iron_leather_boot, itm_leather_gloves],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (440),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   ancester_elf_face_key_1, ancester_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["immortal_seeker","Immortal Seeker","Immortal Seekers",#长生寻觅者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_stones, itm_shortened_spear, itm_pitch_fork, itm_wooden_board_shield, itm_hood_c, itm_green_tunic, itm_wrapping_boots, itm_hood_b, itm_common_hood, itm_stones, itm_ankle_boots, itm_hunter_boots, itm_stones],
   str_11 | agi_7 | int_6 | cha_6|level(10),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_athletics_1|knows_horse_archery_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_devout_4|knows_trade_1,
   yishith_face_middle_1, yishith_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],

  ["ancester_selected_champion","Ancester Selected Champion","Ancester Selected Champions",#先祖之树神选冠军
   tf_elf|tf_mounted|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_spirit_tree_god_selection_sword, itm_spirit_tree_halberd, itm_selected_champion_helmet, itm_selected_champion_graghite_armor, itm_black_greaves, itm_plate_armor_spiritual_horse, itm_heiguang_bikai],
   str_40 | agi_80 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_12|knows_power_strike_9|knows_power_throw_6|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   ancester_elf_face_key_1, ancester_elf_face_key_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#永世者刺客团
  ["immortal_assassin","Immortal Assassin","Immortal Assassin",#永世者刺客
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_verdant_hammer, itm_jingling_liulijian, itm_immortal_soul_bow, itm_full_elf_knight_shield, itm_graghite_steel_small_helmet, itm_immortal_plate_skirt, itm_valkyrie_boot, itm_mogang_yuanzhi_bikai],
   str_28 | agi_62 | int_38 | cha_64|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (580) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_10|knows_power_strike_7|knows_power_throw_4|knows_power_draw_11|knows_weapon_master_12|knows_shield_12|knows_athletics_14|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_12|knows_trade_3, 
   ancester_elf_face_key_1, ancester_elf_face_key_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#蜕生者战团
  ["half_molter","Half Molter","Half Molters",#半蜕生者
   tf_elf|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_sword_medieval_b, itm_sword_medieval_a, itm_sword_medieval_c_small, itm_tab_shield_pavise_b, itm_baotie_toujin, itm_tunic_with_green_cape, itm_leather_boots, itm_leather_gloves, itm_sword_medieval_b_small, itm_footman_helmet, itm_skullcap, itm_hide_boots, itm_splinted_leather_greaves, itm_fenzhi_pishoutao, itm_jiachang_kuotou_qiang, itm_kuotou_qiang, itm_war_spear, itm_jianyi_yejianqiang, itm_spear, itm_ashwood_pike, itm_citou_qiang, itm_jiantou_qiang, itm_lengtou_qiang, itm_boar_spear, itm_military_fork],
   str_10 | agi_10 | int_8 | cha_14|level(15),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_3|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_4|knows_looting_1|knows_tracking_1|knows_pathfinding_1|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_persuasion_2|knows_memory_2|knows_study_6|knows_devout_12|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["yishith_swordman","Yishith Swordman","Yishith Swordmen",#伊希斯剑士
   tf_elf|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_mogang_hushoujian, itm_tab_shield_heater_c, itm_tab_shield_heater_d, itm_tab_shield_heater_b, itm_changmain_qingbiankui, itm_leather_armor, itm_mail_chausses, itm_mail_mittens, itm_baotou_lianjiakui, itm_steel_leather_boot, itm_scale_gauntlets, itm_sword_two_handed_b],
   str_15 | agi_15 | int_8 | cha_19|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (100) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_7|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_6|knows_devout_12|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["yishith_sword_armedman","Yishith Sword Armedman","Yishith Sword Armedmen",#伊希斯剑甲兵
   tf_elf|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_sword_two_handed_a, itm_mogang_zhanshijian, itm_double_deer_fan_shaped_shield, itm_fuhe_guokui, itm_lvzhu_lianjiashan, itm_nailed_iron_leather_boot, itm_fenzhi_lianjiashoutao],
   str_21 | agi_21 | int_9 | cha_24|level(33),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (100) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_8|knows_riding_4|knows_horse_archery_8|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_6|knows_devout_12|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["yishith_sword_dancer","Yishith Sword Dancer","Yishith Sword Dancers",#伊希斯剑舞者
   tf_elf|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_mogang_pohuaijian, itm_lanzong_yuanding_fangmiankui, itm_lvbai_banjiayi, itm_mail_boots, itm_gauntlets],
   str_29 | agi_29 | int_16 | cha_38|level(48),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (280) | wp_archery (100) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_5|knows_athletics_11|knows_riding_8|knows_horse_archery_11|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_6|knows_devout_13|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["molter_knight","Molter Knight","Molter Knights",#蜕生骑士
   tf_elf|tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_lvbai_wenqiqiang, itm_king_deer_fan_shaped_shield, itm_mogang_junyongjian, itm_changmian_lanzong_yuanding_fangmiankui, itm_lvsejianyi_banlianjia, itm_mail_boots, itm_gauntlets, itm_qinlvpijia_ma],
   str_30 | agi_30 | int_16 | cha_40|level(50),wp_one_handed (400) | wp_two_handed (280) | wp_polearm (400) | wp_archery (100) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_5|knows_athletics_11|knows_riding_8|knows_horse_archery_11|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_6|knows_devout_13|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["yishith_crossbowman","Yishith Crossbowman","Yishith Crossbowmen",#伊希斯弩手
   tf_elf|tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_bolts, itm_heavy_crossbow, itm_tab_shield_pavise_c, itm_jianyi_yejianqiang, itm_lianjia_guokui, itm_leather_armor, itm_iron_leather_boot, itm_fenzhi_jiaqiangshoutao],
   str_17 | agi_17 | int_8 | cha_21|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (100) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_7|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_6|knows_devout_12|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["yishith_crossbow_ranger","Yishith Crossbow Ranger","Yishith Crossbow Rangers",#伊希斯弩游侠
   tf_elf|tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_steel_bolts, itm_tab_shield_pavise_d, itm_mogang_changzhuiqiang, itm_oak_corssbow, itm_jiaqiang_guokui2, itm_qingse_lianjiazhaopao, itm_splinted_greaves, itm_fenzhi_huzhishoutao],
   str_24 | agi_24 | int_12 | cha_30|level(43),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (100) | wp_crossbow (350) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_6|knows_devout_13|knows_prisoner_management_4|knows_leadership_7|knows_trade_3,
   molter_elf_face_key_1, molter_elf_face_key_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["molting_failer","Molting Failer","Molting Failers",#未成者
   tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_molting_failer_body, itm_molting_failer_hand, itm_no_head, itm_sword_medieval_a, itm_great_apple],
   str_51 | agi_26 | int_3 | cha_3|level(50),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_15|knows_power_strike_8|knows_athletics_12|knows_riding_4|knows_horse_archery_7|knows_looting_8|knows_tracking_8|knows_spotting_8|knows_study_15,
   yishith_face_middle_1, yishith_face_older_2, 0, 
   0, 0, itm_function_monster, #敌意存在
  ],




#—————————————————————————————————生命之灵树—————————————————————————————————
##
  ["vita_full_elf","Vita Full Elf","Vita Full Elf",#生命之树纯血精灵
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_elf_ornamentation_bow, itm_sergeant_sword, itm_jingling_sanbingjian, itm_blue_breeze_round_shield, itm_xihai_guizumao, itm_westcoast_elf_noble_suit, itm_xihai_pixue, itm_nvshi_shoutao],
   str_12 | agi_30 | int_24 | cha_34|level(20),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (230) | wp_crossbow (200) | wp_throwing (210),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_7|knows_horse_archery_10|knows_looting_3|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_13|knows_devout_14|knows_prisoner_management_3|knows_leadership_5|knows_trade_1,
   vita_elf_face_key_1, vita_elf_face_key_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["yishith_navy_archer","Yishith Navy Archer","Yishith Navy Archers",#伊希斯海军射手
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_elf_woodguard_longbow, itm_yixisi_qingliang_shuangshoujian, itm_jingling_shuyongjian, itm_jingling_shuyongjian, itm_nordic_huscarl_helmet, itm_elf_leather_scale_armor, itm_iron_leather_boot, itm_fenzhi_jiaqiangshoutao],
   str_18 | agi_38 | int_28 | cha_42|level(30),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (330) | wp_crossbow (300) | wp_throwing (310),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_7|knows_shield_8|knows_athletics_11|knows_riding_9|knows_horse_archery_12|knows_looting_6|knows_trainer_6|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   vita_elf_face_key_1, vita_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_seawind_ranger","Yishith Seawind Ranger","Yishith Seawind Ranger",#伊希斯海风游侠
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_qinliang_shuangshoufu, itm_seawind_speaker, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_xihai_wenshikui, itm_yishith_westcoast_chain_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_25 | agi_50 | int_33 | cha_55|level(45),wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (460) | wp_crossbow (440) | wp_throwing (450),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_8|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_12|knows_study_13|knows_devout_14|knows_prisoner_management_6|knows_leadership_10|knows_trade_3,
   vita_elf_face_key_1, vita_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["vita_selected_champion","Vita Selected Champion","Vita Selected Champions",#生命之树神选冠军
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_2,
   [itm_gaojingling_xuejian, itm_eternal_inheritance_bow, itm_qinliang_shuangshoufu, itm_steel_shield, itm_selected_champion_headcrown, itm_selected_champion_windbreaker, itm_elf_valkyrie_boot, itm_mogang_fangxing_bikai],
   str_39 | agi_77 | int_56 | cha_90|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (640) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_9|knows_power_draw_12|knows_weapon_master_15|knows_shield_12|knows_athletics_15|knows_riding_14|knows_horse_archery_15|knows_looting_9|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_14|knows_trade_4,
   vita_elf_face_key_1, vita_elf_face_key_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#灵风游骑团
  ["spiritwind_bowcavalry","Spiritwind Bowcavalry","Spiritwind Bowcavalry",#灵风游骑士
   tf_elf|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_qishi_danshouzhanfu, itm_spiritwind_cavalry_bow, itm_jingling_youxiajian, itm_jingling_youxiajian, itm_changmian_zhumiankui1, itm_spiritwind_light_plate, itm_spiritual_boot, itm_fenzhi_fulianshoutao, itm_leather_armor_spiritual_horse],
   str_28 | agi_59 | int_40 | cha_65|level(55),wp_one_handed (570) | wp_two_handed (570) | wp_polearm (570) | wp_archery (600) | wp_crossbow (570) | wp_throwing (580),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_7|knows_power_draw_10|knows_weapon_master_12|knows_shield_8|knows_athletics_13|knows_riding_11|knows_horse_archery_14|knows_looting_7|knows_trainer_8|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_13|knows_study_14|knows_devout_14|knows_prisoner_management_7|knows_leadership_11|knows_trade_3,
   vita_elf_face_key_1, vita_elf_face_key_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

#伊希斯人类西海自警团
  ["yishith_armed_sailor","Yishith Armed Sailor","Yishith Armed Sailors",#伊希斯武装水手
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_2,
   [itm_wooden_shield, itm_hatchet, itm_sword_viking_1, itm_sword_viking_2_small, itm_lvse_dianchengjia, itm_xihai_pixue],
   str_8 | agi_6 | int_7 | cha_7|level(7),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_looting_1|knows_spotting_1|knows_inventory_management_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_trade_1,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["yishith_boat_guard","Yishith Boat Guard","Yishith Boat Guards",#伊希斯船队护卫
   tf_guarantee_boots|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_nordic_shield, itm_leather_covered_round_shield, itm_fighting_axe, itm_one_handed_war_axe_a, itm_nasal_helmet, itm_yixisirenlei_xiongjia, itm_splinted_leather_greaves, itm_leather_gloves, itm_light_throwing_axes, itm_light_throwing_axes],
   str_15 | agi_13 | int_7 | cha_7|level(20),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_surgery_1|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_1|knows_study_1|knows_devout_3|knows_prisoner_management_1|knows_leadership_1|knows_trade_3,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["vita_shield_axe_guardian","Vita Shield Axe Guardian","Vita Shield Axe Guardians",#生命之都盾斧卫士
   tf_guarantee_boots|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_one_handed_war_axe_b, itm_plate_covered_round_shield, itm_light_throwing_axes, itm_throwing_axes, itm_nordic_fighter_helmet, itm_lvjian_lianjiazhaopao, itm_mail_chausses, itm_scale_gauntlets, itm_sarranid_axe_a],
   str_21 | agi_17 | int_8 | cha_8|level(32),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (270),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_2|knows_horse_archery_6|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_4|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

  ["yishith_recruiting_rider","Yishith Recruiting Rider","Yishith Recruiting Riders",#伊希斯募集骑手
   tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_double_sided_lance, itm_throwing_axes, itm_plate_covered_round_shield, itm_sword_viking_3, itm_guyongbing_tiekui, itm_surcoat_over_mail, itm_mail_chausses, itm_leather_gloves, itm_zase_ma],
   str_21 | agi_16 | int_11 | cha_11|level(30),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_3|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["yishith_sentry_cavalry","Yishith Sentry Cavalry","Yishith Sentry Cavalries",#伊希斯哨戒骑兵
   tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_2,
   [itm_lvbai_wenqiqiang, itm_throwing_axes, itm_steel_shield, itm_lianren_fu, itm_guyongbing_zhongkui, itm_lvbai_banjiayi, itm_iron_greaves, itm_mail_mittens, itm_jinyang_pijia_liema],
   str_28 | agi_23 | int_14 | cha_14|level(45),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (100) | wp_crossbow (100) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_5|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["yishith_throwing_axe_ranger","Yishith Throwing Axe Ranger","Yishith Throwing Axe Rangers",#伊希斯飞斧游侠
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_2,
   [itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_steel_shield, itm_lianren_fu, itm_guyongbing_zhongkui, itm_lvsejianyi_banlianjia, itm_iron_greaves, itm_mail_mittens],
   str_28 | agi_25 | int_14 | cha_14|level(46),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (100) | wp_crossbow (100) | wp_throwing (380),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["yishith_chivalric_knight","Yishith Chivalric Knight","Yishith Chivalric Knights",#伊希斯侠义骑士
   tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_mogang_qiang, itm_tab_shield_heater_cav_b, itm_duangang_youxiajian, itm_rogue_knight_helmet, itm_chivalric_knight_plate, itm_iron_greaves, itm_scale_gauntlets, itm_jinyang_lianjia_pinyuanma, itm_yinsun_lianjia_pingyuanma, itm_jinjiu_lianjia_pingyuanma, itm_ziyi_lianjia_pinyuanma, itm_xunlu_lianjia_pinyuanma],
   str_32 | agi_26 | int_16 | cha_15|level(50),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_8|knows_shield_6|knows_athletics_6|knows_riding_6|knows_horse_archery_9|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_7|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_4|knows_devout_3|knows_prisoner_management_5|knows_leadership_8|knows_trade_7,
   yishith_face_young_1, yishith_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#雪泥商会
  ["snow_trading_company_guard","Snow Trading Company Guard","Snow Trading Company Guards",#雪泥商会护卫
   tf_guarantee_boots|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_2,
   [itm_one_handed_battle_axe_b, itm_ashwood_pike, itm_tab_shield_round_d, itm_nordic_footman_helmet, itm_leather_armor, itm_splinted_leather_greaves, itm_leather_gloves],
   str_17 | agi_13 | int_10 | cha_10|level(25),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (50) | wp_crossbow (50) | wp_throwing (150),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_2|knows_prisoner_management_1|knows_leadership_2|knows_trade_1,
   yishith_face_young_1, yishith_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],


  ["yishith_messenger","Yishith Messenger","Yishith Messengers", #伊希斯信使
   tf_elf|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_2,
   [itm_yixisi_wandao, itm_elf_outrider_bow, itm_jingling_youxiajian, itm_ranger_hood, itm_elf_leaf_scale_armor, itm_female_ranger_leather_boot, itm_fenzhi_pishoutao, itm_silver_mane_steed],
   str_15 | agi_36 | int_25 | cha_38|level(35), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (300) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_7|knows_shield_3|knows_athletics_12|knows_riding_11|knows_horse_archery_11|knows_looting_6|knows_trainer_5|knows_tracking_7|knows_tactics_6|knows_pathfinding_9|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_11|knows_devout_12|knows_prisoner_management_3|knows_leadership_4|knows_trade_1,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["yishith_deserter","Yishith Deserter","Yishith Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_leather_steppe_cap_c,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,yishith_face_young_1, yishith_face_older_2],





##########################################################科鲁托酋长国##########################################################
  ["kouruto_stray_therianthropy", "Kouruto Stray Therianthropy", "Kouruto Stray Therianthropies", #科鲁托离群兽人
   tf_beast_man, 
   0, 0, fac_kingdom_3,
   [],
   str_14 | agi_5 | int_3 | cha_3|level(5), wp_one_handed (5) | wp_two_handed (5) | wp_polearm (5) | wp_archery (5) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_3|knows_power_strike_2|knows_looting_3|knows_devout_1, 
   kouruto_lion_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["kouruto_therianthropy_mercenary", "Kouruto Therianthropy Mercenary", "Kouruto Therianthropies Mercenaries", #科鲁托兽人佣兵
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_kouruto_handmade_sword, itm_sword_khergit_1, itm_khergit_war_helmet, itm_khergit_armor],
   str_20 | agi_7 | int_4 | cha_4|level(15), wp_one_handed (15) | wp_two_handed (15) | wp_polearm (15) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_5|knows_power_strike_4|knows_athletics_1|knows_riding_2|knows_looting_3|knows_tracking_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_lion_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_therianthropy_riding_mercenary", "Kouruto Therianthropy Riding Mercenary", "Kouruto Therianthropies Riding Mercenaries", #科鲁托兽人骑马佣兵
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_khergit_sword_two_handed_a, itm_scimitar_b, itm_sword_khergit_4, itm_vaegir_spiked_helmet, itm_steppe_armor, itm_leather_boots, itm_leather_gloves, itm_steppe_horse],
   str_28 | agi_9 | int_5 | cha_4|level(26), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_weapon_master_1|knows_athletics_2|knows_riding_3|knows_looting_5|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_2, 
   kouruto_lion_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_therianthropy_mercenary_captain", "Kouruto Therianthropy Mercenary Captain", "Kouruto Therianthropy Mercenary Captains", #科鲁托兽人佣兵头领
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_khergit_sword_two_handed_b, itm_kelutuo_duizhangkui, itm_reroupijia, itm_lingjia_xue, itm_lamellar_gauntlets, itm_warhorse_steppe],
   str_36 | agi_11 | int_6 | cha_5|level(38), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_weapon_master_2|knows_athletics_3|knows_riding_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_lion_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],




#—————————————————————————————————图腾同盟—————————————————————————————————
##
#虎族
  ["kouruto_tiger_herdsman", "Kouruto Tiger Herdsman", "Kouruto Tiger Herdsmen", #科鲁托虎族牧民
   tf_beast_man, 
   0, 0, fac_kingdom_3,
   [itm_nomad_vest, itm_sumpter_horse, itm_saddle_horse],
   str_18 | agi_6 | int_4 | cha_4|level(12), wp_one_handed (15) | wp_two_handed (15) | wp_polearm (15) | wp_archery (5) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_4|knows_power_strike_4|knows_athletics_1|knows_riding_1|knows_looting_3|knows_tracking_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_tiger_rider", "Kouruto Tiger Rider", "Kouruto Tiger Riders", #科鲁托虎族骑手
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_shentie_shuangshoufu, itm_kelutuo_qianse_pijia, itm_khergit_leather_boots, itm_steppe_horse],
   str_27 | agi_9 | int_6 | cha_6|level(23), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (5) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_2|knows_weapon_master_1|knows_athletics_2|knows_riding_3|knows_looting_5|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["kouruto_tiger_machete_rider", "Kouruto Tiger Machete Rider", "Kouruto Tiger Machete Riders", #科鲁托虎族刀骑兵
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_khergit_sword_two_handed_a, itm_vaegir_spiked_helmet, itm_sarranid_elite_armor, itm_khergit_leather_boots, itm_steppe_horse],
   str_38 | agi_11 | int_6 | cha_7|level(35), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (5) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_3|knows_weapon_master_2|knows_athletics_3|knows_riding_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_5, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["kouruto_rampant_slaughterer", "Kouruto Rampant Slaughterer", "Kouruto Rampant Slaughterers", #科鲁托狂鬃屠戮者
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_duangang_shourendao, itm_kelutuo_duizhangkui, itm_light_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_lamellar_gauntlets, itm_hualizhajia_ma],
   str_57| agi_13 | int_7 | cha_9|level(50), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (5) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_4|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_9, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["kouruto_tiger_saber", "Kouruto Tiger Saber", "Kouruto Tiger Sabers", #科鲁托虎族剑士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_shentie_shuangshoufu, itm_kelutuo_qianse_pijia, itm_khergit_leather_boots],
   str_25 | agi_10 | int_6 | cha_6|level(21), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (5) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_weapon_master_1|knows_athletics_2|knows_riding_2|knows_looting_5|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_tiger_berserk_saber", "Kouruto Tiger Berserk Saber", "Kouruto Tiger Berserk Sabers", #科鲁托虎族狂剑士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_khergit_sword_two_handed_a, itm_vaegir_spiked_helmet, itm_sarranid_elite_armor, itm_khergit_leather_boots],
   str_35 | agi_12 | int_6 | cha_7|level(32), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (5) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_3|knows_weapon_master_2|knows_athletics_3|knows_riding_3|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_5, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_sword_master", "Kouruto Sword Master", "Kouruto Sword Masters", #科鲁托剑豪
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_duangang_shourendao, itm_kelutuo_duizhangkui, itm_light_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_54 | agi_14 | int_7 | cha_9|level(48), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (5) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_4|knows_shield_1|knows_athletics_5|knows_riding_4|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_9, 
   kouruto_tiger_face_1, kouruto_tiger_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#熊族
  ["kouruto_bear_herdsman", "Kouruto Bear Herdsman", "Kouruto Bear Herdsmen", #科鲁托熊族牧民
   tf_beast_man, 
   0, 0, fac_kingdom_3,
   [itm_maul, itm_club, itm_nomad_vest],
   str_20 | agi_6 | int_4 | cha_4|level(11), wp_one_handed (10) | wp_two_handed (10) | wp_polearm (10) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_5|knows_power_strike_3|knows_shield_1|knows_looting_3|knows_tracking_1|knows_devout_1|knows_prisoner_management_1, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_bear_rider", "Kouruto Bear Rider", "Kouruto Bear Riders", #科鲁托熊族骑手
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_maul, itm_tab_shield_small_round_a, itm_nomad_vest, itm_nomad_boots, itm_steppe_horse, itm_kelutuo_shense_pijia, itm_khergit_guard_boots],
   str_30 | agi_8 | int_5 | cha_5|level(22), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_2|knows_weapon_master_1|knows_shield_2|knows_athletics_1|knows_riding_2|knows_looting_4|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_2, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["kouruto_bear_heavy_cavalry", "Kouruto Bear Heavy Cavalry", "Kouruto Bear Heavy Cavalries", #科鲁托熊族重骑兵
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_tab_shield_small_round_b, itm_sledgehammer, itm_khergit_war_helmet, itm_khergit_elite_armor, itm_khergit_guard_boots, itm_lamellar_gauntlets, itm_warhorse],
   str_40 | agi_10 | int_5 | cha_6|level(34), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_3|knows_weapon_master_1|knows_shield_3|knows_athletics_2|knows_riding_3|knows_looting_4|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["kouruto_ragefist_obliterator", "Kouruto Ragefist Obliterator", "Kouruto Ragefist Obliterators", #科鲁托怒拳碾压者
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_warhammer, itm_kouruto_round_shield, itm_linshi_zhongkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_gauntlets, itm_heisebanlian_ma, itm_zongsebanlian_ma],
   str_60 | agi_11 | int_7 | cha_8|level(49), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_14|knows_power_strike_12|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["kouruto_bear_shieldman", "Kouruto Bear Shieldman", "Kouruto Bear Shieldmen", #科鲁托熊族盾手
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_maul, itm_tab_shield_round_b, itm_nomad_vest, itm_nomad_boots, itm_kelutuo_shense_pijia, itm_khergit_guard_boots],
   str_28 | agi_8 | int_5 | cha_5|level(20), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_8|knows_power_strike_5|knows_power_throw_2|knows_weapon_master_1|knows_shield_3|knows_athletics_1|knows_riding_1|knows_looting_4|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_2, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_bear_tower_shieldman", "Kouruto Bear Tower Shieldman", "Kouruto Bear Tower Shieldmen", #科鲁托熊族塔盾兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_sledgehammer, itm_leather_patterned_broad_shield, itm_khergit_war_helmet, itm_khergit_elite_armor, itm_khergit_guard_boots, itm_lamellar_gauntlets],
   str_38 | agi_10 | int_5 | cha_6|level(31), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_10|knows_power_strike_7|knows_power_throw_3|knows_weapon_master_1|knows_shield_4|knows_athletics_2|knows_riding_2|knows_looting_4|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_earthshaker_guardian", "Kouruto Earthshaker Guardian", "Kouruto Earthshaker Guardians", #科鲁托撼地守护者
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_warhammer, itm_kouruto_tower_shield, itm_linshi_zhongkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_gauntlets],
   str_58 | agi_11 | int_7 | cha_8|level(47), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_14|knows_power_strike_11|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

#狼族
  ["kouruto_wolf_herdsman", "Kouruto Wolf Herdsman", "Kouruto Wolf Herdsmen", #科鲁托狼族牧民
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_nomad_robe, itm_sumpter_horse, itm_nomad_vest, itm_sword_khergit_2, itm_saddle_horse],
   str_15 | agi_9 | int_5 | cha_4|level(10), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (15) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_1|knows_athletics_2|knows_riding_1|knows_horse_archery_1|knows_looting_3|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_wolf_rider", "Kouruto Wolf Rider", "Kouruto Wolf Riders", #科鲁托狼族骑手
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_3, itm_light_lance, itm_double_sided_lance, itm_khergit_war_helmet, itm_nomad_robe, itm_khergit_leather_boots, itm_steppe_horse, itm_sword_khergit_2],
   str_24 | agi_12 | int_8 | cha_6|level(20), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_1|knows_athletics_4|knows_riding_4|knows_horse_archery_2|knows_looting_5|knows_trainer_2|knows_tracking_3|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["kouruto_wolf_lancer", "Kouruto Wolf Lancer", "Kouruto Wolf Lancers", #科鲁托狼族枪骑兵
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_vaegir_lamellar_helmet, itm_lamellar_vest, itm_khergit_leather_boots, itm_leather_gloves, itm_kelutuo_pijia_liema, itm_lance, itm_light_lance, itm_heavy_lance],
   str_35 | agi_14 | int_9 | cha_7|level(32), wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (45) | wp_crossbow (5) | wp_throwing (45),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_3|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["kouruto_bloodclaw_ravager", "Kouruto Bloodclaw Ravager", "Kouruto Bloodclaw Ravagers", #科鲁托血爪突袭者
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_gorgeous_battle_shield, itm_heavy_lance, itm_kouruto_beast_sabre_simple, itm_khergit_guard_helmet, itm_kouruto_elite_heavy_lamellar_armor, itm_khergit_guard_boots, itm_lamellar_gauntlets, itm_shense_banzhajia_caoyuanma, itm_great_lance, itm_heavy_lance, itm_heavy_lance, itm_great_lance, itm_qianse_banzhajia_caoyuanma],
   str_54 | agi_16 | int_10 | cha_7|level(48), wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (65) | wp_crossbow (5) | wp_throwing (65),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["kouruto_wolf_scout", "Kouruto Wolf Scout", "Kouruto Wolf Scouts", #科鲁托狼族斥候
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_3, itm_vaegir_fur_cap, itm_nomad_robe, itm_khergit_leather_boots, itm_steppe_horse, itm_kouruto_bow, itm_sword_khergit_2, itm_khergit_arrows],
   str_22 | agi_13 | int_8 | cha_6|level(18), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (35) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_1|knows_athletics_4|knows_riding_4|knows_horse_archery_2|knows_looting_5|knows_trainer_2|knows_tracking_3|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["kouruto_wolf_ranger", "Kouruto Wolf Ranger", "Kouruto Wolf Rangers", #科鲁托狼族弓骑兵
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_vaegir_lamellar_helmet, itm_lamellar_vest, itm_khergit_leather_boots, itm_leather_gloves, itm_kelutuo_pijia_liema, itm_southern_horn_bow, itm_khergit_arrows],
   str_33 | agi_16 | int_9 | cha_7|level(30), wp_one_handed (55) | wp_two_handed (55) | wp_polearm (55) | wp_archery (55) | wp_crossbow (5) | wp_throwing (55),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_3|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["kouruto_cyclone_marauder", "Kouruto Cyclone Marauder", "Kouruto Cyclone Marauders", #科鲁托旋风劫掠者
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_nanfang_jian, itm_kouruto_beast_sabre_simple, itm_gorgeous_battle_shield, itm_khergit_guard_helmet, itm_kouruto_elite_heavy_lamellar_armor, itm_khergit_guard_boots, itm_lamellar_gauntlets, itm_shense_banzhajia_caoyuanma, itm_southern_horn_bow, itm_qianse_banzhajia_caoyuanma],
   str_51 | agi_18 | int_10 | cha_7|level(44), wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (75) | wp_crossbow (5) | wp_throwing (75),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

#狮族
  ["kouruto_lion_therianthropy", "Kouruto Lion Therianthropy", "Kouruto Lion Therianthropies", #科鲁托狮兽人
   tf_beast_man|tf_guarantee_armor|tf_guarantee_boots, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_2, itm_khergit_armor, itm_hide_boots],
   str_23 | agi_8 | int_5 | cha_5|level(15), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (15) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_5|knows_power_strike_5|knows_weapon_master_1|knows_athletics_2|knows_riding_2|knows_looting_3|knows_tracking_1|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_lion_warrior", "Kouruto Lion Warrior", "Kouruto Lion Warriors", #科鲁托狮战士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_hafted_blade_a, itm_lamellar_armor, itm_khergit_leather_boots, itm_leather_gloves],
   str_32 | agi_10 | int_7 | cha_10|level(30), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (20) | wp_crossbow (5) | wp_throwing (20),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_3|knows_shield_1|knows_athletics_4|knows_riding_4|knows_horse_archery_1|knows_looting_5|knows_trainer_2|knows_tracking_2|knows_tactics_1|knows_prisoner_management_2|knows_leadership_5, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_lion_baatur", "Kouruto Lion Baatur", "Kouruto Lion Baaturs", #科鲁托猛狮八都鲁
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0, 0, fac_kingdom_3,
   [itm_long_bardiche, itm_khergit_cavalry_helmet, itm_linlianfuhe_jia, itm_khergit_leather_boots, itm_leather_gloves, itm_steppe_horse],
   str_45 | agi_13 | int_8 | cha_12|level(42), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_5|knows_riding_6|knows_horse_archery_3|knows_looting_6|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_kheshig", "Kouruto Kheshig", "Kouruto Kheshigs", #科鲁托怯薛
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_mogang_shourendao, itm_beast_king_helmet, itm_kouruto_elite_lamellar_armor, itm_shengtie_banjiaxue, itm_lamellar_gauntlets, itm_charger],
   str_75 | agi_16 | int_10 | cha_3|level(57), wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (35) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_7|knows_power_draw_5|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_8|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_6|knows_leadership_11, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#科鲁托剑斗旅团
  ["kouruto_gladiator","Kouruto Gladiator","Kouruto Gladiators", #科鲁托角斗士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor,
   0, 0, fac_kingdom_3, 
   [itm_duangang_shourendao, itm_khergit_cavalry_helmet, itm_sarranid_elite_armor, itm_khergit_leather_boots],
   str_41 | agi_14 | int_8 | cha_12|level(37), wp_one_handed (20) | wp_two_handed (50) | wp_polearm (50) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),
   knows_ironflesh_9|knows_power_strike_10|knows_power_throw_3|knows_weapon_master_4|knows_shield_1|knows_athletics_4|knows_riding_3|knows_horse_archery_1|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_5, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_sword_fighter","Kouruto Sword Fighter","Kouruto Sword Fighters", #科鲁托剑斗士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0, 0, fac_kingdom_3, 
   [itm_mogang_shourendao, itm_nanfang_lianjiatoukui, itm_kouruto_sword_fighter_lamellar_armor, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_67 | agi_17 | int_11 | cha_17|level(56), wp_one_handed (50) | wp_two_handed (75) | wp_polearm (75) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),
   knows_ironflesh_13|knows_power_strike_14|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_5|knows_shield_2|knows_athletics_7|knows_riding_4|knows_horse_archery_2|knows_looting_5|knows_trainer_5|knows_tracking_4|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_9, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["totem_champion_warrior","Totem Champion Warrior","Totem Champion Warriors", #图腾冠军勇士
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0, 0, fac_kingdom_3, 
   [itm_kouruto_beast_sabre, itm_beast_ancestor_headgear, itm_kouruto_sword_fighter_lamellar_armor, itm_shengtie_banjiaxue, itm_shengtie_banjiabikai, itm_tiesebanlian_ma],
   str_88 | agi_20 | int_18 | cha_30|level(60), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (80) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_7|knows_power_draw_4|knows_weapon_master_9|knows_shield_4|knows_athletics_7|knows_riding_7|knows_horse_archery_4|knows_looting_7|knows_trainer_6|knows_tracking_7|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13, 
   kouruto_lion_face_1, kouruto_lion_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#铁峰守备旅团
  ["kouruto_therianthropy_guardian","Kouruto Therianthropy Guardian","Kouruto Therianthropy Guardians", #科鲁托兽人守备军
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_3, 
   [itm_polehammer, itm_kouruto_round_shield, itm_kelutuo_duizhangkui, itm_strengthen_kouruto_heavy_lamellar_armor, itm_iron_greaves, itm_gauntlets],
   str_52 | agi_10 | int_7 | cha_8|level(40), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_10|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_human_guardian","Kouruto Human Guardian","Kouruto Human Guardians", #科鲁托人类守备军
   tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_3, 
   [itm_sword_khergit_2, itm_nanfang_jichangmao, itm_sword_khergit_3, itm_leather_broad_shield, itm_vaegir_spiked_helmet, itm_lamellar_vest_khergit, itm_steel_leather_boot, itm_lamellar_gauntlets, itm_steppe_crossbow, itm_steel_bolts],
   str_23 | agi_18 | int_12 | cha_10|level(36), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_3|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_7|knows_trainer_3|knows_tracking_5|knows_tactics_3|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_6, 
   kouruto_face_young_1, kouruto_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

#啮铁帮
  ["ironbite_gang_freshman","Ironbite Gang Freshman","Ironbite Gang Freshmen", #啮铁帮新人
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_3, 
   [itm_long_spiked_club, itm_stud_decorated_skin_battle_shield, itm_khergit_war_helmet, itm_khergit_armor, itm_leather_boots, itm_nomad_armor],
   str_28 | agi_8 | int_5 | cha_5|level(20), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_11|knows_power_strike_5|knows_power_throw_2|knows_weapon_master_1|knows_shield_3|knows_athletics_1|knows_riding_1|knows_looting_4|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_2, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["ironbite_gang_veteran","Ironbite Gang Veteran","Ironbite Gang Veterans", #啮铁帮老手
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_3, 
   [itm_sarranid_two_handed_mace_1, itm_maul, itm_long_hafted_knobbed_mace, itm_vaegir_spiked_helmet, itm_lamellar_armor, itm_steel_leather_boot, itm_leather_gloves],
   str_38 | agi_7 | int_5 | cha_6|level(34), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_7|knows_power_throw_3|knows_weapon_master_1|knows_shield_4|knows_athletics_2|knows_riding_2|knows_looting_4|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["metal_devourer_master","Metal Devourer Master","Metal Devourer Masters", #食铁大师
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0, 0, fac_kingdom_3, 
   [itm_polehammer, itm_linshi_zhongkui, itm_linlianfuhe_jia, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_68 | agi_6 | int_7 | cha_8|level(52), wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_15|knows_power_strike_12|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_1|knows_looting_5|knows_trainer_3|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["ferrophaeg_beast","Ferrophaeg Beast","Ferrophaeg Beasts", #炼铁饿兽
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0, 0, fac_kingdom_3, 
   [itm_crushing_hammer, itm_curved_deformed_helmet, itm_zhongxing_zhajia, itm_shengtie_banjiaxue, itm_kongju_bikai],
   str_100 | agi_5 | int_7 | cha_9|level(60), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_15|knows_power_strike_13|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_horse_archery_5|knows_looting_8|knows_trainer_2|knows_study_15|knows_prisoner_management_10|knows_leadership_11, 
   kouruto_bear_face_1, kouruto_bear_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#洪炉监视旅团
  ["furnace_watch_recruit","Furnace Watch Recruit","Furnace Watch Recruits", #洪炉监视者新兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0, 0, fac_kingdom_3, 
   [itm_sword_khergit_2, itm_sword_khergit_1, itm_spike_skin_battle_shield, itm_nomad_robe, itm_leather_boots],
   str_25 | agi_12 | int_8 | cha_6|level(21), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (30) | wp_crossbow (5) | wp_throwing (30),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_1|knows_athletics_4|knows_riding_4|knows_horse_archery_2|knows_looting_5|knows_trainer_2|knows_tracking_5|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["furnace_watch_warrior","Furnace Watch Warrior","Furnace Watch Warriors", #洪炉监视者战士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_3, 
   [itm_war_darts, itm_sword_khergit_4, itm_spike_skin_battle_shield, itm_kelutuo_heikui, itm_kelutuo_xilingjia, itm_leather_boots, itm_lamellar_gauntlets],
   str_36 | agi_14 | int_9 | cha_7|level(33), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (50) | wp_crossbow (5) | wp_throwing (50),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_3|knows_shield_1|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_7|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["furnace_watch_stalker","Furnace Watch Stalker","Furnace Watch Stalkers", #洪炉监视者密探
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_3, 
   [itm_war_darts, itm_kouruto_beast_sabre_simple, itm_spike_skin_battle_shield, itm_kelutuo_heikui, itm_kelutuo_zhajia, itm_black_greaves, itm_gauntlets],
   str_55 | agi_16 | int_10 | cha_7|level(50), wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (70) | wp_crossbow (5) | wp_throwing (70),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_2|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_9|knows_tactics_5|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],

  ["furnace_hunter","Furnace Hunter","Furnace Hunters", #洪炉猎人
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0, 0, fac_kingdom_3, 
   [itm_nanfang_jian, itm_mogang_shourendao, itm_kelutuo_heikui, itm_kelutuo_zhajia, itm_black_greaves, itm_mogang_shalouhushou, itm_tiese_lianjia_caoyuanma, itm_southern_knight_bow],
   str_63 | agi_20 | int_17 | cha_16|level(55), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (20) | wp_throwing (100),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_6|knows_power_draw_7|knows_weapon_master_7|knows_shield_4|knows_athletics_9|knows_riding_9|knows_horse_archery_5|knows_looting_9|knows_trainer_6|knows_tracking_10|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_7|knows_leadership_10|knows_trade_1, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],




#—————————————————————————————————麦汗族—————————————————————————————————
##
#牛族
  ["kouruto_cow_herdsman", "Kouruto Cow Herdsman", "Kouruto Cow Herdsmen", #科鲁托牛族牧民
   tf_beast_man, 
   0, 0, fac_kingdom_3,
   [itm_khergit_armor],
   str_19 | agi_4 | int_3 | cha_3|level(9), wp_one_handed (5) | wp_two_handed (5) | wp_polearm (5) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_3|knows_power_strike_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_2,  
   kouruto_cow_face_1, kouruto_cow_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_cow_axeman", "Kouruto Cow Axeman", "Kouruto Cow Axemen", #科鲁托牛族斧手
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_axe, itm_maopipijia_pijia],
   str_28 | agi_5 | int_3 | cha_3|level(19), wp_one_handed (10) | wp_two_handed (10) | wp_polearm (10) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_7|knows_power_strike_6|knows_weapon_master_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_3|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_cow_face_1, kouruto_cow_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_cow_warrior", "Kouruto Cow Warrior", "Kouruto Cow Warriors", #科鲁托牛族战士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_jianyi_shuangshoufu, itm_leather_steppe_cap_c, itm_maopipijia_linjia, itm_splinted_greaves],
   str_37 | agi_7 | int_4 | cha_4|level(31), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_2|knows_shield_1|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tactics_1|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_devout_4|knows_prisoner_management_2|knows_leadership_2, 
   kouruto_cow_face_1, kouruto_cow_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_ironhorn_ravager", "Kouruto Ironhorn Ravager", "Kouruto Ironhorn Ravager", #科鲁托铁角狂战士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_great_axe, itm_linshi_zhongkui, itm_kelutuo_lianjia, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_54 | agi_9 | int_5 | cha_5|level(45), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_1|knows_array_arrangement_1|knows_memory_1|knows_study_1|knows_devout_5|knows_prisoner_management_3|knows_leadership_3|knows_trade_1, 
   kouruto_cow_face_1, kouruto_cow_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_bloodhoof_axe_reaver", "Kouruto Bloodhoof Axe Reaver", "Kouruto Bloodhoof Axe Reavers", #科鲁托血蹄斧战士
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_sarranid_axe_b, itm_kouruto_round_shield, itm_linshi_zhongkui, itm_kelutuo_lianjia, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_50 | agi_8 | int_5 | cha_5|level(42), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_13|knows_power_strike_11|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_3|knows_shield_4|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_1|knows_array_arrangement_1|knows_memory_1|knows_study_1|knows_devout_5|knows_prisoner_management_3|knows_leadership_3|knows_trade_1, 
   kouruto_cow_face_1, kouruto_cow_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

#羊族
  ["kouruto_sheep_herdsman", "Kouruto Sheep Herdsman", "Kouruto Sheep Herdsmen", #科鲁托羊族牧民
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_rawhide_coat],
   str_14 | agi_5 | int_5 | cha_4|level(8), wp_one_handed (15) | wp_two_handed (15) | wp_polearm (15) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_3|knows_power_strike_2|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1, 
   kouruto_sheep_face_1, kouruto_sheep_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_sheep_light_infantry", "Kouruto Sheep Light Infantry", "Kouruto Sheep Light Infantries", #科鲁托羊族轻兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_nomad_bow, itm_arrows, itm_nomad_vest, itm_hunter_boots],
   str_23 | agi_8 | int_6 | cha_5|level(18), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (25) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_1|knows_shield_3|knows_athletics_2|knows_riding_1|knows_horse_archery_3|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_sheep_face_1, kouruto_sheep_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["kouruto_sheep_skirmisher", "Kouruto Sheep Skirmisher", "Kouruto Sheep Skirmishers", #科鲁托羊族散兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_kouruto_homemade_longbow, itm_khergit_arrows, itm_sword_khergit_3, itm_khergit_helmet, itm_sarranid_cavalry_robe, itm_nomad_boots, itm_leather_gloves],
   str_34 | agi_10 | int_8 | cha_7|level(30), wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (45) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_5|knows_weapon_master_2|knows_shield_5|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_prisoner_management_2|knows_leadership_3, 
   kouruto_sheep_face_1, kouruto_sheep_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["kouruto_stonecliff_guardian", "Kouruto Stonecliff Guardian", "Kouruto Stonecliff Guardians", #科鲁托岩壁戍卫
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_khergit_arrows, itm_long_hafted_spiked_mace, itm_kelutuo_duizhangkui, itm_mamluke_mail, itm_lingjia_xue, itm_leather_gloves, itm_elite_horn_bow],
   str_47 | agi_13 | int_9 | cha_8|level(44), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (65) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_4|knows_power_draw_8|knows_weapon_master_4|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   kouruto_wolf_face_1, kouruto_wolf_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

#鹿族
  ["kouruto_deer_herdsman", "Kouruto Deer Herdsman", "Kouruto Deer Herdsmen", #科鲁托鹿族牧民
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_nomad_armor],
   str_13 | agi_5 | int_5 | cha_4|level(7), wp_one_handed (15) | wp_two_handed (15) | wp_polearm (15) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),
   knows_ironflesh_3|knows_power_strike_2|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1, 
   kouruto_deer_face_1, kouruto_deer_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_deer_swordman", "Kouruto Deer swordman", "Kouruto Deer Swordmen", #科鲁托鹿族佩剑牧民
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_kouruto_handmade_sword, itm_sword_khergit_1, itm_stud_decorated_skin_battle_shield, itm_light_leather, itm_hide_boots],
   str_22 | agi_8 | int_6 | cha_5|level(17), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (15) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_1|knows_shield_3|knows_athletics_2|knows_riding_1|knows_horse_archery_3|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_deer_face_1, kouruto_deer_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_deer_sword_warrior", "Kouruto Deer Sword Warrior", "Kouruto Deer Sword Warrior", #科鲁托鹿族持剑勇士
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_2, itm_stud_decorated_skin_battle_shield, itm_vaegir_spiked_helmet, itm_kelutuo_fujun_zhajia, itm_leather_boots, itm_leather_gloves],
   str_33 | agi_10 | int_8 | cha_7|level(29), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_5|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_prisoner_management_2|knows_leadership_3, 
   kouruto_deer_face_1, kouruto_deer_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_swiftstrike_marirm", "Kouruto Swiftstrike Marirm", "Kouruto Swiftstrike Marirms", #科鲁托游击剑士
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_kouruto_beast_sabre_simple, itm_spike_skin_battle_shield, itm_nanfang_lianjiatoukui, itm_kelutuo_zhajia_pao, itm_lingjia_xue, itm_lamellar_gauntlets],
   str_46 | agi_13 | int_9 | cha_8|level(43), wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (35) | wp_crossbow (5) | wp_throwing (35),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   kouruto_deer_face_1, kouruto_deer_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#兔族
  ["kouruto_rabbit_herdsman", "Kouruto Rabbit Herdsman", "Kouruto Rabbit Herdsmen", #科鲁托兔族牧民
   tf_beast_man|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_stones],
   str_12 | agi_7 | int_5 | cha_5|level(6), wp_one_handed (10) | wp_two_handed (10) | wp_polearm (10) | wp_archery (10) | wp_crossbow (5) | wp_throwing (10),
   knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_athletics_1|knows_horse_archery_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1, 
   kouruto_rabbit_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_rabbit_stone_thrower", "Kouruto Rabbit Stone Thrower", "Kouruto Rabbit Stone Throwers", #科鲁托兔族投石手
   tf_beast_man|tf_guarantee_armor|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_stones, itm_stones, itm_stones, itm_rawhide_coat],
   str_21 | agi_10 | int_6 | cha_5|level(16), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_1|knows_shield_2|knows_athletics_2|knows_riding_1|knows_horse_archery_3|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_rabbit_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["kouruto_rabbit_slingshoter", "Kouruto Rabbit Slingshoter", "Kouruto Rabbit Slingshoters", #科鲁托兔族弹弓手
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_kouruto_handmade_sword, itm_slingshot, itm_slingshot_stones, itm_nomad_cap, itm_steppe_armor, itm_hide_boots],
   str_30 | agi_14 | int_8 | cha_8|level(28), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (50) | wp_crossbow (5) | wp_throwing (50),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_2|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_prisoner_management_2|knows_leadership_3, 
   kouruto_rabbit_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["kouruto_ambulancer", "Kouruto Ambulancer", "Kouruto Ambulancers", #科鲁托伏击者
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_4, itm_slingshot, itm_slingshot_stones, itm_kelutuo_heikui, itm_khergit_elite_armor, itm_lingjia_xue, itm_fenzhi_jiaqiangshoutao],
   str_41 | agi_19 | int_9 | cha_9|level(42), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (80) | wp_crossbow (5) | wp_throwing (80),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_3|knows_prisoner_management_4|knows_leadership_5, 
   kouruto_rabbit_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#炉边萨满联盟
  ["kouruto_novice_shaman", "Kouruto Novice Shaman", "Kouruto Novice Shamans", #科鲁托新手萨满
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_kouruto_handmade_sword, itm_leather_steppe_cap_a, itm_nomad_vest, itm_hunter_boots],
   str_17 | agi_6 | int_5 | cha_4|level(15), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),
   knows_ironflesh_3|knows_power_strike_3|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_devout_3|knows_leadership_1, 
   kouruto_cow_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["kouruto_veteran_shaman", "Kouruto Veteran Shaman", "Kouruto Veteran Shamans", #科鲁托资深萨满
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_bolts, itm_steppe_crossbow, itm_sword_khergit_1, itm_nomad_cap_b, itm_kelutuo_fujun_zhajia, itm_leather_boots, itm_leather_gloves],
   str_29 | agi_8 | int_12 | cha_7|level(27), wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (55) | wp_crossbow (55) | wp_throwing (55),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_2|knows_shield_1|knows_athletics_3|knows_riding_3|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_3|knows_devout_5|knows_prisoner_management_1|knows_leadership_4, 
   kouruto_cow_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["kouruto_ritualist", "Kouruto Ritualist", "Kouruto Ritualists", #科鲁托巫祭
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_steel_bolts, itm_light_crossbow, itm_khergit_sword_two_handed_a, itm_khergit_helmet, itm_red_colored_kouruto_heavy_lamellar_armor, itm_lingjia_xue, itm_leather_gloves, itm_jingzhizhajia_ma],
   str_41 | agi_10 | int_17 | cha_9|level(42), wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_7|knows_study_7|knows_devout_9|knows_prisoner_management_2|knows_leadership_8, 
   kouruto_cow_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["kouruto_furnace_great_ritualist", "Kouruto Furnace Great Ritualist", "Kouruto Furnace Great Ritualists", #科鲁托洪炉大巫
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_heibaiyu_nushi, itm_birch_crossbow, itm_crushing_hammer, itm_linshi_zhongkui, itm_furnace_light_copper_armor, itm_kouruto_copper_boot, itm_lamellar_gauntlets, itm_zongsebanlian_ma],
   str_54 | agi_13 | int_21 | cha_11|level(55), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_looting_4|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_9|knows_study_12|knows_devout_13|knows_prisoner_management_5|knows_leadership_11, 
   kouruto_cow_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_strategic_strength, #战略力量
  ],

  ["furnace_hierophant", "Furnace Hierophant", "Furnace Hierophants", #侍炉祖巫
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_stone_hammer, itm_no_head, itm_furnace_copper_armor, itm_kouruto_copper_boot, itm_lamellar_gauntlets],
   str_70 | agi_18 | int_30 | cha_22|level(60), wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_8|knows_shield_7|knows_athletics_9|knows_riding_8|knows_horse_archery_8|knows_looting_6|knows_trainer_6|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_8|knows_engineer_6|knows_persuasion_8|knows_array_arrangement_6|knows_memory_11|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_13|knows_trade_1, 
   kouruto_cow_face_1, kouruto_rabbit_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],




#—————————————————————————————————金爪子帮—————————————————————————————————
##
#狐族
  ["kouruto_fox_herdsman", "Kouruto Fox Herdsman", "Kouruto Fox Herdsmen", #科鲁托狐族牧民
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_tunic_with_green_cape],
   str_14 | agi_8 | int_7 | cha_4|level(9), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (10) | wp_crossbow (5) | wp_throwing (10),
   knows_ironflesh_3|knows_power_strike_3|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_tracking_1|knows_spotting_1|knows_trade_1, 
   kouruto_fox_face_1, kouruto_fox_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_fox_horseman", "Kouruto Fox Horseman", "Kouruto Fox Horsemen", #科鲁托狐族骑手
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_stud_decorated_skin_battle_shield, itm_kouruto_handmade_sword, itm_leather_jerkin, itm_nomad_boots, itm_sumpter_horse],
   str_23 | agi_11 | int_9 | cha_6|level(19), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_1|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_2|knows_prisoner_management_1|knows_leadership_2|knows_trade_2, 
   kouruto_fox_face_1, kouruto_fox_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["kouruto_fox_blade_rdier", "Kouruto Fox Blade Rdier", "Kouruto Fox Blade Rdiers", #科鲁托狐族刀骑兵
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_spike_skin_battle_shield, itm_sword_khergit_3, itm_khergit_cavalry_helmet, itm_linjiapijian_dingshijia, itm_splinted_leather_greaves, itm_leather_gloves, itm_steppe_horse],
   str_33 | agi_13 | int_12 | cha_9|level(31), wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (40) | wp_crossbow (5) | wp_throwing (40),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_3|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_3|knows_looting_2|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_3, 
   kouruto_fox_face_1, kouruto_fox_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["midul_knight", "Midul Knight", "Midul Knights", #米德骑士
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_beast_ancestor_totem_shield, itm_kouruto_beast_sabre_simple, itm_nanfang_lianjiatoukui, itm_zongse_lianxiongjia, itm_shengtie_banjiaxue, itm_lamellar_gauntlets, itm_tuselianjia_ma],
   str_52 | agi_15 | int_15 | cha_13|level(47), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   kouruto_fox_face_1, kouruto_fox_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#猫族
  ["kouruto_cat_herdsman", "Kouruto Cat Herdsman", "Kouruto Cat Herdsmen", #科鲁托猫族牧民
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_throwing_knives, itm_throwing_knives, itm_red_tunic],
   str_13 | agi_8 | int_7 | cha_4|level(8), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (10) | wp_crossbow (5) | wp_throwing (10),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_tracking_1|knows_spotting_1|knows_trade_1, 
   kouruto_cat_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_cat_hitman", "Kouruto Cat Hitman", "Kouruto Cat Hitmen", #科鲁托猫族打手
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_1, itm_throwing_daggers, itm_throwing_daggers, itm_red_gambeson, itm_hide_boots],
   str_22 | agi_11 | int_9 | cha_6|level(18), wp_one_handed (35) | wp_two_handed (35) | wp_polearm (35) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_1|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_2|knows_prisoner_management_1|knows_leadership_2|knows_trade_2, 
   kouruto_cat_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_cat_killer", "Kouruto Cat Killer", "Kouruto Cat Killer", #科鲁托猫族暗杀者
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_darts, itm_darts, itm_sword_khergit_4, itm_vaegir_spiked_helmet, itm_leather_armor, itm_leather_boots, itm_fenzhi_pishoutao],
   str_32 | agi_13 | int_12 | cha_9|level(30), wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (40) | wp_crossbow (5) | wp_throwing (40),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_3|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_3|knows_looting_2|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_3, 
   kouruto_cat_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],
  ["midul_assassin", "Midul Assassin", "Midul Assassins", #米德刺客
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_war_darts, itm_nanfang_cijian, itm_kelutuo_heikui, itm_heise_lianxiongjia, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao, itm_shense_banzhajia_caoyuanma],
   str_51 | agi_15 | int_15 | cha_13|level(46), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_10|knows_power_draw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   kouruto_cat_face_1, kouruto_cat_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#金爪子商会
  ["kouruto_therianthropy_caravan_guard", "Kouruto Therianthropy Caravan Guard", "Kouruto Therianthropy Caravan Guards", #科鲁托兽人商队护卫
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_double_sided_lance, itm_black_and_white_skoutarion, itm_vaegir_fur_helmet, itm_khergit_guard_armor, itm_splinted_greaves, itm_leather_gloves, itm_steppe_horse],
   str_42 | agi_13 | int_13 | cha_10|level(36), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_3|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_4|knows_looting_4|knows_trainer_1|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_prisoner_management_3|knows_leadership_5|knows_trade_4, 
   kouruto_fox_face_1, kouruto_fox_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

#不死者猎杀旅团
  ["therianthropy_undead_hunter", "Therianthropy Undead Hunter", "Therianthropy Undead Hunters", #兽人猎亡者
   tf_beast_woman|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_silver_plated_sabre, itm_exorcist_battle_shield, itm_papal_believer_chain_hood, itm_lamellar_vest, itm_mail_chausses, itm_lamellar_gauntlets],
   str_43 | agi_14 | int_13 | cha_10|level(38), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (60) | wp_crossbow (5) | wp_throwing (60),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_7|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_4|knows_looting_5|knows_trainer_2|knows_tracking_7|knows_tactics_3|knows_pathfinding_8|knows_spotting_9|knows_inventory_management_1|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_5|knows_devout_3|knows_prisoner_management_2|knows_leadership_5|knows_trade_2, 
   kouruto_cat_woman_face_1, kouruto_cat_woman_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],




#—————————————————————————————————守望派—————————————————————————————————
##
#犬族
  ["kouruto_dog_herdsman", "Kouruto Dog Herdsman", "Kouruto Dog Herdsmen", #科鲁托犬族牧民
   tf_beast_man|tf_guarantee_armor, 
   0, 0, fac_kingdom_3,
   [itm_khergit_armor],
   str_14 | agi_8 | int_5 | cha_4|level(9), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (15) | wp_crossbow (5) | wp_throwing (15),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_1|knows_athletics_2|knows_riding_1|knows_horse_archery_1|knows_looting_3|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_prisoner_management_1|knows_leadership_1, 
   kouruto_dog_face_1, kouruto_dog_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_dog_recuit", "Kouruto Dog Recuit", "Kouruto Dog Recuits", #科鲁托犬族新兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_kingdom_3,
   [itm_wooden_board_shield, itm_boar_spear, itm_leather_steppe_cap_b, itm_khergit_armor, itm_hide_boots],
   str_23 | agi_11 | int_8 | cha_6|level(19), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (25) | wp_crossbow (5) | wp_throwing (25),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_1|knows_athletics_4|knows_riding_4|knows_horse_archery_2|knows_looting_5|knows_trainer_2|knows_tracking_3|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3, 
   kouruto_dog_face_1, kouruto_dog_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_tercio_infantry", "Kouruto Tercio Infantry", "Kouruto Tercio Infantries", #科鲁托战阵步兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_3,
   [itm_sword_khergit_3, itm_leather_broad_shield, itm_vaegir_fur_helmet, itm_lamellar_vest_khergit, itm_splinted_leather_greaves, itm_leather_gloves],
   str_34 | agi_13 | int_9 | cha_7|level(31), wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (45) | wp_crossbow (5) | wp_throwing (45),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_3|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_dog_face_1, kouruto_dog_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_tercio_centurion", "Kouruto Tercio Centurion", "Kouruto Tercio Centurions", #科鲁托战阵百夫长
   tf_beast_man|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_war_darts, itm_lance, itm_kouruto_beast_sabre_simple, itm_kelutuo_duizhangkui, itm_linlianfuhe_jia, itm_lingjia_xue, itm_scale_gauntlets, itm_warhorse_steppe],
   str_51 | agi_15 | int_10 | cha_7|level(47), wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (65) | wp_crossbow (5) | wp_throwing (65),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_3|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_1|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_7, 
   kouruto_dog_face_1, kouruto_dog_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["kouruto_tercio_spearman", "Kouruto Tercio Spearman", "Kouruto Tercio Spearmen", #科鲁托战阵矛兵
   tf_beast_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 
   0, 0, fac_kingdom_3,
   [itm_nanfang_jichangmao, itm_vaegir_lamellar_helmet, itm_lamellar_vest_khergit, itm_splinted_leather_greaves, itm_lamellar_gauntlets],
   str_36 | agi_15 | int_9 | cha_7|level(35), wp_one_handed (65) | wp_two_handed (75) | wp_polearm (65) | wp_archery (45) | wp_crossbow (5) | wp_throwing (45),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_3|knows_shield_2|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_2|knows_leadership_4, 
   kouruto_dog_face_1, kouruto_dog_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

#守望者卫戍旅团
  ["sentinel_bastion_warden","Sentinel Bastion Warden","Sentinel Bastion Wardens", #守望者卫戍骑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_3, 
   [itm_kouruto_tower_shield, itm_nanfang_jian, itm_nanfang_jichangmao, itm_gangshizi_niujiao_dakui3, itm_watcher_knight_lamellar_plate_armor, itm_black_greaves, itm_gauntlets, itm_southern_knight_bow],
   str_33 | agi_30 | int_21 | cha_22|level(50), wp_one_handed (425) | wp_two_handed (425) | wp_polearm (425) | wp_archery (425) | wp_crossbow (425) | wp_throwing (425),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_10|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_6|knows_horse_archery_8|knows_looting_3|knows_trainer_8|knows_tracking_4|knows_tactics_7|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_7|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_7|knows_array_arrangement_6|knows_memory_11|knows_study_9|knows_devout_13|knows_prisoner_management_11|knows_leadership_12|knows_trade_2, 
   kouruto_face_middle_1, kouruto_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["sentinel_servant","Sentinel Servant","Sentinel Servants", #守望者奴仆
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_3, 
   [itm_sword_khergit_4, itm_spike_skin_battle_shield, itm_war_darts, itm_war_darts, itm_vaegir_lamellar_helmet, itm_watcher_sentry_lamellar_armor, itm_nailed_iron_leather_boot, itm_leather_gloves, itm_steppe_horse],
   str_27 | agi_21 | int_15 | cha_14|level(40), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_6|knows_shield_9|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_6|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_4|knows_devout_10|knows_prisoner_management_6|knows_leadership_5|knows_trade_2, 
   kouruto_face_young_1, kouruto_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],




#—————————————————————————————————科鲁托辅助军—————————————————————————————————
##
  ["kouruto_human_settler", "Kourutom Human Settler", "Kouruto Human Settlers", #科鲁托人类定居者
   tf_guarantee_boots|tf_guarantee_armor,
   0, 0, fac_kouruto_auxiliary,
   [itm_kouruto_handmade_desert_sword, itm_kelutuo_pingming_fu, itm_hunter_boots],
   str_8 | agi_6 | int_6 | cha_5|level(5), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (25) | wp_crossbow (25) | wp_throwing (25),
   knows_ironflesh_1|knows_power_throw_1|knows_riding_1|knows_horse_archery_1|knows_looting_1|knows_tracking_1|knows_pathfinding_1|knows_prisoner_management_1|knows_trade_1,
   kouruto_face_younger_1, kouruto_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["kouruto_young_mercenary", "Kourutom Young Mercenary", "Kourutom Young Mercenaries",#科鲁托年轻佣兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0, 0, fac_kouruto_auxiliary,
   [itm_sarranid_leather_armor, itm_kelutuo_shense_pijia, itm_kelutuo_qianse_pijia, itm_leather_gloves, itm_leather_boots, itm_spear, itm_bamboo_spear, itm_war_spear, itm_kouruto_handmade_desert_sword, itm_kouruto_handmade_sword, itm_leather_steppe_cap_b, itm_leather_steppe_cap_c, itm_leather_warrior_cap, itm_wooden_board_shield, itm_darts],
   str_10 | agi_9 | int_6 | cha_6|level(10), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_looting_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_trade_2,
   kouruto_face_young_1, kouruto_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_auxiliary_light_infantry", "Kourutom Auxiliary Light Infantry", "Kouruto Auxiliary Light Infantries", #科鲁托辅军轻步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kouruto_auxiliary,
   [itm_bolts, itm_leather_patterned_broad_shield, itm_nanfang_jichangmao, itm_steppe_crossbow, itm_sarranid_leather_armor, itm_leather_boots],
   str_13 | agi_10 | int_8 | cha_7|level(18), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_2|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   kouruto_face_young_1, kouruto_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["kouruto_auxiliary_rider", "Kourutom Auxiliary Rider", "Kouruto Auxiliary Riders", #科鲁托辅军骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kouruto_auxiliary,
   [itm_khergit_arrows, itm_tab_shield_small_round_b, itm_scimitar_b, itm_khergit_war_helmet, itm_sarranid_mail_shirt, itm_splinted_leather_greaves, itm_leather_gloves, itm_kelutuo_pijia_liema, itm_kouruto_auxiliary_bow],
   str_18 | agi_15 | int_10 | cha_9|level(28), wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (210) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_5|knows_looting_6|knows_trainer_2|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_3|knows_devout_1|knows_prisoner_management_5|knows_leadership_5|knows_trade_5,
   kouruto_face_young_1, kouruto_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_auxiliary_ranger", "Kourutom Auxiliary Ranger", "Kouruto Auxiliary Rangers", #科鲁托辅军游骑兵
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kouruto_auxiliary,
   [itm_nanfang_jian, itm_gorgeous_battle_shield, itm_sword_khergit_4, itm_kelutuo_duizhangkui, itm_kelutuo_zhajia_pao, itm_splinted_greaves, itm_lamellar_gauntlets, itm_linjia_zhaopaozhanma, itm_southern_knight_bow],
   str_25 | agi_23 | int_15 | cha_11|level(40), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (285) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_8|knows_horse_archery_8|knows_looting_8|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_4|knows_devout_1|knows_prisoner_management_8|knows_leadership_9|knows_trade_7,
   kouruto_woman_face_1, kouruto_woman_face_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["kouruto_auxiliary_heavy_rider", "Kourutom Auxiliary Heavy Rider", "Kouruto Auxiliary Heavy Riders", #科鲁托辅军重骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0, 0, fac_kouruto_auxiliary,
   [itm_heavy_lance, itm_kouruto_round_shield, itm_sword_khergit_4, itm_nanfang_lianjiatoukui, itm_kelutuo_lianjia, itm_lingjia_xue, itm_lamellar_gauntlets, itm_linjia_zhaopaozhanma],
   str_24 | agi_21 | int_14 | cha_10|level(38), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (210) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_4|knows_devout_1|knows_prisoner_management_6|knows_leadership_7|knows_trade_6,
   kouruto_face_middle_1, kouruto_face_older_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["kouruto_auxiliary_spearman", "Kourutom Auxiliary Spearman", "Kouruto Auxiliary Spearmen", #科鲁托辅军矛兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
   0, 0, fac_kouruto_auxiliary,
   [itm_nanfang_jichangmao, itm_vaegir_fur_cap, itm_sarranid_leather_armor, itm_leather_boots, itm_lamellar_gauntlets],
   str_16 | agi_12 | int_9 | cha_7|level(22), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (180) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_2|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   kouruto_face_middle_1, kouruto_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["kouruto_auxiliary_longbowman", "Kourutom Auxiliary Longbowman", "Kouruto Auxiliary Longbowmen", #科鲁托辅军长弓手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,
   0, 0, fac_kouruto_auxiliary,
   [itm_nanfang_jian, itm_kouruto_homemade_longbow, itm_tab_shield_small_round_b, itm_nanfang_jichangmao, itm_khergit_war_helmet, itm_sarranid_cavalry_robe, itm_splinted_leather_greaves, itm_leather_gloves],
   str_19 | agi_17 | int_10 | cha_9|level(30), wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (230) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_5|knows_looting_6|knows_trainer_2|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_3|knows_devout_1|knows_prisoner_management_5|knows_leadership_5|knows_trade_5,
   kouruto_face_middle_1, kouruto_face_older_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],


  ["kouruto_messenger","Kouruto Messenger","Kouruto Messengers", #科鲁托信使
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_3,
   [itm_caoyuan_youliejian, itm_kouruto_bow, itm_scimitar, itm_spike_skin_battle_shield, itm_khergit_war_helmet, itm_sarranid_elite_armor, itm_splinted_leather_greaves, itm_lamellar_gauntlets, itm_steppe_horse],
   str_21 | agi_20 | int_15 | cha_10|level(35), wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_6|knows_riding_6|knows_horse_archery_5|knows_looting_6|knows_trainer_4|knows_tracking_7|knows_tactics_3|knows_pathfinding_8|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   kouruto_face_young_1, kouruto_face_older_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["kouruto_deserter","Kouruto Deserter","Kouruto Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_leather_steppe_cap_c,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,kouruto_face_young_1, kouruto_face_older_2],





########################################################乌-迪默-安基亚邦联#######################################################

  ["confederation_serf","Confederation Serf","Confederation Serf", #邦联农奴
   tf_guarantee_armor, 
   0, 0, fac_slavers,
   [itm_hatchet, itm_shirt, itm_burlap_tunic],
   str_8 | agi_6 | int_6 | cha_5|level(5), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (25) | wp_crossbow (25) | wp_throwing (25),
   knows_ironflesh_1|knows_athletics_1|knows_looting_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_3, 
   diemer_face_younger_1, diemer_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_recruits_slave","Confederation Recruits Slave","Confederation Recruits Slave", #邦联奴隶新兵
   tf_guarantee_boots|tf_guarantee_armor,
   0, 0, fac_slavers,
   [itm_hand_axe, itm_beast_skin_round_shield, itm_pitch_fork, itm_nordic_archer_helmet, itm_ragged_outfit, itm_wrapping_boots, itm_rawhide_coat, itm_leather_vest, itm_hunter_boots, itm_boar_spear, itm_slave_rotten_wooden_shield], 
   str_10 | agi_9 | int_7 | cha_6|level(12), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80), 
   knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_2|knows_looting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_3, 
   diemer_face_younger_1, diemer_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_slave_footman","Confederation Slave Footman","Confederation Slave Footman", #邦联奴隶步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 
   0 ,0, fac_slavers,
   [itm_tab_shield_pavise_c, itm_battle_fork, itm_nordic_footman_helmet, itm_hunter_boots, itm_westcoast_iron_ring_cotton_armor, itm_boar_spear],
   str_17 | agi_14 | int_8 | cha_6|level(25), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (150) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_3|knows_shield_3|knows_athletics_4|knows_horse_archery_1|knows_looting_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_3, 
   diemer_face_young_1, diemer_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_slave_perdue","Confederation Slave Perdue","Confederation Slave Perdue", #邦联奴隶敢死军
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
   0, 0, fac_slavers,
   [itm_light_throwing_axes, itm_light_throwing_axes, itm_axe, itm_nordic_fighter_helmet, itm_hide_boots, itm_voulge, itm_westcoast_nailed_leather_armor],
   str_19 | agi_16 | int_9 | cha_6|level(30), wp_one_handed (100) | wp_two_handed (180) | wp_polearm (100) | wp_archery (80) | wp_crossbow (80) | wp_throwing (180),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_5|knows_weapon_master_3|knows_shield_1|knows_athletics_4|knows_horse_archery_1|knows_looting_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_3, 
   diemer_face_young_1, diemer_face_older_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["confederation_serf_warrior","Confederation Serf Warrior","Confederation Serf Warriors", #邦联奴隶战士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_slavers,
   [itm_axe, itm_hatchet, itm_hand_axe, itm_slave_rotten_wooden_shield, itm_nordic_archer_helmet, itm_westcoast_nailed_leather_armor, itm_hunter_boots, itm_hide_boots, itm_wrapping_boots, itm_nomad_boots, itm_scythe, itm_long_pole_machete, itm_military_scythe],
   str_15 | agi_11 | int_8 | cha_6|level(20), wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_weapon_master_1|knows_shield_1|knows_athletics_2|knows_horse_archery_1|knows_trainer_1|knows_tactics_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_3, 
   diemer_face_young_1, diemer_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_serf_gladiator","Confederation Serf Gladiator","Confederation Serf Gladiators", #邦联奴隶斗士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_slavers,
   [itm_one_handed_war_axe_a, itm_tab_shield_pavise_c, itm_flat_head_axe, itm_glaive, itm_spiked_helmet, itm_westcoast_leather_scale_armor, itm_leather_boots, itm_one_handed_battle_axe_a, itm_nordic_footman_helmet, itm_fighting_axe, itm_nordic_fighter_helmet, itm_voulge, itm_splinted_leather_greaves, itm_nomad_boots, itm_tab_shield_round_c, itm_tab_shield_small_round_b],
   str_18 | agi_15 | int_10 | cha_7|level(30), wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_4|knows_riding_1|knows_horse_archery_2|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_1, 
   diemer_face_young_1, diemer_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["meat_puppet","Meat Puppet", "Meat Puppets", #肉傀儡
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0, 0, fac_slavers,
   [itm_silver_winged_great_sword, itm_aquila_relief_shield, itm_banglian_shenniaojian, itm_banglian_shenniaojian, itm_gangpian_wumainkui, itm_lvsejianyi_banlianjia, itm_mail_chausses, itm_mail_mittens, itm_carved_double_edged_axe, itm_hippogriff_recurve_bow],
   str_30 | agi_27 | int_12 | cha_11|level(42), wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (420) | wp_crossbow (420) | wp_throwing (420),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_7|knows_shield_6|knows_athletics_8|knows_riding_4|knows_horse_archery_6|knows_looting_6|knows_trainer_5|knows_tracking_6|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_9, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["confederation_gladiator_champion","Confederation Gladiator Champion","Confederation Gladiator Champions", #邦联角斗冠军
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0, 0, fac_slavers,
   [itm_extra_long_shovel_axe, itm_great_long_bardiche, itm_battle_axe, itm_war_axe, itm_xihai_dingshikui, itm_westcoast_covered_chain_armor_robe, itm_mail_chausses, itm_leather_gloves, itm_long_bardiche],
   str_32 | agi_29 | int_14 | cha_15|level(45), wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (430) | wp_crossbow (430) | wp_throwing (430),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_6|knows_athletics_8|knows_riding_4|knows_horse_archery_6|knows_looting_5|knows_trainer_5|knows_tracking_4|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_2, 
   diemer_face_younger_1, diemer_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],




#—————————————————————————————————黑沼议事会—————————————————————————————————
##
  ["diemer_freeman","Diemer Freeman","Diemer Freeman", #迪默自由民
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
   0,0,fac_kingdom_4,
   [itm_sword_medieval_c_long, itm_sword_medieval_c, itm_sword_medieval_b_small, itm_half_bird_fan_shaped_shield, itm_arming_cap, itm_aketon_green, itm_leather_boots, itm_leather_gloves],
   str_8 | agi_7 | int_8 | cha_8|level(8), wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60), 
   knows_ironflesh_1|knows_power_strike_1|knows_power_draw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_study_1|knows_prisoner_management_2|knows_leadership_1|knows_trade_1, 
   yishith_face_younger_1, yishith_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["diemer_heavy_footman","Diemer Heavy Footman","Diemer Heavy Footman", #迪默重步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_sword, itm_haze_crow_fan_shaped_shield, itm_baotie_toujin, itm_heibai_xiongjia, itm_splinted_leather_greaves, itm_scale_gauntlets],
   str_14 | agi_10 | int_9 | cha_9|level(18), wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130), 
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_3|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_2|knows_trade_1,
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["diemer_warrior","Diemer Warrior","Diemer Warrior", #迪默战士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_long_sword, itm_winged_board_shield, itm_vaegir_noble_helmet, itm_phoenix_chain_armor_short_shirt, itm_mail_chausses, itm_scale_gauntlets],
   str_17 | agi_14 | int_11 | cha_10|level(24), wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130), 
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_3|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_2|knows_prisoner_management_5|knows_leadership_3|knows_trade_2, 
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["diemer_swordman","Diemer Swordman","Diemer Swordmen", #迪默剑斗士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet,
   0,0,fac_kingdom_4,
   [itm_silver_winged_noble_sword, itm_winged_board_shield, itm_vaegir_war_helmet, itm_phoenix_chain_armor, itm_steel_leather_boot, itm_mail_mittens],
   str_21 | agi_16 | int_12 | cha_11|level(30), wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_5|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_4|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_4|knows_study_2|knows_devout_4|knows_prisoner_management_6|knows_leadership_4|knows_trade_3, 
   yishith_face_young_1, yishith_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["marsh_council_guard","Marsh Council Guard","Marsh Council Guards", #暗沼议会守卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_carved_one_handed_axe, itm_silver_winged_great_sword, itm_winged_elliptical_tower_shield, itm_vaegir_mask, itm_phoenix_plate_chain_composite_armor, itm_splinted_greaves, itm_scale_gauntlets],
   str_25 | agi_22 | int_13 | cha_12|level(40), wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_6|knows_shield_7|knows_athletics_5|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_2|knows_devout_4|knows_prisoner_management_7|knows_leadership_5|knows_trade_3, 
   yishith_face_middle_1, yishith_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

  ["diemer_noviciate_cavalory","Diemer Noviciate Cavalory","Diemer Noviciate Cavalory", #迪默见习骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet,
   0,0,fac_kingdom_4,
   [itm_haze_crow_fan_shaped_shield, itm_silver_winged_long_sword, itm_lance, itm_vaegir_noble_helmet, itm_eagle_chain_armor, itm_mail_chausses, itm_scale_gauntlets, itm_huise_ma],
   str_18 | agi_15 | int_12 | cha_11|level(28),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_3|knows_riding_4|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_4|knows_trade_2, 
   yishith_face_middle_1, yishith_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["diemer_hetairoi","Diemer Hetairoi","Diemer Hetairoi", #迪默伙友骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_knight_sword, itm_phoenix_fan_shaped_shield, itm_heavy_lance, itm_hongzong_wumiankui, itm_jinhua_lianjiazhaopao, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_heibaitiaopijia_ma],
   str_23 | agi_20 | int_13 | cha_12|level(38), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (130) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_6|knows_athletics_4|knows_riding_7|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3, 
   yishith_face_middle_1, yishith_face_older_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["diemer_light_footman","Diemer Light Footman","Diemer Light Footman", #迪默轻步兵
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_javelin, itm_carved_mattock_hammer, itm_javelin, itm_leather_cap, itm_huanghei_xiongjia, itm_leather_boots, itm_leather_gloves],
   str_13 | agi_11 | int_9 | cha_9|level(18), wp_one_handed (160) | wp_two_handed (130) | wp_polearm (130) | wp_archery (160) | wp_crossbow (130) | wp_throwing (160), 
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_1|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_2|knows_trade_1, 
   yishith_face_younger_1, yishith_face_young_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["diemer_grenadier","Diemer Grenadier","Diemer Grenadier", #迪默投掷兵
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_simple_carving_axe, itm_throwing_spears, itm_throwing_spears, itm_vaegir_noble_helmet, itm_brown_eagle_chain_armor_robe, itm_iron_leather_boot, itm_leather_gloves],
   str_17 | agi_15 | int_12 | cha_11|level(27), wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (130) | wp_crossbow (130) | wp_throwing (230),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_4|knows_trade_2, 
   yishith_face_younger_1, diemer_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["diemer_guardian","Diemer Guardian","Diemer Guardian", #迪默近卫
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_aquila_relief_shield, itm_jarid, itm_jarid, itm_carved_one_handed_axe, itm_wumiankui, itm_thunderwing_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets],
   str_22 | agi_18 | int_10 | cha_10|level(37), wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (200) | wp_crossbow (200) | wp_throwing (300), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_4|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3,  
   yishith_face_middle_1, yishith_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["diemer_light_cavalry","Diemer Light Cavalry","Diemer Light Cavalry", #迪默轻骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_double_sided_lance, itm_jarid, itm_jarid, itm_carved_one_handed_double_edged_axe, itm_heizong_wumiankui, itm_eagle_flock_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets, itm_huanghiepijia_ma],
   str_21 | agi_18 | int_10 | cha_10|level(36), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (200) | wp_crossbow (200) | wp_throwing (290), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_6|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["diemer_shortbow_archer","Diemer Shortbow Archer","Diemer Shortbow Archer", #迪默短弓手
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_strong_bow, itm_hongyu_sheshoujian, itm_silver_winged_long_sword, itm_crow_hunting_fan_shaped_shield, itm_vaegir_war_helmet, itm_lanse_lianjiazhaopao, itm_mail_chausses, itm_leather_gloves],
   str_17 | agi_16 | int_12 | cha_11|level(28), wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (240) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_2|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_4|knows_trade_2, 
   diemer_face_younger_1, diemer_face_young_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["diemer_heaveybow_marksman","Diemer Heaveybow Marksman","Diemer Heaveybow Marksman", #迪默重弓手
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_banglian_shenniaojian, itm_silver_winged_noble_sword, itm_crow_hunting_fan_shaped_shield, itm_vaegir_mask, itm_lanbai_banjiayi, itm_steel_leather_boot, itm_fenzhi_fulianshoutao, itm_archer_longbow],
   str_22 | agi_21 | int_13 | cha_12|level(38), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (310) | wp_crossbow (130) | wp_throwing (130),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_6|knows_leadership_7|knows_trade_3, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["diemer_young_slaveholder","Diemer Young Slaveholder","Diemer Young Slaveholder", #迪默年轻奴隶主
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_light_lance, itm_phoenix_fan_shaped_shield, itm_silver_winged_noble_sword, itm_steel_mask, itm_silver_plated_breastplate, itm_mail_chausses, itm_leather_gloves, itm_courser],
   str_13 | agi_10 | int_9 | cha_10|level(15), wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (110) | wp_crossbow (110) | wp_throwing (110), 
   knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_2|knows_horse_archery_1|knows_looting_4|knows_persuasion_3|knows_memory_4|knows_study_4|knows_prisoner_management_5|knows_leadership_3|knows_trade_2, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["diemer_knight_retinue","Diemer Knight Retinue","Diemer Knight Retinue", #迪默骑士扈从
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_great_lance, itm_phoenix_fan_shaped_shield, itm_silver_winged_noble_sword, itm_yaunding_wumiankui, itm_shenlan_lianjiazhaopao, itm_splinted_greaves, itm_scale_gauntlets, itm_ziyi_lianjia_pinyuanma],
   str_17 | agi_14 | int_10 | cha_11|level(25), wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160), 
   knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_4|knows_horse_archery_2|knows_looting_6|knows_trainer_2|knows_tracking_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_5|knows_devout_1|knows_prisoner_management_7|knows_leadership_4|knows_trade_3, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["diemer_monster_enslaving_knight","Diemer Monster Enslaving Knight","Diemer Monster Enslaving Knights", #迪默役兽骑士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_carved_double_edged_axe, itm_phoenix_fan_shaped_shield, itm_ellite_lance, itm_shouling_wumiankui, itm_confederation_female_cavalry_armor, itm_marsh_knight_boot, itm_fenzhi_fubanshoutao, itm_great_lizard],
   str_23| agi_19 | int_12 | cha_13|level(40), wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260), 
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_8|knows_horse_archery_6|knows_looting_7|knows_trainer_3|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_5|knows_devout_1|knows_prisoner_management_10|knows_leadership_7|knows_trade_4, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#光瘴学派
  ["optihazation_scholar","Optihazation Scholar","Optihazation Scholars", #光瘴学士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_ellite_lance, itm_silver_winged_noble_sword, itm_aquila_relief_shield, itm_jinshi_toumao, itm_marsh_knight_helmet, itm_optihaze_light_armor, itm_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_armed_great_lizard],
   str_26 | agi_22 | int_28 | cha_18|level(43), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_10|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_4|knows_tactics_6|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_11|knows_study_6|knows_devout_3|knows_prisoner_management_11|knows_leadership_8|knows_trade_4, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["optihazation_adventure_knight","Optihazation Adventure Knight","Optihazation Adventure Knights", #光瘴探险骑士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_medal_sword, itm_aquila_relief_shield, itm_fengniao_jian, itm_optihazation_knight_helmet, itm_optihaze_heavy_armor, itm_valkyrie_boot, itm_fenzhi_fubanshoutao, itm_phoenix_splendid_bow, itm_armed_great_lizard],
   str_33 | agi_29 | int_35 | cha_24|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450), 
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_12|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_8|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_7|knows_devout_4|knows_prisoner_management_13|knows_leadership_9|knows_trade_5, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["diemer_hired_adventurer","Diemer Hired Adventurer","Diemer Hired Adventurers", #迪默受雇冒险者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_steel_bolts, itm_lightweight_winch_crossbow, itm_crow_hunting_fan_shaped_shield, itm_carved_one_handed_double_edged_axe, itm_maoxianzhe_quankui, itm_eagle_chain_armor, itm_splinted_greaves, itm_mail_mittens, itm_carved_one_handed_axe, itm_voulge],
   str_24 | agi_21 | int_18 | cha_14|level(38), wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (300) | wp_crossbow (280) | wp_throwing (280), 
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_7|knows_riding_5|knows_horse_archery_6|knows_looting_7|knows_trainer_4|knows_tracking_8|knows_tactics_4|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_5|knows_surgery_8|knows_first_aid_7|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_7|knows_study_3|knows_devout_3|knows_prisoner_management_7|knows_leadership_5|knows_trade_5, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

#万龛之主
  ["god_raiser_knight","God Raiser Knight","God Raiser Knights", #举神骑士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_phoenix_wand_lance, itm_medal_sword, itm_aquila_relief_shield, itm_black_bustling_helmet, itm_ancient_warrior_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_ancient_warrior_warhorse],
   str_47 | agi_44 | int_45 | cha_70|level(60), wp_one_handed (580) | wp_two_handed (580) | wp_polearm (580) | wp_archery (580) | wp_crossbow (580) | wp_throwing (580), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_8|knows_athletics_10|knows_riding_14|knows_horse_archery_10|knows_looting_9|knows_trainer_7|knows_tracking_8|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_5|knows_surgery_6|knows_first_aid_6|knows_engineer_5|knows_persuasion_12|knows_array_arrangement_5|knows_memory_14|knows_study_15|knows_prisoner_management_15|knows_leadership_11|knows_trade_5, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],
  ["god_raiser_throne","God Raiser Throne","God Raiser Thrones", #举神命主
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_phoenix_wand_lance, itm_medal_sword, itm_aquila_relief_shield, itm_black_bustling_helmet, itm_ancient_hero_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_ancient_warrior_warhorse],
   str_52 | agi_49 | int_50 | cha_90|level(62), wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600), 
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_10|knows_athletics_12|knows_riding_15|knows_horse_archery_12|knows_looting_9|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_9|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_8|knows_engineer_6|knows_persuasion_13|knows_array_arrangement_6|knows_memory_15|knows_study_15|knows_prisoner_management_15|knows_leadership_12|knows_trade_6, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#司奴局
  ["confederation_slave_trainer","Confederation Slave Trainer","Confederation Slave Trainers", #邦联奴隶训练师
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_whip, itm_red_noble_dress, itm_wuzhe_pixue, itm_nvshi_shoutao],
   str_12 | agi_7 | int_9 | cha_10|level(18), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100), 
   knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_2|knows_athletics_1|knows_trainer_2|knows_tactics_1|knows_inventory_management_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_prisoner_management_5|knows_trade_2, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["confederation_slave_dominator","Confederation Slave Dominator","Confederation Slave Dominators", #邦联奴隶调教师
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_light_crossbow, itm_bolts, itm_haze_crow_fan_shaped_shield, itm_lamp_stand_hammer, itm_party_mask, itm_slaveholder_tight_chain_armor, itm_wuzhe_pixue, itm_fenzhi_pishoutao],
   str_18| agi_12 | int_12 | cha_16|level(30), wp_one_handed (220) | wp_two_handed (220) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200), 
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_4|knows_shield_2|knows_athletics_1|knows_riding_3|knows_horse_archery_2|knows_looting_2|knows_trainer_5|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_3|knows_engineer_4|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_9|knows_leadership_3|knows_trade_4, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["confederation_enslavement_warlock","Confederation Enslavement Warlock","Confederation Enslavement Warlocks", #邦联役奴术士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_heibaiyu_nushi, itm_birch_crossbow, itm_phoenix_fan_shaped_shield, itm_jinshi_langtouchui, itm_heizong_wumiankui, itm_confederation_female_cavalry_armor, itm_mail_boots, itm_scale_gauntlets, itm_heibaitiaopijia_ma],
   str_24| agi_16 | int_22 | cha_26|level(42), wp_one_handed (340) | wp_two_handed (340) | wp_polearm (310) | wp_archery (310) | wp_crossbow (310) | wp_throwing (310), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_6|knows_horse_archery_4|knows_looting_4|knows_trainer_8|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_6|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_5|knows_engineer_9|knows_persuasion_6|knows_array_arrangement_3|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_13|knows_leadership_6|knows_trade_5, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#暗沼之花
  ["confederation_new_recruit","Confederation New Recruit","Confederation New Recruits", #邦联新募佣兵
   tf_guarantee_boots|tf_guarantee_armor, 
   0,0,fac_kingdom_4,
   [itm_military_fork, itm_straw_hat, itm_red_tunic, itm_woolen_hose, itm_head_wrappings, itm_wrapping_boots],
   str_9 | agi_7 | int_6 | cha_6|level(8), wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50), 
   knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_looting_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_surgery_1|knows_prisoner_management_2|knows_trade_1, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_hiring_infantry","Confederation Hiring Infantry","Confederation Hiring Infantries", #邦联雇佣步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_simple_black_white_fan_shaped_shield, itm_sword_medieval_b, itm_sword_medieval_c_small, itm_baotie_toujin, itm_red_gambeson, itm_splinted_leather_greaves],
   str_12 | agi_8 | int_6 | cha_6|level(18), wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120), 
   knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_2|knows_shield_1|knows_athletics_2|knows_riding_1|knows_horse_archery_1|knows_looting_3|knows_tactics_1|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_1|knows_trade_2, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["confederation_hiring_spearman","Confederation Hiring Spearman","Confederation Hiring Spearmen", #邦联雇佣长枪兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_tab_shield_pavise_b, itm_citou_qiang, itm_baotie_toujin, itm_red_studded_padded_armor, itm_mail_chausses],
   str_17 | agi_14 | int_9 | cha_8|level(28), wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220), 
   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_3|knows_looting_4|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_2|knows_devout_2|knows_prisoner_management_5|knows_leadership_2|knows_trade_4, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["marsh_flower_dopplesoldner","Marsh Flower Dopplesoldner","Marsh Flower Dopplesoldners", #暗沼之花双薪剑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_sword_two_handed_b, itm_wozhuangkui, itm_heavy_red_breastplate, itm_mail_boots, itm_scale_gauntlets],
   str_21 | agi_18 | int_10 | cha_9|level(38), wp_one_handed (300) | wp_two_handed (340) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300), 
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_6|knows_riding_4|knows_horse_archery_5|knows_looting_5|knows_trainer_4|knows_tracking_4|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_3|knows_devout_3|knows_prisoner_management_8|knows_leadership_4|knows_trade_5, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["marsh_flower_feldweibel","Marsh Flower Feldweibel","Marsh Flower Feldweibels", #暗沼之花军士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_4,
   [itm_sword_two_handed_b, itm_lance, itm_wozhuangkui, itm_heavy_red_breastplate, itm_mail_boots, itm_scale_gauntlets, itm_courser],
   str_19 | agi_15 | int_12 | cha_8|level(34), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280), 
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_6|knows_riding_4|knows_horse_archery_5|knows_looting_5|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_3|knows_devout_3|knows_prisoner_management_8|knows_leadership_7|knows_trade_5, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["marsh_flower_generalobrist","Marsh Flower Generalobrist","Marsh Flower Generalobrists", #暗沼之花上校
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_4,
   [itm_ellite_lance, itm_silver_winged_noble_sword, itm_haze_crow_fan_shaped_shield, itm_shouling_wumiankui, itm_marsh_flower_three_quarter_armour, itm_iron_greaves, itm_gauntlets, itm_yinsun_lianjia_pingyuanma],
   str_25 | agi_20 | int_19 | cha_10|level(45), wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380), 
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_7|knows_looting_7|knows_trainer_6|knows_tracking_6|knows_tactics_8|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_11|knows_leadership_10|knows_trade_8, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["confederation_hiring_conjurer","Confederation Hiring Conjurer","Confederation Hiring Conjurers", #邦联雇佣术士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_sword, itm_wozhuangkui, itm_silver_plated_breastplate, itm_mail_chausses, itm_fenzhi_pishoutao],
   str_18 | agi_14 | int_20 | cha_10|level(30), wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200), 
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_2|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_5|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_2|knows_prisoner_management_7|knows_leadership_5|knows_trade_4, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["marsh_flower_elemental_conjurer","Marsh Flower Elemental Conjurer","Marsh Flower Elemental Conjurers", #暗沼之花元素使
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_noble_sword, itm_haze_crow_fan_shaped_shield, itm_wumiankui, itm_silver_plate_armor, itm_guanze_banjiaxue, itm_yinse_bikai],
   str_23 | agi_18 | int_29 | cha_11|level(40), wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270), 
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_7|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_2|knows_first_aid_2|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_1|knows_memory_9|knows_study_4|knows_devout_4|knows_prisoner_management_9|knows_leadership_7|knows_trade_5, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["marsh_flower_camp_woman","Marsh Flower Camp Woman","Marsh Flower Camp Women", #暗沼之花随营妇女
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_club, itm_hunting_crossbow, itm_bolts, itm_peasant_dress, itm_blue_hose],
   str_10 | agi_9 | int_6 | cha_10|level(15), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (80) | wp_crossbow (100) | wp_throwing (80), 
   knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_1|knows_athletics_1|knows_horse_archery_2|knows_looting_1|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_1|knows_first_aid_1|knows_prisoner_management_1|knows_trade_3, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["marsh_flower_hurenweibel","Marsh Flower Hurenweibel","Marsh Flower Hurenweibels", #暗沼之花女中士
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_bolts, itm_light_crossbow, itm_military_hammer, itm_mail_coif, itm_heavy_red_breastplate, itm_leather_boots, itm_fenzhi_pishoutao],
   str_18 | agi_16 | int_11 | cha_13|level(32), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100), 
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_3|knows_trainer_2|knows_tracking_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_3|knows_inventory_management_7|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_1|knows_prisoner_management_5|knows_leadership_5|knows_trade_4, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],




#—————————————————————————————————乌尔之子女—————————————————————————————————
##
  ["confederation_fishing_serf","Confederation Fishing Serf","Confederation Fishing Serfs", #邦联渔奴
   tf_deep_one_man|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_slavers,
   [itm_chains_full, itm_shirt, itm_knife],
   str_7 | agi_7 | int_6 | cha_5|level(5), wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20), 
   knows_ironflesh_1|knows_weapon_master_1|knows_athletics_1|knows_horse_archery_1|knows_looting_1|knows_pathfinding_1|knows_spotting_1|knows_surgery_1|knows_study_1, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["confederation_deepone_slave","Confederation Deepone Slave","Confederation Deepone Slaves", #邦联鱼人奴兵
   tf_deep_one_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0, 0, fac_slavers,
   [itm_leather_warrior_cap, itm_ragged_outfit, itm_hunter_boots, itm_slave_rotten_wooden_shield, itm_knife],
   str_11 | agi_11 | int_8 | cha_5|level(15), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100), 
   knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_3|knows_shield_1|knows_athletics_2|knows_riding_1|knows_horse_archery_2|knows_looting_3|knows_tracking_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_study_4|knows_devout_2, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_swamp_bandit","Confederation Swamp Bandit","Confederation Swamp Bandits", #邦联沼泽匪兵
   tf_deep_one_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_slavers,
   [itm_nordic_archer_helmet, itm_leather_jerkin, itm_leather_boots, itm_tab_shield_round_b, itm_dagger],
   str_16 | agi_16 | int_9 | cha_5|level(25), wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150), 
   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_6|knows_trainer_1|knows_tracking_6|knows_tactics_1|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_3|knows_persuasion_2|knows_memory_1|knows_study_7|knows_devout_4|knows_prisoner_management_1|knows_leadership_2|knows_trade_1, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["confederation_ship_looter","Confederation Ship Looter","Confederation Ship Looters", #邦联袭船者
   tf_deep_one_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_slavers,
   [itm_nordic_fighter_helmet, itm_westcoast_leather_scale_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_deep_one_knife_shield, itm_deep_one_knife],
   str_23 | agi_23 | int_10 | cha_9|level(34), wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (230), 
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_6|knows_horse_archery_7|knows_looting_9|knows_trainer_3|knows_tracking_7|knows_tactics_3|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_2|knows_study_11|knows_devout_9|knows_prisoner_management_3|knows_leadership_5|knows_trade_2, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

  ["confederation_toxin_dealer","Confederation Toxin Dealer","Confederation Toxin Dealers", #邦联吐毒者
   tf_deep_one_man|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0, 0, fac_slavers,
   [itm_weak_toxin_liquid, itm_weak_toxin_liquid, itm_deep_one_knife, itm_deep_one_knife_shield, itm_skullcap, itm_westcoast_nailed_leather_armor, itm_splinted_leather_greaves, itm_leather_gloves],
   str_23 | agi_23 | int_10 | cha_9|level(36), wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (260), 
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_6|knows_horse_archery_7|knows_looting_9|knows_trainer_3|knows_tracking_7|knows_tactics_3|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_2|knows_study_11|knows_devout_9|knows_prisoner_management_3|knows_leadership_5|knows_trade_2, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["marsh_deepone_freeman","Marsh Deepone Freeman","Marsh Deepone Freemen", #大沼鱼人自由民
   tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_blue_breeze_round_shield, itm_trident_spear, itm_hood_d, itm_blue_gambeson, itm_leather_boots, itm_leather_gloves],
   str_8 | agi_8 | int_7 | cha_7|level(7), wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40), 
   knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_inventory_management_1|knows_study_3|knows_devout_2|knows_prisoner_management_1|knows_leadership_1, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_non_military_personnel #非战斗人员
  ],
  ["marsh_deepone_self_trained_militia","Marsh Deepone Self Trained Militia","Marsh Deepone Self Trained Militias", #大沼鱼人自训民兵
   tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_blue_breeze_round_shield, itm_bend_blade_trident, itm_helmet_with_neckguard, itm_lanse_xiongjia, itm_splinted_leather_greaves, itm_fenzhi_pishoutao],
   str_14 | agi_14 | int_9 | cha_9|level(16), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100), 
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_1|knows_first_aid_1|knows_persuasion_2|knows_memory_1|knows_study_5|knows_devout_4|knows_prisoner_management_2|knows_leadership_4|knows_trade_1, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["marsh_deepone_professional_soldier","Marsh Deepone Professional Soldier","Marsh Deepone Professional Soldiers", #大沼鱼人职业士兵
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_sea_monster_fan_shaped_shield, itm_straight_blade_trident, itm_jiushi_yuandingkui, itm_scale_armor, itm_steel_leather_boot, itm_fenzhi_jiaqiangshoutao],
   str_18 | agi_18 | int_11 | cha_10|level(24), wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160), 
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_4|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_2|knows_study_8|knows_devout_6|knows_prisoner_management_4|knows_leadership_6|knows_trade_3, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["marsh_deepone_warrior","Marsh Deepone Warrior","Marsh Deepone Warriors", #大沼鱼人勇士
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_backhand_sabre, itm_backhand_sabre_shield, itm_yaunding_wumiankui, itm_cormorant_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets],
   str_23 | agi_23 | int_14 | cha_12|level(31), wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240), 
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_7|knows_shield_7|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_5|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_6|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_5|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_3|knows_study_10|knows_devout_8|knows_prisoner_management_6|knows_leadership_9|knows_trade_4, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["marsh_deepone_commander","Marsh Deepone Commander","Marsh Deepone Commanders", #大沼鱼人统领
    tf_deep_one_man|tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_lanwen_qiqiang, itm_pectoral_shield, itm_carved_one_handed_double_edged_axe, itm_yaunding_wumiankui, itm_cormorant_light_plate_chain_composite_armor, itm_mail_boots, itm_fenzhi_huzhishoutao, itm_great_lizard],
   str_27 | agi_27 | int_18 | cha_14|level(40), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300), 
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["dreadmarsh_warrior","Dreadmarsh Warrior","Dreadmarsh Warriors", #噩沼武夫
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_backhand_blade_shield, itm_backhand_blade, itm_yaunding_wumiankui, itm_mail_and_plate, itm_mail_boots, itm_fenzhi_huzhishoutao],
   str_28 | agi_28 | int_18 | cha_14|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330), 
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["marsh_hunter","Marsh Hunter","Marsh Hunters", #大沼猎手
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   0, 0, fac_kingdom_4,
   [itm_blowgun_arrow, itm_blowgun, itm_sea_monster_fan_shaped_shield, itm_straight_blade_trident, itm_jiushi_yuandingkui, itm_scale_armor, itm_steel_leather_boot, itm_fenzhi_jiaqiangshoutao],
   str_18 | agi_18 | int_12 | cha_10|level(27), wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (200) | wp_throwing (160), 
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_4|knows_horse_archery_6|knows_looting_6|knows_trainer_3|knows_tracking_6|knows_tactics_4|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_3|knows_study_8|knows_devout_6|knows_prisoner_management_4|knows_leadership_6|knows_trade_3, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["marsh_venomfin_hunter","Marsh Venomfin Hunter","Marsh Venomfin Hunters", #大沼毒鳍猎手
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   0, 0, fac_kingdom_4,
   [itm_blowgun_arrow, itm_poison_blowgun, itm_backhand_sabre, itm_backhand_sabre_shield, itm_yaunding_wumiankui, itm_cormorant_chain_armor_robe, itm_splinted_greaves, itm_scale_gauntlets],
   str_24 | agi_24 | int_16 | cha_13|level(39), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (320) | wp_throwing (280), 
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_8|knows_shield_7|knows_athletics_9|knows_riding_6|knows_horse_archery_8|knows_looting_7|knows_trainer_5|knows_tracking_6|knows_tactics_9|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_4|knows_study_12|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],

  ["dreadmarsh_knight","Dreadmarsh Knight","Dreadmarsh Knights", #噩沼骑士
    tf_deep_one_man|tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_lanwen_qiqiang, itm_pectoral_shield, itm_carved_double_edged_axe, itm_guizu_wumainkui, itm_lanse_zaoqi_banjia, itm_iron_greaves, itm_gauntlets, itm_great_lizard],
   str_30 | agi_30 | int_20 | cha_17|level(45), wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380), 
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_10|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_7|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_5|knows_study_13|knows_devout_10|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],


#深海恐惧刺客团
  ["deep_dread_assassin","Deep Dread Assassin","Deep Dread Assassins", #深惧刺客
    tf_deep_one_woman|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_ocean_cleaver, itm_rip_current_assassin_helmet, itm_abyss_plate_robe, itm_plate_boots, itm_kongju_bikai, itm_ocean_cleaver_shield],
   str_36 | agi_36 | int_25 | cha_21|level(49), wp_one_handed (450) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400), 
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_8|knows_power_draw_7|knows_weapon_master_12|knows_shield_10|knows_athletics_10|knows_riding_8|knows_horse_archery_10|knows_looting_7|knows_trainer_7|knows_tracking_8|knows_tactics_8|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_5|knows_study_14|knows_devout_11|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_woman_face_1, deep_one_woman_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],
  ["rip_current_blade","Rip Current Blade","Rip Current Blades", #裂流之刃
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_ocean_cleaver, itm_rip_current_assassin_helmet, itm_abyss_plate, itm_plate_boots, itm_kongju_bikai, itm_ocean_cleaver_shield],
   str_41 | agi_41 | int_28 | cha_24|level(55), wp_one_handed (520) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_12|knows_shield_11|knows_athletics_12|knows_riding_9|knows_horse_archery_12|knows_looting_8|knows_trainer_8|knows_tracking_9|knows_tactics_9|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_8|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_7|knows_engineer_5|knows_persuasion_9|knows_array_arrangement_4|knows_memory_6|knows_study_14|knows_devout_12|knows_prisoner_management_9|knows_leadership_12|knows_trade_7, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#深邃封印团
  ["deep_binder_veteran","Deep Binder Veteran","Deep Binder Veterans", #深邃封印老兵
    tf_deep_one_man|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   0, 0, fac_kingdom_4,
   [itm_jarid, itm_ceremonial_axe, itm_jarid, itm_pectoral_shield, itm_lianjia_hubikui, itm_abyss_plate, itm_plate_boots, itm_gauntlets],
   str_32 | agi_32 | int_26 | cha_17|level(46), wp_one_handed (450) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400), 
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_8|knows_power_draw_7|knows_weapon_master_12|knows_shield_10|knows_athletics_10|knows_riding_8|knows_horse_archery_10|knows_looting_7|knows_trainer_7|knows_tracking_8|knows_tactics_8|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_6|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["deep_bishop","Deep Bishop","Deep Bishops", #深邃主教
    tf_deep_one_man|tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, 
   0, 0, fac_kingdom_4,
   [itm_tide_ceremonial_spear, itm_rip_current_assassin_helmet, itm_deep_binder_plate, itm_plate_boots, itm_kongju_bikai, itm_armed_great_lizard],
   str_70 | agi_21 | int_10 | cha_3|level(60), wp_one_handed (390) | wp_two_handed (390) | wp_polearm (390) | wp_archery (390) | wp_crossbow (390) | wp_throwing (390), 
   knows_ironflesh_15|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_11|knows_shield_9|knows_athletics_11|knows_riding_9|knows_horse_archery_6|knows_looting_6|knows_trainer_6|knows_tracking_8|knows_tactics_8|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_6|knows_engineer_4|knows_persuasion_10|knows_array_arrangement_4|knows_memory_7|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_11|knows_trade_6, 
   deep_one_face_1, deep_one_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],




#—————————————————————————————————净世军—————————————————————————————————
##
  ["confederation_armed_faithful","Confederation Armed Faithful","Confederation Armed Faithfuls", #邦联武装教友
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_sword, itm_jianyi_jiantiqiang, itm_simple_papal_fan_shaped_shield, itm_beak_mask, itm_robe, itm_leather_boots],
   str_11 | agi_8 | int_8 | cha_8|level(15), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),
   knows_ironflesh_3|knows_power_strike_2|knows_power_draw_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_trainer_1|knows_tactics_1|knows_persuasion_1|knows_memory_2|knows_study_4|knows_devout_9|knows_prisoner_management_2|knows_leadership_1, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["purifier_recruit","Purifier Recruit","Purifier Recruits", #净世军团新兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_long_sword, itm_carved_mattock_hammer, itm_jiantou_qiang1, itm_purifier_fan_shaped_shield, itm_beak_hood, itm_papal_conscript_cotton_armor, itm_iron_leather_boot, itm_leather_gloves],
   str_16 | agi_12 | int_11 | cha_9|level(23), wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (210) | wp_crossbow (210) | wp_throwing (210),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_5|knows_athletics_3|knows_riding_2|knows_horse_archery_3|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_5|knows_devout_10|knows_prisoner_management_4|knows_leadership_3|knows_trade_2, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["purifier_light_soldier","Purifier Light Soldier","Purifier Light Soldiers", #净世军团轻甲兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_long_sword, itm_carved_one_handed_double_edged_axe, itm_buqiang_jiantiqiang, itm_purifier_fan_shaped_shield, itm_beak_hood, itm_papal_trainee_leather_armor, itm_steel_leather_boot, itm_scale_gauntlets],
   str_22 | agi_16 | int_12 | cha_10|level(30), wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (290) | wp_crossbow (290) | wp_throwing (290),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_7|knows_athletics_4|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_3|knows_devout_11|knows_prisoner_management_6|knows_leadership_4|knows_trade_3, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["purifier_infantry","Purifier Infantry","Purifier Infantries", #净世军团步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_carved_one_handed_double_edged_axe, itm_duyin_zhandouqiang, itm_purifier_eagle_tower_shield, itm_wing_guard_helmet, itm_eagle_flock_chain_armor_robe, itm_splinted_greaves, itm_gauntlets],
   str_24 | agi_20 | int_13 | cha_11|level(37), wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_8|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_12|knows_prisoner_management_7|knows_leadership_5|knows_trade_4, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["purifier_dismounted_knight","Purifier Dismounted Knight","Purifier Dismounted Knight", #净世军步行骑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_carved_double_edged_axe, itm_silver_winged_great_sword, itm_purifier_winged_knight_skoutarion, itm_gorgeous_eagle_helmet, itm_huangbai_banjiayi, itm_iron_greaves, itm_yuanzhi_bikai],
   str_30 | agi_26 | int_16 | cha_14|level(48), wp_one_handed (470) | wp_two_handed (470) | wp_polearm (470) | wp_archery (470) | wp_crossbow (470) | wp_throwing (470),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_8|knows_shield_8|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_4|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_7|knows_devout_12|knows_prisoner_management_9|knows_leadership_6|knows_trade_4, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["purifier_ballistaman","Purifier Ballistaman","Purifier Ballistamen", #净世军团弩炮手
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_graghite_steel_bolts, itm_purifier_eagle_tower_shield, itm_carved_double_edged_axe, itm_tiegu_nu, itm_gorgeous_eagle_helmet, itm_thunderwing_chain_armor_robe, itm_splinted_greaves, itm_gauntlets, itm_asterisk_staff],
   str_28 | agi_25 | int_15 | cha_13|level(45), wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (440) | wp_crossbow (440) | wp_throwing (440),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_9|knows_devout_11|knows_prisoner_management_7|knows_leadership_5|knows_trade_4, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["purifier_pastor","Purifier Pastor","Purifier Pastor", #净世派神官
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_iron_staff, itm_silver_winged_sword, itm_purifier_fan_shaped_shield, itm_beak_dome_hat, itm_friar_robe, itm_leather_boots, itm_leather_gloves],
   str_12 | agi_9 | int_15 | cha_14|level(18),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_6|knows_devout_8|knows_prisoner_management_4|knows_leadership_3|knows_trade_2,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["purifier_combat_pastor","Purifier Combat Pastor","Purifier Combat Pastors", #净世军战斗牧师
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_jiantou_qiang1, itm_purifier_skoutarion, itm_beak_helmet, itm_traveling_friar_cloth, itm_iron_leather_boot, itm_scale_gauntlets],
   str_16 | agi_13 | int_20 | cha_19|level(27),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (175) | wp_crossbow (175) | wp_throwing (175),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_4|knows_horse_archery_6|knows_looting_2|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_7|knows_devout_10|knows_prisoner_management_5|knows_leadership_4|knows_trade_3,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["holy_wing_guard","Holy Wing Guard","Holy Wing Guards", #圣翼侍卫
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_knight_sword, itm_jiaoguo_hei_qizhiqiang, itm_aquila_guard_shield, itm_wing_guard_helmet, itm_thunderwing_chain_armor_robe, itm_mail_chausses, itm_fenzhi_dingshishoutao, itm_mountain_horse],
   str_23 | agi_19 | int_25 | cha_22|level(39),wp_one_handed (370) | wp_two_handed (370) | wp_polearm (370) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_7|knows_athletics_5|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_7|knows_devout_12|knows_prisoner_management_7|knows_leadership_5|knows_trade_3,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["storm_follower","Storm Follower","Storm Followers", #风暴追随者
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_noble_sword, itm_carved_double_edged_axe, itm_aquila_skoutarion, itm_tempestbringer_helmet, itm_huanghei_jiazhong_banjia, itm_iron_greaves, itm_gauntlets, itm_yinsun_lianjia_pingyuanma],
   str_31 | agi_27 | int_30 | cha_28|level(50), wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_9|knows_athletics_6|knows_riding_8|knows_horse_archery_10|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_10|knows_study_7|knows_devout_13|knows_prisoner_management_9|knows_leadership_7|knows_trade_4,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["storm_white_shadow","Storm White Shadow","Storm White Shadows", #风暴白影
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_falcon_sword, itm_silver_plated_sabre, itm_jinshi_touqiang, itm_exorcist_battle_shield, itm_white_beak_helmet, itm_papal_knight_chain_armor, itm_mail_boots, itm_fenzhi_fubanshoutao],
   str_27 | agi_24 | int_30 | cha_26|level(42),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (235) | wp_crossbow (235) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_5|knows_trainer_5|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_9|knows_array_arrangement_3|knows_memory_9|knows_study_8|knows_devout_14|knows_prisoner_management_8|knows_leadership_6|knows_trade_3,
   diemer_face_young_1, diemer_face_middle_2],

#神牙修道军
  ["divinecusp_knight","Divinecusp Knight","Divinecusp Knights", #神牙骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_divinecusp_spear, itm_divine_beak, itm_divinecusp_knight_helmet, itm_spotless_plate, itm_spotless_plate_boot, itm_duangang_shalouhushou, itm_simple_plate_mountanic_horse_iron, itm_iron_eagle_shield],
   str_36 | agi_30 | int_24 | cha_22|level(52), wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_9|knows_shield_9|knows_athletics_7|knows_riding_8|knows_horse_archery_10|knows_looting_6|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_12|knows_study_8|knows_devout_14|knows_prisoner_management_10|knows_leadership_7|knows_trade_4, 
   diemer_face_young_1, diemer_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["divinecusp_knight_captain","Divinecusp Knight Captain","Divinecusp Knight Captains", #神牙骑士长
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_falcon_sword, itm_jinshi_touqiang, itm_divinecusp_spear, itm_divinecusp_knight_helmet, itm_heavy_spotless_plate, itm_spotless_plate_boot, itm_yinse_bikai, itm_iron_eagle_shield, itm_simple_plate_mountanic_horse_iron],
   str_42 | agi_37 | int_29 | cha_27|level(58), wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560), 
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_6|knows_weapon_master_10|knows_shield_10|knows_athletics_8|knows_riding_9|knows_horse_archery_11|knows_looting_7|knows_trainer_7|knows_tracking_5|knows_tactics_7|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_5|knows_memory_13|knows_study_9|knows_devout_15|knows_prisoner_management_11|knows_leadership_8|knows_trade_4, 
   diemer_face_young_1, diemer_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["storm_servant","Storm Servant","Storm Servants", #风暴仆从
   tf_female|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_banglian_shenniaojian, itm_divine_beak, itm_aquila_skoutarion, itm_tempestminion_helmet, itm_confederation_female_cavalry_armor, itm_saintess_boot, itm_fenzhi_huzhishoutao, itm_mountain_horse, itm_phoenix_splendid_bow],
   str_30 | agi_26 | int_17 | cha_14|level(47), wp_one_handed (440) | wp_two_handed (440) | wp_polearm (440) | wp_archery (440) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_8|knows_shield_7|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_5|knows_devout_10|knows_prisoner_management_9|knows_leadership_6|knows_trade_3, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

#鹰圣苦修会
  ["suffering_friar","Suffering Friar","Suffering Friars", #痛楚修士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves, 
   0,0,fac_kingdom_4,
   [itm_simple_carving_axe, itm_friar_robe, itm_victim_leg, itm_victim_hand, itm_whip],
   str_16 | agi_10 | int_12 | cha_11|level(22),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (75) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_3|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_2|knows_array_arrangement_2|knows_memory_4|knows_study_8|knows_devout_14|knows_prisoner_management_3|knows_leadership_1,
   diemer_face_younger_1, diemer_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["agony_priest","Agony Priest","Agony Priests", #苦痛神甫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_silver_winged_great_sword, itm_lianjia_hubikui, itm_papal_black_chain_cotton_armor, itm_mail_chausses, itm_scale_gauntlets],
   str_26 | agi_18 | int_20 | cha_8|level(33),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (185) | wp_archery (185) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_12|knows_devout_15|knows_prisoner_management_6|knows_leadership_3,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["swaybacked_monk","Swaybacked Monk","Swaybacked Monks", #破背僧
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_carved_double_edged_axe, itm_shouling_hubi_wumiankui, itm_swayback_monk_breastplate, itm_mail_boots, itm_gauntlets],
   str_40 | agi_30 | int_33 | cha_6|level(53),wp_one_handed (490) | wp_two_handed (490) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_6|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_8|knows_surgery_8|knows_first_aid_8|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_9|knows_study_14|knows_devout_15|knows_prisoner_management_8|knows_leadership_5, 
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["deceasing_eagle","Deceasing Eagle","Deceasing Eagles", #未死之鹰
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_blue_gliding_eagle_shield, itm_silver_carving_axe, itm_death_eagle_helmet, itm_bloody_eagle_plate, itm_spotless_plate_boot, itm_yinse_bikai],
   str_59 | agi_48 | int_47 | cha_6|level(60),wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_8|knows_athletics_10|knows_riding_7|knows_horse_archery_8|knows_looting_6|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_10|knows_surgery_10|knows_first_aid_10|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_5|knows_memory_11|knows_study_15|knows_devout_15|knows_prisoner_management_11|knows_leadership_7,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],




#—————————————————————————————————食莲人沙龙—————————————————————————————————
##
  ["ankiya_civilized_barbarian","Ankiya Civilized Barbarian","Ankiya Civilized Barbarians", #安基亚开化蛮族
   tf_guarantee_boots|tf_guarantee_armor, 
   0,0,fac_kingdom_4,
   [itm_hatchet, itm_slave_rotten_wooden_shield, itm_rawhide_coat, itm_wrapping_boots],
   str_11 | agi_7 | int_5 | cha_5|level(8), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (25) | wp_crossbow (25) | wp_throwing (25),
   knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_athletics_1|knows_looting_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_devout_2, 
   diemer_face_younger_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["ankiya_recruit","Ankiya Recruit","Ankiya Recruits", #安基亚征召兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_simple_carving_axe, itm_carved_mattock_hammer, itm_half_bird_fan_shaped_shield, itm_nordic_archer_helmet, itm_tribal_warrior_outfit, itm_hide_boots, itm_hunter_boots],
   str_14 | agi_10 | int_6 | cha_6|level(16), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (70) | wp_crossbow (50) | wp_throwing (70),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_athletics_2|knows_riding_1|knows_horse_archery_1|knows_looting_3|knows_tracking_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_3, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["ankiya_mercenary","Ankiya Mercenary","Ankiya Mercenaries", #安基亚佣兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_carved_one_handed_axe, itm_babarian_stone_sword, itm_haze_crow_fan_shaped_shield, itm_vaegir_noble_helmet, itm_pelt_coat, itm_nomad_boots, itm_leather_boots],
   str_18 | agi_14 | int_7 | cha_6|level(25), wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (140) | wp_crossbow (100) | wp_throwing (140),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_horse_archery_2|knows_looting_6|knows_trainer_2|knows_tracking_6|knows_tactics_1|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_persuasion_1|knows_memory_1|knows_devout_3|knows_prisoner_management_1|knows_leadership_2|knows_trade_1, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["ankiya_horseback_mercenary","Ankiya Horseback Mercenary","Ankiya Horseback Mercenaries", #安基亚骑马佣兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_manzu_chui, itm_babarian_stone_sword, itm_carved_knight_axe, itm_haze_crow_fan_shaped_shield, itm_heizong_wumiankui, itm_wailai_manzu_jia, itm_steel_leather_boot, itm_leather_gloves, itm_mountain_horse, itm_shashi_mao],
   str_25 | agi_21 | int_8 | cha_7|level(35), wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (200) | wp_crossbow (170) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_3|knows_shield_3|knows_athletics_6|knows_riding_4|knows_horse_archery_4|knows_looting_7|knows_trainer_4|knows_tracking_7|knows_tactics_3|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_4|knows_persuasion_2|knows_memory_4|knows_devout_4|knows_prisoner_management_3|knows_leadership_3|knows_trade_3, 
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["ankiya_naturalized_noble","Ankiya Naturalized Noble","Ankiya Naturalized Nobles", #安基亚归化贵族
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_babarian_stone_sword, itm_phoenix_fan_shaped_shield, itm_silver_winged_sword, itm_carved_mattock_hammer, itm_leather_noble_gown, itm_woolen_hose, itm_leather_gloves, itm_saddle_horse, itm_manzu_shiqiang],
   str_14 | agi_10 | int_7 | cha_7|level(15), wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (90) | wp_throwing (90),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_3|knows_riding_1|knows_horse_archery_1|knows_looting_3|knows_trainer_1|knows_tracking_3|knows_tactics_1|knows_pathfinding_2|knows_spotting_2|knows_devout_3|knows_prisoner_management_2|knows_leadership_2, 
   diemer_face_younger_1, diemer_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["ankiya_rider","Ankiya Rider","Ankiya Riders", #安基亚骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_shashi_mao, itm_phoenix_fan_shaped_shield, itm_hunting_bow, itm_arrows, itm_vaegir_war_helmet, itm_cormorant_chain_armor_robe, itm_leather_boots, itm_leather_gloves, itm_zase_ma],
   str_18 | agi_15 | int_8 | cha_7|level(28), wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_6|knows_trainer_2|knows_tracking_6|knows_tactics_3|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_1|knows_devout_3|knows_prisoner_management_3|knows_leadership_4|knows_trade_3, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["ankiya_knight","Ankiya Knight","Ankiya Knights", #安基亚骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_carved_knight_axe, itm_phoenix_fan_shaped_shield, itm_strong_bow, itm_bodkin_arrows, itm_guizu_wumainkui, itm_cormorant_light_plate_chain_composite_armor, itm_mail_chausses, itm_leather_gloves, itm_zongse_pijia_liema],
   str_26 | agi_23 | int_9 | cha_7|level(42), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_7|knows_riding_4|knows_horse_archery_5|knows_looting_7|knows_trainer_3|knows_tracking_7|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_4|knows_prisoner_management_5|knows_leadership_4|knows_trade_3, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],




#—————————————————————————————————人类狩猎者—————————————————————————————————
##
  ["confederation_slave_catcher_hitman","Confederation Slave Catcher Hitman","Confederation Slave Catcher Hitmen", #邦联捕奴打手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_iron_staff, itm_padded_coif, itm_ragged_outfit, itm_hide_boots],
   str_10 | agi_8 | int_8 | cha_7|level(13), wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_athletics_1|knows_looting_3|knows_tracking_3|knows_pathfinding_2|knows_spotting_3|knows_prisoner_management_3,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["confederation_slave_catcher_infantry","Confederation Slave Catcher Infantry","Confederation Slave Catcher Infantries", #邦联捕奴步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0,0,fac_kingdom_4,
   [itm_long_hafted_knobbed_mace, itm_segmented_helmet, itm_leather_jerkin, itm_leather_boots],
   str_14 | agi_13 | int_9 | cha_7|level(22),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (150) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_5|knows_trainer_2|knows_tracking_5|knows_tactics_2|knows_pathfinding_2|knows_spotting_4|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_1|knows_first_aid_1|knows_engineer_2|knows_persuasion_1|knows_array_arrangement_1|knows_memory_2|knows_prisoner_management_6|knows_leadership_2|knows_trade_2,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["confederation_slave_catcher_rider","Confederation Slave Catcher Rider","Confederation Slave Catcher Riders", #邦联捕奴骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_long_hafted_knobbed_mace, itm_sarranid_mace_1, itm_half_bird_fan_shaped_shield, itm_vaegir_noble_helmet, itm_duanxiu_lianjiapao, itm_mail_chausses, itm_fenzhi_jiaqiangshoutao, itm_huise_ma],
   str_19 | agi_16 | int_9 | cha_7|level(31), wp_one_handed (220) | wp_two_handed (220) | wp_polearm (230) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_4|knows_looting_7|knows_trainer_4|knows_tracking_7|knows_tactics_4|knows_pathfinding_4|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_3|knows_engineer_4|knows_persuasion_2|knows_array_arrangement_2|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_9|knows_leadership_4|knows_trade_4, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["confederation_human_hunting_cavalry","Confederation Human Hunting Cavalry","Confederation Human Hunting Cavalries", #邦联猎人骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_kingdom_4,
   [itm_polehammer, itm_jinshi_tuntouzhang, itm_half_bird_fan_shaped_shield, itm_hongzong_wumiankui, itm_huisejianyi_banlianjia, itm_mail_boots, itm_mail_mittens, itm_hongbaiyinpijia_ma],
   str_23 | agi_19 | int_10 | cha_8|level(40), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (310) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_8|knows_trainer_5|knows_tracking_8|knows_tactics_5|knows_pathfinding_5|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_6|knows_persuasion_3|knows_array_arrangement_3|knows_memory_5|knows_study_3|knows_devout_4|knows_prisoner_management_11|knows_leadership_6|knows_trade_5, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["venery_slaver","Venery Slaver","Venery Slavers", #狩猎奴从
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_slavers,
   [itm_slave_rotten_wooden_shield, itm_nordic_footman_helmet, itm_westcoast_iron_ring_cotton_armor, itm_splinted_greaves, itm_mail_mittens, itm_silver_mane_steed, itm_jousting_lance],
   str_22 | agi_19 | int_9 | cha_7|level(36), wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_12|knows_horse_archery_9|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_2|knows_devout_1|knows_prisoner_management_4|knows_leadership_4|knows_trade_2, 
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["venery_knight","Venery Knight","Venery Knights", #狩猎骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_kingdom_4,
   [itm_banglian_shenniaojian, itm_crow_hunting_fan_shaped_shield, itm_jinshi_lengtouchui, itm_heijin_qishikui, itm_brilliant_silver_plate_armor, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_ziyi_lianjia_pinyuanma, itm_hippogriff_short_bow],
   str_31 | agi_27 | int_21 | cha_6|level(50), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_8|knows_shield_7|knows_athletics_8|knows_riding_11|knows_horse_archery_9|knows_looting_10|knows_trainer_7|knows_tracking_9|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_6|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_8|knows_persuasion_5|knows_array_arrangement_3|knows_memory_9|knows_study_4|knows_devout_5|knows_prisoner_management_15|knows_leadership_10|knows_trade_6, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],


  ["confederation_messenger","Confederation Messenger","Confederation Messengers", #邦联信使
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_4,
   [itm_silver_winged_sword, itm_jarid, itm_jarid, itm_phoenix_fan_shaped_shield, itm_wumiankui, itm_slaveholder_tight_chain_armor, itm_mail_chausses, itm_mail_mittens, itm_ziyi_lianjia_pinyuanma],
   str_20 | agi_19 | int_16 | cha_11|level(35), wp_one_handed (260) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_6|knows_horse_archery_5|knows_looting_6|knows_trainer_4|knows_tracking_7|knows_tactics_3|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_8|knows_study_3|knows_devout_1|knows_prisoner_management_7|knows_leadership_4|knows_trade_2,
   powell_woman_face_1,powell_woman_face_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["confederation_deserter","Confederation Deserter","Confederation Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_leather_steppe_cap_c,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,diemer_face_young_1, diemer_face_older_2],



#############################################################教皇国##########################################################

#—————————————————————————————————教皇国通用兵种—————————————————————————————————
##
  ["papal_citizen","Papal Citizen","Papal Citizen",#教国平民
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_jiachang_kuotou_qiang, itm_tab_shield_pavise_b, itm_arming_cap, itm_linen_tunic, itm_leather_boots, itm_robe],
   str_6 | agi_4 | int_7 | cha_6|level(3),wp_one_handed (15) | wp_two_handed (15) | wp_polearm (15) | wp_archery (15) | wp_crossbow (15) | wp_throwing (15),
   knows_ironflesh_2|knows_shield_1|knows_horse_archery_1|knows_study_1|knows_devout_6,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["papal_recruit_militia","Papal Recruit Militia","Papal Recruit Militias",#教国征召民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_lengtou_qiang, itm_tab_shield_pavise_c, itm_footman_helmet, itm_papal_conscript_cotton_armor, itm_splinted_leather_greaves, itm_leather_gloves],
   str_12 | agi_10 | int_7 | cha_7|level(15),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (100) | wp_archery (35) | wp_crossbow (35) | wp_throwing (35),
   knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_1|knows_shield_4|knows_athletics_2|knows_riding_1|knows_horse_archery_1|knows_looting_1|knows_tactics_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_devout_7|knows_prisoner_management_1|knows_trade_1,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["papal_recruit_spearman","Papal Recruit Spearman","Papal Recruit Spearmen",#教国征召矛兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_changren_qiang, itm_tab_shield_pavise_d, itm_guard_helmet, itm_papal_refined_cotton_armor, itm_mail_chausses, itm_leather_gloves],
   str_16 | agi_12 | int_9 | cha_8|level(25),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (150) | wp_archery (35) | wp_crossbow (35) | wp_throwing (35),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_7|knows_athletics_3|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_1|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_2|knows_memory_3|knows_study_4|knows_devout_8|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["papal_senior_spearman","Papal Senior Spearman","Papal Senior Spearmen",#教国资深矛兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_awlpike, itm_tab_shield_pavise_d, itm_jiaoguo_sheshoukui, itm_papal_black_chain_cotton_armor, itm_splinted_greaves, itm_scale_gauntlets],
   str_23 | agi_16 | int_10 | cha_9|level(35),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (200) | wp_archery (35) | wp_crossbow (35) | wp_throwing (35),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_9|knows_athletics_4|knows_riding_2|knows_horse_archery_6|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_3|knows_memory_5|knows_study_4|knows_devout_11|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

  ["papal_joint_defense_militia","Papal Joint Defense Militia","Papal Joint Defense Militias",#圣城协防民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_papal_epee, itm_baptism_fan_shaped_shield, itm_mail_coif, itm_padded_cloth, itm_woolen_hose],
   str_12 | agi_10 | int_7 | cha_7|level(15),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (70) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_1|knows_shield_4|knows_athletics_2|knows_riding_1|knows_horse_archery_1|knows_looting_1|knows_tactics_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_devout_7|knows_prisoner_management_1|knows_trade_1,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["holy_city_standing_infantry","Holy City Standing Infantry","Holy City Standing Infantries",#圣城常备步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_silver_plated_sword, itm_baptism_soldier_fan_shaped_shield, itm_wozhuangkui, itm_papal_chest_armor, itm_leather_boots, itm_leather_gloves],
   str_16 | agi_12 | int_9 | cha_8|level(25),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_6|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_looting_2|knows_trainer_1|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_4|knows_study_4|knows_devout_8|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["holy_land_swordsman","Holy Land Swordsman","Holy Land Swordsmen",#圣地剑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_plated_battle_sword, itm_baptism_soldier_fan_shaped_shield, itm_wozhuangkui, itm_mail_with_tunic_white, itm_mail_chausses, itm_scale_gauntlets],
   str_25 | agi_18 | int_17 | cha_16|level(33),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_7|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_3|knows_memory_7|knows_study_4|knows_devout_11|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["church_guard","Church Guard","Church Guards",#教堂守卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_decorated_towers_shield, itm_jinshi_lengtouchui, itm_jiaoguo_tongkui, itm_church_warden_armor, itm_mail_boots, itm_fangxing_bikai],
   str_30 | agi_25 | int_20 | cha_19|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["faith_cavalry","Faith Cavalry","Faith Cavalries",#信义骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_plated_sabre, itm_baptism_knight_fan_shaped_shield, itm_gangshizi_yi_jukui, itm_papal_knight_chain_armor, itm_splinted_greaves, itm_fenzhi_fulianshoutao, itm_jinshizi_ma],
   str_30 | agi_25 | int_20 | cha_19|level(46),wp_one_handed (410) | wp_two_handed (410) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_7|knows_athletics_6|knows_riding_6|knows_horse_archery_8|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["church_fresh_trainee","Papal Fresh Trainee","Papal Fresh Trainees",#教会新手习武者
   tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_jianyi_jiantiqiang, itm_papal_epee, itm_simple_papal_fan_shaped_shield, itm_wozhuangkui, itm_papal_trainee_leather_armor, itm_leather_boots, itm_leather_gloves],
   str_14 | agi_12 | int_12 | cha_12|level(18), wp_one_handed (175) | wp_two_handed (175) | wp_polearm (175) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_3|knows_devout_8|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["church_senior_trainee","Papal Senior Trainee","Papal SeniorTrainees",#教会资深习武者
   tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_jiantou_qiang1, itm_papal_epee, itm_steel_bar_skoutarion, itm_ban_qingbiankui, itm_papal_trainee_heavy_armor, itm_mail_chausses, itm_scale_gauntlets],
   str_18 | agi_15 | int_15 | cha_14|level(27), wp_one_handed (265) | wp_two_handed (265) | wp_polearm (265) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_7|knows_shield_7|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_3|knows_devout_9|knows_prisoner_management_3|knows_leadership_4|knows_trade_2,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["divine_legion_infantry","Divine Legion Infantry","Divine Legion Infantries",#圣教军团步兵
   tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_duyin_duangzhandouqiang, itm_buqiang_jiantiqiang, itm_papal_axe, itm_papal_soldier_tower_shield, itm_hue_qingbiankui, itm_papal_soldier_chain_armor, itm_mail_boots, itm_gauntlets],
   str_26 | agi_21 | int_15 | cha_14|level(39), wp_one_handed (385) | wp_two_handed (265) | wp_polearm (385) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_11|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_3|knows_devout_10|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["divine_legion_rider","Divine Legion Rider","Divine Legion Riders",#圣教军团骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_double_sided_lance, itm_papal_axe, itm_baptism_soldier_fan_shaped_shield, itm_fuhe_guokui, itm_papal_chest_armor, itm_steel_leather_boot, itm_mail_mittens, itm_mountain_horse],
   str_24 | agi_17 | int_16 | cha_15|level(32), wp_one_handed (315) | wp_two_handed (315) | wp_polearm (315) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_9|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_3|knows_devout_11|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["divine_legion_sergeant","Divine Legion Sergeant","Divine Legion Sergeants",#圣教军团士官
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_jiaoguo_hei_qizhiqiang, itm_baptism_knight_fan_shaped_shield, itm_silver_plated_hand_and_half_sword, itm_great_helmet, itm_papal_knight_chain_armor, itm_iron_greaves, itm_gauntlets, itm_papal_chain_armor_mountain_horse],
   str_28 | agi_24 | int_20 | cha_19|level(42), wp_one_handed (415) | wp_two_handed (415) | wp_polearm (415) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_11|knows_athletics_6|knows_riding_7|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_11|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["mission_school_student","Mission School Student","Mission School Students",#教会学校学员
   tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_bolts, itm_crossbow, itm_papal_epee, itm_papal_dagger, itm_theology_student_cloth, itm_woolen_hose, itm_fenzhi_pishoutao],
   str_13 | agi_11 | int_18 | cha_18|level(18),wp_one_handed (150) | wp_two_handed (75) | wp_polearm (150) | wp_archery (75) | wp_crossbow (150) | wp_throwing (75),
   knows_ironflesh_4|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_4|knows_athletics_3|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_8|knows_devout_8|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["church_apprentice_preist","Church Apprentice Priest","Church Apprentice Preist",#教会见习神官
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_bolts, itm_heavy_crossbow, itm_papal_epee, itm_theologian_small_shield, itm_ban_qingbiankui, itm_apprentice_priest_robe, itm_splinted_leather_greaves, itm_fenzhi_jiaqiangshoutao],
   str_17 | agi_14 | int_23 | cha_23|level(27),wp_one_handed (230) | wp_two_handed (125) | wp_polearm (230) | wp_archery (125) | wp_crossbow (230) | wp_throwing (125),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_6|knows_athletics_5|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_8|knows_study_8|knows_devout_9|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["divine_legion_military_chaplain","Divine Legion Military chaplain","Divine Legion Military chaplains",#圣教军团随军神官
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_bolts, itm_birch_crossbow, itm_silver_one_handed_hammer, itm_changmain_qingbiankui, itm_papal_red_light_chain_armor, itm_mail_chausses, itm_fenzhi_huzhishoutao, itm_mountain_horse],
   str_22 | agi_16 | int_27 | cha_25|level(32),wp_one_handed (270) | wp_two_handed (185) | wp_polearm (270) | wp_archery (185) | wp_crossbow (270) | wp_throwing (185),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_8|knows_athletics_6|knows_riding_4|knows_horse_archery_8|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_10|knows_study_8|knows_devout_11|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["divine_legion_combat_pastor","Divine Legion Combat Pastor","Divine Legion Combat Pastors",#圣教军团战斗牧师
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_baiyu_nushi, itm_birch_crossbow, itm_asterisk_staff, itm_deism_skoutarion, itm_jianliang_qingbiankui, itm_sword_pairing_friar_chain_armor, itm_splinted_greaves, itm_fenzhi_dingshishoutao, itm_grey_spiritual_horse, itm_steel_bar_skoutarion],
   str_26 | agi_23 | int_33 | cha_31|level(42),wp_one_handed (380) | wp_two_handed (235) | wp_polearm (380) | wp_archery (235) | wp_crossbow (380) | wp_throwing (235),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_8|knows_shield_11|knows_athletics_6|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_11|knows_study_8|knows_devout_12|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["divine_legion_crossbowman","Divine Legion Crossbowman","Divine Legion Crossbowmen",#圣教军团弩手
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_steel_bolts, itm_oak_corssbow, itm_jiantou_qiang1, itm_papal_soldier_tower_shield, itm_jiaoguo_sheshoukui, itm_papal_red_chain_cotton_armor, itm_mail_chausses, itm_fenzhi_huzhishoutao],
   str_23 | agi_21 | int_25 | cha_22|level(36),wp_one_handed (320) | wp_two_handed (205) | wp_polearm (320) | wp_archery (205) | wp_crossbow (330) | wp_throwing (205),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_7|knows_shield_9|knows_athletics_6|knows_riding_4|knows_horse_archery_8|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_8|knows_study_8|knows_devout_10|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["papal_hunter","Papal Hunter","Papal Hunters",#教国猎人
   tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_practice_arrows_2, itm_hunting_bow, itm_simple_papal_fan_shaped_shield, itm_boar_spear, itm_baotie_toujin, itm_white_tunic, itm_hunter_boots],
   str_10 | agi_9 | int_7 | cha_7|level(10),wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (65) | wp_crossbow (65) | wp_throwing (65),
   knows_ironflesh_2|knows_power_strike_1|knows_power_draw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_looting_1|knows_tracking_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_memory_1|knows_study_1|knows_devout_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["papal_standing_archer","Papal Standing Archer","Papal Standing Archers",#教国常备弓手
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_barbed_arrows, itm_simple_long_bow, itm_simple_papal_fan_shaped_shield, itm_military_fork, itm_norman_helmet, itm_aketon_green, itm_leather_boots, itm_leather_gloves],
   str_14 | agi_13 | int_9 | cha_9|level(20),wp_one_handed (125) | wp_two_handed (125) | wp_polearm (170) | wp_archery (170) | wp_crossbow (125) | wp_throwing (125),
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_6|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   papal_face_young_1, papal_face_old_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["divine_legion_armed_archer","Divine Legion Armed Archer","Divine Legion Armed Archers",#圣教军团武装射手
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_bodkin_arrows, itm_long_bow, itm_steel_bar_skoutarion, itm_battle_fork, itm_jiaoguo_sheshoukui, itm_papal_red_white_light_chain_armor, itm_splinted_leather_greaves, itm_fenzhi_jiaqiangshoutao],
   str_22 | agi_19 | int_14 | cha_14|level(32),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (280) | wp_archery (280) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_power_draw_5|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_3|knows_devout_7|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["papal_devout_noble","Papal Devout Noble","Papal Devout Nobles",#教国虔信贵族
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_spear, itm_simple_papal_fan_shaped_shield, itm_papal_epee, itm_leather_cap, itm_papal_noble_robe, itm_leather_boots, itm_leather_gloves, itm_sumpter_horse],
   str_12 | agi_8 | int_8 | cha_8|level(15),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_4|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_5|knows_devout_7|knows_prisoner_management_2|knows_leadership_4|knows_trade_2,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["divine_legion_trained_recruit","Divine Legion Trained Recruit","Divine Legion Trained Recruits",#圣教军团受训新兵
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_duyin_zhandouqiang, itm_black_white_fan_shaped_shield, itm_papal_axe, itm_guard_helmet, itm_papal_chest_armor, itm_iron_leather_boot, itm_scale_gauntlets],
   str_16 | agi_14 | int_13 | cha_13|level(25),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_5|knows_horse_archery_6|knows_looting_2|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_3|knows_devout_8|knows_prisoner_management_3|knows_leadership_5|knows_trade_2,
   papal_face_young_1, papal_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],




#——————————————————————————————————圣廷—————————————————————————————————
##
  ["blesruth_tzaddiq","Blesruth Tzaddiq","Blesruth Tzaddiqs", #樊加鲁斯义人
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_asterisk_staff, itm_silver_great_sowrd, itm_jiaoguo_zhongkui, itm_armed_priest_plate, itm_iron_greaves, itm_gauntlets, itm_papal_holy_cavalry_shield, itm_simple_plate_mountanic_horse_luxurious],
   str_36 | agi_30 | int_25 | cha_25|level(52),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_7|knows_athletics_6|knows_riding_7|knows_horse_archery_8|knows_looting_4|knows_trainer_8|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_12|knows_study_11|knows_devout_15|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["holy_see_bedrock","Holy See Bedrock","Holy See Bedrocks", #圣座基岩
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_steel_asterisk_staff, itm_gangshizi_yi_dakui, itm_heavy_temple_guardian_plate, itm_guanze_banjiaxue, itm_yuanzhi_bikai, itm_patron_tower_shield],
   str_37 | agi_31 | int_23 | cha_23|level(53),wp_one_handed (530) | wp_two_handed (530) | wp_polearm (530) | wp_archery (530) | wp_crossbow (530) | wp_throwing (530),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_12|knows_athletics_8|knows_riding_6|knows_horse_archery_8|knows_looting_4|knows_trainer_8|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_11|knows_study_11|knows_devout_14|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["cardinal_guard","Cardinal Guard","Cardinal Guards", #枢机近卫
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_touguan_toumao, itm_touguan_toumao, itm_silver_plated_sabre, itm_baptism_noble_fan_shaped_shield, itm_gangshizi_dakui, itm_baipao_banlian, itm_mail_boots, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse],
   str_33 | agi_31 | int_23 | cha_23|level(50),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (150) | wp_crossbow (150) | wp_throwing (330),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_5|knows_weapon_master_10|knows_shield_11|knows_athletics_7|knows_riding_5|knows_horse_archery_8|knows_looting_4|knows_trainer_8|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_10|knows_study_11|knows_devout_13|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["great_sword_church_guard","Great Sowrd Church Guard","Great Sowrd Church Guards",#大剑教堂守卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_jiaoguo_tongkui, itm_church_warden_armor, itm_mail_boots, itm_fangxing_bikai, itm_silver_extra_great_sowrd],
   str_31 | agi_25 | int_20 | cha_19|level(47),wp_one_handed (400) | wp_two_handed (430) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#圣骑士团
  ["holy_knight","Holy Knight","Holy Knights",#圣骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_paladin_armor, itm_palatin_warhorse, itm_paladin_halo_helmet, itm_paladin_shield, itm_paladin_sword, itm_zhongxing_banjiaxue, itm_huali_shalouhushou, itm_holy_selected_lance],
   str_63 | agi_58 | int_47 | cha_57|level(62),wp_one_handed (620) | wp_two_handed (620) | wp_polearm (620) | wp_archery (620) | wp_crossbow (620) | wp_throwing (620),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_13|knows_shield_15|knows_athletics_12|knows_riding_13|knows_horse_archery_13|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_9|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_8|knows_persuasion_10|knows_array_arrangement_8|knows_memory_15|knows_study_14|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_6,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

  ["holy_knight_aide","Holy Knight Aide","Holy Knight Aides", #圣骑士侍从
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_paladin_aide_armor, itm_papal_holy_cavalry_shield, itm_veteran_chain_armor_mountain_horse, itm_baptized_demon_hunting_sword, itm_shengeqishi_fumiankui, itm_yuanzhi_bikai, itm_papal_iron_boot, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_42 | agi_38 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_14|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_10|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],

#圣誓剑勇团
  ["godward_swordman","Godward Swordman","Godward Swordmen",#圣誓剑士
   tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_silver_plated_hand_and_half_sword, itm_papal_blue_skoutarion, itm_mao_guokui, itm_well_painted_papal_chain_armor, itm_steel_leather_boot, itm_scale_gauntlets],
   str_25 | agi_18 | int_17 | cha_18|level(34),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_8|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_7|knows_study_6|knows_devout_12|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   papal_face_young_1, papal_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["godward_great_swordman","Godward Great Swordman","Godward Great Swordmen",#圣誓大剑师
   tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_papal_hand_and_half_sword, itm_papal_blue_skoutarion, itm_winged_great_helmet, itm_godward_plate_chain_composite_armor, itm_iron_greaves, itm_yuanzhi_bikai],
   str_33 | agi_28 | int_30 | cha_20|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_7|knows_athletics_7|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

#宗座骑士团
  ["pontiff_knight","Pontiff Knight","Pontiff Knights", #宗座骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_plated_battle_sword, itm_knight_black_white_fan_shaped_shield, itm_baiwen_qiqiang, itm_jiushi_yuandingkui, itm_pontifical_knight_chain_armor, itm_guanze_banjiaxue, itm_gauntlets, itm_papal_chain_armor_mountain_horse],
   str_30 | agi_26 | int_17 | cha_15|level(47),wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_7|knows_athletics_5|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_6|knows_trade_4, 
   papal_face_young_1, papal_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["marten_honor_guard","Marten Honor Guard","Marten Honor Guards", #马顿仪仗队
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_steel_asterisk_staff, itm_jiushi_yuandingkui, itm_huijing_qingbanlianfuhe_jia, itm_guanze_banjiaxue, itm_fenzhi_fulianshoutao],
   str_30 | agi_26 | int_17 | cha_15|level(47),wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_6|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_6|knows_trade_4, 
   papal_face_young_1, papal_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

#永眠回廊
  ["eternal_rest_warden","Eternal Rest Warden","Eternal Rest Wardens", #永眠巡守
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_throwing_spears, itm_papal_axe, itm_jarid, itm_verification_fan_shaped_shield, itm_segmented_helmet, itm_papal_black_chain_cotton_armor, itm_leather_boots, itm_fenzhi_jiaqiangshoutao],
   str_23 | agi_17 | int_16 | cha_15|level(30),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (150) | wp_crossbow (150) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_7|knows_shield_8|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_5|knows_memory_6|knows_study_3|knows_devout_13|knows_prisoner_management_4|knows_leadership_5|knows_trade_3, 
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["coffin_warden","Coffin Warden","Coffin Wardens", #圣棺守护者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_papal_double_blade_axe, itm_patron_tower_shield, itm_gangshizi_niujiao_dakui2, itm_coffin_watcher_armor, itm_mail_boots, itm_gauntlets],
   str_38 | agi_30 | int_23 | cha_23|level(53),wp_one_handed (510) | wp_two_handed (510) | wp_polearm (510) | wp_archery (150) | wp_crossbow (150) | wp_throwing (200),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_10|knows_shield_8|knows_athletics_8|knows_riding_6|knows_horse_archery_9|knows_looting_4|knows_trainer_5|knows_tracking_5|knows_tactics_6|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_11|knows_study_9|knows_devout_13|knows_prisoner_management_5|knows_leadership_7|knows_trade_3, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["coffin_monitor","Coffin Monitor","Coffin Monitors", #圣棺监视者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_jinshi_touqiang, itm_asterisk_staff, itm_jinshi_touqiang, itm_exorcist_skoutarion, itm_papal_chain_hood, itm_coffin_watcher_light_armor, itm_mail_boots, itm_gauntlets],
   str_37 | agi_31 | int_23 | cha_23|level(53),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (150) | wp_crossbow (150) | wp_throwing (330),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_8|knows_power_draw_5|knows_weapon_master_10|knows_shield_8|knows_athletics_8|knows_riding_6|knows_horse_archery_9|knows_looting_4|knows_trainer_5|knows_tracking_5|knows_tactics_6|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_11|knows_study_9|knows_devout_13|knows_prisoner_management_5|knows_leadership_7|knows_trade_3, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["crazy_coffin_warden","Crazy Coffin Warden","Crazy Coffin Wardens", #发狂圣棺守护者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_steel_asterisk_staff, itm_jiaoguo_zhongkui, itm_coffin_watcher_armor, itm_mail_boots, itm_gauntlets],
   str_50 | agi_37 | int_23 | cha_3|level(58),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (150) | wp_crossbow (150) | wp_throwing (200),
   knows_ironflesh_12|knows_power_strike_12|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_8|knows_athletics_10|knows_riding_6|knows_horse_archery_5|knows_looting_6|knows_tracking_6|knows_pathfinding_6|knows_spotting_6|knows_persuasion_7|knows_memory_11|knows_study_15|knows_devout_15, 
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["holy_foolishness","Holy Foolishness","Holy Foolishness", #圣愚人
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_zhujian_xinzhang, itm_papal_knight_cape, itm_hymn_knight_plate_robeless, itm_mail_boots, itm_yuanzhi_bikai],
   str_45 | agi_40 | int_93 | cha_3|level(60),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_9|knows_power_draw_7|knows_weapon_master_9|knows_shield_9|knows_athletics_9|knows_riding_9|knows_horse_archery_9|knows_engineer_10|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_15, 
   papal_face_young_1, papal_face_old_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#弓圣遗泽射手团
  ["holy_city_sentry","holy_city_sentry","Holy City Sentries", #圣城哨兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_hongyu_sheshoujian, itm_archer_longbow, itm_jiantou_qiang1, itm_papal_blue_skoutarion, itm_jiaoguo_sheshoukui, itm_papal_red_white_light_chain_armor, itm_mail_chausses, itm_mail_mittens],
   str_23 | agi_19 | int_14 | cha_14|level(35),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (310) | wp_archery (310) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_2|knows_power_draw_6|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_6|knows_looting_3|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_3|knows_devout_7|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["papal_elite_archer","Papal Elite Archer","Papal Elite Archers", #教国精锐射手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_noble_hunting_arrow, itm_strengthen_archer_longbow, itm_buqiang_jiantiqiang, itm_papal_blue_skoutarion, itm_jiaoguo_sheshoukui, itm_papal_knight_strengthen_chain_armor, itm_mail_boots, itm_gauntlets],
   str_28 | agi_24 | int_16 | cha_15|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (380) | wp_archery (380) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_7|knows_weapon_master_6|knows_shield_7|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_4|knows_trainer_4|knows_tracking_5|knows_tactics_4|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_7|knows_study_4|knows_devout_9|knows_prisoner_management_4|knows_leadership_5|knows_trade_4, 
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],



#——————————————————————————————————证信宗—————————————————————————————————
##
  ["civilian_exorcist","Civilian Exorcist","Civilian Exorcists",#平民驱魔人
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_throwing_knives, itm_silver_plated_sword, itm_exorcist_battle_shield, itm_throwing_knives, itm_papal_refined_cotton_armor, itm_leather_boots],
   str_13 | agi_12 | int_11 | cha_10|level(18),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_3|knows_looting_1|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_6|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   papal_face_younger_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["exorcist_mercenary","Exorcist Mercenary","Exorcist Mercenaries",#猎魔佣兵
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_throwing_daggers, itm_silver_plated_battle_sword, itm_verification_fan_shaped_shield, itm_throwing_daggers, itm_papal_hood, itm_exorcist_leather_armor, itm_iron_leather_boot, itm_fenzhi_pishoutao],
   str_17 | agi_15 | int_14 | cha_13|level(27),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (230),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_7|knows_prisoner_management_2|knows_leadership_4|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["employed_demon_slayer","Employed Demon Slayer","Employed Demon Slayers",#受雇伐魔师
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_throwing_daggers, itm_silver_plated_exorcist_sword, itm_exorcist_kite_shield, itm_jinshi_feidao, itm_papal_chain_hood, itm_exorcist_strengthening_chest_armor, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_26 | agi_24 | int_18 | cha_17|level(40),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_6|knows_shield_8|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_4|knows_devout_8|knows_prisoner_management_4|knows_leadership_8|knows_trade_7,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],

#狩魔骑士团
  ["reaper_Knight","Reaper Knight","Reaper Knights", #狩魔骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_jinshi_touqiang, itm_knight_lance, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_knight_plate, itm_reaper_knight_boot, itm_mogang_yuanzhi_bikai, itm_exorcist_chain_armor_mountain_horse],
   str_40 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["reaper_Knight_captain","Reaper Knight Captain","Reaper Knight Captains", #狩魔骑士长
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_jinshi_touqiang, itm_mogang_zhuixingqiang, itm_baptized_demon_hunting_sword, itm_exorcist_skoutarion, itm_heiyu_changmian_jianzuikui, itm_reaper_high_knight_plate, itm_reaper_knight_boot, itm_mogang_shalouhushou, itm_divine_iron_warhorse],
   str_60 | agi_55 | int_40 | cha_37|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_12|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_9|knows_trainer_8|knows_tracking_10|knows_tactics_9|knows_pathfinding_8|knows_spotting_10|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_14|knows_study_13|knows_devout_14|knows_prisoner_management_14|knows_leadership_13|knows_trade_6, 
   powell_face_middle_1, powell_face_old_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],
#异端猎手队
  ["heretic_hunter","Heretic Hunter","Heretic Hunters",#异端猎手
   tf_female|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_throwing_daggers, itm_special_agent_sword, itm_heresy_hunter_sting, itm_papal_dagger, itm_papal_chain_hood, itm_heresy_hunter_armor, itm_wuzhe_pixue, itm_fenzhi_jiaqiangshoutao],
   str_25 | agi_28 | int_28 | cha_20|level(42),wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (420) | wp_crossbow (420) | wp_throwing (420),
   knows_ironflesh_7|knows_power_strike_8|knows_power_throw_7|knows_power_draw_5|knows_weapon_master_10|knows_shield_7|knows_athletics_10|knows_riding_6|knows_horse_archery_11|knows_looting_5|knows_trainer_4|knows_tracking_8|knows_tactics_6|knows_pathfinding_10|knows_spotting_8|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_2|knows_memory_7|knows_study_5|knows_devout_11|knows_prisoner_management_7|knows_leadership_7|knows_trade_8,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],
  ["heretic_killer","Heretic Killer","Heretic Killers",#异端猎刺
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_jinshi_feidao, itm_special_agent_sword, itm_heresy_hunter_sting, itm_papal_dagger, itm_papal_chain_hood, itm_high_heresy_hunter_armor, itm_black_greaves, itm_fenzhi_fulianshoutao],
   str_32 | agi_40 | int_32 | cha_20|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_9|knows_power_strike_11|knows_power_throw_9|knows_power_draw_7|knows_weapon_master_11|knows_shield_8|knows_athletics_12|knows_riding_7|knows_horse_archery_13|knows_looting_7|knows_trainer_5|knows_tracking_9|knows_tactics_7|knows_pathfinding_10|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_2|knows_memory_7|knows_study_5|knows_devout_11|knows_prisoner_management_7|knows_leadership_7|knows_trade_9,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#宗教审判局
  ["trial_servant","Trial Servant","Trial Servants",#审判仆役
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_verification_fan_shaped_shield, itm_duying_hushouqiang, itm_silver_plated_battle_sword, itm_black_helmet, itm_verification_chain_armor, itm_iron_leather_boot, itm_mail_mittens],
   str_22 | agi_16 | int_27 | cha_25|level(32),wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_8|knows_athletics_6|knows_riding_4|knows_horse_archery_8|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_10|knows_study_8|knows_devout_13|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["doctrinal_sitting_magistrate","Doctrinal Sitting Magistrate","Doctrinal Sitting Magistrates",#教义审判官
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_jugde_fan_shaped_shield, itm_duyin_fuheqiang, itm_silver_plated_exorcist_sword, itm_mogang_zhumiankui, itm_judge_chain_armor, itm_black_greaves, itm_mogang_yuanzhi_bikai],
   str_35 | agi_27 | int_34 | cha_10|level(50),wp_one_handed (460) | wp_two_handed (460) | wp_polearm (460) | wp_archery (460) | wp_crossbow (460) | wp_throwing (460),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_9|knows_shield_10|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_11|knows_study_8|knows_devout_14|knows_prisoner_management_11|knows_leadership_9|knows_trade_5,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#罪奴辅助军团
  ["accused_believer","Accused Believer","Accused Believer",#戴罪信众
   tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_jianyi_jiantiqiang, itm_wooden_board_shield],
   str_12 | agi_8 | int_6 | cha_6|level(12),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_shield_3|knows_athletics_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_1|knows_memory_2|knows_study_1|knows_devout_3,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["sin_slave_soldier","Sin Slave Soldier","Sin Slave Soldiers",#罪仆奴兵
   tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_jiantou_qiang1, itm_tab_shield_pavise_b, itm_papal_conscript_cotton_armor],
   str_15 | agi_12 | int_8 | cha_8|level(21),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_5|knows_athletics_2|knows_riding_1|knows_horse_archery_2|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_surgery_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_4|knows_prisoner_management_1|knows_leadership_2|knows_trade_2,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["sin_slave_infantry","Sin Slave Infantry","Sin Slave Infantries",#罪仆步兵
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_papal_epee, itm_buqiang_jiantiqiang, itm_tab_shield_pavise_c, itm_mail_coif, itm_papal_conscript_cotton_armor, itm_leather_boots],
   str_21 | agi_16 | int_12 | cha_10|level(30),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_7|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_6|knows_prisoner_management_2|knows_leadership_3|knows_trade_3,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["hyena_knight","Hyena Knight","Hyena Knights",#鬣狗骑士
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_claw_blade, itm_jianzuikui, itm_rogue_iron_chest_plate, itm_mail_boots, itm_scale_gauntlets, itm_silver_beast_sabre],
   str_32 | agi_27 | int_17 | cha_14|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_7|knows_athletics_8|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_6|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_5|knows_devout_9|knows_prisoner_management_5|knows_leadership_7|knows_trade_3,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],

#噬罪秘修会
  ["devouring_sin_friar","Devouring Sin Friar","Devouring Sin Friars",#噬罪秘修士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_long_spiked_club, itm_black_hood, itm_theology_student_cloth, itm_leather_boots, itm_leather_gloves],
   str_14 | agi_12 | int_20 | cha_18|level(20),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),
   knows_ironflesh_4|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_3|knows_athletics_3|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_8|knows_devout_14|knows_prisoner_management_2|knows_leadership_3|knows_trade_2,
   papal_face_younger_1, papal_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["devouring_sin_crazy_monk","Devouring Sin Crazy Monk","Devouring Sin Crazy Monks",#啮罪狂僧
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_verification_crazy_monk_armor, itm_long_hafted_spiked_mace, itm_gangshizi_niujiao_dakui3, itm_nailed_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_23 | agi_18 | int_27 | cha_25|level(33),wp_one_handed (270) | wp_two_handed (185) | wp_polearm (270) | wp_archery (185) | wp_crossbow (270) | wp_throwing (185),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_6|knows_athletics_6|knows_riding_4|knows_horse_archery_8|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_10|knows_study_12|knows_devout_14|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["accumulated_sin_knight","Accumulated Sin Knight","Accumulated Sin Knights",#积罪骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_long_hafted_spiked_mace, itm_dingci_lengtouchui, itm_morningstar, itm_devil_rider_hood, itm_reaper_light_knight_plate, itm_dark_plate_boot, itm_mogang_yuanzhi_bikai, itm_demon_horse],
   str_35 | agi_30 | int_43 | cha_30|level(53),wp_one_handed (490) | wp_two_handed (490) | wp_polearm (490) | wp_archery (490) | wp_crossbow (490) | wp_throwing (490),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_8|knows_athletics_8|knows_riding_6|knows_horse_archery_8|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_11|knows_study_14|knows_devout_14|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   papal_face_young_1, papal_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["martyrs_of_deep_crimes","Martyrs of Deep Crimes","Martyrs of Deep Crimes",#深罪殉道者
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_inhuman_helmet, itm_heijin_banjia, itm_dark_plate_boot, itm_mogang_yuanzhi_bikai, itm_long_cruel_morningstar_hammer],
   str_54 | agi_48 | int_67 | cha_40|level(60),wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_15|knows_power_strike_13|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_12|knows_shield_9|knows_athletics_12|knows_riding_9|knows_horse_archery_9|knows_looting_7|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_10|knows_array_arrangement_6|knows_memory_13|knows_study_15|knows_devout_15|knows_prisoner_management_9|knows_leadership_11|knows_trade_6,
   papal_face_old_1, papal_face_older_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],



#——————————————————————————————————真信施洗会—————————————————————————————————
##
  ["divine_legion_veteran","Divine Legion Veteran","Divine Legion Veterans",#圣教军团老兵
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_papal_double_blade_axe, itm_shouhuzhe_changqiang, itm_duyin_zhandouqiang, itm_ban_qingbiankui, itm_papal_knight_chain_armor, itm_mail_boots, itm_gauntlets, itm_papal_iron_tower_shield],
   str_28 | agi_22 | int_19 | cha_17|level(40),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_9|knows_shield_11|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_5|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_3|knows_devout_10|knows_prisoner_management_3|knows_leadership_6|knows_trade_3, 
   papal_face_old_1, papal_face_older_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

  ["divine_legion_veteran_knight","Divine Legion Veteran Knight","Divine Legion Veteran Knights",#圣教军历战骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_jiaoguo_hong_qizhiqiang, itm_papal_double_blade_axe, itm_baptism_knight_fan_shaped_shield, itm_great_helmet, itm_veteran_chian_armor, itm_mail_boots, itm_mogang_fangxing_bikai, itm_veteran_chain_armor_mountain_horse],
   str_36 | agi_27 | int_21 | cha_20|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_10|knows_shield_9|knows_athletics_7|knows_riding_8|knows_horse_archery_8|knows_looting_4|knows_trainer_5|knows_tracking_5|knows_tactics_7|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_6|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_9|knows_study_4|knows_devout_12|knows_prisoner_management_6|knows_leadership_10|knows_trade_5, 
   papal_face_old_1, papal_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["powell_baptized_infantry","Powell Baptized Infantry","Powell Baptized Infantries",#普威尔受洗步兵
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_military_fork, itm_military_sickle_a, itm_simple_papal_fan_shaped_shield, itm_fighting_pick, itm_papal_believer_hood, itm_wangguobubing_jia, itm_leather_boots, itm_kuotou_qiang, itm_jiachang_kuotou_qiang, itm_lengtou_qiang, itm_citou_qiang],
   str_15|agi_13|int_3|cha_9|level(20),wp_one_handed (145) | wp_two_handed (145) | wp_polearm (145) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_1|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_surgery_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_2|knows_devout_15|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["powell_baptized_rider","Powell Baptized Rider","Powell Baptized Riders",#普威尔受洗骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_military_sickle_a, itm_military_pick, itm_baptism_fan_shaped_shield, itm_papal_believer_chain_hood, itm_shicong_lianjiapao, itm_mail_chausses, itm_mail_mittens, itm_hunter, itm_light_lance, itm_lance, itm_double_sided_lance],
   str_22|agi_17|int_3|cha_10|level(31),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_15|knows_prisoner_management_2|knows_leadership_5|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["powell_baptized_knight","Powell Baptized Knight","Powell Baptized Knights",#普威尔受洗骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_military_pick, itm_zhanshi_chu, itm_baptism_soldier_fan_shaped_shield, itm_hongwen_qiqiang, itm_papal_believer_chain_hood, itm_puweier_lianjia, itm_splinted_greaves, itm_gauntlets, itm_jinhong_pijia_liema, itm_honghua_pijia_liema, itm_hongbai_pijia_liema, itm_heavy_lance, itm_great_lance, itm_honghei_wenqiqiang, itm_honghuang_wenqiqiang],
   str_28|agi_23|int_14|cha_16|level(42), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (145) | wp_crossbow (145) | wp_throwing (145),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_7|knows_study_3|knows_devout_15|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   powell_face_younger_1, powell_face_young_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["yishith_baptized_half_elf","Yishith Baptized Half Elf","Yishith Baptized Half Elves",#伊希斯受洗半精灵
   tf_elf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_elf_simple_bow, itm_yishith_dagger, itm_theologian_small_shield, itm_exorcist_battle_shield, itm_elf_light_leather_armor, itm_jingling_lieren_mianku, itm_practice_arrows_2, itm_papal_believer_hood],
   str_9 | agi_26 | int_3 | cha_26|level(20),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (230) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_power_draw_5|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_4|knows_horse_archery_9|knows_looting_3|knows_trainer_4|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_8|knows_study_10|knows_devout_15|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["yishith_baptized_archer","Yishith Baptized Archer","Yishith Baptized Archers",#伊希斯受洗射手
   tf_elf|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_elf_simple_bow, itm_yixisi_qingliangjian, itm_theologian_small_shield, itm_exorcist_battle_shield, itm_papal_believer_hood, itm_autumn_leather_armor, itm_splinted_leather_greaves, itm_fenzhi_pishoutao, itm_barbed_arrows],
   str_14 | agi_33 | int_3 | cha_33|level(30),wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (320) | wp_crossbow (210) | wp_throwing (210),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_7|knows_shield_4|knows_athletics_11|knows_riding_5|knows_horse_archery_11|knows_looting_6|knows_trainer_5|knows_tracking_7|knows_tactics_6|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_10|knows_study_11|knows_devout_15|knows_prisoner_management_3|knows_leadership_4|knows_trade_1,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["yishith_baptized_ranger","Yishith Baptized Ranger","Yishith Baptized Rangers",#伊希斯受洗游侠
   tf_elf|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_elf_woodguard_longbow, itm_elf_halberd, itm_theologian_small_shield, itm_exorcist_battle_shield, itm_papal_believer_chain_hood, itm_autumn_scale_chest_armor, itm_iron_leather_boot, itm_fenzhi_huzhishoutao, itm_bodkin_arrows],
   str_17 | agi_42 | int_3 | cha_43|level(42),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (420) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_10|knows_shield_5|knows_athletics_13|knows_riding_6|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_9|knows_tactics_7|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_11|knows_study_12|knows_devout_15|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   half_elf_face_key_1, half_elf_face_key_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

#庇护骑士团
  ["patron_knight","Patron Knight","Patron Knight",#庇护骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_shouhuzhe_changqiang, itm_zhongxing_fangmainkui1, itm_patron_high_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_papal_plate_armor_mountain_horse, itm_patron_tower_shield],
   str_35 | agi_27 | int_28 | cha_22|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_14|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_3|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_9|knows_trade_4,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],
  ["patron_warrior","Patron Warrior","Patron Warrior",#庇护武士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_shouhuzhe_chaochangqiang, itm_zhongxing_fangmainkui, itm_patron_plate, itm_shengtie_banjiaxue, itm_gauntlets, itm_patron_tower_shield],
   str_25 | agi_16 | int_18 | cha_12|level(45),wp_one_handed (250) | wp_two_handed (75) | wp_polearm (200) | wp_archery (75) | wp_crossbow (75) | wp_throwing (300),
   knows_ironflesh_10|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_13|knows_athletics_8|knows_riding_7|knows_horse_archery_8|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_9|knows_study_3|knows_devout_12|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

#查尼枪骑兵团
  ["chaney_rider","Chaney Rider","Chaney Riders",#查尼骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_sword_medieval_d_long, itm_lance, itm_baptism_fan_shaped_shield, itm_jiaoguo_sheshoukui, itm_maopipijia_pijia, itm_mail_chausses, itm_leather_gloves, itm_huise_ma, itm_baiyipijia_ma, itm_jinshizi_ma, itm_heibaitiaopijia_ma, itm_heishizipijia_ma, itm_lanshizipijia_ma, itm_hongshizipijia_ma, itm_light_lance, itm_heavy_lance, itm_peizhong_jian, itm_qinse_danshoujian],
   str_25 | agi_19 | int_13 | cha_12|level(33),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_7|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_3|knows_devout_8|knows_prisoner_management_3|knows_leadership_5|knows_trade_6,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["chaney_heavy_cavalry","Chaney Heavy Cavalry","Chaney Heavy Cavalries",#查尼重装枪骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_baptism_noble_fan_shaped_shield, itm_scimitar, itm_zhereng_wandao, itm_wanren_jian, itm_guyongbing_quankui, itm_zongse_lianxiongjia, itm_splinted_greaves, itm_gauntlets, itm_warhorse, itm_heishu_lianjia_pinyuanma, itm_zongsebanlian_ma, itm_pilianjai_liema, itm_heishizipijia_ma, itm_fanquwanren_jian, itm_heibai_wenqiqiang, itm_baiwen_qiqiang, itm_ellite_lance],
   str_30 | agi_25 | int_17 | cha_14|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_7|knows_horse_archery_8|knows_looting_4|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_8|knows_prisoner_management_4|knows_leadership_6|knows_trade_7,
   papal_face_young_1, papal_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

#萨顿卫队
  ["baptism_elite_crossbowman","Baptism Elite Crossbowman","Baptism Elite Crossbowmen",#施洗城精英弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_sanbing_nu, itm_military_cleaver_c, itm_steel_bolts, itm_guyongbing_zhongkui, itm_lanbai_banjiayi, itm_splinted_greaves, itm_gauntlets, itm_papal_iron_tower_shield],
   str_28 | agi_26 | int_17 | cha_14|level(45),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (400) | wp_throwing (380),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_9|knows_athletics_8|knows_riding_5|knows_horse_archery_9|knows_looting_4|knows_trainer_5|knows_tracking_5|knows_tactics_4|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_8|knows_prisoner_management_4|knows_leadership_6|knows_trade_6,
   papal_face_old_1, papal_face_older_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["baptism_archer_captain","Baptism Archer Captain","Baptism Archer Captains",#施洗城弓兵队长
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_hongyu_sheshoujian, itm_gorgeous_composite_bow, itm_military_cleaver_c, itm_steel_bar_skoutarion, itm_guyongbing_tiekui, itm_dingshi_fupi_qingbanlian, itm_mail_chausses, itm_gauntlets, itm_baishizipijia_ma, itm_heibaitiaopijia_ma, itm_jinshizi_ma, itm_baiyipijia_ma],
   str_29 | agi_26 | int_17 | cha_14|level(45),wp_one_handed (390) | wp_two_handed (390) | wp_polearm (390) | wp_archery (400) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_6|knows_horse_archery_9|knows_looting_4|knows_trainer_5|knows_tracking_5|knows_tactics_6|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_8|knows_prisoner_management_6|knows_leadership_8|knows_trade_6,
   papal_face_middle_1, papal_face_old_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#绘盾人
  ["shield_drawer","Shield Drawer","Shield Drawers",#绘盾师
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_battle_axe, itm_club_with_spike_head, itm_eliminating_demon_tower_shield, itm_yuanding_limao, itm_guizu_banlianfuhejia, itm_splinted_greaves, itm_fenzhi_fubanshoutao, itm_pilianjai_liema],
   str_28 | agi_26 | int_37 | cha_30|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_11|knows_athletics_9|knows_riding_7|knows_horse_archery_9|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_7|knows_memory_9|knows_study_13|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],

  ["divine_legion_insane_infantry","Divine Legion Insane Infantry","Divine Legion Insane Infantries",#圣教军团狂战士兵
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_eliminating_demon_tower_shield, itm_sword_two_handed_a, itm_ban_qingbiankui, itm_papal_soldier_chain_armor, itm_mail_chausses, itm_gauntlets],
   str_33 | agi_21 | int_6 | cha_20|level(40),wp_one_handed (385) | wp_two_handed (385) | wp_polearm (385) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_11|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_11|knows_devout_15|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   papal_face_younger_1, papal_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["divine_legion_insane_knight","Divine Legion Insane Knight","Divine Legion Insane Knights",#圣教军团狂战骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_extra_great_sowrd, itm_eliminating_demon_tower_shield, itm_silver_great_sowrd, itm_long_axe_b, itm_gangshizi_niujiao_dakui, itm_temple_guardian_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai, itm_simple_plate_mountanic_horse_yellow],
   str_42 | agi_34 | int_3 | cha_12|level(54),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_10|knows_shield_11|knows_athletics_9|knows_riding_6|knows_horse_archery_9|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_15|knows_devout_15|knows_prisoner_management_5|knows_leadership_7|knows_trade_2,
   papal_face_younger_1, papal_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["shield_angel","Shield Angel","Shield Angels",#盾天使
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_silver_extra_great_sowrd, itm_shield_angel, itm_temple_guardian_plate, itm_shengtie_banjiaxue, itm_yuanzhi_bikai],
   str_58 | agi_55 | int_3 | cha_63|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_14|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_11|knows_shield_13|knows_athletics_12|knows_riding_10|knows_horse_archery_11|knows_looting_6|knows_tracking_7|knows_pathfinding_5|knows_spotting_8|knows_study_15|knows_devout_15,
   papal_face_old_1, papal_face_older_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],



#——————————————————————————————————神哲修道宗—————————————————————————————————
##
  ["armed_female_believer","Armed Female Believer","Armed Female Believers",#武装女教友
   tf_female|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_theologian_small_shield, itm_yixisi_qingliangjian, itm_xiunv_toujin, itm_nun_cloth, itm_woolen_hose, itm_nvshi_shoutao],
   str_10 | agi_7 | int_6 | cha_7|level(10),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),
   knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_2|knows_athletics_2|knows_horse_archery_2|knows_tracking_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_1|knows_study_4|knows_devout_6|knows_trade_2,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["martial_sister","Martial Sister","Martial Sisters",#习剑修女
   tf_female|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_theologian_small_shield, itm_yixisi_qingliangjian, itm_xiunv_toujin, itm_arcane_nun_breastplate, itm_leather_boots, itm_fenzhi_pishoutao],
   str_13 | agi_12 | int_10 | cha_11|level(18),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_3|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_3|knows_looting_1|knows_trainer_1|knows_tracking_3|knows_tactics_2|knows_pathfinding_2|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_5|knows_devout_8|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["papal_female_guard","Papal Female Guard","Papal Female Guards",#教国女护卫
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_deism_skoutarion, itm_yixisi_qingliang_shoubanjian, itm_xiunv_tiemian, itm_arcane_nun_breastplate, itm_mail_chausses, itm_gauntlets, itm_baiyipijia_ma, itm_jinshizi_ma],
   str_17 | agi_15 | int_13 | cha_14|level(28),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (230),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_riding_3|knows_horse_archery_5|knows_looting_3|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_5|knows_devout_9|knows_prisoner_management_2|knows_leadership_4|knows_trade_4,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["papal_swordwoman","Papal Swordwoman","Papal Swordwomen",#教国女剑士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_deism_round_shield, itm_silver_plated_sabre, itm_xiunv_tiemian, itm_arcane_nun_armor, itm_mail_boots, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse],
   str_26 | agi_24 | int_17 | cha_18|level(40),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_3|knows_weapon_master_6|knows_shield_8|knows_athletics_7|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_6|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_6|knows_devout_11|knows_prisoner_management_4|knows_leadership_8|knows_trade_7,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["whitspring_chaplain","Whitspring Chaplain","Whitspring Chaplains",#白泉派神官
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_barbed_arrows, itm_war_bow, itm_yixisi_qingliangjian, itm_theologian_small_shield, itm_papal_believer_chain_hood, itm_armed_theologian_chain_armor, itm_iron_leather_boot, itm_leather_gloves],
   str_22 | agi_16 | int_30 | cha_25|level(32),wp_one_handed (270) | wp_two_handed (185) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (185),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_4|knows_weapon_master_7|knows_shield_8|knows_athletics_6|knows_riding_4|knows_horse_archery_8|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_10|knows_study_8|knows_devout_11|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["arcane_minister","Arcane Minister","Arcane Ministers", #奥法牧师
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_high_theologian_chain_armor, itm_deism_skoutarion, itm_noble_hunting_arrow, itm_archer_longbow, itm_asterisk_staff, itm_papal_believer_chain_hood, itm_steel_leather_boot, itm_yinse_bikai],
   str_26 | agi_23 | int_37 | cha_31|level(42),wp_one_handed (380) | wp_two_handed (235) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (235),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_8|knows_shield_11|knows_athletics_6|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_11|knows_study_8|knows_devout_12|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   papal_face_younger_1, papal_face_young_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

#奥术骑士团
  ["arcane_knight","Arcane Knight","Arcane Knights", #奥术骑士
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_deism_round_shield, itm_iron_sister_chain_hood, itm_arcane_light_plate, itm_saintess_boot, itm_yinse_bikai, itm_theologian_chain_armor_mountain_horse, itm_steel_asterisk_staff, itm_knight_recurve_bow, itm_jingling_sanbingjian],
   str_38 | agi_34 | int_51 | cha_44|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_10|knows_riding_11|knows_horse_archery_12|knows_looting_7|knows_trainer_6|knows_tracking_8|knows_tactics_7|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_4|knows_memory_14|knows_study_6|knows_devout_6|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_strategic_strength, #战略力量
  ],

  ["arcane_knight_captain","Arcane Knight Captain","Arcane Knight Captains", #奥术骑士长
   tf_pretty_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_5,
   [itm_jingling_shuyongjian, itm_deism_round_shield, itm_knight_recurve_bow, itm_steel_asterisk_staff, itm_iron_sister_chain_hood, itm_arcane_eilte_plate, itm_saintess_boot, itm_yinse_bikai, itm_highknight_warhorse],
   str_58 | agi_55 | int_63 | cha_59|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_13|knows_shield_13|knows_athletics_12|knows_riding_12|knows_horse_archery_13|knows_looting_7|knows_trainer_9|knows_tracking_9|knows_tactics_9|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_7|knows_engineer_7|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_13|knows_prisoner_management_7|knows_leadership_12|knows_trade_4, 
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#哲学之卵学派
  ["philosophical_egg_scholar","Philosophical Egg Scholar","Philosophical Egg Scholars",#圣卵派学士
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_papal_epee, itm_theologian_small_shield, itm_woolen_hose, itm_nvshi_shoutao, itm_deism_philosophical_student_cloth, itm_penance_blinder],
   str_15 | agi_13 | int_33 | cha_22|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (125) | wp_crossbow (125) | wp_throwing (125),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_5|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_1|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_3|knows_memory_7|knows_study_12|knows_devout_6|knows_prisoner_management_1|knows_leadership_3|knows_trade_2,
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["philosophical_egg_minister","Philosophical Egg Minister","Philosophical Egg Ministers",#圣卵派神官
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_theologian_small_shield, itm_silver_plated_battle_sword, itm_armed_theologian_chain_armor, itm_yinse_lianjiaxue, itm_mail_mittens, itm_penance_hood],
   str_22 | agi_16 | int_39 | cha_25|level(31),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (185) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_7|knows_athletics_5|knows_riding_4|knows_horse_archery_8|knows_looting_2|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_9|knows_study_13|knows_devout_7|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["gnosis_explorer","Gnosis Explorer","Gnosis Explorers",#真知探求者
   tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_plated_hand_and_half_sword, itm_deism_skoutarion, itm_high_theologian_chain_armor, itm_yinse_lianjiaxue, itm_fenzhi_fubanshoutao, itm_baijin_pijia_liema, itm_penance_chain_hood],
   str_27 | agi_23 | int_46 | cha_33|level(42),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (235) | wp_crossbow (235) | wp_throwing (235),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_8|knows_shield_9|knows_athletics_6|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_11|knows_study_13|knows_devout_8|knows_prisoner_management_5|knows_leadership_8|knows_trade_4,
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],
  ["key_knight","Key Knight","Key Knights",#钥骑士
   tf_pretty_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_plated_hand_and_half_sword, itm_deism_skoutarion, itm_guanze_banjiaxue, itm_yinse_bikai, itm_highknight_warhorse, itm_gnosis_light_plate_armor, itm_key_of_all_doors],
   str_37 | agi_30 | int_53 | cha_40|level(55),wp_one_handed (510) | wp_two_handed (510) | wp_polearm (510) | wp_archery (355) | wp_crossbow (355) | wp_throwing (355),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_10|knows_shield_11|knows_athletics_7|knows_riding_8|knows_horse_archery_9|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_7|knows_persuasion_8|knows_array_arrangement_7|knows_memory_12|knows_study_15|knows_devout_9|knows_prisoner_management_5|knows_leadership_7|knows_trade_3,
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["logos_prophet","Logos Prophet","Logos Prophets",#真造先知
   tf_pretty_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_treacherous_halo, itm_deism_round_shield, itm_snow_sabre, itm_saintess_chain_white, itm_saintess_boot, itm_yinse_bikai, itm_highknight_warhorse],
   str_52 | agi_48 | int_70 | cha_50|level(60),wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_14|knows_power_strike_12|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_11|knows_shield_12|knows_athletics_8|knows_riding_9|knows_horse_archery_12|knows_looting_5|knows_trainer_10|knows_tracking_5|knows_tactics_7|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_10|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_11|knows_prisoner_management_6|knows_leadership_10|knows_trade_4,
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],



#——————————————————————————————————圣别渴求者—————————————————————————————————
##
  ["armed_pilgrim","Armed Pilgrim","Armed Pilgrims",#武装朝圣者
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_simple_papal_fan_shaped_shield, itm_iron_staff, itm_pilgrim_hood, itm_armord_pilgrim_outfit, itm_wrapping_boots, itm_leather_gloves],
   str_12 | agi_8 | int_8 | cha_8|level(15),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_1|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_12|knows_devout_13|knows_prisoner_management_2|knows_leadership_4|knows_trade_2,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["armed_archaeological_team","Armed Archaeological Team","Armed Archaeological Teams",#仗剑考古队
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_divine_right_round_shield, itm_iron_staff, itm_silver_plated_sword, itm_ban_guokui, itm_padded_cloth, itm_leather_boots, itm_leather_gloves, itm_saddle_horse],
   str_16 | agi_14 | int_13 | cha_13|level(25),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_5|knows_athletics_5|knows_riding_5|knows_horse_archery_6|knows_looting_4|knows_trainer_4|knows_tracking_3|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_2|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_12|knows_devout_13|knows_prisoner_management_3|knows_leadership_5|knows_trade_2,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["holy_smuggler","Holy Smuggler","Holy Smugglers",#圣迹走私者
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_saints_painting_fan_shaped_shield, itm_long_hafted_knobbed_mace, itm_silver_one_handed_hammer, itm_ban_qingbiankui, itm_sanctification_seeker_chain_armor, itm_mail_chausses, itm_scale_gauntlets, itm_mountain_horse],
   str_24 | agi_17 | int_16 | cha_15|level(32), wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_riding_6|knows_horse_archery_7|knows_looting_7|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_12|knows_devout_13|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["holy_bandit_cavalry","Holy Bandit Cavalry","Holy Bandit Cavalries",#圣匪骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_polehammer, itm_sanctification_seeker_skoutarion, itm_silver_one_handed_hammer, itm_baotu_jiaokui, itm_pilgrim_plate, itm_mail_boots, itm_gauntlets, itm_simple_plate_mountanic_horse_yellow],
   str_33 | agi_28 | int_20 | cha_18|level(48),wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (430) | wp_crossbow (430) | wp_throwing (430),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_7|knows_athletics_7|knows_riding_7|knows_horse_archery_8|knows_looting_9|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_3|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["sacred_object_thief","Sacred Thief","Sacred thieves",#圣物窃贼
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_throwing_daggers, itm_throwing_daggers, itm_divine_right_round_shield, itm_military_hammer, itm_professional_assassin_hood, itm_papal_trainee_leather_armor, itm_leather_boots, itm_fenzhi_jiaqiangshoutao],
   str_23 | agi_22 | int_16 | cha_15|level(33), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_5|knows_shield_6|knows_athletics_8|knows_riding_6|knows_horse_archery_9|knows_looting_7|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_12|knows_devout_13|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["saintly_thief_ranger","Saintly Thief Ranger","Saintly Thief Rangers",#圣盗游侠
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_throwing_daggers, itm_throwing_daggers, itm_divine_right_round_shield, itm_qinliang_lengtouchui, itm_high_assassin_hood, itm_hymn_knight_plate_robeless, itm_nailed_iron_leather_boot, itm_fenzhi_dingshishoutao],
   str_32 | agi_33 | int_20 | cha_18|level(50),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_4|knows_weapon_master_6|knows_shield_7|knows_athletics_11|knows_riding_7|knows_horse_archery_12|knows_looting_9|knows_trainer_8|knows_tracking_3|knows_tactics_5|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_3|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],

  ["papal_zealot","Papal Zealot","Papal Zealots",#教国狂信徒
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_gangshizi_tongkui, itm_crazy_monk_armor, itm_steel_leather_boot, itm_gauntlets],
   str_31 | agi_28 | int_16 | cha_14|level(45),wp_one_handed (410) | wp_two_handed (410) | wp_polearm (410) | wp_archery (410) | wp_crossbow (410) | wp_throwing (410),
   knows_ironflesh_8|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_8|knows_athletics_9|knows_riding_7|knows_horse_archery_9|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_8|knows_study_12|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_1,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["living_saint","Living Saint","Living Saints",#圣别人
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_jiaoguo_tongkui, itm_heavy_temple_guardian_plate, itm_mail_boots, itm_fangxing_bikai, itm_silver_extra_great_sowrd],
   str_64 | agi_64 | int_64 | cha_64|level(60),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_15|knows_power_draw_15|knows_weapon_master_15|knows_shield_15|knows_athletics_15|knows_riding_15|knows_horse_archery_15|knows_looting_10|knows_trainer_10|knows_tracking_10|knows_tactics_10|knows_pathfinding_10|knows_spotting_10|knows_inventory_management_10|knows_wound_treatment_10|knows_surgery_10|knows_first_aid_10|knows_engineer_10|knows_persuasion_10|knows_array_arrangement_10|knows_memory_15|knows_study_15|knows_devout_15|knows_prisoner_management_15|knows_leadership_15|knows_trade_10,
   papal_face_younger_1, papal_face_older_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#圣歌骑士团
  ["hymn_knight","Hymn Knight","Hymn Knights", #圣歌骑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_decorated_towers_shield, itm_steel_asterisk_staff, itm_hymn_great_sword, itm_shengeqishi_fumiankui, itm_hymn_knight_plate_armor, itm_hymn_knight_boot, itm_yuanzhi_bikai],
   str_42 | agi_36 | int_29 | cha_24|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),
   knows_ironflesh_12|knows_power_strike_10|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_11|knows_shield_12|knows_athletics_9|knows_riding_10|knows_horse_archery_11|knows_looting_5|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_4|knows_persuasion_8|knows_array_arrangement_4|knows_memory_12|knows_study_10|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_3, 
   powell_face_young_1, powell_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

  ["hymn_knight_captain","Hymn Knight Captain","Hymn Knight Captains", #圣歌骑士长
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_hymn_great_sword, itm_sanctification_seeker_shield, itm_steel_asterisk_staff, itm_shengeqishi_fumiankui, itm_hymn_high_knight_plate, itm_hymn_knight_boot, itm_huali_shalouhushou, itm_palatin_warhorse],
   str_63 | agi_45 | int_57 | cha_50|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_15|knows_power_strike_13|knows_power_throw_11|knows_power_draw_11|knows_weapon_master_14|knows_shield_12|knows_athletics_13|knows_riding_11|knows_horse_archery_13|knows_looting_7|knows_trainer_8|knows_tracking_6|knows_tactics_8|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_7|knows_memory_13|knows_study_15|knows_devout_14|knows_prisoner_management_9|knows_leadership_13|knows_trade_5, 
   powell_woman_face_1, powell_woman_face_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

  ["holy_church_guard","Holy Sowrd Church Guard","Holy Sowrd Church Guards",#圣堂守卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_5,
   [itm_papal_iron_tower_shield, itm_morningstar, itm_gangshizi_tongkui, itm_heavy_temple_guardian_plate, itm_iron_greaves, itm_gauntlets],
   str_33 | agi_27 | int_25 | cha_21|level(49),wp_one_handed (490) | wp_two_handed (490) | wp_polearm (490) | wp_archery (490) | wp_crossbow (490) | wp_throwing (490),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_9|knows_shield_7|knows_athletics_6|knows_riding_5|knows_horse_archery_8|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_10|knows_study_7|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

#圣痕商会
  ["sanctification_trader","Sanctification Trader","Sanctification Traders",#圣别游商
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_kingdom_5,
   [itm_silver_one_handed_hammer, itm_sanctification_seeker_skoutarion, itm_silver_great_sowrd, itm_great_helmet, itm_baise_quanshenbanjia, itm_iron_greaves, itm_gauntlets, itm_grey_spiritual_horse],
   str_33 | agi_28 | int_32 | cha_23|level(50),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_9|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_4|knows_trainer_4|knows_tracking_4|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_9|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_8|knows_array_arrangement_3|knows_memory_14|knows_study_12|knows_devout_14|knows_prisoner_management_6|knows_leadership_8|knows_trade_9,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#剔圣人
  ["holy_box_collector","Holy Box Collector","Holy Box Collectors",#圣匣收藏家
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_butchering_knife, itm_sanctification_seeker_skoutarion, itm_cleaver, itm_papal_chain_hood, itm_leather_apron, itm_leather_boots, itm_scale_gauntlets],
   str_14 | agi_12 | int_12 | cha_12|level(18),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_3|knows_horse_archery_4|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_12|knows_devout_13|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["holy_blood_desirer","Holy Blood Desirer","Holy Blood Desirers",#圣血渴求者
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_two_handed_cleaver, itm_wumiankui, itm_butcher_red_chain_cotton_armor, itm_iron_leather_boot, itm_scale_gauntlets],
   str_24 | agi_17 | int_16 | cha_15|level(32),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_9|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_6|knows_trainer_4|knows_tracking_5|knows_tactics_4|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_13|knows_devout_13|knows_prisoner_management_4|knows_leadership_6|knows_trade_3,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["holy_meat_epicure","Holy Meat Epicure","Holy Meat Epicures",#圣肉吞食者
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_silver_beast_sabre, itm_wumiankui, itm_butcher_chain_armor, itm_plate_boots, itm_kongju_bikai],
   str_33 | agi_28 | int_20 | cha_20|level(48),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_10|knows_shield_7|knows_athletics_7|knows_riding_5|knows_horse_archery_8|knows_looting_8|knows_trainer_7|knows_tracking_7|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_6|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_10|knows_study_14|knows_devout_14|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["sage_slayer","Sage Slayer","Sage Slayers",#圣人屠夫
   tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_kingdom_5,
   [itm_gangpian_wumainkui, itm_butcher_plate, itm_papal_elite_knight_boot, itm_mogang_fangxing_bikai, itm_saint_cutter],
   str_60 | agi_48 | int_27 | cha_20|level(60),wp_one_handed (580) | wp_two_handed (580) | wp_polearm (580) | wp_archery (580) | wp_crossbow (580) | wp_throwing (580),
   knows_ironflesh_14|knows_power_strike_13|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_11|knows_athletics_12|knows_riding_10|knows_horse_archery_11|knows_looting_10|knows_trainer_8|knows_tracking_10|knows_tactics_8|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_5|knows_memory_12|knows_study_15|knows_devout_15|knows_prisoner_management_8|knows_leadership_10|knows_trade_4,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],


  ["papal_messenger","Papal Messenger","Papal Messengers", #教国信使
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0, 0, fac_kingdom_5,
   [itm_jiaoguo_hong_qizhiqiang, itm_silver_plated_battle_sword, itm_papal_blue_skoutarion, itm_jiaoguo_sheshoukui, itm_papal_red_white_light_chain_armor, itm_mail_boots, itm_gauntlets, itm_mountain_horse],
   str_23 | agi_17 | int_20 | cha_14|level(35), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (320) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_7|knows_athletics_4|knows_riding_5|knows_horse_archery_5|knows_looting_2|knows_trainer_4|knows_tracking_4|knows_tactics_5|knows_pathfinding_7|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_9|knows_study_4|knows_devout_12|knows_prisoner_management_3|knows_leadership_4|knows_trade_2,
   papal_face_middle_1, papal_face_older_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["papal_deserter","Papal Deserter","Papal Deserter",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_leather_steppe_cap_c,itm_nomad_cap,
itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,papal_face_middle_1, papal_face_older_2],



##############################################################龙树##########################################################

 ["longshu_zhengzu","Longshu Zhengzu","Longshu Zhengzu",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_dongfang_jian, itm_dongfang_nu, itm_dongfanfzhenzu_jia, itm_leather_boots, itm_ghost_cane_shield, itm_steel_bolts],
   str_9 | agi_5 | int_4 | cha_4|level(5),wp(80),knows_common|knows_ironflesh_2|knows_weapon_master_1|knows_shield_1|knows_athletics_1,east_face_younger_1, east_face_younger_2],
 ["longshu_tuanlianbing","Longshu Tuanlianbing","Longshu Tuanlianbing",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_tuanlian_jia, itm_dongfang_jian, itm_dongfang_nu, itm_steel_bolts, itm_ghost_cane_shield, itm_jiantouqibing_xue, itm_leather_gloves],
   str_12 | agi_12 | int_6 | cha_5|level(10),wp(120),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_2|knows_shield_1|knows_athletics_2,east_face_younger_1, east_face_young_2],
 ["longshu_xiaoqi","Longshu Xiaoqi","Longshu Xiaoqi",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_leather_gloves, itm_jiantouqibing_xue, itm_linjia_pao, itm_jiji_kui, itm_steel_bolts, itm_dongfang_nu, itm_huanshou_dao, itm_ghost_cane_shield, itm_donfang_liema],
   str_14 | agi_12 | int_7 | cha_7|level(20),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (200) | wp_throwing (120) | wp_firearm (100),knows_common|knows_ironflesh_6|knows_power_strike_5|knows_weapon_master_4|knows_shield_3|knows_athletics_3|knows_horse_archery_3|knows_riding_5,east_face_young_1, east_face_middle_2],
 ["longshu_lance_guaizima","Longshu Lance Guaizima","Longshu Lance Guaizima",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_jiantouqibing_xue, itm_gauizi_ma, itm_gauizima_kui, itm_jingqi_jia, itm_flintlock_pistol_elite, itm_cartridges, itm_ji, itm_scale_gauntlets, itm_loong_round_shield],
   str_21 | agi_12 | int_11 | cha_11|level(30),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (320) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (200),knows_common|knows_ironflesh_8|knows_power_strike_7|knows_weapon_master_5|knows_shield_6|knows_athletics_3|knows_horse_archery_4|knows_riding_7,east_face_young_1, east_face_middle_2],
 ["longshu_longxiangjun","Longshu Longxiangjun","Longshu Longxiangjun",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_gauntlets, itm_longxiang_jia, itm_longxiang_kui, itm_flintlock_pistol_elite, itm_cartridges, itm_jiantouqibing_xue, itm_loong_shield, itm_dongfang_longyaqiang, itm_xueyin_ma],
   str_27 | agi_19 | int_12 | cha_21|level(45),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (500) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (350),knows_common|knows_ironflesh_10|knows_power_strike_11|knows_weapon_master_8|knows_shield_6|knows_athletics_5|knows_horse_archery_4|knows_riding_7,east_face_young_1, east_face_old_2],
 ["longshu_mace_rider","Longshu Mace Rider","Longshu Mace Rider",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_flintlock_pistol_elite, itm_cartridges, itm_jingqi_jia, itm_gauizi_ma, itm_jiantouqibing_xue, itm_scale_gauntlets, itm_gauizima_kui, itm_loong_round_shield, itm_dongfang_zhongjian],
   str_22 | agi_18 | int_12 | cha_15|level(32),wp_one_handed (350) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (200),knows_common|knows_ironflesh_9|knows_power_strike_7|knows_weapon_master_5|knows_shield_6|knows_athletics_5|knows_horse_archery_4|knows_riding_7,east_face_young_1, east_face_middle_2],
 ["longshu_shenwujun","Longshu Shenwujun","Longshu Shenwujun",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_shenwu_jia, itm_shenwu_ma, itm_shenwu_xue, itm_loong_round_shield, itm_prophase_enchanter_sword, itm_flintlock_pistol_elite, itm_cartridges, itm_dongfangjunguan_kui, itm_gauntlets],
   str_42 | agi_35 | int_25 | cha_34|level(55),wp_one_handed (550) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (380),knows_common|knows_ironflesh_13|knows_power_strike_14|knows_weapon_master_10|knows_shield_8|knows_athletics_8|knows_horse_archery_8|knows_riding_9,east_face_young_1, east_face_old_2],
 ["longshu_jiji","Longshu Jiji","Longshu Jiji",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_steel_bolts, itm_jiji_kui, itm_jiantouqibing_xue, itm_huanshou_dao, itm_ghost_cane_shield, itm_dongfang_nu, itm_yulin_jia, itm_scale_gauntlets],
   str_15 | agi_12 | int_7 | cha_7|level(20),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (150) | wp_throwing (120) | wp_firearm (100),knows_common|knows_ironflesh_6|knows_power_strike_5|knows_weapon_master_4|knows_shield_3|knows_athletics_3,east_face_young_1, east_face_middle_2],
 ["longshu_eagle_ruishi","Longshu Eagle Ruishi","Longshu Eagle Ruishi",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_scale_gauntlets, itm_huanshou_dao, itm_tieyinruishi_jia, itm_ruishi_kui, itm_ghost_cane_shield, itm_dongfang_nu, itm_steel_bolts, itm_jiantouqibing_xue],
   str_21 | agi_18 | int_9 | cha_9|level(30),wp_one_handed (320) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (200),knows_common|knows_ironflesh_8|knows_power_strike_7|knows_weapon_master_5|knows_shield_5|knows_athletics_5,east_face_young_1, east_face_middle_2],
 ["longshu_cangtoujun","Longshu Cangtoujun","Longshu Cangtoujun",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_jiantouqibing_xue, itm_ghost_cane_shield, itm_huanshou_dao, itm_buyong_jia, itm_cangtoujun_kui, itm_flintlock_pistol_elite, itm_cartridges, itm_scale_gauntlets],
   str_28 | agi_21 | int_12 | cha_12|level(45),wp_one_handed (430) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (320) | wp_throwing (120) | wp_firearm (350),knows_common|knows_ironflesh_12|knows_power_strike_10|knows_weapon_master_7|knows_shield_6|knows_athletics_6,east_face_old_1, east_face_older_2],
 ["longshu_spear_ruishi","Longshu Spear Ruishi","Longshu Spear Ruishi",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_scale_gauntlets, itm_steel_bolts, itm_jiantouqibing_xue, itm_ghost_cane_shield, itm_dongfang_nu, itm_ruishi_kui, itm_paishuoruishi_jia, itm_dongfang_yinqiang],
   str_21 | agi_18 | int_9 | cha_9|level(30),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (320) | wp_archery (120) | wp_crossbow (250) | wp_throwing (120) | wp_firearm (200),knows_common|knows_ironflesh_8|knows_power_strike_7|knows_weapon_master_5|knows_shield_5|knows_athletics_5,east_face_young_1, east_face_middle_2],
 ["longshu_baiganjun","Longshu Baiganjun","Longshu Baiganjun",tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_flintlock_pistol_elite, itm_cartridges, itm_baiganjun_kui, itm_buyong_jia, itm_jiantouqibing_xue, itm_scale_gauntlets, itm_ghost_cane_shield, itm_dongfang_yinqiang],
   str_28 | agi_21 | int_12 | cha_12|level(45),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (430) | wp_archery (120) | wp_crossbow (150) | wp_throwing (120) | wp_firearm (350),knows_common|knows_ironflesh_12|knows_power_strike_10|knows_weapon_master_7|knows_shield_6|knows_athletics_6,east_face_young_1, east_face_old_2],
 ["longshu_bubazi","Longshu Bubazi","Longshu Bubazi",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_buba_shan, itm_buba_kui, itm_jiantouqibing_xue, itm_dongfang_jian, itm_dongfang_nu, itm_steel_bolts, itm_steel_bolts, itm_steel_bolts, itm_steel_bolts, itm_leather_gloves],
   str_9 | agi_14 | int_6 | cha_5|level(10),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (150) | wp_crossbow (150) | wp_throwing (120) | wp_firearm (120),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_4|knows_athletics_1|knows_riding_2|knows_horse_archery_1,east_face_younger_1, east_face_young_2],
 ["longshu_bow_guaizima","Longshu Bow Guaizima","Longshu Bow Guaizima",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_scale_gauntlets, itm_gauizi_ma, itm_gauizima_kui, itm_jiantouqibing_xue, itm_loong_shield, itm_dongfangchangbai_lianjai, itm_dongfang_jian, itm_dongfang_gangjian, itm_elite_horn_bow],
   str_15 | agi_14 | int_7 | cha_6|level(24),wp_one_handed (190) | wp_two_handed (190) | wp_polearm (190) | wp_archery (230) | wp_crossbow (230) | wp_throwing (120) | wp_firearm (120),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_4|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_5,east_face_young_1, east_face_middle_2],
 ["longshu_tielinjun","Longshu Tielinjun","Longshu Tielinjun",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_dongfangjingjunjian, itm_tielinjun_kui, itm_tielin_bow, itm_tielinjun_kai, itm_dongfang_jian, itm_jiantouqibing_xue, itm_loong_shield, itm_scale_gauntlets, itm_xueyin_ma],
   str_30 | agi_27 | int_15 | cha_15|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (400) | wp_crossbow (350) | wp_throwing (120) | wp_firearm (120),knows_common|knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_8|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_8,east_face_young_1, east_face_old_2],
 ["longshu_shediaoshou","Longshu Shediaoshou","Longshu Shediaoshou",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_scale_gauntlets, itm_huanshou_dao, itm_shediaoshou_jia, itm_jicha_kui, itm_dongfang_nu, itm_jiantouqibing_xue, itm_heiyu_nushi, itm_hongyu_nushi, itm_baiyu_nushi, itm_heibaiyu_nushi],
   str_18 | agi_14 | int_8 | cha_8|level(20),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (280) | wp_archery (150) | wp_crossbow (280) | wp_throwing (120) | wp_firearm (120),knows_common|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_2|knows_horse_archery_1,east_face_middle_1, east_face_old_2],
 ["longshu_accurate_jicha","Longshu Accurate Jicha","Longshu Accurate Jicha",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_graghite_steel_bolts, itm_graghite_steel_bolts, itm_graghite_steel_bolts, itm_jicha_kui, itm_jiantouqibing_xue, itm_dongfang_nu, itm_scale_gauntlets, itm_dongfangzhalian_jia, itm_huanshou_dao],
   str_21 | agi_18 | int_10 | cha_10|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (280) | wp_archery (150) | wp_crossbow (400) | wp_throwing (120) | wp_firearm (230),knows_common|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_2|knows_horse_archery_1,east_face_middle_1, east_face_old_2],
 ["longshu_power_jicha","Longshu Power Jicha","Longshu Power Jicha",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_dongfangzhalian_jia, itm_scale_gauntlets, itm_huanshou_dao, itm_jicha_kui, itm_jiantouqibing_xue, itm_arquebus, itm_cartridges, itm_cartridges, itm_cartridges],
   str_21 | agi_18 | int_10 | cha_10|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (280) | wp_archery (150) | wp_crossbow (280) | wp_throwing (120) | wp_firearm (350),knows_common|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_2|knows_horse_archery_1,east_face_middle_1, east_face_old_2],
 ["longshu_yulinjun","Longshu Yulinjun","Longshu Yulinjun",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_cartridges, itm_cartridges, itm_cartridges, itm_loong_shield, itm_yulinjun_kai, itm_dongfangjunguan_kui, itm_jiantouqibing_xue, itm_scale_gauntlets, itm_jinjun_jian, itm_arquebus],
   str_26 | agi_27 | int_15 | cha_15|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (150) | wp_crossbow (400) | wp_throwing (120) | wp_firearm (500),knows_common|knows_ironflesh_12|knows_power_strike_9|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_7|knows_shield_6|knows_athletics_7|knows_riding_2|knows_horse_archery_1,east_face_middle_1, east_face_older_2],

 ["longshu_eunuch","Longshu Eunuch","Longshu Eunuch",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_huanguan_pao, itm_jiantouqibing_xue, itm_leather_gloves, itm_dongfang_nu, itm_steel_bolts, itm_dongfang_jian],
   str_16 | agi_23 | int_10 | cha_10|level(20),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200) | wp_firearm (200),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_weapon_master_3|knows_shield_4|knows_athletics_5|knows_horse_archery_2|knows_riding_3,east_face_younger_1, east_face_young_1],
 ["longshu_eunuch_inspector","Longshu Eunuch Inspector","Longshu Eunuch Inspector",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_jiantouqibing_xue, itm_huanguanjianjun_jia, itm_dongfangjunguan_kui, itm_scale_gauntlets, itm_jinjun_jian, itm_flintlock_pistol_elite, itm_cartridges],
   str_19 | agi_26 | int_11 | cha_11|level(26),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300) | wp_firearm (300),knows_common|knows_ironflesh_7|knows_power_strike_6|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_horse_archery_3|knows_riding_4,east_face_young_1, east_face_middle_1],
 ["longshu_jiuyijun","Longshu jiuyijun","Longshu jiuyijun",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_scale_gauntlets, itm_jiuyijun_jia, itm_jiantouqibing_xue, itm_dongfangjunguan_kui, itm_gauizi_ma, itm_flintlock_pistol_elite, itm_cartridges, itm_yanyue_dao],
   str_27 | agi_35 | int_12 | cha_12|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400) | wp_firearm (400),knows_common|knows_ironflesh_9|knows_power_strike_8|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_horse_archery_7|knows_riding_7,east_face_young_1, east_face_middle_1],
 ["longshu_cangyijun","Longshu Cangyijun","Longshu Cangyijun",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_dongfangjunguan_kui, itm_jiantouqibing_xue, itm_scale_gauntlets, itm_cangyijun_jia, itm_flintlock_pistol_elite, itm_cartridges, itm_zhanma_dao],
   str_27 | agi_35 | int_12 | cha_12|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400) | wp_firearm (400),knows_common|knows_ironflesh_9|knows_power_strike_8|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_horse_archery_7|knows_riding_7,east_face_young_1, east_face_middle_1],

 ["longshu_mage_knight","Longshu Mage Knight","Longshu Mage Knight",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arabian_horse_a,itm_courser,itm_hunter],
   str_45 | agi_30 | int_12 | cha_15|level(50),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500) | wp_firearm (500),knows_common|knows_ironflesh_15|knows_power_strike_15|knows_weapon_master_14|knows_shield_6|knows_athletics_10|knows_horse_archery_9|knows_riding_11,east_face_young_1, east_face_old_1],

 ["longshu_gulamu","Longshu Gulamu","Longshu Gulamu",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arabian_horse_a,itm_courser,itm_hunter],
   str_30 | agi_30 | int_12 | cha_15|level(40),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100) | wp_firearm (100),knows_common|knows_ironflesh_10|knows_power_strike_9|knows_weapon_master_11|knows_shield_5|knows_athletics_7,east_face_middle_1, east_face_old_1],

   ["longshu_messenger","Longshu Messenger","Longshu Messengers",tf_hero|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,powell_face_young_1, powell_face_old_2],
  ["longshu_deserter","Longshu Deserter","Longshu Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,powell_face_young_1, powell_face_old_2],




##########################################################斯塔胡克大公国##########################################################

#————————————————————————————————大公国通用部队—————————————————————————————————
##
  ["starkhook_recruit","Starkhook Recruit","Starkhook Recruits", #斯塔胡克平民
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_kingdom_7,
   [itm_hatchet, itm_tab_shield_heater_a, itm_leather_cap, itm_felt_hat, itm_felt_hat, itm_shirt, itm_coarse_tunic, itm_leather_apron, itm_wrapping_boots, itm_hand_axe, itm_sword_viking_2_small],
   str_8 | agi_6 | int_6 | cha_6|level(5), wp_one_handed (45) | wp_two_handed (45) | wp_polearm (35) | wp_archery (35) | wp_crossbow (35) | wp_throwing (35),
   knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_athletics_1|knows_looting_1|knows_pathfinding_1|knows_spotting_1|knows_prisoner_management_1|knows_trade_1,
   diemer_face_younger_1, diemer_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["starkhook_armed_sailor","Starkhook Armed Sailor","Starkhook Armed Sailor", #斯塔胡克武装水手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_blue_tunic, itm_blue_gambeson, itm_nordic_archer_helmet, itm_hand_axe, itm_fighting_axe, itm_light_throwing_axes, itm_wooden_shield, itm_nordic_veteran_archer_helmet, itm_xihai_pixue],
   str_12 | agi_7 | int_6 | cha_6|level(10),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),
   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_looting_2|knows_pathfinding_1|knows_spotting_1|knows_first_aid_1|knows_prisoner_management_1|knows_trade_1,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["starkhook_onboard_infantry","Starkhook Onboard Infantry","Starkhook Onboard Infantry", #斯塔胡克船上步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_nordic_shield, itm_mail_shirt, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_leather_gloves, itm_one_handed_war_axe_a, itm_one_handed_battle_axe_a, itm_light_throwing_axes, itm_throwing_axes, itm_xihai_pixue],
   str_15 | agi_13 | int_7 | cha_7|level(20),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (160) | wp_archery (100) | wp_crossbow (100) | wp_throwing (160),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_looting_3|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_2|knows_persuasion_2|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_trade_1,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["starkhook_axe_thrower","Starkhook Axe Thrower","Starkhook Axe Thrower", #斯塔胡克飞斧手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_nordic_helmet, itm_scale_armor, itm_leather_gloves, itm_nordic_shield, itm_xihai_pixue],
   str_22 | agi_18 | int_9 | cha_9|level(32), wp_one_handed (250) | wp_two_handed (250) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (300),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_1|knows_horse_archery_1|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_3|knows_persuasion_3|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["starkhook_boat_fighter","Starkhook Boat Fighter","Starkhook Boat Fighter", #斯塔胡克舷斗士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_fur_covered_shield, itm_scale_armor, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_nordic_helmet, itm_steel_shield, itm_throwing_axes, itm_one_handed_war_axe_b, itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_xihai_pixue],
   str_24 | agi_18 | int_10 | cha_9|level(35), wp_one_handed (300) | wp_two_handed (200) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_5|knows_shield_4|knows_athletics_4|knows_riding_1|knows_horse_archery_3|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_3|knows_persuasion_3|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["starkhook_enhanced_warrior","Starkhook Enhanced Warrior","Starkhook Enhanced Warrior", #斯塔胡克血益步兵
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_lanse_xiongjia, itm_mail_mittens, itm_mail_chausses, itm_splinted_greaves, itm_nordic_fighter_helmet, itm_battle_axe, itm_war_axe, itm_plate_covered_round_shield, itm_throwing_axes],
   str_17|agi_13|int_8|cha_8|level(21),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (180),
   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_4|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_2,
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["starkhook_berserker_warrior","Starkhook Berserker Warrior","Starkhook Berserker Warrior", #斯塔胡克狂战卫士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_throwing_axes, itm_throwing_axes, itm_lansexiongbanjia, itm_mail_boots, itm_scale_gauntlets, itm_nordic_huscarl_helmet, itm_jainyi_shuangrenfu, itm_plate_covered_round_shield],
   str_26 | agi_19 | int_10 | cha_10|level(30), wp_one_handed (240) | wp_two_handed (280) | wp_polearm (200) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_1|knows_horse_archery_1|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_3|knows_persuasion_3|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["starkhook_megalith_berserker","Starkhook Megalith Berserker","Starkhook Megalith Berserker",#斯塔胡克岩雷狂战士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_heavy_throwing_axes, itm_gongguo_banshenjia, itm_iron_greaves, itm_gauntlets, itm_nordic_warlord_helmet, itm_gangpian_fu],
   str_31 | agi_21 | int_11 | cha_11|level(42),wp_one_handed (240) | wp_two_handed (400) | wp_polearm (200) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_9|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_8|knows_tracking_2|knows_tactics_7|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_2|knows_memory_5|knows_study_6|knows_devout_1|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["starkhook_mercenary","Starkhook Mercenary","Starkhook Mercenary",#斯塔胡克佣兵
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
  0,0,fac_kingdom_7,
  [itm_maopipijia_pijia, itm_linjiapijian_dingshijia, itm_leather_boots, itm_leather_gloves, itm_footman_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_sword_viking_1, itm_sword_viking_2, itm_leather_covered_round_shield, itm_wooden_shield, itm_spear, itm_bamboo_spear, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet],
   str_11|agi_7|int_5|cha_5|level(10),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (90) | wp_throwing (90),
   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_athletics_1|knows_horse_archery_2|knows_looting_1|knows_surgery_1|knows_persuasion_1|knows_prisoner_management_1|knows_trade_2,
   diemer_face_young_1, diemer_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["starkhook_armoured_swordman","Starkhook Armoured Swordman","Starkhook Armoured Swordman",#斯塔胡克装甲剑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
  [itm_plate_covered_round_shield, itm_mail_mittens, itm_splinted_leather_greaves, itm_mail_chausses, itm_sword_viking_2, itm_sword_viking_2_small, itm_sword_viking_3_small, itm_haubergeon, itm_kettle_hat],
   str_18|agi_14|int_6|cha_6|level(24),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (120) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_5|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_4|knows_riding_1|knows_horse_archery_6|knows_looting_4|knows_trainer_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_1|knows_trade_5,
   diemer_face_young_1, diemer_face_young_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["starkhook_armoured_horseman","Starkhook Armoured Horseman","Starkhook Armoured Horseman",#斯塔胡克装甲骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
  [itm_heavy_lance, itm_steel_shield, itm_heise_ma, itm_throwing_axes, itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_mail_boots, itm_mail_mittens, itm_mao_guokui, itm_guyongbing_jia],
   str_24|agi_16|int_7|cha_7|level(35),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (120) | wp_crossbow (120) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_8|knows_power_throw_7|knows_power_draw_2|knows_weapon_master_6|knows_shield_2|knows_athletics_6|knows_riding_3|knows_horse_archery_8|knows_looting_6|knows_trainer_4|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_5|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_3|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_devout_1|knows_prisoner_management_5|knows_leadership_5|knows_trade_8,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["starkhook_armoured_crossbowman","Starkhook Armoured Crossbowman","Starkhook Armoured Crossbowman",#斯塔胡克装甲弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
  [itm_mail_mittens, itm_mail_boots, itm_sword_two_handed_b, itm_battle_axe, itm_war_axe, itm_bolts, itm_heavy_crossbow, itm_mao_guokui2, itm_guyongbing_jia],
   str_25|agi_16|int_7|cha_7|level(35),wp_one_handed (200) | wp_two_handed (270) | wp_polearm (200) | wp_archery (120) | wp_crossbow (300) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_6|knows_shield_4|knows_athletics_7|knows_riding_2|knows_horse_archery_6|knows_looting_6|knows_trainer_4|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_6|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_3|knows_engineer_4|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_3|knows_trade_8,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["starkhook_enhanced_mercenary","Starkhook Enhanced Mercenary","Starkhook Enhanced Mercenary",#斯塔胡克血益佣兵
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
  [itm_javelin, itm_nordic_shield, itm_sarranid_axe_a, itm_sarranid_axe_b, itm_mail_hauberk, itm_splinted_leather_greaves, itm_mail_mittens, itm_javelin, itm_lianjia_quanfu_guokui],
   str_17|agi_13|int_8|cha_8|level(20),wp_one_handed (190) | wp_two_handed (190) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (190),
   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_1|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_5|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_5|knows_study_4|knows_devout_1|knows_prisoner_management_3|knows_leadership_6|knows_trade_2,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["starkhook_condottiere","Starkhook Condottiere","Starkhook Condottiere",#斯塔胡克佣兵队长
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
  [itm_lansexiongbanjia, itm_duangang_banjiaxue, itm_duangang_shalouhushou, itm_steel_shield, itm_jianyixihai_shoulingkui, itm_xihai_shoulingkui, itm_jinshi_shuanshoufu, itm_jinshizhanfu, itm_jinshi_toumao, itm_jinshi_touqiang],
   str_30|agi_18|int_21|cha_18|level(40),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_9|knows_power_throw_7|knows_power_draw_2|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_8|knows_tracking_2|knows_tactics_7|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_2|knows_memory_5|knows_study_6|knows_devout_1|knows_prisoner_management_6|knows_leadership_9|knows_trade_7,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["starkhook_business_armed_captain","Starkhook Business Armed Captain","Starkhook Business Armed Captains", #斯塔胡克武装船长
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_flintlock_pistol, itm_cartridges, itm_plate_covered_round_shield, itm_sergeant_sword, itm_xihai_guizumao, itm_grand_duchy_captain_half_plate, itm_iron_leather_boot, itm_fenzhi_huzhishoutao],
   str_23 | agi_18 | int_14 | cha_12|level(36), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300) | wp_firearm (100),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_6|knows_spotting_4|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_2|knows_prisoner_management_3|knows_leadership_6|knows_trade_8,
   diemer_face_middle_1, diemer_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],



#—————————————————————————————————白塔党—————————————————————————————————
##
  ["starkhook_tower_noble","Starkhook Tower Noble","Starkhook Tower Noble", #斯塔胡克白塔贵族
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_shangyeguizu_fu, itm_leather_gloves, itm_xihai_guizumao2, itm_xihai_guizumao, itm_sword_viking_3, itm_viola_shape_shield, itm_xihai_pixue],
   str_12 | agi_8 | int_8 | cha_8|level(10),wp_one_handed (7) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_1|knows_athletics_1|knows_riding_2|knows_horse_archery_1|knows_trainer_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_2|knows_memory_2|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_3,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["starkhook_enhanced_swordman","Starkhook Enhanced Swordman","Starkhook Enhanced Swordman", #斯塔胡克血益剑士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
   [itm_zenyijianshi_jia, itm_mail_boots, itm_scale_gauntlets, itm_xihan_lingjiamao, itm_papal_hand_and_half_sword],
   str_20 | agi_14 | int_9 | cha_9|level(25),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (120) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_4,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["starkhook_bloody_berserker","Starkhook Bloody Berserker","Starkhook Bloody Berserker", #斯塔胡克血塔狂战士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
   [itm_bloodburst_sword, itm_berserker_half_body_armor, itm_kuangzhanshi_kui, itm_kuangzhanshi_xue, itm_huali_shalouhushou],
   str_42 | agi_30 | int_15 | cha_12|level(45),wp_one_handed (410) | wp_two_handed (410) | wp_polearm (120) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["starkhook_enhanced_halberdman","Starkhook Enhanced Halberdman","Starkhook Enhanced Halberdman", #斯塔胡克血益斧手
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
  [itm_scale_gauntlets, itm_zenyifushi_jia, itm_mail_boots, itm_xihan_lingjiamao, itm_long_bardiche],
   str_20 | agi_14 | int_9 | cha_9|level(25),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (220) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_1|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_4,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["starkhook_mangler_berserker","Starkhook Mangler Berserker","Starkhook Mangler Berserker", #斯塔胡克厉海狂战士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_huali_shalouhushou, itm_berserker_half_body_armor, itm_kuangzhanshi_kui, itm_kuangzhanshi_xue, itm_mangler_halberd],
   str_42 | agi_30 | int_15 | cha_12|level(45),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (410) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["bloodburst_servant","Bloodburst Servant","Bloodburst Servant", #血涌仆从
   tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_slavers,
   [itm_jainyi_xifangfu, itm_nordic_fighter_helmet, itm_westcoast_leather_armed_clothing],
   str_12 | agi_24 | int_6 | cha_3|level(25), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_5|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_1|knows_athletics_8|knows_riding_2|knows_horse_archery_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_persuasion_1|knows_study_2,
   diemer_face_younger_1, diemer_face_older_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["bloodburst_slave","Bloodburst Slave","Bloodburst Slave", #血缚者
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_slavers,
  [itm_jainyi_xifangfu, itm_heibai_wenqiqiang, itm_sword_viking_3, itm_half_bird_fan_shaped_shield, itm_vaegir_noble_helmet, itm_silver_plated_breastplate, itm_splinted_leather_greaves, itm_scale_gauntlets, itm_zase_ma, itm_huise_ma],
   str_22 | agi_30 | int_7 | cha_4|level(38),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_4|knows_athletics_8|knows_riding_5|knows_horse_archery_5|knows_looting_3|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_persuasion_3|knows_memory_4|knows_study_2|knows_devout_1,
   diemer_face_younger_1, diemer_face_older_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["blood_sinner","Blood Sinner","Blood Sinner", #鲜血罪人
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
   [itm_duangang_lianrenfu, itm_long_axe_b, itm_long_axe, itm_tab_shield_small_round_b, itm_xihan_lingjiamao, itm_hongse_zhabanjia, itm_steel_leather_boot, itm_scale_gauntlets, itm_chenyipijia_ma],
   str_33 | agi_31 | int_15 | cha_12|level(46),wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (300) | wp_crossbow (300) | wp_throwing (430),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_young_1, diemer_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],

  ["starkhook_throwing_axe_ranger","Starkhook Throwing Axe Ranger","Starkhook Throwing Axe Rangers", #斯塔胡克飞斧游侠
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_throwing_axes, itm_heavy_throwing_axes, itm_simple_red_wind_skoutarion, itm_lianren_fu, itm_xihan_lingjiamao, itm_xuandoushi_jia, itm_mail_chausses, itm_mail_mittens, itm_huise_ma],
   str_30 | agi_28 | int_17 | cha_16|level(44),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (200) | wp_crossbow (200) | wp_throwing (440),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_8|knows_power_draw_3|knows_weapon_master_7|knows_shield_3|knows_athletics_7|knows_riding_6|knows_horse_archery_9|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["starkhook_throwing_axe_master","Starkhook Throwing Axe Master","Starkhook Throwing Axe Masters", #斯塔胡克飞斧大师
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_heavy_throwing_axes, itm_tab_shield_round_e, itm_heavy_throwing_axes, itm_lianren_fu, itm_xihai_wenshikui, itm_gongguo_banshenjia2, itm_black_greaves, itm_gauntlets],
   str_40 | agi_38 | int_20 | cha_21|level(50),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (300) | wp_crossbow (300) | wp_throwing (500),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_5|knows_horse_archery_7|knows_looting_1|knows_trainer_7|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

#血勋铁卫团
  ["bloodhonor_guard","Bloodhonor Guard","Bloodhonor Guards", #血勋铁卫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
   [itm_bloodthirsty_javelin, itm_kuangzhanshi_kui, itm_bloodhonor_armor, itm_westcoast_guard_boot, itm_westcoast_black_glove, itm_heroic_halberd],
   str_43 | agi_36 | int_18 | cha_24|level(52),wp_one_handed (490) | wp_two_handed (490) | wp_polearm (490) | wp_archery (300) | wp_crossbow (300) | wp_throwing (490),
   knows_ironflesh_11|knows_power_strike_11|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_9|knows_shield_6|knows_athletics_12|knows_riding_5|knows_horse_archery_10|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_5|knows_leadership_8|knows_trade_4, 
   diemer_face_middle_1, diemer_face_older_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["light_bloodhonor_guard","Light Bloodhonor Guard","Light Bloodhonor Guards", #轻装血勋铁卫
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_bloodthirsty_javelin, itm_kuangzhanshi_kui, itm_scarlet_bloodhonor_armor, itm_westcoast_guard_boot, itm_westcoast_black_glove, itm_bloodthirsty_javelin, itm_garrison_sickle_axe, itm_variegated_spiritual_horse, itm_steel_shield],
   str_42 | agi_35 | int_18 | cha_24|level(50),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_10|knows_power_draw_5|knows_weapon_master_8|knows_shield_5|knows_athletics_10|knows_riding_7|knows_horse_archery_10|knows_looting_4|knows_trainer_6|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_7|knows_study_3|knows_devout_4|knows_prisoner_management_5|knows_leadership_7|knows_trade_4, 
   diemer_face_middle_1, diemer_face_older_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["bloodhonor_guard_captain","Bloodhonor Guard Captain","Bloodhonor Guard Captains", #血勋铁卫队长
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
   [itm_bloodthirsty_javelin, itm_kuangzhanshi_kui, itm_azure_bloodhonor_armor, itm_westcoast_guard_boot, itm_westcoast_black_glove, itm_axe_of_bloddhonor, itm_bloodthirsty_javelin, itm_bloodthirsty_javelin],
   str_62 | agi_56 | int_28 | cha_27|level(60),wp_one_handed (590) | wp_two_handed (590) | wp_polearm (590) | wp_archery (400) | wp_crossbow (400) | wp_throwing (590),
   knows_ironflesh_13|knows_power_strike_14|knows_power_throw_15|knows_power_draw_5|knows_weapon_master_9|knows_shield_6|knows_athletics_12|knows_riding_7|knows_horse_archery_11|knows_looting_3|knows_trainer_6|knows_tracking_3|knows_tactics_7|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_3|knows_devout_4|knows_prisoner_management_8|knows_leadership_10|knows_trade_4, 
   diemer_face_middle_1, diemer_face_older_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#血湖之庭
  ["blood_lake_sentry","Blood Lake Sentry","Blood Lake Sentries",#血湖哨兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
  [itm_tab_shield_pavise_c, itm_heavy_crossbow, itm_glaive, itm_danshou_chanfu, itm_wumian_lianjiakui, itm_scale_armor, itm_nailed_iron_leather_boot, itm_leather_gloves, itm_steel_bolts],
   str_26 | agi_19 | int_10 | cha_10|level(30), wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (100) | wp_crossbow (280) | wp_throwing (260),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_1|knows_looting_2|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_3|knows_persuasion_3|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_4|knows_trade_3,
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["blood_lake_patrol_cavalry","Blood Lake Patrol Cavalry","Blood Lake Patrol Cavalries",#血湖巡逻骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
  [itm_jinshi_zhanbiao, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_extra_long_shovel_axe, itm_xihai_fumiankui, itm_heise_zaoqi_banjia, itm_black_greaves, itm_mogang_yuanzhi_bikai, itm_heishu_lianjia_pinyuanma],
   str_40 | agi_38 | int_20 | cha_21|level(50),wp_one_handed (460) | wp_two_handed (460) | wp_polearm (460) | wp_archery (300) | wp_crossbow (400) | wp_throwing (480),
   knows_ironflesh_10|knows_power_strike_10|knows_power_throw_8|knows_power_draw_5|knows_weapon_master_7|knows_shield_3|knows_athletics_8|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_7|knows_tracking_7|knows_tactics_6|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],

  ["crimson_berserker","Crimson Berserker","Crimson Berserkers",#猩红狂战士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_kingdom_7,
   [itm_xianhongchaozhongbanjia, itm_crimson_hand, itm_blood_short_spear, itm_blood_angel_heavy_helmet, itm_zhongxing_banjiaxue],
   str_58 | agi_38 | int_8 | cha_11|level(55),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (300) | wp_crossbow (300) | wp_throwing (480),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_13|knows_power_draw_8|knows_weapon_master_7|knows_shield_6|knows_athletics_12|knows_riding_6|knows_horse_archery_9|knows_looting_3|knows_tracking_3|knows_pathfinding_3|knows_spotting_3|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_2|knows_memory_7|knows_study_15|knows_devout_3, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["red_apostle","Red Apostle","Red Apostles",#红使徒
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_bloody_moon_halo, itm_red_apostle_boot, itm_grip_of_crimson_flow, itm_shadow_of_blood_invasion, itm_crimson_lunar_flowing_light, itm_crimson_lunar_flowing_light, itm_crimson_curtain, itm_red_apostle_armor, itm_scaffold_axe, itm_bloodstar, itm_blood_snatcher],
   str_82 | agi_48 | int_5 | cha_3|level(61),wp_one_handed (510) | wp_two_handed (500) | wp_polearm (510) | wp_archery (300) | wp_crossbow (300) | wp_throwing (500),
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_15|knows_power_draw_11|knows_weapon_master_4|knows_shield_2|knows_athletics_14|knows_riding_7|knows_horse_archery_6|knows_looting_7|knows_tracking_7|knows_pathfinding_7|knows_spotting_7|knows_persuasion_6|knows_memory_8|knows_study_15|knows_devout_4, 
   diemer_face_middle_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],

#戒血执法者
  ["blood_extinguisher","Blood Extinguisher","Blood Extinguisher", #熄血射手
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_glaive, itm_one_handed_battle_axe_a, itm_one_handed_war_axe_a, itm_fighting_axe, itm_nordic_footman_helmet, itm_light_leather, itm_light_leather_boots, itm_leather_gloves, itm_westcoast_longbow, itm_blood_extinguish_arrow],
   str_23 | agi_18 | int_12 | cha_9|level(30), wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (230) | wp_crossbow (100) | wp_throwing (200),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_5|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_2|knows_trainer_2|knows_tracking_4|knows_tactics_3|knows_pathfinding_3|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],
  ["blood_hunter","Blood Hunter","Blood Hunter",#戒血猎人
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_simple_archipelagic_short_bow, itm_duangang_lianrenfu, itm_blue_breeze_round_shield, itm_xihai_dingshikui, itm_gongguo_banshenjia, itm_mail_boots, itm_fenzhi_fubanshoutao, itm_julu_ianjia_pingyuanma, itm_blood_extinguish_arrow],
   str_40 | agi_33 | int_15 | cha_12|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (320) | wp_crossbow (200) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_7|knows_weapon_master_7|knows_shield_6|knows_athletics_7|knows_riding_3|knows_horse_archery_7|knows_looting_3|knows_trainer_7|knows_tracking_5|knows_tactics_5|knows_pathfinding_5|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_5|knows_first_aid_4|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_5|knows_study_4|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_middle_1, diemer_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#闭锁之堡
  ["starkhook_shield_woman","Starkhook Shield Woman","Starkhook Shield Women", #斯塔胡克盾女
   tf_female|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_changren_qiang, itm_sword_viking_2, itm_duangang_lianrenfu, itm_tab_shield_round_e, itm_nordic_huscarl_helmet, itm_lansexiongbanjia, itm_mail_chausses, itm_fenzhi_dingshishoutao],
   str_25 | agi_18 | int_14 | cha_18|level(38),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (380) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_7|knows_athletics_4|knows_riding_5|knows_horse_archery_6|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_3|knows_devout_4|knows_prisoner_management_3|knows_leadership_5|knows_trade_3,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_defend, #防御
  ],



#————————————————————————————————斯塔胡克商业联合—————————————————————————————————
##
  ["starkhook_commercial_nobility","Starkhook Commercial Nobility","Starkhook Commercial Nobility", #斯塔胡克商业贵族
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_shangyeguizu_fu, itm_leather_gloves, itm_xihai_guizumao2, itm_xihai_guizumao, itm_hunter, itm_longshoujian, itm_viola_shape_shield, itm_xihai_pixue],
   str_11 | agi_8 | int_10 | cha_9|level(10),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_athletics_1|knows_riding_3|knows_horse_archery_1|knows_trainer_1|knows_tactics_1|knows_inventory_management_1|knows_persuasion_2|knows_memory_2|knows_study_1|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_4,
   diemer_face_younger_1, diemer_face_young_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["starkhook_attendant_cavalry","Starkhook Attendant Cavalry","Starkhook Attendant Cavalry", #斯塔胡克侍从骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_jinshi_cejian, itm_sergeant_sword, itm_round_shield, itm_sword_viking_3, itm_banmian_lianjiakui, itm_duanxiu_lianjiapao, itm_mail_chausses, itm_mail_mittens, itm_jinhuapijia_ma, itm_lance, itm_heavy_lance],
   str_19 | agi_15 | int_12 | cha_11|level(24),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_2|knows_devout_2|knows_prisoner_management_2|knows_leadership_4|knows_trade_6,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],
  ["starkhook_knight","Starkhook Knight","Starkhook Knight", #斯塔胡克骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_jinshi_cejian, itm_sergeant_sword, itm_hippocampus_skoutarion, itm_sword_viking_3, itm_xihai_guizukui, itm_heise_lianxiongjia, itm_mail_boots, itm_gauntlets, itm_jiaoma_ianjia_pingyuanma, itm_lance, itm_heavy_lance, itm_lianren_fu],
   str_25 | agi_22 | int_14 | cha_13|level(40),wp_one_handed (340) | wp_two_handed (340) | wp_polearm (340) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_8,
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_strike, #突击
  ],

  ["starkhook_blood_arrow_shooter","Starkhook Blood Arrow Shooter","Starkhook Blood Arrow Shooters", #斯塔胡克血箭射手
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_jinshi_cejian, itm_hippocampus_skoutarion, itm_sword_viking_3, itm_xihai_guizukui, itm_heise_lianxiongjia, itm_mail_boots, itm_gauntlets, itm_lianren_fu, itm_red_short_bow, itm_weeping_blood_arrow],
   str_25 | agi_23 | int_14 | cha_13|level(41), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (200) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_5|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_2|knows_prisoner_management_4|knows_leadership_7|knows_trade_8,
   diemer_face_middle_1, diemer_face_old_2, 0, 
   0, 0, itm_function_curved_fire, #曲射火力
  ],

  ["blood_can_slave","Blood Can Slave","Blood Can Slaves", #血罐仆从
   tf_guarantee_boots,
   0,0,fac_slavers,
   [itm_wrapping_boots, itm_dagger, itm_hatchet, itm_hunter_boots],
   str_7 | agi_5 | int_6 | cha_7|level(5), wp_one_handed (25) | wp_two_handed (25) | wp_polearm (25) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),
   knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_devout_1|knows_trade_1,
   diemer_face_young_1, diemer_face_old_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["armed_blood_slave","Armed Blood Slave","Armed Blood Slaves", #武装血仆
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_tab_shield_round_b, itm_ragged_outfit, itm_hide_boots, itm_sword_viking_1, itm_sword_viking_2_small, itm_sword_viking_3_small, itm_long_pole_machete, itm_fighting_axe, itm_one_handed_war_axe_a, itm_one_handed_battle_axe_a, itm_axe, itm_hunter_boots, itm_ankle_boots],
   str_10 | agi_9 | int_8 | cha_8|level(15), wp_one_handed (125) | wp_two_handed (125) | wp_polearm (125) | wp_archery (125) | wp_crossbow (125) | wp_throwing (125),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_2|knows_shield_2|knows_athletics_2|knows_riding_1|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_persuasion_1|knows_memory_2|knows_devout_1|knows_prisoner_management_1|knows_trade_1,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["blood_servant_guard","Blood Servant Guard","Blood Servant Guards", #血眷卫士
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_sarranid_axe_a, itm_tab_shield_round_c, itm_sword_viking_2, itm_sword_viking_3, itm_nordic_footman_helmet, itm_maopipijia_pijia, itm_splinted_leather_greaves, itm_fenzhi_pishoutao, itm_voulge, itm_axe, itm_military_scythe],
   str_14 | agi_12 | int_9 | cha_10|level(25), wp_one_handed (225) | wp_two_handed (225) | wp_polearm (225) | wp_archery (225) | wp_crossbow (225) | wp_throwing (225),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_2|knows_horse_archery_4|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_2|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_2|knows_trade_2,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_cannon_fodder, #炮灰
  ],
  ["starkhook_companion_infantry","Starkhook Companion Infantry","Starkhook Companion Infantries", #斯塔胡克伙友步兵
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_slavers,
   [itm_jainyi_changbingfu, itm_tab_shield_pavise_d, itm_jainyi_shuangrenfu, itm_danshou_biantoufu, itm_banmian_lianjiakui, itm_zenyifushi_jia, itm_mail_chausses, itm_mail_mittens],
   str_19 | agi_17 | int_10 | cha_11|level(37), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_6|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_3|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_6|knows_surgery_6|knows_first_aid_6|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_4|knows_trade_2,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_assistance, #辅助
  ],

  ["starkhook_business_association_rider","Starkhook Business Association Rider","Starkhook Business Association Riders", #斯塔胡克商联骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_tab_shield_small_round_a, itm_one_handed_war_axe_a, itm_footman_helmet, itm_leather_jerkin, itm_splinted_leather_greaves, itm_leather_gloves, itm_sumpter_horse, itm_segmented_helmet, itm_helmet_with_neckguard, itm_mail_coif, itm_light_lance, itm_lance, itm_sword_viking_1, itm_sword_viking_3_small, itm_double_sided_lance, itm_sword_viking_2_small],
   str_14 | agi_11 | int_8 | cha_7|level(20),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_athletics_2|knows_riding_3|knows_horse_archery_2|knows_trainer_2|knows_tactics_2|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_4|knows_surgery_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_2|knows_trade_4,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["starkhook_business_association_leader","Starkhook Business Association Leader","Starkhook Business Association Leaders", #斯塔胡克商联队长
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_tab_shield_round_c, itm_tab_shield_small_round_b, itm_qianse_longxikui, itm_haubergeon, itm_steel_leather_boot, itm_mail_mittens, itm_zongse_dingshi_pijia_liema, itm_lance, itm_heavy_lance, itm_great_lance, itm_chenyipijia_ma, itm_sword_viking_2, itm_sergeant_sword, itm_sword_viking_3, itm_lianren_fu, itm_shense_longxikui, itm_light_crossbow, itm_bolts],
   str_23 | agi_18 | int_14 | cha_12|level(36),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_5|knows_horse_archery_5|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_6|knows_spotting_4|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_2|knows_prisoner_management_3|knows_leadership_6|knows_trade_8,
   diemer_face_middle_1, diemer_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

#猩红满月骑士团
  ["red_moon_knight","Red Moon Knight","Red Moon Knights", #赤月骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_tab_shield_small_round_c, itm_scarlet_heavy_lance, itm_sergeant_sword, itm_starkhook_imported_plate_armor, itm_mail_boots, itm_scale_gauntlets, itm_julu_ianjia_pingyuanma, itm_scarlet_heavy_helmet],
   str_41 | agi_34 | int_19 | cha_21|level(48),wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (320) | wp_crossbow (200) | wp_throwing (320),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_7|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_9|knows_study_7|knows_devout_4|knows_prisoner_management_4|knows_leadership_7|knows_trade_4, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["crimson_war_mage","Crimson War Mage","Crimson War Mages", #猩红战法师
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_kingdom_7,
   [itm_sergeant_sword, itm_tab_shield_round_e, itm_qubing_lianrenfu, itm_starkhook_imported_plate_armor, itm_mail_boots, itm_scale_gauntlets, itm_scarlet_heavy_helmet],
   str_37 | agi_31 | int_18 | cha_20|level(45),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (300) | wp_crossbow (200) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_5|knows_horse_archery_7|knows_looting_3|knows_trainer_6|knows_tracking_5|knows_tactics_5|knows_pathfinding_4|knows_spotting_5|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_4|knows_engineer_1|knows_persuasion_6|knows_array_arrangement_1|knows_memory_8|knows_study_7|knows_devout_4|knows_prisoner_management_4|knows_leadership_6|knows_trade_4, 
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],



#————————————————————————————————蛇夫党—————————————————————————————————
##
  ["abyss_mercenary","Abyss Mercenary","Abyss Mercenaries", #渊海佣兵
   tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_kingdom_7,
   [itm_sea_monster_fan_shaped_shield, itm_jixingfu, itm_longshoujian, itm_nordic_helmet, itm_mail_shirt, itm_splinted_leather_greaves, itm_scale_gauntlets],
   str_25|agi_16|int_7|cha_7|level(35),wp_one_handed (200) | wp_two_handed (270) | wp_polearm (200) | wp_archery (300) | wp_crossbow (120) | wp_throwing (200),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_7|knows_riding_2|knows_horse_archery_6|knows_looting_6|knows_trainer_4|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_6|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_3|knows_engineer_4|knows_persuasion_4|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_devout_1|knows_prisoner_management_3|knows_leadership_3|knows_trade_8,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],


  ["starkhook_messenger","Starkhook Messenger","Starkhook Messengers", #斯塔胡克信使
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 
   0, 0, fac_kingdom_7,
   [itm_throwing_axes, itm_sword_two_handed_b, itm_throwing_axes, itm_nordic_warlord_helmet, itm_heavy_red_breastplate, itm_xihai_pixue, itm_leather_gloves, itm_zase_ma],
   str_23 | agi_18 | int_14 | cha_10|level(35), wp_one_handed (250) | wp_two_handed (280) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (290),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_5|knows_riding_4|knows_horse_archery_4|knows_looting_6|knows_trainer_2|knows_tracking_3|knows_tactics_3|knows_pathfinding_5|knows_spotting_3|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_3|knows_study_4|knows_devout_2|knows_prisoner_management_4|knows_leadership_3|knows_trade_1,
   diemer_face_young_1, diemer_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
 ["starkhook_deserter","starkhook Deserter","starkhook Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
  def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,powell_face_young_1, powell_face_old_2],





#############################################################自由城邦##########################################################
##
  ["citizen_pauper","Citizen Pauper","Citizen Paupers", #自由城邦贫民
   tf_guarantee_armor,
   0, 0, fac_commoners,
   [itm_scythe, itm_hatchet, itm_fighting_pick, itm_club, itm_stones, itm_tab_shield_heater_a, itm_leather_cap, itm_felt_hat, itm_felt_hat, itm_shirt, itm_coarse_tunic, itm_leather_apron, itm_nomad_boots, itm_wrapping_boots, itm_linen_tunic],
   str_7|agi_5|int_5|cha_4|level(1), wp_one_handed (10) | wp_two_handed (10) | wp_polearm (10) | wp_archery (10) | wp_crossbow (10) | wp_throwing (10),
   knows_ironflesh_1|knows_inventory_management_1|knows_wound_treatment_1|knows_first_aid_1|knows_devout_1,
   man_face_younger_1, man_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["citizen_militia","Citizen Militia","Citizen Militias", #自由城邦民兵
   tf_guarantee_boots|tf_guarantee_armor,
   0, 0, fac_commoners,
   [itm_tab_shield_heater_a, itm_ankle_boots, itm_leather_boots, itm_coarse_tunic, itm_tabard, itm_skullcap, itm_mail_coif, itm_leather_warrior_cap, itm_sword_medieval_a, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_battle_fork, itm_boar_spear, itm_fur_covered_shield, itm_tab_shield_round_a, itm_tab_shield_kite_a, itm_sarranid_two_handed_mace_1, itm_sarranid_mace_1],
   str_9|agi_7|int_5|cha_5|level(6), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),
   knows_ironflesh_1|knows_power_strike_1|knows_shield_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_devout_1|knows_prisoner_management_1|knows_trade_1,
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["citizen_defend_militia","Citizen Defend Militia","Citizen Defend Militias", #自由城邦防卫民兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0, 0, fac_commoners,
   [itm_tab_shield_round_b, itm_wooden_shield, itm_fur_covered_shield, itm_leather_vest, itm_nomad_boots, itm_military_fork, itm_battle_fork, itm_boar_spear, itm_sword_medieval_b, itm_sword_medieval_a, itm_military_hammer, itm_rawhide_coat, itm_mace_4, itm_baotie_toujin, itm_hide_boots, itm_footman_helmet, itm_skullcap],
   str_12|agi_8|int_7|cha_6|level(13), wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_shield_2|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_devout_1|knows_prisoner_management_1|knows_trade_1,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["citizen_patrol","Citizen Patrol","Citizen Patrols", #自由城邦巡逻队员
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_manhunters,
   [itm_leather_covered_round_shield, itm_wooden_shield, itm_footman_helmet, itm_padded_cloth, itm_leather_boots, itm_saddle_horse, itm_sumpter_horse, itm_baotie_toujin, itm_boar_spear, itm_nomad_armor, itm_khergit_armor, itm_sword_medieval_b_small, itm_sword_medieval_c_long, itm_sword_medieval_c, itm_kuotou_qiang, itm_jiachang_kuotou_qiang, itm_splinted_leather_greaves],
   str_14|agi_10|int_9|cha_7|level(20), wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_2|knows_shield_3|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_2|knows_memory_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_1|knows_trade_2,
   man_face_middle_1, man_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["manhunter", "Manhunter", "Manhunters", #赏金猎人
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_manhunters,
   [itm_jousting_lance, itm_tab_shield_small_round_a, itm_tab_shield_round_c, itm_tab_shield_small_round_b, itm_mail_coif, itm_leather_jerkin, itm_mail_chausses, itm_leather_gloves, itm_steppe_horse, itm_leather_armor, itm_zhanshi_chui, itm_qinliang_lengtouchui, itm_helmet_with_neckguard, itm_splinted_leather_greaves, itm_iron_leather_greave, itm_arrows, itm_simple_long_bow],
   str_19|agi_15|int_9|cha_8|level(30), wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (230),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_4|knows_looting_2|knows_trainer_3|knows_tracking_4|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_persuasion_3|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_6|knows_leadership_3|knows_trade_3,
   man_face_middle_1, man_face_older_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["citizen_light_infantry","Citizen Light Infantry","Citizen Light Infantris", #自由城邦轻步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_commoners,
   [itm_tab_shield_pavise_a, itm_tab_shield_pavise_b, itm_jiachang_kuotou_qiang, itm_citou_qiang, itm_baotie_toujin, itm_ragged_outfit, itm_leather_boots, itm_tunic_with_green_cape],
   str_13|agi_10|int_9|cha_7|level(18), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (140) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_2|knows_shield_3|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_2|knows_memory_1|knows_devout_2|knows_prisoner_management_3|knows_leadership_1|knows_trade_2,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],
  ["citizen_spearman","Citizen Spearman","Citizen Spearmen", #自由城邦矛兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_commoners,
   [itm_tab_shield_pavise_c, itm_lengtou_qiang, itm_ashwood_pike, itm_helmet_with_neckguard, itm_red_studded_padded_armor, itm_iron_leather_greave, itm_scale_gauntlets],
   str_18|agi_15|int_9|cha_8|level(28), wp_one_handed (210) | wp_two_handed (210) | wp_polearm (230) | wp_archery (210) | wp_crossbow (210) | wp_throwing (210),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_1|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_4|knows_looting_2|knows_trainer_3|knows_tracking_4|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_persuasion_3|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_6|knows_leadership_3|knows_trade_3,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_defend, #防御
  ],

  ["states_civilian","States Civilian","States Civilians", #自由城邦公民
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_heater_c, itm_qinse_danshoujian, itm_sword_medieval_d_long, itm_peizhong_jian, itm_segmented_helmet, itm_ziyouchengbanggongming_fu, itm_iron_leather_greave],
   str_9 | agi_7 | int_7 | cha_7|level(5), wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (30) | wp_crossbow (40) | wp_throwing (30),
   knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_tactics_1|knows_persuasion_1|knows_memory_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_1,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["states_rider","States Rider","States Riders", #自由城邦骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_heater_d, itm_qinse_danshoujian, itm_sword_medieval_d_long, itm_bastard_sword_a, itm_bascinet_2, itm_banded_armor, itm_iron_leather_greave, itm_leather_gloves, itm_huise_ma, itm_light_lance, itm_lance, itm_shenseliema],
   str_13 | agi_10 | int_9 | cha_8|level(14), wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (110) | wp_crossbow (120) | wp_throwing (110),
   knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_2|knows_shield_3|knows_athletics_3|knows_riding_3|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tactics_3|knows_pathfinding_1|knows_inventory_management_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["states_light_cavalry","States Light Cavalry","States Light Cavalris", #自由城邦轻骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_heater_cav_a, itm_tiehuan_danshoujian, itm_dingci_lengtouchui, itm_bascinet_2, itm_cuir_bouilli, itm_steel_leather_boot, itm_scale_gauntlets, itm_zongse_dingshi_pijia_liema, itm_zongse_pijia_liema, itm_lance, itm_heavy_lance],
   str_17 | agi_14 | int_11 | cha_10|level(23), wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (210) | wp_throwing (200),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_4|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["states_heavy_cavalry","States Heavy Cavalry","States Heavy Cavalris", #自由城邦重骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_8,
   [itm_tiehuan_danshoujian, itm_tab_shield_heater_cav_b, itm_bascinet_3, itm_cuir_bouilli, itm_mail_boots, itm_gauntlets, itm_pitie_liema, itm_great_lance, itm_heibai_wenqiqiang],
   str_21 | agi_18 | int_13 | cha_11|level(33), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (290) | wp_crossbow (290) | wp_throwing (290),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_4|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["states_crossbow_cavalry","States Crossbow Cavalry","States Crossbow Cavalris", #自由城邦弩骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_heater_cav_b, itm_tiehuan_danshoujian, itm_birch_crossbow, itm_steel_bolts, itm_bascinet_3, itm_cuir_bouilli, itm_mail_boots, itm_gauntlets, itm_pitie_liema],
   str_20 | agi_18 | int_13 | cha_11|level(32), wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (290) | wp_crossbow (300) | wp_throwing (290),
   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_4|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],

  ["states_skirmisher","States Skirmisher","States Skirmishers", #自由城邦散兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_pavise_c, itm_pike, itm_crossbow, itm_bolts, itm_helmet_with_neckguard, itm_banded_armor, itm_mail_chausses, itm_luzhi_bikai],
   str_13 | agi_10 | int_9 | cha_8|level(15), wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (120) | wp_crossbow (130) | wp_throwing (120),
   knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_2|knows_shield_3|knows_athletics_3|knows_riding_3|knows_horse_archery_2|knows_looting_1|knows_trainer_1|knows_tactics_3|knows_pathfinding_1|knows_inventory_management_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_2|knows_prisoner_management_2|knows_leadership_3|knows_trade_1,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["states_crossbow_ranger","States Crossbow Ranger","States Crossbow Rangers", #自由城邦游击弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_pavise_d, itm_changren_qiang, itm_heavy_crossbow, itm_steel_bolts, itm_guard_helmet, itm_banded_armor, itm_steel_leather_boot, itm_scale_gauntlets],
   str_17 | agi_14 | int_11 | cha_10|level(24), wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (210) | wp_crossbow (220) | wp_throwing (210),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_4|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_maneuver, #机动支援
  ],
  ["states_heavy_armored_crossbowman","States Heavy Armored Crossbowman","States Heavy Armored Crossbowmen", #自由城邦重装弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_pavise_d, itm_changren_qiang, itm_oak_corssbow, itm_steel_bolts, itm_yuanding_lianjiakui, itm_cuir_bouilli, itm_splinted_greaves, itm_lamellar_gauntlets],
   str_21 | agi_18 | int_13 | cha_11|level(31), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (290) | wp_throwing (280),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_5|knows_athletics_4|knows_riding_5|knows_horse_archery_4|knows_looting_3|knows_trainer_3|knows_tracking_2|knows_tactics_4|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["states_fortress_crossbowman","States Fortress Crossbowman","States Fortress Crossbowmen", #自由城邦堡垒弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_pavise_d, itm_awlpike, itm_tiegu_nu, itm_steel_bolts, itm_yuanding_lianjiakui, itm_ziyouchengbang_bibanlian, itm_splinted_greaves, itm_gauntlets],
   str_26 | agi_22 | int_16 | cha_13|level(40), wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (370) | wp_throwing (360),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_6|knows_horse_archery_7|knows_looting_4|knows_trainer_5|knows_tracking_4|knows_tactics_6|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_4|knows_memory_9|knows_study_4|knows_devout_5|knows_prisoner_management_6|knows_leadership_9|knows_trade_3,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["states_nobility","States Nobility","States Nobility", #自由城邦贵族
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_kingdom_8,
   [itm_tab_shield_heater_c, itm_jinse_guizujian, itm_awlpike_long, itm_mao_guokui, itm_cuir_bouilli, itm_steel_leather_boot, itm_leather_gloves],
   str_17 | agi_14 | int_11 | cha_10|level(20), wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (190) | wp_throwing (180),
   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_4|knows_looting_2|knows_trainer_3|knows_tracking_2|knows_tactics_5|knows_pathfinding_3|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_2|knows_devout_3|knows_prisoner_management_4|knows_leadership_6|knows_trade_2,
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  ["states_nobility_crossbowman","States Nobility Crossbowman","States Nobility Crossbowmen", #自由城邦贵族弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_jinse_bubingjian, itm_tab_shield_heater_d, itm_sanbing_nu, itm_steel_bolts, itm_jiaqiang_guokui, itm_ziyouchengbang_bibanlian, itm_mail_boots, itm_scale_gauntlets],
   str_23 | agi_19 | int_13 | cha_11|level(30), wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (290) | wp_throwing (280),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_6|knows_looting_3|knows_trainer_5|knows_tracking_3|knows_tactics_7|knows_pathfinding_4|knows_spotting_3|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_5|knows_memory_8|knows_study_3|knows_devout_4|knows_prisoner_management_5|knows_leadership_9|knows_trade_3,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["states_fortress_ballistaman","States Fortress Ballistaman","States Fortress Ballistamen", #自由城邦堡垒弩炮手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_jinshi_yizhangjian, itm_tab_shield_heater_cav_b, itm_winch_crossbow, itm_baiyu_nushi, itm_gangshizi_tongkui, itm_baoleihucong_jia, itm_iron_greaves, itm_gauntlets],
   str_29 | agi_25 | int_16 | cha_13|level(42), wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (410) | wp_throwing (400),
   knows_ironflesh_9|knows_power_strike_10|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_8|knows_shield_9|knows_athletics_9|knows_riding_9|knows_horse_archery_8|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_8|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_7|knows_memory_10|knows_study_4|knows_devout_5|knows_prisoner_management_6|knows_leadership_11|knows_trade_4,
   man_face_middle_1, man_face_older_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

#权杖下马骑士团
  ["scepter_dismounted_knight","Scepter Dismounted Knight","States Dismounted Knights", #权杖下马骑士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_dismounted_knight_halberd, itm_heiyu_changmian_jianzuikui, itm_scepter_heavy_plate, itm_state_knight_boot, itm_scepter_gauntlet, itm_scepter_tower_shield],
   str_32 | agi_29 | int_20 | cha_18|level(48), wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_9|knows_shield_9|knows_athletics_8|knows_riding_7|knows_horse_archery_9|knows_looting_4|knows_trainer_6|knows_tracking_4|knows_tactics_7|knows_pathfinding_5|knows_spotting_4|knows_inventory_management_6|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_5|knows_array_arrangement_6|knows_memory_9|knows_study_5|knows_devout_8|knows_prisoner_management_6|knows_leadership_10|knows_trade_4,
   man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["scepter_knight_captain","Scepter Knight Captain","Scepter Knight Captains", #权杖骑士长
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_gangshizi_yi_tongkui, itm_scepter_knight_captain_plate, itm_state_knight_boot, itm_scepter_gauntlet, itm_scepter_tower_shield, itm_simple_plate_mountanic_horse_yellow],
   str_40 | agi_36 | int_24 | cha_22|level(54), wp_one_handed (540) | wp_two_handed (540) | wp_polearm (540) | wp_archery (540) | wp_crossbow (540) | wp_throwing (540),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_11|knows_shield_10|knows_athletics_9|knows_riding_8|knows_horse_archery_10|knows_looting_5|knows_trainer_7|knows_tracking_5|knows_tactics_8|knows_pathfinding_6|knows_spotting_5|knows_inventory_management_7|knows_wound_treatment_4|knows_surgery_5|knows_first_aid_5|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_8|knows_memory_10|knows_study_7|knows_devout_9|knows_prisoner_management_8|knows_leadership_12|knows_trade_4,
   man_face_middle_1, man_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],

  ["fasces_consul","Fasces Consul","Fasces Consuls", #束杖执政官
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_jiqiao_nu, itm_graghite_steel_bolts, itm_jinseshoubanjian, itm_red_bustling_helmet, itm_fasces_plate, itm_consul_heavy_boot, itm_huali_shalouhushou, itm_highknight_warhorse, itm_scepter_tower_shield],
   str_70 | agi_61 | int_15 | cha_21|level(63),wp_one_handed (520) | wp_two_handed (520) | wp_polearm (520) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500), 
   knows_ironflesh_15|knows_power_strike_15|knows_power_throw_8|knows_power_draw_6|knows_weapon_master_9|knows_shield_8|knows_athletics_8|knows_riding_8|knows_horse_archery_9|knows_looting_8|knows_trainer_7|knows_tracking_6|knows_tactics_6|knows_pathfinding_7|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_4|knows_surgery_3|knows_first_aid_4|knows_engineer_4|knows_persuasion_9|knows_array_arrangement_10|knows_memory_13|knows_study_15|knows_devout_2|knows_prisoner_management_9|knows_leadership_13|knows_trade_8, 
   man_face_middle_1, man_face_older_2, 0, 
   0, 0, itm_function_hero_agent, #英雄单位
  ],



#————————————————————————————————归宗派—————————————————————————————————
##
#古力奥妖妇团
  ["guilio_vamp","Guilio Vamp","Guilio Vamps", #古力奥妖妇
   tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0, 0, fac_kingdom_8,
   [itm_lyre, itm_assassination_crossbow, itm_graghite_steel_bolts, itm_yishith_dagger, itm_xiunv_toujin, itm_slaveholder_tight_chain_armor, itm_splinted_leather_greaves, itm_fenzhi_pishoutao],
   str_22 | agi_18 | int_17 | cha_16|level(40), wp_one_handed (370) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (380) | wp_throwing (350),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_6|knows_shield_4|knows_athletics_8|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_4|knows_tracking_5|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_7|knows_array_arrangement_1|knows_memory_7|knows_study_4|knows_devout_5|knows_prisoner_management_4|knows_leadership_6|knows_trade_5,
   woman_face_1, woman_face_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],



#————————————————————————————————西求派—————————————————————————————————
##
#裂空狙击团
  ["skytear_sniper","Skytear Sniper","Skytear Snipers", #裂空狙击手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0, 0, fac_kingdom_8,
   [itm_two_handed_cleaver, itm_graghite_steel_bolts, itm_assassination_sniper_crossbow, itm_byzantion_helmet_a, itm_brigandine_red, itm_steel_leather_boot, itm_leather_gloves],
   str_25 | agi_21 | int_14 | cha_9|level(40), wp_one_handed (350) | wp_two_handed (370) | wp_polearm (350) | wp_archery (350) | wp_crossbow (380) | wp_throwing (350),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_8|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_4|knows_tracking_5|knows_tactics_4|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_4|knows_devout_5|knows_prisoner_management_4|knows_leadership_6|knows_trade_5,
   man_face_middle_1, man_face_older_2, 0, 
   0, 0, itm_function_assassin, #刺客
  ],



#————————————————————————————————愚人派—————————————————————————————————
##
  ["sheriff_rider","Sheriff Rider","Sheriff Riders", #治安骑警
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_manhunters,
   [itm_qijing_lengtouchui, itm_tab_shield_heater_cav_a, itm_mao_guokui, itm_surcoat_over_mail, itm_mail_chausses, itm_scale_gauntlets, itm_huangbai_pijia_liema],
   str_26 | agi_22 | int_15 | cha_12|level(40), wp_one_handed (370) | wp_two_handed (370) | wp_polearm (370) | wp_archery (370) | wp_crossbow (370) | wp_throwing (370),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_8|knows_riding_4|knows_horse_archery_7|knows_looting_5|knows_trainer_4|knows_tracking_5|knows_tactics_6|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_4|knows_devout_5|knows_prisoner_management_6|knows_leadership_8|knows_trade_5,
   man_face_middle_1, man_face_older_2, 0, 
   0, 0, itm_function_commander, #指挥
  ],



#————————————————————————————————裁决之锤—————————————————————————————————
##
  ["exorcism_novice","Exorcism Novice","Exorcism Novices", #驱魔新人
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0, 0, fac_hammer_of_judgment,
   [itm_changren_qiang, itm_exorcist_battle_shield, itm_padded_leather, itm_leather_boots],
   str_11 | agi_8 | int_8 | cha_6|level(14), wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (110) | wp_crossbow (110) | wp_throwing (110),
   knows_ironflesh_3|knows_power_strike_2|knows_shield_1|knows_athletics_1|knows_riding_1|knows_shield_2|knows_trainer_1|knows_persuasion_1|knows_memory_2|knows_study_4|knows_devout_9|knows_prisoner_management_1|knows_leadership_1, 
   man_face_young_1, man_face_younger_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["exorcism_hunter","Exorcism Hunter","Exorcism Hunters", #驱魔猎人
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_hammer_of_judgment,
   [itm_silver_plated_sword, itm_exorcist_battle_shield, itm_yuanding_limao, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_jacket],
   str_15 | agi_12 | int_11 | cha_8|level(21), wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),
   knows_ironflesh_5|knows_power_strike_4|knows_power_draw_2|knows_weapon_master_3|knows_shield_5|knows_athletics_3|knows_riding_2|knows_horse_archery_3|knows_looting_1|knows_trainer_3|knows_tracking_1|knows_tactics_3|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_5|knows_devout_10|knows_prisoner_management_3|knows_leadership_4|knows_trade_2, 
   man_face_young_1, man_face_younger_2, 0, 
   0, 0, itm_function_combat, #格斗
  ],
  ["exorcism_archer","Exorcism Archer","Exorcism Archers", #驱魔射手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_hammer_of_judgment,
   [itm_silver_plated_sword, itm_silver_bolts, itm_exorcist_kite_shield, itm_lightweight_winch_crossbow, itm_zongse_gongmingmao, itm_jugdement_light_armor, itm_splinted_leather_greaves, itm_leather_gloves],
   str_20 | agi_17 | int_14 | cha_10|level(28), wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (260) | wp_throwing (250),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_5|knows_shield_7|knows_athletics_4|knows_riding_2|knows_horse_archery_4|knows_looting_2|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_5|knows_study_3|knows_devout_11|knows_prisoner_management_4|knows_leadership_6|knows_trade_3, 
   man_face_young_1, man_face_younger_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
  ["judgment_ranger","Judgment Ranger","Judgment Rangers", #裁决游侠
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_hammer_of_judgment,
   [itm_silver_bolts, itm_silver_plated_battle_sword, itm_guizu_qinnu, itm_zongse_gongmingmao, itm_jugdement_middle_armor, itm_iron_leather_boot, itm_leather_gloves, itm_exorcist_steel_shield],
   str_24 | agi_21 | int_18 | cha_13|level(36), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (340) | wp_throwing (330),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_6|knows_shield_8|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_3|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_6|knows_study_6|knows_devout_12|knows_prisoner_management_5|knows_leadership_7|knows_trade_4, 
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],
  ["judgment_pursuer","Judgment Pursuer","Judgment Pursuers", #裁决猎寻
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
   0, 0, fac_hammer_of_judgment,
   [itm_silver_bolts, itm_silver_plated_sabre, itm_jiqiao_nu, itm_zhongxing_fangmainkui1, itm_jugdement_middle_armor, itm_mail_boots, itm_fenzhi_dingshishoutao, itm_shenseliema, itm_exorcist_steel_shield],
   str_29 | agi_26 | int_22 | cha_16|level(48), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (460) | wp_throwing (450),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_8|knows_shield_9|knows_athletics_7|knows_riding_7|knows_horse_archery_7|knows_looting_4|knows_trainer_5|knows_tracking_3|knows_tactics_5|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_8|knows_study_7|knows_devout_12|knows_prisoner_management_6|knows_leadership_8|knows_trade_4, 
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_flat_fire, #平射火力
  ],

  ["judgment_knight","Judgment Knight","Judgment Knights", #裁决骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0, 0, fac_hammer_of_judgment,
   [itm_baptized_demon_hunting_sword, itm_qinse_lengtouchui, itm_zhongxing_fangmainkui, itm_jugdement_heavy_plate, itm_papal_elite_knight_boot, itm_gauntlets, itm_exorcist_chain_armor_mountain_horse, itm_exorcist_steel_shield],
   str_34 | agi_31 | int_26 | cha_18|level(52), wp_one_handed (490) | wp_two_handed (490) | wp_polearm (490) | wp_archery (490) | wp_crossbow (500) | wp_throwing (490),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_9|knows_shield_10|knows_athletics_8|knows_riding_10|knows_horse_archery_9|knows_looting_5|knows_trainer_6|knows_tracking_4|knows_tactics_6|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_5|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_4|knows_engineer_3|knows_persuasion_7|knows_array_arrangement_3|knows_memory_10|knows_study_10|knows_devout_13|knows_prisoner_management_7|knows_leadership_10|knows_trade_5,
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_strike, #突击
  ],


  ["citizen_messenger","Citizen Messenger","Citizen Messengers", #城邦信使
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, 
   0, 0, fac_kingdom_8,
   [itm_bolts, itm_birch_crossbow, itm_tab_shield_heater_cav_a, itm_jinshi_cejian, itm_qianse_longxikui, itm_cuir_bouilli, itm_steel_leather_boot, itm_scale_gauntlets, itm_zongse_pijia_liema],
   str_20 | agi_16 | int_15 | cha_10|level(35), wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (280) | wp_throwing (250),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_4|knows_riding_4|knows_horse_archery_5|knows_looting_3|knows_trainer_2|knows_tracking_3|knows_tactics_3|knows_pathfinding_6|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_4|knows_devout_7|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   man_face_young_1, man_face_middle_2, 0, 
   0, 0, itm_function_reconnaissance, #侦察
  ],
 ["citizen_deserter","Citizen Deserter","Citizen Deserters",tf_hero|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
  def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,powell_face_young_1, powell_face_old_2],

#以上为各国家军队




#############################################################土匪##########################################################

  ["looter","Looter","Looters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_hatchet, itm_club, itm_butchering_knife, itm_falchion, itm_rawhide_coat, itm_stones, itm_nomad_armor, itm_nomad_armor, itm_woolen_cap, itm_woolen_cap, itm_nomad_boots, itm_wrapping_boots, itm_short_tunic, itm_red_tunic, itm_green_tunic, itm_blue_tunic, itm_wooden_stick, itm_cudgel, itm_hammer, itm_winged_mace, itm_spiked_mace, itm_scythe, itm_pitch_fork, itm_staff],
   str_7 | agi_6 | int_5 | cha_3|level(5),wp(65),knows_ironflesh_1|knows_power_throw_1|knows_shield_1,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_spiked_mace, itm_sword_viking_1, itm_falchion, itm_nordic_shield, itm_rawhide_coat, itm_leather_cap, itm_leather_jerkin, itm_nomad_armor, itm_nomad_boots, itm_wrapping_boots, itm_gambeson, itm_blue_gambeson, itm_red_gambeson, itm_padded_cloth, itm_aketon_green, itm_leather_jerkin, itm_nomad_vest, itm_ragged_outfit, itm_padded_leather, itm_leather_steppe_cap_a, itm_leather_steppe_cap_b, itm_leather_steppe_cap_c, itm_leather_warrior_cap, itm_skullcap, itm_sword_medieval_a, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_sarranid_two_handed_mace_1, itm_sarranid_mace_1, itm_scythe, itm_staff, itm_quarter_staff, itm_shortened_spear, itm_spear],
   str_10 | agi_9 | int_5 | cha_3|level(15),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (135) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_horse_archery_1|knows_riding_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_outlaws_bandit,
   [itm_leather_warrior_cap, itm_skullcap, itm_mail_coif, itm_footman_helmet, itm_nasal_helmet, itm_norman_helmet, itm_padded_leather, itm_tribal_warrior_outfit, itm_nomad_robe, itm_studded_leather_coat, itm_byrnie, itm_haubergeon, itm_mail_shirt, itm_mail_hauberk, itm_padded_leather, itm_tribal_warrior_outfit, itm_nomad_robe, itm_studded_leather_coat, itm_leather_boots, itm_splinted_leather_greaves, itm_mail_chausses, itm_leather_gloves, itm_sumpter_horse, itm_saddle_horse, itm_steppe_horse, itm_military_hammer, itm_fighting_pick, itm_spiked_club, itm_scimitar, itm_arabian_sword_a, itm_hand_axe, itm_fighting_axe, itm_bastard_sword_a, itm_sword_medieval_c, itm_sword_medieval_c_small, itm_sword_viking_2, itm_sword_viking_2_small, itm_sword_khergit_1, itm_sword_khergit_2, itm_boar_spear, itm_jousting_lance, itm_double_sided_lance, itm_light_lance, itm_nordic_shield, itm_fur_covered_shield, itm_plate_covered_round_shield, itm_leather_covered_round_shield, itm_beast_skin_round_shield, itm_dark_lion_fan_shaped_shield, itm_throwing_knives, itm_throwing_daggers],
   str_14 | agi_11 | int_6 | cha_6|level(20),wp_one_handed (175) | wp_two_handed (175) | wp_polearm (175) | wp_archery (175) | wp_crossbow (175) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_2|knows_athletics_4|knows_horse_archery_3|knows_riding_2,bandit_face1, bandit_face2],
  ["bandit_leader","Bandit Leader","Bandit Leaders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_outlaws_bandit,
   [itm_mountain_horse, itm_hunter, itm_warhorse, itm_splinted_greaves, itm_mail_boots, itm_mail_mittens, itm_scale_gauntlets, itm_brigandine_red, itm_lamellar_armor, itm_spiked_helmet, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_great_helmet, itm_scimitar_b, itm_arabian_sword_b, itm_sarranid_cavalry_sword, itm_great_sword, itm_axe, itm_voulge, itm_sword_two_handed_a, itm_military_cleaver_b, itm_military_cleaver_c, itm_long_bardiche, itm_great_long_bardiche, itm_lance, itm_heavy_lance, itm_jarid, itm_stones, itm_throwing_knives],
   str_25 | agi_15 | int_9 | cha_5|level(35),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_horse_archery_6|knows_riding_5,bandit_face1, bandit_face2],



############################################################山林匪徒##########################################################

  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws_forest,
   [itm_sword_viking_1, itm_spear, itm_winged_mace, itm_maul, itm_falchion, itm_javelin, itm_felt_hat, itm_head_wrappings, itm_skullcap, itm_ragged_outfit, itm_rawhide_coat, itm_leather_armor, itm_hide_boots, itm_nomad_boots, itm_arrows, itm_khergit_arrows, itm_arrows, itm_khergit_arrows, itm_hunting_bow, itm_short_bow, itm_nomad_bow, itm_nomad_bow, itm_bamboo_spear, itm_sword_medieval_c_small, itm_sword_medieval_c_long],
   str_11 | agi_10 | int_6 | cha_6|level(16),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (160) | wp_crossbow (160) | wp_throwing (130),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_1|knows_athletics_2|knows_horse_archery_3|knows_riding_1,bandit_face1, bandit_face2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws_forest,
   [itm_bolts, itm_khergit_arrows, itm_barbed_arrows, itm_hunting_crossbow, itm_light_crossbow, itm_hunting_crossbow, itm_hunting_crossbow, itm_light_crossbow, itm_hunting_crossbow, itm_nomad_bow, itm_war_spear, itm_ashwood_pike, itm_awlpike, itm_mail_coif, itm_footman_helmet, itm_nasal_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_maopipijia_pijia, itm_linjiapijian_dingshijia, itm_maopipijia_linjia, itm_leather_boots, itm_splinted_leather_greaves, itm_leather_gloves],
   str_15 | agi_17 | int_7 | cha_7|level(25),wp_one_handed (190) | wp_two_handed (190) | wp_polearm (200) | wp_archery (210) | wp_crossbow (210) | wp_throwing (130),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_2|knows_power_draw_5|knows_weapon_master_3|knows_shield_3|knows_athletics_6|knows_horse_archery_3|knows_riding_2,bandit_face1, bandit_face2],



############################################################安基亚蛮族##########################################################

  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws_ankiya,
   [itm_axe, itm_hatchet, itm_spear, itm_tab_shield_round_a, itm_tab_shield_round_a, itm_hide_boots, itm_nomad_boots, itm_stones, itm_throwing_knives, itm_khergit_armor, itm_rawhide_coat],
   str_13 | agi_8 | int_6 | cha_6|level(10),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (90) | wp_throwing (90),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_1|knows_athletics_2,diemer_face_younger_1, diemer_face_old_2],
  ["ankiya_barbarian","Ankiya Barbarian","Ankiya Barbarians",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws_ankiya,
   [itm_hide_boots, itm_nomad_boots, itm_manzu_shiqiang, itm_manzushoufu, itm_tribal_fur_coat, itm_tribal_warrior_outfit, itm_fur_covered_shield, itm_beast_skin_round_shield, itm_fur_hat, itm_nomad_cap, itm_leather_steppe_cap_c, itm_leather_warrior_cap],
   str_18 | agi_12 | int_6 | cha_6|level(20),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_2|knows_shield_3|knows_athletics_4|knows_riding_4|knows_horse_archery_4,diemer_face_young_1, diemer_face_old_2],
  ["ankiya_warrior","Ankiya Warrior","Ankiya Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws_ankiya,
   [itm_manzu_pixue, itm_manzushoufu, itm_manzu_gangfu, itm_manzu_chui, itm_tribal_fur_coat, itm_beast_skin_round_shield, itm_leather_warrior_cap, itm_skullcap],
   str_25 | agi_16 | int_8 | cha_8|level(30),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_3|knows_shield_3|knows_athletics_4|knows_riding_4|knows_horse_archery_4,diemer_face_middle_1, diemer_face_old_2],
  ["ankiya_leader","Ankiya Leader","Ankiya Leaders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_outlaws_ankiya,
   [itm_manzu_pixue, itm_manzu_shoutao, itm_manzu_zhongjia, itm_babarian_stone_sword, itm_hunter, itm_vaegir_noble_helmet, itm_vaegir_war_helmet, itm_vaegir_mask, itm_beast_skin_round_shield, itm_manzu_gangfu, itm_manzu_shiqiang],
   str_34 | agi_21 | int_12 | cha_10|level(42),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),knows_ironflesh_11|knows_power_strike_10|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_6,diemer_face_middle_1, diemer_face_middle_2],
  ["ankiya_looter_leader","Ankiya Looter Leader","Ankiya Looter Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws_ankiya,
   [itm_manzu_chui, itm_manzu_zhongjia, itm_manzu_gangfu, itm_manzu_shoutao, itm_manzu_pixue, itm_guizu_wumainkui, itm_yaunding_wumiankui],
   str_35 | agi_26 | int_12 | cha_10|level(45),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),knows_ironflesh_11|knows_power_strike_11|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_5|knows_shield_4|knows_athletics_7|knows_riding_5|knows_horse_archery_4,diemer_face_young_1, diemer_face_middle_2],
  ["ankiya_shaman","Ankiya Shaman","Ankiya Shamans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_outlaws_ankiya,
   [itm_wailai_manzu_jia, itm_wailai_manzuxue, itm_saman_kui, itm_leather_gloves, itm_shashijian, itm_nomad_bow, itm_barbed_arrows, itm_bodkin_arrows, itm_barbed_arrows, itm_bodkin_arrows, itm_courser, itm_hunter, itm_beast_skin_round_shield],
   str_28 | agi_18 | int_15 | cha_6|level(35),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_3|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_5,diemer_face_old_1, diemer_face_older_2],



###########################################################热砂的末裔##########################################################

  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws_desert,
   [itm_luotuo, itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b, itm_skirmisher_armor, itm_sarranid_felt_hat, itm_turban, itm_desert_turban, itm_sarranid_warrior_cap, itm_arabian_sword_a, itm_light_lance, itm_throwing_knives, itm_leather_gloves, itm_nomad_boots],
   str_11 | agi_10 | int_6 | cha_5|level(15),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (135) | wp_archery (135) | wp_crossbow (135) | wp_throwing (135),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_1|knows_athletics_2|knows_riding_3|knows_horse_archery_3,kouruto_face_young_1, kouruto_face_old_2],
  ["desert_thief","Desert Thief","Desert Thieves",tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws_desert,
   [itm_arrows, itm_winged_mace, itm_jarid, itm_nomad_bow, itm_short_bow, itm_jarid, itm_leather_covered_round_shield, itm_leather_covered_round_shield, itm_saddle_horse, itm_arabian_horse_a, itm_archers_vest, itm_sarranid_leather_armor, itm_sarranid_cavalry_robe, itm_sarranid_warrior_cap, itm_sarranid_horseman_helmet, itm_sarranid_helmet1, itm_double_sided_lance, itm_lance, itm_arabian_sword_b, itm_mail_mittens, itm_leather_boots, itm_splinted_leather_greaves],
   str_15 | agi_10 | int_6 | cha_6|level(20),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_5|knows_horse_archery_4,kouruto_face_young_1, kouruto_face_old_2],
  ["desert_leader","Desert Leader","Desert Leaders",tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws_desert,
   [itm_arabian_armor_b, itm_sarranid_helmet1, itm_sarranid_mail_coif, itm_sarranid_veiled_helmet, itm_heavy_lance, itm_strong_bow, itm_khergit_arrows, itm_barbed_arrows, itm_bodkin_arrows, itm_sarranid_cavalry_sword, itm_arabian_sword_d, itm_warhorse_sarranid, itm_warhorse_steppe, itm_lamellar_gauntlets, itm_splinted_greaves, itm_mail_boots],
   str_21 | agi_21 | int_9 | cha_9|level(30),wp_one_handed (290) | wp_two_handed (290) | wp_polearm (290) | wp_archery (290) | wp_crossbow (290) | wp_throwing (290),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_6|knows_shield_5|knows_athletics_6|knows_riding_7|knows_horse_archery_7,kouruto_face_middle_1, kouruto_face_old_2],



#############################################################海渊异种##########################################################

  ["abyssal_sailor","Abyssal sailor","Abyssal sailors",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws_abyssal,
   [itm_studded_leather_coat, itm_byrnie, itm_leather_boots, itm_nasal_helmet, itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_hatchet, itm_hand_axe, itm_fighting_axe, itm_axe, itm_light_throwing_axes],
   str_18 | agi_12 | int_6 | cha_6|level(15),wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_weapon_master_3|knows_shield_2|knows_athletics_3,diemer_face_younger_1, diemer_face_young_2],
  ["abyssal_axeman","abyssal axeman","abyssal axemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws_abyssal,
   [itm_light_throwing_axes, itm_wooden_shield, itm_nordic_shield, itm_axe, itm_one_handed_war_axe_a, itm_one_handed_battle_axe_a, itm_two_handed_axe, itm_nordic_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_leather_gloves, itm_leather_boots, itm_byrnie, itm_westcoast_iron_ring_cotton_armor, itm_westcoast_leather_scale_armor, itm_westcoast_nailed_leather_armor, itm_tab_shield_round_a, itm_tab_shield_round_b],
   str_21 | agi_13 | int_6 | cha_6|level(20),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),knows_ironflesh_6|knows_power_strike_5|knows_power_throw_5|knows_weapon_master_4|knows_shield_3|knows_athletics_5,diemer_face_young_1, diemer_face_middle_2],
  ["abyssal_priate_warrior","Abyssal Priate Warrior","Abyssal Priate Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_outlaws_abyssal,
   [itm_westcoast_covered_chain_armor_robe, itm_westcoast_leather_armed_clothing, itm_zongselianjia_shan, itm_scale_gauntlets, itm_splinted_leather_greaves, itm_splinted_greaves, itm_nordic_huscarl_helmet, itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_one_handed_battle_axe_b, itm_two_handed_battle_axe_2, itm_long_axe, itm_long_axe_alt, itm_sarranid_axe_a, itm_sarranid_axe_b, itm_throwing_axes, itm_throwing_axes, itm_throwing_axes, itm_throwing_axes, itm_tab_shield_round_c, itm_tab_shield_round_d, itm_qinliang_shuangshoufu, itm_xihai_niujiaokui],
   str_26 | agi_16 | int_7 | cha_7|level(30),wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_6,diemer_face_middle_1, diemer_face_old_2],
  ["abyssal_surge_prowessman","Abyssal Surge Prowessman","Abyssal Surge Prowessmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_outlaws_abyssal,
   [itm_tab_shield_round_e, itm_splinted_greaves, itm_scale_gauntlets, itm_nordic_warlord_helmet, itm_jinse_jufu, itm_haishenfu, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_hongse_zhabanjia],
   str_33 | agi_22 | int_10 | cha_14|level(42),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),knows_ironflesh_11|knows_power_strike_11|knows_power_throw_11|knows_weapon_master_9|knows_shield_6|knows_athletics_8,diemer_face_young_1, diemer_face_old_2],
  ["abyssal_horseman","Abyssal Horseman","Abyssal Horsemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_mounted|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_outlaws_abyssal,
   [itm_xihan_lingjiamao, itm_xihai_niujiaokui, itm_mail_chausses, itm_splinted_greaves, itm_leather_gloves, itm_mail_mittens, itm_lingjia_pao, itm_quanshen_lianjai, itm_saddle_horse, itm_sumpter_horse, itm_simple_carving_axe, itm_jianyi_danshoufu, itm_jianyi_shuangshoufu, itm_jainyi_xifangfu, itm_jainyi_shuangrenfu, itm_tab_shield_small_round_a, itm_tab_shield_small_round_b],
   str_21 | agi_14 | int_7 | cha_7|level(25),wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (140) | wp_crossbow (140) | wp_throwing (210),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_horse_archery_1|knows_riding_3,diemer_face_young_1, diemer_face_old_2],
  ["abyssal_plunder_captain","Abyssal Plunder Captain","Abyssal Plunder Captain",tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_outlaws_abyssal,
   [itm_xihai_shoulingkui, itm_jianyixihai_shoulingkui, itm_diecengpilian_jia, itm_mail_boots, itm_mail_mittens, itm_scale_gauntlets, itm_huise_ma, itm_heise_ma, itm_jixingfu, itm_blue_breeze_round_shield],
   str_27 | agi_17 | int_9 | cha_9|level(38),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (200) | wp_archery (140) | wp_crossbow (140) | wp_throwing (330),knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_horse_archery_2|knows_riding_5,diemer_face_middle_1, diemer_face_older_2],
  ["abyssal_axe_thrower","Abyssal Axe Thrower","Abyssal Axe Throwers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws_abyssal,
   [itm_throwing_axes, itm_heavy_throwing_axes, itm_light_throwing_axes, itm_throwing_axes, itm_heavy_throwing_axes, itm_heavy_throwing_axes, itm_leather_gloves, itm_leather_boots, itm_haubergeon, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_hatchet],
   str_19 | agi_14 | int_6 | cha_6|level(25),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (120) | wp_crossbow (120) | wp_throwing (210),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_7|knows_weapon_master_4|knows_shield_2|knows_athletics_4,diemer_face_young_1, diemer_face_middle_2],



#############################################################法外骑士团##########################################################

  ["outlaw_swordman","Outlaw Swordman","Outlaw Swordmen",tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws_robber_knight,
   [itm_wulaizhe_lianjia, itm_dingshi_fupi_duanlianjia, itm_quanshen_lianjai, itm_lanse_xiongjia, itm_hongse_xiongjia, itm_leather_gloves, itm_leather_boots, itm_mail_coif, itm_footman_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_kettle_hat, itm_bastard_sword_a, itm_bastard_sword_b, itm_simple_pegasus_skoutarion, itm_simple_green_wind_skoutarion, itm_simple_red_dragon_skoutarion, itm_simple_baptism_skoutarion, itm_simple_red_wind_skoutarion, itm_griffon_skoutarion],
   str_12 | agi_9 | int_6 | cha_6|level(15),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_1,man_face_younger_1, man_face_middle_2],
  ["outlaw_infantry","Outlaw Infantry","Outlaw Infantrys",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws_robber_knight,
   [itm_heise_zaoqi_banjia, itm_heibai_zaoqi_banjia, itm_lanse_zaoqi_banjia, itm_hongse_zaoqi_banjia, itm_mogang_zaoqi_banjia, itm_mail_chausses, itm_mail_mittens, itm_qinxing_jixingkui1, itm_zhongxing_fangmainkui, itm_gangtiao_tongkui, itm_ban_qingbiankui, itm_red_blue_fan_shaped_shield, itm_wildboar_fan_shaped_shield, itm_simple_blue_flower_fan_shaped_shield, itm_simple_papal_fan_shaped_shield, itm_silver_dragon_fan_shaped_shield, itm_half_bird_fan_shaped_shield, itm_blue_lion_fan_shaped_shield, itm_sanjian_qiang, itm_yejian_qiang, itm_changren_qiang, itm_jianyi_yejianqiang],
   str_15 | agi_14 | int_6 | cha_6|level(20),wp_one_handed (200) | wp_two_handed (150) | wp_polearm (200) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_6|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_2,man_face_young_1, man_face_middle_2],
  ["outlaw_horseman","Outlaw Horseman","Outlaw Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws_robber_knight,
   [itm_mail_boots, itm_iron_greaves, itm_mail_mittens, itm_scale_gauntlets, itm_nordic_footman_helmet, itm_vaegir_fur_helmet, itm_vaegir_spiked_helmet, itm_vaegir_lamellar_helmet, itm_vaegir_war_helmet, itm_vaegir_mask, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_shidun_lianjiazhaopao, itm_lvbai_lianjiazhaopao, itm_lvjian_lianjiazhaopao, itm_thunderwing_chain_armor_robe, itm_eagle_chain_armor, itm_jinhua_lianjiazhaopao, itm_hongtiepi_lianjiashan, itm_gongniu_lianjiazhaopao, itm_heibai_lianjiazhaopao, itm_cormorant_chain_armor_robe, itm_eagle_flock_chain_armor_robe, itm_lvlong_lianjaizhaopao, itm_lianghuang_lianjiazhaopao, itm_qingse_lianjiazhaopao, itm_steppe_horse, itm_arabian_horse_a, itm_courser, itm_mountain_horse, itm_hunter, itm_zase_ma, itm_huise_ma, itm_heise_ma, itm_yellow_lion_fan_shaped_shield, itm_red_lion_iron_fan_shaped_shield, itm_blue_flower_fan_shaped_shield, itm_knight_black_white_fan_shaped_shield, itm_demon_fan_shaped_shield, itm_red_blue_fan_shaped_shield, itm_wildboar_fan_shaped_shield, itm_silver_dragon_fan_shaped_shield, itm_blue_lion_fan_shaped_shield, itm_thunderwing_fan_shaped_shield, itm_strengthen_yellow_black_fan_shaped_shield, itm_haze_crow_fan_shaped_shield, itm_griffon_hunting_fan_shaped_shield, itm_double_deer_fan_shaped_shield, itm_bastard_sword_a, itm_bastard_sword_b, itm_honeysuckle_fan_shaped_shield, itm_light_lance, itm_lance],
   str_17 | agi_15 | int_6 | cha_6|level(25),wp_one_handed (220) | wp_two_handed (165) | wp_polearm (220) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_4|knows_athletics_4|knows_riding_4,man_face_middle_1, man_face_old_2],
  ["outlaw_knight","Outlaw Knight","Outlaw Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws_robber_knight,
   [itm_baimian_banlianjia, itm_gouheng_zhongxing_banlianjia, itm_baimian_quanshenbanjia, itm_lanse_quanshenbanjia, itm_hongse_quanshenbanjia, itm_lanbai_jiazhong_banjia, itm_lvbai_jiazhong_banjia, itm_guanze_banjiaxue, itm_wenli_banjiaxue, itm_duangang_banjiaxue, itm_shengtie_banjiaxue, itm_fangxing_bikai, itm_yuanzhi_bikai, itm_lvhua_lianjia_pinyuanma, itm_julu_ianjia_pingyuanma, itm_jiaoma_ianjia_pingyuanma, itm_jinjiu_lianjia_pingyuanma, itm_honghei_lianjia_pingyuanma, itm_ziying_lianjia_pingyuanma, itm_honglong_lianjia_pingyuanma, itm_yinsun_lianjia_pingyuanma, itm_jinyang_lianjia_pinyuanma, itm_xunlu_lianjia_pinyuanma, itm_ziyi_lianjia_pinyuanma, itm_baiyang_lianjia_pinyuanma, itm_hongshi_lianjia_pinyuanma, itm_lanying_lianjia_pinyuanma, itm_heishu_lianjia_pinyuanma, itm_guyongbing_tiekui, itm_guyongbing_zhongkui, itm_hongyu_hue_qingbiankui, itm_jianzuikui, itm_heiyu_jianzuikui, itm_zhumiankui, itm_heiyu_zhumiankui, itm_fangmian_jianzuikui, itm_hongyu_zhumiankui, itm_heavy_lance, itm_great_lance, itm_silver_dragon_fan_shaped_shield, itm_blue_lion_fan_shaped_shield, itm_strengthen_yellow_black_fan_shaped_shield, itm_pride_fan_shaped_shield, itm_yellow_black_fan_shaped_shield, itm_white_dragon_fan_shaped_shield, itm_baptism_noble_fan_shaped_shield, itm_yellow_lion_fan_shaped_shield, itm_haze_crow_fan_shaped_shield, itm_phoenix_fan_shaped_shield, itm_griffon_hunting_fan_shaped_shield, itm_double_deer_fan_shaped_shield, itm_honeysuckle_fan_shaped_shield, itm_ranger_horn_fan_shaped_shield, itm_saints_painting_fan_shaped_shield, itm_military_pick, itm_morningstar, itm_scimitar_b, itm_military_cleaver_c, itm_bastard_sword_b],
   str_21 | agi_17 | int_9 | cha_12|level(40),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_6|knows_shield_5|knows_athletics_5|knows_riding_5,man_face_middle_1, man_face_older_2],
  ["outlaw_bowman","Outlaw Bowman","Outlaw Bowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_outlaws_robber_knight,
   [itm_bastard_sword_a, itm_bastard_sword_b, itm_sword_viking_3, itm_thunderwing_fan_shaped_shield, itm_pride_fan_shaped_shield, itm_yellow_black_fan_shaped_shield, itm_white_dragon_fan_shaped_shield, itm_baptism_noble_fan_shaped_shield, itm_yellow_lion_fan_shaped_shield, itm_haze_crow_fan_shaped_shield, itm_phoenix_fan_shaped_shield, itm_griffon_hunting_fan_shaped_shield, itm_double_deer_fan_shaped_shield, itm_honeysuckle_fan_shaped_shield, itm_quanshen_lianjai, itm_thunderwing_chain_armor_robe, itm_jinhua_lianjiazhaopao, itm_hongtiepi_lianjiashan, itm_gongniu_lianjiazhaopao, itm_eagle_flock_chain_armor_robe, itm_duanxiu_lianjiapao, itm_jianyi_gouheng_zhongxing_banlianjia, itm_mail_mittens, itm_mail_chausses, itm_segmented_helmet, itm_helmet_with_neckguard, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_vaegir_spiked_helmet, itm_guard_helmet, itm_war_bow, itm_long_bow, itm_strong_bow, itm_khergit_arrows, itm_barbed_arrows, itm_bodkin_arrows],
   str_14 | agi_15 | int_6 | cha_6|level(24),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (150) | wp_archery (220) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_1,man_face_young_1, man_face_old_2],



#############################################################权厄之秤##########################################################

  ["thug","Thug","Thugs", #打手
   tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots,
   0,0,fac_outlaws_libra,
   [itm_military_hammer, itm_sarranid_two_handed_mace_1, itm_nordic_archer_helmet, itm_padded_cloth, itm_leather_boots],
   str_15 | agi_12 | int_8 | cha_7|level(22),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (50) | wp_crossbow (50) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_1|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_4|knows_tracking_1|knows_pathfinding_1|knows_spotting_2|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_prisoner_management_1|knows_leadership_2|knows_trade_3,
   man_face_younger_1, man_face_young_2],
  ["libra_hitman","Libra Hitman","Libra Hitmen", #权厄之秤杀手
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_darts, itm_throwing_daggers, itm_leather_covered_round_shield, itm_jinshi_bishou, itm_nordic_veteran_archer_helmet, itm_leather_armor, itm_splinted_leather_greaves, itm_leather_gloves],
   str_17 | agi_15 | int_9 | cha_8|level(29), wp_one_handed (230) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (230),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_5|knows_looting_5|knows_trainer_2|knows_tracking_5|knows_tactics_2|knows_pathfinding_2|knows_spotting_5|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_4,
   man_face_young_1, man_face_middle_2],
  ["alley_hunter","Alley Hunter","Alley Hunters", #黑巷杀手
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_darts, itm_war_darts, itm_steel_shield, itm_jinshi_fanhuajian, itm_bascinet, itm_dingshi_fupi_duanlianjia, itm_steel_leather_boot, itm_fenzhi_huzhishoutao],
   str_23 | agi_22 | int_12 | cha_10|level(40), wp_one_handed (340) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (340),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_7|knows_riding_5|knows_horse_archery_8|knows_looting_8|knows_trainer_4|knows_tracking_7|knows_tactics_4|knows_pathfinding_4|knows_spotting_6|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_5|knows_leadership_4|knows_trade_4,
   man_face_middle_1, man_face_middle_2],
  ["libra_spy","Libra Spy","Libra Spys", #权厄之秤密探
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_darts, itm_war_darts, itm_steel_shield, itm_jinshi_fanhuajian, itm_bascinet, itm_wulaizhe_lianjia, itm_steel_leather_boot, itm_fenzhi_huzhishoutao, itm_steppe_horse],
   str_23 | agi_22 | int_12 | cha_10|level(40), wp_one_handed (340) | wp_two_handed (230) | wp_polearm (230) | wp_archery (230) | wp_crossbow (230) | wp_throwing (340),
   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_6|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_6|knows_riding_7|knows_horse_archery_8|knows_looting_7|knows_trainer_4|knows_tracking_7|knows_tactics_4|knows_pathfinding_4|knows_spotting_8|knows_inventory_management_3|knows_wound_treatment_2|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_4|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_5|knows_leadership_4|knows_trade_4,
   man_face_middle_1, man_face_middle_2],

  ["libra_guard","Libra Guard","Libra Guards", #权厄之秤护卫
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_lance, itm_jinshi_cejian, itm_libra_fan_shaped_shield, itm_wozhuangkui, itm_libra_chest_armor, itm_mail_chausses, itm_mail_mittens, itm_huangshizipijia_ma],
   str_20 | agi_15 | int_8 | cha_7|level(30),wp_one_handed (250) | wp_two_handed (220) | wp_polearm (220) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_2|knows_athletics_4|knows_riding_3|knows_horse_archery_5|knows_looting_4|knows_trainer_3|knows_tracking_3|knows_tactics_4|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_4|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_5|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_4,
   man_face_young_1, man_face_middle_2],
  ["libra_bodyguard_rider","Libra Bodyguard Rider","Libra Bodyguard Riders", #权厄之秤保镖骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_ellite_lance, itm_jinshi_huweijian, itm_libra_fan_shaped_shield, itm_yuanti_kui, itm_libra_plate_chain_composite_armor, itm_iron_greaves, itm_yuanzhi_bikai, itm_heisebanlian_ma],
   str_25 | agi_18 | int_10 | cha_8|level(41),wp_one_handed (350) | wp_two_handed (220) | wp_polearm (220) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_4|knows_athletics_4|knows_riding_5|knows_horse_archery_6|knows_looting_7|knows_trainer_4|knows_tracking_3|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_6|knows_trade_4,
   man_face_middle_1, man_face_old_2],

  ["libra_smuggler","Libra Smuggler","Libra Smugglers", #权厄之秤走私客
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_hunting_crossbow, itm_bolts, itm_wooden_shield, itm_jinshi_bishou, itm_short_tunic, itm_hide_boots],
   str_10 | agi_9 | int_9 | cha_7|level(15),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),
   knows_ironflesh_2|knows_power_strike_1|knows_shield_1|knows_athletics_5|knows_riding_2|knows_horse_archery_2|knows_looting_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_4|knows_first_aid_1|knows_persuasion_3|knows_memory_1|knows_trade_4,
   man_face_younger_1, man_face_older_2],
  ["libra_drug_dealer","Libra Drug Dealer","Libra Drug Dealers",#权厄之秤毒贩
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_crossbow, itm_steel_bolts, itm_tab_shield_heater_b, itm_jinse_minwenjian, itm_helmet_with_neckguard, itm_leather_jacket, itm_leather_boots, itm_leather_gloves],
   str_14 | agi_13 | int_9 | cha_7|level(23),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_6|knows_riding_3|knows_horse_archery_4|knows_looting_6|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_6|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_2|knows_leadership_3|knows_trade_5,
   man_face_young_1, man_face_older_2],
  ["libra_drug_muscleman","Libra Drug Muscleman","Libra Drug Musclemen",#权厄之秤贩毒保镖
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_oak_corssbow, itm_heiyu_nushi, itm_tab_shield_heater_c, itm_jinse_guizujian, itm_guard_helmet, itm_dingshi_fupi_duanlianjia, itm_mail_chausses, itm_scale_gauntlets],
   str_22 | agi_20 | int_12 | cha_7|level(34), wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_6|knows_tactics_3|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_7|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_4|knows_leadership_5|knows_trade_6,
   man_face_young_1, man_face_old_2],
  ["libra_drug_lord","Libra Drug Lord","Libra Drug Lords", #权厄之秤毒枭
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_flintlock_pistol, itm_cartridges, itm_tiegu_nu, itm_heibaiyu_nushi, itm_tab_shield_heater_d, itm_jinse_bubingjian, itm_baotu_jiaokui, itm_dingshi_fupi_qingbanlian, itm_shengtie_banjiaxue, itm_gauntlets],
   str_25 | agi_23 | int_15 | cha_5|level(48), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330) | wp_firearm (100),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_8|knows_spotting_7|knows_inventory_management_9|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_7|knows_leadership_10|knows_trade_9,
   man_face_middle_1, kouruto_face_older_2],

  ["libra_slave_merchant","Libra Slave Merchant","Libra Slave Merchants",#权厄之秤奴贩
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_practice_arrows_2, itm_practice_bow_2, itm_tab_shield_pavise_c, itm_winged_mace, itm_vaegir_war_helmet, itm_padded_leather, itm_splinted_leather_greaves, itm_leather_gloves],
   str_14 | agi_13 | int_9 | cha_7|level(23),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_3|knows_shield_2|knows_athletics_6|knows_riding_3|knows_horse_archery_4|knows_looting_6|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_5|knows_leadership_3|knows_trade_5,
   man_face_young_1, man_face_older_2],
  ["libra_slave_catching_cavalry","Libra Slave Catching Cavalry","Libra Slave Catching Cavalries",#权厄之秤捕奴骑兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_practice_arrows_2, itm_noble_practice_bow, itm_simple_black_white_fan_shaped_shield, itm_qinliang_lengtouchui, itm_yuanpian_humiankui, itm_linjiapijian_dingshijia, itm_splinted_greaves, itm_mail_mittens, itm_saddle_horse],
   str_22 | agi_20 | int_12 | cha_7|level(34), wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_6|knows_tactics_3|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_8|knows_leadership_5|knows_trade_6,
   man_face_young_1, man_face_old_2],
  ["libra_slave_trade_leader","Libra Slave Trade Leader","Libra Slave Trade Leaders", #权厄之秤奴贩首领
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_jousting_lance, itm_tab_shield_heater_cav_b, itm_jinshi_langtouchui, itm_yaunding_wumiankui, itm_shenlan_pilianjia, itm_mail_boots, itm_gauntlets, itm_warhorse],
   str_25 | agi_23 | int_15 | cha_5|level(48), wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_7|knows_shield_8|knows_athletics_7|knows_riding_6|knows_horse_archery_8|knows_looting_9|knows_trainer_5|knows_tracking_5|knows_tactics_5|knows_pathfinding_8|knows_spotting_7|knows_inventory_management_6|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_4|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_6|knows_study_1|knows_devout_1|knows_prisoner_management_14|knows_leadership_10|knows_trade_9,
   man_face_young_1, man_face_old_2],

  ["libra_knight","Libra Knight","Libra Knights", #天秤骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_outlaws_libra,
   [itm_noble_hunting_arrow, itm_iron_bow, itm_libra_fan_shaped_shield, itm_jinseshoubanjian, itm_qinse_qishikui, itm_qingjin_banjia, itm_qinse_banjiaxue, itm_qinse_banjiabikai, itm_iron_knight_warhorse],
   str_29 | agi_26 | int_16 | cha_11|level(50), wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_9|knows_looting_10|knows_trainer_4|knows_tracking_6|knows_tactics_5|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_8|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_5|knows_engineer_2|knows_persuasion_7|knows_array_arrangement_2|knows_memory_9|knows_study_1|knows_devout_1|knows_prisoner_management_12|knows_leadership_10|knows_trade_8,
   man_face_middle_1, man_face_old_2],


#各分舵专属兵种
  ["black_candle_mistress","Black Candle Mistress","Black Candle Mistresses", #黑烛小姐
   tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_blue_lion_fan_shaped_shield, itm_danshou_hudiedao, itm_lady_dress_blue, itm_splinted_leather_greaves, itm_luzhi_bikai, itm_lady_dress_green, itm_lady_dress_ruby, itm_green_dress, itm_pride_fan_shaped_shield, itm_blue_flower_fan_shaped_shield, itm_leather_boots, itm_light_leather_boots, itm_fenzhi_pishoutao, itm_fenzhi_jiaqiangshoutao],
   str_14 | agi_12 | int_8 | cha_11|level(20),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (50) | wp_crossbow (50) | wp_throwing (100),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_3|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_4|knows_tracking_1|knows_pathfinding_1|knows_spotting_2|knows_first_aid_1|knows_persuasion_1|knows_memory_2|knows_prisoner_management_1|knows_leadership_2|knows_trade_3,
   woman_face_1, woman_face_2],

  ["splitting_sailor","Splitting Sailor","Splitting Sailors",#裂帆水手
   tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_wangguo_mingbin_mianjia, itm_xihai_pixue, itm_leather_gloves, itm_zonghong_mianjia, itm_zonghong_diancheng_jia, itm_hongse_dianchengpao, itm_nordic_shield, itm_longshoujian, itm_round_shield, itm_sword_viking_1, itm_hand_axe, itm_sword_viking_2_small, itm_hatchet],
   str_14 | agi_13 | int_9 | cha_7|level(21),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),
   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_3|knows_weapon_master_3|knows_shield_2|knows_athletics_6|knows_riding_3|knows_horse_archery_4|knows_looting_6|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_4|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_5|knows_array_arrangement_1|knows_memory_3|knows_study_1|knows_devout_1|knows_prisoner_management_5|knows_leadership_3|knows_trade_5,
   man_face_young_1, man_face_older_2],
  ["splitting_swordman","Splitting Swordman","Splitting Swordmen",#裂帆剑士
   tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_outlaws_libra,
   [itm_red_lion_iron_fan_shaped_shield, itm_bastard_sword_b, itm_bastard_sword_a, itm_nordic_fighter_helmet, itm_wangguobubing_jia, itm_nailed_iron_leather_boot, itm_scale_gauntlets, itm_iron_leather_greave, itm_leather_gloves],
   str_22 | agi_20 | int_12 | cha_7|level(32), wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (220) | wp_crossbow (220) | wp_throwing (220),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_6|knows_riding_4|knows_horse_archery_7|knows_looting_8|knows_trainer_4|knows_tracking_6|knows_tactics_3|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_2|knows_persuasion_6|knows_array_arrangement_2|knows_memory_4|knows_study_1|knows_devout_1|knows_prisoner_management_8|knows_leadership_5|knows_trade_6,
   man_face_young_1, man_face_old_2],



#############################################################丧钟刺客团##########################################################

  ["primary_killer","Primary Killer","Primary Killers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_deathbell,
   [itm_leather_gloves, itm_leather_boots, itm_skullcap, itm_maopipijia_pijia, itm_steel_shield, itm_throwing_knives, itm_jinshi_zhirengzhandao],
   str_13 | agi_16 | int_6 | cha_6|level(15),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),knows_ironflesh_2|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_1|knows_shield_2|knows_athletics_5|knows_riding_2|knows_horse_archery_2,man_face_younger_1, man_face_young_2],
  ["professional_assassin","Professional Assassin","Professional Assassins",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_deathbell,
   [itm_mogang_jundao, itm_leather_gloves, itm_leather_boots, itm_throwing_daggers, itm_zhiyecike_jia, itm_professional_assassin_hood],
   str_23 | agi_27 | int_10 | cha_10|level(32),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),knows_ironflesh_7|knows_power_strike_10|knows_power_throw_9|knows_weapon_master_4|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_3,man_face_young_1, man_face_middle_2],
  ["knell_assassin","Knell Assassin","Knell Assassins",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_deathbell,
   [itm_forged_steel_nodachi, itm_knell_plate, itm_knell_assassin_hood, itm_wuzhe_pixue, itm_fenzhi_dingshishoutao, itm_sizhong],
   str_57 | agi_63 | int_30 | cha_30|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_11|knows_power_strike_14|knows_power_throw_13|knows_power_draw_10|knows_weapon_master_5|knows_shield_10|knows_athletics_5|knows_riding_4|knows_horse_archery_4,man_face_younger_1, man_face_young_2],
  ["armor_breaker","Armor Breaker","Armor Breakers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_deathbell,
   [itm_nanfang_cijian, itm_zhanzhengcike_jiaqiangjia, itm_high_assassin_hood, itm_strange_short_sword, itm_wuzhe_pixue, itm_fenzhi_pishoutao, itm_war_darts],
   str_25 | agi_29 | int_10 | cha_10|level(30),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),knows_ironflesh_8|knows_power_strike_9|knows_power_throw_7|knows_weapon_master_4|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_5,man_face_young_1, man_face_middle_2],
  ["war_assassin","War Assassin","War Assassins",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_deathbell,
   [itm_strange_sword, itm_strange_short_sword, itm_zhanzhengcike_jia, itm_war_assassin_hood, itm_fenzhi_fubanshoutao, itm_wuzhe_pixue, itm_zhanzheng_feiren],
   str_37 | agi_42 | int_19 | cha_19|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_9|knows_power_strike_13|knows_power_throw_11|knows_weapon_master_9|knows_shield_4|knows_athletics_10|knows_riding_5|knows_horse_archery_5,man_face_younger_1, man_face_young_2],

  ["female_killer","Female Killer","Female Killers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_deathbell,
   [itm_jinshiwandao, itm_steel_shield, itm_leather_gloves, itm_leather_boots, itm_maopipijia_pijia, itm_skullcap, itm_throwing_knives],
   str_12 | agi_17 | int_6 | cha_6|level(15),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),knows_ironflesh_2|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_1|knows_shield_2|knows_athletics_5|knows_riding_2|knows_horse_archery_2,0x00000001800030010000000000000edb00000000000000000000000000000000, 0x00000001800030010000000000000edb00000000000000000000000000000000],
  ["professional_female_assassin","Professional Female Assassin","Professional Female Assassins",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_deathbell,
   [itm_danshou_hudiedao, itm_wunvfu, itm_wuzhe_pixue, itm_dancer_veil, itm_nvshi_shoutao, itm_jinshi_feidao],
   str_22 | agi_28 | int_10 | cha_10|level(32),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),knows_ironflesh_7|knows_power_strike_10|knows_power_throw_6|knows_power_draw_9|knows_weapon_master_4|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_3,0x00000001800030010000000000000edb00000000000000000000000000000000, 0x00000001800030010000000000000edb00000000000000000000000000000000],
  ["death_dancer","Death Dancer","Death Dancers",tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_deathbell,
   [itm_strange_great_sword, itm_qizhi_feidao, itm_wuzhe_pixue, itm_siwangwuzhejia, itm_dancer_veil, itm_fenzhi_jiaqiangshoutao],
   str_57 | agi_63 | int_30 | cha_60|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_11|knows_power_strike_14|knows_power_throw_13|knows_weapon_master_10|knows_shield_5|knows_athletics_10|knows_riding_4|knows_horse_archery_4,0x00000001800030010000000000000edb00000000000000000000000000000000, 0x00000001800030010000000000000edb00000000000000000000000000000000],
  ["eavesdropper","Eavesdropper","Eavesdroppers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_deathbell,
   [itm_shentie_goujian, itm_strange_short_sword, itm_wunvfu, itm_wuzhe_pixue, itm_dancer_veil, itm_nvshi_shoutao, itm_jinshi_feidao],
   str_24 | agi_30 | int_10 | cha_10|level(30),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (330) | wp_crossbow (330) | wp_throwing (330),knows_ironflesh_8|knows_power_strike_9|knows_power_throw_7|knows_weapon_master_4|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_5,0x00000001800030010000000000000edb00000000000000000000000000000000, 0x00000001800030010000000000000edb00000000000000000000000000000000],
  ["eight_sword_dancer","Eight Sword Dancer","Eight Sword Dancers",tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_deathbell,
   [itm_strange_sword, itm_strange_short_sword, itm_bazhidaowuzhe_jia, itm_dancer_veil, itm_qizhi_feidao, itm_wuzhe_pixue, itm_fenzhi_pishoutao],
   str_37 | agi_42 | int_19 | cha_19|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_9|knows_power_strike_13|knows_power_throw_11|knows_weapon_master_9|knows_shield_4|knows_athletics_10|knows_riding_5|knows_horse_archery_5,0x00000001800030010000000000000edb00000000000000000000000000000000, 0x00000001800030010000000000000edb00000000000000000000000000000000],



###########################################################魔物###########################################################

#————————————————————————————————魔王崇拜者—————————————————————————————————
##
  ["the_forsaken","The Forsaken","The Forsakens",#弃世者
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_heresy_demon,
   [itm_mace_2, itm_tab_shield_round_b, itm_tab_shield_round_a, itm_jianyi_langyabang, itm_qishi_pao2, itm_leather_boots, itm_winged_mace],
   str_13 | agi_10 | int_6 | cha_6|level(15), wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_3|knows_power_strike_2|knows_shield_1|knows_athletics_1|knows_looting_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_1|knows_surgery_1|knows_persuasion_1|knows_memory_1|knows_devout_7,
   man_face_younger_1, man_face_older_2],
  ["cult_follower","Cult Follower","Cult Followers", #邪教追随者
   tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
   0,0,fac_heresy_demon,
   [itm_mace_4, itm_simple_cruel_morningstar_hammer, itm_leather_covered_round_shield, itm_wooden_shield, itm_forsaken_hood, itm_qishi_pao, itm_leather_boots, itm_leather_gloves, itm_dingci_lengtouchui, itm_jianyi_langyabang, itm_splinted_leather_greaves],
   str_17 | agi_14 | int_7 | cha_7|level(25), wp_one_handed (210) | wp_two_handed (210) | wp_polearm (210) | wp_archery (210) | wp_crossbow (210) | wp_throwing (210),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_1|knows_looting_3|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_2|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_3|knows_devout_10|knows_prisoner_management_3|knows_leadership_2|knows_trade_2,
   man_face_younger_1, man_face_older_2],
  ["fallen_warrior","Fallen Warrior","Fallen Warriors", #堕落卫士
   tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_heresy_demon,
   [itm_spiked_mace, itm_cruel_morningstar_hammer, itm_steel_shield, itm_simple_cruel_morningstar_hammer, itm_forsaken_chain_hood, itm_dark_worshipper_leather_armor, itm_steel_leather_boot, itm_leather_gloves, itm_qishi_pibanlianjai, itm_leather_covered_round_shield, itm_plate_covered_round_shield, itm_splinted_leather_greaves, itm_morningstar],
   str_30 | agi_25 | int_7 | cha_7|level(35), wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_4|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_5|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_2|knows_devout_12|knows_prisoner_management_3|knows_leadership_5|knows_trade_4,
   man_face_younger_1, man_face_older_2],
  ["degradation_rider","Degradation Rider","Degradation Riders", #坠魔骑手
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, 
   0,0,fac_heresy_demon,
   [itm_long_cruel_morningstar_hammer, itm_cruel_morningstar_hammer, itm_demon_fan_shaped_shield, itm_devil_rider_hood, itm_demon_leather_plate, itm_dark_oath_shoe, itm_renmowushi_glove, itm_demon_horse],
   str_45 | agi_34 | int_7 | cha_7|level(48), wp_one_handed (430) | wp_two_handed (430) | wp_polearm (430) | wp_archery (430) | wp_crossbow (430) | wp_throwing (430),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_looting_8|knows_trainer_6|knows_tracking_7|knows_tactics_5|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_6|knows_wound_treatment_5|knows_surgery_7|knows_first_aid_6|knows_engineer_5|knows_persuasion_7|knows_array_arrangement_5|knows_memory_10|knows_study_4|knows_devout_15|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   man_face_younger_1, man_face_older_2],
  ["dark_oath_knight","Dark Oath Knight","Dark Oath Knights", #黑誓骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, 
   0,0,fac_heresy_demon,
   [itm_demon_knight_lance, itm_havathang, itm_demon_fan_shaped_shield, itm_dark_oath_plate, itm_dark_oath_shoe, itm_dark_oath_hand, itm_anhei_qingshi_moshouma1, itm_dark_oath_helmet],
   str_70 | agi_59 | int_7 | cha_7|level(60), wp_one_handed (560) | wp_two_handed (560) | wp_polearm (560) | wp_archery (560) | wp_crossbow (560) | wp_throwing (560),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_7|knows_shield_7|knows_athletics_8|knows_riding_8|knows_horse_archery_8|knows_looting_10|knows_trainer_7|knows_tracking_8|knows_tactics_6|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_7|knows_wound_treatment_6|knows_surgery_8|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_11|knows_study_6|knows_devout_15|knows_prisoner_management_6|knows_leadership_8|knows_trade_4,
   man_face_younger_1, man_face_older_2],

  ["fallen_apprentice","Fallen Apprentice","Fallen Apprentices", #堕落学徒
   tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_heresy_demon,
   [itm_gangjian, itm_steel_shield, itm_simple_cruel_morningstar_hammer, itm_forsaken_chain_hood, itm_dark_apprentice_robe, itm_steel_leather_boot, itm_scale_gauntlets, itm_war_bow],
   str_31 | agi_25 | int_7 | cha_7|level(36), wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_6|knows_looting_7|knows_trainer_4|knows_tracking_6|knows_tactics_4|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_5|knows_wound_treatment_3|knows_surgery_5|knows_first_aid_4|knows_engineer_3|knows_persuasion_6|knows_array_arrangement_3|knows_memory_8|knows_study_2|knows_devout_12|knows_prisoner_management_3|knows_leadership_5|knows_trade_4,
   man_face_younger_1, man_face_older_2],
  ["desecrate_priest","Desecrate Priest","Desecrate Priests", #亵渎司仪
   tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_heresy_demon,
   [itm_gangjian, itm_demon_fan_shaped_shield, itm_cruel_morningstar_hammer, itm_devil_rider_hood, itm_qishi_pao3, itm_black_greaves, itm_gauntlets, itm_demon_reverse_bow],
   str_46 | agi_34 | int_7 | cha_7|level(48), wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_5|knows_power_draw_8|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_5|knows_horse_archery_7|knows_looting_8|knows_trainer_6|knows_tracking_7|knows_tactics_5|knows_pathfinding_8|knows_spotting_8|knows_inventory_management_6|knows_wound_treatment_5|knows_surgery_7|knows_first_aid_6|knows_engineer_5|knows_persuasion_7|knows_array_arrangement_5|knows_memory_10|knows_study_4|knows_devout_15|knows_prisoner_management_5|knows_leadership_7|knows_trade_4,
   man_face_younger_1, man_face_older_2],
  ["cauter_cardinal","Cauter Cardinal","Cauter Cardinals", #魔烙主教
   tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, 
   0,0,fac_heresy_demon,
   [itm_gangjian, itm_demon_fan_shaped_shield, itm_mozujundao, itm_inhuman_helmet, itm_dark_magician_robe, itm_demon_knight_boot, itm_renmowushi_glove, itm_demon_horse, itm_demon_reverse_bow],
   str_71 | agi_59 | int_7 | cha_7|level(64), wp_one_handed (640) | wp_two_handed (640) | wp_polearm (640) | wp_archery (640) | wp_crossbow (640) | wp_throwing (640),
   knows_ironflesh_15|knows_power_strike_14|knows_power_throw_7|knows_power_draw_11|knows_weapon_master_7|knows_shield_7|knows_athletics_8|knows_riding_7|knows_horse_archery_9|knows_looting_10|knows_trainer_7|knows_tracking_8|knows_tactics_6|knows_pathfinding_9|knows_spotting_9|knows_inventory_management_7|knows_wound_treatment_6|knows_surgery_8|knows_first_aid_7|knows_engineer_6|knows_persuasion_9|knows_array_arrangement_6|knows_memory_11|knows_study_6|knows_devout_15|knows_prisoner_management_6|knows_leadership_8|knows_trade_4,
   man_face_younger_1, man_face_older_2],


#————————————————————————————————魔力侵蚀者—————————————————————————————————
##
  ["demon_corruptor","Demon Corruptor","Demon Corruptors",#魔气侵蚀者
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_heresy_demon,
   [itm_burlap_tunic, itm_woolen_hose, itm_sickle, itm_knife, itm_cleaver, itm_pitch_fork, itm_boar_spear, itm_coarse_tunic, itm_leather_apron, itm_short_tunic, itm_robe, itm_tabard, itm_padded_leather, itm_arming_cap, itm_padded_coif, itm_black_hood, itm_butchering_knife, itm_leather_cap, itm_blue_hose, itm_ankle_boots, itm_wrapping_boots, itm_dagger, itm_jianyi_peizhongjian],
   str_14 | agi_11 | int_6 | cha_6|level(10), wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_3|knows_power_strike_2|knows_athletics_1|knows_tracking_1|knows_pathfinding_1|knows_spotting_1|knows_study_6,
   man_face_younger_1, man_face_older_2],
  ["new_birth_lemure","New Birth Lemure","New Birth Lemures",#新生劣魔
   tf_walker|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_heresy_demon,
   [itm_lemure_head, itm_rawhide_coat, itm_hide_boots, itm_lemure_hand, itm_light_leather, itm_padded_cloth, itm_aketon_green, itm_nomad_armor, itm_leather_vest, itm_fur_covered_shield, itm_beast_skin_round_shield, itm_tab_shield_round_a, itm_wooden_stick, itm_wooden_shield, itm_torch, itm_cudgel, itm_club, itm_hammer, itm_mace_1, itm_maul, itm_spiked_club, itm_hatchet, itm_hand_axe, itm_hunter_boots, itm_nomad_boots, itm_light_leather_boots, itm_leather_boots],
   str_26 | agi_22 | int_6 | cha_6|level(28), wp_one_handed (150) | wp_two_handed (150) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_shield_1|knows_athletics_4|knows_riding_1|knows_horse_archery_1|knows_looting_1|knows_tracking_3|knows_pathfinding_4|knows_spotting_4|knows_study_10,
   man_face_younger_1, man_face_older_2],
  ["lemure","Lemure","Lemures",#劣魔
   tf_walker|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_heresy_demon,
   [itm_lemure_head, itm_brigandine_red, itm_lemure_leg, itm_lemure_hand, itm_dingshi_fupi_duanlianjia, itm_linjiapijian_dingshijia, itm_mail_hauberk, itm_duanxiu_lianjiapao, itm_quanshen_lianjai, itm_lanse_xiongjia, itm_heibai_xiongjia, itm_huanghei_xiongjia, itm_fur_covered_shield, itm_leather_covered_round_shield, itm_plate_covered_round_shield, itm_wooden_board_shield, itm_military_cleaver_b, itm_qinliang_lengtouchui, itm_winged_mace, itm_warhammer, itm_sledgehammer, itm_jianyi_langyabang, itm_dingci_lengtouchui, itm_club_with_spike_head, itm_sarranid_axe_b, itm_one_handed_war_axe_a, itm_one_handed_war_axe_b, itm_one_handed_battle_axe_a],
   str_40 | agi_36 | int_6 | cha_6|level(38), wp_one_handed (250) | wp_two_handed (250) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_11|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_shield_2|knows_athletics_6|knows_riding_2|knows_horse_archery_2|knows_looting_2|knows_tracking_5|knows_pathfinding_6|knows_spotting_5|knows_study_12,
   man_face_younger_1, man_face_older_2],
  ["crazy_lemure","Crazy Lemure","Crazy Lemures",#狂劣魔
   tf_walker|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_heresy_demon,
   [itm_shentie_shuangshoufu, itm_shengtieshuangshoujian, itm_shengtie_changbingfu, itm_shengtie_kaungbaodao, itm_lemure_head, itm_lemure_body, itm_lemure_leg, itm_lemure_hand, itm_war_axe, itm_warhammer, itm_voulge],
   str_54 | agi_49 | int_6 | cha_6|level(48), wp_one_handed (350) | wp_two_handed (350) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_6|knows_power_draw_6|knows_shield_3|knows_athletics_8|knows_riding_3|knows_horse_archery_3|knows_looting_3|knows_tracking_6|knows_pathfinding_7|knows_spotting_6|knows_study_15,
   man_face_younger_1, man_face_older_2],



#############################################################巫蛊##########################################################

  ["witchcraft_trainee","Witchcraft Trainee","Witchcraft Trainees",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_heresy_witchcraft,
   [itm_leather_boots, itm_shepi_shoutao, itm_jinse_hushoujian, itm_jinse_changjian, itm_jinse_zhanjian, itm_jinse_bubingjian, itm_beifang_pijia],
   str_13 | agi_12 | int_16 | cha_12|level(20),wp_one_handed (175) | wp_two_handed (175) | wp_polearm (175) | wp_archery (175) | wp_crossbow (175) | wp_throwing (175),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_3|knows_shield_1|knows_athletics_2,woman_face_1, woman_face_2],
  ["damnation_warrior","Damnation Warrior","Damnation Warriors",tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_witchcraft,
   [itm_beifang_lingxiongjia, itm_lianjia_quanfu_guokui, itm_plate_boots, itm_yuanzhi_bikai, itm_snake_fan_shaped_shield, itm_changliu_duanqiang, itm_podu_qiang, itm_kaitang_qiang],
   str_29 | agi_29 | int_14 | cha_14|level(30),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_5|knows_shield_5|knows_athletics_5|knows_riding_3|knows_horse_archery_2],
  ["poisonous_knight","Poisonous Knight","Poisonous Knights",tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_witchcraft,
   [itm_kaitang_qiang, itm_venomblood_knight_helmet, itm_poison_fang_battle_shield, itm_duxueqishi_jia, itm_heise_banlianjiaxue, itm_heiguang_bikai],
   str_35 | agi_35 | int_19 | cha_17|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (450) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_7|knows_shield_7|knows_athletics_7|knows_riding_4|knows_horse_archery_7,woman_face_1, woman_face_2],
  ["witchcraft_druid","Witchcraft Druid","Witchcraft Druids",tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_heresy_witchcraft,
   [itm_wugu_jian1, itm_witchcraft_poinson_bow, itm_zase_ma, itm_beifang_lingxiongjia, itm_leather_gloves, itm_leather_boots, itm_no_head, itm_jinshi_qibingjian],
   str_18 | agi_12 | int_19 | cha_13|level(25),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (270) | wp_crossbow (175) | wp_throwing (175),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_4|knows_shield_3|knows_athletics_4,woman_face_1, woman_face_2],
  ["witchcraft_warlock","Witchcraft Warlock","Witchcraft Warlocks",tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_heresy_witchcraft,
   [itm_wugushushi_jia, itm_leather_gloves, itm_plate_boots, itm_no_head, itm_shense_banzhajia_caoyuanma, itm_qianse_banzhajia_caoyuanma, itm_witchcraft_poinson_composite_bow, itm_wugu_jian1, itm_snake_fan_shaped_shield, itm_jinse_zhongjian],
   str_24 | agi_15 | int_30 | cha_17|level(40),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (350) | wp_crossbow (175) | wp_throwing (175),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_6|knows_weapon_master_6|knows_shield_5|knows_athletics_6,woman_face_1, woman_face_2],



#############################################################不死者结社##########################################################

  ["junto_member","Junto Member","Junto Members",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_pilgrim_disguise, itm_pilgrim_hood, itm_leather_gloves, itm_leather_boots, itm_sword_viking_2, itm_sword_viking_3, itm_tab_shield_round_a, itm_tab_shield_round_b, itm_arrows, itm_khergit_arrows, itm_strong_bow],
   str_13 | agi_12 | int_16 | cha_12|level(20),wp_one_handed (175) | wp_two_handed (175) | wp_polearm (175) | wp_archery (175) | wp_crossbow (175) | wp_throwing (175),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_3|knows_shield_1|knows_athletics_2,powell_face_younger_1, powell_face_older_2],
  ["junto_student","Junto Student","Junto Students",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_heresy_undead,
   [],
   str_19 | agi_16 | int_21 | cha_17|level(30),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (270) | wp_crossbow (270) | wp_throwing (175),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2,powell_face_younger_1, powell_face_older_2],
  ["necromancer","Necromancer","Necromancers",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [],
   str_27 | agi_21 | int_30 | cha_19|level(45),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (300) | wp_crossbow (300) | wp_throwing (175),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_7|knows_weapon_master_4|knows_shield_5|knows_athletics_7|knows_riding_6|knows_horse_archery_5,powell_face_younger_1, powell_face_older_2],
  ["necro_knight","Necro Knight","Necro Knights",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_necro_knight_armor, itm_silingqishi_kui, itm_heise_banlianjiaxue, itm_mogang_yuanzhi_bikai, itm_busi_diexuefu, itm_anhei_qingshi_moshouma],
   str_32 | agi_24 | int_30 | cha_19|level(45),wp_one_handed (330) | wp_two_handed (330) | wp_polearm (330) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_7|knows_horse_archery_6,powell_face_younger_1, powell_face_older_2],
  ["half_dead","Half dead","Half Deads",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_necro_warrier_armor, itm_busizhe_shanxingdun, itm_busi_diexuefu, itm_silingshuhsi_doumao, itm_jiangshi_ma, itm_leather_boots, itm_mail_boots, itm_skull_staff],
   str_170 | agi_51 | int_60 | cha_6|level(61),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),knows_ironflesh_15|knows_power_strike_12|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_8|knows_shield_7|knows_athletics_7|knows_riding_8|knows_horse_archery_7,powell_face_younger_1, powell_face_older_2],


#Rita ZenI's special troop
  ["nercosteel_shieldward_sergeant","Nercosteel Shieldward Sergeant","Nercosteel Shieldward Sergeants",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_85 | agi_18 | int_10 | cha_3|level(42),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (90) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_12|knows_power_strike_8|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_1, zombie_face],
  ["umbrashot_marksman_sergeant","Umbrashot Marksman Sergeant","Umbrashot Marksman Sergeants",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_50 | agi_50 | int_10 | cha_3|level(42),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),knows_ironflesh_9|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_7|knows_riding_2|knows_horse_archery_2,zombie_face],
  ["foulshadow_sprinter_sergeant","Foulshadow Sprinter Sergeant","Foulshadow Sprinter Sergeants",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_27 | agi_28 | int_10 | cha_3|level(42),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (20) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_2|knows_weapon_master_5|knows_shield_3|knows_athletics_9|knows_riding_3|knows_horse_archery_2,zombie_face],

  ["skull_collector","Skull Collector","Skeleton Collectors",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_35 | agi_35 | int_6 | cha_3|level(25),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_4,zombie_face],
  ["skeleton_executioner","Skeleton Executioner","Skeleton Executioners",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_51 | agi_45 | int_19 | cha_6|level(38),wp_one_handed (380) | wp_two_handed (380) | wp_polearm (380) | wp_archery (380) | wp_crossbow (380) | wp_throwing (380),knows_ironflesh_9|knows_power_strike_8|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_5,zombie_face],
  ["skeleton_beheader","Skeleton Beheader","Skeleton Beheaders",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_62 | agi_57 | int_27 | cha_12|level(50),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),knows_ironflesh_12|knows_power_strike_11|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_6,zombie_face],

  ["rita_zenIs_hound","Rita ZenI's Hound","Rita ZenI's Hounds",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue],
   str_123 | agi_93 | int_19 | cha_3|level(55),wp_one_handed (550) | wp_two_handed (550) | wp_polearm (550) | wp_archery (550) | wp_crossbow (550) | wp_throwing (550),knows_ironflesh_13|knows_power_strike_13|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_10|knows_shield_6|knows_athletics_15|knows_riding_6|knows_horse_archery_2,zombie_face],

  ["deathdam_extraditer","Deathdam Extraditer","Deathdam Extraditers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_52 | agi_55 | int_40 | cha_12|level(48),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_8|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_8|knows_horse_archery_5,zombie_face],
  ["deathdam_archon","Deathdam Archon","Deathdam Archons",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_90 | agi_67 | int_60 | cha_20|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_13|knows_power_strike_11|knows_power_throw_8|knows_power_draw_10|knows_weapon_master_9|knows_shield_8|knows_athletics_12|knows_riding_10|knows_horse_archery_7,zombie_face],

  ["agouti_faceless_shooter","Agouti Faceless Shooter","Agouti Faceless Shooters",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_death_omen, itm_guguan_lianjiaxue, itm_heijin_banjaibikai, itm_heijin_banjia, itm_heijin_qishixue, itm_touguan_toumao],
   str_45 | agi_45 | int_13 | cha_3|level(38),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (350) | wp_throwing (280),knows_ironflesh_9|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_5|knows_shield_4|knows_athletics_6|knows_riding_2|knows_horse_archery_2,zombie_face],


#zombie
  ["low_grade_zombie","Low_garde zombie","Low_garde zombies",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive,0,0,fac_heresy_undead,
   [itm_sword_medieval_a, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_sword_medieval_c, itm_sword_medieval_c_small, itm_sword_medieval_c_long, itm_sword_medieval_d_long, itm_sword_viking_1, itm_sword_viking_2, itm_sword_viking_2_small, itm_sword_viking_3, itm_sword_viking_3_small, itm_boar_spear],
   str_50 | agi_4 | int_3 | cha_3|level(5),wp_one_handed (5) | wp_two_handed (5) | wp_polearm (5) | wp_archery (5) | wp_crossbow (5) | wp_throwing (5),knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_1,zombie_face],
  ["zombie_footman","Zombie footman","Zombie footmen",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_tab_shield_round_a, itm_tab_shield_kite_a, itm_tab_shield_heater_a, itm_tab_shield_pavise_a, itm_spear, itm_bamboo_spear, itm_war_spear, itm_pike, itm_ashwood_pike, itm_awlpike, itm_awlpike_long, itm_leather_warrior_cap, itm_skullcap, itm_mail_coif, itm_footman_helmet, itm_nasal_helmet, itm_norman_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_leather_boots, itm_hunter_boots, itm_hide_boots, itm_ankle_boots, itm_nomad_boots, itm_studded_leather_coat, itm_byrnie, itm_haubergeon, itm_lamellar_vest, itm_lamellar_vest_khergit, itm_mail_shirt, itm_mail_hauberk],
   str_57 | agi_12 | int_3 | cha_3|level(20),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_7|knows_power_strike_5|knows_power_throw_5|knows_power_draw_3,zombie_face],
  ["zombie_swordman","Zombie Swordman","Zombie Swordmen",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet, itm_vaegir_lamellar_helmet, itm_vaegir_noble_helmet, itm_norman_helmet, itm_segmented_helmet, itm_helmet_with_neckguard, itm_flat_topped_helmet, itm_kettle_hat, itm_great_sword, itm_great_sword, itm_sword_two_handed_b, itm_sword_two_handed_a, itm_khergit_sword_two_handed_a, itm_khergit_sword_two_handed_b, itm_two_handed_cleaver, itm_throwing_knives, itm_jiangshi_zhongzhajia, itm_jiangshi_zhajia, itm_lvsejiangshizhongzhajia, itm_huangsejiangshizhongzhajia, itm_lingjia_xue],
   str_61 | agi_12 | int_3 | cha_3|level(30),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),knows_ironflesh_9|knows_power_strike_7|knows_power_throw_7|knows_power_draw_4,zombie_face],
  ["death_knight","Death Knight","Death Knights",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_necro_warrier_armor, itm_jiangshi_kui, itm_jiangshi_ma, itm_plate_boots, itm_mogang_fangxing_bikai, itm_mogang_yuanzhi_bikai, itm_bone_mound_fan_shaped_shield, itm_busi_diexuefu],
   str_90 | agi_20 | int_3 | cha_3|level(45),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),knows_ironflesh_13|knows_power_strike_11|knows_power_throw_11|knows_power_draw_5|knows_weapon_master_2|knows_riding_7,zombie_face],
  ["zombie_lancer","Zombie Lancer","Zombie Lancers",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_jiantou_qiang1, itm_buqiang_jiantiqiang, itm_jianyi_jiantiqiang, itm_jiangshi_zhongzhajia, itm_jiangshi_zhajia, itm_jiangshi_kui, itm_lvsejiangshizhongzhajia, itm_huangsejiangshizhongzhajia, itm_leather_boots, itm_scale_gauntlets, itm_lamellar_gauntlets],
   str_71 | agi_12 | int_3 | cha_3|level(30),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (70) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_7|knows_power_strike_8|knows_power_throw_8|knows_power_draw_8,zombie_face],
  ["zombie_archer","Zombie Archer","Zombie Archers",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_studded_leather_coat, itm_byrnie, itm_haubergeon, itm_nordic_helmet, itm_nordic_fighter_helmet, itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet, itm_javelin, itm_throwing_spears, itm_jarid],
   str_57 | agi_12 | int_3 | cha_3|level(20),wp_one_handed (20) | wp_two_handed (20) | wp_polearm (20) | wp_archery (20) | wp_crossbow (20) | wp_throwing (60),knows_ironflesh_7|knows_power_strike_5|knows_power_throw_5|knows_power_draw_3,zombie_face],
  ["zombie_destroyer","Zombie Destroyer","Zombie Destroyers",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_jinshi_toumao, itm_jinshi_touqiang, itm_touguan_toumao, itm_jiangshi_zhongzhajia, itm_jiangshi_zhajia, itm_jiangshi_kui, itm_lvsejiangshizhongzhajia, itm_huangsejiangshizhongzhajia, itm_lingjia_xue],
   str_62 | agi_12 | int_3 | cha_3|level(30),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (100),knows_ironflesh_10|knows_power_strike_6|knows_power_throw_7|knows_power_draw_5,zombie_face],

  ["zombie_king_warrior","Zombie King Warrior","Zombie King Warrior",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_sword_medieval_a, itm_spear,itm_simple_pegasus_skoutarion, itm_jiaqiang_guokui2, itm_hongse_dianchengjia, itm_leather_boots, itm_leather_gloves, itm_shortened_spear, itm_war_spear, itm_bamboo_spear, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_sword_medieval_c, itm_sword_medieval_c_small],
   str_60 | agi_14 | int_4 | cha_3|level(24),wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (45) | wp_crossbow (45) | wp_throwing (45),knows_ironflesh_8|knows_power_strike_6|knows_power_throw_6|knows_power_draw_2,zombie_face],
  ["zombie_king_guard","Zombie King Guard","Zombie King Guard",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
    [itm_military_cleaver_b, itm_military_cleaver_c, itm_dark_lion_fan_shaped_shield, itm_pike, itm_fuhe_guokui, itm_brigandine_red, itm_splinted_greaves, itm_mail_mittens, itm_mail_with_surcoat, itm_ashwood_pike, itm_awlpike, itm_awlpike_long],
   str_75 | agi_15 | int_7 | cha_3|level(35),wp_one_handed (65) | wp_two_handed (65) | wp_polearm (65) | wp_archery (65) | wp_crossbow (65) | wp_throwing (65),knows_ironflesh_10|knows_power_strike_8|knows_power_throw_8|knows_power_draw_2,zombie_face],
  ["zombie_king_praetorian","Zombie King Praetorian","Zombie King Praetorian",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_powell_noble_hand_and_a_half_sword, itm_busizhe_shanxingdun, itm_jiachang_kuotou_qiang, itm_qinxing_jixingkui2, itm_plate_armor, itm_iron_greaves, itm_gauntlets],
   str_130 | agi_22 | int_10 | cha_3|level(55),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),knows_ironflesh_14|knows_power_strike_12|knows_power_throw_12|knows_power_draw_2|knows_weapon_master_3|knows_shield_1,zombie_face],

  ["resurgam_knight","Resurgam Knight","Resurgam Knight",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_steel_bardiche, itm_short_blade_great_scythe, itm_flat_head_axe, itm_hongyu_hue_qingbiankui, itm_hongjing_qingbanlianfuhe_jia, itm_steel_leather_boot, itm_fenzhi_lianjiashoutao],
   str_67 | agi_16 | int_10 | cha_3|level(30),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (65) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_8|knows_power_draw_3,zombie_face],
  ["posthumous_knight","Posthumous Knight","Posthumous Knight",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_heresy_undead,
   [itm_jinshi_touqiang, itm_jinshi_toumao, itm_qishi_dingtouchui, itm_busizhe_shanxingdun, itm_powell_red_cape, itm_baitie_banjia, itm_baitie_qishixue, itm_shengtie_banjiabikai, itm_powell_jiangshi_ma, itm_changmian_jianzuikui],
   str_160 | agi_24 | int_21 | cha_3|level(62),wp_one_handed (180) | wp_two_handed (160) | wp_polearm (160) | wp_archery (40) | wp_crossbow (40) | wp_throwing (160),knows_ironflesh_14|knows_power_strike_13|knows_power_throw_13|knows_power_draw_3|knows_riding_7|knows_horse_archery_3|knows_trainer_4|knows_tracking_2|knows_tactics_4|knows_pathfinding_1|knows_spotting_2|knows_inventory_management_3,zombie_face],
  ["resurgam_knight_chief","Resurgam Knight Chief","Resurgam Knight Chief",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all_wo_ranged,0,0,fac_heresy_undead,
   [itm_lanwen_qiqiang, itm_qishi_dingtouchui, itm_busizhe_shanxingdun, itm_powell_noble_hand_and_a_half_sword, itm_changtongkui, itm_honglanpao_banlian, itm_duangang_banjiaxue, itm_fangxing_bikai, itm_jiangshi_ma],
   str_118 | agi_19 | int_14 | cha_3|level(52),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_13|knows_power_strike_13|knows_power_throw_10|knows_power_draw_10|knows_riding_6,zombie_face],

  ["undead_gladiatus","Undead Gladiatus","Undead Gladiatuses",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_steel_asterisk_staff, itm_black_hood, itm_light_leather, itm_light_leather_boots, itm_leather_gloves],
   str_110 | agi_13 | int_3 | cha_3|level(54),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (120) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_12|knows_power_strike_14|knows_power_throw_13|knows_power_draw_13,zombie_face],

  ["zombie_armed_infantry","Zombie Armed Infantry","Zombie Armed Infantry",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_tab_shield_pavise_a, itm_sword_medieval_c_small, itm_boar_spear, itm_military_fork, itm_footman_helmet, itm_aketon_green, itm_ankle_boots, itm_padded_cloth, itm_leather_jerkin, itm_padded_leather, itm_leather_boots, itm_skullcap, itm_mail_coif, itm_sarranid_axe_a, itm_battle_fork, itm_scythe, itm_tab_shield_pavise_b],
   str_53 | agi_5 | int_3 | cha_3|level(10),wp_one_handed (10) | wp_two_handed (10) | wp_polearm (10) | wp_archery (10) | wp_crossbow (10) | wp_throwing (10),knows_ironflesh_5|knows_power_strike_3|knows_power_throw_3|knows_power_draw_2|knows_shield_1,zombie_face],
  ["zombie_heavy_armed_soldier","Zombie Heavy Armored Soldier","Zombie Heavy Armored Soldier",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [],
   str_61 | agi_7 | int_4 | cha_3|level(22),wp_one_handed (30) | wp_two_handed (30) | wp_polearm (20) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_shield_1,zombie_face],
  ["zombie_dismounted_knight","Zombie Dismounted knight","Zombie Dismounted knight",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [],
   str_80 | agi_11 | int_8 | cha_3|level(37),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (40) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_5|knows_shield_2,zombie_face],
  ["immortal_blade","Immortal Blade","Immortal Blade",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_necro_tower_shield, itm_busi_guzhuangjian, itm_jiaoguo_guzhi_chaozhongkui, itm_zhengshi_banjiaxue, itm_fangxing_bikai],
   str_146 | agi_16 | int_13 | cha_3|level(60),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (100) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_13|knows_power_strike_13|knows_power_throw_6|knows_power_draw_6|knows_shield_3,zombie_face],
  ["zombie_heavy_shield_soldier","Zombie Heavy Shield Soldier","Zombie Heavy Shield Soldier",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_awlpike_long, itm_tab_shield_pavise_c, itm_tab_shield_pavise_d, itm_pike, itm_gangshizi_niujiao_dakui, itm_iron_greaves, itm_gauntlets, itm_gangshizi_niujiao_dakui2, itm_gangshizi_niujiao_dakui3, itm_awlpike, itm_steel_asterisk_staff],
   str_61 | agi_7 | int_4 | cha_3|level(22),wp_one_handed (20) | wp_two_handed (20) | wp_polearm (30) | wp_archery (20) | wp_crossbow (20) | wp_throwing (20),knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_shield_2,zombie_face],
  ["zombie_shield_spear_knight","Zombie Shield Spear Knight","Zombie Shield Spear Knight",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_decorated_towers_shield, itm_duyin_fuheqiang, itm_jiaoguo_guzhi_chaozhongkui, itm_zaoqi_zhongbanjia, itm_shengtie_banjiaxue, itm_shnegtie_shoutao],
   str_80 | agi_11 | int_8 | cha_3|level(37),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (70) | wp_archery (40) | wp_crossbow (30) | wp_throwing (30),knows_ironflesh_10|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_shield_3,zombie_face],
  ["impurity_shield","Impurity Shield","Impurity Shield",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_infantry,0,0,fac_heresy_undead,
   [itm_ancient_papal_tower_shield, itm_asterisk_staff, itm_jiaoguo_guzhi_chaozhongkui, itm_zhengshi_banjiaxue, itm_fangxing_bikai],
   str_146 | agi_16 | int_13 | cha_3|level(60),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (120) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_14|knows_power_strike_12|knows_power_throw_6|knows_power_draw_6|knows_shield_4,zombie_face],

  ["therianthropy_zombie","Therianthropy Zombie","Therianthropy Zombie",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_shitou, itm_xiongtou, itm_langtou, itm_rawhide_coat, itm_nomad_armor, itm_khergit_armor, itm_hunter_boots, itm_tutorial_club, itm_wooden_stick, itm_cudgel],
   str_90 | agi_3 | int_3 | cha_3|level(6),wp_one_handed (1) | wp_two_handed (1) | wp_polearm (1) | wp_archery (1) | wp_crossbow (1) | wp_throwing (1),knows_ironflesh_10|knows_power_strike_2,zombie_face],
  ["zombie_hammer_soldier","Zombie Hammer Soldier","Zombie Hammer Soldier",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_shitou, itm_xiongtou, itm_langtou, itm_rawhide_coat, itm_nomad_boots, itm_hide_boots, itm_hunter_boots, itm_nomad_armor, itm_hammer, itm_military_hammer, itm_maul, itm_sarranid_mace_1],
   str_100 | agi_3 | int_3 | cha_3|level(15),wp_one_handed (2) | wp_two_handed (2) | wp_polearm (2) | wp_archery (2) | wp_crossbow (2) | wp_throwing (2),knows_ironflesh_11|knows_power_strike_4,zombie_face],
  ["zombie_hammer_cavalry","Zombie Hammer Cavalry","Zombie Hammer Cavalry",tf_zombie|tf_mounted|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_shitou, itm_xiongtou, itm_langtou, itm_lamellar_vest_khergit, itm_nomad_boots, itm_leather_gloves, itm_jiangshi_ma, itm_nomad_robe, itm_lamellar_vest, itm_sarranid_two_handed_mace_1, itm_sledgehammer, itm_maul],
   str_125 | agi_3 | int_3 | cha_3|level(25),wp_one_handed (3) | wp_two_handed (3) | wp_polearm (3) | wp_archery (3) | wp_crossbow (3) | wp_throwing (3),knows_ironflesh_12|knows_power_strike_5|knows_riding_4,zombie_face],
  ["zombie_hammerer","Zombie Hammerer","Zombie Hammerer",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_shitou, itm_xiongtou, itm_langtou, itm_warhammer, itm_lamellar_vest, itm_nomad_boots, itm_leather_gloves, itm_lamellar_vest_khergit],
   str_124 | agi_3 | int_3 | cha_3|level(27),wp_one_handed (4) | wp_two_handed (4) | wp_polearm (4) | wp_archery (4) | wp_crossbow (4) | wp_throwing (4),knows_ironflesh_13|knows_power_strike_5,zombie_face],
  ["zombie_demolisher","Zombie Demolisher","Zombie Demolisher",tf_zombie|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_xiongtou, itm_shitou, itm_langtou, itm_stone_hammer, itm_sarranid_elite_armor, itm_splinted_leather_greaves, itm_lamellar_gauntlets, itm_leather_gloves, itm_nomad_boots, itm_lamellar_armor, itm_khergit_elite_armor],
   str_180 | agi_3 | int_3 | cha_3|level(42),wp_one_handed (6) | wp_two_handed (6) | wp_polearm (6) | wp_archery (6) | wp_crossbow (6) | wp_throwing (6),knows_ironflesh_14|knows_power_strike_6,zombie_face],


#skeleton
  ["rebirth_skeleton","Rebirth Skeleton","Rebirth Skeletons",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_13 | agi_14 | int_3 | cha_3|level(5),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_2|knows_riding_1|knows_horse_archery_1,zombie_face],
  ["skeleton_warrior","Skeleton Warrior","Skeleton Warriors",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_xiongjiakulou, itm_leather_boots, itm_plate_covered_round_shield, itm_leather_covered_round_shield, itm_tab_shield_round_a, itm_tab_shield_kite_a, itm_tab_shield_heater_a, itm_tab_shield_pavise_a, itm_bamboo_spear, itm_war_spear, itm_pike, itm_ashwood_pike, itm_awlpike, itm_leather_warrior_cap, itm_skullcap, itm_mail_coif, itm_footman_helmet, itm_nasal_helmet, itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet],
   str_23 | agi_24 | int_3 | cha_3|level(16),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4,zombie_face],
  ["skeleton_swordman","Skeleton Swordman","Skeleton Swordmen",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_splinted_leather_greaves, itm_mail_chausses, itm_leather_gloves, itm_mail_mittens, itm_kulou_zhanshishenti, itm_flat_topped_helmet, itm_kettle_hat, itm_spiked_helmet, itm_nordic_helmet, itm_vaegir_fur_helmet, itm_vaegir_spiked_helmet, itm_vaegir_lamellar_helmet, itm_steel_shield, itm_jinse_zhanjian, itm_jinse_bubingjian],
   str_34 | agi_35 | int_3 | cha_3|level(25),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_4,zombie_face],
  ["experienced_skeleton","Experienced Skeleton","Experienced Skeletons",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_skeleton_plate, itm_gauntlets, itm_iron_greaves, itm_duangang_xiugaiqi, itm_busi_guzhuangjian],
   str_60 | agi_55 | int_3 | cha_3|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_8|knows_horse_archery_4,zombie_face],
  ["skeleton_rider","Skeleton Rider","Skeleton Riders",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_kulou_zhanshishenti, itm_kulouma, itm_mail_mittens, itm_mail_boots, itm_guyongbing_tiekui, itm_jinshi_qishijian, itm_busizhe_shanxingdun, itm_great_lance],
   str_34 | agi_35 | int_3 | cha_3|level(25),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_7|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_4,zombie_face],
  ["skeleton_knight","Skeleton Knight","Skeleton Knights",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_shihai_liaoyajian, itm_duangang_xiugaiqi, itm_steppe_kulouma, itm_bone_mound_fan_shaped_shield, itm_jinshi_touqiang, itm_liujin_banjia, itm_zhongxing_banjiaxue, itm_kongju_bikai],
   str_54 | agi_55 | int_3 | cha_3|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_4,zombie_face],
  ["skeleton_archer","Skeleton Archer","Skeleton Archers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_arrows, itm_khergit_arrows, itm_hunting_bow, itm_short_bow, itm_nomad_bow, itm_xiongjiakulou, itm_leather_boots, itm_sword_medieval_b_small, itm_sword_medieval_c],
   str_23 | agi_24 | int_3 | cha_3|level(16),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130) | wp_archery (170) | wp_crossbow (130) | wp_throwing (130),knows_ironflesh_5|knows_power_strike_4|knows_power_throw_4|knows_power_draw_5|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4,zombie_face],
  ["skeleton_heavy_archer","Skeleton Heavy Archer","Skeleton Heavy Archers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulou_zhanshishenti, itm_leather_gloves, itm_mail_mittens, itm_splinted_leather_greaves, itm_mail_chausses, itm_arabian_sword_b, itm_sarranid_cavalry_sword, itm_kettle_hat, itm_undead_hateful_bow, itm_busi_jiayuanjian],
   str_34 | agi_35 | int_3 | cha_3|level(25),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (260) | wp_crossbow (200) | wp_throwing (200),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_4,zombie_face],
  ["skeleton_ranger","Skeleton Ranger","Skeleton Rangers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_kulouma, itm_skeleton_plate, itm_lianjia_quanfu_guokui, itm_mail_mittens, itm_mail_boots, itm_undead_hateful_bow, itm_busi_jiayuanjian, itm_busi_jiayuanjian, itm_shihai_liaoyajian],
   str_48 | agi_55 | int_3 | cha_3|level(45),wp_one_handed (390) | wp_two_handed (390) | wp_polearm (390) | wp_archery (460) | wp_crossbow (390) | wp_throwing (390),knows_ironflesh_9|knows_power_strike_9|knows_power_throw_9|knows_power_draw_10|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_7,zombie_face],

  ["fragmented_dragonbone_guardian","Fragmented Dragonbone Guardian","Fragmented Dragonbone Guardians",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_30 | agi_30 | int_12 | cha_3|level(20),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_3|knows_horse_archery_4,zombie_face],
  ["debris_dragonbone_warrior","Debris Dragonbone Warrior","Debris Dragonbone Warriors",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_40 | agi_40 | int_12 | cha_3|level(28),wp_one_handed (260) | wp_two_handed (260) | wp_polearm (260) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260),knows_ironflesh_9|knows_power_strike_8|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_4,zombie_face],
  ["relic_dragonbone_swordsmaster","Relic Dragonbone Swordsmaster","Relic Dragonbone Swordsmasters",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_50 | agi_50 | int_12 | cha_3|level(36),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_6|knows_shield_5|knows_athletics_6|knows_riding_6|knows_horse_archery_4,zombie_face],
  ["dragonbone_knight","Dragonbone Knight","Dragonbone Knights",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_65 | agi_60 | int_12 | cha_3|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),knows_ironflesh_11|knows_power_strike_10|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_8|knows_shield_6|knows_athletics_8|knows_riding_8|knows_horse_archery_5,zombie_face],
  ["dragonbone_overlord","Dragonbone Overlord","Dragonbone Overlords",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_100 | agi_90 | int_12 | cha_3|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),knows_ironflesh_15|knows_power_strike_13|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_10|knows_shield_7|knows_athletics_9|knows_riding_10|knows_horse_archery_7,zombie_face],

  ["dragonfang_lancer","Dragonfang Lancer","Dragonfang Lancers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_32 | agi_33 | int_6 | cha_3|level(24),wp_one_handed (240) | wp_two_handed (240) | wp_polearm (240) | wp_archery (240) | wp_crossbow (240) | wp_throwing (240),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_3,zombie_face],
  ["dragonfang_foehn_lancer","Dragonfang Foehn Lancer","Dragonfang Foehn Lancers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_54 | agi_55 | int_6 | cha_3|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_4,zombie_face],
  ["dragonfang_frostgravel_ranger","Dragonfang Frostgravel Ranger","Dragonfang Frostgravel Rangers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_54 | agi_55 | int_6 | cha_3|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_4,zombie_face],

  ["dragonclaw_assassin","Dragonclaw Assassin","Dragonclaw Assassins",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_60 | agi_55 | int_6 | cha_3|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (450) | wp_throwing (450),knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_8|knows_riding_8|knows_horse_archery_4,zombie_face],

  ["unburned_bones","Unburned Bones","Unburned Bones",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_skeleton_unburned, itm_skull_unburned, itm_skeleton_unburned_calf, itm_skeleton_unburned_hand],
   str_27 | agi_31 | int_99 | cha_3|level(25),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_6|knows_shield_2|knows_athletics_3,zombie_face],
  ["candle_of_bone","Candle of Bone","Candles of Bone",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_skeleton_candle, itm_skull_candle, itm_skeleton_candle_calf, itm_skeleton_candle_hand],
   str_36 | agi_40 | int_99 | cha_3|level(35),wp_one_handed (40) | wp_two_handed (40) | wp_polearm (40) | wp_archery (40) | wp_crossbow (40) | wp_throwing (40),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_8|knows_shield_4|knows_athletics_4,zombie_face],
  ["blazing_thing_imitation","Blazing Thing Imitation","Blazing Thing Imitations",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_skeleton_blazing_thing, itm_skeleton_blazing_thing_skull, itm_skeleton_blazing_thing_calf, itm_skeleton_blazing_thing_hand],
   str_54 | agi_60 | int_99 | cha_3|level(50),wp_one_handed (325) | wp_two_handed (325) | wp_polearm (325) | wp_archery (325) | wp_crossbow (325) | wp_throwing (325),knows_ironflesh_14|knows_power_strike_8|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_9|knows_shield_5|knows_athletics_5,zombie_face],
  ["eternalflame_unburned_one","Eternalflame Unburned One","Eternalflame Unburned Ones",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_eternalflame_unburned_plate, itm_eternalflame_unburned_skull, itm_eternalflame_unburned_boot, itm_skeleton_blazing_thing_hand],
   str_77 | agi_90 | int_199 | cha_3|level(60),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),knows_ironflesh_15|knows_power_strike_9|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_10|knows_shield_6|knows_athletics_6,zombie_face],

  ["curse_carrier","Curse Carrier","Curse Carriers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_10 | agi_30 | int_3 | cha_3|level(25),wp_one_handed (30) | wp_two_handed (30) | wp_polearm (30) | wp_archery (30) | wp_crossbow (30) | wp_throwing (30),knows_ironflesh_4|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_2|knows_shield_4|knows_athletics_7|knows_riding_2|knows_horse_archery_2,zombie_face],
  ["curse_exploder","Curse Exploder","Curse Exploders",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_16 | agi_48 | int_3 | cha_3|level(32),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_6|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_5|knows_athletics_11|knows_riding_4|knows_horse_archery_4,zombie_face],

  ["elf_skeleton","Elf Skeleton","Elf Skeletons",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_12 | agi_26 | int_3 | cha_3|level(15),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (180) | wp_crossbow (120) | wp_throwing (120),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_power_draw_5|knows_weapon_master_4|knows_shield_1|knows_athletics_5|knows_riding_3|knows_horse_archery_4,zombie_face],
  ["resentment_archer","Resentment Archer","Resentment Archers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_25 | agi_57 | int_7 | cha_3|level(36),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (400) | wp_crossbow (300) | wp_throwing (300),knows_ironflesh_5|knows_power_strike_4|knows_power_throw_4|knows_power_draw_9|knows_weapon_master_6|knows_shield_3|knows_athletics_9|knows_riding_7|knows_horse_archery_8,zombie_face],
  ["frostcurse_cavalier","Frostcurse Cavalier","Frostcurse Cavaliers",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_25 | agi_71 | int_14 | cha_3|level(55),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (580) | wp_crossbow (500) | wp_throwing (500),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_13|knows_weapon_master_9|knows_shield_5|knows_athletics_12|knows_riding_9|knows_horse_archery_10,zombie_face],

  ["kouruto_wild_hunter_cavalry","Kouruto Wild Hunter Cavalry","Kouruto Wild Hunter Cavalries",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_leather_boots, itm_sword_medieval_a, itm_sword_medieval_b, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_60 | agi_60 | int_3 | cha_3|level(48),wp_one_handed (480) | wp_two_handed (480) | wp_polearm (480) | wp_archery (480) | wp_crossbow (480) | wp_throwing (480),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_7|knows_power_draw_8|knows_weapon_master_7|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_7,zombie_face],


#ghost
  ["poltergeist","Poltergeist","Poltergeist",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_ghost_dress, itm_ghost_court_dress, itm_ghost_woolen_dress, itm_ghost_boot, itm_ghost_tulbent, itm_ghost_knife],
   str_6 | agi_18 | int_3 | cha_17|level(10),wp_one_handed (50) | wp_two_handed (50) | wp_polearm (50) | wp_archery (50) | wp_crossbow (50) | wp_throwing (50),knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_7|knows_riding_1|knows_horse_archery_1,0],
  ["grudge_ghost","Grudge Ghost","Grudge Ghost",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_ghost_nobleman_outf, itm_ghost_merchant_outf, itm_ghost_boot, itm_ghost_leather_cap, itm_ghost_lthr_glove, itm_ghost_dagger],
   str_11 | agi_29 | int_3 | cha_25|level(20),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (80) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_9|knows_riding_2|knows_horse_archery_2,0],
  ["ghost_soldier","Ghost Soldier","Ghost Soldier",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_ghost_blue_gambeson, itm_ghost_white_gambeson, itm_ghost_boot, itm_ghost_padded_coif, itm_ghost_lthr_glove, itm_ghost_long_sword],
   str_17 | agi_50 | int_3 | cha_31|level(32),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_5|knows_shield_3|knows_athletics_11|knows_riding_3|knows_horse_archery_3,0],
  ["shadow_reaper","Shadow Reaper","Shadow Reaper",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_duagang_liandao, itm_ghost_boot, itm_ghost_mail_coif, itm_ghost_surcoat, itm_ghost_mail_mitten],
   str_22 | agi_61 | int_3 | cha_48|level(45),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (1770) | wp_archery (170) | wp_crossbow (170) | wp_throwing (170),knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_7|knows_shield_4|knows_athletics_13|knows_riding_4|knows_horse_archery_4,0],
  ["shadow_runner","Shadow Runner","Shadow Runner",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_ghost_boot, itm_ghost_outfit, itm_ghost_hood, itm_ghost_lthr_glove, itm_ghost_sickle],
   str_19 | agi_57 | int_3 | cha_40|level(38),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_3|knows_athletics_12|knows_riding_2|knows_horse_archery_2,0],

  ["phantom_rider","Phantom Rider","Phantom Rider",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_ghost_horse, itm_ghost_boot, itm_ghost_mail_coif, itm_ghost_surcoat, itm_ghost_lthr_glove, itm_ghost_steel_pick],
   str_20 | agi_60 | int_6 | cha_41|level(40),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),knows_ironflesh_5|knows_power_strike_4|knows_power_throw_4|knows_power_draw_3|knows_weapon_master_6|knows_shield_3|knows_athletics_13|knows_riding_6|knows_horse_archery_6,0],
  ["shatter_knight","Shatter Knight","Shatter Knight",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_fantom_nightmare, itm_death_omen, itm_death_announcer_cloak, itm_ghost_boot, itm_no_head],
   str_38 | agi_150 | int_15 | cha_71|level(60),wp_one_handed (260) | wp_two_handed (200) | wp_polearm (260) | wp_archery (200) | wp_crossbow (200) | wp_throwing (260),knows_ironflesh_9|knows_power_strike_8|knows_power_throw_8|knows_power_draw_7|knows_weapon_master_10|knows_shield_7|knows_athletics_15|knows_riding_10|knows_horse_archery_10,0],
  ["deadlight_cavalry","Deadlight Cavalry","Deadlight Cavalry",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_ghost_horse, itm_ghost_boot, itm_ghost_flattop_helmet, itm_ghost_surcoat, itm_ghost_lthr_glove],
   str_26 | agi_93 | int_9 | cha_54|level(51),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (200) | wp_archery (150) | wp_crossbow (150) | wp_throwing (200),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_5|knows_weapon_master_8|knows_shield_5|knows_athletics_14|knows_riding_8|knows_horse_archery_8,0],

  ["backstabber","Backstabber","Backstabber",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_ghost_boot, itm_ghost_assassin_cloth, itm_ghost_hood, itm_ghost_lthr_glove],
   str_21 | agi_100 | int_7 | cha_50|level(49),wp_one_handed (200) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (200),knows_ironflesh_6|knows_power_strike_7|knows_power_throw_7|knows_power_draw_3|knows_weapon_master_7|knows_shield_4|knows_athletics_13|knows_riding_4|knows_horse_archery_4,0],
  ["shadow_assassin","Shadow Assassin","Shadow Assassin",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_ghost_boot, itm_ghost_assassin_cloth, itm_ghost_lthr_glove],
   str_30 | agi_170 | int_12 | cha_70|level(58),wp_one_handed (200) | wp_two_handed (230) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (230),knows_ironflesh_7|knows_power_strike_8|knows_power_throw_8|knows_power_draw_4|knows_weapon_master_9|knows_shield_5|knows_athletics_14|knows_riding_5|knows_horse_archery_5,0],

  ["qingqiu_nagzul","Qingqiu Nagzul","Qingqiu Nagzul",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_ghost_boot, itm_ghost_lthr_glove, itm_ghost_battle_fork],
   str_17 | agi_53 | int_18 | cha_34|level(35),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (180) | wp_crossbow (160) | wp_throwing (160) | wp_firearm (50),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_4|knows_weapon_master_6|knows_shield_3|knows_athletics_10|knows_riding_3|knows_horse_archery_2,0],
  ["qingqiu_warrior","Qingqiu Warrior","Qingqiu Warrior",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_ghost_boot, itm_ghost_lthr_glove],
   str_22 | agi_78 | int_21 | cha_48|level(42),wp_one_handed (190) | wp_two_handed (190) | wp_polearm (190) | wp_archery (240) | wp_crossbow (190) | wp_throwing (190) | wp_firearm (80),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_5|knows_weapon_master_7|knows_shield_5|knows_athletics_12|knows_riding_3|knows_horse_archery_3,0],
  ["soul_summoning_envoy","Soul Summoning Envoy","Soul Summoning Envoy",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_ghost_boot],
   str_30 | agi_120 | int_25 | cha_67|level(54),wp_one_handed (230) | wp_two_handed (230) | wp_polearm (230) | wp_archery (280) | wp_crossbow (230) | wp_throwing (230) | wp_firearm (100),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_7|knows_weapon_master_9|knows_shield_7|knows_athletics_13|knows_riding_5|knows_horse_archery_5,0],
  ["devil_bride","Devil's Bride","Devil's Bride",tf_ghost|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_ghost_boot, itm_ghost_bride_crown, itm_ghost_bride_dress],
   str_19 | agi_57 | int_3 | cha_40|level(60),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (140) | wp_crossbow (140) | wp_throwing (140),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_6|knows_shield_3|knows_athletics_12|knows_riding_2|knows_horse_archery_2,0],


#walker
  ["new_walker","New Walker","New Walker",tf_walker|tf_allways_fall_dead|tf_no_capture_alive,0,0,fac_heresy_undead,
   [itm_wrapping_boots, itm_woolen_hose, itm_blue_hose, itm_hunter_boots, itm_hide_boots, itm_ankle_boots, itm_nomad_boots, itm_coarse_tunic, itm_leather_apron, itm_tabard, itm_shirt, itm_linen_tunic, itm_leather_jacket, itm_rawhide_coat, itm_fur_coat, itm_sickle, itm_cleaver, itm_knife, itm_butchering_knife, itm_dagger, itm_falchion, itm_wooden_stick, itm_cudgel, itm_hammer],
   str_14 | agi_7 | int_3 | cha_3|level(10),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),knows_power_throw_1|knows_weapon_master_1|knows_athletics_1,man_face_younger_1, man_face_older_2],
  ["walker_warrior","Walker Warrior","Walker Warriors",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_steppe_armor, itm_gambeson, itm_blue_gambeson, itm_red_gambeson, itm_padded_cloth, itm_aketon_green, itm_leather_jerkin, itm_nomad_vest, itm_ragged_outfit, itm_padded_leather, itm_tribal_warrior_outfit, itm_nomad_robe, itm_nomad_boots, itm_leather_boots, itm_splinted_leather_greaves, itm_arming_cap, itm_leather_steppe_cap_a, itm_leather_steppe_cap_b, itm_leather_steppe_cap_c, itm_leather_warrior_cap, itm_skullcap, itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_military_fork, itm_battle_fork, itm_boar_spear, itm_shortened_spear, itm_spear, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield],
   str_20 | agi_12 | int_3 | cha_3|level(25),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),knows_ironflesh_1|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_1|knows_athletics_3,man_face_younger_1, man_face_older_2],
  ["walker_swordman","Walker Swordman","Walker Swordmen",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_heresy_undead,
   [itm_mail_with_surcoat, itm_surcoat_over_mail, itm_puweier_lianjia, itm_westcoast_covered_chain_armor_robe, itm_shenlan_lianjiazhaopao, itm_honghua_lianjia, itm_brown_eagle_chain_armor_robe, itm_mail_mittens, itm_mail_chausses, itm_splinted_greaves, itm_helmet_with_neckguard, itm_flat_topped_helmet, itm_kelutuo_duizhangkui, itm_banmian_lianjiakui, itm_guyongbing_tiekui, itm_tab_shield_kite_c, itm_tab_shield_heater_c, itm_tab_shield_small_round_b, itm_bastard_sword_a, itm_bastard_sword_b, itm_throwing_spears, itm_jarid],
   str_24 | agi_18 | int_3 | cha_3|level(30),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_3|knows_athletics_5|knows_riding_2,man_face_younger_1, man_face_older_2],
  ["walker_soldier","Walker Soldier","Walker Soldiers",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_guyongbing_jia, itm_guyongbing_tiekui, itm_mail_mittens, itm_mail_boots, itm_great_axe, itm_long_axe, itm_long_axe_alt, itm_long_axe_b, itm_long_axe_b_alt, itm_long_axe_c, itm_long_axe_c_alt],
   str_27 | agi_21 | int_3 | cha_3|level(35),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),knows_ironflesh_5|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_3,man_face_younger_1, man_face_older_2],
  ["turbid_cavalry","Turbid Cavalry","Submerge Cavalries",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_jiangshi_ma, itm_powell_lifeguard_plate, itm_silingqishi_kui, itm_bone_mound_fan_shaped_shield, itm_heise_banlianjiaxue, itm_mogang_yuanzhi_bikai, itm_yanlun_kongnvefu, itm_touguan_toumao],
   str_30 | agi_29 | int_3 | cha_3|level(47),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_1,man_face_younger_1, man_face_older_2],
  ["walker_centurion","Walker Centurion","Walker Centurions",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [],
   str_26 | agi_21 | int_3 | cha_3|level(35),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_4|knows_shield_4|knows_athletics_6|knows_riding_2,man_face_younger_1, man_face_older_2],
  ["walker_chieftain","Walker Chieftain","Walker Chieftains",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_heresy_undead,
   [itm_gauntlets, itm_iron_greaves, itm_bascinet, itm_tuzai_zhandao, itm_steel_asterisk_staff],
   str_33 | agi_24 | int_3 | cha_3|level(50),wp_one_handed (370) | wp_two_handed (370) | wp_polearm (370) | wp_archery (370) | wp_crossbow (370) | wp_throwing (370),knows_riding_2|knows_athletics_10|knows_shield_5|knows_weapon_master_7|knows_power_draw_5|knows_power_throw_5|knows_power_strike_8|knows_ironflesh_7,man_face_younger_1, man_face_older_2],

  ["submerge_knight","Submerge Knight","Submerge Knights",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_heresy_undead,
   [itm_jiangshi_ma, itm_powell_lifeguard_plate, itm_silingqishi_kui, itm_bone_mound_fan_shaped_shield, itm_heise_banlianjiaxue, itm_mogang_yuanzhi_bikai, itm_yanlun_kongnvefu, itm_touguan_toumao],
   str_138 | agi_27 | int_3 | cha_3|level(59),wp_one_handed (420) | wp_two_handed (420) | wp_polearm (420) | wp_archery (420) | wp_crossbow (420) | wp_throwing (420),knows_ironflesh_8|knows_power_strike_9|knows_power_throw_7|knows_power_draw_7|knows_weapon_master_9|knows_shield_5|knows_athletics_6|knows_riding_6|knows_horse_archery_3,man_face_younger_1, man_face_older_2],

  ["new_walker_mission_1","New Walker","New Walker",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_armor,0,0,fac_heresy_undead,#use for mozu charpter two
   [itm_qishi_pao2, itm_qishi_pao, itm_leather_covered_round_shield, itm_beast_skin_round_shield, itm_shortened_spear, itm_spear, itm_fighting_pick, itm_military_hammer, itm_spiked_mace, itm_winged_mace, itm_black_hood, itm_sword_viking_1, itm_leather_gloves, itm_ankle_boots, itm_leather_boots, itm_pilgrim_hood],
   str_37 | agi_8 | int_3 | cha_3|level(20),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),knows_ironflesh_1|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_1|knows_shield_1,man_face_younger_1, man_face_older_2],
  ["new_walker_mission_2","New Walker","New Walker",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_armor,0,0,fac_heresy_undead,
   [itm_dark_worshipper_leather_armor, itm_forsaken_chain_hood, itm_qishi_pibanlianjai, itm_qishi_pao3, itm_mail_mittens, itm_splinted_greaves, itm_steel_shield, itm_cruel_morningstar_hammer, itm_simple_cruel_morningstar_hammer],
   str_37 | agi_8 | int_3 | cha_3|level(20),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),knows_ironflesh_1|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_1|knows_shield_1,man_face_younger_1, man_face_older_2],
  ["new_walker_mission_3","New Walker","New Walker",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_heresy_undead,
   [itm_dark_apprentice_robe, itm_fenzhi_jiaqiangshoutao, itm_leather_boots, itm_forsaken_chain_hood],
   str_37 | agi_8 | int_3 | cha_3|level(20),wp_one_handed (180) | wp_two_handed (180) | wp_polearm (180) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180),knows_ironflesh_1|knows_power_throw_1|knows_power_draw_3|knows_weapon_master_1|knows_shield_1,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, 0x00000001b80032473ac49738206626b200000000001da7660000000000000000],
  ["walker_swordman_mission","Walker Swordman","Walker Swordmen",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_mounted|tf_guarantee_horse,0,0,fac_heresy_undead,
   [itm_jiangshi_ma, itm_puweier_lianjia, itm_mail_mittens, itm_splinted_greaves, itm_flat_topped_helmet, itm_tab_shield_kite_c, itm_bastard_sword_b, itm_throwing_spears],
   str_45 | agi_15 | int_3 | cha_3|level(30),wp_one_handed (280) | wp_two_handed (280) | wp_polearm (280) | wp_archery (280) | wp_crossbow (280) | wp_throwing (280),knows_ironflesh_6|knows_power_strike_5|knows_power_throw_5|knows_power_draw_8|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_2,man_face_younger_1, man_face_older_2],
  ["walker_soldier_mission","Walker Soldier","Walker Soldiers",tf_walker|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,0,0,fac_heresy_undead,
   [itm_jiangshi_ma, itm_guyongbing_jia, itm_guyongbing_tiekui, itm_mail_mittens, itm_mail_boots, itm_long_axe_c_alt],
   str_57 | agi_21 | int_3 | cha_3|level(35),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_9|knows_weapon_master_4|knows_shield_5|knows_athletics_6|knows_riding_3,man_face_younger_1, man_face_older_2],



#############################################################科鲁托浪民##########################################################

  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws_kouruto_refugee,
   [],
   str_9 | agi_8 | int_5 | cha_5|level(10),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),knows_ironflesh_3|knows_power_strike_1|knows_power_throw_1|knows_power_draw_2|knows_weapon_master_2|knows_shield_2|knows_athletics_2|knows_riding_3|knows_horse_archery_2,kouruto_face_younger_1, kouruto_face_young_2],
  ["kouruto_refugee_thief","Kouruto Refugee Thief","Kouruto Refugee Thieves",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_outlaws_kouruto_refugee,
   [],
   str_15 | agi_12 | int_9 | cha_9|level(20),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (170) | wp_crossbow (170) | wp_throwing (170),knows_ironflesh_6|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_weapon_master_3|knows_shield_3|knows_athletics_4|knows_riding_4|knows_horse_archery_4,kouruto_face_young_1, kouruto_face_middle_2],
  ["kouruto_refugee_looter","Kouruto Refugee Looter","Kouruto Refugee Looters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_outlaws_kouruto_refugee,
   [],
   str_19 | agi_15 | int_9 | cha_9|level(28),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (250) | wp_archery (250) | wp_crossbow (250) | wp_throwing (250),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_6|knows_weapon_master_6|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_6,kouruto_face_middle_1, kouruto_face_old_2],
  ["kouruto_refugee_warrior","Kouruto Refugee Warrior","Kouruto Refugee Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_outlaws_kouruto_refugee,
   [],
   str_26 | agi_18 | int_12 | cha_15|level(42),wp_one_handed (360) | wp_two_handed (360) | wp_polearm (360) | wp_archery (360) | wp_crossbow (360) | wp_throwing (360),knows_ironflesh_9|knows_power_strike_8|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_7,kouruto_face_middle_1, kouruto_face_old_2],
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_outlaws_kouruto_refugee,
   [],
   str_24 | agi_18 | int_15 | cha_12|level(45),wp_one_handed (320) | wp_two_handed (320) | wp_polearm (320) | wp_archery (320) | wp_crossbow (320) | wp_throwing (320),knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_7|knows_weapon_master_7|knows_shield_5|knows_athletics_7|knows_riding_8|knows_horse_archery_8,kouruto_face_middle_1, kouruto_face_old_2],



#############################################################冒险者协会##########################################################

  ["blackiron_adventurer","Blackiron Adventurer","Blackiron Adventurers",#黑铁级冒险者
   tf_guarantee_boots|tf_guarantee_armor,
   0,0,fac_adventurers_association,
   [itm_wrapping_boots, itm_woolen_hose, itm_blue_hose, itm_hunter_boots, itm_hide_boots, itm_ankle_boots, itm_nomad_boots, itm_leather_boots, itm_coarse_tunic, itm_leather_apron, itm_tabard, itm_leather_vest, itm_steppe_armor, itm_padded_cloth, itm_blue_gambeson, itm_red_gambeson, itm_aketon_green, itm_leather_jerkin, itm_straw_hat, itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_headcloth, itm_woolen_hood, itm_arming_cap, itm_fur_hat, itm_turban, itm_leather_warrior_cap, itm_cudgel, itm_hammer, itm_club, itm_fighting_pick, itm_dagger, itm_hatchet, itm_sword_medieval_a, itm_sword_medieval_b_small, itm_mace_1, itm_sarranid_two_handed_mace_1, itm_boar_spear, itm_wooden_shield, itm_nordic_shield, itm_fur_covered_shield, itm_beast_skin_round_shield, itm_throwing_knives, itm_arrows, itm_hunting_bow, itm_shortened_spear],
   str_6 | agi_6 | int_5 | cha_4|level(5),wp_one_handed (45) | wp_two_handed (45) | wp_polearm (45) | wp_archery (45) | wp_crossbow (45) | wp_throwing (45),
   knows_ironflesh_1|knows_athletics_1|knows_looting_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_first_aid_1|knows_devout_1|knows_trade_1,
   man_face_younger_1, man_face_older_2],
  ["barecopper_adventurer","Barecopper Adventurer","Barecopper Adventurers",#赤铜级冒险者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 
   0,0,fac_adventurers_association,
   [itm_leather_gloves, itm_arrows, itm_leather_boots, itm_nomad_boots, itm_blue_gambeson, itm_red_gambeson, itm_padded_cloth, itm_aketon_green, itm_leather_jerkin, itm_nomad_vest, itm_ragged_outfit, itm_padded_leather, itm_tribal_warrior_outfit, itm_nomad_robe, itm_studded_leather_coat, itm_kelutuo_shense_pijia, itm_kelutuo_qianse_pijia, itm_hongse_dianchengjia, itm_hongse_dianchengpao, itm_wangguo_mingbin_mianjia, itm_zonghong_mianjia, itm_zonghong_diancheng_jia, itm_lvse_dianchengjia, itm_lvse_minbing_mianjia, itm_leather_warrior_cap, itm_skullcap, itm_mail_coif, itm_footman_helmet, itm_nasal_helmet, itm_norman_helmet, itm_segmented_helmet, itm_darts, itm_throwing_daggers, itm_short_bow, itm_nomad_bow, itm_sword_medieval_c, itm_sword_medieval_c_small, itm_sword_medieval_c_long, itm_sword_medieval_d_long, itm_one_handed_war_axe_a, itm_one_handed_battle_axe_a, itm_two_handed_axe, itm_scimitar, itm_spear, itm_bamboo_spear, itm_war_spear, itm_pike, itm_plate_covered_round_shield, itm_leather_covered_round_shield, itm_beast_skin_round_shield, itm_tab_shield_round_a, itm_tab_shield_round_b],
   str_9 | agi_8 | int_7 | cha_6|level(10),wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (85) | wp_crossbow (85) | wp_throwing (85),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_looting_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_devout_1|knows_leadership_1|knows_trade_1,
   man_face_younger_1, man_face_older_2],
  ["whitesilver_adventurer","Whitesilver Adventurer","Whitesilver Adventurers",#白银级冒险者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield ,
   0,0,fac_adventurers_association,
   [itm_byrnie, itm_haubergeon, itm_lamellar_vest, itm_lamellar_vest_khergit, itm_mail_shirt, itm_mail_hauberk, itm_leather_boots, itm_splinted_leather_greaves, itm_mail_chausses, itm_leather_gloves, itm_mail_mittens, itm_helmet_with_neckguard, itm_flat_topped_helmet, itm_kettle_hat, itm_spiked_helmet, itm_nordic_helmet, itm_sarranid_warrior_cap, itm_sarranid_horseman_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_vaegir_fur_helmet, itm_sarranid_cavalry_sword, itm_arabian_sword_d, itm_fighting_axe, itm_bastard_sword_a, itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_two_handed_battle_axe_2, itm_long_axe, itm_bardiche, itm_sword_medieval_d_long, itm_sword_viking_3, itm_sword_khergit_3, itm_sword_khergit_4, itm_ashwood_pike, itm_awlpike, itm_awlpike_long, itm_tab_shield_round_c, itm_tab_shield_kite_b, itm_tab_shield_kite_c, itm_tab_shield_heater_b, itm_tab_shield_heater_c, itm_war_darts, itm_throwing_spears, itm_throwing_daggers, itm_nomad_bow, itm_long_bow, itm_kouruto_bow, itm_khergit_arrows, itm_barbed_arrows],
   str_14 | agi_13 | int_8 | cha_7|level(20),wp_one_handed (185) | wp_two_handed (185) | wp_polearm (185) | wp_archery (185) | wp_crossbow (185) | wp_throwing (185),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_2,
   man_face_younger_1, man_face_old_2],

  ["gold_adventurer","Gold Adventurer","Gold Adventurers",#黄金级冒险者
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_adventurers_association,
   [itm_arabian_armor_b, itm_sarranid_mail_shirt, itm_mail_with_surcoat, itm_surcoat_over_mail, itm_brigandine_red, itm_lamellar_armor, itm_scale_armor, itm_splinted_greaves, itm_mail_boots, itm_sarranid_boots_c, itm_sarranid_boots_d, itm_tab_shield_round_c, itm_tab_shield_round_d, itm_tab_shield_kite_c, itm_tab_shield_kite_cav_a, itm_tab_shield_heater_d, itm_tab_shield_heater_cav_a, itm_tab_shield_small_round_a, itm_tab_shield_small_round_b, itm_throwing_spears, itm_jarid, itm_throwing_axes, itm_kouruto_bow, itm_strong_bow, itm_barbed_arrows, itm_bodkin_arrows, itm_shidun_lianjiazhaopao, itm_lvbai_lianjiazhaopao, itm_lvjian_lianjiazhaopao, itm_thunderwing_chain_armor_robe, itm_jinhua_lianjiazhaopao, itm_hongtiepi_lianjiashan, itm_gongniu_lianjiazhaopao, itm_cormorant_chain_armor_robe, itm_eagle_flock_chain_armor_robe, itm_lianghuang_lianjiazhaopao, itm_qingse_lianjiazhaopao, itm_lanse_lianjiazhaopao, itm_zase_ma, itm_huise_ma, itm_heise_ma, itm_steppe_horse, itm_arabian_horse_a, itm_courser, itm_mountain_horse, itm_hunter, itm_light_lance, itm_lance, itm_awlpike, itm_awlpike_long, itm_scimitar_b, itm_arabian_sword_d, itm_military_cleaver_b, itm_bastard_sword_b, itm_two_handed_battle_axe_2, itm_long_axe_b_alt, itm_great_bardiche, itm_sword_medieval_d_long, itm_sword_khergit_4, itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_vaegir_war_helmet, itm_bascinet_2, itm_bascinet_3],
   str_19 | agi_17 | int_10 | cha_9|level(30),wp_one_handed (285) | wp_two_handed (285) | wp_polearm (285) | wp_archery (285) | wp_crossbow (285) | wp_throwing (285),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_5|knows_study_3|knows_devout_3|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   man_face_younger_1, man_face_old_2],

  ["mithril_adventurer","Mithril Adventurer","Mithril Adventurers",#秘银级冒险者
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,
   0,0,fac_adventurers_association,
   [itm_heibai_banjiayi, itm_lanbai_banjiayi, itm_lvbai_banjiayi, itm_hongbai_banjiayi, itm_huangbai_banjiayi, itm_westcoast_leather_armed_clothing, itm_coat_of_plates, itm_coat_of_plates_red, itm_khergit_elite_armor, itm_kouruto_elite_heavy_lamellar_armor, itm_sarranid_elite_armor, itm_mail_mittens, itm_scale_gauntlets, itm_lamellar_gauntlets, itm_mail_boots, itm_iron_greaves, itm_sarranid_veiled_helmet, itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet, itm_vaegir_war_helmet, itm_vaegir_mask, itm_bascinet_3, itm_guard_helmet, itm_tab_shield_round_e, itm_tab_shield_kite_cav_b, itm_tab_shield_heater_cav_b, itm_tab_shield_small_round_c, itm_strong_bow, itm_war_bow, itm_bodkin_arrows, itm_jarid, itm_heavy_throwing_axes, itm_great_lance, itm_scimitar_b, itm_arabian_sword_d, itm_great_sword, itm_military_cleaver_c, itm_bastard_sword_b, itm_great_long_bardiche, itm_sword_medieval_d_long, itm_powell_noble_hand_and_a_half_sword, itm_silver_plated_hand_and_half_sword, itm_powell_noble_sword, itm_silver_plated_sword, itm_zhiren_zhandao, itm_duangang_zhandao, itm_duangang_kuanrengzhandao, itm_duangang_youxiajian, itm_heibaitiaopijia_ma, itm_shiwenpijia_ma, itm_jinhongpijia_ma, itm_lanlvshipijia_ma, itm_jinyinpijia_ma, itm_lvqinpijia_ma, itm_jinshizi_ma, itm_lanjinpijia_ma, itm_shifupijia_ma, itm_qinlvpijia_ma, itm_hongbaiyinpijia_ma, itm_lanshizipijia_ma, itm_languanpijia_ma, itm_hongshizipijia_ma, itm_huangyingpijia_ma],
   str_24 | agi_22 | int_11 | cha_9|level(40),wp_one_handed (385) | wp_two_handed (385) | wp_polearm (385) | wp_archery (385) | wp_crossbow (385) | wp_throwing (385),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_7|knows_study_5|knows_devout_3|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   man_face_younger_1, man_face_old_2],

  ["orichalcos_adventurer","Orichalcos Adventurer","Orichalcos Adventurers", #山铜级冒险者
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_baipao_banlian, itm_honghuangpao_banlian, itm_heibai_banjiayi, itm_lanbai_banjiayi, itm_lvbai_banjiayi, itm_hongbai_banjiayi, itm_huangbai_banjiayi, itm_coat_of_plates, itm_coat_of_plates_red, itm_plate_armor, itm_tiesezhongxingbanjia, itm_iron_chest_plate, itm_rogue_iron_chest_plate, itm_heise_zaoqi_banjia, itm_heibai_zaoqi_banjia, itm_lanse_zaoqi_banjia, itm_hongse_zaoqi_banjia, itm_honeysuckle_fan_shaped_shield, itm_black_yellow_skoutarion, itm_red_yellow_skoutarion, itm_blue_breeze_round_shield, itm_sea_monster_fan_shaped_shield, itm_hippocampus_skoutarion, itm_tab_shield_small_round_c, itm_tab_shield_heater_cav_b, itm_knight_black_white_fan_shaped_shield, itm_tab_shield_kite_cav_b, itm_powell_noble_sword, itm_zhanshi_chu, itm_qishi_dingtouchui, itm_sword_khergit_4, itm_silver_plated_battle_sword, itm_silver_plated_sabre, itm_silver_plated_hand_and_half_sword, itm_duangang_youxiajian, itm_duangang_danshoujian, itm_mogang_guizujian, itm_jinshi_qibingjian, itm_jinse_bubingjian, itm_handguard_hammer, itm_one_handed_battle_axe_c, itm_danshou_chanfu, itm_flat_topped_helmet, itm_gorgeous_eagle_helmet, itm_jiaoguo_zhongkui, itm_xihai_dingshikui, itm_xihai_shoulingkui, itm_xihai_fumiankui, itm_guyongbing_tiekui, itm_guyongbing_zhongkui, itm_guyongbing_quankui, itm_mercenary_knight_helmet, itm_mail_boots, itm_iron_greaves, itm_lamellar_gauntlets, itm_mail_mittens, itm_sorcery_lance, itm_ellite_lance, itm_knight_recurve_bow, itm_maoxianzhe_buqiangjian, itm_shense_banzhajia_caoyuanma, itm_tuselianjia_ma, itm_honglong_lianjia_pingyuanma, itm_baiyang_lianjia_pinyuanma],
   str_32 | agi_30 | int_18 | cha_13|level(50), wp_one_handed (485) | wp_two_handed (485) | wp_polearm (485) | wp_archery (485) | wp_crossbow (485) | wp_throwing (485),
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_6|knows_power_draw_6|knows_weapon_master_8|knows_shield_8|knows_athletics_9|knows_riding_8|knows_horse_archery_7|knows_looting_5|knows_trainer_5|knows_tracking_6|knows_tactics_5|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_5|knows_first_aid_6|knows_engineer_5|knows_persuasion_8|knows_array_arrangement_6|knows_memory_9|knows_study_8|knows_devout_3|knows_prisoner_management_8|knows_leadership_8|knows_trade_5,
   man_face_younger_1, man_face_middle_2],

  ["primordite_adventurer","Primordite Adventurer","Primordite Adventurers", #奥钢级冒险者
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_hongsequanbanjia_ma, itm_zongsequanbangjia_ma, itm_heisequanbangjia_ma, itm_maoxianzhe_quankui, itm_maoxianzhe_shizikui, itm_maoxianzhe_buqiangjian, itm_baijing_maoxianzhe_jia, itm_huali_banjiaxue, itm_yinse_bikai, itm_mogang_jundao, itm_papal_hand_and_half_sword, itm_silver_winged_knight_sword, itm_kouruto_beast_sabre_simple, itm_mogang_pohuaijian, itm_shihai_liaoyajian, itm_busi_guzhuangjian, itm_baptized_demon_hunting_sword, itm_bloodburst_sword, itm_simple_griffon_skoutarion, itm_blue_dragon_skoutarion, itm_yellow_black_skoutarion, itm_blue_flower_skoutarion],
   str_48 | agi_46 | int_30 | cha_40|level(60),wp_one_handed (585) | wp_two_handed (585) | wp_polearm (585) | wp_archery (585) | wp_crossbow (585) | wp_throwing (585),
   knows_ironflesh_13|knows_power_strike_12|knows_power_throw_9|knows_power_draw_9|knows_weapon_master_11|knows_shield_10|knows_athletics_11|knows_riding_12|knows_horse_archery_11|knows_looting_8|knows_trainer_6|knows_tracking_8|knows_tactics_6|knows_pathfinding_7|knows_spotting_9|knows_inventory_management_6|knows_wound_treatment_7|knows_surgery_7|knows_first_aid_8|knows_engineer_7|knows_persuasion_9|knows_array_arrangement_7|knows_memory_12|knows_study_11|knows_devout_2|knows_prisoner_management_10|knows_leadership_11|knows_trade_7,
   man_face_younger_1, man_face_young_2],

#协会治安兵
  ["association_footman","Association Footman","Association Footmen",#协会治安轻步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_adventurers_association,
   [itm_leather_gloves, itm_leather_boots, itm_aketon_green, itm_helmet_with_neckguard, itm_awlpike, itm_tab_shield_pavise_a],
   str_9 | agi_9 | int_7 | cha_7|level(10),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (70) | wp_crossbow (70) | wp_throwing (70),
   knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1|knows_shield_1|knows_athletics_1|knows_riding_1|knows_horse_archery_1|knows_looting_2|knows_tracking_1|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_1|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_persuasion_1|knows_memory_1|knows_study_1|knows_devout_1|knows_leadership_1|knows_trade_1,
   man_face_young_1, man_face_old_2],
  ["association_infantry","Association Infantry","Association Infantries",#协会治安步兵
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_adventurers_association,
   [itm_tab_shield_pavise_c, itm_lingjia_pao, itm_mail_mittens, itm_splinted_greaves, itm_guard_helmet, itm_sword_medieval_d_long, itm_war_darts],
   str_14 | agi_12 | int_7 | cha_7|level(20),wp_one_handed (170) | wp_two_handed (170) | wp_polearm (170) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_2,
   man_face_middle_1, man_face_old_2],
  ["association_warrior","Association Warrior","Association Warriors",#协会治安武士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,
   0,0,fac_adventurers_association,
   [itm_baipao_banlian, itm_gauntlets, itm_iron_greaves, itm_great_helmet, itm_maoxianzhe_dajian, itm_tab_shield_pavise_d],
   str_19 | agi_16 | int_10 | cha_9|level(30),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_5|knows_study_3|knows_devout_3|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   man_face_old_1, man_face_older_2],
  ["association_crossbowman","Association Crossbowman","Association Crossbowmen",#协会治安弩手
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_baise_xiongjia, itm_leather_gloves, itm_leather_boots, itm_kettle_hat, itm_crossbow, itm_steel_bolts, itm_tab_shield_pavise_c, itm_awlpike_long],
   str_14 | agi_12 | int_7 | cha_7|level(20),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (170) | wp_archery (100) | wp_crossbow (170) | wp_throwing (100),
   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_2|knows_looting_4|knows_trainer_1|knows_tracking_2|knows_tactics_1|knows_pathfinding_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_2|knows_engineer_1|knows_persuasion_2|knows_array_arrangement_1|knows_memory_2|knows_study_2|knows_devout_1|knows_prisoner_management_1|knows_leadership_1|knows_trade_2,
   man_face_young_1, man_face_old_2],
  ["association_ranger","Association Ranger","Association Rangers",#协会治安巡逻兵
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_baise_xiongjia, itm_mail_mittens, itm_splinted_leather_greaves, itm_steel_bolts, itm_tab_shield_heater_cav_a, itm_light_crossbow, itm_lance, itm_lianjia_guokui, itm_warhorse],
   str_18 | agi_17 | int_10 | cha_9|level(30),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (270) | wp_archery (200) | wp_crossbow (270) | wp_throwing (200),
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_4|knows_trainer_2|knows_tracking_3|knows_tactics_2|knows_pathfinding_3|knows_spotting_3|knows_inventory_management_2|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_5|knows_study_3|knows_devout_3|knows_prisoner_management_2|knows_leadership_4|knows_trade_3,
   man_face_young_1, man_face_old_2],

#协会暗部
  ["association_shade","Association Shade","Association Shades", #协会暗部
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_wulaizhe_lianjia, itm_mail_boots, itm_scale_gauntlets, itm_jinshi_zhanbiao, itm_jinshi_zhanbiao, itm_jinshi_zhanbiao, itm_black_helmet, itm_bastard_sword_b],
   str_19 | agi_18 | int_15 | cha_8|level(30),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|knows_power_draw_2|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_4|knows_horse_archery_4|knows_looting_4|knows_trainer_2|knows_tracking_4|knows_tactics_2|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_3|knows_first_aid_3|knows_engineer_3|knows_persuasion_5|knows_array_arrangement_3|knows_memory_5|knows_study_3|knows_devout_3|knows_prisoner_management_3|knows_leadership_2|knows_trade_3,
   man_face_middle_1, man_face_old_2],
  ["association_guardian","Association Guardian","Association Guardians", #协会影卫
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_black_armor, itm_gauntlets, itm_black_greaves, itm_black_helmet, itm_heisebanlian_ma, itm_yellow_black_skoutarion, itm_maoxianzhe_dajian, itm_maoxianzhe_buqiangjian, itm_knight_recurve_bow],
   str_30 | agi_28 | int_18 | cha_8|level(45),wp_one_handed (450) | wp_two_handed (450) | wp_polearm (450) | wp_archery (450) | wp_crossbow (300) | wp_throwing (300),
   knows_ironflesh_9|knows_power_strike_8|knows_power_throw_5|knows_power_draw_6|knows_weapon_master_7|knows_shield_7|knows_athletics_7|knows_riding_6|knows_horse_archery_7|knows_looting_7|knows_trainer_3|knows_tracking_5|knows_tactics_4|knows_pathfinding_7|knows_spotting_7|knows_inventory_management_4|knows_wound_treatment_5|knows_surgery_4|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_7|knows_study_5|knows_devout_3|knows_prisoner_management_8|knows_leadership_6|knows_trade_4,
   man_face_middle_1, man_face_old_2],
  ["association_spy","Association Spy","Association Spys", #协会密探
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_leather_gloves, itm_jinshi_feidao, itm_jinshi_feidao, itm_jinshi_feidao, itm_heise_ma, itm_black_greaves, itm_black_armor, itm_black_helmet],
   str_24 | agi_26 | int_16 | cha_8|level(40),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_power_draw_4|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_looting_5|knows_trainer_3|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_7|knows_study_5|knows_devout_3|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   man_face_middle_1, man_face_old_2],

  ["association_examiner","Association Examiner","Association Examiners", #协会考官
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
   0,0,fac_adventurers_association,
   [itm_brigandine_red, itm_leather_gloves, itm_leather_boots, itm_longshoujian, itm_jinshi_feidao],
   str_24 | agi_22 | int_11 | cha_9|level(40),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_6|knows_shield_6|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_looting_5|knows_trainer_8|knows_tracking_4|knows_tactics_3|knows_pathfinding_4|knows_spotting_4|knows_inventory_management_3|knows_wound_treatment_4|knows_surgery_4|knows_first_aid_5|knows_engineer_4|knows_persuasion_6|knows_array_arrangement_4|knows_memory_7|knows_study_5|knows_devout_3|knows_prisoner_management_5|knows_leadership_6|knows_trade_4,
   man_face_old_1, man_face_older_2],



#############################################################拜星教##########################################################

  ["sabianist","Sabianist","Sabianists",tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_heresy_sabianism,
   [itm_silver_mane_steed, itm_mail_shirt, itm_mail_mittens, itm_mail_chausses, itm_sword_viking_2, itm_sword_viking_2_small],
   str_12 | agi_10 | int_15 | cha_14|level(15),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (160) | wp_crossbow (160) | wp_throwing (160),knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_weapon_master_3|knows_shield_3|knows_athletics_3|knows_riding_4|knows_horse_archery_5,woman_face_1, woman_face_2],
  ["sabianist_guardian_warrior","Sabianist Guardian Warrior","Sabianist Guardian Warriors",tf_pretty_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_heresy_sabianism,
   [itm_shenlan_lianjiazhaopao, itm_huali_banjiaxue, itm_huali_shalouhushou, itm_no_head, itm_yinyue_jian, itm_xinhua_qiqiang],
   str_23 | agi_18 | int_15 | cha_18|level(30),wp_one_handed (300) | wp_two_handed (300) | wp_polearm (300) | wp_archery (300) | wp_crossbow (300) | wp_throwing (300),knows_ironflesh_10|knows_power_strike_8|knows_power_throw_7|knows_power_draw_8|knows_weapon_master_6|knows_shield_6|knows_athletics_5|knows_riding_6|knows_horse_archery_6,woman_face_1, woman_face_2],
  ["starcourt_knight","Starcourt Knight","Starcourt Knights",tf_pretty_female|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_sabianism,
   [itm_xinyue_qiqiang, itm_meteorite_bow, itm_yinyue_jian, itm_stardust_light_plate_armor, itm_yinse_bikai, itm_silver_winged_great_sword, itm_xinyue_qiqiang, itm_unicorn, itm_huali_banjiaxue, itm_knight_white_cape],
   str_38 | agi_25 | int_23 | cha_30|level(50),wp_one_handed (500) | wp_two_handed (500) | wp_polearm (500) | wp_archery (500) | wp_crossbow (500) | wp_throwing (500),knows_ironflesh_13|knows_power_strike_12|knows_power_throw_8|knows_power_draw_10|knows_weapon_master_8|knows_shield_9|knows_athletics_9|knows_riding_8|knows_horse_archery_7,woman_face_1, woman_face_2],
  ["sabianist_diviner","Sabianist Diviner","Sabianist Diviners",tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_sabianism,
   [itm_xingting_lianjiazhaopao, itm_chunbaimiansha, itm_yinyue_jian, itm_meteorite_bow, itm_mail_mittens, itm_mail_chausses, itm_yinyue_jian, itm_silver_winged_great_sword],
   str_19 | agi_24 | int_20 | cha_20|level(30),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_3,woman_face_1, woman_face_2],
  ["sabianist_confessor","Sabianist Confessor","Sabianist Confessors",tf_pretty_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_heresy_sabianism,
   [itm_silver_winged_great_sword, itm_yinyue_jian, itm_yinyue_jian, itm_meteorite_bow, itm_shengnv_guan, itm_yinse_xue, itm_yinse_bikai, itm_stardust_light_plate_armor],
   str_23 | agi_30 | int_30 | cha_30|level(45),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_5|knows_shield_5|knows_athletics_7|knows_riding_5|knows_horse_archery_5,woman_face_1, woman_face_2],





#############################################################自生者##########################################################

##—————————————————————————————————龙孽————————————————————————————
##
  ["dragonmania","Dragonmania","Dragonmanias",#龙癫
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_slavers,
   [],
   str_24 | agi_24 | int_9 | cha_9|level(30),wp_one_handed (270) | wp_two_handed (270) | wp_polearm (270) | wp_archery (270) | wp_crossbow (270) | wp_throwing (270),
   knows_ironflesh_9|knows_power_strike_9|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_5|knows_shield_3|knows_athletics_7|knows_riding_4|knows_horse_archery_5|knows_looting_4|knows_tracking_4|knows_tactics_2|knows_pathfinding_4|knows_spotting_4|knows_persuasion_4|knows_memory_6|knows_study_10|knows_leadership_5, 
   powell_face_young_1, powell_face_young_2],

  ["dragonfrenzy","Dragonfrenzy","Dragonfrenzies",#龙狂
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_slavers,
   [],
   str_40 | agi_40 | int_9 | cha_9|level(40),wp_one_handed (460) | wp_two_handed (460) | wp_polearm (460) | wp_archery (460) | wp_crossbow (460) | wp_throwing (460),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_7|knows_shield_4|knows_athletics_11|knows_riding_5|knows_horse_archery_8|knows_looting_7|knows_tracking_6|knows_tactics_3|knows_pathfinding_6|knows_spotting_6|knows_persuasion_7|knows_memory_11|knows_study_12|knows_leadership_7, 
   powell_face_young_1, powell_face_young_2],

  ["dragon_abomination","Dragon Abomination","Dragon Abominations",#龙孽
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_slavers,
   [],
   str_40 | agi_40 | int_9 | cha_9|level(50),wp_one_handed (460) | wp_two_handed (460) | wp_polearm (460) | wp_archery (460) | wp_crossbow (460) | wp_throwing (460),
   knows_ironflesh_13|knows_power_strike_13|knows_power_throw_8|knows_power_draw_8|knows_weapon_master_7|knows_shield_4|knows_athletics_11|knows_riding_5|knows_horse_archery_8|knows_looting_7|knows_tracking_6|knows_tactics_3|knows_pathfinding_6|knows_spotting_6|knows_persuasion_7|knows_memory_11|knows_study_12|knows_leadership_7, 
   powell_face_young_1, powell_face_young_2],



##—————————————————————————————————绯世————————————————————————————
##
  ["crimson_residual","Crimson Residual","Crimson Residuals",#绯世残响
   tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,
   0,0,fac_monster,
  [itm_crimson_body, itm_crimson_foot, itm_crimson_hand, itm_blood_thorn],
   str_30 | agi_27 | int_3 | cha_3|level(35),wp_one_handed (350) | wp_two_handed (350) | wp_polearm (350) | wp_archery (350) | wp_crossbow (350) | wp_throwing (350),
   knows_ironflesh_10|knows_power_strike_7|knows_power_throw_4|knows_power_draw_4|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_2|knows_horse_archery_5, 
   crimson_face, crimson_face],
  ["blood_pool_phantom","Blood Pool Phantom","Blood Pool Phantoms",#血池幻形
   tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
   0,0,fac_monster,
  [itm_blood_pool_weaving_chain, itm_blood_shell, itm_crimson_thorn, itm_blood_veil, itm_crimson_flow_swiftstep, itm_crimson_hand],
   str_36 | agi_33 | int_3 | cha_3|level(40),wp_one_handed (400) | wp_two_handed (400) | wp_polearm (400) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400),
   knows_ironflesh_11|knows_power_strike_8|knows_power_throw_5|knows_power_draw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_7|knows_riding_4|knows_horse_archery_6, 
   crimson_face, crimson_face],
  ["blood_sea_raven","Blood Sea Raven","Blood Sea Ravens",#血海渡鸦
   tf_zombie|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
   0,0,fac_monster,
  [itm_blood_crow_robe, itm_blood_crow_claw, itm_hood_of_the_red_raven, itm_veinnet_agility, itm_crimson_hand, itm_veinshade_wing, itm_veinshade_wing, itm_red_thread_whisperer, itm_blood_crow_claw_shield],
   str_39 | agi_58 | int_3 | cha_5|level(45),wp_one_handed (450) | wp_two_handed (449) | wp_polearm (449) | wp_archery (449) | wp_crossbow (449) | wp_throwing (449),
   knows_ironflesh_11|knows_power_strike_8|knows_power_throw_5|knows_power_draw_9|knows_weapon_master_9|knows_shield_6|knows_athletics_15|knows_riding_7|knows_horse_archery_15, 
   crimson_face, crimson_face],
  ["red_dream_shadow","Red Dream Shadow","Red Dream Shadows",#赤梦幽影
   tf_zombie|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
   0,0,fac_monster,
  [itm_resonant_crimson_plate, itm_red_dream_heavy_crown, itm_sea_treading_blood_boot, itm_grip_of_crimson_flow, itm_blood_snatcher, itm_crimson_monster, itm_crimson_lunar_flowing_light],
   str_50 | agi_48 | int_3 | cha_3|level(55),wp_one_handed (549) | wp_two_handed (549) | wp_polearm (550) | wp_archery (549) | wp_crossbow (549) | wp_throwing (549),
   knows_ironflesh_13|knows_power_strike_10|knows_power_throw_9|knows_power_draw_7|knows_weapon_master_9|knows_shield_7|knows_athletics_11|knows_riding_8|knows_horse_archery_10, 
   crimson_face, crimson_face],
  ["blood_moon_birth_one","Blood Moon Birth One","Blood Moon Birth Ones",#血月降生者
   tf_zombie|tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,
   0,0,fac_monster,
  [itm_resonant_crimson_heavy_plate, itm_scarlet_flame_sword, itm_blood_tide_ironclad, itm_sea_treading_blood_boot, itm_grip_of_crimson_flow, itm_shadow_of_blood_invasion],
   str_70 | agi_67 | int_3 | cha_3|level(60),wp_one_handed (600) | wp_two_handed (600) | wp_polearm (600) | wp_archery (600) | wp_crossbow (600) | wp_throwing (600),
   knows_ironflesh_15|knows_power_strike_12|knows_power_throw_10|knows_power_draw_10|knows_weapon_master_12|knows_shield_9|knows_athletics_13|knows_riding_10|knows_horse_archery_12, 
   crimson_face, crimson_face],



##—————————————————————————————————谬史————————————————————————————
##
  ["restless_soldier","Restless Soldier","Restless Soldiers", #无法安息的士兵
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_monster,
   [itm_light_armor_of_soldiers, itm_the_absurd, itm_light_boot_of_soldiers, itm_glove_of_soldiers, itm_shengtieshuangshoujian, itm_war_darts],
   str_18| agi_16 | int_6 | cha_5|level(25), wp_one_handed (220) | wp_two_handed (220) | wp_polearm (200) | wp_archery (180) | wp_crossbow (180) | wp_throwing (180), 
   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_3|knows_weapon_master_4|knows_shield_3|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_looting_1|knows_trainer_2|knows_tracking_2|knows_tactics_3|knows_pathfinding_2|knows_spotting_2|knows_inventory_management_3|knows_wound_treatment_1|knows_surgery_2|knows_first_aid_1|knows_engineer_1|knows_persuasion_3|knows_array_arrangement_1|knows_memory_4|knows_study_2|knows_devout_2|knows_prisoner_management_1|knows_leadership_3|knows_trade_1, 
   powell_woman_face_1,powell_woman_face_2],
  ["restless_sergeant","Restless Sergeant","Restless Sergeants", #无法安息的军士
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 
   0,0,fac_monster,
  [itm_middle_armor_of_sergeants, itm_the_absurd, itm_middle_boot_of_sergeants, itm_gauntlet_of_sergeants, itm_lianren_fu, itm_purifier_eagle_tower_shield, itm_mogang_changzhuiqiang],
   str_25| agi_22 | int_7 | cha_6|level(35), wp_one_handed (320) | wp_two_handed (320) | wp_polearm (300) | wp_archery (260) | wp_crossbow (260) | wp_throwing (260), 
   knows_ironflesh_8|knows_power_strike_7|knows_power_throw_5|knows_power_draw_4|knows_weapon_master_5|knows_shield_5|knows_athletics_5|knows_riding_4|knows_horse_archery_5|knows_looting_5|knows_trainer_3|knows_tracking_5|knows_tactics_3|knows_pathfinding_5|knows_spotting_5|knows_inventory_management_4|knows_wound_treatment_3|knows_surgery_4|knows_first_aid_3|knows_engineer_2|knows_persuasion_4|knows_array_arrangement_2|knows_memory_7|knows_study_2|knows_devout_1|knows_prisoner_management_3|knows_leadership_5|knows_trade_3, 
   powell_woman_face_1,powell_woman_face_2],
  ["restless_knight","Restless Knight","Restless Knights", #无法安息的骑士
   tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield, 
   0,0,fac_monster,
   [itm_heavy_armor_of_knights, itm_the_absurd, itm_heavy_boot_of_knights, itm_gauntlet_of_knights, itm_red_yellow_lion_fan_shaped_shield, itm_yishith_knight_sword, itm_jiaoguo_hei_qizhiqiang, itm_fantom_nightmare],
   str_33| agi_30 | int_8 | cha_7|level(48), wp_one_handed (450) | wp_two_handed (450) | wp_polearm (430) | wp_archery (400) | wp_crossbow (400) | wp_throwing (400), 
   knows_ironflesh_10|knows_power_strike_9|knows_power_throw_7|knows_power_draw_6|knows_weapon_master_8|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_6|knows_looting_6|knows_trainer_6|knows_tracking_6|knows_tactics_5|knows_pathfinding_6|knows_spotting_6|knows_inventory_management_5|knows_wound_treatment_5|knows_surgery_6|knows_first_aid_5|knows_engineer_4|knows_persuasion_7|knows_array_arrangement_4|knows_memory_10|knows_study_5|knows_devout_4|knows_prisoner_management_5|knows_leadership_6|knows_trade_4, 
   powell_woman_face_1,powell_woman_face_2],





###########################################################################################################################

  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
[itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_beast_skin_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_beast_skin_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_fur_covered_shield,itm_beast_skin_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c, itm_crossbow,itm_plate_armor,itm_coat_of_plates,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_courser,itm_leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],




#街上的行人（位置不能动）
#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2, 0, 
   0, 0, itm_function_non_military_personnel, #非战斗人员
  ],
# Ryan END
#This troop is the troop marked as spy_walkers_end
 ["walker_end","{!}Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

]+troops_npc + troops_multiplayer + troops_mission



#Troop upgrade declarations

upgrade(troops,"watchman","hunter")
upgrade(troops,"hunter","mercenary_archer")
upgrade(troops,"mercenary_archer","mercenary_skirmisher")

##__________________________________________________________________________普威尔联合王国____________________________________________________________________________
upgrade2(troops,"powell_peasant","powell_militia","powell_huntsman")
upgrade2(troops,"powell_militia","powell_footman","powell_horseman")
upgrade(troops,"powell_footman","powell_conjuring_infantry")
upgrade(troops,"powell_huntsman","powell_skirmisher")
upgrade(troops,"powell_horseman","powell_conjuring_rider")
upgrade2(troops,"powell_conjuring_rider","powell_windscorching_lancer","powell_rockglacier_ranger")

upgrade(troops,"powell_nobility","powell_noble_trainee")
upgrade2(troops,"powell_noble_trainee","powell_noble_knight", "powell_armored_conjurer")

#普威尔中央
upgrade(troops,"powell_kingcity_citizen","powell_armed_footman")
upgrade2(troops,"powell_armed_footman","powell_strike_swordman", "powell_heavy_infantry")
upgrade2(troops,"powell_strike_swordman","powell_great_swordman", "powell_sword_cavalry")
upgrade2(troops,"powell_heavy_infantry","powell_halberd_infantry", "powell_halberd_cavalry")

upgrade(troops,"powell_court_nobility","powell_bodyguard")
upgrade2(troops,"powell_bodyguard","powell_court_knight", "powell_praetorian")

upgrade(troops,"king_spy","national_knight")

upgrade(troops,"tocsin_attendant","tocsin_knight")
upgrade(troops,"tocsin_knight","tocsin_assassin")

upgrade2(troops,"powell_headsman","eliminater_recruit", "powell_executioner")
upgrade2(troops,"eliminater_recruit", "eliminater_sergeant","eliminater_vanguard")
upgrade2(troops,"eliminater_vanguard","eliminater_knight", "purification_sickle")


#罗德里格斯公国
upgrade(troops,"red_dolphin_attendant","red_dolphin_worrier")
upgrade(troops,"red_dolphin_worrier","red_dolphin_knight")
upgrade(troops,"red_dolphin_knight","red_dolphin_banneret")

upgrade(troops,"lesaff_armed_sailor","lesaff_shipboard_infantry")
upgrade2(troops,"lesaff_shipboard_infantry","lesaff_axe_warrior","lesaff_iron_axe_sergeant")

upgrade(troops,"trade-wind_gulf_guard","holding_guard")

upgrade(troops,"grenier_militia","grenier_wellselected_militia")
upgrade2(troops,"grenier_wellselected_militia", "grenier_rider", "grenier_longbow_archer")

upgrade2(troops,"bloodfire_mercenary_corps_veteran","bloodfire_vanguard","bloodfire_berserker_warrior")

upgrade(troops,"garcia_bodyguard","faceless_cavalry")


#北境开拓领
upgrade2(troops,"northern_militia","northern_infantry","northern_crossbowman")
upgrade2(troops,"northern_infantry","northern_tower_shield_sergeant","northern_cavalry")
upgrade(troops,"northern_crossbowman","northern_heavy_crossbow_shooter")

upgrade(troops,"northern_serf","northern_serf_infantry")
upgrade(troops,"northern_serf_infantry","northern_serf_rider")
upgrade(troops,"northern_serf_rider","northern_ministeriales")

upgrade(troops,"northern_hunter","dragon_scout")
upgrade(troops,"dragon_scout","powell_dragon_archer")

upgrade(troops,"revenge_iron_hoof","hometownless_knight")

upgrade(troops,"brand_dragonmania","brand_dragonfrenzy")
upgrade(troops,"brand_dragonfrenzy","brand_dragon_abomination")


#普属自由城邦
upgrade(troops,"preist_porter","preist_infantry")
upgrade(troops,"preist_infantry","preist_horseback_crossbow_sergeant")

upgrade(troops,"preist_noble_crossbowman","preist_noble_cavalry")

upgrade2(troops,"powell_novice_divineguider","powell_conscripted_therapist","powell_military_divineguider")
upgrade(troops,"powell_military_divineguider","powell_armour_divineguider")

upgrade(troops,"powell_orthodox_believer","powell_parishioner_warrier")
upgrade(troops,"powell_parishioner_warrier","powell_orthodox_zealot")


#南沙公国
upgrade(troops,"powell_rogue_farmer","sousanth_militia")
upgrade2(troops,"sousanth_militia","sousanth_guard","sousanth_rider")
upgrade2(troops,"sousanth_guard","sousanth_elite_bowman", "sousanth_darts_sergeant")

upgrade(troops,"powell_rogue_attendant","powell_rogue_knight")
upgrade(troops,"rodriguez_rogue_attendant","rodriguez_rogue_knight")
upgrade(troops,"city_rogue_attendant","city_rogue_knight")

upgrade(troops,"araiharsa_mercenary_infantry","araiharsa_mercenary_rider")

#龙神教
upgrade(troops,"dragon_power_worshipper","dragon_god_follower")
upgrade2(troops,"dragon_god_follower","dragon_blood_swordsman","dragonword_practitioner")
upgrade2(troops,"dragon_blood_swordsman","dragon_power_great_swordman", "dragonwings_knight")
upgrade(troops,"dragonword_practitioner","dragonword_great_presbyter")

upgrade(troops,"sedative_pavilion_nurse","sedative_pavilion_maid")
upgrade(troops,"sedative_pavilion_maid","sedative_pavilion_physician")
upgrade(troops,"sedative_pavilion_physician","tranquility_chief_physician")


##______________________________________________________________________________伊希斯公国________________________________________________________________________________
upgrade(troops,"yishith_inferior_elf","yishith_elf_hunter")
upgrade(troops,"yishith_elf_hunter","yishith_elf_skirmisher")
upgrade(troops,"yishith_elf_skirmisher","yishith_elf_woodguard")
upgrade2(troops,"yishith_elf_woodguard","yishith_jungleslaughterer", "yishith_elf_outrider")

upgrade(troops,"yishith_human_resident","yishith_human_militia")
upgrade(troops,"yishith_human_militia","yishith_human_infantry")
upgrade2(troops,"yishith_human_infantry","yishith_human_cavalry","yishith_human_heavyinfantry")
upgrade(troops,"yishith_human_heavyinfantry","yishith_human_guard")

#灵魄之树
upgrade(troops,"soul_full_elf","yishith_equerry")
upgrade(troops,"yishith_equerry","yishith_spiritual_horse_knight")

upgrade(troops,"seddlined_thrall","seddlined_puppet")
upgrade2(troops,"seddlined_puppet","seddlined_desperater", "seddlined_crazy_cavalry")
upgrade(troops,"seddlined_desperater","seddlined_dare_to_die_corp")
upgrade(troops,"seddlined_crazy_cavalry","seddlined_apostle")

#死亡之树
upgrade(troops,"demise_full_elf","hotbed_gatekeeper")
upgrade(troops,"hotbed_gatekeeper","hotbed_farmer")
upgrade(troops,"hotbed_farmer","demise_gardener")

upgrade(troops,"the_composted","living_root")
upgrade(troops,"living_root","root_borning_one")
upgrade2(troops,"root_borning_one","humic_walker", "humic_vanguard")
upgrade(troops,"humic_walker","hotbed_hollow")
upgrade(troops,"humic_vanguard","humus_lord")

#先祖之树
upgrade(troops,"ancester_full_elf","yishith_elf_sergeant")
upgrade2(troops, "yishith_elf_sergeant", "yishith_elf_heavy_cavalry", "yishith_heavy_ranger")

upgrade2(troops,"half_molter","yishith_swordman", "yishith_crossbowman")
upgrade(troops, "yishith_swordman", "yishith_sword_armedman")
upgrade2(troops,"yishith_sword_armedman","yishith_sword_dancer","molter_knight")
upgrade(troops, "yishith_crossbowman", "yishith_crossbow_ranger")

#生命之树
upgrade(troops,"vita_full_elf","yishith_navy_archer")
upgrade(troops,"yishith_navy_archer","yishith_seawind_ranger")

upgrade(troops,"yishith_armed_sailor","yishith_boat_guard")
upgrade(troops,"yishith_boat_guard","vita_shield_axe_guardian")
upgrade2(troops,"yishith_recruiting_rider","yishith_sentry_cavalry", "yishith_throwing_axe_ranger")


##______________________________________________________________________________科鲁托酋长国________________________________________________________________________________
upgrade(troops,"kouruto_stray_therianthropy","kouruto_therianthropy_mercenary")
upgrade(troops,"kouruto_therianthropy_mercenary","kouruto_therianthropy_riding_mercenary")
upgrade(troops,"kouruto_therianthropy_riding_mercenary","kouruto_therianthropy_mercenary_captain")

#图腾同盟
#虎族
upgrade2(troops,"kouruto_tiger_herdsman","kouruto_tiger_rider","kouruto_tiger_saber")
upgrade(troops,"kouruto_tiger_rider","kouruto_tiger_machete_rider")
upgrade(troops,"kouruto_tiger_machete_rider","kouruto_rampant_slaughterer")
upgrade(troops,"kouruto_tiger_saber","kouruto_tiger_berserk_saber")
upgrade(troops,"kouruto_tiger_berserk_saber","kouruto_sword_master")

#熊族
upgrade2(troops,"kouruto_bear_herdsman","kouruto_bear_rider","kouruto_bear_shieldman")
upgrade(troops,"kouruto_bear_rider","kouruto_bear_heavy_cavalry")
upgrade(troops,"kouruto_bear_heavy_cavalry","kouruto_ragefist_obliterator")
upgrade(troops,"kouruto_bear_shieldman","kouruto_bear_tower_shieldman")
upgrade(troops,"kouruto_bear_tower_shieldman","kouruto_earthshaker_guardian")

#狼族
upgrade2(troops,"kouruto_wolf_herdsman","kouruto_wolf_rider","kouruto_wolf_scout")
upgrade(troops,"kouruto_wolf_rider","kouruto_wolf_lancer")
upgrade(troops,"kouruto_wolf_lancer","kouruto_bloodclaw_ravager")
upgrade(troops,"kouruto_wolf_scout","kouruto_wolf_ranger")
upgrade(troops,"kouruto_wolf_ranger","kouruto_cyclone_marauder")

#狮族
upgrade(troops,"kouruto_lion_therianthropy","kouruto_lion_warrior")
upgrade(troops,"kouruto_lion_warrior","kouruto_lion_baatur")
upgrade(troops,"kouruto_lion_baatur","kouruto_kheshig")

#科鲁托剑斗旅团
upgrade(troops,"kouruto_gladiator","kouruto_sword_fighter")
#铁峰守备旅团
upgrade(troops,"ironbite_gang_freshman","ironbite_gang_veteran")
upgrade(troops,"ironbite_gang_veteran","metal_devourer_master")
#啮铁帮
upgrade(troops,"furnace_watch_recruit","furnace_watch_warrior")
upgrade(troops,"furnace_watch_warrior","furnace_watch_stalker")

#麦汗族
#牛族
upgrade(troops,"kouruto_cow_herdsman","kouruto_cow_axeman")
upgrade(troops,"kouruto_cow_axeman","kouruto_cow_warrior")
upgrade2(troops,"kouruto_cow_warrior","kouruto_ironhorn_ravager","kouruto_bloodhoof_axe_reaver")

#羊族
upgrade(troops,"kouruto_sheep_herdsman","kouruto_sheep_light_infantry")
upgrade(troops,"kouruto_sheep_light_infantry","kouruto_sheep_skirmisher")
upgrade(troops,"kouruto_sheep_skirmisher","kouruto_stonecliff_guardian")

#鹿族
upgrade(troops,"kouruto_deer_herdsman","kouruto_deer_swordman")
upgrade(troops,"kouruto_deer_swordman","kouruto_deer_sword_warrior")
upgrade(troops,"kouruto_deer_sword_warrior","kouruto_swiftstrike_marirm")

#兔族
upgrade(troops,"kouruto_rabbit_herdsman","kouruto_rabbit_stone_thrower")
upgrade(troops,"kouruto_rabbit_stone_thrower","kouruto_rabbit_slingshoter")
upgrade(troops,"kouruto_rabbit_slingshoter","kouruto_ambulancer")

#炉边萨满联盟
upgrade(troops,"kouruto_novice_shaman","kouruto_veteran_shaman")
upgrade(troops,"kouruto_veteran_shaman","kouruto_ritualist")
upgrade(troops,"kouruto_ritualist","kouruto_furnace_great_ritualist")

#金爪子帮
#狐族
upgrade(troops,"kouruto_fox_herdsman","kouruto_fox_horseman")
upgrade(troops,"kouruto_fox_horseman","kouruto_fox_blade_rdier")
upgrade(troops,"kouruto_fox_blade_rdier","midul_knight")

#猫族
upgrade(troops,"kouruto_cat_herdsman","kouruto_cat_hitman")
upgrade(troops,"kouruto_cat_hitman","kouruto_cat_killer")
upgrade(troops,"kouruto_cat_killer","midul_assassin")

#守望派
#犬族
upgrade(troops,"kouruto_dog_herdsman","kouruto_dog_recuit")
upgrade2(troops,"kouruto_dog_recuit","kouruto_tercio_infantry", "kouruto_tercio_spearman")
upgrade(troops,"kouruto_tercio_infantry","kouruto_tercio_centurion")

#科鲁托辅助军
upgrade(troops,"kouruto_human_settler","kouruto_young_mercenary")
upgrade2(troops,"kouruto_young_mercenary","kouruto_auxiliary_light_infantry","kouruto_auxiliary_spearman")
upgrade2(troops,"kouruto_auxiliary_light_infantry","kouruto_auxiliary_rider","kouruto_auxiliary_longbowman")
upgrade2(troops,"kouruto_auxiliary_rider","kouruto_auxiliary_ranger","kouruto_auxiliary_heavy_rider")

##__________________________________________________________________________乌-迪默-安基亚邦联________________________________________________________________________________

upgrade(troops,"confederation_serf","confederation_recruits_slave")
upgrade2(troops,"confederation_recruits_slave","confederation_slave_footman","confederation_slave_perdue")

upgrade(troops,"confederation_serf_warrior","confederation_serf_gladiator")
upgrade2(troops,"confederation_serf_gladiator","meat_puppet","confederation_gladiator_champion")

#黑沼议事会
upgrade2(troops,"diemer_freeman","diemer_heavy_footman","diemer_light_footman")
upgrade2(troops,"diemer_heavy_footman","diemer_warrior","diemer_noviciate_cavalory")
upgrade(troops,"diemer_warrior","diemer_swordman")
upgrade(troops,"diemer_swordman","marsh_council_guard")
upgrade(troops,"diemer_noviciate_cavalory","diemer_hetairoi")

upgrade2(troops,"diemer_light_footman","diemer_grenadier","diemer_shortbow_archer")
upgrade2(troops,"diemer_grenadier","diemer_guardian","diemer_light_cavalry")
upgrade(troops,"diemer_shortbow_archer","diemer_heaveybow_marksman")

upgrade(troops,"diemer_young_slaveholder","diemer_knight_retinue")
upgrade(troops,"diemer_knight_retinue","diemer_monster_enslaving_knight")

upgrade(troops,"confederation_slave_trainer","confederation_slave_dominator")
upgrade(troops,"confederation_slave_dominator","confederation_enslavement_warlock")

upgrade(troops,"restless_soldier","restless_sergeant")
upgrade(troops,"restless_sergeant","restless_knight")

upgrade(troops,"confederation_new_recruit","confederation_hiring_infantry")
upgrade(troops,"confederation_hiring_infantry","confederation_hiring_spearman")
upgrade2(troops,"confederation_hiring_spearman","marsh_flower_dopplesoldner","marsh_flower_feldweibel")
upgrade(troops,"marsh_flower_feldweibel","marsh_flower_generalobrist")
upgrade(troops,"confederation_hiring_conjurer","marsh_flower_elemental_conjurer")
upgrade(troops,"marsh_flower_camp_woman","marsh_flower_hurenweibel")

#乌尔之子女
upgrade(troops,"confederation_fishing_serf","confederation_deepone_slave")
upgrade(troops,"confederation_deepone_slave","confederation_swamp_bandit")
upgrade(troops,"confederation_swamp_bandit","confederation_ship_looter")

upgrade(troops,"marsh_deepone_freeman","marsh_deepone_self_trained_militia")
upgrade2(troops,"marsh_deepone_self_trained_militia","marsh_deepone_professional_soldier", "marsh_hunter")
upgrade(troops,"marsh_deepone_professional_soldier","marsh_deepone_warrior")
upgrade2(troops,"marsh_deepone_warrior","marsh_deepone_commander", "dreadmarsh_warrior")
upgrade(troops,"marsh_hunter","marsh_venomfin_hunter")

#净世军
upgrade(troops,"confederation_armed_faithful","purifier_recruit")
upgrade(troops,"purifier_recruit","purifier_light_soldier")
upgrade(troops,"purifier_light_soldier","purifier_infantry")
upgrade2(troops,"purifier_infantry","purifier_dismounted_knight","purifier_ballistaman")

upgrade(troops,"purifier_pastor","purifier_combat_pastor")
upgrade2(troops,"purifier_combat_pastor","holy_wing_guard","storm_white_shadow")
upgrade(troops,"holy_wing_guard","storm_follower")

upgrade(troops,"suffering_friar","agony_priest")
upgrade(troops,"agony_priest","swaybacked_monk")

#食莲人沙龙
upgrade(troops,"ankiya_civilized_barbarian","ankiya_recruit")
upgrade(troops,"ankiya_recruit","ankiya_mercenary")
upgrade(troops,"ankiya_mercenary","ankiya_horseback_mercenary")

upgrade(troops,"ankiya_naturalized_noble","ankiya_rider")
upgrade(troops,"ankiya_rider","ankiya_knight")

#人类狩猎者
upgrade(troops,"confederation_slave_catcher_hitman","confederation_slave_catcher_infantry")
upgrade(troops,"confederation_slave_catcher_infantry","confederation_slave_catcher_rider")
upgrade(troops,"confederation_slave_catcher_rider","confederation_human_hunting_cavalry")

##_______________________________________________________________________________教皇国________________________________________________________________________________

upgrade2(troops,"papal_citizen","papal_recruit_militia", "papal_joint_defense_militia")
upgrade(troops,"papal_recruit_militia","papal_recruit_spearman")
upgrade(troops,"papal_recruit_spearman","papal_senior_spearman")
upgrade(troops,"papal_joint_defense_militia","holy_city_standing_infantry")
upgrade(troops,"holy_city_standing_infantry", "holy_land_swordsman")
upgrade2(troops,"holy_land_swordsman","church_guard", "faith_cavalry")

upgrade(troops,"church_fresh_trainee","church_senior_trainee")
upgrade2(troops,"church_senior_trainee","divine_legion_infantry","divine_legion_rider")
upgrade(troops,"divine_legion_rider","divine_legion_sergeant")

upgrade(troops,"mission_school_student","church_apprentice_preist")
upgrade2(troops,"church_apprentice_preist","divine_legion_military_chaplain","divine_legion_crossbowman")
upgrade(troops,"divine_legion_military_chaplain","divine_legion_combat_pastor")

upgrade(troops,"papal_hunter","papal_standing_archer")
upgrade(troops,"papal_standing_archer","divine_legion_armed_archer")

upgrade(troops,"papal_devout_noble","divine_legion_trained_recruit")
upgrade2(troops,"divine_legion_trained_recruit","divine_legion_sergeant","divine_legion_combat_pastor")

#圣廷
upgrade(troops,"godward_swordman","godward_great_swordman")
upgrade2(troops,"eternal_rest_warden","coffin_warden","coffin_monitor")

upgrade(troops,"holy_city_sentry","papal_elite_archer")

#证信宗
upgrade(troops,"civilian_exorcist","exorcist_mercenary")
upgrade(troops,"exorcist_mercenary","employed_demon_slayer")

upgrade(troops,"trial_servant","doctrinal_sitting_magistrate")

upgrade(troops,"accused_believer","sin_slave_soldier")
upgrade(troops,"sin_slave_soldier","sin_slave_infantry")

upgrade(troops,"devouring_sin_friar","devouring_sin_crazy_monk")
upgrade(troops,"devouring_sin_crazy_monk","accumulated_sin_knight")

#真信施洗会
upgrade(troops,"powell_baptized_infantry","powell_baptized_rider")
upgrade(troops,"powell_baptized_rider","powell_baptized_knight")

upgrade(troops,"yishith_baptized_half_elf","yishith_baptized_archer")
upgrade(troops,"yishith_baptized_archer","yishith_baptized_ranger")

upgrade(troops,"chaney_rider","chaney_heavy_cavalry")

upgrade(troops,"divine_legion_insane_infantry","divine_legion_insane_knight")

#神哲修道宗
upgrade(troops,"armed_female_believer","martial_sister")
upgrade(troops,"martial_sister","papal_female_guard")
upgrade(troops,"papal_female_guard","papal_swordwoman")

upgrade(troops,"whitspring_chaplain","arcane_minister")

upgrade(troops,"philosophical_egg_scholar","philosophical_egg_minister")
upgrade(troops,"philosophical_egg_minister","gnosis_explorer")
upgrade(troops,"gnosis_explorer","key_knight")

#圣别渴求者
upgrade(troops,"armed_pilgrim","armed_archaeological_team")
upgrade2(troops,"armed_archaeological_team","holy_smuggler","sacred_object_thief")
upgrade(troops,"holy_smuggler","holy_bandit_cavalry")
upgrade(troops,"sacred_object_thief","saintly_thief_ranger")

upgrade(troops,"holy_box_collector","holy_blood_desirer")
upgrade(troops,"holy_blood_desirer","holy_meat_epicure")

##_______________________________________________________________________________龙树________________________________________________________________________________

upgrade2(troops,"longshu_zhengzu","longshu_tuanlianbing","longshu_bubazi")
upgrade2(troops,"longshu_tuanlianbing","longshu_xiaoqi","longshu_jiji")
upgrade2(troops,"longshu_xiaoqi","longshu_lance_guaizima","longshu_mace_rider")
upgrade(troops,"longshu_lance_guaizima","longshu_longxiangjun")
upgrade(troops,"longshu_mace_rider","longshu_shenwujun")
upgrade2(troops,"longshu_jiji","longshu_eagle_ruishi","longshu_spear_ruishi")
upgrade(troops,"longshu_eagle_ruishi","longshu_cangtoujun")
upgrade(troops,"longshu_spear_ruishi","longshu_baiganjun")
upgrade2(troops,"longshu_bubazi","longshu_bow_guaizima","longshu_shediaoshou")
upgrade(troops,"longshu_bow_guaizima","longshu_tielinjun")
upgrade2(troops,"longshu_shediaoshou","longshu_accurate_jicha","longshu_power_jicha")
upgrade(troops,"longshu_accurate_jicha","longshu_yulinjun")
upgrade(troops,"longshu_power_jicha","longshu_yulinjun")

upgrade(troops,"longshu_eunuch","longshu_eunuch_inspector")
upgrade2(troops,"longshu_eunuch_inspector","longshu_jiuyijun","longshu_cangyijun")

##_______________________________________________________________________________大公国________________________________________________________________________________

upgrade2(troops,"starkhook_recruit","starkhook_mercenary","starkhook_armed_sailor")
upgrade2(troops,"starkhook_mercenary","starkhook_armoured_swordman","starkhook_enhanced_mercenary")
upgrade2(troops,"starkhook_armoured_swordman","starkhook_armoured_horseman","starkhook_armoured_crossbowman")
upgrade(troops,"starkhook_enhanced_mercenary","starkhook_condottiere")
upgrade2(troops,"starkhook_armed_sailor","starkhook_onboard_infantry","starkhook_enhanced_warrior")
upgrade2(troops,"starkhook_onboard_infantry","starkhook_axe_thrower","starkhook_boat_fighter")
upgrade(troops,"starkhook_enhanced_warrior","starkhook_berserker_warrior")
upgrade(troops,"starkhook_berserker_warrior","starkhook_megalith_berserker")

#白塔党
upgrade2(troops,"starkhook_tower_noble","starkhook_enhanced_swordman","starkhook_enhanced_halberdman")
upgrade(troops,"starkhook_enhanced_swordman","starkhook_bloody_berserker")
upgrade(troops,"starkhook_enhanced_halberdman","starkhook_mangler_berserker")

upgrade(troops,"blood_lake_sentry","blood_lake_patrol_cavalry")
upgrade(troops,"crimson_berserker","red_apostle")

upgrade(troops,"bloodburst_servant","bloodburst_slave")
upgrade(troops,"blood_extinguisher","blood_hunter")

#斯塔胡克商业联合
upgrade(troops,"starkhook_commercial_nobility","starkhook_attendant_cavalry")
upgrade2(troops,"starkhook_attendant_cavalry","starkhook_knight", "starkhook_blood_arrow_shooter")

upgrade(troops,"blood_can_slave","armed_blood_slave")
upgrade(troops,"armed_blood_slave","blood_servant_guard")
upgrade(troops,"blood_servant_guard","starkhook_companion_infantry")

upgrade(troops,"starkhook_business_association_rider","starkhook_business_association_leader")

##_______________________________________________________________________________自由城邦________________________________________________________________________________

upgrade(troops,"citizen_pauper","citizen_militia")
upgrade(troops,"citizen_militia","citizen_defend_militia")
upgrade2(troops,"citizen_defend_militia","citizen_patrol", "citizen_light_infantry")
upgrade(troops,"citizen_patrol","manhunter")
upgrade(troops,"citizen_light_infantry","citizen_spearman")

upgrade2(troops,"states_civilian","states_rider", "states_skirmisher")
upgrade(troops,"states_rider","states_light_cavalry")
upgrade2(troops,"states_light_cavalry","states_heavy_cavalry", "states_crossbow_cavalry")
upgrade(troops,"states_skirmisher","states_crossbow_ranger")
upgrade(troops,"states_crossbow_ranger","states_heavy_armored_crossbowman")
upgrade(troops,"states_heavy_armored_crossbowman","states_fortress_crossbowman")

upgrade(troops,"states_nobility","states_nobility_crossbowman")
upgrade(troops,"states_nobility_crossbowman","states_fortress_ballistaman")

upgrade(troops,"exorcism_novice","exorcism_hunter")
upgrade(troops,"exorcism_hunter","exorcism_archer")
upgrade(troops,"exorcism_archer","judgment_ranger")
upgrade(troops,"judgment_ranger","judgment_pursuer")


#outlaws#
upgrade2(troops,"looter","bandit", "mountain_bandit")
upgrade2(troops,"bandit","brigand", "blackguard_mercenary")
upgrade(troops,"brigand","bandit_leader")
upgrade(troops,"blackguard_mercenary","blackguard_sergeant")
upgrade(troops,"mountain_bandit","forest_bandit")

upgrade(troops,"steppe_bandit","kouruto_refugee_thief")
upgrade2(troops,"kouruto_refugee_thief","kouruto_refugee_looter", "kouruto_refugee_mercenary")
upgrade2(troops,"kouruto_refugee_looter","kouruto_refugee_warrior", "black_khergit_horseman")

upgrade(troops,"roving_bandits", "outlaw_swordman")
upgrade2(troops,"outlaw_swordman","outlaw_infantry", "outlaw_bowman")
upgrade(troops,"outlaw_infantry","outlaw_horseman")
upgrade(troops,"outlaw_horseman","outlaw_knight")

##_______________________________________________________________________________权厄之秤________________________________________________________________________________

upgrade2(troops,"thug","libra_hitman", "libra_guard")
upgrade2(troops,"libra_hitman","libra_spy", "alley_hunter")
upgrade(troops,"libra_guard","libra_bodyguard_rider")

upgrade2(troops,"libra_smuggler","libra_drug_dealer","libra_slave_merchant")
upgrade(troops,"libra_drug_dealer","libra_drug_muscleman")
upgrade(troops,"libra_drug_muscleman", "libra_drug_lord")
upgrade(troops,"libra_slave_merchant","libra_slave_catching_cavalry")
upgrade(troops,"libra_slave_catching_cavalry", "libra_slave_trade_leader")

upgrade(troops,"splitting_sailor", "splitting_swordman")


upgrade2(troops,"primary_killer","professional_assassin", "armor_breaker")
upgrade(troops,"professional_assassin","knell_assassin")
upgrade(troops,"armor_breaker","war_assassin")
upgrade2(troops,"female_killer","professional_female_assassin", "eavesdropper")
upgrade(troops,"professional_female_assassin","death_dancer")
upgrade(troops,"eavesdropper","eight_sword_dancer")

upgrade(troops,"taiga_bandit","ankiya_barbarian")
upgrade2(troops,"ankiya_barbarian","ankiya_warrior", "ankiya_shaman")
upgrade2(troops,"ankiya_warrior","ankiya_leader", "ankiya_looter_leader")

upgrade(troops,"desert_bandit","desert_thief")
upgrade(troops,"desert_thief","desert_leader")

upgrade2(troops,"abyssal_sailor","abyssal_axeman","abyssal_axe_thrower")
upgrade2(troops,"abyssal_axeman","abyssal_priate_warrior","abyssal_horseman")
upgrade(troops,"abyssal_priate_warrior","abyssal_surge_prowessman")
upgrade(troops,"abyssal_horseman","abyssal_plunder_captain")

upgrade2(troops,"witchcraft_trainee","damnation_warrior","witchcraft_druid")
upgrade(troops,"damnation_warrior","poisonous_knight")
upgrade(troops,"witchcraft_druid","witchcraft_warlock")


##________________________________________________________________________________魔物__________________________________________________________________________________
upgrade(troops,"the_forsaken","cult_follower")
upgrade2(troops,"cult_follower","fallen_warrior","fallen_apprentice")
upgrade(troops,"fallen_warrior","degradation_rider")
upgrade(troops,"degradation_rider","dark_oath_knight")
upgrade(troops,"fallen_apprentice","desecrate_priest")
upgrade(troops,"desecrate_priest","cauter_cardinal")

upgrade(troops,"demon_corruptor","new_birth_lemure")
upgrade(troops,"new_birth_lemure","lemure")
upgrade(troops,"lemure","crazy_lemure")


##________________________________________________________________________________不死者__________________________________________________________________________________
upgrade(troops,"junto_member","junto_student")
upgrade2(troops,"junto_student","necromancer","necro_knight")
upgrade(troops,"necromancer","half_dead")
upgrade(troops,"necro_knight","half_dead")

#zombie
upgrade2(troops,"low_grade_zombie","zombie_footman","zombie_archer")
upgrade2(troops,"zombie_footman","zombie_swordman","zombie_lancer")
upgrade(troops,"zombie_swordman","death_knight")
upgrade(troops,"zombie_archer","zombie_destroyer")

upgrade(troops,"zombie_king_warrior","zombie_king_guard")
upgrade(troops,"zombie_king_guard","zombie_king_praetorian")
upgrade2(troops,"resurgam_knight", "posthumous_knight", "resurgam_knight_chief")

upgrade2(troops,"zombie_armed_infantry","zombie_heavy_armed_soldier","zombie_heavy_shield_soldier")
upgrade(troops,"zombie_heavy_armed_soldier","zombie_dismounted_knight")
upgrade(troops,"zombie_dismounted_knight","immortal_blade")
upgrade(troops,"zombie_heavy_shield_soldier","zombie_shield_spear_knight")
upgrade(troops,"zombie_shield_spear_knight","impurity_shield")

upgrade(troops,"therianthropy_zombie","zombie_hammer_soldier")
upgrade2(troops,"zombie_hammer_soldier","zombie_hammer_cavalry","zombie_hammerer")
upgrade(troops,"zombie_hammerer","zombie_demolisher")

#skeleton
upgrade2(troops,"rebirth_skeleton","skeleton_warrior","skeleton_archer")
upgrade2(troops,"skeleton_warrior","skeleton_swordman","skeleton_rider")
upgrade(troops,"skeleton_swordman","experienced_skeleton")
upgrade(troops,"skeleton_rider","skeleton_knight")
upgrade(troops,"skeleton_archer","skeleton_heavy_archer")
upgrade(troops,"skeleton_heavy_archer","skeleton_ranger")

upgrade(troops,"deathdam_extraditer","deathdam_archon")
upgrade(troops,"skull_collector","skeleton_executioner")
upgrade(troops,"skeleton_executioner","skeleton_beheader")

upgrade(troops,"fragmented_dragonbone_guardian","debris_dragonbone_warrior")
upgrade(troops,"debris_dragonbone_warrior","relic_dragonbone_swordsmaster")
upgrade(troops,"relic_dragonbone_swordsmaster","dragonbone_knight")
upgrade(troops,"dragonbone_knight","dragonbone_overlord")
upgrade2(troops,"dragonfang_lancer","dragonfang_foehn_lancer","dragonfang_frostgravel_ranger")

upgrade(troops,"unburned_bones","candle_of_bone")
upgrade(troops,"candle_of_bone","blazing_thing_imitation")
upgrade(troops,"blazing_thing_imitation","eternalflame_unburned_one")

upgrade(troops,"curse_carrier","curse_exploder")
upgrade(troops,"elf_skeleton","resentment_archer")
upgrade(troops,"resentment_archer","frostcurse_cavalier")

#walker
upgrade(troops,"new_walker","walker_warrior")
upgrade(troops,"walker_warrior","walker_swordman")
upgrade2(troops,"walker_swordman","walker_soldier","walker_centurion")
upgrade(troops,"walker_soldier","turbid_cavalry")
upgrade(troops,"walker_centurion","walker_chieftain")

#ghost
upgrade(troops,"poltergeist","grudge_ghost")
upgrade2(troops,"grudge_ghost","ghost_soldier", "shadow_runner")
upgrade(troops,"ghost_soldier","shadow_reaper")
upgrade2(troops,"phantom_rider","shatter_knight", "deadlight_cavalry")
upgrade(troops,"qingqiu_nagzul","qingqiu_warrior")
upgrade(troops,"qingqiu_warrior","soul_summoning_envoy")


##_____________________________________________________________________________冒险者协会________________________________________________________________________________
upgrade(troops,"blackiron_adventurer","barecopper_adventurer")
upgrade(troops,"barecopper_adventurer","whitesilver_adventurer")

upgrade2(troops,"association_footman","association_infantry","association_crossbowman")
upgrade(troops,"association_infantry","association_warrior")
upgrade(troops,"association_crossbowman","association_ranger")

upgrade2(troops,"association_shade","association_guardian","association_spy")


upgrade2(troops,"sabianist","sabianist_guardian_warrior","sabianist_diviner")
upgrade(troops,"sabianist_guardian_warrior","starcourt_knight")
upgrade(troops,"sabianist_diviner","sabianist_confessor")


##_____________________________________________________________________________自生者________________________________________________________________________________
##龙孽
upgrade(troops,"dragonmania","dragonfrenzy")
upgrade(troops,"dragonfrenzy","dragon_abomination")



upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")