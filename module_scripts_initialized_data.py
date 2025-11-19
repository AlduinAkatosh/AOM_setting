# -*- coding: UTF-8 -*-

from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from header_presentations import *
from ID_animations import *
from process_troops import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


##将存在troop里的兵种职能存进slot
def set_troop_function():
  troop_function = []
  for i_troop in xrange(len(troops)):
    troop_function.append((troop_set_slot, i_troop, slot_troop_function, troops[i_troop][16]))
  return troop_function[:]


scripts_initialized_data = [

#This script integrates other definition scripts, and all newly added definition scripts are written here. This script will be in called in game_start.
  ("initiallization_script_integration", [
      (call_script, "script_initial_necromacer_state"),
      (call_script, "script_initialize_culture"),#设置文化
      (call_script, "script_initialize_npcs"), #npc设置
      (call_script, "script_initial_troop_skill"),
      (call_script, "script_initial_active_skill_information"),
      (call_script, "script_initial_troop_root_data"),
      (call_script, "script_initialize_troop_function"),
      (call_script, "script_initial_faction_data"),
      (call_script, "script_initial_center_zone"),
      (call_script, "script_initial_detachment"),

      (assign, "$player_adventuror_level", -1),#冒险等阶
      (assign, "$campaign_round", -1),#会战轮数
  ]),


#定义兵种职能，用于会战分兵，数据定义在troop里。
("initialize_troop_function", set_troop_function()),

#初始化文化相关
  ("initialize_culture", [
      (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, "itm_culture_powell"), #玩家先默认是文化1

#普威尔文化
      (faction_set_slot, "fac_kingdom_1", slot_faction_culture, "itm_culture_powell"),
      (item_set_slot, "itm_culture_powell",  slot_culture_tier_1_troop, "trp_powell_peasant"), #村庄募兵
      (item_set_slot, "itm_culture_powell",  slot_culture_tier_2_troop, "trp_powell_militia"),
      (item_set_slot, "itm_culture_powell",  slot_culture_tier_3_troop, "trp_powell_footman"),
      (item_set_slot, "itm_culture_powell",  slot_culture_tier_4_troop, "trp_powell_conjuring_infantry"),
      (item_set_slot, "itm_culture_powell",  slot_culture_tier_5_troop, "trp_powell_conjuring_rider"),

      (item_set_slot, "itm_culture_powell",  slot_culture_reinforcements_a, "pt_kingdom_1_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_powell",  slot_culture_reinforcements_b, "pt_kingdom_1_reinforcements_b"),
      (item_set_slot, "itm_culture_powell",  slot_culture_reinforcements_c, "pt_kingdom_1_reinforcements_c"),
      (item_set_slot, "itm_culture_powell",  slot_culture_deserter_troop, "trp_powell_deserter"), #任务设置
      (item_set_slot, "itm_culture_powell",  slot_culture_messenger_troop, "trp_powell_messenger"),
      (item_set_slot, "itm_culture_powell",  slot_culture_formation, "itm_formation_assault"), #阵型

      (item_set_slot, "itm_culture_powell",  slot_culture_guard_troop, "trp_powell_armored_conjurer"), #场景人物设置
      (item_set_slot, "itm_culture_powell",  slot_culture_prison_guard_troop, "trp_powell_executioner"),
      (item_set_slot, "itm_culture_powell",  slot_culture_castle_guard_troop, "trp_powell_praetorian"),

      (item_set_slot, "itm_culture_powell", slot_culture_town_walker_male_troop, "trp_powell_peasant"), 
      (item_set_slot, "itm_culture_powell", slot_culture_town_walker_female_troop, "trp_town_walker_2"),
      (item_set_slot, "itm_culture_powell", slot_culture_village_walker_male_troop, "trp_village_walker_1"),
      (item_set_slot, "itm_culture_powell", slot_culture_village_walker_female_troop, "trp_village_walker_2"),
      (item_set_slot, "itm_culture_powell", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_powell", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#伊希斯文化
      (faction_set_slot, "fac_kingdom_2", slot_faction_culture, "itm_culture_elf"),
      (item_set_slot, "itm_culture_elf",  slot_culture_tier_1_troop, "trp_yishith_human_resident"), #村庄募兵
      (item_set_slot, "itm_culture_elf",  slot_culture_tier_2_troop, "trp_yishith_human_militia"),
      (item_set_slot, "itm_culture_elf",  slot_culture_tier_3_troop, "trp_yishith_human_infantry"),
      (item_set_slot, "itm_culture_elf",  slot_culture_tier_4_troop, "trp_yishith_inferior_elf"),
      (item_set_slot, "itm_culture_elf",  slot_culture_tier_5_troop, "trp_yishith_elf_hunter"),

      (item_set_slot, "itm_culture_elf",  slot_culture_reinforcements_a, "pt_kingdom_2_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_elf",  slot_culture_reinforcements_b, "pt_kingdom_2_reinforcements_b"),
      (item_set_slot, "itm_culture_elf",  slot_culture_reinforcements_c, "pt_kingdom_2_reinforcements_c"),
      (item_set_slot, "itm_culture_elf", slot_culture_deserter_troop, "trp_yishith_deserter"),  #任务设置
      (item_set_slot, "itm_culture_elf", slot_culture_messenger_troop, "trp_yishith_messenger"),
      (item_set_slot, "itm_culture_elf",  slot_culture_formation, "itm_formation_suppress"), #阵型

      (item_set_slot, "itm_culture_elf", slot_culture_guard_troop, "trp_yishith_jungleslaughterer"), #场景人物设置
      (item_set_slot, "itm_culture_elf", slot_culture_prison_guard_troop, "trp_yishith_elf_outrider"),
      (item_set_slot, "itm_culture_elf", slot_culture_castle_guard_troop, "trp_yishith_elf_woodguard"),

      (item_set_slot, "itm_culture_elf", slot_culture_town_walker_male_troop, "trp_yishith_human_resident"), 
      (item_set_slot, "itm_culture_elf", slot_culture_town_walker_female_troop, "trp_yishith_inferior_elf"),
      (item_set_slot, "itm_culture_elf", slot_culture_village_walker_male_troop, "trp_yishith_human_resident"),
      (item_set_slot, "itm_culture_elf", slot_culture_village_walker_female_troop, "trp_yishith_inferior_elf"),
      (item_set_slot, "itm_culture_elf", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_elf", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#科鲁托文化
      (faction_set_slot, "fac_kingdom_3", slot_faction_culture, "itm_culture_therianthropy_tribe"),
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_tier_1_troop, "trp_kouruto_human_settler"), #村庄募兵
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_tier_2_troop, "trp_kouruto_stray_therianthropy"),
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_tier_3_troop, "trp_kouruto_young_mercenary"),
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_tier_4_troop, "trp_kouruto_therianthropy_mercenary"),
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_tier_5_troop, "trp_kouruto_auxiliary_light_infantry"),

      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_reinforcements_a, "pt_kingdom_3_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_reinforcements_b, "pt_kingdom_3_reinforcements_b"),
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_reinforcements_c, "pt_kingdom_3_reinforcements_c"),
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_deserter_troop, "trp_kouruto_deserter"),  #任务设置
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_messenger_troop, "trp_kouruto_messenger"),
      (item_set_slot, "itm_culture_therianthropy_tribe",  slot_culture_formation, "itm_formation_common"), #阵型

      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_guard_troop, "trp_kouruto_auxiliary_ranger"), #场景人物设置
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_prison_guard_troop, "trp_kouruto_auxiliary_heavy_rider"),
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_castle_guard_troop, "trp_kouruto_therianthropy_mercenary_captain"),

      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_town_walker_male_troop, "trp_kouruto_stray_therianthropy"), 
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_town_walker_female_troop, "trp_kouruto_human_settler"),
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_village_walker_male_troop, "trp_kouruto_stray_therianthropy"),
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_village_walker_female_troop, "trp_kouruto_human_settler"),
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_therianthropy_tribe", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#邦联文化
      (faction_set_slot, "fac_kingdom_4", slot_faction_culture, "itm_culture_confederation"),
      (item_set_slot, "itm_culture_confederation",  slot_culture_tier_1_troop, "trp_confederation_serf"), #村庄募兵
      (item_set_slot, "itm_culture_confederation",  slot_culture_tier_2_troop, "trp_confederation_recruits_slave"),
      (item_set_slot, "itm_culture_confederation",  slot_culture_tier_3_troop, "trp_confederation_serf_warrior"),
      (item_set_slot, "itm_culture_confederation",  slot_culture_tier_4_troop, "trp_diemer_freeman"),
      (item_set_slot, "itm_culture_confederation",  slot_culture_tier_5_troop, "trp_diemer_heavy_footman"),

      (item_set_slot, "itm_culture_confederation",  slot_culture_reinforcements_a, "pt_kingdom_4_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_confederation",  slot_culture_reinforcements_b, "pt_kingdom_4_reinforcements_b"),
      (item_set_slot, "itm_culture_confederation",  slot_culture_reinforcements_c, "pt_kingdom_4_reinforcements_c"),
      (item_set_slot, "itm_culture_confederation", slot_culture_deserter_troop, "trp_confederation_deserter"),  #任务设置
      (item_set_slot, "itm_culture_confederation", slot_culture_messenger_troop, "trp_confederation_messenger"),
      (item_set_slot, "itm_culture_confederation",  slot_culture_formation, "itm_formation_counterattack"), #阵型

      (item_set_slot, "itm_culture_confederation", slot_culture_guard_troop, "trp_meat_puppet"), #场景人物设置
      (item_set_slot, "itm_culture_confederation", slot_culture_prison_guard_troop, "trp_marsh_council_guard"),
      (item_set_slot, "itm_culture_confederation", slot_culture_castle_guard_troop, "trp_diemer_guardian"),

      (item_set_slot, "itm_culture_confederation", slot_culture_town_walker_male_troop, "trp_diemer_freeman"), 
      (item_set_slot, "itm_culture_confederation", slot_culture_town_walker_female_troop, "trp_marsh_deepone_freeman"),
      (item_set_slot, "itm_culture_confederation", slot_culture_village_walker_male_troop, "trp_confederation_serf"),
      (item_set_slot, "itm_culture_confederation", slot_culture_village_walker_female_troop, "trp_confederation_fishing_serf"),
      (item_set_slot, "itm_culture_confederation", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_confederation", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#教国文化
      (faction_set_slot, "fac_kingdom_5", slot_faction_culture, "itm_culture_papal"),
      (item_set_slot, "itm_culture_papal",  slot_culture_tier_1_troop, "trp_papal_citizen"), #村庄募兵
      (item_set_slot, "itm_culture_papal",  slot_culture_tier_2_troop, "trp_papal_recruit_militia"),
      (item_set_slot, "itm_culture_papal",  slot_culture_tier_3_troop, "trp_papal_recruit_spearman"),
      (item_set_slot, "itm_culture_papal",  slot_culture_tier_4_troop, "trp_papal_hunter"),
      (item_set_slot, "itm_culture_papal",  slot_culture_tier_5_troop, "trp_papal_joint_defense_militia"),

      (item_set_slot, "itm_culture_papal",  slot_culture_reinforcements_a, "pt_kingdom_5_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_papal",  slot_culture_reinforcements_b, "pt_kingdom_5_reinforcements_b"),
      (item_set_slot, "itm_culture_papal",  slot_culture_reinforcements_c, "pt_kingdom_5_reinforcements_c"),
      (item_set_slot, "itm_culture_papal", slot_culture_deserter_troop, "trp_papal_deserter"),  #任务设置
      (item_set_slot, "itm_culture_papal", slot_culture_messenger_troop, "trp_papal_messenger"),
      (item_set_slot, "itm_culture_papal",  slot_culture_formation, "itm_formation_defense"), #阵型

      (item_set_slot, "itm_culture_papal", slot_culture_guard_troop, "trp_patron_knight"), #场景人物设置
      (item_set_slot, "itm_culture_papal", slot_culture_prison_guard_troop, "trp_doctrinal_sitting_magistrate"),
      (item_set_slot, "itm_culture_papal", slot_culture_castle_guard_troop, "trp_holy_church_guard"),

      (item_set_slot, "itm_culture_papal", slot_culture_town_walker_male_troop, "trp_papal_citizen"), 
      (item_set_slot, "itm_culture_papal", slot_culture_town_walker_female_troop, "trp_town_walker_2"),
      (item_set_slot, "itm_culture_papal", slot_culture_village_walker_male_troop, "trp_papal_citizen"),
      (item_set_slot, "itm_culture_papal", slot_culture_village_walker_female_troop, "trp_village_walker_2"),
      (item_set_slot, "itm_culture_papal", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_papal", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#东方文化
      (faction_set_slot, "fac_kingdom_6", slot_faction_culture, "itm_culture_east"),
      (item_set_slot, "itm_culture_east",  slot_culture_tier_1_troop, "trp_longshu_zhengzu"), #村庄募兵
      (item_set_slot, "itm_culture_east",  slot_culture_tier_2_troop, "trp_longshu_zhengzu"),
      (item_set_slot, "itm_culture_east",  slot_culture_tier_3_troop, "trp_longshu_zhengzu"),
      (item_set_slot, "itm_culture_east",  slot_culture_tier_4_troop, "trp_longshu_zhengzu"),
      (item_set_slot, "itm_culture_east",  slot_culture_tier_5_troop, "trp_longshu_zhengzu"),

      (item_set_slot, "itm_culture_east",  slot_culture_reinforcements_a, "pt_kingdom_6_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_east",  slot_culture_reinforcements_b, "pt_kingdom_6_reinforcements_b"),
      (item_set_slot, "itm_culture_east",  slot_culture_reinforcements_c, "pt_kingdom_6_reinforcements_c"),
      (item_set_slot, "itm_culture_east", slot_culture_deserter_troop, "trp_longshu_deserter"),  #任务设置
      (item_set_slot, "itm_culture_east", slot_culture_messenger_troop, "trp_longshu_messenger"),
      (item_set_slot, "itm_culture_east",  slot_culture_formation, "itm_formation_common"), #阵型

      (item_set_slot, "itm_culture_east", slot_culture_guard_troop, "trp_longshu_zhengzu"), #场景人物设置
      (item_set_slot, "itm_culture_east", slot_culture_prison_guard_troop, "trp_longshu_zhengzu"),
      (item_set_slot, "itm_culture_east", slot_culture_castle_guard_troop, "trp_longshu_zhengzu"),

      (item_set_slot, "itm_culture_east", slot_culture_town_walker_male_troop, "trp_town_walker_1"), 
      (item_set_slot, "itm_culture_east", slot_culture_town_walker_female_troop, "trp_town_walker_2"),
      (item_set_slot, "itm_culture_east", slot_culture_village_walker_male_troop, "trp_village_walker_1"),
      (item_set_slot, "itm_culture_east", slot_culture_village_walker_female_troop, "trp_village_walker_2"),
      (item_set_slot, "itm_culture_east", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_east", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#大公国文化
      (faction_set_slot, "fac_kingdom_7", slot_faction_culture, "itm_culture_westcoast"),
      (item_set_slot, "itm_culture_westcoast",  slot_culture_tier_1_troop, "trp_starkhook_recruit"), #村庄募兵
      (item_set_slot, "itm_culture_westcoast",  slot_culture_tier_2_troop, "trp_starkhook_armed_sailor"),
      (item_set_slot, "itm_culture_westcoast",  slot_culture_tier_3_troop, "trp_starkhook_mercenary"),
      (item_set_slot, "itm_culture_westcoast",  slot_culture_tier_4_troop, "trp_starkhook_onboard_infantry"),
      (item_set_slot, "itm_culture_westcoast",  slot_culture_tier_5_troop, "trp_starkhook_enhanced_warrior"),

      (item_set_slot, "itm_culture_westcoast",  slot_culture_reinforcements_a, "pt_kingdom_7_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_westcoast",  slot_culture_reinforcements_b, "pt_kingdom_7_reinforcements_b"),
      (item_set_slot, "itm_culture_westcoast",  slot_culture_reinforcements_c, "pt_kingdom_7_reinforcements_c"),
      (item_set_slot, "itm_culture_westcoast", slot_culture_deserter_troop, "trp_starkhook_deserter"),  #任务设置
      (item_set_slot, "itm_culture_westcoast", slot_culture_messenger_troop, "trp_starkhook_messenger"),
      (item_set_slot, "itm_culture_westcoast",  slot_culture_formation, "itm_formation_common"), #阵型

      (item_set_slot, "itm_culture_westcoast", slot_culture_guard_troop, "trp_starkhook_boat_fighter"), #场景人物设置
      (item_set_slot, "itm_culture_westcoast", slot_culture_prison_guard_troop, "trp_starkhook_berserker_warrior"),
      (item_set_slot, "itm_culture_westcoast", slot_culture_castle_guard_troop, "trp_starkhook_armoured_swordman"),

      (item_set_slot, "itm_culture_westcoast", slot_culture_town_walker_male_troop, "trp_starkhook_recruit"), 
      (item_set_slot, "itm_culture_westcoast", slot_culture_town_walker_female_troop, "trp_town_walker_2"),
      (item_set_slot, "itm_culture_westcoast", slot_culture_village_walker_male_troop, "trp_starkhook_recruit"),
      (item_set_slot, "itm_culture_westcoast", slot_culture_village_walker_female_troop, "trp_village_walker_2"),
      (item_set_slot, "itm_culture_westcoast", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_westcoast", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),

#自由城邦文化
      (faction_set_slot, "fac_kingdom_8", slot_faction_culture, "itm_culture_state"),
      (item_set_slot, "itm_culture_state",  slot_culture_tier_1_troop, "trp_citizen_pauper"), #村庄募兵
      (item_set_slot, "itm_culture_state",  slot_culture_tier_2_troop, "trp_citizen_militia"),
      (item_set_slot, "itm_culture_state",  slot_culture_tier_3_troop, "trp_citizen_defend_militia"),
      (item_set_slot, "itm_culture_state",  slot_culture_tier_4_troop, "trp_states_civilian"),
      (item_set_slot, "itm_culture_state",  slot_culture_tier_5_troop, "trp_states_skirmisher"),

      (item_set_slot, "itm_culture_state",  slot_culture_reinforcements_a, "pt_kingdom_8_reinforcements_a"), #增援设置
      (item_set_slot, "itm_culture_state",  slot_culture_reinforcements_b, "pt_kingdom_8_reinforcements_b"),
      (item_set_slot, "itm_culture_state",  slot_culture_reinforcements_c, "pt_kingdom_8_reinforcements_c"),
      (item_set_slot, "itm_culture_state", slot_culture_deserter_troop, "trp_citizen_deserter"),  #任务设置
      (item_set_slot, "itm_culture_state", slot_culture_messenger_troop, "trp_citizen_messenger"),
      (item_set_slot, "itm_culture_state",  slot_culture_formation, "itm_formation_fortress"), #阵型

      (item_set_slot, "itm_culture_state", slot_culture_guard_troop, "trp_scepter_dismounted_knight"), #场景人物设置
      (item_set_slot, "itm_culture_state", slot_culture_prison_guard_troop, "trp_states_heavy_armored_crossbowman"),
      (item_set_slot, "itm_culture_state", slot_culture_castle_guard_troop, "trp_states_nobility"),

      (item_set_slot, "itm_culture_state", slot_culture_town_walker_male_troop, "trp_states_civilian"), 
      (item_set_slot, "itm_culture_state", slot_culture_town_walker_female_troop, "trp_town_walker_2"),
      (item_set_slot, "itm_culture_state", slot_culture_village_walker_male_troop, "trp_village_walker_1"),
      (item_set_slot, "itm_culture_state", slot_culture_village_walker_female_troop, "trp_citizen_pauper"),
      (item_set_slot, "itm_culture_state", slot_culture_town_spy_male_troop, "trp_spy_walker_1"),
      (item_set_slot, "itm_culture_state", slot_culture_town_spy_female_troop, "trp_spy_walker_2"),
  ]),


#伙伴npc设置（包括会入队的谋国者）
  ("initialize_npcs",
    [
        (assign, "$disable_npc_complaints", 0), #npc吵架开启

        (troop_set_slot, "trp_npc1", slot_troop_morality_type, tmt_egalitarian),  #恩和enghe
        (troop_set_slot, "trp_npc1", slot_troop_morality_value, 2),  
        (troop_set_slot, "trp_npc1", slot_troop_2ary_morality_type, tmt_aristocratic),  #enghe
        (troop_set_slot, "trp_npc1", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc1", slot_troop_personalityclash_object, "trp_npc6"),  #enghe - Odungova
        (troop_set_slot, "trp_npc1", slot_troop_personalityclash2_object, "trp_npc15"),  #enghe - Vivian
        (troop_set_slot, "trp_npc1", slot_troop_personalitymatch_object, "trp_npc3"),  #enghe - Apry
        (troop_set_slot, "trp_npc1", slot_troop_home, "p_village_3_3"), #Tumenbaoyin_Gather
        (troop_set_slot, "trp_npc1", slot_troop_payment_request, 3000), 
		(troop_set_slot, "trp_npc1", slot_troop_kingsupport_argument, argument_ruler),
		(troop_set_slot, "trp_npc1", slot_troop_kingsupport_opponent, "trp_npc6"), #Odungova
		(troop_set_slot, "trp_npc1", slot_troop_town_with_contacts, "p_village_1_11"), #Yagen_Village
		(troop_set_slot, "trp_npc1", slot_troop_original_faction, 0), #ichamur
		(troop_set_slot, "trp_npc1", slot_lord_reputation_type, lrep_roguish), #
		
		
		
        (troop_set_slot, "trp_npc2", slot_troop_morality_type, tmt_humanitarian), #Amily
        (troop_set_slot, "trp_npc2", slot_troop_morality_value, 2),  
        (troop_set_slot, "trp_npc2", slot_troop_2ary_morality_type, tmt_honest),  
        (troop_set_slot, "trp_npc2", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc2", slot_troop_personalityclash_object, "trp_npc5"), #Amily - Sadi
        (troop_set_slot, "trp_npc2", slot_troop_personalityclash2_object, "trp_npc14"), #Amily - Pelop
        (troop_set_slot, "trp_npc2", slot_troop_personalitymatch_object, "trp_npc19"),  #Amily - Mayvis
        (troop_set_slot, "trp_npc2", slot_troop_home, "p_village_1_9"), #Griffland_Village
        (troop_set_slot, "trp_npc2", slot_troop_payment_request, 4000), 
		(troop_set_slot, "trp_npc2", slot_troop_kingsupport_argument, argument_victory),
		(troop_set_slot, "trp_npc2", slot_troop_kingsupport_opponent, "trp_npc14"), #Pelop
		(troop_set_slot, "trp_npc2", slot_troop_town_with_contacts, "p_village_1_9"), #Griffland_Village
		(troop_set_slot, "trp_npc2", slot_troop_original_faction, 0), #ichamur
		(troop_set_slot, "trp_npc2", slot_lord_reputation_type, lrep_custodian), #

#
        (troop_set_slot, "trp_npc3", slot_troop_morality_type, tmt_humanitarian), #Apry
        (troop_set_slot, "trp_npc3", slot_troop_morality_value, 4),  
        (troop_set_slot, "trp_npc3", slot_troop_2ary_morality_type, tmt_aristocratic), 
        (troop_set_slot, "trp_npc3", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc3", slot_troop_personalityclash_object, "trp_npc13"), #Apry - Meroy
        (troop_set_slot, "trp_npc3", slot_troop_personalityclash2_object, "trp_npc20"), #Apry - Sabina
        (troop_set_slot, "trp_npc3", slot_troop_personalitymatch_object, "trp_npc1"), #Apry - Enghe
        (troop_set_slot, "trp_npc3", slot_troop_home, "p_town_33"), #Tradewind
        (troop_set_slot, "trp_npc3", slot_troop_payment_request, 0), 
		(troop_set_slot, "trp_npc3", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc3", slot_troop_kingsupport_opponent, "trp_npc20"), #Sabina
		(troop_set_slot, "trp_npc3", slot_troop_town_with_contacts, "p_town_15"), #yalen
		(troop_set_slot, "trp_npc3", slot_troop_original_faction, 0), #ichamur
		(troop_set_slot, "trp_npc3", slot_lord_reputation_type, lrep_benefactor), #

		
		
        (troop_set_slot, "trp_npc4", slot_troop_morality_type, tmt_aristocratic), #Fanlentina
        (troop_set_slot, "trp_npc4", slot_troop_morality_value, 4),  
        (troop_set_slot, "trp_npc4", slot_troop_2ary_morality_type, tmt_honest), 
        (troop_set_slot, "trp_npc4", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc4", slot_troop_personalityclash_object, "trp_npc8"), #Fanlentina - Caisiale
        (troop_set_slot, "trp_npc4", slot_troop_personalityclash2_object, "trp_npc18"), #Fanlentina - Isidor
        (troop_set_slot, "trp_npc4", slot_troop_personalitymatch_object, "trp_npc10"), #Fanlentina - Laurie
        (troop_set_slot, "trp_npc4", slot_troop_home, "p_castle_1_10"), #Gaccya_Fief
        (troop_set_slot, "trp_npc4", slot_troop_payment_request, 0), 
		(troop_set_slot, "trp_npc4", slot_troop_kingsupport_argument, argument_claim),
		(troop_set_slot, "trp_npc4", slot_troop_kingsupport_opponent, "trp_npc18"), #Isidor
		(troop_set_slot, "trp_npc4", slot_troop_town_with_contacts, "p_town_3"), #veluca
		(troop_set_slot, "trp_npc4", slot_troop_original_faction, 0), #ichamur
		(troop_set_slot, "trp_npc4", slot_lord_reputation_type, lrep_cunning), #

		
        (troop_set_slot, "trp_npc5", slot_troop_morality_type, tmt_egalitarian),  #Sadi
        (troop_set_slot, "trp_npc5", slot_troop_morality_value, 3),  
        (troop_set_slot, "trp_npc5", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc5", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc5", slot_troop_personalityclash_object, "trp_npc2"),  #Sadi - Amily
        (troop_set_slot, "trp_npc5", slot_troop_personalityclash2_object, "trp_npc22"),  #Sadi- Ai_Miye
        (troop_set_slot, "trp_npc5", slot_troop_personalitymatch_object, "trp_npc7"),  #Sadi - Qester
        (troop_set_slot, "trp_npc5", slot_troop_home, "p_village_5_7"), #Raydiciar_Town
        (troop_set_slot, "trp_npc5", slot_troop_payment_request, 4000),
		(troop_set_slot, "trp_npc5", slot_troop_kingsupport_argument, argument_ruler),
		(troop_set_slot, "trp_npc5", slot_troop_kingsupport_opponent, "trp_npc2"), #Amily
		(troop_set_slot, "trp_npc5", slot_troop_town_with_contacts, "p_town_10"), #tulga
		(troop_set_slot, "trp_npc5", slot_troop_original_faction, "fac_kingdom_3"), #khergit
		(troop_set_slot, "trp_npc5", slot_lord_reputation_type, lrep_cunning), #

		
		
        (troop_set_slot, "trp_npc6", slot_troop_morality_type, tmt_humanitarian), #Odungova
        (troop_set_slot, "trp_npc6", slot_troop_morality_value, 2),  
        (troop_set_slot, "trp_npc6", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc6", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc6", slot_troop_personalityclash_object, "trp_npc1"), #Odungova - Enghe
        (troop_set_slot, "trp_npc6", slot_troop_personalityclash2_object, "trp_npc12"), #Odungova - Su_Budao
        (troop_set_slot, "trp_npc6", slot_troop_personalitymatch_object, "trp_npc20"),  #Odungova - Sabina
        (troop_set_slot, "trp_npc6", slot_troop_home, "p_steppe_bandit_spawn_point"), #p_steppe_bandit_spawn_point
        (troop_set_slot, "trp_npc6", slot_troop_payment_request, 3800),
		(troop_set_slot, "trp_npc6", slot_troop_kingsupport_argument, argument_victory),
		(troop_set_slot, "trp_npc6", slot_troop_kingsupport_opponent, "trp_npc12"), #Su_Budao
		(troop_set_slot, "trp_npc6", slot_troop_town_with_contacts, "p_town_7"), #uxkhal
		(troop_set_slot, "trp_npc6", slot_troop_original_faction, "fac_kingdom_1"), #swadia
		(troop_set_slot, "trp_npc6", slot_lord_reputation_type, lrep_upstanding), #

		
		
        (troop_set_slot, "trp_npc7", slot_troop_morality_type, tmt_egalitarian),  #Qester
        (troop_set_slot, "trp_npc7", slot_troop_morality_value, 3),  
        (troop_set_slot, "trp_npc7", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc7", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc7", slot_troop_personalityclash_object, "trp_npc19"),  #Qester - Mayvis
        (troop_set_slot, "trp_npc7", slot_troop_personalityclash2_object, "trp_npc21"),  #Qester - Ouyang_Mingna
        (troop_set_slot, "trp_npc7", slot_troop_personalitymatch_object, "trp_npc5"),  #Qester - Sadi
        (troop_set_slot, "trp_npc7", slot_troop_home, "p_town_12"), #Mourngelith
#        (troop_set_slot, "trp_npc7", slot_troop_payment_request, 5000),
		(troop_set_slot, "trp_npc7", slot_troop_kingsupport_argument, argument_victory),
		(troop_set_slot, "trp_npc7", slot_troop_kingsupport_opponent, "trp_npc19"), #Mayvis
		(troop_set_slot, "trp_npc7", slot_troop_town_with_contacts, "p_town_2"), #Norwind
		(troop_set_slot, "trp_npc7", slot_troop_original_faction, 0), #swadia
		(troop_set_slot, "trp_npc7", slot_lord_reputation_type, lrep_custodian), #

		
		
        (troop_set_slot, "trp_npc8", slot_troop_morality_type, tmt_aristocratic), #Caisiale
        (troop_set_slot, "trp_npc8", slot_troop_morality_value, 3),  
        (troop_set_slot, "trp_npc8", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc8", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc8", slot_troop_personalityclash_object, "trp_npc4"), #Caisiale - Fanlentina
        (troop_set_slot, "trp_npc8", slot_troop_personalityclash2_object, "trp_npc9"), #Caisiale - Alexia
        (troop_set_slot, "trp_npc8", slot_troop_personalitymatch_object, "trp_npc16"),  #Caisiale - Lei_Lisi
        (troop_set_slot, "trp_npc8", slot_troop_home, "p_town_18"), #zherrow
        (troop_set_slot, "trp_npc8", slot_troop_payment_request, 5000),
		(troop_set_slot, "trp_npc8", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc8", slot_troop_kingsupport_opponent, "trp_npc4"), #Fanlentina
		(troop_set_slot, "trp_npc8", slot_troop_town_with_contacts, "p_town_12"), #wercheg
		(troop_set_slot, "trp_npc8", slot_troop_original_faction, "fac_kingdom_4"), #nords
		(troop_set_slot, "trp_npc8", slot_lord_reputation_type, lrep_martial), #

		
        (troop_set_slot, "trp_npc9", slot_troop_morality_type, tmt_aristocratic), #Alexia
        (troop_set_slot, "trp_npc9", slot_troop_morality_value, 2),  #beheshtur
        (troop_set_slot, "trp_npc9", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc9", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc9", slot_troop_personalityclash_object, "trp_npc8"), #Alexia vs Caisiale
        (troop_set_slot, "trp_npc9", slot_troop_personalityclash2_object, "trp_npc20"), #Alexia vs Sabina
        (troop_set_slot, "trp_npc9", slot_troop_personalitymatch_object, "trp_npc12"),  #Alexia - Su_Budao
        (troop_set_slot, "trp_npc9", slot_troop_home, "p_town_9"), #Ardor_of_Demise
        (troop_set_slot, "trp_npc9", slot_troop_payment_request, 5000),
		(troop_set_slot, "trp_npc9", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc9", slot_troop_kingsupport_opponent, "trp_npc8"), #Caisiale
		(troop_set_slot, "trp_npc9", slot_troop_town_with_contacts, "p_town_8"), #reyvadin
		(troop_set_slot, "trp_npc9", slot_troop_original_faction, "fac_kingdom_2"), #vaegirs
		(troop_set_slot, "trp_npc9", slot_lord_reputation_type, lrep_martial), #

		
        (troop_set_slot, "trp_npc10", slot_troop_morality_type, tmt_humanitarian), #Laurie
        (troop_set_slot, "trp_npc10", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc10", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc10", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc10", slot_troop_personalityclash_object, "trp_npc16"), #Laurie vs Lei_Lisi
        (troop_set_slot, "trp_npc10", slot_troop_personalityclash2_object, "trp_npc17"), #Laurie vs Michelia
        (troop_set_slot, "trp_npc10", slot_troop_personalitymatch_object, "trp_npc4"),  #Laurie likes Fanlentina
        (troop_set_slot, "trp_npc10", slot_troop_home, "p_town_16"), #Slaufete
        (troop_set_slot, "trp_npc10", slot_troop_payment_request, 3200),
		(troop_set_slot, "trp_npc10", slot_troop_kingsupport_argument, argument_ruler),
		(troop_set_slot, "trp_npc10", slot_troop_kingsupport_opponent, "trp_npc17"), #Michelia
		(troop_set_slot, "trp_npc10", slot_troop_town_with_contacts, "p_town_5"), #jelkala
		(troop_set_slot, "trp_npc10", slot_troop_original_faction, "fac_kingdom_5"), #rhodoks
		(troop_set_slot, "trp_npc10", slot_lord_reputation_type, lrep_benefactor), #

		
		
        (troop_set_slot, "trp_npc11", slot_troop_morality_type, tmt_egalitarian),  #Lilian
        (troop_set_slot, "trp_npc11", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc11", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc11", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc11", slot_troop_personalityclash_object, "trp_npc13"),  #Lilian vs Meroy
        (troop_set_slot, "trp_npc11", slot_troop_personalityclash2_object, "trp_npc19"),  #Lilian - Mayvis
        (troop_set_slot, "trp_npc11", slot_troop_personalitymatch_object, "trp_npc14"),  #Lilian likes Pelop
        (troop_set_slot, "trp_npc11", slot_troop_home, "p_town_4"), #Lesaff
        (troop_set_slot, "trp_npc11", slot_troop_payment_request, 4200),
		(troop_set_slot, "trp_npc11", slot_troop_kingsupport_argument, argument_claim),
		(troop_set_slot, "trp_npc11", slot_troop_kingsupport_opponent, "trp_npc13"), #Meroy
		(troop_set_slot, "trp_npc11", slot_troop_town_with_contacts, "p_town_6"), #praven
		(troop_set_slot, "trp_npc11", slot_troop_original_faction, 0), #	
		(troop_set_slot, "trp_npc11", slot_lord_reputation_type, lrep_custodian), #
		

        (troop_set_slot, "trp_npc12", slot_troop_morality_type, tmt_humanitarian), #Su_Budao
        (troop_set_slot, "trp_npc12", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc12", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc12", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc12", slot_troop_personalityclash_object, "trp_npc6"), #Su_Budao - Odungova
        (troop_set_slot, "trp_npc12", slot_troop_personalityclash2_object, "trp_npc16"), #Su_Budao - Lei_Lisi
        (troop_set_slot, "trp_npc12", slot_troop_personalitymatch_object, "trp_npc9"),  #Su_Budao - Alexia
        (troop_set_slot, "trp_npc12", slot_troop_home, "p_town_10"), #Kouruto
        (troop_set_slot, "trp_npc12", slot_troop_payment_request, 2500),
		(troop_set_slot, "trp_npc12", slot_troop_kingsupport_argument, argument_claim),
		(troop_set_slot, "trp_npc12", slot_troop_kingsupport_opponent, "trp_npc16"), #Lei_Lisi
		(troop_set_slot, "trp_npc12", slot_troop_town_with_contacts, "p_town_14"), #halmar
		(troop_set_slot, "trp_npc12", slot_troop_original_faction, 0), #	
		(troop_set_slot, "trp_npc12", slot_lord_reputation_type, lrep_benefactor), #

		
		
        (troop_set_slot, "trp_npc13", slot_troop_morality_type, tmt_aristocratic), #Meroy
        (troop_set_slot, "trp_npc13", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc13", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc13", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc13", slot_troop_personalityclash_object, "trp_npc3"), #Meroy - Apry
        (troop_set_slot, "trp_npc13", slot_troop_personalityclash2_object, "trp_npc11"), #Meroy - Lilian
        (troop_set_slot, "trp_npc13", slot_troop_personalitymatch_object, "trp_npc15"), #Meroy - Vivian
        (troop_set_slot, "trp_npc13", slot_troop_home, "p_village_5_18"), #Renon_Town
        (troop_set_slot, "trp_npc13", slot_troop_payment_request, 8000),
		(troop_set_slot, "trp_npc13", slot_troop_kingsupport_argument, argument_claim),
		(troop_set_slot, "trp_npc13", slot_troop_kingsupport_opponent, "trp_npc3"), #Apry
		(troop_set_slot, "trp_npc13", slot_troop_town_with_contacts, "p_town_4"), #suno
		(troop_set_slot, "trp_npc13", slot_troop_original_faction, 0), #	
		(troop_set_slot, "trp_npc13", slot_lord_reputation_type, lrep_roguish), #

		
		
        (troop_set_slot, "trp_npc14", slot_troop_morality_type, tmt_aristocratic), #Pelop
        (troop_set_slot, "trp_npc14", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc14", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc14", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc14", slot_troop_personalityclash_object, "trp_npc2"), #Pelop - Amily
        (troop_set_slot, "trp_npc14", slot_troop_personalityclash2_object, "trp_npc15"), #Pelop - Vivian
        (troop_set_slot, "trp_npc14", slot_troop_personalitymatch_object, "trp_npc11"), #Pelop - Lilian
        (troop_set_slot, "trp_npc14", slot_troop_home, "p_town_30"), #Whitspring
        (troop_set_slot, "trp_npc14", slot_troop_payment_request, 5000),
		(troop_set_slot, "trp_npc14", slot_troop_kingsupport_argument, argument_victory),
		(troop_set_slot, "trp_npc14", slot_troop_kingsupport_opponent, "trp_npc15"), #Vivian
		(troop_set_slot, "trp_npc14", slot_troop_town_with_contacts, "p_town_16"), #dhirim
		(troop_set_slot, "trp_npc14", slot_troop_original_faction, 0), #	
		(troop_set_slot, "trp_npc14", slot_lord_reputation_type, lrep_selfrighteous), #


        (troop_set_slot, "trp_npc15", slot_troop_morality_type, tmt_egalitarian),  #Vivian
        (troop_set_slot, "trp_npc15", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc15", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc15", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc15", slot_troop_personalityclash_object, "trp_npc1"), #Vivian - Enghe
        (troop_set_slot, "trp_npc15", slot_troop_personalityclash2_object, "trp_npc14"), #Vivian - Pelop
        (troop_set_slot, "trp_npc15", slot_troop_personalitymatch_object, "trp_npc13"), #Vivian - Meroy
        (troop_set_slot, "trp_npc15", slot_troop_home, "p_village_1_11"), #Yagen_Village
        (troop_set_slot, "trp_npc15", slot_troop_payment_request, 5000),
		(troop_set_slot, "trp_npc15", slot_troop_kingsupport_argument, argument_ruler),
		(troop_set_slot, "trp_npc15", slot_troop_kingsupport_opponent, "trp_npc1"), #Enghe
 		(troop_set_slot, "trp_npc15", slot_troop_town_with_contacts, "p_town_18"), #narra
		(troop_set_slot, "trp_npc15", slot_lord_reputation_type, lrep_custodian), #

		
        (troop_set_slot, "trp_npc16", slot_troop_morality_type, tmt_aristocratic), #Lei_Lisi
        (troop_set_slot, "trp_npc16", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc16", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc16", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc16", slot_troop_personalityclash_object, "trp_npc12"), #Lei_Lisi - Su_Budao
        (troop_set_slot, "trp_npc16", slot_troop_personalityclash2_object, "trp_npc10"), #Lei_Lisi - Laurie
        (troop_set_slot, "trp_npc16", slot_troop_personalitymatch_object, "trp_npc8"),  #Lei_Lisi - Caisiale
        (troop_set_slot, "trp_npc16", slot_troop_home, "p_village_6_2"), #Yachuan_Xian
        (troop_set_slot, "trp_npc16", slot_troop_payment_request, 1500),
		(troop_set_slot, "trp_npc16", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc16", slot_troop_kingsupport_opponent, "trp_npc10"), #Laurie
 		(troop_set_slot, "trp_npc16", slot_troop_town_with_contacts, "p_town_20"), #Shangzhou
		(troop_set_slot, "trp_npc16", slot_lord_reputation_type, lrep_roguish), #


        (troop_set_slot, "trp_npc17", slot_troop_morality_type, tmt_aristocratic), #Michelia
        (troop_set_slot, "trp_npc17", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc17", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc17", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc17", slot_troop_personalityclash_object, "trp_npc10"), #Michelia - Laurie
        (troop_set_slot, "trp_npc17", slot_troop_personalityclash2_object, "trp_npc21"), #Michelia - Ouyang_Mingna
        (troop_set_slot, "trp_npc17", slot_troop_personalitymatch_object, "trp_npc18"),  #Michelia - Isidor
        (troop_set_slot, "trp_npc17", slot_troop_home, "p_town_34"), #Congress
        (troop_set_slot, "trp_npc17", slot_troop_payment_request, 6000),
		(troop_set_slot, "trp_npc17", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc17", slot_troop_kingsupport_opponent, "trp_npc21"), #Ouyang_Mingna
 		(troop_set_slot, "trp_npc17", slot_troop_town_with_contacts, "p_town_9"), #khudan
		(troop_set_slot, "trp_npc17", slot_lord_reputation_type, lrep_roguish), #


        (troop_set_slot, "trp_npc18", slot_troop_morality_type, tmt_aristocratic), #Isidor
        (troop_set_slot, "trp_npc18", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc18", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc18", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc18", slot_troop_personalityclash_object, "trp_npc4"), #Isidor - Fanlentina
        (troop_set_slot, "trp_npc18", slot_troop_personalityclash2_object, "trp_npc22"), #Isidor - Ai_Miye
        (troop_set_slot, "trp_npc18", slot_troop_personalitymatch_object, "trp_npc17"),  #Isidor - Michelia
        (troop_set_slot, "trp_npc18", slot_troop_home, "p_village_1_21"), #Kolry_Village
        (troop_set_slot, "trp_npc18", slot_troop_payment_request, 400),
		(troop_set_slot, "trp_npc18", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc18", slot_troop_kingsupport_opponent, "trp_npc22"), #Ai_Miye
 		(troop_set_slot, "trp_npc18", slot_troop_town_with_contacts, "p_village_1_5"), #Gloff_Village
		(troop_set_slot, "trp_npc18", slot_lord_reputation_type, lrep_roguish), #


        (troop_set_slot, "trp_npc19", slot_troop_morality_type, tmt_aristocratic), #Mayvis
        (troop_set_slot, "trp_npc19", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc19", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc19", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc19", slot_troop_personalityclash_object, "trp_npc7"), #Mayvis - Qester
        (troop_set_slot, "trp_npc19", slot_troop_personalityclash2_object, "trp_npc11"), #Mayvis - Lilian
        (troop_set_slot, "trp_npc19", slot_troop_personalitymatch_object, "trp_npc2"),  #Mayvis - Amily
        (troop_set_slot, "trp_npc19", slot_troop_home, "p_town_13"), #Ardor_of_Vita
        (troop_set_slot, "trp_npc19", slot_troop_payment_request, 0),
		(troop_set_slot, "trp_npc19", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc19", slot_troop_kingsupport_opponent, "trp_npc11"), #Lilian
 		(troop_set_slot, "trp_npc19", slot_troop_town_with_contacts, "p_town_9"), #khudan
		(troop_set_slot, "trp_npc19", slot_lord_reputation_type, lrep_roguish), #


        (troop_set_slot, "trp_npc20", slot_troop_morality_type, tmt_aristocratic), #Sabina
        (troop_set_slot, "trp_npc20", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc20", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc20", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc20", slot_troop_personalityclash_object, "trp_npc3"), #Sabina - Apry
        (troop_set_slot, "trp_npc20", slot_troop_personalityclash2_object, "trp_npc9"), #Sabina - Alexia
        (troop_set_slot, "trp_npc20", slot_troop_personalitymatch_object, "trp_npc6"),  #Sabina - Odungova
        (troop_set_slot, "trp_npc20", slot_troop_home, "p_village_1_7"), #Yrina_Plantation
        (troop_set_slot, "trp_npc20", slot_troop_payment_request, 3700),
		(troop_set_slot, "trp_npc20", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc20", slot_troop_kingsupport_opponent, "trp_npc9"), #Alexia
 		(troop_set_slot, "trp_npc20", slot_troop_town_with_contacts, "p_town_9"), #khudan
		(troop_set_slot, "trp_npc20", slot_lord_reputation_type, lrep_roguish), #


        (troop_set_slot, "trp_npc21", slot_troop_morality_type, tmt_aristocratic), #Ouyang_Mingna
        (troop_set_slot, "trp_npc21", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc21", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc21", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc21", slot_troop_personalityclash_object, "trp_npc7"), #Ouyang_Mingna - Qester
        (troop_set_slot, "trp_npc21", slot_troop_personalityclash2_object, "trp_npc17"), #Ouyang_Mingna - Michelia
        (troop_set_slot, "trp_npc21", slot_troop_personalitymatch_object, "trp_npc22"),  #Ouyang_Mingna - Ai_Miye
        (troop_set_slot, "trp_npc21", slot_troop_home, "p_town_19"), #Jingzhou
        (troop_set_slot, "trp_npc21", slot_troop_payment_request, 7000),
		(troop_set_slot, "trp_npc21", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc21", slot_troop_kingsupport_opponent, "trp_npc7"), #Qester
 		(troop_set_slot, "trp_npc21", slot_troop_town_with_contacts, "p_town_9"), #khudan
		(troop_set_slot, "trp_npc21", slot_lord_reputation_type, lrep_roguish), #


        (troop_set_slot, "trp_npc22", slot_troop_morality_type, tmt_aristocratic), #Ai_Miye
        (troop_set_slot, "trp_npc22", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc22", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc22", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc22", slot_troop_personalityclash_object, "trp_npc5"), #Ai_Miye - Sadi
        (troop_set_slot, "trp_npc22", slot_troop_personalityclash2_object, "trp_npc18"), #Ai_Miye - Isidor
        (troop_set_slot, "trp_npc22", slot_troop_personalitymatch_object, "trp_npc21"),  #Ai_Miye - Ouyang_Mingna
        (troop_set_slot, "trp_npc22", slot_troop_home, "p_town_22"), #Sakulano
        (troop_set_slot, "trp_npc22", slot_troop_payment_request, 0),
		(troop_set_slot, "trp_npc22", slot_troop_kingsupport_argument, argument_lords),
		(troop_set_slot, "trp_npc22", slot_troop_kingsupport_opponent, "trp_npc5"), #Sadi
 		(troop_set_slot, "trp_npc22", slot_troop_town_with_contacts, "p_town_9"), #khudan
		(troop_set_slot, "trp_npc22", slot_lord_reputation_type, lrep_roguish), #


        (store_sub, "$number_of_npc_slots", slot_troop_strings_end, slot_troop_intro),#define all npc dialogs

        (try_for_range, ":npc", companions_begin, companions_end),


            (try_for_range, ":slot_addition", 0, "$number_of_npc_slots"),
                (store_add, ":slot", ":slot_addition", slot_troop_intro),

                (store_mul, ":string_addition", ":slot_addition", 22),
                (store_add, ":string", "str_npc1_intro", ":string_addition"), 
                (val_add, ":string", ":npc"),
                (val_sub, ":string", companions_begin),

                (troop_set_slot, ":npc", ":slot", ":string"),
            (try_end),
        (try_end),
		
#Post 0907 changes begin
        (call_script, "script_add_log_entry", logent_game_start, "trp_player", -1, -1, -1),
#Post 0907 changes end

#Rebellion changes begin
        (troop_set_slot, "trp_kingdom_1_pretender",  slot_troop_original_faction, "fac_kingdom_1"),
        (troop_set_slot, "trp_kingdom_2_pretender",  slot_troop_original_faction, "fac_kingdom_2"),
        (troop_set_slot, "trp_kingdom_3_pretender",  slot_troop_original_faction, "fac_kingdom_3"),
        (troop_set_slot, "trp_kingdom_4_pretender",  slot_troop_original_faction, "fac_kingdom_4"),
        (troop_set_slot, "trp_kingdom_5_pretender",  slot_troop_original_faction, "fac_kingdom_5"),
        (troop_set_slot, "trp_kingdom_6_pretender",  slot_troop_original_faction, "fac_kingdom_6"),

#        (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_support_base,     "p_town_4"), #suno
#        (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_support_base,     "p_town_11"), #curaw
#        (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_support_base,     "p_town_18"), #town_18
#        (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_support_base,     "p_town_12"), #wercheg
#        (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_support_base,     "p_town_3"), #veluca
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
            (troop_set_slot, ":pretender", slot_lord_reputation_type, lrep_none),
        (try_end),
#Rebellion changes end
     ]),


###Here begin scripts used in necromancer branch line
###
  ("initial_necromacer_state", [      #use for initialize necromance state in the beginning of the game

     (try_for_range, ":troop_no", "trp_beheading_necromancer", "trp_reception"),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 1),
     (try_end),

     (troop_set_slot, "trp_npc2", slot_troop_teacher, "trp_beheading_necromancer"),
     (troop_set_slot, "trp_assistant_1", slot_troop_teacher, "trp_inflammation_necromancer"),
     (troop_set_slot, "trp_assistant_2", slot_troop_teacher, "trp_cyan_necromancer"),
     (troop_set_slot, "trp_assistant_3", slot_troop_teacher, "trp_armor_necromancer"),
     (troop_set_slot, "trp_assistant_4", slot_troop_teacher, "trp_power_necromancer"),
     (troop_set_slot, "trp_assistant_5", slot_troop_teacher, "trp_shadow_necromancer"),
     (troop_set_slot, "trp_assistant_6", slot_troop_teacher, "trp_element_necromancer"),
     (troop_set_slot, "trp_assistant_7", slot_troop_teacher, "trp_shower_necromancer"),
     (troop_set_slot, "trp_assistant_8", slot_troop_teacher, "trp_shattered_necromancer"),

     (troop_set_slot, "trp_apprentice_1", slot_troop_teacher, "trp_shadow_necromancer"),
     (troop_set_slot, "trp_apprentice_2", slot_troop_teacher, "trp_inflammation_necromancer"),
     (troop_set_slot, "trp_apprentice_3", slot_troop_teacher, "trp_storm_necromancer"),
     (troop_set_slot, "trp_apprentice_4", slot_troop_teacher, "trp_storm_necromancer"),
     (troop_set_slot, "trp_apprentice_5", slot_troop_teacher, "trp_defend_necromancer"),
     (troop_set_slot, "trp_apprentice_6", slot_troop_teacher, "trp_cyan_necromancer"),
     (troop_set_slot, "trp_apprentice_7", slot_troop_teacher, "trp_shadow_necromancer"),
     (troop_set_slot, "trp_apprentice_8", slot_troop_teacher, "trp_defend_necromancer"),
     (troop_set_slot, "trp_apprentice_9", slot_troop_teacher, "trp_shattered_necromancer"),
     (troop_set_slot, "trp_apprentice_10", slot_troop_teacher, "trp_power_necromancer"),
     (troop_set_slot, "trp_apprentice_11", slot_troop_teacher, "trp_power_necromancer"),
     (troop_set_slot, "trp_apprentice_12", slot_troop_teacher, "trp_cyan_necromancer"),
     (troop_set_slot, "trp_apprentice_13", slot_troop_teacher, "trp_element_necromancer"),
     (troop_set_slot, "trp_apprentice_14", slot_troop_teacher, "trp_inflammation_necromancer"),
     (troop_set_slot, "trp_apprentice_15", slot_troop_teacher, "trp_shower_necromancer"),
     (troop_set_slot, "trp_apprentice_16", slot_troop_teacher, "trp_armor_necromancer"),

     (troop_set_slot, "trp_beheading_necromancer", slot_troop_necromancer_clique, 2),    #skeleton
     (troop_set_slot, "trp_inflammation_necromancer", slot_troop_necromancer_clique, 1),    #zombie
     (troop_set_slot, "trp_cyan_necromancer", slot_troop_necromancer_clique, 2), 
     (troop_set_slot, "trp_armor_necromancer", slot_troop_necromancer_clique, 1),
     (troop_set_slot, "trp_shower_necromancer", slot_troop_necromancer_clique, 2),
     (troop_set_slot, "trp_shattered_necromancer", slot_troop_necromancer_clique, 2),
     (troop_set_slot, "trp_element_necromancer", slot_troop_necromancer_clique, 2),
     (troop_set_slot, "trp_power_necromancer", slot_troop_necromancer_clique, 1),
     (troop_set_slot, "trp_shadow_necromancer", slot_troop_necromancer_clique, 2),
     (troop_set_slot, "trp_storm_necromancer", slot_troop_necromancer_clique, 2),
     (troop_set_slot, "trp_defend_necromancer", slot_troop_necromancer_clique, 1),

     (troop_set_slot, "trp_turbid_necromancer", slot_troop_necromancer_clique, 4),             #walker

     (try_for_range, ":troop_no", "trp_knight_master_1_1", "trp_relative_of_merchants_end"),
       (troop_get_slot, ":troop_teacher", ":troop_no", slot_troop_teacher),
       (ge, ":troop_teacher", 0),
       (troop_get_slot, ":troop_teacher_clique", ":troop_teacher", slot_troop_necromancer_clique),
       (gt, ":troop_teacher_clique", 0),
       (troop_set_slot, ":troop_no", slot_troop_necromancer_clique, ":troop_teacher_clique"),
     (try_end),
     (troop_set_slot, "trp_reception", slot_troop_necromancer_clique, 4),
    ]),


##skill
##############################################################################################################
###These scripts definite troop skill
###
  ("initial_troop_skill", [

      (try_for_range, ":troop_no", "trp_player", "trp_relative_of_merchants_end"),
         (try_for_range, ":count_no", 0, 6),
            (store_add, ":slot_no", ":count_no", slot_troop_passive_skill_1),
            (troop_set_slot, ":troop_no", ":slot_no", 0),
         (try_end),
      (try_end),

#boss列表
      (troop_set_slot, "trp_boss_array", 1, "trp_starkhook_megalith_berserker"),#斯塔胡克岩雷狂战士
      (troop_set_slot, "trp_boss_array", 2, "trp_confederation_gladiator_champion"),#邦联角斗冠军
      (troop_set_slot, "trp_boss_array", 3, "trp_zela"),#泽拉
      (troop_set_slot, "trp_boss_array", 4, "trp_restless_soldier"),#无法安息的士兵
      (troop_set_slot, "trp_boss_array", 5, "trp_npc5"),#萨蒂
      (troop_set_slot, "trp_boss_array", 6, "trp_skeleton_beheader"),#猎颅军
      (troop_set_slot, "trp_boss_array", 7, "trp_mercenary_skirmisher"),#雇佣游击兵
      (troop_set_slot, "trp_boss_array", 8, "trp_libra_hitman"),#权厄之秤杀手

      (troop_set_slot, "trp_boss_scene_array", 6, "scn_village_cemetery"),#猎颅军


#农民
      (call_script, "script_set_troop_passive_skill_on", "trp_farmer", "itm_passive_stoical", 1),

#邦联角斗冠军
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_critical_attack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_fake_shield", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_damage_management", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_desperate_counterattack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_desperate_defense", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_confederation_gladiator_champion", "itm_passive_obsession_blow", 2),
      (troop_set_slot, "trp_confederation_gladiator_champion", slot_troop_active_skill_1, "itm_active_leap_attack"),#武技：跳劈
      (troop_set_slot, "trp_confederation_gladiator_champion", slot_troop_active_skill_2, "itm_active_double_slant_slash"),#武技：刃旋舞
      (troop_set_slot, "trp_confederation_gladiator_champion", slot_troop_active_skill_3, "itm_active_casual_attack"),#武技：盲击
      (troop_set_slot, "trp_confederation_gladiator_champion", slot_troop_active_skill_4, "itm_active_spinning_slash_simple"),#武技：小旋进斩
      (troop_set_slot, "trp_confederation_gladiator_champion", slot_troop_active_skill_5, "itm_active_spinning_defense_slash"),#武技：旋退反击斩
      (troop_set_slot, "trp_confederation_gladiator_champion", slot_troop_active_skill_6, "itm_active_sweep_away"),#武技：旋刃斩
#泽拉
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_critical_attack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_fake_shield", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_damage_management", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_desperate_counterattack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_desperate_defense", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_obsession_blow", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_zela", "itm_passive_inner_domination", 3),
      (troop_set_slot, "trp_zela", slot_troop_active_skill_1, "itm_active_leap_attack"),#武技：跳劈
      (troop_set_slot, "trp_zela", slot_troop_active_skill_2, "itm_active_double_slant_slash"),#武技：刃旋舞
      (troop_set_slot, "trp_zela", slot_troop_active_skill_3, "itm_active_casual_attack"),#武技：盲击
      (troop_set_slot, "trp_zela", slot_troop_active_skill_4, "itm_active_spinning_slash_simple"),#武技：小旋进斩
      (troop_set_slot, "trp_zela", slot_troop_active_skill_5, "itm_active_spinning_defense_slash"),#武技：旋退反击斩
      (troop_set_slot, "trp_zela", slot_troop_active_skill_6, "itm_active_sweep_away"),#武技：旋刃斩

#斯塔胡克佣兵
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_mercenary", "itm_passive_stoical", 2),
#斯塔胡克装甲剑士
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_swordman", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_swordman", "itm_starkhook_military_tradition", 1),
#斯塔胡克装甲骑手
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_horseman", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_horseman", "itm_passive_damage_management", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_horseman", "itm_passive_blood_arrogance", 1),
#斯塔胡克装甲弩手
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_crossbowman", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_crossbowman", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armoured_crossbowman", "itm_passive_blood_jealousy", 1),
#斯塔胡克增益佣兵
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_mercenary", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_mercenary", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_mercenary", "itm_passive_blood_boil", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_mercenary", "itm_passive_blood_defend", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_mercenary", "itm_passive_strong_vitality", 1),
#斯塔胡克佣兵队长
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_ricochet", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_blood_boil", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_blood_attack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_blood_defend", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_blood_arrogance", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_blood_jealousy", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_condottiere", "itm_passive_strong_vitality", 2),
#斯塔胡克新兵
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_recruit", "itm_passive_stoical", 2),
#斯塔胡克武装水手
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armed_sailor", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_armed_sailor", "itm_starkhook_military_tradition", 1),
#斯塔胡克船上步兵
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_onboard_infantry", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_onboard_infantry", "itm_passive_ricochet", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_onboard_infantry", "itm_starkhook_military_tradition", 1),
#斯塔胡克飞斧手
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_axe_thrower", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_axe_thrower", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_axe_thrower", "itm_passive_critical_attack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_axe_thrower", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_axe_thrower", "itm_passive_blood_arrogance", 1),
#斯塔胡克舷斗士
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_critical_attack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_blood_motivation", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_blood_attack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_blood_jealousy", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_bloodswallower", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_boat_fighter", "itm_passive_strong_vitality", 2),
#斯塔胡克增益步兵
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_warrior", "itm_passive_stoical", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_warrior", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_warrior", "itm_passive_blood_boil", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_warrior", "itm_passive_blood_defend", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_enhanced_warrior", "itm_passive_strong_vitality", 1),
#斯塔胡克狂战卫士
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_fake_shield", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_desperate_defense", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_blood_boil", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_blood_defend", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_bloodswallower", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_berserker_warrior", "itm_passive_strong_vitality", 2),
#斯塔胡克岩雷狂战士
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_fake_shield", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_damage_management", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_desperate_counterattack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_desperate_defense", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_starkhook_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_blood_churn", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_blood_motivation", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_blood_boil", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_blood_defend", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_blood_arrogance", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_blood_jealousy", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_bloodswallower", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_starkhook_megalith_berserker", "itm_passive_strong_vitality", 3),
      (troop_set_slot, "trp_starkhook_megalith_berserker", slot_troop_active_skill_1, "itm_active_blood_strike"),#武技：血星冲击
      (troop_set_slot, "trp_starkhook_megalith_berserker", slot_troop_active_skill_2, "itm_active_warcy_bloodsteel"),#血钢战吼
      (troop_set_slot, "trp_starkhook_megalith_berserker", slot_troop_active_skill_3, "itm_active_warcy_bloodburst"),#血涌战誓
      (troop_set_slot, "trp_starkhook_megalith_berserker", slot_troop_active_skill_4, "itm_active_earthsplitting_charge"),#武技：裂地猛进
      (troop_set_slot, "trp_starkhook_megalith_berserker", slot_troop_active_skill_5, "itm_active_heavy_casual_attack"),#武技：野盲击
      (troop_set_slot, "trp_starkhook_megalith_berserker", slot_troop_active_skill_6, "itm_active_warcy_red_tide"),#赤潮战誓

#打手
      (call_script, "script_set_troop_passive_skill_on", "trp_thug", "itm_passive_stoical", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_thug", "itm_passive_ricochet", 1),
#权厄之秤杀手
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_stoical", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_critical_attack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_fake_shield", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_damage_management", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_concealing", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_libra_hitman", "itm_passive_dragon_power_surging", 1),
      (troop_set_slot, "trp_libra_hitman", slot_troop_active_skill_1, "itm_active_curve_sword"),#武技：撩剑
      (troop_set_slot, "trp_libra_hitman", slot_troop_active_skill_2, "itm_active_undercover_slash"),#武技：潜身斩
      (troop_set_slot, "trp_libra_hitman", slot_troop_active_skill_3, "itm_active_spinning_assault_slash"),#武技：旋进突击斩
      (troop_set_slot, "trp_libra_hitman", slot_troop_active_skill_4, "itm_active_double_lunge"),#武技：二连穿刺
      (troop_set_slot, "trp_libra_hitman", slot_troop_active_skill_5, "itm_active_fire_throw"),#火弹投掷
      (troop_set_slot, "trp_libra_hitman", slot_troop_active_skill_6, "itm_active_wind_blade"),#风刃射击

#哀荣骑士
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_stoical", 4),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_ricochet", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_critical_attack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_critical_protection", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_fake_shield", 6),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_damage_management", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_desperate_counterattack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_desperate_defense", 4),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_powell_military_tradition", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_posthumous_knight", "itm_passive_dead_shell", 1),

#复生骷髅
      (call_script, "script_set_troop_passive_skill_on", "trp_rebirth_skeleton", "itm_passive_ricochet", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_rebirth_skeleton", "itm_passive_critical_protection", 1),
#骷髅矛兵
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_warrior", "itm_passive_stoical", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_warrior", "itm_passive_ricochet", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_warrior", "itm_passive_critical_protection", 1),
#骷髅剑士
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_swordman", "itm_passive_stoical", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_swordman", "itm_passive_ricochet", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_swordman", "itm_passive_critical_protection", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_swordman", "itm_passive_desperate_counterattack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_swordman", "itm_passive_undead_rebirth", 1),
#百战亡骸
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_ricochet", 5),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_critical_attack", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_critical_protection", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_fake_shield_penetration", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_damage_management", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_desperate_counterattack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_desperate_defense", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_experienced_skeleton", "itm_passive_undead_rebirth", 1),
#骷髅骑兵
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_rider", "itm_passive_stoical", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_rider", "itm_passive_ricochet", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_rider", "itm_passive_critical_protection", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_rider", "itm_passive_desperate_counterattack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_rider", "itm_passive_undead_rebirth", 1),
#骨环骑士
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_stoical", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_ricochet", 5),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_critical_attack", 3),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_critical_protection", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_fake_shield_penetration", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_damage_management", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_desperate_counterattack", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_desperate_defense", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_skeleton_knight", "itm_passive_undead_rebirth", 1),

#无法安息的士兵
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_passive_stoical", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_passive_ricochet", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_passive_damage_management", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_passive_desperate_counterattack", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_passive_concealing", 2),
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_passive_undead_rebirth", 1),
      (call_script, "script_set_troop_passive_skill_on", "trp_restless_soldier", "itm_powell_military_tradition", 1),
      (troop_set_slot, "trp_restless_soldier", slot_troop_active_skill_1, "itm_active_heavy_spin_chop"),#武技：重旋斩
      (troop_set_slot, "trp_restless_soldier", slot_troop_active_skill_2, "itm_active_spinning_defense_slash"),#武技：旋退反击斩
      (troop_set_slot, "trp_restless_soldier", slot_troop_active_skill_3, "itm_active_flame_sweep"),#武技：火焰横扫
      (troop_set_slot, "trp_restless_soldier", slot_troop_active_skill_4, "itm_active_fire_arrow"),#火矢射击
      (troop_set_slot, "trp_restless_soldier", slot_troop_active_skill_5, "itm_active_stone_shoot"),#地刺射击
      (troop_set_slot, "trp_restless_soldier", slot_troop_active_skill_6, "itm_active_wind_blade"),#风刃射击
  ]),


#set the action of this skill through slot
  ("initial_active_skill_information", [

     (item_set_slot, "itm_active_lunge", slot_active_skill_attacker_anim, "anim_active_lunge"),
     (item_set_slot, "itm_active_double_lunge", slot_active_skill_attacker_anim, "anim_active_double_lunge"),

     (item_set_slot, "itm_active_leap_attack", slot_active_skill_attacker_anim, "anim_active_leap_attack"),
     (item_set_slot, "itm_active_curve_sword", slot_active_skill_attacker_anim, "anim_active_curve_sword"),

     (item_set_slot, "itm_active_double_slant_slash", slot_active_skill_attacker_anim, "anim_active_double_slant_slash"),

     (item_set_slot, "itm_active_sweep_away", slot_active_skill_attacker_anim, "anim_active_sweep_away"),
     (item_set_slot, "itm_active_undercover_slash", slot_active_skill_attacker_anim, "anim_active_undercover_slash"),

     (item_set_slot, "itm_active_thump", slot_active_skill_attacker_anim, "anim_active_thump"),
     (item_set_slot, "itm_active_casual_attack", slot_active_skill_attacker_anim, "anim_active_casual_attack"),
     (item_set_slot, "itm_active_heavy_casual_attack", slot_active_skill_attacker_anim, "anim_active_heavy_casual_attack"),

     (item_set_slot, "itm_active_heavy_jump_chop", slot_active_skill_attacker_anim, "anim_active_heavy_jump_chop"),
     (item_set_slot, "itm_active_heavy_spin_chop", slot_active_skill_attacker_anim, "anim_active_heavy_spin_chop"),

     (item_set_slot, "itm_active_spinning_slash_simple", slot_active_skill_attacker_anim, "anim_active_spinning_slash_simple"),
     (item_set_slot, "itm_active_spinning_assault_slash", slot_active_skill_attacker_anim, "anim_active_spinning_assault_slash"),
     (item_set_slot, "itm_active_spinning_defense_slash", slot_active_skill_attacker_anim, "anim_active_spinning_defense_slash"),

     (item_set_slot, "itm_active_earthsplitting_charge", slot_active_skill_attacker_anim, "anim_active_earthsplitting_charge"),
     (item_set_slot, "itm_active_ground_heaving", slot_active_skill_attacker_anim, "anim_active_ground_heaving"),

     (item_set_slot, "itm_active_release_toxin_fog", slot_active_skill_attacker_anim, "anim_active_release_toxin_fog"),#释放毒雾

     (item_set_slot, "itm_active_blood_strike", slot_active_skill_attacker_anim, "anim_active_blood_strike"),#血星冲击
    ]),




########################################################新阵营系统###################################################
##
#这个脚本用于绘制兵种树。设置的兵种即为每个兵种树的起始兵种。
  ("initial_troop_root_data", [
     (try_for_range, ":troop_no", "trp_farmer", "trp_knight_master_1_1"),
        (neg|troop_is_hero, ":troop_no"),
        (store_faction_of_troop, ":faction_no", ":troop_no"),
        (faction_set_slot, ":faction_no", slot_faction_is_availiable, 1),#用于排除{!}打头和_end一类未使用的faction。
     (try_end),


##___________________________________________________________________________联合王国_________________________________________________________________________________
#联合王国通用
     (troop_set_slot, "trp_powell_peasant", slot_troop_affiliation, "itm_kingdom_1"),
     (troop_set_slot, "trp_powell_nobility", slot_troop_affiliation, "itm_kingdom_1"),
     (troop_set_slot, "trp_powell_messenger", slot_troop_affiliation, "itm_kingdom_1"),#信使
#普威尔中央
     (troop_set_slot, "trp_powell_kingcity_citizen", slot_troop_affiliation, "itm_kingdom_1_1"),
     (troop_set_slot, "trp_powell_court_nobility", slot_troop_affiliation, "itm_kingdom_1_1"),
     (troop_set_slot, "trp_crown_knight", slot_troop_affiliation, "itm_knight_order_1_1"),#王冠骑士团
     (troop_set_slot, "trp_king_spy", slot_troop_affiliation, "itm_national_knights_order"),#国家骑士团

     (troop_set_slot, "trp_tocsin_attendant", slot_troop_affiliation, "itm_tocsin_forbidden_guard"),#戒钟禁卫队
     (troop_set_slot, "trp_powell_headsman", slot_troop_affiliation, "itm_eliminater"),#肃正之镰
#罗德里格斯公国
     (troop_set_slot, "trp_red_dolphin_attendant", slot_troop_affiliation, "itm_kingdom_1_2"),
     (troop_set_slot, "trp_lesaff_armed_sailor", slot_troop_affiliation, "itm_kingdom_1_2"),
     (troop_set_slot, "trp_garcia_bodyguard", slot_troop_affiliation, "itm_kingdom_1_2"),

     (troop_set_slot, "trp_grenier_militia", slot_troop_affiliation, "itm_grenier_militia"),#戈兰尼尔民兵自卫队
     (troop_set_slot, "trp_grenier_chivalric_knight", slot_troop_affiliation, "itm_grenier_militia"),
     (troop_set_slot, "trp_trade-wind_gulf_guard", slot_troop_affiliation, "itm_holding_guard_order"),#扼守之盾

     (troop_set_slot, "trp_elemental_knight", slot_troop_affiliation, "itm_knight_order_1_2"),#元素骑士团
     (troop_set_slot, "trp_elemental_ranger", slot_troop_affiliation, "itm_knight_order_1_2"),
     (troop_set_slot, "trp_elemental_attendant", slot_troop_affiliation, "itm_knight_order_1_2"),
     (troop_set_slot, "trp_bloodfire_mercenary_corps_veteran", slot_troop_affiliation, "itm_bloodfire_mercenary_corps"),#血火佣兵团
#北境开拓领
     (troop_set_slot, "trp_northern_militia", slot_troop_affiliation, "itm_kingdom_1_3"),
     (troop_set_slot, "trp_northern_serf", slot_troop_affiliation, "itm_kingdom_1_3"),
     (troop_set_slot, "trp_dragonblood_knight", slot_troop_affiliation, "itm_knight_order_1_3"),#龙血骑士团
     (troop_set_slot, "trp_northern_hunter", slot_troop_affiliation, "itm_knight_order_1_3"),

     (troop_set_slot, "trp_brand_dragonmania", slot_troop_affiliation, "itm_dragon_prison"),#龙狱
     (troop_set_slot, "trp_extinction_tornado", slot_troop_affiliation, "itm_dragon_prison"),
     (troop_set_slot, "trp_revenge_iron_hoof", slot_troop_affiliation, "itm_hometownless_knight_order"),#无乡骑士团
#普属自由城邦
     (troop_set_slot, "trp_preist_porter", slot_troop_affiliation, "itm_kingdom_1_4"),
     (troop_set_slot, "trp_preist_noble_crossbowman", slot_troop_affiliation, "itm_kingdom_1_4"),

     (troop_set_slot, "trp_preist_knight", slot_troop_affiliation, "itm_knight_order_1_4"),#奉神骑士团
     (troop_set_slot, "trp_preist_attendant", slot_troop_affiliation, "itm_knight_order_1_4"),

     (troop_set_slot, "trp_powell_novice_divineguider", slot_troop_affiliation, "itm_powell_orthodox"),#普威尔正教
     (troop_set_slot, "trp_powell_orthodox_believer", slot_troop_affiliation, "itm_powell_orthodox"),
     (troop_set_slot, "trp_divine_swordsworn_cavalry", slot_troop_affiliation, "itm_divine_swordsworn_seminary"),#奉剑修会
#南沙公国
     (troop_set_slot, "trp_powell_rogue_farmer", slot_troop_affiliation, "itm_kingdom_1_5"),
     (troop_set_slot, "trp_araiharsa_mercenary_infantry", slot_troop_affiliation, "itm_kingdom_1_5"),

     (troop_set_slot, "trp_sandboat_knight", slot_troop_affiliation, "itm_knight_order_1_5"),#沙舟骑士团
     (troop_set_slot, "trp_sousanth_servant", slot_troop_affiliation, "itm_knight_order_1_5"),
     (troop_set_slot, "trp_gurorrion_guard", slot_troop_affiliation, "itm_gurorrion_guard"),#古洛隆卫队
#龙神教
     (troop_set_slot, "trp_dragon_power_worshipper", slot_troop_affiliation, "itm_dragon_worship"),
     (troop_set_slot, "trp_dragonhead_master", slot_troop_affiliation, "itm_dragon_worship"),
     (troop_set_slot, "trp_sedative_pavilion_nurse", slot_troop_affiliation, "itm_sedative_pavilion"),#镇静公馆
     (troop_set_slot, "trp_liminal_physician", slot_troop_affiliation, "itm_sedative_pavilion"),
#圣龙骑士团
     (troop_set_slot, "trp_holy_dragoon_knight", slot_troop_affiliation, "itm_order_of_holy_dragoon"),

##_____________________________________________________________________________公国_________________________________________________________________________________
     (troop_set_slot, "trp_yishith_inferior_elf", slot_troop_affiliation, "itm_kingdom_2"),
     (troop_set_slot, "trp_yishith_human_resident", slot_troop_affiliation, "itm_kingdom_2"),
     (troop_set_slot, "trp_yishith_messenger", slot_troop_affiliation, "itm_kingdom_2"),#信使
#灵魄之灵树
     (troop_set_slot, "trp_soul_full_elf", slot_troop_affiliation, "itm_kingdom_2_1"),
     (troop_set_slot, "trp_seddlined_thrall", slot_troop_affiliation, "itm_kingdom_2_1"),
     (troop_set_slot, "trp_soul_selected_champion", slot_troop_affiliation, "itm_kingdom_2_1"),

     (troop_set_slot, "trp_spirittree_knight", slot_troop_affiliation, "itm_knight_order_2_1"),#灵树骑士团
#死亡之灵树
     (troop_set_slot, "trp_demise_full_elf", slot_troop_affiliation, "itm_kingdom_2_2"),
     (troop_set_slot, "trp_the_composted", slot_troop_affiliation, "itm_kingdom_2_2"),
     (troop_set_slot, "trp_demise_selected_champion", slot_troop_affiliation, "itm_kingdom_2_2"),

     (troop_set_slot, "trp_spiritrain_ranger", slot_troop_affiliation, "itm_knight_order_2_2"),#灵雨游侠团
#先祖之灵树
     (troop_set_slot, "trp_ancester_full_elf", slot_troop_affiliation, "itm_kingdom_2_3"),
     (troop_set_slot, "trp_immortal_seeker", slot_troop_affiliation, "itm_kingdom_2_3"),
     (troop_set_slot, "trp_ancester_selected_champion", slot_troop_affiliation, "itm_kingdom_2_3"),

     (troop_set_slot, "trp_immortal_assassin", slot_troop_affiliation, "itm_knight_order_2_3"),#永世者刺客团

     (troop_set_slot, "trp_half_molter", slot_troop_affiliation, "itm_molter_legion"),#蜕生者战团
     (troop_set_slot, "trp_molting_failer", slot_troop_affiliation, "itm_great_apple_garden"),#嘉果园
#生命之灵树
     (troop_set_slot, "trp_vita_full_elf", slot_troop_affiliation, "itm_kingdom_2_4"),
     (troop_set_slot, "trp_vita_selected_champion", slot_troop_affiliation, "itm_kingdom_2_4"),

     (troop_set_slot, "trp_spiritwind_bowcavalry", slot_troop_affiliation, "itm_knight_order_2_4"),#灵风游骑团

     (troop_set_slot, "trp_yishith_armed_sailor", slot_troop_affiliation, "itm_yishith_westcoast_militia"),#伊希斯人类西海自警团
     (troop_set_slot, "trp_yishith_recruiting_rider", slot_troop_affiliation, "itm_yishith_westcoast_militia"),
     (troop_set_slot, "trp_yishith_chivalric_knight", slot_troop_affiliation, "itm_yishith_westcoast_militia"),

     (troop_set_slot, "trp_snow_trading_company_guard", slot_troop_affiliation, "itm_snow_trading_company"),#雪泥商会

##_____________________________________________________________________________酋长国_________________________________________________________________________________
     (troop_set_slot, "trp_kouruto_stray_therianthropy", slot_troop_affiliation, "itm_kingdom_3"),
     (troop_set_slot, "trp_kouruto_messenger", slot_troop_affiliation, "itm_kingdom_3"),#信使
#图腾同盟
     (troop_set_slot, "trp_kouruto_tiger_herdsman", slot_troop_affiliation, "itm_kingdom_3_1"),
     (troop_set_slot, "trp_kouruto_bear_herdsman", slot_troop_affiliation, "itm_kingdom_3_1"),
     (troop_set_slot, "trp_kouruto_wolf_herdsman", slot_troop_affiliation, "itm_kingdom_3_1"),
     (troop_set_slot, "trp_kouruto_lion_therianthropy", slot_troop_affiliation, "itm_kingdom_3_1"),

     (troop_set_slot, "trp_kouruto_gladiator", slot_troop_affiliation, "itm_knight_order_3_1"),#科鲁托剑斗旅团
     (troop_set_slot, "trp_totem_champion_warrior", slot_troop_affiliation, "itm_knight_order_3_1"),

     (troop_set_slot, "trp_kouruto_therianthropy_guardian", slot_troop_affiliation, "itm_ironpeak_garrison_brigade"),#铁峰守备旅团
     (troop_set_slot, "trp_kouruto_human_guardian", slot_troop_affiliation, "itm_ironpeak_garrison_brigade"),
     (troop_set_slot, "trp_ironbite_gang_freshman", slot_troop_affiliation, "itm_ironbite_gang"),#啮铁帮
     (troop_set_slot, "trp_ferrophaeg_beast", slot_troop_affiliation, "itm_ironbite_gang"),

     (troop_set_slot, "trp_furnace_watch_recruit", slot_troop_affiliation, "itm_furnace_watch_brigade"),#洪炉监视旅团
     (troop_set_slot, "trp_furnace_hunter", slot_troop_affiliation, "itm_furnace_watch_brigade"),

     (troop_set_slot, "trp_kouruto_human_settler", slot_troop_affiliation, "itm_kouruto_auxiliary"),
#麦汗族
     (troop_set_slot, "trp_kouruto_cow_herdsman", slot_troop_affiliation, "itm_kingdom_3_2"),
     (troop_set_slot, "trp_kouruto_sheep_herdsman", slot_troop_affiliation, "itm_kingdom_3_2"),
     (troop_set_slot, "trp_kouruto_deer_herdsman", slot_troop_affiliation, "itm_kingdom_3_2"),
     (troop_set_slot, "trp_kouruto_rabbit_herdsman", slot_troop_affiliation, "itm_kingdom_3_2"),

     (troop_set_slot, "trp_kouruto_novice_shaman", slot_troop_affiliation, "itm_fireside_circle_of_shaman"),#炉边萨满联盟
     (troop_set_slot, "trp_furnace_hierophant", slot_troop_affiliation, "itm_fireside_circle_of_shaman"),
#金爪子帮
     (troop_set_slot, "trp_kouruto_fox_herdsman", slot_troop_affiliation, "itm_kingdom_3_3"),
     (troop_set_slot, "trp_kouruto_cat_herdsman", slot_troop_affiliation, "itm_kingdom_3_3"),

     (troop_set_slot, "trp_kouruto_therianthropy_caravan_guard", slot_troop_affiliation, "itm_goldclaw_guild"),#金爪子商会
     (troop_set_slot, "trp_therianthropy_undead_hunter", slot_troop_affiliation, "itm_undead_slayer_brigade"),#不死者猎杀旅团
#守望派
     (troop_set_slot, "trp_kouruto_dog_herdsman", slot_troop_affiliation, "itm_kingdom_3_4"),
     (troop_set_slot, "trp_sentinel_bastion_warden", slot_troop_affiliation, "itm_knight_order_3_2"),#守望者卫戍旅团
     (troop_set_slot, "trp_sentinel_servant", slot_troop_affiliation, "itm_knight_order_3_2"),

##_____________________________________________________________________________邦联_________________________________________________________________________________
     (troop_set_slot, "trp_confederation_serf", slot_troop_affiliation, "itm_kingdom_4"),
     (troop_set_slot, "trp_confederation_serf_warrior", slot_troop_affiliation, "itm_kingdom_4"),
     (troop_set_slot, "trp_confederation_messenger", slot_troop_affiliation, "itm_kingdom_4"),#信使
#黑沼议事会
     (troop_set_slot, "trp_diemer_freeman", slot_troop_affiliation, "itm_kingdom_4_1"),
     (troop_set_slot, "trp_diemer_young_slaveholder", slot_troop_affiliation, "itm_kingdom_4_1"),

     (troop_set_slot, "trp_optihazation_scholar", slot_troop_affiliation, "itm_knight_order_4_1"),#光瘴学派
     (troop_set_slot, "trp_optihazation_adventure_knight", slot_troop_affiliation, "itm_knight_order_4_1"),
     (troop_set_slot, "trp_diemer_hired_adventurer", slot_troop_affiliation, "itm_knight_order_4_1"),
     (troop_set_slot, "trp_god_raiser_knight", slot_troop_affiliation, "itm_lord_of_myriad_altars"),#万龛之主
     (troop_set_slot, "trp_god_raiser_throne", slot_troop_affiliation, "itm_lord_of_myriad_altars"),

     (troop_set_slot, "trp_confederation_slave_trainer", slot_troop_affiliation, "itm_slave_bureau"),#司奴局
     (troop_set_slot, "trp_confederation_new_recruit", slot_troop_affiliation, "itm_marsh_flower_landsknechts"),#暗沼之花佣兵团
     (troop_set_slot, "trp_confederation_hiring_conjurer", slot_troop_affiliation, "itm_marsh_flower_landsknechts"),
     (troop_set_slot, "trp_marsh_flower_camp_woman", slot_troop_affiliation, "itm_marsh_flower_landsknechts"),
#乌尔之子女
     (troop_set_slot, "trp_confederation_fishing_serf", slot_troop_affiliation, "itm_kingdom_4_2"),
     (troop_set_slot, "trp_confederation_toxin_dealer", slot_troop_affiliation, "itm_kingdom_4_2"),
     (troop_set_slot, "trp_marsh_deepone_freeman", slot_troop_affiliation, "itm_kingdom_4_2"),
     (troop_set_slot, "trp_dreadmarsh_knight", slot_troop_affiliation, "itm_kingdom_4_2"),

     (troop_set_slot, "trp_deep_dread_assassin", slot_troop_affiliation, "itm_dread_of_the_deep"),#深海恐惧刺客团
     (troop_set_slot, "trp_rip_current_blade", slot_troop_affiliation, "itm_dread_of_the_deep"),
     (troop_set_slot, "trp_deep_binder_veteran", slot_troop_affiliation, "itm_deep_binder"),#深邃封印团
     (troop_set_slot, "trp_deep_bishop", slot_troop_affiliation, "itm_deep_binder"),
#净世军
     (troop_set_slot, "trp_confederation_armed_faithful", slot_troop_affiliation, "itm_kingdom_4_3"),
     (troop_set_slot, "trp_purifier_pastor", slot_troop_affiliation, "itm_kingdom_4_3"), 

     (troop_set_slot, "trp_divinecusp_knight", slot_troop_affiliation, "itm_knight_order_4_2"),#神牙修道军
     (troop_set_slot, "trp_divinecusp_knight_captain", slot_troop_affiliation, "itm_knight_order_4_2"),
     (troop_set_slot, "trp_storm_servant", slot_troop_affiliation, "itm_knight_order_4_2"),
     (troop_set_slot, "trp_suffering_friar", slot_troop_affiliation, "itm_eagle_saint_hardship_seminary"),#鹰圣苦修会
     (troop_set_slot, "trp_deceasing_eagle", slot_troop_affiliation, "itm_eagle_saint_hardship_seminary"),
#食莲人沙龙
     (troop_set_slot, "trp_ankiya_civilized_barbarian", slot_troop_affiliation, "itm_kingdom_4_4"),
     (troop_set_slot, "trp_ankiya_naturalized_noble", slot_troop_affiliation, "itm_kingdom_4_4"), 
#人类狩猎者
     (troop_set_slot, "trp_confederation_slave_catcher_hitman", slot_troop_affiliation, "itm_human_hunter"),
     (troop_set_slot, "trp_venery_slaver", slot_troop_affiliation, "itm_human_hunter"),
     (troop_set_slot, "trp_venery_knight", slot_troop_affiliation, "itm_human_hunter"),

##_____________________________________________________________________________教皇国_________________________________________________________________________________
     (troop_set_slot, "trp_papal_citizen", slot_troop_affiliation, "itm_kingdom_5"),
     (troop_set_slot, "trp_church_fresh_trainee", slot_troop_affiliation, "itm_kingdom_5"),
     (troop_set_slot, "trp_mission_school_student", slot_troop_affiliation, "itm_kingdom_5"),
     (troop_set_slot, "trp_papal_hunter", slot_troop_affiliation, "itm_kingdom_5"),
     (troop_set_slot, "trp_papal_devout_noble", slot_troop_affiliation, "itm_kingdom_5"),
     (troop_set_slot, "trp_godward_swordman", slot_troop_affiliation, "itm_kingdom_5"),
     (troop_set_slot, "trp_papal_messenger", slot_troop_affiliation, "itm_kingdom_5"),#信使
#圣廷
     (troop_set_slot, "trp_blesruth_tzaddiq", slot_troop_affiliation, "itm_kingdom_5_1"),
     (troop_set_slot, "trp_holy_see_bedrock", slot_troop_affiliation, "itm_kingdom_5_1"),
     (troop_set_slot, "trp_cardinal_guard", slot_troop_affiliation, "itm_kingdom_5_1"),
     (troop_set_slot, "trp_great_sword_church_guard", slot_troop_affiliation, "itm_kingdom_5_1"),

     (troop_set_slot, "trp_holy_knight", slot_troop_affiliation, "itm_order_of_holy_knight"),#圣骑士团
     (troop_set_slot, "trp_holy_knight_aide", slot_troop_affiliation, "itm_order_of_holy_knight"),

     (troop_set_slot, "trp_pontiff_knight", slot_troop_affiliation, "itm_knight_order_5_1"),#宗座骑士团
     (troop_set_slot, "trp_marten_honor_guard", slot_troop_affiliation, "itm_knight_order_5_1"),

     (troop_set_slot, "trp_godward_swordman", slot_troop_affiliation, "itm_order_of_godward_warrior"),#圣誓剑勇团
     (troop_set_slot, "trp_eternal_rest_warden", slot_troop_affiliation, "itm_eternal_galleries"),#永眠回廊
     (troop_set_slot, "trp_crazy_coffin_warden", slot_troop_affiliation, "itm_eternal_galleries"),
     (troop_set_slot, "trp_holy_foolishness", slot_troop_affiliation, "itm_eternal_galleries"),
     (troop_set_slot, "trp_holy_city_sentry", slot_troop_affiliation, "itm_legacy_of_the_bow_saint"),#弓圣遗泽射手团
#证信宗
     (troop_set_slot, "trp_civilian_exorcist", slot_troop_affiliation, "itm_kingdom_5_2"),

     (troop_set_slot, "trp_reaper_Knight", slot_troop_affiliation, "itm_knight_order_5_2"),#狩魔骑士团
     (troop_set_slot, "trp_reaper_Knight_captain", slot_troop_affiliation, "itm_knight_order_5_2"),
     (troop_set_slot, "trp_heretic_hunter", slot_troop_affiliation, "itm_heretic_killer"),#异端猎手队
     (troop_set_slot, "trp_heretic_killer", slot_troop_affiliation, "itm_heretic_killer"),

     (troop_set_slot, "trp_trial_servant", slot_troop_affiliation, "itm_religious_trial_bureau"),#宗教审判局
     (troop_set_slot, "trp_accused_believer", slot_troop_affiliation, "itm_sin_slave_legion"),#戴罪信众
     (troop_set_slot, "trp_hyena_knight", slot_troop_affiliation, "itm_sin_slave_legion"),
     (troop_set_slot, "trp_devouring_sin_friar", slot_troop_affiliation, "itm_sect_of_devouring_sin"),#噬罪秘修会
     (troop_set_slot, "trp_martyrs_of_deep_crimes", slot_troop_affiliation, "itm_sect_of_devouring_sin"),
#真信施洗会
     (troop_set_slot, "trp_divine_legion_veteran", slot_troop_affiliation, "itm_kingdom_5_3"),
     (troop_set_slot, "trp_divine_legion_veteran_knight", slot_troop_affiliation, "itm_kingdom_5_3"),
     (troop_set_slot, "trp_powell_baptized_infantry", slot_troop_affiliation, "itm_kingdom_5_3"),
     (troop_set_slot, "trp_yishith_baptized_half_elf", slot_troop_affiliation, "itm_kingdom_5_3"),

     (troop_set_slot, "trp_patron_knight", slot_troop_affiliation, "itm_knight_order_5_3"),#庇护骑士团
     (troop_set_slot, "trp_patron_warrior", slot_troop_affiliation, "itm_knight_order_5_3"),
     (troop_set_slot, "trp_chaney_rider", slot_troop_affiliation, "itm_chaney_cavalry_army"),#查尼枪骑兵团

     (troop_set_slot, "trp_baptism_elite_crossbowman", slot_troop_affiliation, "itm_sutton_guard"),#萨顿卫队
     (troop_set_slot, "trp_baptism_archer_captain", slot_troop_affiliation, "itm_sutton_guard"),

     (troop_set_slot, "trp_shield_drawer", slot_troop_affiliation, "itm_shield_drawing_man"),#绘盾人
     (troop_set_slot, "trp_divine_legion_insane_infantry", slot_troop_affiliation, "itm_shield_drawing_man"),
     (troop_set_slot, "trp_shield_angel", slot_troop_affiliation, "itm_shield_drawing_man"),
#神哲修道宗
     (troop_set_slot, "trp_armed_female_believer", slot_troop_affiliation, "itm_kingdom_5_4"),
     (troop_set_slot, "trp_whitspring_chaplain", slot_troop_affiliation, "itm_kingdom_5_4"),

     (troop_set_slot, "trp_arcane_knight", slot_troop_affiliation, "itm_knight_order_5_4"),#奥术骑士团
     (troop_set_slot, "trp_arcane_knight_captain", slot_troop_affiliation, "itm_knight_order_5_4"),

     (troop_set_slot, "trp_philosophical_egg_scholar", slot_troop_affiliation, "itm_egg_of_philosophy_school"),#哲学之卵学派
     (troop_set_slot, "trp_logos_prophet", slot_troop_affiliation, "itm_egg_of_philosophy_school"),
#圣别渴求者
     (troop_set_slot, "trp_armed_pilgrim", slot_troop_affiliation, "itm_kingdom_5_5"),
     (troop_set_slot, "trp_papal_zealot", slot_troop_affiliation, "itm_kingdom_5_5"),
     (troop_set_slot, "trp_living_saint", slot_troop_affiliation, "itm_kingdom_5_5"),

     (troop_set_slot, "trp_hymn_knight", slot_troop_affiliation, "itm_knight_order_5_5"),#圣歌骑士团
     (troop_set_slot, "trp_hymn_knight_captain", slot_troop_affiliation, "itm_knight_order_5_5"),
     (troop_set_slot, "trp_holy_church_guard", slot_troop_affiliation, "itm_knight_order_5_5"),

     (troop_set_slot, "trp_sanctification_trader", slot_troop_affiliation, "itm_holy_scar_chamber_of_commerce"),#圣痕商会

     (troop_set_slot, "trp_holy_box_collector", slot_troop_affiliation, "itm_holy_picking_man"),#剔圣人
     (troop_set_slot, "trp_sage_slayer", slot_troop_affiliation, "itm_holy_picking_man"),

##_____________________________________________________________________________龙树_________________________________________________________________________________
     (troop_set_slot, "trp_longshu_zhengzu", slot_troop_affiliation, "itm_kingdom_6"),
     (troop_set_slot, "trp_longshu_eunuch", slot_troop_affiliation, "itm_kingdom_6"),
     (troop_set_slot, "trp_longshu_gulamu", slot_troop_affiliation, "itm_kingdom_6"),
     (troop_set_slot, "trp_longshu_messenger", slot_troop_affiliation, "itm_kingdom_6"),#信使

##___________________________________________________________________________大公国_________________________________________________________________________________
#公国通用
     (troop_set_slot, "trp_starkhook_recruit", slot_troop_affiliation, "itm_kingdom_7"),
     (troop_set_slot, "trp_starkhook_business_armed_captain", slot_troop_affiliation, "itm_kingdom_7"),
     (troop_set_slot, "trp_starkhook_messenger", slot_troop_affiliation, "itm_kingdom_7"),#信使
#白塔党
     (troop_set_slot, "trp_starkhook_tower_noble", slot_troop_affiliation, "itm_kingdom_7_1"),
     (troop_set_slot, "trp_bloodburst_servant", slot_troop_affiliation, "itm_kingdom_7_1"),
     (troop_set_slot, "trp_blood_sinner", slot_troop_affiliation, "itm_kingdom_7_1"),
     (troop_set_slot, "trp_starkhook_throwing_axe_ranger", slot_troop_affiliation, "itm_kingdom_7_1"),
     (troop_set_slot, "trp_starkhook_throwing_axe_master", slot_troop_affiliation, "itm_kingdom_7_1"),

     (troop_set_slot, "trp_bloodhonor_guard", slot_troop_affiliation, "itm_knight_order_7_1"),#血勋铁卫队
     (troop_set_slot, "trp_light_bloodhonor_guard", slot_troop_affiliation, "itm_knight_order_7_1"),
     (troop_set_slot, "trp_bloodhonor_guard_captain", slot_troop_affiliation, "itm_knight_order_7_1"),

     (troop_set_slot, "trp_blood_lake_sentry", slot_troop_affiliation, "itm_blood_lake_court"),#血湖之庭
     (troop_set_slot, "trp_crimson_berserker", slot_troop_affiliation, "itm_blood_lake_court"),

     (troop_set_slot, "trp_blood_extinguisher", slot_troop_affiliation, "itm_blood_hunter"),#戒血执法者
     (troop_set_slot, "trp_starkhook_shield_woman", slot_troop_affiliation, "itm_blocked_fortress"),#闭锁之堡
#斯塔胡克商业联盟
     (troop_set_slot, "trp_starkhook_commercial_nobility", slot_troop_affiliation, "itm_kingdom_7_2"),
     (troop_set_slot, "trp_starkhook_business_association_rider", slot_troop_affiliation, "itm_kingdom_7_2"),
     (troop_set_slot, "trp_blood_can_slave", slot_troop_affiliation, "itm_kingdom_7_2"),

     (troop_set_slot, "trp_red_moon_knight", slot_troop_affiliation, "itm_knight_order_of_scarlet_full_moon"),#猩红满月骑士团
     (troop_set_slot, "trp_crimson_war_mage", slot_troop_affiliation, "itm_knight_order_of_scarlet_full_moon"),
#蛇夫党
     (troop_set_slot, "trp_abyss_mercenary", slot_troop_affiliation, "itm_kingdom_7_3"),

##___________________________________________________________________________自由城邦_________________________________________________________________________________
     (troop_set_slot, "trp_citizen_pauper", slot_troop_affiliation, "itm_kingdom_8"),
     (troop_set_slot, "trp_states_civilian", slot_troop_affiliation, "itm_kingdom_8"),
     (troop_set_slot, "trp_states_nobility", slot_troop_affiliation, "itm_kingdom_8"),
     (troop_set_slot, "trp_citizen_messenger", slot_troop_affiliation, "itm_kingdom_8"),#信使
#权杖下马骑士团
     (troop_set_slot, "trp_scepter_dismounted_knight", slot_troop_affiliation, "itm_knight_order_8_1"),
     (troop_set_slot, "trp_scepter_knight_captain", slot_troop_affiliation, "itm_knight_order_8_1"),
#裁决之锤
     (troop_set_slot, "trp_exorcism_novice", slot_troop_affiliation, "itm_hammer_of_judgment"),
     (troop_set_slot, "trp_judgment_knight", slot_troop_affiliation, "itm_hammer_of_judgment"),
#归宗派
     (troop_set_slot, "trp_guilio_vamp", slot_troop_affiliation, "itm_guilio_vamp"),#古力奥妖妇团
#西求派
     (troop_set_slot, "trp_skytear_sniper", slot_troop_affiliation, "itm_skytear_sniper_army"),#裂空狙击团
#愚人派
     (troop_set_slot, "trp_sheriff_rider", slot_troop_affiliation, "itm_kingdom_8_3"),

##___________________________________________________________________________权厄之秤_________________________________________________________________________________
     (troop_set_slot, "trp_thug", slot_troop_affiliation, "itm_libra"),
     (troop_set_slot, "trp_libra_smuggler", slot_troop_affiliation, "itm_libra"),
     (troop_set_slot, "trp_libra_knight", slot_troop_affiliation, "itm_libra"),
#勒塞夫区的分舵
     (troop_set_slot, "trp_black_candle_mistress", slot_troop_affiliation, "itm_black_candle_gang"),
     (troop_set_slot, "trp_splitting_sailor", slot_troop_affiliation, "itm_splitting_sail_brotherhood"),

##___________________________________________________________________________法外骑士_________________________________________________________________________________
     (troop_set_slot, "trp_roving_bandits", slot_troop_affiliation, "itm_robber_knight"),

     (troop_set_slot, "trp_powell_rogue_attendant", slot_troop_affiliation, "itm_robber_knight"),
     (troop_set_slot, "trp_rodriguez_rogue_attendant", slot_troop_affiliation, "itm_robber_knight"),
     (troop_set_slot, "trp_city_rogue_attendant", slot_troop_affiliation, "itm_robber_knight"),

##__________________________________________________________________________科鲁托浪民_________________________________________________________________________________
     (troop_set_slot, "trp_steppe_bandit", slot_troop_affiliation, "itm_kouruto_refugee"),

##___________________________________________________________________________海渊异种_________________________________________________________________________________
     (troop_set_slot, "trp_abyssal_sailor", slot_troop_affiliation, "itm_ankiya_barbarian"),

##__________________________________________________________________________安基亚蛮族_________________________________________________________________________________
     (troop_set_slot, "trp_taiga_bandit", slot_troop_affiliation, "itm_ankiya_barbarian"),

##__________________________________________________________________________热砂的末裔_________________________________________________________________________________
     (troop_set_slot, "trp_desert_bandit", slot_troop_affiliation, "itm_desertus_bandit"),

##_____________________________________________________________________________魔族_________________________________________________________________________________
     (troop_set_slot, "trp_the_forsaken", slot_troop_affiliation, "itm_devil_worshipper"),
     (troop_set_slot, "trp_demon_corruptor", slot_troop_affiliation, "itm_demonic_corruptor"),

##___________________________________________________________________________不死者_________________________________________________________________________________
     (troop_set_slot, "trp_junto_member", slot_troop_affiliation, "itm_undead_association"),

     (troop_set_slot, "trp_nercosteel_shieldward_sergeant", slot_troop_affiliation, "itm_beheading_necromancer"),
     (troop_set_slot, "trp_umbrashot_marksman_sergeant", slot_troop_affiliation, "itm_beheading_necromancer"),
     (troop_set_slot, "trp_foulshadow_sprinter_sergeant", slot_troop_affiliation, "itm_beheading_necromancer"),
     (troop_set_slot, "trp_deathdam_extraditer", slot_troop_affiliation, "itm_beheading_necromancer"),
     (troop_set_slot, "trp_skull_collector", slot_troop_affiliation, "itm_beheading_necromancer"),
     (troop_set_slot, "trp_rita_zenIs_hound", slot_troop_affiliation, "itm_beheading_necromancer"),
     (troop_set_slot, "trp_agouti_faceless_shooter", slot_troop_affiliation, "itm_agouti_commerce_chamber"),

     (troop_set_slot, "trp_low_grade_zombie", slot_troop_affiliation, "itm_zombie_clique"),
     (troop_set_slot, "trp_zombie_king_warrior", slot_troop_affiliation, "itm_power_necromancer"),
     (troop_set_slot, "trp_resurgam_knight", slot_troop_affiliation, "itm_power_necromancer"),
     (troop_set_slot, "trp_undead_gladiatus", slot_troop_affiliation, "itm_power_necromancer"),
     (troop_set_slot, "trp_zombie_armed_infantry", slot_troop_affiliation, "itm_armor_necromancer"),
     (troop_set_slot, "trp_therianthropy_zombie", slot_troop_affiliation, "itm_defend_necromancer"),

     (troop_set_slot, "trp_rebirth_skeleton", slot_troop_affiliation, "itm_skeleton_clique"),
     (troop_set_slot, "trp_fragmented_dragonbone_guardian", slot_troop_affiliation, "itm_element_necromancer"),
     (troop_set_slot, "trp_dragonfang_lancer", slot_troop_affiliation, "itm_element_necromancer"),
     (troop_set_slot, "trp_dragonclaw_assassin", slot_troop_affiliation, "itm_element_necromancer"),
     (troop_set_slot, "trp_unburned_bones", slot_troop_affiliation, "itm_inflammation_necromancer"),
     (troop_set_slot, "trp_curse_carrier", slot_troop_affiliation, "itm_shower_necromancer"),
     (troop_set_slot, "trp_elf_skeleton", slot_troop_affiliation, "itm_shower_necromancer"),
     (troop_set_slot, "trp_kouruto_wild_hunter_cavalry", slot_troop_affiliation, "itm_storm_necromancer"),

     (troop_set_slot, "trp_poltergeist", slot_troop_affiliation, "itm_fantom_clique"),
     (troop_set_slot, "trp_phantom_rider", slot_troop_affiliation, "itm_shattered_necromancer"),
     (troop_set_slot, "trp_backstabber", slot_troop_affiliation, "itm_shadow_necromancer"),
     (troop_set_slot, "trp_shadow_assassin", slot_troop_affiliation, "itm_shadow_necromancer"),
     (troop_set_slot, "trp_qingqiu_nagzul", slot_troop_affiliation, "itm_cyan_necromancer"),
     (troop_set_slot, "trp_devil_bride", slot_troop_affiliation, "itm_cyan_necromancer"),

     (troop_set_slot, "trp_new_walker", slot_troop_affiliation, "itm_walker_clique"),
     (troop_set_slot, "trp_submerge_knight", slot_troop_affiliation, "itm_walker_clique"),

##___________________________________________________________________________巫蛊世家_________________________________________________________________________________
     (troop_set_slot, "trp_witchcraft_trainee", slot_troop_affiliation, "itm_witchcraft_aristocrat"),

##___________________________________________________________________________拜星教_________________________________________________________________________________
     (troop_set_slot, "trp_sabianist", slot_troop_affiliation, "itm_sabianism"),

##__________________________________________________________________________赤铜孑遗_________________________________________________________________________________

##___________________________________________________________________________金瘾症_________________________________________________________________________________

##_________________________________________________________________________丧钟刺客团_________________________________________________________________________________
     (troop_set_slot, "trp_primary_killer", slot_troop_affiliation, "itm_deathbell"),
     (troop_set_slot, "trp_female_killer", slot_troop_affiliation, "itm_deathbell"),

##_________________________________________________________________________冒险者协会_________________________________________________________________________________
     (troop_set_slot, "trp_blackiron_adventurer", slot_troop_affiliation, "itm_adventurers_association"),
     (troop_set_slot, "trp_gold_adventurer", slot_troop_affiliation, "itm_adventurers_association"),
     (troop_set_slot, "trp_mithril_adventurer", slot_troop_affiliation, "itm_adventurers_association"),
     (troop_set_slot, "trp_orichalcos_adventurer", slot_troop_affiliation, "itm_adventurers_association"),
     (troop_set_slot, "trp_primordite_adventurer", slot_troop_affiliation, "itm_adventurers_association"),

     (troop_set_slot, "trp_association_footman", slot_troop_affiliation, "itm_adventurers_association"),
     (troop_set_slot, "trp_association_shade", slot_troop_affiliation, "itm_adventurers_association"),
     (troop_set_slot, "trp_association_examiner", slot_troop_affiliation, "itm_adventurers_association"),

##___________________________________________________________________________边缘人_________________________________________________________________________________
     (troop_set_slot, "trp_blackguard_mercenary", slot_troop_affiliation, "itm_outlawers"),

##___________________________________________________________________________自生者_________________________________________________________________________________
#龙孽
     (troop_set_slot, "trp_dragonmania", slot_troop_affiliation, "itm_dragon_abomination"),
#绯世
     (troop_set_slot, "trp_crimson_residual", slot_troop_affiliation, "itm_crimson_world"),
     (troop_set_slot, "trp_blood_pool_phantom", slot_troop_affiliation, "itm_crimson_world"),
     (troop_set_slot, "trp_blood_sea_raven", slot_troop_affiliation, "itm_crimson_world"),
     (troop_set_slot, "trp_red_dream_shadow", slot_troop_affiliation, "itm_crimson_world"),
     (troop_set_slot, "trp_blood_moon_birth_one", slot_troop_affiliation, "itm_crimson_world"),
#缪史
     (troop_set_slot, "trp_restless_soldier", slot_troop_affiliation, "itm_erroneous_history"),

##___________________________________________________________________________庸众凡夫_________________________________________________________________________________
     (troop_set_slot, "trp_farmer", slot_troop_affiliation, "itm_normal_people"),
     (troop_set_slot, "trp_townsman", slot_troop_affiliation, "itm_normal_people"),
     (troop_set_slot, "trp_watchman", slot_troop_affiliation, "itm_normal_people"),


#兵种界面展示的动作姿势
     (troop_set_slot, "trp_eternalflame_unburned_one", slot_troop_window_animation , "anim_powerhouse_position_1"),
     (troop_set_slot, "trp_church_guard", slot_troop_window_animation , "anim_powerhouse_position_2"),
     (troop_set_slot, "trp_hyena_knight", slot_troop_window_animation , "anim_powerhouse_position_3"),
     (troop_set_slot, "trp_papal_zealot", slot_troop_window_animation , "anim_powerhouse_position_4"),
     (troop_set_slot, "trp_blood_sea_raven", slot_troop_window_animation , "anim_powerhouse_position_5"),
     (troop_set_slot, "trp_red_dream_shadow", slot_troop_window_animation , "anim_powerhouse_position_6"),
     (troop_set_slot, "trp_blood_moon_birth_one", slot_troop_window_animation , "anim_powerhouse_position_7"),
     (troop_set_slot, "trp_swaybacked_monk", slot_troop_window_animation , "anim_powerhouse_position_8"),
     (troop_set_slot, "trp_deceasing_eagle", slot_troop_window_animation , "anim_powerhouse_position_8"),

     (troop_set_slot, "trp_brand_dragonmania", slot_troop_window_animation , "anim_powerhouse_position_9"),
     (troop_set_slot, "trp_brand_dragonfrenzy", slot_troop_window_animation , "anim_powerhouse_position_9"),
     (troop_set_slot, "trp_brand_dragon_abomination", slot_troop_window_animation , "anim_powerhouse_position_9"),
     (troop_set_slot, "trp_extinction_tornado", slot_troop_window_animation , "anim_powerhouse_position_9"),


#私兵
     #普威尔联合王国
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_1_lord", "trp_holy_dragoon_knight", 2, 6, 1), #国王克罗龙斯七世的1号私兵圣龙骑士
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_1_lord", "trp_crown_knight", 4, 120, 2), #国王克罗龙斯七世的2号私兵王冠骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_17", "trp_eliminater_sergeant", 3, 15, 1), #拉法齐·雷克斯伯爵的1号私兵肃正军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_17", "trp_powell_executioner", 2, 18, 2), #拉法齐·雷克斯伯爵的2号私兵普威尔行刑官
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_50", "trp_powell_great_swordman", 2, 20, 1), #多纳塔斯·杜波依斯侯爵的1号私兵普威尔大剑师
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_50", "trp_dragon_power_great_swordman", 1, 8, 2), #多纳塔斯·杜波依斯侯爵的2号私兵龙力大剑师
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_42", "trp_powell_court_knight", 4, 24, 1), #歌德弗鲁瓦·文森伯爵的1号私兵普威尔内府骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_42", "trp_powell_sword_cavalry", 6, 60, 2), #歌德弗鲁瓦·文森伯爵的2号私兵普威尔剑骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_44", "trp_powell_halberd_cavalry", 6, 60, 1), #佐尔·高提耶侯爵的1号私兵普威尔戟骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_44", "trp_powell_halberd_infantry", 2, 20, 2), #佐尔·高提耶侯爵的2号私兵普威尔戟兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_45", "trp_crown_knight", 2, 12, 1), #基文·马丁内兹伯爵的1号私兵王冠骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_45", "trp_king_spy", 8, 64, 2), #基文·马丁内兹伯爵的2号私兵普威尔密探
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_46", "trp_eliminater_knight", 3, 9, 1), #罗纳尔·舍瓦利侯爵的1号私兵肃正骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_46", "trp_eliminater_vanguard", 5, 40, 2), #罗纳尔·舍瓦利侯爵的2号私兵肃正尖兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_47", "trp_crown_knight", 2, 12, 1), #拉吉夫·勒罗伊伯爵的1号私兵王冠骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_47", "trp_powell_praetorian", 6, 30, 2), #拉吉夫·勒罗伊伯爵的2号私兵普威尔贵族禁卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_15", "trp_crown_knight", 2, 10, 1), #雷蒙·希尔顿侯爵的1号私兵王冠骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_15", "trp_powell_orthodox_zealot", 15, 105, 2), #雷蒙·希尔顿侯爵的2号私兵普威尔正教狂信徒
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_34", "trp_eliminater_recruit", 7, 63, 1), #伊冯娜·希尔顿勋爵的1号私兵肃正新兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_43", "trp_crown_knight", 2, 10, 1), #纪晓姆·杜朋伯爵的1号私兵王冠骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_43", "trp_grenier_longbow_archer", 10, 60, 2), #纪晓姆·杜朋伯爵的2号私兵戈兰尼尔长弓手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_19", "trp_powell_sword_cavalry", 6, 48, 1), #加布里埃勒·迪斯平子爵的1号私兵普威尔剑骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_48", "trp_powell_court_knight", 3, 18, 1), #玛尼翁·乔利伯爵的1号私兵普威尔内府骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_48", "trp_king_spy", 5, 40, 2), #玛尼翁·乔利伯爵的2号私兵普威尔密探
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_49", "trp_powell_praetorian", 4, 20, 1), #苏蒂里奥斯·梅西耶伯爵的1号私兵普威尔贵族禁卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_49", "trp_dragon_blood_swordsman", 5, 40, 2), #苏蒂里奥斯·梅西耶伯爵的2号私兵龙血剑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_59", "trp_tocsin_knight", 1, 4, 1), #塔维·缪顿男爵的1号私兵戒钟骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_59", "trp_powell_praetorian", 4, 20, 2), #塔维·缪顿男爵的2号私兵普威尔贵族禁卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_60", "trp_powell_heavy_infantry", 14, 70, 1), #尚利亚·多伊尔子爵的1号私兵普威尔重步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_60", "trp_powell_halberd_infantry", 8, 40, 2), #尚利亚·多伊尔子爵的2号私兵普威尔戟兵

     (call_script, "script_bodyguard_troop_import", "trp_knight_1_1", "trp_elemental_knight", 5, 40, 1), #罗德里格斯公爵的1号私兵元素骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_1", "trp_red_dolphin_banneret", 6, 48, 2), #罗德里格斯公爵的2号私兵红海豚方旗骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_5", "trp_garcia_bodyguard", 50, 50, 1), #加西亚侯爵的1号私兵加西亚亲卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_5", "trp_faceless_cavalry", 7, 7, 2), #加西亚侯爵的2号私兵无面骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_13", "trp_powell_armored_conjurer", 6, 30, 1), #萨维尼安·尤尔伯利伯爵的1号私兵普威尔铠甲术士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_13", "trp_lesaff_iron_axe_sergeant", 8, 40, 2), #萨维尼安·尤尔伯利伯爵的2号私兵勒塞夫铁斧军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_14", "trp_elemental_knight", 4, 16, 1), #勒内·威登伯爵的1号私兵元素骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_14", "trp_red_dolphin_knight", 7, 56, 2), #勒内·威登伯爵的2号私兵红海豚骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_20", "trp_elemental_ranger", 5, 25, 1), #克莉斯特的1号私兵元素游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_20", "trp_red_dolphin_banneret", 6, 30, 2), #克莉斯特的2号私兵红海豚方旗骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_36", "trp_elemental_knight", 4, 16, 1), #科莫·洛佩兹伯爵的1号私兵元素骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_36", "trp_red_dolphin_knight", 7, 56, 2), #科莫·洛佩兹伯爵的2号私兵红海豚骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_41", "trp_elemental_knight", 3, 12, 1), #加斯东·鲁克斯伯爵的1号私兵元素骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_41", "trp_grenier_rider", 12, 72, 2), #加斯东·鲁克斯伯爵的2号私兵戈兰尼尔骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_24", "trp_lesaff_iron_axe_sergeant", 6, 36, 1), #格扎维埃·加西亚勋爵的1号私兵勒塞夫铁斧军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_32", "trp_lesaff_axe_warrior", 7, 49, 1), #奥克塔夫·尤尔伯利男爵的1号私兵勒塞夫斧战士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_33", "trp_elemental_attendant", 4, 32, 1), #皮维·威登子爵的1号私兵元素侍从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_52", "trp_elemental_ranger", 3, 15, 1), #莉艾·方丹伯爵的1号私兵元素游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_54", "trp_elemental_knight", 2, 6, 1), #罗克兰·马克斯子爵的1号私兵元素骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_54", "trp_grenier_rider", 10, 60, 2), #罗克兰·马克斯子爵的2号私兵戈兰尼尔骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_58", "trp_red_dolphin_banneret", 3, 12, 1), #泽菲尔·李子爵的1号私兵红海豚方旗骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_58", "trp_grenier_longbow_archer", 12, 72, 2), #泽菲尔·李子爵的2号私兵戈兰尼尔长弓手

     (call_script, "script_bodyguard_troop_import", "trp_knight_1_2", "trp_dragonblood_knight", 5, 35, 1), #伊格纳兹公爵的1号私兵龙血骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_2", "trp_dragonwings_knight", 5, 30, 2), #伊格纳兹公爵的2号私兵龙翼骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_9", "trp_dragonblood_knight", 4, 24, 1), #康坦·华洛夫伯爵的1号私兵龙血骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_9", "trp_powell_dragon_archer", 7, 56, 2), #康坦·华洛夫伯爵的2号私兵普威尔猎龙射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_10", "trp_dragonblood_knight", 4, 24, 1), #菲利贝尔·温卡德伯爵的1号私兵龙血骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_10", "trp_hometownless_knight", 5, 40, 2), #菲利贝尔·温卡德伯爵的2号私兵无乡骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_35", "trp_dragonblood_knight", 4, 24, 1), #亚瑟·莱菲布勒侯爵的1号私兵龙血骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_35", "trp_northern_cavalry", 6, 60, 2), #亚瑟·莱菲布勒侯爵的2号私兵北境枪骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_18", "trp_powell_noble_knight", 5, 30, 1), #朱斯蒂纳·罗车巴斯伯爵的1号私兵普威尔贵胄骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_21", "trp_northern_ministeriales", 6, 36, 1), #若阿尚·伊格纳兹子爵的1号私兵北境农奴骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_21", "trp_northern_cavalry", 9, 63, 2), #若阿尚·伊格纳兹子爵的2号私兵北境枪骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_28", "trp_powell_dragon_archer", 5, 30, 1), #普罗斯佩耳·华洛夫男爵的1号私兵普威尔猎龙射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_28", "trp_northern_heavy_crossbow_shooter", 7, 49, 2), #普罗斯佩耳·华洛夫男爵的2号私兵北境强弩攻坚手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_29", "trp_revenge_iron_hoof", 7, 49, 1), #纳坦·温卡德男爵的1号私兵复仇铁骑
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_29", "trp_hometownless_knight", 4, 20, 2), #纳坦·温卡德男爵的2号私兵无乡骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_51", "trp_northern_tower_shield_sergeant", 6, 42, 1), #博尔奇·摩勒欧伯爵的1号私兵北境塔盾军士

     (call_script, "script_bodyguard_troop_import", "trp_knight_1_3", "trp_preist_knight", 7, 63, 1), #派崔克公爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_3", "trp_divine_swordsworn_cavalry", 5, 30, 2), #派崔克公爵的2号私兵奉剑圣骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_7", "trp_preist_knight", 5, 30, 1), #斯特凡·埃克苏佩里侯爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_7", "trp_preist_noble_cavalry", 6, 42, 2), #斯特凡·埃克苏佩里侯爵的2号私兵奉神城贵胄骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_11", "trp_preist_knight", 5, 30, 1), #马丁·罗尔斯查德侯爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_11", "trp_preist_horseback_crossbow_sergeant", 7, 42, 2), #马丁·罗尔斯查德侯爵的2号私兵奉神城骑弩军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_22", "trp_preist_knight", 5, 30, 1), #蒂埃里·派崔克勋爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_22", "trp_powell_armour_divineguider", 5, 35, 2), #蒂埃里·派崔克勋爵的2号私兵普威尔圣军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_37", "trp_preist_knight", 5, 30, 1), #塞琉斯·卡斯特尔伯爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_37", "trp_preist_attendant", 6, 42, 2), #塞琉斯·卡斯特尔伯爵的2号私兵奉神侍从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_38", "trp_preist_knight", 4, 24, 1), #奥托尼·密特朗伯爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_38", "trp_powell_orthodox_zealot", 14, 98, 2), #奥托尼·密特朗伯爵的2号私兵普威尔正教狂信徒
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_53", "trp_preist_knight", 4, 24, 1), #尚德隆·里安德尔子爵的1号私兵奉神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_53", "trp_preist_noble_crossbowman", 15, 135, 2), #尚德隆·里安德尔子爵的2号私兵奉神城贵胄弩手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_26", "trp_preist_noble_cavalry", 5, 25, 1), #维尔日妮·埃克苏佩里子爵的1号私兵奉神城贵胄骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_26", "trp_powell_conscripted_therapist", 12, 72, 2), #维尔日妮·埃克苏佩里子爵的2号私兵普威尔治疗师
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_30", "trp_preist_horseback_crossbow_sergeant", 5, 30, 1), #路易·罗尔斯查德伯爵的1号私兵奉神城骑弩军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_30", "trp_preist_infantry", 13, 65, 2), #路易·罗尔斯查德伯爵的2号私兵奉神城步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_56", "trp_powell_armour_divineguider", 4, 24, 1), #邓斯坦·史丹尼男爵的1号私兵普威尔圣军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_57", "trp_powell_military_divineguider", 7, 63, 1), #史班瑟·路加男爵的1号私兵普威尔军事神术使

     (call_script, "script_bodyguard_troop_import", "trp_knight_1_4", "trp_sandboat_knight", 6, 36, 1), #马哈茂德公爵的1号私兵沙舟骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_4", "trp_gurorrion_guard", 8, 48, 2), #马哈茂德公爵的2号私兵古洛隆卫士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_6", "trp_rodriguez_rogue_knight", 7, 56, 1), #于里安·索恩德伯爵的1号私兵罗德里格斯无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_6", "trp_rodriguez_rogue_attendant", 12, 72, 2), #于里安·索恩德伯爵的2号私兵罗德里格斯无赖扈从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_8", "trp_powell_rogue_knight", 7, 56, 1), #萝萨·曼帕顿伯爵的1号私兵普威尔无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_8", "trp_powell_rogue_attendant", 12, 72, 2), #萝萨·曼帕顿伯爵的2号私兵普威尔无赖扈从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_12", "trp_sandboat_knight", 4, 20, 1), #瓦尔多·范德比尔特侯爵的1号私兵沙舟骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_12", "trp_sousanth_servant", 6, 36, 2), #瓦尔多·范德比尔特侯爵的2号私兵南沙仆从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_39", "trp_city_rogue_knight", 7, 56, 1), #特拉洛克·盖兰伯爵的1号私兵自由城邦无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_39", "trp_city_rogue_attendant", 12, 72, 2), #特拉洛克·盖兰伯爵的2号私兵自由城邦无赖扈从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_40", "trp_sandboat_knight", 4, 20, 1), #阿尔邦·福勒伯爵的1号私兵沙舟骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_40", "trp_sousanth_elite_bowman", 10, 50, 2), #阿尔邦·福勒伯爵的2号私兵南沙精锐射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_16", "trp_sousanth_rider", 5, 25, 1), #奥迪莱·菲比子爵的1号私兵南沙骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_16", "trp_araiharsa_mercenary_infantry", 12, 72, 2), #奥迪莱·菲比子爵的2号私兵阿利哈沙雇佣步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_23", "trp_sandboat_knight", 4, 24, 1), #伊夫·马哈茂德勋爵的1号私兵沙舟骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_23", "trp_sousanth_darts_sergeant", 7, 49, 2), #伊夫·马哈茂德勋爵的2号私兵南沙战镖军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_25", "trp_rodriguez_rogue_knight", 5, 30, 1), #托马·索恩德男爵的1号私兵罗德里格斯无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_25", "trp_rodriguez_rogue_attendant", 8, 48, 2), #托马·索恩德男爵的2号私兵罗德里格斯无赖扈从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_27", "trp_powell_rogue_knight", 5, 30, 1), #西梅翁·曼帕顿男爵的1号私兵普威尔无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_27", "trp_powell_rogue_attendant", 8, 48, 2), #西梅翁·曼帕顿男爵的2号私兵普威尔无赖扈从
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_31", "trp_araiharsa_mercenary_rider", 4, 20, 1), #奥德蕾·范德比尔特男爵的1号私兵阿利哈沙雇佣骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_31", "trp_araiharsa_mercenary_infantry", 10, 60, 2), #奥德蕾·范德比尔特男爵的2号私兵阿利哈沙雇佣步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_55", "trp_city_rogue_knight", 5, 30, 1), #巴伦·尼尔勋爵的1号私兵自由城邦无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_1_55", "trp_city_rogue_attendant", 8, 48, 2), #巴伦·尼尔勋爵的2号私兵自由城邦无赖扈从


     #伊希斯公国
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_2_lord", "trp_soul_selected_champion", 1, 3, 1), #辛希安·灵魂议长的1号私兵灵魄之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_2_lord", "trp_spirittree_knight", 3, 120, 2), #辛希安·灵魂议长的2号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_5", "trp_soul_selected_champion", 1, 1, 1), #嘉比里拉·灵魂议员的1号私兵灵魄之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_5", "trp_seddlined_apostle", 4, 28, 2), #嘉比里拉·灵魂议员的2号私兵灵花使徒
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_9", "trp_soul_selected_champion", 1, 1, 1), #埃卡捷琳·灵魂议员的1号私兵灵魄之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_9", "trp_yishith_spiritual_horse_knight", 3, 18, 2), #埃卡捷琳·灵魂议员的2号私兵伊希斯灵马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_28", "trp_soul_selected_champion", 1, 1, 1), #凯缇亚·灵魂议员的1号私兵灵魄之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_28", "trp_seddlined_dare_to_die_corp", 5, 30, 2), #凯缇亚·灵魂议员的2号私兵灵花决死剑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_30", "trp_soul_selected_champion", 1, 1, 1), #内莎·灵魂议员的1号私兵灵魄之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_30", "trp_spirittree_knight", 3, 15, 2), #内莎·灵魂议员的2号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_11", "trp_spirittree_knight", 2, 10, 1), #爱德莱德·伊莲恩议员的1号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_11", "trp_seddlined_crazy_cavalry", 7, 42, 2), #爱德莱德·伊莲恩议员的2号私兵灵苗狂骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_14", "trp_spirittree_knight", 2, 10, 1), #赫尔娜·因格拉谬议员的1号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_14", "trp_yishith_equerry", 4, 20, 2), #赫尔娜·因格拉谬议员的2号私兵伊希斯骑士侍从
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_12", "trp_spirittree_knight", 2, 10, 1), #奈伯尼尔·希尔维斯特议员的1号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_12", "trp_seddlined_desperater", 10, 60, 2), #奈伯尼尔·希尔维斯特议员的2号私兵灵苗死士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_19", "trp_spirittree_knight", 2, 10, 1), #海洛伊斯·嘉比里拉议员的1号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_19", "trp_seddlined_thrall", 36, 180, 2), #海洛伊斯·嘉比里拉议员的2号私兵灵芽隶从
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_23", "trp_spirittree_knight", 2, 12, 1), #安东妮儿·埃卡捷琳议员的1号私兵灵树骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_34", "trp_yishith_spiritual_horse_knight", 2, 12, 1), #奥克莎·米萨议员的1号私兵伊希斯灵马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_34", "trp_yishith_equerry", 4, 20, 2), #奥克莎·米萨议员的2号私兵伊希斯骑士侍从
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_33", "trp_seddlined_dare_to_die_corp", 3, 18, 1), #乔卡·特吉娜议员的1号私兵灵花决死剑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_33", "trp_seddlined_puppet", 30, 150, 2), #乔卡·特吉娜议员的2号私兵灵芽傀儡

     (call_script, "script_bodyguard_troop_import", "trp_knight_2_1", "trp_demise_selected_champion", 1, 3, 1), #伊芙琳·死亡代议长的1号私兵死亡之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_1", "trp_spiritrain_ranger", 3, 120, 2), #伊芙琳·死亡代议长的2号私兵灵雨游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_7", "trp_demise_selected_champion", 1, 1, 1), #尤拉诺斯·死亡议员的1号私兵死亡之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_7", "trp_demise_gardener", 3, 15, 2), #尤拉诺斯·死亡议员的2号私兵死亡园丁
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_26", "trp_demise_selected_champion", 1, 1, 1), #茱丽莎·死亡议员的1号私兵死亡之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_26", "trp_hotbed_hollow", 4, 24, 2), #茱丽莎·死亡议员的2号私兵温床幽魂
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_29", "trp_demise_selected_champion", 1, 1, 1), #戴瑞那·死亡议员的1号私兵死亡之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_29", "trp_humus_lord", 4, 24, 2), #戴瑞那·死亡议员的2号私兵腐土领主
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_15", "trp_spiritrain_ranger", 2, 10, 1), #菲丽斯·伊芙琳议员的1号私兵灵雨游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_15", "trp_hotbed_farmer", 5, 25, 2), #菲丽斯·伊芙琳议员的2号私兵温床护苗人
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_21", "trp_spiritrain_ranger", 2, 10, 1), #芝妮雅·尤拉诺斯议员的1号私兵灵雨游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_21", "trp_humic_vanguard", 8, 56, 2), #芝妮雅·尤拉诺斯议员的2号私兵腐殖先锋
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_31", "trp_demise_gardener", 2, 10, 1), #塔芭斯·佩莱卡议员的1号私兵死亡园丁
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_31", "trp_root_borning_one", 30, 150, 2), #塔芭斯·佩莱卡议员的2号私兵根生者
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_37", "trp_hotbed_farmer", 5, 25, 1), #斯哈维·艾瑞琦娜议员的1号私兵温床护苗人
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_37", "trp_humic_walker", 8, 56, 2), #斯哈维·艾瑞琦娜议员的2号私兵腐殖行者

     (call_script, "script_bodyguard_troop_import", "trp_knight_2_2", "trp_ancester_selected_champion", 1, 3, 1), #绯雷德翠卡·先祖代议长的1号私兵先祖之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_2", "trp_immortal_assassin", 3, 120, 2), #绯雷德翠卡·先祖代议长的2号私兵永世者刺客
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_6", "trp_ancester_selected_champion", 1, 1, 1), #奥克塔薇·先祖议员的1号私兵先祖之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_6", "trp_yishith_elf_heavy_cavalry", 4, 20, 2), #奥克塔薇·先祖议员的2号私兵伊希斯精灵重骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_10", "trp_ancester_selected_champion", 1, 1, 1), #加菲尔德·先祖议员的1号私兵先祖之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_10", "trp_yishith_heavy_ranger", 4, 20, 2), #加菲尔德·先祖议员的2号私兵伊希斯重甲游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_27", "trp_ancester_selected_champion", 1, 1, 1), #瑟欧密斯·先祖议员的1号私兵先祖之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_27", "trp_molter_knight", 3, 18, 2), #瑟欧密斯·先祖议员的2号私兵蜕生骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_16", "trp_immortal_assassin", 2, 10, 1), #孟莉萨·绯雷德翠卡议员的1号私兵永世者刺客
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_16", "trp_yishith_elf_heavy_cavalry", 3, 15, 2), #孟莉萨·绯雷德翠卡议员的2号私兵伊希斯精灵重骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_20", "trp_immortal_assassin", 2, 10, 1), #葛丽歇尔达·奥克塔薇议员的1号私兵永世者刺客
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_20", "trp_yishith_sword_dancer", 4, 20, 2), #葛丽歇尔达·奥克塔薇议员的2号私兵伊希斯剑舞者
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_24", "trp_immortal_assassin", 2, 10, 1), #克洛怡·加菲尔德议员的1号私兵永世者刺客
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_24", "trp_molter_knight", 2, 12, 2), #克洛怡·加菲尔德议员的2号私兵蜕生骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_35", "trp_yishith_elf_sergeant", 5, 20, 1), #安吉丽娜·奥德瑞议员的1号私兵伊希斯精灵军士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_35", "trp_yishith_crossbow_ranger", 4, 28, 2), #安吉丽娜·奥德瑞议员的2号私兵伊希斯弩游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_38", "trp_yishith_sword_armedman", 7, 49, 1), #塔玛尔·瓦尔卡议员的1号私兵伊希斯剑甲兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_38", "trp_half_molter", 10, 60, 2), #塔玛尔·瓦尔卡议员的2号私兵半蜕生者

     (call_script, "script_bodyguard_troop_import", "trp_knight_2_3", "trp_vita_selected_champion", 1, 3, 1), #珍妮芙·生命代议长的1号私兵生命之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_3", "trp_spiritwind_bowcavalry", 3, 120, 2), #珍妮芙·生命代议长的2号私兵灵风游骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_25", "trp_vita_selected_champion", 1, 1, 1), #莱伊拉·生命议员的1号私兵生命之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_25", "trp_yishith_seawind_ranger", 4, 20, 2), #莱伊拉·生命议员的2号私兵伊希斯海风游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_4", "trp_vita_selected_champion", 1, 1, 1), #尤莱雅·生命议员的1号私兵生命之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_4", "trp_yishith_chivalric_knight", 3, 12, 2), #尤莱雅·生命议员的2号私兵伊希斯侠义骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_8", "trp_vita_selected_champion", 1, 1, 1), #维兰·生命议员的1号私兵生命之树神选冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_8", "trp_yishith_throwing_axe_ranger", 6, 36, 2), #维兰·生命议员的2号私兵伊希斯飞斧游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_17", "trp_spiritwind_bowcavalry", 2, 10, 1), #奥利维塔·珍妮芙议员的1号私兵灵风游骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_17", "trp_yishith_sentry_cavalry", 5, 25, 2), #奥利维塔·珍妮芙议员的2号私兵伊希斯哨戒骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_18", "trp_spiritwind_bowcavalry", 2, 10, 1), #娜提雅维达·尤莱雅议员的1号私兵灵风游骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_18", "trp_yishith_recruiting_rider", 7, 35, 2), #娜提雅维达·尤莱雅议员的2号私兵伊希斯募集骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_22", "trp_spiritwind_bowcavalry", 2, 10, 1), #爱德文娜·维兰议员的1号私兵灵风游骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_22", "trp_yishith_throwing_axe_ranger", 5, 25, 2), #爱德文娜·维兰议员的2号私兵伊希斯飞斧游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_36", "trp_yishith_navy_archer", 5, 25, 1), #雪帕·伊亚莉娜议员的1号私兵伊希斯海军射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_36", "trp_vita_shield_axe_guardian", 9, 72, 2), #雪帕·伊亚莉娜议员的2号私兵伊希斯盾斧卫士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_13", "trp_yishith_seawind_ranger", 3, 15, 1), #诺亚·朱莉尔思议员的1号私兵伊希斯海风游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_13", "trp_yishith_boat_guard", 12, 96, 2), #诺亚·朱莉尔思议员的2号私兵伊希斯船团守卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_32", "trp_yishith_chivalric_knight", 2, 8, 1), #海瑞丝·法耶议员的1号私兵伊希斯侠义骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_2_32", "trp_snow_trading_company_guard", 12, 48, 2), #海瑞丝·法耶议员的2号私兵雪泥商会护卫


     #科鲁托酋长国
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_3_lord", "trp_totem_champion_warrior", 2, 6, 1), #阿古达木可汗的1号私兵图腾冠军勇士
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_3_lord", "trp_kouruto_sword_fighter", 3, 90, 2), #阿古达木可汗的2号私兵科鲁托剑斗士
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_7", "trp_kouruto_sword_fighter", 2, 26, 1), #“英雄”巴特尔的1号私兵科鲁托剑斗士
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_19", "trp_kouruto_gladiator", 4, 40, 1), #“硬铁”帖木日布赫的1号私兵科鲁托角斗士
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_6", "trp_kouruto_therianthropy_guardian", 4, 40, 1), #“石头”朝鲁的1号私兵科鲁托兽人守备军
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_6", "trp_kouruto_human_guardian", 8, 80, 2), #“石头”朝鲁的2号私兵科鲁托人类守备军
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_18", "trp_metal_devourer_master", 1, 4, 1), #“大力”呼其图的1号私兵食铁大师
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_18", "trp_ironbite_gang_freshman", 3, 30, 2), #“大力”呼其图的2号私兵啮铁帮新人
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_26", "trp_furnace_hunter", 2, 16, 1), #“飞鹰”少布的1号私兵洪炉猎人
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_26", "trp_furnace_watch_stalker", 3, 24, 2), #“飞鹰”少布的2号私兵洪炉监视者密探
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_28", "trp_furnace_watch_recruit", 7, 56, 1), #“和平”恩金的1号私兵洪炉监视者新兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_28", "trp_furnace_watch_warrior", 4, 32, 1), #“和平”恩金的2号私兵洪炉监视者战士

     (call_script, "script_bodyguard_troop_import", "trp_knight_3_1", "trp_furnace_hierophant", 1, 3, 1), #大酋长“柱子”巴根的1号私兵侍炉祖巫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_1", "trp_kouruto_furnace_great_ritualist", 3, 12, 2), #大酋长“柱子”巴根的2号私兵科鲁托洪炉大巫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_23", "trp_kouruto_furnace_great_ritualist", 1, 3, 1), #“好人”宁金的1号私兵洪炉大巫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_23", "trp_kouruto_ritualist", 3, 30, 2), #“好人”宁金的2号私兵科鲁托巫祭
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_13", "trp_kouruto_ritualist", 2, 4, 1), #“竖耳”德勒德格日的1号私兵科鲁托巫祭
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_27", "trp_kouruto_furnace_great_ritualist", 1, 3, 1), #“狗屎运”吉雅赛音的1号私兵洪炉大巫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_27", "trp_kouruto_veteran_shaman", 5, 40, 2), #“好运”吉雅赛音的2号私兵科鲁托资深萨满
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_29", "trp_kouruto_ritualist", 2, 4, 1), #“星枝”奥敦木其尔的1号私兵科鲁托巫祭
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_24", "trp_kouruto_furnace_great_ritualist", 1, 3, 1), #“大山”阿古拉的1号私兵洪炉大巫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_24", "trp_kouruto_novice_shaman", 7, 42, 2), #“大山”阿古拉的2号私兵科鲁托新手萨满
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_10", "trp_kouruto_furnace_great_ritualist", 1, 3, 1), #“金钱豹”伊日毕斯的1号私兵洪炉大巫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_10", "trp_kouruto_novice_shaman", 7, 42, 2), #“金钱豹”伊日毕斯的2号私兵科鲁托新手萨满
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_31", "trp_kouruto_ritualist", 2, 4, 1), #“威严”苏日立格的1号私兵科鲁托巫祭

     (call_script, "script_bodyguard_troop_import", "trp_knight_3_2", "trp_kouruto_therianthropy_caravan_guard", 10, 60, 1), #大酋长“兴隆”满都拉图的1号私兵科鲁托兽人商队护卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_14", "trp_kouruto_therianthropy_caravan_guard", 5, 30, 1), #“扁头”哈布其克的1号私兵科鲁托兽人商队护卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_5", "trp_therianthropy_undead_hunter", 10, 60, 1), #“黑虎”哈尔巴拉的1号私兵兽人猎亡者
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_17", "trp_therianthropy_undead_hunter", 5, 30, 1), #“白小子”查干夫的1号私兵兽人猎亡者

     (call_script, "script_bodyguard_troop_import", "trp_knight_3_3", "trp_sentinel_bastion_warden", 2, 20, 1), #大酋长“斧头”苏合的1号私兵守望者卫戍骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_3", "trp_sentinel_servant", 4, 40, 2), #大酋长“斧头”苏合的2号私兵守望者奴仆
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_15", "trp_sentinel_bastion_warden", 1, 10, 1), #“凹脸”翁和日的1号私兵守望者卫戍骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_3_15", "trp_sentinel_servant", 2, 20, 2), #“凹脸”翁和日的2号私兵守望者奴仆


     #科鲁托酋长国
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_4_lord", "trp_god_raiser_knight", 2, 6, 1), #女皇依文洁琳·昆庭的1号私兵举神骑士
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_4_lord", "trp_optihazation_adventure_knight", 10, 100, 2), #女皇依文洁琳·昆庭的2号私兵光瘴探险骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_7", "trp_diemer_monster_enslaving_knight", 4, 40, 1), #伯爵哈罗德·柏邵斯的1号私兵迪默役兽骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_7", "trp_diemer_hetairoi", 5, 50, 2), #伯爵哈罗德·柏邵斯的2号私兵迪默伙友骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_10", "trp_optihazation_adventure_knight", 3, 24, 1), #伯爵特尔格·郝根的1号私兵光瘴探险骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_10", "trp_diemer_hired_adventurer", 10, 100, 2), #伯爵特尔格·郝根的2号私兵迪默受雇冒险者
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_24", "trp_optihazation_scholar", 3, 15, 1), #男爵克努特·郝根的1号私兵光瘴学士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_11", "trp_god_raiser_knight", 1, 1, 1), #子爵罗格森·哈根的1号私兵举神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_28", "trp_optihazation_adventure_knight", 3, 24, 1), #伯爵哈坎·梅基宁的1号私兵光瘴探险骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_28", "trp_diemer_hired_adventurer", 10, 100, 2), #伯爵哈坎·梅基宁的2号私兵迪默受雇冒险者
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_31", "trp_marsh_council_guard", 4, 40, 1), #伯爵哈登·瓦尔克帕的1号私兵暗沼议会守卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_31", "trp_diemer_swordman", 6, 60, 2), #伯爵哈登·瓦尔克帕的2号私兵迪默剑斗士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_26", "trp_diemer_heaveybow_marksman", 4, 40, 1), #伯爵托伊沃·科诺宁的1号私兵迪默重弓手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_26", "trp_diemer_shortbow_archer", 6, 60, 2), #伯爵托伊沃·科诺宁的2号私兵迪默短弓手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_27", "trp_diemer_light_cavalry", 4, 40, 1), #伯爵翁尼·佩卡宁的1号私兵迪默轻骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_27", "trp_diemer_guardian", 6, 60, 2), #伯爵翁尼·佩卡宁的2号私兵迪默近卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_29", "trp_confederation_enslavement_warlock", 6, 60, 1), #伯爵汉斯·尼布鲁姆的1号私兵邦联役奴术士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_29", "trp_confederation_gladiator_champion", 3, 30, 2), #伯爵汉斯·尼布鲁姆的2号私兵邦联角斗冠军
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_30", "trp_god_raiser_knight", 1, 3, 1), #选帝侯尼尔斯·赖科宁的1号私兵举神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_30", "trp_venery_knight", 5, 70, 2), #选帝侯尼尔斯·赖科宁的2号私兵狩猎骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_37", "trp_confederation_human_hunting_cavalry", 4, 40, 1), #子爵奥伊瓦·阿赫蒂萨里的1号私兵邦联猎人骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_37", "trp_confederation_slave_catcher_hitman", 10, 100, 2), #子爵奥伊瓦·阿赫蒂萨里的2号私兵邦联捕奴打手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_12", "trp_venery_knight", 3, 27, 1), #子爵艾尔瑞克·雅各布森的1号私兵狩猎骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_12", "trp_venery_slaver", 5, 40, 2), #子爵艾尔瑞克·雅各布森的2号私兵狩猎奴从
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_21", "trp_confederation_slave_trainer", 6, 60, 1), #男爵俄丽克·哈罗德森的1号私兵邦联奴隶训练师
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_21", "trp_confederation_slave_dominator", 10, 100, 2), #男爵俄丽克·哈罗德森的2号私兵邦联奴隶调教师

     (call_script, "script_bodyguard_troop_import", "trp_knight_4_1", "trp_rip_current_blade", 5, 60, 1), #选帝侯伊登·艾萨克的1号私兵裂流之刃
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_1", "trp_dreadmarsh_knight", 5, 80, 2), #选帝侯伊登·艾萨克的2号私兵噩沼骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_15", "trp_rip_current_blade", 2, 20, 1), #男爵雷耶克·伊登森的1号私兵裂流之刃
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_15", "trp_deep_dread_assassin", 4, 48, 2), #男爵雷耶克·伊登森的2号私兵深惧刺客
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_4", "trp_marsh_deepone_commander", 5, 60, 1), #侯爵瑞马尔德·谢勒森的1号私兵大沼鱼人统领
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_4", "trp_confederation_ship_looter", 6, 60, 2), #侯爵瑞马尔德·谢勒森的2号私兵邦联袭船者
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_18", "trp_marsh_deepone_warrior", 5, 80, 1), #男爵吉尔斯·瑞马尔德森的1号私兵大沼鱼人勇士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_18", "trp_confederation_deepone_slave", 10, 100, 2), #男爵吉尔丝·瑞马尔德森的2号私兵邦联鱼人奴兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_8", "trp_dreadmarsh_warrior", 5, 60, 1), #伯爵鲁德·汉森的1号私兵噩沼武夫
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_8", "trp_confederation_swamp_bandit", 8, 80, 2), #伯爵鲁德·汉森的2号私兵邦联沼泽匪兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_22", "trp_marsh_deepone_professional_soldier", 10, 100, 1), #男爵拉尔斯·鲁德森的1号私兵大沼鱼人职业士兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_22", "trp_confederation_fishing_serf", 15, 150, 2), #男爵拉尔斯·鲁德森的2号私兵邦联渔奴
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_9", "trp_marsh_venomfin_hunter", 5, 60, 1), #伯爵海达·乌勒森的1号私兵大沼毒鳍猎手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_9", "trp_confederation_toxin_dealer", 2, 20, 2), #伯爵海达·乌勒森的2号私兵邦联吐毒者
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_23", "trp_marsh_hunter", 5, 80, 1), #男爵莱芙·海达森的1号私兵大沼猎手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_23", "trp_confederation_toxin_dealer", 2, 10, 2), #男爵莱芙·海达森的2号私兵邦联吐毒者

     (call_script, "script_bodyguard_troop_import", "trp_knight_4_2", "trp_deceasing_eagle", 2, 4, 1), #选帝侯伊阿亚·斯旺达斯特的1号私兵未死之鹰
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_2", "trp_divinecusp_knight_captain", 4, 32, 2), #选帝侯伊阿亚·斯旺达斯特的2号私兵神牙骑士长
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_16", "trp_divinecusp_knight", 3, 30, 1), #男爵迪里刚·斯旺达斯特的1号私兵神牙骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_16", "trp_storm_servant", 4, 32, 2), #男爵迪里刚·斯旺达斯特的2号私兵风暴仆从
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_13", "trp_swaybacked_monk", 3, 30, 1), #子爵法恩·哈勒沃森的1号私兵破背僧
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_13", "trp_storm_follower", 4, 32, 2), #子爵法恩·哈勒沃森的2号私兵风暴追随者
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_6", "trp_deceasing_eagle", 1, 1, 1), #侯爵阿斯特里德·度勒郝格的1号私兵未死之鹰
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_6", "trp_divinecusp_knight", 3, 30, 2), #侯爵阿斯特里德·度勒郝格的2号私兵神牙骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_20", "trp_storm_follower", 2, 20, 1), #男爵各勒塔·度勒郝格的1号私兵风暴追随者
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_20", "trp_holy_wing_guard", 3, 30, 2), #男爵各勒塔·度勒郝格的2号私兵圣翼侍卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_25", "trp_purifier_dismounted_knight", 4, 36, 1), #侯爵哈里·维尔塔宁的1号私兵净世军步行骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_25", "trp_storm_white_shadow", 3, 30, 2), #侯爵哈里·维尔塔宁的2号私兵风暴白影
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_36", "trp_purifier_infantry", 8, 64, 1), #子爵马尔科·涅米宁的1号私兵净世军团步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_36", "trp_purifier_light_soldier", 10, 60, 2), #子爵马尔科·涅米宁的2号私兵净世军团轻甲兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_5", "trp_purifier_infantry", 8, 64, 1), #侯爵图亚·图热森的1号私兵净世军团弩炮手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_5", "trp_purifier_light_soldier", 4, 40, 2), #侯爵图亚·图热森的2号私兵净世军战斗牧师
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_19", "trp_god_raiser_knight", 1, 1, 1), #男爵索尔顿·图亚森的1号私兵举神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_19", "trp_purifier_recruit", 10, 160, 2), #男爵索尔顿·图亚森的2号私兵净世军团新兵

     (call_script, "script_bodyguard_troop_import", "trp_knight_4_3", "trp_god_raiser_knight", 1, 3, 1), #选帝侯奥拉夫·特吕伊鲁的1号私兵举神骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_3", "trp_ankiya_knight", 7, 63, 2), #选帝侯奥拉夫·特吕伊鲁的2号私兵安基亚骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_17", "trp_ankiya_rider", 5, 30, 1), #男爵勒纳·特吕伊鲁的1号私兵安基亚骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_17", "trp_ankiya_horseback_mercenary", 5, 30, 2), #男爵勒纳·特吕伊鲁的2号私兵安基亚骑马佣兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_32", "trp_ankiya_naturalized_noble", 3, 30, 1), #伯爵奥吉·哈马莱宁的1号私兵安基亚归化贵族
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_32", "trp_ankiya_mercenary", 4, 40, 2), #伯爵奥吉·哈马莱宁的2号私兵安基亚佣兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_33", "trp_ankiya_naturalized_noble", 3, 30, 1), #侯爵海尔维·瓦洛的1号私兵安基亚归化贵族
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_33", "trp_ankiya_civilized_barbarian", 6, 60, 2), #侯爵海尔维·瓦洛的2号私兵安基亚开化蛮族
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_34", "trp_ankiya_naturalized_noble", 3, 30, 1), #伯爵西蒙·尼尼托斯的1号私兵安基亚归化贵族
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_34", "trp_ankiya_recruit", 5, 60, 2), #伯爵西蒙·尼尼托斯的2号私兵安基亚征召兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_4_35", "trp_ankiya_naturalized_noble", 3, 30, 1), #伯爵莉雅·郝吉奥的1号私兵安基亚归化贵族


     #教皇国
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_5_lord", "trp_holy_knight", 2, 6, 1), #教皇孔苏斯三世的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_5_lord", "trp_holy_knight_aide", 4, 120, 2), #教皇孔苏斯三世的2号私兵圣骑士侍从
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_10", "trp_holy_foolishness", 1, 2, 1), #主教伊曼纽尔·瓦勒的1号私兵圣愚人
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_10", "trp_coffin_warden", 4, 24, 2), #主教伊曼纽尔·瓦勒的2号私兵圣棺守护者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_13", "trp_holy_knight", 1, 1, 1), #主教约书亚·西西里的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_13", "trp_godward_great_swordman", 6, 36, 2), #主教约书亚·西西里的2号私兵圣誓大剑师
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_38", "trp_holy_knight", 1, 1, 1), #主教保罗·比萨的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_38", "trp_papal_elite_archer", 6, 42, 2), #主教保罗·比萨的2号私兵教国精锐射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_37", "trp_holy_knight", 1, 1, 1), #主教奥马尔·奥特兰托的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_37", "trp_pontiff_knight", 7, 42, 2), #主教奥马尔·奥特兰托的2号私兵宗座骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_9", "trp_holy_knight", 1, 1, 1), #主教奥雷里奥·维尼托的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_9", "trp_great_sword_church_guard", 7, 42, 2), #主教奥雷里奥·维尼托的2号私兵教堂守卫（大剑）
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_18", "trp_blesruth_tzaddiq", 4, 24, 1), #教长古列尔莫·阿布鲁佐的1号私兵樊加鲁斯义人
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_29", "trp_holy_see_bedrock", 4, 24, 1), #教长米卡兰吉洛·翁布里亚的1号私兵圣座基岩
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_28", "trp_cardinal_guard", 4, 24, 1), #教长萨德罗·瓦勒的1号私兵枢机近卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_31", "trp_coffin_monitor", 3, 18, 1), #教长马尔克龙·西西里的1号私兵圣棺监视者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_31", "trp_eternal_rest_warden", 6, 42, 2), #教长马尔克龙·西西里的2号私兵永眠巡守
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_27", "trp_godward_great_swordman", 4, 28, 1), #教长拉法勒·维尼托的1号私兵圣誓大剑师
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_27", "trp_godward_swordman", 8, 64, 2), #教长拉法勒·维尼托的2号私兵圣誓剑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_53", "trp_papal_elite_archer", 4, 28, 1), #教长泰·罗戈维的1号私兵教国精锐射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_53", "trp_holy_city_sentry", 8, 56, 2), #教长泰·罗戈维的2号私兵圣城哨兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_55", "trp_marten_honor_guard", 4, 20, 1), #教长达奇·坎波迪梅莱的1号私兵马顿仪仗队
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_30", "trp_church_guard", 3, 15, 1), #教长马思米利安诺·托斯卡纳的1号私兵教堂守卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_30", "trp_great_sword_church_guard", 3, 15, 2), #教长马思米利安诺·托斯卡纳的2号私兵教堂守卫

     (call_script, "script_bodyguard_troop_import", "trp_knight_5_1", "trp_holy_knight", 1, 3, 1), #都主教奥格斯特·拉齐奥的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_1", "trp_reaper_knight_captain", 1, 4, 2), #都主教奥格斯特·拉齐奥的2号私兵狩魔骑士长
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_40", "trp_martyrs_of_deep_crimes", 1, 1, 1), #主教布鲁娜·加尔达的1号私兵深罪殉道者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_40", "trp_accumulated_sin_knight", 4, 16, 2), #主教布鲁娜·加尔达的2号私兵积罪骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_36", "trp_holy_knight", 1, 1, 1), #主教马特奥·都立的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_36", "trp_doctrinal_sitting_magistrate", 4, 24, 2), #主教马特奥·都立的2号私兵教义审判官
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_41", "trp_holy_knight", 1, 1, 1), #主教富尔维奥·贝加莫的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_41", "trp_hyena_knight", 4, 16, 2), #主教富尔维奥·贝加莫的2号私兵鬣狗骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_42", "trp_holy_knight", 1, 1, 1), #主教伊拉里奥·弗雷斯卡蒂的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_42", "trp_employed_demon_slayer", 8, 72, 2), #主教伊拉里奥·弗雷斯卡蒂的2号私兵受雇伐魔师
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_56", "trp_reaper_knight", 3, 15, 1), #教长罗斯科·月玛德纳的1号私兵狩魔骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_26", "trp_heretic_killer", 3, 15, 1), #教长萨瓦托·法夫的1号私兵异端猎刺
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_26", "trp_heretic_hunter", 5, 40, 2), #教长萨瓦托·法夫的2号私兵异端猎手
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_57", "trp_accumulated_sin_knight", 3, 12, 1), #教长邓高夫·提契诺的1号私兵积罪骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_57", "trp_devouring_sin_crazy_monk", 5, 35, 2), #教长邓高夫·提契诺的2号私兵啮罪狂僧
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_25", "trp_doctrinal_sitting_magistrate", 3, 12, 1), #教长苏缪勒·鲁索的1号私兵教义审判官
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_25", "trp_trial_servant", 8, 64, 2), #教长苏缪勒·鲁索的2号私兵审判仆役
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_58", "trp_sin_slave_infantry", 12, 96, 1), #教长乔坤·帕尔马的1号私兵罪仆步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_58", "trp_accused_believer", 20, 100, 2), #教长乔坤·帕尔马的2号私兵戴罪信众
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_51", "trp_exorcist_mercenary", 15, 150, 1), #教长奥兹·威尼托的1号私兵猎魔佣兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_2", "trp_holy_knight", 1, 3, 1), #都主教阿蒙瑞·萨顿的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_2", "trp_patron_knight", 7, 63, 2), #都主教阿蒙瑞·萨顿的2号私兵庇护骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_12", "trp_holy_knight", 1, 1, 1), #主教詹卡洛·托斯卡纳的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_12", "trp_yishith_baptized_ranger", 4, 28, 2), #主教詹卡洛·托斯卡纳的2号私兵伊希斯受洗游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_39", "trp_holy_knight", 1, 1, 1), #主教帕斯夸尔·奥斯塔的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_39", "trp_powell_baptized_knight", 5, 35, 2), #主教帕斯夸尔·奥斯塔的2号私兵普威尔受洗骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_11", "trp_shield_angel", 1, 2, 1), #主教费德里科·翁布里亚的1号私兵盾天使
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_11", "trp_divine_legion_insane_knight", 4, 16, 2), #主教费德里科·翁布里亚的2号私兵圣教军团狂战骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_34", "trp_holy_knight", 1, 1, 1), #主教果戈里·巴勒莫的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_34", "trp_divine_legion_veteran_knight", 4, 24, 2), #主教果戈里·巴勒莫的2号私兵圣教军历战骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_32", "trp_patron_warrior", 10, 70, 1), #教长伊莎贝拉·萨德尼亚的1号私兵庇护武士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_46", "trp_baptism_elite_crossbowman", 4, 24, 1), #教长蒂奇亚诺·卡拉布里亚的1号私兵施洗城精英弩手
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_46", "trp_baptism_archer_captain", 4, 12, 2), #教长蒂奇亚诺·卡拉布里亚的2号私兵施洗城弓兵队长
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_48", "trp_yishith_baptized_archer", 5, 30, 1), #教长科洛玛·埃尔巴的1号私兵伊希斯受洗射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_48", "trp_yishith_baptized_half_elf", 7, 42, 2), #教长科洛玛·埃尔巴的2号私兵伊希斯受洗半精灵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_47", "trp_powell_baptized_rider", 8, 40, 1), #教长斯特凡诺·特里雅斯特的1号私兵普威尔受洗骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_47", "trp_powell_baptized_infantry", 12, 72, 2), #教长斯特凡诺·特里雅斯特的2号私兵普威尔受洗步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_54", "trp_divine_legion_insane_infantry", 7, 49, 1), #教长奥克斯·普尔加托里奥的1号私兵圣教军团狂战士兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_33", "trp_divine_legion_veteran", 8, 80, 1), #主教阿尔菲奥·布林迪西的1号私兵圣教军团老兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_3", "trp_holy_knight", 1, 3, 1), #都主教阿拉蒂诺·罗希的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_3", "trp_arcane_knight_captain", 1, 4, 2), #都主教阿拉蒂诺·罗希的2号私兵奥术骑士长
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_7", "trp_holy_knight", 1, 1, 1), #主教卡米洛·鲁索的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_7", "trp_arcane_minister", 6, 36, 2), #主教卡米洛·鲁索的2号私兵奥法牧师
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_45", "trp_holy_knight", 1, 1, 1), #主教米克罗·多洛米泰斯的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_45", "trp_papal_swordwoman", 6, 36, 2), #主教米克罗·多洛米泰斯的2号私兵教国女剑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_8", "trp_logos_prophet", 1, 1, 1), #主教卡梅罗·法夫的1号私兵真造先知
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_8", "trp_key_knight", 4, 16, 2), #主教卡梅罗·法夫的2号私兵钥骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_44", "trp_holy_knight", 1, 1, 1), #主教爱德华·奇思里奥的1号私兵圣骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_44", "trp_key_knight", 4, 16, 2), #主教爱德华·奇思里奥的2号私兵钥骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_16", "trp_arcane_knight", 3, 15, 1), #教长卡特琳娜·弗留利的1号私兵奥术骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_17", "trp_arcane_minister", 4, 20, 1), #教长西蒙娜·卡拉布里亚的1号私兵奥法牧师
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_17", "trp_whitspring_chaplain", 5, 40, 2), #教长西蒙娜·卡拉布里亚的2号私兵白泉派神官
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_15", "trp_papal_female_guard", 6, 42, 1), #教长伊莱诺拉·利古里亚的1号私兵教国女护卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_15", "trp_armed_female_believer", 10, 50, 2), #教长伊莱诺拉·利古里亚的2号私兵武装女教友
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_52", "trp_gnosis_explorer", 4, 16, 1), #教长卡洛特·罗马涅的1号私兵真知探求者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_52", "trp_philosophical_egg_scholar", 9, 54, 2), #教长卡洛特·罗马涅的2号私兵圣卵派学士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_20", "trp_gnosis_explorer", 4, 16, 1), #教长曼努埃拉·萨顿的1号私兵真知探求者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_20", "trp_philosophical_egg_scholar", 9, 54, 2), #教长曼努埃拉·萨顿的2号私兵圣卵派学士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_4", "trp_living_saint", 1, 3, 1), #都主教安布罗吉奥·帕罗迪的1号私兵圣别人
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_4", "trp_hymn_knight_captain", 1, 4, 2), #都主教安布罗吉奥·帕罗迪的2号私兵圣歌骑士长
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_14", "trp_living_saint", 1, 1, 1), #主教伊莉莎·萨德尼亚的1号私兵圣别人
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_14", "trp_holy_bandit_cavalry", 4, 24, 2), #主教伊莉莎·萨德尼亚的2号私兵圣匪骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_35", "trp_living_saint", 1, 1, 1), #主教洛伦佐·巴里的1号私兵圣别人
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_35", "trp_saintly_thief_ranger", 4, 24, 2), #主教洛伦佐·巴里的2号私兵圣盗游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_6", "trp_sage_slayer", 1, 2, 1), #主教贝内代托·费雷罗的1号私兵圣人屠夫
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_6", "trp_holy_meat_epicure", 4, 24, 2), #主教贝内代托·费雷罗的2号私兵圣肉吞食者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_50", "trp_hymn_knight", 3, 15, 1), #教长扬尼·阿斯帝的1号私兵圣歌骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_23", "trp_holy_church_guard", 3, 21, 1), #教长罗伯特·科伦坡的1号私兵圣堂守卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_24", "trp_papal_zealot", 7, 28, 1), #教长罗莎里奥·费雷罗的1号私兵教国狂信徒
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_49", "trp_holy_smuggler", 6, 24, 1), #教长速穆勒·阿斯里托琴的1号私兵圣迹走私者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_49", "trp_armed_pilgrim", 9, 90, 2), #教长速穆勒·阿斯里托琴的2号私兵武装朝圣者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_19", "trp_sacred_object_thief", 6, 24, 1), #教长阿格尼斯·拉齐奥的1号私兵圣物窃贼
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_19", "trp_armed_pilgrim", 9, 90, 2), #教长阿格尼斯·拉齐奥的2号私兵武装朝圣者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_21", "trp_holy_meat_epicure", 3, 15, 1), #教长萨曼塔·罗希的1号私兵圣肉吞食者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_21", "trp_holy_blood_desirer", 6, 42, 2), #教长萨曼塔·罗希的2号私兵圣血渴求者
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_43", "trp_papal_senior_spearman", 6, 48, 1), #主教阿莱安娜·福贾的1号私兵教国资深矛兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_5", "trp_papal_senior_spearman", 6, 48, 1), #主教詹卢卡·科伦坡的1号私兵教国资深矛兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_22", "trp_papal_recruit_spearman", 5, 30, 1), #教长维吉利奥·帕罗迪的1号私兵教国征召矛兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_5_22", "trp_papal_recruit_militia", 8, 32, 2), #教长维吉利奥·帕罗迪的2号私兵教国征召民兵


     #斯塔胡克大公国
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_7_lord", "trp_bloodhonor_guard_captain", 1, 3, 1), #大公齐格弗里德·斯塔胡克的1号私兵血勋铁卫队长
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_7_lord", "trp_bloodhonor_guard", 3, 36, 2), #大公齐格弗里德·斯塔胡克的2号私兵血勋铁卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_2", "trp_starkhook_mangler_berserker", 4, 20, 1), #提督阿普伯爵的1号私兵斯塔胡克厉海狂战士
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_2", "trp_bloodburst_slave", 5, 30, 2), #提督阿普伯爵的2号私兵血缚者
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_11", "trp_starkhook_throwing_axe_master", 2, 12, 1), #提督克尔凯郭尔伯爵的1号私兵斯塔胡克飞斧大师
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_11", "trp_starkhook_throwing_axe_ranger", 3, 12, 2), #提督克尔凯郭尔伯爵的2号私兵斯塔胡克飞斧游侠
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_10", "trp_blood_hunter", 3, 15, 1), #提督迪内森伯爵的1号私兵戒血猎人
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_10", "trp_blood_lake_patrol_cavalry", 3, 15, 2), #提督迪内森伯爵的2号私兵血湖巡逻骑兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_4", "trp_light_bloodhonor_guard", 2, 15, 1), #提督冈瑟子爵的1号私兵轻装血勋铁卫
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_15", "trp_starkhook_bloody_berserker", 2, 12, 1), #提督拉尔斯男爵的1号私兵斯塔胡克血塔狂战士
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_15", "trp_bloodburst_slave", 5, 30, 2), #提督拉尔斯男爵的2号私兵血缚者
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_8", "trp_starkhook_enhanced_halberdman", 10, 40, 1), #提督海伍德男爵的1号私兵斯塔胡克血益斧手
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_14", "trp_blood_extinguisher", 4, 16, 1), #提督拉斯穆森子爵的1号私兵熄血射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_14", "trp_blood_lake_sentry", 4, 12, 2), #提督拉斯穆森子爵的2号私兵血湖哨兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_16", "trp_blood_sinner", 3, 12, 1), #提督伊萨克男爵的1号私兵鲜血罪人

     (call_script, "script_bodyguard_troop_import", "trp_knight_7_1", "trp_crimson_berserker", 4, 16, 1), #总督诺伯鲁侯爵的1号私兵猩红狂战士
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_1", "trp_red_moon_knight", 4, 20, 2), #总督诺伯鲁侯爵的2号私兵赤月骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_3", "trp_starkhook_knight", 5, 25, 1), #提督奥登伯爵的1号私兵斯塔胡克骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_3", "trp_starkhook_companion_infantry", 7, 35, 2), #提督奥登伯爵的2号私兵斯塔胡克伙友步兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_5", "trp_starkhook_blood_arrow_shooter", 4, 24, 1), #提督贝拉米子爵的1号私兵斯塔胡克血箭射手
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_6", "trp_starkhook_business_association_leader", 4, 20, 1), #提督巴内特子爵的1号私兵斯塔胡克商联队长
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_6", "trp_starkhook_business_association_rider", 6, 36, 2), #提督巴内特子爵的2号私兵斯塔胡克商联骑手
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_7", "trp_crimson_war_mage", 4, 24, 1), #提督斯捷潘男爵的1号私兵猩红战法师

     (call_script, "script_bodyguard_troop_import", "trp_knight_7_9", "trp_starkhook_business_armed_captain", 3, 12, 1), #提督索伦伯爵的1号私兵斯塔胡克武装船长
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_9", "trp_abyss_mercenary", 8, 48, 2), #提督索伦伯爵的2号私兵渊海佣兵
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_13", "trp_abyssal_surge_prowessman", 4, 16, 1), #提督勒克子爵的1号私兵深海巨蟒巨浪武夫
     (call_script, "script_bodyguard_troop_import", "trp_knight_7_12", "trp_abyss_mercenary", 6, 30, 1), #提督迪皮卡伯爵的1号私兵渊海佣兵


     #自由城邦
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_8_lord", "trp_scepter_knight_captain", 2, 10, 1), #执政官斯塔法诺爵士的1号私兵权杖骑士长
     (call_script, "script_bodyguard_troop_import", "trp_kingdom_8_lord", "trp_scepter_dismounted_knight", 4, 40, 2), #执政官斯塔法诺爵士的2号私兵权杖下马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_2", "trp_scepter_dismounted_knight", 4, 24, 1), #执政官斯尔维尔爵士的1号私兵权杖下马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_2", "trp_guilio_vamp", 5, 40, 2), #执政官斯尔维尔爵士的1号私兵古力奥妖妇
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_7", "trp_guilio_vamp", 4, 32, 1), #执政官尼可罗爵士的1号私兵古力奥妖妇
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_7", "trp_states_fortress_crossbowman", 4, 32, 2), #执政官尼可罗爵士的2号私兵自由城邦堡垒弩手

     (call_script, "script_bodyguard_troop_import", "trp_knight_8_3", "trp_scepter_knight_captain", 1, 8, 1), #执政官提兹安诺爵士的1号私兵权杖骑士长
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_3", "trp_scepter_dismounted_knight", 4, 24, 2), #执政官提兹安诺爵士的2号私兵权杖下马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_9", "trp_scepter_dismounted_knight", 4, 24, 1), #执政官法利法诺奥爵士的1号私兵权杖下马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_9", "trp_powell_rogue_knight", 4, 32, 2), #执政官法利法诺奥爵士的2号私兵普威尔无赖骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_1", "trp_scepter_dismounted_knight", 4, 24, 1), #执政官斯塔法诺爵士的1号私兵权杖下马骑士
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_1", "trp_skytear_sniper", 5, 40, 2), #执政官斯塔法诺爵士的2号私兵裂空狙击手
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_5", "trp_skytear_sniper", 4, 32, 1), #执政官理卡多爵士的1号私兵裂空狙击手
     (call_script, "script_bodyguard_troop_import", "trp_knight_8_5", "trp_powell_rogue_attendant", 4, 32, 2), #执政官理卡多爵士的2号私兵普威尔无赖扈从

     (call_script, "script_bodyguard_troop_import", "trp_knight_8_10", "trp_sheriff_rider", 8, 40, 1), #执政官比安奇奥爵士的1号私兵治安骑警
    ]),





  ("initial_faction_data", [
     (try_for_range, ":faction_no", "itm_faction_begin", "itm_faction_end"),
        (try_for_range, ":culture_faction_no", "fac_no_faction", "fac_faction_end"),
           (item_has_faction, ":faction_no", ":culture_faction_no"),
           (item_set_slot, ":faction_no", slot_item_faction_related, ":culture_faction_no"),
           (store_relation, ":total_relation", ":culture_faction_no", "fac_player_supporters_faction"),#根据玩家对其总阵营的关系，初始化每个小势力对玩家的关系
           (item_set_slot, ":faction_no", slot_faction_relation_with_player, ":total_relation"),
        (try_end),
     (try_end),

#######################################################创世与创生女神教#######################################################
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5", 0, "itm_creation_goddess_religion", 2),




##########################################################冒险者协会#######################################################
#勒塞夫冒险者协会
     (call_script, "script_set_faction_affiliation", "itm_powell_adventures_association", 0, "itm_adventurers_association", 1),
     (call_script, "script_set_faction_affiliation", "itm_powell_adventures_association_in_lesaff", 0, "itm_powell_adventures_association", 1),#勒塞夫分会
     (call_script, "script_set_faction_affiliation", "trp_sterling_branch_president", 1, "itm_powell_adventures_association_in_lesaff", 2),##斯特林分会长
     (call_script, "script_set_faction_affiliation", "trp_npc10", 1, "itm_powell_adventures_association_in_lesaff", 0),##劳瑞
     (call_script, "script_set_faction_affiliation", "trp_matton_adams", 1, "itm_powell_adventures_association_in_lesaff", 0),##马顿·亚当斯



##########################################################权厄之秤#######################################################
#勒塞夫分部
     (call_script, "script_set_faction_affiliation", "itm_libra_in_lesaff", 0, "itm_libra", 1),
     (call_script, "script_set_faction_affiliation", "itm_black_candle_gang", 0, "itm_libra_in_lesaff", 1),#黑烛帮
     (call_script, "script_set_faction_affiliation", "trp_anne_laure_deschamps", 1, "itm_black_candle_gang", 2),##安妮-洛尔·德尚男爵
     (call_script, "script_set_faction_affiliation", "itm_splitting_sail_brotherhood", 0, "itm_libra_in_lesaff", 1),#裂帆兄弟会
     (call_script, "script_set_faction_affiliation", "trp_marcel_chansonier", 1, "itm_splitting_sail_brotherhood", 2),#马塞尔·夏索尼埃




#领主在排序的时候，最好根据亲疏远近，比如一个城的城主和其下村装的领主基本上可以认为是同一派系的。目前虽然对此没有游戏内的明确规划，但可以作为参考。

##########################################################普威尔联合王国#######################################################

#————————————————————————————————联合王国直属—————————————————————————————————
##
     (call_script, "script_set_faction_template", "itm_kingdom_1", "pt_kingdom_1_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_1", "pt_kingdom_1_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_1", "pt_kingdom_1_reinforcements_c", 15, 3),
#圣龙骑士团
     (call_script, "script_set_faction_affiliation", "itm_order_of_holy_dragoon", 0, "itm_kingdom_1", 1),

#龙神教
     (call_script, "script_set_faction_affiliation", "itm_dragon_worship", 0, "itm_kingdom_1", 1),
     (call_script, "script_set_faction_affiliation", "itm_sedative_pavilion", 0, "itm_dragon_worship", 0),#镇静公馆
     (call_script, "script_set_faction_template", "itm_dragon_worship", "pt_dragon_worship_reinforcements_a", 80, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_dragon_worship", "pt_dragon_worship_reinforcements_b", 20, 2),

#合法拾荒队
     (call_script, "script_set_faction_affiliation", "itm_legal_scavenger", 0, "itm_kingdom_1", 0),

#————————————————————————————————普威尔中央—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_1_1", 0, "itm_kingdom_1", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_1_lord", 1, "itm_kingdom_1_1", 2),#国王克罗龙斯七世
     (call_script, "script_set_faction_affiliation", "trp_knight_1_17", 1, "itm_kingdom_1_1", 0),#拉法齐·雷克斯伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_50", 1, "itm_kingdom_1_1", 1),#多纳塔斯·杜波依斯侯爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_47", 1, "itm_kingdom_1_1", 1),#拉吉夫·勒罗伊伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_49", 1, "itm_kingdom_1_1", 0),#苏蒂里奥斯·梅西耶伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_44", 1, "itm_kingdom_1_1", 1),#佐尔·高提耶侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_59", 1, "itm_kingdom_1_1", 0),#塔维·缪顿男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_42", 1, "itm_kingdom_1_1", 1),#歌德弗鲁瓦·文森伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_60", 1, "itm_kingdom_1_1", 0),#尚利亚·多伊尔子爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_46", 1, "itm_kingdom_1_1", 1),#罗纳尔·舍瓦利侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_45", 1, "itm_kingdom_1_1", 1),#基文·马丁内兹伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_48", 1, "itm_kingdom_1_1", 0),#玛尼翁·乔利伯爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_15", 1, "itm_kingdom_1_1", 1),#雷蒙·希尔顿侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_34", 1, "itm_kingdom_1_1", 0),#伊冯娜·希尔顿勋爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_43", 1, "itm_kingdom_1_1", 1),#纪晓姆·杜朋伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_19", 1, "itm_kingdom_1_1", 0),#加布里埃勒·迪斯平子爵

     (call_script, "script_set_faction_template", "itm_kingdom_1_1", "pt_kingcity_citizen_reinforcements_a", 5, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_1_1", "pt_kingcity_citizen_reinforcements_b", 3, 2),
#王冠骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_1_1", 0, "itm_kingdom_1_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_1_1", 1, "itm_knight_order_1_1", 2),#大团长马格特·阿德勒
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_1_1", 1, "itm_knight_order_1_1", 1),
     #国家骑士团
     (call_script, "script_set_faction_affiliation", "itm_national_knights_order", 0, "itm_knight_order_1_1", 1),

#戒钟禁卫队
     (call_script, "script_set_faction_affiliation", "itm_tocsin_forbidden_guard", 0, "itm_kingdom_1_1", 0),

#肃正之镰
     (call_script, "script_set_faction_affiliation", "itm_eliminater", 0, "itm_kingdom_1_1", 0),
     (call_script, "script_set_faction_template", "itm_eliminater", "pt_eliminater_reinforcements", 0, 1),#部队模板

#王家元素研究院
     (call_script, "script_set_faction_affiliation", "itm_royal_element_research_institute", 0, "itm_kingdom_1_1", 1),

#国立龙学院
     (call_script, "script_set_faction_affiliation", "itm_national_dragon_college", 0, "itm_kingdom_1_1", 1),

#普威尔兵工厂
     (call_script, "script_set_faction_affiliation", "itm_powell_military_factory", 0, "itm_kingdom_1_1", 1),

#———————————————————————————————罗德里格斯公国—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_1_2", 0, "itm_kingdom_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_1_1", 1, "itm_kingdom_1_2", 2),#罗德里格斯公爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_20", 1, "itm_kingdom_1_2", 1),#克莉斯特
     (call_script, "script_set_faction_affiliation", "trp_knight_1_54", 1, "itm_kingdom_1_2", 0),#罗克兰·马克斯子爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_41", 1, "itm_kingdom_1_2", 1),#加斯东·鲁克斯伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_58", 1, "itm_kingdom_1_2", 0),#泽菲尔·李子爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_13", 1, "itm_kingdom_1_2", 1),#萨维尼安·尤尔伯利伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_32", 1, "itm_kingdom_1_2", 0),#奥克塔夫·尤尔伯利男爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_36", 1, "itm_kingdom_1_2", 1),#科莫·洛佩兹伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_52", 1, "itm_kingdom_1_2", 0),#莉艾·方丹伯爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_5", 1, "itm_kingdom_1_2", 1),#加西亚侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_24", 1, "itm_kingdom_1_2", 0),#格扎维埃·加西亚勋爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_14", 1, "itm_kingdom_1_2", 1),#勒内·威登伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_33", 1, "itm_kingdom_1_2", 0),#皮维·威登子爵

     (call_script, "script_set_faction_template", "itm_kingdom_1_2", "pt_rodriguez_duchy_reinforcements_a", 4, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_1_2", "pt_rodriguez_duchy_reinforcements_b", 2, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_1_2", "pt_grenier_militia_reinforcements", 3, 3),
#元素骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_1_2", 0, "itm_kingdom_1_2", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_1_2", 1, "itm_knight_order_1_2", 2),#大团长桑德南·卡逊
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_1_2", 1, "itm_knight_order_1_2", 1),#骑士长阿梅代·席尔瓦
     (call_script, "script_set_faction_affiliation", "trp_npc11", 1, "itm_knight_order_1_2", 0),#丽莲
     #血火佣兵团
     (call_script, "script_set_faction_affiliation", "itm_bloodfire_mercenary_corps", 0, "itm_knight_order_1_2", 0),
     (call_script, "script_set_faction_template", "itm_bloodfire_mercenary_corps", "pt_bloodfire_mercenary_reinforcements", 0, 1),#部队模板

#罗德里格斯商会
     (call_script, "script_set_faction_affiliation", "itm_rodriguez_firm", 0, "itm_kingdom_1_2", 1),

#戈兰尼尔民兵自卫军
     (call_script, "script_set_faction_affiliation", "itm_grenier_militia", 0, "itm_kingdom_1_2", 0),
     (call_script, "script_set_faction_affiliation", "trp_lance_protector_francois_beaumont", 1, "itm_grenier_militia", 2),#护枪官弗朗索瓦·博蒙
     (call_script, "script_set_faction_template", "itm_grenier_militia", "pt_grenier_militia_reinforcements", 0, 1),#部队模板

#罗德里格斯盾卫队
     (call_script, "script_set_faction_affiliation", "itm_holding_guard_order", 0, "itm_kingdom_1_2", 0),

#———————————————————————————————北境开拓领—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_1_3", 0, "itm_kingdom_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_1_2", 1, "itm_kingdom_1_3", 2),#伊格纳兹公爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_9", 1, "itm_kingdom_1_3", 1),#康坦·华洛夫伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_28", 1, "itm_kingdom_1_3", 0),#普罗斯佩耳·华洛夫男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_35", 1, "itm_kingdom_1_3", 1),#亚瑟·莱菲布勒侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_51", 1, "itm_kingdom_1_3", 0),#博尔奇·摩勒欧伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_10", 1, "itm_kingdom_1_3", 1),#菲利贝尔·温卡德伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_29", 1, "itm_kingdom_1_3", 0),#纳坦·温卡德男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_18", 1, "itm_kingdom_1_3", 0),#朱斯蒂纳·罗车巴斯伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_21", 1, "itm_kingdom_1_3", 0),#若阿尚·伊格纳兹子爵

     (call_script, "script_set_faction_template", "itm_kingdom_1_3", "pt_northern_reclaimer_reinforcements_a", 5, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_1_3", "pt_northern_reclaimer_reinforcements_b", 3, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_1_3", "pt_northern_reclaimer_reinforcements_c", 1, 3),
#龙血骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_1_3", 0, "itm_kingdom_1_3", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_1_3", 1, "itm_knight_order_1_3", 2),#大团长特杰德·巴赫
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_1_3", 1, "itm_knight_order_1_3", 1),

#龙狱
     (call_script, "script_set_faction_affiliation", "itm_dragon_prison", 0, "itm_kingdom_1_3", 0),
     (call_script, "script_set_faction_template", "itm_dragon_prison", "pt_brand_dragonmania_reinforcements", 0, 1),#部队模板

#无乡骑士团
     (call_script, "script_set_faction_affiliation", "itm_hometownless_knight_order", 0, "itm_kingdom_1_3", 0),

#———————————————————————————————普属自由城邦—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_1_4", 0, "itm_kingdom_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_1_3", 1, "itm_kingdom_1_4", 2),#派崔克公爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_53", 1, "itm_kingdom_1_4", 1),#尚德隆·里安德尔子爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_11", 1, "itm_kingdom_1_4", 1),#马丁·罗尔斯查德侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_7", 1, "itm_kingdom_1_4", 1),#斯特凡·埃克苏佩里侯爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_22", 1, "itm_kingdom_1_4", 1),#蒂埃里·派崔克勋爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_30", 1, "itm_kingdom_1_4", 0),#路易·罗尔斯查德伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_26", 1, "itm_kingdom_1_4", 0),#维尔日妮·埃克苏佩里子爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_38", 1, "itm_kingdom_1_4", 1),#奥托尼·密特朗伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_56", 1, "itm_kingdom_1_4", 0),#邓斯坦·史丹尼男爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_37", 1, "itm_kingdom_1_4", 1),#塞琉斯·卡斯特尔伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_57", 1, "itm_kingdom_1_4", 0),#史班瑟·路加男爵

     (call_script, "script_set_faction_template", "itm_kingdom_1_4", "pt_powell_state_reinforcements", 4, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_1_4", "pt_powell_orthodox_reinforcements", 2, 2),
#奉神骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_1_4", 0, "itm_kingdom_1_4", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_1_4", 1, "itm_knight_order_1_4", 2),#大团长拉切尔·加农
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_1_4", 1, "itm_knight_order_1_4", 1),

#普威尔正教
     (call_script, "script_set_faction_affiliation", "itm_powell_orthodox", 0, "itm_kingdom_1_4", 1),
     (call_script, "script_set_faction_affiliation", "itm_divine_swordsworn_seminary", 0, "itm_powell_orthodox", 1),
     (call_script, "script_set_faction_template", "itm_divine_swordsworn_seminary", "pt_powell_orthodox_reinforcements", 0, 1),#部队模板

#————————————————————————————————南沙公国—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_1_5", 0, "itm_kingdom_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_1_4", 1, "itm_kingdom_1_5", 2),#马哈茂德公爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_23", 1, "itm_kingdom_1_5", 0),#伊夫·马哈茂德勋爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_6", 1, "itm_kingdom_1_5", 1),#于里安·索恩德伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_25", 1, "itm_kingdom_1_5", 0),#托马·索恩德男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_39", 1, "itm_kingdom_1_5", 1),#特拉洛克·盖兰伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_55", 1, "itm_kingdom_1_5", 0),#巴伦·尼尔勋爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_8", 1, "itm_kingdom_1_5", 1),#萝萨·曼帕顿伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_27", 1, "itm_kingdom_1_5", 0),#西梅翁·曼帕顿男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_40", 1, "itm_kingdom_1_5", 1),#阿尔邦·福勒伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_16", 1, "itm_kingdom_1_5", 0),#奥迪莱·菲比子爵

     (call_script, "script_set_faction_affiliation", "trp_knight_1_12", 1, "itm_kingdom_1_5", 1),#瓦尔多·范德比尔特侯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_1_31", 1, "itm_kingdom_1_5", 0),#奥德蕾·范德比尔特男爵

     (call_script, "script_set_faction_template", "itm_kingdom_1_5", "pt_sousanth_duchy_reinforcements_a", 5, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_1_5", "pt_sousanth_duchy_reinforcements_b", 2, 2),
#沙舟骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_1_5", 0, "itm_kingdom_1_5", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_1_5", 1, "itm_knight_order_1_5", 2),#大团长拉瓦汗·帕克斯
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_1_5", 1, "itm_knight_order_1_5", 1),
     (call_script, "script_set_faction_affiliation", "itm_gurorrion_guard", 0, "itm_knight_order_1_5", 1),#古洛隆卫队




##########################################################伊希斯公国##########################################################

     (call_script, "script_set_faction_template", "itm_kingdom_2", "pt_kingdom_2_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_2", "pt_kingdom_2_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_2", "pt_kingdom_2_reinforcements_c", 15, 3),
#—————————————————————————————————灵魄之灵树—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_2_1", 0, "itm_kingdom_2", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_2_lord", 1, "itm_kingdom_2_1", 2),#辛希安·灵魂议长
     (call_script, "script_set_faction_affiliation", "trp_knight_2_5", 1, "itm_kingdom_2_1", 1),#嘉比里拉·灵魂议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_19", 1, "itm_kingdom_2_1", 0),#海洛伊斯·嘉比里拉议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_9", 1, "itm_kingdom_2_1", 1),#埃卡捷琳·灵魂议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_23", 1, "itm_kingdom_2_1", 0),#安东妮儿·埃卡捷琳议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_30", 1, "itm_kingdom_2_1", 1),#内莎·灵魂议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_28", 1, "itm_kingdom_2_1", 1),#凯缇亚·灵魂议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_11", 1, "itm_kingdom_2_1", 0),#爱德莱德·伊莲恩议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_14", 1, "itm_kingdom_2_1", 0),#赫尔娜·因格拉谬议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_12", 1, "itm_kingdom_2_1", 0),#奈伯尼尔·希尔维斯特议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_34", 1, "itm_kingdom_2_1", 0),#奥克莎·米萨议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_33", 1, "itm_kingdom_2_1", 0),#乔卡·特吉娜议员

     (call_script, "script_set_faction_template", "itm_kingdom_2_1", "pt_spirittree_of_soul_reinforcements_a", 30, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_2_1", "pt_spirittree_of_soul_reinforcements_b", 10, 2),
#灵树骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_2_1", 0, "itm_kingdom_2_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_2_1", 1, "itm_knight_order_2_1", 2),#大团长伊妮德·灵魂
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_2_1", 1, "itm_knight_order_2_1", 1),
     (call_script, "script_set_faction_affiliation", "itm_spiritual_horse_pasture", 0, "itm_knight_order_2_1", 1),#灵马牧场

#墨钢工坊
     (call_script, "script_set_faction_affiliation", "itm_grachite_workshop", 0, "itm_kingdom_2_1", 1),

#—————————————————————————————————死亡之灵树—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_2_2", 0, "itm_kingdom_2", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_2_1", 1, "itm_kingdom_2_2", 2),#伊芙琳·死亡代议长
     (call_script, "script_set_faction_affiliation", "trp_knight_2_15", 1, "itm_kingdom_2_2", 0),#菲丽斯·伊芙琳议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_7", 1, "itm_kingdom_2_2", 1),#尤拉诺斯·死亡议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_21", 1, "itm_kingdom_2_2", 0),#芝妮雅·尤拉诺斯议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_26", 1, "itm_kingdom_2_2", 1),#茱丽莎·死亡议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_29", 1, "itm_kingdom_2_2", 1),#戴瑞那·死亡议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_31", 1, "itm_kingdom_2_2", 0),#塔芭斯·佩莱卡议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_37", 1, "itm_kingdom_2_2", 0),#斯哈维·艾瑞琦娜议员

     (call_script, "script_set_faction_template", "itm_kingdom_2_2", "pt_spirittree_of_demise_reinforcements_a", 30, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_2_2", "pt_spirittree_of_demise_reinforcements_b", 10, 2),
#灵雨游侠团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_2_2", 0, "itm_kingdom_2_2", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_2_2", 1, "itm_knight_order_2_2", 2),#大团长葛加斯塔芙·死亡
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_2_2", 1, "itm_knight_order_2_2", 1),

#冰河探险队
     (call_script, "script_set_faction_affiliation", "itm_glacier_exploration_team", 0, "itm_kingdom_2_2", 0),

#—————————————————————————————————先祖之灵树—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_2_3", 0, "itm_kingdom_2", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_2_2", 1, "itm_kingdom_2_3", 2),#绯雷德翠卡·先祖代议长
     (call_script, "script_set_faction_affiliation", "trp_knight_2_16", 1, "itm_kingdom_2_3", 0),#孟莉萨·绯雷德翠卡议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_6", 1, "itm_kingdom_2_3", 1),#奥克塔薇·先祖议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_20", 1, "itm_kingdom_2_3", 0),#葛丽歇达·奥克塔薇议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_10", 1, "itm_kingdom_2_3", 1),#加菲尔德·先祖议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_24", 1, "itm_kingdom_2_3", 0),#克洛怡·加菲尔德议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_27", 1, "itm_kingdom_2_3", 1),#瑟欧密斯·先祖议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_35", 1, "itm_kingdom_2_3", 0),#安吉丽娜·奥德瑞议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_38", 1, "itm_kingdom_2_3", 0),#塔玛尔·瓦尔卡议员

     (call_script, "script_set_faction_template", "itm_kingdom_2_3", "pt_molter_legion_reinforcements", 30, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_2_3", "pt_spirittree_of_ancester_reinforcements", 10, 2),
#永世者刺客团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_2_3", 0, "itm_kingdom_2_3", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_2_3", 1, "itm_knight_order_2_3", 2),#永世者奥蒂列特·先祖
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_2_3", 1, "itm_knight_order_2_3", 1),

#嘉果园
     (call_script, "script_set_faction_affiliation", "itm_great_apple_garden", 0, "itm_kingdom_2_3", 1),
#蜕生者战团
     (call_script, "script_set_faction_affiliation", "itm_molter_legion", 0, "itm_kingdom_2_3", 0),
     (call_script, "script_set_faction_template", "itm_molter_legion", "pt_molter_legion_reinforcements", 0, 1),#部队模板

#库勒斯煤矿
     (call_script, "script_set_faction_affiliation", "itm_kules_coal_mine", 0, "itm_kingdom_2_3", 1),

#—————————————————————————————————生命之灵树—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_2_4", 0, "itm_kingdom_2", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_2_3", 1, "itm_kingdom_2_4", 2),#珍妮芙·生命代议长
     (call_script, "script_set_faction_affiliation", "trp_knight_2_17", 1, "itm_kingdom_2_4", 1),#奥利维塔·珍妮芙议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_25", 1, "itm_kingdom_2_4", 1),#莱伊拉·生命议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_36", 1, "itm_kingdom_2_4", 0),#雪帕·伊亚莉娜议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_4", 1, "itm_kingdom_2_4", 1),#尤莱雅·生命议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_18", 1, "itm_kingdom_2_4", 0),#娜提雅维达·尤莱雅议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_8", 1, "itm_kingdom_2_4", 1),#维兰·生命议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_22", 1, "itm_kingdom_2_4", 0),#爱德文娜·维兰议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_13", 1, "itm_kingdom_2_4", 0),#诺亚·朱莉尔思议员
     (call_script, "script_set_faction_affiliation", "trp_knight_2_32", 1, "itm_kingdom_2_4", 0),#海瑞丝·法耶议员

     (call_script, "script_set_faction_template", "itm_kingdom_2_4", "pt_yishith_westcoast_militia_reinforcements", 60, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_2_4", "pt_spirittree_of_vita_reinforcements", 10, 2),
#灵风游骑团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_2_4", 0, "itm_kingdom_2_4", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_2_4", 1, "itm_knight_order_2_4", 2),#大团长利蒂西娅·生命
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_2_4", 1, "itm_knight_order_2_4", 1),

#伊希斯人类西海自警团
     (call_script, "script_set_faction_affiliation", "itm_yishith_westcoast_militia", 0, "itm_kingdom_2_4", 1),
     (call_script, "script_set_faction_template", "itm_yishith_westcoast_militia", "pt_yishith_westcoast_militia_reinforcements", 0, 1),#部队模板

#雪泥商会
     (call_script, "script_set_faction_affiliation", "itm_snow_trading_company", 0, "itm_kingdom_2_4", 0),




##########################################################科鲁托酋长国##########################################################

     (call_script, "script_set_faction_template", "itm_kingdom_3", "pt_kingdom_3_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_3", "pt_kingdom_3_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_3", "pt_kingdom_3_reinforcements_c", 15, 3),
#—————————————————————————————————图腾同盟—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_3_1", 0, "itm_kingdom_3", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_3_lord", 1, "itm_kingdom_3_1", 2),#阿古达木可汗
     (call_script, "script_set_troop_conscription_mode", "trp_kingdom_3_lord", rsm_tribe, 150, "pt_lion_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_7", 1, "itm_kingdom_3_1", 1),#“英雄”巴特尔
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_7", rsm_tribe, 150, "pt_lion_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_19", 1, "itm_kingdom_3_1", 1),#“硬铁”帖木日布赫
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_19", rsm_tribe, 150, "pt_lion_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_11", 1, "itm_kingdom_3_1", 0),#“长矛”吉达
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_11", rsm_tribe, 150, "pt_lion_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_12", 1, "itm_kingdom_3_1", 0),#“邋遢”努桑哈
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_12", rsm_tribe, 150, "pt_lion_tribe_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_3_22", 1, "itm_kingdom_3_1", 1),#“飞虎”尼格斯巴日
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_22", rsm_tribe, 150, "pt_tiger_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_33", 1, "itm_kingdom_3_1", 0),#“暴富”巴亚金
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_33", rsm_tribe, 150, "pt_tiger_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_4", 1, "itm_kingdom_3_1", 1),#“铁块”特木尔酋长
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_4", rsm_tribe, 150, "pt_bear_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_16", 1, "itm_kingdom_3_1", 0),#“凸目”波勒特和日
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_16", rsm_tribe, 150, "pt_bear_tribe_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_3_25", 1, "itm_kingdom_3_1", 1),#“河流”牧仁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_25", rsm_tribe, 150, "pt_wolf_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_34", 1, "itm_kingdom_3_1", 0),#“炎热”阿给玛
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_34", rsm_tribe, 150, "pt_wolf_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_8", 1, "itm_kingdom_3_1", 1),#“魁梧”拉克申
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_8", rsm_tribe, 150, "pt_bear_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_20", 1, "itm_kingdom_3_1", 0),#“坚固”巴图布赫
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_20", rsm_tribe, 150, "pt_bear_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_6", 1, "itm_kingdom_3_1", 1),#“石头”朝鲁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_6", rsm_tribe, 150, "pt_bear_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_18", 1, "itm_kingdom_3_1", 0),#“大力”呼其图
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_18", rsm_tribe, 150, "pt_bear_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_21", 1, "itm_kingdom_3_1",1),#“歼敌”岱森达日
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_21", rsm_tribe, 150, "pt_wolf_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_32", 1, "itm_kingdom_3_1", 0),#“全都要”古日
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_32", rsm_tribe, 150, "pt_wolf_tribe_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_3_26", 1, "itm_kingdom_3_1", 1),#“飞鹰”少布
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_26", rsm_tribe, 150, "pt_wolf_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_28", 1, "itm_kingdom_3_1", 0),#“和平”恩金
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_28", rsm_tribe, 150, "pt_wolf_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_9", 1, "itm_kingdom_3_2", 1),#“威武”苏日勒和克
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_9", rsm_tribe, 150, "pt_tiger_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_30", 1, "itm_kingdom_3_2", 0),#“干眼睛”陶日崩
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_30", rsm_tribe, 150, "pt_tiger_tribe_reinforcements"), 

#科鲁托剑斗旅团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_3_1", 0, "itm_kingdom_3_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_3_1", 1, "itm_knight_order_3_1", 2),#旅团长思钦巴日
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_3_1", 1, "itm_knight_order_3_1", 1),

#科鲁托辅助军
     (call_script, "script_set_faction_affiliation", "itm_kouruto_auxiliary", 0, "itm_kingdom_3_1", 1),
     (call_script, "script_set_faction_template", "itm_kouruto_auxiliary", "pt_kouruto_auxiliary_reinforcements", 0, 1),#部队模板

#铁峰守备旅团
     (call_script, "script_set_faction_affiliation", "itm_ironpeak_garrison_brigade", 0, "itm_kingdom_3_1", 1),
     (call_script, "script_set_faction_affiliation", "itm_ironbite_gang", 0, "itm_ironpeak_garrison_brigade", 2),#啮铁帮

#洪炉监视旅团
     (call_script, "script_set_faction_affiliation", "itm_furnace_watch_brigade", 0, "itm_kingdom_3_1", 0),
     (call_script, "script_set_faction_template", "itm_furnace_watch_brigade", "pt_furnace_watch_brigade_reinforcements", 0, 1),#部队模板


#—————————————————————————————————麦汗族—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_3_2", 0, "itm_kingdom_3", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_3_1", 1, "itm_kingdom_3_2", 2),#大酋长“柱子”巴根
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_1", rsm_tribe, 150, "pt_cow_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_23", 1, "itm_kingdom_3_2", 1),#“好人”宁金
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_23", rsm_tribe, 150, "pt_rabbit_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_13", 1, "itm_kingdom_3_2", 0),#“竖耳”德勒德格日
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_13", rsm_tribe, 150, "pt_rabbit_tribe_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_3_27", 1, "itm_kingdom_3_2", 1),#“好运”吉雅赛音
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_27", rsm_tribe, 150, "pt_sheep_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_29", 1, "itm_kingdom_3_2", 0),#“星枝”奥敦木其尔
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_29", rsm_tribe, 150, "pt_sheep_tribe_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_3_24", 1, "itm_kingdom_3_2", 1),#“大山”阿古拉
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_24", rsm_tribe, 150, "pt_cow_tribe_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_3_10", 1, "itm_kingdom_3_1", 1),#“金钱豹”伊日毕斯
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_10", rsm_tribe, 150, "pt_deer_tribe_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_3_31", 1, "itm_kingdom_3_1", 0),#“威严”苏日立格
     (call_script, "script_set_troop_conscription_mode", "trp_knight_3_31", rsm_tribe, 150, "pt_deer_tribe_reinforcements"), 

#炉边萨满联盟
     (call_script, "script_set_faction_affiliation", "itm_fireside_circle_of_shaman", 0, "itm_kingdom_3_2", 1),


#—————————————————————————————————金爪子帮—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_3_3", 0, "itm_kingdom_3", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_3_2", 1, "itm_kingdom_3_3", 2),#大酋长“兴隆”满都拉图
     (call_script, "script_set_faction_affiliation", "trp_knight_3_14", 1, "itm_kingdom_3_3", 0),#“扁头”哈布其克
     (call_script, "script_set_faction_affiliation", "trp_knight_3_5", 1, "itm_kingdom_3_3", 1),#“黑虎”哈尔巴拉
     (call_script, "script_set_faction_affiliation", "trp_knight_3_17", 1, "itm_kingdom_3_3", 0),#“白小子”查干夫

     (call_script, "script_set_faction_template", "itm_kingdom_3_3", "pt_goldclaw_reinforcements", 80, 1),#部队模板
#金爪子商会
     (call_script, "script_set_faction_affiliation", "itm_goldclaw_guild", 0, "itm_kingdom_3_3", 1),

#不死者猎杀旅团
     (call_script, "script_set_faction_affiliation", "itm_undead_slayer_brigade", 0, "itm_kingdom_3_3", 0),


#—————————————————————————————————守望派—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_3_4", 0, "itm_kingdom_3", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_3_3", 1, "itm_kingdom_3_4", 2),#大酋长“斧头”苏合
     (call_script, "script_set_faction_affiliation", "trp_knight_3_15", 1, "itm_kingdom_3_4", 1),#“凹脸”翁和日

     (call_script, "script_set_faction_template", "itm_kingdom_3_4", "pt_sentinel_clique_reinforcements", 80, 1),#部队模板
#守望者卫戍旅团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_3_2", 0, "itm_kingdom_3_4", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_3_2", 1, "itm_knight_order_3_2", 2),#旅团长明安温都思
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_3_2", 1, "itm_knight_order_3_2", 1),


#—————————————————————————————————人子之刃—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_3_5", 0, "itm_kingdom_3", 0),
     (call_script, "script_set_faction_affiliation", "trp_knight_3_35", 1, "itm_kingdom_3_5", 2),#女酋长“精明”司晨黛




########################################################乌-迪默-安基亚邦联#######################################################

     (call_script, "script_set_faction_template", "itm_kingdom_4", "pt_kingdom_4_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_4", "pt_kingdom_4_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_4", "pt_kingdom_4_reinforcements_c", 15, 3),
#—————————————————————————————————黑沼议事会—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_4_1", 0, "itm_kingdom_4", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_4_lord", 1, "itm_kingdom_4_1", 2),#女皇依文洁琳·昆庭
     (call_script, "script_set_troop_conscription_mode", "trp_kingdom_4_lord", rsm_mercenary, 50, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_7", 1, "itm_kingdom_4_1", 1),#伯爵哈罗德·柏邵斯
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_7", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_10", 1, "itm_kingdom_4_1", 1),#伯爵特尔格·郝根
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_10", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_24", 1, "itm_kingdom_4_1", 0),#男爵克努特·郝根
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_24", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_11", 1, "itm_kingdom_4_1", 0),#子爵罗格森·哈根
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_11", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_14", 1, "itm_kingdom_4_1", 0),#子爵奥尔卡·贝尔格
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_14", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_28", 1, "itm_kingdom_4_4", 1),#伯爵哈坎·梅基宁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_28", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_31", 1, "itm_kingdom_4_4", 1),#伯爵哈登·瓦尔克帕
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_31", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_38", 1, "itm_kingdom_4_4", 0),#男爵金·马林
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_38", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_26", 1, "itm_kingdom_4_1", 1),#伯爵托伊沃·科诺宁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_26", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_27", 1, "itm_kingdom_4_1", 1),#伯爵翁尼·佩卡宁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_27", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_29", 1, "itm_kingdom_4_1", 1),#伯爵汉斯·尼布鲁姆
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_29", rsm_mercenary, 50, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_30", 1, "itm_kingdom_4_1", 1),#选帝侯尼尔斯·赖科宁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_30", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_37", 1, "itm_kingdom_4_1", 0),#子爵奥伊瓦·阿赫蒂萨里
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_37", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_12", 1, "itm_kingdom_4_1", 0),#子爵艾尔瑞克·雅各布森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_12", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_21", 1, "itm_kingdom_4_1", 0),#男爵俄丽克·哈罗德森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_21", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_template", "itm_kingdom_4_1", "pt_black_marsh_council_reinforcements_a", 8, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_4_1", "pt_black_marsh_council_reinforcements_b", 5, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_4_1", "pt_black_marsh_council_reinforcements_c", 2, 3),
#光瘴学派
     (call_script, "script_set_faction_affiliation", "itm_knight_order_4_1", 0, "itm_kingdom_4_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_4_1", 1, "itm_knight_order_4_1", 1),
     (call_script, "script_set_faction_affiliation", "itm_lord_of_myriad_altars", 0, "itm_knight_order_4_1", 2),#万龛之主
     (call_script, "script_set_faction_affiliation", "trp_knight_master_4_1", 1, "itm_lord_of_myriad_altars", 2),#选帝侯尼克勒斯·哈格尔伯格

