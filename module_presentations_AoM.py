# -*- coding: UTF-8 -*-

from header_common import *
from header_presentations import *
from header_mission_templates import *
from header_terrain_types import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from header_skills import *
from module_constants import *
from header_items import *
import string


####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

AoM_presentations = [

  ("inventory_new",0,mesh_inventory_background,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (assign, "$item_exchange_1", -1),
        (assign, "$item_exchange_2", -1),
        (assign, "$item_reorder_indication", -1),#indicate which kind of item is showed at right side, referring to weapon slot no.
        (assign, "$item_display_indication", -1),#indicate which kind of item is showed in the middle, store item no.

        (assign, ":count_no", 0),
        (try_for_range, ":count_no", 2, 24),
           (try_begin),
              (is_between, ":count_no", 2, 4),#ammo
              (assign, ":cur_y", 250),
              (assign, ":mesh_no", "mesh_inventory_ammo"),
              (try_begin),
                 (eq, ":count_no", 2),#ammo 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 3),#ammo 2
                 (assign, ":cur_x", 120),
              (try_end),
           (else_try),
              (eq, ":count_no", 4),#head
              (assign, ":cur_x", 45),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_head"),
           (else_try),
              (eq, ":count_no", 5),#body
              (assign, ":cur_x", 120),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_body"),
           (else_try),
              (eq, ":count_no", 6),#hand
              (assign, ":cur_x", 195),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_foot"),
           (else_try),
              (eq, ":count_no", 7),#foot
              (assign, ":cur_x", 270),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_hand"),
           (else_try),
              (eq, ":count_no", 8),#horse
              (assign, ":cur_x", 45),
              (assign, ":cur_y", 325),
              (assign, ":mesh_no", "mesh_inventory_empty_slot"),
           (else_try),
              (eq, ":count_no", 9),#food
              (assign, ":cur_x", 195),
              (assign, ":cur_y", 325),
              (assign, ":mesh_no", "mesh_inventory_empty_slot"),
           (else_try),
              (is_between, ":count_no", 10, 13),#right hands
              (assign, ":cur_y", 550),
              (assign, ":mesh_no", "mesh_inventory_right_hand"),
              (try_begin),
                 (eq, ":count_no", 10),#right hand 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 11),#right hand 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 12),#right hand 3
                 (assign, ":cur_x", 195),
              (try_end),
           (else_try),
              (is_between, ":count_no", 13, 16),#left hands
              (assign, ":cur_y", 475),
              (assign, ":mesh_no", "mesh_inventory_left_hand"),
              (try_begin),
                 (eq, ":count_no", 13),#left hand 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 14),#left hand 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 15),#left hand 3
                 (assign, ":cur_x", 195),
              (try_end),
           (else_try),
              (is_between, ":count_no", 16, 20),#accessory
              (assign, ":cur_y", 175),
              (assign, ":mesh_no", "mesh_inventory_accessory"),
              (try_begin),
                 (eq, ":count_no", 16),#accessory 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 17),#accessory 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 18),#accessory 3
                 (assign, ":cur_x", 195),
              (else_try),
                 (eq, ":count_no", 19),#accessory 4
                 (assign, ":cur_x", 270),
              (try_end),
           (else_try),
              (is_between, ":count_no", 20, 24),#small props
              (assign, ":cur_y", 100),
              (assign, ":mesh_no", "mesh_inventory_small_prop"),
              (try_begin),
                 (eq, ":count_no", 20),#small prop 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 21),#small prop 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 22),#small prop 3
                 (assign, ":cur_x", 195),
              (else_try),
                 (eq, ":count_no", 23),#small prop 4
                 (assign, ":cur_x", 270),
              (try_end),
           (try_end),
           (create_image_button_overlay, reg0, ":mesh_no", "mesh_inventory_highlight"),
           (create_mesh_overlay, reg1, "mesh_inventory_highlight"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg0, pos1),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 70),
           (position_set_y, pos1, 70),
           (overlay_set_size, reg0, pos1),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg0, 2),
           (overlay_set_additional_render_height, reg1, 1),
           (troop_set_slot, "trp_temp_array_a", ":count_no", reg0),

           (troop_get_inventory_slot, ":item_no", "trp_player", ":count_no"),
           (try_begin),
              (lt, ":item_no", 0),
              (assign, ":item_no", 0),
           (try_end),
           (val_add, ":cur_x", 35),
           (val_add, ":cur_y", 35),
           (create_mesh_overlay_with_item_id, reg2, ":item_no"),
           (set_fixed_point_multiplier, 1000),                #以防盾牌或铠甲改变分辨率
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg2, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg2, pos1),
           (overlay_set_additional_render_height, reg2, 3),
           (troop_set_slot, "trp_temp_array_b", ":count_no", reg2),
        (try_end),

        (assign, ":count_no", 0),
        (try_for_range, ":count_no", 0, 8),
           (try_begin),
              (eq, ":count_no", 7),
              (assign, ":cur_x", 195),
           (else_try),
              (assign, ":cur_x", 45),
           (try_end),
           (try_begin),
              (lt, ":count_no", 7),
              (store_mul, ":cur_y", ":count_no", 75),
              (store_sub, ":cur_y", 605, ":cur_y"),
           (else_try),
              (assign, ":cur_y", 380),
           (try_end),
           (store_add, ":string_no", "str_right_hand", ":count_no"),
           (str_store_string, s1, ":string_no"),
           (create_text_overlay, reg1, s1, tf_right_align),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_1", "@Back"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_container_1", "@ ", tf_scrollable),
        (position_set_x, pos1, 720),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 230),
        (position_set_y, pos1, 525),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),

        (assign, ":cur_x", 5),
        (assign, ":cur_y", 1800),
        (call_script, "script_player_get_new_inventory_capacity"),
        (assign, ":player_capacity", reg0),
        (try_for_range, ":count_no", 24, ":player_capacity"),
           (create_image_button_overlay, reg0, "mesh_inventory_empty_slot", "mesh_inventory_highlight"),
           (create_mesh_overlay, reg1, "mesh_inventory_highlight"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg0, pos1),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 70),
           (position_set_y, pos1, 70),
           (overlay_set_size, reg0, pos1),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg0, 2),
           (overlay_set_additional_render_height, reg1, 1),
           (overlay_set_display, reg0, 0),
           (overlay_set_display, reg1, 0),
           (troop_set_slot, "trp_temp_array_a", ":count_no", reg0),

           (store_add, ":cur_x_2", ":cur_x", 35),
           (store_add, ":cur_y_2", ":cur_y", 35),
           (call_script, "script_player_get_new_inventory_slot", ":count_no"),
           (assign, ":item_no", reg0),
           (try_begin),
              (eq, ":item_no", -1),
              (assign, ":item_no", 0),
           (try_end),
           (create_mesh_overlay_with_item_id, reg2, ":item_no"),
           (set_fixed_point_multiplier, 1000),
           (position_set_x, pos1, ":cur_x_2"),
           (position_set_y, pos1, ":cur_y_2"),
           (overlay_set_position, reg2, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg2, pos1),
           (overlay_set_additional_render_height, reg2, 3),
           (overlay_set_display, reg2, 0),
           (troop_set_slot, "trp_temp_array_b", ":count_no", reg2),

           (try_begin),
              (neq, ":cur_x", 155),
              (val_add, ":cur_x", 75),
           (else_try),
              (assign, ":cur_x", 5),
              (val_sub, ":cur_y", 75),
           (try_end),
        (try_end),

        (set_container_overlay, -1),

        (create_button_overlay, "$g_presentation_obj_2", "@交 换 所 选 物 品 ", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_2", 0),

        (call_script, "script_new_inventory_reorder", -1),

        (call_script, "script_cf_inventory_show_item_create", 0),

        (create_button_overlay, "$g_presentation_obj_4", "@近 战 模 式 "),#view melee pattern
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_color, "$g_presentation_obj_4", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_4", 0),

        (create_button_overlay, "$g_presentation_obj_5", "@投 掷 模 式 "),#view thrown pattern
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_color, "$g_presentation_obj_5", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_5", 0),

        (create_button_overlay, "$g_presentation_obj_6", "@查 看 所 有 物 品 "),#view all item
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_7", "@清 空 所 有 选 择 "),#clear all choosen
        (position_set_x, pos1, 230),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_color, "$g_presentation_obj_7", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_8", "@服 用 "),
        (position_set_x, pos1, 430),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_color, "$g_presentation_obj_8", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_8", 0),

            ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_load"),
            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
        ]),

    (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (try_begin),
           (lt, ":object", "$g_presentation_obj_2"),
           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 2, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (try_begin),
                 (eq, ":enter_leave", 0),
                 (call_script, "script_highlight_certain_block", ":object"),
              (else_try),
                 (neq, "$item_exchange_1", ":count_no"),
                 (neq, "$item_exchange_2", ":count_no"),
                 (call_script, "script_lowlight_certain_block", ":object"),
              (try_end),
              (assign, ":end_cond", 0),#break
           (try_end),
        (try_end),
      ]),

#      (ti_on_presentation_run,
#       [
            ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_run"),
            ####### mouse fix pos system #######
#        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"), #结束
           (presentation_set_duration, 0),
#           (change_screen_return),     
        (else_try),
           (lt, ":object", "$g_presentation_obj_1"),#快捷键ctrl
           (key_is_down, key_left_control),
           (le, "$item_exchange_1", 0),
           (le, "$item_exchange_2", 0),

           (assign, ":end_cond", 24),
           (try_for_range, ":count_no", 2, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (assign, "$item_exchange_1", ":count_no"),
              (assign, ":end_cond", 0),#break
           (try_end),
           (call_script, "script_new_inventory_reorder", "$item_exchange_1"),

           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 24, ":end_cond"),
              (call_script, "script_player_get_new_inventory_slot", ":count_no"),
              (lt, reg0, 0),
              (assign, "$item_exchange_2", ":count_no"),
              (assign, ":end_cond", 0),#break
           (try_end),
           (ge, "$item_exchange_2", 0),
           (call_script, "script_exchange_two_item", "$item_exchange_1", "trp_player", "$item_exchange_2", "trp_player"),
           (assign, "$item_exchange_1", -1),
           (assign, "$item_exchange_2", -1),

        (else_try),
           (lt, ":object", "$g_presentation_obj_2"),#快捷键ctrl
           (key_is_down, key_left_control),
           (le, "$item_exchange_1", 0),
           (le, "$item_exchange_2", 0),

           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 24, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (assign, "$item_exchange_1", ":count_no"),
              (assign, ":end_cond", 0),#break
           (try_end),

           (try_begin),
              (call_script, "script_item_difficulty_check", "trp_player", "trp_player", ":count_no"),
              (eq, reg1, 0),          #cannot equip
              (display_message, "str_cannot_equip"),
           (else_try),
              (assign, ":end_cond", 24),
              (try_for_range, ":count_no", 2, ":end_cond"),
                 (call_script, "script_player_get_new_inventory_slot", ":count_no"),
                 (lt, reg0, 0),
                 (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_1"),
                 (eq, reg0, 1),
                 (assign, "$item_exchange_2", ":count_no"),
                 (assign, ":end_cond", 0),#break
              (try_end),
              (ge, "$item_exchange_2", 0),
              (call_script, "script_exchange_two_item", "$item_exchange_1", "trp_player", "$item_exchange_2", "trp_player"),
           (try_end),
           (assign, "$item_exchange_1", -1),
           (assign, "$item_exchange_2", -1),

        (else_try),
           (lt, ":object", "$g_presentation_obj_2"),#选择物品栏
           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 2, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (try_begin),
                 (lt, ":count_no", 24),       #item already equipped
                 (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_1"),
                 (eq, reg0, 1),
                 (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_2"),
                 (eq, reg0, 1),
                 (call_script, "script_new_inventory_reorder", ":count_no"),
              (try_end),

              (try_begin),
                 (eq, "$item_exchange_1", ":count_no"),
                 (assign, "$item_exchange_1", -1),
                 (call_script, "script_lowlight_certain_block", ":object"),
              (else_try),
                 (eq, "$item_exchange_2", ":count_no"),
                 (assign, "$item_exchange_2", -1),
                 (call_script, "script_lowlight_certain_block", ":object"),
              (else_try),
                 (le, "$item_exchange_1", 0),
                 (assign, ":continue", 0),
                 (try_begin),
                    (ge, ":count_no", 24),
                    (call_script, "script_player_get_new_inventory_slot", ":count_no"),
                    (le, reg0, 0),
                    (assign, ":continue", 1),
                 (else_try),
                    (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_2"),
                    (eq, reg0, 1),
                    (assign, ":continue", 1),
                 (try_end),
                 (eq, ":continue", 1),
                 (assign, "$item_exchange_1", ":count_no"),
                 (call_script, "script_highlight_certain_block", ":object"),
              (else_try),
                 (le, "$item_exchange_2", 0),
                 (assign, ":continue", 0),
                 (try_begin),
                    (ge, ":count_no", 24),
                    (call_script, "script_player_get_new_inventory_slot", ":count_no"),
                    (le, reg0, 0),
                    (assign, ":continue", 1),
                 (else_try),
                    (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_1"),
                    (eq, reg0, 1),
                    (assign, ":continue", 1),
                 (try_end),
                 (eq, ":continue", 1),
                 (assign, "$item_exchange_2", ":count_no"),
                 (call_script, "script_highlight_certain_block", ":object"),
              (try_end),
              (assign, ":end_cond", 0),#break
           (try_end),

           (try_begin),
              (gt, "$item_exchange_1", 0),
              (gt, "$item_exchange_2", 0),
              (overlay_set_display, "$g_presentation_obj_2", 1),
           (else_try),
              (overlay_set_display, "$g_presentation_obj_2", 0),
           (try_end),

           (call_script, "script_player_get_new_inventory_slot", ":count_no"),
           (gt, reg0, 0),
           (call_script, "script_cf_inventory_show_item_change", reg0, ":count_no"),         #need to be placed here, in case cores beneath being abolish by "can fail"
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),#交换物品键

           (try_begin),
              (ge, "$item_exchange_1", 24),
              (lt, "$item_exchange_2", 24),
              (call_script, "script_item_difficulty_check", "trp_player", "trp_player", "$item_exchange_1"),
              (eq, reg1, 0),          #cannot equip
              (display_message, "str_cannot_equip"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_2"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
           (else_try),
              (ge, "$item_exchange_2", 24),
              (lt, "$item_exchange_1", 24),
              (call_script, "script_item_difficulty_check", "trp_player", "trp_player", "$item_exchange_2"),
              (eq, reg1, 0),          #cannot equip
              (display_message, "str_cannot_equip"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_2"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
           (else_try),
              (call_script, "script_exchange_two_item", "$item_exchange_1", "trp_player", "$item_exchange_2", "trp_player"),
           (try_end),

           (assign, "$item_exchange_1", -1),
           (assign, "$item_exchange_2", -1),

           (overlay_set_display, ":object", 0),
        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),#check melee pattern statistic
           (val_add, "$item_display_indication", 1),
           (call_script, "script_cf_inventory_show_item_change", "$item_display_indication", -1),
        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),#check thrown pattern statistic
           (val_sub, "$item_display_indication", 1),
           (call_script, "script_cf_inventory_show_item_change", "$item_display_indication", -1),
        (else_try),
           (eq, ":object", "$g_presentation_obj_6"),#显示全部物品
           (call_script, "script_new_inventory_reorder", -1),
        (else_try),
           (eq, ":object", "$g_presentation_obj_7"),#清除全部选择
           (try_begin),
              (ge, "$item_exchange_1", 0),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (assign, "$item_exchange_1", -1),
           (try_end),
           (try_begin),
              (ge, "$item_exchange_2", 0),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_2"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (assign, "$item_exchange_2", -1),
           (try_end),
           (overlay_set_display, "$g_presentation_obj_2", 0),

        (else_try),
           (eq, ":object", "$g_presentation_obj_8"),#使用物品
           (call_script, "script_player_get_new_inventory_slot", "$current_show_slot"),
           (gt, reg0, 0),
           (assign, ":item_no", reg0),
           (item_get_type, ":type_no", ":item_no"),
           (eq, ":type_no", itp_type_goods),
           (item_has_property, ":item_no", itp_expendable),
           (call_script, "script_expendable_item_effect", "trp_player", ":item_no"),
           (call_script, "script_player_remove_new_inventory_slot", "$current_show_slot"),
           (start_presentation, "prsnt_inventory_new"),
        (try_end),
       ]),
  ]),


#场景内使用的物品栏
  ("inventory_new_battle",0,0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (create_mesh_overlay, reg1, "mesh_black_panel"),
        (overlay_set_additional_render_height, reg1, -2),

        (assign, "$item_exchange_1", -1),
        (assign, "$item_exchange_2", -1),
        (assign, "$item_reorder_indication", -1),#indicate which kind of item is showed at right side, referring to weapon slot no.
        (assign, "$item_display_indication", -1),#indicate which kind of item is showed in the middle, store item no.
        (assign, "$g_presentation_obj_8", -1),#无法服用物品

        (assign, ":count_no", 0),
        (try_for_range, ":count_no", 2, 24),
           (try_begin),
              (is_between, ":count_no", 2, 4),#ammo
              (assign, ":cur_y", 250),
              (assign, ":mesh_no", "mesh_inventory_ammo"),
              (try_begin),
                 (eq, ":count_no", 2),#ammo 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 3),#ammo 2
                 (assign, ":cur_x", 120),
              (try_end),
           (else_try),
              (eq, ":count_no", 4),#head
              (assign, ":cur_x", 45),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_head"),
           (else_try),
              (eq, ":count_no", 5),#body
              (assign, ":cur_x", 120),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_body"),
           (else_try),
              (eq, ":count_no", 6),#hand
              (assign, ":cur_x", 195),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_foot"),
           (else_try),
              (eq, ":count_no", 7),#foot
              (assign, ":cur_x", 270),
              (assign, ":cur_y", 400),
              (assign, ":mesh_no", "mesh_inventory_hand"),
           (else_try),
              (eq, ":count_no", 8),#horse
              (assign, ":cur_x", 45),
              (assign, ":cur_y", 325),
              (assign, ":mesh_no", "mesh_inventory_empty_slot"),
           (else_try),
              (eq, ":count_no", 9),#food
              (assign, ":cur_x", 195),
              (assign, ":cur_y", 325),
              (assign, ":mesh_no", "mesh_inventory_empty_slot"),
           (else_try),
              (is_between, ":count_no", 10, 13),#right hands
              (assign, ":cur_y", 550),
              (assign, ":mesh_no", "mesh_inventory_right_hand"),
              (try_begin),
                 (eq, ":count_no", 10),#right hand 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 11),#right hand 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 12),#right hand 3
                 (assign, ":cur_x", 195),
              (try_end),
           (else_try),
              (is_between, ":count_no", 13, 16),#left hands
              (assign, ":cur_y", 475),
              (assign, ":mesh_no", "mesh_inventory_left_hand"),
              (try_begin),
                 (eq, ":count_no", 13),#left hand 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 14),#left hand 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 15),#left hand 3
                 (assign, ":cur_x", 195),
              (try_end),
           (else_try),
              (is_between, ":count_no", 16, 20),#accessory
              (assign, ":cur_y", 175),
              (assign, ":mesh_no", "mesh_inventory_accessory"),
              (try_begin),
                 (eq, ":count_no", 16),#accessory 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 17),#accessory 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 18),#accessory 3
                 (assign, ":cur_x", 195),
              (else_try),
                 (eq, ":count_no", 19),#accessory 4
                 (assign, ":cur_x", 270),
              (try_end),
           (else_try),
              (is_between, ":count_no", 20, 24),#small props
              (assign, ":cur_y", 100),
              (assign, ":mesh_no", "mesh_inventory_small_prop"),
              (try_begin),
                 (eq, ":count_no", 20),#small prop 1
                 (assign, ":cur_x", 45),
              (else_try),
                 (eq, ":count_no", 21),#small prop 2
                 (assign, ":cur_x", 120),
              (else_try),
                 (eq, ":count_no", 22),#small prop 3
                 (assign, ":cur_x", 195),
              (else_try),
                 (eq, ":count_no", 23),#small prop 4
                 (assign, ":cur_x", 270),
              (try_end),
           (try_end),
           (create_image_button_overlay, reg0, ":mesh_no", "mesh_inventory_highlight"),
           (create_mesh_overlay, reg1, "mesh_inventory_highlight"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg0, pos1),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 70),
           (position_set_y, pos1, 70),
           (overlay_set_size, reg0, pos1),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg0, 2),
           (overlay_set_additional_render_height, reg1, 1),
           (troop_set_slot, "trp_temp_array_a", ":count_no", reg0),

           (troop_get_inventory_slot, ":item_no", "trp_player", ":count_no"),
           (try_begin),
              (lt, ":item_no", 0),
              (assign, ":item_no", 0),
           (try_end),
           (val_add, ":cur_x", 35),
           (val_add, ":cur_y", 35),
           (create_mesh_overlay_with_item_id, reg2, ":item_no"),
           (set_fixed_point_multiplier, 1000),                #以防盾牌或铠甲改变分辨率
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg2, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg2, pos1),
           (overlay_set_additional_render_height, reg2, 3),
           (troop_set_slot, "trp_temp_array_b", ":count_no", reg2),
        (try_end),

        (assign, ":count_no", 0),
        (try_for_range, ":count_no", 0, 8),
           (try_begin),
              (eq, ":count_no", 7),
              (assign, ":cur_x", 195),
           (else_try),
              (assign, ":cur_x", 45),
           (try_end),
           (try_begin),
              (lt, ":count_no", 7),
              (store_mul, ":cur_y", ":count_no", 75),
              (store_sub, ":cur_y", 605, ":cur_y"),
           (else_try),
              (assign, ":cur_y", 380),
           (try_end),
           (store_add, ":string_no", "str_right_hand", ":count_no"),
           (str_store_string, s1, ":string_no"),
           (create_text_overlay, reg1, s1, tf_right_align),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_1", "@Back"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_container_1", "@ ", tf_scrollable),
        (position_set_x, pos1, 720),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 230),
        (position_set_y, pos1, 525),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),

        (assign, ":cur_x", 5),
        (assign, ":cur_y", 1800),
        (call_script, "script_player_get_new_inventory_capacity"),
        (assign, ":player_capacity", reg0),
        (try_for_range, ":count_no", 24, ":player_capacity"),
           (create_image_button_overlay, reg0, "mesh_inventory_empty_slot", "mesh_inventory_highlight"),
           (create_mesh_overlay, reg1, "mesh_inventory_highlight"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg0, pos1),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 70),
           (position_set_y, pos1, 70),
           (overlay_set_size, reg0, pos1),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg0, 2),
           (overlay_set_additional_render_height, reg1, 1),
           (overlay_set_display, reg0, 0),
           (overlay_set_display, reg1, 0),
           (troop_set_slot, "trp_temp_array_a", ":count_no", reg0),

           (store_add, ":cur_x_2", ":cur_x", 35),
           (store_add, ":cur_y_2", ":cur_y", 35),
           (call_script, "script_player_get_new_inventory_slot", ":count_no"),
           (assign, ":item_no", reg0),
           (try_begin),
              (eq, ":item_no", -1),
              (assign, ":item_no", 0),
           (try_end),
           (create_mesh_overlay_with_item_id, reg2, ":item_no"),
           (set_fixed_point_multiplier, 1000),
           (position_set_x, pos1, ":cur_x_2"),
           (position_set_y, pos1, ":cur_y_2"),
           (overlay_set_position, reg2, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg2, pos1),
           (overlay_set_additional_render_height, reg2, 3),
           (overlay_set_display, reg2, 0),
           (troop_set_slot, "trp_temp_array_b", ":count_no", reg2),

           (try_begin),
              (neq, ":cur_x", 155),
              (val_add, ":cur_x", 75),
           (else_try),
              (assign, ":cur_x", 5),
              (val_sub, ":cur_y", 75),
           (try_end),
        (try_end),

        (set_container_overlay, -1),

        (create_button_overlay, "$g_presentation_obj_2", "@交 换 所 选 物 品 ", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_2", 0),

        (call_script, "script_new_inventory_reorder", -1),

        (call_script, "script_cf_inventory_show_item_create", 0),

        (create_button_overlay, "$g_presentation_obj_4", "@近 战 模 式 "),#view melee pattern
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_color, "$g_presentation_obj_4", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_4", 0),

        (create_button_overlay, "$g_presentation_obj_5", "@投 掷 模 式 "),#view thrown pattern
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_color, "$g_presentation_obj_5", 0xFFFFFF),
        (overlay_set_display, "$g_presentation_obj_5", 0),

        (create_button_overlay, "$g_presentation_obj_6", "@查 看 所 有 物 品 "),#view all item
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_7", "@清 空 所 有 选 择 "),#clear all choosen
        (position_set_x, pos1, 230),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_color, "$g_presentation_obj_7", 0xFFFFFF),

        (presentation_set_duration, 999999),
        ]),

    (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (try_begin),
           (lt, ":object", "$g_presentation_obj_2"),
           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 2, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (try_begin),
                 (eq, ":enter_leave", 0),
                 (call_script, "script_highlight_certain_block", ":object"),
              (else_try),
                 (neq, "$item_exchange_1", ":count_no"),
                 (neq, "$item_exchange_2", ":count_no"),
                 (call_script, "script_lowlight_certain_block", ":object"),
              (try_end),
              (assign, ":end_cond", 0),#break
           (try_end),
        (try_end),
      ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"), #结束
           (try_for_range, ":inventory_slot_no", 10, 16),
              (troop_get_inventory_slot, ":weapon_no", "trp_player", ":inventory_slot_no"),#刷新左右手武器
              (store_add, ":inventory_modifier_slot_no", ":inventory_slot_no", 1201),
              (troop_get_slot, ":modifier_no", "trp_player", ":inventory_modifier_slot_no"),
              (store_add, ":slot_no", ":inventory_slot_no", 31),
              (agent_set_slot, "$mission_player_agent", ":slot_no", ":weapon_no"),#item_kind
              (val_add, ":slot_no", 12),
              (agent_set_slot, "$mission_player_agent", ":slot_no", ":modifier_no"),#modifier
           (try_end),
           (presentation_set_duration, 0), 
           (start_presentation, "prsnt_total_battle_interface"),#跳转到通用战场信息面板
        (else_try),
           (lt, ":object", "$g_presentation_obj_1"),#快捷键ctrl
           (key_is_down, key_left_control),
           (le, "$item_exchange_1", 0),
           (le, "$item_exchange_2", 0),

           (assign, ":end_cond", 24),
           (try_for_range, ":count_no", 2, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (assign, "$item_exchange_1", ":count_no"),
              (assign, ":end_cond", 0),#break
           (try_end),
           (call_script, "script_new_inventory_reorder", "$item_exchange_1"),

           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 24, ":end_cond"),
              (call_script, "script_player_get_new_inventory_slot", ":count_no"),
              (lt, reg0, 0),
              (assign, "$item_exchange_2", ":count_no"),
              (assign, ":end_cond", 0),#break
           (try_end),
           (ge, "$item_exchange_2", 0),
           (call_script, "script_exchange_two_item", "$item_exchange_1", "trp_player", "$item_exchange_2", "trp_player"),
           (assign, "$item_exchange_1", -1),
           (assign, "$item_exchange_2", -1),

        (else_try),
           (lt, ":object", "$g_presentation_obj_2"),#快捷键ctrl
           (key_is_down, key_left_control),
           (le, "$item_exchange_1", 0),
           (le, "$item_exchange_2", 0),

           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 24, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (assign, "$item_exchange_1", ":count_no"),
              (assign, ":end_cond", 0),#break
           (try_end),

           (try_begin),
              (call_script, "script_item_difficulty_check", "trp_player", "trp_player", ":count_no"),
              (eq, reg1, 0),          #cannot equip
              (display_message, "str_cannot_equip"),
           (else_try),
              (assign, ":end_cond", 24),
              (try_for_range, ":count_no", 2, ":end_cond"),
                 (call_script, "script_player_get_new_inventory_slot", ":count_no"),
                 (lt, reg0, 0),
                 (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_1"),
                 (eq, reg0, 1),
                 (assign, "$item_exchange_2", ":count_no"),
                 (assign, ":end_cond", 0),#break
              (try_end),
              (ge, "$item_exchange_2", 0),
              (call_script, "script_exchange_two_item", "$item_exchange_1", "trp_player", "$item_exchange_2", "trp_player"),
           (try_end),
           (assign, "$item_exchange_1", -1),
           (assign, "$item_exchange_2", -1),

        (else_try),
           (lt, ":object", "$g_presentation_obj_2"),#选择物品栏
           (call_script, "script_player_get_new_inventory_capacity"),
           (assign, ":end_cond", reg0),
           (try_for_range, ":count_no", 2, ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":count_no", ":object"),
              (try_begin),
                 (lt, ":count_no", 24),       #item already equipped
                 (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_1"),
                 (eq, reg0, 1),
                 (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_2"),
                 (eq, reg0, 1),
                 (call_script, "script_new_inventory_reorder", ":count_no"),
              (try_end),

              (try_begin),
                 (eq, "$item_exchange_1", ":count_no"),
                 (assign, "$item_exchange_1", -1),
                 (call_script, "script_lowlight_certain_block", ":object"),
              (else_try),
                 (eq, "$item_exchange_2", ":count_no"),
                 (assign, "$item_exchange_2", -1),
                 (call_script, "script_lowlight_certain_block", ":object"),
              (else_try),
                 (le, "$item_exchange_1", 0),
                 (assign, ":continue", 0),
                 (try_begin),
                    (ge, ":count_no", 24),
                    (call_script, "script_player_get_new_inventory_slot", ":count_no"),
                    (le, reg0, 0),
                    (assign, ":continue", 1),
                 (else_try),
                    (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_2"),
                    (eq, reg0, 1),
                    (assign, ":continue", 1),
                 (try_end),
                 (eq, ":continue", 1),
                 (assign, "$item_exchange_1", ":count_no"),
                 (call_script, "script_highlight_certain_block", ":object"),
              (else_try),
                 (le, "$item_exchange_2", 0),
                 (assign, ":continue", 0),
                 (try_begin),
                    (ge, ":count_no", 24),
                    (call_script, "script_player_get_new_inventory_slot", ":count_no"),
                    (le, reg0, 0),
                    (assign, ":continue", 1),
                 (else_try),
                    (call_script, "script_check_if_two_inventory_slot_are_same_kind", ":count_no", "$item_exchange_1"),
                    (eq, reg0, 1),
                    (assign, ":continue", 1),
                 (try_end),
                 (eq, ":continue", 1),
                 (assign, "$item_exchange_2", ":count_no"),
                 (call_script, "script_highlight_certain_block", ":object"),
              (try_end),
              (assign, ":end_cond", 0),#break
           (try_end),

           (try_begin),
              (gt, "$item_exchange_1", 0),
              (gt, "$item_exchange_2", 0),
              (overlay_set_display, "$g_presentation_obj_2", 1),
           (else_try),
              (overlay_set_display, "$g_presentation_obj_2", 0),
           (try_end),

           (call_script, "script_player_get_new_inventory_slot", ":count_no"),
           (gt, reg0, 0),
           (call_script, "script_cf_inventory_show_item_change", reg0, ":count_no"),         #need to be placed here, in case cores beneath being abolish by "can fail"
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),#交换物品键

           (try_begin),
              (ge, "$item_exchange_1", 24),
              (lt, "$item_exchange_2", 24),
              (call_script, "script_item_difficulty_check", "trp_player", "trp_player", "$item_exchange_1"),
              (eq, reg1, 0),          #cannot equip
              (display_message, "str_cannot_equip"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_2"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
           (else_try),
              (ge, "$item_exchange_2", 24),
              (lt, "$item_exchange_1", 24),
              (call_script, "script_item_difficulty_check", "trp_player", "trp_player", "$item_exchange_2"),
              (eq, reg1, 0),          #cannot equip
              (display_message, "str_cannot_equip"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_2"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
           (else_try),
              (call_script, "script_exchange_two_item", "$item_exchange_1", "trp_player", "$item_exchange_2", "trp_player"),
           (try_end),

           (assign, "$item_exchange_1", -1),
           (assign, "$item_exchange_2", -1),

           (overlay_set_display, ":object", 0),
        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),#check melee pattern statistic
           (val_add, "$item_display_indication", 1),
           (call_script, "script_cf_inventory_show_item_change", "$item_display_indication", -1),
        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),#check thrown pattern statistic
           (val_sub, "$item_display_indication", 1),
           (call_script, "script_cf_inventory_show_item_change", "$item_display_indication", -1),
        (else_try),
           (eq, ":object", "$g_presentation_obj_6"),#view all items
           (call_script, "script_new_inventory_reorder", -1),
        (else_try),
           (eq, ":object", "$g_presentation_obj_7"),#clear all choosen
           (try_begin),
              (ge, "$item_exchange_1", 0),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (assign, "$item_exchange_1", -1),
           (try_end),
           (try_begin),
              (ge, "$item_exchange_2", 0),
              (troop_get_slot,  ":overlay_background", "trp_temp_array_a", "$item_exchange_2"),
              (call_script, "script_lowlight_certain_block", ":overlay_background"),
              (assign, "$item_exchange_2", -1),
           (try_end),
           (overlay_set_display, "$g_presentation_obj_2", 0),
        (try_end),
       ]),
  ]),



  ("enter_background",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        
        (create_game_button_overlay, "$g_presentation_obj_1", "@You enter the Atrium World"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_display, "$g_presentation_obj_1", 0),

        (try_for_range, ":count_no", 0, 800),
           (store_add, ":cur_x", ":count_no", 100),
           (create_mesh_overlay, reg0, "mesh_white_plane"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, 120),
           (overlay_set_position, reg0, pos1),
           (position_set_x, pos1, 50),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg0, pos1),
           (overlay_set_color, reg0, 0x003399), 
           (overlay_set_display, reg0, 0),
           (troop_set_slot, "trp_temp_array_a", ":count_no", reg0),
        (try_end),

        (presentation_set_duration, 999999),
        ]),

      (ti_on_presentation_run,[
         (try_begin),
            (le, "$map_point_count_no", 1000000),
            (call_script, "script_initial_map_point"),
         (try_end),

         (store_div, ":progressbar_x", "$map_point_count_no", 800),
         (troop_get_slot, ":progressbar_x_overlay", "trp_temp_array_a", ":progressbar_x"),
         (overlay_set_display, ":progressbar_x_overlay", 1),
         (try_begin),
            (ge, "$map_point_count_no", 1000000),
            (overlay_set_display, "$g_presentation_obj_1", 1),
         (try_end),
       ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
           (jump_to_menu, "mnu_start_game_1"),
        (try_end),
       ]),
      ]),


