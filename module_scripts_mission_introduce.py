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
from ID_strings import *



####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


scripts_mission_introduce = [

##special scene(used with prsnt)
############################################################################
  #script_infitarte_into_necromancer_hidden_position
  ("character_window",
   [
      (store_script_param, ":showed_troop", 1),

      (modify_visitors_at_site, "scn_character_window_dungon"),
      (reset_visitors),
      (set_visitor, 0, ":showed_troop"),
 
      (set_jump_mission,"mt_character_window"),
      (jump_to_scene,"scn_character_window_dungon"),
      (change_screen_mission),
    ]),


##mission scene
############################################################################

   #script_prepare_alley_to_fight
   (
   "prepare_alley_to_fight",
   [
     (party_get_slot, ":scene_no", "$current_town", slot_town_alley),
     
     #(store_faction_of_party, ":faction_no", "$current_town"),     
     
     (modify_visitors_at_site, ":scene_no"),
     
     (reset_visitors),
     (set_visitor, 0, "trp_player"),
     
     #(try_begin),
     #  (eq, ":faction_no", "fac_kingdom_1"), #swadian
     #  (assign, ":bandit_troop", "trp_steppe_bandit"),
     #(else_try),
     #  (eq, ":faction_no", "fac_kingdom_2"), #vaegir
     #  (assign, ":bandit_troop", "trp_taiga_bandit"),
     #(else_try),
     #  (eq, ":faction_no", "fac_kingdom_3"), #khergit
     #  (assign, ":bandit_troop", "trp_mountain_bandit"),
     #(else_try),
     #  (eq, ":faction_no", "fac_kingdom_4"), #nord
     #  (assign, ":bandit_troop", "trp_abyssal_sailor"),
     #(else_try),
     #  (eq, ":faction_no", "fac_kingdom_5"), #rhodok
     #  (assign, ":bandit_troop", "trp_forest_bandit"),
     #(else_try),
     #  (eq, ":faction_no", "fac_kingdom_6"), #sarradin
     #  (assign, ":bandit_troop", "trp_desert_bandit"),
     #(try_end),  
               
     #(set_visitor, 3, ":bandit_troop"),
     (set_visitor, 3, "trp_cult_follower"),#alley fight

     (assign, "$talked_with_merchant", 0),
     (set_jump_mission, "mt_alley_fight"),
     (jump_to_scene, ":scene_no"),
     (change_screen_mission),         
   ]),


   #script_prepare_town_to_fight
   (
   "prepare_town_to_fight",
   [
     (str_store_party_name_link, s9, "$g_starting_town"),
     (str_store_string, s2, "str_save_town_from_bandits"),        
         (call_script, "script_start_quest", "qst_save_town_from_bandits", "$g_talk_troop"),
  
     (assign, "$g_mt_mode", tcm_default),
     
     (party_get_slot, ":town_scene", "$g_starting_town", slot_town_center),
     (modify_visitors_at_site, ":town_scene"),
     (reset_visitors),
    
     #people spawned at #32, #33, #34, #35, #36, #37, #38 and #39 are town walkers.
     (try_begin),
       #(eq, "$town_nighttime", 0),
       (try_for_range, ":walker_no", 0, num_town_walkers),
         (store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
         (party_get_slot, ":walker_troop_id", "$current_town", ":troop_slot"),
         (gt, ":walker_troop_id", 0),                        
         (store_add, ":entry_no", town_walker_entries_start, ":walker_no"),
         (set_visitor, ":entry_no", ":walker_troop_id"),
       (try_end),  
     (try_end),  

     #guards will be spawned at #25, #26 and #27 
     (set_visitors, 25, "trp_whitesilver_adventurer", 1),
     (set_visitors, 26, "trp_barecopper_adventurer", 1),
     (set_visitors, 27, "trp_blackiron_adventurer", 1),
    
     (set_visitors, 10, "trp_cult_follower", 2),
     (set_visitors, 11, "trp_gold_adventurer", 1),
     (set_visitors, 12, "trp_the_forsaken", 1),    

     (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),    
     (try_begin),
       (eq, ":starting_town_faction", "fac_kingdom_1"),
       (assign, ":troop_of_merchant", "trp_powell_merchant"),
       #(assign, ":troop_of_bandit", "trp_outlaw_swordman"),
     (else_try),  
       (eq, ":starting_town_faction", "fac_kingdom_2"),
       (assign, ":troop_of_merchant", "trp_yishith_merchant"),
       #(assign, ":troop_of_bandit", "trp_cult_follower"),
     (else_try),                   
       (eq, ":starting_town_faction", "fac_kingdom_3"),
       (assign, ":troop_of_merchant", "trp_kouruto_merchant"),
       #(assign, ":troop_of_bandit", "trp_kouruto_refugee_thief"),
     (else_try),  
       (eq, ":starting_town_faction", "fac_kingdom_4"),
       (assign, ":troop_of_merchant", "trp_confederation_merchant"),
       #(assign, ":troop_of_bandit", "trp_ankiya_barbarian"),
     (else_try),  
       (eq, ":starting_town_faction", "fac_kingdom_5"),
       (assign, ":troop_of_merchant", "trp_papal_merchant"),
       #(assign, ":troop_of_bandit", "trp_mountain_bandit"),
     (else_try),  
       (eq, ":starting_town_faction", "fac_kingdom_6"),
       (assign, ":troop_of_merchant", "trp_longshu_merchant"),
       #(assign, ":troop_of_bandit", "trp_bandit"),
     (else_try),  
       (eq, ":starting_town_faction", "fac_kingdom_7"),
       (assign, ":troop_of_merchant", "trp_starkhook_merchant"),
       #(assign, ":troop_of_bandit", "trp_abyssal_sailor"),
     (else_try),  
       (eq, ":starting_town_faction", "fac_kingdom_8"),
       (assign, ":troop_of_merchant", "trp_state_merchant"),
       #(assign, ":troop_of_bandit", "trp_libra_low_member"),
     (try_end),
     (str_store_troop_name, s10, ":troop_of_merchant"),
    
     (set_visitors, 24, "trp_gold_adventurer", 1),
     (set_visitors, 2, "trp_the_forsaken", 2),
     (set_visitors, 4, "trp_the_forsaken", 1),
     (set_visitors, 5, "trp_blackiron_adventurer", 2),
     (set_visitors, 6, "trp_the_forsaken", 1),
     (set_visitors, 7, "trp_fallen_warrior", 1),
    
     (set_visitors, 3, ":troop_of_merchant", 1),    

     (assign, "$merchant_sign_count",0), #time count
    
     (set_jump_mission,"mt_town_fight"),
     (jump_to_scene, ":town_scene"),
     (change_screen_mission),   
   ]),


#use for undead base
   (
   "undead_base_midul",
   [ 
     (modify_visitors_at_site, "scn_undead_base_midul"),
     (reset_visitors),

     (set_visitors, 1, "trp_player", 1),

     (set_visitors, 2, "trp_reception", 1),
     (set_visitors, 3, "trp_apprentice_1", 1),
     (set_visitors, 4, "trp_apprentice_2", 1),
     (set_visitors, 5, "trp_apprentice_3", 1),
     (set_visitors, 6, "trp_assistant_1", 1),
     (set_visitors, 7, "trp_apprentice_4", 1),
     (set_visitors, 8, "trp_apprentice_5", 1),
     (set_visitors, 9, "trp_apprentice_6", 1),
     (set_visitors, 10, "trp_inflammation_necromancer", 1),
     (set_visitors, 11, "trp_cyan_necromancer", 1),
     (set_visitors, 12, "trp_armor_necromancer", 1),
     (set_visitors, 13, "trp_shower_necromancer", 1),
     (set_visitors, 14, "trp_assistant_2", 1),
     (set_visitors, 15, "trp_shattered_necromancer", 1),
     (set_visitors, 16, "trp_element_necromancer", 1),
     (set_visitors, 17, "trp_apprentice_7", 1),
     (set_visitors, 18, "trp_skeleton_heavy_archer", 1),#guard
     (set_visitors, 19, "trp_turbid_necromancer", 1),
     (set_visitors, 20, "trp_apprentice_8", 1),
     (set_visitors, 21, "trp_apprentice_9", 1),
     (set_visitors, 22, "trp_assistant_3", 1),
     (set_visitors, 23, "trp_apprentice_10", 1),
     (set_visitors, 24, "trp_apprentice_11", 1),
     (set_visitors, 25, "trp_zombie_footman", 1),#guard
     (set_visitors, 26, "trp_assistant_4", 1),
     (set_visitors, 27, "trp_assistant_5", 1),
     (set_visitors, 28, "trp_power_necromancer", 1),
     (set_visitors, 29, "trp_shadow_necromancer", 1),
     (set_visitors, 30, "trp_apprentice_12", 1),
     (set_visitors, 31, "trp_apprentice_13", 1),
     (set_visitors, 32, "trp_storm_necromancer", 1),
     (set_visitors, 33, "trp_zombie_swordman", 10),
     (set_visitors, 34, "trp_assistant_6", 1),
     (set_visitors, 35, "trp_defend_necromancer", 1),
     (set_visitors, 36, "trp_assistant_7", 1),
     (set_visitors, 37, "trp_experienced_skeleton", 1),
     (set_visitors, 38, "trp_apprentice_14", 1),
     (set_visitors, 39, "trp_apprentice_15", 1),
     (set_visitors, 40, "trp_assistant_8", 1),
     (set_visitors, 41, "trp_apprentice_16", 1),

     (set_jump_mission,"mt_undead_base_midul"),
     (jump_to_scene, "scn_undead_base_midul"),
     (change_screen_mission),   
   ]),


#cemetery in daytime
   (
   "cemetery_day",
   [ 
     (modify_visitors_at_site, "scn_village_cemetery"),
     (reset_visitors),

     (set_visitors, 1, "trp_player", 1),

     (quest_get_slot, ":giver_troop", "qst_cemetery_travel", slot_quest_giver_troop),
     (set_visitor, 2, ":giver_troop", 1),    

     (set_visitor, 3, "trp_cemetery_watcher", 1),    

     (set_jump_mission,"mt_cemetery_day"),
     (jump_to_scene, "scn_village_cemetery"),
     (change_screen_mission),   
   ]),


#cemetery in nighttime
   (
   "cemetery_night_fight",
   [
     (modify_visitors_at_site, "scn_village_cemetery"),
     (reset_visitors),

     (set_visitor, 1, "trp_player"),    

     (quest_get_slot, ":giver_troop", "qst_cemetery_travel", slot_quest_giver_troop),
     (set_visitor, 2, ":giver_troop", 1),    

     (store_random_in_range, ":entry_point", 4, 9),
     (quest_get_slot, ":object_troop", "qst_cemetery_travel", slot_quest_object_troop),
     (set_visitor, ":entry_point", ":object_troop", 1),    

     (set_jump_mission,"mt_cemetery_night_fight"),
     (jump_to_scene, "scn_village_cemetery"),
     (change_screen_mission),   
   ]),


  # script_cf_enter_center_location_bandit_check
  # Input: none
  # Output: none
  ("cf_enter_center_location_bandit_check",
    [
      (neq, "$town_nighttime", 0),
      (party_slot_ge, "$current_town", slot_center_has_bandits, 1),
      (eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)
      (eq, "$sneaked_into_town", 0),#Skip if sneaked
      (try_begin),
        (party_slot_eq, "$current_town", slot_party_type, spt_village),
        (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),
      (else_try),
        (party_get_slot, ":cur_scene", "$current_town", slot_town_center),
      (try_end),
      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),
      (party_get_slot, ":bandit_troop", "$current_town", slot_center_has_bandits),
      (store_character_level, ":level", "trp_player"),

      (set_jump_mission, "mt_bandits_at_night"),
      (try_begin),
        (party_slot_eq, "$current_town", slot_party_type, spt_village),
        (assign, ":spawn_amount", 2),
        (store_div, ":level_fac",  ":level", 10),
        (val_add, ":spawn_amount", ":level_fac"),
        (try_for_range, ":unused", 0, 3),
          (gt, ":level", 10),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":level"),
          (val_add, ":spawn_amount", 1),
        (try_end),
        (set_visitors, 4, ":bandit_troop", ":spawn_amount"),
        (assign, "$num_center_bandits", ":spawn_amount"),
        (set_jump_entry, 2),
      (else_try),
        (assign, ":spawn_amount", 1),
        (assign, "$num_center_bandits", 0),
        (try_begin),
          (gt, ":level", 15),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":level"),
          (assign, ":spawn_amount", 2),
        (try_end),
        (val_add, "$num_center_bandits",  ":spawn_amount"),
        (set_visitors, 11, ":bandit_troop", ":spawn_amount"),
        (assign, ":spawn_amount", 1),
        (try_begin),
          (gt, ":level", 20),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":level"),
          (assign, ":spawn_amount", 2),
        (try_end),
        (set_visitors, 27, ":bandit_troop", ":spawn_amount"),
        (val_add, "$num_center_bandits",  ":spawn_amount"),
        (try_begin),
          (gt, ":level", 9),
          (assign, ":spawn_amount", 1),
          (try_begin),
            (gt, ":level", 25),
            (store_random_in_range, ":random_no", 0, 100),
            (lt, ":random_no", ":level"),
            (assign, ":spawn_amount", 2),
          (try_end),
          (set_visitors, 28, ":bandit_troop", ":spawn_amount"),
          (val_add, "$num_center_bandits",  ":spawn_amount"),
        (try_end),
        (assign, "$town_entered", 1),
        (assign, "$all_doors_locked", 1),
      (try_end),

      (display_message, "@You have run into a trap!", 0xFFFF2222),
      (display_message, "@You are attacked by a group of bandits!", 0xFFFF2222),

      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),
      ]),


   ("setup_meet_lady",
    [
      (store_script_param_1, ":lady_no"), 
      (store_script_param_2, ":center_no"), 
    
      #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_horse),
      (troop_set_slot, ":lady_no", slot_lady_last_suitor, "trp_player"),
	  
      (set_jump_mission,"mt_visit_town_castle"),
      (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
      (modify_visitors_at_site,":castle_scene"),
      (reset_visitors),

	  (troop_set_age, "trp_nurse_for_lady", 100),
      (set_visitor, 7, "trp_nurse_for_lady"),

      (assign, ":cur_pos", 16),
	  (set_visitor, ":cur_pos", ":lady_no"),

      (assign, "$talk_context", tc_garden),
	  
      (jump_to_scene,":castle_scene"),
      (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
      (change_screen_mission),	  
	]),  


  # script_enter_court
  # Input: arg1 = center_no
  # Output: none
  #other search term: setup_court
  ("enter_court",
    [
      (store_script_param_1, ":center_no"),
      
      (assign, "$talk_context", tc_court_talk),

      (set_jump_mission,"mt_visit_town_castle"),
         
      (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),#entry 0为玩家
      #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_all),
      
      (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
      (modify_visitors_at_site,":castle_scene"),
      (reset_visitors),
      #Adding guards
      (store_faction_of_party, ":center_faction", ":center_no"),
      (faction_get_slot, ":center_culture", ":center_faction", slot_faction_culture), #获取文化
      (item_get_slot, ":guard_troop", ":center_culture", slot_culture_guard_troop),
      (try_begin),
         (le, ":guard_troop", 0),
         (assign, ":guard_troop", "trp_blackguard_mercenary"),#如果没有指定守卫，则默认设置为无赖佣兵
      (try_end),
      (set_visitor, 6, ":guard_troop"),#entry 6、7号为守卫
      (set_visitor, 7, ":guard_troop"),

      (assign, ":cur_pos", 16),

      (try_begin),
         (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),#玩家配偶
         (gt, ":player_spouse", 0),
         (troop_slot_eq, ":player_spouse", slot_troop_cur_center, ":center_no"),
         (set_visitor, ":cur_pos", ":player_spouse"),
         (val_add,":cur_pos", 1),
      (else_try),	
         (troop_get_slot, ":player_betrothed", "trp_player", slot_troop_betrothed),#未婚妻
         (gt, ":player_betrothed", 0),
         (troop_slot_eq, ":player_betrothed", slot_troop_cur_center, ":center_no"),
         (set_visitor, ":cur_pos", ":player_betrothed"),
         (val_add,":cur_pos", 1),
      (try_end),
	  
      (try_begin),
         (eq, "$g_player_court", ":center_no"),
         (gt, "$g_player_minister", 0),
         (neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_player_minister"),#玩家大臣
         (set_visitor, ":cur_pos", "$g_player_minister"),
         (val_add,":cur_pos", 1),
      (try_end),	  
	  
        #Lords wishing to pledge allegiance - inactive, but part of player faction
      (try_begin),                                                                                                               #希望被玩家分封的无地领主，等在玩家宫廷里
         (eq, "$g_player_court", ":center_no"), 
         (faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"), 
         (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", "fac_player_supporters_faction"),
            (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
            (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
            (neq, ":active_npc", "$g_player_minister"),
            (set_visitor, ":cur_pos", ":active_npc"),	      
            (val_add,":cur_pos", 1),
         (try_end),
      (try_end),	  
	  
      (call_script, "script_get_heroes_attached_to_center", ":center_no", "p_temp_party"),#在城中休息的部队中的hero单位，包括领主和玩家的伙伴npc
      (party_get_num_companion_stacks, ":num_stacks","p_temp_party"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),
         (lt, ":cur_pos", 32), # spawn up to entry point 32 - is it possible to add another 10 spots?
         (set_visitor, ":cur_pos", ":stack_troop"),
         (val_add,":cur_pos", 1),
      (try_end),

      (try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),#领主女眷
         (neq, ":cur_troop", "trp_knight_relatives_begin"), #The one who should not appear in game
        #(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
         (troop_slot_eq, ":cur_troop", slot_troop_cur_center, ":center_no"),
		
		(assign, ":lady_meets_visitors", 0),
		(try_begin),
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":cur_troop"), #player spouse goes in position of honor
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_betrothed, ":cur_troop"), #player spouse goes in position of honor
			(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_spouse, "trp_player"), #player spouse goes in position of honor
				(troop_slot_eq, ":cur_troop", slot_troop_betrothed, "trp_player"),
				
			(assign, ":lady_meets_visitors", 0), #She is already in the place of honor
		
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":cur_troop"),
				(display_message, "str_s4_is_present_at_the_center_and_in_place_of_honor"),
			(try_end),
		
		(else_try), #lady is troop
			(store_faction_of_troop, ":lady_faction", ":cur_troop"),
			(neq, ":lady_faction", ":center_faction"),
			
			(assign, ":lady_meets_visitors", 1),
			
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":cur_troop"),
				(display_message, "str_s4_is_present_at_the_center_as_a_refugee"),
			(try_end),

		(else_try),
			(troop_slot_ge, ":cur_troop", slot_troop_spouse, 1),
			
			(try_begin),
			 #married ladies at a feast will not mingle - this is ahistorical, as married women and widows probably had much more freedom than unmarried ones, at least in the West, but the game needs to leave slots for them to show off their unmarried daughters
				(faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
				(faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
				(assign, ":lady_meets_visitors", 0),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "str_s4_is_present_at_the_center_and_not_attending_the_feast"),
				(try_end),				
			(else_try),
				(assign, ":lady_meets_visitors", 1),
				
				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "str_s4_is_present_at_the_center_and_is_married"),
				(try_end),				
			(try_end),
			
		(else_try), #feast is in progress			
			(faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
			(faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
			(assign, ":lady_meets_visitors", 1),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":cur_troop"),
				(display_message, "@{!}DEBUG -- {s4} is present at the center and is attending the feast"),
			(try_end),
						
		(else_try), #already met - awaits in private
			(troop_slot_ge, ":cur_troop", slot_troop_met, 2),
			(assign, ":lady_meets_visitors", 0),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":cur_troop"),
				(display_message, "@{!}DEBUG -- {s4} is present at the center and is awaiting the player in private"),
			(try_end),
			
		(else_try),	
			(call_script, "script_get_kingdom_lady_social_determinants", ":cur_troop"),
			(call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", reg0, "trp_player"),
			(gt, reg0, 0),
			(assign, ":lady_meets_visitors", 1),
			
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":cur_troop"),
				(display_message, "@{!}DEBUG -- {s4} is_present_at_the_center_and_is_allowed_to_meet_the_player"),
			(try_end),
			
		(else_try),	
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, s4, ":cur_troop"),
				(display_message, "@{!}DEBUG -- {s4}is_present_at_the_center_and_is_not_allowed_to_meet_the_player"),
			(try_end),
		
		(try_end),				

		(eq, ":lady_meets_visitors", 1),
		
        (lt, ":cur_pos", 32), # spawn up to entry point 32
        (set_visitor, ":cur_pos", ":cur_troop"),
        (val_add,":cur_pos", 1),
      (try_end),

      (try_begin),
         (eq, ":center_no", "p_castle_1_18"),#鲁克斯领
         (set_visitor, ":cur_pos", "trp_lance_protector_francois_beaumont"),#护枪官弗朗索瓦·博蒙
         (val_add,":cur_pos", 1),
      (try_end),
      
      (set_jump_entry, 0),
      
      (jump_to_scene,":castle_scene"),
      (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
      (change_screen_mission),
  ]),


  # script_enter_dungeon
  # Input: arg1 = center_no, arg2 = mission_template_no
  # Output: none
  ("enter_dungeon",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":mission_template_no"),
      
      (set_jump_mission,":mission_template_no"),
      #new added...
      (mission_tpl_entry_set_override_flags, ":mission_template_no", 0, af_override_horse),
      (try_begin),
        (eq, "$sneaked_into_town", 1),
        (mission_tpl_entry_set_override_flags, ":mission_template_no", 0, af_override_all),                
        
        (mission_tpl_entry_clear_override_items, ":mission_template_no", 0),
        (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_pilgrim_hood"),
        (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_pilgrim_disguise"),
        (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_practice_staff"),
        (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_throwing_daggers"),
      (try_end),   
      #new added end              

      (party_get_slot, ":dungeon_scene", ":center_no", slot_town_prison),
      
      (modify_visitors_at_site,":dungeon_scene"),
      (reset_visitors),
      (assign, ":cur_pos", 16),
	  
	  
      (call_script, "script_get_heroes_attached_to_center_as_prisoner", ":center_no", "p_temp_party"),
      (party_get_num_companion_stacks, ":num_stacks","p_temp_party"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),

		(assign, ":prisoner_offered_parole", 0),
		(try_begin),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
		(else_try),
			(call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
			(assign, ":prisoner_offered_parole", 1),
		(else_try),
			(assign, ":prisoner_offered_parole", 0),
		(try_end),
		(eq, ":prisoner_offered_parole", 0),
		
        (lt, ":cur_pos", 32), # spawn up to entry point 32
        (set_visitor, ":cur_pos", ":stack_troop"),
        (val_add,":cur_pos", 1),
      (try_end),
      	 
#	  (set_visitor, ":cur_pos", "trp_npc3"),
#	  (troop_set_slot, "trp_npc3", slot_troop_prisoner_of_party, "$g_encountered_party"),	  
	  
      (set_jump_entry, 0),
      (jump_to_scene,":dungeon_scene"),
      (scene_set_slot, ":dungeon_scene", slot_scene_visited, 1),
      (change_screen_mission),
  ]),


  #script_start_training_at_training_ground
  # INPUT:
  # param1: training_weapon_type, param2: training_param
  ("start_training_at_training_ground",
   [
     (val_add, "$g_training_ground_training_count", 1),
     (store_script_param, ":mission_weapon_type", 1),
     (store_script_param, ":training_param", 2),

     (set_jump_mission, "mt_training_ground_training"),

     (assign, ":training_default_weapon_1", -1),
     (assign, ":training_default_weapon_2", -1),
     (assign, ":training_default_weapon_3", -1),
     (assign, "$scene_num_total_gourds_destroyed", 0),
     (try_begin),
       (eq, ":mission_weapon_type", itp_type_bow),
       (assign, "$g_training_ground_used_weapon_proficiency", wpt_archery),
       (assign, ":training_default_weapon_1", "itm_practice_bow"),
       (try_begin),
         (eq, "$g_mt_mode", ctm_mounted),
         (assign, ":training_default_weapon_2", "itm_practice_arrows_100_amount"),
       (else_try),
         (assign, ":training_default_weapon_2", "itm_practice_arrows_10_amount"),
       (try_end),
     (else_try),
       (eq, ":mission_weapon_type", itp_type_crossbow),
       (assign, "$g_training_ground_used_weapon_proficiency", wpt_crossbow),
       (assign, ":training_default_weapon_1", "itm_practice_crossbow"),
       (assign, ":training_default_weapon_2", "itm_practice_bolts_9_amount"),
     (else_try),
       (eq, ":mission_weapon_type", itp_type_thrown),
       (assign, "$g_training_ground_used_weapon_proficiency", wpt_throwing),
       (try_begin),
         (eq, "$g_mt_mode", ctm_mounted),
         (assign, ":training_default_weapon_2", "itm_practice_throwing_daggers_100_amount"),
       (else_try),
         (assign, ":training_default_weapon_2", "itm_practice_throwing_daggers"),
       (try_end),
     (else_try),
       (eq, ":mission_weapon_type", itp_type_one_handed_wpn),
       (assign, "$g_training_ground_used_weapon_proficiency", wpt_one_handed_weapon),
       (assign, ":training_default_weapon_1", "itm_practice_sword"),
     (else_try),
       (eq, ":mission_weapon_type", itp_type_polearm),
       (assign, "$g_training_ground_used_weapon_proficiency", wpt_polearm),
       (assign, ":training_default_weapon_1", "itm_practice_lance"),
     (else_try),
       #weapon_type comes as -1 when melee training is selected
       (assign, "$g_training_ground_used_weapon_proficiency", wpt_one_handed_weapon),
       (call_script, "script_get_random_melee_training_weapon"),
       (assign, ":training_default_weapon_1", reg0),
       (assign, ":training_default_weapon_2", reg1),
     (try_end),
     
##     (assign, "$g_training_ground_training_troop_stack_index", ":stack_index"),
     (try_begin),
       (eq, "$g_mt_mode", ctm_mounted),
       (assign, ":training_default_weapon_3", "itm_practice_horse"),
       (store_add, "$g_training_ground_training_scene", "scn_training_ground_horse_track_1", "$g_encountered_party"),
       (val_sub, "$g_training_ground_training_scene", training_grounds_begin),
     (else_try),
       (store_add, "$g_training_ground_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
       (val_sub, "$g_training_ground_training_scene", training_grounds_begin),
     (try_end),

     (modify_visitors_at_site, "$g_training_ground_training_scene"),
     (reset_visitors),
     (set_visitor, 0, "trp_player"),

     (assign, ":selected_weapon", -1),
     (try_for_range, ":cur_slot", 0, 4),#equipment slots
       (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
       (ge, ":cur_item", 0),
       (item_get_type, ":item_type", ":cur_item"),
       (try_begin),
         (eq, ":item_type", ":mission_weapon_type"),
         (eq, ":selected_weapon", -1),
         (assign, ":selected_weapon", ":cur_item"),
       (try_end),
     (try_end),
     (mission_tpl_entry_clear_override_items, "mt_training_ground_training", 0),
     (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, "itm_practice_boots"),
     (try_begin),
       (ge, ":training_default_weapon_1", 0),
       (try_begin),
         (ge, ":selected_weapon", 0),
         (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":selected_weapon"),
       (else_try),
         (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_1"),
       (try_end),
     (try_end),
     (try_begin),
       (ge, ":training_default_weapon_2", 0),
       (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_2"),
     (try_end),
     (try_begin),
       (ge, ":training_default_weapon_3", 0),
       (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_3"),
     (try_end),

     (assign, ":cur_visitor_point", 5),
     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
     (store_add, ":end_cond", 5, ":num_fit"),
     (val_min, ":end_cond", 13),
     (try_for_range, ":cur_visitor_point", 5, ":end_cond"),
       (call_script, "script_remove_random_fit_party_member_from_stack_selection"),
       (set_visitor, ":cur_visitor_point", reg0),
       (val_add, ":cur_visitor_point", 1),
     (try_end),
     (try_begin),
       (eq, "$g_mt_mode", ctm_melee),
       (assign, ":total_difficulty", 0),
       (try_for_range, ":i", 0, ":training_param"),
         (troop_get_slot, ":cur_troop", "trp_temp_array_a", ":i"),
         (store_add, ":cur_entry_point", ":i", 1),
         (set_visitor, ":cur_entry_point", ":cur_troop"),
         (mission_tpl_entry_clear_override_items, "mt_training_ground_training", ":cur_entry_point"),
         (mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", "itm_practice_boots"),
         (call_script, "script_get_random_melee_training_weapon"),
         (mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", reg0),
         (try_begin),
           (ge, reg1, 0),
           (mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", reg1),
         (try_end),
         (store_character_level, ":cur_troop_level", ":cur_troop"),
         (val_add, ":cur_troop_level", 10),
         (val_mul, ":cur_troop_level", ":cur_troop_level"),
         (val_add, ":total_difficulty", ":cur_troop_level"),
       (try_end),

       (assign, "$g_training_ground_training_num_enemies", ":training_param"),
       (assign, "$g_training_ground_training_hardness",  ":total_difficulty"),
       (store_add, ":number_multiplier", "$g_training_ground_training_num_enemies", 4),
       (val_mul, "$g_training_ground_training_hardness", ":number_multiplier"),
       (val_div, "$g_training_ground_training_hardness", 2400),
       (str_store_string, s0, "@Your opponents are ready for the fight."),
     (else_try),
       (eq, "$g_mt_mode", ctm_mounted),
       (try_begin),
         (eq, ":mission_weapon_type", itp_type_bow),
         (assign, "$g_training_ground_training_hardness", 350),
         (assign, "$g_training_ground_training_num_gourds_to_destroy", 30),
       (else_try),
         (eq, ":mission_weapon_type", itp_type_thrown),
         (assign, "$g_training_ground_training_hardness", 400),
         (assign, "$g_training_ground_training_num_gourds_to_destroy", 30),
       (else_try),
         (eq, ":mission_weapon_type", itp_type_one_handed_wpn),
         (assign, "$g_training_ground_training_hardness", 200),
         (assign, "$g_training_ground_training_num_gourds_to_destroy", 45),
       (else_try),
         (eq, ":mission_weapon_type", itp_type_polearm),
         (assign, "$g_training_ground_training_hardness", 280),
         (assign, "$g_training_ground_training_num_gourds_to_destroy", 35),
       (try_end),
       (str_store_string, s0, "@Try to destroy as many targets as you can. You have two and a half minutes to clear the track."),
     (else_try),
       (eq, "$g_mt_mode", ctm_ranged),
       (store_mul, "$g_training_ground_ranged_distance", ":training_param", 100),
       (assign, ":hardness_modifier", ":training_param"),
       (val_mul, ":hardness_modifier", ":hardness_modifier"),
       (try_begin),
         (eq, ":mission_weapon_type", itp_type_bow),
         (val_mul, ":hardness_modifier", 3),
         (val_div, ":hardness_modifier", 2),
       (else_try),
         (eq, ":mission_weapon_type", itp_type_thrown),
         (val_mul, ":hardness_modifier", 5),
         (val_div, ":hardness_modifier", 2),
         (val_mul, ":hardness_modifier", ":training_param"),
         (val_div, ":hardness_modifier", 2),
       (try_end),
       (store_mul, "$g_training_ground_training_hardness", 100, ":hardness_modifier"),
       (val_div, "$g_training_ground_training_hardness", 6000),
       (str_store_string, s0, "@Stay behind the line on the ground and shoot the targets. Try not to waste any shots."),
     (try_end),
     (jump_to_menu, "mnu_training_ground_description"),
     ]),


  #在大地图上遇到部队后对话
  #script_setup_party_meeting:
  # INPUT:
  # param1: Party-id with which meeting will be made.
  ("setup_party_meeting",
    [
      (store_script_param_1, ":meeting_party"),
#      (try_begin),
#        (lt, "$g_encountered_party_relation", 0), #hostile
#        (call_script, "script_music_set_situation_with_culture", mtf_sit_encounter_hostile),
#      (try_end),
      (call_script, "script_get_meeting_scene"), #确定对话场景
      (assign, ":meeting_scene", reg0),
      (modify_visitors_at_site, ":meeting_scene"),
      (reset_visitors),
      (set_visitor, 0, "trp_player"), #玩家入口

      (try_begin), #获取对话者
         (party_slot_eq, ":meeting_party", slot_party_type, spt_kingdom_hero_party), #领主部队，当玩家声望、等级和地位较低时，领主不会亲自来见，而是派出信使
         (store_faction_of_party, ":party_faction", ":meeting_party"),
         (neq, ":party_faction", "$players_kingdom"), #不是玩家自己人
         (party_get_num_companions, ":party_size", ":meeting_party"),#人数超过500
         (gt, ":party_size", 500),
         (faction_get_slot, ":party_culture", ":party_faction", slot_faction_culture), #获取文化
         (gt, ":party_culture", 0),
         (item_get_slot, ":meeting_troop", ":party_culture", slot_culture_messenger_troop),
         (gt, ":meeting_troop", 0),
         (assign, ":troop_dna", 0),
      (else_try),
         (party_stack_get_troop_id, ":meeting_troop", ":meeting_party", 0),
         (party_stack_get_troop_dna, ":troop_dna", ":meeting_party", 0),
      (try_end),
      (set_visitor,17,":meeting_troop",":troop_dna"),
      (set_jump_mission,"mt_conversation_encounter"),
      (jump_to_scene,":meeting_scene"),
      (change_screen_map_conversation, ":meeting_troop"),
  ]),


  #script_setup_troop_meeting:
  # INPUT:
  # param1: troop_id with which meeting will be made.
  # param2: troop_dna (optional)
  ("setup_troop_meeting",
    [
      (store_script_param_1, ":meeting_troop"),
      (store_script_param_2, ":troop_dna"),
      (call_script, "script_get_meeting_scene"), 
      (assign, ":meeting_scene", reg0),
      (modify_visitors_at_site,":meeting_scene"),
      (reset_visitors),
      (set_visitor,0,"trp_player"),
	  (try_begin),
		(gt, ":troop_dna", -1),
        (set_visitor,17,":meeting_troop",":troop_dna"),
	  (else_try),
        (set_visitor,17,":meeting_troop"),
	  (try_end),	
      (set_jump_mission,"mt_conversation_encounter"),
      (jump_to_scene,":meeting_scene"),
      (change_screen_map_conversation, ":meeting_troop"),
  ]),


  #script_start_wedding_cutscene
  # INPUT: arg1 = groom_troop, arg2 = bride_troop
  # OUTPUT: none
  ("start_wedding_cutscene",
   [
     (store_script_param, "$g_wedding_groom_troop", 1),
     (store_script_param, "$g_wedding_bride_troop", 2),

     (assign, "$g_wedding_bishop_troop", "trp_temporary_minister"),
     (try_begin),
       (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
       (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_wedding_groom_troop"),
       (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_wedding_bride_troop"),
       (faction_get_slot, ":players_king", "$players_kingdom", slot_faction_leader),
       (troop_get_type, ":troop_type", ":players_king"),
       (eq, ":troop_type", 0), #male
       (neq, ":players_king", "$g_wedding_groom_troop"),
       (assign, "$g_wedding_bishop_troop", ":players_king"),
     (else_try),
       (eq, "$players_kingdom", "fac_player_supporters_faction"),
       (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
       (gt, "$g_player_minister", 0),
       (troop_get_type, ":troop_type", "$g_player_minister"),
       (eq, ":troop_type", 0), #male
       (neq, "$g_player_minister", "$g_wedding_groom_troop"),
       (assign, "$g_wedding_bishop_troop", "$g_player_minister"),
     (try_end),

     (assign, "$g_wedding_brides_dad_troop", "trp_temporary_minister"),
     (try_begin),
       (neq, "$g_wedding_bride_troop", "trp_player"),
       (try_begin),
         (troop_get_slot, ":father", "$g_wedding_bride_troop", slot_troop_father),
         (gt, ":father", 0),
         (troop_get_type, ":troop_type", ":father"), #just to make sure
         (eq, ":troop_type", 0), #male
         (neq, ":father", "$g_wedding_groom_troop"), #this might be 0 due to an error
         (neq, ":father", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":father"),
       (else_try),
         (troop_get_slot, ":guardian", "$g_wedding_bride_troop", slot_troop_guardian),
         (gt, ":guardian", 0),
         (troop_get_type, ":troop_type", ":guardian"), #just to make sure
         (eq, ":troop_type", 0), #male
         (neq, ":guardian", "$g_wedding_groom_troop"), #this might be 0 due to an error
         (neq, ":guardian", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":guardian"),
       (try_end),
     (else_try),
       (try_for_range, ":cur_companion", companions_begin, companions_end),
         (this_or_next|troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_player_companion),
         (troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_type, ":troop_type", ":cur_companion"), #just to make sure
         (eq, ":troop_type", 0), #male
         (neq, ":cur_companion", "$g_wedding_groom_troop"),
         (neq, ":cur_companion", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":cur_companion"),
       (try_end),
     (try_end),

     (modify_visitors_at_site,"scn_wedding"),
     (reset_visitors,0),
     (set_visitor, 0, "$g_wedding_groom_troop"),
     (set_visitor, 1, "$g_wedding_bride_troop"),
     (set_visitor, 2, "$g_wedding_brides_dad_troop"),
     (set_visitor, 3, "$g_wedding_bishop_troop"),
     (assign, ":num_visitors", 4),
     (assign, ":num_male_visitors", 0),
     (try_for_range, ":cur_npc", active_npcs_begin, kingdom_ladies_end),
       (lt, ":num_visitors", 32),
       (neq, ":cur_npc", "$g_wedding_groom_troop"),
       (neq, ":cur_npc", "$g_wedding_bride_troop"),
       (neq, ":cur_npc", "$g_wedding_brides_dad_troop"),
       (neq, ":cur_npc", "$g_wedding_bishop_troop"),
       (store_troop_faction, ":npc_faction", ":cur_npc"),
       (is_between, ":npc_faction", kingdoms_begin, kingdoms_end),
       (eq, ":npc_faction", "$players_kingdom"),
       (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_player_companion),
       (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_hero),
       (troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_lady),
       (troop_get_type, ":troop_type", ":cur_npc"),
       (assign, ":continue_adding", 1),
       (try_begin),
         (eq, ":troop_type", 0),
         (assign, ":continue_adding", 0),
         (lt, ":num_male_visitors", 16), #limit number of male visitors
         (assign, ":continue_adding", 1),
         (val_add, ":num_male_visitors", 1),
       (try_end),
       (eq, ":continue_adding", 1),
       (set_visitor, ":num_visitors", ":cur_npc"),
       (val_add, ":num_visitors", 1),
     (try_end),
     (set_jump_mission,"mt_wedding"),
     (jump_to_scene,"scn_wedding"),
     (change_screen_mission),
    ]),


  #script_infitarte_into_necromancer_hidden_position
  ("infitarte_into_necromancer_hidden_position",
   [
      (modify_visitors_at_site, "scn_necromancer_hidden_position"),
      (reset_visitors),
      (set_visitor, 0, "trp_player"),

      (quest_get_slot, ":object_troop", "qst_destroy_results", slot_quest_object_troop),
      (set_visitor, 33, ":object_troop"),

#      (quest_get_slot, ":target_troop", "qst_destroy_results", slot_quest_target_troop),
#      (troop_get_slot, ":clique_no",":target_troop", slot_troop_necromancer_clique),
#      (try_begin),
#         (eq, ":clique_no", 1),#zombie
         (set_visitor, 2, "trp_zombie_swordman"),#standing sentry
         (set_visitor, 3, "trp_zombie_lancer"),#patrol sentry
         (set_visitor, 6, "trp_zombie_destroyer"),#patrol sentry
         (set_visitor, 10, "trp_zombie_lancer"),#patrol sentry
         (set_visitor, 12, "trp_zombie_footman"),#standing sentry
         (set_visitor, 13, "trp_zombie_footman"),#standing sentry
         (set_visitor, 14, "trp_zombie_footman"),#standing sentry
         (set_visitor, 15, "trp_zombie_swordman"),#standing sentry
         (set_visitor, 16, "trp_zombie_lancer"),#standing sentry
         (set_visitor, 17, "trp_zombie_footman"),#standing sentry
         (set_visitor, 18, "trp_zombie_swordman"),#standing sentry
         (set_visitor, 19, "trp_zombie_swordman"),#patrol sentry
         (set_visitor, 21, "trp_zombie_lancer"),#standing sentry
         (set_visitor, 22, "trp_zombie_footman"),#standing sentry
         (set_visitor, 25, "trp_zombie_footman"),#standing sentry
         (set_visitor, 27, "trp_zombie_footman"),#patrol sentry
         (set_visitor, 28, "trp_zombie_footman"),#patrol sentry
         (set_visitor, 29, "trp_zombie_swordman"),#patrol sentry
         (set_visitor, 30, "trp_zombie_archer"),#patrol sentry
         (set_visitor, 40, "trp_zombie_swordman"),#patrol sentry
         (set_visitor, 42, "trp_zombie_footman"),#standing sentry
         (set_visitor, 43, "trp_zombie_footman"),#patrol sentry
         (set_visitor, 46, "trp_zombie_footman"),#standing sentry
         (set_visitor, 47, "trp_undead_gladiatus"),#standing sentry
#      (else_try),
#         (eq, ":clique_no", 2),#skeleton
#      (try_end),

      #Storing which visitor is standing sentry, will be called immediately when mission begin.
      (try_for_range, ":count_no", 0, 200),
         (troop_set_slot, "trp_temp_array_inflitration_sentry", ":count_no", -1),#清空
      (try_end),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 2, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 12, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 13, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 14, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 15, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 16, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 17, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 18, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 21, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 22, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 25, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 42, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 46, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 47, 1),

      (troop_set_slot, "trp_temp_array_inflitration_sentry", 3, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 6, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 10, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 19, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 20, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 27, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 28, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 40, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 43, 2),
 
      (set_jump_mission,"mt_infiltrate_necromancer_hidden_position"),
      (jump_to_scene,"scn_necromancer_hidden_position"),
      (change_screen_mission),
    ]),


#遭遇抢劫（用于随机事件）
  ("random_event_center_bandit",
    [
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),
      (else_try),
         (party_get_slot, ":cur_scene", "$current_town", slot_town_center),
      (try_end),

      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (set_visitors, 4, "trp_looter", 3),
         (set_jump_entry, 2),
      (else_try),
         (set_visitors, 11, "trp_looter", 1),
         (set_visitors, 27, "trp_looter", 1),
         (set_visitors, 28, "trp_looter", 1),
         (assign, "$all_doors_locked", 1),
      (try_end),

      (display_message, "@You are attacked by a group of bandits!", 0xFFFF2222),
      (set_jump_mission, "mt_bandits_at_night"),
      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),
      ]),


#遭遇刺杀（用于随机事件）
  ("random_event_center_assassin",
    [
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),
      (else_try),
         (party_get_slot, ":cur_scene", "$current_town", slot_town_center),
      (try_end),

      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (set_visitors, 4, "trp_professional_assassin", 1),
         (set_jump_entry, 2),
      (else_try),
         (set_visitors, 28, "trp_professional_assassin", 1),
         (assign, "$all_doors_locked", 1),
      (try_end),

      (display_message, "@You have run into a trap!", 0xFFFF2222),
      (set_jump_mission, "mt_bandits_at_night"),
      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),
      ]),


#发现丑闻（用于随机事件）
  ("random_event_discover_scandal",
    [
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),
      (else_try),
         (party_get_slot, ":cur_scene", "$current_town", slot_town_center),
      (try_end),

      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (set_visitors, 4, "trp_libra_guard", 2),
         (set_jump_entry, 2),
      (else_try),
         (set_visitors, 27, "trp_libra_guard", 1),
         (set_visitors, 28, "trp_libra_guard", 1),
         (assign, "$all_doors_locked", 1),
      (try_end),

      (set_jump_mission, "mt_bandits_at_night"),
      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),
      ]),


#贵族被刺杀（用于随机事件）
  ("random_event_noble_assassinated",
    [
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),
      (else_try),
         (party_get_slot, ":cur_scene", "$current_town", slot_town_center),
      (try_end),

      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),
      (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
         (set_visitors, 4, "trp_alley_hunter", 1),
         (set_jump_entry, 2),
      (else_try),
         (set_visitors, 28, "trp_alley_hunter", 1),
         (assign, "$all_doors_locked", 1),
      (try_end),

      (set_jump_mission, "mt_bandits_at_night"),
      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),
      ]),


#挑战赛（用于随机事件）
  ("random_event_competition",
    [
      (party_get_slot, ":cur_scene", "$current_town", slot_town_arena), 
      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),
      (set_visitor, 32, "trp_player"),
      (set_visitors, 34, "$temp", 1),
      (set_jump_mission, "mt_common_competition"),
      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),
      ]),


#小型据点场景自动设置人员
#1号固定为玩家刷新位置，2号为剧情特殊位置，不用，3号为势力首领刷新位置，后续4到10位置如果有其余剧情人物则顺延刷新，没有则刷新该势力兵种
  ("scene_auto_visitor",
   [
      (store_script_param, ":scene_no", 1),
      (store_script_param, ":item_faction_no", 2),#所属势力
      (store_script_param, ":visitor_limit", 3),#刷新点数量限制
      (modify_visitors_at_site, ":scene_no"),
      (reset_visitors),
      (set_visitor, 1, "trp_player"),#一号玩家入口

      (try_begin),#3号为势力首领
         (call_script, "script_faction_leader_check", ":item_faction_no"),
         (eq, reg2, 1),#首领是兵种
         (set_visitor, 3, reg1),
      (try_end),

      (assign, ":visitor_no", 4),#4号往后先刷新成员
      (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),
         (troop_is_hero, ":count_no"),
         (call_script, "script_get_faction_affiliation", ":count_no", 1),
         (eq, reg1, ":item_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 1),
         (is_between, reg1, 0, 2),#支柱或一般成员
         (set_visitor, ":visitor_no", ":count_no"),
         (val_add, ":visitor_no", 1),
      (try_end),

      (try_for_range, ":count_no", 1, 200),
         (troop_set_slot, "trp_temp_array_a", ":count_no", -1),#清空
      (try_end),
      (assign, reg3, 1),#计算总数
      (call_script, "script_get_scene_random_troop", ":item_faction_no", 40),#获取可用兵种，最高四十级
      (val_add, ":visitor_limit", 1),
      (try_for_range, ":entry_no", ":visitor_no", ":visitor_limit"),#剩余刷新点用小兵填满
         (store_random_in_range, ":count_no_2", 1, reg3),
         (troop_get_slot, ":cur_troop_no", "trp_temp_array_a", ":count_no_2"),
         (gt, ":cur_troop_no", 1),#以防没取到兵种
         (set_visitor, ":entry_no", ":cur_troop_no"),
      (try_end),
 
      (set_jump_mission,"mt_normal_building_enter"),
      (jump_to_scene, ":scene_no"),
      (change_screen_mission),
    ]),





###################################################新剧情####################################################
#新手剧情：港口潜入
  ("infitarte_into_libra_smuggle_wharf",
   [
      (modify_visitors_at_site, "scn_libra_smuggle_wharf"),
      (reset_visitors),
      (set_visitor, 1, "trp_player"),

      (set_visitor, 2, "trp_thug"),
      (set_visitor, 3, "trp_libra_slave_merchant"),
      (set_visitor, 4, "trp_libra_drug_dealer"),
      (set_visitor, 5, "trp_libra_smuggler"),
      (set_visitor, 7, "trp_thug"),
      (set_visitor, 11, "trp_watchman"),
      (set_visitor, 13, "trp_libra_smuggler"),
      (set_visitor, 14, "trp_blackguard_mercenary"),
      (set_visitor, 17, "trp_thug"),
      (set_visitor, 18, "trp_libra_smuggler"),
      (set_visitor, 19, "trp_libra_smuggler"),
      (set_visitor, 20, "trp_thug"),
      (set_visitor, 21, "trp_libra_smuggler"),
      (set_visitor, 22, "trp_thug"),
      (set_visitor, 25, "trp_thug"),

      #Storing which visitor is standing sentry, will be called immediately when mission begin.
      (try_for_range, ":count_no", 0, 200),
         (troop_set_slot, "trp_temp_array_inflitration_sentry", ":count_no", -1),#清空
      (try_end),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 2, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 3, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 4, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 5, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 13, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 17, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 18, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 19, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 20, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 21, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 25, 1),

      (troop_set_slot, "trp_temp_array_inflitration_sentry", 7, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 11, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 14, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 22, 2),
 
      (troop_clear_inventory, "trp_plot_chest_1"),
      (try_begin),
         (eq, "$current_startup_quest_phase", 2),
         (troop_add_item, "trp_plot_chest_1", "itm_jinse_changjian", imod_masterwork),#宝箱
      (try_end),
      (assign, "$total_patrol_entry", 25),#前25个entry之间巡逻
      (set_jump_mission,"mt_libra_smuggle_wharf"),
      (jump_to_scene,"scn_libra_smuggle_wharf"),
      (change_screen_mission),
    ]),

#新手剧情：勒塞夫街头观摩公开处刑
  ("lesaff_street_execution",
   [
      (modify_visitors_at_site, "scn_lesaff_square"),
      (reset_visitors),
      (set_visitor, 1, "trp_player"),
 
      (troop_clear_inventory, "trp_plot_chest_1"),#宝箱
      (set_jump_mission,"mt_lesaff_street_execution"),
      (jump_to_scene,"scn_lesaff_square"),
      (change_screen_mission),
    ]),

#新手剧情：进入权厄之秤据点
  ("lesaff_underworld_stronghold",
   [
      (modify_visitors_at_site, "scn_underworld_stronghold_1"),
      (reset_visitors),
      (set_visitor, 1, "trp_player"),#一号玩家入口
      (set_visitor, 2, "trp_anne_laure_deschamps"),#二号据点首领刷新点
      (set_visitor, 4, "trp_thug"),
      (set_visitor, 5, "trp_libra_hitman"),
      (set_visitor, 6, "trp_libra_guard"),
      (set_visitor, 7, "trp_libra_spy"),
      (set_visitor, 8, "trp_libra_smuggler"),
      (set_visitor, 9, "trp_libra_drug_muscleman"),
      (set_visitor, 10, "trp_libra_slave_catching_cavalry"),
 
      (set_jump_mission,"mt_lesaff_underworld_stronghold"),
      (jump_to_scene,"scn_underworld_stronghold_1"),
      (change_screen_mission),
    ]),


#新手剧情：第二次港口潜入
  ("infitarte_into_libra_smuggle_wharf_2",
   [
      (modify_visitors_at_site, "scn_libra_smuggle_wharf"),
      (reset_visitors),
      (set_visitor, 0, "trp_player"),

      (set_visitor, 2, "trp_thug"),
      (set_visitor, 3, "trp_libra_slave_merchant"),
      (set_visitor, 4, "trp_libra_drug_dealer"),
      (set_visitor, 5, "trp_libra_smuggler"),
      (set_visitor, 7, "trp_thug"),
      (set_visitor, 11, "trp_watchman"),
      (set_visitor, 13, "trp_libra_smuggler"),
      (set_visitor, 14, "trp_blackguard_mercenary"),
      (set_visitor, 17, "trp_thug"),
      (set_visitor, 18, "trp_libra_smuggler"),
      (set_visitor, 19, "trp_libra_smuggler"),
      (set_visitor, 20, "trp_thug"),
      (set_visitor, 21, "trp_libra_smuggler"),
      (set_visitor, 22, "trp_thug"),

      #Storing which visitor is standing sentry, will be called immediately when mission begin.
      (try_for_range, ":count_no", 0, 200),
         (troop_set_slot, "trp_temp_array_inflitration_sentry", ":count_no", -1),#清空
      (try_end),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 2, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 3, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 4, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 5, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 13, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 17, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 18, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 19, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 20, 1),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 21, 1),

      (troop_set_slot, "trp_temp_array_inflitration_sentry", 7, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 11, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 14, 2),
      (troop_set_slot, "trp_temp_array_inflitration_sentry", 22, 2),
 
      (assign, "$total_patrol_entry", 25),#前25个entry之间巡逻
      (assign, "$infiltrate_tut", -1),#初始化潜行模式

      (set_jump_mission,"mt_libra_smuggle_wharf_2"),
      (jump_to_scene,"scn_libra_smuggle_wharf"),
      (change_screen_mission),
    ]),


#支线剧情：冠军拍卖
  ("champion_auction",
   [
      (modify_visitors_at_site, "scn_champion_auction"),
      (reset_visitors),
      (set_visitor, 1, "trp_player"),
      (set_visitor, 3, "trp_blackguard_sergeant"),
      (set_visitor, 4, "trp_meat_puppet"),
      (set_visitor, 5, "trp_blackguard_mercenary"),
      (set_visitor, 6, "trp_blackguard_mercenary"),
      (set_visitor, 7, "trp_diemer_swordman"),
      (set_visitor, 8, "trp_sword_sister"),#接待员
      (set_visitor, 9, "trp_libra_slave_catching_cavalry"),#拍卖员
      (set_visitor, 10, "trp_libra_slave_merchant"),
      (set_visitor, 11, "trp_libra_slave_merchant"),
      (set_visitor, 12, "trp_libra_slave_merchant"),
      (set_visitor, 13, "trp_libra_slave_merchant"),
      (try_begin),
         (check_quest_active, "qst_champion_auction"),
         (set_visitor, 14, "trp_zela"),#俘虏
      (else_try),
         (set_visitor, 14, "trp_confederation_gladiator_champion"),#俘虏
      (try_end),

      (try_for_range, ":entry_no", 15, 31),
         (store_random_in_range, ":troop_no", 0, 10),
         (try_begin),
            (eq, ":troop_no", 0),
            (assign, ":troop_no", "trp_diemer_young_slaveholder"),
         (else_try),
            (eq, ":troop_no", 1),
            (assign, ":troop_no", "trp_diemer_knight_retinue"),
         (else_try),
            (eq, ":troop_no", 2),
            (assign, ":troop_no", "trp_diemer_monster_enslaving_knight"),
         (else_try),
            (eq, ":troop_no", 3),
            (assign, ":troop_no", "trp_purifier_pastor"),
         (else_try),
            (eq, ":troop_no", 4),
            (assign, ":troop_no", "trp_purifier_combat_pastor"),
         (else_try),
            (eq, ":troop_no", 5),
            (assign, ":troop_no", "trp_suffering_friar"),
         (else_try),
            (eq, ":troop_no", 6),
            (assign, ":troop_no", "trp_confederation_armed_faithful"),
         (else_try),
            (eq, ":troop_no", 7),
            (assign, ":troop_no", "trp_ankiya_naturalized_noble"),
         (else_try),
            (eq, ":troop_no", 8),
            (assign, ":troop_no", "trp_ankiya_rider"),
         (else_try),
            (eq, ":troop_no", 9),
            (assign, ":troop_no", "trp_ankiya_knight"),
         (try_end),
         (set_visitor, ":entry_no", ":troop_no"),
      (try_end),
      (set_jump_mission,"mt_champion_auction_mission"),
      (jump_to_scene, "scn_champion_auction"),
    ]),


#支线剧情：第三个死
  ("third_death",
   [
      (modify_visitors_at_site, "scn_third_death"),
      (reset_visitors),
      (try_begin),
         (eq, "$third_death_quest_phase", 1),
         (set_visitor, 1, "trp_player"),
         (set_visitor, 2, "trp_npc4"),#范伦汀娜
         (set_visitor, 3, "trp_yannick_village_elder"),#扬尼克村长
         (set_visitor, 4, "trp_farmer"),#农民
         (set_visitor, 5, "trp_grenier_wellselected_militia"),#戈兰尼尔精选民兵
         (set_visitor, 6, "trp_hunter"),#猎人
         (set_visitor, 7, "trp_caravan_master"),#商队头领
         (set_visitor, 8, "trp_peasant_woman"),#农妇
         (set_jump_mission,"mt_third_death_1"),
      (else_try),
         (is_between, "$third_death_quest_phase", 11, 13),
         (assign, "$third_death_quest_phase", 12),
         (set_visitor, 1, "trp_player"),
         (set_visitor, 2, "trp_npc4"),#范伦汀娜
         (set_visitor, 15, "trp_yannick_village_elder"),#扬尼克村长
         (set_visitor, 16, "trp_lance_protector_antoine_moro"),#护枪官安托万.莫罗
         (set_visitor, 17, "trp_farmer"),#农民
         (set_visitor, 18, "trp_grenier_wellselected_militia"),#戈兰尼尔精选民兵
         (set_visitor, 19, "trp_caravan_master"),#商队头领
         (set_visitor, 20, "trp_peasant_woman"),#农妇
         (set_visitor, 21, "trp_hunter"),#猎人
         (set_jump_mission,"mt_third_death_2"),
      (else_try),
         (eq, "$third_death_quest_phase", 20),
         (set_visitor, 1, "trp_player"),
         (set_visitor, 2, "trp_npc4"),#范伦汀娜
         (set_visitor, 22, "trp_lance_protector_antoine_moro"),#护枪官安托万.莫罗
         (set_jump_mission,"mt_third_death_3"),
      (try_end),
      (jump_to_scene, "scn_third_death"),
      (change_screen_mission),
    ]),

]