#司奴局
     (call_script, "script_set_faction_affiliation", "itm_slave_bureau", 0, "itm_kingdom_4_1", 1),

#暗沼之花佣兵团
     (call_script, "script_set_faction_affiliation", "itm_marsh_flower_landsknechts", 0, "itm_kingdom_4_1", 1),
     (call_script, "script_set_faction_template", "itm_marsh_flower_landsknechts", "pt_marsh_flower_reinforcements_a", 70, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_marsh_flower_landsknechts", "pt_marsh_flower_reinforcements_b", 30, 2),


#—————————————————————————————————乌尔之子女—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_4_2", 0, "itm_kingdom_4", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_4_1", 1, "itm_kingdom_4_2", 2),#选帝侯伊登·艾萨克
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_1", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_15", 1, "itm_kingdom_4_2", 1),#男爵雷耶克·伊登森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_15", rsm_mercenary, 50, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_4", 1, "itm_kingdom_4_2", 1),#侯爵瑞马尔德·谢勒森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_4", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_18", 1, "itm_kingdom_4_2", 0),#男爵吉尔丝·瑞马尔德森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_18", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_8", 1, "itm_kingdom_4_2", 1),#伯爵鲁德·汉森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_8", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_22", 1, "itm_kingdom_4_2", 0),#男爵拉尔斯·鲁德森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_22", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_9", 1, "itm_kingdom_4_2", 1),#伯爵海达·乌勒森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_9", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_23", 1, "itm_kingdom_4_2", 0),#男爵莱芙·海达森
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_23", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_template", "itm_kingdom_4_2", "pt_offspring_of_uhr_reinforcements_a", 30, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_4_2", "pt_offspring_of_uhr_reinforcements_b", 2, 2),
#深海恐惧刺客团
     (call_script, "script_set_faction_affiliation", "itm_dread_of_the_deep", 0, "itm_kingdom_4_2", 1),
     (call_script, "script_set_faction_affiliation", "itm_deep_binder", 0, "itm_dread_of_the_deep", 1),#深邃封印团