#这个菜单是所有需要在战斗页面上展示的信息的整合，比如boss血条，潜行状态，对话等等
#在mission的各个位置都会有其刷新，几乎不需要任何操控，只有展示的功能。
#其余在战斗中呼出的界面，比如物品栏和指挥，退出时应返回该界面。
  ("total_battle_interface", prsntf_read_only,0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
######################################boss血条部分###############################
#        (call_script, "script_get_boss"),
        (try_begin),
           (ge, "$mission_boss_1", 0),
           (store_agent_hit_points, ":boss_hp", "$mission_boss_1"),

           (create_mesh_overlay, reg1, "mesh_progressbar_handle"),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 700),
           (overlay_set_position, reg1, pos1),
           (val_mul, ":boss_hp", 10),
           (position_set_x, pos1, ":boss_hp"),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),

           (create_mesh_overlay, reg1, "mesh_progressbar"),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 700),
           (overlay_set_position, reg1, pos1),

           (agent_get_troop_id, ":troop_no", "$mission_boss_1"),
           (str_store_troop_name, s1, ":troop_no"),
           (create_text_overlay, reg1, s1),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 710),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xffffff), 
        (try_end),

        (try_begin),
           (ge, "$mission_boss_2", 0),
           (store_agent_hit_points, ":boss_hp", "$mission_boss_2"),

           (create_mesh_overlay, reg1, "mesh_progressbar_handle"),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 670),
           (overlay_set_position, reg1, pos1),
           (val_mul, ":boss_hp", 10),
           (position_set_x, pos1, ":boss_hp"),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),

           (create_mesh_overlay, reg1, "mesh_progressbar"),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 670),
           (overlay_set_position, reg1, pos1),

           (agent_get_troop_id, ":troop_no", "$mission_boss_2"),
           (str_store_troop_name, s1, ":troop_no"),
           (create_text_overlay, reg1, s1),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 680),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xffffff), 
        (try_end),

        (try_begin),
           (ge, "$mission_boss_3", 0),
           (store_agent_hit_points, ":boss_hp", "$mission_boss_3"),

           (create_mesh_overlay, reg1, "mesh_progressbar_handle"),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 640),
           (overlay_set_position, reg1, pos1),
           (val_mul, ":boss_hp", 10),
           (position_set_x, pos1, ":boss_hp"),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),

           (create_mesh_overlay, reg1, "mesh_progressbar"),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 640),
           (overlay_set_position, reg1, pos1),

           (agent_get_troop_id, ":troop_no", "$mission_boss_3"),
           (str_store_troop_name, s1, ":troop_no"),
           (create_text_overlay, reg1, s1),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 650),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xffffff), 
        (try_end),

######################################对话###############################
#对话由script_start_conversation_battle引入，录入时将对话内容填入s20中
        (try_begin),
           (ge, "$g_talking_agent", 0),
#           (agent_is_alive, "$g_talking_agent"),

           (agent_get_troop_id, ":troop_no", "$g_talking_agent"),
           (str_store_troop_name, s1, ":troop_no"),
           (create_text_overlay, reg1, "@{s1} ： {s67}", tf_scrollable|tf_center_justify),
           (position_set_x, pos1, 250),
           (position_set_y, pos1, 40),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 950),
           (position_set_y, pos1, 950),
           (overlay_set_size, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 60),
           (overlay_set_area_size, reg1, pos1),
           (overlay_set_color, reg1, 0xffffff), 
        (try_end),

######################################地名###############################
#显示在屏幕中央的地名
        (try_begin),
           (gt, "$g_scene_name", 0),
           (create_text_overlay, reg1, s67, tf_center_justify),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 400),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 2500),
           (position_set_y, pos1, 2500),
           (overlay_set_size, reg1, pos1),
           (try_begin),
              (eq, "$g_scene_name", 1),
              (overlay_set_color, reg1, 0xffffff), 
           (try_end),
           (overlay_animate_to_alpha, reg1, 4000,0x00),
        (try_end),

######################################潜行相关###############################
#隐蔽等级
        (try_begin),
           (ge, "$infiltrate_tut", 1),
           (try_begin),
              (lt, "$infiltrate_hiding_level", 30),
              (str_store_string, s1, "@极 低 "),
              (assign, ":color_no", 0xFF0033),
           (else_try),
              (lt, "$infiltrate_hiding_level", 60),
              (str_store_string, s1, "@较 低 "),
              (assign, ":color_no", 0xFF6666),
           (else_try),
              (lt, "$infiltrate_hiding_level", 100),
              (str_store_string, s1, "@中 等 "),
              (assign, ":color_no", 0xFFCCCC),
           (else_try),
              (lt, "$infiltrate_hiding_level", 170),
              (str_store_string, s1, "@较 高 "),
              (assign, ":color_no", 0x99FF99),
           (else_try),
              (str_store_string, s1, "@极 高 "),
              (assign, ":color_no", 0x33FF33),
           (try_end),
           (create_text_overlay, reg1, "@隐 蔽 水 平 ： {s1}", tf_center_justify),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 30),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, ":color_no"), 
        (try_end),

        (presentation_set_duration, 999999),
        ]),

      (ti_on_presentation_run,
       [    
        (is_presentation_active, "prsnt_total_battle_interface"),
        (game_key_clicked, gk_view_orders),
        (presentation_set_duration, 0),
        (start_presentation, "prsnt_battle"),
       ]),
      ]),




#委托
  ("center_quest_window", 0, 0, [
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (create_mesh_overlay, reg1, "mesh_black_panel"),
        (overlay_set_additional_render_height, reg1, -2),

        (try_for_range, ":count_no", 0, 1000),
           (troop_set_slot, "trp_temp_array_c", ":count_no", -1),#清理数列信息
        (try_end),

        (create_button_overlay, "$g_presentation_obj_1", "@Back"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 35),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (assign, ":cur_x", 20),
        (assign, ":cur_y", 500),
        (try_for_range, ":quest_no", 1, 10),
           (store_add, ":slot_no", ":quest_no", slot_center_quest_begin),
           (val_sub, ":slot_no", 1),
           (party_get_slot, ":count_no", "$current_town", ":slot_no"),
           (gt, ":count_no", 1),#存在委托

           (create_mesh_overlay, reg1, "mesh_mp_ui_host_main"),#委托栏底板
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 300),
           (position_set_y, pos1, 300),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg1, -1),

           (store_add, ":cur_x_1", ":cur_x", 5),
           (store_add, ":cur_y_1", ":cur_y", 5),
           (create_text_overlay, reg1, "@ ", tf_scrollable),
           (position_set_x, pos1, ":cur_x_1"),
           (position_set_y, pos1, ":cur_y_1"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 290),
           (position_set_y, pos1, 155),
           (overlay_set_area_size, reg1, pos1),
           (set_container_overlay, reg1),

           (assign, ":cur_y_1", 115),
           (call_script, "script_get_center_quest_target", "$current_town", ":quest_no"),
           (assign, ":target_no", reg1),
           (assign, ":target_type", reg2),
           (try_begin),
              (eq, ":target_type", 0),#物品
              (str_store_item_name, s1, ":target_no"),
           (else_try),
              (str_store_troop_name, s1, ":target_no"),
           (try_end),
           (create_text_overlay, reg1, "@委 托 目 标 ： {s1}"),#委托目标
           (position_set_x, pos1, 10),
           (position_set_y, pos1, ":cur_y_1"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),

           (try_begin),
              (gt, reg3, 1),
              (val_sub, ":cur_y_1", 25),
              (create_text_overlay, reg1, "@需 求 数 量 ： {reg1}"),#委托数量
              (position_set_x, pos1, 10),
              (position_set_y, pos1, ":cur_y_1"),
              (overlay_set_position, reg1, pos1),
              (position_set_x, pos1, 900),
              (position_set_y, pos1, 900),
              (overlay_set_size, reg1, pos1),
           (try_end),

           (val_sub, ":cur_y_1", 25),
           (call_script, "script_get_center_quest_recycle", "$current_town", ":quest_no"),
           (try_begin),
              (eq, reg1, 0),#不用回收
              (str_store_string, s1, "@带 来 即 可 "),
           (else_try),
              (str_store_string, s1, "@带 来 并 交 付 "),
           (try_end),
           (create_text_overlay, reg1, s1),#委托要求
           (position_set_x, pos1, 10),
           (position_set_y, pos1, ":cur_y_1"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),

           (val_sub, ":cur_y_1", 25),
           (call_script, "script_get_center_quest_reward", "$current_town", ":quest_no"),
           (create_text_overlay, reg1, "@赏 金 ： {reg1}"),#赏金
           (position_set_x, pos1, 10),
           (position_set_y, pos1, ":cur_y_1"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),

           (create_button_overlay, reg1, "@结 算 委 托 ", tf_center_justify),#完成委托的按钮
           (troop_set_slot, "trp_temp_array_c", reg1, ":quest_no"),
           (position_set_x, pos1, 140),
           (position_set_y, pos1, 15),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),

           (set_container_overlay, -1),
           (try_begin),
              (lt, ":cur_x", 660),
              (val_add, ":cur_x", 320),
           (else_try),
              (val_sub, ":cur_y", 200),
              (assign, ":cur_x", 20),
           (try_end),
        (try_end),

#            ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_load"),
#            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
        ]),

#      (ti_on_presentation_run,
#       [
#            ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_run"),
#            ####### mouse fix pos system #######
#        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"), #结束
           (presentation_set_duration, 0), 
           (start_presentation, "prsnt_total_battle_interface"),#跳转到通用战场信息面板
        (else_try),
           (troop_get_slot, ":quest_no", "trp_temp_array_c", ":object"),#获取委托
           (is_between, ":quest_no", 1, 10),
           (call_script, "script_get_center_quest_target", "$current_town", ":quest_no"),
           (assign, ":target_no", reg1),
           (assign, ":target_type", reg2),
           (assign, ":target_num", reg3),
           (call_script, "script_get_center_quest_recycle", "$current_town", ":quest_no"),
           (assign, ":target_recycle", reg1),

           (assign, ":continue_no", 0),
           (try_begin),
              (eq, ":target_type", 0),#物品
              (call_script, "script_troop_caculate_item_num_with_modifier", "trp_player", ":target_no", -1),
              (ge, reg1, ":target_num"),#有足够的物品
              (assign, ":continue_no", 1),
              (eq, ":target_recycle", 1),#回收类型的委托才需交付
              (try_for_range, reg4, 0, ":target_num"),#移除指定数量的该物品
                 (call_script, "script_troop_remove_item_with_modifier_new", "trp_player", ":target_no", -1),
              (try_end),

           (else_try),
              (eq, ":target_type", 1),#人物
              (try_begin),
                 (eq, ":target_recycle", 1),#需要回收，只会在俘虏里
                 (party_count_prisoners_of_type, ":count_no", "p_main_party", ":target_no"),
                 (ge, ":count_no", ":target_num"),
                 (party_remove_prisoners, "p_main_party", ":target_no", ":target_num"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, ":target_recycle", 0),#无需回收，只会在部队里
                 (party_count_members_of_type, ":count_no", "p_main_party", ":target_no"),
                 (ge, ":count_no", ":target_num"),
                 (assign, ":continue_no", 1),
              (try_end),
           (try_end),

           (try_begin),
              (eq, ":continue_no", 1),
              (call_script, "script_set_center_quest_finish", "$current_town", ":quest_no"),#委托完成
              (start_presentation, "prsnt_center_quest_window"),#刷新界面
           (else_try),
              (display_message, "@未 满 足 提 交 条 件 "),
           (try_end),
        (try_end),
       ]),
  ]),




#图鉴
  ("troop_window", 0, 0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (assign, "$troop_faction_choose", -1),#所属阵营选择
        (assign, "$troop_grade_choose", -1),#等级选择
        (assign, "$troop_class_choose", -1),#兵种选择
        (assign, "$troop_show", -1),#用于刷新agent
        (assign, "$troop_show_2", -1),#用于刷新信息

        (try_for_range, ":count_no", 0, 1000),
           (troop_set_slot, "trp_temp_array_a", ":count_no", -1),#清理数列信息
        (try_end),

        (create_button_overlay, "$g_presentation_obj_1", "@Back", tf_center_justify),
        (position_set_x, pos1, 840),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_black_panel"),
        (position_set_x, pos1, 25),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 700),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -2),

        (create_text_overlay, "$g_presentation_container_1", "@ ", tf_scrollable),
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 90),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 400),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),

        (assign, ":cur_y", 5),
        (try_for_range, ":troop_no", soldiers_begin, soldiers_end),
           (neg|troop_is_hero, ":troop_no"),
           (val_add, ":cur_y", 20),
        (try_end),

        (try_for_range, ":troop_no", soldiers_begin, soldiers_end), #检索栏
           (neg|troop_is_hero, ":troop_no"),
           (str_store_troop_name, s1, ":troop_no"),
           (create_button_overlay, reg1 , s1),
           (val_sub, ":cur_y", 20),
           (position_set_x, pos1, 10),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (troop_set_slot, "trp_temp_array_a", reg1, ":troop_no"),#store troop id
        (try_end),
        (set_container_overlay, -1),

        (str_store_string, s1, "@全 部 "),
        (str_store_string, s2, "@阵 营 筛 选 "),
        (create_button_overlay, "$g_presentation_obj_2" , "@{s2}:_{s1}"),#阵营选择
        (position_set_x, pos1, 27),
        (position_set_y, pos1, 560),
        (overlay_set_position,"$g_presentation_obj_2", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),

        (str_store_string, s1, "@全 部 "),
        (str_store_string, s2, "@等 级 筛 选 "),
        (create_button_overlay, "$g_presentation_obj_3" , "@{s2}:_{s1}"),#等级选择
        (position_set_x, pos1, 27),
        (position_set_y, pos1, 535),
        (overlay_set_position,"$g_presentation_obj_3", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_obj_3", pos1),
        (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFF),

        (str_store_string, s1, "@全 部 "),
        (str_store_string, s2, "@兵 种 筛 选 "),
        (create_button_overlay, "$g_presentation_obj_4" , "@{s2}:_{s1}"),#兵种选择
        (position_set_x, pos1, 27),
        (position_set_y, pos1, 510),
        (overlay_set_position,"$g_presentation_obj_4", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        (overlay_set_color, "$g_presentation_obj_4", 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 25),
        (position_set_y, pos1, 500),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 9000),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

#——————————————————————————————————右侧信息框——————————————————————————————————
        (create_text_overlay, "$g_presentation_text_1", "@_", tf_center_justify),#名字
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_text_1", pos1),
        (overlay_set_color, "$g_presentation_text_1", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_2", "@_",  tf_scrollable),#介绍
        (position_set_x, pos1, 630),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 320),
        (position_set_y, pos1, 115),
        (overlay_set_area_size, "$g_presentation_text_2", pos1),
        (overlay_set_color, "$g_presentation_text_2", 0xFFFFFF),

        (create_mesh_overlay, "$g_presentation_mesh_1", "mesh_white_plane"),
        (position_set_x, pos1, 630),
        (position_set_y, pos1, 590),
        (overlay_set_position, "$g_presentation_mesh_1", pos1),
        (position_set_x, pos1, 16000),
        (position_set_y, pos1, 50),
        (overlay_set_size, "$g_presentation_mesh_1", pos1),

        (assign, ":cur_x", 700),
        (try_for_range, ":count", 0, 4),
           (store_add, ":string_no", ":count", "str_strength"),
           (str_store_string, s1, ":string_no"),

           (store_add, ":attribute_no", ":count", ca_strength),
           (store_attribute_level, ":attribute_level", "$troop_show_3", ":attribute_no"),#属性
           (assign, reg2, ":attribute_level"),

           (create_text_overlay, reg1, "@{s1}_{reg2}"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, 560),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (val_add, ":cur_x", 65),
        (try_end),

        (try_for_range, ":count", 0, 7),
           (store_add, ":string_no", ":count", "str_wpt_one_handed"),
           (str_store_string, s1, ":string_no"),

           (store_add, ":weapon_no", wpt_one_handed_weapon, ":count"),
           (store_proficiency_level, ":weapon_level", "$troop_show_3", ":weapon_no"),#熟练
           (assign, reg2, ":weapon_level"),

           (create_button_overlay, reg1, "@{s1}_{reg2}"),
           (position_set_x, pos1, 700),
           (store_mul, ":high", ":count", -20),
           (val_add, ":high", 530),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (create_text_overlay, reg1, "@ ", tf_scrollable),
        (position_set_x, pos1, 820),
        (position_set_y, pos1, 415),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 130),
        (position_set_y, pos1, 130),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (try_for_range, ":count", 0, 42),
           (store_add, ":string_no", ":count", "str_reserved_18"),
           (str_store_string, s1, ":string_no"),

           (store_sub, ":skill_no", skl_reserved_18, ":count"),
           (store_skill_level, ":skill_level", ":skill_no", "$troop_show_3"),#技能
           (assign, reg2, ":skill_level"),

           (create_button_overlay, reg1, "@{s1}_{reg2}"),
           (position_set_x, pos1, 10),
           (position_set_y, pos1, 10),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),
        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_3", "@_", tf_right_align),#阵营
        (position_set_x, pos1, 970),
        (position_set_y, pos1, 720),
        (overlay_set_position, "$g_presentation_text_3", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_3", pos1),
        (overlay_set_color, "$g_presentation_text_3", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_4", "@_", tf_left_align),#等级
        (position_set_x, pos1, 623),
        (position_set_y, pos1, 560),
        (overlay_set_position, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_4", pos1),
        (overlay_set_color, "$g_presentation_text_4", 0x66FFFF),

        (create_text_overlay, "$g_presentation_text_5", "@_", tf_left_align),#血量
        (position_set_x, pos1, 623),
        (position_set_y, pos1, 530),
        (overlay_set_position, "$g_presentation_text_5", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_5", pos1),
        (overlay_set_color, "$g_presentation_text_5", 0x66FFFF),

        (create_text_overlay, "$g_presentation_text_6", "@_", tf_left_align),#伤害
        (position_set_x, pos1, 623),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_text_6", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_6", pos1),
        (overlay_set_color, "$g_presentation_text_6", 0x66FFFF),

        (create_text_overlay, "$g_presentation_text_7", "@_", tf_left_align),#速度
        (position_set_x, pos1, 623),
        (position_set_y, pos1, 470),
        (overlay_set_position, "$g_presentation_text_7", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_7", pos1),
        (overlay_set_color, "$g_presentation_text_7", 0x66FFFF),

        (create_text_overlay, "$g_presentation_text_8", "@_", tf_left_align),#精准
        (position_set_x, pos1, 623),
        (position_set_y, pos1, 440),
        (overlay_set_position, "$g_presentation_text_8", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_8", pos1),
        (overlay_set_color, "$g_presentation_text_8", 0x66FFFF),

        (create_text_overlay, "$g_presentation_text_9", "@_", tf_left_align),#装填
        (position_set_x, pos1, 623),
        (position_set_y, pos1, 410),
        (overlay_set_position, "$g_presentation_text_9", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_9", pos1),
        (overlay_set_color, "$g_presentation_text_9", 0x66FFFF),

        (create_text_overlay, reg1, "@passive_skill", tf_left_align),#被动技能
        (position_set_x, pos1, 630),
        (position_set_y, pos1, 370),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (create_text_overlay, "$g_presentation_container_2", "@ ", tf_scrollable),
        (position_set_x, pos1, 630),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_container_2", pos1),
        (position_set_x, pos1, 90),
        (position_set_y, pos1, 260),
        (overlay_set_area_size, "$g_presentation_container_2", pos1),
        (set_container_overlay, "$g_presentation_container_2"),

        (store_add, ":passive_begin", "itm_passive_skills_begin", 1),
        (try_for_range, ":count", ":passive_begin", "itm_passive_skills_end"),#被动技能
           (create_mesh_overlay_with_item_id, reg1, ":count"),
           (position_set_x, pos1, 20),
           (position_set_y, pos1, 20),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (overlay_set_display, reg1, 0),
        (try_end),

        (set_container_overlay, -1),

        (call_script, "script_troop_attribute_refresh", "$troop_show_3"),#刷新数据

        (create_mesh_overlay, "$g_presentation_mesh_2", "mesh_white_plane"),
        (position_set_x, pos1, 630),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_mesh_2", pos1),
        (position_set_x, pos1, 16000),
        (position_set_y, pos1, 50),
        (overlay_set_size, "$g_presentation_mesh_2", pos1),

        (create_mesh_overlay, reg1, "mesh_black_panel"),
        (position_set_x, pos1, 625),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 853),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -2),

#——————————————————————————————————被动显示——————————————————————————————————

        (create_text_overlay, "$g_presentation_text_10", "@_", tf_left_align),#被动名称
        (position_set_x, pos1, 745),
        (position_set_y, pos1, 330),
        (overlay_set_position, "$g_presentation_text_10", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_10", pos1),
        (overlay_set_color, "$g_presentation_text_10", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_11", "@_", tf_left_align),#被动等级
        (position_set_x, pos1, 745),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_text_11", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_text_11", pos1),
        (overlay_set_color, "$g_presentation_text_11", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_12", "@_",  tf_scrollable),#介绍
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_text_12", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_text_12", pos1),
        (position_set_x, pos1, 210),
        (position_set_y, pos1, 200),
        (overlay_set_area_size, "$g_presentation_text_12", pos1),
        (overlay_set_color, "$g_presentation_text_12", 0xFFFFFF),

#——————————————————————————————————部队选择——————————————————————————————————
#储存进pt_temp_party里
        (try_begin),
           (eq, "$party_show", "p_temp_party"),
           (create_text_overlay, "$g_presentation_text_13", "@已 选 择 敌 方 兵 种 ：", tf_left_align),#部队选择
        (else_try),
           (eq, "$party_show", "p_temp_party_2"),
           (create_text_overlay, "$g_presentation_text_13", "@已 选 择 友 方 兵 种 ：", tf_left_align),#部队选择
        (try_end),
        (position_set_x, pos1, 35),
        (position_set_y, pos1, 725),
        (overlay_set_position, "$g_presentation_text_13", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_13", pos1),
        (overlay_set_color, "$g_presentation_text_13", 0xFFFFFF),

        (assign, ":cur_y", 705),
        (try_for_range, ":count_no", 0, 8),
           (create_button_overlay, reg1 , "@_"),
           (position_set_x, pos1, 130),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (val_sub, ":cur_y", 15),
        (try_end),

        (call_script, "script_troop_party_refresh"),#刷新部队信息

        (str_store_string, s1, "@添 加 该 兵 种 "),#添加兵种
        (call_script, "script_create_special_button_overlay", 64, 695),
        (assign, "$g_presentation_obj_5", reg1),

        (str_store_string, s1, "@清 除 该 兵 种 "),#清除兵种
        (call_script, "script_create_special_button_overlay", 64, 635),
        (assign, "$g_presentation_obj_6", reg1),

        (str_store_string, s1, "@添 加 十 该 兵 种 "),#添加10个该兵种
        (call_script, "script_create_special_button_overlay", 64, 665),
        (assign, "$g_presentation_obj_7", reg1),

        (str_store_string, s1, "@清 除 十 该 兵 种 "),#清除10个该兵种
        (call_script, "script_create_special_button_overlay", 64, 605),
        (assign, "$g_presentation_obj_8", reg1),


#            ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_load"),
#            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
        ]),

#      (ti_on_presentation_run,
#       [
#            ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_run"),
#            ####### mouse fix pos system #######
#        ]),

    (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (try_begin),
           (gt, ":object", "$g_presentation_container_2"),
           (lt, ":object", "$g_presentation_mesh_2"),#被动
           (try_begin),
              (eq, ":enter_leave", 0),   #enter
              (store_sub, ":skill_no", ":object", "$g_presentation_container_2"),
              (val_add, ":skill_no", "itm_passive_skills_begin"),
              (call_script, "script_check_agent_passive_skill", "$mission_show_agent", ":skill_no"),
              (gt, reg1, 0),

              (assign, reg2, reg1),
              (overlay_set_text, "$g_presentation_text_11", "@等 级 :{reg2}"),#技能等级
              (str_store_item_name, s1, ":skill_no"),
              (overlay_set_text, "$g_presentation_text_10", s1),#技能名称
              (str_store_item_name_plural, s1, ":skill_no"),
              (overlay_set_text, "$g_presentation_text_12", s1),#技能描述
           (try_end),
        (try_end),
      ]),

      (ti_on_presentation_run,
       [
        (gt, "$troop_show_2", 0),
        (call_script, "script_troop_attribute_refresh", "$troop_show_2"),#刷新数据
#被动技能描述刷新
        (overlay_set_text, "$g_presentation_text_10", "@_"),#技能名称
        (overlay_set_text, "$g_presentation_text_11", "@_"),#技能等级
        (overlay_set_text, "$g_presentation_text_12", "@_"),#技能描述
        (assign, "$troop_show_2", -1),
        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
           (show_object_details_overlay, 1),
           (finish_mission, 0),
        (else_try),
           (is_between, ":object", "$g_presentation_obj_1", "$g_presentation_obj_2"),#选择兵种
           (troop_get_slot, ":troop_no", "trp_temp_array_a", ":object"),
           (assign, "$troop_show_3", ":troop_no"),#用于记录当前troop
           (assign, "$troop_show", ":troop_no"),#用于刷新agent

        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),#阵营筛选
           (try_begin),
              (eq, "$troop_faction_choose", -1),
              (assign, "$troop_faction_choose", "fac_commoners"),
              (str_store_faction_name, s1, "$troop_faction_choose"),
           (else_try),
              (is_between, "$troop_faction_choose", "fac_commoners", "fac_faction_end"),
              (call_script, "script_troop_get_next_faction", "$troop_faction_choose"),
              (assign, "$troop_faction_choose", reg1),
           (try_end),
           (str_store_string, s2, "@阵 营 筛 选 "),
           (overlay_set_text, "$g_presentation_obj_2", "@{s2}:_{s1}"),
           (call_script, "script_troop_retrieve_refresh"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),#等级筛选
           (try_begin),
              (ge, "$troop_grade_choose", 6),
              (assign, "$troop_grade_choose", -1),
              (str_store_string, s1, "@全 部 "),
           (else_try),
              (val_add, "$troop_grade_choose", 1),
              (store_add, ":string_no", "$troop_grade_choose", "str_grade_blackiron"),
              (str_store_string, s1, ":string_no"),
           (try_end),
           (str_store_string, s2, "@等 级 筛 选 "),
           (overlay_set_text, "$g_presentation_obj_3", "@{s2}:_{s1}"),
           (call_script, "script_troop_retrieve_refresh"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),#兵种筛选
           (try_begin),
              (ge, "$troop_class_choose", 3),
              (assign, "$troop_class_choose", -1),
              (str_store_string, s1, "@全 部 "),
           (else_try),
              (val_add, "$troop_class_choose", 1),
              (store_add, ":string_no", "$troop_class_choose", "str_class_infantry"),
              (str_store_string, s1, ":string_no"),
           (try_end),
           (str_store_string, s2, "@兵 种 筛 选 "),
           (overlay_set_text, "$g_presentation_obj_4", "@{s2}:_{s1}"),
           (call_script, "script_troop_retrieve_refresh"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),#添加兵种
           (party_get_num_companion_stacks, ":stack_num", "$party_show"),
           (party_count_members_of_type, ":troop_num", "$party_show", "$troop_show_3"),#堆栈数小于8或者已经存在该兵种，可以继续添加。
           (this_or_next|lt, ":stack_num", 8),
           (gt, ":troop_num", 0),
           (party_add_members, "$party_show", "$troop_show_3", 1),
           (call_script, "script_troop_party_refresh"),#刷新部队信息

        (else_try),
           (eq, ":object", "$g_presentation_obj_6"),#清除兵种
           (party_remove_members, "$party_show", "$troop_show_3", 1),
           (call_script, "script_troop_party_refresh"),#刷新部队信息

        (else_try),
           (eq, ":object", "$g_presentation_obj_7"),#添加10个该兵种
           (party_get_num_companion_stacks, ":stack_num", "$party_show"),
           (party_count_members_of_type, ":troop_num", "$party_show", "$troop_show_3"),#堆栈数小于8或者已经存在该兵种，可以继续添加。
           (this_or_next|lt, ":stack_num", 8),
           (gt, ":troop_num", 0),
           (party_add_members, "$party_show", "$troop_show_3", 10),
           (call_script, "script_troop_party_refresh"),#刷新部队信息

        (else_try),
           (eq, ":object", "$g_presentation_obj_8"),#清除10个该兵种
           (party_remove_members, "$party_show", "$troop_show_3", 10),
           (call_script, "script_troop_party_refresh"),#刷新部队信息

        (else_try),
           (is_between, ":object", "$g_presentation_text_13", "$g_presentation_obj_5"),#点击已选兵种跳转
           (store_sub, ":overlay_no", ":object", "$g_presentation_text_13"),
           (is_between, ":overlay_no", 1, 9),
           (party_get_num_companion_stacks, ":stack_num", "$party_show"),
           (le, ":overlay_no", ":stack_num"),

           (val_sub, ":overlay_no", 1),
           (party_stack_get_troop_id, ":troop_no", "$party_show", ":overlay_no"),
           (assign, "$troop_show_3", ":troop_no"),#用于记录当前troop
           (assign, "$troop_show", ":troop_no"),#用于刷新agent
        (try_end),
       ]),
  ]),



#技能面板
  ("skill_window", 0, 0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (try_for_range, ":count_no", 0, 1000),
           (troop_set_slot, "trp_temp_array_a", ":count_no", -1),#清理数列信息
        (try_end),

        (troop_get_slot, ":active_skill_1", "trp_player", slot_troop_active_skill_1),
        (troop_get_slot, ":active_skill_2", "trp_player", slot_troop_active_skill_2),
        (troop_get_slot, ":active_skill_3", "trp_player", slot_troop_active_skill_3),
        (troop_get_slot, ":active_skill_4", "trp_player", slot_troop_active_skill_4),
        (troop_get_slot, ":active_skill_5", "trp_player", slot_troop_active_skill_5),
        (troop_get_slot, ":active_skill_6", "trp_player", slot_troop_active_skill_6),

        (create_button_overlay, "$g_presentation_obj_1", "@Back", tf_center_justify),
        (position_set_x, pos1, 840),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_2", "@Show_all_passive_skills", tf_center_justify),
        (position_set_x, pos1, 640),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),

        (create_mesh_overlay, "$g_presentation_mesh_1", "mesh_black_star_panel"),
        (overlay_set_additional_render_height, "$g_presentation_mesh_1", -2),

#——————————————————————————————————中央部分——————————————————————————————————
        (create_text_overlay, "$g_presentation_container_1", "@ ", tf_scrollable),#主动技能一览
        (position_set_x, pos1, 220),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 560),
        (position_set_y, pos1, 600),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),

#主动技能
        (try_for_range, ":count_no", 0, 6),
           (store_mul, ":count_no_2", 60, ":count_no"),#角度
           (call_script, "script_overlay_get_position_around_center", 280, 300, 58, ":count_no_2"),

           (store_add, ":slot_no", ":count_no", slot_troop_active_skill_1),#技能已选中
           (troop_get_slot, ":skill_no", "trp_player", ":slot_no"),
           (gt, ":skill_no", 0),

           (create_mesh_overlay_with_item_id, reg1, ":skill_no"),
           (position_set_x, pos1, reg3),
           (position_set_y, pos1, reg4),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 550),
           (position_set_y, pos1, 550),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":skill_no"),

        (else_try),
           (create_image_button_overlay, reg1, "mesh_skill_back", "mesh_skill_back_2"),#主动技能按钮
           (position_set_x, pos1, reg3),
           (position_set_y, pos1, reg4),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 50),
           (position_set_y, pos1, 50),
           (overlay_set_size, reg1, pos1),

           (assign, reg1, ":count_no"),
           (val_add, reg1, 1),
           (create_text_overlay, reg2, "str_key", tf_center_justify),#主动技能文字
           (val_sub, reg4, 8),
           (position_set_x, pos1, reg3),
           (position_set_y, pos1, reg4),
           (overlay_set_position, reg2, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg2, pos1),
           (overlay_set_color, reg2, 0xFFFFFF),
        (try_end),

        (create_text_overlay, "$g_presentation_text_1", "@ ", tf_center_justify),#用于分割主动技能和被动技能两块，便于后续处理
        (position_set_x, pos1, 280),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_text_1", pos1),

#被动技能
        (assign, ":skill_no", "itm_passive_skills_begin"),
        (try_for_range, ":count_no", 0, 36),
           (try_begin),
              (lt, ":count_no", 8),
              (store_mul, ":count_no_2", 15, ":count_no"),#角度
              (val_sub, ":count_no_2", 15),
              (assign, ":radius", 230),
           (else_try),
              (lt, ":count_no", 16),
              (store_sub, ":count_no_2", ":count_no", 8),
              (val_mul, ":count_no_2", 15),#角度
              (val_add, ":count_no_2", 165),
              (assign, ":radius", 230),
           (else_try),
              (lt, ":count_no", 22),
              (store_sub, ":count_no_2", ":count_no", 16),
              (val_mul, ":count_no_2", 18),#角度
              (val_sub, ":count_no_2", 27),
              (assign, ":radius", 180),
           (else_try),
              (lt, ":count_no", 28),
              (store_sub, ":count_no_2", ":count_no", 22),
              (val_mul, ":count_no_2", 18),#角度
              (val_add, ":count_no_2", 153),
              (assign, ":radius", 180),
           (else_try),
              (lt, ":count_no", 32),
              (store_sub, ":count_no_2", ":count_no", 28),
              (val_mul, ":count_no_2", 30),#角度
              (val_sub, ":count_no_2", 45),
              (assign, ":radius", 130),
           (else_try),
              (lt, ":count_no", 36),
              (store_sub, ":count_no_2", ":count_no", 32),
              (val_mul, ":count_no_2", 30),#角度
              (val_add, ":count_no_2", 135),
              (assign, ":radius", 130),
           (try_end),
           (call_script, "script_overlay_get_position_around_center", 280, 300, ":radius", ":count_no_2"),

           (call_script, "script_player_get_next_passive", ":skill_no"),#被动技能还未填入完
           (gt, reg1, 0),
           (assign, ":skill_no", reg1),
           (create_mesh_overlay_with_item_id, reg1, ":skill_no"),
           (position_set_x, pos1, reg3),
           (position_set_y, pos1, reg4),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":skill_no"),

        (else_try),
           (create_image_button_overlay, reg1, "mesh_skill_back", "mesh_skill_back_2"),#被动技能
           (position_set_x, pos1, reg3),
           (position_set_y, pos1, reg4),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 45),
           (position_set_y, pos1, 45),
          (overlay_set_size, reg1, pos1),

           (create_text_overlay, reg1, "@+", tf_center_justify),#被动技能文字（加号）
           (val_sub, reg4, 8),
           (position_set_x, pos1, reg3),
           (position_set_y, pos1, reg4),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (set_container_overlay, -1),

#——————————————————————————————————主动技能部分——————————————————————————————————

        (try_begin),
           (eq, "$show_active_or_passive", 1),#显示主动技能面板
           (assign, ":cur_x", 20),
        (else_try),
           (assign, ":cur_x", -300),
        (try_end),

        (create_text_overlay, "$g_presentation_container_2", "@ ", tf_scrollable),#主动技能一览
        (position_set_x, pos1, ":cur_x"),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_container_2", pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 580),
        (overlay_set_area_size, "$g_presentation_container_2", pos1),
        (set_container_overlay, "$g_presentation_container_2"),

        (store_add, ":skill_begin", "itm_active_skills_begin", 1),
        (assign, ":cur_y", 0),
        (try_for_range, ":skill_no", ":skill_begin", "itm_active_skills_end"),
           (call_script, "script_check_troop_active_skill", "trp_player", ":skill_no"),
           (gt, reg1, 0),
           (neq, ":active_skill_1", ":skill_no"),
           (neq, ":active_skill_2", ":skill_no"),
           (neq, ":active_skill_3", ":skill_no"),
           (neq, ":active_skill_4", ":skill_no"),
           (neq, ":active_skill_5", ":skill_no"),
           (neq, ":active_skill_6", ":skill_no"),
           (val_add, ":cur_y", 1),
        (try_end),

        (val_add, ":cur_y", 3),
        (val_div, ":cur_y", 4),
        (val_mul, ":cur_y", 45),
        (create_text_overlay, reg1, "@active_skill", tf_right_align),
        (position_set_x, pos1, 187),
        (position_set_y, pos1, ":cur_y"),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (store_mul, ":length_y", ":cur_y", 50),
        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 190),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, ":length_y"),
        (overlay_set_size, reg1, pos1),

        (val_sub, ":cur_y", 20),
        (assign, ":cur_x", 20),
        (try_for_range, ":skill_no", ":skill_begin", "itm_active_skills_end"),
           (call_script, "script_check_troop_active_skill", "trp_player", ":skill_no"),#持有该主动技能
           (gt, reg1, 0),
           (neq, ":active_skill_1", ":skill_no"),
           (neq, ":active_skill_2", ":skill_no"),
           (neq, ":active_skill_3", ":skill_no"),
           (neq, ":active_skill_4", ":skill_no"),
           (neq, ":active_skill_5", ":skill_no"),
           (neq, ":active_skill_6", ":skill_no"),

           (create_mesh_overlay_with_item_id, reg1, ":skill_no"),#生成该主动技能
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":skill_no"),
           (try_begin),
              (lt, ":cur_x", 155),
              (val_add, ":cur_x", 45),
           (else_try),
              (assign, ":cur_x", 20),
             (val_sub, ":cur_y", 45),
          (try_end),
        (try_end),

        (set_container_overlay, -1),

