# -*- coding: UTF-8 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *
from module_constants import *

from module_dialogs_new_mission import *
from module_dialogs_old import *


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.  
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

dialogs = [
  [anyone ,"start", [(store_conversation_troop, "$g_talk_troop"),
                     (store_conversation_agent, "$g_talk_agent"),
                     (store_troop_faction, "$g_talk_troop_faction", "$g_talk_troop"),
#                     (troop_get_slot, "$g_talk_troop_relation", "$g_talk_troop", slot_troop_player_relation),
                     (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
                     (assign, "$g_talk_troop_relation", reg0),
					 
					 #This may be different way to handle persuasion, which might be a little more transparent to the player in its effects
					 #Persuasion will affect the player's relation with the other character -- but only for 1 on 1 conversations
					 (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
					 (assign, "$g_talk_troop_effective_relation", "$g_talk_troop_relation"),
					 (val_add, "$g_talk_troop_effective_relation", ":persuasion"),
					 (try_begin),
						(gt, "$g_talk_troop_effective_relation", 0),
						(store_add, ":persuasion_modifier", 10, ":persuasion"),
						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
						(val_div, "$g_talk_troop_effective_relation", 10),
					 (else_try),
						(lt, "$g_talk_troop_effective_relation", 0),
						(store_sub, ":persuasion_modifier", 20, ":persuasion"),
						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
						(val_div, "$g_talk_troop_effective_relation", 20),
					 (try_end),
					 (val_clamp, "$g_talk_troop_effective_relation", -100, 101), 
					 (try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg3, "$g_talk_troop_effective_relation"),
						(display_message, "str_test_effective_relation_=_reg3"),
					 (try_end),
					 
                     (try_begin),
                       (this_or_next|is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
                       (is_between, "$g_talk_troop", mayors_begin, mayors_end),
                       (party_get_slot, "$g_talk_troop_relation", "$current_town", slot_center_player_relation),
                     (try_end),
                     (store_relation, "$g_talk_troop_faction_relation", "$g_talk_troop_faction", "fac_player_faction"),
                     
                     (assign, "$g_talk_troop_party", "$g_encountered_party"),
                     (try_begin),
                       (troop_slot_ge, "$g_talk_troop", slot_troop_leaded_party, 1),
                       (troop_get_slot, "$g_talk_troop_party", "$g_talk_troop", slot_troop_leaded_party),
                     (try_end),
                     
#                     (assign, "$g_talk_troop_kingdom_relation", 0),
#                     (try_begin),
#                       (gt, "$players_kingdom", 0),
#                       (store_relation, "$g_talk_troop_kingdom_relation", "$g_talk_troop_faction", "$players_kingdom"),
#                     (try_end),


                     
                     (store_current_hours, "$g_current_hours"),
                     (troop_get_slot, "$g_talk_troop_last_talk_time", "$g_talk_troop", slot_troop_last_talk_time),
                     (troop_set_slot, "$g_talk_troop", slot_troop_last_talk_time, "$g_current_hours"),
                     (store_sub, "$g_time_since_last_talk","$g_current_hours","$g_talk_troop_last_talk_time"),
                     (troop_get_slot, "$g_talk_troop_met", "$g_talk_troop", slot_troop_met),
					 (val_min, "$g_talk_troop_met", 1), #the global variable goes no higher than one
					 (try_begin),
					    (troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
						(troop_set_slot, "$g_talk_troop", slot_troop_met, 1),
						
						#Possible later activations of notes
						(try_begin),
							(is_between, "$g_talk_troop", kingdom_ladies_begin, kingdom_ladies_end),
						(try_end),
						
					 (try_end),
					 
                     (try_begin),
#                       (this_or_next|eq, "$talk_context", tc_party_encounter),
#                       (this_or_next|eq, "$talk_context", tc_castle_commander),
                       (call_script, "script_party_calculate_strength", "p_collective_enemy",0),
                       (assign, "$g_enemy_strength", reg0),
                       (call_script, "script_party_calculate_strength", "p_main_party",0),
                       (assign, "$g_ally_strength", reg0),
                       (store_mul, "$g_strength_ratio", "$g_ally_strength", 100),
					   (assign, ":enemy_strength", "$g_enemy_strength"), #these two lines added to avoid div by zero error
					   (val_max, ":enemy_strength", 1),
                       (val_div, "$g_strength_ratio", ":enemy_strength"),
                     (try_end),

                     (assign, "$g_comment_found", 0),

					 (assign, "$g_comment_has_rejoinder", 0),
					 (assign, "$g_romantic_comment_made", 0),
					 (assign, "$skip_lord_assumes_argument", 0), #a lord pre-empts a player's issue, ie, when the player is conducting a rebellion
					 (assign, "$bypass_female_vassal_explanation", 0),
					 (assign, "$g_done_wedding_comment", 0),
					 
#					 (assign, "$g_time_to_spare", 0),
					 
					 
                     (try_begin),
                       (troop_is_hero, "$g_talk_troop"),
                       (talk_info_show, 1),
                       (call_script, "script_setup_talk_info"),
                     (try_end),

					 (assign, "$g_last_comment_copied_to_s42", 0),
                     (try_begin),
                       (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
                       (call_script, "script_get_relevant_comment_to_s42"),
                       (assign, "$g_comment_found", reg0),
                     (try_end),

                     (troop_get_type, reg65, "$g_talk_troop"),
                     (try_begin),
                       (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                       (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                       (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                       (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
                       (str_store_string,s67,"@{reg65?My Lady:My Lord}"), #bug fix
                     (else_try),
                       (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                       (str_store_string,s65,"@{reg65?madame:sir}"),
                       (str_store_string,s66,"@{reg65?Madame:Sir}"),
                       (str_store_string,s67,"@{reg65?Madame:Sir}"), #bug fix
                     (try_end),

					 (try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, "$talk_context"),
						(display_message, "@{!}DEBUG -- Talk context: {reg4}"),
					 (try_end),

					 (try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, "$g_time_since_last_talk"),
						(display_message, "@{!}DEBUG -- Time since last talk: {reg4}"),
					 (try_end),
					 
					 
					 (try_begin),
						(eq, "$cheat_mode", 0),
						(store_partner_quest, ":quest"),
						(ge, ":quest", 0),
						(str_store_quest_name, s4, ":quest"),
						
					 (try_end),
					 
                     (eq, 1, 0)],
   "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],

  [anyone ,"member_chat", [
					(store_conversation_troop, "$g_talk_troop"),
                    (try_begin),
                        (is_between, "$g_talk_troop", companions_begin, companions_end),
                        (talk_info_show, 1),
                        (call_script, "script_setup_talk_info_companions"),
                    (else_try),
                        (is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
                        (talk_info_show, 1),
                        (call_script, "script_setup_talk_info"),
                    (try_end),
	   
					(troop_get_type, reg65, "$g_talk_troop"),
                           
                    (troop_get_type, reg65, "$g_talk_troop"),
                    (try_begin),
                        (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                        (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                        (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                        (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
                    (else_try),
                        (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                        (str_store_string,s65,"@{reg65?madame:sir}"),
                        (str_store_string,s66,"@{reg65?Madame:Sir}"),
                    (try_end),

					(store_current_hours, "$g_current_hours"),
					(troop_set_slot, "$g_talk_troop", slot_troop_last_talk_time, "$g_current_hours"),					 
					 
                    (eq, 1, 0)],  
   "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],

  [anyone ,"event_triggered", [(store_conversation_troop, "$g_talk_troop"),
                           (try_begin),
                               (is_between, "$g_talk_troop", companions_begin, companions_end),
                               (talk_info_show, 1),
                               (call_script, "script_setup_talk_info_companions"),
                           (try_end),
                               
                     (troop_get_type, reg65, "$g_talk_troop"),
                     (try_begin),
                       (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                       (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                       (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                       (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
                     (else_try),
                       (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                       (str_store_string,s65,"@{reg65?madame:sir}"),
                       (str_store_string,s66,"@{reg65?Madame:Sir}"),
                     (try_end),

					 
                     (eq, 1, 0)],  
   "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],

  [anyone, "event_triggered",
   [
     (eq, "$talk_context", tc_give_center_to_fief),

     (assign, ":there_are_vassals", 0),
     (assign, ":end_cond", active_npcs_end),
     (try_for_range, ":troop_no", active_npcs_begin, ":end_cond"),
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (neq, "trp_player", ":troop_no"),
       (store_troop_faction, ":faction_no", ":troop_no"),
       (eq, ":faction_no", "fac_player_supporters_faction"),
       (val_add, ":there_are_vassals", 1),
       (assign, ":end_cond", 0),
     (try_end),
     
     (try_begin),
       (gt, ":there_are_vassals", 0),
       (str_store_string, s2, "str_do_you_wish_to_award_it_to_one_of_your_vassals"),
     (else_try),
       (str_store_string, s2, "str_who_do_you_wish_to_give_it_to"),
     (try_end),

     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
  	 (str_store_string, s5, "str_sire_my_lady_we_have_taken_s1_s2"),
     ],
   "{!}{s5}", "award_fief_to_vassal", 
   []],

  [anyone|plyr, "award_fief_to_vassal",
   [
   (is_between, "$g_player_court", centers_begin, centers_end), 
   (store_faction_of_party, ":player_court_faction", "$g_player_court"),
   (eq, ":player_court_faction", "fac_player_supporters_faction"),
	 ],
   "I wish to defer the appointment of a lord, until I take the counsel of my subjects", "award_fief_to_vassal_defer",
   [
     ]],

  [anyone, "award_fief_to_vassal_defer",
   [
     ],
   "As you wish, {sire/my lady}. You may decide this matter at a later date.", "close_window",
   [
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, -1),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
	 (try_end),	 
	 (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", -1, 0), #-1 for the faction lord in this script is used exclusively in this context
	 #It is only used because script_give_center_to_faction does not reset the town lord if fac_player_supporters_faction is the attacker

     (assign, "$g_center_taken_by_player_faction", -1),
	 
     #new start
     (try_begin),
       (eq, "$g_next_menu", "mnu_castle_taken"), 
       (jump_to_menu, "$g_next_menu"),
     (try_end),  
     #new end
	 
     ]],
   
   
   
   [anyone|plyr|repeat_for_troops,"award_fief_to_vassal",
   [  
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (neq, "trp_player", ":troop_no"),
     (store_troop_faction, ":faction_no", ":troop_no"),
     (eq, ":faction_no", "fac_player_supporters_faction"),
     (str_store_troop_name, s11, ":troop_no"),
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),
	 
	 (try_begin),
	   (troop_slot_eq, "$g_talk_troop", slot_lord_recruitment_argument, argument_benefit),
	   (str_store_string, s12, "str__promised_fief"),
	 (else_try),
	   (str_clear, s12),
	 (try_end),
	 
     (try_begin),
       (eq, reg0, 0),
       (str_store_string, s1, "str_no_fiefss12"),
     (else_try),
       (str_store_string, s1, "str_fiefs_s0s12"),
     (try_end),
    ],
   "{!}{s11} {s1}.", "award_fief_to_vassal_2",[(store_repeat_object, "$temp")]],

  [anyone|plyr, "award_fief_to_vassal",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),

	 (try_begin),
		(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
		(str_store_string, s12, "str_please_s65_"),
	 (else_try),	
		(str_clear, s12),
	 (try_end),	
	 
     (assign, ":there_are_vassals", 0),
     (assign, ":end_cond", active_npcs_end),
     (try_for_range, ":troop_no", active_npcs_begin, ":end_cond"),
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (neq, "trp_player", ":troop_no"),
       (store_troop_faction, ":faction_no", ":troop_no"),
       (eq, ":faction_no", "fac_player_supporters_faction"),
       (val_add, ":there_are_vassals", 1),
       (assign, ":end_cond", 0),
     (try_end),
     
     (try_begin),
       (gt, ":there_are_vassals", 0),
  	   (str_store_string, s2, "str_fiefs_s0"),
  	 (else_try),
  	   (str_clear, s2),
  	 (try_end),
  	 
  	 (str_store_string, s5, "str_s12i_want_to_have_s1_for_myself"),
	 ],
   "{!}{s5}", "award_fief_to_vassal_2",      
   [
     (assign, "$temp", "trp_player"),
     ]],  

  [anyone, "award_fief_to_vassal_2",
   [
     ],
   "As you wish, {sire/my lady}. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
   [
     (assign, ":new_owner", "$temp"),
	 
     (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	 (try_end),
   
     (assign, reg6, 0),
     (assign, reg7, 0),
     (try_begin),
       (eq, ":new_owner", "$g_talk_troop"),
       (assign, reg6, 1),
     (else_try),
       (eq, ":new_owner", "trp_player"),
       (assign, reg7, 1),
     (else_try),
       (str_store_troop_name, s11, ":new_owner"),
     (try_end),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     (troop_get_type, reg3, ":new_owner"),
     
     (assign, "$g_center_taken_by_player_faction", -1),	 	           

     #new start
     (try_begin),
       (eq, "$g_next_menu", "mnu_castle_taken"), 
       (jump_to_menu, "$g_next_menu"),
     (try_end),  
     #new end
     ]],

# Awarding fiefs in rebellion...
	 
  [anyone, "event_triggered",
   [
     (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
     (ge, "$g_center_taken_by_player_faction", 0),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ],
   "{s1} is not being managed by anyone. Whom shall I put in charge?", "center_captured_rebellion",
   []],

  [anyone|plyr|repeat_for_troops, "center_captured_rebellion",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (neq, "$g_talk_troop", ":troop_no"),
     (neq, "trp_player", ":troop_no"),
     (store_troop_faction, ":faction_no", ":troop_no"),
     (eq, ":faction_no", "fac_player_supporters_faction"),
     (str_store_troop_name, s11, ":troop_no"),
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),
     (try_begin),
       (eq, reg0, 0),
       (str_store_string, s1, "@(no fiefs)"),
     (else_try),
       (str_store_string, s1, "@(fiefs: {s0})"),
     (try_end),
     ],
   "{s11}. {s1}", "center_captured_rebellion_2",
   [
     (store_repeat_object, "$temp"),
     ]],

  [anyone|plyr, "center_captured_rebellion",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
    ],
   "Please {s65}, I want to have {s1} for myself. (fiefs: {s0})", "center_captured_rebellion_2",
   [
     (assign, "$temp", "trp_player"),
     ]],

  [anyone|plyr, "center_captured_rebellion",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "$g_talk_troop"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ],
   "{s66}, you should have {s1} for yourself. (fiefs: {s0})", "center_captured_rebellion_2",
   [
     (assign, "$temp", "$g_talk_troop"),
     ]],

  [anyone, "center_captured_rebellion_2",
   [
#     (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
#     (ge, "$g_center_taken_by_player_faction", 0),
     ],
   "Hmmm. All right, {playername}. I value your counsel highly. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
   [
     (assign, ":new_owner", "$temp"),
     (call_script, "script_calculate_troop_score_for_center", ":new_owner", "$g_center_taken_by_player_faction"),
     (assign, ":new_owner_score", reg0),
     (assign, ":total_negative_effect"),
     (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
	   (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),     
       (store_troop_faction, ":cur_faction", ":cur_troop"),
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (neq, ":cur_troop", ":new_owner"),
	   (neg|troop_slot_eq, ":cur_troop", slot_troop_stance_on_faction_issue, ":new_owner"),
	   (call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":new_owner"),
	   (lt, reg0, 25),
	   
	   
       (call_script, "script_calculate_troop_score_for_center", ":cur_troop", "$g_center_taken_by_player_faction"),
       (assign, ":cur_troop_score", reg0),
       (gt, ":cur_troop_score", ":new_owner_score"),
       (store_sub, ":difference", ":cur_troop_score", ":new_owner_score"),
       (store_random_in_range, ":random_dif", 0, ":difference"),
       (val_div, ":random_dif", 1000),
       (gt, ":random_dif", 0),
       (val_add, ":total_negative_effect", ":random_dif"),
       (val_mul, ":random_dif", -1),
       (call_script, "script_change_player_relation_with_troop", ":cur_troop", ":random_dif"),
     (try_end),
     (val_mul, ":total_negative_effect", 2),
     (val_div, ":total_negative_effect", 3),
     (val_add, ":total_negative_effect", 5),
     (try_begin),
       (neq, ":new_owner", "trp_player"),
       (val_min, ":total_negative_effect", 30),
       (call_script, "script_change_player_relation_with_troop", ":new_owner", ":total_negative_effect"),
     (try_end),
     
     (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	 (try_end),
	    
     (assign, reg6, 0),
     (assign, reg7, 0),
     (try_begin),
       (eq, ":new_owner", "$g_talk_troop"),
       (assign, reg6, 1),
     (else_try),
       (eq, ":new_owner", "trp_player"),
       (assign, reg7, 1),
     (else_try),
       (str_store_troop_name, s11, ":new_owner"),
     (try_end),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     (troop_get_type, reg3, ":new_owner"),
     
     (assign, "$g_center_taken_by_player_faction", -1),	 	           

     #new start
     (try_begin),
       (eq, "$g_next_menu", "mnu_castle_taken"), 
       (jump_to_menu, "$g_next_menu"),
     (try_end),  
     #new end
     ]],

  #TUTORIAL START
  [anyone, "start",
   [
     (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
     (eq, "$g_tutorial_training_ground_conversation_state", 0),
     (eq, "$g_tutorial_fighter_talk_before", 0)],
   "Hello there. We are polishing off our combat skills here with a bit of sparring practice.\
 You look like you could use a bit of training. Why don't you join us, and we can show you a few tricks.\
 And if you need explanation of any combat concepts, just ask, and I will do my best to fill you in.", "fighter_talk",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),
     (assign, "$g_tutorial_fighter_talk_before", 1)]],

   [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 0)],
   "What do you want to practice?", "fighter_talk", []],

   [anyone, "fighter_pretalk", [],
   "Tell me what kind of practice you want.", "fighter_talk", []],
   
   [anyone|plyr, "fighter_talk",
   [],
   "I want to practice attacking.", "fighter_talk_train_attack", []],

  [anyone|plyr, "fighter_talk",
   [],
   "I want to practice blocking with my weapon.", "fighter_talk_train_parry", []],

  [anyone|plyr, "fighter_talk",
   [],
   "Let's do some sparring practice.", "fighter_talk_train_combat", []],

  [anyone|plyr, "fighter_talk",
   [(eq,1,0)],
   "{!}TODO: Let's train chamber blocking.", "fighter_talk_train_chamber", []],

  [anyone|plyr, "fighter_talk",
   [],
   "[Leave]", "close_window", []],
  
  [anyone, "fighter_talk_train_attack",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "All right. There are four principle directions for attacking. These are overhead swing, right swing, left swing and thrust.\
 Now, I will tell you which direction to attack from and you must try to do the correct attack.\
 ^^(Move your mouse while you press the left mouse button to specify attack direction. For example, to execute an overhead attack, move the mouse up at the instant you press the left mouse button.\
 The icons on your screen will help you do the correct action.)" , "fighter_talk_train_attack_2",
   []],

  [anyone|plyr, "fighter_talk_train_attack_2",  [],
   "Let's begin then. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_melee_trainer_attack", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     (assign, "$g_tutorial_training_ground_current_score", 0),
     (assign, "$g_tutorial_training_ground_current_score_2", 0),
     (assign, "$g_tutorial_update_mouse_presentation", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_attack_2",  [],
   "Actually I want to do something else.", "fighter_pretalk", []],
	 
  [anyone, "fighter_talk_train_attack",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "fighter_talk_train_parry",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "Unlike a shield, blocking with a weapon can only stop attacks coming from one direction.\
 For example if you block up, you'll deflect overhead attacks, but you can still be hit by side swings or thrust attacks.\
 ^^(You must press and hold down the right mouse button to block.)", "fighter_talk_train_parry_2", [ ]],

	 [anyone, "fighter_talk_train_parry_2", [],
   "I'll now attack you with different types of strokes, and I will wait until you do the correct block before attacking.\
 Try to do the correct block as soon as you can.\
 ^^(This practice is easy to do with the 'automatic block direction' setting which is the default.\
 If you go to the Options menu and change defend direction control to 'mouse movement' or 'keyboard', you'll need to manually choose block direction. This is much more challenging, but makes the game much more interesting.\
 This practice can be very useful if you use manual blocking.)", "fighter_talk_train_parry_3",
   []],
	 
  [anyone|plyr, "fighter_talk_train_parry_3",  [],
   "Let's begin then. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_melee_trainer_parry", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     (assign, "$g_tutorial_training_ground_current_score", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_parry_3",  [],
   "Actually I want to do something else.", "fighter_pretalk", []],
	 
	 

  [anyone, "fighter_talk_train_parry",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "fighter_talk_train_chamber",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "{!}TODO: OK.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_melee_trainer_chamber", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     (assign, "$g_tutorial_training_ground_current_score", 0),
     ]],

  [anyone, "fighter_talk_train_chamber",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "fighter_talk_train_combat",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "Sparring is an excellent way to prepare for actual combat.\
 We'll fight each other with non-lethal weapons now, until one of us falls to the ground.\
 You can get some bruises of course, but better that than being cut down in the real thing.", "fighter_talk_train_combat_2",
   []],

  [anyone|plyr, "fighter_talk_train_combat_2",  [],
   "Let's begin then. I am ready.", "close_window", [
     (assign, "$g_tutorial_training_ground_melee_trainer_combat", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_combat_2",  [],
   "Actually I want to do something else.", "fighter_pretalk", []],
	 
  [anyone, "fighter_talk_train_combat",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 1)], #parry complete
   "Good. You were able to block my attacks successfully. You may repeat this practice and try to get faster each time, until you are confident of your defense skills. Do you want to have another go?", "fighter_parry_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 2)], #player knocked down in parry
   "Well that didn't go too well, did it? (Remember, you must press and hold down the right mouse button to keep your block effective.) Do you want to try again?", "fighter_parry_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone|plyr, "fighter_parry_try_again",
   [],
   "Yes. Let's try again.", "fighter_talk_train_parry", []],

  [anyone|plyr, "fighter_parry_try_again",
   [],
   "No, I think I am done for now.", "fighter_talk_leave_parry", []],
	 
  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 3)], #trainer knocked down in parry
   "Hey! We are doing a blocking practice, mate! You are supposed to block my attacks, not attack me back.", "fighter_parry_warn",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone|plyr, "fighter_parry_warn",
   [],
   "I am sorry. Let's try once again.", "fighter_talk_train_parry", []],

  [anyone|plyr, "fighter_parry_warn",
   [],
   "Sorry. I must leave this practice now.", "fighter_talk_leave_parry", []],

  [anyone, "fighter_talk_leave_parry",
   [],
   "All right. As you wish.", "close_window", []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 4)], #player knocked down in combat
   "Well that didn't go too well, did it?  Don't feel bad, and try not to do same mistakes next time. Do you want to have a go again?", "fighter_combat_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone|plyr, "fighter_combat_try_again",
   [],
   "Yes. Let's do another round.", "fighter_talk_train_combat", []],

  [anyone|plyr, "fighter_combat_try_again",
   [],
   "No. That was enough for me.", "fighter_talk_leave_combat", []],

  [anyone, "fighter_talk_leave_combat",
   [],
   "Well, all right. Talk to me again if you change your mind.", "close_window", []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 5)], #trainer knocked down in combat
   "Hey, that was good sparring. You defeated me, but next time I'll be more careful. Do you want to have a go again?", "fighter_combat_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  # [anyone, "start",
   # [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   # (eq, "$g_tutorial_training_ground_conversation_state", 6)], #chamber complete
   # "{!}TODO: Congratulations. Anything else?", "fighter_talk",
   # [
     # (assign, "$g_tutorial_training_ground_conversation_state", 0),
     # ]],
	 
  # [anyone, "start",
   # [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   # (eq, "$g_tutorial_training_ground_conversation_state", 7)], #player knocked down in chamber
   # "{!}TODO: Want to try again?", "fighter_chamber_try_again",
   # [
     # (assign, "$g_tutorial_training_ground_conversation_state", 0),
     # ]],

  # [anyone|plyr, "fighter_chamber_try_again",
   # [],
   # "{!}TODO: OK let's try again.", "fighter_talk_train_chamber", []],

  # [anyone|plyr, "fighter_chamber_try_again",
   # [],
   # "TODO: No, let's leave it there.", "fighter_talk_leave_chamber", []],

  # [anyone, "fighter_talk_leave_chamber",
   # [],
   # "{!}TODO: OK. Bye.", "close_window", []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 8)], #trainer knocked down in chamber
   "{!}TODO: What are you doing? Don't attack me except while chambering!", "fighter_chamber_warn",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 9)], #attack complete
   "Very good. You have learned how to attack from any direction you want. If you like we can try this again or move to a different exercise.", "fighter_talk",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 

  [anyone|plyr, "fighter_chamber_warn", # unused
   [],
   "{!}TODO: Sorry, let's try once again.", "fighter_talk_train_chamber", []],

  [anyone|plyr, "fighter_chamber_warn", # unused
   [],
   "{!}TODO: Sorry. I want to leave the exercise.", "close_window", []],

  [trp_tutorial_archer_1|auto_proceed, "start",
   [],
   "{!}.", "tutorial_troop_default",
   []],

  [trp_tutorial_master_archer, "start",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
     ],
   "Not bad. Not bad at all! You seem to have grasped the basics of archery. Now, try to do the same thing with a crossbow.\
 Take the crossbow and the bolts over there and shoot those three targets. The crossbow is much easier to shoot with compared with the bow,\
 but you need to reload it after each shot.", "archer_challenge_2", []],

	 [trp_tutorial_master_archer, "start",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 2),
     ],
   "Good. You didn't have too much difficulty using the crossbow either. Next you will learn to use throwing weapons.\
 Pick up the javelins you see over there and try to hit those three targets. ", 
 "archer_challenge_2", []],

  [trp_tutorial_master_archer, "start",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 3),
     ],
   "Well, with that you have recevied the basic skills to use all three types of ranged weapons. The rest will come with practice. Train each and every day, and in time you will be as good as the best marksmen in Calradia.", 
   "ranged_end", []],
	 
	 [trp_tutorial_master_archer, "ranged_end", [],
   "Now, you can go talk with the melee fighters or the horsemanship trainer if you haven't already done so. They can teach you important skills too.", 
   "close_window", []],

  [trp_tutorial_master_archer, "start",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),

     ],
   "Good day to you, young fellow. I spend my days teaching about ranged weapons to anyone that is willing to learn.\
 If you need a tutor, let me know and I'll teach you how to use the bow, the crossbow and the javelin.", "archer_talk",
   []],

  [anyone|plyr, "archer_talk",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     ],
   "Yes, show me how to use ranged weapons.", "archer_challenge", []],

  # [anyone|plyr, "archer_talk",
   # [
     # (gt, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     # ],
   # "{!}TODO: I want to move to the next stage.", "archer_challenge", []],

  [anyone|plyr, "archer_talk",
   [],
   "No, not now.", "close_window", []],

  [trp_tutorial_master_archer, "archer_challenge",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     ],
   "All right. Your first training will be in bowmanship. The bow is a difficult weapon to master. But once you are sufficiently good at it, you can shoot quickly and with great power.\
 Go pick up the bow and arrows you see over there now and shoot those targets.", "archer_challenge_2",
   []],

  # [trp_tutorial_master_archer, "archer_challenge",
   # [
     # (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
     # ],
   # "{!}TODO: Make 3 shots with crossbow.", "archer_challenge_2",
   # []],

  # [trp_tutorial_master_archer, "archer_challenge",
   # [],
   # "{!}TODO: Make 3 shots with javelin.", "archer_challenge_2",
   # []],

  [anyone|plyr, "archer_challenge_2",
   [],
   "All right. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_archer_trainer_state", 1),
     (try_begin),
       (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_bow"),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_arrows"),
     (else_try),
       (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_crossbow"),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_bolts"),
     (else_try),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_javelin"),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_2", -1),
     (try_end),
     ]],

  [anyone|plyr, "archer_challenge_2",
   [],
   "Just a minute. I want to do something else first.", "close_window",
   []],


  [trp_tutorial_master_horseman, "start",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
     ],
   "I hope you enjoyed the ride. Now we move on to something a bit more difficult. Grab the lance you see over there and ride around the course hitting each target at least once.", 
   "horseman_melee_challenge_2", []],
   
  [trp_tutorial_master_horseman, "start",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 2),
     ],
   "Good! You have been able to hit all targets on horseback. That's no easy feat for a starter. Your next challange will be using a bow and arrows to shoot at the archery targets by the road. You need to put an arrow to each target to consider yourself successful.", 
   "horseman_melee_challenge_2", []],

  [trp_tutorial_master_horseman, "start",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 3),
     ],
   "Very good. You were able to shoot all targets from horseback. Keep riding and practicing each day and in time you will be an expert horseman.", "horsemanship_end",
   [
     ]],
	 
	 [trp_tutorial_master_horseman, "horsemanship_end",
   [
     ],
   "Now, you can go talk with the melee fighters or the archery trainer if you haven't already done so. You need to learn everything you can to be prepared when you have to defend yourself.", "close_window",
   []],
	 

	 
  [trp_tutorial_master_horseman, "start",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),
     ],
   "Good day! I have come here for some riding practice, but my old bones are aching badly so I decided to give myself a rest today.\
 If you would like to practice your horsemanship, you can take my horse here. The exercise would be good for her.", "horseman_talk",
   []],

  [anyone|plyr, "horseman_talk",
   [],
   "Yes, I would like to practice riding.", "horseman_challenge", []],

  [anyone|plyr, "horseman_talk",
   [],
   "Uhm. Maybe later.", "close_window", []],

  # [trp_tutorial_master_horseman, "horseman_challenge",
   # [
     # (eq, "$g_tutorial_training_ground_player_continue_without_basics", 0),
     # (this_or_next|eq, "$g_tutorial_training_ground_melee_trainer_attack_completed", 0),
     # (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
    # ],
   # "Hmm. Do you know how to use your weapons? You'd better learn to use those on foot before you start to train using them on horseback.", "horseman_ask",
   # []],

  # [anyone|plyr, "horseman_ask",
   # [],
   # "Yes, I know ", "horseman_challenge",
   # [
     # (assign, "$g_tutorial_training_ground_player_continue_without_basics", 1),
     # ]],

  # [anyone|plyr, "horseman_ask",
   # [],
   # "{!}TODO: No", "horseman_ask_2",
   # []],

  # [trp_tutorial_master_horseman, "horseman_ask_2",
   # [],
   # "{!}TODO: Come back later then.", "close_window",
   # []],

  [trp_tutorial_master_horseman, "horseman_challenge",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
    ],
   "Good. Now, I will give you a few exercises that'll teach you riding and horseback weapon use.\
 Your first assignment is simple. Just take your horse for a ride around the course.\
 Go as slow or as fast as you like.\
 Come back when you feel confident as a rider and I'll give you some tougher exercises.", "horseman_melee_challenge_2",
   []],

  [anyone|plyr, "horseman_melee_challenge_2",
   [],
   "All right. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_horseman_trainer_state", 1),
     (try_begin),
       (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", -1),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
     (else_try),
       (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_arena_lance"),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
     (else_try),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_practice_bow_2"),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", "itm_practice_arrows_2"),
     (try_end),
     ]],

  [anyone|plyr, "horseman_melee_challenge_2",
   [],
   "Just a minute. I need to do something else first.", "close_window", []],

  [trp_tutorial_rider_1|auto_proceed, "start",
   [],
   "{!}Warning: This line is never displayed.", "tutorial_troop_default",
   []],

  [trp_tutorial_rider_2|auto_proceed, "start",
   [],
   "{!}Warning: This line is never displayed.", "tutorial_troop_default",
   []],

  [anyone, "tutorial_troop_default",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),
     ],
   "Hey, I am trying to practice here. Go, talk with the archery trainer if you need guidance about ranged weapons.", "close_window", []],


   #PRISON BREAK START
   [anyone,"start",
   [                    
     (eq, "$talk_context", tc_prison_break),                    
     (troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"),
     (troop_slot_ge, "$g_talk_troop", slot_troop_mission_participation, mp_stay_out),
   ],
   "Is there a change of plans?", "lord_prison_break_confirm_3",[]],
   
   [anyone,"start",
   [
     (eq, "$talk_context", tc_prison_break),
     (try_begin),
       (eq, "$cheat_mode", 1),
       (assign, reg0, "$g_talk_troop"),
       (assign, reg1, "$g_encountered_party"),
       (troop_get_slot, reg2, "$g_talk_troop", slot_troop_prisoner_of_party),
       (display_message, "@{!}g_talk_troop = {reg0} , g_encountered_party = {reg1} , slot value = {reg2}"),
     (try_end),
     (troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"),
   ],
   "What's going on?", "lord_prison_break",[]],
   
   
   #TAVERN DRUNK DIALOGS
   [anyone, "start", 
   [
	(eq, "$g_talk_troop", "trp_belligerent_drunk"),
	],
   "What are you looking at?", "drunk_response", 
   [
     (try_begin),
       (eq, "$g_main_attacker_agent", 0),
       (call_script, "script_activate_tavern_attackers"),       
     (try_end),
     (mission_disable_talk),
   ]],

   [anyone, "start", 
   [
	(eq, "$g_talk_troop", "trp_hired_assassin"),
	],
   "Are you looking at me?", "drunk_response", 
   [
     (try_begin),
       (eq, "$g_main_attacker_agent", 0),
       (call_script, "script_activate_tavern_attackers"),       
     (try_end),
     (mission_disable_talk),
   ]],

   [anyone, "start", 
   [
	(eq, "$g_talk_troop", "trp_hired_assassin"),
		(eq,1,0),
	],
   "{!}Added to match dialog ids with translations.", "close_window", 
   []],
 
   
  [anyone, "start", [
  (is_between, "$g_talk_troop", tavernkeepers_begin, tavernkeepers_end),
  (gt, "$g_main_attacker_agent", 0),
  (neg|agent_is_alive, "$g_main_attacker_agent"),
  
  (try_begin),
 	(neg|agent_is_alive, "$g_main_attacker_agent"),
	(agent_get_troop_id, ":type", "$g_main_attacker_agent"),
	(eq, ":type", "trp_hired_assassin"),
	
	(str_store_string, s9, "str_strange_that_one_didnt_seem_like_your_ordenary_troublemaker_he_didnt_drink_all_that_much__he_just_stood_there_quietly_and_watched_the_door_you_may_wish_to_consider_whether_you_have_any_enemies_who_know_you_are_in_town_a_pity_that_blood_had_to_be_spilled_in_my_establishment"),

    (assign, "$g_main_attacker_agent", 0),
	(troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_sword_viking_1", 0),
	
  (else_try),
	#(display_message, "str_wielded_item_reg3"),
	
	(lt, "$g_attacker_drawn_weapon", "itm_tutorial_spear"),
	(str_store_string, s9, "str_you_never_let_him_draw_his_weapon_still_it_looked_like_he_was_going_to_kill_you_take_his_sword_and_purse_i_suppose_he_was_trouble_but_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed"),

    (assign, "$g_main_attacker_agent", 0),
	(troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_sword_viking_1", 0),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", -1),
  (else_try),
	(neg|agent_is_alive, "$g_main_attacker_agent"),
	(str_store_string, s9, "str_well_id_say_that_he_started_it_that_entitles_you_to_his_sword_and_purse_i_suppose_have_a_drink_on_the_house_as_i_daresay_youve_saved_a_patron_or_two_a_broken_skull_still_i_hope_he_still_has_a_pulse_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed"),
    (assign, "$g_main_attacker_agent", 0),
	(troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_sword_viking_1", 0),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", 1),
  (try_end),	
  (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
  ],
   "{!}{s9}", "player_duel_response", [
   ]],

   
  [anyone, "start", [
  (is_between, "$g_talk_troop", tavernkeepers_begin, tavernkeepers_end),
  (gt, "$g_main_attacker_agent", 0),
  (try_begin),
	(get_player_agent_no, ":player_agent"),
	(agent_get_wielded_item, ":wielded_item", ":player_agent", 0),
	(is_between, ":wielded_item", "itm_darts", "itm_torch"),
	(neq, ":wielded_item", "itm_javelin_melee"),
	(neq, ":wielded_item", "itm_throwing_spear_melee"),
	(neq, ":wielded_item", "itm_jarid_melee"),
	(neq, ":wielded_item", "itm_light_throwing_axes_melee"),
	(neq, ":wielded_item", "itm_throwing_axes_melee"),
	(neq, ":wielded_item", "itm_heavy_throwing_axes_melee"),
	(str_store_string, s9, "str_stop_no_shooting_no_shooting"),

    (assign, ":default_item", -1),
	(troop_get_inventory_capacity, ":end_cond", "trp_player"), 
	(try_for_range, ":i_slot", 0, ":end_cond"),
      (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
      
      (is_between, ":item_id", weapons_begin, weapons_end),
      (neg|is_between, ":item_id", ranged_weapons_begin, ranged_weapons_end),
      
      (assign, ":default_item", ":item_id"),
      (assign, ":end_cond", 0), #break
    (try_end),
	
	(agent_set_wielded_item, ":player_agent", ":default_item"),
  (else_try),
	(str_store_string, s9, "str_em_ill_stay_out_of_this"),
  (try_end),
  ],
   "{!}{s9}", "close_window", [
   ]],

  [anyone|plyr, "player_duel_response", [],
   "Such a waste...", "close_window", [
   ]],
   
  [anyone|plyr, "player_duel_response", [],
   "Better him than me", "close_window", [
   ]],

   
  [anyone|plyr, "drunk_response", [],
   "I'm not sure... Some sort of animal, clearly", "drunk_fight_start", [
   ]],
   
  [anyone|plyr, "drunk_response", [],
   "Excuse me -- please accept my apologies", "drunk_fight_start", [
   ]],
   
  [anyone, "drunk_fight_start", [],
   "I'll wipe that smirk right off your face!", "close_window", [
	(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, 0),	
   ]],
      
  [anyone|plyr, "drunk_response", 
  [
    (troop_slot_ge, "trp_player", slot_troop_renown, 150),
  ],
   "Do you have any idea who I am?", "drunk_player_high_renown", [
   ]],

  [anyone, "drunk_player_high_renown", [
  (eq, "$g_talk_troop", "trp_hired_assassin"),
  ],
   "Do I care?", "drunk_fight_start", [
   ]],
   
  [anyone, "drunk_player_high_renown", [],
   "Emmm... Actually... Yes, yes, I do know who you are, {sir/madame}. Please forgive me, your grace -- it must be the drink. I'll be leaving, now...", "drunk_player_high_renown", [
   ]],
   
  [anyone|plyr, "drunk_player_high_renown", [],
   "Why, if you want a fight, you shall have one!", "drunk_fight_start", [
   ]],
   
  [anyone|plyr, "drunk_player_high_renown", [],
   "I thought as much. Now, remove yourself from here", "close_window", 
   [
     (assign, "$drunks_dont_pick_fights", 1),
     (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, 0),
          
     (call_script, "script_deactivate_tavern_attackers"),
     
     (assign, "$g_belligerent_drunk_leaving", "$g_main_attacker_agent"),
     
     (mission_enable_talk),
     
     (try_for_agents, ":agent"),
       (agent_is_alive, ":agent"),
       (agent_get_position, pos4, ":agent"),
       (agent_set_scripted_destination, ":agent", pos4),
     (try_end),
     
     (entry_point_get_position, pos1, 0),
     (agent_set_scripted_destination, "$g_main_attacker_agent", pos1),
     
     (assign, "$g_main_attacker_agent", 0),
   ]],
   
   
   [anyone, "start", 
   [
	 (eq, "$g_talk_troop", "trp_fight_promoter"),	
   ],
   "You look like a {fellow/lady} who can take a few hard knocks -- and deal them out, too. I have a business proposition for you.", "fistfight_response", [
   ]],
   
  [anyone|plyr, "fistfight_response", [],
   "How's that?", "fistfight_response_2", [
   ]],

  [anyone, "fistfight_response_2", [
  ],
   "Good -- I'm glad you're interested. Here's the plan... It's a little complicated, so listen well. ", "fistfight_response_2a", [
   ]],

  [anyone, "fistfight_response_2a", [
  ],
	"You and this other fellow will start up a fight here. No weapons, no armor -- I'll sit back and take bets, and split the profits with the winner. If we make a loss, then I'll cover it. You've got nothing to lose -- except a bit of blood, of course.", "fistfight_response_3", [
   ]],

  [anyone, "fistfight_response_3", [
  ],
   "However, we can't organize this like one of those nice arena bouts, where everyone places their bets beforehand. People will walk in, drawn by the noise, and put a denar or two on whichever one of your two they think is winning. I'll give 'em even odds -- anything else is going to be too tricky for someone who's already on his third flagon of ale.", "fistfight_response_4", [
   ]],
   
  [anyone, "fistfight_response_4", [
  ],
   "So, as you can see, the trick is to stretch things out for as long as possible where it looks like you're losing, and people bet against you -- and then come back fast, and win, before the betting can turn. The best way to make money is for you to be battered almost to the floor, and then jump back off your feet and take the other guy down. However, you have to win in the end in order for me, and you, to make money. ", "fistfight_response_4a", [
   ]],
   
  [anyone, "fistfight_response_4a", [
  ],
   "Also, you can't stretch the fight out too long, or people will suspect a fix. So, one of you has to take a punch every so often. I don't care whose blood is spilled, but there has to be some blood.", "fistfight_response_5", [
   ]],

  [anyone, "fistfight_response_5", [
  ],
   "And one other thing -- my mate, your opponent, he doesn't take to well to complexity. So he's just going to come straight at you. It's up to you to supply the artistry.", "fistfight_response_5a", [
   ]],
   
  [anyone, "fistfight_response_5a", [
  ],
   "So, what do you think?", "fistfight_response_confirm", [
   ]],

  [anyone|plyr, "fistfight_response_confirm", [
  ],
   "{!}[Yes -- not yet implemented]", "close_window", [
   ]],

  [anyone|plyr, "fistfight_response_confirm", [
  ],
   "I have better things to do", "close_window", [
   ]],
   
   
   
  [trp_ramun_the_slave_trader, "start", [
   (troop_slot_eq, "$g_talk_troop", slot_troop_met_previously, 0),
   ], "Good day to you, {young man/lassie}.", "ramun_introduce_1",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_1", [], "Forgive me, you look like a trader, but I see none of your merchandise.", "ramun_introduce_2",[
   (troop_set_slot, "$g_talk_troop", slot_troop_met_previously, 1),
  ]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_1", [], "Never mind.", "close_window",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_2", [], "A trader? Oh, aye, I certainly am that.\
 My merchandise is a bit different from most, however. It has to be fed and watered twice a day and tries to run away if I turn my back.", "ramun_introduce_3",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_3", [], "Livestock?", "ramun_introduce_4",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_4", [], "Close enough. I like to call myself the man who keeps every boat on this ocean moving.\
 Boats are driven by oars, you see, and oars need men to pull them or they stop. That's where I come in.", "ramun_introduce_5",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_5", [], "Galley slaves.", "ramun_introduce_6",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_6", [], "Now you're catching on! A trading port like this couldn't survive without them.\
 The ships lose a few hands on every voyage, so there's always a high demand. The captains come to me and they pay well.", "ramun_introduce_7",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_7", [], "Where do the slaves come from?", "ramun_introduce_8",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_8", [], "Mostly I deal in convicted criminals bought from the authorities.\
 Others are prisoners of war from various nations, brought to me because I offer the best prices.\
 However, on occasion I'll buy from privateers and other . . . 'individuals'. You can't be picky about your suppliers in this line of work.\
 You wouldn't happen to have any prisoners with you, would you?", "ramun_introduce_9",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_9", [], "Me? ", "ramun_introduce_10",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_10", [], "Why not? If you intend to set foot outside this town,\
 you're going to cross swords with someone sooner or later. And, God willing, you'll come out on top.\
 Why not make some extra money off the whole thing? Take them alive, bring them back to me, and I'll pay you fifty denars for each head.\
 Don't much care who they are or where they come from.", "ramun_introduce_11",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_11", [], "Hmm. I'll think about it.", "ramun_introduce_12",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_12", [], "Do think about it!\
 There's a lot of silver to be made, no mistake. More than enough for the both of us.", "close_window",[]],

  [trp_ramun_the_slave_trader,"start", [], "Hello, {playername}.", "ramun_talk",[]],
  [trp_ramun_the_slave_trader,"ramun_pre_talk", [], "Anything else?", "ramun_talk",[]],

  [trp_ramun_the_slave_trader|plyr,"ramun_talk",
   [[store_num_regular_prisoners,reg(0)],[ge,reg(0),1]],
   "I've brought you some prisoners, Ramun. Would you like a look?", "ramun_sell_prisoners",[]],
  [trp_ramun_the_slave_trader,"ramun_sell_prisoners", [],
  "Let me see what you have...", "ramun_sell_prisoners_2",
   [[change_screen_trade_prisoners]]],
  [trp_ramun_the_slave_trader, "ramun_sell_prisoners_2", [], "A pleasure doing business with you.", "close_window",[]],

  [trp_ramun_the_slave_trader|plyr,"ramun_talk", [(neg|troop_slot_ge,"$g_talk_troop",slot_troop_met_previously,1)], "How do I take somebody as prisoner?", "ramun_ask_about_capturing",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_talk", [(troop_slot_ge,"$g_talk_troop", slot_troop_met_previously, 1)], "Can you tell me again about capturing prisoners?", "ramun_ask_about_capturing",[(troop_set_slot,"$g_talk_troop", slot_troop_met_previously, 2)]],

  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing", [(neg|troop_slot_ge,"$g_talk_troop",slot_troop_met_previously,1)],
 "You're new to this, aren't you? Let me explain it in simple terms.\
 The basic rule of taking someone prisoner is knocking him down with a blunt weapon, like a mace or a club,\
 rather than cutting him open with a sword. That way he goes to sleep for a little while rather than bleeding to death, you see?\
 I'm assuming you have a blunt weapon with you . . .", "ramun_have_blunt_weapon",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_have_blunt_weapon", [],
 "Of course.", "ramun_have_blunt_weapon_yes",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_have_blunt_weapon", [],
 "As a matter of fact, I don't.", "ramun_have_blunt_weapon_no",[]],
  [trp_ramun_the_slave_trader,"ramun_have_blunt_weapon_yes", [],
 "Good. Then all you need to do is beat the bugger down with your weapon, and when the fighting's over you clap him in irons.\
 It's a bit different for nobles and such, they tend to be protected enough that it won't matter what kind of weapon you use,\
 but your average rabble-rouser will bleed like a stuck pig if you get him with something sharp. I don't have many requirements in my merchandise,\
 but I do insist they be breathing when I buy them.", "ramun_ask_about_capturing_2",[]],
  [trp_ramun_the_slave_trader,"ramun_have_blunt_weapon_no", [],
 "No? Heh, well, this must be your lucky day. I've got an old club lying around that I was going to throw away.\
 It a bit battered, but still good enough bash someone until he stops moving.\
 Here, have it.","ramun_have_blunt_weapon_no_2",[(troop_add_item, "trp_player","itm_club",imod_cracked)]],
  [trp_ramun_the_slave_trader|plyr,"ramun_have_blunt_weapon_no_2", [],
 "Thanks, Ramun. Perhaps I may try my hand at it.", "ramun_have_blunt_weapon_yes",[]],
  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing", [],
 "Alright, I'll try and expain it again in simple terms. The basic rule of taking someone prisoner is knocking him down with a blunt weapon, like a mace or a club,\
 rather than cutting him open with a sword. That way he goes to sleep for a little while rather than bleeding to death, you see?\
 It's a bit different for nobles and such, they tend to be protected enough that it won't matter what kind of weapon you use,\
 but your average rabble-rouser will bleed like a stuck pig if you get him with something sharp.", "ramun_ask_about_capturing_2",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_ask_about_capturing_2", [], "Alright, I think I understand. Anything else?", "ramun_ask_about_capturing_3",[]],
  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing_3", [],
 "Well, it's not as simple as all that. Blunt weapons don't do as much damage as sharp ones, so they won't bring your enemies down as quickly.\
 And trust me, given the chance, most of the scum you run across would just as soon kill you as look at you, so don't expect any courtesy when you pull out a club instead of a sword.\
 Moreover, having to drag prisoners to and fro will slow down your party, which is why some people simply set their prisoners free after the fighting's done.\
 It's madness. How could anyone turn down all that silver, eh?", "ramun_ask_about_capturing_4",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_ask_about_capturing_4", [],
 "Is that everything?", "ramun_ask_about_capturing_5",[]],
  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing_5", [],
 "Just one final thing. Managing prisoners safely is not an easy thing to do, you could call it a skill in itself.\
 If you want to capture a lot of prisoners, you should try and learn the tricks of it yourself,\
 or you won't be able to hang on to a single man you catch.", "ramun_ask_about_capturing_7",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_ask_about_capturing_7", [],
 "Thanks, I'll keep it in mind.", "ramun_pre_talk",[]],

  [trp_ramun_the_slave_trader|plyr,"ramun_talk", [], "I'd better be going.", "ramun_leave",[]],
  [trp_ramun_the_slave_trader,"ramun_leave", [], "Remember, any prisoners you've got, bring them to me. I'll pay you good silver for every one.", "close_window",[]],

  

  
  
  
  [trp_nurse_for_lady, "start", [
#  (eq, "$talk_context", tc_garden),
  ], "I humbly request that your lordship keeps his hands where I can see them.", "close_window",[]],

##  [trp_tutorial_trainer, "start", [(eq, "$tutorial_1_state", 1),], "TODO: Watch me.", "tutorial_1_1_1",[]],
##  [trp_tutorial_trainer, "tutorial_1_1_1", [], "TODO: This is up.", "tutorial_1_1_2",[(agent_set_attack_action, "$g_talk_agent", 3),]],
##  [trp_tutorial_trainer, "tutorial_1_1_2", [], "TODO: This is left.", "tutorial_1_1_3",[(agent_set_attack_action, "$g_talk_agent", 2),]],
##  [trp_tutorial_trainer, "tutorial_1_1_3", [], "TODO: This is right.", "tutorial_1_1_4",[(agent_set_attack_action, "$g_talk_agent", 1),]],
##  [trp_tutorial_trainer|plyr, "tutorial_1_1_4", [], "TODO: OK.", "close_window",[]],


#old tutorial is below

##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_award_taken", 1),], "I think you have trained enough. Perhaps you should go to Zendar for the next step of your adventure.", "close_window",[]],
##  [trp_tutorial_trainer,"start", [(store_character_level, ":player_level", "trp_player"),(gt, ":player_level", 1)], "I think you have trained enough. Perhaps you should go to Zendar for the next step of your adventure.", "close_window",[]],
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 0),], "Greetings stranger. What's your name?", "tutorial1_1",[]],
##  [trp_tutorial_trainer|plyr, "tutorial1_1", [], "Greetings sir, it's {playername}.", "tutorial1_2", []],
##  [trp_tutorial_trainer, "tutorial1_2", [], "Well {playername}, this place you see is the training ground. Locals come here to practice their combat skills. Since you are here you may have a go as well.", "tutorial1_3", []],
##  [trp_tutorial_trainer|plyr, "tutorial1_3", [], "I'd like that very much sir. Thank you.", "tutorial1_4", []],
##  [trp_tutorial_trainer, "tutorial1_4", [], "You will learn the basics of weapons and riding a horse here.\
##  First you'll begin with melee weapons. Then you'll enter an archery range to test your skills. And finally you'll see a horse waiting for you.\
##  I advise you to train in all these 3 areas. But you can skip some of them, it's up to you.", "tutorial1_6", []],
##  [trp_tutorial_trainer, "tutorial1_6", [], "Tell you what, if you destroy at least 10 dummies while training, I will give you my old knife as a reward. It's a little rusty but it's a good blade.", "tutorial1_7", []],
##  [trp_tutorial_trainer|plyr, "tutorial1_7", [], "Sounds nice, I'm ready for training.", "tutorial1_9", []],
##  [trp_tutorial_trainer, "tutorial1_9", [], "Good. Return to me when you have earned your reward.", "close_window", [(eq, "$tutorial_quest_taken", 0),
##                                                                                                                     (str_store_troop_name, 1, "trp_tutorial_trainer"),
##                                                                                                                     (str_store_party_name, 2, "p_training_ground"),
##                                                                                                                     (setup_quest_giver, "qst_destroy_dummies", "str_given_by_s1_at_s2"),
##                                                                                                                     (str_store_string, s2, "@Trainer ordered you to destroy 10 dummies in the training camp."),
##                                                                                                                     (call_script, "script_start_quest", "qst_destroy_dummies", "$g_talk_troop"),
##                                                                                                                     (assign, "$tutorial_quest_taken", 1)]],
##
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 1),
##                                  (eq, "$tutorial_quest_succeeded", 1),], "Well done {playername}. Now you earned this knife. There you go.", "tutorial2_1",[]],
##  [trp_tutorial_trainer|plyr, "tutorial2_1", [], "Thank you master.", "close_window", [(call_script, "script_end_quest", "qst_destroy_dummies"),(assign, "$tutorial_quest_award_taken", 1),(add_xp_to_troop, 100, "trp_player"),(troop_add_item, "trp_player","itm_knife",imod_chipped),]],
##
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 1),
##                                  (eq, "$tutorial_quest_succeeded", 1),], "Greetings {playername}. Feel free to train with the targets.", "tutorial2_1",[]],
##
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 1),
##                                  (eq, "$tutorial_quest_succeeded", 0),], "I don't see 10 dummies on the floor from here. You haven't earned your reward yet.", "tutorial3_1",[]],
##  [trp_tutorial_trainer|plyr, "tutorial3_1", [], "Alright alright, I was just tired and wanted to talk to you while resting.", "tutorial3_2", []],
##  [trp_tutorial_trainer, "tutorial3_2", [], "Less talk, more work.", "close_window", []],