#—————————————————————————————————净世军—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_4_3", 0, "itm_kingdom_4", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_4_2", 1, "itm_kingdom_4_3", 1),#选帝侯伊阿亚·斯旺达斯特
     (call_script, "script_set_faction_affiliation", "trp_knight_4_16", 1, "itm_kingdom_4_3", 0),#男爵迪里刚·斯旺达斯特
     (call_script, "script_set_faction_affiliation", "trp_knight_4_13", 1, "itm_kingdom_4_3", 0),#子爵法恩·哈勒沃森

     (call_script, "script_set_faction_affiliation", "trp_knight_4_6", 1, "itm_kingdom_4_3", 1),#侯爵阿斯特里德·度勒郝格
     (call_script, "script_set_faction_affiliation", "trp_knight_4_20", 1, "itm_kingdom_4_3", 0),#男爵各勒塔·度勒郝格

     (call_script, "script_set_faction_affiliation", "trp_knight_4_25", 1, "itm_kingdom_4_3", 1),#侯爵哈里·维尔塔宁
     (call_script, "script_set_faction_affiliation", "trp_knight_4_36", 1, "itm_kingdom_4_3", 0),#子爵马尔科·涅米宁

     (call_script, "script_set_faction_affiliation", "trp_knight_4_5", 1, "itm_kingdom_4_3", 1),#侯爵图亚·图热森
     (call_script, "script_set_faction_affiliation", "trp_knight_4_19", 1, "itm_kingdom_4_3", 0),#男爵索尔顿·图亚森

     (call_script, "script_set_faction_template", "itm_kingdom_4_3", "pt_purifier_reinforcements_a", 75, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_4_3", "pt_purifier_reinforcements_b", 7, 2),
#神牙修道军
     (call_script, "script_set_faction_affiliation", "itm_knight_order_4_2", 0, "itm_kingdom_4_3", 2),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_4_2", 1, "itm_knight_order_4_2", 2),#选帝侯哈帝·琼森修道长
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_4_2", 1, "itm_knight_order_4_2", 1),
     #鹰圣苦修会
     (call_script, "script_set_faction_affiliation", "itm_eagle_saint_hardship_seminary", 0, "itm_knight_order_4_2", 1),


#—————————————————————————————————食莲人沙龙—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_4_4", 0, "itm_kingdom_4", 0),
     (call_script, "script_set_faction_affiliation", "trp_knight_4_3", 1, "itm_kingdom_4_4", 2),#选帝侯奥拉夫·特吕伊鲁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_3", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_17", 1, "itm_kingdom_4_4", 0),#男爵勒纳·特吕伊鲁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_17", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_4_32", 1, "itm_kingdom_4_4", 0),#伯爵奥吉·哈马莱宁
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_32", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_33", 1, "itm_kingdom_4_4", 1),#侯爵海尔维·瓦洛
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_33", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_34", 1, "itm_kingdom_4_4", 0),#伯爵西蒙·尼尼托斯
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_34", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_4_35", 1, "itm_kingdom_4_4", 0),#伯爵莉雅·郝吉奥 
     (call_script, "script_set_troop_conscription_mode", "trp_knight_4_35", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_template", "itm_kingdom_4_4", "pt_lotus_eater_reinforcements", 30, 1),#部队模板
#—————————————————————————————————人类狩猎者—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_human_hunter", 0, "itm_kingdom_4", 0),
     (call_script, "script_set_faction_template", "itm_human_hunter", "pt_human_hunter_reinforcements", 0, 1),#部队模板



###########################################################教皇国#######################################################

     (call_script, "script_set_faction_template", "itm_kingdom_5", "pt_kingdom_5_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_5", "pt_kingdom_5_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_5", "pt_kingdom_5_reinforcements_c", 15, 3),
#——————————————————————————————————圣廷—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5_1", 0, "itm_kingdom_5", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_5_lord", 1, "itm_kingdom_5_1", 2),#教皇孔苏斯三世
     (call_script, "script_set_faction_affiliation", "trp_knight_5_18", 1, "itm_kingdom_5_1", 0),#教长古列尔莫·阿布鲁佐
     (call_script, "script_set_faction_affiliation", "trp_knight_5_29", 1, "itm_kingdom_5_1", 0),#教长米卡兰吉洛·翁布里亚
     (call_script, "script_set_faction_affiliation", "trp_knight_5_28", 1, "itm_kingdom_5_1", 0),#教长萨德罗·瓦勒

     (call_script, "script_set_faction_affiliation", "trp_knight_5_10", 1, "itm_kingdom_5_1", 1),#主教伊曼纽尔·瓦勒
     (call_script, "script_set_faction_affiliation", "trp_knight_5_31", 1, "itm_kingdom_5_1", 0),#教长马尔克龙·西西里

     (call_script, "script_set_faction_affiliation", "trp_knight_5_13", 1, "itm_kingdom_5_1", 1),#主教约书亚·西西里
     (call_script, "script_set_faction_affiliation", "trp_knight_5_27", 1, "itm_kingdom_5_1", 0),#教长拉法勒·维尼托

     (call_script, "script_set_faction_affiliation", "trp_knight_5_38", 1, "itm_kingdom_5_1", 1),#主教保罗·比萨
     (call_script, "script_set_faction_affiliation", "trp_knight_5_53", 1, "itm_kingdom_5_1", 0),#教长泰·罗戈维

     (call_script, "script_set_faction_affiliation", "trp_knight_5_37", 1, "itm_kingdom_5_1", 1),#主教奥马尔·奥特兰托
     (call_script, "script_set_faction_affiliation", "trp_knight_5_55", 1, "itm_kingdom_5_1", 0),#教长达奇·坎波迪梅莱

     (call_script, "script_set_faction_affiliation", "trp_knight_5_9", 1, "itm_kingdom_5_1", 1),#主教奥雷里奥·维尼托
     (call_script, "script_set_faction_affiliation", "trp_knight_5_30", 1, "itm_kingdom_5_1", 0),#教长马思米利安诺·托斯卡纳

#圣骑士团
     (call_script, "script_set_faction_affiliation", "itm_order_of_holy_knight", 0, "itm_kingdom_5_1", 1),

#宗座骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_5_1", 0, "itm_kingdom_5_1", 0),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_5_1", 1, "itm_knight_order_5_1", 2),#队长阿利安罗德·勒乌
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_5_1", 1, "itm_knight_order_5_1", 1),

#圣誓剑勇团
     (call_script, "script_set_faction_affiliation", "itm_order_of_godward_warrior", 0, "itm_kingdom_5_1", 1),
#永眠回廊
     (call_script, "script_set_faction_affiliation", "itm_eternal_galleries", 0, "itm_kingdom_5_1", 1),
#弓圣遗泽射手团
     (call_script, "script_set_faction_affiliation", "itm_legacy_of_the_bow_saint", 0, "itm_kingdom_5_1", 0),


#——————————————————————————————————证信宗—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5_2", 0, "itm_kingdom_5", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_5_1", 1, "itm_kingdom_5_2", 2),#都主教奥格斯特·拉齐奥
     (call_script, "script_set_faction_affiliation", "trp_knight_5_56", 1, "itm_kingdom_5_2", 0),#教长罗斯科·月玛德纳
     (call_script, "script_set_faction_affiliation", "trp_knight_5_26", 1, "itm_kingdom_5_2", 0),#教长萨瓦托·法夫

     (call_script, "script_set_faction_affiliation", "trp_knight_5_40", 1, "itm_kingdom_5_2", 1),#主教布鲁娜·加尔达
     (call_script, "script_set_faction_affiliation", "trp_knight_5_57", 1, "itm_kingdom_5_2", 0),#教长邓高夫·提契诺

     (call_script, "script_set_faction_affiliation", "trp_knight_5_36", 1, "itm_kingdom_5_2", 1),#主教马特奥·都立
     (call_script, "script_set_faction_affiliation", "trp_knight_5_25", 1, "itm_kingdom_5_2", 0),#教长苏缪勒·鲁索

     (call_script, "script_set_faction_affiliation", "trp_knight_5_41", 1, "itm_kingdom_5_2", 1),#主教富尔维奥·贝加莫
     (call_script, "script_set_faction_affiliation", "trp_knight_5_58", 1, "itm_kingdom_5_2", 0),#教长乔坤·帕尔马

     (call_script, "script_set_faction_affiliation", "trp_knight_5_42", 1, "itm_kingdom_5_2", 1),#主教伊拉里奥·弗雷斯卡蒂
     (call_script, "script_set_faction_affiliation", "trp_knight_5_51", 1, "itm_kingdom_5_2", 0),#教长奥兹·威尼托

     (call_script, "script_set_faction_template", "itm_kingdom_5_2", "pt_sin_slave_legion_reinforcements", 2, 1),#部队模板
#狩魔骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_5_2", 0, "itm_kingdom_5_2", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_5_2", 1, "itm_knight_order_5_2", 2),#大团长“血门”狄提朗伯斯
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_5_2", 1, "itm_knight_order_5_2", 1),
     #异端猎手队
     (call_script, "script_set_faction_affiliation", "itm_heretic_killer", 0, "itm_knight_order_5_2", 1),

#宗教审判局
     (call_script, "script_set_faction_affiliation", "itm_religious_trial_bureau", 0, "itm_kingdom_5_2", 1),
#罪奴辅助军团
     (call_script, "script_set_faction_affiliation", "itm_sin_slave_legion", 0, "itm_kingdom_5_2", 1),
     (call_script, "script_set_faction_template", "itm_sin_slave_legion", "pt_sin_slave_legion_reinforcements", 0, 1),#部队模板

#噬罪秘修会
     (call_script, "script_set_faction_affiliation", "itm_sect_of_devouring_sin", 0, "itm_kingdom_5_2", 0),


#—————————————————————————————————真信施洗会—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5_3", 0, "itm_kingdom_5", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_5_2", 1, "itm_kingdom_5_3", 2),#都主教阿蒙瑞·萨顿
     (call_script, "script_set_faction_affiliation", "trp_knight_5_32", 1, "itm_kingdom_5_3", 0),#教长伊莎贝拉·萨德尼亚
     (call_script, "script_set_faction_affiliation", "trp_knight_5_46", 1, "itm_kingdom_5_3", 0),#教长蒂奇亚诺·卡拉布里亚

     (call_script, "script_set_faction_affiliation", "trp_knight_5_12", 1, "itm_kingdom_5_3", 1),#主教詹卡洛·托斯卡纳
     (call_script, "script_set_faction_affiliation", "trp_knight_5_48", 1, "itm_kingdom_5_3", 0),#教长科洛玛·埃尔巴

     (call_script, "script_set_faction_affiliation", "trp_knight_5_39", 1, "itm_kingdom_5_3", 1),#主教帕斯夸尔·奥斯塔
     (call_script, "script_set_faction_affiliation", "trp_knight_5_47", 1, "itm_kingdom_5_3", 0),#教长斯特凡诺·特里雅斯特

     (call_script, "script_set_faction_affiliation", "trp_knight_5_11", 1, "itm_kingdom_5_3", 1),#主教费德里科·翁布里亚
     (call_script, "script_set_faction_affiliation", "trp_knight_5_54", 1, "itm_kingdom_5_3", 0),#教长奥克斯·普尔加托里奥

     (call_script, "script_set_faction_affiliation", "trp_knight_5_34", 1, "itm_kingdom_5_3", 1),#主教果戈里·巴勒莫
     (call_script, "script_set_faction_affiliation", "trp_knight_5_33", 1, "itm_kingdom_5_3", 1),#主教阿尔菲奥·布林迪西

     (call_script, "script_set_faction_template", "itm_kingdom_5_3", "pt_baptized_legion_reinforcements", 2, 1),#部队模板
#庇护骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_5_3", 0, "itm_kingdom_5_3", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_5_3", 1, "itm_knight_order_5_3", 2),#大团长露丝拉·查尼
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_5_3", 1, "itm_knight_order_5_3", 1),
     #查尼骑兵团
     (call_script, "script_set_faction_affiliation", "itm_chaney_cavalry_army", 0, "itm_knight_order_5_3", 0),

#萨顿卫兵团
     (call_script, "script_set_faction_affiliation", "itm_sutton_guard", 0, "itm_kingdom_5_3", 0),
#绘盾人
     (call_script, "script_set_faction_affiliation", "itm_shield_drawing_man", 0, "itm_kingdom_5_3", 0),


#—————————————————————————————————神哲修道宗—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5_4", 0, "itm_kingdom_5", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_5_3", 1, "itm_kingdom_5_4", 2),#都主教阿拉蒂诺·罗希
     (call_script, "script_set_faction_affiliation", "trp_knight_5_16", 1, "itm_kingdom_5_4", 0),#教长卡特琳娜·弗留利
     (call_script, "script_set_faction_affiliation", "trp_knight_5_17", 1, "itm_kingdom_5_4", 0),#教长西蒙娜·卡拉布里亚

     (call_script, "script_set_faction_affiliation", "trp_knight_5_7", 1, "itm_kingdom_5_4", 1),#主教卡米洛·鲁索
     (call_script, "script_set_faction_affiliation", "trp_knight_5_15", 1, "itm_kingdom_5_4", 0),#教长伊莱诺拉·利古里亚

     (call_script, "script_set_faction_affiliation", "trp_knight_5_45", 1, "itm_kingdom_5_4", 1),#主教米克罗·多洛米泰斯
     (call_script, "script_set_faction_affiliation", "trp_knight_5_52", 1, "itm_kingdom_5_4", 0),#教长卡洛特·罗马涅

     (call_script, "script_set_faction_affiliation", "trp_knight_5_8", 1, "itm_kingdom_5_4", 1),#主教卡梅罗·法夫
     (call_script, "script_set_faction_affiliation", "trp_knight_5_20", 1, "itm_kingdom_5_4", 0),#教长曼努埃拉·萨顿

     (call_script, "script_set_faction_affiliation", "trp_knight_5_44", 1, "itm_kingdom_5_4", 1),#主教爱德华·奇思里奥

#奥术骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_5_4", 0, "itm_kingdom_5_4", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_5_4", 1, "itm_knight_order_5_4", 2),#大团长汤姆逊·里尔德
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_5_4", 1, "itm_knight_order_5_4", 1),

#哲学之卵学派
     (call_script, "script_set_faction_affiliation", "itm_egg_of_philosophy_school", 0, "itm_kingdom_5_4", 0),


#—————————————————————————————————圣别渴求者—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5_5", 0, "itm_kingdom_5", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_5_4", 1, "itm_kingdom_5_5", 2),#都主教安布罗吉奥·帕罗迪
     (call_script, "script_set_faction_affiliation", "trp_knight_5_50", 1, "itm_kingdom_5_5", 0),#教长扬尼·阿斯帝
     (call_script, "script_set_faction_affiliation", "trp_knight_5_23", 1, "itm_kingdom_5_5", 0),#教长罗伯特·科伦坡
     (call_script, "script_set_faction_affiliation", "trp_knight_5_24", 1, "itm_kingdom_5_5", 0),#教长罗莎里奥·费雷罗

     (call_script, "script_set_faction_affiliation", "trp_knight_5_14", 1, "itm_kingdom_5_5", 1),#主教伊莉莎·萨德尼亚
     (call_script, "script_set_faction_affiliation", "trp_knight_5_49", 1, "itm_kingdom_5_5", 0),#教长速穆勒·阿斯里托琴

     (call_script, "script_set_faction_affiliation", "trp_knight_5_35", 1, "itm_kingdom_5_5", 1),#主教洛伦佐·巴里 
     (call_script, "script_set_faction_affiliation", "trp_knight_5_19", 1, "itm_kingdom_5_5", 0),#教长阿格尼斯·拉齐奥

     (call_script, "script_set_faction_affiliation", "trp_knight_5_6", 1, "itm_kingdom_5_5", 1),#主教贝内代托·费雷罗
     (call_script, "script_set_faction_affiliation", "trp_knight_5_21", 1, "itm_kingdom_5_5", 0),#教长萨曼塔·罗希

     (call_script, "script_set_faction_template", "itm_kingdom_5_5", "pt_armed_pilgrim_reinforcements", 2, 1),#部队模板
#圣歌骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_5_5", 0, "itm_kingdom_5_5", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_5_5", 1, "itm_knight_order_5_5", 2),#大团长萨马蒂诺·爱德华兹
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_5_5", 1, "itm_knight_order_5_5", 1),

#圣痕商会
     (call_script, "script_set_faction_affiliation", "itm_holy_scar_chamber_of_commerce", 0, "itm_kingdom_5_5", 1),
#剔圣人
     (call_script, "script_set_faction_affiliation", "itm_holy_picking_man", 0, "itm_kingdom_5_5", 0),


#————————————————————————————————外省教友互助会—————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_5_6", 0, "itm_kingdom_5", 0),

     (call_script, "script_set_faction_affiliation", "trp_knight_5_43", 1, "itm_kingdom_5_6", 1),#主教阿莱安娜·福贾
     (call_script, "script_set_troop_conscription_mode", "trp_knight_5_43", rsm_conscriptive, 20, "pt_remote_militia_reinforcements"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_5_5", 1, "itm_kingdom_5_6", 1),#主教詹卢卡·科伦坡
     (call_script, "script_set_troop_conscription_mode", "trp_knight_5_5", rsm_conscriptive, 20, "pt_remote_militia_reinforcements"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_5_22", 1, "itm_kingdom_5_6", 0),#教长维吉利奥·帕罗迪
     (call_script, "script_set_troop_conscription_mode", "trp_knight_5_22", rsm_conscriptive, 10, "pt_remote_militia_reinforcements"), 

     (call_script, "script_set_faction_template", "itm_kingdom_5_6", "pt_remote_militia_reinforcements", 0, 1),#部队模板



###########################################################龙树#######################################################
     (call_script, "script_set_faction_affiliation", "trp_kingdom_6_lord", 1, "itm_kingdom_6", 2),#狩元皇帝欧阳崇明





########################################################斯塔胡克大公国####################################################

     (call_script, "script_set_faction_template", "itm_kingdom_7", "pt_kingdom_7_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_7", "pt_kingdom_7_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_7", "pt_kingdom_7_reinforcements_c", 15, 3),
#血湖之庭
     (call_script, "script_set_faction_affiliation", "itm_blood_lake_court", 0, "itm_kingdom_7", 1),

#—————————————————————————————————白塔党————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_7_1", 0, "itm_kingdom_7", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_7_lord", 1, "itm_kingdom_7_1", 2),#大公齐格弗里德·斯塔胡克
     (call_script, "script_set_faction_affiliation", "trp_knight_7_4", 1, "itm_kingdom_7_1", 0),#提督冈瑟子爵
     (call_script, "script_set_faction_affiliation", "trp_knight_7_15", 1, "itm_kingdom_7_1", 0),#提督拉尔斯男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_7_2", 1, "itm_kingdom_7_1", 1),#提督阿普伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_7_8", 1, "itm_kingdom_7_1", 0),#提督海伍德男爵

     (call_script, "script_set_faction_affiliation", "trp_knight_7_11", 1, "itm_kingdom_7_1", 1),#提督克尔凯郭尔伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_7_14", 1, "itm_kingdom_7_1", 0),#提督拉斯穆森子爵

     (call_script, "script_set_faction_affiliation", "trp_knight_7_10", 1, "itm_kingdom_7_1", 1),#提督迪内森伯爵
     (call_script, "script_set_faction_affiliation", "trp_knight_7_16", 1, "itm_kingdom_7_1", 0),#提督伊萨克男爵

     (call_script, "script_set_faction_template", "itm_kingdom_7_1", "pt_party_of_tower_reinforcements", 3, 1),#部队模板
#血勋铁卫队
     (call_script, "script_set_faction_affiliation", "itm_knight_order_7_1", 0, "itm_kingdom_7_1", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_7_1", 1, "itm_knight_order_7_1", 2),#队长扎克利·艾弗森
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_7_1", 1, "itm_knight_order_7_1", 1),

#英穹塔内
     (call_script, "script_set_faction_affiliation", "itm_blocked_fortress", 0, "itm_kingdom_7_1", 0),#闭锁之堡

#戒血执法者
     (call_script, "script_set_faction_affiliation", "itm_blood_hunter", 0, "itm_kingdom_7_1", 1),


#———————————————————————————————斯塔胡克商业联合————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_7_2", 0, "itm_kingdom_7", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_7_1", 1, "itm_kingdom_7_2", 2),#总督诺伯鲁侯爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_1", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_7_3", 1, "itm_kingdom_7_2", 1),#提督奥登伯爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_3", rsm_mercenary, 50, 0), 

     (call_script, "script_set_faction_affiliation", "trp_knight_7_5", 1, "itm_kingdom_7_2", 0),#提督贝拉米子爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_5", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_7_6", 1, "itm_kingdom_7_2", 0),#提督巴内特子爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_6", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_7_7", 1, "itm_kingdom_7_2", 0),#提督斯捷潘男爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_7", rsm_mercenary, 40, 0), 

     (call_script, "script_set_faction_affiliation", "itm_knight_order_of_scarlet_full_moon", 0, "itm_kingdom_7_2", 1),#猩红满月骑士团

     (call_script, "script_set_faction_template", "itm_kingdom_7_2", "pt_starkhook_commercial_union_reinforcements_a", 2, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_7_2", "pt_starkhook_commercial_union_reinforcements_b", 1, 2),

#—————————————————————————————————蛇夫党————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_7_3", 0, "itm_kingdom_7", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_7_9", 1, "itm_kingdom_7_3", 2),#提督索伦伯爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_9", rsm_mercenary, 50, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_7_13", 1, "itm_kingdom_7_3", 1),#提督勒克子爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_13", rsm_mercenary, 40, 0), 
     (call_script, "script_set_faction_affiliation", "trp_knight_7_12", 1, "itm_kingdom_7_3", 0),#提督迪皮卡伯爵
     (call_script, "script_set_troop_conscription_mode", "trp_knight_7_12", rsm_mercenary, 40, 0), 




#########################################################自由城邦####################################################

     (call_script, "script_set_faction_template", "itm_kingdom_8", "pt_kingdom_8_reinforcements_a", 55, 1),#部队模板
     (call_script, "script_set_faction_template", "itm_kingdom_8", "pt_kingdom_8_reinforcements_b", 30, 2),
     (call_script, "script_set_faction_template", "itm_kingdom_8", "pt_kingdom_8_reinforcements_c", 15, 3),
#————————————————————————————————外来干涉————————————————————————————————
##
#裁决之锤
     (call_script, "script_set_faction_affiliation", "itm_hammer_of_judgment", 0, "itm_kingdom_8", 1),

#权杖下马骑士团
     (call_script, "script_set_faction_affiliation", "itm_knight_order_8_1", 0, "itm_kingdom_8", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_master_8_1", 1, "itm_knight_order_8_1", 2),#大团长法布里齐奥爵士
     (call_script, "script_set_faction_affiliation", "trp_knight_captain_8_1", 1, "itm_knight_order_8_1", 1),

#—————————————————————————————————归宗派————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_8_1", 0, "itm_kingdom_8", 2),
     (call_script, "script_set_faction_affiliation", "trp_kingdom_8_lord", 1, "itm_kingdom_8_1", 2),#执政官斯塔法诺爵士
     (call_script, "script_set_troop_conscription_mode", "trp_kingdom_8_lord", rsm_conscriptive, 30, "pt_kingdom_8_reinforcements_a"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_8_2", 1, "itm_kingdom_8_1", 1),#执政官斯尔维尔爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_2", rsm_conscriptive, 30, "pt_kingdom_8_reinforcements_a"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_8_7", 1, "itm_kingdom_8_1", 0),#执政官尼可罗爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_7", rsm_conscriptive, 30, "pt_kingdom_8_reinforcements_a"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_8_4", 1, "itm_kingdom_8_1", 0),#执政官维托里奥爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_4", rsm_conscriptive, 20, "pt_kingdom_8_reinforcements_a"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_8_6", 1, "itm_kingdom_8_1", 0),#执政官安娜施特希雅爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_6", rsm_conscriptive, 20, "pt_kingdom_8_reinforcements_a"), 
#古力奥妖妇团
     (call_script, "script_set_faction_affiliation", "itm_guilio_vamp", 0, "itm_kingdom_8_1", 0),


#—————————————————————————————————西求派————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_8_2", 0, "itm_kingdom_8", 1),
     (call_script, "script_set_faction_affiliation", "trp_knight_8_3", 1, "itm_kingdom_8_2", 2),#执政官提兹安诺爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_3", rsm_conscriptive, 30, "pt_kingdom_8_reinforcements_a"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_8_8", 1, "itm_kingdom_8_2", 0),#执政官路易吉爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_8", rsm_conscriptive, 20, "pt_kingdom_8_reinforcements_a"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_8_9", 1, "itm_kingdom_8_2", 1),#执政官法利法诺奥爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_9", rsm_conscriptive, 30, "pt_kingdom_8_reinforcements_a"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_8_11", 1, "itm_kingdom_8_2", 0),#执政官提可可诺爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_11", rsm_conscriptive, 20, "pt_kingdom_8_reinforcements_a"), 

     (call_script, "script_set_faction_affiliation", "trp_knight_8_1", 1, "itm_kingdom_8_2", 1),#执政官斯塔法诺爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_1", rsm_conscriptive, 30, "pt_kingdom_8_reinforcements_a"), 
     (call_script, "script_set_faction_affiliation", "trp_knight_8_5", 1, "itm_kingdom_8_2", 0),#执政官理卡多爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_5", rsm_conscriptive, 20, "pt_kingdom_8_reinforcements_a"), 
#裂空狙击团
     (call_script, "script_set_faction_affiliation", "itm_skytear_sniper_army", 0, "itm_kingdom_8_2", 0),


#—————————————————————————————————愚人派————————————————————————————————
##
     (call_script, "script_set_faction_affiliation", "itm_kingdom_8_3", 0, "itm_kingdom_8", 0),
     (call_script, "script_set_faction_affiliation", "trp_knight_8_10", 1, "itm_kingdom_8_3", 2),#执政官比安奇奥爵士
     (call_script, "script_set_troop_conscription_mode", "trp_knight_8_10", rsm_conscriptive, 40, "pt_kingdom_8_reinforcements_a"), 




#########################################################不死者结社####################################################

##______________________________________________________________________________无派系_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "trp_reception", 1, "itm_undead_association", 0),


##________________________________________________________________________莉达·采尼的派阀_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_beheading_necromancer", 0, "itm_undead_association", 2),
     (call_script, "script_set_faction_affiliation", "trp_beheading_necromancer", 1, "itm_beheading_necromancer", 2),#枭首之死灵术士莉达·采尼
     (call_script, "script_set_faction_affiliation", "trp_npc2", 1, "itm_beheading_necromancer", 1),#钢之死灵术士爱蜜莉·采尼

#人类附属实力
     (call_script, "script_set_faction_affiliation", "itm_derlin_mercenary_corps", 0, "itm_beheading_necromancer", 0),#德林商会
     (call_script, "script_set_faction_affiliation", "itm_agouti_commerce_chamber", 0, "itm_beheading_necromancer", 0),#刺鼠商会
     (call_script, "script_set_faction_affiliation", "itm_dusk_locker_mercenary_corps", 0, "itm_beheading_necromancer", 0),#黄昏之锁佣兵团


##____________________________________________________________________________枯派_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_zombie_clique", 0, "itm_undead_association", 1),
#权的派阀
     (call_script, "script_set_faction_affiliation", "itm_power_necromancer", 0, "itm_zombie_clique", 2),
     (call_script, "script_set_faction_affiliation", "trp_power_necromancer", 1, "itm_power_necromancer", 2),#权之死灵术士卡尔文·比尔博姆
     (call_script, "script_set_faction_affiliation", "trp_assistant_4", 1, "itm_power_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_10", 1, "itm_power_necromancer", 0),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_11", 1, "itm_power_necromancer", 0),

#装甲的派阀
     (call_script, "script_set_faction_affiliation", "itm_armor_necromancer", 0, "itm_zombie_clique", 1),
     (call_script, "script_set_faction_affiliation", "trp_armor_necromancer", 1, "itm_armor_necromancer", 2),#装甲之死灵术士费戴里格·托纳托雷
     (call_script, "script_set_faction_affiliation", "trp_assistant_3", 1, "itm_armor_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_16", 1, "itm_armor_necromancer", 0),

#坚城的派阀
     (call_script, "script_set_faction_affiliation", "itm_defend_necromancer", 0, "itm_zombie_clique", 0),
     (call_script, "script_set_faction_affiliation", "trp_defend_necromancer", 1, "itm_defend_necromancer", 2),#坚城之死灵术士达日阿赤
     (call_script, "script_set_faction_affiliation", "trp_apprentice_5", 1, "itm_defend_necromancer", 0),


##____________________________________________________________________________骸派_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_skeleton_clique", 0, "itm_undead_association", 1),
#元素的派阀
     (call_script, "script_set_faction_affiliation", "itm_element_necromancer", 0, "itm_skeleton_clique", 2),
     (call_script, "script_set_faction_affiliation", "trp_element_necromancer", 1, "itm_element_necromancer", 2),#元素之死灵术士雅克·杜兰
     (call_script, "script_set_faction_affiliation", "trp_assistant_6", 1, "itm_element_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_13", 1, "itm_element_necromancer", 0),

#炎的派阀
     (call_script, "script_set_faction_affiliation", "itm_inflammation_necromancer", 0, "itm_skeleton_clique", 1),
     (call_script, "script_set_faction_affiliation", "trp_inflammation_necromancer", 1, "itm_inflammation_necromancer", 2),#炎之死灵术士费尔南·迪布瓦
     (call_script, "script_set_faction_affiliation", "trp_assistant_1", 1, "itm_inflammation_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_2", 1, "itm_inflammation_necromancer", 0),

#骤雨的派阀
     (call_script, "script_set_faction_affiliation", "itm_shower_necromancer", 0, "itm_skeleton_clique", 0),
     (call_script, "script_set_faction_affiliation", "trp_shower_necromancer", 1, "itm_shower_necromancer", 2),#骤雨之死灵术士艾希礼·妮萨
     (call_script, "script_set_faction_affiliation", "trp_assistant_7", 1, "itm_shower_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_15", 1, "itm_shower_necromancer", 0),

#强袭的派阀
     (call_script, "script_set_faction_affiliation", "itm_storm_necromancer", 0, "itm_skeleton_clique", 0),
     (call_script, "script_set_faction_affiliation", "trp_storm_necromancer", 1, "itm_storm_necromancer", 2),#强袭之死灵术士迪夫·布鲁诺
     (call_script, "script_set_faction_affiliation", "trp_apprentice_3", 1, "itm_storm_necromancer", 0),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_4", 1, "itm_storm_necromancer", 0),


##____________________________________________________________________________魂派_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_fantom_clique", 0, "itm_undead_association", 1),
#破灭的派阀
     (call_script, "script_set_faction_affiliation", "itm_shattered_necromancer", 0, "itm_fantom_clique", 2),
     (call_script, "script_set_faction_affiliation", "trp_shattered_necromancer", 1, "itm_shattered_necromancer", 2),#破灭之里尔德·汉森
     (call_script, "script_set_faction_affiliation", "trp_assistant_8", 1, "itm_shattered_necromancer", 0),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_9", 1, "itm_shattered_necromancer", 0),

#青的派阀
     (call_script, "script_set_faction_affiliation", "itm_cyan_necromancer", 0, "itm_fantom_clique", 1),
     (call_script, "script_set_faction_affiliation", "trp_cyan_necromancer", 1, "itm_cyan_necromancer", 2),#青之死灵术士冷瑾萱
     (call_script, "script_set_faction_affiliation", "trp_assistant_2", 1, "itm_cyan_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_6", 1, "itm_cyan_necromancer", 0),

#影的派阀
     (call_script, "script_set_faction_affiliation", "itm_shadow_necromancer", 0, "itm_fantom_clique", 1),
     (call_script, "script_set_faction_affiliation", "trp_shadow_necromancer", 1, "itm_shadow_necromancer", 2),#影之死灵术士夏佐·布罗德
     (call_script, "script_set_faction_affiliation", "trp_assistant_5", 1, "itm_shadow_necromancer", 1),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_1", 1, "itm_shadow_necromancer", 0),
     (call_script, "script_set_faction_affiliation", "trp_apprentice_7", 1, "itm_shadow_necromancer", 0),


##____________________________________________________________________________朽派_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_walker_clique", 0, "itm_undead_association", 1),

#浊的派阀
     (call_script, "script_set_faction_affiliation", "itm_turbid_necromancer", 0, "itm_walker_clique", 2),
     (call_script, "script_set_faction_affiliation", "trp_turbid_necromancer", 1, "itm_turbid_necromancer", 2),#浊之死灵术士巴泽尔·巴比特




#########################################################渊教####################################################


##_____________________________________________________________________深海巨蟒船团_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_abyssal_pirate", 0, "itm_abyssal_order", 1),


##_____________________________________________________________________不死者溺派_________________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_drowner_clique", 0, "itm_abyssal_order", 1),




######################################################热砂的末裔####################################################
##________________________________________________________________________应许绿洲______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_desertus_bandit", 0, "itm_desertus_tribe", 1),




#######################################################边缘人####################################################
##________________________________________________________________________盗拾者集团______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_burglar_scavenger", 0, "itm_outlawers", 1),
##________________________________________________________________________养皮人______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_skin_raiser", 0, "itm_outlawers", 1),




#######################################################自生者####################################################
##________________________________________________________________________绯世______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_crimson_world", 0, "itm_ownerless_one", 1),

##________________________________________________________________________谬史______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_erroneous_history", 0, "itm_ownerless_one", 1),




########################################################黑暗####################################################

##________________________________________________________________________魔王崇拜者______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_devil_worshipper", 0, "itm_demon", 0),

##________________________________________________________________________魔气侵蚀者______________________________________________________________________________
##
     (call_script, "script_set_faction_affiliation", "itm_demonic_corruptor", 0, "itm_demon", 0),
    ]),





########################################################新会战系统###################################################
##
#初始化城镇村的平面拓扑图
  ("initial_center_zone", [
#     (assign, "$center_zone_show", 1),
     (assign, "$g_current_rank", 1),
     (assign, "$g_current_procession", 1),

     (item_set_slot, "itm_zone_slum", event_default, 1),#无事发生
     (item_set_slot, "itm_zone_slum", event_find_hidden_place, 5),#发现隐藏场所
     (item_set_slot, "itm_zone_slum", event_assassination, 1),#遇到刺杀
     (item_set_slot, "itm_zone_slum", event_encountered_pickpocket, 3),#遭遇扒手
     (item_set_slot, "itm_zone_slum", event_encountered_robbery, 2),#遭遇抢劫
     (item_set_slot, "itm_zone_slum", event_recruit_refugee, 3),#招募难民
     (item_set_slot, "itm_zone_slum", event_slave_trader, 2),#奴隶贩子贩卖奴隶
     (item_set_slot, "itm_zone_slum", event_ransom_broker, 1),#赎金经纪人贩卖士兵
     (item_set_slot, "itm_zone_slum", event_beggar_begging, 3),#乞丐乞讨
     (item_set_slot, "itm_zone_slum", event_find_stolen_goods, 1),#找到赃物

     (item_set_slot, "itm_zone_residential_area", event_default, 1),#无事发生
     (item_set_slot, "itm_zone_residential_area", event_find_hidden_place, 5),#发现隐藏场所
     (item_set_slot, "itm_zone_residential_area", event_assassination, 1),#遇到刺杀
     (item_set_slot, "itm_zone_residential_area", event_encountered_pickpocket, 1),#遭遇扒手
     (item_set_slot, "itm_zone_residential_area", event_encountered_robbery, 1),#遭遇抢劫
     (item_set_slot, "itm_zone_residential_area", event_recruit_citizen, 2),#招募市民
     (item_set_slot, "itm_zone_residential_area", event_found_wallet, 2),#捡到钱包
     (item_set_slot, "itm_zone_residential_area", event_slave_trader, 2),#奴隶贩子贩卖奴隶
     (item_set_slot, "itm_zone_residential_area", event_ransom_broker, 2),#赎金经纪人贩卖士兵
     (item_set_slot, "itm_zone_residential_area", event_small_competition, 1),#小型挑战赛
     (item_set_slot, "itm_zone_residential_area", event_street_singing, 2),#街头卖唱
     (item_set_slot, "itm_zone_residential_area", event_handling_expired_food, 1),#商家处理临期产品
     (item_set_slot, "itm_zone_residential_area", event_beggar_begging, 1),#乞丐乞讨
     (item_set_slot, "itm_zone_residential_area", event_discover_orphanage, 1),#发现孤儿院

     (item_set_slot, "itm_zone_rich_area", event_default, 1),#无事发生
     (item_set_slot, "itm_zone_rich_area", event_find_hidden_place, 5),#发现隐藏场所
     (item_set_slot, "itm_zone_rich_area", event_assassination, 1),#遇到刺杀
     (item_set_slot, "itm_zone_rich_area", event_recruit_noble, 2),#招募贵族子弟
     (item_set_slot, "itm_zone_rich_area", event_commercial_information, 1),#偷听商业信息
     (item_set_slot, "itm_zone_rich_area", event_found_wallet, 3),#捡到钱包
     (item_set_slot, "itm_zone_rich_area", event_bookcollector, 1),#藏书家抛售书籍
     (item_set_slot, "itm_zone_rich_area", event_visit_master, 1),#拜访大师
     (item_set_slot, "itm_zone_rich_area", event_ransom_broker, 2),#赎金经纪人贩卖士兵
     (item_set_slot, "itm_zone_rich_area", event_dragon_blood_merchant, 1),#龙血商人
     (item_set_slot, "itm_zone_rich_area", event_discover_scandal_1, 1),#发现丑闻一
     (item_set_slot, "itm_zone_rich_area", event_discover_scandal_2, 1),#发现丑闻二
     (item_set_slot, "itm_zone_rich_area", event_noble_beat_servant, 2),#贵族殴打仆人
     (item_set_slot, "itm_zone_rich_area", event_noble_assassinated, 1),#贵族遭遇刺杀
     (item_set_slot, "itm_zone_rich_area", event_street_singing, 2),#街头卖唱

#各种建筑的场景起始位置，通过序号确定具体是哪个
     (item_set_slot, "itm_adventurer_station", slot_building_scene_begin, "scn_adventurer_station_1"),

     (item_set_slot, "itm_underworld_stronghold", slot_building_scene_begin, "scn_underworld_stronghold_1"),

##________________________________________________________________________城镇村______________________________________________________________________________
##前行后列
#勒塞夫
     (party_set_slot, "p_town_4", slot_center_scene, "scn_town_4_sandtable"),
     (call_script, "script_set_center_zone", "p_town_4", 1, 4, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 5, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 6, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 7, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 8, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 9, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 10, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 11, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 1, 12, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 2, 3, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 4, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 5, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 6, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 7, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 13, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 2, 14, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 3, 2, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 3, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 4, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 5, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 6, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 7, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 10, "itm_zone_rural", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 3, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 4, 2, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 3, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 4, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 5, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 6, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 7, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 10, "itm_zone_forest", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 11, "itm_zone_forest", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 4, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 5, 2, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 3, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 4, "itm_zone_rich_area", 0, "itm_castle", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 5, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 6, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 7, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 8, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 13, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 5, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 6, 2, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 3, "itm_zone_rich_area", 0, "itm_base", "itm_knight_order_1_2", 0),#元素骑士
     (call_script, "script_set_center_zone", "p_town_4", 6, 4, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 5, "itm_zone_rich_area", 0, "itm_office", 0, 0),#市政府
     (call_script, "script_set_center_zone", "p_town_4", 6, 6, "itm_zone_commercial_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 7, "itm_zone_commercial_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 8, "itm_zone_industry_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 9, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 12, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 13, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 14, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 6, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 7, 2, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 3, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 4, "itm_zone_rich_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 5, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 6, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 7, "itm_zone_water", 0, "itm_bridge", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 8, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 9, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 10, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 11, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 12, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 13, "itm_zone_field", 0, "itm_fort", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 14, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 7, 15, "itm_zone_water", 0, 0, 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 8, 2, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 3, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 4, "itm_zone_water", 0, "itm_bridge", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 5, "itm_zone_water", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 6, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 7, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 8, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 9, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 10, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 14, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 8, 15, "itm_zone_slum", 0, 0, 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 9, 2, "itm_zone_commercial_area", 0, "itm_wharf", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 3, "itm_zone_commercial_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 4, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 5, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 6, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 7, "itm_zone_residential_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 8, "itm_zone_residential_area", 0, "itm_adventurer_station", "itm_powell_adventures_association_in_lesaff", 1),#冒险者协会
     (call_script, "script_set_center_zone", "p_town_4", 9, 9, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 14, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 9, 15, "itm_zone_field", 0, 0, 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 10, 2, "itm_zone_commercial_area", 0, "itm_wharf", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 3, "itm_zone_commercial_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 4, "itm_zone_industry_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 5, "itm_zone_industry_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 6, "itm_zone_commercial_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 7, "itm_zone_commercial_area", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 8, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 10, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 11, 2, "itm_zone_commercial_area", 0, "itm_wharf", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 3, "itm_zone_commercial_area", 0, "itm_warehouse", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 4, "itm_zone_commercial_area", 0, "itm_warehouse", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 5, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 6, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 7, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 11, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 12, 3, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 4, "itm_zone_none", 0, "itm_high_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 5, "itm_zone_slum", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 6, "itm_zone_slum", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 7, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 11, "itm_zone_rural", 0, "itm_barrack", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 12, "itm_zone_rural", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 12, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 13, 1, "itm_zone_ruin", 0, "itm_fort", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 3, "itm_zone_slum", 0, "itm_wharf", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 4, "itm_zone_slum", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 5, "itm_zone_slum", 0, "itm_underworld_stronghold", "itm_black_candle_gang", 1),#权厄之秤据点
     (call_script, "script_set_center_zone", "p_town_4", 13, 6, "itm_zone_slum", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 7, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 14, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 13, 15, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 14, 3, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 4, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 5, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 6, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 7, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 8, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 9, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 10, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 11, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 12, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 13, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 14, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 14, 15, "itm_zone_field", 0, 0, 0, 0),

     (call_script, "script_set_center_zone", "p_town_4", 15, 4, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 5, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 6, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 7, "itm_zone_field", 0, 0, 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 8, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 9, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 10, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 11, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 12, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 13, "itm_zone_none", 0, "itm_tremendous_wall", 0, 0),
     (call_script, "script_set_center_zone", "p_town_4", 15, 15, "itm_zone_field", 0, 0, 0, 0),


##________________________________________________________________________随机战场______________________________________________________________________________
##
#平原1
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 1, 14, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 1, 15, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 2, 6, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 2, 13, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 2, 14, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 3, 6, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 3, 12, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 3, 13, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 4, 6, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 4, 11, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 4, 12, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 5, 6, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 5, 11, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 6, 9, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 6, 10, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 6, 11, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 7, 8, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 7, 9, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 8, 7, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 8, 8, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 9, 6, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 9, 7, "itm_zone_water"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 10, 5, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 10, 6, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 10, 7, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 10, 13, "itm_zone_cliff"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 11, 3, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 11, 4, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 11, 5, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 11, 7, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 11, 13, "itm_zone_cliff"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 12, 2, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 12, 3, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 12, 6, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 12, 7, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 12, 12, "itm_zone_cliff"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 13, 1, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 13, 2, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 13, 6, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 13, 7, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 13, 12, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 13, 14, "itm_zone_cliff"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 14, 12, "itm_zone_cliff"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 14, 13, "itm_zone_cliff"),

     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 15, 4, "itm_zone_water"),
     (call_script, "script_store_scene_zone", "scn_random_sandtable_plain_1", 15, 5, "itm_zone_water"),
  ]),


#初始化编队相关信息
  ("initial_detachment", [
#默认
     (call_script, "script_store_formation_function", "itm_formation_common", "itm_detachment_common", 1),
#进攻
     (call_script, "script_store_formation_function", "itm_formation_assault", "itm_detachment_commander", 1),
     (call_script, "script_store_formation_function", "itm_formation_assault", "itm_detachment_strike", 4),
     (call_script, "script_store_formation_function", "itm_formation_assault", "itm_detachment_support", 2),
     (call_script, "script_store_formation_function", "itm_formation_assault", "itm_detachment_logistic", 1),
     (call_script, "script_store_formation_prefer_function", "itm_formation_assault", "itm_function_strike", 35), 
#压制
     (call_script, "script_store_formation_function", "itm_formation_suppress", "itm_detachment_commander", 1),
     (call_script, "script_store_formation_function", "itm_formation_suppress", "itm_detachment_support", 1),
     (call_script, "script_store_formation_function", "itm_formation_suppress", "itm_detachment_firepower", 4),
     (call_script, "script_store_formation_function", "itm_formation_suppress", "itm_detachment_defend", 2),
     (call_script, "script_store_formation_function", "itm_formation_suppress", "itm_detachment_logistic", 1),
     (call_script, "script_store_formation_function", "itm_formation_suppress", "itm_detachment_cannon_fodder", 3),
     (call_script, "script_store_formation_prefer_function", "itm_formation_suppress", "itm_function_curved_fire", 20), 
#反冲击
     (call_script, "script_store_formation_function", "itm_formation_counterattack", "itm_detachment_commander", 1),
     (call_script, "script_store_formation_function", "itm_formation_counterattack", "itm_detachment_strike", 2),
     (call_script, "script_store_formation_function", "itm_formation_counterattack", "itm_detachment_support", 2),
     (call_script, "script_store_formation_function", "itm_formation_counterattack", "itm_detachment_defend", 1),
     (call_script, "script_store_formation_function", "itm_formation_counterattack", "itm_detachment_cannon_fodder", 5),
     (call_script, "script_store_formation_prefer_function", "itm_formation_counterattack", "itm_function_cannon_fodder", 35), 
#防御
     (call_script, "script_store_formation_function", "itm_formation_defense", "itm_detachment_commander", 1),
     (call_script, "script_store_formation_function", "itm_formation_defense", "itm_detachment_support", 1),
     (call_script, "script_store_formation_function", "itm_formation_defense", "itm_detachment_firepower", 2),
     (call_script, "script_store_formation_function", "itm_formation_defense", "itm_detachment_defend", 4),
     (call_script, "script_store_formation_function", "itm_formation_defense", "itm_detachment_logistic", 1),
     (call_script, "script_store_formation_prefer_function", "itm_formation_defense", "itm_function_defend", 25), 
#筑垒
     (call_script, "script_store_formation_function", "itm_formation_fortress", "itm_detachment_commander", 1),
     (call_script, "script_store_formation_function", "itm_formation_fortress", "itm_detachment_support", 1),
     (call_script, "script_store_formation_function", "itm_formation_fortress", "itm_detachment_defend", 1),
     (call_script, "script_store_formation_function", "itm_formation_fortress", "itm_detachment_cannon_fodder", 2),
     (call_script, "script_store_formation_function", "itm_formation_fortress", "itm_detachment_sapper", 1),
     (call_script, "script_store_formation_function", "itm_formation_fortress", "itm_detachment_logistic", 1),
     (call_script, "script_store_formation_prefer_function", "itm_formation_fortress", "itm_function_non_military_personnel", 40), #劳工
#驻扎
     (call_script, "script_store_formation_function", "itm_formation_station", "itm_detachment_commander", 1),
     (call_script, "script_store_formation_function", "itm_formation_station", "itm_detachment_common", 3),
     (call_script, "script_store_formation_function", "itm_formation_station", "itm_detachment_support", 1),
     (call_script, "script_store_formation_function", "itm_formation_station", "itm_detachment_defend", 1),


#各个职能的编队对技能的倾向，三个主要技能三个次要技能
#强袭
     (item_set_slot, "itm_detachment_strike", 1, skl_ironflesh),
     (item_set_slot, "itm_detachment_strike", 2, skl_power_strike),
     (item_set_slot, "itm_detachment_strike", 3, skl_persuasion),
     (item_set_slot, "itm_detachment_strike", 4, skl_shield),
     (item_set_slot, "itm_detachment_strike", 5, skl_athletics),
     (item_set_slot, "itm_detachment_strike", 6, skl_riding),
#支援
     (item_set_slot, "itm_detachment_support", 1, skl_athletics),
     (item_set_slot, "itm_detachment_support", 2, skl_riding),
     (item_set_slot, "itm_detachment_support", 3, skl_tracking),
     (item_set_slot, "itm_detachment_support", 4, skl_power_strike),
     (item_set_slot, "itm_detachment_support", 5, skl_power_throw),
     (item_set_slot, "itm_detachment_support", 6, skl_tactics),
#火力
     (item_set_slot, "itm_detachment_firepower", 1, skl_power_draw),
     (item_set_slot, "itm_detachment_firepower", 2, skl_power_throw),
     (item_set_slot, "itm_detachment_firepower", 3, skl_persuasion),
     (item_set_slot, "itm_detachment_firepower", 4, skl_spotting),
     (item_set_slot, "itm_detachment_firepower", 5, skl_horse_archery),
     (item_set_slot, "itm_detachment_firepower", 6, skl_memory),
#固守
     (item_set_slot, "itm_detachment_defend", 1, skl_ironflesh),
     (item_set_slot, "itm_detachment_defend", 2, skl_shield),
     (item_set_slot, "itm_detachment_defend", 3, skl_array_arrangement),
     (item_set_slot, "itm_detachment_defend", 4, skl_horse_archery),
     (item_set_slot, "itm_detachment_defend", 5, skl_surgery),
     (item_set_slot, "itm_detachment_defend", 6, skl_leadership),
#指挥
     (item_set_slot, "itm_detachment_commander", 1, skl_tactics),
     (item_set_slot, "itm_detachment_commander", 2, skl_leadership),
     (item_set_slot, "itm_detachment_commander", 3, skl_prisoner_management),
     (item_set_slot, "itm_detachment_commander", 4, skl_ironflesh),
     (item_set_slot, "itm_detachment_commander", 5, skl_power_strike),
     (item_set_slot, "itm_detachment_commander", 6, skl_shield),
#特种
     (item_set_slot, "itm_detachment_special_force", 1, skl_athletics),
     (item_set_slot, "itm_detachment_special_force", 2, skl_tracking),
     (item_set_slot, "itm_detachment_special_force", 3, skl_spotting),
     (item_set_slot, "itm_detachment_special_force", 4, skl_looting),
     (item_set_slot, "itm_detachment_special_force", 5, skl_pathfinding),
     (item_set_slot, "itm_detachment_special_force", 6, skl_study),
#强识
     (item_set_slot, "itm_detachment_strategic", 1, skl_persuasion),
     (item_set_slot, "itm_detachment_strategic", 2, skl_array_arrangement),
     (item_set_slot, "itm_detachment_strategic", 3, skl_memory),
     (item_set_slot, "itm_detachment_strategic", 4, skl_horse_archery),
     (item_set_slot, "itm_detachment_strategic", 5, -1),
     (item_set_slot, "itm_detachment_strategic", 6, -1),
#炮灰
     (item_set_slot, "itm_detachment_cannon_fodder", 1, skl_looting),
     (item_set_slot, "itm_detachment_cannon_fodder", 2, skl_prisoner_management),
     (item_set_slot, "itm_detachment_cannon_fodder", 3, skl_leadership),
     (item_set_slot, "itm_detachment_cannon_fodder", 4, skl_pathfinding),
     (item_set_slot, "itm_detachment_cannon_fodder", 5, skl_tracking),
     (item_set_slot, "itm_detachment_cannon_fodder", 6, skl_persuasion),
#工兵
     (item_set_slot, "itm_detachment_sapper", 1, skl_engineer),
     (item_set_slot, "itm_detachment_sapper", 2, skl_engineer),
     (item_set_slot, "itm_detachment_sapper", 3, skl_inventory_management),
     (item_set_slot, "itm_detachment_sapper", 4, skl_array_arrangement),
     (item_set_slot, "itm_detachment_sapper", 5, -1),
     (item_set_slot, "itm_detachment_sapper", 6, -1),
#后勤
     (item_set_slot, "itm_detachment_logistic", 1, skl_inventory_management),
     (item_set_slot, "itm_detachment_logistic", 2, skl_first_aid),
     (item_set_slot, "itm_detachment_logistic", 3, skl_prisoner_management),
     (item_set_slot, "itm_detachment_logistic", 4, skl_looting),
     (item_set_slot, "itm_detachment_logistic", 5, skl_wound_treatment),
     (item_set_slot, "itm_detachment_logistic", 6, skl_trade),

#兵种职能加个各编队的倾向
#格斗
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_strike", 30),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_support", 15),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_firepower", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_defend", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_commander", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_special_force", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_strategic", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_combat", "itm_detachment_logistic", 10),
#突击
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_strike", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_support", 15),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_firepower", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_commander", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_special_force", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strike", "itm_detachment_logistic", 1),
#机动支援
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_strike", 15),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_support", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_firepower", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_defend", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_commander", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_special_force", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_cannon_fodder", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_maneuver", "itm_detachment_logistic", 15),
#防御
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_support", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_firepower", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_defend", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_commander", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_special_force", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_strategic", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_sapper", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_defend", "itm_detachment_logistic", 5),
#指挥
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_common", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_support", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_firepower", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_commander", 3),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_special_force", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_commander", "itm_detachment_logistic", 1),
#英雄单位
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_common", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_strike", 3),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_support", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_firepower", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_commander", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_special_force", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_hero_agent", "itm_detachment_logistic", 1),
#侦察
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_support", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_firepower", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_commander", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_special_force", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_reconnaissance", "itm_detachment_logistic", 1),
#刺客
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_strike", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_support", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_firepower", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_commander", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_special_force", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_assassin", "itm_detachment_logistic", 1),
#曲射火力
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_support", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_firepower", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_defend", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_commander", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_special_force", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_curved_fire", "itm_detachment_logistic", 1),
#平射火力
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_support", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_firepower", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_defend", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_commander", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_special_force", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_strategic", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_cannon_fodder", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_sapper", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_flat_fire", "itm_detachment_logistic", 1),
#战略力量
     (call_script, "script_store_detachment_tendency", "itm_function_strategic_strength", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_strategic_strength", "itm_detachment_firepower", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_strategic_strength", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strategic_strength", "itm_detachment_commander", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_strategic_strength", "itm_detachment_special_force", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_strategic_strength", "itm_detachment_strategic", 50),
#辅助
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_strike", 15),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_support", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_firepower", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_defend", 15),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_commander", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_special_force", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_strategic", 10),
     (call_script, "script_store_detachment_tendency", "itm_function_assistance", "itm_detachment_cannon_fodder", 1),
#炮灰
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_support", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_firepower", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_defend", 5),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_commander", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_cannon_fodder", 50),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_sapper", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_cannon_fodder", "itm_detachment_logistic", 5),
#非战斗人员
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_strike", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_support", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_firepower", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_defend", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_commander", 1),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_cannon_fodder", 15),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_sapper", 30),
     (call_script, "script_store_detachment_tendency", "itm_function_non_military_personnel", "itm_detachment_logistic", 30),
#敌意存在
     (call_script, "script_store_detachment_tendency", "itm_function_monster", "itm_detachment_common", 20),
     (call_script, "script_store_detachment_tendency", "itm_function_monster", "itm_detachment_monster", 50),
  ]),
]