#——————————————————————————————————被动技能部分——————————————————————————————————

        (try_begin),
           (eq, "$show_active_or_passive", 2),#显示被动技能面板
           (assign, ":cur_x", 790),
        (else_try),
           (assign, ":cur_x", 1110),
        (try_end),

        (create_text_overlay, "$g_presentation_container_3", "@ ", tf_scrollable),#被动技能一览
        (position_set_x, pos1, ":cur_x"),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_container_3", pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 580),
        (overlay_set_area_size, "$g_presentation_container_3", pos1),
        (set_container_overlay, "$g_presentation_container_3"),

        (store_add, ":skill_begin", "itm_passive_skills_begin", 1),#统计
        (assign, ":cur_y", 0),
        (try_for_range, ":skill_no", ":skill_begin", "itm_passive_skills_end"),
           (call_script, "script_check_troop_passive_skill_learned", "trp_player", ":skill_no"),#已习得
           (gt, reg1, 0),
           (call_script, "script_check_troop_passive_skill_activited", "trp_player", ":skill_no"),#未激活
           (le, reg1, 0),
           (val_add, ":cur_y", 1),
        (try_end),

        (val_add, ":cur_y", 3),
        (val_div, ":cur_y", 4),
        (val_mul, ":cur_y", 45),
        (create_text_overlay, reg1, "@passive_skill"),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, ":cur_y"),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (store_mul, ":length_y", ":cur_y", 50),
        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, ":length_y"),
        (overlay_set_size, reg1, pos1),

        (val_sub, ":cur_y", 20),
        (assign, ":cur_x", 40),
        (try_for_range, ":skill_no", ":skill_begin", "itm_passive_skills_end"),
           (call_script, "script_check_troop_passive_skill_learned", "trp_player", ":skill_no"),#已习得
           (gt, reg1, 0),
           (call_script, "script_check_troop_passive_skill_activited", "trp_player", ":skill_no"),#未激活
           (le, reg1, 0),

           (create_mesh_overlay_with_item_id, reg1, ":skill_no"),#生成该主动技能
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":skill_no"),
           (try_begin),
              (lt, ":cur_x", 175),
              (val_add, ":cur_x", 45),
           (else_try),
              (assign, ":cur_x", 40),
             (val_sub, ":cur_y", 45),
          (try_end),
        (try_end),

        (set_container_overlay, -1),

#————————————————————————————————主动技能信息框——————————————————————————————

        (create_text_overlay, "$g_presentation_container_4", "@ ", tf_scrollable),#主动技能信息框
        (position_set_x, pos1, 1110),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_container_4", pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 580),
        (overlay_set_area_size, "$g_presentation_container_4", pos1),
        (set_container_overlay, "$g_presentation_container_4"),

        (create_text_overlay, "$g_presentation_text_2", "@_"),#技能名称
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 540),
        (overlay_set_position, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_text_2", pos1),
        (overlay_set_color, "$g_presentation_text_2", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_3", "@_", tf_scrollable),#技能描述
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 310),
        (overlay_set_position, "$g_presentation_text_3", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_text_3", pos1),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 160),
        (overlay_set_area_size, "$g_presentation_text_3", pos1),
        (overlay_set_color, "$g_presentation_text_3", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_4", "@_"),#技能类型（武技/术法/魔法）与消耗
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_4", pos1),
        (overlay_set_color, "$g_presentation_text_4", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_8", "@_"),#技能基础伤害
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 480),
        (overlay_set_position, "$g_presentation_text_8", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_8", pos1),
        (overlay_set_color, "$g_presentation_text_8", 0xFFFFFF),

        (assign, reg3, 1),#添加进一键
        (str_store_string, s1, "@select_active"),
        (call_script, "script_create_special_button_overlay", 90, 270),
        (assign, "$g_presentation_obj_3", reg1),

        (assign, reg3, 2),#添加进二键
        (str_store_string, s1, "@select_active"),
        (call_script, "script_create_special_button_overlay", 90, 237),
        (assign, "$g_presentation_obj_4", reg1),

        (assign, reg3, 3),#添加进三键
        (str_store_string, s1, "@select_active"),
        (call_script, "script_create_special_button_overlay", 90, 204),
        (assign, "$g_presentation_obj_5", reg1),

        (assign, reg3, 4),#添加进四键
        (str_store_string, s1, "@select_active"),
        (call_script, "script_create_special_button_overlay", 90, 171),
        (assign, "$g_presentation_obj_6", reg1),

        (assign, reg3, 5),#添加进五键
        (str_store_string, s1, "@select_active"),
        (call_script, "script_create_special_button_overlay", 90, 138),
        (assign, "$g_presentation_obj_7", reg1),

        (assign, reg3, 6),#添加进六键
        (str_store_string, s1, "@select_active"),
        (call_script, "script_create_special_button_overlay", 90, 105),
        (assign, "$g_presentation_obj_8", reg1),

        (str_store_string, s1, "@Suspend_selected_active_skills"),
        (call_script, "script_create_special_button_overlay", 90, 270),#卸载该技能
        (assign, "$g_presentation_obj_9", reg1),

        (set_container_overlay, -1),

#———————————————————————————————被动技能信息框———————————————————————————————

        (create_text_overlay, "$g_presentation_container_5", "@ ", tf_scrollable),#被动技能信息框
        (position_set_x, pos1, -300),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_container_5", pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 580),
        (overlay_set_area_size, "$g_presentation_container_5", pos1),
        (set_container_overlay, "$g_presentation_container_5"),

        (create_text_overlay, "$g_presentation_text_5", "@_"),#技能名称
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 540),
        (overlay_set_position, "$g_presentation_text_5", pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_text_5", pos1),
        (overlay_set_color, "$g_presentation_text_5", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_6", "@_", tf_scrollable),#技能描述
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 330),
        (overlay_set_position, "$g_presentation_text_6", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_text_6", pos1),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 160),
        (overlay_set_area_size, "$g_presentation_text_6", pos1),
        (overlay_set_color, "$g_presentation_text_6", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_7", "@_"),#技能等级
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 510),
        (overlay_set_position, "$g_presentation_text_7", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_7", pos1),
        (overlay_set_color, "$g_presentation_text_7", 0xFFFFFF),

        (str_store_string, s1, "@Activite_this_passive_skills"),
        (call_script, "script_create_special_button_overlay", 90, 290),#添加该技能
        (assign, "$g_presentation_obj_10", reg1),

        (str_store_string, s1, "@Suspend_selected_active_skills"),
        (call_script, "script_create_special_button_overlay", 90, 290),#卸载该技能
        (assign, "$g_presentation_obj_11", reg1),

        (set_container_overlay, -1),

        (create_text_overlay, reg1, "@skill_hint"),#说明
        (position_set_x, pos1, 60),
        (position_set_y, pos1, 30),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (presentation_set_duration, 999999),
       ]),

    (ti_on_presentation_mouse_enter_leave,
       [(set_fixed_point_multiplier, 1000),
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (neg|key_is_down, key_left_control),
        (eq, ":enter_leave", 0),   #enter
        (troop_get_slot, ":skill_no", "trp_temp_array_a", ":object"),#技能图标
        (gt, ":skill_no", 0),
        (try_begin),
           (neq, "$show_active_or_passive", 2),#没有显示被动
           (is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),#主动技能
           (position_set_x, pos1, 790),
           (position_set_y, pos1, 80),
           (overlay_set_position, "$g_presentation_container_4", pos1),#显示主动技能介绍面板
           (position_set_x, pos1, -300),
           (position_set_y, pos1, 80),
           (overlay_set_position, "$g_presentation_container_5", pos1),#隐藏被动技能介绍面板

           (str_store_item_name, s1, ":skill_no"),
           (overlay_set_text, "$g_presentation_text_2", "@_^{s1}"),#技能名字
           (str_store_item_name_plural, s1, ":skill_no"),
           (overlay_set_text, "$g_presentation_text_3", s1),#技能描述

           (item_get_abundance, reg1, ":skill_no"),#消耗
           (try_begin),
              (item_has_property, ":skill_no", itp_unique),#武技
              (str_store_string, s1, "str_martial_art"),
              (str_store_string, s2, "str_vigour_consume"),
              (overlay_set_color, "$g_presentation_text_4", 0x33CC33),
           (else_try),
              (item_has_property, ":skill_no", itp_always_loot),#术法
              (str_store_string, s1, "str_sorcery"),
              (str_store_string, s2, "str_chant_time_consume"),
              (overlay_set_color, "$g_presentation_text_4", 0xFFFFFF),
           (else_try),
              (item_has_property, ":skill_no", itp_always_loot),#魔法
              (str_store_string, s1, "str_magic"),
              (str_store_string, s2, "str_magic_consume"),
              (overlay_set_color, "$g_presentation_text_4", 0x663399),
           (try_end),
           (overlay_set_text, "$g_presentation_text_4", "@{s1}^{s2}"),

           (overlay_set_display, "$g_presentation_text_8", 0),
           (item_get_food_quality, reg1, ":skill_no"),#基础伤害
           (try_begin),
              (gt, reg1, 0),
              (overlay_set_display, "$g_presentation_text_8", 1),
              (str_store_string, s1, "@basic_damage"),
              (overlay_set_text, "$g_presentation_text_8", "@{s1}:_{reg1}"),
           (try_end),

           (store_sub, ":overlay_no_1", "$g_presentation_obj_3", 1),
           (store_add, ":overlay_no_2", "$g_presentation_obj_8", 1),
           (try_begin),
              (lt, ":object", "$g_presentation_container_2"),#已装载
              (try_for_range, ":count_no", ":overlay_no_1", ":overlay_no_2"),
                 (overlay_set_display, ":count_no", 0),
              (try_end),
              (overlay_set_display, ":overlay_no_2", 1),
              (overlay_set_display, "$g_presentation_obj_9", 1),#停用该技能
           (else_try),
              (try_for_range, ":count_no", ":overlay_no_1", ":overlay_no_2"),#装载该技能
                 (overlay_set_display, ":count_no", 1),
              (try_end),
              (overlay_set_display, ":overlay_no_2", 0),
              (overlay_set_display, "$g_presentation_obj_9", 0),
           (try_end),
           (assign, "$active_show", ":skill_no"),

        (else_try),
           (neq, "$show_active_or_passive", 1),#没有显示主动
           (is_between, ":skill_no", "itm_passive_skills_begin", "itm_passive_skills_end"),#被动技能
           (position_set_x, pos1, 1110),
           (position_set_y, pos1, 80),
           (overlay_set_position, "$g_presentation_container_4", pos1),#隐藏主动技能介绍面板
           (position_set_x, pos1, 20),
           (position_set_y, pos1, 80),
           (overlay_set_position, "$g_presentation_container_5", pos1),#显示被动技能介绍面板
           (call_script, "script_check_troop_passive_skill_learned", "trp_player", ":skill_no"),
           (gt, reg1, 0),

           (str_store_item_name, s1, ":skill_no"),
           (overlay_set_text, "$g_presentation_text_5", "@_^{s1}"),#技能名字
           (str_store_item_name_plural, s1, ":skill_no"),
           (overlay_set_text, "$g_presentation_text_6", s1),#技能描述
           (assign, reg2, reg1),
           (overlay_set_text, "$g_presentation_text_7", "@等 级 :{reg2}"),#技能等级

           (store_sub, ":overlay_no_1", "$g_presentation_obj_10", 1),
           (store_sub, ":overlay_no_2", "$g_presentation_obj_11", 1),
           (try_begin),
              (lt, ":object", "$g_presentation_container_2"),#已装载
              (overlay_set_display, ":overlay_no_1", 0),
              (overlay_set_display, "$g_presentation_obj_10", 0),
              (overlay_set_display, ":overlay_no_2", 1),
              (overlay_set_display, "$g_presentation_obj_11", 1),#停用该技能
           (else_try),
              (overlay_set_display, ":overlay_no_1", 1),
              (overlay_set_display, "$g_presentation_obj_10", 1),#装载该技能
              (overlay_set_display, ":overlay_no_2", 0),
              (overlay_set_display, "$g_presentation_obj_11", 0),
           (try_end),
           (assign, "$passive_show", ":skill_no"),
        (try_end),
      ]),

      (ti_on_presentation_event_state_change,
       [(set_fixed_point_multiplier, 1000),
        (store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
           (show_object_details_overlay, 1),
           (finish_mission, 0),
        (else_try),
           (neg|key_is_down, key_left_control),
           (this_or_next|eq, ":object", "$g_presentation_obj_2"),
           (is_between, ":object", "$g_presentation_container_1", "$g_presentation_text_1"),#主动技能中央部分，点击拖出主动技能面板
           (neq, "$show_active_or_passive", 1),#未显示主动技能面板
           (assign, "$show_active_or_passive", 1),
           (position_set_x, pos1, 20),
           (position_set_y, pos1, 80),
           (overlay_animate_to_position, "$g_presentation_container_2", 2000, pos1),#显示主动技能面板
           (position_set_x, pos1, 1110),
           (position_set_y, pos1, 80),
           (overlay_animate_to_position, "$g_presentation_container_3", 2000, pos1),#隐藏被动技能面板
           (position_set_x, pos1, -300),
           (position_set_y, pos1, 80),
           (overlay_set_position, "$g_presentation_container_5", pos1),#隐藏被动技能介绍面板
        (else_try),
           (neg|key_is_down, key_left_control),
           (this_or_next|eq, ":object", "$g_presentation_obj_2"),
           (is_between, ":object", "$g_presentation_text_1", "$g_presentation_container_2"),#被动技能中央部分，点击拖出被动技能面板
           (neq, "$show_active_or_passive", 2),#未显示被动技能面板
           (assign, "$show_active_or_passive", 2),
           (position_set_x, pos1, -300),
           (position_set_y, pos1, 80),
           (overlay_animate_to_position, "$g_presentation_container_2", 2000, pos1),#隐藏主动技能面板
           (position_set_x, pos1, 790),
           (position_set_y, pos1, 80),
           (overlay_animate_to_position, "$g_presentation_container_3", 2000, pos1),#显示被动技能面板
           (position_set_x, pos1, 1110),
           (position_set_y, pos1, 80),
           (overlay_set_position, "$g_presentation_container_4", pos1),#隐藏主动技能介绍面板

        (else_try),
           (is_between, ":object", "$g_presentation_obj_3", "$g_presentation_obj_9"),#装填主动技能
           (call_script, "script_check_if_skill_activited_by_troop", "trp_player", "$active_show"),
           (lt, reg1, 0),#未装填重复技能
           (try_begin),
              (eq, ":object", "$g_presentation_obj_3"),
              (assign, ":slot_no", slot_troop_active_skill_1),
           (else_try),
              (eq, ":object", "$g_presentation_obj_4"),
              (assign, ":slot_no", slot_troop_active_skill_2),
           (else_try),
              (eq, ":object", "$g_presentation_obj_5"),
              (assign, ":slot_no", slot_troop_active_skill_3),
           (else_try),
              (eq, ":object", "$g_presentation_obj_6"),
              (assign, ":slot_no", slot_troop_active_skill_4),
           (else_try),
              (eq, ":object", "$g_presentation_obj_7"),
              (assign, ":slot_no", slot_troop_active_skill_5),
           (else_try),
              (eq, ":object", "$g_presentation_obj_8"),
              (assign, ":slot_no", slot_troop_active_skill_6),
           (try_end),
           (troop_set_slot, "trp_player", ":slot_no", "$active_show"),
           (start_presentation, "prsnt_skill_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_9"),#卸载主动技能
           (call_script, "script_check_if_skill_activited_by_troop", "trp_player", "$active_show"),
           (store_add, ":slot_no", reg1, slot_troop_active_skill_1),
           (troop_set_slot, "trp_player", ":slot_no", -1),
           (start_presentation, "prsnt_skill_window"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_10"),#装填被动技能
           (call_script, "script_calculate_troop_passive_skill_activited", "trp_player"),#未装满
           (lt, reg1, 36),
           (call_script, "script_set_player_passive_skill_on_simple", "$passive_show"),
           (start_presentation, "prsnt_skill_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_11"),#卸载被动技能
           (call_script, "script_set_troop_passive_skill_off", "trp_player", "$passive_show", 0),
           (start_presentation, "prsnt_skill_window"),
        (try_end),
       ]),
  ]),



#boss图鉴
  ("boss_window", 0, 0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
#选择boss使用的是boss_num、boss_num_2、boss_num_3三个全局变量。用法为：boss_num全局记录选取的boss的序号，也是在这个界面之外唯一使用的全局变量；boss_num_2用于记录正在展示的boss的序号，随时准备将自己的内容传递给boss_num输出；boss_num_3用于临时刷新，在选取其他boss时载入数据，刷新以后立马把数据传递给boss_num_2并清空。

        (try_for_range, ":count_no", 0, 500),#清空数据
           (troop_set_slot, "trp_temp_array_a", ":count_no", -1),
           (troop_set_slot, "trp_temp_array_b", ":count_no", -1),
           (troop_set_slot, "trp_temp_array_c", ":count_no", -1),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_1", "@Back", tf_center_justify),
        (position_set_x, pos1, 920),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_container_1", "@ ", tf_scrollable),
        (position_set_x, pos1, 5),
        (position_set_y, pos1, 525),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 195),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),

        (assign, ":cur_y", 5),
        (try_for_range, ":slot_no", 1, 1000),
           (troop_get_slot, ":troop_no", "trp_boss_array", ":slot_no"),
           (gt, ":troop_no", 1),
           (str_store_troop_name, s1, ":troop_no"),
           (create_button_overlay, reg1 , s1),
           (val_add, ":cur_y", 20),
           (position_set_x, pos1, 10),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),
        (set_container_overlay, -1),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 520),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 9000),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_button_overlay, "$g_presentation_obj_2", "str_choose_troop", tf_center_justify),
        (position_set_x, pos1, 820),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),


#——————————————————————————————————左侧信息框——————————————————————————————————

        (agent_get_troop_id, ":troop_no", "$mission_show_agent"),

        (str_store_troop_name, s1, ":troop_no"),
        (create_text_overlay, "$g_presentation_text_1", s1, tf_center_justify),#名字
        (position_set_x, pos1, 525),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_text_1", pos1),
        (overlay_set_color, "$g_presentation_text_1", 0xFFFFFF),

        (str_store_troop_name_plural, s1, ":troop_no"),
        (create_text_overlay, "$g_presentation_text_2", s1,  tf_scrollable),#介绍
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 320),
        (position_set_y, pos1, 115),
        (overlay_set_area_size, "$g_presentation_text_2", pos1),
        (overlay_set_color, "$g_presentation_text_2", 0xFFFFFF),

        (create_mesh_overlay, "$g_presentation_mesh_1", "mesh_white_plane"),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 390),
        (overlay_set_position, "$g_presentation_mesh_1", pos1),
        (position_set_x, pos1, 16000),
        (position_set_y, pos1, 50),
        (overlay_set_size, "$g_presentation_mesh_1", pos1),

        (assign, ":cur_x", 80),
        (try_for_range, ":count", 0, 4),
           (store_add, ":string_no", ":count", "str_strength"),
           (str_store_string, s1, ":string_no"),

           (store_add, ":attribute_no", ":count", ca_strength),
           (store_attribute_level, ":attribute_level", ":troop_no", ":attribute_no"),#属性
           (assign, reg2, ":attribute_level"),

           (create_text_overlay, reg1, "@{s1}_{reg2}"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, 360),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (val_add, ":cur_x", 65),
        (try_end),

        (try_for_range, ":count", 0, 7),
           (try_begin),
              (eq, ":count", 0),
              (str_store_string, s1, "@单 手 "),
           (else_try),
              (eq, ":count", 1),
              (str_store_string, s1, "@双 手 "),
           (else_try),
              (eq, ":count", 2),
              (str_store_string, s1, "@长 杆 "),
           (else_try),
              (eq, ":count", 3),
              (str_store_string, s1, "@弓 "),
           (else_try),
              (eq, ":count", 4),
              (str_store_string, s1, "@弩 "),
           (else_try),
              (eq, ":count", 5),
              (str_store_string, s1, "@投 掷 "),
           (else_try),
              (eq, ":count", 6),
              (str_store_string, s1, "@火 器 "),
           (try_end),

           (store_add, ":weapon_no", wpt_one_handed_weapon, ":count"),
           (store_proficiency_level, ":weapon_level", ":troop_no", ":weapon_no"),#熟练
           (assign, reg2, ":weapon_level"),

           (create_text_overlay, reg1, "@{s1}_{reg2}"),
           (position_set_x, pos1, 80),
           (store_mul, ":high", ":count", -20),
           (val_add, ":high", 330),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (create_text_overlay, reg1, "@ ", tf_scrollable),
        (position_set_x, pos1, 135),
        (position_set_y, pos1, 215),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 130),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":height_no", 0),
        (try_for_range, ":count", 0, 42),
           (store_sub, ":skill_no", skl_reserved_18, ":count"),
           (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
           (gt, ":skill_level", 0),
           (val_add, ":height_no", 1),#统计
        (try_end),
        (val_add, ":height_no", 1),
        (val_div, ":height_no", 3),
        (val_add, ":height_no", 1),
        (val_mul, ":height_no", 20),#高度

        (assign, ":count_no", 0),
        (try_for_range, ":count", 0, 42),
           (store_sub, ":skill_no", skl_reserved_18, ":count"),
           (store_skill_level, reg2, ":skill_no", ":troop_no"),#技能
           (gt, reg2, 0),

           (store_add, ":string_no", ":count", "str_reserved_18"),
           (str_store_string, s1, ":string_no"),

           (create_text_overlay, reg1, "@{s1}_{reg2}"),

            (store_mod, ":count_no_1", ":count_no", 3),
            (store_div, ":count_no_2", ":count_no", 3),
            (try_begin),
               (eq, ":count_no_1", 0),
               (position_set_x, pos1, 10),
            (else_try),
               (eq, ":count_no_1", 1),
               (position_set_x, pos1, 75),
            (else_try),
               (position_set_x, pos1, 140),
            (try_end),
            (val_mul, ":count_no_2", -20),
            (store_add, ":high", ":count_no_2", ":height_no"),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (val_add, ":count_no", 1),
        (try_end),
        (set_container_overlay, -1),

        (store_character_level, reg2, ":troop_no"),
        (create_text_overlay, "$g_presentation_text_3", "@等 级 :{reg2}", tf_left_align),#等级
        (position_set_x, pos1, 3),
        (position_set_y, pos1, 360),
        (overlay_set_position, "$g_presentation_text_3", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_3", pos1),
        (overlay_set_color, "$g_presentation_text_3", 0x66FFFF),

        (store_agent_hit_points, reg2, "$mission_show_agent", 1),#血量
        (try_begin),
           (store_mod, ":count_no", reg2, 10),
           (eq, ":count_no", 9),
           (val_add, reg2, 1),
        (try_end),
        (create_text_overlay, "$g_presentation_text_4", "@生 命 :{reg2}", tf_left_align),#血量
        (position_set_x, pos1, 3), 
        (position_set_y, pos1, 330),
        (overlay_set_position, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_4", pos1),
        (overlay_set_color, "$g_presentation_text_4", 0x66FFFF),

        (agent_get_damage_modifier, reg2, "$mission_show_agent"),#伤害
        (try_begin),
           (store_mod, ":count_no", reg2, 10),
           (eq, ":count_no", 9),
           (val_add, reg2, 1),
        (try_end),
        (create_text_overlay, "$g_presentation_text_5", "@伤 害 :{reg2}", tf_left_align),#伤害
        (position_set_x, pos1, 3),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_text_5", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_5", pos1),
        (overlay_set_color, "$g_presentation_text_5", 0x66FFFF),

        (agent_get_speed_modifier, reg2, "$mission_show_agent"),#速度
        (try_begin),
           (store_mod, ":count_no", reg2, 10),
           (eq, ":count_no", 9),
           (val_add, reg2, 1),
        (try_end),
        (create_text_overlay, "$g_presentation_text_6", "@速 度 :{reg2}", tf_left_align),#速度
        (position_set_x, pos1, 3),
        (position_set_y, pos1, 270),
        (overlay_set_position, "$g_presentation_text_6", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_6", pos1),
        (overlay_set_color, "$g_presentation_text_6", 0x66FFFF),

        (agent_get_accuracy_modifier, reg2, "$mission_show_agent"),#精准
        (try_begin),
           (store_mod, ":count_no", reg2, 10),
           (eq, ":count_no", 9),
           (val_add, reg2, 1),
        (try_end),
        (create_text_overlay, "$g_presentation_text_7", "@精 准 :{reg2}", tf_left_align),#精准
        (position_set_x, pos1, 3),
        (position_set_y, pos1, 240),
        (overlay_set_position, "$g_presentation_text_7", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_7", pos1),
        (overlay_set_color, "$g_presentation_text_7", 0x66FFFF),

        (agent_get_reload_speed_modifier, reg2, "$mission_show_agent", 1),#装填
        (try_begin),
           (store_mod, ":count_no", reg2, 10),
           (eq, ":count_no", 9),
           (val_add, reg2, 1),
        (try_end),
        (create_text_overlay, "$g_presentation_text_8", "@装 填 :{reg2}", tf_left_align),#装填
        (position_set_x, pos1, 3),
        (position_set_y, pos1, 210),
        (overlay_set_position, "$g_presentation_text_8", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_8", pos1),
        (overlay_set_color, "$g_presentation_text_8", 0x66FFFF),

#物品栏
        (create_text_overlay, reg1, "@ ", tf_scrollable),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 40),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 130),
        (position_set_y, pos1, 150),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":cur_y", 100),
        (assign, ":cur_x", 5),
        (try_for_range, ":count_no", 0, 9),
#           (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
           (create_image_button_overlay, reg1, "mesh_mp_inventory_choose", "mesh_mp_inventory_choose"),
           (position_set_x, pos1, 320),
           (position_set_y, pos1, 320),
           (overlay_set_size, reg1, pos1),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (troop_set_slot, "trp_temp_array_b", ":count_no", reg1),

           (create_mesh_overlay, reg1, "mesh_inv_slot"),
           (position_set_x, pos1, 400),
           (position_set_y, pos1, 400),
           (overlay_set_size, reg1, pos1),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),

           (agent_get_item_slot, ":item_no", "$mission_show_agent", ":count_no"),
           (try_begin),
              (eq, ":count_no", 8),#给马留的位置
              (ge, "$mission_show_horse", 0),#生成了马
              (agent_get_item_id, ":item_no", "$mission_show_horse"),
           (else_try),
              (eq, ":count_no", 8),#给马留的位置
              (assign, ":item_no", -1),
           (try_end),
           (val_max, ":item_no", 0),
           (create_mesh_overlay_with_item_id, reg1, ":item_no"),
           (position_set_x, pos1, 400),
           (position_set_y, pos1, 400),
           (overlay_set_size, reg1, pos1),
           (store_add, ":cur_x_1", ":cur_x", 20),
           (store_add, ":cur_y_1", ":cur_y", 20),
           (position_set_x, pos1, ":cur_x_1"),
           (position_set_y, pos1, ":cur_y_1"),
           (overlay_set_position, reg1, pos1),
           (troop_set_slot, "trp_temp_array_c", ":count_no", reg1),

           (try_begin),
              (store_mod, ":position_change", ":count_no", 3),
              (neq, ":position_change", 2),
              (val_add, ":cur_x", 40),
           (else_try),
              (assign, ":cur_x", 5),
              (val_sub, ":cur_y", 40),
           (try_end),
        (try_end),
        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_9", "@_", tf_scrollable),#物品介绍
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_text_9", pos1),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_text_9", pos1),
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 150),
        (overlay_set_area_size, "$g_presentation_text_9", pos1),
        (overlay_set_color, "$g_presentation_text_9", 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 200),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 16000),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_mesh_overlay, reg1, "mesh_black_panel"),
        (position_set_x, pos1, 5),
        (position_set_y, pos1, 30),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 330),
        (position_set_y, pos1, 640),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -2),

#——————————————————————————————————右侧信息——————————————————————————————————
        (create_mesh_overlay, reg1, "mesh_black_panel"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 280),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -2),

        (create_text_overlay, reg1, "@passive_skill", tf_left_align),#被动技能
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 240),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 783),
        (position_set_y, pos1, 248),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 9900),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, "$g_presentation_container_2", "@ ", tf_scrollable),
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 105),
        (overlay_set_position, "$g_presentation_container_2", pos1),
        (position_set_x, pos1, 90),
        (position_set_y, pos1, 125),
        (overlay_set_area_size, "$g_presentation_container_2", pos1),
        (set_container_overlay, "$g_presentation_container_2"),

        (assign, ":cur_y", 0),
        (store_add, ":passive_begin", "itm_passive_skills_begin", 1),
        (try_for_range, ":count_no", ":passive_begin", "itm_passive_skills_end"),#被动统计
           (call_script, "script_check_agent_passive_skill", "$mission_show_agent", ":count_no"),#持有该被动
           (gt, reg1, 0),
           (val_add, ":cur_y", 1),
        (try_end),

        (val_add, ":cur_y", 1),
        (val_div, ":cur_y", 2),
        (val_mul, ":cur_y", 45),
        (val_sub, ":cur_y", 20),
        (assign, ":cur_x", 20),
        (store_add, ":passive_begin", "itm_passive_skills_begin", 1),
        (try_for_range, ":count_no", ":passive_begin", "itm_passive_skills_end"),#被动技能

           (call_script, "script_check_agent_passive_skill", "$mission_show_agent", ":count_no"),#持有该被动
           (gt, reg1, 0),
           (create_mesh_overlay_with_item_id, reg1, ":count_no"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":count_no"),

           (try_begin),
              (eq, ":cur_x", 20),
              (assign, ":cur_x", 65),
           (else_try),
              (eq, ":cur_x", 65),
              (assign, ":cur_x", 20),
              (val_sub, ":cur_y", 45),
           (try_end),
        (try_end),
        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_10", "@_", tf_left_align),#被动名称
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 210),
        (overlay_set_position, "$g_presentation_text_10", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$g_presentation_text_10", pos1),
        (overlay_set_color, "$g_presentation_text_10", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_11", "@_", tf_left_align),#被动等级
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 197),
        (overlay_set_position, "$g_presentation_text_11", pos1),
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 650),
        (overlay_set_size, "$g_presentation_text_11", pos1),
        (overlay_set_color, "$g_presentation_text_11", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_12", "@_",  tf_scrollable),#介绍
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 105),
        (overlay_set_position, "$g_presentation_text_12", pos1),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_text_12", pos1),
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 95),
        (overlay_set_area_size, "$g_presentation_text_12", pos1),
        (overlay_set_color, "$g_presentation_text_12", 0xFFFFFF),

