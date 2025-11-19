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


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

game_scripts = [

  #script_game_start:
  # This script is called when a new game is started
  # INPUT: none
  ("game_start",
   [
           (troop_get_type,"$your_type","trp_player"), #use for change race

           (call_script, "script_initiallization_script_integration"),

           (assign, "$auxiliary_number", 0),#use for create attendant parties

     (item_set_slot, "itm_demon_corpse", slot_corpse_amount, 0),
     (item_set_slot, "itm_elf_corpse", slot_corpse_amount, 0),
     (item_set_slot, "itm_highest_corpse", slot_corpse_amount, 0),
     (item_set_slot, "itm_excellent_corpse", slot_corpse_amount, 0),
     (item_set_slot, "itm_good_corpse", slot_corpse_amount, 0),
     (item_set_slot, "itm_normal_corpse", slot_corpse_amount, 0),
     (item_set_slot, "itm_bad_corpse", slot_corpse_amount, 0),


      (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
      (assign, "$g_player_luck", 200),
      (assign, "$g_player_luck", 200),
      (troop_set_slot, "trp_player", slot_troop_occupation, slto_kingdom_hero),
      (store_random_in_range, ":starting_training_ground", training_grounds_begin, training_grounds_end),
      (party_relocate_near_party, "p_main_party", ":starting_training_ground", 3),
      (str_store_troop_name, s5, "trp_player"),
      (party_set_name, "p_main_party", s5),
      (call_script, "script_update_party_creation_random_limits"),
      (assign, "$g_player_party_icon", -1),
	  
	  #Warband changes begin -- set this early 
	  (try_for_range, ":npc", 0, kingdom_ladies_end),
	    (this_or_next|eq, ":npc", "trp_player"),
		(is_between, ":npc", active_npcs_begin, kingdom_ladies_end),
		(troop_set_slot, ":npc", slot_troop_father, -1),
		(troop_set_slot, ":npc", slot_troop_mother, -1),
		(troop_set_slot, ":npc", slot_troop_guardian, -1),
		(troop_set_slot, ":npc", slot_troop_spouse, -1),
		(troop_set_slot, ":npc", slot_troop_betrothed, -1),
        (troop_set_slot, ":npc", slot_troop_prisoner_of_party, -1),		
        (troop_set_slot, ":npc", slot_lady_last_suitor, -1),		
        (troop_set_slot, ":npc", slot_troop_stance_on_faction_issue, -1),		
		
		(store_random_in_range, ":decision_seed", 0, 10000),
        (troop_set_slot, ":npc", slot_troop_set_decision_seed, ":decision_seed"),	#currently not used
        (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":decision_seed"),	#currently not used, holds for at least 24 hours			
	  (try_end),

	  (assign, "$g_lord_long_term_count", 0),
	  (call_script, "script_initialize_banner_info"),
	  (call_script, "script_initialize_item_info"),
	  (call_script, "script_initialize_aristocracy"),
      
      # Setting random feast time
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (store_random_in_range, ":last_feast_time", 0, 312), #240 + 72
        (val_mul, ":last_feast_time", -1),
        (faction_set_slot, ":faction_no", slot_faction_last_feast_start_time, ":last_feast_time"),
      (try_end),
      
      # Setting the random town sequence:
      (store_sub, ":num_towns", towns_end, towns_begin),
      (assign, ":num_iterations", ":num_towns"),
      (try_for_range, ":cur_town_no", 0, ":num_towns"),
        (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", -1),
      (try_end),
      (assign, ":cur_town_no", 0),
      (try_for_range, ":unused", 0, ":num_iterations"),
        (store_random_in_range, ":random_no", 0, ":num_towns"),
        (assign, ":is_unique", 1),
        (try_for_range, ":cur_town_no_2", 0, ":num_towns"),
          (troop_slot_eq, "trp_random_town_sequence", ":cur_town_no_2", ":random_no"),
          (assign, ":is_unique", 0),
        (try_end),
        (try_begin),
          (eq, ":is_unique", 1),
          (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", ":random_no"),
          (val_add, ":cur_town_no", 1),
        (else_try),
          (val_add, ":num_iterations", 1),
        (try_end),
      (try_end),

      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$cheat_mode"),
        (display_message, "@{!}DEBUG : Completed faction troop assignments, cheat mode: {reg3}"),
      (try_end),
      
# Factions:
      (faction_set_slot, "fac_kingdom_1",  slot_faction_leader, "trp_kingdom_1_lord"),
	  (troop_set_slot, "trp_kingdom_1_lord", slot_troop_renown, 13505),#国王声望
	  
      (faction_set_slot, "fac_kingdom_2",  slot_faction_leader, "trp_kingdom_2_lord"),
	  (troop_set_slot, "trp_kingdom_2_lord", slot_troop_renown, 17016),

      (faction_set_slot, "fac_kingdom_3",  slot_faction_leader, "trp_kingdom_3_lord"),
	  (troop_set_slot, "trp_kingdom_3_lord", slot_troop_renown, 13227),

      (faction_set_slot, "fac_kingdom_4",  slot_faction_leader, "trp_kingdom_4_lord"),
	  (troop_set_slot, "trp_kingdom_4_lord", slot_troop_renown, 16303),

      (faction_set_slot, "fac_kingdom_5",  slot_faction_leader, "trp_kingdom_5_lord"),
	  (troop_set_slot, "trp_kingdom_5_lord", slot_troop_renown, 14881),

      (faction_set_slot, "fac_kingdom_6",  slot_faction_leader, "trp_kingdom_6_lord"),
	  (troop_set_slot, "trp_kingdom_6_lord", slot_troop_renown, 33351),

      (faction_set_slot, "fac_kingdom_7", slot_faction_leader, "trp_kingdom_7_lord"),
          (troop_set_slot, "trp_kingdom_7_lord", slot_troop_renown, 12037),

      (faction_set_slot, "fac_kingdom_8", slot_faction_leader, "trp_kingdom_8_lord"),
          (troop_set_slot, "trp_kingdom_8_lord", slot_troop_renown, 11862),
	  
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
      (try_end), 
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),

# Towns:
      (try_for_range, ":item_no", trade_goods_begin, trade_goods_end),
        (store_sub, ":offset", ":item_no", trade_goods_begin),
        (val_add, ":offset", slot_town_trade_good_prices_begin),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_set_slot, ":center_no", ":offset", average_price_factor), #1000
        (try_end),
      (try_end),

	  (call_script, "script_initialize_trade_routes"),
	  (call_script, "script_initialize_town_arena_info"),
      #start some tournaments
      (try_for_range, ":town_no", towns_begin, towns_end),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 20),
        (store_random_in_range, ":random_days", 12, 15),
        (party_set_slot, ":town_no", slot_town_has_tournament, ":random_days"),
      (try_end),

      #village products -- at some point we might make it so that the villages supply raw materials to towns, and the towns produce manufactured goods
	  #village products designate the raw materials produced in the vicinity
	  #right now, just doing a test for grain produced in the swadian heartland

#分配村庄所属
     (party_set_slot, "p_village_1_1", slot_village_bound_center, "p_town_29"),#Sousanth
     (party_set_slot, "p_village_1_2", slot_village_bound_center, "p_castle_1_17"),#Faure_Fief
     (party_set_slot, "p_village_1_3", slot_village_bound_center, "p_castle_1_11"),#Jurbury_Fief
     (party_set_slot, "p_village_1_4", slot_village_bound_center, "p_castle_1_1"),#Souende_Fief
     (party_set_slot, "p_village_1_5", slot_village_bound_center, "p_castle_1_4"),#Witon_Fief
     (party_set_slot, "p_village_1_6", slot_village_bound_center, "p_castle_1_6"),#Ecsupely_Fief
     (party_set_slot, "p_village_1_7", slot_village_bound_center, "p_town_6"),#King of Powell
     (party_set_slot, "p_village_1_8", slot_village_bound_center, "p_town_7"),#Preist
     (party_set_slot, "p_village_1_9", slot_village_bound_center, "p_castle_1_23"),#Chevalier_Fief
     (party_set_slot, "p_village_1_10", slot_village_bound_center, "p_castle_1_7"),#Rosschealder_Fief
     (party_set_slot, "p_village_1_11", slot_village_bound_center, "p_castle_1_3"),#Fanderbilt_Fief
     (party_set_slot, "p_village_1_12", slot_village_bound_center, "p_castle_1_20"),#Dupond_Fief
     (party_set_slot, "p_village_1_13", slot_village_bound_center, "p_castle_1_22"),#Martinez_Fief
     (party_set_slot, "p_village_1_14", slot_village_bound_center, "p_castle_1_24"),#Leroy_Fief
     (party_set_slot, "p_village_1_15", slot_village_bound_center, "p_town_6"),#King of Powell
     (party_set_slot, "p_village_1_16", slot_village_bound_center, "p_town_16"),#Slaufete
     (party_set_slot, "p_village_1_17", slot_village_bound_center, "p_castle_1_12"),#Lefebvre_Fief
     (party_set_slot, "p_village_1_18", slot_village_bound_center, "p_castle_1_8"),#Walrof_Fief
     (party_set_slot, "p_village_1_19", slot_village_bound_center, "p_castle_1_9"),#Wercard_Fief
     (party_set_slot, "p_village_1_20", slot_village_bound_center, "p_town_16"),#Slaufete
     (party_set_slot, "p_village_1_21", slot_village_bound_center, "p_town_7"),#Preist
     (party_set_slot, "p_village_1_22", slot_village_bound_center, "p_castle_1_13"),#Lepez_Fief
     (party_set_slot, "p_village_1_23", slot_village_bound_center, "p_town_6"),#King of Powell
     (party_set_slot, "p_village_1_24", slot_village_bound_center, "p_castle_1_5"),#Hilton_Fief
     (party_set_slot, "p_village_1_25", slot_village_bound_center, "p_town_4"),#Lesaff
     (party_set_slot, "p_village_1_26", slot_village_bound_center, "p_town_7"),#Preist
     (party_set_slot, "p_village_1_27", slot_village_bound_center, "p_town_4"),#Lesaff
     (party_set_slot, "p_village_1_28", slot_village_bound_center, "p_town_4"),#Lesaff
     (party_set_slot, "p_village_1_29", slot_village_bound_center, "p_castle_1_16"),#Guerin_Fief
     (party_set_slot, "p_village_1_30", slot_village_bound_center, "p_castle_1_2"),#Menpaton_Fief
     (party_set_slot, "p_village_1_31", slot_village_bound_center, "p_town_29"),#Sousanth
     (party_set_slot, "p_village_1_32", slot_village_bound_center, "p_castle_1_15"),#Mitterrand_Fief
     (party_set_slot, "p_village_1_33", slot_village_bound_center, "p_castle_1_14"),#Castel_Fief
     (party_set_slot, "p_village_1_34", slot_village_bound_center, "p_castle_1_10"),#Gaccya_Fief
     (party_set_slot, "p_village_1_35", slot_village_bound_center, "p_castle_1_18"),#Roux_Fief
     (party_set_slot, "p_village_1_36", slot_village_bound_center, "p_castle_1_21"),#Gautier_Fief
     (party_set_slot, "p_village_1_37", slot_village_bound_center, "p_castle_1_19"),#Vincent_Fief

     (party_set_slot, "p_village_2_1", slot_village_bound_center, "p_town_13"),#Ardor of Vita
     (party_set_slot, "p_village_2_2", slot_village_bound_center, "p_town_13"),#Ardor of Vita
     (party_set_slot, "p_village_2_3", slot_village_bound_center, "p_castle_2_10"),#Machilus_Kusanoi_Hay_Castle
     (party_set_slot, "p_village_2_4", slot_village_bound_center, "p_castle_2_2"),#Mesua_Ferrea_Castle
     (party_set_slot, "p_village_2_5", slot_village_bound_center, "p_castle_2_11"),#Olea_Europaea_Castle
     (party_set_slot, "p_village_2_6", slot_village_bound_center, "p_town_8"),#Ardor of Soul
     (party_set_slot, "p_village_2_7", slot_village_bound_center, "p_castle_2_7"),#Planchonella_Obovata_Pierre_Castle
     (party_set_slot, "p_village_2_8", slot_village_bound_center, "p_castle_2_5"),#Metasequoia_Glyptostroboides_Castle
     (party_set_slot, "p_village_2_9", slot_village_bound_center, "p_castle_2_6"),#Davidia_Involucrata_Castle
     (party_set_slot, "p_village_2_10", slot_village_bound_center, "p_castle_2_3"),#Pyramidale__Castle
     (party_set_slot, "p_village_2_11", slot_village_bound_center, "p_castle_2_13"),#Osmanthus_Fordii_Hemsl_Castle
     (party_set_slot, "p_village_2_12", slot_village_bound_center, "p_castle_2_4"),#Rhus_Chinensis_Mill_Castle
     (party_set_slot, "p_village_2_13", slot_village_bound_center, "p_town_11"),#Ardor of Ancester

     (party_set_slot, "p_village_2_14", slot_village_bound_center, "p_castle_2_16"),#Yulania_Denudata_Castle
     (party_set_slot, "p_village_2_15", slot_village_bound_center, "p_town_11"),#Ardor of Ancester
     (party_set_slot, "p_village_2_16", slot_village_bound_center, "p_castle_2_14"),#Berberis_Amurensis_Rupr_Castle
     (party_set_slot, "p_village_2_17", slot_village_bound_center, "p_town_8"),#Ardor of Soul
     (party_set_slot, "p_village_2_18", slot_village_bound_center, "p_castle_2_8"),#Cinnamomum_Burmanni_Blume_Castle
     (party_set_slot, "p_village_2_19", slot_village_bound_center, "p_town_13"),#Ardor of Vita
     (party_set_slot, "p_village_2_20", slot_village_bound_center, "p_castle_2_9"),#Platycarya_Strobilacea_Sieb_Castle
     (party_set_slot, "p_village_2_21", slot_village_bound_center, "p_castle_2_1"),#Magnolia_Sinica_Castle
     (party_set_slot, "p_village_2_22", slot_village_bound_center, "p_castle_2_12"),#Osmanthus_Lanceolatus_Hayata_Castle
     (party_set_slot, "p_village_2_23", slot_village_bound_center, "p_town_9"),#Ardor of Demise
     (party_set_slot, "p_village_2_24", slot_village_bound_center, "p_castle_2_15"),#RobiniapseudoacaciaL_Castle

     (party_set_slot, "p_village_3_1", slot_village_bound_center, "p_castle_3_1"),#Xurigan_Barracks
     (party_set_slot, "p_village_3_2", slot_village_bound_center, "p_castle_3_13"),#Aili_Barracks
     (party_set_slot, "p_village_3_3", slot_village_bound_center, "p_castle_3_3"),#Daikan_Barracks
     (party_set_slot, "p_village_3_4", slot_village_bound_center, "p_castle_3_5"),#Huriwuhu_Barracks
     (party_set_slot, "p_village_3_5", slot_village_bound_center, "p_town_10"),#Kouruto
     (party_set_slot, "p_village_3_6", slot_village_bound_center, "p_town_10"),#Kouruto
     (party_set_slot, "p_village_3_7", slot_village_bound_center, "p_castle_3_14"),#Duulag_Barracks
     (party_set_slot, "p_village_3_8", slot_village_bound_center, "p_town_14"),#Menamir
     (party_set_slot, "p_village_3_9", slot_village_bound_center, "p_castle_3_6"),#Boriboge_Barracks
     (party_set_slot, "p_village_3_10", slot_village_bound_center, "p_town_14"),#Menamir
     (party_set_slot, "p_village_3_11", slot_village_bound_center, "p_castle_3_7"),#Batu_Barracks
     (party_set_slot, "p_village_3_12", slot_village_bound_center, "p_castle_3_2"),#Chaoluomeng_Barracks
     (party_set_slot, "p_village_3_13", slot_village_bound_center, "p_town_18"),#Zherrow
     (party_set_slot, "p_village_3_14", slot_village_bound_center, "p_castle_3_4"),#Eridunbari_Barracks
     (party_set_slot, "p_village_3_15", slot_village_bound_center, "p_castle_3_8"),#Alatancang_Barracks
     (party_set_slot, "p_village_3_16", slot_village_bound_center, "p_castle_3_9"),#Narisong_Barracks
     (party_set_slot, "p_village_3_17", slot_village_bound_center, "p_castle_3_11"),#Gajier_Barracks
     (party_set_slot, "p_village_3_18", slot_village_bound_center, "p_castle_3_10"),#Gegen_Barracks
     (party_set_slot, "p_village_3_19", slot_village_bound_center, "p_castle_3_12"),#Namuri_Barracks
     (party_set_slot, "p_village_3_20", slot_village_bound_center, "p_town_10"),#Kouruto
     (party_set_slot, "p_village_3_21", slot_village_bound_center, "p_town_17"),#Midul
     (party_set_slot, "p_village_3_22", slot_village_bound_center, "p_town_17"),#Midul
     (party_set_slot, "p_village_3_23", slot_village_bound_center, "p_town_18"),#Zherrow

     (party_set_slot, "p_village_4_1", slot_village_bound_center, "p_castle_4_8"),#Floatingwaves_Citadel
     (party_set_slot, "p_village_4_2", slot_village_bound_center, "p_castle_4_3"),#Ragewind_Citadel
     (party_set_slot, "p_village_4_3", slot_village_bound_center, "p_town_12"),#Mourngelith
     (party_set_slot, "p_village_4_4", slot_village_bound_center, "p_castle_4_5"),#Fisheleton_Citadel
     (party_set_slot, "p_village_4_5", slot_village_bound_center, "p_castle_4_2"),#Colcloud_Citadel
     (party_set_slot, "p_village_4_6", slot_village_bound_center, "p_town_1"),#Darkfen
     (party_set_slot, "p_village_4_7", slot_village_bound_center, "p_town_1"),#Darkfen
     (party_set_slot, "p_village_4_8", slot_village_bound_center, "p_castle_4_1"),#Resirain_Citadel
     (party_set_slot, "p_village_4_9", slot_village_bound_center, "p_castle_4_14"),#Humidcold_Citadel
     (party_set_slot, "p_village_4_10", slot_village_bound_center, "p_castle_4_6"),#Staplcrew_Citadel
     (party_set_slot, "p_village_4_11", slot_village_bound_center, "p_castle_4_7"),#Frigisun_Citadel
     (party_set_slot, "p_village_4_12", slot_village_bound_center, "p_town_2"),#Norwind
     (party_set_slot, "p_village_4_13", slot_village_bound_center, "p_town_2"),#Norwind
     (party_set_slot, "p_village_4_14", slot_village_bound_center, "p_town_12"),#Mourngelith
     (party_set_slot, "p_village_4_15", slot_village_bound_center, "p_town_12"),#Mourngelith
     (party_set_slot, "p_village_4_16", slot_village_bound_center, "p_castle_4_4"),#Bloodwave_Citadel
     (party_set_slot, "p_village_4_17", slot_village_bound_center, "p_town_2"),#Norwind
     (party_set_slot, "p_village_4_18", slot_village_bound_center, "p_castle_4_11"),#Inversnow_Citadel
     (party_set_slot, "p_village_4_19", slot_village_bound_center, "p_castle_4_15"),#Haze_Citadel
     (party_set_slot, "p_village_4_20", slot_village_bound_center, "p_castle_4_12"),#Corpse-beach_Citadel
     (party_set_slot, "p_village_4_21", slot_village_bound_center, "p_castle_4_9"),#Brackish_Citadel
     (party_set_slot, "p_village_4_22", slot_village_bound_center, "p_town_1"),#Darkfen
     (party_set_slot, "p_village_4_23", slot_village_bound_center, "p_castle_4_10"),#Plantive_Citadel
     (party_set_slot, "p_village_4_24", slot_village_bound_center, "p_castle_4_16"),#Bane_Citadel
     (party_set_slot, "p_village_4_25", slot_village_bound_center, "p_castle_4_13"),#Miasmapain_Citadel

     (party_set_slot, "p_village_5_1", slot_village_bound_center, "p_castle_5_3"),#Grack_Parish
     (party_set_slot, "p_village_5_2", slot_village_bound_center, "p_town_30"),#Whitspring
     (party_set_slot, "p_village_5_3", slot_village_bound_center, "p_town_30"),#Whitspring
     (party_set_slot, "p_village_5_4", slot_village_bound_center, "p_town_5"),#Blesruth
     (party_set_slot, "p_village_5_5", slot_village_bound_center, "p_castle_5_13"),#Abrienne_Parish
     (party_set_slot, "p_village_5_6", slot_village_bound_center, "p_castle_5_4"),#Deruca_Parish
     (party_set_slot, "p_village_5_7", slot_village_bound_center, "p_castle_5_2"),#Mamcheny_Parish
     (party_set_slot, "p_village_5_8", slot_village_bound_center, "p_castle_5_1"),#Camorranash_Parish
     (party_set_slot, "p_village_5_9", slot_village_bound_center, "p_town_31"),#Former the Holiton
     (party_set_slot, "p_village_5_10", slot_village_bound_center, "p_town_31"),#Former the Holiton
     (party_set_slot, "p_village_5_11", slot_village_bound_center, "p_castle_5_14"),#Fiorenza_Parish
     (party_set_slot, "p_village_5_12", slot_village_bound_center, "p_town_3"),#Pilgrimage
     (party_set_slot, "p_village_5_13", slot_village_bound_center, "p_castle_5_9"),#Diego_Parish
     (party_set_slot, "p_village_5_14", slot_village_bound_center, "p_town_5"),#Blesruth
     (party_set_slot, "p_village_5_15", slot_village_bound_center, "p_town_5"),#Blesruth
     (party_set_slot, "p_village_5_16", slot_village_bound_center, "p_castle_5_5"),#Laqiurnay_Parish
     (party_set_slot, "p_village_5_17", slot_village_bound_center, "p_castle_5_6"),#Ethpoxito_Parish
     (party_set_slot, "p_village_5_18", slot_village_bound_center, "p_town_15"),#Baptism
     (party_set_slot, "p_village_5_19", slot_village_bound_center, "p_town_15"),#Baptism
     (party_set_slot, "p_village_5_20", slot_village_bound_center, "p_castle_5_17"),#Cecilio_Parish
     (party_set_slot, "p_village_5_21", slot_village_bound_center, "p_castle_5_8"),#Kongtin_Parish
     (party_set_slot, "p_village_5_22", slot_village_bound_center, "p_castle_5_10"),#Emanuele_Parish
     (party_set_slot, "p_village_5_23", slot_village_bound_center, "p_town_31"),#Former the Holiton
     (party_set_slot, "p_village_5_24", slot_village_bound_center, "p_castle_5_20"),#Giaccherini_Parish
     (party_set_slot, "p_village_5_25", slot_village_bound_center, "p_castle_5_23"),#Cigarini_Parish
     (party_set_slot, "p_village_5_26", slot_village_bound_center, "p_castle_5_16"),#Innocenzio_Parish
     (party_set_slot, "p_village_5_27", slot_village_bound_center, "p_castle_5_7"),#Barroney_Parish
     (party_set_slot, "p_village_5_28", slot_village_bound_center, "p_castle_5_15"),#Fontana_Parish
     (party_set_slot, "p_village_5_29", slot_village_bound_center, "p_town_3"),#Pilgrimage
     (party_set_slot, "p_village_5_30", slot_village_bound_center, "p_castle_5_18"),#Valiant_Parish
     (party_set_slot, "p_village_5_31", slot_village_bound_center, "p_castle_5_19"),#Marcely_Parish
     (party_set_slot, "p_village_5_32", slot_village_bound_center, "p_castle_5_21"),#Ranocchia_Parish
     (party_set_slot, "p_village_5_33", slot_village_bound_center, "p_castle_5_22"),#Chiellini_Parish
     (party_set_slot, "p_village_5_34", slot_village_bound_center, "p_town_30"),#Whitspring
     (party_set_slot, "p_village_5_35", slot_village_bound_center, "p_castle_5_11"),#Gustava_Parish
     (party_set_slot, "p_village_5_36", slot_village_bound_center, "p_castle_5_12"),#Enrichetta_Parish

     (party_set_slot, "p_village_6_1", slot_village_bound_center, "p_castle_6_2"),#Leshui_Fu
     (party_set_slot, "p_village_6_2", slot_village_bound_center, "p_town_27"),#Lizhou
     (party_set_slot, "p_village_6_3", slot_village_bound_center, "p_town_20"),#Shangzhou
     (party_set_slot, "p_village_6_4", slot_village_bound_center, "p_castle_6_1"),#Anyang_Fu
     (party_set_slot, "p_village_6_5", slot_village_bound_center, "p_town_21"),#Yuanzhou
     (party_set_slot, "p_village_6_6", slot_village_bound_center, "p_castle_6_11"),#Hongming_fu
     (party_set_slot, "p_village_6_7", slot_village_bound_center, "p_castle_6_14"),#Qishan_fu
     (party_set_slot, "p_village_6_8", slot_village_bound_center, "p_castle_6_27"),#Zhengjie_fu
     (party_set_slot, "p_village_6_9", slot_village_bound_center, "p_town_22"),#Sakulano
     (party_set_slot, "p_village_6_10", slot_village_bound_center, "p_castle_6_4"),#Gongjing_Fu
     (party_set_slot, "p_village_6_11", slot_village_bound_center, "p_castle_6_39"),#Xicheng_fu
     (party_set_slot, "p_village_6_12", slot_village_bound_center, "p_castle_6_6"),#Shunan_Fu
     (party_set_slot, "p_village_6_13", slot_village_bound_center, "p_castle_6_5"),#Fuchuan_Fu
     (party_set_slot, "p_village_6_14", slot_village_bound_center, "p_town_23"),#Taozhou
     (party_set_slot, "p_village_6_15", slot_village_bound_center, "p_castle_6_13"),#Dongzhi_fu
     (party_set_slot, "p_village_6_16", slot_village_bound_center, "p_town_19"),#Jingzhou
     (party_set_slot, "p_village_6_17", slot_village_bound_center, "p_town_28"),#Yuzhou
     (party_set_slot, "p_village_6_18", slot_village_bound_center, "p_town_20"),#Shangzhou
     (party_set_slot, "p_village_6_19", slot_village_bound_center, "p_castle_6_16"),#Longyun_fu
     (party_set_slot, "p_village_6_20", slot_village_bound_center, "p_town_26"),#Tianzhou
     (party_set_slot, "p_village_6_21", slot_village_bound_center, "p_castle_6_34"),#Shilin_fu
     (party_set_slot, "p_village_6_22", slot_village_bound_center, "p_castle_6_3"),#Huping_Fu
     (party_set_slot, "p_village_6_23", slot_village_bound_center, "p_castle_6_12"),#Lishun_fu
     (party_set_slot, "p_village_6_24", slot_village_bound_center, "p_castle_6_32"),#Riyu_fu
     (party_set_slot, "p_village_6_25", slot_village_bound_center, "p_town_21"),#Yuanzhou
     (party_set_slot, "p_village_6_26", slot_village_bound_center, "p_castle_6_9"),#Tianyuan_fu
     (party_set_slot, "p_village_6_27", slot_village_bound_center, "p_castle_6_7"),#Zhitiangu_Fu
     (party_set_slot, "p_village_6_28", slot_village_bound_center, "p_town_22"),#Sakulano
     (party_set_slot, "p_village_6_29", slot_village_bound_center, "p_castle_6_29"),#Mingqi_fu
     (party_set_slot, "p_village_6_30", slot_village_bound_center, "p_castle_6_21"),#Cexun_fu
     (party_set_slot, "p_village_6_31", slot_village_bound_center, "p_town_19"),#Jingzhou
     (party_set_slot, "p_village_6_32", slot_village_bound_center, "p_town_19"),#Jingzhou
     (party_set_slot, "p_village_6_33", slot_village_bound_center, "p_town_19"),#Jingzhou
     (party_set_slot, "p_village_6_34", slot_village_bound_center, "p_town_23"),#Taozhou
     (party_set_slot, "p_village_6_35", slot_village_bound_center, "p_castle_6_10"),#Tuoyang_fu
     (party_set_slot, "p_village_6_36", slot_village_bound_center, "p_town_20"),#Shangzhou
     (party_set_slot, "p_village_6_37", slot_village_bound_center, "p_town_27"),#Lizhou
     (party_set_slot, "p_village_6_38", slot_village_bound_center, "p_town_25"),#Pingzhou
     (party_set_slot, "p_village_6_39", slot_village_bound_center, "p_town_27"),#lizhou
     (party_set_slot, "p_village_6_40", slot_village_bound_center, "p_castle_6_19"),#Guji_fu
     (party_set_slot, "p_village_6_41", slot_village_bound_center, "p_castle_6_20"),#Fengwei_fu
     (party_set_slot, "p_village_6_42", slot_village_bound_center, "p_castle_6_15"),#Lianyang_fu
     (party_set_slot, "p_village_6_43", slot_village_bound_center, "p_castle_6_26"),#Fengyong_fu
     (party_set_slot, "p_village_6_44", slot_village_bound_center, "p_castle_6_25"),#Jiazhou_fu
     (party_set_slot, "p_village_6_45", slot_village_bound_center, "p_castle_6_30"),#Qiaoyue_fu
     (party_set_slot, "p_village_6_46", slot_village_bound_center, "p_town_24"),#Xizhou
     (party_set_slot, "p_village_6_47", slot_village_bound_center, "p_castle_6_33"),#Shidao_fu
     (party_set_slot, "p_village_6_48", slot_village_bound_center, "p_castle_6_36"),#Zhengshan_fu
     (party_set_slot, "p_village_6_49", slot_village_bound_center, "p_town_24"),#Xizhou
     (party_set_slot, "p_village_6_50", slot_village_bound_center, "p_castle_6_38"),#Wushi_fu
     (party_set_slot, "p_village_6_51", slot_village_bound_center, "p_castle_6_18"),#Xingzhao_fu
     (party_set_slot, "p_village_6_52", slot_village_bound_center, "p_castle_6_31"),#Shangshu_fu
     (party_set_slot, "p_village_6_53", slot_village_bound_center, "p_town_25"),#Pingzhou
     (party_set_slot, "p_village_6_54", slot_village_bound_center, "p_castle_6_37"),#Tuge_fu
     (party_set_slot, "p_village_6_55", slot_village_bound_center, "p_castle_6_40"),#Wulie_fu
     (party_set_slot, "p_village_6_56", slot_village_bound_center, "p_town_28"),#Yuzhou
     (party_set_slot, "p_village_6_57", slot_village_bound_center, "p_castle_6_8"),#Mingshun_fu
     (party_set_slot, "p_village_6_58", slot_village_bound_center, "p_town_22"),#Sakulano
     (party_set_slot, "p_village_6_59", slot_village_bound_center, "p_town_23"),#Taozhou
     (party_set_slot, "p_village_6_60", slot_village_bound_center, "p_castle_6_17"),#Xichaun_fu
     (party_set_slot, "p_village_6_61", slot_village_bound_center, "p_town_26"),#Tianzhou
     (party_set_slot, "p_village_6_62", slot_village_bound_center, "p_town_28"),#Yuzhou
     (party_set_slot, "p_village_6_63", slot_village_bound_center, "p_castle_6_28"),#kesu_fu
     (party_set_slot, "p_village_6_64", slot_village_bound_center, "p_castle_6_35"),#Silun_fu
     (party_set_slot, "p_village_6_65", slot_village_bound_center, "p_castle_6_22"),#Baijian_fu
     (party_set_slot, "p_village_6_66", slot_village_bound_center, "p_castle_6_24"),#Huoluo_fu
     (party_set_slot, "p_village_6_67", slot_village_bound_center, "p_castle_6_23"),#Gongxu_fu

     (party_set_slot, "p_village_7_1", slot_village_bound_center, "p_town_32"),#Starkhook
     (party_set_slot, "p_village_7_2", slot_village_bound_center, "p_castle_7_1"),#White_Fortress
     (party_set_slot, "p_village_7_3", slot_village_bound_center, "p_town_33"),#Tradewind
     (party_set_slot, "p_village_7_4", slot_village_bound_center, "p_town_33"),#Tradewind
     (party_set_slot, "p_village_7_5", slot_village_bound_center, "p_castle_7_2"),#Tower_Fortress
     (party_set_slot, "p_village_7_6", slot_village_bound_center, "p_town_33"),#Tradewind
     (party_set_slot, "p_village_7_7", slot_village_bound_center, "p_castle_7_3"),#Oceanwatch_Fortress
     (party_set_slot, "p_village_7_8", slot_village_bound_center, "p_castle_7_5"),#Endmountain_Fortress
     (party_set_slot, "p_village_7_9", slot_village_bound_center, "p_town_32"),#Starkhook
     (party_set_slot, "p_village_7_10", slot_village_bound_center, "p_castle_7_4"),#South_Fortress
     (party_set_slot, "p_village_7_11", slot_village_bound_center, "p_town_32"),#Starkhook

     (party_set_slot, "p_village_8_1", slot_village_bound_center, "p_town_34"),#Congress
     (party_set_slot, "p_village_8_2", slot_village_bound_center, "p_castle_8_2"),#Guilio_State
     (party_set_slot, "p_village_8_3", slot_village_bound_center, "p_castle_8_1"),#Francesco_State
     (party_set_slot, "p_village_8_4", slot_village_bound_center, "p_town_34"),#Congress
     (party_set_slot, "p_village_8_5", slot_village_bound_center, "p_town_34"),#Congress
     (party_set_slot, "p_village_8_6", slot_village_bound_center, "p_castle_8_3"),#Luca_State
     (party_set_slot, "p_village_8_7", slot_village_bound_center, "p_castle_8_4"),#Giuseppe_State

      (try_for_range, ":village_no", villages_begin, villages_end),
         (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
         (store_faction_of_party, ":bound_center_faction", ":bound_center"),
         (call_script, "script_give_center_to_faction_aux", ":village_no", ":bound_center_faction"),
      (try_end),

      		  	  
	# Towns (loop)
      (try_for_range, ":town_no", towns_begin, towns_end),
        (store_sub, ":offset", ":town_no", towns_begin),
        (party_set_slot,":town_no", slot_party_type, spt_town),
        #(store_add, ":cur_object_no", "trp_town_1_seneschal", ":offset"),
        #(party_set_slot,":town_no", slot_town_seneschal, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_center", ":offset"),
        (party_set_slot,":town_no", slot_town_center, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_castle", ":offset"),
        (party_set_slot,":town_no", slot_town_castle, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_prison", ":offset"),
        (party_set_slot,":town_no", slot_town_prison, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_walls", ":offset"),
        (party_set_slot,":town_no", slot_town_walls, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_tavern", ":offset"),
        (party_set_slot,":town_no", slot_town_tavern, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_store", ":offset"),
        (party_set_slot,":town_no", slot_town_store, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_arena", ":offset"),
        (party_set_slot,":town_no", slot_town_arena, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_alley", ":offset"),
        (party_set_slot,":town_no", slot_town_alley, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_mayor", ":offset"),
        (party_set_slot,":town_no", slot_town_elder, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_tavernkeeper", ":offset"),
        (party_set_slot,":town_no", slot_town_tavernkeeper, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_weaponsmith", ":offset"),
        (party_set_slot,":town_no", slot_town_weaponsmith, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_armorer", ":offset"),
        (party_set_slot,":town_no", slot_town_armorer, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_merchant", ":offset"),
        (party_set_slot,":town_no", slot_town_merchant, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_horse_merchant", ":offset"),
        (party_set_slot,":town_no", slot_town_horse_merchant, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_center", ":offset"),
        (party_set_slot,":town_no", slot_town_center, ":cur_object_no"),
        (party_set_slot,":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
      (try_end),
	  	  
# Castles
      (try_for_range, ":castle_no", castles_begin, castles_end),
        (store_sub, ":offset", ":castle_no", castles_begin),
        (val_mul, ":offset", 3),

#        (store_add, ":senechal_troop_no", "trp_castle_1_seneschal", ":offset"),
#        (party_set_slot,":castle_no", slot_town_seneschal, ":senechal_troop_no"),
        (store_add, ":exterior_scene_no", "scn_castle_1_1_exterior", ":offset"),
        (party_set_slot,":castle_no", slot_castle_exterior, ":exterior_scene_no"),
        (store_add, ":interior_scene_no", "scn_castle_1_1_interior", ":offset"),
        (party_set_slot,":castle_no", slot_town_castle, ":interior_scene_no"),
        (store_add, ":interior_scene_no", "scn_castle_1_1_prison", ":offset"),
        (party_set_slot,":castle_no", slot_town_prison, ":interior_scene_no"),
        
        (party_set_slot,":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
        (party_set_slot,":castle_no", slot_party_type, spt_castle),
        (party_set_slot,":castle_no", slot_center_is_besieged_by, -1),
      (try_end),

# Set which castles need to be attacked with siege towers.
      (party_set_slot,"p_town_13", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_town_16", slot_center_siege_with_belfry, 1),

      (party_set_slot,"p_castle_1_2", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_1_6", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_1_10", slot_center_siege_with_belfry, 1),

      (party_set_slot,"p_castle_2_2", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_2_3", slot_center_siege_with_belfry, 1),

      (party_set_slot,"p_castle_3_1", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_3_2", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_3_6", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_3_7", slot_center_siege_with_belfry, 1),

      (party_set_slot,"p_castle_4_3", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_4_6", slot_center_siege_with_belfry, 1),

      (party_set_slot,"p_castle_5_1", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_5_2", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_5_6", slot_center_siege_with_belfry, 1),

      (party_set_slot,"p_castle_6_1", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_6_2", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_6_3", slot_center_siege_with_belfry, 1),

#设置村庄相关内容
      (try_for_range, ":village_no", villages_begin, villages_end),
         (store_sub, ":offset", ":village_no", villages_begin),

         (store_add, ":exterior_scene_no", "scn_village_1_1", ":offset"),
         (party_set_slot,":village_no", slot_castle_exterior, ":exterior_scene_no"), #设置村庄场景
      
         (store_add, ":store_troop_no", "trp_village_1_1_elder", ":offset"),
         (party_set_slot,":village_no", slot_town_elder, ":store_troop_no"), #设置村庄长老
        
         (party_set_slot,":village_no", slot_party_type, spt_village),
         (party_set_slot,":village_no", slot_village_raided_by, -1), #设置村庄相关slot，包括类型和没被洗劫
      
#         (call_script, "script_refresh_village_defenders", ":village_no"),#刷出少量农民
      (try_end),
      
      (try_for_range, ":center_no", centers_begin, centers_end),
        (party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
        (party_set_slot, ":center_no", slot_center_is_besieged_by, -1),
        (party_set_slot, ":center_no", slot_center_last_taken_by_troop, -1),
      (try_end),

# Troops:

# Assign banners and renown.
# We assume there are enough banners for all kingdom heroes.

      #faction banners
      (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_c"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_d"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_e"),
      (faction_set_slot, "fac_kingdom_7", slot_faction_banner, "mesh_banner_kingdom_e"),
      (faction_set_slot, "fac_kingdom_8", slot_faction_banner, "mesh_banner_kingdom_e"),

      (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, ":cur_faction_king", ":cur_faction", slot_faction_leader),
        (faction_get_slot, ":cur_faction_banner", ":cur_faction", slot_faction_banner),
        (val_sub, ":cur_faction_banner", banner_meshes_begin),
        (val_add, ":cur_faction_banner", banner_scene_props_begin),
        (troop_set_slot, ":cur_faction_king", slot_troop_banner_scene_prop, ":cur_faction_banner"),
      (try_end),
      (assign, ":num_khergit_lords_assigned", 0),
      (assign, ":num_sarranid_lords_assigned", 0),
      (assign, ":num_other_lords_assigned", 0),
            
      (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
        (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_inactive_pretender),
        

#把据点分配给国家
	  #Give centers to factions first, to ensure more equal distributions
	  (call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_4"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_2", "fac_kingdom_4"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_3", "fac_kingdom_5"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_4", "fac_kingdom_1"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_5", "fac_kingdom_5"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_6", "fac_kingdom_1"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_7", "fac_kingdom_1"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_8", "fac_kingdom_2"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_9", "fac_kingdom_2"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_10", "fac_kingdom_3"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_11", "fac_kingdom_2"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_12", "fac_kingdom_4"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_13", "fac_kingdom_2"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_14", "fac_kingdom_3"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_15", "fac_kingdom_5"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_16", "fac_kingdom_1"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_17", "fac_kingdom_3"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_18", "fac_kingdom_3"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_19", "fac_kingdom_6"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_20", "fac_kingdom_6"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_21", "fac_kingdom_6"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_22", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_23", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_24", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_25", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_26", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_27", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_28", "fac_kingdom_6"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_29", "fac_kingdom_1"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_30", "fac_kingdom_5"),
                  (call_script, "script_give_center_to_faction_aux", "p_town_31", "fac_kingdom_5"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_32", "fac_kingdom_7"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_33", "fac_kingdom_7"),
	  (call_script, "script_give_center_to_faction_aux", "p_town_34", "fac_kingdom_8"),
	  
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_1", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_2", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_3", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_4", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_5", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_6", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_7", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_8", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_9", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_10", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_11", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_12", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_13", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_14", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_15", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_16", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_17", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_18", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_19", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_20", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_21", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_22", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_23", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_1_24", "fac_kingdom_1"),

      (call_script, "script_give_center_to_faction_aux", "p_castle_2_1", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_2", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_3", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_4", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_5", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_6", "fac_kingdom_2"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_7", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_8", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_9", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_10", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_11", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_12", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_13", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_14", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_15", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2_16", "fac_kingdom_2"),

      (call_script, "script_give_center_to_faction_aux", "p_castle_3_1", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_2", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_3", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_4", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_5", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_6", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_7", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_8", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_9", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_10", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_11", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_12", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_13", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3_14", "fac_kingdom_3"),

      (call_script, "script_give_center_to_faction_aux", "p_castle_4_1", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_2", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_3", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_4", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_5", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_6", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_7", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_8", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_9", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_10", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_11", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_12", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_13", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_14", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_15", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4_16", "fac_kingdom_4"),

      (call_script, "script_give_center_to_faction_aux", "p_castle_5_1", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_2", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_3", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_4", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_5", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_6", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_7", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_8", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_9", "fac_kingdom_5"),    
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_10", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_11", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_12", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_13", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_14", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_15", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_16", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_17", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_18", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_19", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_20", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_21", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_22", "fac_kingdom_5"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_5_23", "fac_kingdom_5"), 

      (call_script, "script_give_center_to_faction_aux", "p_castle_6_1", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_2", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_3", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_4", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_5", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_6", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_7", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_8", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_9", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_10", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_11", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_12", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_13", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_14", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_15", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_16", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_17", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_18", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_19", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_20", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_21", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_22", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_23", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_24", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_25", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_26", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_27", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_28", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_29", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_30", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_31", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_32", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_33", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_34", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_35", "fac_kingdom_6"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_6_36", "fac_kingdom_6"), 

      (call_script, "script_give_center_to_faction_aux", "p_castle_7_1", "fac_kingdom_7"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_7_2", "fac_kingdom_7"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_7_3", "fac_kingdom_7"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_7_4", "fac_kingdom_7"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_7_5", "fac_kingdom_7"), 

      (call_script, "script_give_center_to_faction_aux", "p_castle_8_1", "fac_kingdom_8"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_8_2", "fac_kingdom_8"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_8_3", "fac_kingdom_8"), 
      (call_script, "script_give_center_to_faction_aux", "p_castle_8_4", "fac_kingdom_8"), 

#给领主分配领地
      #powell
      (call_script, "script_give_center_to_lord", "p_town_4",  "trp_knight_1_1", 0),
      (call_script, "script_give_center_to_lord", "p_town_6",  "trp_kingdom_1_lord", 0),
      (call_script, "script_give_center_to_lord", "p_town_7",  "trp_knight_1_3", 0),
      (call_script, "script_give_center_to_lord", "p_town_16",  "trp_knight_1_2", 0),
      (call_script, "script_give_center_to_lord", "p_town_29",  "trp_knight_1_4", 0),

      #yishith
      (call_script, "script_give_center_to_lord", "p_town_8",  "trp_kingdom_2_lord", 0),
      (call_script, "script_give_center_to_lord", "p_town_9",  "trp_knight_2_1", 0),
      (call_script, "script_give_center_to_lord", "p_town_11",  "trp_knight_2_2", 0),
      (call_script, "script_give_center_to_lord", "p_town_13",  "trp_knight_2_3", 0),

      #korouto     
      (call_script, "script_give_center_to_lord", "p_town_10",  "trp_kingdom_3_lord", 0),
      (call_script, "script_give_center_to_lord", "p_town_14",  "trp_knight_3_1", 0),
      (call_script, "script_give_center_to_lord", "p_town_17", "trp_knight_3_2", 0),
      (call_script, "script_give_center_to_lord", "p_town_18", "trp_knight_3_3", 0),

      #conferderation
      (call_script, "script_give_center_to_lord", "p_town_1", "trp_kingdom_4_lord", 0),
      (call_script, "script_give_center_to_lord", "p_town_2", "trp_knight_4_1", 0),
      (call_script, "script_give_center_to_lord", "p_town_12", "trp_knight_4_2", 0),

      #papal
      (call_script, "script_give_center_to_lord", "p_town_3", "trp_knight_5_1", 0),
      (call_script, "script_give_center_to_lord", "p_town_5", "trp_kingdom_5_lord", 0), 
      (call_script, "script_give_center_to_lord", "p_town_15", "trp_knight_5_2", 0),
      (call_script, "script_give_center_to_lord", "p_town_30", "trp_knight_5_3", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_31", "trp_knight_5_4", 0),

      #longshu
      (call_script, "script_give_center_to_lord", "p_town_19", "trp_kingdom_6_lord", 0),
      (call_script, "script_give_center_to_lord", "p_town_20", "trp_knight_6_1", 0), 
      (call_script, "script_give_center_to_lord", "p_town_21", "trp_knight_6_2", 0),
      (call_script, "script_give_center_to_lord", "p_town_22", "trp_knight_6_8", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_23", "trp_knight_6_9", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_24", "trp_knight_6_3", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_25", "trp_knight_6_7", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_26", "trp_knight_6_5", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_27", "trp_knight_6_6", 0),	  
      (call_script, "script_give_center_to_lord", "p_town_28", "trp_knight_6_4", 0),	  

      #starkhook
      (call_script, "script_give_center_to_lord", "p_town_32", "trp_kingdom_7_lord", 0),
      (call_script, "script_give_center_to_lord", "p_town_33", "trp_knight_7_1", 0),

      #state
      (call_script, "script_give_center_to_lord", "p_town_34", "trp_kingdom_8_lord", 0),	  

                              # Give family castles and village to certain nobles.
##____________________________________________________________________________powell____________________________________________________________________________
#father lords 5 to 19
      (call_script, "script_give_center_to_lord", "p_castle_1_1", "trp_knight_1_6", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_2", "trp_knight_1_8", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_3", "trp_knight_1_12", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_4", "trp_knight_1_14", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_5", "trp_knight_1_15", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_6", "trp_knight_1_7", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_7", "trp_knight_1_11", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_8", "trp_knight_1_9", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_9", "trp_knight_1_10", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_10", "trp_knight_1_5", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_11", "trp_knight_1_13", 0), 

#bachelor village lord 16 to 19
      (call_script, "script_give_center_to_lord", "p_village_1_2", "trp_knight_1_16", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_7", "trp_knight_1_17", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_9", "trp_knight_1_18", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_12", "trp_knight_1_19", 0), 

#son lords(village lord) 20 to 34
      (call_script, "script_give_center_to_lord", "p_village_1_1", "trp_knight_1_23", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_3", "trp_knight_1_32", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_4", "trp_knight_1_25", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_5", "trp_knight_1_33", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_6", "trp_knight_1_26", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_8", "trp_knight_1_22", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_10", "trp_knight_1_30", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_11", "trp_knight_1_31", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_16", "trp_knight_1_21", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_18", "trp_knight_1_28", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_19", "trp_knight_1_29", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_20", "trp_knight_1_21", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_21", "trp_knight_1_22", 0), 
#      (call_script, "script_give_center_to_lord", "p_village_1_23", "trp_knight_1_16", 0), #spare village
      (call_script, "script_give_center_to_lord", "p_village_1_24", "trp_knight_1_34", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_25", "trp_knight_1_20", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_27", "trp_knight_1_20", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_30", "trp_knight_1_27", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_31", "trp_knight_1_23", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_34", "trp_knight_1_24", 0), 

#bachelor castle lord 35 to 47
      (call_script, "script_give_center_to_lord", "p_castle_1_12", "trp_knight_1_35", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_13", "trp_knight_1_36", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_14", "trp_knight_1_37", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_15", "trp_knight_1_38", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_16", "trp_knight_1_39", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_17", "trp_knight_1_40", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_18", "trp_knight_1_41", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_19", "trp_knight_1_42", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_20", "trp_knight_1_43", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_21", "trp_knight_1_44", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_22", "trp_knight_1_45", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_23", "trp_knight_1_46", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_1_24", "trp_knight_1_47", 0), 

#bachelor village lord 48 to 60
      (call_script, "script_give_center_to_lord", "p_village_1_13", "trp_knight_1_48", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_14", "trp_knight_1_49", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_15", "trp_knight_1_50", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_17", "trp_knight_1_51", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_22", "trp_knight_1_52", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_26", "trp_knight_1_53", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_28", "trp_knight_1_54", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_29", "trp_knight_1_55", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_32", "trp_knight_1_56", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_33", "trp_knight_1_57", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_35", "trp_knight_1_58", 0), 
      (call_script, "script_give_center_to_lord", "p_village_1_36", "trp_knight_1_59", 0),
      (call_script, "script_give_center_to_lord", "p_village_1_37", "trp_knight_1_60", 0),



##____________________________________________________________________________yishith____________________________________________________________________________
#father lords 4 to 11
      (call_script, "script_give_center_to_lord", "p_castle_2_1", "trp_knight_2_4", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_2", "trp_knight_2_5", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_3", "trp_knight_2_6", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_4", "trp_knight_2_7", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_5", "trp_knight_2_8", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_6", "trp_knight_2_9", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_7", "trp_knight_2_10", 0), 

      (call_script, "script_give_center_to_lord", "p_village_2_3", "trp_knight_2_3", 0),
      (call_script, "script_give_center_to_lord", "p_village_2_6", "trp_kingdom_2_lord", 0),
#bachelor village lord 11 to 14
      (call_script, "script_give_center_to_lord", "p_castle_2_8", "trp_knight_2_11", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_5", "trp_knight_2_12", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_11", "trp_knight_2_13", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_14", "trp_knight_2_14", 0), 

#son lords(village lord) 16 to 24
      (call_script, "script_give_center_to_lord", "p_village_2_1", "trp_knight_2_17", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_2", "trp_knight_2_17", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_4", "trp_knight_2_19", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_7", "trp_knight_2_24", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_8", "trp_knight_2_22", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_9", "trp_knight_2_23", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_10", "trp_knight_2_20", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_12", "trp_knight_2_21", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_13", "trp_knight_2_16", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_15", "trp_knight_2_16", 0), 
#      (call_script, "script_give_center_to_lord", "p_village_2_17", "trp_kingdom_2_lord", 0),#spare
      (call_script, "script_give_center_to_lord", "p_village_2_21", "trp_knight_2_18", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_23", "trp_knight_2_15", 0), 

#bachelor castle lord 25 to 32
      (call_script, "script_give_center_to_lord", "p_castle_2_9", "trp_knight_2_25", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_10", "trp_knight_2_26", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_11", "trp_knight_2_27", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_12", "trp_knight_2_28", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_13", "trp_knight_2_29", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_14", "trp_knight_2_30", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_15", "trp_knight_2_31", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_2_16", "trp_knight_2_32", 0), 

#bachelor village lord 33 to 38
      (call_script, "script_give_center_to_lord", "p_village_2_16", "trp_knight_2_33", 0),
      (call_script, "script_give_center_to_lord", "p_village_2_18", "trp_knight_2_34", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_19", "trp_knight_2_35", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_20", "trp_knight_2_36", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_22", "trp_knight_2_37", 0), 
      (call_script, "script_give_center_to_lord", "p_village_2_24", "trp_knight_2_38", 0), 



##____________________________________________________________________________korouto____________________________________________________________________________
#father lords 4 to 11
      (call_script, "script_give_center_to_lord", "p_castle_3_1", "trp_knight_3_4", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_2", "trp_knight_3_5", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_3", "trp_knight_3_22", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_4", "trp_knight_3_7", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_5", "trp_knight_3_8", 0), 

#bachelor castle lord 9 and 10
      (call_script, "script_give_center_to_lord", "p_castle_3_6", "trp_knight_3_9", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_7", "trp_knight_3_10", 0), 
#bachelor village lord 11 and 12
      (call_script, "script_give_center_to_lord", "p_village_3_5", "trp_knight_3_11", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_6", "trp_knight_3_12", 0), 

#son lords(village lord) 11 to 20
      (call_script, "script_give_center_to_lord", "p_village_3_1", "trp_knight_3_16", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_3", "trp_knight_3_18", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_4", "trp_knight_3_20", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_8", "trp_knight_3_13", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_10", "trp_knight_3_13", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_12", "trp_knight_3_17", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_13", "trp_knight_3_15", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_14", "trp_knight_3_19", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_21", "trp_knight_3_14", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_22", "trp_knight_3_14", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_23", "trp_knight_3_15", 0), 

#bachelor castle lord 21 to 27
      (call_script, "script_give_center_to_lord", "p_castle_3_8", "trp_knight_3_21", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_9", "trp_knight_3_6", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_10", "trp_knight_3_23", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_11", "trp_knight_3_24", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_12", "trp_knight_3_25", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_13", "trp_knight_3_26", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_3_14", "trp_knight_3_27", 0), 

#bachelor village lord 33 to 38
      (call_script, "script_give_center_to_lord", "p_village_3_2", "trp_knight_3_28", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_7", "trp_knight_3_29", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_9", "trp_knight_3_30", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_11", "trp_knight_3_31", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_15", "trp_knight_3_32", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_16", "trp_knight_3_33", 0), 
#      (call_script, "script_give_center_to_lord", "p_village_3_17", "trp_knight_3_35", 0), #spare
#      (call_script, "script_give_center_to_lord", "p_village_3_18", "trp_knight_3_35", 0), #spare
      (call_script, "script_give_center_to_lord", "p_village_3_19", "trp_knight_3_34", 0), 
      (call_script, "script_give_center_to_lord", "p_village_3_20", "trp_knight_3_35", 0), 



##____________________________________________________________________________conferderation____________________________________________________________________________
#father lords 4 to 11
      (call_script, "script_give_center_to_lord", "p_castle_4_1", "trp_knight_4_4", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_2", "trp_knight_4_5", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_3", "trp_knight_4_6", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_4", "trp_knight_4_7", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_5", "trp_knight_4_8", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_6", "trp_knight_4_9", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_7", "trp_knight_4_10", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_8", "trp_knight_4_3", 0), 

      (call_script, "script_give_center_to_lord", "p_village_4_6", "trp_knight_4_1", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_7", "trp_knight_4_2", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_22", "trp_knight_4_3", 0), 
#bachelor castle lord 11
      (call_script, "script_give_center_to_lord", "p_castle_4_9", "trp_knight_4_11", 0), 
#bachelor village lord 12 to 14
      (call_script, "script_give_center_to_lord", "p_village_4_9", "trp_knight_4_12", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_14", "trp_knight_4_13", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_17", "trp_knight_4_14", 0), 

#son lords(village lord) 15 to 24
      (call_script, "script_give_center_to_lord", "p_village_4_1", "trp_knight_4_17", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_2", "trp_knight_4_20", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_3", "trp_knight_4_16", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_4", "trp_knight_4_22", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_5", "trp_knight_4_19", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_8", "trp_knight_4_33", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_10", "trp_knight_4_23", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_11", "trp_knight_4_24", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_12", "trp_knight_4_15", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_13", "trp_knight_4_15", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_15", "trp_knight_4_16", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_16", "trp_knight_4_21", 0), 

#bachelor castle lord 25 to 31
      (call_script, "script_give_center_to_lord", "p_castle_4_10", "trp_knight_4_25", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_11", "trp_knight_4_26", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_12", "trp_knight_4_27", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_13", "trp_knight_4_28", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_14", "trp_knight_4_29", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_15", "trp_knight_4_30", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_4_16", "trp_knight_4_31", 0), 

#bachelor village lord 32 to 38
      (call_script, "script_give_center_to_lord", "p_village_4_18", "trp_knight_4_32", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_19", "trp_knight_4_18", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_20", "trp_knight_4_34", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_21", "trp_knight_4_35", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_23", "trp_knight_4_36", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_24", "trp_knight_4_37", 0), 
      (call_script, "script_give_center_to_lord", "p_village_4_25", "trp_knight_4_38", 0), 



##____________________________________________________________________________papal____________________________________________________________________________
#father lords
      (call_script, "script_give_center_to_lord", "p_castle_5_1", "trp_knight_5_5", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_2", "trp_knight_5_6", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_3", "trp_knight_5_7", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_4", "trp_knight_5_8", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_5", "trp_knight_5_9", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_6", "trp_knight_5_10", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_7", "trp_knight_5_11", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_8", "trp_knight_5_12", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_9", "trp_knight_5_13", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_10", "trp_knight_5_14", 0), 

#son lords(village lord)
      (call_script, "script_give_center_to_lord", "p_village_5_1", "trp_knight_5_15", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_2", "trp_knight_5_16", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_3", "trp_knight_5_17", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_4", "trp_knight_5_18", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_5", "trp_knight_5_19", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_6", "trp_knight_5_20", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_7", "trp_knight_5_21", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_8", "trp_knight_5_22", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_9", "trp_knight_5_23", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_10", "trp_knight_5_24", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_11", "trp_knight_5_25", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_12", "trp_knight_5_26", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_13", "trp_knight_5_27", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_14", "trp_knight_5_28", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_15", "trp_knight_5_29", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_16", "trp_knight_5_30", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_17", "trp_knight_5_31", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_18", "trp_knight_5_32", 0), 

#bachelor castle lords
      (call_script, "script_give_center_to_lord", "p_castle_5_11", "trp_knight_5_33", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_12", "trp_knight_5_34", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_13", "trp_knight_5_35", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_14", "trp_knight_5_36", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_15", "trp_knight_5_37", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_16", "trp_knight_5_38", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_17", "trp_knight_5_39", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_18", "trp_knight_5_40", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_19", "trp_knight_5_41", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_20", "trp_knight_5_42", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_21", "trp_knight_5_43", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_22", "trp_knight_5_44", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_5_23", "trp_knight_5_45", 0), 

#bachelor village lords
      (call_script, "script_give_center_to_lord", "p_village_5_19", "trp_knight_5_46", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_20", "trp_knight_5_47", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_21", "trp_knight_5_48", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_22", "trp_knight_5_49", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_23", "trp_knight_5_50", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_24", "trp_knight_5_51", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_25", "trp_knight_5_52", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_26", "trp_knight_5_53", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_27", "trp_knight_5_54", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_28", "trp_knight_5_55", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_29", "trp_knight_5_56", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_30", "trp_knight_5_57", 0), 
      (call_script, "script_give_center_to_lord", "p_village_5_31", "trp_knight_5_58", 0), 



##____________________________________________________________________________longshu____________________________________________________________________________
#longshu has no spare
      (call_script, "script_give_center_to_lord", "p_castle_6_1", "trp_knight_6_10", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_2", "trp_knight_6_11", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_3", "trp_knight_6_12", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_4", "trp_knight_6_13", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_5", "trp_knight_6_14", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_6", "trp_knight_6_15", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_7", "trp_knight_6_16", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_8", "trp_knight_6_17", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_9", "trp_knight_6_18", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_10", "trp_knight_6_19", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_11", "trp_knight_6_20", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_12", "trp_knight_6_21", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_13", "trp_knight_6_22", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_14", "trp_knight_6_23", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_15", "trp_knight_6_24", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_16", "trp_knight_6_25", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_17", "trp_knight_6_26", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_18", "trp_knight_6_27", 0), 

      (call_script, "script_give_center_to_lord", "p_castle_6_19", "trp_knight_6_65", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_20", "trp_knight_6_66", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_21", "trp_knight_6_67", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_22", "trp_knight_6_68", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_23", "trp_knight_6_69", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_24", "trp_knight_6_70", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_25", "trp_knight_6_71", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_26", "trp_knight_6_72", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_27", "trp_knight_6_73", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_28", "trp_knight_6_74", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_29", "trp_knight_6_75", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_30", "trp_knight_6_76", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_31", "trp_knight_6_77", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_32", "trp_knight_6_78", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_33", "trp_knight_6_79", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_34", "trp_knight_6_80", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_35", "trp_knight_6_81", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_36", "trp_knight_6_82", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_37", "trp_knight_6_83", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_38", "trp_knight_6_84", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_39", "trp_knight_6_85", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_6_40", "trp_knight_6_86", 0), 

      (call_script, "script_give_center_to_lord", "p_village_6_1", "trp_knight_6_28", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_2", "trp_knight_6_29", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_3", "trp_knight_6_30", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_4", "trp_knight_6_31", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_5", "trp_knight_6_32", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_6", "trp_knight_6_33", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_7", "trp_knight_6_34", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_8", "trp_knight_6_35", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_9", "trp_knight_6_42", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_10", "trp_knight_6_37", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_11", "trp_knight_6_38", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_12", "trp_knight_6_39", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_13", "trp_knight_6_40", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_14", "trp_knight_6_43", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_15", "trp_knight_6_36", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_16", "trp_knight_6_41", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_17", "trp_knight_6_44", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_18", "trp_knight_6_45", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_19", "trp_knight_6_46", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_20", "trp_knight_6_47", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_21", "trp_knight_6_48", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_22", "trp_knight_6_49", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_23", "trp_knight_6_50", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_24", "trp_knight_6_51", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_25", "trp_knight_6_52", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_26", "trp_knight_6_53", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_27", "trp_knight_6_54", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_28", "trp_knight_6_55", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_29", "trp_knight_6_56", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_30", "trp_knight_6_57", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_31", "trp_knight_6_58", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_32", "trp_knight_6_59", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_33", "trp_knight_6_60", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_34", "trp_knight_6_61", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_35", "trp_knight_6_62", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_36", "trp_knight_6_63", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_37", "trp_knight_6_64", 0), 

      (call_script, "script_give_center_to_lord", "p_village_6_38", "trp_knight_6_87", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_39", "trp_knight_6_88", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_40", "trp_knight_6_89", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_41", "trp_knight_6_90", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_42", "trp_knight_6_91", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_43", "trp_knight_6_92", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_44", "trp_knight_6_93", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_45", "trp_knight_6_94", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_46", "trp_knight_6_95", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_47", "trp_knight_6_96", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_48", "trp_knight_6_97", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_49", "trp_knight_6_98", 0),
      (call_script, "script_give_center_to_lord", "p_village_6_50", "trp_knight_6_99", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_51", "trp_knight_6_100", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_52", "trp_knight_6_101", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_53", "trp_knight_6_102", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_54", "trp_knight_6_103", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_55", "trp_knight_6_104", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_56", "trp_knight_6_105", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_57", "trp_knight_6_106", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_58", "trp_knight_6_107", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_59", "trp_knight_6_108", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_60", "trp_knight_6_109", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_61", "trp_knight_6_110", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_62", "trp_knight_6_111", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_63", "trp_knight_6_112", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_64", "trp_knight_6_113", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_65", "trp_knight_6_114", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_66", "trp_knight_6_115", 0), 
      (call_script, "script_give_center_to_lord", "p_village_6_67", "trp_knight_6_116", 0), 



##____________________________________________________________________________starkhook____________________________________________________________________________
      (call_script, "script_give_center_to_lord", "p_castle_7_1", "trp_knight_7_2", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_7_2", "trp_knight_7_3", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_7_3", "trp_knight_7_9", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_7_4", "trp_knight_7_10", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_7_5", "trp_knight_7_11", 0), 

      (call_script, "script_give_center_to_lord", "p_village_7_1", "trp_knight_7_4", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_2", "trp_knight_7_8", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_3", "trp_knight_7_7", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_4", "trp_knight_7_6", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_6", "trp_knight_7_5", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_7", "trp_knight_7_13", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_8", "trp_knight_7_14", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_9", "trp_knight_7_15", 0), 
      (call_script, "script_give_center_to_lord", "p_village_7_10", "trp_knight_7_16", 0), 



##____________________________________________________________________________state____________________________________________________________________________
      (call_script, "script_give_center_to_lord", "p_castle_8_1", "trp_knight_8_1", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_8_2", "trp_knight_8_2", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_8_3", "trp_knight_8_3", 0), 
      (call_script, "script_give_center_to_lord", "p_castle_8_4", "trp_knight_8_9", 0), 

      (call_script, "script_give_center_to_lord", "p_village_8_1", "trp_knight_8_4", 0), 
      (call_script, "script_give_center_to_lord", "p_village_8_2", "trp_knight_8_7", 0), 
      (call_script, "script_give_center_to_lord", "p_village_8_3", "trp_knight_8_5", 0), 
      (call_script, "script_give_center_to_lord", "p_village_8_5", "trp_knight_8_6", 0), 
      (call_script, "script_give_center_to_lord", "p_village_8_6", "trp_knight_8_8", 0), 
      (call_script, "script_give_center_to_lord", "p_village_8_7", "trp_knight_8_11", 0),

#      (call_script, "script_assign_lords_to_empty_centers"),


#分配旗帜和设置声望
        (store_troop_faction, ":kingdom_hero_faction", ":kingdom_hero"),
        (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),#不是国王
        (try_begin), 
          (eq, ":kingdom_hero_faction", "fac_kingdom_3"), #Khergit Khanate
          (store_add, ":kingdom_3_banners_begin", banner_scene_props_begin, khergit_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_3_banners_begin", ":num_khergit_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_khergit_lords_assigned", 1),
        (else_try),
          (eq, ":kingdom_hero_faction", "fac_kingdom_6"), #Sarranid Sultanate
          (store_add, ":kingdom_6_banners_begin", banner_scene_props_begin, sarranid_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_6_banners_begin", ":num_sarranid_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_sarranid_lords_assigned", 1),
        (else_try),
          (assign, ":hero_offset", ":num_other_lords_assigned"),
          (try_begin),
            (gt, ":hero_offset", khergit_banners_begin_offset),#Do not add khergit banners to other lords
            (val_add, ":hero_offset", khergit_banners_end_offset),
            (val_sub, ":hero_offset", khergit_banners_begin_offset),
          (try_end),
          (try_begin),
            (gt, ":hero_offset", sarranid_banners_begin_offset),#Do not add sarranid banners to other lords
            (val_add, ":hero_offset", sarranid_banners_end_offset),
            (val_sub, ":hero_offset", sarranid_banners_begin_offset),
          (try_end),
          (store_add, ":banner_id", banner_scene_props_begin, ":hero_offset"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_other_lords_assigned", 1),
        (try_end),
        (try_begin),
          (this_or_next|lt, ":banner_id", banner_scene_props_begin),
          (gt, ":banner_id", banner_scene_props_end_minus_one),
          (display_message, "@{!}ERROR: Not enough banners for heroes!"),
        (try_end),

#领主声望
        (store_random_in_range, ":renown", 3500, 4500),#基础4000左右
        (store_character_level, ":level", ":kingdom_hero"),#等级×20
        (val_mul, ":level", 20), 
        (val_add, ":renown", ":level"),

        (troop_get_slot, ":age", ":kingdom_hero", slot_troop_age),
        (try_begin),
           (lt, ":age", 100),#非精灵
           (val_mul, ":age", 5),#年龄×5
        (else_try),
           (val_mul, ":age", 2),#年龄×2
        (try_end),
        (val_add, ":renown", ":age"),
	
        (try_begin),
           (try_for_range, ":cur_center", towns_begin, towns_end),#领主领地增加声望
             (party_slot_eq, ":cur_center", slot_town_lord, ":kingdom_hero"),#每有一个城镇提高6000
             (val_add, ":renown", 6000),
           (try_end),
           (try_for_range, ":cur_center", castles_begin, castles_end),
             (party_slot_eq, ":cur_center", slot_town_lord, ":kingdom_hero"),#每有一个城堡提高3000
             (val_add, ":renown", 3000),
           (try_end),
           (try_for_range, ":cur_center", villages_begin, villages_end),
             (party_slot_eq, ":cur_center", slot_town_lord, ":kingdom_hero"),#每有一个村庄提高1000
             (val_add, ":renown", 1000),
           (try_end),
        (try_end),
        (troop_set_slot, ":kingdom_hero", slot_troop_renown, ":renown"),				
      (try_end),

#领主、据点和国家添加到记录里
      (try_for_range, ":troop_no", "trp_player", "trp_merchants_end"),
        (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
      (try_end),
	  
      (try_for_range, ":center_no", centers_begin, centers_end),
        (add_party_note_tableau_mesh, ":center_no", "tableau_center_note_mesh"),
      (try_end),

      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh"),
      (else_try),
        (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh_banner"),
      (try_end),
	  	  
#设置据点初始文化
      (try_for_range, ":center_no", centers_begin, centers_end),
        (store_faction_of_party, ":original_faction", ":center_no"),
        (faction_get_slot, ":culture", ":original_faction", slot_faction_culture), #获取文化
        (party_set_slot, ":center_no", slot_center_culture,  ":culture"), #初始文化
        (party_set_slot, ":center_no", slot_center_original_faction,  ":original_faction"), #初始国家
        (party_set_slot, ":center_no", slot_center_ex_faction,  ":original_faction"),
      (try_end),
	  	  
#设置争议地区
	  (party_set_slot, "p_castle_4_2", slot_center_ex_faction, "fac_kingdom_2"), #yishith claim conferderation
	  (party_set_slot, "p_castle_1_10", slot_center_ex_faction, "fac_kingdom_4"), #conferderation claim powell
	  (party_set_slot, "p_castle_5_4", slot_center_ex_faction, "fac_kingdom_1"), #powell claim papal
  	  	  	  
#设置与村庄贸易的城镇（农民去城镇做生意）
      (call_script, "script_update_village_market_towns"),	  

#初始化城镇行人
      (try_for_range, ":center_no", centers_begin, centers_end),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
                     (party_slot_eq, ":center_no", slot_party_type, spt_village),
        (try_for_range, ":walker_no", 0, num_town_walkers),
          (call_script, "script_center_set_walker_to_type", ":center_no", ":walker_no", walkert_default),
        (try_end),
      (try_end),
	  	  
#初始化经济信息（必须在设置村庄与城镇的贸易关系之后）
      (call_script, "script_initialize_economic_information"),
#刷新村庄商店
      (try_for_range, ":village_no", villages_begin, villages_end),	        
        (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
      (try_end),	  

#设置领主母国	  	  	 
      (try_for_range, ":troop_id", original_kingdom_heroes_begin, active_npcs_end),
        (try_begin),
          (store_troop_faction, ":faction_id", ":troop_id"),
          (is_between, ":faction_id", kingdoms_begin, kingdoms_end),
          (troop_set_slot, ":troop_id", slot_troop_original_faction, ":faction_id"),
          (try_begin),
            (is_between, ":troop_id", pretenders_begin, pretenders_end),
            (faction_set_slot, ":faction_id", slot_faction_has_rebellion_chance, 1),			
          (try_end),
        (try_end),
        (assign, ":initial_wealth", 200000),#设置领主资产
        (try_begin),
          (store_troop_faction, ":faction", ":troop_id"),
          (faction_slot_eq, ":faction", slot_faction_leader, ":troop_id"),
          (assign, ":initial_wealth", 1000000),#国王钱更多
        (try_end),
        (troop_set_slot, ":troop_id", slot_troop_wealth, ":initial_wealth"),
      (try_end),

#刷出据点驻军
      (try_for_range, ":center_no", centers_begin, centers_end),
         (try_begin),#初始化据点资产，确定征兵轮数
            (party_slot_eq, ":center_no", slot_party_type, spt_town),#城镇翻一倍
            (assign, ":initial_wealth", 4000000),
            (assign, ":garrison_strength", 400),
         (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_castle),#城堡
            (assign, ":initial_wealth", 1000000),
            (assign, ":garrison_strength", 135),
         (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_village),#村庄
            (assign, ":initial_wealth", 200000),
            (assign, ":garrison_strength", 24),
         (try_end),
         (party_set_slot, ":center_no", slot_town_wealth, ":initial_wealth"),
         (try_for_range, ":unused", 0, ":garrison_strength"),
            (call_script, "script_cf_reinforce_party", ":center_no"),
         (try_end),

#食物补满
         (call_script, "script_center_get_food_store_limit", ":center_no"),
         (assign, ":food_store_limit", reg0),
         (party_set_slot, ":center_no", slot_party_food_store, ":food_store_limit"),
         (party_set_slot, ":center_no", slot_town_player_odds, 1000), #玩家参加竞技大会的基础赔率

#在城里刷出其领主
         (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
         (ge, ":center_lord", 1),
         (troop_slot_eq, ":center_lord", slot_troop_leaded_party, 0), #目前没带兵
             (assign, "$g_there_is_no_avaliable_centers", 0), #设置表示有城可刷
         (call_script, "script_create_kingdom_hero_party", ":center_lord", ":center_no"),
         (assign, ":lords_party", "$pout_party"),
         (party_attach_to_party, ":lords_party", ":center_no"),
      (try_end),
		
	#More pre-Warband family structures removed here

	  #Warband changes begin - set companions relations
	  (try_for_range, ":companion", companions_begin, companions_end),
		(try_for_range, ":other_companion", companions_begin, companions_end),
			(neq, ":other_companion", ":companion"),
			(neg|troop_slot_eq, ":companion", slot_troop_personalityclash_object, ":other_companion"),
			(neg|troop_slot_eq, ":companion", slot_troop_personalityclash2_object, ":other_companion"),
			(call_script, "script_troop_change_relation_with_troop", ":companion", ":other_companion", 7), #companions have a starting relation of 14, unless they are rivals
		(try_end),
	  (try_end),	
	
	  #Warband changes continue -  sets relations in the same faction
      (try_for_range, ":lord", original_kingdom_heroes_begin, active_npcs_end),
		(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
		(troop_get_slot, ":lord_faction", ":lord", slot_troop_original_faction),
				
		(try_for_range, ":other_hero", original_kingdom_heroes_begin, active_npcs_end),
			(this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
				(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_inactive_pretender),
			(troop_get_slot, ":other_hero_faction", ":other_hero", slot_troop_original_faction),
			(eq, ":other_hero_faction", ":lord_faction"),
			(call_script, "script_troop_get_family_relation_to_troop", ":lord", ":other_hero"),
			(call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", reg0),
			
			(store_random_in_range, ":random", 0, 11), #this will be scored twice between two kingdom heroes, so starting relation will average 10. Between lords and pretenders it will average 7.5
			(call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", ":random"),
		(try_end),		
	  (try_end),

	  #do about 5 years' worth of political history (assuming 3 random checks a day)
	  (try_for_range, ":unused", 0, 5000),
		(call_script, "script_cf_random_political_event"),
	  (try_end),
	  (assign, "$total_random_quarrel_changes", 0),
	  (assign, "$total_relation_adds", 0),
	  (assign, "$total_relation_subs", 0),
	  
	  (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
		(call_script, "script_evaluate_realm_stability", ":kingdom"),
	  (try_end),
	  #Warband changes end
	  
	  (try_begin),
	    (eq, "$cheat_mode", 1),
	    (assign, reg3, "$cheat_mode"),
	    (display_message, "@{!}DEBUG : Completed political events, cheat mode: {reg3}"),
	  (try_end),

	  #assign love interests to unmarried male lords
	  (try_for_range, ":cur_troop", lords_begin, lords_end),
	    (troop_slot_eq, ":cur_troop", slot_troop_spouse, -1),
		(neg|is_between, ":cur_troop", kings_begin, kings_end),
		(neg|is_between, ":cur_troop", pretenders_begin, pretenders_end),
		
		(call_script, "script_assign_troop_love_interests", ":cur_troop"),
	  (try_end),

	  (store_random_in_range, "$romantic_attraction_seed", 0, 5),
	  
	  (try_begin),
	    (eq, "$cheat_mode", 1),
	    (assign, reg3, "$romantic_attraction_seed"),
	    (display_message, "@{!}DEBUG : Assigned love interests. Attraction seed: {reg3}"),
	  (try_end),
	  
	  #we need to spawn more bandits in warband, because map is bigger.
      #(try_for_range, ":unused", 0, 7),
      #  (call_script, "script_spawn_bandits"),
      #(try_end),

      #(set_spawn_radius, 50),
      #(try_for_range, ":unused", 0, 25),
      #  (spawn_around_party, "p_main_party", "pt_looters"),
      #(try_end),
	  	  
      (try_for_range, ":unused", 0, 10),
        (call_script, "script_spawn_bandits"),
      (try_end),

      #we are adding looter parties around each village with 1/5 probability.
      (set_spawn_radius, 5),
      (try_for_range, ":cur_village", villages_begin, villages_end),
        (store_random_in_range, ":random_value", 0, 5),               
        (eq, ":random_value", 0),
        (spawn_around_party, ":cur_village", "pt_looters"),
      (try_end),

      (call_script, "script_update_mercenary_units_of_towns"),
      (call_script, "script_update_companion_candidates_in_taverns"),
      (call_script, "script_update_ransom_brokers"),
      (call_script, "script_update_auxiliary_in_taverns"),
      (call_script, "script_update_tavern_travellers"),
      (call_script, "script_update_tavern_minstrels"),
      (call_script, "script_update_booksellers"),
	  
      (try_for_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
      (try_end),
	  
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom"),
        (store_random_in_range, ":random_no", -60, 0),
        (faction_set_slot, ":faction_no", slot_faction_last_offensive_concluded, ":random_no"),
      (try_end),
	  
      (try_for_range, ":cur_troop", original_kingdom_heroes_begin, active_npcs_end),
        (call_script, "script_update_troop_notes", ":cur_troop"),
      (try_end),

      (try_for_range, ":cur_center", centers_begin, centers_end),
        (call_script, "script_update_center_notes", ":cur_center"),
      (try_end),
	  
      (call_script, "script_update_troop_notes", "trp_player"),

	  #Place kingdom ladies
      (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
		(call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
		(troop_set_slot, ":troop_id", slot_troop_cur_center, reg1),
	  (try_end),
	  
	  (try_begin),
	    (eq, "$cheat_mode", 1),
	    (assign, reg3, "$cheat_mode"),
	    (display_message, "@{!}DEBUG : Located kingdom ladies, cheat mode: {reg3}"),
	  (try_end),
	  
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (call_script, "script_faction_recalculate_strength", ":faction_no"),
      (try_end),

	  
##      (assign, "$players_kingdom", "fac_kingdom_1"),
##      (call_script, "script_give_center_to_lord", "p_town_7", "trp_player", 0),
##      (call_script, "script_give_center_to_lord", "p_town_16", "trp_player", 0),
####      (call_script, "script_give_center_to_lord", "p_castle_10", "trp_player", 0),
##      (assign, "$g_castle_requested_by_player", "p_castle_10"),
      (call_script, "script_get_player_party_morale_values"),
      (party_set_morale, "p_main_party", reg0),

      (troop_set_note_available, "trp_player", 1),

      (try_for_range, ":troop_no", kings_begin, kings_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
	  
      (try_for_range, ":troop_no", lords_begin, lords_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),

	  (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
	  (troop_set_note_available, "trp_knight_relatives_begin", 0),

      (try_for_range, ":troop_no", pretenders_begin, pretenders_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
	  
	  #Lady and companion notes become available as you meet/recruit them
	  
      (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_set_note_available, ":faction_no", 1),
      (try_end),
      (faction_set_note_available, "fac_neutral", 0),
	  
      (try_for_range, ":party_no", centers_begin, centers_end),
        (party_set_note_available, ":party_no", 1),
      (try_end),

#            (call_script, "script_initial_map_point"),
    ]),


  #script_game_get_use_string
  # This script is called from the game engine for getting using information text
  # INPUT: used_scene_prop_id  
  # OUTPUT: s0
  ("game_get_use_string",
   [
     (store_script_param, ":instance_id", 1),

     (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
     
     (try_begin),
       (this_or_next|eq, ":scene_prop_id", "spr_winch_b"),
       (eq, ":scene_prop_id", "spr_winch"),
       (assign, ":effected_object", "spr_portcullis"),
     (else_try),
       (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
       (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
       (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
       (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
       (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
       (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
       (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
       (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
       (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
       (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
       (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
       (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
       (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
       (eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
       (assign, ":effected_object", ":scene_prop_id"),
     (try_end),   

     (scene_prop_get_slot, ":item_situation", ":instance_id", scene_prop_open_or_close_slot),
   
     (try_begin), #opening/closing portcullis
       (eq, ":effected_object", "spr_portcullis"),

       (try_begin),
         (eq, ":item_situation", 0),
         (str_store_string, s0, "str_open_gate"),
       (else_try), 
         (str_store_string, s0, "str_close_gate"),
       (try_end),
     (else_try), #opening/closing door
       (this_or_next|eq, ":effected_object", "spr_door_destructible"),
       (this_or_next|eq, ":effected_object", "spr_castle_f_door_b"),
       (this_or_next|eq, ":effected_object", "spr_castle_e_sally_door_a"),
       (this_or_next|eq, ":effected_object", "spr_castle_f_sally_door_a"),
       (this_or_next|eq, ":effected_object", "spr_earth_sally_gate_left"),
       (this_or_next|eq, ":effected_object", "spr_earth_sally_gate_right"),
       (this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_left"),
       (this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_right"),
       (eq, ":effected_object", "spr_castle_f_door_a"),

       (try_begin),
         (eq, ":item_situation", 0),
         (str_store_string, s0, "str_open_door"),
       (else_try),
         (str_store_string, s0, "str_close_door"),
       (try_end),
     (else_try), #raising/dropping ladder
       (try_begin),
         (eq, ":item_situation", 0),
         (str_store_string, s0, "str_raise_ladder"),
       (else_try),
         (str_store_string, s0, "str_drop_ladder"),
       (try_end),
     (try_end),

     (try_begin),
        (eq, ":scene_prop_id", "spr_blackboard"),
        (str_store_string, s0, "@阅 读 委 托 板 "),
     (try_end),
   ]),



  #script_game_quick_start
  # This script is called from the game engine for initializing the global variables for tutorial, multiplayer and custom battle modes.
  # INPUT:
  # none
  # OUTPUT:
  # none
  ("game_quick_start",
    [
           (call_script, "script_initiallization_script_integration"),

      #for quick battle mode
      (assign, "$g_is_quick_battle", 0),
      (assign, "$g_quick_battle_game_type", 0),
      (assign, "$g_quick_battle_troop", quick_battle_troops_begin),
      (assign, "$g_quick_battle_map", quick_battle_scenes_begin),
      (assign, "$g_quick_battle_team_1_faction", "fac_kingdom_1"),
      (assign, "$g_quick_battle_team_2_faction", "fac_kingdom_2"),
      (assign, "$g_quick_battle_army_1_size", 25),
      (assign, "$g_quick_battle_army_2_size", 25),

      (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_infantry, "trp_mountain_bandit"),
      (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_infantry, "trp_abyssal_sailor"),
      (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_archer, "trp_forest_bandit"),
      (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_archer, "trp_taiga_bandit"),
      (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_cavalry, "trp_steppe_bandit"),
      (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_cavalry, "trp_desert_bandit"),
      (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_infantry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_infantry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_archer, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_archer, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_cavalry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_cavalry, "trp_powell_militia"),

      (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_infantry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_infantry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_archer, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_archer, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_cavalry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_cavalry, "trp_powell_militia"),

      (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_infantry, "trp_khergit_dismounted_lancer_multiplayer_ai"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_infantry, "trp_khergit_dismounted_lancer_multiplayer_ai"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_archer, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_archer, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_cavalry, "trp_powell_militia"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_cavalry, "trp_powell_militia"),

      (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_infantry, "trp_diemer_swordman"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_infantry, "trp_marsh_council_guard"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_archer, "trp_diemer_shortbow_archer"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_archer, "trp_diemer_heaveybow_marksman"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_cavalry, "trp_nord_scout_multiplayer_ai"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_cavalry, "trp_nord_scout_multiplayer_ai"),

      (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_infantry, "trp_papal_citizen"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_infantry, "trp_papal_citizen"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_archer, "trp_papal_citizen"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_archer, "trp_papal_citizen"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_cavalry, "trp_rhodok_scout_multiplayer_ai"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_cavalry, "trp_rhodok_scout_multiplayer_ai"),

      (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_infantry, "trp_longshu_baiganjun"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_infantry, "trp_longshu_cangtoujun"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_archer, "trp_longshu_tielinjun"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_archer, "trp_longshu_yulinjun"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_cavalry, "trp_longshu_longxiangjun"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_cavalry, "trp_longshu_shenwujun"),

      #for multiplayer mode
      (assign, "$g_multiplayer_selected_map", multiplayer_scenes_begin),
      (assign, "$g_multiplayer_respawn_period", 5),
      (assign, "$g_multiplayer_round_max_seconds", 300),
      (assign, "$g_multiplayer_game_max_minutes", 30),
      (assign, "$g_multiplayer_game_max_points", 300),

      (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
      (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
      (assign, "$g_multiplayer_point_gained_from_flags", 100),
      (assign, "$g_multiplayer_point_gained_from_capturing_flag", 5),
      (assign, "$g_multiplayer_game_type", 0),
      (assign, "$g_multiplayer_team_1_faction", "fac_kingdom_1"),
      (assign, "$g_multiplayer_team_2_faction", "fac_kingdom_2"),
      (assign, "$g_multiplayer_next_team_1_faction", "$g_multiplayer_team_1_faction"),
      (assign, "$g_multiplayer_next_team_2_faction", "$g_multiplayer_team_2_faction"),
      (assign, "$g_multiplayer_num_bots_team_1", 0),
      (assign, "$g_multiplayer_num_bots_team_2", 0),
      (assign, "$g_multiplayer_number_of_respawn_count", 0),
      (assign, "$g_multiplayer_num_bots_voteable", 50),
      (assign, "$g_multiplayer_max_num_bots", 101),
      (assign, "$g_multiplayer_factions_voteable", 1),
      (assign, "$g_multiplayer_maps_voteable", 1),
      (assign, "$g_multiplayer_kick_voteable", 1),
      (assign, "$g_multiplayer_ban_voteable", 1),
      (assign, "$g_multiplayer_valid_vote_ratio", 51), #more than 50 percent
      (assign, "$g_multiplayer_auto_team_balance_limit", 3), #auto balance when difference is more than 2
      (assign, "$g_multiplayer_player_respawn_as_bot", 1),
      (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
      (assign, "$g_multiplayer_mission_end_screen", 0),
      (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
      (assign, "$g_multiplayer_welcome_message_shown", 0),
      (assign, "$g_multiplayer_allow_player_banners", 1),
      (assign, "$g_multiplayer_force_default_armor", 1),
      (assign, "$g_multiplayer_disallow_ranged_weapons", 0),
      
      (assign, "$g_multiplayer_initial_gold_multiplier", 100),
      (assign, "$g_multiplayer_battle_earnings_multiplier", 100),
      (assign, "$g_multiplayer_round_earnings_multiplier", 100),
  
      #faction banners
      (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_c"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_d"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_e"),

      (try_for_range, ":cur_item", all_items_begin, all_items_end),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (store_sub, ":faction_index", ":cur_faction", npc_kingdoms_begin),
          (val_add, ":faction_index", slot_item_multiplayer_faction_price_multipliers_begin),
          (item_set_slot, ":cur_item", ":faction_index", 100), #100 is the default price multiplier
        (try_end),
      (try_end),
      (store_sub, ":swadian_price_slot", "fac_kingdom_1", npc_kingdoms_begin),
      (val_add, ":swadian_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":vaegir_price_slot", "fac_kingdom_2", npc_kingdoms_begin),
      (val_add, ":vaegir_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":khergit_price_slot", "fac_kingdom_3", npc_kingdoms_begin),
      (val_add, ":khergit_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":nord_price_slot", "fac_kingdom_4", npc_kingdoms_begin),
      (val_add, ":nord_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":rhodok_price_slot", "fac_kingdom_5", npc_kingdoms_begin),
      (val_add, ":rhodok_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":sarranid_price_slot", "fac_kingdom_6", npc_kingdoms_begin),
      (val_add, ":sarranid_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),

#      (item_set_slot, "itm_steppe_horse", ":khergit_price_slot", 50),

      #arrows
      (item_set_slot, "itm_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),      
      (item_set_slot, "itm_barbed_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),      
      (item_set_slot, "itm_bodkin_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_khergit_arrows", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      #bolts
      (item_set_slot, "itm_bolts", slot_item_multiplayer_item_class, multi_item_class_type_bolt),
      (item_set_slot, "itm_steel_bolts", slot_item_multiplayer_item_class, multi_item_class_type_bolt),
      #bows
      (item_set_slot, "itm_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_heavy_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_steppe_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_nomad_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_kouruto_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_strong_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_war_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_short_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_long_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_light_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),      
      #swords
      (item_set_slot, "itm_sword_medieval_a", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_medieval_b", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_medieval_b_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_medieval_c", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_medieval_c_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_scimitar", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_scimitar_b", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_dagger", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_khergit_1", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_khergit_2", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_khergit_3", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_khergit_4", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_viking_1", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_viking_2", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_viking_2_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_viking_3", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_sword_viking_3_small", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_bastard_sword_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_bastard_sword_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_sword_two_handed_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_sword_two_handed_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_arabian_sword_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_arabian_sword_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_sarranid_cavalry_sword", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_arabian_sword_d", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
	  
      #axe
      (item_set_slot, "itm_axe", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_battle_axe", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_one_handed_war_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_one_handed_war_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_one_handed_battle_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_one_handed_battle_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_one_handed_battle_axe_c", slot_item_multiplayer_item_class, multi_item_class_type_axe),
	  
      (item_set_slot, "itm_two_handed_axe", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_two_handed_battle_axe_2", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_shortened_voulge", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_great_axe", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_great_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_long_axe", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_long_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_long_axe_c", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_voulge", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_long_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_great_long_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
	  
      #blunt
      (item_set_slot, "itm_mace_1", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_mace_2", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_mace_3", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_mace_4", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_long_spiked_club", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_long_hafted_spiked_mace", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
	  
      (item_set_slot, "itm_maul", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_sledgehammer", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_warhammer", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_morningstar", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      #picks
      (item_set_slot, "itm_military_sickle_a", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_fighting_pick", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_military_pick", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_club_with_spike_head", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
	  
	  #Cleavers
      (item_set_slot, "itm_military_cleaver_b", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_military_cleaver_c", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_two_handed_cleaver", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_hafted_blade_a", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_hafted_blade_b", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_shortened_military_scythe", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
	  
      (item_set_slot, "itm_sarranid_mace_1", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_sarranid_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_sarranid_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_sarranid_two_handed_axe_a", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_sarranid_two_handed_axe_b", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_sarranid_two_handed_mace_1", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_bamboo_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
	  
	  
	  
      #spears
      (item_set_slot, "itm_double_sided_lance", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_glaive", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_poleaxe", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_polehammer", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_quarter_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_iron_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
	  
      (item_set_slot, "itm_shortened_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_war_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_military_scythe", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_pike", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_ashwood_pike", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_awlpike", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_awlpike_long", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      #lance
      (item_set_slot, "itm_light_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_heavy_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_great_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      #shields
	  
      (item_set_slot, "itm_tab_shield_round_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_round_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_round_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_round_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_round_e", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_kite_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_kite_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_kite_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_kite_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_kite_cav_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_kite_cav_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_heater_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_heater_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_heater_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_heater_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_heater_cav_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_heater_cav_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_pavise_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_pavise_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_pavise_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_pavise_d", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_small_round_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_small_round_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_tab_shield_small_round_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_spear", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      #throwing
      (item_set_slot, "itm_darts", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_war_darts", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_javelin", slot_item_multiplayer_item_class, multi_item_class_type_throwing), 
      (item_set_slot, "itm_jarid", slot_item_multiplayer_item_class, multi_item_class_type_throwing), 
      (item_set_slot, "itm_throwing_spears", slot_item_multiplayer_item_class, multi_item_class_type_throwing), 
	  
      (item_set_slot, "itm_throwing_axes", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_light_throwing_axes", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_heavy_throwing_axes", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
       #armors
      (item_set_slot, "itm_red_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_aketon_green", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_padded_cloth", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_red_gambeson", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_leather_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_haubergeon", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_coat_of_plates_red", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_brigandine_red", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_mail_with_surcoat", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_linen_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_leather_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_leather_jerkin", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_studded_leather_coat", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellar_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellar_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_coarse_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_tribal_warrior_outfit", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_khergit_guard_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_blue_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_mail_hauberk", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_mail_shirt", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_byrnie", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
	  (item_set_slot, "itm_lamellar_vest_khergit", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
	  (item_set_slot, "itm_steppe_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),

	  
      (item_set_slot, "itm_banded_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_cuir_bouilli", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
	  
      (item_set_slot, "itm_padded_leather", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_green_tunic", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunic_with_green_cape", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_aketon_green", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ragged_outfit", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_surcoat_over_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),

      (item_set_slot, "itm_sarranid_elite_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_skirmisher_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_archers_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_sarranid_leather_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_sarranid_cloth_robe", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_sarranid_mail_shirt", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_sarranid_cavalry_robe", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_arabian_armor_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_mamluke_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_khergit_elite_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_kouruto_elite_heavy_lamellar_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
	  (item_set_slot, "itm_khergit_armor", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),

	  
	  

  
      #boots
      (item_set_slot, "itm_hide_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_ankle_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_nomad_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_leather_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_splinted_leather_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_mail_chausses", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_splinted_leather_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_splinted_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_mail_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_iron_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_sarranid_boots_b", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_sarranid_boots_c", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_sarranid_boots_d", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
	  (item_set_slot, "itm_plate_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
	  (item_set_slot, "itm_khergit_leather_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
	  (item_set_slot, "itm_khergit_guard_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),

	  
	  

	  

	  
	  
      #helmets
	  
	  
      (item_set_slot, "itm_leather_steppe_cap_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_leather_steppe_cap_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_khergit_war_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_khergit_guard_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
	  
	  
	  
      (item_set_slot, "itm_arming_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_padded_coif", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_mail_coif", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_footman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_norman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_kettle_hat", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_helmet_with_neckguard", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
	  
	  (item_set_slot, "itm_bascinet_2", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
	  (item_set_slot, "itm_bascinet_3", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),


	  
      (item_set_slot, "itm_flat_topped_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_guard_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_full_helm", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_great_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nomad_cap_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_skullcap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_leather_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),

      (item_set_slot, "itm_spiked_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
#      (item_set_slot, "itm_nasal_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nordic_archer_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nordic_veteran_archer_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nordic_footman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nordic_fighter_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nordic_huscarl_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_nordic_warlord_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),

      (item_set_slot, "itm_sarranid_helmet1", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_sarranid_horseman_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_sarranid_felt_hat", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_sarranid_veiled_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_turban", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_desert_turban", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_sarranid_warrior_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_sarranid_mail_coif", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),

      (item_set_slot, "itm_vaegir_fur_cap", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_vaegir_fur_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_vaegir_spiked_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_vaegir_lamellar_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_vaegir_noble_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_vaegir_war_helmet", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_vaegir_mask", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
	  
	  
	  #gloves
      (item_set_slot, "itm_leather_gloves", slot_item_multiplayer_item_class, multi_item_class_type_glove),           
      (item_set_slot, "itm_mail_mittens", slot_item_multiplayer_item_class, multi_item_class_type_glove),           
      (item_set_slot, "itm_scale_gauntlets", slot_item_multiplayer_item_class, multi_item_class_type_glove),
	  (item_set_slot, "itm_lamellar_gauntlets", slot_item_multiplayer_item_class, multi_item_class_type_glove),	  
	  (item_set_slot, "itm_gauntlets", slot_item_multiplayer_item_class, multi_item_class_type_glove),
	  
      #horses
      (item_set_slot, "itm_saddle_horse", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_hunter", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_courser", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_hunter", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_warhorse", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_charger", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_steppe_horse", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_arabian_horse_a", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_mountain_horse", slot_item_multiplayer_item_class, multi_item_class_type_horse),
	  (item_set_slot, "itm_warhorse_steppe", slot_item_multiplayer_item_class, multi_item_class_type_horse),
	  (item_set_slot, "itm_warhorse_sarranid", slot_item_multiplayer_item_class, multi_item_class_type_horse),
	  

      #1-Swadian Warriors
      #1a-Swadian Crossbowman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steel_bolts", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_crossbow", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_crossbow", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_crossbow", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_b", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_c", "trp_swadian_crossbowman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_cloth", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_haubergeon", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_crossbowman_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_crossbowman_multiplayer"),

      #1b-Swadian Infantry
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_awlpike", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_awlpike_long", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c_small", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_b", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_two_handed_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_two_handed_b", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_b", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_c", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_d", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_tunic", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_gambeson", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_haubergeon", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_brigandine_red", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_helmet", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_swadian_infantry_multiplayer"),

      #1c-Swadian Man At Arms
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_lance", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c_small", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_b", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_b", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_c", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_d", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_tunic", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_cloth", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_with_surcoat", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_coat_of_plates_red", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plate_boots", "trp_swadian_man_at_arms_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_helmet", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_charger", "trp_swadian_man_at_arms_multiplayer"),

      # #1d-Swadian Mounted Crossbowman
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_crossbow", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_crossbow", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_crossbow", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_a", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_b", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bastard_sword_a", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_shirt", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_cloth", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_with_surcoat", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_coat_of_plates_red", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_norman_helmet", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helmet_with_neckguard", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_flat_topped_helmet", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_guard_helmet", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_swadian_mounted_crossbowman_multiplayer"),
      # (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_swadian_mounted_crossbowman_multiplayer"),

      #2-Vaegir Warriors
      #2a-Vaegir Archer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_barbed_arrows", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_2", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_bow", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kouruto_bow", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_strong_bow", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_bow", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_tunic", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_vest", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_cap", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_cap", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_helmet", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_spiked_helmet", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_lamellar_helmet", "trp_vaegir_archer_multiplayer"),
      
      #2b-Vaegir Spearman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_awlpike", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_b", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_c", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_d", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_2", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_3", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_4", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_hafted_spiked_mace", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_spiked_club", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_b", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bardiche", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_bardiche", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_bardiche", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_long_bardiche", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_tunic", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_vest", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_armor", "trp_vaegir_spearman_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kouruto_elite_heavy_lamellar_armor", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_vaegir_spearman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spiked_helmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_cap", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_helmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_spiked_helmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_lamellar_helmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_noble_helmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_war_helmet", "trp_vaegir_spearman_multiplayer"),
	  #      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nasal_helmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_vaegir_spearman_multiplayer"),

      #2c-Vaegir Horseman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bardiche", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_bardiche", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar_b", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_cav_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_cav_b", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_c", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_d", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_tunic", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_vest", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_studded_leather_coat", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_armor", "trp_vaegir_horseman_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kouruto_elite_heavy_lamellar_armor", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plate_boots", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spiked_helmet", "trp_vaegir_horseman_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nasal_helmet", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_cap", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_fur_helmet", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_spiked_helmet", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_lamellar_helmet", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_noble_helmet", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_war_helmet", "trp_vaegir_horseman_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaegir_mask", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse_steppe", "trp_vaegir_horseman_multiplayer"),
   
      #3-Khergit Warriors
      #3a-Khergit Veteran Horse Archer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_1", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_2", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_3", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_4", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_bow", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kouruto_bow", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_strong_bow", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_arrows", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_a", "trp_khergit_veteran_horse_archer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_cap_b", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_b", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_armor", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_armor", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tribal_warrior_outfit", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_vest_khergit", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_leather_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_horse", "trp_khergit_veteran_horse_archer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_khergit_veteran_horse_archer_multiplayer"),
      #3a-Khergit Lancer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_1", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_2", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_3", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_khergit_4", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_c", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hafted_blade_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hafted_blade_b", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_2", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_3", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_b", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_a", "trp_khergit_lancer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_cap_b", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_steppe_cap_b", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_war_helmet", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_guard_helmet", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_armor", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_armor", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tribal_warrior_outfit", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_armor", "trp_khergit_lancer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_elite_armor", "trp_khergit_lancer_multiplayer"),	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_boots", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_boots", "trp_khergit_lancer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_leather_boots", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_khergit_lancer_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar_gauntlets", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_horse", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse_steppe", "trp_khergit_lancer_multiplayer"),
      
      #Nord Warriors 

      #4c-Nord Archer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_barbed_arrows", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bodkin_arrows", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_1", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2_small", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3_small", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_b", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_axe", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_short_bow", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_bow", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_tunic", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_byrnie", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_boots", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_archer_helmet", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_veteran_archer_helmet", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_footman_helmet", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_fighter_helmet", "trp_nord_archer_multiplayer"),
 
      #4a-Nord Veteran      
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_nord_veteran_multiplayer"),
#      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spears", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_1", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2_small", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3_small", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_war_axe_b", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_battle_axe_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_battle_axe_b", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_one_handed_battle_axe_c", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_axe", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_battle_axe_2", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_great_axe", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_axe", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_axe_b", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_long_axe_c", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_nord_veteran_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_b", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_c", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_d", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_round_e", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_throwing_axes", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_veteran_archer_helmet", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_footman_helmet", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_fighter_helmet", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_huscarl_helmet", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_warlord_helmet", "trp_nord_veteran_multiplayer"),	  
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_tunic", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_shirt", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_hauberk", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_banded_armor", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_boots", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_nord_veteran_multiplayer"),
            
      #4b-Nord Scout
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spears", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_1", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_2", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_viking_3", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_axe", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_battle_axe_2", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortened_voulge", "trp_nord_scout_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_lance", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_c", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_archer_helmet", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_veteran_archer_helmet", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_footman_helmet", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_fighter_helmet", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nordic_huscarl_helmet", "trp_nord_scout_multiplayer"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_tunic", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_jerkin", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_shirt", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_hauberk", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_chausses", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_boots", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_nord_scout_multiplayer"),
            
      
      #5-Rhodok Warriors         
      #5a-Rhodok Veteran Crossbowman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steppe_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_steel_bolts", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_fighting_pick", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_pick", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_with_spike_head", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sledgehammer", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b_small", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_b", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_c", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_d", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_cap", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_coif", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_footman_helmet", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kettle_hat", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunic_with_green_cape", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_aketon_green", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_rhodok_veteran_crossbowman_multiplayer"),

	  #5b-Rhodok Sergeant
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_fighting_pick", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_pick", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_morningstar", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_with_spike_head", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_b", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_c", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_cleaver", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_sickle_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sledgehammer", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhammer", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pike", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ashwood_pike", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_spear", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_glaive", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_b", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_c", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_pavise_d", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_cap", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_coif", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_footman_helmet", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kettle_hat", "trp_rhodok_sergeant_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bascinet_2", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_full_helm", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_tunic", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_aketon_green", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ragged_outfit", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_surcoat_over_mail", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_iron_greaves", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_rhodok_sergeant_multiplayer"),

	  #5c-Rhodok Horseman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_darts", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_b", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword_medieval_c", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_fighting_pick", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_pick", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_morningstar", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_b", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_military_cleaver_c", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_two_handed_cleaver", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortened_military_scythe", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_lance", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_heater_cav_b", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_padded_coif", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_footman_helmet", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_kettle_hat", "trp_rhodok_horseman_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bascinet_3", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_tunic", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_aketon_green", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ragged_outfit", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_armor", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_surcoat_over_mail", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankle_boots", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_boots", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_greaves", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plate_boots", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gauntlets", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courser", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunter", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse", "trp_rhodok_horseman_multiplayer"),
	  
	  
	  
      #6-Sarranid Warriors         
      #5a-Sarranid archer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cloth_robe", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skirmisher_armor", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_archers_vest", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_armor_b", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_felt_hat", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_turban", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_desert_turban", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_coif", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_horseman_helmet", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_warrior_cap", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_b", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_c", "trp_sarranid_archer_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_short_bow", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nomad_bow", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_barbed_arrows", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scimitar", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mace_1", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_a", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_b", "trp_sarranid_archer_multiplayer"),
	  
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_sarranid_archer_multiplayer"),
     
	  
	  
	  #Sarranid footman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cloth_robe", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skirmisher_armor", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_archers_vest", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_leather_armor", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_armor_b", "trp_sarranid_footman_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_elite_armor", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_felt_hat", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_turban", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_desert_turban", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_coif", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_warrior_cap", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_veiled_helmet", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_b", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_c", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_d", "trp_sarranid_footman_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_b", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_d", "trp_sarranid_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mace_1", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_b", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_axe_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_axe_b", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_mace_1", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamboo_spear", "trp_sarranid_footman_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jarid", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_sarranid_footman_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_b", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_c", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_kite_d", "trp_sarranid_footman_multiplayer"),
	  
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_sarranid_footman_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_sarranid_footman_multiplayer"),
	  
	  
	  

	  #Sarranid mamluke
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cloth_robe", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skirmisher_armor", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_archers_vest", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_shirt", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cavalry_robe", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mamluke_mail", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_elite_armor", "trp_sarranid_mamluke_multiplayer"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_turban", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_desert_turban", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_horseman_helmet", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mail_coif", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_veiled_helmet", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_b", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_c", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_boots_d", "trp_sarranid_mamluke_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_b", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_cavalry_sword", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_sword_d", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_mace_1", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_axe_b", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sarranid_two_handed_axe_a", "trp_sarranid_mamluke_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lance", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_heavy_lance", "trp_sarranid_mamluke_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jarid", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelin", "trp_sarranid_mamluke_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_b", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tab_shield_small_round_c", "trp_sarranid_mamluke_multiplayer"),
	  
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saddle_horse", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arabian_horse_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mountain_horse", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warhorse_sarranid", "trp_sarranid_mamluke_multiplayer"),
	  
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves", "trp_sarranid_mamluke_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_mittens", "trp_sarranid_mamluke_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_gauntlets", "trp_sarranid_mamluke_multiplayer"),

      ]),


  #script_game_set_multiplayer_mission_end
  # This script is called from the game engine when a multiplayer map is ended in clients (not in server).
  # INPUT:
  # none
  # OUTPUT:
  # none
  ("game_set_multiplayer_mission_end",
    [
      (assign, "$g_multiplayer_mission_end_screen", 1),
  ]),


  #script_game_enable_cheat_menu
  # This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
  # INPUT:
  # none
  # OUTPUT:
  # none
  ("game_enable_cheat_menu",
    [
      (store_script_param, ":input", 1),
      (try_begin),
        (eq, ":input", 0),
        (assign, "$cheat_mode", 0),
      (else_try),
        (eq, ":input", 1),
        (assign, "$cheat_mode", 1),
      (try_end),
      ]),


  #script_game_get_console_command
  # This script is called from the game engine when a console command is entered from the dedicated server.
  # INPUT: anything
  # OUTPUT: s0 = result text
  ("game_get_console_command",
   [
     (store_script_param, ":input", 1),
     (store_script_param, ":val1", 2),
     (try_begin),
       #getting val2 for some commands
       (eq, ":input", 2),
       (store_script_param, ":val2", 3),
     (end_try),
     (try_begin),
       (eq, ":input", 1),
       (assign, reg0, ":val1"),
       (try_begin),
         (eq, ":val1", 1),
         (assign, reg1, "$g_multiplayer_num_bots_team_1"),
         (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
       (else_try),
         (eq, ":val1", 2),
         (assign, reg1, "$g_multiplayer_num_bots_team_2"),
         (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 2),
       (assign, reg0, ":val1"),
       (assign, reg1, ":val2"),
       (try_begin),
         (eq, ":val1", 1),
         (ge, ":val2", 0),
         (assign, "$g_multiplayer_num_bots_team_1", ":val2"),
         (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
       (else_try),
         (eq, ":val1", 2),
         (ge, ":val2", 0),
         (assign, "$g_multiplayer_num_bots_team_2", ":val2"),
         (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 3),
       (assign, reg0, "$g_multiplayer_round_max_seconds"),
       (str_store_string, s0, "str_maximum_seconds_for_round_is_reg0"),
     (else_try),
       (eq, ":input", 4),
       (assign, reg0, ":val1"),
       (try_begin),
         (is_between, ":val1", multiplayer_round_max_seconds_min, multiplayer_round_max_seconds_max),
         (assign, "$g_multiplayer_round_max_seconds", ":val1"),
         (str_store_string, s0, "str_maximum_seconds_for_round_is_reg0"),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_round_max_seconds, ":val1"),
         (try_end),            
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 5),
       (assign, reg0, "$g_multiplayer_respawn_period"),
       (str_store_string, s0, "str_respawn_period_is_reg0_seconds"),
     (else_try),
       (eq, ":input", 6),
       (assign, reg0, ":val1"),
       (try_begin),
         (is_between, ":val1", multiplayer_respawn_period_min, multiplayer_respawn_period_max),
         (assign, "$g_multiplayer_respawn_period", ":val1"),
         (str_store_string, s0, "str_respawn_period_is_reg0_seconds"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 7),
       (assign, reg0, "$g_multiplayer_num_bots_voteable"),
       (str_store_string, s0, "str_bots_upper_limit_for_votes_is_reg0"),
     (else_try),
       (eq, ":input", 8),
       (try_begin),
         (is_between, ":val1", 0, 51),
         (assign, "$g_multiplayer_num_bots_voteable", ":val1"),
         (store_add, "$g_multiplayer_max_num_bots", ":val1", 1),
         (assign, reg0, "$g_multiplayer_num_bots_voteable"),
         (str_store_string, s0, "str_bots_upper_limit_for_votes_is_reg0"),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_num_bots_voteable, ":val1"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 9),
       (try_begin),
         (eq, "$g_multiplayer_maps_voteable", 1),
         (str_store_string, s0, "str_map_is_voteable"),
       (else_try),
         (str_store_string, s0, "str_map_is_not_voteable"),
       (try_end),
     (else_try),
       (eq, ":input", 10),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_maps_voteable", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_map_is_voteable"),
         (else_try),
           (str_store_string, s0, "str_map_is_not_voteable"),
         (try_end),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_maps_voteable, ":val1"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 11),
       (try_begin),
         (eq, "$g_multiplayer_factions_voteable", 1),
         (str_store_string, s0, "str_factions_are_voteable"),
       (else_try),
         (str_store_string, s0, "str_factions_are_not_voteable"),
       (try_end),
     (else_try),
       (eq, ":input", 12),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_factions_voteable", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_factions_are_voteable"),
         (else_try),
           (str_store_string, s0, "str_factions_are_not_voteable"),
         (try_end),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_factions_voteable, ":val1"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 13),
       (try_begin),
         (eq, "$g_multiplayer_player_respawn_as_bot", 1),
         (str_store_string, s0, "str_players_respawn_as_bot"),
       (else_try),
         (str_store_string, s0, "str_players_do_not_respawn_as_bot"),
       (try_end),
     (else_try),
       (eq, ":input", 14),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_player_respawn_as_bot", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_players_respawn_as_bot"),
         (else_try),
           (str_store_string, s0, "str_players_do_not_respawn_as_bot"),
         (try_end),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_player_respawn_as_bot, ":val1"),
         (try_end),            
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 15),
       (try_begin),
         (eq, "$g_multiplayer_kick_voteable", 1),
         (str_store_string, s0, "str_kicking_a_player_is_voteable"),
       (else_try),
         (str_store_string, s0, "str_kicking_a_player_is_not_voteable"),
       (try_end),
     (else_try),
       (eq, ":input", 16),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_kick_voteable", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_kicking_a_player_is_voteable"),
         (else_try),
           (str_store_string, s0, "str_kicking_a_player_is_not_voteable"),
         (try_end),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_kick_voteable, ":val1"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 17),
       (try_begin),
         (eq, "$g_multiplayer_ban_voteable", 1),
         (str_store_string, s0, "str_banning_a_player_is_voteable"),
       (else_try),
         (str_store_string, s0, "str_banning_a_player_is_not_voteable"),
       (try_end),
     (else_try),
       (eq, ":input", 18),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_ban_voteable", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_banning_a_player_is_voteable"),
         (else_try),
           (str_store_string, s0, "str_banning_a_player_is_not_voteable"),
         (try_end),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_ban_voteable, ":val1"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 19),
       (assign, reg0, "$g_multiplayer_valid_vote_ratio"),
       (str_store_string, s0, "str_percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0"),
     (else_try),
       (eq, ":input", 20),
       (try_begin),
         (is_between, ":val1", 50, 101),
         (assign, "$g_multiplayer_valid_vote_ratio", ":val1"),
         (assign, reg0, ":val1"),
         (str_store_string, s0, "str_percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 21),
       (assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
       (str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
     (else_try),
       (eq, ":input", 22),
       (try_begin),
         (is_between, ":val1", 2, 7),
         (assign, "$g_multiplayer_auto_team_balance_limit", ":val1"),
         (assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
         (str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":val1"),
         (try_end),
       (else_try),
         (ge, ":val1", 7),
         (assign, "$g_multiplayer_auto_team_balance_limit", 1000),
         (assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
         (str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":val1"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 23),
       (assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
       (str_store_string, s0, "str_starting_gold_ratio_is_reg0"),
     (else_try),
       (eq, ":input", 24),
       (try_begin),
         (is_between, ":val1", 0, 1001),
         (assign, "$g_multiplayer_initial_gold_multiplier", ":val1"),
         (assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
         (str_store_string, s0, "str_starting_gold_ratio_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 25),
       (assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
       (str_store_string, s0, "str_combat_gold_bonus_ratio_is_reg0"),
     (else_try),
       (eq, ":input", 26),
       (try_begin),
         (is_between, ":val1", 0, 1001),
         (assign, "$g_multiplayer_battle_earnings_multiplier", ":val1"),
         (assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
         (str_store_string, s0, "str_combat_gold_bonus_ratio_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 27),
       (assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
       (str_store_string, s0, "str_round_gold_bonus_ratio_is_reg0"),
     (else_try),
       (eq, ":input", 28),
       (try_begin),
         (is_between, ":val1", 0, 1001),
         (assign, "$g_multiplayer_round_earnings_multiplier", ":val1"),
         (assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
         (str_store_string, s0, "str_round_gold_bonus_ratio_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 29),
       (try_begin),
         (eq, "$g_multiplayer_allow_player_banners", 1),
         (str_store_string, s0, "str_player_banners_are_allowed"),
       (else_try),
         (str_store_string, s0, "str_player_banners_are_not_allowed"),
       (try_end),
     (else_try),
       (eq, ":input", 30),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_allow_player_banners", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_player_banners_are_allowed"),
         (else_try),
           (str_store_string, s0, "str_player_banners_are_not_allowed"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 31),
       (try_begin),
         (eq, "$g_multiplayer_force_default_armor", 1),
         (str_store_string, s0, "str_default_armor_is_forced"),
       (else_try),
         (str_store_string, s0, "str_default_armor_is_not_forced"),
       (try_end),
     (else_try),
       (eq, ":input", 32),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_force_default_armor", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_default_armor_is_forced"),
         (else_try),
           (str_store_string, s0, "str_default_armor_is_not_forced"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 33),
       (assign, reg0, "$g_multiplayer_point_gained_from_flags"),
       (str_store_string, s0, "str_point_gained_from_flags_is_reg0"),
     (else_try),
       (eq, ":input", 34),
       (try_begin),
         (is_between, ":val1", 25, 401),
         (assign, "$g_multiplayer_point_gained_from_flags", ":val1"),
         (assign, reg0, "$g_multiplayer_point_gained_from_flags"),
         (str_store_string, s0, "str_point_gained_from_flags_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 35),
       (assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
       (str_store_string, s0, "str_point_gained_from_capturing_flag_is_reg0"),
     (else_try),
       (eq, ":input", 36),
       (try_begin),
         (is_between, ":val1", 0, 11),
         (assign, "$g_multiplayer_point_gained_from_capturing_flag", ":val1"),
         (assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
         (str_store_string, s0, "str_point_gained_from_capturing_flag_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 37),
       (assign, reg0, "$g_multiplayer_game_max_minutes"),
       (str_store_string, s0, "str_map_time_limit_is_reg0"),
     (else_try),
       (eq, ":input", 38),
       (try_begin),
         (is_between, ":val1", 5, 121),
         (assign, "$g_multiplayer_game_max_minutes", ":val1"),
         (assign, reg0, "$g_multiplayer_game_max_minutes"),
         (str_store_string, s0, "str_map_time_limit_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 39),
       (assign, reg0, "$g_multiplayer_game_max_points"),
       (str_store_string, s0, "str_team_points_limit_is_reg0"),
     (else_try),
       (eq, ":input", 40),
       (try_begin),
         (is_between, ":val1", 3, 1001),
         (assign, "$g_multiplayer_game_max_points", ":val1"),
         (assign, reg0, "$g_multiplayer_game_max_points"),
         (str_store_string, s0, "str_team_points_limit_is_reg0"),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 41),
       (assign, reg0, "$g_multiplayer_number_of_respawn_count"),
       (try_begin),
         (eq, reg0, 0),
         (str_store_string, s1, "str_unlimited"),
       (else_try),
         (str_store_string, s1, "str_reg0"),
       (try_end),
       (str_store_string, s0, "str_defender_spawn_count_limit_is_s1"),
     (else_try),
       (eq, ":input", 42),
       (try_begin),
         (is_between, ":val1", 0, 6),
         (assign, "$g_multiplayer_number_of_respawn_count", ":val1"),
         (assign, reg0, "$g_multiplayer_number_of_respawn_count"),
         (try_begin),
           (eq, reg0, 0),
           (str_store_string, s1, "str_unlimited"),
         (else_try),
           (str_store_string, s1, "str_reg0"),
         (try_end),
         (str_store_string, s0, "str_defender_spawn_count_limit_is_s1"),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 1, ":num_players"),
           (player_is_active, ":cur_player"),
           (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_count, ":val1"),
         (try_end),                  
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (eq, ":input", 43),
       (try_begin),
         (eq, "$g_multiplayer_disallow_ranged_weapons", 1),
         (str_store_string, s0, "str_ranged_weapons_are_disallowed"),
       (else_try),
         (str_store_string, s0, "str_ranged_weapons_are_allowed"),
       (try_end),
     (else_try),
       (eq, ":input", 44),
       (try_begin),
         (is_between, ":val1", 0, 2),
         (assign, "$g_multiplayer_disallow_ranged_weapons", ":val1"),
         (try_begin),
           (eq, ":val1", 1),
           (str_store_string, s0, "str_ranged_weapons_are_disallowed"),
         (else_try),
           (str_store_string, s0, "str_ranged_weapons_are_allowed"),
         (try_end),
       (else_try),
         (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
       (try_end),
     (else_try),
       (str_store_string, s0, "@{!}DEBUG : SYSTEM ERROR!"),
     (try_end),
  ]),


#大地图遭遇
  # script_game_event_party_encounter:
  # This script is called from the game engine whenever player party encounters another party or a battle on the world map
  # INPUT:
  # param1: encountered_party
  # param2: second encountered_party (if this was a battle
  ("game_event_party_encounter",
   [
       (store_script_param_1, "$g_encountered_party"),
       (store_script_param_2, "$g_encountered_party_2"),#攻城或者已经在交战了才会有
       (store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
       (store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"), #获取遭遇部队的关系
              
       (party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
       (party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),

#NPC companion changes begin
       (call_script, "script_party_count_fit_regulars", "p_main_party"),
       (assign, "$playerparty_prebattle_regulars", reg0),
#NPC companion changes end

       #enter a center in map
       (assign, "$g_last_rest_center", -1),
       (assign, "$talk_context", 0),
       (assign,"$g_player_surrenders",0),
       (assign,"$g_enemy_surrenders",0),
       (assign, "$g_leave_encounter",0),
       (assign, "$g_engaged_enemy", 0),
       (try_begin),
         (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
         (rest_for_hours, 0), #stop waiting
         (assign, "$g_infinite_camping", 0),
       (try_end),

       (assign, "$new_encounter", 1), #第一次接触，比如野战对话只会出现一次就用这个控制，用于menu
       (try_begin),                                                            #先处理特殊进入，比如剧情要求进入某城堡村时直接进入某场景
          (assign, ":continue_no", 0),
          (try_begin),
             (eq, "$current_startup_quest_phase", 5),
             (eq, "$g_encountered_party", "p_town_4"),#勒塞夫
             (party_get_slot, "$current_scene", "$g_encountered_party", slot_center_scene),#会战地图
             (check_quest_active, "qst_game_start_quest"),#开局剧情：勒塞夫街头观摩公开处刑
             (assign, ":continue_no", 1),
          (else_try),
             (this_or_next|eq, "$third_death_quest_phase", 1),
             (this_or_next|is_between, "$third_death_quest_phase", 11, 13),
             (eq, "$third_death_quest_phase", 20),
             (eq, "$g_encountered_party", "p_village_1_12"),#加尔村
             (check_quest_active, "qst_third_death"),#支线剧情：第三个死
             (assign, ":continue_no", 1),
          (try_end),
          (gt, ":continue_no", 0),
          (jump_to_menu, "mnu_plot_special_enter"),

       (else_try),
         (lt, "$g_encountered_party_2",0), #普通encounter
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town), #进入城镇
#           (jump_to_menu, "mnu_castle_outside"),
           (party_get_slot, "$current_scene", "$g_encountered_party", slot_center_scene),#会战地图
           (jump_to_menu, "mnu_center_new"),#新会战
         (else_try),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle), #进入城堡
           (jump_to_menu, "mnu_castle_outside"),
         (else_try),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship),
           (jump_to_menu, "mnu_ship_reembark"),
         (else_try),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
           (jump_to_menu, "mnu_village"),
         (else_try),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
           (jump_to_menu, "mnu_cattle_herd"),
         (else_try),
           (is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
           (jump_to_menu, "mnu_training_ground"),
		 (else_try),  
		   (party_get_template_id, ":template", "$g_encountered_party"),
		   (ge, ":template", "pt_steppe_bandit_lair"),
		   (lt, ":template", "pt_bandit_lair_templates_end"),
		   (assign, "$loot_screen_shown", 0),
		   (jump_to_menu, "mnu_bandit_lair"),
         (else_try),
           (eq, "$g_encountered_party", "p_zendar"),
           (jump_to_menu, "mnu_zendar"),
         (else_try),
           (eq, "$g_encountered_party", "p_salt_mine"),
           (jump_to_menu, "mnu_salt_mine"),

         (else_try),
           (eq, "$g_encountered_party", "p_libra_smuggle_wharf"),#权厄之秤码头，新手开局所用的场地
           (jump_to_menu, "mnu_start_game_scene"),
         (else_try),
           (eq, "$g_encountered_party", "p_fiend_nest_1"),
           (jump_to_menu, "mnu_fiend_nest_1"),
         (else_try),
           (eq, "$g_encountered_party", "p_fiend_nest_2"),
           (jump_to_menu, "mnu_fiend_nest_2"),
         (else_try),
           (eq, "$g_encountered_party", "p_fiend_nest_3"),
           (jump_to_menu, "mnu_fiend_nest_3"),
         (else_try),
           (eq, "$g_encountered_party", "p_fiend_nest_4"),
           (jump_to_menu, "mnu_fiend_nest_4"),
         (else_try),
           (eq, "$g_encountered_party", "p_east_castle"),
           (jump_to_menu, "mnu_east_castle"),

         (else_try),
           (eq, "$g_encountered_party", "p_four_ways_inn"),
           (jump_to_menu, "mnu_four_ways_inn"),
         (else_try),
           (eq, "$g_encountered_party", "p_test_scene"),
           (jump_to_menu, "mnu_test_scene"),
         (else_try),
           (eq, "$g_encountered_party", "p_battlefields"),
           (jump_to_menu, "mnu_battlefields"),
         (else_try),
           (eq, "$g_encountered_party", "p_training_ground"),
           (jump_to_menu, "mnu_tutorial"),
         (else_try),
           (eq, "$g_encountered_party", "p_camp_bandits"),           
           (jump_to_menu, "mnu_camp"),

         (else_try),
           (eq, "$g_encountered_party", "$g_plot_enemy"),#剧情敌对部队的统合
           (try_begin),
              (eq, "$current_startup_quest_phase", 13),
              (check_quest_active, "qst_game_start_quest"),#开局剧情：从码头出来后进入战斗
              (party_get_template_id, ":template_no", "$g_encountered_party"),
              (eq, ":template_no", "pt_leaded_looters"),
              (jump_to_menu, "mnu_start_quest_battle_1"),
           (try_end),
         (else_try),
#         (jump_to_menu, "mnu_simple_encounter"),#野战（进入先对话）
         (jump_to_menu, "mnu_campaign_enter"),#新会战
         (try_end),

       (else_try), #战斗或攻城
         (try_begin),
           (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),#攻城
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
           (try_begin),
             (eq, "$auto_enter_town", "$g_encountered_party"),
             (jump_to_menu, "mnu_center_new"),#新会战
           (else_try),
             (eq, "$auto_besiege_town", "$g_encountered_party"),
             (jump_to_menu, "mnu_besiegers_camp_with_allies"),
           (else_try),
             (jump_to_menu, "mnu_join_siege_outside"),
           (try_end),
         (else_try),
           (jump_to_menu, "mnu_pre_join"),
         (try_end),
       (try_end),
       (assign,"$auto_enter_town",0),
       (assign,"$auto_besiege_town",0),
      ]),


  #script_game_event_simulate_battle:
  # This script is called whenever the game simulates the battle between two parties on the map.
  # INPUT:
  # param1: Defender Party
  # param2: Attacker Party
  ("game_event_simulate_battle",
    [
      (store_script_param_1, ":root_defender_party"),
      (store_script_param_2, ":root_attacker_party"),

      (assign, "$marshall_defeated_in_battle", -1),

      (store_current_hours, ":hours"),
      
      (try_for_parties, ":party"),
        (party_get_battle_opponent, ":opponent", ":party"),
        (gt, ":opponent", 0),
        (party_set_slot, ":party", slot_party_last_in_combat, ":hours"),
      (try_end),

      (assign, ":trigger_result", 1),
      (try_begin),
        (ge, ":root_defender_party", 0),
        (ge, ":root_attacker_party", 0),
        (party_is_active, ":root_defender_party"),
        (party_is_active, ":root_attacker_party"),
        (store_faction_of_party, ":defender_faction", ":root_defender_party"),
        (store_faction_of_party, ":attacker_faction", ":root_attacker_party"),
        #(neq, ":defender_faction", "fac_player_faction"),
        #(neq, ":attacker_faction", "fac_player_faction"),		
        (store_relation, ":reln", ":defender_faction", ":attacker_faction"),
        (lt, ":reln", 0),
        (assign, ":trigger_result", 0),

        (try_begin),
          (this_or_next|eq, "$g_battle_simulation_cancel_for_party", ":root_defender_party"),
          (eq, "$g_battle_simulation_cancel_for_party", ":root_attacker_party"),
          (assign, "$g_battle_simulation_cancel_for_party", -1),
          (assign, "$auto_enter_town", "$g_battle_simulation_auto_enter_town_after_battle"),		  
          (assign, ":trigger_result", 1),
        (else_try),
          (try_begin),
            (this_or_next|party_slot_eq, ":root_defender_party", slot_party_retreat_flag, 1),
            (party_slot_eq, ":root_attacker_party", slot_party_retreat_flag, 1),
            (assign, ":trigger_result", 1), #End battle!
          (try_end),
          (party_set_slot, ":root_attacker_party", slot_party_retreat_flag, 0),		  

          #(assign, ":cancel_attack", 0),

          (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
          (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),

          #(call_script, "script_party_count_fit_for_battle", "p_collective_ally"),
          (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
          (assign, ":defender_strength", reg0),
          #(call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
          (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
          (assign, ":attacker_strength", reg0),

          (store_div, ":defender_strength", ":defender_strength", 20),
          (val_min, ":defender_strength", 50),
          (val_max, ":defender_strength", 1),
          (store_div, ":attacker_strength", ":attacker_strength", 20),
          (val_min, ":attacker_strength", 50),
          (val_add, ":attacker_strength", 1),
          (try_begin),
            #For sieges increase attacker casualties and reduce defender casualties.
            (this_or_next|party_slot_eq, ":root_defender_party", slot_party_type, spt_castle),
            (party_slot_eq, ":root_defender_party", slot_party_type, spt_town),
            (val_mul, ":defender_strength", 123), #it was 1.5 in old version, now it is only 1.23
            (val_div, ":defender_strength", 100),
      
            (val_mul, ":attacker_strength", 100), #it was 0.5 in old version, now it is only 1 / 1.23
            (val_div, ":attacker_strength", 123),
          (try_end),		  

          (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
          (assign, ":old_defender_strength", reg0),

          (try_begin),
            (neg|is_currently_night), #Don't fight at night
            (inflict_casualties_to_party_group, ":root_attacker_party", ":defender_strength", "p_temp_casualties"),
            (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),
          (try_end),
          (call_script, "script_party_count_fit_for_battle", "p_collective_enemy", 0),
          (assign, ":new_attacker_strength", reg0),

          (try_begin),
            (gt, ":new_attacker_strength", 0),
            (neg|is_currently_night), #Don't fight at night
            (inflict_casualties_to_party_group, ":root_defender_party", ":attacker_strength", "p_temp_casualties"),
            (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
          (try_end),
          (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
          (assign, ":new_defender_strength", reg0),		  

          (try_begin),
            (this_or_next|eq, ":new_attacker_strength", 0),
            (eq, ":new_defender_strength", 0),
            # Battle concluded! determine winner			
            
            (assign, ":do_not_end_battle", 0),
            (try_begin),
              (neg|troop_is_wounded, "trp_player"),
              (eq, ":new_defender_strength", 0),              
              (eq, "$auto_enter_town", "$g_encountered_party"),
              (eq, ":old_defender_strength", ":new_defender_strength"),
              (assign, ":do_not_end_battle", 1),
            (try_end),            
            (eq, ":do_not_end_battle", 0),

            (try_begin),
              (eq, ":new_attacker_strength", 0),
              (eq, ":new_defender_strength", 0),
              (assign, ":root_winner_party", -1),
              (assign, ":root_defeated_party", -1),
              (assign, ":collective_casualties", -1),
            (else_try),
              (eq, ":new_attacker_strength", 0),
              (assign, ":root_winner_party", ":root_defender_party"),
              (assign, ":root_defeated_party", ":root_attacker_party"),
              (assign, ":collective_casualties", "p_collective_enemy"),
            (else_try),
              (assign, ":root_winner_party", ":root_attacker_party"),
              (assign, ":root_defeated_party", ":root_defender_party"),
              (assign, ":collective_casualties", "p_collective_ally"),
            (try_end),

            (try_begin),
              (ge, ":root_winner_party", 0),
              (call_script, "script_get_nonempty_party_in_group", ":root_winner_party"),
              (assign, ":nonempty_winner_party", reg0),
              (store_faction_of_party, ":faction_receiving_prisoners", ":nonempty_winner_party"),
              (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),
            (else_try),
              (assign, ":nonempty_winner_party", -1),
            (try_end),

            (try_begin),                                                                                                                          #your auxiliary was defeated
              (party_slot_eq, ":root_defeated_party", slot_party_type, spt_attendant_party),              #is auxiliary
              (try_begin),
                   (eq, ":defeated_faction", "fac_player_supporters_faction"),
                   (call_script, "script_get_closest_town", ":root_attacker_party"),
                   (assign, ":location_after_defeat", reg0),
                   (val_sub, "$auxiliary_number", 1),
                   (party_get_num_companion_stacks,":num_stack",":root_defeated_party"),
                   (try_for_range,":stack_no",0,":num_stack"),
                       (party_stack_get_troop_id,":troop_npc",":root_defeated_party",":stack_no"),        #all npc in this auxiliary
                       (troop_is_hero,":troop_npc"),
                       (troop_set_slot, ":troop_npc", slot_troop_leading_auxiliary, 0),                              #clear this auxiliary
                       (troop_set_slot, ":troop_npc", slot_troop_occupation, 0),                                        #let them show in taverns
                       (troop_set_slot, ":troop_npc", slot_troop_playerparty_history, 1),
                       (try_begin),
                             (neg|troop_slot_ge, ":troop_npc", slot_troop_prisoner_of_party, centers_begin),
                             (troop_set_slot, ":troop_npc", slot_troop_cur_center, ":location_after_defeat"),
                             (str_store_party_name_link, s4, ":location_after_defeat"),
                             (str_store_troop_name_link, s5, ":troop_npc"),
                             (display_log_message, "str_auxiliary_escape"),
                       (try_end),
                   (try_end),
              (try_end),
            (try_end),

            (try_begin),
              (ge, ":collective_casualties", 0),
              (party_get_num_companion_stacks, ":num_stacks", ":collective_casualties"),
            (else_try),
              (assign, ":num_stacks", 0),
            (try_end),
                                                                         
            (try_for_range, ":troop_iterator", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":cur_troop_id", ":collective_casualties", ":troop_iterator"),
              (troop_is_hero, ":cur_troop_id"),
              
              (try_begin),
                #abort quest if troop loses a battle during rest time
                (check_quest_active, "qst_lend_surgeon"),
                (quest_slot_eq, "qst_lend_surgeon", slot_quest_giver_troop, ":cur_troop_id"),
                (call_script, "script_abort_quest", "qst_lend_surgeon", 0),
              (try_end),
              
              (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
                              
              (troop_set_slot, ":cur_troop_id", slot_troop_leaded_party, -1),
               
              (store_random_in_range, ":rand", 0, 100),
              (str_store_troop_name_link, s1, ":cur_troop_id"),
              (str_store_faction_name_link, s2, ":faction_receiving_prisoners"),
              (store_troop_faction, ":defeated_troop_faction", ":cur_troop_id"),
              (str_store_faction_name_link, s3, ":defeated_troop_faction"),

              (try_begin),
                (ge, ":rand", hero_escape_after_defeat_chance),
                (party_stack_get_troop_id, ":leader_troop_id", ":nonempty_winner_party", 0),
                (is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end), #disable non-kingdom parties capturing enemy lords
                (party_add_prisoners, ":nonempty_winner_party", ":cur_troop_id", 1),
                (gt, reg0, 0),
                #(troop_set_slot, ":cur_troop_id", slot_troop_is_prisoner, 1),
                (troop_set_slot, ":cur_troop_id", slot_troop_prisoner_of_party, ":nonempty_winner_party"),
                (display_log_message, "str_hero_taken_prisoner"),
				 
                (try_begin),
                  (call_script, "script_cf_prisoner_offered_parole", ":cur_troop_id"),

                  (try_begin),
                    (eq, "$cheat_mode", 1),
                    (display_message, "@{!}DEBUG : Prisoner granted parole"),
                  (try_end),

                  (call_script, "script_troop_change_relation_with_troop", ":leader_troop_id", ":cur_troop_id", 3),
				  (val_add, "$total_battle_enemy_changes", 3),
                (else_try),			 
                  (try_begin),
                    (eq, "$cheat_mode", 1),
                    (display_message, "@{!}DEBUG : Prisoner not offered parole"),
		          (try_end),

		          (call_script, "script_troop_change_relation_with_troop", ":leader_troop_id", ":cur_troop_id", -5),
				  (val_add, "$total_battle_enemy_changes", -5),
		        (try_end),
				 				 				 				 			
				(store_faction_of_party, ":capturer_faction", ":nonempty_winner_party"),
                (call_script, "script_update_troop_location_notes_prisoned", ":cur_troop_id", ":capturer_faction"),
              (else_try),
                (display_message,"@{s1} of {s3} was defeated in battle but managed to escape."),
              (try_end),
              
              (try_begin),
                (store_troop_faction, ":cur_troop_faction", ":cur_troop_id"),
                (is_between, ":cur_troop_faction", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, ":cur_troop_faction", slot_faction_marshall, ":cur_troop_id"),
                (is_between, ":cur_troop_faction", kingdoms_begin, kingdoms_end),
                (assign, "$marshall_defeated_in_battle", ":cur_troop_id"),
                #Marshall is defeated, refresh ai.
                (assign, "$g_recalculate_ais", 1),
              (try_end),
            (try_end),
			 
             (try_begin),
               (ge, ":collective_casualties", 0),
               (party_get_num_prisoner_stacks, ":num_stacks", ":collective_casualties"),
             (else_try),
               (assign, ":num_stacks", 0),
             (try_end),
             (try_for_range, ":troop_iterator", 0, ":num_stacks"),
               (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":collective_casualties", ":troop_iterator"),
               (troop_is_hero, ":cur_troop_id"),
               (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
               (store_troop_faction, ":cur_troop_faction", ":cur_troop_id"),
               (str_store_troop_name_link, s1, ":cur_troop_id"),
               (str_store_faction_name_link, s2, ":faction_receiving_prisoners"),
               (str_store_faction_name_link, s3, ":cur_troop_faction"),
               (display_log_message,"str_hero_freed"),
             (try_end),

             (try_begin),
               (ge, ":collective_casualties", 0),
               (party_clear, "p_temp_party"),
               (assign, "$g_move_heroes", 0), #heroes are already processed above. Skip them here.
               (call_script, "script_party_add_party_prisoners", "p_temp_party", ":collective_casualties"),
               (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", ":collective_casualties"),
               (distribute_party_among_party_group, "p_temp_party", ":root_winner_party"),
			   
               (call_script, "script_battle_political_consequences", ":root_defeated_party", ":root_winner_party"),
			
               (call_script, "script_clear_party_group", ":root_defeated_party"),
             (try_end),
             (assign, ":trigger_result", 1), #End battle!

             #Center captured
             (try_begin),
               (ge, ":collective_casualties", 0),
               (party_get_slot, ":cur_party_type", ":root_defeated_party", slot_party_type),
               (this_or_next|eq, ":cur_party_type", spt_town),                                                    #center is attacked
               (eq, ":cur_party_type", spt_castle),

               (assign, "$g_recalculate_ais", 1),

               (store_faction_of_party, ":winner_faction", ":root_winner_party"),
               (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),

               (try_begin),
                     (party_slot_eq, ":root_winner_party", slot_party_type, spt_attendant_party),       #attacker is auxiliary
                     (party_set_slot, ":root_winner_party", slot_party_orders_type, spai_holding_center),    #hold the center after fight
                     (party_set_slot, ":root_winner_party", slot_party_orders_object, ":root_defeated_party"),
                     (party_set_ai_behavior, ":root_winner_party", ai_bhvr_travel_to_party), 
                     (party_set_ai_object, ":root_winner_party", ":root_defeated_party"),
               (try_end),

               (str_store_party_name, s1, ":root_defeated_party"),
               (str_store_faction_name, s2, ":winner_faction"),
               (str_store_faction_name, s3, ":defeated_faction"),
               (display_log_message, "str_center_captured"),
			
			   (store_current_hours, ":hours"),
			   (faction_set_slot, ":winner_faction", slot_faction_ai_last_decisive_event, ":hours"),
			
               (try_begin),
                 (eq, "$g_encountered_party", ":root_defeated_party"),
                 (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
               (try_end),

               (try_begin),
                 (party_get_num_companion_stacks, ":num_stacks", ":root_winner_party"),
                 (gt, ":num_stacks", 0),
                 (party_stack_get_troop_id, ":leader_troop_no", ":root_winner_party", 0),
                 (is_between, ":leader_troop_no", active_npcs_begin, active_npcs_end),
                 (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, ":leader_troop_no"),
               (else_try),
                 (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, -1),
               (try_end),

               (call_script, "script_lift_siege", ":root_defeated_party", 0),
			   (store_faction_of_party, ":fortress_faction", ":root_defeated_party"),			   
			   (try_begin),
			     (is_between, ":root_defeated_party", towns_begin, towns_end),
			     (assign, ":damage", 40),
			   (else_try),
			     (assign, ":damage", 20),
			   (try_end),
			   (call_script, "script_faction_inflict_war_damage_on_faction", ":winner_faction", ":fortress_faction", ":damage"),
			   
               (call_script, "script_give_center_to_faction", ":root_defeated_party", ":winner_faction"),
               (try_begin),
                 (eq, ":defeated_faction", "fac_player_supporters_faction"),
                 (call_script, "script_add_notification_menu", "mnu_notification_center_lost", ":root_defeated_party", ":winner_faction"),
               (try_end),
               
               (party_get_num_attached_parties, ":num_attached_parties",  ":root_attacker_party"),
                 (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                 (party_get_attached_party_with_rank, ":attached_party", ":root_attacker_party", ":attached_party_rank"),
                                                                                                       
                 (party_get_num_companion_stacks, ":num_stacks", ":attached_party"),                 
                 (assign, ":total_size", 0),
                 (try_for_range, ":i_stack", 0, ":num_stacks"),
                   (party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
                   (val_add, ":total_size", ":stack_size"),
                 (try_end),  
                 
                 (try_begin),
                   (ge, ":total_size", 10),
                   
                   (assign, ":stacks_added", 0),
                   (assign, ":last_random_stack", -1),
                   
                   (assign, ":end_condition", 10),
                   (try_for_range, ":unused", 0, ":end_condition"),
                     (store_random_in_range, ":random_stack", 1, ":num_stacks"),
                     (party_stack_get_troop_id, ":random_stack_troop", ":attached_party", ":random_stack"),
                     (party_stack_get_size, ":stack_size", ":attached_party", ":random_stack"),
                     (ge, ":stack_size", 4),
                     (neq, ":random_stack", ":last_random_stack"),
                   
                     (store_mul, ":total_size_mul_2", ":total_size", 2),
                     (assign, ":percentage", ":total_size_mul_2"),
                     (val_min, ":percentage", 100),                   
                   
                     (val_mul, ":stack_size", ":percentage"),
                     (val_div, ":stack_size", 100),
                   
                     (party_stack_get_troop_id, ":party_leader", ":attached_party", 0),

                     (try_begin),
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_goodnatured),
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_upstanding),
                       (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_martial),
                       (assign, reg2, 0),
                       (store_random_in_range, ":random_percentage", 40, 50), #average 45%
                     (else_try),  
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_quarrelsome),
                       (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_cunning),
                       (assign, reg2, 1),
                       (store_random_in_range, ":random_percentage", 30, 40), #average 35%
                     (else_try),  
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_selfrighteous),
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_roguish),
                       (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_debauched),
                       (assign, reg2, 2),
                       (store_random_in_range, ":random_percentage", 20, 30), #average 25%
                     (else_try),  
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_benefactor),
                       (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_custodian),
                       (assign, reg2, 3),
                       (store_random_in_range, ":random_percentage", 50, 60), #average 55%
                     (try_end),                   
                   
                     (val_min, ":random_percentage", 100),                   
                     (val_mul, ":stack_size", ":random_percentage"),
                     (val_div, ":stack_size", 100),
                                                    
                     (party_add_members, ":root_defender_party", ":random_stack_troop", ":stack_size"),
                     (party_remove_members, ":attached_party", ":random_stack_troop", ":stack_size"),
                     
                     (val_add, ":stacks_added", 1),
                     (assign, ":last_random_stack", ":random_stack"),
                     
                     (try_begin),
                       #if troops from three different stack is already added then break
                       (eq, ":stacks_added", 3),
                       (assign, ":end_condition", 0),
                     (try_end),
                   (try_end),  
                 (try_end),  
               (try_end),
               
               #Reduce prosperity of the center by 5
			   (try_begin),
			     (neg|is_between, ":root_defeated_party", castles_begin, castles_end),
			     (call_script, "script_change_center_prosperity", ":root_defeated_party", -5),
			     (val_add, "$newglob_total_prosperity_from_townloot", -5),
			   (try_end),
               (call_script, "script_order_best_besieger_party_to_guard_center", ":root_defeated_party", ":winner_faction"),
               (call_script, "script_cf_reinforce_party", ":root_defeated_party"),
               (call_script, "script_cf_reinforce_party", ":root_defeated_party"),			   
             (try_end),
           (try_end),

           #ADD XP
           (try_begin),
             (party_slot_eq, ":root_attacker_party", slot_party_type, spt_kingdom_hero_party),
                          
             (assign, ":xp_gained_attacker", 200),
             (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
             (store_faction_of_party, ":root_attacker_party_faction", ":root_attacker_party"),
             (try_begin),
               (this_or_next|eq, ":root_attacker_party", "p_main_party"),
               (this_or_next|eq, ":root_attacker_party_faction", "fac_player_supporters_faction"),
               (eq, ":root_attacker_party_faction", "$players_kingdom"),               
               #same
             (else_try),
               (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
               (val_mul, ":xp_gained_attacker", 3),
               (val_div, ":xp_gained_attacker", 2),
             (else_try),
               (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
               #same
             (else_try),                        
               (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
               (val_div, ":xp_gained_attacker", 2),
             (try_end),           
             
             (gt, ":new_attacker_strength", 0),             
             (call_script, "script_upgrade_hero_party", ":root_attacker_party", ":xp_gained_attacker"),
           (try_end),
           (try_begin),
             (party_slot_eq, ":root_defender_party", slot_party_type, spt_kingdom_hero_party),
                          
             (assign, ":xp_gained_defender", 200),
             (store_faction_of_party, ":root_defender_party_faction", ":root_defender_party"),             
             (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
             (try_begin),
               (this_or_next|eq, ":root_defender_party", "p_main_party"),
               (this_or_next|eq, ":root_defender_party_faction", "fac_player_supporters_faction"),
               (eq, ":root_defender_party_faction", "$players_kingdom"),               
               #same
             (else_try),
               (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
               (val_mul, ":xp_gained_defender", 3),
               (val_div, ":xp_gained_defender", 2),
             (else_try),
               (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
               #same
             (else_try),         
               (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
               (val_div, ":xp_gained_defender", 2),
             (try_end),           

             (gt, ":new_defender_strength", 0),
             (call_script, "script_upgrade_hero_party", ":root_defender_party", ":xp_gained_defender"),
           (try_end),

           (try_begin),         
             #ozan - do not randomly end battles aganist towns or castles.
             (neg|party_slot_eq, ":root_defender_party", slot_party_type, spt_castle), #added by ozan
             (neg|party_slot_eq, ":root_defender_party", slot_party_type, spt_town),   #added by ozan        
             #end ozan
                          
             (party_get_slot, ":attacker_root_strength", ":root_attacker_party", slot_party_cached_strength),
             (party_get_slot, ":attacker_nearby_friend_strength", ":root_attacker_party", slot_party_nearby_friend_strength),
             (party_get_slot, ":strength_of_attacker_followers", ":root_attacker_party", slot_party_follower_strength),
             (store_add, ":total_attacker_strength", ":attacker_root_strength", ":attacker_nearby_friend_strength"),
             (val_add, ":total_attacker_strength", ":strength_of_attacker_followers"),

             (party_get_slot, ":defender_root_strength", ":root_defender_party", slot_party_cached_strength),
             (party_get_slot, ":defender_nearby_friend_strength", ":root_defender_party", slot_party_nearby_friend_strength),
             (party_get_slot, ":strength_of_defender_followers", ":root_defender_party", slot_party_follower_strength),
             (store_add, ":total_defender_strength", ":defender_root_strength", ":defender_nearby_friend_strength"),
             (val_add, ":total_attacker_strength", ":strength_of_defender_followers"),

             #Players can make save loads and change history because these random values are not determined from random_slots of troops
             (store_random_in_range, ":random_num", 0, 100),
                          
             (try_begin),
               (lt, ":random_num", 10),
               (assign, ":trigger_result", 1), #End battle!
             (try_end),
           (else_try),
             (party_get_slot, ":attacker_root_strength", ":root_attacker_party", slot_party_cached_strength),
             (party_get_slot, ":attacker_nearby_friend_strength", ":root_attacker_party", slot_party_nearby_friend_strength),
             (party_get_slot, ":strength_of_followers", ":root_attacker_party", slot_party_follower_strength),
             (store_add, ":total_attacker_strength", ":attacker_root_strength", ":attacker_nearby_friend_strength"),
             (val_add, ":total_attacker_strength", ":strength_of_followers"),

             (party_get_slot, ":defender_root_strength", ":root_defender_party", slot_party_cached_strength),
             (party_get_slot, ":defender_nearby_friend_strength", ":root_defender_party", slot_party_nearby_friend_strength),
             (store_add, ":total_defender_strength", ":defender_root_strength", ":defender_nearby_friend_strength"),

             (val_mul, ":total_defender_strength", 13), #multiply defender strength with 1.3
             (val_div, ":total_defender_strength", 10),

             (gt, ":total_defender_strength", ":total_attacker_strength"),
             (gt, ":total_defender_strength", 3),

             #Players can make save loads and change history because these random values are not determined from random_slots of troops
             (store_random_in_range, ":random_num", 0, 100),

             (try_begin),
               (lt, ":random_num", 15), #15% is a bit higher than 10% (which is open area escape probability)
               (assign, ":trigger_result", 1), #End battle!
                                             
               (assign, "$g_recalculate_ais", 1), #added new
                              
               (try_begin),
                 (eq, "$cheat_mode", 1),
                 (display_message, "@{!}DEBUG : Siege attackers are running away"),
               (try_end),
             (try_end),      
           (try_end),
         (try_end),  
       (try_end),
       (set_trigger_result, ":trigger_result"),
  ]),


  #script_game_event_battle_end:
  # This script is called whenever the game ends the battle between two parties on the map.
  # INPUT:
  # param1: Defender Party
  # param2: Attacker Party
  ("game_event_battle_end",
    [
##       (store_script_param_1, ":root_defender_party"),
##       (store_script_param_2, ":root_attacker_party"),
        
      #Fixing deleted heroes
      (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
		(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
        (troop_get_slot, ":cur_prisoner_of_party", ":cur_troop", slot_troop_prisoner_of_party),
        (try_begin),
          (ge, ":cur_party", 0),
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, ":cur_party"),
            (assign, ":continue", 1),
          (else_try),
            (party_count_companions_of_type, ":amount", ":cur_party", ":cur_troop"),
            (le, ":amount", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s1, ":cur_troop"),
            (display_message, "@{!}DEBUG: {s1} no longer leads a party."),
          (try_end),
         
          (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
          #(str_store_troop_name, s5, ":cur_troop"),
          #(display_message, "@{!}DEBUG : {s5}'s troop_leaded_party set to -1"),
        (try_end),
        (try_begin),
          (ge, ":cur_prisoner_of_party", 0),
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, ":cur_prisoner_of_party"),
            (assign, ":continue", 1),
          (else_try),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party", ":cur_troop"),
            (le, ":amount", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s1, ":cur_troop"),
            (display_message, "@{!}DEBUG: {s1} is no longer a prisoner."),
          (try_end),
          (call_script, "script_remove_troop_from_prison", ":cur_troop"),
          #searching player
          (try_begin),
            (party_count_prisoners_of_type, ":amount", "p_main_party", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, "p_main_party"),
            (assign, ":continue", 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of player."),                         
            (try_end),
          (try_end),
          (eq, ":continue", 1),
          #searching kingdom heroes
          (try_for_range, ":cur_troop_2", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":cur_troop_2", slot_troop_occupation, slto_kingdom_hero),
			(eq, ":continue", 1),
            (troop_get_slot, ":cur_prisoner_of_party_2", ":cur_troop_2", slot_troop_leaded_party),
            (party_is_active, ":cur_prisoner_of_party_2"),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party_2", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, ":cur_prisoner_of_party_2"),
            (assign, ":continue", 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of {s2}."),
            (try_end),
          (try_end),
          #searching walled centers
          (try_for_range, ":cur_prisoner_of_party_2", walled_centers_begin, walled_centers_end),
            (eq, ":continue", 1),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party_2", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, ":cur_prisoner_of_party_2"),
            (assign, ":continue", 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of {s2}."),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
  ]),   


  #script_order_best_besieger_party_to_guard_center:
  # INPUT:
  # param1: defeated_center, param2: winner_faction
  # OUTPUT:
  # none
  ("order_best_besieger_party_to_guard_center",
    [
      (store_script_param, ":defeated_center", 1),
      (store_script_param, ":winner_faction", 2),
      (assign, ":best_party", -1),
      (assign, ":best_party_strength", 0),
      (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
        (troop_get_slot, ":kingdom_hero_party", ":kingdom_hero", slot_troop_leaded_party),
        (gt, ":kingdom_hero_party", 0),
        (party_is_active, ":kingdom_hero_party"),
        (store_faction_of_party, ":kingdom_hero_party_faction", ":kingdom_hero_party"),
        (eq, ":winner_faction", ":kingdom_hero_party_faction"),
        (store_distance_to_party_from_party, ":dist", ":kingdom_hero_party", ":defeated_center"),
        (lt, ":dist", 5),
        #If marshall has captured the castle, then do not leave him behind.
        (neg|faction_slot_eq, ":winner_faction", slot_faction_marshall, ":kingdom_hero"),
        (assign, ":has_besiege_ai", 0),
        (try_begin),
          (party_slot_eq, ":kingdom_hero_party", slot_party_ai_state, spai_besieging_center),
          (party_slot_eq, ":kingdom_hero_party", slot_party_ai_object, ":defeated_center"),
          (assign, ":has_besiege_ai", 1),
        (else_try),
          (party_slot_eq, ":kingdom_hero_party", slot_party_ai_state, spai_accompanying_army),
          (party_get_slot, ":kingdom_hero_party_commander_party", ":kingdom_hero_party", slot_party_ai_object),
          (party_slot_eq, ":kingdom_hero_party_commander_party", slot_party_ai_state, spai_besieging_center),
          (party_slot_eq, ":kingdom_hero_party_commander_party", slot_party_ai_object, ":defeated_center"),
          (assign, ":has_besiege_ai", 1),
        (try_end),
        (eq, ":has_besiege_ai", 1),
        (party_get_slot, ":kingdom_hero_party_strength", ":kingdom_hero_party", slot_party_cached_strength),#recently calculated
        (gt, ":kingdom_hero_party_strength", ":best_party_strength"),
        (assign, ":best_party_strength", ":kingdom_hero_party_strength"),
        (assign, ":best_party", ":kingdom_hero_party"),
      (try_end),
      (try_begin),
        (gt, ":best_party", 0),
        (call_script, "script_party_set_ai_state", ":best_party", spai_holding_center, ":defeated_center"),
        #(party_set_slot, ":best_party", slot_party_commander_party, -1),
        (party_set_flags, ":best_party", pf_default_behavior, 1),
      (try_end),
      ]),


  #script_game_get_item_buy_price_factor:
  # This script is called from the game engine for calculating the buying price of any item.
  # INPUT:
  # param1: item_kind_id
  # OUTPUT:
  # trigger_result and reg0 = price_factor
  ("game_get_item_buy_price_factor",
    [
      (store_script_param_1, ":item_kind_id"),
      (assign, ":price_factor", 100),

      (call_script, "script_get_trade_penalty", ":item_kind_id"),
      (assign, ":trade_penalty", reg0),

      (try_begin),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
		
		#new
		#(try_begin),
		#	(is_between, "$g_encountered_party", villages_begin, villages_end),
		#	(party_get_slot, ":market_town", "$g_encountered_party", slot_village_market_town),
		#	(party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
		#	(val_max, ":price_factor", ":price_in_market_town"),
		#(try_end),
		
		#For villages, the good will be sold no cheaper than in the market town
		#This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers
				
        (val_mul, ":price_factor", 100), #normalize price factor to range 0..100
        (val_div, ":price_factor", average_price_factor),
      (try_end),
      
      (store_add, ":penalty_factor", 100, ":trade_penalty"),
      
      (val_mul, ":price_factor", ":penalty_factor"),
      (val_div, ":price_factor", 100),

      (assign, reg0, ":price_factor"),
      (set_trigger_result, reg0),
  ]),


  #script_game_get_item_sell_price_factor:
  # This script is called from the game engine for calculating the selling price of any item.
  # INPUT:
  # param1: item_kind_id
  # OUTPUT:
  # trigger_result and reg0 = price_factor
  ("game_get_item_sell_price_factor",
    [
      (store_script_param_1, ":item_kind_id"),
      (assign, ":price_factor", 100),

      (call_script, "script_get_trade_penalty", ":item_kind_id"),
      (assign, ":trade_penalty", reg0),

      (try_begin),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
        (val_mul, ":price_factor", 100),#normalize price factor to range 0..100
        (val_div, ":price_factor", average_price_factor),
      (else_try),
        #increase trade penalty while selling weapons, armor, and horses
        (val_mul, ":trade_penalty", 4),
      (try_end),
            
      (store_add, ":penalty_divisor", 100, ":trade_penalty"),
      
      (val_mul, ":price_factor", 100),
      (val_div, ":price_factor", ":penalty_divisor"),
      
      (assign, reg0, ":price_factor"),
      (set_trigger_result, reg0),
  ]),


  #script_game_event_buy_item:
  # This script is called from the game engine when player buys an item.
  # INPUT:
  # param1: item_kind_id
  ("game_event_buy_item",
    [
      (store_script_param_1, ":item_kind_id"),
      (store_script_param_2, ":reclaim_mode"),
      (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
        (try_begin),
          (eq, ":reclaim_mode", 0),
          (val_add, ":multiplier", 20),
        (else_try),
          (val_add, ":multiplier", 30),
        (try_end),

		(store_item_value, ":item_value", ":item_kind_id"),
		(try_begin),
		  (ge, ":item_value", 100),
		  (store_sub, ":item_value_sub_100", ":item_value", 100),
		  (store_div, ":item_value_sub_100_div_8", ":item_value_sub_100", 8),
		  (val_add, ":multiplier", ":item_value_sub_100_div_8"),
		(try_end),

        (val_min, ":multiplier", maximum_price_factor),
        
		(party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
      (try_end),
  ]),


  #script_game_event_sell_item:
  # This script is called from the game engine when player sells an item.
  # INPUT:
  # param1: item_kind_id
  ("game_event_sell_item",
    [
      (store_script_param_1, ":item_kind_id"),
      (store_script_param_2, ":return_mode"),
      (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
        (try_begin),
          (eq, ":return_mode", 0),
          (val_sub, ":multiplier", 30),
        (else_try),
          (val_sub, ":multiplier", 20),
        (try_end),

		(store_item_value, ":item_value", ":item_kind_id"),
		(try_begin),
		  (ge, ":item_value", 100),
		  (store_sub, ":item_value_sub_100", ":item_value", 100),
		  (store_div, ":item_value_sub_100_div_8", ":item_value_sub_100", 8),
		  (val_sub, ":multiplier", ":item_value_sub_100_div_8"),
		(try_end),

        (val_max, ":multiplier", minimum_price_factor),
        
		(party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
      (try_end),
  ]),


  # script_game_get_troop_wage
  # This script is called from the game engine for calculating troop wages.
  # Input:
  # param1: troop_id, param2: party-id
  # Output: reg0: weekly wage
  
  ("game_get_troop_wage",
    [
      (store_script_param_1, ":troop_id"),
      (store_script_param_2, ":unused"), #party id
      
      (assign,":wage", 0),
      (try_begin),
        (this_or_next|eq, ":troop_id", "trp_player"),
        (eq, ":troop_id", "trp_kidnapped_girl"),
      (else_try),
        (is_between, ":troop_id", pretenders_begin, pretenders_end),
      (else_try),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":wage", ":troop_level"),
        (val_add, ":wage", 3),
        (val_mul, ":wage", ":wage"),
        (val_div, ":wage", 25),
      (try_end),

      (try_begin), #mounted troops cost 65% more than the normal cost
        (neg|is_between, ":troop_id", companions_begin, companions_end),
        (troop_is_mounted, ":troop_id"),
        (val_mul, ":wage", 5),
        (val_div, ":wage", 3),
      (try_end),

      (try_begin), #mercenaries cost %50 more than the normal cost
        (is_between, ":troop_id", mercenary_troops_begin, mercenary_troops_end),
        (val_mul, ":wage", 3),
        (val_div, ":wage", 2),
      (try_end),

      (try_begin),
        (is_between, ":troop_id", companions_begin, companions_end),
        (val_mul, ":wage", 2),
      (try_end),
      
      (store_skill_level, ":leadership_level", "skl_leadership", "trp_player"),
      (store_mul, ":leadership_bonus", 5, ":leadership_level"),
      (store_sub, ":leadership_factor", 100, ":leadership_bonus"), 
      (val_mul, ":wage", ":leadership_factor"),  #wage = wage * (100 - 5*leadership)/100
      (val_div, ":wage", 100),

      (try_begin),
        (neq, ":troop_id", "trp_player"),
        (neq, ":troop_id", "trp_kidnapped_girl"),
        (neg|is_between, ":troop_id", pretenders_begin, pretenders_end),
        (val_max, ":wage", 1),
      (try_end),
       
      (assign, reg0, ":wage"),
      (set_trigger_result, reg0),
  ]),


  # script_game_get_total_wage
  # This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
  # Input: none
  # Output: reg0: weekly wage
  
  ("game_get_total_wage",
    [
      (assign, ":total_wage", 0),
      (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
        (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
        (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
        (val_mul, reg0, ":stack_size"),
        (val_add, ":total_wage", reg0),
      (try_end),
      (assign, reg0, ":total_wage"),
      (set_trigger_result, reg0),
  ]),
  

  # script_game_get_join_cost
  # This script is called from the game engine for calculating troop join cost.
  # Input:
  # param1: troop_id,
  # Output: reg0: weekly wage
  
  ("game_get_join_cost",#price for tavern mercenary
    [
      (store_script_param_1, ":troop_id"),
      
      (assign,":join_cost", 0),
      (try_begin),
        (troop_is_hero, ":troop_id"),
      (else_try),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":join_cost", ":troop_level"),
        (val_add, ":join_cost", 5),
        (val_mul, ":join_cost", ":join_cost"),
        (val_add, ":join_cost", 40),
        (val_div, ":join_cost", 5),
        (try_begin), #mounted troops cost %100 more than the normal cost
          (troop_is_mounted, ":troop_id"),
          (val_mul, ":join_cost", 2),
        (try_end),
      (try_end),
      (assign, reg0, ":join_cost"),
      (set_trigger_result, reg0),
  ]),


  # script_game_get_upgrade_xp
  # This script is called from game engine for calculating needed troop upgrade exp
  # Input:
  # param1: troop_id,
  # Output: reg0 = needed exp for upgrade 
  ("game_get_upgrade_xp",
    [
      (store_script_param_1, ":troop_id"),
      
      (assign, ":needed_upgrade_xp", 0),
      #formula : int needed_upgrade_xp = 2 * (30 + 0.006f * level_boundaries[troops[troop_id].level + 3]);
      (store_character_level, ":troop_level", ":troop_id"),
      (store_add, ":needed_upgrade_xp", ":troop_level", 3),
      (get_level_boundary, reg0, ":needed_upgrade_xp"),        
      (val_mul, reg0, 6),
      (val_div, reg0, 1000),
      (val_add, reg0, 30),

      (try_begin),               
        (ge, ":troop_id", bandits_begin),
        (lt, ":troop_id", bandits_end),
        (val_mul, reg0, 2),
      (try_end),

      (set_trigger_result, reg0),
  ]),


  # script_game_get_upgrade_cost
  # This script is called from game engine for calculating needed troop upgrade exp
  # Input:
  # param1: troop_id,
  # Output: reg0 = needed cost for upgrade
  ("game_get_upgrade_cost",
    [
      (store_script_param_1, ":troop_id"),
      
      (store_character_level, ":troop_level", ":troop_id"),
      
      (try_begin),
        (is_between, ":troop_level", 0, 6),
        (assign, reg0, 10),
      (else_try),  
        (is_between, ":troop_level", 6, 11),
        (assign, reg0, 20),
      (else_try),  
        (is_between, ":troop_level", 11, 16),
        (assign, reg0, 40),
      (else_try),  
        (is_between, ":troop_level", 16, 21),
        (assign, reg0, 80),
      (else_try),  
        (is_between, ":troop_level", 21, 26),
        (assign, reg0, 120),
      (else_try),  
        (is_between, ":troop_level", 26, 31),
        (assign, reg0, 160),
      (else_try),  
        (assign, reg0, 200),
      (try_end),  
        
      (set_trigger_result, reg0),
  ]),


  # script_game_get_prisoner_price
  # This script is called from the game engine for calculating prisoner price
  # Input:
  # param1: troop_id,
  # Output: reg0  
  ("game_get_prisoner_price",
    [
      (store_script_param_1, ":troop_id"),
            
      (try_begin),
        (is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":ransom_amount", ":troop_level"),
        (val_add, ":ransom_amount", 10), 
        (val_mul, ":ransom_amount", ":ransom_amount"),
        (val_div, ":ransom_amount", 6),
      (else_try),  
        (assign, ":ransom_amount", 50),
      (try_end),
      
      (assign, reg0, ":ransom_amount"),
      
      (set_trigger_result, reg0),
  ]),


  # script_game_check_prisoner_can_be_sold
  # This script is called from the game engine for checking if a given troop can be sold.
  # Input: 
  # param1: troop_id,
  # Output: reg0: 1= can be sold; 0= cannot be sold.
  
  ("game_check_prisoner_can_be_sold",
    [
      (store_script_param_1, ":troop_id"),
      (assign, reg0, 0),
      (try_begin),
        (neg|troop_is_hero, ":troop_id"),
        (assign, reg0, 1),
      (try_end),
      (set_trigger_result, reg0),
  ]),


  # script_game_get_morale_of_troops_from_faction
  # This script is called from the game engine 
  # Input: 
  # param1: faction_no,
  # Output: reg0: extra morale x 100
  
  ("game_get_morale_of_troops_from_faction",
    [
      (store_script_param_1, ":troop_no"),            
      
      (store_troop_faction, ":faction_no", ":troop_no"),
      
      (try_begin),
        (ge, ":faction_no", npc_kingdoms_begin),
        (lt, ":faction_no", npc_kingdoms_end),
        
        (faction_get_slot, reg0, ":faction_no",  slot_faction_morale_of_player_troops),

        #(assign, reg1, ":faction_no"),
        #(assign, reg2, ":troop_no"),
        #(assign, reg3, reg0),
        #(display_message, "@extra morale for troop {reg2} of faction {reg1} is {reg3}"),
      (else_try),
        (assign, reg0, 0),
      (try_end),
            
      (val_div, reg0, 100),
      
      (party_get_morale, reg1, "p_main_party"),
      
      (val_add, reg0, reg1),
      
      (set_trigger_result, reg0),
  ]),


  #script_game_event_detect_party:
  # This script is called from the game engine when player party inspects another party.
  # INPUT:
  # param1: Party-id
  ("game_event_detect_party",
    [
        (store_script_param_1, ":party_id"),
        (try_begin),
          (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
          (party_stack_get_troop_id, ":leader", ":party_id", 0),
          (is_between, ":leader", active_npcs_begin, active_npcs_end),
          (call_script, "script_update_troop_location_notes", ":leader", 0),
        (else_try),
          (is_between, ":party_id", walled_centers_begin, walled_centers_end),
          (party_get_num_attached_parties, ":num_attached_parties",  ":party_id"),
          (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
            (party_get_attached_party_with_rank, ":attached_party", ":party_id", ":attached_party_rank"),
            (party_stack_get_troop_id, ":leader", ":attached_party", 0),
            (is_between, ":leader", active_npcs_begin, active_npcs_end),
            (call_script, "script_update_troop_location_notes", ":leader", 0),
          (try_end),
        (try_end),
  ]),


  #script_game_event_undetect_party:
  # This script is called from the game engine when player party inspects another party.
  # INPUT:
  # param1: Party-id
  ("game_event_undetect_party",
    [
        (store_script_param_1, ":party_id"),
        (try_begin),
          (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
          (party_stack_get_troop_id, ":leader", ":party_id", 0),
          (is_between, ":leader", active_npcs_begin, active_npcs_end),
          (call_script, "script_update_troop_location_notes", ":leader", 0),
        (try_end),
  ]),


  #script_game_get_statistics_line:
  # This script is called from the game engine when statistics page is opened.
  # INPUT:
  # param1: line_no
  ("game_get_statistics_line",
    [
      (store_script_param_1, ":line_no"),
      (try_begin),
        (eq, ":line_no", 0),
        (get_player_agent_kill_count, reg1),
        (str_store_string, s1, "str_number_of_troops_killed_reg1"),
        (set_result_string, s1),
      (else_try),
        (eq, ":line_no", 1),
        (get_player_agent_kill_count, reg1, 1),
        (str_store_string, s1, "str_number_of_troops_wounded_reg1"),
        (set_result_string, s1),
      (else_try),
        (eq, ":line_no", 2),
        (get_player_agent_own_troop_kill_count, reg1),
        (str_store_string, s1, "str_number_of_own_troops_killed_reg1"),
        (set_result_string, s1),
      (else_try),
        (eq, ":line_no", 3),
        (get_player_agent_own_troop_kill_count, reg1, 1),
        (str_store_string, s1, "str_number_of_own_troops_wounded_reg1"),
        (set_result_string, s1),
      (try_end),
  ]),


  #script_game_get_date_text:
  # This script is called from the game engine when the date needs to be displayed.
  # INPUT: arg1 = number of days passed since the beginning of the game
  # OUTPUT: result string = date
  ("game_get_date_text",
    [
      (store_script_param_2, ":num_hours"),
      (store_div, ":num_days", ":num_hours", 24),
      (store_add, ":cur_day", ":num_days", 23),
      (assign, ":cur_month", 1),
      (assign, ":cur_year", 1413),
      (assign, ":try_range", 99999),
      (try_for_range, ":unused", 0, ":try_range"),
        (try_begin),
          (this_or_next|eq, ":cur_month", 1),
          (this_or_next|eq, ":cur_month", 3),
          (this_or_next|eq, ":cur_month", 5),
          (this_or_next|eq, ":cur_month", 7),
          (this_or_next|eq, ":cur_month", 8),
          (this_or_next|eq, ":cur_month", 10),
          (eq, ":cur_month", 12),
          (assign, ":month_day_limit", 31),
        (else_try),
          (this_or_next|eq, ":cur_month", 4),
          (this_or_next|eq, ":cur_month", 6),
          (this_or_next|eq, ":cur_month", 9),
          (eq, ":cur_month", 11),
          (assign, ":month_day_limit", 30),
        (else_try),
          (try_begin),
            (store_div, ":cur_year_div_4", ":cur_year", 4),
            (val_mul, ":cur_year_div_4", 4),
            (eq, ":cur_year_div_4", ":cur_year"),
            (assign, ":month_day_limit", 29),
          (else_try),
            (assign, ":month_day_limit", 28),      
          (try_end),
        (try_end),
        (try_begin),
          (gt, ":cur_day", ":month_day_limit"),
          (val_sub, ":cur_day", ":month_day_limit"),
          (val_add, ":cur_month", 1),
          (try_begin),
            (gt, ":cur_month", 12),
            (val_sub, ":cur_month", 12),
            (val_add, ":cur_year", 1),
          (try_end),
        (else_try),
          (assign, ":try_range", 0),
        (try_end),
      (try_end),
      (assign, reg1, ":cur_day"),
      (assign, reg2, ":cur_year"),
      (try_begin),
        (eq, ":cur_month", 1),
        (str_store_string, s1, "str_january_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 2),
        (str_store_string, s1, "str_february_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 3),
        (str_store_string, s1, "str_march_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 4),
        (str_store_string, s1, "str_april_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 5),
        (str_store_string, s1, "str_may_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 6),
        (str_store_string, s1, "str_june_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 7),
        (str_store_string, s1, "str_july_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 8),
        (str_store_string, s1, "str_august_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 9),
        (str_store_string, s1, "str_september_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 10),
        (str_store_string, s1, "str_october_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 11),
        (str_store_string, s1, "str_november_reg1_reg2"),
      (else_try),
        (eq, ":cur_month", 12),
        (str_store_string, s1, "str_december_reg1_reg2"),
      (try_end),
      (set_result_string, s1),
    ]),  


  #script_game_get_money_text:
  # This script is called from the game engine when an amount of money needs to be displayed.
  # INPUT: arg1 = amount in units
  # OUTPUT: result string = money in text
  ("game_get_money_text",
    [
      (store_script_param_1, ":amount"),
      (try_begin),
        (eq, ":amount", 1),
        (str_store_string, s1, "str_1_denar"),
      (else_try),
        (assign, reg1, ":amount"),
        (str_store_string, s1, "str_reg1_denars"),
      (try_end),
      (set_result_string, s1),
  ]),


  #script_game_get_party_companion_limit:
  # This script is called from the game engine when the companion limit is needed for a party.
  # INPUT: arg1 = none
  # OUTPUT: reg0 = companion_limit
  ("game_get_party_companion_limit",
    [
      (assign, ":troop_no", "trp_player"),

      (assign, ":limit", 60),
      (store_skill_level, ":skill", "skl_leadership", ":troop_no"),
      (store_attribute_level, ":charisma", ":troop_no", ca_charisma),
      (val_mul, ":skill", 20),
      (val_add, ":limit", ":skill"),
      (val_mul, ":charisma", 5),
      (val_add, ":limit", ":charisma"),

      (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
      (store_div, ":renown_bonus", ":troop_renown", 15),
      (val_add, ":limit", ":renown_bonus"),

      (assign, reg0, ":limit"),
      (set_trigger_result, reg0),
  ]),


  #script_game_reset_player_party_name:
  # This script is called from the game engine when the player name is changed.
  # INPUT: none
  # OUTPUT: none
  ("game_reset_player_party_name",
    [(str_store_troop_name, s5, "trp_player"),
     (party_set_name, "p_main_party", s5),
     ]),


  #script_game_get_troop_note
  # This script is called from the game engine when the notes of a troop is needed.
  # INPUT: arg1 = troop_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_troop_note",
    [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0),

      (str_store_troop_name, s54, ":troop_no"),
      (try_begin),
        (eq, ":troop_no", "trp_player"),
        (this_or_next|eq, "$player_has_homage", 1),
        (eq, "$players_kingdom", "fac_player_supporters_faction"),
        (assign, ":troop_faction", "$players_kingdom"),
      (else_try),
        (store_troop_faction, ":troop_faction", ":troop_no"),
		

		
      (try_end),
      (str_clear, s49),
	  
	  #Family notes
      (try_begin),
        (this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),
        (eq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
        (assign, ":num_relations", 0),

        (try_begin),
          (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
          (gt, reg0, 0),
          (val_add, ":num_relations", 1),
        (try_end),
        (try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
          (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
          (gt, reg0, 0),
          (val_add, ":num_relations", 1),
        (try_end),
        (try_begin),
          (gt, ":num_relations", 0),
          (try_begin),
            (eq, ":troop_no", "trp_player"),
            (str_store_string, s49, "str__family_"),
          (else_try),
            (troop_get_slot, reg1, ":troop_no", slot_troop_age),
            (str_store_string, s49, "str__age_reg1_family_"),
          (try_end),
          (try_begin),
            (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
            (gt, reg0, 0),
            (str_store_troop_name_link, s12, "trp_player"),
            (val_sub, ":num_relations", 1),
            (try_begin),
              (eq, ":num_relations", 0),
              (str_store_string, s49, "str_s49_s12_s11_end"),
            (else_try),
              (str_store_string, s49, "str_s49_s12_s11"),
            (try_end),
          (try_end),
          (try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
            (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
            (gt, reg0, 0),
            (try_begin),
              (neg|is_between, ":aristocrat", kingdom_ladies_begin, kingdom_ladies_end),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name_link, s12, ":aristocrat"),
              (call_script, "script_troop_get_relation_with_troop", ":aristocrat", ":troop_no"),
              (str_store_string, s49, "str_s49_s12_s11_rel_reg0"),
            (else_try),
              (str_store_troop_name_link, s12, ":aristocrat"),
              (val_sub, ":num_relations", 1),
              (try_begin),
                (eq, ":num_relations", 0),
                (str_store_string, s49, "str_s49_s12_s11_end"),
              (else_try),
                (str_store_string, s49, "str_s49_s12_s11"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
      
      (try_begin),
        (neq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
        (neg|is_between, ":troop_no", companions_begin, companions_end),
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),

        (try_begin),
          (eq, ":note_index", 0),
          (str_store_string, s0, "str_s54_has_left_the_realm"),
          (set_trigger_result, 1),
        (else_try),
          (str_clear, s0),
          (this_or_next|eq, ":note_index", 1),
          (eq, ":note_index", 2),
          (set_trigger_result, 1),
        (try_end),

      (else_try),
        (is_between, ":troop_no", companions_begin, companions_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (eq, ":note_index", 0),
        (set_trigger_result, 1),
        (str_clear, s0),
        (assign, ":companion", ":troop_no"),
        (str_store_troop_name, s4, ":companion"),
        (try_begin),
			(troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),

			(this_or_next|main_party_has_troop, ":companion"),
			(this_or_next|troop_slot_ge, ":companion", slot_troop_current_mission, 1),
				(eq, "$g_player_minister", ":companion"),

			(try_begin),
				(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
				(str_store_string, s8, "str_gathering_support"),
				(try_begin),
					(eq, ":days_left", 1),
					(str_store_string, s5, "str_expected_back_imminently"),
				(else_try),	
					(assign, reg3, ":days_left"),
					(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
				(try_end),
			(else_try),
				(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
				(troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
				(str_store_party_name, s11, ":town_with_contacts"),
				
				(str_store_string, s8, "str_gathering_intelligence"),
				(try_begin),
					(eq, ":days_left", 1),
					(str_store_string, s5, "str_expected_back_imminently"),
				(else_try),	
					(assign, reg3, ":days_left"),
					(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
				(try_end),
			(else_try),	
				
				(troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
				(neg|troop_slot_ge, ":companion", slot_troop_current_mission, 8),

				(troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
				(str_store_faction_name, s9, ":faction"),
				(str_store_string, s8, "str_diplomatic_embassy_to_s9"),
				(try_begin),
					(eq, ":days_left", 1),
					(str_store_string, s5, "str_expected_back_imminently"),
				(else_try),	
					(assign, reg3, ":days_left"),
					(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
				(try_end),
			(else_try),
				(eq, ":companion", "$g_player_minister"),
				(str_store_string, s8, "str_serving_as_minister"),
				(str_store_party_name, s9, "$g_player_court"),
				(is_between, "$g_player_court", centers_begin, centers_end),
				(str_store_string, s5, "str_in_your_court_at_s9"),
			(else_try),
				(eq, ":companion", "$g_player_minister"),
				(str_store_string, s8, "str_serving_as_minister"),
				(str_store_string, s5, "str_awaiting_the_capture_of_a_fortress_which_can_serve_as_your_court"),
			(else_try),
				(main_party_has_troop, ":companion"),
				(str_store_string, s8, "str_under_arms"),
				(str_store_string, s5, "str_in_your_party"),
			(try_end),	
			
			(str_store_string, s0, "str_s4_s8_s5"),
		(else_try),
                                                (call_script, "script_troop_in_which_party", ":companion"),#get npc auxiliary location
                                                (assign, ":party_no", reg0),
                                                (party_get_slot,":party_type",":party_no",slot_party_type),
                                                (eq, ":party_type", spt_attendant_party),
                                                (str_store_party_name,s8,":party_no"),

                                                (try_begin),
                                                     (party_is_in_any_town,":party_no"),#in town
                                                     (str_store_string, s5, "@In"),
                                                     (party_get_cur_town, ":center_no", ":party_no"),
                                                     (str_store_party_name_link, s4, ":center_no"),
                                                (else_try),
                                                     (str_store_string, s5, "@Around"),
                                                     (call_script, "script_get_closest_center", ":party_no"),
                                                     (str_store_party_name_link, s4, reg0),
                                                (try_end),

                                                (party_get_slot, ":temp_order", ":party_no", slot_party_orders_type),
                                                (party_get_slot,  ":target_no", ":party_no", slot_party_orders_object),
                                                (try_begin),
                                                      (eq, ":temp_order", spai_undefined),#stay here
                                                      (str_store_string, s7, "@stay here"),
                                                (else_try),
                                                      (eq, ":temp_order", spai_accompanying_army),#guard a party
                                                      (str_store_party_name, s6, ":target_no"),
                                                      (str_store_string, s7, "@guard {s6} party"),
                                                (else_try),
                                                      (eq, ":temp_order", spai_patrolling_around_center),#patrol around a party
                                                      (neg|is_between, ":target_no", centers_begin, centers_end),
                                                      (str_store_party_name, s6, ":target_no"),
                                                      (str_store_string, s7, "@patrol around {s6} party"),
                                                (else_try),
                                                      (eq, ":temp_order", spai_patrolling_around_center),#patrol around a center
                                                      (str_store_party_name_link, s6, ":target_no"),
                                                      (str_store_string, s7, "@patrol around {s6} party"),
                                                (else_try),
                                                      (eq, ":temp_order", spai_retreating_to_center),#hide in a town
                                                      (str_store_party_name_link, s6, ":target_no"),
                                                      (str_store_string, s7, "@hide in {s6} town"),
                                                (else_try),
                                                      (eq, ":temp_order", spai_holding_center),#join a town's garrison
                                                      (str_store_party_name_link, s6, ":target_no"),
                                                      (str_store_string, s7, "@join {s6} town's garrison"),
                                                (else_try),
                                                      (eq, ":temp_order", spai_besieging_center),#attack a party
                                                      (str_store_party_name_link, s6, ":target_no"),
                                                      (str_store_string, s7, "@attack {s6} party"),
                                                (try_end),
			(str_store_string, s0, "str_in_auxiliary"),		
		(else_try),
			(str_store_string, s0, "str_whereabouts_unknown"),
		(try_end),
		
	  
	  (else_try),
        (is_between, ":troop_no", pretenders_begin, pretenders_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, ":troop_no", "$supported_pretender"),

		
        (troop_get_slot, ":orig_faction", ":troop_no", slot_troop_original_faction),
        (try_begin),
          (faction_slot_eq, ":orig_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":orig_faction", slot_faction_has_rebellion_chance, 1),
          (try_begin),
            (eq, ":note_index", 0),
            (str_store_faction_name_link, s56, ":orig_faction"),
            (str_store_string, s0, "@{s54} is a claimant to the throne of {s56}.", 0),
            (set_trigger_result, 1),
          (try_end),
        (else_try),
          (try_begin),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
            (set_trigger_result, 1),
          (try_end),
        (try_end),
		
      (else_try),
        (try_begin),
          (eq, ":note_index", 0),
          (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
          (str_store_troop_name_link, s55, ":faction_leader"),
          (str_store_faction_name_link, s56, ":troop_faction"),
          (assign, ":troop_is_player_faction", 0),
          (assign, ":troop_is_faction_leader", 0),
          (try_begin),
            (eq, ":troop_faction", "fac_player_faction"),
            (assign, ":troop_is_player_faction", 1),
          (else_try),
            (eq, ":faction_leader", ":troop_no"),
            (assign, ":troop_is_faction_leader", 1),
          (try_end),
          (assign, ":num_centers", 0),
          (str_store_string, s58, "@nowhere"),
          (try_for_range_backwards, ":cur_center", centers_begin, centers_end),                     
            (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
            (try_begin),
              (eq, ":num_centers", 0),
              (str_store_party_name_link, s58, ":cur_center"),
            (else_try),
              (eq, ":num_centers", 1),
              (str_store_party_name_link, s57, ":cur_center"),
              (str_store_string, s58, "@{s57} and {s58}"),
            (else_try),
              (str_store_party_name_link, s57, ":cur_center"),
              (str_store_string, s58, "@{!}{s57}, {s58}"),
            (try_end),
            (val_add, ":num_centers", 1),
          (try_end),
          (troop_get_type, reg3, ":troop_no"),
          (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
          (troop_get_slot, reg15, ":troop_no", slot_troop_controversy),
		  
          (str_clear, s59),
          (try_begin),   
            (call_script, "script_troop_get_player_relation", ":troop_no"),
            (assign, ":relation", reg0),
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            (store_add, ":str_id", "str_relation_mnus_100_ns",  ":str_offset"),
            (neq, ":str_id", "str_relation_plus_0_ns"),
            (str_store_string, s60, "@{reg3?She:He}"),
            (str_store_string, s59, ":str_id"),
            (str_store_string, s59, "@{!}^{s59}"),
          (try_end),
          #lord recruitment changes begin
          #This sends a bunch of political information to s47.
    
          #refresh registers
          (assign, reg9, ":num_centers"),
          (troop_get_type, reg3, ":troop_no"),
          (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
          (assign, reg4, ":troop_is_faction_leader"),
          (assign, reg6, ":troop_is_player_faction"),
          
          (troop_get_slot, reg17, ":troop_no", slot_troop_wealth), #DEBUGS
          (str_store_string, s0, "str_lord_info_string", 0),
          #lord recruitment changes end
          (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
          (set_trigger_result, 1),
        (try_end),
      (try_end),
     ]),


  #script_game_get_center_note
  # This script is called from the game engine when the notes of a center is needed.
  # INPUT: arg1 = center_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_center_note",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":note_index"),

      (set_trigger_result, 0),
      (try_begin),
        (eq, ":note_index", 0),
        (party_get_slot, ":lord_troop", ":center_no", slot_town_lord),
        (try_begin),
          (ge, ":lord_troop", 0),
          (store_troop_faction, ":lord_faction", ":lord_troop"),
          (str_store_troop_name_link, s1, ":lord_troop"),
          (try_begin),
            (eq, ":lord_troop", "trp_player"),
            (gt, "$players_kingdom", 0),
            (str_store_faction_name_link, s2, "$players_kingdom"),
          (else_try),
            (str_store_faction_name_link, s2, ":lord_faction"),
          (try_end),
          (str_store_party_name, s50, ":center_no"),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (str_store_string, s51, "@The town of {s50}"),
          (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_village),
            (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
            (str_store_party_name_link, s52, ":bound_center"),
            (str_store_string, s51, "@The village of {s50} near {s52}"),
          (else_try),
            (str_store_string, s51, "@{!}{s50}"),
          (try_end),
          (str_store_string, s2, "@{s51} belongs to {s1} of {s2}.^"),
        (else_try),
          (str_clear, s2),
        (try_end),
        (try_begin),
          (is_between, ":center_no", villages_begin, villages_end),
        (else_try),
          (assign, ":num_villages", 0),
          (try_for_range_backwards, ":village_no", villages_begin, villages_end),
            (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
            (try_begin),
              (eq, ":num_villages", 0),
              (str_store_party_name_link, s8, ":village_no"),
            (else_try),
              (eq, ":num_villages", 1),
              (str_store_party_name_link, s7, ":village_no"),
              (str_store_string, s8, "@{s7} and {s8}"),
            (else_try),
              (str_store_party_name_link, s7, ":village_no"),
              (str_store_string, s8, "@{!}{s7}, {s8}"),
            (try_end),
            (val_add, ":num_villages", 1),
          (try_end),
          (try_begin),
            (eq, ":num_villages", 0),
            (str_store_string, s2, "@{s2}It has no villages.^"),
          (else_try),
            (store_sub, reg0, ":num_villages", 1),
            (str_store_string, s2, "@{s2}{reg0?Its villages are:Its village is} {s8}.^"),
          (try_end),
        (try_end),
        (call_script, "script_get_prosperity_text_to_s50", ":center_no"),
        #(party_get_slot, reg7, ":center_no", slot_town_prosperity),
        (str_store_string, s0, "@{s2}Its prosperity is: {s50}", 0),
      
        (set_trigger_result, 1),
      (try_end),
     ]),


  #script_game_get_faction_note
  # This script is called from the game engine when the notes of a faction is needed.
  # INPUT: arg1 = faction_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_faction_note",
    [
      (store_script_param_1, ":faction_no"),
      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0),
      
##      (try_begin),
##        (eq, 2, 1),
##        (str_store_faction_name, s14, ":faction_no"),
##        (assign, reg4, "$temp"),
##        (display_message, "str_updating_faction_notes_for_s14_temp_=_reg4"),
##      (try_end),

      (try_begin),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        #conditions end
        (try_begin),
            (eq, ":note_index", 0),
          (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
          (str_store_faction_name, s5, ":faction_no"),
          (str_store_troop_name_link, s6, ":faction_leader"),
          (assign, ":num_centers", 0),
          (str_store_string, s8, "@nowhere"),
          (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
            (store_faction_of_party, ":center_faction", ":cur_center"),
            (eq, ":center_faction", ":faction_no"),
            (try_begin),
              (eq, ":num_centers", 0),
              (str_store_party_name_link, s8, ":cur_center"),
            (else_try),
              (eq, ":num_centers", 1),
              (str_store_party_name_link, s7, ":cur_center"),
              (str_store_string, s8, "@{s7} and {s8}"),
            (else_try),
              (str_store_party_name_link, s7, ":cur_center"),
              (str_store_string, s8, "@{!}{s7}, {s8}"),
            (try_end),
            (val_add, ":num_centers", 1),
          (try_end),
          (assign, ":num_members", 0),
          (str_store_string, s10, "@noone"),
          (try_for_range_backwards, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
            (assign, ":cur_troop", ":loop_var"),
            (try_begin),
              (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
              (assign, ":cur_troop", "trp_player"),
              (assign, ":troop_faction", "$players_kingdom"),
            (else_try),
              (store_troop_faction, ":troop_faction", ":cur_troop"),
            (try_end),
            (eq, ":troop_faction", ":faction_no"),
            (neq, ":cur_troop", ":faction_leader"),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (try_begin),
              (eq, ":num_members", 0),
              (str_store_troop_name_link, s10, ":cur_troop"),
            (else_try),
              (eq, ":num_members", 1),
              (str_store_troop_name_link, s9, ":cur_troop"),
              (str_store_string, s10, "@{s9} and {s10}"),
            (else_try),
              (str_store_troop_name_link, s9, ":cur_troop"),
              (str_store_string, s10, "@{!}{s9}, {s10}"),
            (try_end),
            (val_add, ":num_members", 1),
          (try_end),
              
              #wars
          (str_store_string, s12, "@noone"),
   #       (assign, ":num_enemies", 0),
   #       (try_for_range_backwards, ":cur_faction", kingdoms_begin, kingdoms_end),
   #         (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
   #         (store_relation, ":cur_relation", ":cur_faction", ":faction_no"),
   #         (lt, ":cur_relation", 0),
   #         (try_begin),
   #           (eq, ":num_enemies", 0),
   #           (str_store_faction_name_link, s12, ":cur_faction"),
   #         (else_try),
   #           (eq, ":num_enemies", 1),
   #           (str_store_faction_name_link, s11, ":cur_faction"),
   #           (str_store_string, s12, "@the {s11} and the {s12}"),
   #         (else_try),
   #           (str_store_faction_name_link, s11, ":cur_faction"),
   #           (str_store_string, s12, "@the {s11}, the {s12}"),
   #         (try_end),
   #         (val_add, ":num_enemies", 1),
   #       (try_end),
              
          (str_store_string, s21, "str_foreign_relations__"),
              
              #other foreign relations
          (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (neq, ":faction_no", ":cur_faction"),
            (str_store_faction_name_link, s14, ":cur_faction"),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction_no", ":cur_faction"),
            (assign, ":diplomatic_status", reg0),
			(assign, ":duration_of_status", reg1),
			
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_faction", ":faction_no"),
            (assign, ":reverse_diplomatic_status", reg0),
#			(assign, ":reverse_diplomatic_duration", reg1),

            (try_begin),
              (eq, ":diplomatic_status", -2),
              (str_store_string, s21, "str_s21__the_s5_is_at_war_with_the_s14"),
              (store_add, ":slot_war_damage_inflicted", ":cur_faction", slot_faction_war_damage_inflicted_on_factions_begin),
              (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
              (faction_get_slot, ":war_damage_inflicted", ":faction_no", ":slot_war_damage_inflicted"),
              (store_mul, ":war_damage_inflicted_x_2", ":war_damage_inflicted", 2),

              (store_add, ":slot_war_damage_suffered", ":faction_no", slot_faction_war_damage_inflicted_on_factions_begin),
              (val_sub, ":slot_war_damage_suffered", kingdoms_begin),
              (faction_get_slot, ":war_damage_suffered", ":cur_faction", ":slot_war_damage_suffered"),
              (store_mul, ":war_damage_suffered_x_2", ":war_damage_suffered", 2),
			  
			  
			  (assign, ":war_cause", 0),
			  (assign, ":attacker", 0),
			  (try_for_range, ":log_entry", 0, "$num_log_entries"),
				(troop_get_slot, ":type", "trp_log_array_entry_type", ":log_entry"),
				(is_between, ":type", logent_faction_declares_war_out_of_personal_enmity, logent_war_declaration_types_end),
				(troop_get_slot, ":actor", "trp_log_array_actor", ":log_entry"),
				(troop_get_slot, ":object", "trp_log_array_faction_object", ":log_entry"),

				(try_begin),
					(eq, ":actor", ":cur_faction"),
					(eq, ":object", ":faction_no"),
					(assign, ":war_cause", ":type"),
					(assign, ":attacker", ":actor"),
				(else_try),	
					(eq, ":actor", ":faction_no"),
					(eq, ":object", ":cur_faction"),
					(assign, ":war_cause", ":type"),
					(assign, ":attacker", ":actor"),
				(try_end),
			  (try_end),	

			  #bug fix! backing up s8 to somewhere else
                          (str_store_string, s25, s8),
			  (try_begin),
			    (gt, ":war_cause", 0),
				(str_store_faction_name, s8, ":attacker"),
				(try_begin),
					(eq, ":war_cause", logent_faction_declares_war_out_of_personal_enmity),
					(str_store_string, s21, "str_s21_the_s8_declared_war_out_of_personal_enmity"),
				(else_try),			
					(eq, ":war_cause", logent_faction_declares_war_to_respond_to_provocation),
					(str_store_string, s21, "str_s21_the_s8_declared_war_in_response_to_border_provocations"),
				(else_try),			
					(eq, ":war_cause", logent_faction_declares_war_to_curb_power),
					(str_store_string, s21, "str_s21_the_s8_declared_war_to_curb_the_other_realms_power"),
				(else_try),	
					(eq, ":war_cause", logent_faction_declares_war_to_regain_territory),
					(str_store_string, s21, "str_s21_the_s8_declared_war_to_regain_lost_territory"),
				(else_try),
					(eq, ":war_cause", logent_player_faction_declares_war),
					(neq, ":attacker", "fac_player_supporters_faction"),
					(str_store_string, s21, "str_s21_the_s8_declared_war_as_part_of_a_bid_to_conquer_all_calradia"),
				(try_end),
			  (try_end),
			  #bug fix! restoring the back up to s8
                          (str_store_string, s8, s25),

              (try_begin),
                (gt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
                (str_store_string, s21, "str_s21_the_s5_has_had_the_upper_hand_in_the_fighting"),
              (else_try),
                (gt, ":war_damage_suffered", ":war_damage_inflicted_x_2"),
                (str_store_string, s21, "str_s21_the_s5_has_gotten_the_worst_of_the_fighting"),
              (else_try),
                (gt, ":war_damage_inflicted", 100),
                (gt, ":war_damage_inflicted", 100),
                (str_store_string, s21, "str_s21_the_fighting_has_gone_on_for_some_time_and_the_war_may_end_soon_with_a_truce"),
              (else_try),
                (str_store_string, s21, "str_s21_the_fighting_has_begun_relatively_recently_and_the_war_may_continue_for_some_time"),
              (try_end),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (assign, reg4, ":war_damage_inflicted"),
                (assign, reg5, ":war_damage_suffered"),
                (str_store_string, s21, "str_s21_reg4reg5"),
              (try_end),
            (else_try),
              (eq, ":diplomatic_status", 1),
              (str_clear, s18),
              (try_begin),
                (neq, ":reverse_diplomatic_status", 1),
                (str_store_string, s18, "str__however_the_truce_is_no_longer_binding_on_the_s14"),
              (try_end),
			  (assign, reg1, ":duration_of_status"),
              (str_store_string, s21, "str_s21__the_s5_is_bound_by_truce_not_to_attack_the_s14s18_the_truce_will_expire_in_reg1_days"),
            (else_try),
              (eq, ":diplomatic_status", -1),
              (str_store_string, s21, "str_s21__the_s5_has_recently_suffered_provocation_by_subjects_of_the_s14_and_there_is_a_risk_of_war"),
            (else_try),
              (eq, ":diplomatic_status", 0),
              (str_store_string, s21, "str_s21__the_s5_has_no_outstanding_issues_with_the_s14"),
            (try_end),
            (try_begin),
              (eq, ":reverse_diplomatic_status", -1),
              (str_store_string, s21, "str_s21_the_s14_was_recently_provoked_by_subjects_of_the_s5_and_there_is_a_risk_of_war_"),
            (try_end),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (call_script, "script_npc_decision_checklist_peace_or_war", ":faction_no", ":cur_faction", -1),
			  (str_store_string, s21, "@{!}DEBUG : {s21}.^CHEAT MODE ASSESSMENT: {s14}^"), 
            (try_end),
          (try_end),
          (str_store_string, s0, "str_the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21", 0),
          (set_trigger_result, 1),
        (try_end),
      (else_try),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_defeated),
        (try_begin),
          (eq, ":note_index", 0),
          (str_store_faction_name, s5, ":faction_no"),
          (str_store_string, s0, "@{s5} has been defeated!", 0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":note_index", 1),
          (str_clear, s0),
          (set_trigger_result, 1),
        (try_end),
      (else_try),
        (try_begin),
          (this_or_next|eq, ":note_index", 0),
          (eq, ":note_index", 1),
          (str_clear, s0),
          (set_trigger_result, 1),
        (try_end),
      (try_end),
     ]),


  #script_game_get_quest_note
  # This script is called from the game engine when the notes of a quest is needed.
  # INPUT: arg1 = quest_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_quest_note",
    [
##      (store_script_param_1, ":quest_no"),
##      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0), # set it to 1 if this script is wanted to be used rather than static notes
     ]),


  #script_game_get_info_page_note
  # This script is called from the game engine when the notes of a info_page is needed.
  # INPUT: arg1 = info_page_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_info_page_note",
    [
##      (store_script_param_1, ":info_page_no"),
##      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0), # set it to 1 if this script is wanted to be used rather than static notes
     ]),


  #script_game_get_scene_name
  # This script is called from the game engine when a name for the scene is needed.
  # INPUT: arg1 = scene_no
  # OUTPUT: s0 = name
  ("game_get_scene_name",
    [
      (store_script_param, ":scene_no", 1),
      (try_begin),
        (is_between, ":scene_no", multiplayer_scenes_begin, multiplayer_scenes_end),
        (store_sub, ":string_id", ":scene_no", multiplayer_scenes_begin),
        (val_add, ":string_id", multiplayer_scene_names_begin),
        (str_store_string, s0, ":string_id"),
      (try_end),
     ]),


  #script_game_get_mission_template_name
  # This script is called from the game engine when a name for the mission template is needed.
  # INPUT: arg1 = mission_template_no
  # OUTPUT: s0 = name
  ("game_get_mission_template_name",
    [
      (store_script_param, ":mission_template_no", 1),
      (call_script, "script_multiplayer_get_mission_template_game_type", ":mission_template_no"),
      (assign, ":game_type", reg0),
      (try_begin),
        (is_between, ":game_type", 0, multiplayer_num_game_types),
        (store_add, ":string_id", ":game_type", multiplayer_game_type_names_begin),
        (str_store_string, s0, ":string_id"),
      (try_end),
     ]),


  #script_add_kill_death_counts
  # INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
  # OUTPUT: none
  ("add_kill_death_counts",
   [
      (store_script_param, ":killer_agent_no", 1),
      (store_script_param, ":dead_agent_no", 2),
      
      (try_begin),
        (ge, ":killer_agent_no", 0),
        (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
      (else_try),
        (assign, ":killer_agent_team", -1),
      (try_end),

      (try_begin),
        (ge, ":dead_agent_no", 0),
        (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
      (else_try),
        (assign, ":dead_agent_team", -1),
      (try_end),
      
      #adjusting kill counts of players/bots
      (try_begin), 
        (try_begin), 
          (ge, ":killer_agent_no", 0),
          (ge, ":dead_agent_no", 0),
          (agent_is_human, ":killer_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (neq, ":killer_agent_no", ":dead_agent_no"),
          
          (this_or_next|neq, ":killer_agent_team", ":dead_agent_team"),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          
          (agent_get_player_id, ":killer_agent_player", ":killer_agent_no"),
          (try_begin),
            (agent_is_non_player, ":killer_agent_no"), #if killer agent is bot then increase bot kill counts of killer agent's team by one.
            (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
            (team_get_bot_kill_count, ":killer_agent_team_bot_kill_count", ":killer_agent_team"),
            (val_add, ":killer_agent_team_bot_kill_count", 1),
            (team_set_bot_kill_count, ":killer_agent_team", ":killer_agent_team_bot_kill_count"),            
          (else_try), #if killer agent is not bot then increase kill counts of killer agent's player by one.
            (player_is_active, ":killer_agent_player"),
            (player_get_kill_count, ":killer_agent_player_kill_count", ":killer_agent_player"),
            (val_add, ":killer_agent_player_kill_count", 1),
            (player_set_kill_count, ":killer_agent_player", ":killer_agent_player_kill_count"),
          (try_end),
        (try_end),           

        (try_begin), 
          (ge, ":dead_agent_no", 0),
          (agent_is_human, ":dead_agent_no"),
          (try_begin),
            (agent_is_non_player, ":dead_agent_no"), #if dead agent is bot then increase bot kill counts of dead agent's team by one.
            (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
            (team_get_bot_death_count, ":dead_agent_team_bot_death_count", ":dead_agent_team"),
            (val_add, ":dead_agent_team_bot_death_count", 1),
            (team_set_bot_death_count, ":dead_agent_team", ":dead_agent_team_bot_death_count"),
          (else_try), #if dead agent is not bot then increase death counts of dead agent's player by one.
            (agent_get_player_id, ":dead_agent_player", ":dead_agent_no"),
            (player_is_active, ":dead_agent_player"),
            (player_get_death_count, ":dead_agent_player_death_count", ":dead_agent_player"),
            (val_add, ":dead_agent_player_death_count", 1),
            (player_set_death_count, ":dead_agent_player", ":dead_agent_player_death_count"),
          (try_end),

          (try_begin),
            (assign, ":continue", 0),
      
            (try_begin),
              (this_or_next|lt, ":killer_agent_no", 0), #if he killed himself (1a(team change) or 1b(self kill)) then decrease kill counts of killer player by one.
              (eq, ":killer_agent_no", ":dead_agent_no"),
              (assign, ":continue", 1),
            (try_end),

            (try_begin),
              (eq, ":killer_agent_team", ":dead_agent_team"), #if he killed a teammate and game mod is not deathmatch then decrease kill counts of killer player by one.
              (neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
              (neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
              (assign, ":continue", 1),
            (try_end),

            (eq, ":continue", 1),
                    
            (try_begin),
              (ge, ":killer_agent_no", 0),
              (assign, ":responsible_agent", ":killer_agent_no"),                
            (else_try),
              (assign, ":responsible_agent", ":dead_agent_no"),
            (try_end),

            (try_begin),
              (ge, ":responsible_agent", 0),
              (neg|agent_is_non_player, ":responsible_agent"),
              (agent_get_player_id, ":responsible_player", ":responsible_agent"),
              (ge, ":responsible_player", 0),
              (player_get_kill_count, ":dead_agent_player_kill_count", ":responsible_player"),
              (val_add, ":dead_agent_player_kill_count", -1),
              (player_set_kill_count, ":responsible_player", ":dead_agent_player_kill_count"),
            (try_end),
          (try_end),               
        (try_end),
      (try_end),
    ]),


  #script_game_receive_url_response
  #response format should be like this:
  #  [a number or a string]|[another number or a string]|[yet another number or a string] ...
  # here is an example response:
  # 12|Player|100|another string|142|323542|34454|yet another string
  # INPUT: arg1 = num_integers, arg2 = num_strings
  # reg0, reg1, reg2, ... up to 128 registers contain the integer values
  # s0, s1, s2, ... up to 128 strings contain the string values
  ("game_receive_url_response",
    [
      #here is an example usage
##      (store_script_param, ":num_integers", 1),
##      (store_script_param, ":num_strings", 2),
##      (try_begin),
##        (gt, ":num_integers", 4),
##        (display_message, "@{reg0}, {reg1}, {reg2}, {reg3}, {reg4}"),
##      (try_end),
##      (try_begin),
##        (gt, ":num_strings", 4),
##        (display_message, "@{s0}, {s1}, {s2}, {s3}, {s4}"),
##      (try_end),
      ]),


  ("game_get_cheat_mode",
  [
    (assign, reg0, "$cheat_mode"),
  ]), 


  #script_game_receive_network_message
  # This script is called from the game engine when a new network message is received.
  # INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
  ("game_receive_network_message",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":event_type", 2),
      (try_begin),
        ###############
        #SERVER EVENTS#
        ###############
        (eq, ":event_type", multiplayer_event_set_item_selection),
        (store_script_param, ":slot_no", 3),
        (store_script_param, ":value", 4),
        (try_begin),
          #valid slot check
          (is_between, ":slot_no", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
          #valid item check
          (assign, ":valid_item", 0),
          (try_begin),
            (eq, ":value", -1),
            (assign, ":valid_item", 1),
          (else_try),
            (ge, ":value", 0),
            (player_get_troop_id, ":player_troop_no", ":player_no"),
            (is_between, ":player_troop_no", multiplayer_troops_begin, multiplayer_troops_end),
            (store_sub, ":troop_index", ":player_troop_no", multiplayer_troops_begin),
            (val_add, ":troop_index", slot_item_multiplayer_availability_linked_list_begin),
            (item_get_slot, ":prev_next_item_ids", ":value", ":troop_index"),
            (gt, ":prev_next_item_ids", 0), #0 if the item is not valid for the multiplayer mode
            (assign, ":valid_item", 1),
            (try_begin),
              (neq, "$g_horses_are_avaliable", 1),
              (item_get_slot, ":item_class", ":value", slot_item_multiplayer_item_class),
              (is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
              (assign, ":valid_item", 0),
            (try_end),
            (try_begin),
              (eq, "$g_multiplayer_disallow_ranged_weapons", 1),
              (item_get_slot, ":item_class", ":value", slot_item_multiplayer_item_class),
              (is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
              (assign, ":valid_item", 0),
            (try_end),
          (try_end),
          (eq, ":valid_item", 1),
          #condition checks are done
          (player_set_slot, ":player_no", ":slot_no", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_set_bot_selection),
        (store_script_param, ":slot_no", 3),
        (store_script_param, ":value", 4),
        (try_begin),
          #condition check
          (is_between, ":slot_no", slot_player_bot_type_1_wanted, slot_player_bot_type_4_wanted + 1),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (player_set_slot, ":player_no", ":slot_no", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_change_team_no),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_get_team_no, ":player_team", ":player_no"),
          (neq, ":player_team", ":value"),

          #condition checks are done
          (try_begin),
            #check if available
            (call_script, "script_cf_multiplayer_team_is_available", ":player_no", ":value"),
            #reset troop_id to -1
            (player_set_troop_id, ":player_no", -1),
            (player_set_team_no, ":player_no", ":value"),
            (try_begin),
              (neq, ":value", multi_team_spectator),
              (neq, ":value", multi_team_unassigned),
      
              (store_mission_timer_a, ":player_last_team_select_time"),         
              (player_set_slot, ":player_no", slot_player_last_team_select_time, ":player_last_team_select_time"),
      
              (multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_confirmation),
            (try_end),
          (else_try),
            #reject request
            (multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_rejection),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_change_troop_id),
        (store_script_param, ":value", 3),
        #troop-faction validity check
        (try_begin),
          (eq, ":value", -1),
          (player_set_troop_id, ":player_no", -1),
        (else_try),
          (is_between, ":value", multiplayer_troops_begin, multiplayer_troops_end),
          (player_get_team_no, ":player_team", ":player_no"),
          (is_between, ":player_team", 0, multi_team_spectator),
          (team_get_faction, ":team_faction", ":player_team"),
          (store_troop_faction, ":new_troop_faction", ":value"),
          (eq, ":new_troop_faction", ":team_faction"),
          (player_set_troop_id, ":player_no", ":value"),
          (call_script, "script_multiplayer_clear_player_selected_items", ":player_no"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_start_map),
        (store_script_param, ":value", 3),
        (store_script_param, ":value_2", 4),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", multiplayer_scenes_begin, multiplayer_scenes_end),
          (is_between, ":value_2", 0, multiplayer_num_game_types),
          (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
          (this_or_next|eq, "$g_multiplayer_changing_game_type_allowed", 1),
          (eq, "$g_multiplayer_game_type", ":value_2"),
          (call_script, "script_multiplayer_fill_map_game_types", ":value_2"),
          (assign, ":num_maps", reg0),
          (assign, ":is_valid", 0),
          (store_add, ":end_cond", multi_data_maps_for_game_type_begin, ":num_maps"),
          (try_for_range, ":i_map", multi_data_maps_for_game_type_begin, ":end_cond"),
            (troop_slot_eq, "trp_multiplayer_data", ":i_map", ":value"),
            (assign, ":is_valid", 1),
            (assign, ":end_cond", 0),
          (try_end),
          (eq, ":is_valid", 1),
          #condition checks are done
          (assign, "$g_multiplayer_game_type", ":value_2"),
          (assign, "$g_multiplayer_selected_map", ":value"),
          (team_set_faction, 0, "$g_multiplayer_next_team_1_faction"),
          (team_set_faction, 1, "$g_multiplayer_next_team_2_faction"),
          (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
          (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 1),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_max_num_players),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 2, 201),
          #condition checks are done
          (server_set_max_num_players, ":value"),      
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_num_bots_in_team),
        (store_script_param, ":value", 3),
        (store_script_param, ":value_2", 4),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 1, 3),
          (is_between, ":value_2", 0, "$g_multiplayer_max_num_bots"),
          #condition checks are done
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_num_bots_team_1", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_num_bots_team_2", ":value_2"),
          (try_end),
          (get_max_players, ":num_players"),                               
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, ":value", ":value_2"),
          (try_end),            
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_anti_cheat),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_anti_cheat, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_friendly_fire),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_friendly_fire, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_melee_friendly_fire),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_melee_friendly_fire, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_friendly_fire_damage_self_ratio),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 101),
          #condition checks are done
          (server_set_friendly_fire_damage_self_ratio, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_friendly_fire_damage_friend_ratio),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 101),
          #condition checks are done
          (server_set_friendly_fire_damage_friend_ratio, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_ghost_mode),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 4),
          #condition checks are done
          (server_set_ghost_mode, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_control_block_dir),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_control_block_dir, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_combat_speed),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 5),
          #condition checks are done
          (server_set_combat_speed, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_respawn_count),
        (store_script_param, ":value", 3),
        #validity check
        (player_is_admin, ":player_no"),
        (is_between, ":value", 0, 6),
        #condition checks are done       
        (assign, "$g_multiplayer_number_of_respawn_count", ":value"),
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 1, ":num_players"),
          (player_is_active, ":cur_player"),
          (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_count, ":value"),
        (try_end),                  
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_add_to_servers_list),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_set_add_to_game_servers_list, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_respawn_period), 
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 3, 31),
          #condition checks are done
          (assign, "$g_multiplayer_respawn_period", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_period, ":value"),
          (try_end),            
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_game_max_minutes),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 5, 121),
          #condition checks are done
          (assign, "$g_multiplayer_game_max_minutes", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_round_max_seconds),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 60, 901),
          #condition checks are done
          (assign, "$g_multiplayer_round_max_seconds", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_round_max_seconds, ":value"),
          (try_end),            
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_player_respawn_as_bot),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_player_respawn_as_bot", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_player_respawn_as_bot, ":value"),
          (try_end),            
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_game_max_points),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 3, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_game_max_points", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_point_gained_from_flags),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 25, 401),
          #condition checks are done
          (assign, "$g_multiplayer_point_gained_from_flags", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_point_gained_from_capturing_flag),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 11),
          #condition checks are done
          (assign, "$g_multiplayer_point_gained_from_capturing_flag", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_initial_gold_multiplier),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_initial_gold_multiplier", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_battle_earnings_multiplier),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_battle_earnings_multiplier", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_round_earnings_multiplier),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_round_earnings_multiplier", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_server_name),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
          (eq, "$g_multiplayer_renaming_server_allowed", 1),
          #condition checks are done
          (server_set_name, s0), #validity is checked inside this function
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_game_password),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_set_password, s0), #validity is checked inside this function
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_welcome_message),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_set_welcome_message, s0), #validity is checked inside this function
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_team_faction),
        (store_script_param, ":value", 3),
        (store_script_param, ":value_2", 4),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 1, 3),
          (is_between, ":value_2", npc_kingdoms_begin, npc_kingdoms_end),
##          (assign, ":is_valid", 0),
##          (try_begin),
##            (eq, ":value", 1),
##            (neq, ":value_2", "$g_multiplayer_next_team_2_faction"),
##            (assign, ":is_valid", 1),
##          (else_try),
##            (neq, ":value_2", "$g_multiplayer_next_team_1_faction"),
##            (assign, ":is_valid", 1),
##          (try_end),
##          (eq, ":is_valid", 1),
          #condition checks are done
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_next_team_1_faction", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_next_team_2_faction", ":value_2"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_open_game_rules),
        (try_begin),
          #no validity check
          (server_get_max_num_players, ":max_num_players"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 1, "$g_multiplayer_next_team_1_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 2, "$g_multiplayer_next_team_2_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
          (server_get_anti_cheat, ":server_anti_cheat"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
          (server_get_friendly_fire, ":server_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
          (server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
          (server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (server_get_ghost_mode, ":server_ghost_mode"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
          (server_get_control_block_dir, ":server_control_block_dir"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
          (server_get_combat_speed, ":server_combat_speed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
          (server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_minutes, "$g_multiplayer_game_max_minutes"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_points, "$g_multiplayer_game_max_points"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_flags, "$g_multiplayer_point_gained_from_flags"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_capturing_flag, "$g_multiplayer_point_gained_from_capturing_flag"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_initial_gold_multiplier, "$g_multiplayer_initial_gold_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_battle_earnings_multiplier, "$g_multiplayer_battle_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_earnings_multiplier, "$g_multiplayer_round_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
          (str_store_server_name, s0),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
          (multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_open_game_rules),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_open_admin_panel),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
          (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
          (server_get_max_num_players, ":max_num_players"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 1, "$g_multiplayer_next_team_1_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 2, "$g_multiplayer_next_team_2_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
          (server_get_anti_cheat, ":server_anti_cheat"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
          (server_get_friendly_fire, ":server_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
          (server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
          (server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (server_get_ghost_mode, ":server_ghost_mode"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
          (server_get_control_block_dir, ":server_control_block_dir"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
          (server_get_combat_speed, ":server_combat_speed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
          (server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_minutes, "$g_multiplayer_game_max_minutes"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_points, "$g_multiplayer_game_max_points"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_flags, "$g_multiplayer_point_gained_from_flags"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_capturing_flag, "$g_multiplayer_point_gained_from_capturing_flag"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_initial_gold_multiplier, "$g_multiplayer_initial_gold_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_battle_earnings_multiplier, "$g_multiplayer_battle_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_earnings_multiplier, "$g_multiplayer_round_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_bots, "$g_multiplayer_max_num_bots"),
          (str_store_server_name, s0),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
          (str_store_server_password, s0),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_game_password, s0),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_start_new_poll),
        (try_begin),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
           #validity check
          (eq, "$g_multiplayer_poll_running", 0),
          (store_mission_timer_a, ":mission_timer"),
          (player_get_slot, ":poll_disable_time", ":player_no", slot_player_poll_disabled_until_time),
          (ge, ":mission_timer", ":poll_disable_time"),
          (assign, ":continue", 0),
          (try_begin),
            (eq, ":value", 1), # kicking a player
            (try_begin),
              (eq, "$g_multiplayer_kick_voteable", 1),
              (player_is_active, ":value_2"),
              (assign, ":continue", 1),
            (try_end),
          (else_try),
            (eq, ":value", 2), # banning a player
            (try_begin),
              (eq, "$g_multiplayer_ban_voteable", 1),
              (player_is_active, ":value_2"),
              (save_ban_info_of_player, ":value_2"),
              (assign, ":continue", 1),
            (try_end),
          (else_try), # vote for map
            (eq, ":value", 0),
            (try_begin),
              (eq, "$g_multiplayer_maps_voteable", 1),
              (call_script, "script_multiplayer_fill_map_game_types", "$g_multiplayer_game_type"),
              (assign, ":num_maps", reg0),
              (try_for_range, ":i_map", 0, ":num_maps"),
                (store_add, ":map_slot", ":i_map", multi_data_maps_for_game_type_begin),
                (troop_slot_eq, "trp_multiplayer_data", ":map_slot", ":value_2"),
                (assign, ":continue", 1),
                (assign, ":num_maps", 0), #break
              (try_end),
            (try_end),
          (else_try),
            (eq, ":value", 3), #vote for map and factions
            (try_begin),
              (eq, "$g_multiplayer_factions_voteable", 1),
              (store_script_param, ":value_3", 5),
              (store_script_param, ":value_4", 6),
              (call_script, "script_multiplayer_fill_map_game_types", "$g_multiplayer_game_type"),
              (assign, ":num_maps", reg0),
              (try_for_range, ":i_map", 0, ":num_maps"),
                (store_add, ":map_slot", ":i_map", multi_data_maps_for_game_type_begin),
                (troop_slot_eq, "trp_multiplayer_data", ":map_slot", ":value_2"),
                (assign, ":continue", 1),
                (assign, ":num_maps", 0), #break
              (try_end),
              (try_begin),
                (eq, ":continue", 1),
                (this_or_next|neg|is_between, ":value_3", npc_kingdoms_begin, npc_kingdoms_end),
                (this_or_next|neg|is_between, ":value_4", npc_kingdoms_begin, npc_kingdoms_end),
                (eq, ":value_3", ":value_4"),
                (assign, ":continue", 0),
              (try_end),
            (try_end),
          (else_try),
            (eq, ":value", 4), #vote for number of bots
            (store_script_param, ":value_3", 5),
            (store_add, ":upper_limit", "$g_multiplayer_num_bots_voteable", 1),
            (is_between, ":value_2", 0, ":upper_limit"),
            (is_between, ":value_3", 0, ":upper_limit"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          #condition checks are done
          (str_store_player_username, s0, ":player_no"),
          (try_begin),
            (eq, ":value", 1), #kicking a player
            (str_store_player_username, s1, ":value_2"),
            (server_add_message_to_log, "str_poll_kick_player_s1_by_s0"),
          (else_try),
            (eq, ":value", 2), #banning a player
            (str_store_player_username, s1, ":value_2"),
            (server_add_message_to_log, "str_poll_ban_player_s1_by_s0"),
          (else_try),
            (eq, ":value", 0), #vote for map
            (store_sub, ":string_index", ":value_2", multiplayer_scenes_begin),
            (val_add, ":string_index", multiplayer_scene_names_begin),
            (str_store_string, s1, ":string_index"),
            (server_add_message_to_log, "str_poll_change_map_to_s1_by_s0"),
          (else_try),
            (eq, ":value", 3), #vote for map and factions
            (store_sub, ":string_index", ":value_2", multiplayer_scenes_begin),
            (val_add, ":string_index", multiplayer_scene_names_begin),
            (str_store_string, s1, ":string_index"),
            (str_store_faction_name, s2, ":value_3"),
            (str_store_faction_name, s3, ":value_4"),
            (server_add_message_to_log, "str_poll_change_map_to_s1_and_factions_to_s2_and_s3_by_s0"),
          (else_try),
            (eq, ":value", 4), #vote for number of bots
            (assign, reg0, ":value_2"),
            (assign, reg1, ":value_3"),
            (server_add_message_to_log, "str_poll_change_number_of_bots_to_reg0_and_reg1_by_s0"),
          (try_end),
          (assign, "$g_multiplayer_poll_running", 1),
          (assign, "$g_multiplayer_poll_ended", 0),
          (assign, "$g_multiplayer_poll_num_sent", 0),
          (assign, "$g_multiplayer_poll_yes_count", 0),
          (assign, "$g_multiplayer_poll_no_count", 0),
          (assign, "$g_multiplayer_poll_to_show", ":value"),
          (assign, "$g_multiplayer_poll_value_to_show", ":value_2"),
          (try_begin),
            (eq, ":value", 3),
            (assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
            (assign, "$g_multiplayer_poll_value_3_to_show", ":value_4"),
          (else_try),
            (eq, ":value", 4),
            (assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
            (assign, "$g_multiplayer_poll_value_3_to_show", -1),
          (else_try),
            (assign, "$g_multiplayer_poll_value_2_to_show", -1),
            (assign, "$g_multiplayer_poll_value_3_to_show", -1),
          (try_end),
          (store_add, ":poll_disable_until", ":mission_timer", multiplayer_poll_disable_period),
          (player_set_slot, ":player_no", slot_player_poll_disabled_until_time, ":poll_disable_until"),
          (store_add, "$g_multiplayer_poll_end_time", ":mission_timer", 60),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 0, ":num_players"),
            (player_is_active, ":cur_player"),
            (player_set_slot, ":cur_player", slot_player_can_answer_poll, 1),
            (val_add, "$g_multiplayer_poll_num_sent", 1),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_ask_for_poll, "$g_multiplayer_poll_to_show", "$g_multiplayer_poll_value_to_show", "$g_multiplayer_poll_value_2_to_show", "$g_multiplayer_poll_value_3_to_show"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_answer_to_poll),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (eq, "$g_multiplayer_poll_running", 1),
          (is_between, ":value", 0, 2),
          (player_slot_eq, ":player_no", slot_player_can_answer_poll, 1),
          #condition checks are done
          (player_set_slot, ":player_no", slot_player_can_answer_poll, 0),
          (try_begin),
            (eq, ":value", 0),
            (val_add, "$g_multiplayer_poll_no_count", 1),
          (else_try),
            (eq, ":value", 1),
            (val_add, "$g_multiplayer_poll_yes_count", 1),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_kick_player),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (player_is_active, ":value"),
          #condition checks are done
          (kick_player, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_ban_player),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (player_is_active, ":value"),
          #condition checks are done
          (ban_player, ":value", 0, ":player_no"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_valid_vote_ratio),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 50, 101),
          #condition checks are done
          (assign, "$g_multiplayer_valid_vote_ratio", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_auto_team_balance_limit),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (this_or_next|is_between, ":value", 2, 7),
          (eq, ":value", 1000),
          #condition checks are done
          (assign, "$g_multiplayer_auto_team_balance_limit", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_num_bots_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 51),
          (is_between, ":value", 0, "$g_multiplayer_max_num_bots"),
          #condition checks are done
          (assign, "$g_multiplayer_num_bots_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_num_bots_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_factions_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_factions_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_factions_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_maps_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_maps_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_maps_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_kick_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_kick_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_kick_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_ban_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_ban_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_ban_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_allow_player_banners),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_allow_player_banners", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_force_default_armor),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_force_default_armor", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_offer_duel),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          (agent_is_active, ":value"),
          (agent_is_alive, ":value"),
          (agent_is_human, ":value"),
          (player_get_agent_id, ":player_agent_no", ":player_no"),
          (agent_is_active, ":player_agent_no"),
          (agent_is_alive, ":player_agent_no"),
          (agent_get_position, pos0, ":player_agent_no"),
          (agent_get_position, pos1, ":value"),
          (get_sq_distance_between_positions_in_meters, ":agent_dist_sq", pos0, pos1),
          (le, ":agent_dist_sq", 49),
          #allow duelists to receive new offers
          (this_or_next|agent_check_offer_from_agent, ":player_agent_no", ":value"),
          (agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, -1),
          (neg|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, ":value"), #don't allow spamming duel offers during countdown
          #condition checks are done
          (try_begin),
            #accepting a duel
            (agent_check_offer_from_agent, ":player_agent_no", ":value"),
            (call_script, "script_multiplayer_accept_duel", ":player_agent_no", ":value"),
          (else_try),
            #sending a duel request
            (assign, ":display_notification", 1),
            (try_begin),
              (agent_check_offer_from_agent, ":value", ":player_agent_no"),
              (assign, ":display_notification", 0),
            (try_end),
            (agent_add_offer_with_timeout, ":value", ":player_agent_no", 10000), #10 second timeout
            (agent_get_player_id, ":value_player", ":value"),
            (try_begin),
              (player_is_active, ":value_player"), #might be AI
              (try_begin),
                (eq, ":display_notification", 1),
                (multiplayer_send_int_to_player, ":value_player", multiplayer_event_show_duel_request, ":player_agent_no"),
              (try_end),
            (else_try),
              (call_script, "script_multiplayer_accept_duel", ":value", ":player_agent_no"),
            (try_end),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_disallow_ranged_weapons),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_disallow_ranged_weapons", ":value"),
        (try_end),
      (else_try),
        ###############
        #CLIENT EVENTS#
        ###############
        (neg|multiplayer_is_dedicated_server),
        (try_begin),      
          (eq, ":event_type", multiplayer_event_return_renaming_server_allowed),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_renaming_server_allowed", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_changing_game_type_allowed),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_changing_game_type_allowed", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_max_num_players),
          (store_script_param, ":value", 3),
          (server_set_max_num_players, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_next_team_faction),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_next_team_1_faction", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_next_team_2_faction", ":value_2"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_num_bots_in_team),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_num_bots_team_1", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_num_bots_team_2", ":value_2"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_anti_cheat),
          (store_script_param, ":value", 3),
          (server_set_anti_cheat, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_friendly_fire),
          (store_script_param, ":value", 3),
          (server_set_friendly_fire, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_melee_friendly_fire),
          (store_script_param, ":value", 3),
          (server_set_melee_friendly_fire, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_friendly_fire_damage_self_ratio),
          (store_script_param, ":value", 3),
          (server_set_friendly_fire_damage_self_ratio, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_friendly_fire_damage_friend_ratio),
          (store_script_param, ":value", 3),
          (server_set_friendly_fire_damage_friend_ratio, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_ghost_mode),
          (store_script_param, ":value", 3),
          (server_set_ghost_mode, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_control_block_dir),
          (store_script_param, ":value", 3),
          (server_set_control_block_dir, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_add_to_servers_list),
          (store_script_param, ":value", 3),
          (server_set_add_to_game_servers_list, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_respawn_period),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_respawn_period", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_max_minutes),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_game_max_minutes", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_round_max_seconds),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_round_max_seconds", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_player_respawn_as_bot),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_player_respawn_as_bot", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_max_points),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_game_max_points", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_point_gained_from_flags),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_point_gained_from_flags", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_point_gained_from_capturing_flag),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_point_gained_from_capturing_flag", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_initial_gold_multiplier),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_initial_gold_multiplier", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_battle_earnings_multiplier),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_battle_earnings_multiplier", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_round_earnings_multiplier),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_round_earnings_multiplier", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_respawn_count),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_number_of_respawn_count", ":value"),          
        (else_try),
          (eq, ":event_type", multiplayer_event_return_server_name),
          (server_set_name, s0),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_password),
          (server_set_password, s0),
          #this is the last option in admin panel, so start the presentation
          (start_presentation, "prsnt_game_multiplayer_admin_panel"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_open_game_rules),
          #this is the last message for game rules, so start the presentation
          (assign, "$g_multiplayer_show_server_rules", 1),
          (start_presentation, "prsnt_multiplayer_welcome_message"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_type),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_game_type", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_valid_vote_ratio),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_valid_vote_ratio", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_max_num_bots),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_max_num_bots", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_server_mission_timer_while_player_joined),
          (store_script_param, ":value", 3),
          (assign, "$server_mission_timer_while_player_joined", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_auto_team_balance_limit),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_auto_team_balance_limit", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_num_bots_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_num_bots_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_factions_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_factions_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_maps_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_maps_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_kick_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_kick_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_ban_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_ban_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_allow_player_banners),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_allow_player_banners", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_force_default_armor),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_force_default_armor", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_disallow_ranged_weapons),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_disallow_ranged_weapons", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_confirmation),
          (assign, "$g_confirmation_result", 1),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_rejection),
          (assign, "$g_confirmation_result", -1),
        (else_try),
          (eq, ":event_type", multiplayer_event_show_multiplayer_message),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_show_multiplayer_message", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_draw_this_round),
          (store_script_param, ":value", 3),          
          (call_script, "script_draw_this_round", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_attached_scene_prop),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_set_attached_scene_prop", ":value", ":value_2"), 
          (try_begin),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
            (try_begin),
              (neq, ":value_2", -1),
              (agent_set_horse_speed_factor, ":value", 75),
            (else_try),
              (agent_set_horse_speed_factor, ":value", 100),
            (try_end),              
          (try_end),  
        (else_try),
          (eq, ":event_type", multiplayer_event_set_team_flag_situation),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_set_team_flag_situation", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_team_score),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_team_set_score", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_player_score_kill_death), 
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (store_script_param, ":value_3", 5),
          (store_script_param, ":value_4", 6),
          (call_script, "script_player_set_score", ":value", ":value_2"),
          (call_script, "script_player_set_kill_count", ":value", ":value_3"),
          (call_script, "script_player_set_death_count", ":value", ":value_4"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_num_agents_around_flag),
          (store_script_param, ":flag_no", 3),
          (store_script_param, ":current_owner_code", 4),
          (call_script, "script_set_num_agents_around_flag", ":flag_no", ":current_owner_code"),
        (else_try),
          (eq, ":event_type", multiplayer_event_ask_for_poll),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (store_script_param, ":value_3", 5),
          (store_script_param, ":value_4", 6),
          (assign, ":continue_to_poll", 0),
          (try_begin),
            (this_or_next|eq, ":value", 1),
            (eq, ":value", 2),
            (player_is_active, ":value_2"), #might go offline before here
            (assign, ":continue_to_poll", 1),
          (else_try),
            (assign, ":continue_to_poll", 1),
          (try_end),
          (try_begin),
            (eq, ":continue_to_poll", 1),
            (assign, "$g_multiplayer_poll_to_show", ":value"),
            (assign, "$g_multiplayer_poll_value_to_show", ":value_2"),
            (assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
            (assign, "$g_multiplayer_poll_value_3_to_show", ":value_4"),
            (store_mission_timer_a, ":mission_timer"),
            (store_add, "$g_multiplayer_poll_client_end_time", ":mission_timer", 60),
            (start_presentation, "prsnt_multiplayer_poll"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_change_flag_owner),
          (store_script_param, ":flag_no", 3),
          (store_script_param, ":owner_code", 4),
          (call_script, "script_change_flag_owner", ":flag_no", ":owner_code"),
        (else_try),
          (eq, ":event_type", multiplayer_event_use_item),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_use_item", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_scene_prop_open_or_close),
          (store_script_param, ":instance_id", 3),       
        
          (scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 1),

          (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),

          (try_begin),
            (eq, ":scene_prop_id", "spr_winch_b"),
            (assign, ":effected_object", "spr_portcullis"),
          (else_try),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),     
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),     
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),     
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),                             
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),                             
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
            (eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
            (assign, ":effected_object", ":scene_prop_id"),
          (try_end),

          (try_begin),
            (eq, ":effected_object", "spr_portcullis"),

            (assign, ":smallest_dist", -1),
            (prop_instance_get_position, pos0, ":instance_id"),
            (scene_prop_get_num_instances, ":num_instances_of_effected_object", ":effected_object"),     
            (try_for_range, ":cur_instance", 0, ":num_instances_of_effected_object"),
              (scene_prop_get_instance, ":cur_instance_id", ":effected_object", ":cur_instance"),
              (prop_instance_get_position, pos1, ":cur_instance_id"),
              (get_sq_distance_between_positions, ":dist", pos0, pos1),
              (this_or_next|eq, ":smallest_dist", -1),
              (lt, ":dist", ":smallest_dist"),
              (assign, ":smallest_dist", ":dist"),
              (assign, ":effected_object_instance_id", ":cur_instance_id"),
            (try_end),

            (ge, ":smallest_dist", 0),
            (prop_instance_is_animating, ":is_animating", ":effected_object_instance_id"),
            (eq, ":is_animating", 0),

            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),      
            (position_move_z, pos0, 375),
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
          (else_try),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),     
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),     
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),     
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),     
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),     
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
            (eq, ":scene_prop_id", "spr_castle_f_door_b"),
            (assign, ":effected_object_instance_id", ":instance_id"),  
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            (position_rotate_z, pos0, -80),
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
          (else_try),
            (assign, ":effected_object_instance_id", ":instance_id"),
            (prop_instance_is_animating, ":is_animating", ":effected_object_instance_id"),
            (eq, ":is_animating", 0),
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),      
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),          
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_round_start_time),
          (store_script_param, ":value", 3),

          (try_begin),
            (neq, ":value", -9999),
            (assign, "$g_round_start_time", ":value"),
          (else_try),
            (store_mission_timer_a, "$g_round_start_time"),

            #if round start time is assigning to current time (so new round is starting) then also initialize moveable object slots too.
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_6m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_8m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_10m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_12m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_14m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_winch_b"),         
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_force_start_team_selection),
          (try_begin),
            (is_presentation_active, "prsnt_multiplayer_item_select"),
            (assign, "$g_close_equipment_selection", 1),
          (try_end),
          (start_presentation, "prsnt_multiplayer_troop_select"),
        (else_try),     
          (eq, ":event_type", multiplayer_event_start_death_mode),
          (assign, "$g_battle_death_mode_started", 2),
          (start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
          (call_script, "script_start_death_mode"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_player_respawn_spent),
          (store_script_param, ":value", 3),
          (try_begin),
            (gt, "$g_my_spawn_count", 0),
            (store_add, "$g_my_spawn_count", "$g_my_spawn_count", ":value"),
          (else_try),
            (assign, "$g_my_spawn_count", ":value"),      
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_show_duel_request),
          (store_script_param, ":value", 3),
          (try_begin),
            (agent_is_active, ":value"),
            (agent_get_player_id, ":value_player_no", ":value"),
            (try_begin),
              (player_is_active, ":value_player_no"),
              (str_store_player_username, s0, ":value_player_no"),
            (else_try),
              (str_store_agent_name, s0, ":value"),
            (try_end),
            (display_message, "str_s0_offers_a_duel_with_you"),
            (try_begin),
              (get_player_agent_no, ":player_agent"),
              (agent_is_active, ":player_agent"),
              (agent_add_offer_with_timeout, ":player_agent", ":value", 10000), #10 second timeout
            (try_end),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_start_duel),
          (store_script_param, ":value", 3),
          (store_mission_timer_a, ":mission_timer"),
          (try_begin),
            (agent_is_active, ":value"),
            (get_player_agent_no, ":player_agent"),
            (agent_is_active, ":player_agent"),
            (agent_get_player_id, ":value_player_no", ":value"),
            (try_begin),
              (player_is_active, ":value_player_no"),
              (str_store_player_username, s0, ":value_player_no"),
            (else_try),
              (str_store_agent_name, s0, ":value"),
            (try_end),
            (display_message, "str_a_duel_between_you_and_s0_will_start_in_3_seconds"),
            (assign, "$g_multiplayer_duel_start_time", ":mission_timer"),
            (start_presentation, "prsnt_multiplayer_duel_start_counter"),
            (agent_set_slot, ":player_agent", slot_agent_in_duel_with, ":value"),
            (agent_set_slot, ":value", slot_agent_in_duel_with, ":player_agent"),
            (agent_set_slot, ":player_agent", slot_agent_duel_start_time, ":mission_timer"),
            (agent_set_slot, ":value", slot_agent_duel_start_time, ":mission_timer"),
            (agent_clear_relations_with_agents, ":player_agent"),
            (agent_clear_relations_with_agents, ":value"),
##            (agent_add_relation_with_agent, ":player_agent", ":value", -1),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_cancel_duel),
          (store_script_param, ":value", 3),
          (try_begin),
            (agent_is_active, ":value"),
            (agent_get_player_id, ":value_player_no", ":value"),
            (try_begin),
              (player_is_active, ":value_player_no"),
              (str_store_player_username, s0, ":value_player_no"),
            (else_try),
              (str_store_agent_name, s0, ":value"),
            (try_end),
            (display_message, "str_your_duel_with_s0_is_cancelled"),
          (try_end),
          (try_begin),
            (get_player_agent_no, ":player_agent"),
            (agent_is_active, ":player_agent"),
            (agent_set_slot, ":player_agent", slot_agent_in_duel_with, -1),
            (agent_clear_relations_with_agents, ":player_agent"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_show_server_message),
          (display_message, "str_server_s0", 0xFFFF6666),
        (try_end),
     ]),


  #script_game_get_party_prisoner_limit:
  # This script is called from the game engine when the prisoner limit is needed for a party.
  # INPUT: arg1 = party_no
  # OUTPUT: reg0 = prisoner_limit
  ("game_get_party_prisoner_limit",
    [
#      (store_script_param_1, ":party_no"),
      (assign, ":troop_no", "trp_player"),

      (assign, ":limit", 0),
      (store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
      (store_mul, ":limit", ":skill", 5),
      (assign, reg0, ":limit"),
      (set_trigger_result, reg0),
  ]),


  #script_game_get_item_extra_text:
  # This script is called from the game engine when an item's properties are displayed.
  # INPUT: arg1 = item_no, arg2 = extra_text_id (this can be between 0-7 (7 included)), arg3 = item_modifier
  # OUTPUT: result_string = item extra text, trigger_result = text color (0 for default)
  ("game_get_item_extra_text",
    [
      (store_script_param, ":item_no", 1),
      (store_script_param, ":extra_text_id", 2),
      (store_script_param, ":item_modifier", 3),
      (try_begin),
        (is_between, ":item_no", food_begin, food_end),
        (try_begin),
          (eq, ":extra_text_id", 0),
          (assign, ":continue", 1),
          (try_begin),
            (this_or_next|eq, ":item_no", "itm_cattle_meat"),
            (this_or_next|eq, ":item_no", "itm_pork"),
				(eq, ":item_no", "itm_chicken"),
				
            (eq, ":item_modifier", imod_rotten),
            (assign, ":continue", 0),
          (try_end),
          (eq, ":continue", 1),
          (item_get_slot, ":food_bonus", ":item_no", slot_item_food_bonus),
          (assign, reg1, ":food_bonus"),
          (set_result_string, "@+{reg1} to party morale"),
          (set_trigger_result, 0x4444FF),
        (try_end),
      (else_try),
        (is_between, ":item_no", readable_books_begin, readable_books_end),
        (try_begin),
          (eq, ":extra_text_id", 0),
          (item_get_slot, reg1, ":item_no", slot_item_intelligence_requirement),
          (set_result_string, "@Requires {reg1} intelligence to read"),
          (set_trigger_result, 0xFFEEDD),
        (else_try),
          (eq, ":extra_text_id", 1),
          (item_get_slot, ":progress", ":item_no", slot_item_book_reading_progress),
          (val_div, ":progress", 10),
          (assign, reg1, ":progress"),
          (set_result_string, "@Reading Progress: {reg1}%"),
          (set_trigger_result, 0xFFEEDD),
        (try_end),
      (else_try),
        (is_between, ":item_no", reference_books_begin, reference_books_end),#book
        (try_begin),
          (eq, ":extra_text_id", 0),
          (try_begin),
            (eq, ":item_no", "itm_book_wound_treatment_reference"),
            (str_store_string, s1, "@wound treament"),
          (else_try),
            (eq, ":item_no", "itm_book_training_reference"),
            (str_store_string, s1, "@trainer"),
          (else_try),
            (eq, ":item_no", "itm_book_surgery_reference"),
            (str_store_string, s1, "@surgery"),
          (try_end),
          (set_result_string, "@+1 to {s1} while in inventory"),
          (set_trigger_result, 0xFFEEDD),
        (try_end),
      (try_end),
  ]),


  #script_game_on_disembark:
  # This script is called from the game engine when the player reaches the shore with a ship.
  # INPUT: pos0 = disembark position
  # OUTPUT: none
  ("game_on_disembark",
   [(jump_to_menu, "mnu_disembark"),
  ]),


  #script_game_context_menu_get_buttons:
  # This script is called from the game engine when the player clicks the right mouse button over a party on the map.
  # INPUT: arg1 = party_no
  # OUTPUT: none, fills the menu buttons
  ("game_context_menu_get_buttons",
   [
     (store_script_param, ":party_no", 1),
     (try_begin),
       (neq, ":party_no", "p_main_party"),
       (context_menu_add_item, "@Move here", cmenu_move),
     (try_end),
        
     (try_begin),
       (is_between, ":party_no", centers_begin, centers_end),
       (context_menu_add_item, "@View notes", 1),
     (else_try),
       (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
       (gt, ":num_stacks", 0),
       (party_stack_get_troop_id, ":troop_no", ":party_no", 0),
       (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
       (context_menu_add_item, "@View notes", 2),
     (try_end),
    
     (try_begin),
       (neq, ":party_no", "p_main_party"),       
       (store_faction_of_party, ":party_faction", ":party_no"),
                     
       (this_or_next|eq, ":party_faction", "$players_kingdom"),
       (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
       (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
       
       (neg|is_between, ":party_no", centers_begin, centers_end),
       
       (context_menu_add_item, "@Accompany", cmenu_follow), 
     (try_end),    
  ]),


  #script_game_event_context_menu_button_clicked:
  # This script is called from the game engine when the player clicks on a button at the right mouse menu.
  # INPUT: arg1 = party_no, arg2 = button_value
  # OUTPUT: none
  ("game_event_context_menu_button_clicked",
   [(store_script_param, ":party_no", 1),
    (store_script_param, ":button_value", 2),
    (try_begin),
      (eq, ":button_value", 1),
      (change_screen_notes, 3, ":party_no"),
    (else_try),
      (eq, ":button_value", 2),
      (party_stack_get_troop_id, ":troop_no", ":party_no", 0),
      (change_screen_notes, 1, ":troop_no"),
    (try_end),
  ]),


  #script_game_get_skill_modifier_for_troop
  # This script is called from the game engine when a skill's modifiers are needed
  # INPUT: arg1 = troop_no, arg2 = skill_no
  # OUTPUT: trigger_result = modifier_value
  ("game_get_skill_modifier_for_troop",
   [(store_script_param, ":troop_no", 1),
    (store_script_param, ":skill_no", 2),
    (assign, ":modifier_value", 0),
    (try_begin),
      (eq, ":skill_no", "skl_wound_treatment"),
      (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_wound_treatment_reference"),
      (gt, reg0, 0),
      (val_add, ":modifier_value", 1),
    (else_try),
      (eq, ":skill_no", "skl_trainer"),
      (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_training_reference"),
      (gt, reg0, 0),
      (val_add, ":modifier_value", 1),
    (else_try),
      (eq, ":skill_no", "skl_surgery"),
      (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_surgery_reference"),
      (gt, reg0, 0),
      (val_add, ":modifier_value", 1),
    (try_end),
    (set_trigger_result, ":modifier_value"),
    ]),


  #script_game_check_party_sees_party
  # This script is called from the game engine when a party is inside the range of another party
  # INPUT: arg1 = party_no_seer, arg2 = party_no_seen
  # OUTPUT: trigger_result = true or false (1 = true, 0 = false)
#  ("game_check_party_sees_party",
#   [
#     (store_script_param, ":party_no_seer", 1),
#     (store_script_param, ":party_no_seen", 2),
#     (set_trigger_result, 1),
#    ]),


  #script_game_get_party_speed_multiplier
  # This script is called from the game engine when a skill's modifiers are needed
  # INPUT: arg1 = party_no
  # OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
#  ("game_get_party_speed_multiplier",
#   [
#     (store_script_param, ":party_no", 1),
#     (set_trigger_result, 100),
#    ]),


  ("game_character_screen_requested",
  [
  ]),


  # script_game_get_multiplayer_server_option_for_mission_template
  # Input: arg1 = mission_template_id, arg2 = option_index
  # Output: trigger_result = 1 for option available, 0 for not available
  # reg0 = option_value
  ("game_get_multiplayer_server_option_for_mission_template",
   [
     (store_script_param, ":mission_template_id", 1),
     (store_script_param, ":option_index", 2),
     (try_begin),
       (eq, ":option_index", 0),
       (assign, reg0, "$g_multiplayer_team_1_faction"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 1),
       (assign, reg0, "$g_multiplayer_team_2_faction"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 2),
       (assign, reg0, "$g_multiplayer_num_bots_team_1"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 3),
       (assign, reg0, "$g_multiplayer_num_bots_team_2"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 4),
       (server_get_friendly_fire, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 5),
       (server_get_melee_friendly_fire, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 6),
       (server_get_friendly_fire_damage_self_ratio, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 7),
       (server_get_friendly_fire_damage_friend_ratio, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 8),
       (server_get_ghost_mode, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 9),
       (server_get_control_block_dir, reg0),       
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 10),
       (server_get_combat_speed, reg0),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (eq, ":mission_template_id", "mt_multiplayer_hq"),
         (val_add, ":option_index", 1), #max game time
       (try_end),
       (eq, ":option_index", 11),
       (assign, reg0, "$g_multiplayer_game_max_minutes"),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_bt"),
         (neq, ":mission_template_id", "mt_multiplayer_fd"),
         (neq, ":mission_template_id", "mt_multiplayer_sg"),
         (val_add, ":option_index", 1), #max round time
       (try_end),
       (eq, ":option_index", 12),
       (assign, reg0, "$g_multiplayer_round_max_seconds"),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_bt"),
         (neq, ":mission_template_id", "mt_multiplayer_fd"),
         (val_add, ":option_index", 1), #respawn as bot
       (try_end),
       (eq, ":option_index", 13),
       (assign, reg0, "$g_multiplayer_player_respawn_as_bot"),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_sg"),
         (val_add, ":option_index", 1), #respawn limit
       (try_end),
       (eq, ":option_index", 14),
       (assign, reg0, "$g_multiplayer_number_of_respawn_count"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 15),
       (assign, reg0, "$g_multiplayer_game_max_points"),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_hq"),
         (val_add, ":option_index", 1), #point gained from flags
       (try_end),
       (eq, ":option_index", 16),
       (assign, reg0, "$g_multiplayer_point_gained_from_flags"),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_cf"),
         (val_add, ":option_index", 1), #point gained from capturing flag
       (try_end),
       (eq, ":option_index", 17),
       (assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 18),
       (assign, reg0, "$g_multiplayer_respawn_period"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 19),
       (assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 20),
       (assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
       (set_trigger_result, 1),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_bt"),
         (neq, ":mission_template_id", "mt_multiplayer_fd"),
         (neq, ":mission_template_id", "mt_multiplayer_sg"),
         (val_add, ":option_index", 1),
       (try_end),
       (eq, ":option_index", 21),
       (assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
       (set_trigger_result, 1),
     (try_end),     
     ]),


  # script_game_multiplayer_server_option_for_mission_template_to_string
  # Input: arg1 = mission_template_id, arg2 = option_index, arg3 = option_value
  # Output: s0 = option_text
  ("game_multiplayer_server_option_for_mission_template_to_string",
   [
     (store_script_param, ":mission_template_id", 1),
     (store_script_param, ":option_index", 2),
     (store_script_param, ":option_value", 3),
     (str_clear, s0),
     (try_begin),
       (eq, ":option_index", 0),
       (assign, reg1, 1),
       (str_store_string, s0, "str_team_reg1_faction"),
       (str_store_faction_name, s1, ":option_value"),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 1),
       (assign, reg1, 2),
       (str_store_string, s0, "str_team_reg1_faction"),
       (str_store_faction_name, s1, ":option_value"),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 2),
       (assign, reg1, 1),
       (str_store_string, s0, "str_number_of_bots_in_team_reg1"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 3),
       (assign, reg1, 2),
       (str_store_string, s0, "str_number_of_bots_in_team_reg1"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 4),
       (str_store_string, s0, "str_allow_friendly_fire"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 5),
       (str_store_string, s0, "str_allow_melee_friendly_fire"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 6),
       (str_store_string, s0, "str_friendly_fire_damage_self_ratio"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 7),
       (str_store_string, s0, "str_friendly_fire_damage_friend_ratio"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 8),
       (str_store_string, s0, "str_spectator_camera"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_free"),
       (else_try),
         (eq, ":option_value", 1),
         (str_store_string, s1, "str_stick_to_any_player"),
       (else_try),
         (eq, ":option_value", 2),
         (str_store_string, s1, "str_stick_to_team_members"),
       (else_try),
         (str_store_string, s1, "str_stick_to_team_members_view"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 9),
       (str_store_string, s0, "str_control_block_direction"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_automatic"),
       (else_try),
         (str_store_string, s1, "str_by_mouse_movement"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 10),
       (str_store_string, s0, "str_combat_speed"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_combat_speed_0"),
       (else_try),
         (eq, ":option_value", 1),
         (str_store_string, s1, "str_combat_speed_1"),
       (else_try),
         (eq, ":option_value", 2),
         (str_store_string, s1, "str_combat_speed_2"),
       (else_try),
         (eq, ":option_value", 3),
         (str_store_string, s1, "str_combat_speed_3"),
       (else_try),
         (str_store_string, s1, "str_combat_speed_4"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (try_begin),
         (eq, ":mission_template_id", "mt_multiplayer_hq"),
         (val_add, ":option_index", 1), #max game time
       (try_end),
       (eq, ":option_index", 11),
       (str_store_string, s0, "str_map_time_limit"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_bt"),
         (neq, ":mission_template_id", "mt_multiplayer_fd"),
         (neq, ":mission_template_id", "mt_multiplayer_sg"),
         (val_add, ":option_index", 1), #max round time
       (try_end),
       (eq, ":option_index", 12),
       (str_store_string, s0, "str_round_time_limit"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_bt"),
         (neq, ":mission_template_id", "mt_multiplayer_fd"),
         (val_add, ":option_index", 1), #respawn as bot
       (try_end),
       (eq, ":option_index", 13),
       (str_store_string, s0, "str_players_take_control_of_a_bot_after_death"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_sg"),
         (val_add, ":option_index", 1), #respawn limit
       (try_end),
       (eq, ":option_index", 14),
       (str_store_string, s0, "str_defender_spawn_count_limit"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_unlimited"),
       (else_try),
         (assign, reg1, ":option_value"),
         (str_store_string, s1, "str_reg1"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 15),
       (str_store_string, s0, "str_team_points_limit"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_hq"),
         (val_add, ":option_index", 1), #point gained from flags
       (try_end),
       (eq, ":option_index", 16),
       (str_store_string, s0, "str_point_gained_from_flags"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_cf"),
         (val_add, ":option_index", 1), #point gained from capturing flag
       (try_end),
       (eq, ":option_index", 17),
       (str_store_string, s0, "str_point_gained_from_capturing_flag"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 18),
       (str_store_string, s0, "str_respawn_period"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 19),
       (str_store_string, s0, "str_initial_gold_multiplier"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 20),
       (str_store_string, s0, "str_battle_earnings_multiplier"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (try_begin),
         (neq, ":mission_template_id", "mt_multiplayer_bt"),
         (neq, ":mission_template_id", "mt_multiplayer_fd"),
         (neq, ":mission_template_id", "mt_multiplayer_sg"),
         (val_add, ":option_index", 1),
       (try_end),
       (eq, ":option_index", 21),
       (str_store_string, s0, "str_round_earnings_multiplier"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (try_end),
     ]),


  # script_game_multiplayer_event_duel_offered
  # Input: arg1 = agent_no
  # Output: none
  ("game_multiplayer_event_duel_offered",
   [
     (store_script_param, ":agent_no", 1),
     (get_player_agent_no, ":player_agent_no"),
     (try_begin),
       (agent_is_active, ":player_agent_no"),
       (this_or_next|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, -1),
       (agent_check_offer_from_agent, ":player_agent_no", ":agent_no"),
       (neg|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, ":agent_no"), #don't allow spamming duel offers during countdown
       (multiplayer_send_int_to_server, multiplayer_event_offer_duel, ":agent_no"),
       (agent_get_player_id, ":player_no", ":agent_no"),
       (try_begin),
         (player_is_active, ":player_no"),
         (str_store_player_username, s0, ":player_no"),
       (else_try),
         (str_store_agent_name, s0, ":agent_no"),
       (try_end),
       (display_message, "str_a_duel_request_is_sent_to_s0"),
     (try_end),
     ]),


  # script_game_get_multiplayer_game_type_enum
  # Input: none
  # Output: reg0:first type, reg1:type count
  ("game_get_multiplayer_game_type_enum",
   [
     (assign, reg0, multiplayer_game_type_deathmatch),
	 (assign, reg1, multiplayer_num_game_types),
	 ]),


  # script_game_multiplayer_get_game_type_mission_template
  # Input: arg1 = game_type
  # Output: mission_template 
  ("game_multiplayer_get_game_type_mission_template",
   [
     (assign, ":selected_mt", -1),
     (store_script_param, ":game_type", 1),
     (try_begin),
       (eq, ":game_type", multiplayer_game_type_deathmatch),
       (assign, ":selected_mt", "mt_multiplayer_dm"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_team_deathmatch),
       (assign, ":selected_mt", "mt_multiplayer_tdm"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_battle),
       (assign, ":selected_mt", "mt_multiplayer_bt"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_destroy),
       (assign, ":selected_mt", "mt_multiplayer_fd"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_capture_the_flag),
       (assign, ":selected_mt", "mt_multiplayer_cf"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_headquarters),
       (assign, ":selected_mt", "mt_multiplayer_hq"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_siege),
       (assign, ":selected_mt", "mt_multiplayer_sg"),
     (else_try),
       (eq, ":game_type", multiplayer_game_type_duel),
       (assign, ":selected_mt", "mt_multiplayer_duel"),
     (try_end),
     (assign, reg0, ":selected_mt"),
     ]),
]