##  [party_tpl|pt_peasant,"start", [(eq,"$talk_context",tc_party_encounter)], "Greetings traveller.", "peasant_talk_1",[(play_sound,"snd_encounter_farmers")]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_1", [[eq,"$quest_accepted_zendar_looters"]], "Greetings to you too.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_1", [[neq,"$quest_accepted_zendar_looters"],[eq,"$peasant_misunderstanding_said"]], "I have been charged with hunting down outlaws in this area...", "peasant_talk_2",[[assign,"$peasant_misunderstanding_said",1]]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_1", [[neq,"$quest_accepted_zendar_looters"],[neq,"$peasant_misunderstanding_said"]], "Greetings. I am hunting outlaws. Have you seen any around here?", "peasant_talk_2b",[]],
##  [party_tpl|pt_peasant,"peasant_talk_2", [], "I swear to God {sir/madam}. I am not an outlaw... I am just a simple peasant. I am taking my goods to the market, see.", "peasant_talk_3",[]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_3", [], "I was just going to ask if you saw any outlaws around here.", "peasant_talk_4",[]],
##  [party_tpl|pt_peasant,"peasant_talk_4", [], "Oh... phew... yes, outlaws are everywhere. They are making life miserable for us.\
## I pray to God you will kill them all.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [party_tpl|pt_peasant,"peasant_talk_2b", [], "Outlaws? They are everywhere. They are making life miserable for us.\
## I pray to God you will kill them all.", "close_window",[(assign, "$g_leave_encounter",1)]],

  [party_tpl|pt_manhunters,"start", [(eq,"$talk_context",tc_party_encounter)], "Hey, you there! You seen any outlaws around here?", "manhunter_talk_b",[]],
  [party_tpl|pt_manhunters|plyr,"manhunter_talk_b", [], "Yes, they went this way about an hour ago.", "manhunter_talk_b1",[]],
  [party_tpl|pt_manhunters,"manhunter_talk_b1", [], "I knew it! Come on, lads, lets go get these bastards! Thanks a lot, friend.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [party_tpl|pt_manhunters|plyr,"manhunter_talk_b", [], "No, haven't seen any outlaws lately.", "manhunter_talk_b2",[]],
  [party_tpl|pt_manhunters,"manhunter_talk_b2", [], "Bah. They're holed up in this country like rats, but we'll smoke them out yet. Sooner or later.", "close_window",[(assign, "$g_leave_encounter",1)]],

  [party_tpl|pt_looters|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker),], "{!}Warning: This line should never be displayed.", "looters_1",[
	(str_store_string, s11, "@It's your money or your life, {mate/girlie}. No sudden moves or we'll run you through."),
	(str_store_string, s12, "@Lucky for you, you caught me in a good mood. Give us all your coin and I might just let you live."),
	(str_store_string, s13, "@This a robbery, eh? I givin' you one chance to hand over everythin' you got, or me and my mates'll kill you. Understand?"),
	(store_random_in_range, ":random", 11, 14),
	(str_store_string_reg, s4, ":random"),
	(play_sound, "snd_encounter_looters")
  ]],
  [party_tpl|pt_looters,"looters_1", [], "{s4}", "looters_2",[]],
  [party_tpl|pt_looters|plyr,"looters_2", [[store_character_level,reg(1),"trp_player"],[lt,reg(1),4]], "I'm not afraid of you lot. Fight me if you dare!", "close_window",
   [[encounter_attack]]],
  [party_tpl|pt_looters|plyr,"looters_2", [[store_character_level,reg(1),"trp_player"],[ge,reg(1),4]], "You'll have nothing of mine but cold steel, scum.", "close_window",
   [[encounter_attack]]],

  [party_tpl|pt_village_farmers,"start", [(eq,"$talk_context",tc_party_encounter),
                                          (agent_play_sound, "$g_talk_agent", "snd_encounter_farmers"),
  ],
   " My {lord/lady}, we're only poor farmers from the village of {s11}. {reg1?We are taking our products to the market at {s12}.:We are returning from the market at {s12} back to our village.}", "village_farmer_talk",
   [(party_get_slot, ":target_center", "$g_encountered_party", slot_party_ai_object),
    (party_get_slot, ":home_center", "$g_encountered_party", slot_party_home_center),
    (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
    (str_store_party_name, s11, ":home_center"),
    (str_store_party_name, s12, ":market_town"),
    (assign, reg1, 1),
    (try_begin),
      (party_slot_eq, ":target_center", slot_party_type, spt_village),
      (assign, reg1, 0),
    (try_end),
    ]],

  [anyone|plyr,"village_farmer_talk",
  [(check_quest_active, "qst_track_down_bandits"),
   (neg|check_quest_succeeded, "qst_track_down_bandits"),
   
  ], "I am hunting a group of bandits with the following description... Have you seen them?", "farmer_bandit_information",[]],
  
  [anyone,"farmer_bandit_information", [
	(call_script, "script_get_manhunt_information_to_s15", "qst_track_down_bandits"),
  ], "{s15}", "village_farmer_talk",[]],
			
	
  [anyone|plyr,"village_farmer_talk", 
  [ 
    (store_faction_of_party, ":faction_of_villager", "$g_encountered_party"),
    
    (neq, ":faction_of_villager", "$players_kingdom"),
    (neq, ":faction_of_villager", "fac_player_supporters_faction"),
  ], 
  "We'll see how poor you are after I take what you've got!", "close_window",
   [(party_get_slot, ":home_center", "$g_encountered_party", slot_party_home_center),
    (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
    (party_get_slot, ":village_owner", ":home_center", slot_town_lord),
    (call_script, "script_change_player_relation_with_center", ":home_center", -4),
    (call_script, "script_change_player_relation_with_center", ":market_town", -2),
    (call_script, "script_change_player_relation_with_troop", ":village_owner", -2),
	(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
	
    (store_relation,":rel", "$g_encountered_party_faction","fac_player_supporters_faction"),
    (try_begin),
      (gt, ":rel", 0),
      (val_sub, ":rel", 5),
    (try_end),
	
    (val_sub, ":rel", 3),
    (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
    
    (assign,"$encountered_party_hostile",1),
    (assign,"$encountered_party_friendly",0),
    ]],
  [anyone|plyr,"village_farmer_talk", [], "Carry on, then. Farewell.", "close_window",[(assign, "$g_leave_encounter",1)]],


### COMPANIONS

  [anyone,"start", [(gt,"$g_talk_troop", 0),
                    (eq, "$g_talk_troop", "$g_player_minister"),
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop")],
   "I am at your service, {sire/my lady}", "minister_issues",[]],

   [anyone, "minister_issues",
  [
    (eq, "$cheese", 0),
   ],
   "Welcome {reg63?Lord:Lady} {playername}. It is time for you to assume the throne of your new kingdom.", "declaration_of_indep1", []],

[anyone, "declaration_of_indep1",
[
],
"Do you Swear upon this crown to accept the duty to fairly rule the peoples who have sworn their oath of loyalty to you, and to defend these lands from those who would take them by force or guile, and to continue, by the grace of the divine, to uphold your oath to your last breath, and upon your passing to provide an heir that shall take your mantle to discharge your oath and so forth to the end of days?", "declaration_of_indep2", 
[
    (assign, "$cheese", 1),
]],

[anyone|plyr, "declaration_of_indep2",
[
],
"I so swear by the grace of the Divine henceforth and to my last breath, to fairly rule the peoples of this land, provide for the defense against any who would do harm to its peoples and provide an heir to continue my bloodline to the end of days.", "declaration_of_indep2a", []],

[anyone, "declaration_of_indep2a", 
[
],
"This line should not be displayed.", "declaration_of_indep2a", []],
#自立时选文化
[anyone|plyr, "declaration_of_indep2a",
[
],
"I take this Chalice as a symbol of my divine right, and declare that our culture will follow the Old Kings of Pendor.", "declaration_of_indep3", 
[
    (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, "itm_culture_powell"),
]],

[anyone, "declaration_of_indep3",
[
],
"All Hail {reg63?King:Queen} {playername}! ^^ Long live the {reg63?King:Queen}!!!", "declaration_of_indep3", 
[
]],

[anyone|plyr, "declaration_of_indep3",
[
],
"Very good... let the mighty tremble at my coming!", "declaration_of_indep4", []],

[anyone, "declaration_of_indep4",
[
],
"Long live the {reg63?King:Queen}!!!", "close_window", []],##culturechangeforthefirsttime



  [anyone,"start", [(eq,"$g_talk_troop", "trp_temporary_minister"),
                    (neq, "$g_talk_troop", "$g_player_minister")],
   "It has been an honor to serve you, {sire/my lady}", "close_window",[]],
   
   
  [anyone,"start", [(troop_slot_eq,"$g_talk_troop", slot_troop_occupation, slto_player_companion),
                    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
                    (ge, ":num_stacks", 1),
                    (party_stack_get_troop_id, ":castle_leader", "$g_encountered_party", 0),
                    (eq, ":castle_leader", "$g_talk_troop"),
                    (eq, "$talk_context", 0)],
   "Yes, {playername}? What can I do for you?", "member_castellan_talk",[]],
  
  [anyone,"member_castellan_pretalk", [], "Anything else?", "member_castellan_talk",[]],
  
  [anyone|plyr,"member_castellan_talk", [],
   "I want to review the castle garrison.", "member_review_castle_garrison",[]],
  [anyone,"member_review_castle_garrison", [], "Of course. Here are our lists, let me know of any changes you require...", "member_castellan_pretalk",[(change_screen_exchange_members,0)]],
  [anyone|plyr,"member_castellan_talk", [],
   "Let me see your equipment.", "member_review_castellan_equipment",[]],
  [anyone,"member_review_castellan_equipment", [], "Very well, it's all here...", "member_castellan_pretalk",[(change_screen_equip_other)]],
  [anyone|plyr,"member_castellan_talk", [],
   "I want you to abandon the castle and join my party.", "member_castellan_join",[]],
  [anyone,"member_castellan_join", [(party_can_join_party,"$g_encountered_party","p_main_party")],
   "I've grown quite fond of the place... But if it is your wish, {playername}, I'll come with you.", "close_window", [
       (assign, "$g_move_heroes", 1),
       (call_script, "script_party_add_party", "p_main_party", "$g_encountered_party"),
       (party_clear, "$g_encountered_party"),
       ]],
  [anyone,"member_castellan_join", [],
   "And where would we sleep? You're dragging a whole army with you, {playername}, there's no more room for all of us.", "member_castellan_pretalk",[]],
  
  [anyone|plyr,"member_castellan_talk", [], "[Leave]", "close_window",[]],


#  [anyone,"start", [(troop_slot_eq,"$g_talk_troop", slot_troop_occupation, slto_player_companion),
#                    (neg|main_party_has_troop,"$g_talk_troop"),
#                    (eq, "$talk_context", tc_party_encounter)],
#   "{!}Do you want me to rejoin you?", "close_window",[]], # unused
#  [anyone,"start", [(neg|main_party_has_troop,"$g_talk_troop"),(eq, "$g_encountered_party", "p_four_ways_inn")], "{!}Do you want me to rejoin you?", #"close_window",[]], # unused
#  [anyone,"member_separate_inn", [], "I don't know what you will do without me, but you are the boss. I'll wait for you at the Four Ways inn.", #"close_window",
#  [anyone,"member_separate_inn", [], "All right then. I'll meet you at the four ways inn. Good luck.", "close_window",
#   [(remove_member_from_party,"$g_talk_troop", "p_main_party"),(add_troop_to_site, "$g_talk_troop", "scn_four_ways_inn", borcha_inn_entry)]],

#Quest heroes member chats

  [trp_kidnapped_girl,"member_chat", [], "Are we home yet?", "kidnapped_girl_chat_1",[]],
  [trp_kidnapped_girl|plyr,"kidnapped_girl_chat_1", [], "Not yet.", "kidnapped_girl_chat_2",[]],
  [trp_kidnapped_girl,"kidnapped_girl_chat_2", [], "I can't wait to get back. I've missed my family so much, I'd give anything to see them again.", "close_window",[]],

  [anyone,"member_chat",
   [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    ], "{playername}, when do you think we can reach our destination?", "member_lady_1",[]],
  [anyone|plyr, "member_lady_1", [],  "We still have a long way ahead of us.", "member_lady_2a", []],
  [anyone|plyr, "member_lady_1", [],  "Very soon. We're almost there.", "member_lady_2b", []],

  [anyone ,"member_lady_2a", [],  "Ah, I am going to enjoy the road for a while longer then. I won't complain.\
 I find riding out in the open so much more pleasant than sitting in the castle all day.\
 You know, I envy you. You can live like this all the time.", "close_window", []],
  [anyone ,"member_lady_2b", [],  "That's good news. Not that I don't like your company, but I did miss my little luxuries.\
 Still I am sorry that I'll leave you soon. You must promise me, you'll come visit me when you can.", "close_window", []],

  [anyone ,"member_chat", [(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),],
   "Greetings, {playername}, my first and foremost vassal. I await your counsel.", "supported_pretender_talk", []],
  [anyone ,"supported_pretender_pretalk", [],
   "Anything else?", "supported_pretender_talk", []],

  [anyone|plyr,"supported_pretender_talk", [],
   "What do you think about our progress so far?", "pretender_progress",[]],

  [anyone,"pretender_progress", [
       (assign, reg11, 0),(assign, reg13, 0),(assign, reg14, 0),(assign, reg15, 0),
       (assign, reg21, 0),(assign, reg23, 0),(assign, reg24, 0),(assign, reg25, 0),
       
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
	     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         (store_troop_faction, ":troop_faction", ":troop_no"),
         (try_begin),
           (eq, ":troop_faction", "fac_player_supporters_faction"),
           (neq, ":troop_no", "trp_player"),
           (neq, ":troop_no", "$supported_pretender"),
           (val_add, reg11, 1),
         (else_try),
           (eq, ":troop_faction", "$supported_pretender_old_faction"),
           (neg|faction_slot_eq, "$supported_pretender_old_faction", slot_faction_leader, ":troop_no"),
           (val_add, reg21, 1),
         (try_end),
       (try_end),
       (try_for_range, ":center_no", centers_begin, centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (try_begin),
           (eq, ":center_faction", "fac_player_supporters_faction"),
           (try_begin),
             (party_slot_eq, ":center_no", slot_party_type, spt_town),
             (val_add, reg13, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_castle),
             (val_add, reg14, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_village),
             (val_add, reg15, 1),
           (try_end),
         (else_try),
           (eq, ":center_faction", "$supported_pretender_old_faction"),
           (try_begin),
             (party_slot_eq, ":center_no", slot_party_type, spt_town),
             (val_add, reg23, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_castle),
             (val_add, reg24, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_village),
             (val_add, reg25, 1),
           (try_end),
         (try_end),
       (try_end),
       (store_add, reg19, reg13, reg14),
       (val_add, reg19, reg15),
       (store_add, reg29, reg23, reg24),
       (val_add, reg29, reg25),
       (store_add, ":our_score", reg13, reg14),
       (val_add, ":our_score", reg11),
       (store_add, ":their_score", reg23, reg24),
       (val_add, ":their_score", reg21),
       (store_add, ":total_score", ":our_score", ":their_score"),
       (val_mul, ":our_score", 100),
       (store_div, ":our_ratio", ":our_score", ":total_score"),
       (try_begin),
         (lt, ":our_ratio", 10),
         (str_store_string, s30, "@we have made very little progress so far"),
       (else_try),
         (lt, ":our_ratio", 30),
         (str_store_string, s30, "@we have suceeded in gaining some ground, but we still have a long way to go"),
       (else_try),
         (lt, ":our_ratio", 50),
         (str_store_string, s30, "@we have become a significant force, and we have an even chance of victory"),
       (else_try),
         (lt, ":our_ratio", 75),
         (str_store_string, s30, "@we are winning the war, but our enemies are still holding on."),
       (else_try),
         (str_store_string, s30, "@we are on the verge of victory. The remaining enemies pose no threat, but we still need to hunt them down."),
       (try_end),
       (faction_get_slot, ":enemy_king", "$supported_pretender_old_faction", slot_faction_leader),
       (str_store_troop_name, s9, ":enemy_king"),
      ],
   "{reg11?We have {reg11} lords on our side:We have no lord with us yet},\
 whereas {reg21?{s9} still has {reg21} lords supporting him:{s9} has no loyal lords left}.\
 {reg19?We control {reg13?{reg13} towns:} {reg14?{reg14} castles:} {reg15?and {reg15} villages:}:We don't control any settlements},\
 while {reg29?they have {reg23?{reg23} towns:} {reg24?{reg24} castles:} {reg25?and {reg25} villages:}:they have no remaining settlements}.\
 Overall, {s30}.", "pretender_progress_2",[]],

  [anyone|plyr,"pretender_progress_2", [],
   "Then, we must keep fighting and rally our supporters!", "supported_pretender_pretalk",[]],

  [anyone|plyr,"pretender_progress_2", [],
   "It seems this rebellion is not going anywhere. We must give up.", "pretender_quit_rebel_confirm",[]],
  
  [anyone,"pretender_quit_rebel_confirm", [],
   "{playername}, you can't abandon me now. Are you serious?", "pretender_quit_rebel_confirm_2",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_2", [],
   "Indeed, I am. I can't support you any longer.", "pretender_quit_rebel_confirm_3",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_2", [],
   "I was jesting. I will fight for you until we succeed.", "supported_pretender_pretalk",[]],
 
   [anyone,"pretender_quit_rebel_confirm_3", [],
   "Are you absolutely sure? I will never forgive you if you abandon my cause.", "pretender_quit_rebel_confirm_4",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_4", [],
   "I am sure.", "pretender_quit_rebel",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_4", [],
   "Let me think about this some more.", "supported_pretender_pretalk",[]],
 
  [anyone,"pretender_quit_rebel", [],
   "So be it. Then my cause is lost. There is only one thing to do for me now. I will go from Calradia and never come back. With me gone, you may try to make your peace with {s4}.", "close_window",
   [
     (troop_get_slot, ":original_faction", "$g_talk_troop", slot_troop_original_faction),
	 (faction_get_slot, ":original_faction_leader", ":original_faction", slot_faction_leader),
	 (str_store_troop_name, s4, ":original_faction_leader"),
	 
     (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
	   (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
	   (neq, "$supported_pretender", ":cur_troop"),
       (store_troop_faction, ":cur_faction", ":cur_troop"),
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (call_script, "script_change_troop_faction", ":cur_troop", ":original_faction"),
     (try_end),
     (troop_set_faction, "$g_talk_troop", "fac_neutral"),
     (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
     (assign, ":has_center", 0),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (store_faction_of_party, ":cur_faction", ":cur_center"),
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (assign, ":has_center", 1),
       (neg|party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
       (call_script, "script_give_center_to_lord", ":cur_center", "trp_player", 0),
     (try_end),
     (party_remove_members, "p_main_party", "$supported_pretender", 1),
     (faction_set_slot, ":original_faction", slot_faction_has_rebellion_chance, 0),
     (assign, "$supported_pretender", 0),
     (try_begin), #Still has center
       (eq, ":has_center", 1),
       (faction_set_color, "fac_player_supporters_faction", 0xFF0000),
	   (try_begin), #added to prevent no minister if player gives up rebellion
		(eq, "$g_player_minister", 0),
		(assign, "$g_player_minister", "trp_temporary_minister"),
	   (try_end), 
     (else_try), #No center
       (call_script, "script_deactivate_player_faction"),
     (try_end),
     (call_script, "script_change_player_honor", -20),
     (call_script, "script_fail_quest", "qst_rebel_against_kingdom"),
     (call_script, "script_end_quest", "qst_rebel_against_kingdom"),
    ]],


  [anyone|plyr,"supported_pretender_talk", [],
   "{reg65?My lady:My lord}, would you allow me to check out your equipment?", "supported_pretender_equip",[]],
  [anyone,"supported_pretender_equip", [], "Very well, it's all here...", "supported_pretender_pretalk",[
      (change_screen_equip_other),
      ]],

  [anyone|plyr,"supported_pretender_talk", [], "If it would please you, can you tell me about your skills?", "pretneder_view_char_requested",[]],
  [anyone,"pretneder_view_char_requested", [], "Well, all right.", "supported_pretender_pretalk",[(change_screen_view_character)]],

  
  [anyone|plyr,"supported_pretender_talk", [
  
  (assign, ":center_found", 0),
  (try_for_range, ":fief_to_grant", centers_begin, centers_end),
	(store_faction_of_party, ":fief_faction", ":fief_to_grant"),
	(eq, ":fief_faction", "fac_player_supporters_faction"),  
	(party_slot_eq, ":fief_to_grant", slot_town_lord, -1),
    (assign, ":center_found", 1),
  (try_end),
  (eq, ":center_found", 1),
  
  ],
   "I suggest that you decide who should hold a fief that does not have a lord.", "supported_pretender_grant_fief",[]],
  
  [anyone,"supported_pretender_grant_fief", [
  ],
   "Which fief did you have in mind?", "supported_pretender_grant_fief_select",[]],

  [anyone|plyr|repeat_for_parties,"supported_pretender_grant_fief_select", [
  (store_repeat_object, ":fief_to_grant"),
  (is_between, ":fief_to_grant", centers_begin, centers_end),
  (store_faction_of_party, ":fief_faction", ":fief_to_grant"),
  (eq, ":fief_faction", "fac_player_supporters_faction"),  
  (party_slot_eq, ":fief_to_grant", slot_town_lord, -1),
  (str_store_party_name, s4, ":fief_to_grant"),
  ],
   "{s4}", "supported_pretender_grant_fief_choose_recipient",[
   (store_repeat_object, "$g_center_taken_by_player_faction"),   
   ]],

  [anyone,"supported_pretender_grant_fief_choose_recipient", [
  ],
   "And who should receive it?", "center_captured_rebellion",[
   (str_store_party_name, s4, "$g_center_taken_by_player_faction"),
   ]],
   
  [anyone|plyr,"supported_pretender_grant_fief_select", [
  ],
   "Never mind.", "supported_pretender_pretalk",[]],
  
  
  

  [anyone|plyr,"supported_pretender_talk", [],
   "Let us keep going, {reg65?my lady:sir}.", "close_window",[]],








#伙伴NPC  
  [anyone,"do_member_trade", [], "Anything else?", "member_talk",[]],

  [anyone,"member_pretalk", [], "Anything else?", "member_talk",[]],


  [anyone,"member_chat", 
  [
    (store_conversation_troop,"$g_talk_troop"),
    (troop_is_hero,"$g_talk_troop"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ], "Yes, {s5}?", "member_talk",
  [
    (try_begin),
      (is_between, "$g_talk_troop", companions_begin, companions_end),
      (unlock_achievement, ACHIEVEMENT_TALKING_HELPS),
    (try_end),
  ]],
						  
  [anyone|plyr,"member_talk", [ (main_party_has_troop,"$g_talk_troop"),
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(faction_slot_eq,  "$players_kingdom", slot_faction_marshall, "trp_player"),
  ], "As marshal, I wish you to send a message to the vassals of the realm", "member_direct_campaign",[]],


  [anyone|plyr,"member_talk", [ (gt, "$auxiliary_number", 0),], "I wish you to call up my auxiliaries", "call_up_all_auxiliary",[]],
  [anyone,"call_up_all_auxiliary", [], "Who do you want to call up", "call_up_all_auxiliary_1",[]],
  [anyone|plyr,"call_up_all_auxiliary_1", [], "Okey", "call_up_all_auxiliary_2",[#all
     (try_for_range, ":npc_no", companions_begin, companions_end),
          (troop_get_slot, ":auxiliary_no", ":npc_no", slot_troop_leading_auxiliary),
          (neq, ":auxiliary_no", 0),
          (try_begin),
              (party_get_attached_to, ":cur_attached_center", ":auxiliary_no"),#detatch from center garrison
              (ge, ":cur_attached_center", 1),
              (party_detach, ":auxiliary_no"),
          (try_end),
          (party_set_slot, ":auxiliary_no", slot_party_orders_type, spai_accompanying_army),
          (party_set_slot, ":auxiliary_no", slot_party_orders_object, "p_main_party"),
     (try_end),]],
  [anyone|plyr|repeat_for_parties,"call_up_all_auxiliary_1", [
     (store_repeat_object, ":party_no"),
     (assign, ":continue", 0),
     (try_begin),
          (party_get_slot, ":party_type", ":party_no", slot_party_type),
          (eq, ":party_type", spt_attendant_party),
          (store_faction_of_party, ":party_faction", ":party_no"),
          (eq, ":party_faction", "fac_player_supporters_faction"),
          (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     (str_store_party_name, s2, ":party_no"), 
], "{s2}", "call_up_all_auxiliary_2",[(store_repeat_object, ":party_no"),
          (try_begin),
              (party_get_attached_to, ":cur_attached_center", ":party_no"),
              (ge, ":cur_attached_center", 1),
              (party_detach, ":party_no"),
          (try_end),
          (party_set_slot, ":party_no", slot_party_orders_type, spai_accompanying_army),
          (party_set_slot, ":party_no", slot_party_orders_object, "p_main_party"),]],
  [anyone|plyr,"call_up_all_auxiliary_1", [], "Never mind", "member_pretalk",[]],
  [anyone,"call_up_all_auxiliary_2", [], "Okey", "member_pretalk",[]],

#分出支队
  [anyone|plyr,"member_talk", [    (main_party_has_troop,"$g_talk_troop"),(store_troop_gold, ":gold", "trp_player"),(ge, ":gold", 1000)], "I want you to lead some of my men.", "member_create_attendant_perty",[]],
  [anyone,"member_create_attendant_perty", [(party_get_skill_level, ":tatics", "trp_player", skl_tactics),(val_sub, ":tatics", 3), (gt, ":tatics", "$auxiliary_number")], "Thank you for your trust.", "close_window",[
  (call_script, "script_create_auxiliary_forces", "$g_talk_troop"),(remove_member_from_party,"$g_talk_troop","p_main_party"),(val_add, "$auxiliary_number", 1),(call_script, "script_change_player_relation_with_troop","$g_talk_troop", 20),(troop_remove_gold,"trp_player",1000)]],
  [anyone|plyr,"member_create_attendant_perty", [], "thinking.", "member_talk",[]],

#与分队交换兵种	  
  [anyone|plyr,"member_talk", [(neg|main_party_has_troop,"$g_talk_troop"),(party_is_active,"$g_encountered_party"),
    (party_slot_eq,"$g_encountered_party",slot_party_type, spt_attendant_party),], "I want exchange soldiers", "exchange_solider",[(change_screen_exchange_members)]],
  [anyone|plyr,"exchange_solider", [], "That's all. report your condition.", "exchange_solider_1",[]],
  [anyone,"exchange_solider_1", [
        (store_encountered_party,":party_no"),
        (call_script, "script_party_count_fit_regulars", ":party_no"),
        (assign, reg1, reg0),
        (call_script, "script_caculate_auxiliary_limit", ":party_no"),
        (assign, reg2, reg0),
        (gt, reg1, reg2),
        (store_sub,"$auxiliary_addition_bill",reg1,reg2),
        (val_mul, "$auxiliary_addition_bill", 50),
        (assign, reg3, "$auxiliary_addition_bill")], "I can carries {reg2}, but there are {reg1}, or you should pay {reg3}", "exchange_solider_2",[]],
  [anyone,"exchange_solider_1", [        (store_encountered_party,":party_no"),(call_script, "script_party_count_fit_regulars", ":party_no"),
        (assign, reg1, reg0),        (call_script, "script_caculate_auxiliary_limit", ":party_no"),
        (assign, reg2, reg0),(le, reg1, reg2)], "I can carries {reg2}, there are {reg1},all right, ", "do_member_trade",[]],

  [anyone|plyr,"exchange_solider_2", [], "Okey I think twice", "exchange_solider",[(change_screen_exchange_members)]],
  [anyone|plyr,"exchange_solider_2", [], "No I ask you to", "do_member_trade",[(store_encountered_party,":party_no"),(call_script, "script_change_party_morale",":party_no", -20), (call_script, "script_change_player_relation_with_troop","$g_talk_troop", -20)]],
  [anyone|plyr,"exchange_solider_2", [(store_troop_gold, ":gold", "trp_player"),(ge, ":gold", "$auxiliary_addition_bill")], "No I pay for it", "do_member_trade",[(troop_remove_gold,"trp_player","$auxiliary_addition_bill"),]],

#解散支队，收回士兵
  [anyone|plyr,"member_talk", [(neg|main_party_has_troop,"$g_talk_troop"),(party_is_active,"$g_encountered_party"),
    (party_slot_eq,"$g_encountered_party",slot_party_type, spt_attendant_party),], "I want dissolute this auxiliary party.", "auxiliary_dissolute_1",[]],
  [anyone,"auxiliary_dissolute_1", [], "Why", "auxiliary_dissolute_2",[]],
  [anyone|plyr,"auxiliary_dissolute_2", [], "Obey my order", "auxiliary_dissolute_4",[(party_join),(call_script, "script_change_player_relation_with_troop","$g_talk_troop", -20),(val_sub, "$auxiliary_number", 1),]],
  [anyone|plyr,"auxiliary_dissolute_2", [], "Persuade", "auxiliary_dissolute_3",[]],
  [anyone|plyr,"auxiliary_dissolute_2", [], "let me think twice.", "member_pretalk",[]],
  [anyone,"auxiliary_dissolute_3", [(party_get_skill_level, ":persuasion", "trp_player", skl_persuasion),(ge, ":persuasion", 5)], "All_right", "auxiliary_dissolute_4",[(party_join),(val_sub, "$auxiliary_number", 1), ]],
  [anyone,"auxiliary_dissolute_3", [(party_get_skill_level, ":persuasion", "trp_player", skl_persuasion),(lt, ":persuasion", 5)], "Dont say that", "auxiliary_dissolute_2",[(call_script, "script_change_player_relation_with_troop","$g_talk_troop", -3)]],
  [anyone,"auxiliary_dissolute_4", [], "I listent to you", "close_window",[          (troop_set_slot,"$g_talk_troop",slot_troop_leading_auxiliary, 0),]],


  [anyone|plyr,"member_talk", [(neg|main_party_has_troop,"$g_talk_troop"),(party_is_active,"$g_encountered_party"),
    (party_slot_eq,"$g_encountered_party",slot_party_type, spt_attendant_party),], "I have some orders.", "auxiliary_give_order_1",[]],
  [anyone,"auxiliary_give_order_1", [], "For what?", "auxiliary_give_order_2",[]],

  [anyone|plyr,"auxiliary_give_order_2", [], "Stay here", "member_pretalk",[
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_type, spai_undefined),
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_object, "p_main_party"),]],              #special order
  [anyone|plyr,"auxiliary_give_order_2", [], "Follow me", "auxiliary_give_order_5",[
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_type, spai_accompanying_army),
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_object, "p_main_party"),]],              #special order
  [anyone|plyr,"auxiliary_give_order_2", [], "Patrol around me", "auxiliary_give_order_6",[
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_type, spai_patrolling_around_center),
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_object, "p_main_party"),]],               #special order
  [anyone|plyr,"auxiliary_give_order_2", [], "Hide in...", "auxiliary_give_order_3",[
          (assign, "$temp", spai_retreating_to_center),]],
  [anyone|plyr,"auxiliary_give_order_2", [], "Hold ...", "auxiliary_give_order_3",[
          (assign, "$temp", spai_holding_center),]],
  [anyone|plyr,"auxiliary_give_order_2", [], "Patrol aound...", "auxiliary_give_order_3",[
          (assign, "$temp", spai_patrolling_around_center),]],                                                     #patrol around a center
  [anyone|plyr,"auxiliary_give_order_2", [], "Beseige..", "auxiliary_give_order_3",[
          (assign, "$temp", spai_besieging_center),]],
  [anyone|plyr,"auxiliary_give_order_2", [], "Nothing", "member_pretalk",[]],

  [anyone,"auxiliary_give_order_3", [], "Where", "auxiliary_give_order_4",[]],
  [anyone|plyr|repeat_for_parties,"auxiliary_give_order_4", [
     (store_repeat_object, ":party_no"),
     (store_faction_of_party, ":party_faction", ":party_no"),
     (store_relation, ":relation", ":party_faction", "fac_player_supporters_faction"),
     (assign, ":continue", 0),
     (try_begin),
       (eq, "$temp", spai_retreating_to_center),#hide in a town
       (try_begin),
         (party_slot_eq, ":party_no", slot_party_type, spt_town),#only town, because npc will appear in the tavern
         (ge, ":relation", 0),
         (assign, ":continue", 1),
       (try_end),
     (else_try),
       (eq, "$temp", spai_holding_center),#hold a center
       (try_begin),
         (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(party_slot_eq, ":party_no", slot_party_type, spt_town),
         (eq, ":party_faction", "fac_player_supporters_faction"),
         (assign, ":continue", 1),
       (try_end),
     (else_try),
       (eq, "$temp", spai_patrolling_around_center),#patrol around a center
       (try_begin),
         (ge, ":relation", 0),
         (is_between, ":party_no", centers_begin, centers_end),
         (assign, ":continue", 1),
	   (else_try),	 
         (is_between, ":party_no", centers_begin, centers_end),	   
		 (store_distance_to_party_from_party, ":distance", ":party_no", "p_main_party"),
		 (le, ":distance", 25),
         (assign, ":continue", 1),		 
       (try_end),
     (else_try),
       (eq, "$temp", spai_besieging_center),#attack a city
       (try_begin),
         (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(party_slot_eq, ":party_no", slot_party_type, spt_town),
		 (party_slot_eq, ":party_no", slot_center_is_besieged_by, -1),
         (lt, ":relation", 0),
         (assign, ":continue", 1),
       (try_end),	   	   
     (try_end),
     (eq, ":continue", 1),
     (neq, ":party_no", "$g_encountered_party"),
     (str_store_party_name, s1, ":party_no"),
     (str_store_faction_name, s2, ":party_faction")], "{s1} of {s2}", "auxiliary_give_order_5",[
          (store_repeat_object, ":temp_order_2"),
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_object, ":temp_order_2"),
          (party_set_slot, "$g_talk_troop_party", slot_party_orders_type, "$temp"),]],
  [anyone|plyr, "auxiliary_give_order_4", [], "Never mind.", "member_pretalk",[]],
  [anyone,"auxiliary_give_order_5", [], "I get it", "member_pretalk",[]],

  [anyone,"auxiliary_give_order_6", [], "How far should I patrol?", "auxiliary_give_order_7",[]],
  [anyone|plyr,"auxiliary_give_order_7", [], "radius", "member_pretalk",[(party_set_ai_patrol_radius,"$g_talk_troop_party",1),(party_set_ai_initiative,"$g_talk_troop_party",20),(party_set_courage, "$g_talk_troop_party", 10),(party_set_aggressiveness, "$g_talk_troop_party", 6),]],
  [anyone|plyr,"auxiliary_give_order_7", [], "radius_1", "member_pretalk",[(party_set_ai_patrol_radius,"$g_talk_troop_party",2),(party_set_ai_initiative,"$g_talk_troop_party",40),(party_set_courage, "$g_talk_troop_party", 10),(party_set_aggressiveness, "$g_talk_troop_party", 8),]],
  [anyone|plyr,"auxiliary_give_order_7", [], "radius_2", "member_pretalk",[(party_set_ai_patrol_radius,"$g_talk_troop_party",3),(party_set_ai_initiative,"$g_talk_troop_party",60),(party_set_courage, "$g_talk_troop_party", 10),(party_set_aggressiveness, "$g_talk_troop_party", 10),]],
  [anyone|plyr,"auxiliary_give_order_7", [], "radius_3", "member_pretalk",[(party_set_ai_patrol_radius,"$g_talk_troop_party",4),(party_set_ai_initiative,"$g_talk_troop_party",80),(party_set_courage, "$g_talk_troop_party", 10),(party_set_aggressiveness, "$g_talk_troop_party", 12),]],
  [anyone|plyr,"auxiliary_give_order_7", [], "radius_4", "member_pretalk",[(party_set_ai_patrol_radius,"$g_talk_troop_party",5),(party_set_ai_initiative,"$g_talk_troop_party",100),(party_set_courage, "$g_talk_troop_party", 10),(party_set_aggressiveness, "$g_talk_troop_party", 15),]],

## CC
  [anyone|plyr,"member_talk",
    [
      (try_begin),
        (eq, "$g_weapons_set_no", 0),
        (assign, reg1, 2),
      (else_try),
        (assign, reg1, 1),
      (try_end),
    ],
   "Toggle weapons to set {reg1} for all heroes.", "toggle_weapons",[]],
  [anyone,"toggle_weapons",
    [
      (try_begin),
        (eq, "$g_weapons_set_no", 0),
        (assign, reg1, 2),
      (else_try),
        (assign, reg1, 1),
      (try_end),
    ],
    "OK, all heroes in our party include you will toggle weapons to set {reg1}.", "do_member_trade",
    [
      (val_add, "$g_weapons_set_no", 1),
      (val_mod, "$g_weapons_set_no", 2),
      # strict_mode
      (call_script, "script_all_toggle_weapons_set", 1),
    ]],
## CC

  [anyone|plyr,"member_talk", [],

   "Let me see your equipment.", "member_trade",
   [
    ## CC
    # strict_mode
    (call_script, "script_all_toggle_weapons_set", 1),
    ## CC
   ]],
  [anyone,"member_trade", [], "Very well, it's all here...", "do_member_trade",[
#      (change_screen_trade)
      (change_screen_equip_other),
      ]],

  [anyone,"do_member_trade", [], "Anything else?", "member_talk",[]],

  [anyone|plyr,"member_talk", [], "What can you tell me about your skills?", "view_member_char_requested",[]],
  [anyone,"view_member_char_requested", [], "All right, let me tell you...", "do_member_view_char",[(change_screen_view_character)]],

  [anyone|plyr,"member_talk", [ (main_party_has_troop,"$g_talk_troop"),], "We need to separate for a while.", "member_separate",[
            (call_script, "script_npc_morale", "$g_talk_troop"),
            (assign, "$npc_quit_morale", reg0),
      ]],

  [anyone,"member_separate", [
            (gt, "$npc_quit_morale", 30),
      ], "Oh really? Well, I'm not just going to wait around here. I'm going to go to the towns to look for other work. Is that what you want?", "member_separate_confirm",
   []],

  [anyone,"member_separate", [
      ], "Well, actually, there was something I needed to tell you.", "companion_quitting",
   [
        (assign, "$player_can_refuse_npc_quitting", 0),
        (assign, "$player_can_persuade_npc", 0),
       ]],


  [anyone|plyr,"member_separate_confirm", [], "That's right. We need to part ways.", "member_separate_yes",[]],
  [anyone|plyr,"member_separate_confirm", [], "No, I'd rather have you at my side.", "do_member_trade",[]],

  [anyone,"member_separate_yes", [
      ], "Well. I'll be off, then. Look me up if you need me.", "close_window",
   [
            (troop_set_slot, "$g_talk_troop", slot_troop_occupation, 0),
            (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_dismissed),
            (remove_member_from_party, "$g_talk_troop"),
       ]],


  [anyone|plyr,"member_talk", [], "I'd like to ask you something.", "member_question",[]],

  [anyone|plyr,"member_talk", [], "Never mind.", "close_window",
  [
    ## CC
    # not strict_mode, toggle to none-empty weapons_set
    (call_script, "script_all_toggle_weapons_set", 0),
    ## CC
  ]],

  [anyone,"member_question", [], "Very well. What did you want to ask?", "member_question_2",[]],

  [anyone|plyr,"member_question_2", [], "How do you feel about the way things are going in this company?", "member_morale",[]],
  [anyone|plyr,"member_question_2", [], "Tell me your story again.", "member_background_recap",[]],
  [anyone|plyr,"member_question_2", [ (main_party_has_troop,"$g_talk_troop"),
	(troop_slot_eq, "$g_talk_troop", slot_troop_kingsupport_state, 0),
  ], "I suppose you know that I aspire to be {king/queen} of this land?", "member_kingsupport_1",[]],

  [anyone|plyr,"member_question_2", [ (main_party_has_troop,"$g_talk_troop"),
  ], "Do you have any connections that we could use to our advantage?", "member_intelgathering_1",[]],
  
  [anyone|plyr,"member_question_2", [ (main_party_has_troop,"$g_talk_troop"),
	(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
  ], "Would you be interested in holding a fief?", "member_fief_grant_1",[]],
  
  
  [anyone,"member_morale", [
        (call_script, "script_npc_morale", "$g_talk_troop"),
      ], "{s21}", "do_member_trade",[]],

  [anyone,"member_background_recap", [
          (troop_get_slot, ":first_met", "$g_talk_troop", slot_troop_first_encountered),
          (str_store_party_name, 20, ":first_met"),
          (troop_get_slot, ":home", "$g_talk_troop", slot_troop_home),
          (str_store_party_name, 21, ":home"),
          (troop_get_slot, ":recap", "$g_talk_troop", slot_troop_home_recap),
          (str_store_string, 5, ":recap"),
      ], "{s5}", "member_background_recap_2",[]],

  [anyone,"member_background_recap_2", [
          (str_clear, 19),
          (troop_get_slot, ":background", "$g_talk_troop", slot_troop_backstory_b),
          (str_store_string, 5, ":background"),
      ], "{s5}", "member_background_recap_3",[]],

	  [anyone,"member_background_recap_3", [
      ], "Then shortly after, I joined up with you.", "do_member_trade",[]],

  [anyone,"do_member_view_char", [], "Anything else?", "member_talk",[]],

  
  [anyone,"member_kingsupport_1", [
		 (troop_get_slot, ":morality_grievances", "$g_talk_troop", slot_troop_morality_penalties),
		 (gt, ":morality_grievances", 10),
        ], "Um... Yes. I had heard.", "do_member_trade",[]],

  [anyone,"member_kingsupport_1", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_1", ":npc_no"),
#		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_1),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_1a",[]],
  
  [anyone|plyr,"member_kingsupport_1a", [
        ], "Would you then support my cause?", "member_kingsupport_2",[]],

  [anyone|plyr,"member_kingsupport_1a", [
        ], "Very good. I shall keep that in mind.", "do_member_trade",[]],


  [anyone,"member_kingsupport_2", [
		(assign, ":companion_already_on_mission", -1),
		(try_for_range, ":companion", companions_begin, companions_end),
			(troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
			(troop_get_slot, ":days_on_mission", ":companion", slot_troop_days_on_mission),
			(gt, ":days_on_mission", 17),
			(neg|main_party_has_troop, ":companion"),
			(assign, ":companion_already_on_mission", ":companion"),
		(try_end),

		(gt, ":companion_already_on_mission", -1),
		(troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
		(str_store_string, s21, ":honorific"),
		(str_store_troop_name, s22, ":companion_already_on_mission"),

		], "I would, {s21}. Moreover, I have a proposal on how I might help you attain your throne. But you recently sent {s22} off on a similar mission. Perhaps we should wait for a couple of weeks to avoid drawing too much attention to ourselves.", "do_member_trade",[]],

		
  [anyone,"member_kingsupport_2", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_2", ":npc_no"),
#		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_2),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_2a",[]],
  
  [anyone|plyr,"member_kingsupport_2a", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_2a", ":npc_no"),
#  		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_2a),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_3",[]],

  [anyone|plyr,"member_kingsupport_2a", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_2b", ":npc_no"),
#    	 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_2b),
		 (str_store_string, s21, ":string"),

        ], "{s21}", "do_member_trade",[]],

  [anyone,"member_kingsupport_3", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_3", ":npc_no"),
#		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_3),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_3a",[]],


  [anyone|plyr,"member_kingsupport_3a", [
        ], "Very good. You do that", "member_kingsupport_4",[
		]],

  [anyone|plyr,"member_kingsupport_3a", [
        ], "On second thought, stay with me for a while", "do_member_trade",[]],

  [anyone,"member_kingsupport_4", [
  		 (troop_set_slot, "$g_talk_troop", slot_troop_days_on_mission, 21),
  		 (troop_set_slot, "$g_talk_troop", slot_troop_current_mission, npc_mission_kingsupport),

		 (remove_member_from_party, "$g_talk_troop", "p_main_party"),
		 		 
		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_honorific),
		 (str_store_string, s21, ":string"),

		 ], "Farewell then, {s21}, for a little while", "close_window",[]],

  [anyone,"member_intelgathering_1", [
		 (troop_get_slot, ":town_with_contacts", "$g_talk_troop", slot_troop_town_with_contacts),
		 (str_store_party_name, s17, ":town_with_contacts"),
		 (store_faction_of_party, ":contact_town_faction", ":town_with_contacts"),
		 (str_store_faction_name, s18, ":contact_town_faction"),
		 
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":connections_string", "str_npc1_intel_mission", ":npc_no"),
		 (str_store_string, s21, ":connections_string"),
		 ], "{s21}", "member_intelgathering_3",[]],
		
  [anyone,"member_intelgathering_3", [ #change back to member_intelgathering_2 if this will be used
		(eq, 1, 0),
  ], "Of course, as few people should know of this as possible. If you want to collect the information, or pull me out, then don't send a messenger. Come and get me yourself -- even if that means you have to sneak through the gates.", "member_intelgathering_3",[]],
		
  [anyone|plyr,"member_intelgathering_3", [
		 ], "Splendid idea -- you do that.", "member_intelgathering_4",[]],
		
  [anyone|plyr,"member_intelgathering_3", [
		 ], "Actually, hold off for now.", "do_member_trade",[]],

  [anyone,"member_intelgathering_4", [
  		 (troop_set_slot, "$g_talk_troop", slot_troop_days_on_mission, 5),
  		 (troop_set_slot, "$g_talk_troop", slot_troop_current_mission, npc_mission_gather_intel),
		 
		 (remove_member_from_party, "$g_talk_troop", "p_main_party"),
		 		 
		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_honorific),
		 (str_store_string, s21, ":string"),

		 ], "Good. I should be ready to report in about five days. Farewell then, {s21}, for a little while.", "close_window",[]],

#talk with auxiliary party	 
  [anyone,"start", 
  [
    (store_encountered_party,":party_no"),
    (party_slot_eq,":party_no",slot_party_type, spt_attendant_party),
    (neg|main_party_has_troop,"$g_talk_troop"),
    (store_conversation_troop,"$g_talk_troop"),
    (troop_is_hero,"$g_talk_troop"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ], "Allright, {s5}?", "member_talk",[]],


]

dialogs = dialogs + dialogs_mission +dialogs_old