#主动技能
        (create_text_overlay, reg1, "@active_skill", tf_left_align),#主动技能
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 410),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 783),
        (position_set_y, pos1, 418),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 9900),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, "$g_presentation_container_3", "@ ", tf_scrollable),
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 275),
        (overlay_set_position, "$g_presentation_container_3", pos1),
        (position_set_x, pos1, 90),
        (position_set_y, pos1, 125),
        (overlay_set_area_size, "$g_presentation_container_3", pos1),
        (set_container_overlay, "$g_presentation_container_3"),

        (assign, ":cur_x", 20),
        (assign, ":cur_y", 25),
        (try_for_range, ":count_no", 0, 6),#主动技能
           (store_add, ":slot_no", slot_agent_active_skill_1, ":count_no"),
           (agent_get_slot, ":skill_no", "$mission_show_agent", ":slot_no"),
           (gt, ":skill_no", 0),
           (create_mesh_overlay_with_item_id, reg1, ":skill_no"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 500),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":skill_no"),

           (try_begin),
              (eq, ":cur_x", 20),
              (assign, ":cur_x", 65),
           (else_try),
              (eq, ":cur_x", 65),
              (assign, ":cur_x", 20),
              (val_add, ":cur_y", 45),
           (try_end),
        (try_end),
        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_13", "@_", tf_left_align),#主动名称
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$g_presentation_text_13", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$g_presentation_text_13", pos1),
        (overlay_set_color, "$g_presentation_text_13", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_14", "@_",  tf_scrollable),#介绍
        (position_set_x, pos1, 830),
        (position_set_y, pos1, 270),
        (overlay_set_position, "$g_presentation_text_14", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_14", pos1),
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 110),
        (overlay_set_area_size, "$g_presentation_text_14", pos1),
        (overlay_set_color, "$g_presentation_text_14", 0xFFFFFF),

        (create_text_overlay, reg1, "str_boss_description_begin", tf_left_align),#攻击模式和剧情介绍
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 675),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 890),
        (position_set_y, pos1, 683),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 4500),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (store_add, ":string_no", "$boss_num_2", "str_boss_description_begin"),
        (str_store_string, s1, ":string_no"),
        (create_text_overlay, "$g_presentation_text_15", s1,  tf_scrollable),#攻击模式和剧情介绍
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 440),
        (overlay_set_position, "$g_presentation_text_15", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$g_presentation_text_15", pos1),
        (position_set_x, pos1, 270),
        (position_set_y, pos1, 220),
        (overlay_set_area_size, "$g_presentation_text_15", pos1),
        (overlay_set_color, "$g_presentation_text_15", 0xFFFFFF),

        (presentation_set_duration, 999999),
       ]),

    (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (try_begin),
           (gt, ":object", "$g_presentation_container_2"),
           (lt, ":object", "$g_presentation_text_10"),#被动技能框
           (try_begin),
              (eq, ":enter_leave", 0),   #enter
              (troop_get_slot, ":skill_no", "trp_temp_array_a", ":object"),
              (gt, ":skill_no", 0),
              (call_script, "script_check_agent_passive_skill", "$mission_show_agent", ":skill_no"),
              (gt, reg1, 0),

              (assign, reg2, reg1),
              (overlay_set_text, "$g_presentation_text_11", "@等 级 :{reg2}"),#技能等级
              (str_store_item_name, s1, ":skill_no"),
              (overlay_set_text, "$g_presentation_text_10", s1),#技能名称
              (str_store_item_name_plural, s1, ":skill_no"),
              (overlay_set_text, "$g_presentation_text_12", "@{s1}^_"),#技能描述
           (try_end),

        (else_try),
           (gt, ":object", "$g_presentation_container_3"),
           (lt, ":object", "$g_presentation_text_13"),#主动技能框
           (try_begin),
              (eq, ":enter_leave", 0),   #enter
              (troop_get_slot, ":skill_no", "trp_temp_array_a", ":object"),
              (gt, ":skill_no", 0),

              (str_store_item_name, s1, ":skill_no"),
              (overlay_set_text, "$g_presentation_text_13", s1),#技能名称
              (str_store_item_name_plural, s1, ":skill_no"),
              (overlay_set_text, "$g_presentation_text_14", "@{s1}^_"),#技能描述
           (try_end),

        (else_try),
            (is_between, ":object", "$g_presentation_text_8", "$g_presentation_text_9"),#物品栏
            (try_begin),
               (eq, ":enter_leave", 0),#enter
               (try_for_range, ":inventory_slot_no", 0, 9),
                  (troop_slot_eq, "trp_temp_array_b", ":inventory_slot_no", ":object"),
                  (try_begin),
                     (eq, ":inventory_slot_no", 8),#给马留的位置
                     (ge, "$mission_show_horse", 0),#生成了马
                     (agent_get_item_id, ":item_no", "$mission_show_horse"),
                  (else_try),
                     (eq, ":inventory_slot_no", 8),#给马留的位置
                     (assign, ":item_no", -1),
                  (else_try),
                     (agent_get_item_slot, ":item_no", "$mission_show_agent", ":inventory_slot_no"),
                  (try_end),
                  (gt, ":item_no", 0),

                  (troop_get_slot, ":inventroy_position", "trp_temp_array_c", ":inventory_slot_no"),
                  (overlay_get_position, pos0, ":inventroy_position"),
                  (show_item_details_with_modifier, ":item_no", 0, pos0, 100),
                  (assign, "$g_current_opened_item_details", ":inventory_slot_no"),
               (try_end),
            (else_try),
               (eq, ":enter_leave", 1),#leave
               (try_for_range, ":inventory_slot_no", 0, 9),
                  (troop_slot_eq, "trp_temp_array_b", ":inventory_slot_no", ":object"),
                  (eq, "$g_current_opened_item_details", ":inventory_slot_no"),
                  (close_item_details),
               (try_end),
           (try_end),
        (try_end),
      ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
           (show_object_details_overlay, 1),
           (finish_mission, 0),
        (else_try),
           (is_between, ":object", "$g_presentation_container_1", "$g_presentation_obj_2"),#选择兵种
           (val_sub, ":object", "$g_presentation_container_1"),
           (assign, "$boss_num_3", ":object"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),#确认选择
           (assign, "$boss_num", "$boss_num_2"),#输出

        (else_try),
           (is_between, ":object", "$g_presentation_text_8", "$g_presentation_text_9"),#物品栏
              (try_for_range, ":inventory_slot_no", 0, 9),
                 (troop_slot_eq, "trp_temp_array_b", ":inventory_slot_no", ":object"),
                 (try_begin),
                    (eq, ":inventory_slot_no", 8),#给马留的位置
                    (ge, "$mission_show_horse", 0),#生成了马
                    (agent_get_item_id, ":item_no", "$mission_show_horse"),
                 (else_try),
                    (eq, ":inventory_slot_no", 8),#给马留的位置
                    (assign, ":item_no", -1),
                 (else_try),
                    (agent_get_item_slot, ":item_no", "$mission_show_agent", ":inventory_slot_no"),
                 (try_end),
                 (gt, ":item_no", 0),
                 (str_store_item_name, s1, ":item_no"),
                 (str_store_item_name_plural, s2, ":item_no"),
                 (overlay_set_text, "$g_presentation_text_9", "@{s1}^^{s2}^"),#物品介绍
        (try_end),
       ]),
  ]),




  ("character_window", 0, 0,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (try_begin),
          (eq, 1,0),
          (create_mesh_overlay, reg1, "mesh_character_background"),
        (try_end),
 
        (try_for_range, ":count_no", 0, 200),
           (troop_set_slot, "trp_temp_array_a", ":count_no", -1),#clear all temp arrays
        (try_end),
        (assign, "$active_choose_1", -1),
        (assign, "$active_choose_2", -1),

        (create_button_overlay, "$g_presentation_obj_1", "@Back"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

#        (store_mul, ":cur_troop", "trp_player", 2),#with weapons
#        (create_mesh_overlay_with_tableau_material, "$g_presentation_obj_2", -1, "tableau_game_character_sheet", ":cur_troop"),
#        (position_set_x, pos1, 60),
#        (position_set_y, pos1, 455),
#        (overlay_set_position, "$g_presentation_obj_2", pos1),
#        (position_set_x, pos1, 700),
#        (position_set_y, pos1, 800),
#        (overlay_set_size, "$g_presentation_obj_2", pos1),

##__________________________________from here begins the basic porperty's part____________________________________________________

        (create_text_overlay, reg1, "@ ", tf_scrollable),
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 290),
        (position_set_y, pos1, 300),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (try_for_range, ":count", 0, 4),
           (store_add, ":string_no", ":count", "str_strength"),
           (str_store_string, s1, ":string_no"),

           (store_div, ":count_1", ":count", 2),
           (store_mod, ":count_2", ":count", 2),
           (store_mul, ":high", ":count_1", -20),
           (val_add, ":high", 460),

           (create_button_overlay, reg1, s1),
           (try_begin),
              (eq, ":count_2", 0),
              (position_set_x, pos1, 0),
           (else_try),
              (position_set_x, pos1, 140),
           (try_end),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (store_add, ":attribute_no", ":count", ca_strength),
           (store_attribute_level, ":attribute_level", "trp_player", ":attribute_no"),
           (assign, reg2, ":attribute_level"),
           (create_button_overlay, reg1, "@_{reg2}_"),
           (try_begin),
              (eq, ":count_2", 0),
              (position_set_x, pos1, 100),
           (else_try),
              (position_set_x, pos1, 240),
           (try_end),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (try_for_range, ":count", 0, 7),
           (store_add, ":string_no", ":count", "str_wpt_one_handed"),
           (str_store_string, s1, ":string_no"),

           (store_div, ":count_1", ":count", 2),
           (store_mod, ":count_2", ":count", 2),
           (store_mul, ":high", ":count_1", -20),
           (val_add, ":high", 400),

           (create_button_overlay, reg1, s1),
           (try_begin),
              (eq, ":count_2", 0),
              (position_set_x, pos1, 0),
           (else_try),
              (position_set_x, pos1, 140),
           (try_end),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (store_add, ":weapon_no", wpt_one_handed_weapon, ":count"),
           (store_proficiency_level, ":weapon_level", "trp_player", ":weapon_no"),
           (assign, reg2, ":weapon_level"),
           (create_button_overlay, reg1, "@_{reg2}_"),
           (try_begin),
              (eq, ":count_2", 0),
              (position_set_x, pos1, 100),
           (else_try),
              (position_set_x, pos1, 240),
           (try_end),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (assign, ":count_3", -1),
        (try_for_range, ":count", 0, 42),
           (store_sub, ":skill_no", skl_reserved_18, ":count"),
           (store_skill_level, ":skill_level", ":skill_no", "trp_player"),
           (gt, ":skill_level", 0),
           (val_add, ":count_3", 1),

           (store_add, ":string_no", ":count", "str_reserved_18"),
           (str_store_string, s1, ":string_no"),

           (store_div, ":count_1", ":count_3", 2),
           (store_mod, ":count_2", ":count_3", 2),
           (store_mul, ":high", ":count_1", -20),
           (val_add, ":high", 300),

           (create_button_overlay, reg1, s1),
           (try_begin),
              (eq, ":count_2", 0),
              (position_set_x, pos1, 0),
           (else_try),
              (position_set_x, pos1, 140),
           (try_end),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (assign, reg2, ":skill_level"),
           (create_button_overlay, reg1, "@_{reg2}_"),
           (try_begin),
              (eq, ":count_2", 0),
              (position_set_x, pos1, 100),
           (else_try),
              (position_set_x, pos1, 240),
           (try_end),
           (position_set_y, pos1, ":high"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (set_container_overlay, -1),

#        (create_game_button_overlay, "$g_presentation_obj_3", "@View_basic_porperty", tf_center_justify),
#        (position_set_x, pos1, 150),
#        (position_set_y, pos1, 425),
#        (overlay_set_position, "$g_presentation_obj_3", pos1),

##__________________________________from here begins the passive skills' part____________________________________________________

        (create_text_overlay, reg1, "@_", tf_scrollable),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 470),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 160),
        (position_set_y, pos1, 205),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":height", 5000),
        (store_add, ":passive_skill_begin", "itm_passive_skills_begin", 1),
        (try_for_range, ":passive_skill_no", ":passive_skill_begin", "itm_passive_skills_end"),
           (assign, ":continue", 0),
           (try_begin),
              (call_script, "script_check_troop_passive_skill_activited", "trp_player", ":passive_skill_no"),
              (gt, reg1, 0),                  #activited
              (assign, ":continue", 1),
           (else_try),
              (call_script, "script_check_troop_passive_skill_activited", "trp_player", ":passive_skill_no"),
              (le, reg1, 0),
              (call_script, "script_check_troop_passive_skill_learned", "trp_player", ":passive_skill_no"),
              (gt, reg1, 0),                  #learned but not activated, active
              (ge, "$passive_skill_show", 1),
              (assign, ":continue", 2),
           (else_try),
              (call_script, "script_check_troop_passive_skill_activited", "trp_player", ":passive_skill_no"),
              (le, reg1, 0),
              (call_script, "script_check_troop_passive_skill_learned", "trp_player", ":passive_skill_no"),
              (le, reg1, 0),                  #havent learned, learned but not activated, active
              (eq, "$passive_skill_show", 2),
              (assign, ":continue", 3),
           (try_end),

           (gt, ":continue", 0),
           (str_store_item_name, s1, ":passive_skill_no"),
           (create_button_overlay, reg1, "@{s1}_Lv{reg1}"),
           (try_begin),
              (eq, ":continue", 3),
              (overlay_set_color, reg1, 0xFF0000),
           (else_try),
              (overlay_set_color, reg1, 0xFFFFFF),
           (try_end),
           (position_set_x, pos1, 0),
           (position_set_y, pos1, ":height"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (troop_set_slot, "trp_temp_array_a", reg1, ":passive_skill_no"),

           (val_sub, ":height", 40),
        (try_end),

        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_1", "@_", tf_scrollable),
        (position_set_x, pos1, 540),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_text_1", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_text_1", pos1),
        (position_set_x, pos1, 240),
        (position_set_y, pos1, 100),
        (overlay_set_area_size, "$g_presentation_text_1", pos1),
        (overlay_set_color, "$g_presentation_text_1", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_2", "@_"),
        (position_set_x, pos1, 640),
        (position_set_y, pos1, 640),
        (overlay_set_position, "$g_presentation_text_2", pos1),
        (overlay_set_color, "$g_presentation_text_2", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_3", "@_"),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 470),
        (overlay_set_position, "$g_presentation_text_3", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_3", pos1),
        (overlay_set_color, "$g_presentation_text_3", 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_progressbar"),
        (position_set_x, pos1, 540),
        (position_set_y, pos1, 470),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 310),
        (position_set_y, pos1, 700),
        (overlay_set_size, reg1, pos1),

        (create_mesh_overlay, "$g_presentation_progress_bar_1", "mesh_white_plane"),
        (overlay_set_color, "$g_presentation_progress_bar_1", 0x6699cc),       #progress bar
        (position_set_x, pos1, 540),
        (position_set_y, pos1, 477),
        (overlay_set_position, "$g_presentation_progress_bar_1", pos1),
        (position_set_x, pos1, 9880),
        (position_set_y, pos1, 370),
        (overlay_set_size, "$g_presentation_progress_bar_1", pos1),
        (overlay_set_display, "$g_presentation_progress_bar_1", 0),

        (create_mesh_overlay_with_item_id, "$g_presentation_obj_4", "itm_passive_skills_begin"),
        (position_set_x, pos1, 580),
        (position_set_y, pos1, 640),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        (overlay_set_display, "$g_presentation_obj_4", 0),


        (str_store_string, s1, "@Show_all_passive_skills"),
        (call_script, "script_create_special_button_overlay", 463, 645),
        (assign, "$g_presentation_obj_5", reg1),

        (str_store_string, s1, "@Activite_this_passive_skills"),
        (call_script, "script_create_special_button_overlay", 463, 590),
        (assign, "$g_presentation_obj_6", reg1),

        (str_store_string, s1, "@Suspend_this_passive_skills"),
        (call_script, "script_create_special_button_overlay", 463, 535),
        (assign, "$g_presentation_obj_7", reg1),

        (str_store_string, s1, "@Suspend_all_passive_skills"),
        (call_script, "script_create_special_button_overlay", 463, 480),
        (assign, "$g_presentation_obj_8", reg1),

##__________________________________from here begins the active skills' part____________________________________________________

        (create_text_overlay, "$g_presentation_text_4", "@All_selected_active_skills", tf_scrollable),
        (position_set_x, pos1, 845),
        (position_set_y, pos1, 365),
        (overlay_set_position, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 55),
        (overlay_set_area_size, "$g_presentation_text_4", pos1),
        (overlay_set_color, "$g_presentation_text_4", 0xFFFFFF),

        (assign, ":cur_x", 400),
        (try_for_range, ":count_no", 1, 7),                                                                                 #six selected skills
           (create_image_button_overlay, reg0, "mesh_inventory_empty_slot", "mesh_inventory_highlight"),
           (create_mesh_overlay, reg1, "mesh_inventory_highlight"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, 350),
           (overlay_set_position, reg0, pos1),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 70),
           (position_set_y, pos1, 70),
           (overlay_set_size, reg0, pos1),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg0, 2),
           (overlay_set_additional_render_height, reg1, 1),
           (troop_set_slot, "trp_temp_array_a", reg0, ":count_no"),

           (store_add, ":string_no", "str_key_1", ":count_no"),
           (val_sub, ":string_no", 1),
           (str_store_string, s1, ":string_no"),
           (store_add, ":cur_x_1", ":cur_x", 35),
           (create_text_overlay, reg1, s1, tf_center_justify),
           (position_set_x, pos1, ":cur_x_1"),
           (position_set_y, pos1, 320),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (val_add, ":cur_x", 75),
        (try_end),

        (str_store_string, s1, "@Suspend_selected_active_skills"),
        (call_script, "script_create_special_button_overlay", 918, 330),
        (assign, "$g_presentation_obj_9", reg1),

        (create_text_overlay, reg1, "@_", tf_scrollable),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 200),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":cur_x", 35),
        (assign, ":cur_y", 1000),
        (store_add, ":active_begin", "itm_active_skills_begin", 1),                                #skills can be selected
        (try_for_range, ":active_skill_no", ":active_begin", "itm_active_skills_end"),
           (create_mesh_overlay_with_item_id, reg1, ":active_skill_no"),
           (position_set_x, pos1, ":cur_x"),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 840),
           (position_set_y, pos1, 840),
           (overlay_set_size, reg1, pos1),
           (overlay_set_additional_render_height, reg1, 2),

           (store_sub, ":cur_x_1", ":cur_x", 35),
           (store_sub, ":cur_y_1", ":cur_y", 35),
           (create_image_button_overlay, reg2, "mesh_inventory_empty_slot", "mesh_inventory_highlight"),
           (position_set_x, pos1, ":cur_x_1"),
           (position_set_y, pos1, ":cur_y_1"),
           (overlay_set_position, reg2, pos1),
           (position_set_x, pos1, 70),
           (position_set_y, pos1, 70),
           (overlay_set_size, reg2, pos1),
           (overlay_set_additional_render_height, reg2, 1),
           (troop_set_slot, "trp_temp_array_a", reg2, ":active_skill_no"),

           (try_begin),
              (neq, ":cur_x", 260),
              (val_add, ":cur_x", 75),
           (else_try),
              (assign, ":cur_x", 35),
              (val_sub, ":cur_y", 75),
           (try_end),
        (try_end),

        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_5", "@_", tf_scrollable),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 170),
        (overlay_set_position, "$g_presentation_text_5", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_5", pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 120),
        (overlay_set_area_size, "$g_presentation_text_5", pos1),
        (overlay_set_color, "$g_presentation_text_5", 0xFFFFFF),

        (str_store_string, s1, "@Activite_this_active_skills"),
        (call_script, "script_create_special_button_overlay", 848, 130),
        (assign, "$g_presentation_obj_10", reg1),

        (troop_get_slot, ":skill_no", "trp_player", slot_troop_active_skill_1),
        (try_begin),
           (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
           (assign, ":skill_no", 0),
        (try_end),
        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_1", ":skill_no"),
        (position_set_x, pos1, 435),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_mesh_1", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_mesh_1", pos1),
        (overlay_set_additional_render_height, "$g_presentation_mesh_1", 3),

        (troop_get_slot, ":skill_no", "trp_player", slot_troop_active_skill_2),
        (try_begin),
           (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
           (assign, ":skill_no", 0),
        (try_end),
        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_2", ":skill_no"),
        (position_set_x, pos1, 510),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_mesh_2", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_mesh_2", pos1),
        (overlay_set_additional_render_height, "$g_presentation_mesh_2", 3),

        (troop_get_slot, ":skill_no", "trp_player", slot_troop_active_skill_3, ":skill_no"),
        (try_begin),
           (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
           (assign, ":skill_no", 0),
        (try_end),
        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_3", ":skill_no"),
        (position_set_x, pos1, 585),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_mesh_3", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_mesh_3", pos1),
        (overlay_set_additional_render_height, "$g_presentation_mesh_3", 3),

        (troop_get_slot, ":skill_no", "trp_player", slot_troop_active_skill_4),
        (try_begin),
           (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
           (assign, ":skill_no", 0),
        (try_end),
        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_4", ":skill_no"),
        (position_set_x, pos1, 660),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_mesh_4", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_mesh_4", pos1),
        (overlay_set_additional_render_height, "$g_presentation_mesh_4", 3),

        (troop_get_slot, ":skill_no", "trp_player", slot_troop_active_skill_5),
        (try_begin),
           (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
           (assign, ":skill_no", 0),
        (try_end),
        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_5", ":skill_no"),
        (position_set_x, pos1, 735),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_mesh_5", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_mesh_5", pos1),
        (overlay_set_additional_render_height, "$g_presentation_mesh_5", 3),

        (troop_get_slot, ":skill_no", "trp_player", slot_troop_active_skill_6),
        (try_begin),
           (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
           (assign, ":skill_no", 0),
        (try_end),
        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_6", ":skill_no"),
        (position_set_x, pos1, 810),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_mesh_6", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_mesh_6", pos1),
        (overlay_set_additional_render_height, "$g_presentation_mesh_6", 3),

        (create_text_overlay, "$g_presentation_text_6", "@_"),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 165),
        (overlay_set_position, "$g_presentation_text_6", pos1),

        (create_text_overlay, "$g_presentation_text_7", "@_"),
        (position_set_x, pos1, 805),
        (position_set_y, pos1, 165),
        (overlay_set_position, "$g_presentation_text_7", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_7", pos1),

            ####### mouse fix pos system #######
        (call_script, "script_mouse_fix_pos_load"),
            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
       ]),

      (ti_on_presentation_run,
       [
            ####### mouse fix pos system #######
        (call_script, "script_mouse_fix_pos_run"),
            ####### mouse fix pos system #######
        ]),

      (ti_on_presentation_mouse_enter_leave,
         [(store_trigger_param_1, ":object"),
          (store_trigger_param_2, ":enter_leave"),
          (try_begin),
             (is_between, ":object", "$g_presentation_text_4", "$g_presentation_obj_9"),
             (troop_get_slot, ":count_no", "trp_temp_array_a", ":object"),
             (is_between, ":count_no", 1, 7),
             (try_begin),
                (eq, ":enter_leave", 0),#enter
                (call_script, "script_highlight_certain_block", ":object"),
             (else_try),#leave
                (neq, "$active_choose_1", ":count_no"),
                (call_script, "script_lowlight_certain_block", ":object"),
             (try_end),
          (try_end),
        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
           (show_object_details_overlay, 1),
           (finish_mission, 0),
           (change_screen_map),
#        (else_try),
#           (eq, ":object", "$g_presentation_obj_3"),
#           (presentation_set_duration, 0),
#           (finish_mission, 0),
#           (change_screen_view_character),

##________________________________________________________passive part___________________________________________________________________
        (else_try),
           (is_between, ":object", "$g_presentation_obj_3", "$g_presentation_text_1"),                                  #choose passive skills
           (troop_get_slot, "$passive_skill_choosen", "trp_temp_array_a", ":object"),
           (str_store_item_name_plural, s1, "$passive_skill_choosen"),
           (overlay_set_text, "$g_presentation_text_1", "@{s1}^_"),

           (overlay_set_display, "$g_presentation_obj_4", 0),
           (create_mesh_overlay_with_item_id, "$g_presentation_obj_4", "$passive_skill_choosen"),
           (position_set_x, pos1, 580),
           (position_set_y, pos1, 640),
           (overlay_set_position, "$g_presentation_obj_4", pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, "$g_presentation_obj_4", pos1),
           (overlay_set_display, "$g_presentation_obj_4", 1),

           (overlay_set_text, "$g_presentation_text_2", "@_"),
           (try_begin),
              (item_has_property, "$passive_skill_choosen", itp_always_loot),#dangerous
              (overlay_set_text, "$g_presentation_text_2", "@Dangerous"),
              (overlay_set_color, "$g_presentation_text_2", 0xFF0033),
           (try_end),

           (overlay_set_text, "$g_presentation_text_3", "@_"),
           (overlay_set_display, "$g_presentation_progress_bar_1", 0),
           (try_begin),
              (call_script, "script_check_troop_passive_skill_activited", "trp_player", "$passive_skill_choosen"),#Only activited passive skills show the progressbar.
              (gt, reg1, 0),

              (overlay_set_text, "$g_presentation_text_3", "@Lv{reg1}"),
              (item_get_weight, ":max grade", "$passive_skill_choosen"),
              (val_div, ":max grade", 1000),                                                      #max grade
              (store_mul, ":length", reg1, 9880),
              (val_div, ":length", ":max grade"),
              (position_set_x, pos1, ":length"),
              (position_set_y, pos1, 370),
              (overlay_set_size, "$g_presentation_progress_bar_1", pos1),
              (overlay_set_display, "$g_presentation_progress_bar_1", 1),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),                                                                                   #show all passive skills
           (try_begin),
              (eq, "$passive_skill_show", 1),
              (assign, "$passive_skill_show", 2),#show all skills
           (else_try),
              (eq, "$passive_skill_show", 2),
              (assign, "$passive_skill_show", 0),#only show active skills
           (else_try),
              (assign, "$passive_skill_show", 1),#show skills learned
           (try_end),
           (start_presentation, "prsnt_character_window"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_6"),                                                                                    #activitive passive skills
           (gt, "$passive_skill_choosen", 0),
           (call_script, "script_check_troop_passive_skill_learned", "trp_player", "$passive_skill_choosen"),
           (try_begin),
              (le, reg1, 0),
              (display_message, "@Cant_acttivite_this_skill", 0xFF0000),
           (try_end),
           (gt, reg1, 0),

           (overlay_set_text, "$g_presentation_text_3", "@Lv{reg1}"),
           (item_get_weight, ":max_grade", "$passive_skill_choosen"),#max grade
           (val_div, ":max_grade", 1000),
           (store_mul, ":length", reg1, 9880),
           (val_div, ":length", ":max_grade"),
           (position_set_x, pos1, ":length"),
           (position_set_y, pos1, 370),
           (overlay_set_size, "$g_presentation_progress_bar_1", pos1),
           (overlay_set_display, "$g_presentation_progress_bar_1", 1),
           (call_script, "script_set_troop_passive_skill_on", "trp_player", "$passive_skill_choosen", reg1),

        (else_try),
           (eq, ":object", "$g_presentation_obj_7"),                                                                                   #suspend choosed passive skill
           (gt, "$passive_skill_choosen", 0),
           (call_script, "script_set_troop_passive_skill_on", "trp_player", "$passive_skill_choosen", 0),

           (assign, ":end_cond", "$g_presentation_text_1"),
           (try_for_range, ":overlay_id", "$g_presentation_obj_3", ":end_cond"),
              (troop_slot_eq, "trp_temp_array_a", ":overlay_id", "$passive_skill_choosen"),
              (assign, ":end_cond", 0),#break
           (try_end),
           (overlay_set_text, "$g_presentation_text_3", "@_"),
           (overlay_set_display, "$g_presentation_progress_bar_1", 0),

        (else_try),
           (eq, ":object", "$g_presentation_obj_8"),                                                                                   #suspend all passive skills
           (store_add, ":passive_skill_begin", "itm_passive_skills_begin", 1),
           (try_for_range, ":passive_skill_no", ":passive_skill_begin", "itm_passive_skills_end"),
              (call_script, "script_set_troop_passive_skill_on", "trp_player", ":passive_skill_no", 0),
           (try_end),
           (start_presentation, "prsnt_character_window"),

##________________________________________________________active part___________________________________________________________________

        (else_try),
           (is_between, ":object", "$g_presentation_text_4", "$g_presentation_obj_9"),                       #selected active skills slot
           (troop_get_slot, ":count_no", "trp_temp_array_a", ":object"),
           (is_between, ":count_no", 1, 7),
           (try_begin),
              (neg|is_between, "$active_choose_2", "itm_active_skills_begin", "itm_active_skills_end"),
              (store_add, ":slot_no", ":count_no", slot_troop_active_skill_1),
              (val_sub, ":slot_no", 1),
              (troop_get_slot, ":skill_no", "trp_player", ":slot_no"),
              (is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
              (call_script, "script_cf_show_active_skill", ":skill_no"),
              (assign, "$active_choose_2", ":skill_no"),
           (try_end),
           (try_begin),
              (eq, ":count_no", "$active_choose_1"),
              (call_script, "script_lowlight_certain_block", ":object"),
              (assign, "$active_choose_1", -1),
           (else_try),
              (try_for_range, ":overlay_no", "$g_presentation_text_4", "$g_presentation_obj_9"),
                 (gt, "$active_choose_1", 0),
                 (troop_slot_eq, "trp_temp_array_a", ":overlay_no", "$active_choose_1"),
                 (call_script, "script_lowlight_certain_block", ":overlay_no"),
              (try_end),
              (call_script, "script_highlight_certain_block", ":object"),
              (assign, "$active_choose_1", ":count_no"),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_9"),                                                                              #suspend selected active skill
           (gt, "$active_choose_1", 0),
           (try_for_range, ":overlay_no", "$g_presentation_text_4", "$g_presentation_obj_9"),
              (gt, "$active_choose_1", 0),
              (troop_slot_eq, "trp_temp_array_a", ":overlay_no", "$active_choose_1"),
              (call_script, "script_lowlight_certain_block", ":overlay_no"),
           (try_end),
           (store_add, ":slot_no", "$active_choose_1", slot_troop_active_skill_1),
           (val_sub, ":slot_no", 1),
           (troop_set_slot, "trp_player", ":slot_no", -1),
           (call_script, "script_active_skill_mesh_change", "$active_choose_1", 0),
           (assign, "$active_choose_1", -1),

        (else_try),
           (neq, ":object", "$g_presentation_obj_9"),
           (is_between, ":object", "$g_presentation_obj_9", "$g_presentation_text_5"),                       #show an active skill
           (troop_get_slot, ":active_skill_no", "trp_temp_array_a", ":object"),
           (call_script, "script_cf_show_active_skill", ":active_skill_no"),
           (assign, "$active_choose_2", ":active_skill_no"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_10"),                                                                              #activite an active skill
           (try_begin),
              (le, "$active_choose_1", 0),
              (assign, ":end_cond", 7),
              (try_for_range, ":count_no", 1, ":end_cond"),
                 (store_add, ":slot_no", ":count_no", slot_troop_active_skill_1),
                 (val_sub, ":slot_no", 1),
                 (troop_get_slot, ":skill_no", "trp_player", ":slot_no"),
                 (neg|is_between, ":skill_no", "itm_active_skills_begin", "itm_active_skills_end"),#emtpy
                 (troop_set_slot, "trp_player", ":slot_no", "$active_choose_2"),
                 (call_script, "script_active_skill_mesh_change", ":count_no", "$active_choose_2"),
                 (assign, ":end_cond", 1),#break
              (try_end),
           (else_try),
              (is_between, "$active_choose_1", 1, 7),
              (store_add, ":slot_no", "$active_choose_1", slot_troop_active_skill_1),
              (val_sub, ":slot_no", 1),
              (troop_set_slot, "trp_player", ":slot_no", "$active_choose_2"),
              (call_script, "script_active_skill_mesh_change", "$active_choose_1", "$active_choose_2"),
              (try_for_range, ":overlay_no", "$g_presentation_text_4", "$g_presentation_obj_9"),
                 (troop_slot_eq, "trp_temp_array_a", ":overlay_no", "$active_choose_1"),
                 (call_script, "script_lowlight_certain_block", ":overlay_no"),
              (try_end),
              (assign, "$active_choose_1", -1),
           (try_end),

        (try_end),
       ]),
  ]),


  ("character_state_view", 0, mesh_character_background,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (create_button_overlay, "$g_presentation_obj_1", "@Done", tf_center_justify),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_text_overlay, reg1, "@state_introduce", tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 620),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 100),
        (overlay_set_area_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (create_text_overlay, reg1, "@_", tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 500),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":cur_y", 50),
        (store_add, ":state_begin", "itm_state_begin", 1),
        (try_for_range, ":state_no", ":state_begin", "itm_state_end"),
           (create_mesh_overlay_with_item_id, reg1, ":state_no"),
           (position_set_x, pos1, 35),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 700),
           (position_set_y, pos1, 700),
           (overlay_set_size, reg1, pos1),

           (str_store_item_name, s1, ":state_no"),
           (create_button_overlay, reg1, s1),
           (position_set_x, pos1, 65),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (troop_set_slot, "trp_temp_array_a", reg1, ":state_no"),
           (val_add, ":cur_y", 70),
        (try_end),

        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_obj_2", "@_", tf_scrollable),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 200),
        (overlay_set_area_size, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),

        (create_mesh_overlay_with_item_id, "$g_presentation_mesh_1", 0),
        (position_set_x, pos1, 345),
        (position_set_y, pos1, 48),
        (overlay_set_position, "$g_presentation_mesh_1", pos1),

        (create_text_overlay, "$g_presentation_obj_3", "@_"),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 240),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_3", pos1),
        (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_obj_4", "@_"),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        (overlay_set_color, "$g_presentation_obj_4", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_obj_5", "@_"),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 160),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_5", pos1),
        (overlay_set_color, "$g_presentation_obj_5", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_obj_6", "@_"),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 120),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_6", pos1),
        (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFF),

            ####### mouse fix pos system #######
        (call_script, "script_mouse_fix_pos_load"),
            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
       ]),

      (ti_on_presentation_run,
       [
            ####### mouse fix pos system #######
        (call_script, "script_mouse_fix_pos_run"),
            ####### mouse fix pos system #######
        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
           (start_presentation, "prsnt_character_window_pass"),
        (else_try),
           (is_between, ":object", "$g_presentation_obj_1", "$g_presentation_obj_2"),
           (troop_get_slot, ":state_no", "trp_temp_array_a", ":object"),
           (str_store_item_name_plural, s1, ":state_no"),
           (overlay_set_text, "$g_presentation_obj_2", s1),

           (overlay_set_display, "$g_presentation_mesh_1", 0),
           (create_mesh_overlay_with_item_id, "$g_presentation_mesh_1", ":state_no"),
           (position_set_x, pos1, 345),
           (position_set_y, pos1, 480),
           (overlay_set_position, "$g_presentation_mesh_1", pos1),

           (try_begin),
              (item_has_property, ":state_no", itp_unique),
              (str_store_string, s1, "str_timing_type"),
              (item_get_abundance, reg1, ":state_no"),
              (str_store_string, s2, "str_basic_timer_add"),
              (item_get_max_ammo, reg2, ":state_no"),
              (str_store_string, s3, "str_basic_timer"),
              (item_get_food_quality, reg3, ":state_no"),
              (str_store_string, s4, "str_basic_timer_minus"),
           (else_try),
              (item_has_property, ":state_no", itp_always_loot),
              (str_store_string, s1, "str_counting_type"),
              (str_store_string, s2, "@_"),
              (item_get_max_ammo, reg2, ":state_no"),
              (str_store_string, s3, "str_basic_times"),
              (str_store_string, s4, "@_"),
           (else_try),
              (str_store_string, s1, "str_unlimited"),
              (str_store_string, s2, "@_"),
              (str_store_string, s3, "@_"),
              (str_store_string, s4, "@_"),
           (try_end),
           (overlay_set_text, "$g_presentation_obj_3", s1),
           (overlay_set_text, "$g_presentation_obj_4", s2),
           (overlay_set_text, "$g_presentation_obj_5", s3),
           (overlay_set_text, "$g_presentation_obj_6", s4),
        (try_end),
       ]),
  ]),


  ("character_window_pass", 0, mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (create_game_button_overlay, "$g_presentation_obj_1", "@View_character_window", tf_center_justify),
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 425),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        (create_game_button_overlay, "$g_presentation_obj_2", "@View_basic_porperty", tf_center_justify),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 425),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

        (create_game_button_overlay, "$g_presentation_obj_3", "@View_state", tf_center_justify),
        (position_set_x, pos1, 550),
        (position_set_y, pos1, 425),
        (overlay_set_position, "$g_presentation_obj_3", pos1),

        (create_game_button_overlay, "$g_presentation_obj_4", "@Done", tf_center_justify),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 425),
        (overlay_set_position, "$g_presentation_obj_4", pos1),

        (presentation_set_duration, 999999),
       ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (call_script, "script_character_window", "trp_player"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),
           (change_screen_view_character),
        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),
           (start_presentation, "prsnt_character_state_view"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),
           (presentation_set_duration, 0),
           (change_screen_map),
        (try_end),
       ]),
  ]),


#########################################################新阵营面板/兵种树##################################################
####
  ("faction_window",0,mesh_faction_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

#faction_choosen>> the object of whole prsnt about. When it is 0, showed the retrival.
#faction_showed>> what is showed in main area, including retrival, introduction, member and army.
#faction_biref_show/troop_biref_show/lord_biref_show>> Brief information showed in the right side of prsnt, the note part.
#faction_grade/faction_character/faction_affiliation is three retrival conditions.

#_________________________________________________________________________________initialization___________________________________________________________________________
        (try_for_range, ":count_no", 0, 500),
           (troop_set_slot, "trp_temp_array_a", ":count_no", -1),
           (troop_set_slot, "trp_temp_array_b", ":count_no", -1),
           (troop_set_slot, "trp_temp_array_c", ":count_no", -1),
        (try_end),

        (assign, "$g_presentation_obj_1", -1),
        (assign, "$g_presentation_obj_2", -1),
        (assign, "$g_presentation_obj_3", -1),
        (assign, "$g_presentation_obj_4", -1),

        (assign, "$g_presentation_retrival_1", -1),
        (assign, "$g_presentation_retrival_2", -1),
        (assign, "$g_presentation_retrival_3", -1),

#______________________________________________________________________________unchangeable prsnt______________________________________________________________________
        (try_begin),
           (gt, "$faction_chossen", 0),
           (call_script, "script_faction_superior_country_check", "$faction_chossen", 0),
           (gt, reg1, 0),
           (try_begin),
              (eq, reg1, "itm_kingdom_1"),
              (assign, ":mesh_no", "mesh_background_powell"),
           (else_try),
              (eq, reg1, "itm_kingdom_2"),
              (assign, ":mesh_no", "mesh_background_yishith"),
           (else_try),
              (eq, reg1, "itm_kingdom_3"),
              (assign, ":mesh_no", "mesh_background_korouto"),
           (else_try),
              (eq, reg1, "itm_kingdom_4"),
              (assign, ":mesh_no", "mesh_background_confederation"),
           (else_try),
              (eq, reg1, "itm_kingdom_5"),
              (assign, ":mesh_no", "mesh_background_papal"),
           (else_try),
              (eq, reg1, "itm_kingdom_6"),
              (assign, ":mesh_no", "mesh_background_longshu"),
           (else_try),
              (eq, reg1, "itm_kingdom_7"),
              (assign, ":mesh_no", "mesh_background_starkhook"),
           (else_try),
              (eq, reg1, "itm_kingdom_8"),
              (assign, ":mesh_no", "mesh_background_state"),
           (try_end),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_abyssal_order", 0),
           (assign, ":mesh_no", "mesh_background_abyss"),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_desertus_tribe", 0),
           (assign, ":mesh_no", "mesh_background_desertus"),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_demon", 0),
           (assign, ":mesh_no", "mesh_background_demon"),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_undead_association", 0),
           (assign, ":mesh_no", "mesh_background_undead"),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_adventurers_association", 0),
           (assign, ":mesh_no", "mesh_background_association"),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_libra", 0),
           (assign, ":mesh_no", "mesh_background_libra"),
        (else_try),
           (gt, "$faction_chossen", 0),
           (call_script, "script_cf_faction_superior_check", "$faction_chossen", "itm_ownerless_one", 0),
           (assign, ":mesh_no", "mesh_background_ownerless_one"),
        (else_try),
           (assign, ":mesh_no", "mesh_faction_window"),
        (try_end),
        (create_mesh_overlay, reg1, ":mesh_no"),
        (overlay_set_additional_render_height, reg1, -1),

        (create_mesh_overlay, reg1, "mesh_faction_panel"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 660),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 700),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -1),

        (create_mesh_overlay, reg1, "mesh_faction_note"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 50),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),

        (create_button_overlay, "$g_presentation_obj_1", "@Back", tf_center_justify),
        (position_set_x, pos1, 885),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

