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

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

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


troops_multiplayer = [

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_studded_leather_coat,itm_ankle_boots,itm_flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
    itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_spiked_helmet,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   def_attrib|level(23),wp(150),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_kouruto_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(21),wp(90)|wp_archery(150),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   def_attrib|level(23),wp(130),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_nordic_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_nomad_boots,itm_ankle_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_mail_shirt,itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_ankle_boots],
   def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wp_melee(110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_linen_tunic,itm_hide_boots],
   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_linen_tunic,itm_hide_boots],
   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic,itm_hide_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   def_attrib_multiplayer|level(21),wpe(70,130,60,100),knows_riding_2|knows_power_draw_3|knows_horse_archery_2|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   def_attrib_multiplayer|level(21),wp(115),knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic,itm_leather_boots],
   def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_leather_boots],
   def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(19),wp(105),knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wp(100),knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_5|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_saddle_horse],
   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  #replacable troop, not used
  ["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors

]