#_________________________________________________________________________________top and button part______________________________________________________________________
        (try_begin),
           (gt, "$faction_chossen", 0),
           (str_store_item_name, s1, "$faction_chossen"),
        (else_try),
           (str_store_string, s1, "@Retrieval"),
        (try_end),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 720),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (try_begin),
           (gt, "$faction_chossen", 0),
           (item_get_slot, ":culture_faction_no", "$faction_chossen", slot_item_faction_related),
           (faction_get_color, ":color_no", ":culture_faction_no"),
           (create_mesh_overlay, reg1, "mesh_white_plane"),
           (overlay_set_color, reg1, ":color_no"),
           (position_set_x, pos1, 485),
           (position_set_y, pos1, 675),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1500),
           (position_set_y, pos1, 1500),
           (overlay_set_size, reg1, pos1),
        (try_end),

        (str_store_string, s1, "@简 介 "),
        (call_script, "script_create_special_button_overlay", 88, 690),
        (assign, "$g_presentation_button_1", reg1),

        (str_store_string, s1, "@成 员 "),
        (call_script, "script_create_special_button_overlay", 228, 690),
        (assign, "$g_presentation_button_2", reg1),

        (str_store_string, s1, "@军 事 力 量 "),
        (call_script, "script_create_special_button_overlay", 368, 690),
        (assign, "$g_presentation_button_3", reg1),

        (str_store_string, s1, "@_"),
        (call_script, "script_create_special_button_overlay", 633, 690),
        (assign, "$g_presentation_button_4", reg1),

        (str_store_string, s1, "@_"),
        (call_script, "script_create_special_button_overlay", 773, 690),
        (assign, "$g_presentation_button_5", reg1),

        (str_store_string, s1, "@_"),
        (call_script, "script_create_special_button_overlay", 913, 690),
        (assign, "$g_presentation_button_6", reg1),


        (create_button_overlay, "$g_presentation_obj_2", "@势 力 检 索 ", tf_center_justify),
        (position_set_x, pos1, 775),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),

#_________________________________________________________________________________member part__________________________________________________________________________
#leader and other information show in the left part, unscrollable
        (try_begin),
           (eq, "$faction_showed", 2),
           (gt, "$faction_chossen", 0),

           (create_text_overlay, reg1, "str_leader", tf_center_justify),
           (position_set_x, pos1, 100),
           (position_set_y, pos1, 630),
           (overlay_set_position, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (create_text_overlay, reg1, "str_pillar", tf_center_justify),
           (position_set_x, pos1, 300),
           (position_set_y, pos1, 630),
           (overlay_set_position, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (create_text_overlay, reg1, "str_normal_member", tf_center_justify),
           (position_set_x, pos1, 500),
           (position_set_y, pos1, 630),
           (overlay_set_position, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (call_script, "script_faction_leader_check", "$faction_chossen"),
           (try_begin),
              (ge, reg1, 0),
              (assign, ":faction_affiliation_no", reg1),
              (val_mul, reg1, 10),
              (assign, ":leader_faction_no", reg2),
              (val_add, ":leader_faction_no", reg1),                                                          #10*id+type(0>>faction and 1>>troop)
              (call_script, "script_draw_faction_image", ":faction_affiliation_no", reg2, 100, 540),
              (troop_set_slot, "trp_temp_array_a", reg1, ":leader_faction_no"),
           (try_end),

           (item_get_abundance, ":count_no", "$faction_chossen"),                        #faction_power_structure
           (try_begin),
              (gt, ":count_no", 3),#防止默认填0时输出为100
              (assign, ":count_no", 0),
           (try_end),
           (store_add, ":string_no", ":count_no", "str_power_structure_default"),
           (str_store_string, s1, ":string_no"),
           (str_store_string, s2, "str_power_structure"),
           (create_text_overlay, reg1, "@{s2}:_{s1}", tf_center_justify),
           (position_set_x, pos1, 100),
           (position_set_y, pos1, 430),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (try_begin),
              (eq, ":count_no", 0),#default
              (overlay_set_color, reg1, 0xCCCCCC),
           (else_try),
              (eq, ":count_no", 1),#autocrat
              (overlay_set_color, reg1, 0x336688),
           (else_try),
              (eq, ":count_no", 2),#centralization
              (overlay_set_color, reg1, 0x6699CC),
           (else_try),
              (eq, ":count_no", 3),#co-discussion
              (overlay_set_color, reg1, 0x99CCFF),
           (try_end),

           (store_add, ":string_no", ":count_no", "str_power_structure_default_description"),
           (str_store_string, s1, ":string_no"),
           (create_text_overlay, reg1, s1, tf_scrollable),
           (position_set_x, pos1, 10),
           (position_set_y, pos1, 300),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (position_set_x, pos1, 180),
           (position_set_y, pos1, 100),
           (overlay_set_area_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (call_script, "script_faction_pillar_number_check", "$faction_chossen"),
           (str_store_string, s1, "str_pillar"),
           (assign, ":member_count_1", reg1),
           (create_text_overlay, reg1, "@{s1}数 量 :_{reg1}", tf_center_justify),
           (position_set_x, pos1, 100),
           (position_set_y, pos1, 270),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (call_script, "script_faction_normal_number_check", "$faction_chossen"),
           (str_store_string, s1, "str_normal_member"),
           (assign, ":member_count_2", reg1),
           (create_text_overlay, reg1, "@{s1}数 量 : {reg1}", tf_center_justify),
           (position_set_x, pos1, 100),
           (position_set_y, pos1, 240),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (val_max, ":member_count_1", ":member_count_2"),

           (create_mesh_overlay, reg1, "mesh_white_plane"),
           (position_set_x, pos1, 200),
           (position_set_y, pos1, 55),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 50),
           (position_set_y, pos1, 28500),
           (overlay_set_size, reg1, pos1),

           (create_mesh_overlay, reg1, "mesh_white_plane"),
           (position_set_x, pos1, 400),
           (position_set_y, pos1, 55),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 50),
           (position_set_y, pos1, 28500),
           (overlay_set_size, reg1, pos1),
        (try_end),

#_______________________________________________________________________________________右侧简讯栏____________________________________________________________________________
        (try_begin),
           (gt, "$faction_biref_show", 0),
           (call_script, "script_faction_brief_show", "$faction_biref_show"),
        (else_try),
           (gt, "$lord_biref_show", 0),
           (call_script, "script_lord_brief_show", "$lord_biref_show"),
        (else_try),
           (gt, "$troop_biref_show", 0),
           (call_script, "script_troop_brief_show", "$troop_biref_show"),
        (try_end),

#_______________________________________________________________________________________main part____________________________________________________________________________
        (create_text_overlay, "$g_presentation_container_1", "@ ", tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 70),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 550),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),
#________________________________________________________________________________________retrival___________________________________________________________________________
        (try_begin),
           (le, "$faction_showed", 0),
           (le, "$faction_chossen", 0),

           (assign, ":cur_y", 30),
           (store_add, ":faction_begin", "itm_faction_begin", 1),
           (try_for_range, ":count_no", ":faction_begin", "itm_faction_end"),
              (item_get_difficulty, ":grade_no", ":count_no"),#faction grade
              (ge, ":grade_no", 1),
              (call_script, "script_cf_faction_retrival_check", ":count_no"),

              (str_store_item_name, s1, ":count_no"),
              (create_button_overlay, reg1, s1),
              (position_set_x, pos1, 20),
              (position_set_y, pos1, ":cur_y"),
              (overlay_set_position, reg1, pos1),
              (position_set_x, pos1, 1000),
              (position_set_y, pos1, 1000),
              (overlay_set_size, reg1, pos1),
              (overlay_set_color, reg1, 0xFFFFFF),
              (val_add, ":cur_y", 30),
              (troop_set_slot, "trp_temp_array_a", reg1, ":count_no"),
           (try_end),
#_____________________________________________________________________________________introduction___________________________________________________________________________
        (else_try),
           (eq, "$faction_showed", 1),
           (gt, "$faction_chossen", 0),

           (create_mesh_overlay_with_item_id, reg1, "$faction_chossen"),
           (position_set_x, pos1, 300),
           (position_set_y, pos1, 540),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 2500),
           (position_set_y, pos1, 2500),
           (overlay_set_size, reg1, pos1),

           (str_store_item_name_plural, s1, "$faction_chossen"),
           (create_text_overlay, reg1, s1, tf_scrollable),
           (position_set_x, pos1, 20),
           (position_set_y, pos1, 320),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (position_set_x, pos1, 560),
           (position_set_y, pos1, 70),
           (overlay_set_area_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (item_get_difficulty, ":grade_no", "$faction_chossen"),#派系等级
           (val_sub, ":grade_no", 1),
           (val_add, ":grade_no", "str_faction_grade_1"),
           (str_store_string, s1, ":grade_no"),
           (create_text_overlay, reg1, s1),
           (position_set_x, pos1, 40),
           (position_set_y, pos1, 250),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (try_begin),
              (eq, ":grade_no", "str_faction_grade_1"),
              (overlay_set_color, reg1, 0xCCCCCC),
           (else_try),
              (eq, ":grade_no", "str_faction_grade_2"),
              (overlay_set_color, reg1, 0xFFCCCC),
           (else_try),
              (eq, ":grade_no", "str_faction_grade_3"),
              (overlay_set_color, reg1, 0xFF9999),
           (else_try),
              (eq, ":grade_no", "str_faction_grade_4"),
              (overlay_set_color, reg1, 0xFF6666),
           (else_try),
              (eq, ":grade_no", "str_faction_grade_5"),
              (overlay_set_color, reg1, 0xFF3333),
           (try_end),

           (item_get_thrust_damage, reg1, "$faction_chossen"),#order and chaos
           (item_get_swing_damage, reg2, "$faction_chossen"),#good_and_evil
           (try_begin),
              (le, reg1, 30),
              (str_store_string, s1, "@中 立 "),
           (else_try),
              (item_get_thrust_damage_type, ":return_value", "$faction_chossen"),#0秩序1混乱
              (try_begin),
                 (eq, ":return_value", 0),
                 (str_store_string, s1, "@秩 序 "),
              (else_try),
                 (str_store_string, s1, "@混 乱 "),
              (try_end),
           (try_end),
           (try_begin),
              (le, reg2, 30),
              (str_store_string, s2, "@中 庸 "),
           (else_try),
              (item_get_swing_damage_type, ":return_value", "$faction_chossen"),#0善良1邪恶
              (try_begin),
                 (eq, ":return_value", 0),
                 (str_store_string, s2, "@善 良 "),
              (else_try),
                 (str_store_string, s2, "@邪 恶 "),
              (try_end),
           (try_end),
           (create_text_overlay, reg1, "@{s1}{s2}_({reg1}|{reg2})_"),
           (position_set_x, pos1, 40),
           (position_set_y, pos1, 220),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (store_add, ":count_no", reg1, reg2),
           (try_begin),
              (gt, ":count_no", 60),
              (overlay_set_color, reg1, 0x66CC00),
           (else_try),
              (gt, ":count_no", 0),
              (overlay_set_color, reg1, 0xCCFFFF),
           (else_try),
              (eq, ":count_no", 0),
              (overlay_set_color, reg1, 0xCCCCCC),
           (else_try),
              (ge, ":count_no", -60),
              (overlay_set_color, reg1, 0xCC99FF),
           (else_try),
              (overlay_set_color, reg1, 0x9933FF),
           (try_end),

           (item_get_slot, reg1, "$faction_chossen", slot_faction_relation_with_player),
           (create_text_overlay, reg1, "@与 玩 家 的 关 系 ： {reg1}"),
           (position_set_x, pos1, 400),
           (position_set_y, pos1, 220),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (create_mesh_overlay, reg1, "mesh_white_plane"),
           (position_set_x, pos1, 25),
           (position_set_y, pos1, 200),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 27500),
           (position_set_y, pos1, 50),
           (overlay_set_size, reg1, pos1),

           (create_text_overlay, reg1, "@上 级 势 力 ", tf_center_justify),
           (position_set_x, pos1, 300),
           (position_set_y, pos1, 160),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (try_begin),
              (call_script, "script_get_faction_affiliation", "$faction_chossen", 0),
              (gt, reg1, 0),
              (assign, ":faction_affiliation_no", reg1),
              (call_script, "script_draw_faction_image", ":faction_affiliation_no", 0, 100, 100),
              (assign, "$g_presentation_obj_4", reg1),

              (call_script, "script_get_faction_position", "$faction_chossen", 0),
              (val_add, reg1, "str_normal_member"),
              (str_store_string, s1, reg1),
              (create_text_overlay, reg1, "@该 势 力 在 上 级 势 力 中 的 地 位 为 ： {s1}", tf_center_justify),
              (position_set_x, pos1, 400),
              (position_set_y, pos1, 90),
              (overlay_set_position, reg1, pos1),
              (position_set_x, pos1, 1000),
              (position_set_y, pos1, 1000),
              (overlay_set_size, reg1, pos1),
              (overlay_set_color, reg1, 0xFFFFFF),
           (try_end),

           (store_relation, reg1, ":culture_faction_no", "fac_player_supporters_faction"),
           (create_text_overlay, reg1, "@总 阵 营 与 玩 家 的 关 系 ： {reg1}", tf_center_justify),
           (position_set_x, pos1, 400),
           (position_set_y, pos1, 60),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
#_____________________________________________________________________________________member___________________________________________________________________________
        (else_try),
           (eq, "$faction_showed", 2),#显示派系成员
           (gt, "$faction_chossen", 0),

           (store_mul, ":cur_y", ":member_count_1", 150),
           (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),#阵营类型的支柱
              (call_script, "script_get_faction_affiliation", ":count_no", 0),
              (eq, reg1, "$faction_chossen"),
              (call_script, "script_get_faction_position", ":count_no", 0),
              (eq, reg1, 1),#pillar
              (call_script, "script_draw_faction_image", ":count_no", 0, 250, ":cur_y"),
              (store_mul, ":member_faction_no", ":count_no", 10),
              (troop_set_slot, "trp_temp_array_a", reg1, ":member_faction_no"),
              (val_sub, ":cur_y", 150),
           (try_end),

           (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),#兵种类型的支柱
              (troop_is_hero, ":count_no"),
              (call_script, "script_get_faction_affiliation", ":count_no", 1),
              (eq, reg1, "$faction_chossen"),
              (call_script, "script_get_faction_position", ":count_no", 1),
              (eq, reg1, 1),#pillar
              (call_script, "script_draw_faction_image", ":count_no", 1, 250, ":cur_y"),
              (store_mul, ":member_troop_no", ":count_no", 10),
              (val_add, ":member_troop_no", 1),
              (troop_set_slot, "trp_temp_array_a", reg1, ":member_troop_no"),
              (val_sub, ":cur_y", 150),
           (try_end),

           (store_mul, ":cur_y", ":member_count_1", 150),
           (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),#阵营类型的普通成员
              (call_script, "script_get_faction_affiliation", ":count_no", 0),
              (eq, reg1, "$faction_chossen"),
              (call_script, "script_get_faction_position", ":count_no", 0),
              (eq, reg1, 0),#normal member
              (call_script, "script_draw_faction_image", ":count_no", 0, 450, ":cur_y"),
              (store_mul, ":member_faction_no", ":count_no", 10),
              (troop_set_slot, "trp_temp_array_a", reg1, ":member_faction_no"),
              (val_sub, ":cur_y", 150),
           (try_end),

           (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),#兵种类型的普通成员
              (troop_is_hero, ":count_no"),
              (call_script, "script_get_faction_affiliation", ":count_no", 1),
              (eq, reg1, "$faction_chossen"),
              (call_script, "script_get_faction_position", ":count_no", 1),
              (eq, reg1, 0),#normal member
              (call_script, "script_draw_faction_image", ":count_no", 1, 450, ":cur_y"),
              (store_mul, ":member_troop_no", ":count_no", 10),
              (val_add, ":member_troop_no", 1),
              (troop_set_slot, "trp_temp_array_a", reg1, ":member_troop_no"),
              (val_sub, ":cur_y", 150),
           (try_end),

#_________________________________________________________________________________________troop__________________________________________________________________________
        (else_try),
           (eq, "$faction_showed", 3),
           (gt, "$faction_chossen", 0),

           (assign, reg2, 100), #纵轴
           (try_for_range_backwards, ":cur_troop_no", soldiers_begin, soldiers_end),           # find all root troops of selected faction
              (neg|troop_is_hero, ":cur_troop_no"),
              (troop_slot_eq, ":cur_troop_no", slot_troop_affiliation, "$faction_chossen"),
              (call_script, "script_faction_troop_tree_recursive_backtracking", ":cur_troop_no", 50, reg2, 125),
              (val_add, reg2, 200),
           (try_end),
           (assign, ":cur_y", reg2),
           (val_sub,  ":cur_y", 80),

           (create_mesh_overlay, reg1, "mesh_white_plane"),
           (position_set_x, pos1, 25),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 27500),
           (position_set_y, pos1, 50),
           (overlay_set_size, reg1, pos1),

           (val_add,  ":cur_y", 10),
           (try_for_range, ":count_no", 1, 4),
              (call_script, "script_cf_get_faction_template", "$faction_chossen", ":count_no"),
              (val_sub, reg1, party_template_uesd_begin),
              (val_add, reg1, party_template_name_begin),
              (str_store_string, s10, reg1),
              (create_text_overlay, reg3, "@{s10}（ {reg2}%） "),
              (position_set_x, pos1, 25),
              (position_set_y, pos1, ":cur_y"),
              (overlay_set_position, reg3, pos1),
              (position_set_x, pos1, 800),
              (position_set_y, pos1, 800),
              (overlay_set_size, reg3, pos1),
              (overlay_set_color, reg3, 0xFFFFFF),
              (val_add, ":cur_y", 20),
           (try_end),

           (create_text_overlay, reg1, "@该 阵 营 提 供 的 部 队 模 板 及 概 率 ： "),
           (position_set_x, pos1, 25),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
        (try_end),

        (set_container_overlay, -1),

#_______________________________________________________________________________retrival condition__________________________________________________________________________

        (try_begin),
           (le, "$faction_showed", 0),
           (le, "$faction_chossen", 0),

           (create_text_overlay, reg1, "@检 索 条 件 ", tf_center_justify),
           (position_set_x, pos1, 535),
           (position_set_y, pos1, 220),
           (overlay_set_position, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (create_text_overlay, reg1, "@势 力 规 模 "),
           (position_set_x, pos1, 435),
           (position_set_y, pos1, 180),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (create_text_overlay, reg1, "@势 力 性 质 "),
           (position_set_x, pos1, 435),
           (position_set_y, pos1, 120),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (create_text_overlay, reg1, "@势 力 所 属 "),
           (position_set_x, pos1, 435),
           (position_set_y, pos1, 60),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1000),
           (position_set_y, pos1, 1000),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),

           (try_begin),
              (le, "$faction_grade", 0),
              (str_store_string, s1, "@全 部 "),
           (else_try),
              (store_add, ":string_no", "$faction_grade", "str_faction_grade_1"),
              (val_sub, ":string_no", 1),
              (str_store_string, s1, ":string_no"),
           (try_end),
           (call_script, "script_create_special_button_overlay", 580, 180),
           (assign, "$g_presentation_retrival_1", reg1),

           (try_begin),
              (le, "$faction_character", 0),
              (str_store_string, s1, "@全 部 "),
           (else_try),
              (le, "$faction_character", 1),
              (str_store_string, s1, "@国 家 及 所 属 势 力 "),
           (else_try),
              (le, "$faction_character", 2),
              (str_store_string, s1, "@非 国 家 势 力 "),
           (try_end),
           (call_script, "script_create_special_button_overlay", 580, 120),
           (assign, "$g_presentation_retrival_2", reg1),

           (try_begin),
              (le, "$faction_affiliation", 0),
              (str_store_string, s1, "@全 部 "),
           (else_try),
              (le, "$faction_affiliation", 1),
              (str_store_string, s1, "@无 上 级 势 力 "),
           (else_try),
              (le, "$faction_affiliation", 2),
              (str_store_string, s1, "@有 上 级 势 力 "),
           (else_try),
              (le, "$faction_affiliation", 3),
              (str_store_string, s1, "@无 下 属 势 力 "),
           (else_try),
              (le, "$faction_affiliation", 4),
              (str_store_string, s1, "@有 下 属 势 力 "),
           (try_end),
           (call_script, "script_create_special_button_overlay", 580, 60),
           (assign, "$g_presentation_retrival_3", reg1),
        (try_end),

            ####### mouse fix pos system #######
        (call_script, "script_mouse_fix_pos_load"),
            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
       ]),

      (ti_on_presentation_run,
       [
            ####### mouse fix pos system #######
        (call_script, "script_mouse_fix_pos_run"),
            ####### mouse fix pos system #######
        ]),

      (ti_on_presentation_mouse_enter_leave, [
         (store_trigger_param_1, ":object"),
         (store_trigger_param_2, ":enter_leave"),
         (try_begin),
            (gt, "$troop_biref_show", 0),
            (is_between, ":object", "$g_presentation_obj_3", "$g_presentation_container_1"),
            (troop_get_inventory_capacity, ":inventroy_limit", "$troop_biref_show"),
            (try_begin),
               (eq, ":enter_leave", 0),#enter
               (try_for_range, ":inventory_slot_no", 0, ":inventroy_limit"),
                  (troop_slot_eq, "trp_temp_array_b", ":inventory_slot_no", ":object"),
                  (troop_get_inventory_slot, ":item_no", "$troop_biref_show", ":inventory_slot_no"),
                  (gt, ":item_no", -1),
                  (troop_get_inventory_slot_modifier, ":modifier_no", "$troop_biref_show", ":inventory_slot_no"),

                  (troop_get_slot, ":inventroy_position", "trp_temp_array_c", ":inventory_slot_no"),
                  (overlay_get_position, pos0, ":inventroy_position"),
                  (show_item_details_with_modifier, ":item_no", ":modifier_no", pos0, 100),
                  (assign, "$g_current_opened_item_details", ":inventory_slot_no"),
               (try_end),
            (else_try),
               (eq, ":enter_leave", 1),#leave
               (try_for_range, ":inventory_slot_no", 0, ":inventroy_limit"),
                  (troop_slot_eq, "trp_temp_array_b", ":inventory_slot_no", ":object"),
                  (eq, "$g_current_opened_item_details", ":inventory_slot_no"),
                  (close_item_details),
               (try_end),
           (try_end),
        (try_end),
        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
         (else_try),                                                                         #show retrival
           (eq, ":object", "$g_presentation_obj_2"),
           (assign, "$faction_showed", 0),
           (assign, "$faction_chossen", 0),
           (start_presentation, "prsnt_faction_window"),
#_______________________________________________________________________________main button__________________________________________________________________________
        (else_try),
           (gt, "$faction_chossen", 0),
           (lt, ":object", "$g_presentation_obj_2"),
           (try_begin),
              (eq, ":object", "$g_presentation_button_1"),
              (neq, "$faction_showed", 1),
              (assign, "$faction_showed", 1),
              (start_presentation, "prsnt_faction_window"),
           (else_try),
              (eq, ":object", "$g_presentation_button_2"),
              (neq, "$faction_showed", 2),
              (assign, "$faction_showed", 2),
              (start_presentation, "prsnt_faction_window"),
           (else_try),
              (eq, ":object", "$g_presentation_button_3"),
              (neq, "$faction_showed", 3),
              (assign, "$faction_showed", 3),
              (start_presentation, "prsnt_faction_window"),
           (else_try),
              (eq, ":object", "$g_presentation_button_4"),
              (neq, "$faction_showed", 4),
              (assign, "$faction_showed", 4),
              (start_presentation, "prsnt_faction_window"),
           (else_try),
              (eq, ":object", "$g_presentation_button_5"),
              (neq, "$faction_showed", 5),
              (assign, "$faction_showed", 5),
              (start_presentation, "prsnt_faction_window"),
           (else_try),
              (eq, ":object", "$g_presentation_button_6"),
              (neq, "$faction_showed", 6),
              (assign, "$faction_showed", 6),
              (start_presentation, "prsnt_faction_window"),
           (try_end),

#__________________________________________________________________________________retrival__________________________________________________________________________
        (else_try),                                                                            #retrival show brief
           (le, "$faction_showed", 0),
           (le, "$faction_chossen", 0),
           (troop_slot_ge, "trp_temp_array_a", ":object", 1),
           (troop_get_slot, "$faction_biref_show", "trp_temp_array_a", ":object"),
           (assign, "$lord_biref_show", -1),
           (assign, "$troop_biref_show", -1),
           (start_presentation, "prsnt_faction_window"),
        (else_try),
           (le, "$faction_showed", 0),
           (le, "$faction_chossen", 0),
           (eq, ":object", "$g_presentation_retrival_1"),
           (val_add, "$faction_grade", 1),
           (try_begin),
              (eq, "$faction_grade", 6),
              (assign, "$faction_grade", 0),
           (try_end),
           (start_presentation, "prsnt_faction_window"),
        (else_try),
           (le, "$faction_showed", 0),
           (le, "$faction_chossen", 0),
           (eq, ":object", "$g_presentation_retrival_2"),
           (val_add, "$faction_character", 1),
           (try_begin),
              (eq, "$faction_character", 3),
              (assign, "$faction_character", 0),
           (try_end),
           (start_presentation, "prsnt_faction_window"),
        (else_try),
           (le, "$faction_showed", 0),
           (le, "$faction_chossen", 0),
           (eq, ":object", "$g_presentation_retrival_3"),
           (val_add, "$faction_affiliation", 1),
           (try_begin),
              (eq, "$faction_affiliation", 5),
              (assign, "$faction_affiliation", 0),
           (try_end),
           (start_presentation, "prsnt_faction_window"),

#_______________________________________________________________________________右侧简讯栏__________________________________________________________________________
        (else_try),                                                                          #enter another faction's window
           (gt, "$faction_biref_show", 0),
           (eq, ":object", "$g_presentation_obj_3"),
           (assign, "$faction_chossen", "$faction_biref_show"),
           (assign, "$faction_biref_show", -1),
           (assign, "$lord_biref_show", -1),
           (assign, "$troop_biref_show", -1),
           (start_presentation, "prsnt_faction_window"),
        (else_try),                                                                          #show brief information in the right part, used in introduction part
           (eq, "$faction_showed", 1),
           (gt, "$faction_chossen", 0),
           (eq, ":object", "$g_presentation_obj_4"),
           (call_script, "script_get_faction_affiliation", "$faction_chossen", 0),
           (gt, reg1, 0),
           (assign, "$faction_biref_show", reg1),
           (assign, "$lord_biref_show", -1),
           (assign, "$troop_biref_show", -1),
           (start_presentation, "prsnt_faction_window"),
        (else_try),                                                                          #show brief information in the right part, used in member part
           (eq, "$faction_showed", 2),
           (gt, "$faction_chossen", 0),
           (troop_slot_ge, "trp_temp_array_a", ":object", 1),
           (troop_get_slot, ":target_no", "trp_temp_array_a", ":object"),
           (store_mod, ":type_no", ":target_no", 10),
           (val_div, ":target_no", 10),
           (try_begin),
              (eq, ":type_no", 1),#troop
              (assign, "$faction_biref_show", -1),
              (assign, "$lord_biref_show", ":target_no"),
           (else_try),
              (assign, "$faction_biref_show", ":target_no"),
              (assign, "$lord_biref_show", -1),
           (try_end),
           (assign, "$troop_biref_show", -1),
           (start_presentation, "prsnt_faction_window"),
        (else_try),                                                                          #show brief information in the right part, used in troop part
           (eq, "$faction_showed", 3),
           (gt, "$faction_chossen", 0),
           (troop_slot_ge, "trp_temp_array_a", ":object", 1),
           (troop_get_slot, ":troop_no", "trp_temp_array_a", ":object"),
           (assign, "$faction_biref_show", -1),
           (assign, "$lord_biref_show", -1),
           (assign, "$troop_biref_show", ":troop_no"),
           (start_presentation, "prsnt_faction_window"),
        (try_end),
       ]),
  ]),



##############################################################新会战######################################################
####
  ("center_sandbox_window", 0, 0, [
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (try_for_range, ":count_no", 0, 300),#清空数据
           (troop_set_slot, "trp_temp_array_new_map_3", ":count_no", -1),
        (try_end),
        (try_begin),
           (ge, "$g_sandbox_chosse", 0),
           (assign, ":cur_x", "$g_current_rank"),
           (assign, ":cur_y", "$g_current_procession"),
           (val_mul, ":cur_x", 10000),
           (val_sub, ":cur_x", 5000),
           (val_mul, ":cur_y", 10000),
           (val_sub, ":cur_y", 5000),
           (init_position, pos50),
           (position_set_x, pos50, ":cur_x"),
           (position_set_y, pos50, ":cur_y"),#中心点位置
           (prop_instance_set_position, "$g_sandbox_chosse", pos50),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_1", "@显 示 所 有 区 块 的 划 分 "),
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_text_overlay, reg1, "@镜 头 ", tf_center_justify),
        (position_set_x, pos1, 70),
        (position_set_y, pos1, 130),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (create_image_button_overlay, "$g_presentation_obj_2", "mesh_overlay_arrow", "mesh_overlay_arrow_down"),#向下
        (init_position, pos1),
        (position_set_x, pos1, 70),
        (position_set_y, pos1, 105),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

        (create_image_button_overlay, reg1, "mesh_overlay_arrow", "mesh_overlay_arrow_down"),#向右
        (init_position, pos1),
        (position_set_x, pos1, 105, 1),
        (position_set_y, pos1, 140, 1),
        (overlay_set_position, reg1, pos1),
        (init_position, pos1),
        (position_rotate_z, pos1, 90),
        (overlay_set_mesh_rotation, reg1, pos1),

        (create_image_button_overlay, reg1, "mesh_overlay_arrow", "mesh_overlay_arrow_down"),#向上
        (init_position, pos1),
        (position_set_x, pos1, 70, 1),
        (position_set_y, pos1, 175, 1),
        (overlay_set_position, reg1, pos1),
        (init_position, pos1),
        (position_rotate_z, pos1, 180),
        (overlay_set_mesh_rotation, reg1, pos1),

        (create_image_button_overlay, reg1, "mesh_overlay_arrow", "mesh_overlay_arrow_down"),#向左
        (init_position, pos1),
        (position_set_x, pos1, 35, 1),
        (position_set_y, pos1, 140, 1),
        (overlay_set_position, reg1, pos1),
        (init_position, pos1),
        (position_rotate_z, pos1, 270),
        (overlay_set_mesh_rotation, reg1, pos1),

        (create_button_overlay, "$g_presentation_obj_3", "@显 示 任 务 地 点 "),
        (init_position, pos1),
        (position_set_x, pos1, 20),
        (position_set_y, pos1, 55),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_3", pos1),
        (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_4", "@使 用 说 明 "),
        (init_position, pos1),
        (position_set_x, pos1, 230),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (init_position, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        (overlay_set_color, "$g_presentation_obj_4", 0xFFFFFF),

        (create_mesh_overlay, reg1, "mesh_black_panel"), #上方横幅，用于填写地区和区块信息
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 690),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 80),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -2),

        (create_mesh_overlay, reg1, "mesh_black_panel"), #右侧窗口，用于操作
        (position_set_x, pos1, 775),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 225),
        (position_set_y, pos1, 775),
        (overlay_set_size, reg1, pos1),
        (overlay_set_additional_render_height, reg1, -2),
        (overlay_set_display, reg1, 0),

        (call_script, "script_get_center_zone_ground", "$current_town", "$g_current_rank", "$g_current_procession"), #区块名称
        (str_store_item_name, s1, reg1),
        (create_text_overlay, "$g_presentation_text_1", s1, tf_center_justify),
        (init_position, pos1),
        (position_set_x, pos1, 940),
        (position_set_y, pos1, 720),
        (overlay_set_position, "$g_presentation_text_1", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_text_1", pos1),
        (overlay_set_color, "$g_presentation_text_1", 0xFFFFFF),

        (assign, reg3, "$g_current_rank"), #坐标
        (assign, reg4, "$g_current_procession"),
        (create_text_overlay, reg1, "@({reg3}，{reg4}) ", tf_center_justify),
        (init_position, pos1),
        (position_set_x, pos1, 940),
        (position_set_y, pos1, 705),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),

        (try_begin),
           (call_script, "script_get_center_zone_building", "$current_town", "$g_current_rank", "$g_current_procession"),#建筑类型
           (assign, ":building_no", reg1),
           (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#有建筑
           (gt, ":building_no", "itm_building_begin"),
           (call_script, "script_cf_check_building_showed", "$current_town", "$g_current_rank", "$g_current_procession"),#已经发现

           (str_store_item_name, s1, ":building_no"),
           (create_text_overlay, "$g_presentation_text_2", s1, tf_center_justify),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 580),
           (overlay_set_position, "$g_presentation_text_2", pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, "$g_presentation_text_2", pos1),
           (overlay_set_color, "$g_presentation_text_2", 0xFFFFFF),

           (call_script, "script_get_center_zone_building_owner", "$current_town", "$g_current_rank", "$g_current_procession"),#建筑所有者
           (assign, ":building_owner_no", reg1),
           (is_between, ":building_owner_no", "itm_faction_begin", "itm_faction_end"),#有所有者
           (gt, ":building_owner_no", "itm_faction_begin"),

           (str_store_item_name, s1, ":building_owner_no"),
           (create_text_overlay, reg1, s1, tf_center_justify),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 530),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 900),
           (position_set_y, pos1, 900),
           (overlay_set_size, reg1, pos1),
           (item_get_slot, ":culture_faction_no", ":building_owner_no", slot_item_faction_related),
           (faction_get_color, ":color_no", ":culture_faction_no"),
           (overlay_set_color, reg1, ":color_no"),
        (try_end),

        (create_button_overlay, "$g_presentation_obj_5", "@进 入 该 区 域 "),
        (position_set_x, pos1, 790),
        (position_set_y, pos1, 110),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_5", pos1),
        (overlay_set_color, "$g_presentation_obj_5", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_6", "@前 往 该 区 域 "),
        (position_set_x, pos1, 790),
        (position_set_y, pos1, 110),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, "$g_presentation_obj_6", pos1),
        (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFF),
        (try_begin),
           (eq, "$g_current_rank", "$g_player_rank"),
           (eq, "$g_current_procession", "$g_player_procession"),#正在这个区块
           (overlay_set_display, "$g_presentation_obj_6", 0),
        (else_try),
           (overlay_set_display, "$g_presentation_obj_5", 0),
        (try_end),

##———————————————————————————————编队————————————————————————————————————
        (val_min, "$g_detachment_show", 1), #初始化，新启动界面时不会展示编队详情
        (create_image_button_overlay, "$g_presentation_obj_7", "mesh_command_arrow", "mesh_command_arrow_down"),
        (init_position, pos1),
        (position_set_x, pos1, 260),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (init_position, pos1),
        (position_rotate_z, pos1, 135),
        (overlay_set_mesh_rotation, "$g_presentation_obj_7", pos1),
        (init_position, pos1),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_7", pos1),
        (overlay_set_color, "$g_presentation_obj_7", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_container_1", "@_", tf_scrollable),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 210),
        (overlay_set_position, "$g_presentation_container_1", pos1),
        (position_set_x, pos1, 255),
        (position_set_y, pos1, 475),
        (overlay_set_area_size, "$g_presentation_container_1", pos1),
        (set_container_overlay, "$g_presentation_container_1"),

        (assign, ":cur_x", 0),
        (assign, ":cur_y", 5),
        (assign, ":count_no", 0),
        (try_for_range_backwards, ":slot_no", 0, "$g_total_detachment"), #遍历编队
           (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
           (party_slot_eq, ":temp_party_id", slot_tool_party_position_x, "$g_current_rank"),
           (party_slot_eq, ":temp_party_id", slot_tool_party_position_y, "$g_current_procession"),
           (call_script, "script_draw_detachment_window", ":temp_party_id", ":cur_x", ":cur_y"), #绘制单个编队的窗口
           (val_add, ":count_no", 1),
           (val_add, ":cur_y", 150),
        (try_end),
        (set_container_overlay, -1),

        (try_begin),
           (le, ":count_no", 0), #该区块无编队
           (overlay_set_display, "$g_presentation_container_1", 0), 
           (overlay_set_display, "$g_presentation_obj_7", 0), 
        (else_try),
           (gt, ":count_no", 0), #有编队且收起编队信息
           (lt, "$g_detachment_show", 1), 
           (position_set_x, pos1, -300),
           (position_set_y, pos1, 210),
           (overlay_set_position, "$g_presentation_container_1", pos1), #把container收回左侧
           (overlay_set_display, "$g_presentation_container_1", 0), 
           (init_position, pos1),
           (position_set_x, pos1, 10),
           (position_set_y, pos1, 410),
           (overlay_set_position, "$g_presentation_obj_7", pos1),
           (init_position, pos1),
           (position_rotate_z, pos1, -45),
           (overlay_set_mesh_rotation, "$g_presentation_obj_7", pos1),
           (init_position, pos1),
        (try_end),

        (create_mesh_overlay, "$g_presentation_obj_8", "mesh_campaign_detachment_window"),
        (position_set_x, pos1, 270),
        (position_set_y, pos1, 205),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_8", pos1),
        (overlay_set_alpha, "$g_presentation_obj_8", 0xFF),
        (overlay_set_display, "$g_presentation_obj_8", 0), 

        (create_text_overlay, reg1, "@ ", tf_scrollable), #编队成员、领队加成等文本
        (position_set_x, pos1, 285),
        (position_set_y, pos1, 230),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 270),
        (position_set_y, pos1, 425),
        (overlay_set_area_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFF),
        (overlay_set_display, reg1, 0),

            ####### mouse fix pos system #######
       (call_script, "script_mouse_fix_pos_load"),
            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
       ]),

     (ti_on_presentation_run,
      [
           ####### mouse fix pos system #######
       (call_script, "script_mouse_fix_pos_run"),
           ####### mouse fix pos system #######
       ]),

      (ti_on_presentation_run,
       [
          (key_clicked, key_right_mouse_button),
          (mouse_get_position, pos49),
          (mouse_get_world_projection, pos49, pos50),
          (call_script, "script_pos_aim_at_pos", pos49, pos50),#获取射击方向
          (cast_ray, reg1, pos50, pos49),
          (set_fixed_point_multiplier, 1000),
          (position_get_x, ":cur_x", pos50),
          (position_get_y, ":cur_y", pos50),
          (val_div, ":cur_x", 10000),
          (val_max, ":cur_x", 0),
          (val_min, ":cur_x", 14),
          (val_add, ":cur_x", 1),
          (val_div, ":cur_y", 10000),
          (val_max, ":cur_y", 0),
          (val_min, ":cur_y", 14),
          (val_add, ":cur_y", 1),
          (assign, "$g_current_rank", ":cur_x"),
          (assign, "$g_current_procession", ":cur_y"),

          (val_mul, ":cur_x", 10000),
          (val_sub, ":cur_x", 5000),
          (val_mul, ":cur_y", 10000),
          (val_sub, ":cur_y", 5000),
          (init_position, pos50),
          (position_set_x, pos50, ":cur_x"),
          (position_set_y, pos50, ":cur_y"),#中心点位置
          (prop_instance_set_position, "$g_sandbox_chosse", pos50),
          (start_presentation, "prsnt_center_sandbox_window"),
        ]),

      (ti_on_presentation_event_state_change,
       [(set_fixed_point_multiplier, 1000),
        (store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (scene_prop_get_visibility, ":visible_count", "$g_sandbox_full"),
           (try_begin),
              (eq, ":visible_count", 0), 
              (scene_prop_set_visibility, "$g_sandbox_full", 1),
              (overlay_set_text, "$g_presentation_obj_1", "@关 闭 所 有 区 块 的 显 示 "),
           (else_try),
              (eq, ":visible_count", 1), 
              (scene_prop_set_visibility, "$g_sandbox_full", 0),
              (overlay_set_text, "$g_presentation_obj_1", "@显 示 所 有 区 块 的 划 分 "),
           (try_end),
        (else_try),
           (is_between, ":object", "$g_presentation_obj_2", "$g_presentation_obj_3"),#镜头旋转
           (store_sub, ":count_no", ":object", "$g_presentation_obj_2"),
           (try_begin),
              (eq, ":count_no", 0), 
              (prop_instance_get_position, pos49, "$g_mission_cam"),#向下
              (position_rotate_x, pos49, -15),
              (prop_instance_set_position, "$g_mission_cam", pos49),
           (else_try),
              (eq, ":count_no", 1), 
              (prop_instance_get_position, pos49, "$g_mission_cam"),#向右
              (position_rotate_z, pos49, -15, 1),
              (prop_instance_set_position, "$g_mission_cam", pos49),
           (else_try),
              (eq, ":count_no", 2), 
              (prop_instance_get_position, pos49, "$g_mission_cam"),#向上
              (position_rotate_x, pos49, 15),
              (prop_instance_set_position, "$g_mission_cam", pos49),
           (else_try),
              (eq, ":count_no", 3), 
              (prop_instance_get_position, pos49, "$g_mission_cam"),#向左
              (position_rotate_z, pos49, 15, 1),
              (prop_instance_set_position, "$g_mission_cam", pos49),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),#显示任务地点
           (try_for_range, ":count_no", 1, 200),
              (troop_get_slot, ":instance_no", "trp_temp_array_new_map_2", ":count_no"),
              (gt, ":instance_no", 0),
              (scene_prop_get_visibility, ":visible_count", ":instance_no"),
              (val_sub, ":visible_count", 1),
              (val_abs, ":visible_count"),
              (scene_prop_set_visibility, ":instance_no", ":visible_count"),
           (try_end),
           (try_begin),
              (eq, ":visible_count", 1),
              (overlay_set_text, "$g_presentation_obj_3", "@隐 藏 任 务 地 点 "),
           (else_try),
              (overlay_set_text, "$g_presentation_obj_3", "@显 示 任 务 地 点 "),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),#教程
           (dialog_box, "@基 础 操 作 ： WASD前 后 左 右 移 动 镜 头 ， 左 下 角 箭 头 转 动 镜 头 ， 鼠 标 右 键 点 击 地 面 选 中 区 域 。 ^^使 用 方 式 ： 选 中 区 域 后 ， 点 击 “ 前 往 该 区 域 ” ， 进 入 后 即 可 使 用 各 种 功 能 。 在 地 图 边 缘 的 区 域 才 能 返 回 大 地 图 。 ^^探 索 ： 探 索 可 触 发 各 种 随 机 事 件 ， 部 分 技 能 的 提 升 可 缩 短 探 索 时 间 。 部 分 区 块 有 隐 藏 建 筑 ， 需 经 探 索 才 能 发 现 。 "),

        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),#进入该区域
           (presentation_set_duration, 0),
           (finish_mission),
#           (jump_to_menu, "mnu_center_new"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_6"),#前往该区域
           (assign, "$g_player_rank", "$g_current_rank"),
           (assign, "$g_player_procession", "$g_current_procession"),
           (start_presentation, "prsnt_center_sandbox_window"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_7"),#显隐编队展示
           (try_begin),
              (lt, "$g_detachment_show", 1), #隐藏编队信息时，点一下打开
              (init_position, pos1),
              (position_set_x, pos1, 0),
              (position_set_y, pos1, 210),
              (overlay_set_position, "$g_presentation_container_1", pos1), #把藏在左边的container移出来
              (overlay_set_display, "$g_presentation_container_1", 1), 
              (init_position, pos1),
              (position_set_x, pos1, 260),
              (position_set_y, pos1, 600),
              (overlay_set_position, "$g_presentation_obj_7", pos1),
              (init_position, pos1),
              (position_rotate_z, pos1, 135),
              (overlay_set_mesh_rotation, "$g_presentation_obj_7", pos1),
              (init_position, pos1),
              (assign, "$g_detachment_show", 1),
           (else_try),
              (eq, "$g_detachment_show", 1), #只展示了编队信息没展示编队详情，这时点此按钮会收起编队信息
              (position_set_x, pos1, -300),
              (position_set_y, pos1, 210),
              (overlay_set_position, "$g_presentation_container_1", pos1), #把container收回左侧
              (overlay_set_display, "$g_presentation_container_1", 0), 
              (init_position, pos1),
              (position_set_x, pos1, 10),
              (position_set_y, pos1, 410),
              (overlay_set_position, "$g_presentation_obj_7", pos1),
              (init_position, pos1),
              (position_rotate_z, pos1, -45),
              (overlay_set_mesh_rotation, "$g_presentation_obj_7", pos1),
              (init_position, pos1),
              (assign, "$g_detachment_show", 0),
           (else_try),
              (eq, "$g_detachment_show", 2), #编队详情也显示了的时候，按一下只关掉详情
              (overlay_set_display, "$g_presentation_obj_8", 0), #背景框
              (assign, ":object", "$g_presentation_obj_8"), 
              (val_add, ":object", 1),
              (overlay_set_display, ":object", 0), #文本
              (overlay_set_text, ":object", "@ "),
              (position_set_x, pos1, 260),
              (position_set_y, pos1, 600),
              (overlay_set_position, "$g_presentation_obj_7", pos1),
              (assign, "$g_detachment_show", 1),
           (try_end),

        (else_try),
           (is_between, ":object", "$g_presentation_container_1", "$g_presentation_obj_8"), #编队成员展示
           (neq, ":object", "$g_presentation_container_1"),
           (troop_get_slot, ":value_no", "trp_temp_array_new_map_3", ":object"),
           (ge, ":value_no", 0),
           (store_div, ":temp_party_id", ":value_no", 10),
           (val_mod, ":value_no", 10),

           (try_begin), #返回s1
              (eq, ":value_no", 0), #检测框，展示编队人员详情
              (str_store_string, s1, "@编 队 人 员 ： "),
              (party_get_num_companion_stacks, ":num_stacks", ":temp_party_id"),
              (try_for_range, ":i_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":stack_troop", ":temp_party_id", ":i_stack"),
                (str_store_troop_name, s3, ":stack_troop"),
                (try_begin),
                   (troop_is_hero, ":stack_troop"),
                   (store_troop_health, reg3, ":stack_troop"),
                   (str_store_string, s2, "@{s3}_（ {reg3}%） "),
                (else_try),
                   (party_stack_get_size, reg3, ":temp_party_id", ":i_stack"),
                   (party_stack_get_num_wounded, reg4, ":temp_party_id", ":i_stack"),
                   (store_sub, reg4, reg3, reg4),
                   (str_store_string, s2, "@{s3}_（ {reg4}/{reg3}） "),
                 (try_end),
                 (str_store_string, s1, "@{s1}^{s2}"),
              (try_end),
           (else_try),
              (eq, ":value_no", 2), #人头像，展示领队加成的教程框
              (party_stack_get_troop_id, ":stack_troop", ":temp_party_id", 0), #领队
              (str_store_troop_name, s1, ":stack_troop"),
           (try_end),

           (overlay_set_display, "$g_presentation_obj_8", 1), #背景框
           (assign, ":object", "$g_presentation_obj_8"), 
           (val_add, ":object", 1),
           (overlay_set_display, ":object", 1), #文本
           (overlay_set_text, ":object", s1),
           (position_set_x, pos1, 580),
           (position_set_y, pos1, 460),
           (overlay_set_position, "$g_presentation_obj_7", pos1),
           (assign, "$g_detachment_show", 2), #展开编队详情（展开了两层页面）
        (try_end),
       ]),
  ]),



##########################################################快速战斗和开局###################################################
#####
  ("game_custom_battle_designer", 0, -1, [
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (create_mesh_overlay, "$g_presentation_background_1", "mesh_entertain_mode"),
        (overlay_set_additional_render_height, "$g_presentation_background_1", -1),
        (create_mesh_overlay, "$g_presentation_background_2", "mesh_formidable_enemy_mode"),
        (overlay_set_additional_render_height, "$g_presentation_background_2", -2),
        (create_mesh_overlay, "$g_presentation_background_3", "mesh_campaign_mode"),
        (overlay_set_additional_render_height, "$g_presentation_background_3", -2),
        (create_mesh_overlay, "$g_presentation_background_4", "mesh_quick_battle_mode"),
        (overlay_set_additional_render_height, "$g_presentation_background_4", -2),

        (create_button_overlay, "$g_presentation_obj_1", "@回 归 ", tf_center_justify),#返回
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 30),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_2", "@娱 乐 割 草 ", tf_center_justify),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),
        (overlay_set_hilight_color, "$g_presentation_obj_2", 0xFFFFDD00),

        (create_button_overlay, "$g_presentation_obj_3", "@挑 战 劲 敌 ", tf_center_justify),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, "$g_presentation_obj_3", pos1),
        (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFF),
        (overlay_set_hilight_color, "$g_presentation_obj_3", 0xFFFFDD00),

        (create_button_overlay, "$g_presentation_obj_4", "@沙 盘 会 战 ", tf_center_justify),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        (overlay_set_color, "$g_presentation_obj_4", 0xFFFFFF),
        (overlay_set_hilight_color, "$g_presentation_obj_4", 0xFFFFDD00),

        (create_button_overlay, "$g_presentation_obj_5", "@快 速 战 斗 ", tf_center_justify),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 80),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
        (overlay_set_size, "$g_presentation_obj_5", pos1),
        (overlay_set_color, "$g_presentation_obj_5", 0xFFFFFF),
        (overlay_set_hilight_color, "$g_presentation_obj_5", 0xFFFFDD00),

        (create_text_overlay, "$g_presentation_text_1", "@娱 乐 割 草 ", tf_center_justify),#标题
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 700),
        (overlay_set_position, "$g_presentation_text_1", pos1),
        (position_set_x, pos1, 1700),
        (position_set_y, pos1, 1700),
        (overlay_set_size, "$g_presentation_text_1", pos1),
        (overlay_set_color, "$g_presentation_text_1", 0xFFFFFF),

        (create_text_overlay, "$g_presentation_text_2", "@娱 乐 割 草 模 式 下 玩 家 可 以 自 行 选 择 一 切 主 动 技 能 和 被 动 技 能 ， 并 且 设 置 敌 人 的 强 度 模 板 。 进 入 战 斗 后 请 尽 情 使 用 技 能 ， 享 受 割 草 的 快 感 。 ", tf_scrollable),#介绍
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 1100),
        (position_set_y, pos1, 1100),
        (overlay_set_size, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 300),
        (overlay_set_area_size, "$g_presentation_text_2", pos1),
        (overlay_set_color, "$g_presentation_text_2", 0xFFFFFF),

        (presentation_set_duration, 999999),
       ]),

      (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_2"),
           (overlay_set_additional_render_height, "$g_presentation_background_1", -1),
           (overlay_set_additional_render_height, "$g_presentation_background_2", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_3", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_4", -2),
           (overlay_set_text, "$g_presentation_text_1", "@娱 乐 割 草 "),
           (overlay_set_text, "$g_presentation_text_2", "@娱 乐 割 草 模 式 下 玩 家 可 以 自 行 选 择 一 切 主 动 技 能 和 被 动 技 能 ， 并 且 设 置 敌 人 的 强 度 模 板 。 进 入 战 斗 后 请 尽 情 使 用 技 能 ， 享 受 割 草 的 快 感 。 "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),
           (overlay_set_additional_render_height, "$g_presentation_background_1", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_2", -1),
           (overlay_set_additional_render_height, "$g_presentation_background_3", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_4", -2),
           (overlay_set_text, "$g_presentation_text_1", "@挑 战 劲 敌 "),
           (overlay_set_text, "$g_presentation_text_2", "@挑 战 劲 敌 模 式 允 许 玩 家 挑 战 在 剧 情 中 出 现 过 以 及 未 曾 登 场 过 的 一 切 头 目 单 位 。 头 目 将 会 有 远 比 一 般 战 斗 更 为 复 杂 的 行 为 模 式 和 技 能 。 "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),
           (overlay_set_additional_render_height, "$g_presentation_background_1", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_2", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_3", -1),
           (overlay_set_additional_render_height, "$g_presentation_background_4", -2),
           (overlay_set_text, "$g_presentation_text_1", "@沙 盘 会 战 "),
           (overlay_set_text, "$g_presentation_text_2", "@会 战 模 式 是 本 mod的 新 系 统 ， 在 大 地 图 与 进 场 战 斗 间 引 入 一 层 新 的 战 役 界 面 ， 实 现 远 程 火 力 投 射 甚 至 炮 击 、 埋 伏 与 侦 察 、 工 事 建 造 与 拆 毁 、 斩 首 、 后 勤 以 及 海 战 等 等 原 本 难 以 实 现 的 战 术 ， 并 且 — — 能 够 支 持 战 团 无 法 想 象 的 数 十 万 人 的 真 正 大 战 。 "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),
           (overlay_set_additional_render_height, "$g_presentation_background_1", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_2", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_3", -2),
           (overlay_set_additional_render_height, "$g_presentation_background_4", -1),
           (overlay_set_text, "$g_presentation_text_1", "@快 速 战 斗 "),
           (overlay_set_text, "$g_presentation_text_2", "@快 速 战 斗 模 式 中 玩 家 能 操 纵 几 种 特 殊 NPC ， 率 领 上 百 部 队 与 敌 人 来 一 场 短 平 快 的 白 刃 战 。 "),
        (try_end),
        ]),
    
      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),
           (presentation_set_duration, 0),
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),#割草模式
#录入数据
     (troop_raise_attribute, "trp_player", ca_strength, 23),#到30
     (troop_raise_attribute, "trp_player", ca_agility, 23),#到30
     (troop_raise_attribute, "trp_player", ca_intelligence, 13),#到20
     (troop_raise_attribute, "trp_player", ca_charisma, 13),#到20

     (troop_raise_skill, "trp_player", skl_ironflesh, 9),
     (troop_raise_skill, "trp_player", skl_power_strike, 9),
     (troop_raise_skill, "trp_player", skl_power_throw, 9),
     (troop_raise_skill, "trp_player", skl_power_draw, 9),
     (troop_raise_skill, "trp_player", skl_weapon_master, 8),
     (troop_raise_skill, "trp_player", skl_shield, 7),
     (troop_raise_skill, "trp_player", skl_athletics, 7),
     (troop_raise_skill, "trp_player", skl_riding, 7),
     (troop_raise_skill, "trp_player", skl_horse_archery, 6),
     (troop_raise_skill, "trp_player", skl_inventory_management, 15),
     (troop_raise_skill, "trp_player", skl_persuasion, 9),
     (troop_raise_skill, "trp_player", skl_memory, 9),

     (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 250),
     (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 250),
     (troop_raise_proficiency, "trp_player", wpt_polearm, 250),
     (troop_raise_proficiency, "trp_player", wpt_archery, 250),
     (troop_raise_proficiency, "trp_player", wpt_crossbow, 250),
     (troop_raise_proficiency, "trp_player", wpt_throwing, 250),
     (troop_raise_proficiency, "trp_player", wpt_firearm, 250),

     (call_script, "script_player_set_new_inventory_slot", ek_item_2, "itm_graghite_steel_bolts"),
     (call_script, "script_player_set_new_inventory_slot", ek_item_3, "itm_fengniao_jian"),
     (call_script, "script_player_set_new_inventory_slot", ek_head, "itm_papal_chain_hood"),
     (call_script, "script_player_set_new_inventory_slot", ek_body, "itm_vacuum_oath_armor"),
     (call_script, "script_player_set_new_inventory_slot", ek_foot, "itm_dark_oath_shoe"),
     (call_script, "script_player_set_new_inventory_slot", ek_gloves, "itm_dark_oath_hand"),
     (call_script, "script_player_set_new_inventory_slot", ek_horse, "itm_unicorn"),

     (call_script, "script_player_set_new_inventory_slot", 10, "itm_asterisk_staff"),
     (call_script, "script_player_set_new_inventory_slot", 11, "itm_jinshi_qishijian"),
     (call_script, "script_player_set_new_inventory_slot", 12, "itm_jiqiao_nu"),

     (call_script, "script_player_set_new_inventory_slot", 13, "itm_steel_shield"),
     (call_script, "script_player_set_new_inventory_slot", 14, "itm_phoenix_splendid_bow"),
     (call_script, "script_player_set_new_inventory_slot", 29, "itm_throwing_daggers"),

     (call_script, "script_player_set_new_inventory_slot", 30, "itm_sadi_dagger"),
     (call_script, "script_player_set_new_inventory_slot", 31, "itm_special_agent_sword"),
     (call_script, "script_player_set_new_inventory_slot", 32, "itm_heresy_hunter_armor"),
     (call_script, "script_player_set_new_inventory_slot", 33, "itm_papal_chain_hood"),
     (call_script, "script_player_set_new_inventory_slot", 34, "itm_heise_banlianjiaxue"),
     (call_script, "script_player_set_new_inventory_slot", 35, "itm_mogang_fangxing_bikai"),
     (call_script, "script_player_set_new_inventory_slot", 36, "itm_papal_dagger"),
     (call_script, "script_player_set_new_inventory_slot", 37, "itm_yejian_qiang"),
     (call_script, "script_player_set_new_inventory_slot", 38, "itm_ancient_papal_tower_shield"),
     (call_script, "script_player_set_new_inventory_slot", 39, "itm_patron_plate"),
     (call_script, "script_player_set_new_inventory_slot", 40, "itm_patron_high_plate"),
     (call_script, "script_player_set_new_inventory_slot", 41, "itm_purifier_eagle_tower_shield"),
     (call_script, "script_player_set_new_inventory_slot", 42, "itm_shouhuzhe_changqiang"),
     (call_script, "script_player_set_new_inventory_slot", 43, "itm_chaozhong_jixingkui"),
     (call_script, "script_player_set_new_inventory_slot", 44, "itm_zhengshi_banjiaxue"),
     (call_script, "script_player_set_new_inventory_slot", 45, "itm_duangang_banjiabikai"),
     (call_script, "script_player_set_new_inventory_slot", 46, "itm_patron_tower_shield"),
     (call_script, "script_player_set_new_inventory_slot", 47, "itm_stone_hammer"),
     (call_script, "script_player_set_new_inventory_slot", 48, "itm_kouruto_beast_sabre"),
     (call_script, "script_player_set_new_inventory_slot", 49, "itm_kouruto_beast_sabre_simple"),
     (call_script, "script_player_set_new_inventory_slot", 50, "itm_jinshi_cejian"),
     (call_script, "script_player_set_new_inventory_slot", 51, "itm_jinshi_longshoujian"),
     (call_script, "script_player_set_new_inventory_slot", 52, "itm_crushing_hammer"),
     (call_script, "script_player_set_new_inventory_slot", 53, "itm_bloodburst_sword"),
     (call_script, "script_player_set_new_inventory_slot", 54, "itm_westcoast_black_glove"),
     (call_script, "script_player_set_new_inventory_slot", 55, "itm_westcoast_guard_boot"),
     (call_script, "script_player_set_new_inventory_slot", 56, "itm_garrison_sickle_axe"),
     (call_script, "script_player_set_new_inventory_slot", 57, "itm_skull_staff"),
     (call_script, "script_player_set_new_inventory_slot", 58, "itm_bone_thruncheon"),
     (call_script, "script_player_set_new_inventory_slot", 59, "itm_death_omen"),
     (call_script, "script_player_set_new_inventory_slot", 60, "itm_ghost_knife"),
     (call_script, "script_player_set_new_inventory_slot", 61, "itm_ghost_dagger"),
     (call_script, "script_player_set_new_inventory_slot", 62, "itm_ghost_long_sword"),
     (call_script, "script_player_set_new_inventory_slot", 63, "itm_dolphin_chest_armor"),
     (call_script, "script_player_set_new_inventory_slot", 64, "itm_dolphin_chain_armor"),
     (call_script, "script_player_set_new_inventory_slot", 65, "itm_dolphin_mail_and_plate"),
     (call_script, "script_player_set_new_inventory_slot", 66, "itm_ghost_sickle"),

     (call_script, "script_player_set_new_inventory_slot", 67, "itm_fengniao_jian"),
     (call_script, "script_player_set_new_inventory_slot", 68, "itm_blood_extinguish_arrow"),

     (store_add, ":skill_begin", "itm_active_skills_begin", 1),
     (try_for_range, ":count_no", ":skill_begin", "itm_active_skills_end"),
        (call_script, "script_set_troop_active_skill_level", "trp_player", ":count_no"),#解锁全部主动技能
     (try_end),

     (store_add, ":skill_begin", "itm_passive_skills_begin", 1),
     (try_for_range, ":count_no", ":skill_begin", "itm_passive_skills_end"),
        (item_get_abundance, ":level_no", ":count_no"),
        (call_script, "script_set_troop_passive_skill_level", "trp_player", ":count_no", ":level_no"),#解锁全部被动技能
     (try_end),

           (jump_to_menu, "mnu_custom_battle_entertainment"),
           (presentation_set_duration, 0),

        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),#挑战强敌
#录入数据
     (troop_raise_attribute, "trp_player", ca_strength, 23),#到30
     (troop_raise_attribute, "trp_player", ca_agility, 23),#到30
     (troop_raise_attribute, "trp_player", ca_intelligence, 13),#到20
     (troop_raise_attribute, "trp_player", ca_charisma, 13),#到20

     (troop_raise_skill, "trp_player", skl_ironflesh, 9),
     (troop_raise_skill, "trp_player", skl_power_strike, 9),
     (troop_raise_skill, "trp_player", skl_power_throw, 9),
     (troop_raise_skill, "trp_player", skl_power_draw, 9),
     (troop_raise_skill, "trp_player", skl_weapon_master, 8),
     (troop_raise_skill, "trp_player", skl_shield, 7),
     (troop_raise_skill, "trp_player", skl_athletics, 7),
     (troop_raise_skill, "trp_player", skl_riding, 7),
     (troop_raise_skill, "trp_player", skl_horse_archery, 6),
     (troop_raise_skill, "trp_player", skl_inventory_management, 15),
     (troop_raise_skill, "trp_player", skl_persuasion, 9),
     (troop_raise_skill, "trp_player", skl_memory, 9),

     (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 250),
     (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 250),
     (troop_raise_proficiency, "trp_player", wpt_polearm, 250),
     (troop_raise_proficiency, "trp_player", wpt_archery, 250),
     (troop_raise_proficiency, "trp_player", wpt_crossbow, 250),
     (troop_raise_proficiency, "trp_player", wpt_throwing, 250),
     (troop_raise_proficiency, "trp_player", wpt_firearm, 250),

     (call_script, "script_player_set_new_inventory_slot", ek_item_2, "itm_graghite_steel_bolts"),
     (call_script, "script_player_set_new_inventory_slot", ek_item_3, "itm_fengniao_jian"),
     (call_script, "script_player_set_new_inventory_slot", ek_head, "itm_papal_chain_hood"),
     (call_script, "script_player_set_new_inventory_slot", ek_body, "itm_vacuum_oath_armor"),
     (call_script, "script_player_set_new_inventory_slot", ek_foot, "itm_dark_oath_shoe"),
     (call_script, "script_player_set_new_inventory_slot", ek_gloves, "itm_dark_oath_hand"),
     (call_script, "script_player_set_new_inventory_slot", ek_horse, "itm_unicorn"),

     (call_script, "script_player_set_new_inventory_slot", 10, "itm_asterisk_staff"),
     (call_script, "script_player_set_new_inventory_slot", 11, "itm_jinshi_qishijian"),
     (call_script, "script_player_set_new_inventory_slot", 12, "itm_jiqiao_nu"),

     (call_script, "script_player_set_new_inventory_slot", 13, "itm_steel_shield"),
     (call_script, "script_player_set_new_inventory_slot", 14, "itm_phoenix_splendid_bow"),
     (call_script, "script_player_set_new_inventory_slot", 15, "itm_throwing_daggers"),

     (store_add, ":skill_begin", "itm_active_skills_begin", 1),
     (try_for_range, ":count_no", ":skill_begin", "itm_active_skills_end"),
        (call_script, "script_set_troop_active_skill_level", "trp_player", ":count_no"),#解锁全部主动技能
     (try_end),
     (store_add, ":skill_begin", "itm_passive_skills_begin", 1),
     (try_for_range, ":count_no", ":skill_begin", "itm_passive_skills_end"),
        (item_get_abundance, ":level_no", ":count_no"),
        (call_script, "script_set_troop_passive_skill_level", "trp_player", ":count_no", ":level_no"),#解锁全部被动技能
     (try_end),

           (assign, "$boss_num", -1),
           (jump_to_menu, "mnu_custom_battle_formidable_enemy"),
           (presentation_set_duration, 0),

        (else_try),
           (eq, ":object", "$g_presentation_obj_4"), #会战模式
           (jump_to_menu, "mnu_custom_battle_campaign"),
           (presentation_set_duration, 0),

        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),#快速战斗
           (presentation_set_duration, 0),
           (start_presentation, "prsnt_game_custom_battle_designer_old"),
        (try_end),
       ]),
  ]),


#开局选择人物
  ("character_choose_window",0,mesh_undead_production_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),

        (create_button_overlay, "$g_presentation_obj_1", "@复 苏 ", tf_center_justify),
        (position_set_x, pos1, 885),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (call_script, "script_characer_choose_card", 1, 37),#下级骑士
        (assign, "$g_presentation_obj_2", reg1),
        (call_script, "script_characer_choose_card", 2, 172),#军士
        (assign, "$g_presentation_obj_3", reg1),
        (call_script, "script_characer_choose_card", 3, 308),#侍女
        (assign, "$g_presentation_obj_4", reg1),
        (call_script, "script_characer_choose_card", 4, 444),#密探
        (assign, "$g_presentation_obj_5", reg1),
        (call_script, "script_characer_choose_card", 5, 580),#水手
        (assign, "$g_presentation_obj_6", reg1),
        (call_script, "script_characer_choose_card", 6, 703),#术士
        (assign, "$g_presentation_obj_7", reg1),

        (create_image_button_overlay, "$g_presentation_obj_8", "mesh_character_choose_window", "mesh_character_choose_window_lighten"),  #公主
        (position_set_x, pos1, 839),
        (position_set_y, pos1, 160),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (position_set_x, pos1, 238),
        (position_set_y, pos1, 1350),
        (overlay_set_size, "$g_presentation_obj_8", pos1),
        (overlay_set_additional_render_height, "$g_presentation_obj_8", -1),

        (create_text_overlay, reg1, "@ 困 难 模 式 ", tf_scrollable),
        (position_set_x, pos1, 851),
        (position_set_y, pos1, 135),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 115),
        (position_set_y, pos1, 440),
        (overlay_set_area_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFF0000),
        (set_container_overlay, reg1),

        (set_container_overlay, -1),

        (try_begin),
           (gt, "$character_choose", 0),
           (str_store_troop_name_plural, s1, "$character_choose"),
           (create_text_overlay, reg1, s1, tf_scrollable),#介绍
           (position_set_x, pos1, 200),
           (position_set_y, pos1, 50),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 1100),
           (position_set_y, pos1, 1100),
           (overlay_set_size, reg1, pos1),
           (position_set_x, pos1, 600),
           (position_set_y, pos1, 100),
           (overlay_set_area_size, reg1, pos1),
           (try_begin),
              (eq, "$character_choose", "trp_quick_battle_troop_7"),
              (overlay_set_color, reg1, 0xFF0000),
              (overlay_set_color, "$g_presentation_obj_1", 0xFF0000),
              (create_mesh_overlay, reg1, "mesh_background_demon"),
#              (overlay_set_additional_render_height, reg1, -1),
           (else_try),
              (overlay_set_color, reg1, 0xFFFFFF),
           (try_end),
        (try_end),

        (presentation_set_duration, 999999),
       ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),#选择完毕，载入玩家数据
           (try_for_range, ":count", 0, 4),
              (store_add, ":attribute_no", ":count", ca_strength),
              (store_attribute_level, ":level_no_1", "$character_choose", ":attribute_no"),#属性
              (store_attribute_level, ":level_no_2", "trp_player", ":attribute_no"),
              (val_sub, ":level_no_1", ":level_no_2"),
              (troop_raise_attribute, "trp_player", ":attribute_no", ":level_no_1"),
           (try_end),
           (try_for_range, ":count", 0, 42),
              (store_sub, ":skill_no", skl_reserved_18, ":count"),
              (store_skill_level, ":level_no_1", ":skill_no", "$character_choose"),#技能
              (store_skill_level, ":level_no_2", ":skill_no", "trp_player"),
              (val_sub, ":level_no_1", ":level_no_2"),
              (troop_raise_skill, "trp_player", ":skill_no", ":level_no_1"),
           (try_end),
           (try_for_range, ":count", 0, 7),
              (store_add, ":weapon_no", wpt_one_handed_weapon, ":count"),
              (store_proficiency_level, ":level_no_1", "$character_choose", ":weapon_no"),#熟练
              (store_proficiency_level, ":level_no_2", "trp_player", ":weapon_no"),
              (val_sub, ":level_no_1", ":level_no_2"),
              (troop_raise_proficiency, "trp_player", ":weapon_no", ":level_no_1"),
           (try_end),

           (presentation_set_duration, 0),
           (try_begin),
              (this_or_next|eq, "$character_choose", "trp_quick_battle_troop_1"),#骑士和公主可以选择旗帜
              (eq, "$character_choose", "trp_quick_battle_troop_7"),
#normal_banner_begin
              (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#            (start_presentation, "prsnt_custom_banner"),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"),#下级骑士
           (assign, "$character_choose", "trp_quick_battle_troop_1"),
           (start_presentation, "prsnt_character_choose_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),#军士
           (assign, "$character_choose", "trp_quick_battle_troop_2"),
           (start_presentation, "prsnt_character_choose_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_4"),#侍女
           (assign, "$character_choose", "trp_quick_battle_troop_3"),
           (start_presentation, "prsnt_character_choose_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_5"),#密探
           (assign, "$character_choose", "trp_quick_battle_troop_4"),
           (start_presentation, "prsnt_character_choose_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_6"),#水手
           (assign, "$character_choose", "trp_quick_battle_troop_5"),
           (start_presentation, "prsnt_character_choose_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_7"),#术士
           (assign, "$character_choose", "trp_quick_battle_troop_6"),
           (start_presentation, "prsnt_character_choose_window"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_8"),#公主
           (assign, "$character_choose", "trp_quick_battle_troop_7"),
           (start_presentation, "prsnt_character_choose_window"),
        (try_end),
       ]),
  ]),


#快速战斗-会战战前选择
  ("custom_battle_campaign",0, mesh_black_panel_nontransparent,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
        (try_for_range, ":count_no", 0, 2000),#清空数据
           (troop_set_slot, "trp_temp_array_a", ":count_no", -1), #存slot
        (try_end),

##————————————————————————————————核心部分——————————————————————————————
        (create_mesh_overlay, reg1, "mesh_character_arch"),
        (position_set_x, pos1, 364),
        (position_set_y, pos1, 5),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 600),
        (overlay_set_size, reg1, pos1),

        (create_button_overlay, "$g_presentation_obj_1", "@离 开 ", tf_center_justify),
        (position_set_x, pos1, 554),
        (position_set_y, pos1, 20),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),

        (create_button_overlay, "$g_presentation_obj_3", "@重 设 "),
        (position_set_x, pos1, 420),
        (position_set_y, pos1, 20),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFF),

        (create_text_overlay, reg1, "@说 明 ", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_text_overlay, "$g_presentation_text_1", "str_campaign_brief", tf_scrollable),
        (position_set_x, pos1, 340),
        (position_set_y, pos1, 560),
        (overlay_set_position, "$g_presentation_text_1", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_1", pos1),
        (position_set_x, pos1, 320),
        (position_set_y, pos1, 130),
        (overlay_set_area_size, "$g_presentation_text_1", pos1),
        (overlay_set_color, "$g_presentation_text_1", 0xFFFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 340),
        (position_set_y, pos1, 555),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 16000),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, "$g_presentation_text_4", "@ ", tf_scrollable),
        (position_set_x, pos1, 340),
        (position_set_y, pos1, 360),
        (overlay_set_position, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_presentation_text_4", pos1),
        (position_set_x, pos1, 320),
        (position_set_y, pos1, 180),
        (overlay_set_area_size, "$g_presentation_text_4", pos1),
        (overlay_set_color, "$g_presentation_text_4", 0xFFFFFFFF),

##————————————————————————————————友方部分——————————————————————————————
        (create_text_overlay, reg1, "@己 方 ", tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 1500),
        (position_set_y, pos1, 1500),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 175),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg1, pos1),

        (create_combo_label_overlay, "$g_presentation_obj_label_1"), #进场方式选择
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_label_1", pos1),
        (position_set_x, pos1, 175),
        (position_set_y, pos1, 665),
        (overlay_set_position, "$g_presentation_obj_label_1", pos1),
        (try_for_range, ":cur_mode", "str_encounter_mode_1", "str_encounter_mode_1_brief"),
           (str_store_string, s1, ":cur_mode"),
           (overlay_add_item, "$g_presentation_obj_label_1", s1),
        (try_end),
        (overlay_set_val, "$g_presentation_obj_label_1", "$g_quick_battle_encounter_mode_player"),

        (create_text_overlay, "$g_presentation_text_2", "@部 队 数 : 1 "),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_text_2", pos1),
        (position_set_x, pos1, 60),
        (position_set_y, pos1, 635),
        (overlay_set_position, "$g_presentation_text_2", pos1),
        (overlay_set_color, "$g_presentation_text_2", 0xFFFFFFFF),

        (create_image_button_overlay, "$g_presentation_obj_4", "mesh_small_arrow_up", "mesh_small_arrow_up_clicked"), #增加
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 170),
        (overlay_set_size, "$g_presentation_obj_4", pos1),
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 639),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_display, "$g_presentation_obj_4", 0), 
        (create_image_button_overlay, "$g_presentation_obj_5", "mesh_small_arrow_down", "mesh_small_arrow_down_clicked"), #减少
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 170),
        (overlay_set_size, "$g_presentation_obj_5", pos1),
        (position_set_x, pos1, 185),
        (position_set_y, pos1, 639),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_display, "$g_presentation_obj_5", 0), 

        (create_button_overlay, "$g_presentation_obj_6", "@确 定 选 择 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 635),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_color, "$g_presentation_obj_6", 0xFFFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 625),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 12500),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, reg1, "@已 选 部 队               进 场 轮 次 "),
        (position_set_x, pos1, 900), 
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 60),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_mesh_overlay, reg1, "mesh_campaign_detachment_window"),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 425),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 300),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, reg1, "@基 础 模 板 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 35),
        (position_set_y, pos1, 390),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_3"), #选择基础部队模板的派系
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_label_3", pos1),
        (position_set_x, pos1, 245),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_obj_label_3", pos1),
        (try_for_range, ":cur_faction", "itm_faction_begin", "itm_faction_end"),
           (assign, ":value_no", 0),
           (try_for_range, ":count_no", 1, 4),
              (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
              (val_add, ":value_no", reg2),
           (try_end),
           (eq, ":value_no", 100), #总和100才是提供基础模板的派系
           (str_store_item_name, s1, ":cur_faction"),
           (overlay_add_item, "$g_presentation_obj_label_3", s1),
           (eq, "$g_quick_battle_encounter_player_basic_template", 0), 
           (assign, "$g_quick_battle_encounter_player_basic_template", ":cur_faction"), #记录第一个（即第0号label对应的那个）
        (try_end),
        (overlay_set_val, "$g_presentation_obj_label_3", 0),

        (create_text_overlay, reg1, "@特 殊 模 板 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 35),
        (position_set_y, pos1, 345),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_4"), #选择特殊部队模板的派系
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_label_4", pos1),
        (position_set_x, pos1, 245),
        (position_set_y, pos1, 340),
        (overlay_set_position, "$g_presentation_obj_label_4", pos1),
        (try_for_range, ":cur_faction", "itm_faction_begin", "itm_faction_end"),
           (eq, ":cur_faction", "itm_faction_begin"),
           (overlay_add_item, "$g_presentation_obj_label_4", "@无 "),
        (else_try),
           (assign, ":value_no", 0),
           (try_for_range, ":count_no", 1, 4),
              (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
              (val_add, ":value_no", reg2),
           (try_end),
           (is_between, ":value_no", 1, 100), #多于1但是少于100
           (str_store_item_name, s1, ":cur_faction"),
           (overlay_add_item, "$g_presentation_obj_label_4", s1),
           (eq, "$g_quick_battle_encounter_player_special_template", 0), 
        (try_end),
        (overlay_set_val, "$g_presentation_obj_label_4", 0),

        (create_text_overlay, reg1, "@预 估 规 模 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 35),
        (position_set_y, pos1, 300),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_slider_overlay, "$g_presentation_obj_slider_1", 1000, 80000),
        (overlay_set_val, "$g_presentation_obj_slider_1", 8000),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_slider_1", pos1),
        (position_set_x, pos1, 210),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_slider_1", pos1),
        (assign, "$g_quick_battle_encounter_player_party_num", 8000),

        (create_text_overlay, "$g_presentation_text_5", "@8000 "),
        (position_set_x, pos1, 700), 
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_5", pos1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 304),
        (overlay_set_position, "$g_presentation_text_5", pos1),
        (overlay_set_color, "$g_presentation_text_5", 0xFFFFFFFF),

        (create_text_overlay, reg1, "@_", tf_scrollable), 
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 15),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 275),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":cur_y", 3),
        (try_for_range_backwards, ":troop_no", total_npcs_begin, total_npcs_end),
           (troop_slot_eq, ":troop_no", 1, 0), #未使用的npc
           (str_store_troop_name, s1, ":troop_no"),
           (create_button_overlay, reg1, s1),
           (position_set_x, pos1, 5),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (val_add, ":cur_y", 15),
        (try_end),
        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_7", "@ ", tf_scrollable),
        (position_set_x, pos1, 230),
        (position_set_y, pos1, 70),
        (overlay_set_position, "$g_presentation_text_7", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_7", pos1),
        (position_set_x, pos1, 80),
        (position_set_y, pos1, 220),
        (overlay_set_area_size, "$g_presentation_text_7", pos1),
        (overlay_set_color, "$g_presentation_text_7", 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_10"), #选择阵型
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 670),
        (overlay_set_size, "$g_presentation_obj_label_10", pos1),
        (position_set_x, pos1, 340),
        (position_set_y, pos1, 60),
        (overlay_set_position, "$g_presentation_obj_label_10", pos1),
        (try_for_range, ":formation_no", "itm_formation_common", "itm_formation_end"),
           (str_store_item_name, s1, ":formation_no"),
           (overlay_add_item, "$g_presentation_obj_label_10", s1),
        (try_end),
        (overlay_add_item, "$g_presentation_obj_label_10", "@自 动 "), #使用与大地图相同的逻辑计算使用什么阵型
        (assign, "$g_quick_battle_encounter_player_formation", "itm_formation_end"),
        (store_sub, ":value_no", "itm_formation_end", "itm_formation_common"),
        (overlay_set_val, "$g_presentation_obj_label_10", ":value_no"),

        (str_store_string, s1, "@添 加 至 部 队 "),#添加兵种
        (call_script, "script_create_special_button_overlay", 295, 25),
        (assign, "$g_presentation_obj_10", reg1),

##————————————————————————————————敌方部分——————————————————————————————
        (create_text_overlay, reg1, "@敌 方 ",  tf_center_justify|tf_single_line|tf_with_outline),
        (overlay_set_color, reg1, 0xFFFFFFFF),
        (position_set_x, pos1, 1500),
        (position_set_y, pos1, 1500),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 820),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg1, pos1),

        (create_combo_label_overlay, "$g_presentation_obj_label_2"), #进场方式选择
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_label_2", pos1),
        (position_set_x, pos1, 825),
        (position_set_y, pos1, 665),
        (overlay_set_position, "$g_presentation_obj_label_2", pos1),
        (try_for_range, ":cur_mode", "str_encounter_mode_1", "str_encounter_mode_1_brief"),
           (str_store_string, s1, ":cur_mode"),
           (overlay_add_item, "$g_presentation_obj_label_2", s1),
        (try_end),
        (overlay_set_val, "$g_presentation_obj_label_2", "$g_quick_battle_encounter_mode_enemy"),

        (create_text_overlay, "$g_presentation_text_3", "@部 队 数 : 1 "),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_text_3", pos1),
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 635),
        (overlay_set_position, "$g_presentation_text_3", pos1),
        (overlay_set_color, "$g_presentation_text_3", 0xFFFFFFFF),

        (create_image_button_overlay, "$g_presentation_obj_7", "mesh_small_arrow_up", "mesh_small_arrow_up_clicked"), #增加
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 170),
        (overlay_set_size, "$g_presentation_obj_7", pos1),
        (position_set_x, pos1, 820),
        (position_set_y, pos1, 639),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_display, "$g_presentation_obj_7", 0), 
        (create_image_button_overlay, "$g_presentation_obj_8", "mesh_small_arrow_down", "mesh_small_arrow_down_clicked"), #减少
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 170),
        (overlay_set_size, "$g_presentation_obj_8", pos1),
        (position_set_x, pos1, 835),
        (position_set_y, pos1, 639),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_display, "$g_presentation_obj_8", 0), 

        (create_button_overlay, "$g_presentation_obj_9", "@确 定 选 择 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, "$g_presentation_obj_9", pos1),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 635),
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (overlay_set_color, "$g_presentation_obj_9", 0xFFFFFFFF),

        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 625),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 12500),
        (position_set_y, pos1, 50),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, reg1, "@已 选 部 队               进 场 轮 次 "),
        (position_set_x, pos1, 900), 
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_mesh_overlay, reg1, "mesh_campaign_detachment_window"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 425),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 300),
        (overlay_set_size, reg1, pos1),

        (create_text_overlay, reg1, "@基 础 模 板 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 685),
        (position_set_y, pos1, 390),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_5"), #选择基础部队模板的派系
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_label_5", pos1),
        (position_set_x, pos1, 895),
        (position_set_y, pos1, 385),
        (overlay_set_position, "$g_presentation_obj_label_5", pos1),
        (try_for_range, ":cur_faction", "itm_faction_begin", "itm_faction_end"),
           (assign, ":value_no", 0),
           (try_for_range, ":count_no", 1, 4),
              (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
              (val_add, ":value_no", reg2),
           (try_end),
           (eq, ":value_no", 100), #总和100才是提供基础模板的派系
           (str_store_item_name, s1, ":cur_faction"),
           (overlay_add_item, "$g_presentation_obj_label_5", s1),
           (eq, "$g_quick_battle_encounter_enemy_basic_template", 0), 
           (assign, "$g_quick_battle_encounter_enemy_basic_template", ":cur_faction"), #记录第一个（即第0号label对应的那个）
        (try_end),
        (overlay_set_val, "$g_presentation_obj_label_5", 0),

        (create_text_overlay, reg1, "@特 殊 模 板 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 685),
        (position_set_y, pos1, 345),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_6"), #选择特殊部队模板的派系
        (position_set_x, pos1, 650),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_label_6", pos1),
        (position_set_x, pos1, 895),
        (position_set_y, pos1, 340),
        (overlay_set_position, "$g_presentation_obj_label_6", pos1),
        (try_for_range, ":cur_faction", "itm_faction_begin", "itm_faction_end"),
           (eq, ":cur_faction", "itm_faction_begin"),
           (overlay_add_item, "$g_presentation_obj_label_6", "@无 "),
        (else_try),
           (assign, ":value_no", 0),
           (try_for_range, ":count_no", 1, 4),
              (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
              (val_add, ":value_no", reg2),
           (try_end),
           (is_between, ":value_no", 1, 100), #多于1但是少于100
           (str_store_item_name, s1, ":cur_faction"),
           (overlay_add_item, "$g_presentation_obj_label_6", s1),
           (eq, "$g_quick_battle_encounter_enemy_special_template", 0), 
        (try_end),
        (overlay_set_val, "$g_presentation_obj_label_6", 0),

        (create_text_overlay, reg1, "@预 估 规 模 "),
        (position_set_x, pos1, 1000), 
        (position_set_y, pos1, 1000),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 685),
        (position_set_y, pos1, 300),
        (overlay_set_position, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_slider_overlay, "$g_presentation_obj_slider_2", 1000, 80000),
        (overlay_set_val, "$g_presentation_obj_slider_2", 8000),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_slider_2", pos1),
        (position_set_x, pos1, 860),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_slider_2", pos1),

        (create_text_overlay, "$g_presentation_text_6", "@8000 "),
        (position_set_x, pos1, 700), 
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_6", pos1),
        (position_set_x, pos1, 950),
        (position_set_y, pos1, 304),
        (overlay_set_position, "$g_presentation_text_6", pos1),
        (overlay_set_color, "$g_presentation_text_6", 0xFFFFFFFF),
        (assign, "$g_quick_battle_encounter_enemy_party_num", 8000),

        (create_text_overlay, reg1, "@_", tf_scrollable), 
        (position_set_x, pos1, 660),
        (position_set_y, pos1, 15),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 275),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, ":cur_y", 3),
        (try_for_range_backwards, ":troop_no", total_npcs_begin, total_npcs_end),
           (troop_slot_eq, ":troop_no", 1, 0), #未使用的npc
           (str_store_troop_name, s1, ":troop_no"),
           (create_button_overlay, reg1, s1),
           (position_set_x, pos1, 5),
           (position_set_y, pos1, ":cur_y"),
           (overlay_set_position, reg1, pos1),
           (position_set_x, pos1, 800),
           (position_set_y, pos1, 800),
           (overlay_set_size, reg1, pos1),
           (overlay_set_color, reg1, 0xFFFFFF),
           (val_add, ":cur_y", 15),
        (try_end),
        (set_container_overlay, -1),

        (create_text_overlay, "$g_presentation_text_8", "@ ", tf_scrollable),
        (position_set_x, pos1, 880),
        (position_set_y, pos1, 70),
        (overlay_set_position, "$g_presentation_text_8", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_presentation_text_8", pos1),
        (position_set_x, pos1, 80),
        (position_set_y, pos1, 220),
        (overlay_set_area_size, "$g_presentation_text_8", pos1),
        (overlay_set_color, "$g_presentation_text_8", 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_11"), #选择阵型
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 670),
        (overlay_set_size, "$g_presentation_obj_label_11", pos1),
        (position_set_x, pos1, 990),
        (position_set_y, pos1, 60),
        (overlay_set_position, "$g_presentation_obj_label_11", pos1),
        (try_for_range, ":formation_no", "itm_formation_common", "itm_formation_end"),
           (str_store_item_name, s1, ":formation_no"),
           (overlay_add_item, "$g_presentation_obj_label_11", s1),
        (try_end),
        (overlay_add_item, "$g_presentation_obj_label_11", "@自 动 "), #使用与大地图相同的逻辑计算使用什么阵型
        (assign, "$g_quick_battle_encounter_enemy_formation", "itm_formation_end"),
        (store_sub, ":value_no", "itm_formation_end", "itm_formation_common"),
        (overlay_set_val, "$g_presentation_obj_label_11", ":value_no"),

        (str_store_string, s1, "@添 加 至 部 队 "),#添加兵种
        (call_script, "script_create_special_button_overlay", 945, 25),
        (assign, "$g_presentation_obj_11", reg1),

##————————————————————————————————场景部分——————————————————————————————
        (create_text_overlay, reg1, "@战 场 设 置 ", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 250),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 900),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_7"), #选择模式
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 670),
        (overlay_set_size, "$g_presentation_obj_label_7", pos1),
        (position_set_x, pos1, 545),
        (position_set_y, pos1, 210),
        (overlay_set_position, "$g_presentation_obj_label_7", pos1),
        (overlay_add_item, "$g_presentation_obj_label_7", "@野 战 "),
        (overlay_add_item, "$g_presentation_obj_label_7", "@攻 城 "),
        (overlay_add_item, "$g_presentation_obj_label_7", "@守 城 "),
        (overlay_add_item, "$g_presentation_obj_label_7", "@海 战 "),

        (create_button_overlay, "$g_presentation_obj_12", "@下 一 步 ", tf_center_justify),
        (position_set_x, pos1, 551),
        (position_set_y, pos1, 214),
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_12", pos1),
        (overlay_set_color, "$g_presentation_obj_12", 0xFFFFFFFF),

        (create_combo_label_overlay, "$g_presentation_obj_label_8"), #选择类型
        (position_set_x, pos1, 320),
        (position_set_y, pos1, 670),
        (overlay_set_size, "$g_presentation_obj_label_8", pos1),
        (position_set_x, pos1, 535),
        (position_set_y, pos1, 180),
        (overlay_set_position, "$g_presentation_obj_label_8", pos1),
        (overlay_set_display, "$g_presentation_obj_label_8", 0), 

        (create_button_overlay, "$g_presentation_obj_13", "@下 一 步 ", tf_center_justify),
        (position_set_x, pos1, 562),
        (position_set_y, pos1, 184),
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_13", pos1),
        (overlay_set_color, "$g_presentation_obj_13", 0xFFFFFFFF),
        (overlay_set_display, "$g_presentation_obj_13", 0), 

        (create_combo_label_overlay, "$g_presentation_obj_label_9"), #选择类型
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 670),
        (overlay_set_size, "$g_presentation_obj_label_9", pos1),
        (position_set_x, pos1, 535),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_label_9", pos1),
        (overlay_set_display, "$g_presentation_obj_label_9", 0), 

        (create_text_overlay, reg1, "@时 间 "),
        (position_set_x, pos1, 425),
        (position_set_y, pos1, 125),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0xFFFFFFFF),

        (create_slider_overlay, "$g_presentation_obj_slider_3", 0, 23), #战场设置1，时间
        (overlay_set_val, "$g_presentation_obj_slider_3", 10),
        (assign, "$g_quick_battle_encounter_map_set_1", 10),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_slider_3", pos1),
        (position_set_x, pos1, 510),
        (position_set_y, pos1, 125),
        (overlay_set_position, "$g_presentation_obj_slider_3", pos1),

        (create_text_overlay, "$g_presentation_text_9", "@10 "),
        (position_set_x, pos1, 555),
        (position_set_y, pos1, 125),
        (overlay_set_position, "$g_presentation_text_9", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$g_presentation_text_9", pos1),
        (overlay_set_color, "$g_presentation_text_9", 0xFFFFFFFF),

        (create_text_overlay, "$g_presentation_text_10", "@ "),
        (position_set_x, pos1, 425),
        (position_set_y, pos1, 105),
        (overlay_set_position, "$g_presentation_text_10", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$g_presentation_text_10", pos1),
        (overlay_set_color, "$g_presentation_text_10", 0xFFFFFFFF),

        (create_slider_overlay, "$g_presentation_obj_slider_4", 0, 20), #战场设置2，比如野战就是植被
        (overlay_set_val, "$g_presentation_obj_slider_4", 1),
        (assign, "$g_quick_battle_encounter_map_set_2", 1),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 600),
        (overlay_set_size, "$g_presentation_obj_slider_4", pos1),
        (position_set_x, pos1, 510),
        (position_set_y, pos1, 105),
        (overlay_set_position, "$g_presentation_obj_slider_4", pos1),
        (overlay_set_display, "$g_presentation_obj_slider_4", 0), 

        (create_text_overlay, "$g_presentation_text_11", "@ "),
        (position_set_x, pos1, 555),
        (position_set_y, pos1, 105),
        (overlay_set_position, "$g_presentation_text_11", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 750),
        (overlay_set_size, "$g_presentation_text_11", pos1),
        (overlay_set_color, "$g_presentation_text_11", 0xFFFFFFFF),


        (create_button_overlay, "$g_presentation_obj_2", "@开 始 ", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 20),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),

#            ####### mouse fix pos system #######
#       (call_script, "script_mouse_fix_pos_load"),
#            ####### mouse fix pos system ####### 

        (presentation_set_duration, 999999),
       ]),

#     (ti_on_presentation_run,
#      [
#           ####### mouse fix pos system #######
#       (call_script, "script_mouse_fix_pos_run"),
#           ####### mouse fix pos system #######
#       ]),

      (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":enter_leave"),
        (try_begin),
           (this_or_next|eq, ":object", "$g_presentation_obj_label_1"), #友方进场方式选择
           (eq, ":object", "$g_presentation_obj_label_2"), #敌方进场方式选择
           (try_begin),
              (eq, ":enter_leave", 0), #进入
              (try_begin),
                 (eq, ":object", "$g_presentation_obj_label_1"), 
                 (store_add, ":string_no", "$g_quick_battle_encounter_mode_player", "str_encounter_mode_1_brief"),
              (else_try),
                 (eq, ":object", "$g_presentation_obj_label_2"), 
                 (store_add, ":string_no", "$g_quick_battle_encounter_mode_enemy", "str_encounter_mode_1_brief"),
              (try_end),
              (str_store_string, s1, ":string_no"),
              (overlay_set_text, "$g_presentation_text_1", s1),
           (else_try),
              (eq, ":enter_leave", 1),
              (overlay_set_text, "$g_presentation_text_1", "str_campaign_brief"),
           (try_end),

        (else_try),
           (this_or_next|eq, ":object", "$g_presentation_obj_label_3"), #友方基础模板
           (this_or_next|eq, ":object", "$g_presentation_obj_label_5"), #敌方基础模板
           (this_or_next|eq, ":object", "$g_presentation_obj_label_4"), #友方特殊模板
           (eq, ":object", "$g_presentation_obj_label_6"), #敌方特殊模板
           (try_begin),
              (eq, ":enter_leave", 0), #进入
              (try_begin),
                 (eq, ":object", "$g_presentation_obj_label_3"), 
                 (assign, ":faction_no", "$g_quick_battle_encounter_player_basic_template"),
              (else_try),
                 (eq, ":object", "$g_presentation_obj_label_5"), 
                 (assign, ":faction_no", "$g_quick_battle_encounter_enemy_basic_template"),
              (else_try),
                 (eq, ":object", "$g_presentation_obj_label_4"), 
                 (assign, ":faction_no", "$g_quick_battle_encounter_player_special_template"),
              (else_try),
                 (eq, ":object", "$g_presentation_obj_label_6"), 
                 (assign, ":faction_no", "$g_quick_battle_encounter_enemy_special_template"),
              (try_end),
              (gt, ":faction_no", 0), #显示无的时候不生成
              (str_store_string, s1, "@提 供 的 部 队 模 板 ： "),
              (try_for_range, ":count_no", 1, 4),
                 (call_script, "script_cf_get_faction_template", ":faction_no", ":count_no"),
                 (val_sub, reg1, party_template_uesd_begin),
                 (val_add, reg1, party_template_name_begin),
                 (str_store_string, s2, reg1),
                 (str_store_string, s1, "@{s1}^{s2}（ {reg2}%） "),
              (try_end),
              (overlay_set_text, "$g_presentation_text_4", s1),
           (try_end),
        (try_end),
        ]),

      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (try_begin),
           (eq, ":object", "$g_presentation_obj_1"),#返回开始界面
           (assign, "$g_leave_encounter", 1),
           (presentation_set_duration, 0),
        (else_try),
           (eq, ":object", "$g_presentation_obj_3"),#重设
           (assign, "$g_leave_encounter", 0),
           (presentation_set_duration, 0),
        (else_try),
           (eq, ":object", "$g_presentation_obj_label_1"), #友方进场方式选择
           (try_begin),
              (neq, "$g_quick_battle_encounter_mode_player_confirmed", 1), #未确认生成部队之前
              (overlay_set_val, "$g_presentation_obj_label_1", ":value"),
              (assign, "$g_quick_battle_encounter_mode_player", ":value"),
              (val_min, ":value", 1), 
              (overlay_set_display, "$g_presentation_obj_4", ":value"), #单一部队模式不能选部队数量
              (overlay_set_display, "$g_presentation_obj_5", ":value"),
           (else_try), 
              (overlay_set_val, "$g_presentation_obj_label_1", "$g_quick_battle_encounter_mode_player"),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_label_2"), #敌方进场方式选择
           (try_begin),
              (neq, "$g_quick_battle_encounter_mode_enemy_confirmed", 1), #未确认生成部队之前
              (overlay_set_val, "$g_presentation_obj_label_2", ":value"),
              (assign, "$g_quick_battle_encounter_mode_enemy", ":value"),
              (val_min, ":value", 1), 
              (overlay_set_display, "$g_presentation_obj_7", ":value"), #单一部队模式不能选部队数量
              (overlay_set_display, "$g_presentation_obj_8", ":value"), 
           (else_try), 
              (overlay_set_val, "$g_presentation_obj_label_2", "$g_quick_battle_encounter_mode_enemy"),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_4"), #友方部队增
           (val_add, "$g_quick_battle_encounter_player_num", 1), 
           (val_min, "$g_quick_battle_encounter_player_num", 10), #最多10
           (assign, reg1, "$g_quick_battle_encounter_player_num"),
           (overlay_set_text, "$g_presentation_text_2", "@部 队 数 : {reg1} "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_5"), #友方部队减
           (val_sub, "$g_quick_battle_encounter_player_num", 1), 
           (val_max, "$g_quick_battle_encounter_player_num", 1), #最少1
           (assign, reg1, "$g_quick_battle_encounter_player_num"),
           (overlay_set_text, "$g_presentation_text_2", "@部 队 数 : {reg1} "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_7"), #敌方部队增
           (val_add, "$g_quick_battle_encounter_enemy_num", 1), 
           (val_min, "$g_quick_battle_encounter_enemy_num", 10), #最多10
           (assign, reg1, "$g_quick_battle_encounter_enemy_num"),
           (overlay_set_text, "$g_presentation_text_3", "@部 队 数 : {reg1} "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_8"), #敌方部队减
           (val_sub, "$g_quick_battle_encounter_enemy_num", 1), 
           (val_max, "$g_quick_battle_encounter_enemy_num", 1), #最少1
           (assign, reg1, "$g_quick_battle_encounter_enemy_num"),
           (overlay_set_text, "$g_presentation_text_3", "@部 队 数 : {reg1} "),

##————————————————————————————————刷出部队——————————————————————————————
        (else_try),
           (eq, ":object", "$g_presentation_obj_6"), #友方部队确认选择
           (try_begin),
              (eq, "$g_quick_battle_encounter_mode_player", 0),
              (neq, "$g_quick_battle_encounter_player_num", 1),
              (display_message, "@请 检 查 部 队 模 式 和 部 队 数 量 的 设 置 。 ", 0xFF0000),
           (else_try),
              (assign, "$g_quick_battle_encounter_mode_player_confirmed", 1), #确定选择，无法再更改进场模式
              (overlay_set_display, "$g_presentation_obj_4", 0), 
              (overlay_set_display, "$g_presentation_obj_5", 0), 
              (overlay_set_display, "$g_presentation_obj_6", 0), 
              (create_text_overlay, reg1, "@_", tf_scrollable), 
              (position_set_x, pos1, 59),
              (position_set_y, pos1, 435),
              (overlay_set_position, reg1, pos1),
              (position_set_x, pos1, 220),
              (position_set_y, pos1, 155),
              (overlay_set_area_size, reg1, pos1),
              (set_container_overlay, reg1),

              (store_mul, ":cur_y", "$g_quick_battle_encounter_player_num", 15),
              (val_sub, ":cur_y", 10),
              (try_for_range, ":slot_no", 0, "$g_quick_battle_encounter_player_num"), #寻找对应数量的工具人party
                 (assign, ":party_no", "$g_quick_battle_party_used"),
                 (disable_party, ":party_no"), 
                 (party_clear, ":party_no"), 
                 (store_add, reg4, ":slot_no", 1),
                 (party_set_name, ":party_no", "@{reg4}军 "), #预设名字
                 (party_set_slot, ":party_no", slot_tool_party_team, 1), #1为友方
                 (party_set_slot, ":party_no", slot_tool_party_enter, 1), #进场轮次
                 (try_begin),
                    (eq, ":slot_no", 0), #友军第一位，加入玩家
                    (party_force_add_members, ":party_no", "trp_player", 1), #添加玩家进部队
                    (party_set_name, ":party_no", "@玩 家 部 队 "), #预设名字
                 (try_end),

                 (str_store_party_name, s1, ":party_no"),
                 (store_mul, ":value_no", ":party_no", 10), #数位储存
                 (create_button_overlay, reg1, s1),
                 (position_set_x, pos1, 5),
                 (position_set_y, pos1, ":cur_y"),
                 (overlay_set_position, reg1, pos1),
                 (position_set_x, pos1, 800),
                 (position_set_y, pos1, 800),
                 (overlay_set_size, reg1, pos1),
                 (overlay_set_color, reg1, 0xFFFFFF),
                 (val_add, ":value_no", 1),
                 (troop_set_slot, "trp_temp_array_a", reg1, ":value_no"), #记录slot以待使用

                 (store_add, ":cur_y_2", ":cur_y", 4), 
                 (create_image_button_overlay, reg1, "mesh_small_arrow_up", "mesh_small_arrow_up_clicked"), #增加
                 (position_set_x, pos1, 130),
                 (position_set_y, pos1, 130),
                 (overlay_set_size, reg1, pos1),
                 (position_set_x, pos1, 170),
                 (position_set_y, pos1, ":cur_y_2"),
                 (overlay_set_position, reg1, pos1),
                 (val_add, ":value_no", 1),
                 (troop_set_slot, "trp_temp_array_a", reg1, ":value_no"), #记录slot以待使用
                 (try_begin),
                    (this_or_next|eq, "$g_quick_battle_encounter_mode_player", 0), #单一部队
                    (eq, "$g_quick_battle_encounter_mode_player", 1), #分别进场
                    (overlay_set_display, reg1, 0), 
                 (try_end),

                 (create_text_overlay, reg1, "@1 ", tf_center_justify),
                 (position_set_x, pos1, 200),
                 (position_set_y, pos1, ":cur_y"),
                 (overlay_set_position, reg1, pos1),
                 (position_set_x, pos1, 800),
                 (position_set_y, pos1, 800),
                 (overlay_set_size, reg1, pos1),
                 (overlay_set_color, reg1, 0xFFFFFF),

                 (create_image_button_overlay, reg1, "mesh_small_arrow_down", "mesh_small_arrow_down_clicked"), #减少
                 (position_set_x, pos1, 130),
                 (position_set_y, pos1, 130),
                 (overlay_set_size, reg1, pos1),
                 (position_set_x, pos1, 210),
                 (position_set_y, pos1, ":cur_y_2"),
                 (overlay_set_position, reg1, pos1),
                 (val_add, ":value_no", 2),
                 (troop_set_slot, "trp_temp_array_a", reg1, ":value_no"), #记录slot以待使用
                 (try_begin),
                    (this_or_next|eq, "$g_quick_battle_encounter_mode_player", 0), #单一部队
                    (eq, "$g_quick_battle_encounter_mode_player", 1), #分别进场
                    (overlay_set_display, reg1, 0), 
                 (try_end),

                 (val_sub, ":cur_y", 15),
                 (val_add, "$g_quick_battle_party_used", 1),
              (try_end),
              (set_container_overlay, -1),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_9"), #敌方部队确认选择
           (try_begin),
              (eq, "$g_quick_battle_encounter_mode_enemy", 0),
              (neq, "$g_quick_battle_encounter_enemy_num", 1),
              (display_message, "@请 检 查 部 队 模 式 和 部 队 数 量 的 设 置 。 ", 0xFF0000),
           (else_try),
              (assign, "$g_quick_battle_encounter_mode_enemy_confirmed", 1), #确定选择，无法再更改进场模式
              (overlay_set_display, "$g_presentation_obj_7", 0), 
              (overlay_set_display, "$g_presentation_obj_8", 0), 
              (overlay_set_display, "$g_presentation_obj_9", 0), 
              (create_text_overlay, reg1, "@_", tf_scrollable), 
              (position_set_x, pos1, 709),
              (position_set_y, pos1, 435),
              (overlay_set_position, reg1, pos1),
              (position_set_x, pos1, 220),
              (position_set_y, pos1, 155),
              (overlay_set_area_size, reg1, pos1),
              (set_container_overlay, reg1),

              (store_mul, ":cur_y", "$g_quick_battle_encounter_enemy_num", 15),
              (val_sub, ":cur_y", 10),
              (try_for_range, ":slot_no", 0, "$g_quick_battle_encounter_enemy_num"), #寻找对应数量的工具人party
                 (assign, ":party_no", "$g_quick_battle_party_used"),
                 (disable_party, ":party_no"), 
                 (party_clear, ":party_no"), 
                 (store_add, reg4, ":slot_no", 1),
                 (party_set_name, ":party_no", "@{reg4}军 "), #预设名字
                 (party_set_slot, ":party_no", slot_tool_party_team, 2), #2为敌方
                 (party_set_slot, ":party_no", slot_tool_party_enter, 1), #进场轮次

                 (store_mul, ":value_no", ":party_no", 10), #数位储存
                 (create_button_overlay, reg1, "@{reg4}军 "),
                 (position_set_x, pos1, 5),
                 (position_set_y, pos1, ":cur_y"),
                 (overlay_set_position, reg1, pos1),
                 (position_set_x, pos1, 800),
                 (position_set_y, pos1, 800),
                 (overlay_set_size, reg1, pos1),
                 (overlay_set_color, reg1, 0xFFFFFF),
                 (val_add, ":value_no", 1),
                 (troop_set_slot, "trp_temp_array_a", reg1, ":value_no"), #记录slot以待使用

                 (store_add, ":cur_y_2", ":cur_y", 4), 
                 (create_image_button_overlay, reg1, "mesh_small_arrow_up", "mesh_small_arrow_up_clicked"), #增加
                 (position_set_x, pos1, 130),
                 (position_set_y, pos1, 130),
                 (overlay_set_size, reg1, pos1),
                 (position_set_x, pos1, 170),
                 (position_set_y, pos1, ":cur_y_2"),
                 (overlay_set_position, reg1, pos1),
                 (val_add, ":value_no", 1),
                 (troop_set_slot, "trp_temp_array_a", reg1, ":value_no"), #记录slot以待使用
                 (try_begin),
                    (this_or_next|eq, "$g_quick_battle_encounter_mode_enemy", 0), #单一部队
                    (eq, "$g_quick_battle_encounter_mode_enemy", 1), #分别进场
                    (overlay_set_display, reg1, 0), 
                 (try_end),

                 (create_text_overlay, reg1, "@1 ", tf_center_justify),
                 (position_set_x, pos1, 200),
                 (position_set_y, pos1, ":cur_y"),
                 (overlay_set_position, reg1, pos1),
                 (position_set_x, pos1, 800),
                 (position_set_y, pos1, 800),
                 (overlay_set_size, reg1, pos1),
                 (overlay_set_color, reg1, 0xFFFFFF),

                 (create_image_button_overlay, reg1, "mesh_small_arrow_down", "mesh_small_arrow_down_clicked"), #减少
                 (position_set_x, pos1, 130),
                 (position_set_y, pos1, 130),
                 (overlay_set_size, reg1, pos1),
                 (position_set_x, pos1, 210),
                 (position_set_y, pos1, ":cur_y_2"),
                 (overlay_set_position, reg1, pos1),
                 (val_add, ":value_no", 2),
                 (troop_set_slot, "trp_temp_array_a", reg1, ":value_no"), #记录slot以待使用
                 (try_begin),
                    (this_or_next|eq, "$g_quick_battle_encounter_mode_enemy", 0), #单一部队
                    (eq, "$g_quick_battle_encounter_mode_enemy", 1), #分别进场
                    (overlay_set_display, reg1, 0), 
                 (try_end),

                 (val_sub, ":cur_y", 15),
                 (val_add, "$g_quick_battle_party_used", 1),
              (try_end),
              (set_container_overlay, -1),
           (try_end),

##————————————————————————————————刷出部队后设置——————————————————————————————
        (else_try),
           (gt, ":object", "$g_presentation_obj_2"), #后刷的按钮
           (troop_get_slot, ":value_no", "trp_temp_array_a", ":object"), 
           (gt, ":value_no", 0),
           (store_div, ":party_no", ":value_no", 10),
           (val_mod, ":value_no", 10),
           (try_begin),
              (eq, ":value_no", 1), #选中部队进行设置
              (party_get_slot, ":count_no", ":party_no", slot_tool_party_team), 
              (try_begin), 
                 (eq, ":count_no", 1), #友方
                 (try_begin), 
                    (gt, "$g_quick_battle_encounter_player_set", 0), #已选别的
                    (store_sub, ":object_2", "$g_quick_battle_encounter_player_set", ":party_no"),
                    (val_mul, ":object_2", 4),
                    (val_add, ":object_2", ":object"),
                    (overlay_set_color, ":object_2", 0xFFFFFF),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_player_set", ":party_no"),
                 (overlay_set_color, ":object", 0x00FF00),
              (else_try),
                 (eq, ":count_no", 2), #敌方
                 (try_begin), 
                    (gt, "$g_quick_battle_encounter_enemy_set", 0), #已选别的
                    (store_sub, ":object_2", "$g_quick_battle_encounter_enemy_set", ":party_no"),
                    (val_mul, ":object_2", 4),
                    (val_add, ":object_2", ":object"),
                    (overlay_set_color, ":object_2", 0xFFFFFF),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_enemy_set", ":party_no"),
                 (overlay_set_color, ":object", 0x00FF00),
              (try_end),
           (else_try),
              (eq, ":value_no", 2), #进场轮次增
              (party_get_slot, ":count_no", ":party_no", slot_tool_party_enter), 
              (val_add, ":count_no", 1),
              (val_min, ":count_no", 999), #最大不超过999
              (party_set_slot, ":party_no", slot_tool_party_enter, ":count_no"), 
              (assign, reg1, ":count_no"),
              (val_add, ":object", 1),
              (overlay_set_text, ":object", "@{reg1} "),
           (else_try),
              (eq, ":value_no", 4), #进场轮次减
              (party_get_slot, ":count_no", ":party_no", slot_tool_party_enter), 
              (val_sub, ":count_no", 1),
              (val_max, ":count_no", 1), #最小不超过1
              (party_set_slot, ":party_no", slot_tool_party_enter, ":count_no"), 
              (assign, reg1, ":count_no"),
              (val_sub, ":object", 1),
              (overlay_set_text, ":object", "@{reg1} "),
           (try_end),

           (party_get_num_companion_stacks, ":num_stacks", ":party_no"), #展示部队人员
           (try_begin),
              (lt, ":num_stacks", 1),
              (str_store_string, s1, "@    无 成 员 ， 请 在 下 方 选 项 设 置 。 ^    基 础 模 板 类 似 文 化 提 供 的 基 础 模 板 ， 特 殊 模 板 会 以 一 定 概 率 替 换 基 础 模 板 加 入 。 最 下 方 可 选 择 多 个 npc加 入 此 部 队 ， 点 击 即 会 高 亮 ， 进 入 预 选 状 态 。 ^    选 择 完 毕 后 ， 点 击 “ 添 加 部 队 ” ， 即 可 按 设 定 的 数 量 和 模 板 为 选 中 部 队 提 供 成 员 。 "),
           (else_try),
              (str_store_string, s1, "@部 队 成 员 ： "),
              (try_for_range, ":i_stack", 0, ":num_stacks"),
                 (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
                 (str_store_troop_name, s3, ":stack_troop"),
                 (try_begin),
                    (troop_is_hero, ":stack_troop"),
                    (store_troop_health, reg3, ":stack_troop"),
                    (str_store_string, s2, "@{s3}_({reg3}%) "),
                 (else_try),
                    (party_stack_get_size, reg3, ":party_no", ":i_stack"),
                    (party_stack_get_num_wounded, reg4, ":party_no", ":i_stack"),
                    (store_sub, reg4, reg3, reg4),
                    (str_store_string, s2, "@{s3}_({reg4}/{reg3}) "),
                 (try_end),
                 (str_store_string, s1, "@{s1}^{s2}"),
              (try_end),
           (try_end),
           (overlay_set_text, "$g_presentation_text_4", "@{s1}^^"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_label_3"), #选择友方基础部队模板
           (assign, ":count_num", 0),
           (assign, ":limit_count", "itm_faction_end"),
           (try_for_range, ":cur_faction", "itm_faction_begin", ":limit_count"),
              (assign, ":value_no", 0),
              (try_for_range, ":count_no", 1, 4),
                 (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
                 (val_add, ":value_no", reg2),
              (try_end),
              (eq, ":value_no", 100), #总和100才是提供基础模板的派系
              (try_begin),
                 (eq, ":count_num", ":value"), #寻找当前条目对应的派系
                 (assign, ":limit_count", 0), #结束
              (else_try),
                 (val_add, ":count_num", 1),
              (try_end),
           (try_end),
           (assign, "$g_quick_battle_encounter_player_basic_template", ":cur_faction"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_label_4"), #选择友方特殊部队模板
           (assign, ":count_num", 0),
           (assign, ":limit_count", "itm_faction_end"),
           (try_for_range, ":cur_faction", "itm_faction_begin", ":limit_count"),
              (eq, ":cur_faction", "itm_faction_begin"),
              (try_begin),
                 (eq, ":count_num", ":value"), #寻找当前条目对应的派系
                 (assign, "$g_quick_battle_encounter_player_special_template", 0), #第一个条目是无
                 (assign, ":limit_count", 0), #结束
              (else_try),
                 (val_add, ":count_num", 1),
              (try_end),
           (else_try),
              (assign, ":value_no", 0),
              (try_for_range, ":count_no", 1, 4),
                 (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
                 (val_add, ":value_no", reg2),
              (try_end),
              (is_between, ":value_no", 1, 100), #多于1但是少于100
              (try_begin),
                 (eq, ":count_num", ":value"), #寻找当前条目对应的派系
                 (assign, "$g_quick_battle_encounter_player_special_template", ":cur_faction"),
                 (assign, ":limit_count", 0), #结束
              (else_try),
                 (val_add, ":count_num", 1),
              (try_end),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_label_5"), #选择敌方基础部队模板
           (assign, ":count_num", 0),
           (assign, ":limit_count", "itm_faction_end"),
           (try_for_range, ":cur_faction", "itm_faction_begin", ":limit_count"),
              (assign, ":value_no", 0),
              (try_for_range, ":count_no", 1, 4),
                 (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
                 (val_add, ":value_no", reg2),
              (try_end),
              (eq, ":value_no", 100), #总和100才是提供基础模板的派系
              (try_begin),
                 (eq, ":count_num", ":value"), #寻找当前条目对应的派系
                 (assign, ":limit_count", 0), #结束
              (else_try),
                 (val_add, ":count_num", 1),
              (try_end),
           (try_end),
           (assign, "$g_quick_battle_encounter_enemy_basic_template", ":cur_faction"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_label_6"), #选择敌方特殊部队模板
           (assign, ":count_num", 0),
           (assign, ":limit_count", "itm_faction_end"),
           (try_for_range, ":cur_faction", "itm_faction_begin", ":limit_count"),
              (eq, ":cur_faction", "itm_faction_begin"),
              (try_begin),
                 (eq, ":count_num", ":value"), #寻找当前条目对应的派系
                 (assign, "$g_quick_battle_encounter_enemy_special_template", 0), #第一个条目是无
                 (assign, ":limit_count", 0), #结束
              (else_try),
                 (val_add, ":count_num", 1),
              (try_end),
           (else_try),
              (assign, ":value_no", 0),
              (try_for_range, ":count_no", 1, 4),
                 (call_script, "script_cf_get_faction_template", ":cur_faction", ":count_no"),
                 (val_add, ":value_no", reg2),
              (try_end),
              (is_between, ":value_no", 1, 100), #多于1但是少于100
              (try_begin),
                 (eq, ":count_num", ":value"), #寻找当前条目对应的派系
                 (assign, "$g_quick_battle_encounter_enemy_special_template", ":cur_faction"),
                 (assign, ":limit_count", 0), #结束
              (else_try),
                 (val_add, ":count_num", 1),
              (try_end),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_slider_1"), #友方预估人数
           (assign, "$g_quick_battle_encounter_player_party_num", ":value"),
           (assign, reg1, "$g_quick_battle_encounter_player_party_num"),
           (overlay_set_text, "$g_presentation_text_5", "@{reg1} "),
        (else_try),
           (eq, ":object", "$g_presentation_obj_slider_2"), #敌方预估人数
           (assign, "$g_quick_battle_encounter_enemy_party_num", ":value"),
           (assign, reg1, "$g_quick_battle_encounter_enemy_party_num"),
           (overlay_set_text, "$g_presentation_text_6", "@{reg1} "),

        (else_try),
           (is_between, ":object", "$g_presentation_text_5", "$g_presentation_text_7"), #友军npc选择
           (store_sub, ":troop_no", "$g_presentation_text_7", ":object"), #是反向生成的
           (val_sub, ":troop_no", 1),
           (val_add, ":troop_no", total_npcs_begin),
           (try_begin),
              (neg|troop_slot_eq, ":troop_no", 1, 1), #选中
              (troop_set_slot, ":troop_no", 1, 1), 
              (overlay_set_color, ":object", 0x00FF00), #标绿
              (val_sub, ":object", "$g_presentation_text_5"),
              (val_add, ":object", "$g_presentation_text_6"),
              (overlay_set_color, ":object", 0xFFFFFF), #把敌方对应npc颜色去掉
           (else_try),
              (troop_set_slot, ":troop_no", 1, 0), #清除
              (overlay_set_color, ":object", 0xFFFFFF), 
           (try_end),
        (else_try),
           (is_between, ":object", "$g_presentation_text_6", "$g_presentation_text_8"), #敌军npc选择
           (store_sub, ":troop_no", "$g_presentation_text_8", ":object"),
           (val_sub, ":troop_no", 1),
           (val_add, ":troop_no", total_npcs_begin),
           (try_begin),
              (neg|troop_slot_eq, ":troop_no", 1, 2), #选中
              (troop_set_slot, ":troop_no", 1, 2), #选中
              (overlay_set_color, ":object", 0x00FF00), #标绿
              (val_sub, ":object", "$g_presentation_text_6"),
              (val_add, ":object", "$g_presentation_text_5"),
              (overlay_set_color, ":object", 0xFFFFFF), #把友方对应npc颜色去掉
           (else_try),
              (troop_set_slot, ":troop_no", 1, 0), #清除
              (overlay_set_color, ":object", 0xFFFFFF), 
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_label_10"), #友军阵型选择
           (val_add, ":value", "itm_formation_common"),
           (assign, "$g_quick_battle_encounter_player_formation", ":value"),
        (else_try),
           (eq, ":object", "$g_presentation_obj_label_11"), #敌军阵型选择
           (val_add, ":value", "itm_formation_common"),
           (assign, "$g_quick_battle_encounter_enemy_formation", ":value"),

        (else_try),
           (eq, ":object", "$g_presentation_obj_10"), #友军添加至部队
           (try_begin),
              (lt, "$g_quick_battle_encounter_player_set", 0), #未选择部队
              (display_message, "@请 先 选 择 部 队 ", 0xFF0000),
           (else_try),
              (try_for_range, ":troop_no", total_npcs_begin, total_npcs_end), #友军预选的npc
                 (troop_slot_eq, ":troop_no", 1, 1), 
                 (troop_set_slot, ":troop_no", 1, 0), 
                 (party_force_add_members, "$g_quick_battle_encounter_player_set", ":troop_no", 1), #添加npc进部队
                 (try_for_range, ":slot_no", 0, 2),          #添加私兵，数量控制在上限的一半，最少不会少于1
                    (val_add, ":slot_no", slot_bodygaurd_troop_1),
                    (troop_get_slot, ":bodyguard_troop_no", ":troop_no", ":slot_no"),
                    (gt, ":bodyguard_troop_no", 0),
                    (store_div, ":num_limit", ":bodyguard_troop_no", 10000000),#上限
                    (val_mod, ":bodyguard_troop_no", 10000),
                    (val_div, ":num_limit", 2), 
                    (val_max, ":num_limit", 1), 
                    (party_add_members, "$g_quick_battle_encounter_player_set", ":bodyguard_troop_no", ":num_limit"),#添加
                 (try_end),
                 (store_sub, ":object", ":troop_no", total_npcs_begin), #隐藏友军此npc选项
                 (val_add, ":object", 1),
                 (store_sub, ":object", "$g_presentation_text_7", ":object"), #是反向生成的
                 (overlay_set_display, ":object", 0), 
                 (val_sub, ":object", "$g_presentation_text_5"), #隐藏敌军此npc选项
                 (val_add, ":object", "$g_presentation_text_6"),
                 (overlay_set_display, ":object", 0), 
              (try_end),

              (store_div, ":recuit_round", "$g_quick_battle_encounter_player_party_num", 155),
              (try_for_range, ":unused", 0, ":recuit_round"),
                 (try_begin),
                    (gt, "$g_quick_battle_encounter_player_special_template", 0),
                    (call_script, "script_cf_random_get_party_template", "$g_quick_battle_encounter_player_special_template"), #随机特殊部队模板
                    (assign, ":template_no", reg1),
                 (else_try),
                    (call_script, "script_cf_random_get_party_template", "$g_quick_battle_encounter_player_basic_template"), #随机基础部队模板
                    (assign, ":template_no", reg1),
                 (try_end),
                 (gt, ":template_no", 0), 
                 (party_add_template, "$g_quick_battle_encounter_player_set", ":template_no"),#按部队模板添加兵
              (try_end),
              (call_script, "script_party_reorder", "$g_quick_battle_encounter_player_set"), #重排
              (party_set_slot, "$g_quick_battle_encounter_player_set", slot_tool_party_formation, "$g_quick_battle_encounter_player_formation"), #预设阵型

              (assign, ":count_limit", 2000),
              (try_for_range, ":object", "$g_presentation_obj_2", ":count_limit"), #后刷的部队按钮
                 (troop_slot_ge, "trp_temp_array_a", ":object", 1), #存了部队
                 (troop_get_slot, ":value_no", "trp_temp_array_a", ":object"), 
                 (store_div, ":party_no", ":value_no", 10),
                 (eq, ":party_no", "$g_quick_battle_encounter_player_set"), #是当前部队
                 (val_mod, ":value_no", 10),
                 (eq, ":value_no", 1), #找到名字的overlay
                 (assign, ":count_limit", 0), #break
              (try_end),
              (str_store_item_name, s1, "$g_quick_battle_encounter_player_basic_template"),
              (str_store_party_name, s2, "$g_quick_battle_encounter_player_set"),
              (overlay_set_text, ":object", "@{s1}{s2}"),
              (overlay_set_color, ":object", 0xFFFFFF),
              (party_set_name, "$g_quick_battle_encounter_player_set", "@{s1}{s2}"), #部队改名
              (assign, "$g_quick_battle_encounter_player_set", -1), #清除部队选择
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_11"), #敌军添加至部队
           (try_begin),
              (lt, "$g_quick_battle_encounter_enemy_set", 0), #未选择部队
              (display_message, "@请 先 选 择 部 队 ", 0xFF0000),
           (else_try),
              (try_for_range, ":troop_no", total_npcs_begin, total_npcs_end), #敌军预选的npc
                 (troop_slot_eq, ":troop_no", 1, 2), 
                 (troop_set_slot, ":troop_no", 1, 0), 
                 (party_force_add_members, "$g_quick_battle_encounter_enemy_set", ":troop_no", 1), #添加npc进部队
                 (try_for_range, ":slot_no", 0, 2),          #添加私兵，数量控制在上限的一半，最少不会少于1
                    (val_add, ":slot_no", slot_bodygaurd_troop_1),
                    (troop_get_slot, ":bodyguard_troop_no", ":troop_no", ":slot_no"),
                    (gt, ":bodyguard_troop_no", 0),
                    (store_div, ":num_limit", ":bodyguard_troop_no", 10000000),#上限
                    (val_mod, ":bodyguard_troop_no", 10000),
                    (val_div, ":num_limit", 2), 
                    (val_max, ":num_limit", 1), 
                    (party_add_members, "$g_quick_battle_encounter_enemy_set", ":bodyguard_troop_no", ":num_limit"),#添加
                 (try_end),
                 (store_sub, ":object", ":troop_no", total_npcs_begin), #隐藏敌军此npc选项
                 (val_add, ":object", 1),
                 (store_sub, ":object", "$g_presentation_text_8", ":object"), #是反向生成的
                 (overlay_set_display, ":object", 0), 
                 (val_sub, ":object", "$g_presentation_text_6"), #隐藏友军此npc选项
                 (val_add, ":object", "$g_presentation_text_5"),
                 (overlay_set_display, ":object", 0), 
              (try_end),

              (store_div, ":recuit_round", "$g_quick_battle_encounter_enemy_party_num", 155),
              (try_for_range, ":unused", 0, ":recuit_round"),
                 (try_begin),
                    (gt, "$g_quick_battle_encounter_enemy_special_template", 0),
                    (call_script, "script_cf_random_get_party_template", "$g_quick_battle_encounter_enemy_special_template"), #随机特殊部队模板
                    (assign, ":template_no", reg1),
                 (else_try),
                    (call_script, "script_cf_random_get_party_template", "$g_quick_battle_encounter_enemy_basic_template"), #随机基础部队模板
                    (assign, ":template_no", reg1),
                 (try_end),
                 (gt, ":template_no", 0), 
                 (party_add_template, "$g_quick_battle_encounter_enemy_set", ":template_no"),#按部队模板添加兵
              (try_end),
              (call_script, "script_party_reorder", "$g_quick_battle_encounter_enemy_set"), #重排
              (party_set_slot, "$g_quick_battle_encounter_enemy_set", slot_tool_party_formation, "$g_quick_battle_encounter_enemy_formation"), #预设阵型

              (assign, ":count_limit", 2000),
              (try_for_range, ":object", "$g_presentation_obj_2", ":count_limit"), #后刷的部队按钮
                 (troop_slot_ge, "trp_temp_array_a", ":object", 1), #存了部队
                 (troop_get_slot, ":value_no", "trp_temp_array_a", ":object"), 
                 (store_div, ":party_no", ":value_no", 10),
                 (eq, ":party_no", "$g_quick_battle_encounter_enemy_set"), #是当前部队
                 (val_mod, ":value_no", 10),
                 (eq, ":value_no", 1), #找到名字的overlay
                 (assign, ":count_limit", 0), #break
              (try_end),
              (str_store_item_name, s1, "$g_quick_battle_encounter_enemy_basic_template"),
              (str_store_party_name, s2, "$g_quick_battle_encounter_enemy_set"),
              (overlay_set_text, ":object", "@{s1}{s2}"),
              (overlay_set_color, ":object", 0xFFFFFF),
              (party_set_name, "$g_quick_battle_encounter_enemy_set", "@{s1}{s2}"), #部队改名
              (assign, "$g_quick_battle_encounter_enemy_set", -1), #清除部队选择
           (try_end),

##————————————————————————————————战场设置——————————————————————————————
        (else_try),
           (eq, ":object", "$g_presentation_obj_label_7"), #选择战场模式
           (try_begin),
              (neq, "$g_quick_battle_encounter_mode_confirmed", 1), #未确认之前可选
              (assign, "$g_quick_battle_encounter_mode", ":value"),
           (else_try),
              (overlay_set_val, "$g_presentation_obj_label_7", "$g_quick_battle_encounter_mode"),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_12"), #确定战场模式
           (neq, "$g_quick_battle_encounter_mode_confirmed", 1), 
           (assign, "$g_quick_battle_encounter_mode_confirmed", 1), 
           (overlay_set_display, "$g_presentation_obj_label_8", 1), #显示下一级选择
           (overlay_set_display, "$g_presentation_obj_13", 1), 
           (try_begin),
              (eq, "$g_quick_battle_encounter_mode", 0), #野战
              (overlay_add_item, "$g_presentation_obj_label_8", "@平 原 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@山 地 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@草 原 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@荒 山 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@沼 泽 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@雪 原 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@雪 山 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@沙 漠 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@戈 壁 "),
           (else_try),
              (is_between, "$g_quick_battle_encounter_mode", 1, 3), #攻守城
              (overlay_add_item, "$g_presentation_obj_label_8", "@都 市 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@城 堡 "),
              (overlay_add_item, "$g_presentation_obj_label_8", "@村 庄 "),
           (else_try),
              (eq, "$g_quick_battle_encounter_mode", 3), #海战
              (overlay_add_item, "$g_presentation_obj_label_8", "@空 旷 海 域 "),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_label_8"), #选择战场类型
           (try_begin),
              (neq, "$g_quick_battle_encounter_type_confirmed", 1), #未确认之前可选
              (assign, "$g_quick_battle_encounter_type", ":value"),
           (else_try),
              (overlay_set_val, "$g_presentation_obj_label_8", "$g_quick_battle_encounter_type"),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_13"), #确定战场类型
           (neq, "$g_quick_battle_encounter_type_confirmed", 1), 
           (assign, "$g_quick_battle_encounter_type_confirmed", 1), 
           (overlay_set_display, "$g_presentation_obj_label_9", 1), #显示下一级选择
           (try_begin),
              (eq, "$g_quick_battle_encounter_mode", 0), #野战
              (try_begin),
                 (eq, "$g_quick_battle_encounter_type", 0), #平原
                 (try_for_range, ":unused", "scn_random_sandtable_plain_1", "scn_random_sandtable_mountain_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_plain_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@平 原 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_plain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 1), #山地
                 (try_for_range, ":unused", "scn_random_sandtable_mountain_1", "scn_random_sandtable_steppe_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_mountain_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@山 地 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_mountain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 2), #草原
                 (try_for_range, ":unused", "scn_random_sandtable_steppe_1", "scn_random_sandtable_steppe_mountain_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_steppe_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@草 原 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_steppe_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 3), #荒山
                 (try_for_range, ":unused", "scn_random_sandtable_steppe_mountain_1", "scn_random_sandtable_marsh_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_steppe_mountain_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@荒 山 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_steppe_mountain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 4), #沼泽
                 (try_for_range, ":unused", "scn_random_sandtable_marsh_1", "scn_random_sandtable_snow_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_marsh_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@沼 泽 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_marsh_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 5), #雪原
                 (try_for_range, ":unused", "scn_random_sandtable_snow_1", "scn_random_sandtable_snow_mountain_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_snow_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@雪 原 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_snow_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 6), #雪山
                 (try_for_range, ":unused", "scn_random_sandtable_snow_mountain_1", "scn_random_sandtable_desert_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_snow_mountain_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@雪 山 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_snow_mountain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 7), #沙漠
                 (try_for_range, ":unused", "scn_random_sandtable_desert_1", "scn_random_sandtable_desert_mountain_1"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_desert_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@沙 漠 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_desert_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 8), #戈壁
                 (try_for_range, ":unused", "scn_random_sandtable_desert_mountain_1", "scn_random_sandtable_end"),
                    (store_sub, reg1, ":unused", "scn_random_sandtable_desert_mountain_1"),
                    (val_add, reg1, 1),
                    (overlay_add_item, "$g_presentation_obj_label_9", "@戈 壁 地 图 {reg1} "),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", "scn_random_sandtable_desert_mountain_1"),
              (try_end),
              (overlay_set_text, "$g_presentation_text_10", "@植 被 "), #显示植被设置
              (overlay_set_display, "$g_presentation_obj_slider_4", 1), 
              (overlay_set_text, "$g_presentation_text_11", "@1 "), 
           (else_try),
              (is_between, "$g_quick_battle_encounter_mode", 1, 3), #攻守城
              (try_begin),
                 (eq, "$g_quick_battle_encounter_type", 0), #都市
                 (try_for_range, ":party_no", towns_begin, towns_end),
                    (str_store_party_name, s1, ":party_no"),
                    (overlay_add_item, "$g_presentation_obj_label_9", s1),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", towns_begin),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 1), #城堡
                 (try_for_range, ":party_no", castles_begin, castles_end),
                    (str_store_party_name, s1, ":party_no"),
                    (overlay_add_item, "$g_presentation_obj_label_9", s1),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", castles_begin),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 2), #村庄
                 (try_for_range, ":party_no", villages_begin, villages_end),
                    (str_store_party_name, s1, ":party_no"),
                    (overlay_add_item, "$g_presentation_obj_label_9", s1),
                 (try_end),
                 (assign, "$g_quick_battle_encounter_map", villages_begin),
              (try_end),
           (else_try),
              (eq, "$g_quick_battle_encounter_mode", 3), #海战
              (overlay_add_item, "$g_presentation_obj_label_9", "@暂 无 "),
           (try_end),

        (else_try),
           (eq, ":object", "$g_presentation_obj_label_9"), #选择战场地图
           (try_begin),
              (eq, "$g_quick_battle_encounter_mode", 0), #野战
              (try_begin),
                 (eq, "$g_quick_battle_encounter_type", 0), #平原
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_plain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 1), #山地
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_mountain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 2), #草原
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_steppe_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 3), #荒山
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_steppe_mountain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 4), #沼泽
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_marsh_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 5), #雪原
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_snow_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 6), #雪山
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_snow_mountain_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 7), #沙漠
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_desert_1"),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 8), #戈壁
                 (store_add, "$g_quick_battle_encounter_map", ":value", "scn_random_sandtable_desert_mountain_1"),
              (try_end),
           (else_try),
              (is_between, "$g_quick_battle_encounter_mode", 1, 3), #攻守城
              (try_begin),
                 (eq, "$g_quick_battle_encounter_type", 0), #都市
                 (store_add, "$g_quick_battle_encounter_map", ":value", towns_begin),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 1), #城堡
                 (store_add, "$g_quick_battle_encounter_map", ":value", castles_begin),
              (else_try),
                 (eq, "$g_quick_battle_encounter_type", 2), #村庄
                 (store_add, "$g_quick_battle_encounter_map", ":value", villages_begin),
              (try_end),
           (try_end),
        (else_try),
           (eq, ":object", "$g_presentation_obj_slider_3"), #第一个战场设置，时间
           (assign, "$g_quick_battle_encounter_map_set_1", ":value"),
           (assign, reg1, ":value"),
           (overlay_set_text, "$g_presentation_text_9", "@{reg1} "), 
        (else_try),
           (eq, ":object", "$g_presentation_obj_slider_4"), #第一个战场设置，比如野战的植被
           (assign, "$g_quick_battle_encounter_map_set_2", ":value"),
           (assign, reg1, ":value"),
           (overlay_set_text, "$g_presentation_text_11", "@{reg1} "), 

##————————————————————————————————开始按钮——————————————————————————————
        (else_try),
           (eq, ":object", "$g_presentation_obj_2"), #开始
           (eq, "$g_quick_battle_encounter_type_confirmed", 1), #已设置到场景那一步
           (eq, "$g_quick_battle_encounter_mode_player_confirmed", 1), #友方已确定选择
           (eq, "$g_quick_battle_encounter_mode_enemy_confirmed", 1), #敌方已确定选择

           (assign, "$g_quick_battle_party_total", "$g_quick_battle_party_used"), #记录部队总数
           (assign, "$current_scene", "$g_quick_battle_encounter_map"), #定下所用的沙盘底板
           (assign, "$campaign_time", "$g_quick_battle_encounter_map_set_1"), #记录当前时间
           (assign, "$campaign_round", 1), #记录会战轮次
           (assign, "$campaign_cam_set", -1), #初始化镜头
           (assign, "$current_town", "p_campaign_temp"), #为了与城镇统一，使用"$current_town"，不过并不影响"$g_encountered_party"

           (try_for_range, ":cur_x", 1, 16),
              (try_for_range, ":cur_y", 1, 16),
                 (call_script, "script_get_scene_zone", "$current_scene", ":cur_x", ":cur_y"), #获取储存的地形信息，包括水体岩壁等无法被直接获取的
                 (assign, ":ground_type", reg1),
                 (try_begin),
                    (le, ":ground_type", 0), #无地形
                    (assign, ":ground_type", "itm_zone_none"), #默认
                 (try_end),
                 (call_script, "script_set_center_zone", "$current_town", ":cur_x", ":cur_y", ":ground_type", 0, 0, 0, 0), #初始化（只包括水体岩壁，不包括各种森林）
              (try_end),
           (try_end),

           (try_begin), #确定森林类型
              (this_or_next|is_between, "$g_quick_battle_encounter_map", "scn_random_sandtable_plain_1", "scn_random_sandtable_steppe_1"),
              (is_between, "$g_quick_battle_encounter_map", "scn_random_sandtable_marsh_1", "scn_random_sandtable_snow_1"),
              (assign, ":tree_type", "itm_zone_forest"), #普通森林
           (else_try),
              (is_between, "$g_quick_battle_encounter_map", "scn_random_sandtable_steppe_1", "scn_random_sandtable_marsh_1"),
              (assign, ":tree_type", "itm_zone_steppe_forest"), #稀树森林
           (else_try),
              (is_between, "$g_quick_battle_encounter_map", "scn_random_sandtable_snow_1", "scn_random_sandtable_desert_1"),
              (assign, ":tree_type", "itm_zone_taiga_forest"), #泰加林
           (else_try),
              (is_between, "$g_quick_battle_encounter_map", "scn_random_sandtable_desert_1", "scn_random_sandtable_end"),
              (assign, ":tree_type", "itm_zone_oasis"), #绿洲
           (try_end),

           (assign, ":diffusion_intensity", "$g_quick_battle_encounter_map_set_2"), #森林的扩散强度
           (try_for_range, ":cur_x", 1, 16), #生成森林
              (try_for_range, ":cur_y", 1, 16),
                 (gt, "$g_quick_battle_encounter_map_set_2", 0), #还能够生成森林
                 (call_script, "script_get_center_zone_ground", "$current_town", ":cur_x", ":cur_y"),
                 (eq, reg1, "itm_zone_none"), #只有默认才能继续生成，水体、岩壁等基础地形，和已经生成了其他区块包括其他森林的不动
                 (call_script, "script_change_coordinate_to_number", 15, ":cur_x", ":cur_y"),
                 (assign, ":count_no", reg1),
                 (store_random_in_range, ":value_no", ":count_no", 225),
                 (val_add, ":count_no", "$g_quick_battle_encounter_map_set_2"),
                 (eq, ":count_no", ":value_no"),
                 (val_sub, "$g_quick_battle_encounter_map_set_2", 1), #减少待生成森林量
                 (call_script, "script_set_center_zone", "$current_town", ":cur_x", ":cur_y", ":tree_type", 0, 0, 0, 0), #生成森林
                 (call_script, "script_set_forest_diffusion", "$current_town", ":cur_x", ":cur_y", ":tree_type", ":diffusion_intensity"), #森林扩散
              (try_end),
           (try_end),

           (assign, "$g_total_detachment", 0), #编队总数，便于存取slot，切记其累加是在script_auto_create_detachment里完成的，不能重复
           (try_for_range, ":party_no", 1, "$g_quick_battle_party_total"), #生成编队
              (call_script, "script_party_count_members_function", ":party_no"), #人数和职能
              (gt, reg0, 0), #为提高系统韧性，即使有部队未设置成员也能开始
              (assign, ":troop_count", reg0),
              (party_get_slot, ":team_no", ":party_no", slot_tool_party_team), 
              (call_script, "script_auto_create_detachment", ":party_no", ":troop_count", ":team_no", 1), #计算总人数获得编队人数、数量，并设置临时party以待使用
              (assign, ":detachment_count", reg1), #分队数量（只包括由这一个部队生成的）
              (party_get_slot, ":formation_no", ":party_no", slot_tool_party_formation), #获取预设的阵型
              (try_begin),
                 (eq, ":formation_no", "itm_formation_end"), #阵营设置为自动，采用和大地图一样的脚本获取
                 (call_script, "script_auto_choose_formation", ":party_no"),
                 (assign, ":formation_no", reg1),
              (try_end),
              (call_script, "script_auto_allocate_troop", ":party_no", ":formation_no", ":detachment_count"), #分兵
              (call_script, "script_set_detachment_attitude", ":party_no", -1), #设置编队初始姿态，暂无预设，根据会战的模式可能会改
              (call_script, "script_auto_spawn_detachment", ":party_no", ":formation_no", "$current_town"), #刷出编队
           (try_end),

##新增
           #AI处理
           (try_for_range, ":party_no", 1, "$g_quick_battle_party_total"), #预处理，让聚在一起刷新的部队散开，摆出阵型
              (call_script, "script_auto_create_formation", ":party_no"), #预设该军用于摆阵的权重
              (try_for_range_backwards, ":slot_no", 0, "$g_total_detachment"), 
                 (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
                 (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
                 (try_for_range, ":unused", 0, 5), #先预设五步，后续可能根据会战情况，不同部队有所不同
                    (call_script, "script_cf_campaign_ai", "$current_town", ":party_no"), #AI自动行动
                 (try_end),
              (try_end),
           (try_end),
##新增

           (jump_to_menu, "mnu_campaign_round"),
           (presentation_set_duration, 0),
        (try_end),
       ]),
  ]),


  ]