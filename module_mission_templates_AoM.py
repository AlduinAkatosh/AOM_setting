# -*- coding: UTF-8 -*-

from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *
from module_skills import *

from module_mission_templates_common_trigger import *
from module_mission_templates_boss_trigger import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################


#玩家用开局时物品栏设置
common_AoM_battle_initialize_player_inventory = (
       ti_on_agent_spawn, 0, 0, [],
      [
       (store_trigger_param, ":agent_no", 1),
       (agent_is_human, ":agent_no"),
       (agent_is_alive, ":agent_no"),
       (agent_get_troop_id, ":troop_no", ":agent_no"),
       (ge, ":troop_no", 0),
       (troop_is_hero, ":troop_no"),
       (eq, ":troop_no", "trp_player"),#锁定玩家
       (assign, "$mission_player_agent", ":agent_no"),

       (lt, "$g_inventory_allow", 1),#允许启用新物品栏（不在竞技场等地方）
       (assign, "$cur_weapon_right_hand", 40),
       (assign, "$cur_weapon_left_hand", 43),

       (try_for_range, ":inventory_slot_no", 10, 16),
          (troop_get_inventory_slot, ":weapon_no", ":troop_no", ":inventory_slot_no"),
          (store_add, ":inventory_modifier_slot_no", ":inventory_slot_no", 1201),
          (troop_get_slot, ":modifier_no", ":troop_no", ":inventory_modifier_slot_no"),

          (store_add, ":slot_no", ":inventory_slot_no", 31),
          (agent_set_slot, ":agent_no", ":slot_no", ":weapon_no"),#item_kind
          (val_add, ":slot_no", 12),
          (agent_set_slot, ":agent_no", ":slot_no", ":modifier_no"),#modifier
       (try_end),

       (try_for_range, ":inventory_slot_no", 10, 13),
          (troop_get_inventory_slot, ":weapon_no", ":troop_no", ":inventory_slot_no"),
          (gt, ":weapon_no", 0),
          (item_get_max_ammo, ":ammo_num", ":weapon_no"),
          (store_add, ":slot_no", ":inventory_slot_no", 37),
          (agent_set_slot, "$mission_player_agent", ":slot_no", ":ammo_num"),
       (try_end),

       (try_for_range, ":inventory_slot_no", 13, 16),
          (troop_get_inventory_slot, ":weapon_no", ":troop_no", ":inventory_slot_no"),
          (gt, ":weapon_no", 0),
          (item_get_hit_points, ":shield_hp", ":weapon_no"),
          (store_add, ":slot_no", ":inventory_slot_no", 37),
          (agent_set_slot, "$mission_player_agent", ":slot_no", ":shield_hp"),
       (try_end),
      ])

#新物品栏：切换右手武器
common_AoM_battle_change_right_hand_weapon = (
      0, 0, 0, [
       (lt, "$g_inventory_allow", 1),#允许启用新物品栏（不在竞技场等地方）
       (store_current_scene, ":scene_no"),
       (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
       (neg|conversation_screen_is_active),#不在对话
       (ge, "$mission_player_agent", 0),
       (key_clicked, key_mouse_scroll_up),],
      [
          (assign, "$change_weapon_try_time", 0),
          (call_script, "script_right_hand_get_next_usable_weapon"),
          (try_begin),
             (gt, reg1, 0),
             (agent_equip_item, "$mission_player_agent", reg1, 1), #1槽专供右手武器切换
             (agent_set_wielded_item, "$mission_player_agent", reg1),

             (store_add, ":slot_no", "$cur_weapon_right_hand", 6),
             (agent_get_slot, ":ammo_num", "$mission_player_agent", ":slot_no"),
             (agent_set_ammo, "$mission_player_agent", reg1, ":ammo_num"),
          (try_end),
          (assign, "$change_weapon_try_time", 0),
      ])
#新物品栏：切换左手武器
common_AoM_battle_change_left_hand_weapon = (
      0, 0, 0, [
       (lt, "$g_inventory_allow", 1),#允许启用新物品栏（不在竞技场等地方）
       (store_current_scene, ":scene_no"),
       (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
       (neg|conversation_screen_is_active),#不在对话
       (ge, "$mission_player_agent", 0),
       (key_clicked, key_mouse_scroll_down),],
      [
          (assign, "$change_weapon_try_time", 0),
          (call_script, "script_left_hand_get_next_usable_weapon"), #2槽专供左手武器切换
          (try_begin),
             (gt, reg1, 0),
             (agent_equip_item, "$mission_player_agent", reg1, 2),
             (agent_set_wielded_item, "$mission_player_agent", reg1),
          (try_end),
          (assign, "$change_weapon_try_time", 0),
      ])
#新物品栏：收回武器
common_AoM_battle_change_sheath_weapon = (
      0, 0, 0, [
       (lt, "$g_inventory_allow", 1),#允许启用新物品栏（不在竞技场等地方）
       (store_current_scene, ":scene_no"),
       (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
       (neg|conversation_screen_is_active),#不在对话
       (ge, "$mission_player_agent", 0),
       (game_key_clicked, gk_sheath_weapon),],
      [
          (agent_set_wielded_item, "$mission_player_agent", -1),
          (try_begin),
             (agent_get_slot, ":item_no", "$mission_player_agent", "$cur_weapon_right_hand"),
             (gt, ":item_no", 0),
             (agent_unequip_item,  "$mission_player_agent", ":item_no", 1),
          (try_end),
          (try_begin),
             (agent_get_slot, ":item_no", "$mission_player_agent", "$cur_weapon_left_hand"),
             (gt, ":item_no", 0),
             (agent_unequip_item,  "$mission_player_agent", ":item_no", 2),
          (try_end),
          (try_begin),
             (agent_get_item_slot, ":item_no", "$mission_player_agent", 1),#防止因拾捡道具导致无法使用武器
             (gt, ":item_no", 0),
             (agent_unequip_item,  "$mission_player_agent", ":item_no", 1),
          (else_try),
             (agent_get_item_slot, ":item_no", "$mission_player_agent", 2),
             (gt, ":item_no", 0),
             (agent_unequip_item,  "$mission_player_agent", ":item_no", 2),
          (try_end),
      ])
#新物品栏：丢下武器
common_AoM_battle_drop_weapon = (
      ti_on_item_dropped, 0, 0, [
       (lt, "$g_inventory_allow", 1),#允许启用新物品栏（不在竞技场等地方）
       (store_current_scene, ":scene_no"),
       (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
       (neg|conversation_screen_is_active),#不在对话
       (ge, "$mission_player_agent", 0),],
      [
       (store_trigger_param, ":agent_no", 1),
       (store_trigger_param, ":item_no", 2),
       (eq, ":agent_no", "$mission_player_agent"),#玩家
       (item_get_type, ":type_no", ":item_no"),
       (try_begin),
          (neq, ":type_no", itp_type_shield),
          (neq, ":type_no", itp_type_bow),
          (agent_set_slot, "$mission_player_agent", "$cur_weapon_right_hand", -1),
          (store_add, ":modifier_slot_no", "$cur_weapon_right_hand", 12),
          (agent_set_slot, "$mission_player_agent", ":modifier_slot_no", -1),#modifier
       (else_try),
          (agent_set_slot, "$mission_player_agent", "$cur_weapon_left_hand", -1),
          (store_add, ":modifier_slot_no", "$cur_weapon_left_hand", 12),
          (agent_set_slot, "$mission_player_agent", ":modifier_slot_no", -1),#modifier
       (try_end),
      ])
#新物品栏：捡起武器
common_AoM_battle_pick_weapon = (
      ti_on_item_picked_up, 0, 0, [
(eq, 0, 1),
       (lt, "$g_inventory_allow", 1),#允许启用新物品栏（不在竞技场等地方）
       (store_current_scene, ":scene_no"),
       (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
       (neg|conversation_screen_is_active),#不在对话
       (ge, "$mission_player_agent", 0),],
      [
       (store_trigger_param, ":agent_no", 1),
       (store_trigger_param, ":item_no", 2),
       (eq, ":agent_no", "$mission_player_agent"),#玩家
       (item_get_type, ":type_no", ":item_no"),
       (try_begin),
          (neq, ":type_no", itp_type_goods),
          (neq, ":type_no", itp_type_shield),
          (neq, ":type_no", itp_type_bow),
          (agent_set_slot, "$mission_player_agent", "$cur_weapon_right_hand", ":item_no"),
#          (store_add, ":modifier_slot_no", "$cur_weapon_right_hand", 12),
#          (agent_set_slot, "$mission_player_agent", ":modifier_slot_no", -1),#modifier
       (else_try),
          (neq, ":type_no", itp_type_goods),
          (agent_set_slot, "$mission_player_agent", "$cur_weapon_left_hand", ":item_no"),
#          (store_add, ":modifier_slot_no", "$cur_weapon_left_hand", 12),
#          (agent_set_slot, "$mission_player_agent", ":modifier_slot_no", -1),#modifier
       (try_end),
      ])


#翻滚
#from user jj95198 and user get.shot.with.. in M&B Chinese Station
common_rolling =( 0, 0, 0, 
      [
       (key_is_down, key_left_shift),
       (store_current_scene, ":scene_no"),
       (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
       (neg|conversation_screen_is_active),#不在对话
       (ge, "$mission_player_agent", 0),
       (agent_is_alive,"$mission_player_agent"),
       (agent_get_horse, ":horse_no", "$mission_player_agent"),#步行
       (le, ":horse_no", -1),
       (neq, "$crouch_mode", 1),#最普通的潜行术不能翻滚
      ],
      [#four directions' rolling四向翻滚
          (try_begin),
             (game_key_clicked, gk_move_forward),
             (agent_set_animation,"$mission_player_agent","anim_roll_forward"),
             (play_sound, "snd_tc_fangun"),
          (else_try),
             (game_key_clicked, gk_move_backward),
             (agent_set_animation,"$mission_player_agent","anim_roll_backward"),
             (play_sound, "snd_tc_fangun"),
          (else_try),
             (game_key_clicked, gk_move_left),
             (agent_set_animation,"$mission_player_agent","anim_roll_left"),
             (play_sound, "snd_tc_fangun"),
          (else_try),
             (game_key_clicked, gk_move_right),
             (agent_set_animation,"$mission_player_agent","anim_roll_right"),
             (play_sound, "snd_tc_fangun"),
         (try_end),
      ])

#自飞测试
common_battle_fly_open = (
  0, 0, 0, [
    (key_clicked, key_z),
    (store_current_scene, ":scene_no"),
    (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
    (neg|conversation_screen_is_active),#不在对话
    (ge, "$mission_player_agent", 0),
    (agent_is_alive,"$mission_player_agent"),
    (agent_get_horse, ":horse_no", "$mission_player_agent"),
    (le, ":horse_no", -1),
  ],
  [
    (try_begin),
        (eq, "$fly_mode", 0),
        (display_message, "@Can_fly"),
        (agent_set_no_dynamics, "$mission_player_agent", 1),
        (assign, "$fly_mode", 1),
    (else_try),
        (eq, "$fly_mode", 1),
        (display_message, "@Stop_fly"),
        (agent_set_no_dynamics, "$mission_player_agent", 0),
        (assign, "$fly_mode", 0),
    (try_end),
    ])

common_battle_fly = (
  0, 0, 0, [
    (eq, "$fly_mode", 1),
    (store_current_scene, ":scene_no"),
    (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
    (neg|conversation_screen_is_active),#不在对话
    (ge, "$mission_player_agent", 0),
    (agent_is_alive,"$mission_player_agent"),
    (agent_get_horse, ":horse_no", "$mission_player_agent"),
    (le, ":horse_no", -1),

    (this_or_next|game_key_clicked, gk_jump),
    (this_or_next|game_key_is_down, gk_jump),
    (this_or_next|key_clicked, key_left_control),
    (this_or_next|key_is_down, key_left_control),
    (this_or_next|game_key_clicked, gk_move_forward),
    (this_or_next|game_key_is_down, gk_move_forward),
    (this_or_next|game_key_clicked, gk_move_backward),
    (this_or_next|game_key_is_down, gk_move_backward),
    (this_or_next|game_key_clicked, gk_move_left),
    (this_or_next|game_key_is_down, gk_move_left),
    (this_or_next|game_key_clicked, gk_move_right),
    (game_key_is_down, gk_move_right),],
  [
      (agent_get_position, pos10, "$mission_player_agent"),
      (assign, ":move_x", 0),
      (assign, ":move_y", 0),
      (assign, ":move_z", 0),
      (try_begin), #up
        (this_or_next|game_key_clicked, gk_jump),
        (game_key_is_down, gk_jump),
        (assign, ":move_z", 30),
      (try_end),
      (try_begin), #down
        (this_or_next|key_clicked, key_left_control),
        (key_is_down, key_left_control),
        (assign, ":move_z", -30),
      (try_end),
      (try_begin), #forward
        (this_or_next|game_key_clicked, gk_move_forward),
        (game_key_is_down, gk_move_forward),
        (assign, ":move_y", 30),
      (try_end),
      (try_begin), #backward
        (this_or_next|game_key_clicked, gk_move_backward),
        (game_key_is_down, gk_move_backward),
        (assign, ":move_y", -30),
      (try_end),
      (try_begin), #left
        (this_or_next|game_key_clicked, gk_move_left),
        (game_key_is_down, gk_move_left),
        (assign, ":move_x", -30),
      (try_end),
      (try_begin), #right
        (this_or_next|game_key_clicked, gk_move_right),
        (game_key_is_down, gk_move_right),
        (assign, ":move_x", 30),
      (try_end),
      (position_move_x, pos10, ":move_x"),
      (position_move_y, pos10, ":move_y"),
      (position_move_z, pos10, ":move_z"),
      (agent_set_position, "$mission_player_agent", pos10),
    ])


## 战场延续＋视角
common_init_deathcam = (
   0, 0, ti_once,
   [],
   [
      (assign, "$pop_camera_on", 0),
      # mouse center coordinates (non-windowed)
      (assign, "$pop_camera_mouse_center_x", 500),
      (assign, "$pop_camera_mouse_center_y", 375),
      # last recorded mouse coordinates
      (assign, "$pop_camera_mouse_x", "$pop_camera_mouse_center_x"),
      (assign, "$pop_camera_mouse_y", "$pop_camera_mouse_center_y"),
      # counts how many cycles the mouse stays in the same position, to determine new center in windowed mode
      (assign, "$pop_camera_mouse_counter", 0),
   ]
)

common_start_deathcam = (
   0, 4, ti_once, # 4 seconds delay before the camera activates
   [
     (main_hero_fallen),
     (eq, "$pop_camera_on", 0),
   ],
   [
      (agent_get_position, pos1, "$mission_player_agent"),
      (position_get_x, ":pos_x", pos1),
      (position_get_y, ":pos_y", pos1),
      (init_position, pos47),
      (position_set_x, pos47, ":pos_x"),
      (position_set_y, pos47, ":pos_y"),
      (position_set_z_to_ground_level, pos47),
      (position_move_z, pos47, 250),
      (mission_cam_set_mode, 1, 0, 0),
      (mission_cam_set_position, pos47),
      (assign, "$pop_camera_rotx", 0),
      (assign, "$pop_camera_on", 1),
   ]
)

common_move_deathcam = (
   0, 0, 0,
   [
      (eq, "$pop_camera_on", 1),
      (this_or_next|game_key_clicked, gk_move_forward),
      (this_or_next|game_key_is_down, gk_move_forward),
      (this_or_next|game_key_clicked, gk_move_backward),
      (this_or_next|game_key_is_down, gk_move_backward),
      (this_or_next|game_key_clicked, gk_move_left),
      (this_or_next|game_key_is_down, gk_move_left),
      (this_or_next|game_key_clicked, gk_move_right),
      (game_key_is_down, gk_move_right),
   ],
   [
      (mission_cam_get_position, pos47),
      (assign, ":move_x", 0),
      (assign, ":move_y", 0),
      (try_begin), #forward
        (this_or_next|game_key_clicked, gk_move_forward),
        (game_key_is_down, gk_move_forward),
        (assign, ":move_y", 10),
      (try_end),
      (try_begin), #backward
        (this_or_next|game_key_clicked, gk_move_backward),
        (game_key_is_down, gk_move_backward),
        (assign, ":move_y", -10),
      (try_end),
      (try_begin), #left
        (this_or_next|game_key_clicked, gk_move_left),
        (game_key_is_down, gk_move_left),
        (assign, ":move_x", -10),
      (try_end),
      (try_begin), #right
        (this_or_next|game_key_clicked, gk_move_right),
        (game_key_is_down, gk_move_right),
        (assign, ":move_x", 10),
      (try_end),
      (position_move_x, pos47, ":move_x"),
      (position_move_y, pos47, ":move_y"),
      (mission_cam_set_position, pos47),      
   ]
)

deathcam_mouse_deadzone = 2 #set this to a positive number (MV: 2 or 3 works well for me, but needs testing on other people's PCs)

common_rotate_deathcam = (
   0, 0, 0,
   [
      (eq, "$pop_camera_on", 1),
      (neg|is_presentation_active, "prsnt_battle"),
      (mouse_get_position, pos1),
      (set_fixed_point_multiplier, 1000),
      (position_get_x, reg1, pos1),
      (position_get_y, reg2, pos1),
      (this_or_next|neq, reg1, "$pop_camera_mouse_center_x"),
      (neq, reg2, "$pop_camera_mouse_center_y"),
   ],
   [
      # fix for windowed mode: recenter the mouse
      (assign, ":continue", 1),
      (try_begin),
        (eq, reg1, "$pop_camera_mouse_x"),
        (eq, reg2, "$pop_camera_mouse_y"),
        (val_add, "$pop_camera_mouse_counter", 1),
        (try_begin), #hackery: if the mouse hasn't moved for X cycles, recenter it
          (gt, "$pop_camera_mouse_counter", 50),
          (assign, "$pop_camera_mouse_center_x", reg1),
          (assign, "$pop_camera_mouse_center_y", reg2),
          (assign, "$pop_camera_mouse_counter", 0),
        (try_end),
        (assign, ":continue", 0),
      (try_end),
      (eq, ":continue", 1), #continue only if mouse has moved
      (assign, "$pop_camera_mouse_counter", 0), # reset recentering hackery
      
      # update recorded mouse position
      (assign, "$pop_camera_mouse_x", reg1),
      (assign, "$pop_camera_mouse_y", reg2),
      
      (mission_cam_get_position, pos47),
      (store_sub, ":shift", "$pop_camera_mouse_center_x", reg1), #horizontal shift for pass 0
      (store_sub, ":shift_vertical", reg2, "$pop_camera_mouse_center_y"), #for pass 1
      
      (try_for_range, ":pass", 0, 2), #pass 0: check mouse x movement (left/right), pass 1: check mouse y movement (up/down)
        (try_begin),
          (eq, ":pass", 1),
          (assign, ":shift", ":shift_vertical"), #get ready for the second pass
        (try_end),
        (this_or_next|lt, ":shift", -deathcam_mouse_deadzone), #skip pass if not needed (mouse deadzone)
        (gt, ":shift", deathcam_mouse_deadzone),
        
        (assign, ":sign", 1),
        (try_begin),
          (lt, ":shift", 0),
          (assign, ":sign", -1),
        (try_end),
        # square root calc
        (val_abs, ":shift"),
        (val_sub, ":shift", deathcam_mouse_deadzone), # ":shift" is now 1 or greater
        (convert_to_fixed_point, ":shift"),
        (store_sqrt, ":shift", ":shift"),
        (convert_from_fixed_point, ":shift"),
        (val_clamp, ":shift", 1, 6), #limit rotation speed
        (val_mul, ":shift", ":sign"),
        (try_begin),
          (eq, ":pass", 0), # rotate around z (left/right)
          (store_mul, ":minusrotx", "$pop_camera_rotx", -1),
          (position_rotate_x, pos47, ":minusrotx"), #needed so camera yaw won't change
          (position_rotate_z, pos47, ":shift"),
          (position_rotate_x, pos47, "$pop_camera_rotx"), #needed so camera yaw won't change
        (try_end),
        (try_begin),
          (eq, ":pass", 1), # rotate around x (up/down)
          (position_rotate_x, pos47, ":shift"),
          (val_add, "$pop_camera_rotx", ":shift"),
        (try_end),
      (try_end), #try_for_range ":pass"
      (mission_cam_set_position, pos47),
   ]
)

common_kt_move_right_deathcam = (
0, 0, 0,
[
(main_hero_fallen),
(this_or_next|game_key_clicked, key_d),
(key_is_down, key_d),
],
[
(get_player_agent_no, ":player_agent"),
(agent_get_look_position, pos1, ":player_agent"),
(position_move_x, pos1, 10),
(agent_set_position, ":player_agent", pos1),
]
)
## MadVader deathcam end


#triggers related to deathcam
deathcam_triggers = [
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
]


#triggers of Atrium of Milky commonly uesd in normal battles
AoM_battle_triggers = [
      common_AoM_battle_initialize_player_inventory, #触发器1
      common_AoM_battle_change_right_hand_weapon, #触发器2
      common_AoM_battle_change_left_hand_weapon, #触发器3
      common_AoM_battle_change_sheath_weapon, #触发器4
      common_AoM_battle_pick_weapon, #触发器5
      common_AoM_battle_drop_weapon, #触发器6

      common_rolling, #触发器7
#      common_battle_fly_open,
#      common_battle_fly,

      (ti_before_mission_start, 0, 0, [], #触发器8
      [
         (set_fixed_point_multiplier, 100),
         (assign, "$mission_player_agent", -1),#设置为-1，生成时刷新
         (store_sub, "$state_total_number", "itm_state_end", "itm_state_begin"),
         (val_sub, "$state_total_number", 1),
         (assign, "$battle_environment", -1),#全局环境归零
         (assign, "$scene_sea_level", 114514),#水面高度归零，只有需要下水的图才会放浮标，只有放了浮标才会有水面高度，才会判断是否在水下。

         (assign, "$g_film_state", -1),#cam、dialog和stage都是0时关停，123456逐步推进
         (assign, "$g_film_cam", -1),
         (assign, "$g_film_dialog", -1),

         (assign, "$mission_boss_agent", -1),#用于AI处理时的临时变量，储存agent    #bossAI系统归零
         (assign, "$mission_boss_1", -1),#一号boss的agent
         (assign, "$mission_boss_2", -1),#二号boss的agent
         (assign, "$mission_boss_3", -1),#三号boss的agent
         (assign, "$g_talking_agent", -1),#对话展示
         (assign, "$g_scene_name", -1),#地名展示
      ]),

############刷出时设定各种技能###################
      (ti_on_agent_spawn, 0, 0, [], #触发器9
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_alive, ":agent_no"),

#————————————————————————————————人马通用的初始化————————————————————————————
         (agent_set_slot, ":agent_no", slot_agent_state_caculate, 0),
         (try_for_range, ":count_no", 0, "$state_total_number"),                 #state slot
            (store_add, ":slot_no", ":count_no", slot_agent_state_count_1),
            (agent_set_slot, ":agent_no", ":slot_no", 0),
         (try_end),

         (try_for_range, ":count_no", 0, 8),#特效件
            (store_add, ":slot_no", slot_agent_prop_using_1, ":count_no"),
            (agent_set_slot, ":agent_no", ":slot_no", -1),
         (try_end),

         (agent_set_slot, ":agent_no", slot_ai_target, -1),#AI目标清空

#———————————————————————因为先生成人再生成马，所以将涉及步骑兵的判定改为分析troop——————————————————
         (try_begin),
            (agent_is_human, ":agent_no"),
            (agent_get_troop_id, ":troop_no", ":agent_no"),#原兵种
            (troop_get_type, ":agent_race_no", ":troop_no"),#种族

            (try_begin),
               (this_or_next|eq, ":agent_race_no", tf_beast_man),#兽人强制装备兽爪
               (eq, ":agent_race_no", tf_beast_woman),
               (try_begin),
                  (neg|agent_has_item_equipped, ":agent_no", "itm_therianthropy_claw"),#没装备兽爪
                  (assign, ":limit_no", 4),
                  (assign, ":value_no", -1),
                  (try_for_range, ":itm_slot", 0, ":limit_no"),
                     (agent_get_item_slot, ":item_no", ":agent_no", ":itm_slot"),
                     (le, ":item_no", 0),
                     (assign, ":value_no", ":itm_slot"),
                     (assign, ":limit_no", 0),#break
                  (try_end),
                  (try_begin),
                     (eq, ":value_no", -1),
                     (store_random_in_range, ":value_no", 0, 4),#没空位就随机抽一个放
                  (try_end),
                  (agent_equip_item, ":agent_no", "itm_therianthropy_claw", ":value_no"),
               (try_end),
            (try_end),

            (call_script, "script_troop_mounted_check", ":troop_no"),
            (assign, ":mounted_type_no", reg1),

            (try_for_range, ":count_no", 0, 6),                                                    #new passive slots, each passive skill slot records 15 skills.
               (store_add, ":slot_no_1", ":count_no", slot_troop_passive_skill_1),
               (troop_get_slot, ":passive_skill_count", ":troop_no", ":slot_no_1"),
               (store_add, ":slot_no_2", ":count_no", slot_agent_passive_skill_1),
               (agent_set_slot, ":agent_no", ":slot_no_2", ":passive_skill_count"),
            (try_end),

            (assign, ":slot_begin", slot_troop_active_skill_1),                             #active slot
            (store_add, ":slot_end", ":slot_begin", 6),
            (try_for_range, ":slot_no", ":slot_begin", ":slot_end"),#active skill
               (troop_get_slot, ":skill_no", ":troop_no", ":slot_no"),
               (gt, ":skill_no", 0),
               (store_sub, ":slot_no_2", ":slot_no", slot_troop_active_skill_1),
               (val_add, ":slot_no_2", slot_agent_active_skill_1),
               (agent_set_slot, ":agent_no", ":slot_no_2", ":skill_no"),
            (try_end),

##________________________________________________________________________移动速度___________________________________________________________

            (assign, ":speed_modifier_caculate", 100),
            (try_begin),#军事传统只能选一个
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_yishith_military_tradition"),#伊希斯军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (eq, ":mounted_type_no", 1),                #步行
               (val_add, ":speed_modifier_caculate", 40),#+40
            (else_try),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_longshu_military_tradition"),#龙树军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (val_add, ":speed_modifier_caculate", 20),#+20
            (else_try),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_state_military_tradition"),#自由城邦据军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (eq, ":mounted_type_no", 3),                #骑行步兵
               (val_sub, ":speed_modifier_caculate", 20),#-20
            (try_end),

            (try_begin),
               (eq, ":agent_race_no", tf_zombie),#僵尸
               (val_sub, ":speed_modifier_caculate", 60),#-60
            (else_try),
               (eq, ":agent_race_no", tf_ghost),#幽灵
               (val_add, ":speed_modifier_caculate", 65),#+65
            (else_try),
               (eq, ":agent_race_no", tf_walker),#丧尸
               (val_sub, ":speed_modifier_caculate", 70),#-70
            (try_end),

            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_blood_churn"),#逆流恶血
               (gt, reg1, 0),                                                                                                                          #success
               (call_script, "script_proceed_state", ":agent_no", "itm_state_blood_burst", reg1),#血潮汹涌
               (val_add, ":speed_modifier_caculate", 30),#+30
            (try_end),

            (agent_set_speed_modifier, ":agent_no", ":speed_modifier_caculate"),

            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_korouto_military_tradition"),#科鲁托军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (eq, ":mounted_type_no", 2),                #骑兵
               (agent_set_horse_speed_factor, ":agent_no", 110),
            (try_end),

##________________________________________________________________________血量上限___________________________________________________________
            (call_script, "script_store_troop_max_hit_points", ":troop_no"),
            (assign, ":max_hp", reg1),
            (assign, ":max_hp_caculate", reg1),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_strong_vitality"),#鲜血旺盛
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 15),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_stubborn_beast_body"),#野性兽魄
               (gt, reg1, 0),                                                                                                                          #success
               (val_add, ":max_hp_caculate", 40),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_inner_domination"),#内在支配
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 20),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_vonbining_yin_and_yang"),#两仪兼济
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 5),
               (val_mul, reg1, ":max_hp"),
               (val_div, reg1, 100),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_living_organs"),#活物脏器
               (gt, reg1, 0),                                                                                                                          #success
               (val_add, ":max_hp_caculate", 200),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_protecting_qi"),#护体真气
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 20),
               (val_add, reg1, 10),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_five_element_quenching_body"),#五相淬体
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 10),
               (val_add, reg1, 100),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_dragon_power_surging"),#龙力涌动
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 20),
               (val_mul, reg1, ":max_hp"),
               (val_div, reg1, 100),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_flesh_consecration"),#肉身祝圣
               (gt, reg1, 0),                                                                                                                          #success
               (store_div, reg1, ":max_hp", 2),
               (val_add, ":max_hp_caculate", reg1),
               (call_script, "script_proceed_state", ":agent_no", "itm_state_rebirth", 1),#回生
               (agent_set_no_death_knock_down_only, ":agent_no", 1),
            (else_try),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_dead_shell"),#死性外壳
               (gt, reg1, 0),                                                                                                                          #success
               (store_mul, reg1, ":max_hp", 2),
               (val_add, ":max_hp_caculate", reg1),
               (call_script, "script_proceed_state", ":agent_no", "itm_state_rebirth", 1),#回生
               (agent_set_no_death_knock_down_only, ":agent_no", 1),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_human_summit"),#人巅之躯
               (gt, reg1, 0),                                                                                                                          #success
               (store_add, ":active_begin", "itm_active_skills_begin", 1),
               (assign, ":count_no", 0),
               (try_for_range, ":active_skill_no", ":active_begin", "itm_active_skills_end"),
                  (call_script, "script_check_troop_active_skill", ":troop_no", ":active_skill_no"),
                  (gt, reg1, 0),
                  (item_has_property, ":active_skill_no", itp_unique),
                  (val_add, ":count_no", 1),
               (try_end),
               (val_mul, ":count_no", 50),
               (val_mul, ":count_no", ":max_hp"),
               (val_div, ":count_no", 100),
               (val_add, ":max_hp_caculate", ":count_no"),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_resentment"),#积怨
               (gt, reg1, 0),   
               (val_mul, ":max_hp_caculate", 9),
               (val_div, ":max_hp_caculate", 10),
            (try_end),
##########饰物
            (try_begin),
               (call_script, "script_check_accessorise_equipped", ":troop_no", "itm_small_life_talisman"),#残破命脉护符
               (gt, reg1, 0),   
               (store_div, reg1, ":max_hp", 20),
               (val_add, ":max_hp_caculate", reg1),
            (try_end),
            (agent_set_max_hit_points, ":agent_no", ":max_hp_caculate", 1),


##________________________________________________________________受被动技能影响的攻击力___________________________________________________________
            (assign, ":damage_caculate", 100),
#a few military traditions that add damage
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_powell_military_tradition"),#普威尔军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (neg|agent_is_defender, ":agent_no"),#attacker party
               (val_add, ":damage_caculate", 20),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_longshu_military_tradition"),#龙树军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (val_add, ":damage_caculate", 10),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_starkhook_military_tradition"),#大公国军事传统
               (gt, reg1, 0),                                                                                                                          #success
               (eq, ":mounted_type_no", 1),                #步兵
               (val_add, ":damage_caculate", 15),
            (try_end),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_dragon_power_surging"),#龙力涌动
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 5),
               (val_add, ":damage_caculate", reg1),
            (try_end),
            (agent_set_damage_modifier, ":agent_no", ":damage_caculate"),

##_______________________________________________________________________装填速度___________________________________________________________
            (assign, ":damage_caculate", 100),
            (try_begin),
               (eq, ":agent_race_no", tf_zombie),#僵尸
               (val_sub, ":damage_caculate", 90),#-90
            (else_try),
               (eq, ":agent_race_no", tf_skeleton),#骷髅
               (val_add, ":damage_caculate", 10),#+1
            (else_try),
               (eq, ":agent_race_no", tf_walker),#丧尸
               (val_sub, ":damage_caculate", 70),#-70
            (try_end),
            (agent_set_reload_speed_modifier, ":agent_no", ":damage_caculate"),

##_______________________________________________________________________特殊能力___________________________________________________________
            (try_begin),
               (eq, ":agent_race_no", tf_ghost),#幽灵
               (item_get_max_ammo, ":timer_threshold", "itm_state_blurs"),#阈值
               (call_script, "script_activate_state", ":agent_no", "itm_state_blurs", ":timer_threshold"),#虚影化开始
            (try_end),

            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_bone_accumulation"),#积骨
               (gt, reg1, 0),                                                                                                                          #success
               (val_mul, reg1, 30),
               (call_script, "script_proceed_state", ":agent_no", "itm_state_moving_cemetery", reg1),#移动墓地
            (try_end),

            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_holy_rebirth"),#圣善夜
               (gt, reg1, 0),                                                                                                                          #success
               (call_script, "script_proceed_state", ":agent_no", "itm_state_rebirth", reg1),#回生
               (agent_set_no_death_knock_down_only, ":agent_no", 1),
            (else_try),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_undead_rebirth"),#回魂夜
               (gt, reg1, 0),                                                                                                                          #success
               (call_script, "script_proceed_state", ":agent_no", "itm_state_rebirth", reg1),#回生
               (agent_set_no_death_knock_down_only, ":agent_no", 1),
            (try_end),

##_______________________________________________________________________马的部分___________________________________________________________
         (else_try),
            (neg|agent_is_human, ":agent_no"),
         (try_end),

#储存boss的agent，避免反复try for agents
         (try_begin),
            (neq, ":troop_no", "trp_player"),
            (eq, ":troop_no", "$boss_choose_1"),
            (assign, "$mission_boss_1", ":agent_no"),
         (else_try),
            (neq, ":troop_no", "trp_player"),
            (eq, ":troop_no", "$boss_choose_2"),
            (assign, "$mission_boss_2", ":agent_no"),
         (else_try),
            (neq, ":troop_no", "trp_player"),
            (eq, ":troop_no", "$boss_choose_3"),
            (assign, "$mission_boss_3", ":agent_no"),
         (try_end),
         ]),


############新摄像机角度（未使用）
      (0, 0, 0, [ #触发器10
(eq, 0, 1),
         (agent_is_alive, "$mission_player_agent"),
         (agent_get_horse, ":horse_no", "$mission_player_agent"),
         (lt, ":horse_no", 0),],        #cam
      [
         (agent_get_position, pos1, "$mission_player_agent"),
         (copy_position, pos3, pos1),
         (agent_get_look_position, pos2, "$mission_player_agent"),
         (position_copy_rotation, pos3, pos2),
         (position_move_y, pos3, -230),   
         (position_move_z, pos3, 160),   
         (mission_cam_set_mode, 1),   
         (mission_cam_set_position, pos3),     
         ]),

############伤害计算###################
#First calculate special effects, then add damage, then reduce damage, and finally settle special effects
      (ti_on_agent_hit, 0, 0, [],  #触发器11
      [  
         (store_trigger_param_1, ":beattacked_agent_no"),
         (store_trigger_param_2, ":attack_agent_no"),
         (store_trigger_param_3, ":damage"),
#         (store_trigger_param_5, ":missile_no"),
         (try_begin),
            (gt, reg0, 0),
            (assign, ":weapon_no", reg0),
            (item_get_type, ":weapon_type_no", ":weapon_no"),

            (set_fixed_point_multiplier, 100),
            (item_get_weight, ":weapon_weight_count", ":weapon_no"),
            (eq, ":weapon_type_no", itp_type_thrown),
            (item_get_max_ammo, ":weapon_max_ammo", ":weapon_no"),
            (val_div, ":weapon_weight_count", ":weapon_max_ammo"),#投掷武器按单个的算
         (try_end),

         (agent_is_alive, ":beattacked_agent_no"),
#         (agent_is_human, ":beattacked_agent_no"),
         (agent_is_alive, ":attack_agent_no"),
#         (agent_is_human, ":attack_agent_no"),
         (get_player_agent_no, "$mission_player_agent"),
         (agent_get_troop_id, ":beattacked_troop_no", ":beattacked_agent_no"),
         (troop_get_type, ":beattacked_race_no", ":beattacked_troop_no"),#种族
         (agent_get_troop_id, ":attack_troop_no", ":attack_agent_no"),
         (agent_get_horse, ":attack_agent_horse_no", ":attack_agent_no"),
         (agent_get_horse, ":beattacked_agent_horse_no", ":beattacked_agent_no"),
         (store_agent_hit_points, ":attack_agent_hp_percent", ":attack_agent_no", 0),
         (store_agent_hit_points, ":beattacked_agent_hp_percent", ":beattacked_agent_no", 0),

         (assign, ":damage_caculate", ":damage"),

#伤害抑制技能
         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_fake_shield"),#假性护盾
            (gt, reg1, 0),                                                                                                                          #success
            (assign, ":fake_shield_count", reg1),

            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_fake_shield_penetration"),#真性贯穿
            (le, reg1, 0),                                                                                                                            #success

            (val_add, ":fake_shield_count", 2),
            (gt, ":fake_shield_count", ":damage_caculate"),
            (assign, ":damage_caculate", 0),
         (try_end),

##_____________________________________________________________________增伤部分______________________________________________________________________
         (try_begin),
            (gt, ":damage", 0),
            (assign, ":critical_attack_count", 0),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_fatal"),#致命
               (gt, reg1, 0),                                                                                                                          #success
               (assign, ":critical_attack_count", reg1),
            (else_try),
               (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_critical_protection"),#弱点防御
               (le, reg1, 0),                                                                                                                           #success
               (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_critical_attack"),#弱点攻击
               (gt, reg1, 0),                                                                                                                          #success

               (store_skill_level, ":npc_skl", skl_weapon_master, ":attack_troop_no"),
               (store_random_in_range, ":npc_skl_1",0 ,100),
               (lt, ":npc_skl_1", ":npc_skl"),                                                                                                   #success
               (assign, ":critical_attack_count", reg1),
            (else_try),
               (eq, "$infiltrate_tut", 1),#潜行模式
               (neg|agent_slot_eq, ":beattacked_agent_no", slot_agent_alarmed_level, 3),#不在警戒3
               (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_critical_protection"),#弱点防御
               (le, reg1, 0),                                                                                                                           #success
               (assign, ":critical_attack_count", 5),
            (try_end),
            (gt, ":critical_attack_count", 0),                                                                                                  #success

            (val_mul, ":critical_attack_count", ":damage"),
            (val_div, ":critical_attack_count", 5),
            (val_add, ":damage_caculate", ":critical_attack_count"),#damage*(1.2\1.4\1.6\1.7\2)
            (try_begin),
               (eq, "$mission_player_agent", ":attack_agent_no"),
               (display_message, "@暴 击 ! ", 0x71C671),
            (try_end),
         (try_end),

#a few military traditions that add damage
         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_korouto_military_tradition"),#科鲁托军事传统
            (gt, reg1, 0),                                                                                                                          #success
            (gt, ":attack_agent_horse_no", 0),#rider
            (store_mul, reg1, ":damage", 115),
            (val_div, reg1, 100),
            (val_add, ":damage_caculate", reg1),
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_living_organs"),#活性脏器
            (gt, reg1, 0),                                                                                                                          #success
            (val_add, ":damage_caculate", 10),
         (try_end),

#和血量有关的增伤技能
         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_desperate_counterattack"),#绝境反击
            (gt, reg1, 0),                                                                                                                          #success
            (val_mul, reg1, 10),
            (val_add, reg1, 10),
            (ge, reg1, ":attack_agent_hp_percent"),                                                                               #success
            (store_mul, reg1, ":damage", 6),
            (val_div, reg1, 5),
            (val_add, ":damage_caculate", reg1),
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (gt, ":attack_agent_hp_percent", ":beattacked_agent_hp_percent"),                                  #success
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_blood_arrogance"),#血傲
            (gt, reg1, 0),                                                                                                                          #success
            (val_add, reg1, 2),
            (val_add, ":damage_caculate", reg1),
         (else_try),
            (gt, ":damage", 0),
            (lt, ":attack_agent_hp_percent", ":beattacked_agent_hp_percent"),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_blood_jealousy"),#血妒
            (gt, reg1, 0),                                                                                                                          #success
            (val_add, reg1, 2),
            (val_add, ":damage_caculate", reg1),
         (try_end),

#related to shield block
         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_get_state_timer", ":beattacked_agent_no", "itm_state_lose_balance"),#失去平衡
            (gt, reg1, 0),
            (store_mul, reg1, ":damage", 3),
            (val_div, reg1, 10),
            (val_add, ":damage_caculate", reg1),#伤害提高30%
            (try_begin),
               (ge, ":damage_caculate", 20),
               (agent_set_animation, ":beattacked_agent_no", "anim_shield_against_bechase_2"),#击倒
            (else_try),
               (gt, ":damage_caculate", 10),
               (agent_set_animation, ":beattacked_agent_no", "anim_shield_against_bechase_1"),#踉跄
            (try_end),
         (try_end),

#skills related to percentile hp
         (try_begin),
            (gt, ":damage", 0),
            (lt, ":beattacked_agent_hp_percent", 40),                                                                            #success
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_five_element_quenching_body"),#五相淬体
            (gt, reg1, 0),                                                                                                                          #success
            (store_mul, reg1, ":damage", 4),
            (val_div, reg1, 10),
            (val_add, ":damage_caculate", reg1),
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_blood_intoxication"),#血醉
            (gt, reg1, 0),                                                                                                                           #success
            (call_script, "script_get_state_count", ":attack_agent_no", "itm_state_bleeding"),#流血
            (gt, reg1, 0),                                                                                                                          #success
            (val_add, ":damage_caculate", reg1),
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_get_state_timer", ":attack_agent_no", "itm_state_encouraged"),#昂扬
            (gt, reg1, 0),                                                                                                                           #success
            (store_mul, ":value_no", ":damage", 15),
            (val_div, ":value_no", 100),
            (val_add, ":damage_caculate", ":value_no"),
         (try_end),
         (try_begin),
            (gt, ":damage", 0),
            (call_script, "script_get_state_timer", ":attack_agent_no", "itm_state_generous_death"),#背水一战
            (gt, reg1, 0),                                                                                                                           #success
            (store_mul, ":value_no", ":damage", 25),
            (val_div, ":value_no", 100),
            (val_add, ":damage_caculate", ":value_no"),
         (try_end),

##########饰物
            (try_begin),
               (gt, ":weapon_type_no", 0),
               (neq, ":weapon_type_no", itp_type_bow),#近战
               (neq, ":weapon_type_no", itp_type_crossbow),
               (neq, ":weapon_type_no", itp_type_thrown),
               (neq, ":weapon_type_no", itp_type_pistol),
               (neq, ":weapon_type_no", itp_type_musket),
               (lt, ":attack_agent_horse_no", 0),#步战
               (call_script, "script_check_accessorise_equipped", ":attack_troop_no", "itm_mark_of_scars"),#伤痕印记
               (gt, reg1, 0),   
               (val_add, ":damage_caculate", 10),
            (try_end),

##_____________________________________________________________________减伤部分______________________________________________________________________

         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (eq, ":beattacked_race_no", tf_zombie),#僵尸
            (store_character_level, ":value_no", ":beattacked_troop_no"),#等级除以3的减伤。
            (val_div, ":value_no", 3),
            (val_sub, ":damage_caculate", ":value_no"),
         (try_end),
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (eq, ":beattacked_race_no", tf_skeleton),#骷髅
            (store_div, ":value_no", ":weapon_weight_count", 10),#2.5千克武器攻击无影响，每增减0.1千克，伤害增减1，最多增加20。
            (val_sub, ":value_no", 25),
            (try_begin),
               (gt, ":value_no", 20),
               (assign, ":value_no", 20),
            (try_end),
            (val_add, ":damage_caculate", ":value_no"),
         (try_end),

#skills related to percentile hp
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_desperate_defense"),#绝境防御
            (gt, reg1, 0),                                                                                                                          #success
            (val_mul, reg1, 10),
            (val_add, reg1, 10),
            (ge, reg1, ":beattacked_agent_hp_percent"),                                                                               #success
            (store_div, reg1, ":damage", 5),
            (val_sub, ":damage_caculate", reg1),
         (try_end),

#passive skill stoical, ironflesh decrease damage
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (this_or_next|eq, ":weapon_type_no", itp_type_one_handed_wpn),
            (this_or_next|eq, ":weapon_type_no", itp_type_two_handed_wpn),
            (eq, ":weapon_type_no", itp_type_polearm),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_stoical"),#坚忍
            (gt, reg1, 0),                                                                                                                            #success
            (assign, ":stoical_count", reg1),

            (store_skill_level, ":npc_skl", skl_ironflesh, ":beattacked_troop_no"),
            (store_sub, ":stoical_count", 6, ":stoical_count"),
            (store_div, ":stoical_count", ":npc_skl", ":stoical_count"),
            (store_random_in_range, ":npc_skl_1", 0 , ":npc_skl"),
            (val_sub, ":damage_caculate", ":stoical_count"),
            (val_sub, ":damage_caculate", ":npc_skl_1"),#damage-ironflesh/(5,4,3,2)-random(0,ironflesh)
         (try_end),

#passive skill riotchet, athletics decrease damage
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (gt, ":weapon_type_no", 0),
            (this_or_next|eq, ":weapon_type_no", itp_type_bow),
            (this_or_next|eq, ":weapon_type_no", itp_type_crossbow),
            (this_or_next|eq, ":weapon_type_no", itp_type_thrown),
            (this_or_next|eq, ":weapon_type_no", itp_type_pistol),
            (eq, ":weapon_type_no", itp_type_musket),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_ricochet"),#避矢
            (gt, reg1, 0),                                                                                                                            #success
            (assign, ":ricochet_count", reg1),

            (store_skill_level, ":npc_skl", skl_athletics, ":beattacked_troop_no"),
            (store_random_in_range, ":npc_skl_1",0 ,100),
            (val_div, ":npc_skl_1", ":ricochet_count"),
            (try_begin),
               (le, ":npc_skl_1", ":npc_skl"),   #success
               (assign, ":damage_caculate", 0),
               (try_begin),
                  (eq, "$mission_player_agent", ":attack_agent_no"),
                  (display_message, "@跳 弹 ！", 0xFF0000),
               (try_end),
            (else_try),
               (val_sub, ":damage_caculate", ":npc_skl"),#damage-athletics
            (try_end),
         (try_end),

#a few military traditions that reduce hurt
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_papal_military_tradition"),#教皇国军事传统
            (gt, reg1, 0),                                                                                                                          #success
            (agent_is_defender, ":beattacked_agent_no"),#defender party
            (store_div, reg1, ":damage", 5),
            (val_sub, ":damage_caculate", reg1),
         (try_end),
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_longshu_military_tradition"),#龙树军事传统
            (gt, reg1, 0),                                                                                                                          #success
            (store_div, reg1, ":damage", 10),
            (val_sub, ":damage_caculate", reg1),
         (try_end),

#damage controlling passive
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_force_unloading"),#消力
            (gt, reg1, 0),                                                                                                                          #success
            (assign, ":force_unloading_count", reg1),

            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_collapse_force"),#崩劲
            (this_or_next|le, reg1, 0),                                                                                                                            #success
            (item_has_property, ":weapon_no", itp_unbalanced),

            (val_mul, ":force_unloading_count", 5),
            (store_mul, reg1, ":damage", ":force_unloading_count"),
            (val_div, reg1, 100),
            (val_sub, ":damage_caculate", reg1),
         (try_end),

#伤害抑制的被动技能
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_damage_management"),#损伤管理
            (gt, reg1, 0),                                                                                                                          #success

            (store_skill_level, ":npc_skl", skl_weapon_master, ":attack_troop_no"),
            (val_mul, ":npc_skl", 2),
            (store_sub,":npc_skl",  40, ":npc_skl"),
            (gt, ":damage", ":npc_skl"),                                                                                                   #success

            (val_mul, reg1, 3),
            (val_sub, ":damage_caculate", reg1),
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_get_state_timer", ":beattacked_agent_no", "itm_state_blurs"),#状态：虚影化（幽灵）
            (ge, reg1, 1),                                                                                                                         #success
            (item_get_max_ammo, ":timer_threshold", "itm_state_blurs"),#阈值
            (try_begin),
               (ge, reg1, ":timer_threshold"),
               (assign, ":damage_caculate", 0),#虚影化免疫物理伤害
            (else_try),
               (agent_set_animation, ":beattacked_agent_no", "anim_fantom_withdraw"),#非虚影化则受击后撤
            (try_end),
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_get_state_timer", ":beattacked_agent_no", "itm_passive_blood_armor"),#血衣
            (ge, reg1, 1),                                                                                                                         #success
            (assign, ":value_no", reg1),

            (call_script, "script_get_state_count", ":beattacked_agent_no", "itm_state_bleeding"),#流血
            (gt, reg1, 0),                                                                                                                          #success
            (val_sub, ":value_no", 1),
            (val_mul, ":value_no", 3),
            (store_sub, ":value_no", 35, ":value_no"),
            (gt, reg1, ":value_no"),                                                                                                          #success

            (val_mul, ":damage_caculate", 3),
            (val_div, ":damage_caculate", 10),#当流血值超过（35-3×血衣技能等级）时，减伤70%
         (try_end),

         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_get_state_count", ":attack_agent_no", "itm_state_fighting_spirit"),#无畏
            (gt, reg1, 0),                                                                                                                           #success
            (store_mul, ":value_no", ":damage", 15),
            (val_div, ":value_no", 100),
            (val_sub, ":damage_caculate", ":value_no"),
         (try_end),
         (try_begin),
            (gt, ":damage", 0),
            (gt, ":damage_caculate", 0),
            (call_script, "script_get_state_count", ":attack_agent_no", "itm_state_war_anger"),#血脉偾张
            (gt, reg1, 0),                                                                                                                           #success
            (store_mul, ":value_no", ":damage", 25),
            (val_div, ":value_no", 100),
            (val_sub, ":damage_caculate", ":value_no"),
         (try_end),
##_____________________________________________________________________特殊技能______________________________________________________________________

#保底伤害
         (try_begin),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_obsession_blow"),#被动：执念一击
            (gt, reg1, 0),                                                                                                                          #success
            (assign, ":obsession_blow_count", reg1),
            (lt, ":damage_caculate", ":obsession_blow_count"),                                                                                                   #success
            (assign, ":damage_caculate", ":obsession_blow_count"),
         (try_end),

         (try_begin),
            (le, ":damage_caculate", 0),
            (call_script, "script_get_state_timer", ":attack_agent_no", "itm_state_blurs"),#状态：虚影化（幽灵）
            (gt, reg1, 0),             
            (assign, ":damage_caculate", 2),#幽灵穿伤
         (try_end),

#特殊任务技能
         (try_begin),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_guess_seven_game"),#猜七游戏
            (gt, reg1, 0),                                                                                                                          #success
            (store_random_in_range, ":count_no", 1, 8), 
            (try_begin),
               (eq, ":count_no", 1),
               (val_mul, ":damage_caculate", 2),
            (else_try),
               (eq, ":count_no", 2),
               (assign, ":damage_caculate", 0),
            (else_try),
               (eq, ":count_no", 3),
               (val_div, ":damage_caculate", 7),
               (agent_deliver_damage_to_agent, ":beattacked_agent_no", ":attack_agent_no", ":damage_caculate"),
               (assign, ":damage_caculate", 0),
            (else_try),
               (eq, ":count_no", 4),
               (le, ":attack_agent_horse_no", 0),
               (le, ":beattacked_agent_horse_no", 0),#both footman
               (agent_get_position, pos1, ":attack_agent_no"),
               (agent_get_position, pos2, ":beattacked_agent_horse_no"),
               (agent_set_position, ":attack_agent_no", pos2),
               (agent_set_position, ":beattacked_agent_horse_no", pos1),
            (else_try),
               (eq, ":count_no", 5),
               (store_agent_hit_points, ":beattacked_agent_hp", ":beattacked_agent_no", 1),
               (val_div, ":beattacked_agent_hp", 7),
               (val_add, ":damage_caculate", ":beattacked_agent_hp"),
            (try_end),
         (try_end),
##_____________________________________________________________________结束阶段______________________________________________________________________

         (try_begin),
            (gt, ":damage_caculate", 10),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_crazy_bloodthirsty"),#癫血客
            (gt, reg1, 0),                                                                                                                          #success
            (val_add, ":attack_agent_hp_percent", 2),
            (try_begin),
              (gt, ":attack_agent_hp_percent", 100),
              (assign, ":attack_agent_hp_percent", 100),
            (try_end),
            (agent_set_hit_points, ":attack_agent_no", ":attack_agent_hp_percent", 0),#砍人回血2%
         (try_end),

         (try_begin),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_bloodswallower"),#吞血客
            (gt, reg1, 0),                                                                                                                          #success
            (assign, ":bloodswallower_count", reg1),

            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_blood_atresia"),#血液闭锁
            (le, reg1, 0),                                                                                                                          #success
            (store_sub, ":bloodswallower_count", 8, ":bloodswallower_count"),
            (store_div, ":bloodswallower_count", ":damage_caculate", ":bloodswallower_count"),
            (gt, ":bloodswallower_count", 0),
            (store_agent_hit_points, ":attack_agent_hp", ":attack_agent_no", 1),
            (val_add, ":attack_agent_hp", ":bloodswallower_count"),
            (agent_set_hit_points, ":attack_agent_no", ":attack_agent_hp", 1),
         (try_end),

         (try_begin),
            (gt, ":damage_caculate", 0),
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_blood_addition"),#添血
            (gt, reg1, 0),                                                                                                                          #success

            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_blood_atresia"),#血液闭锁
            (le, reg1, 0),                                                                                                                          #success
            (call_script, "script_restrain_state", ":attack_agent_no", "itm_state_bleeding", 2),#减少两点流血值
         (try_end),

         (try_begin),
            (gt, ":damage_caculate", 0),
            (call_script, "script_get_state_count", ":attack_agent_no", "itm_state_blood_burst"),#血潮汹涌
            (gt, reg1, 3),                                                                                                                          #success
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_blood_attack"),#血发
            (gt, reg1, 0),                                                                                                                          #success
            (call_script, "script_restrain_state_full", ":attack_agent_no", "itm_state_blood_burst", 1),#减少一层血潮汹涌
            (call_script, "script_proceed_state", ":attack_agent_no", "itm_state_generous_death", 10),#背水一战
         (try_end),
         (try_begin),
            (gt, ":damage_caculate", 0),
            (call_script, "script_get_state_count", ":beattacked_agent_no", "itm_state_blood_burst"),#血潮汹涌
            (gt, reg1, 3),                                                                                                                          #success
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_blood_defend"),#血守
            (gt, reg1, 0),                                                                                                                          #success
            (call_script, "script_restrain_state_full", ":beattacked_agent_no", "itm_state_blood_burst", 1),#减少一层血潮汹涌
            (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_war_anger", 10),#血脉偾张
         (try_end),

         (try_begin),
            (gt, ":attack_agent_hp_percent", 0),#以防血潮汹涌叠满九层时反复判伤导致卡退
            (call_script, "script_check_agent_passive_skill", ":attack_agent_no", "itm_passive_blood_motivation"),#励血
            (gt, reg1, 0),                                                                                                                          #success
            (store_mul, ":value_no", reg1, 5),
            (val_add, ":value_no", ":damage_caculate"),
            (this_or_next|ge, ":value_no", 65),#造成的伤害不小于于65-5×励血等级或者血量低于30%
            (lt, ":attack_agent_hp_percent", 30),                                                                               #success
            (call_script, "script_get_state_count", ":attack_agent_no", "itm_state_blood_burst"),#血潮汹涌
            (lt, reg1, 8),                                                                                                                          #以免自爆
            (call_script, "script_proceed_state", ":attack_agent_no", "itm_state_blood_burst", 1),#增加一层血潮汹涌
         (try_end),

         (try_begin),
            (gt, ":beattacked_agent_hp_percent", 0),#以防血潮汹涌叠满九层时反复判伤导致卡退
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_blood_boil"),#沸血
            (gt, reg1, 0),                                                                                                                          #success
            (store_mul, ":value_no", reg1, 5),
            (val_add, ":value_no", ":damage_caculate"),
            (this_or_next|ge, ":value_no", 45),#受到的伤害不小于于45-5×沸血等级或者血量低于40%
            (lt, ":beattacked_agent_hp_percent", 40),                                                                               #success
            (call_script, "script_get_state_count", ":beattacked_agent_no", "itm_state_blood_burst"),#血潮汹涌
            (lt, reg1, 8),                                                                                                                          #以免自爆
            (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_blood_burst", 1),#增加一层血潮汹涌
         (try_end),

         (try_begin),
            (lt, ":damage_caculate", 0),
            (assign, ":damage_caculate", 0),
         (try_end),
         (set_trigger_result, ":damage_caculate"),

         #boss血条
         (try_begin),
            (this_or_next|eq, ":beattacked_agent_no", "$mission_boss_1"),
            (this_or_next|eq, ":beattacked_agent_no", "$mission_boss_2"),
            (eq, ":beattacked_agent_no", "$mission_boss_3"),
            (start_presentation, "prsnt_total_battle_interface"),
         (try_end),
         ]),


#击倒阶段（复活专用）
      (ti_on_agent_knocked_down, 0, 0, [], #触发器12
        [
         (store_trigger_param, ":beattacked_agent_no", 1),
         (call_script, "script_get_state_count", ":beattacked_agent_no", "itm_state_rebirth"),#回生
         (gt, reg1, 0),
         (assign, ":skill_count", reg1),
         (agent_set_hit_points, ":beattacked_agent_no", 70, 0),
         (agent_get_troop_id, ":beattacked_troop_no", ":beattacked_agent_no"),
         (troop_get_type, ":beattacked_race_no", ":beattacked_troop_no"),#种族
         (try_begin),
            (eq, ":beattacked_race_no", tf_skeleton),#骷髅
            (agent_set_animation, ":beattacked_agent_no", "anim_active_skeleton_rebirth_2", 0),#爬起动作
            (agent_play_sound, ":beattacked_agent_no", "snd_break_ground"),
         (try_end),
         (call_script, "script_restrain_state_full", ":beattacked_agent_no", "itm_state_rebirth", 1),#减少一层回生
         (val_sub, ":skill_count", 1),
         (le, ":skill_count", 0),
         (agent_set_no_death_knock_down_only, ":beattacked_agent_no", 0),#回生效果消失
      ]),

#击倒阶段
      (ti_on_agent_killed_or_wounded, 0, 0, [],  #触发器13
        [  
         (store_trigger_param_1, ":beattacked_agent_no"),
#         (store_trigger_param_2, ":attack_agent_no"),
         (store_trigger_param_3, ":wounded_or_dead"),#0 is killed, 1 is wounded

         (try_begin),
            (eq, ":wounded_or_dead", 0),#死亡
            (call_script, "script_get_state_count", ":beattacked_agent_no", "itm_state_blood_burst"),#血潮汹涌
            (gt, reg1, 0),                                                                                                                          #success
            (try_begin),
               (ge, reg1, 9),
               (assign, ":item_no", "itm_blood_explosion"),#大于等于九层即为血爆
            (else_try),
               (assign, ":item_no", "itm_blood_overflow"),#血溢
            (try_end),

            (agent_get_position, pos1, ":beattacked_agent_no"),
            (set_spawn_position, pos1),
            (spawn_item, ":item_no", 0, 3),
            (assign, ":cur_instance", reg0),
            (scene_prop_set_slot, ":cur_instance", slot_instance_item, ":item_no"),
            (prop_instance_deform_in_range, ":cur_instance", 0, 110, 3100),
            (call_script, "script_mission_create_timer", -1, ":cur_instance", 300, 1),#计时器
         (try_end),

         (try_begin),
            (call_script, "script_check_agent_passive_skill", ":beattacked_agent_no", "itm_passive_resentment"),#积怨
            (gt, reg1, 0),
            (assign, ":level_no", reg1),
            (agent_get_bone_position, pos5, ":beattacked_agent_no", hb_thorax, 1),#胸部
            (agent_get_position, pos6, ":beattacked_agent_no"),
            (call_script, "script_pos_copy_rotation_from_pos", pos5, pos6),#复制旋转角
            (try_begin),
               (agent_get_slot, ":target_agent_no", ":beattacked_agent_no", slot_ai_target),
               (ge, ":target_agent_no", 0),
               (try_for_range, ":count_no", 0, ":level_no"),
                  (copy_position, pos1, pos5),
                  (store_random_in_range, ":cur_x", -50, 50),
                  (store_random_in_range, ":cur_y", -50, 50),
                  (store_random_in_range, ":cur_z", -50, 50),
                  (position_move_x, pos1, ":cur_x"),
                  (position_move_y, pos1, ":cur_y"),
                  (position_move_z, pos1, ":cur_z"),
                  (store_mul, ":bone_no", ":count_no", 2),
                  (agent_get_bone_position, pos2, ":target_agent_no", ":bone_no", 1),
                  (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
                  (add_missile, ":beattacked_agent_no", pos1, 1000, "itm_spectre", 0, "itm_spectre", 0),
               (try_end),
            (else_try),
               (try_for_range, reg1, 0, ":level_no"),
                  (copy_position, pos1, pos5),
                  (store_random_in_range, ":cur_x", -50, 50),
                  (store_random_in_range, ":cur_y", -50, 50),
                  (store_random_in_range, ":cur_z", -50, 50),
                  (position_move_x, pos1, ":cur_x"),
                  (position_move_y, pos1, ":cur_y"),
                  (position_move_z, pos1, ":cur_z"),
                  (copy_position, pos2, pos1),#向前射击
                  (position_move_y, pos2, 10),
                  (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
                  (add_missile, ":beattacked_agent_no", pos1, 1000, "itm_spectre", 0, "itm_spectre", 0),
               (try_end),
            (try_end),

         (try_end),
        ]),



############主动技能active skills###################
      (0, 0, 0, [ #触发器14
         (this_or_next|key_clicked, key_1),#按下了键
         (this_or_next|key_clicked, key_2),
         (this_or_next|key_clicked, key_3),
         (this_or_next|key_clicked, key_4),
         (this_or_next|key_clicked, key_5),
         (key_clicked, key_6),
         (ge, "$mission_player_agent", 0)],                      #玩家主动技能
      [
         (assign, ":active_skill_no", -1),
         (try_begin),
            (key_clicked, key_1),
            (neg|agent_slot_ge, "$mission_player_agent", slot_agent_activiting_skill, "itm_active_skills_begin"),
            (agent_get_slot, ":active_skill_no", "$mission_player_agent", slot_agent_active_skill_1),
         (else_try),
            (key_clicked, key_2),
            (neg|agent_slot_ge, "$mission_player_agent", slot_agent_activiting_skill, "itm_active_skills_begin"),
            (agent_get_slot, ":active_skill_no", "$mission_player_agent", slot_agent_active_skill_2),
         (else_try),
            (key_clicked, key_3),
            (neg|agent_slot_ge, "$mission_player_agent", slot_agent_activiting_skill, "itm_active_skills_begin"),
            (agent_get_slot, ":active_skill_no", "$mission_player_agent", slot_agent_active_skill_3),
         (else_try),
            (key_clicked, key_4),
            (neg|agent_slot_ge, "$mission_player_agent", slot_agent_activiting_skill, "itm_active_skills_begin"),
            (agent_get_slot, ":active_skill_no", "$mission_player_agent", slot_agent_active_skill_4),
         (else_try),
            (key_clicked, key_5),
            (neg|agent_slot_ge, "$mission_player_agent", slot_agent_activiting_skill, "itm_active_skills_begin"),
            (agent_get_slot, ":active_skill_no", "$mission_player_agent", slot_agent_active_skill_5),
         (else_try),
            (key_clicked, key_6),
            (neg|agent_slot_ge, "$mission_player_agent", slot_agent_activiting_skill, "itm_active_skills_begin"),
            (agent_get_slot, ":active_skill_no", "$mission_player_agent", slot_agent_active_skill_6),
         (try_end),
         (gt, ":active_skill_no", 0),#获取使用的技能
         (try_begin),
            (item_has_property, ":active_skill_no", itp_martial_art),#骑技
            (item_has_property, ":active_skill_no", itp_riding_skill),
            (call_script, "script_cf_riding_skill_technique", "$mission_player_agent", ":active_skill_no"),
         (else_try),
            (item_has_property, ":active_skill_no", itp_martial_art),#投技
            (item_has_property, ":active_skill_no", itp_grab_skill),
            (call_script, "script_cf_grab_skill_technique", "$mission_player_agent", ":active_skill_no"),
         (else_try),
            (item_has_property, ":active_skill_no", itp_martial_art),#武技
            (neg|item_has_property, ":active_skill_no", itp_riding_skill),
            (call_script, "script_cf_close_combat_technique", "$mission_player_agent", ":active_skill_no"),
         (else_try),
            (item_has_property, ":active_skill_no", itp_sorcery),#术法
            (call_script, "script_cf_sorcery_chant_technique", "$mission_player_agent", ":active_skill_no"),
         (try_end),
         ]),

#技能随时触发器（用于武技判伤和骨骼拼接）
      (0, 0, 0, [], #触发器15
      [
         (try_for_agents, ":agent_no"),
            (agent_is_alive,  ":agent_no"),

            (try_begin),
(eq, 0, 1),
               (agent_slot_ge, ":agent_no", slot_agent_sepcial_effect_num, 1),#正在使用拼接特效件
               (try_for_range, ":count_no", 0, 3),#骨骼拼接
                  (store_add, ":slot_no", slot_agent_prop_using_1, ":count_no"),
                  (agent_get_slot, ":instance_no", ":agent_no", ":slot_no"),
                  (store_div, ":bone_no", ":instance_no", 10000),
                  (gt, ":bone_no", 0),#召唤物存在且需要拼接
                  (val_sub, ":bone_no", 1),
                  (val_mod, ":instance_no", 10000),#召唤物agent ID
                  (prop_instance_is_valid, ":instance_no"),#召唤物还存在
                  (agent_get_bone_position, pos1, ":agent_no", ":bone_no", 1),#召唤者的目标骨骼位置
                  (prop_instance_set_position, ":instance_no", pos1),
               (try_end),

               (try_for_range, ":count_no", 0, 5),#骨骼拼接
                  (store_add, ":slot_no", slot_agent_creature_1, ":count_no"),
                  (agent_get_slot, ":creature_agent_count", ":agent_no", ":slot_no"),
                  (store_div, ":bone_no", ":creature_agent_count", 10000),
                  (gt, ":bone_no", 0),#召唤物存在且需要拼接
                  (store_mod, ":target_bone_no", ":bone_no", 100),#召唤者的目标骨骼
                  (val_sub, ":target_bone_no", 1),
                  (val_div, ":bone_no", 100),#召唤物的对应骨骼
                  (val_sub, ":bone_no", 1),
                  (val_mod, ":creature_agent_count", 10000),#召唤物agent ID

                  (agent_get_bone_position, pos1, ":agent_no", ":target_bone_no", 1),#召唤者的目标位置
                  (agent_get_position, pos3, ":creature_agent_count"),#召唤物位置，之后设置的也只能是这个
                  (position_copy_rotation, pos3, pos1),
                  (agent_set_position, ":creature_agent_count", pos3),
                  (agent_get_bone_position, pos2, ":creature_agent_count", ":bone_no", 1),#召唤物对应骨骼的位置
                  (position_get_x, ":cur_x_2", pos2),
                  (position_get_y, ":cur_y_2", pos2),
                  (position_get_z, ":cur_z_2", pos2),
                  (position_get_x, ":cur_x_3", pos3),
                  (position_get_y, ":cur_y_3", pos3),
                  (position_get_z, ":cur_z_3", pos3),
                  (val_sub, ":cur_x_3", ":cur_x_2"),
                  (val_sub, ":cur_y_3", ":cur_y_2"),
                  (val_sub, ":cur_z_3", ":cur_z_2"),
                  (position_get_x, ":cur_x_1", pos1),
                  (position_get_y, ":cur_y_1", pos1),
                  (position_get_z, ":cur_z_1", pos1),
                  (val_add, ":cur_x_3", ":cur_x_1"),
                  (val_add, ":cur_y_3", ":cur_y_1"),
                  (val_add, ":cur_z_3", ":cur_z_1"),
                  (position_set_x, pos3, ":cur_x_3"),
                  (position_set_y, pos3, ":cur_y_3"),
                  (position_set_z, pos3, ":cur_z_3"),
                  (agent_set_position, ":creature_agent_count", pos3),
               (try_end),
            (try_end),

            (agent_get_slot, ":timer_count", ":agent_no", slot_agent_skill_timer),
            (gt, ":timer_count", 0),                                                                               #正在使用主动技能
            (lt, ":timer_count", 1000),                                                                           #还能再次判定
            (agent_get_slot, ":active_skill_no", ":agent_no", slot_agent_activiting_skill),#获取正在使用的技能
            (is_between, ":active_skill_no", "itm_active_skills_begin", "itm_active_skills_end"),
#判伤达到最后一个检查点后，技能设置为0，不再判定，节省算力。但计时器（下一个触发器）还是会继续运行，作为技能后摇。
            (item_has_property, ":active_skill_no", itp_martial_art),#武技
            (item_has_property, ":active_skill_no", itp_damage_type),#通用的造成伤害型
            (call_script, "script_cf_AoM_active_weapon_hit", ":timer_count", ":active_skill_no", ":agent_no"),#判伤，其原理为检测武器骨骼所在位置并给其穿过的目标施加伤害。
         (try_end),
         ]),

#技能0.1秒计时器（用于处理前后摇、读条等）
#与弹反检测
      (0.1, 0, 0, [], #触发器16
      [
         (try_for_agents, ":agent_no"),
            (agent_is_alive,  ":agent_no"),

            (try_begin),
               (agent_is_human,  ":agent_no"),
               (agent_get_defend_action, ":if_strick", ":agent_no"),#弹反
               (eq, ":if_strick", 2),
               (agent_get_slot, ":blocking_count", ":agent_no", slot_agent_blocking),
               (val_add, ":blocking_count", 1),
               (agent_set_slot, ":agent_no", slot_agent_blocking, ":blocking_count"),#检测到举盾就每0.1秒加1，在盾牌触发器中检测该slot小于指定值，就判定为“格挡及时”。
            (else_try),
               (agent_is_human,  ":agent_no"),
               (agent_set_slot, ":agent_no", slot_agent_blocking, 0),
            (try_end),

            (agent_get_slot, ":timer_count", ":agent_no", slot_agent_skill_timer),
            (gt, ":timer_count", 0),                                                                               #正在使用主动技能

#timer_count进行了分层，如果在0到1000（100秒）之间，就是真正的随时间推进的动作（武技和施法的动作）；如果在1000到10000之间，则是武技造成了一次伤害后，防止这个0.1秒重复触发设置的限制；如果大于10000秒，则是咏唱的倒计时或者投技的前摇，到10000时就算咏唱完成。
            (try_begin),
               (eq, ":timer_count", 10000),#咏唱完成，进入术法效应阶段
               (agent_is_human,  ":agent_no"),
               (agent_get_slot, ":active_skill_no", ":agent_no", slot_agent_activiting_skill),
               (gt, ":active_skill_no", 0),
               (try_begin),
                  (item_has_property, ":active_skill_no", itp_sorcery),#以防万一，检测是否为术法或者投技
                  (call_script, "script_AoM_active_sorcery_result", ":active_skill_no", ":agent_no"),
               (else_try),
                  (item_has_property, ":active_skill_no", itp_grab_skill),
                  (call_script, "script_cf_AoM_active_grab_skill_success", ":active_skill_no", ":agent_no"),
               (try_end),
               (item_get_max_ammo, ":timer_count", ":active_skill_no"),#效应阶段的计时，相当于后摇
            (else_try),
               (is_between, ":timer_count", 1000, 10000),#伤害类型的武技防止一个时间点多次触发
               (val_mod, ":timer_count", 1000),#武技用，进入下一个0.1秒即可解除对再次判伤的限制。
            (else_try),
               (lt, ":timer_count", 1000),#武技
               (agent_get_slot, ":active_skill_no", ":agent_no", slot_agent_activiting_skill),
               (gt, ":active_skill_no", 0),
               (item_has_property, ":active_skill_no", itp_martial_art),#武技
               (item_has_property, ":active_skill_no", itp_special_type),#特殊类型
               (item_get_max_ammo, ":max_timer", ":active_skill_no"),           #获取技能总时间
               (val_sub, ":max_timer", ":timer_count"),#由于计时从大往小，所以进行处理
               (try_begin),
                  (item_has_property, ":active_skill_no", itp_grab_skill),
                  (call_script, "script_AoM_grab_skill", ":agent_no", ":active_skill_no", ":max_timer"),#投技
               (else_try),
                  (call_script, "script_AoM_special_skill", ":agent_no", ":active_skill_no", ":max_timer"),
               (try_end),
            (try_end),

            (val_sub, ":timer_count", 1),
            (agent_set_slot, ":agent_no", slot_agent_skill_timer, ":timer_count"),
            (lt, ":timer_count", 1),
            (agent_set_slot, ":agent_no", slot_agent_activiting_skill, -1),#清除技能
         (try_end),
         ]),

#全局环境
      (0.01, 0, 0, #触发器17
       [(gt, "$battle_environment", 0),],
       [
         (store_div, ":cur_environment", "$battle_environment", 10000),
         (store_mod, ":timer_count", "$battle_environment", 10000),
         (try_begin),
            (eq, ":cur_environment", "itm_active_warcy_bloodrain"),#唤来血雨的战歌
            (set_fixed_point_multiplier, 100),
            (mission_cam_get_position, pos1),
            (position_move_z, pos1, 300),
            (position_move_y, pos1, 300),
            (particle_system_burst, "psys_blood_rain", pos1),
         (try_end),
         (val_sub, "$battle_environment", 1),#计时

         (le, ":timer_count", 1),
         (assign, "$battle_environment", -1),#结束
       ]),


####################################################状态state#################################################
      (1, 0, 0, [],#1 second timer #触发器18
      [
         (try_for_agents, ":agent_no"),
            (agent_is_alive,  ":agent_no"),

            (try_begin),
               (neq, "$scene_sea_level", 114514),
               (agent_is_human,  ":agent_no"),
               (agent_get_bone_position, pos1, ":agent_no", hb_head, 1),#头
               (set_fixed_point_multiplier, 1000),
               (position_get_z, ":cur_z", pos1),
               (val_div, ":cur_z", 10),
               (lt, ":cur_z", "$scene_sea_level"),
               (assign, ":count_no", 3),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_diving"),#潜泳技艺
               (val_sub, ":count_no",  reg1),
               (call_script, "script_proceed_state", ":agent_no", "itm_state_breath_holding", ":count_no"),#每秒增加三
            (else_try),
               (neq, "$scene_sea_level", 114514),
               (agent_is_human,  ":agent_no"),
               (call_script, "script_get_state_count", ":agent_no", "itm_state_breath_holding"),#闭气
               (gt, reg1, 0),                                                                                                                          #success
               (call_script, "script_restrain_state_full", ":agent_no", "itm_state_breath_holding", 1145141919810),#上浮
            (try_end),

#           (agent_is_human,  ":agent_no"),#include animals
            (agent_get_slot, ":state_count", ":agent_no", slot_agent_state_caculate),#状态
            (gt, ":state_count", 0),
            (try_for_range, ":count_no", 0, "$state_total_number"),
               (store_add, ":slot_no", ":count_no", slot_agent_state_count_1),
               (agent_get_slot, ":timer_count", ":agent_no", ":slot_no"),
               (gt, ":timer_count", 0),

               (store_add, ":state_no", ":count_no", "itm_state_begin"),
               (val_add, ":state_no", 1),                                                  #get state no
               (item_has_property, ":state_no", itp_timing_type),         #计时类型

               (call_script, "script_timer_state_technique", ":agent_no", ":state_no", ":timer_count"),

               (agent_set_slot, ":agent_no", ":slot_no", reg1),
               (le, reg1, 0),                            #该状态归零
               (val_sub, ":state_count", 1),
            (try_end),
            (agent_set_slot, ":agent_no", slot_agent_state_caculate, ":state_count"),
         (try_end),
         ]),

#用于附魔类的状态清除
      (ti_on_item_wielded, 0, 0, #触发器19
       [],
       [
        (store_trigger_param_1, ":agent_no"),
        (agent_get_slot, ":state_no", ":agent_no", slot_agent_enchant),
        (gt, ":state_no", 0),                                     #已有附魔
        (val_mod, ":state_no", 1000),
        (val_add, ":state_no", "itm_state_begin"), #获取现有附魔
        (call_script, "script_get_state_timer", ":agent_no", ":state_no"),
        (gt, reg1, 1),
        (call_script, "script_activate_state", ":agent_no", ":state_no", 1),
       ]),

#离开
      (ti_on_leave_area, 0, 0, [], #触发器20
       [
        (assign, "$g_inventory_allow", 0),#新物品栏恢复默认
       ]),
      (ti_tab_pressed, 0, 0, [], #触发器21
       [
        (assign, "$g_inventory_allow", 0),#新物品栏恢复默认
       ]),
]



AoM_inflitration_triggers = [
      (ti_before_mission_start, 0, 0, [],
      [
       (assign, "$infiltrate_tut", 1),#启动潜行模式
       (assign, "$crouch_mode", 0),#下蹲模式
       (assign, "$infiltrate_alarm_level", 0),#警戒等级
       (assign, "$infiltrate_hiding_level", 0),#隐蔽水平（越高越隐蔽，常规在60上下）
      ]),

      (ti_on_agent_spawn, 0, 0, [],
      [
       (store_trigger_param_1, ":agent_no"),
       (agent_add_relation_with_agent, ":agent_no", "$mission_player_agent", 0),#玩家刷新点一定要靠前，以免敌方刷新时玩家还没刷新，导致报错
      ]),

      (0, 1, ti_once, [],
      [
       (get_player_agent_no, "$mission_player_agent"),
       (try_for_agents, ":agent_no"),
          (agent_is_alive, ":agent_no"),
          (agent_is_human, ":agent_no"),
          (agent_get_entry_no, ":entry_no", ":agent_no"),
          (troop_get_slot, ":type_no", "trp_temp_array_inflitration_sentry", ":entry_no"),#1是固定哨，2是巡逻哨
          (gt, ":type_no", 0),#是敌人
          (agent_set_slot, ":agent_no", slot_agent_standing_guard, ":type_no"),
          (agent_set_slot, ":agent_no", slot_agent_alarmed_level, 0),

          (agent_set_slot, ":agent_no", slot_agent_last_position, ":entry_no"),#用于巡逻
          (agent_set_slot, ":agent_no", slot_agent_target_position, 0),
          (agent_add_relation_with_agent, ":agent_no", "$mission_player_agent", 0),
       (try_end),
      ]),

      (0,0,0,[
       (ge, "$infiltrate_tut", 1),
       (agent_is_alive, "$mission_player_agent"),
       (try_begin),
          (key_clicked, key_z),
          (try_begin),
             (eq, "$crouch_mode", 0),
             (assign, "$crouch_mode", 1),
             (agent_set_speed_modifier, "$mission_player_agent", 40),
             (agent_set_animation, "$mission_player_agent", "anim_stand_to_crouch_new", 0),#蹲下
          (else_try),
             (ge, "$crouch_mode", 1),
             (assign, "$crouch_mode", 0),
             (agent_set_speed_modifier, "$mission_player_agent", 100),
             (agent_set_animation, "$mission_player_agent", "anim_crouch_to_stand_new", 0),#站起
          (try_end),
       (try_end),],
      [
       (ge, "$crouch_mode", 1),
       (try_begin),
          (this_or_next|game_key_is_down, gk_move_forward),
          (this_or_next|game_key_is_down, gk_move_backward),
          (this_or_next|game_key_is_down, gk_move_left),
          (game_key_is_down, gk_move_right),
          (agent_set_animation, "$mission_player_agent", "anim_walk_forward_crouch_new", 0),
       (else_try),
          (agent_set_animation, "$mission_player_agent", "anim_crouch_state_new", 0),
       (try_end),
      ]),

      (1,0,0,[
       (ge, "$infiltrate_tut", 1),
       (try_begin),
          (call_script, "script_cf_agent_caculate_hiding_level", "$mission_player_agent"),#刷新隐蔽等级
          (assign, "$infiltrate_hiding_level", reg1),
          (lt, "$g_film_cam", 1),#动画播放完再刷新
          (neg|is_presentation_active, "prsnt_inventory_new_battle"),#没开物品栏
          (start_presentation, "prsnt_total_battle_interface"),
       (try_end),
       ],
      [
       (agent_get_bone_position, pos54, "$mission_player_agent", hb_thorax, 1),
       (assign, ":alarm_level_count", 0),
       (try_for_agents, ":enemy_no"),
          (neq, ":enemy_no", "$mission_player_agent"),
          (agent_is_alive, ":enemy_no"),
          (agent_is_human, ":enemy_no"),
          (agent_slot_ge, ":enemy_no", slot_agent_standing_guard, 1), #敌人
          (agent_get_position, pos53, ":enemy_no"),

#刷新巡逻目标
          (try_begin),
             (agent_slot_eq, ":enemy_no", slot_agent_standing_guard, 1),#固定哨
             (agent_set_slot, ":enemy_no", slot_agent_target_position, 0),#清空
             (agent_get_slot, ":last_entry", ":enemy_no", slot_agent_last_position),
             (entry_point_get_position, pos52, ":last_entry"),
             (get_distance_between_positions_in_meters, ":position_distance_1", pos53, pos52),
             (gt, ":position_distance_1", 1),                                                             #不在岗位上，就回正，其他情况不需要
             (agent_set_slot, ":enemy_no", slot_agent_target_position, ":last_entry"),
          (else_try),
             (agent_slot_eq, ":enemy_no", slot_agent_standing_guard, 2),#流动哨
             (agent_get_slot, ":target_entry", ":enemy_no", slot_agent_target_position),
             (entry_point_get_position, pos52, ":target_entry"),
             (get_distance_between_positions_in_meters, ":position_distance_1", pos53, pos52),
             (this_or_next|le, ":position_distance_1", 1),                                                             #抵达目的地，需要获取新的巡逻位置
             (eq, ":target_entry", 0),

             (assign, ":distance", 10000),#寻找新的目标entry
             (assign, ":count_no", 0),
             (store_add, ":entry_limit", "$total_patrol_entry", 1),
             (try_for_range, ":entry_no", 1, ":entry_limit"),
                (neq, ":entry_no", ":target_entry"),#现在的不能选
                (agent_get_slot, ":last_entry", ":enemy_no", slot_agent_last_position),
                (neq, ":entry_no", ":last_entry"),#上一个不能选
                (entry_point_get_position, pos52, ":entry_no"),

                (get_distance_between_positions_in_meters, ":distance_count", pos52, pos53),#找一个最近的
                (le, ":distance_count", ":distance"),                                          
                (assign, ":distance", ":distance_count"),    #the nearest point except last point
                (assign, ":count_no", ":entry_no"),
             (try_end),
             (is_between, ":count_no", 1, ":entry_limit"),
             (agent_set_slot, ":enemy_no", slot_agent_target_position, ":count_no"),
             (agent_set_slot, ":enemy_no", slot_agent_last_position, ":target_entry"),
          (try_end),     

#目击判断
          (agent_get_bone_position, pos53, ":enemy_no", hb_head, 1),
          (get_distance_between_positions_in_meters, ":distance", pos54, pos53),#玩家和此人的距离
          (try_begin),
             (agent_slot_ge, ":enemy_no", slot_agent_alarmed_level, 3),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 2),    #警戒等级三的敌人不需要再判断目击，直接就是目击等级2
          (else_try),
             (eq, "$infiltrate_alarm_level", 3),
             (ge, ":distance", 5),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 1),     #玩家正在战斗，其他敌人跑过来看发生了什么，目击等级1
          (else_try),
             (store_div, ":detected_distance", "$infiltrate_hiding_level", 10),
             (store_sub, ":detected_distance", 25, ":detected_distance"),
             (ge, ":distance", ":detected_distance"),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 0),      #距离太远，不需要判断目击
          (else_try),
             (is_between, ":distance", 5, ":detected_distance"),
             (store_random_in_range, ":count_no", "$infiltrate_hiding_level", 200),
             (le, ":count_no", 185),
             (neg|position_is_behind_position, pos54, pos53),#排除背后
             (agent_is_in_line_of_sight, ":enemy_no", pos54),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 1),    #玩家在中距离被看见了，目击等级1
          (else_try),
             (lt, ":distance", 4),
             (lt, "$infiltrate_hiding_level", 30),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 2),     #隐蔽等级太低，近距离直接被发现，目击等级2 
          (else_try),
             (lt, ":distance", 5),
             (store_random_in_range, ":count_no", "$infiltrate_hiding_level", 200),
             (le, ":count_no", 198),
             (neg|position_is_behind_position, pos54, pos53),#排除背后
             (agent_is_in_line_of_sight, ":enemy_no", pos54),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 2),     #玩家在近处被看见了，目击等级2 
          (else_try),
             (agent_set_slot, ":enemy_no", slot_agent_witness_player, 0),
          (try_end),

#疑心设置
#不在警戒等级三且完全没看到玩家时，疑心慢慢减少
          (try_begin),
              (neg|agent_slot_eq, ":enemy_no", slot_agent_alarmed_level, 3),
              (agent_slot_eq, ":enemy_no", slot_agent_witness_player, 0),
              (agent_get_slot, ":suspicious_amount", ":enemy_no", slot_agent_suspicous_amount),  
              (gt, ":suspicious_amount", 0),
              (val_sub, ":suspicious_amount", 1),
              (agent_set_slot, ":enemy_no", slot_agent_suspicous_amount, ":suspicious_amount"),    #need double time to dispel suspicion
          (try_end),

#发现尸体，疑心飙增
#有bug先停用
          (try_begin),
             (eq, 0, 1),
             (neg|agent_slot_eq, ":enemy_no", slot_agent_alarmed_level, 3),  
             (set_fixed_point_multiplier, 1000),
             (agent_get_position, ":enemy_no", pos1),
             (try_for_agents, ":dead_agent_no", pos1, 3000),#三米
                (neg|agent_is_alive, ":dead_agent_no"),
                (agent_set_slot, ":enemy_no", slot_agent_suspicous_amount, 1145141919810),    
             (try_end),
          (try_end),

#警戒设置
#设置警戒等级（根据目击判断）
          (init_position, pos55),
          (try_begin),
              (store_agent_hit_points, ":enemy_hp", ":enemy_no", 0),     #AI被攻击，立马进入警戒三
              (lt, ":enemy_hp", 100),
              (agent_set_slot, ":enemy_no", slot_agent_alarmed_level, 3),
              (agent_get_position, pos55, "$mission_player_agent"),                    #the place where player is last vitnessed
          (else_try),
              (agent_slot_eq, ":enemy_no", slot_agent_witness_player, 2),  #五米内目击等级二，暴露
              (le, ":distance", 5),
              (agent_set_slot, ":enemy_no", slot_agent_alarmed_level, 3),
              (agent_get_position, pos55, "$mission_player_agent"),                    #the place where player is last vitnessed
          (else_try),
              (neg|agent_slot_eq, ":enemy_no", slot_agent_alarmed_level, 3),  #疑心等级达到8，进入警戒二
              (agent_get_slot, ":suspicious_amount", ":enemy_no", slot_agent_suspicous_amount),
              (gt, ":suspicious_amount", 6),
              (agent_set_slot, ":enemy_no", slot_agent_alarmed_level, 2),
              (try_begin),
                  (agent_slot_ge, ":enemy_no", slot_agent_witness_player, 1),
                  (agent_get_position, pos55, "$mission_player_agent"),
              (else_try),
                  (agent_get_position, pos55, ":enemy_no"),
              (try_end),
          (else_try),
              (neg|agent_slot_eq, ":enemy_no", slot_agent_alarmed_level, 3),     #目击等级一（远远地看到），进入警戒一，开始每秒两点积累疑心
              (agent_slot_eq, ":enemy_no", slot_agent_witness_player, 1),
              (agent_set_slot, ":enemy_no", slot_agent_alarmed_level, 1),
              (agent_get_slot, ":suspicious_amount", ":enemy_no", slot_agent_suspicous_amount),  
              (val_add, ":suspicious_amount", 2),
              (agent_set_slot, ":enemy_no", slot_agent_suspicous_amount, ":suspicious_amount"),
              (agent_get_position, pos55, "$mission_player_agent"),                    #the place where player is last vitnessed
          (else_try),
              (neg|agent_slot_eq, ":enemy_no", slot_agent_alarmed_level, 3),     #不在警戒等级三且完全没看到玩家时，疑心消除后，警戒解除
              (agent_slot_eq, ":enemy_no", slot_agent_witness_player, 0),
              (le, ":suspicious_amount", 0),
              (agent_set_slot, ":enemy_no", slot_agent_alarmed_level, 0),
              (agent_set_slot, ":enemy_no", slot_agent_suspicous_amount, 0),
          (try_end),

#行动部分
#不同警戒等级，守卫状态的变化（移速和姿态等）
          (agent_get_slot, ":alarmed_level", ":enemy_no", slot_agent_alarmed_level),
          (try_begin),
               (eq, ":alarmed_level", 3),                                  #自身警戒等级达到三，全力追击，所有守卫都被惊动。
               (agent_clear_scripted_mode, ":enemy_no"),
               (agent_set_speed_modifier, ":enemy_no", 100),
               (agent_add_relation_with_agent, ":enemy_no", "$mission_player_agent", -1),
               (agent_set_is_alarmed, ":enemy_no", 1),
               (agent_set_scripted_destination, ":enemy_no", pos55, 0, 1),
          (else_try),
               (eq, ":alarmed_level", 2),      #自身警戒等级二（惊动），前往最后目击玩家处调查
               (agent_set_speed_modifier, ":enemy_no", 50),
               (agent_set_scripted_destination_no_attack, ":enemy_no", pos55, 0, 1),
               (agent_add_relation_with_agent, ":enemy_no", "$mission_player_agent", -1),
          (else_try),
               (lt, ":alarmed_level", 2),      #自身警戒等级不到二（未被惊动），但是有其他人在和玩家战斗，前往玩家所在处探查
               (eq, "$infiltrate_alarm_level", 3),
               (agent_set_slot, ":enemy_no", slot_agent_alarmed_level, 2),
               (agent_set_slot, ":enemy_no", slot_agent_suspicous_amount, 7),
          (else_try),
               (eq, ":alarmed_level", 1),      #自身警戒等级一（起疑），停止巡逻，看向玩家处
               (agent_set_speed_modifier, ":enemy_no", 1),
               (agent_add_relation_with_agent, ":enemy_no", "$mission_player_agent", -1),
          (else_try),
               (eq, ":alarmed_level", 0),      #消除警戒，重新巡逻
               (agent_slot_eq, ":enemy_no", slot_agent_standing_guard, 2),#巡逻哨
               (agent_set_speed_modifier, ":enemy_no", 30),
               (agent_get_slot, ":target_entry", ":enemy_no", slot_agent_target_position),
               (entry_point_get_position, pos52, ":target_entry"),
               (agent_set_scripted_destination_no_attack, ":enemy_no", pos52, 0, 1),
               (agent_add_relation_with_agent, ":enemy_no", "$mission_player_agent", 0),
          (else_try),
               (eq, ":alarmed_level", 0),      #消除警戒，重新回到岗位
               (agent_slot_eq, ":enemy_no", slot_agent_standing_guard, 1),#固定哨
               (agent_get_slot, ":target_entry", ":enemy_no", slot_agent_target_position),
               (gt, ":target_entry", 0),
               (entry_point_get_position, pos52, ":target_entry"),#回正
               (agent_set_scripted_destination_no_attack, ":enemy_no", pos52, 0, 1),
               (agent_add_relation_with_agent, ":enemy_no", "$mission_player_agent", 0),
               (agent_set_speed_modifier, ":enemy_no", 30),
               (agent_set_is_alarmed, ":enemy_no", 0),
               (agent_set_wielded_item, ":enemy_no", -1),
          (try_end),

#统计部分
#获取最高一个守卫的警戒等级，作为整体的警戒等级。
          (gt, ":alarmed_level", ":alarm_level_count"),
          (assign, ":alarm_level_count", ":alarmed_level"),
       (try_end),

       (try_begin),
          (lt, "$infiltrate_alarm_level", 3),#进入警戒三
          (eq, ":alarm_level_count", 3),
          (display_message, "@暴 露 ！", 0xFF0000),
       (else_try),
          (lt, "$infiltrate_alarm_level", 2),#有人进入警戒二
          (eq, ":alarm_level_count", 2),
          (call_script, "script_check_agent_passive_skill", "$mission_player_agent", "itm_passive_malicious_perception"),#恶意感知
          (gt, reg1, 0),                                                                                                                          #success
          (play_sound, "snd_inflitration_sound_1", pos1),#提示音
          (display_message, "@你 正 在 被 搜 寻 ！", 0xFF0000),
       (else_try),
          (lt, "$infiltrate_alarm_level", 1),#有人进入警戒一
          (eq, ":alarm_level_count", 1),
          (call_script, "script_check_agent_passive_skill", "$mission_player_agent", "itm_passive_malicious_perception"),#恶意感知
          (gt, reg1, 0),                                                                                                                          #success
          (play_sound, "snd_inflitration_sound_1", pos1),#提示音
          (display_message, "@你 被 注 意 到 ！", 0xFF0000),
       (else_try),
          (ge, "$infiltrate_alarm_level", 2),#解除警戒二或者三
          (lt, ":alarm_level_count", 2),
          (call_script, "script_check_agent_passive_skill", "$mission_player_agent", "itm_passive_malicious_perception"),#恶意感知
          (gt, reg1, 0),                                                                                                                          #success
          (play_sound, "snd_inflitration_sound_2", pos1),#提示音
          (display_message, "@搜 寻 停 止 了 。 ", 0x336600),
       (else_try),
          (eq, "$infiltrate_alarm_level", 1),#解除警戒一
          (lt, ":alarm_level_count", 1),
          (call_script, "script_check_agent_passive_skill", "$mission_player_agent", "itm_passive_malicious_perception"),#恶意感知
          (gt, reg1, 0),                                                                                                                          #success
          (play_sound, "snd_inflitration_sound_2", pos1),#提示音
          (display_message, "@疑 心 消 除 了 。 ", 0x336600),
       (try_end),
       (assign, "$infiltrate_alarm_level", ":alarm_level_count"),
      ]),
]


#将所有boss战AI的触发器包汇总到一起，方便快速战斗之类的mt调用。
AoM_boss_triggers_summary = boss_triggers_megalith_berserker + boss_triggers_libra_hitman + boss_triggers_confederation_gladiator_champion + boss_triggers_zela + boss_triggers_restless_soldier



##上面是各种打包好的触发器或者触发器包，下面才是真正的mission template
##some AoM special mission, for example, character window background.
############################################################################################
mission_templates_AoM = [


  (#会战地图
    "sandbox",0,-1,
     "sandbox",
    [
      (0, mtef_visitor_source, af_override_horse, 0, 1, []),
      (1, mtef_visitor_source, af_override_horse, 0, 1, []),
    ],
      [
      common_battle_init_banner,
      (ti_before_mission_start, 0, 0, [],
      [
         (assign, "$g_mission_cam", -1),
         (assign, "$g_sandbox_full", -1),
         (assign, "$g_sandbox_chosse", -1),
         (scene_set_day_time, "$campaign_time"),
      ]),

      (ti_after_mission_start, 0, 0, [],
      [
         (set_fixed_point_multiplier, 100),
         (init_position, pos3),
         (position_set_x, pos3, 0),
         (position_set_y, pos3, 0),
         (position_set_z, pos3, 0),
         (set_spawn_position, pos3),
         (spawn_scene_prop, "spr_sand_box"), #盒子大小
         (spawn_scene_prop, "spr_sandbox_choose_full"),#全局分块的显示
         (assign, "$g_sandbox_full", reg0),
         (scene_prop_set_visibility, "$g_sandbox_full", 0),
         (spawn_scene_prop, "spr_sandbox_choose_red"),#选择某块的显示
         (assign, "$g_sandbox_chosse", reg0),

         (try_for_range, ":count_no", 1, 200),
            (troop_set_slot, "trp_temp_array_new_map_2", ":count_no", 0),#清空，记录任务分块
         (try_end),
         (assign, ":cur_slot", 1),
         (try_for_range, ":count_no", "qst_deliver_message", "qst_quests_end"),#任务分块
            (try_for_range, ":slot_no", 1, 4),
               (call_script, "script_get_quest_zone", ":count_no", ":slot_no"),
               (eq, reg3, "$current_town"),
               (assign, ":cur_x", reg1),
               (assign, ":cur_y", reg2),
               (val_mul, ":cur_x", 1000),
               (val_sub, ":cur_x", 500),
               (val_mul, ":cur_y", 1000),
               (val_sub, ":cur_y", 500),
               (init_position, pos50),
               (position_set_x, pos50, ":cur_x"),
               (position_set_y, pos50, ":cur_y"),#中心点位置
               (set_spawn_position, pos50),
               (spawn_scene_prop, "spr_sandbox_choose_green"),
               (scene_prop_set_visibility, reg0, 0),
               (troop_set_slot, "trp_temp_array_new_map_2", ":cur_slot", reg0),
               (val_add, ":cur_slot", 1),
            (try_end),
         (try_end),

         (assign, ":length_no", 15),
         (val_mul, ":length_no", ":length_no"),
         (val_add, ":length_no", 1),
         (try_for_range, ":count_no", 1, ":length_no"),
            (call_script, "script_change_number_to_coordinate", 15, ":count_no"),
            (assign, ":rank", reg1),#行
            (assign, ":procession", reg2),#列
            (call_script, "script_draw_center_zone", "$current_town", ":rank", ":procession"),#生成建筑
         (try_end),

         (assign, ":cam_x", 7500),
         (assign, ":cam_y", 7500),
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), #生成编队模型
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (ge, ":temp_party_id", 0),
            (party_get_slot, ":cur_x", ":temp_party_id", slot_tool_party_position_x),#获取位置
            (party_get_slot, ":cur_y", ":temp_party_id", slot_tool_party_position_y),
            (call_script, "script_draw_detachment", ":temp_party_id", ":cur_x", ":cur_y"),#生成编队
            (party_count_members_of_type, ":count_no", ":temp_party_id", "trp_player"), #找到玩家在的编队，把视角刷在它上面
            (gt, ":count_no", 0),
            (assign, ":cam_x", ":cur_x"),
            (assign, ":cam_y", ":cur_y"),
            (val_mul, ":cam_x", 1000),
            (val_sub, ":cam_x", 500),
            (val_mul, ":cam_y", 1000),
            (val_sub, ":cam_y", 500), #中心点位置
         (try_end),

         (set_fixed_point_multiplier, 100),
         (init_position, pos4),
         (try_begin),
            (neq, "$campaign_cam_set", 1), #镜头未设置
            (assign, "$campaign_cam_set", 1), 
            (position_set_x, pos4, ":cam_x"),
            (position_set_y, pos4, ":cam_y"),
            (position_set_z, pos4, 500),
            (position_rotate_z, pos4, 90, 1),
            (position_rotate_x, pos4, -30, 1),
            (set_spawn_position, pos4),
            (spawn_scene_prop, "spr_mission_cam"),#摄像机
            (assign, "$g_mission_cam", reg0),
            (scene_prop_set_visibility, "$g_mission_cam", 0),
            (prop_instance_get_position, pos47, "$g_mission_cam"),
            (position_move_y, pos47, -500),
            (prop_instance_set_position, "$g_mission_cam", pos47),
         (else_try),
            (position_set_x, pos4, "$g_sandbox_cam_x"), 
            (position_set_y, pos4, "$g_sandbox_cam_y"),
            (position_set_z, pos4, "$g_sandbox_cam_z"),
            (position_rotate_x, pos4, "$g_sandbox_cam_rotate_x"),
            (position_rotate_z, pos4, "$g_sandbox_cam_rotate_z", 1),
            (set_spawn_position, pos4),
            (spawn_scene_prop, "spr_mission_cam"),#摄像机
            (assign, "$g_mission_cam", reg0),
            (scene_prop_set_visibility, "$g_mission_cam", 0),
         (try_end),

         (start_presentation, "prsnt_center_sandbox_window"),
      ]),

      (ti_on_agent_spawn, 0, 0, [],#隐藏玩家
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),
         (agent_set_visibility, ":agent_no", 0),
         (agent_fade_out, ":agent_no"),
      ]),

      (0, 0, 0,#镜头移动
       [
         (ge, "$g_mission_cam", 0),
         (prop_instance_get_position, pos48, "$g_mission_cam"),
         (mission_cam_set_position, pos48),
         (set_fixed_point_multiplier, 100),
         (position_get_x, "$g_sandbox_cam_x", pos48), #记录镜头位置
         (position_get_y, "$g_sandbox_cam_y", pos48),
         (position_get_z, "$g_sandbox_cam_z", pos48),
         (position_get_rotation_around_x, "$g_sandbox_cam_rotate_x", pos48),
         (position_get_rotation_around_z, "$g_sandbox_cam_rotate_z", pos48),

         (this_or_next|game_key_clicked, gk_move_forward),
         (this_or_next|game_key_is_down, gk_move_forward),
         (this_or_next|game_key_clicked, gk_move_backward),
         (this_or_next|game_key_is_down, gk_move_backward),
         (this_or_next|game_key_clicked, gk_move_left),
         (this_or_next|game_key_is_down, gk_move_left),
         (this_or_next|game_key_clicked, gk_move_right),
         (game_key_is_down, gk_move_right),
       ],
       [
         (prop_instance_get_position, pos47, "$g_mission_cam"),
         (assign, ":move_x", 0),
         (assign, ":move_y", 0),
         (try_begin), #forward
            (this_or_next|game_key_clicked, gk_move_forward),
            (game_key_is_down, gk_move_forward),
            (assign, ":move_y", 10),
         (try_end),
         (try_begin), #backward
            (this_or_next|game_key_clicked, gk_move_backward),
            (game_key_is_down, gk_move_backward),
            (assign, ":move_y", -10),
         (try_end),
         (try_begin), #left
            (this_or_next|game_key_clicked, gk_move_left),
            (game_key_is_down, gk_move_left),
            (assign, ":move_x", -10),
         (try_end),
         (try_begin), #right
            (this_or_next|game_key_clicked, gk_move_right),
            (game_key_is_down, gk_move_right),
            (assign, ":move_x", 10),
         (try_end),
         (position_move_x, pos47, ":move_x"),
         (position_move_y, pos47, ":move_y"),
         (prop_instance_set_position, "$g_mission_cam", pos47),
       ]),

      (0, 0, 0,#唤起菜单
       [
         (key_clicked, key_v),
       ],
       [
         (start_presentation, "prsnt_center_sandbox_window"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
         (presentation_set_duration, 0),
         (finish_mission),
       ]),
    ],
  ),



  (
    "character_window",0,-1,
     "character window background.",
    [
      (0, mtef_visitor_source, af_override_horse, 0, 1, []),
      (1, mtef_visitor_source, af_override_horse, 0, 1, []),
      (2, mtef_visitor_source, af_override_horse, 0, 1, []),
      (3, mtef_visitor_source, af_override_horse, 0, 1, []),
      (4, mtef_visitor_source, af_override_horse, 0, 1, []),
    ],
    AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [],
      [
         (show_object_details_overlay, 0),
#         (start_presentation, "prsnt_character_window"),
         (start_presentation, "prsnt_skill_window"),
      ]),

      (ti_on_agent_spawn, 0, 0, [],
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),

         (try_begin),
            (call_script, "script_player_get_new_inventory_slot", 10),#右手武器
            (gt, reg0, 0),
            (agent_equip_item, ":agent_no", reg0, 1),
            (agent_set_wielded_item, ":agent_no", reg0),
         (try_end),
         (try_begin),
            (call_script, "script_player_get_new_inventory_slot", 13),#左手武器
            (gt, reg0, 0),
            (agent_equip_item, ":agent_no", reg0, 2),
            (agent_set_wielded_item, ":agent_no", reg0),
         (try_end),

         (call_script, "script_player_get_new_inventory_slot", ek_horse),#坐骑
         (try_begin),
            (gt, reg0, 0),
            (assign, ":item_no", reg0),
            (entry_point_get_position, pos1, 5),
            (set_spawn_position, pos1),
            (spawn_horse, ":item_no"),
         (try_end),
      ]),

      (ti_after_mission_start, 0, 0, [],        #cam
      [
         (assign, "$troop_show", -1),
         (entry_point_get_position, pos3, 3),
         (mission_cam_set_mode, 1),   
         (mission_cam_set_position, pos3),    
      ]),
#pos3 is this mission's normal camera position

      (ti_on_agent_spawn, 0, 0, [],#坐骑
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),
         (neg|agent_is_human, ":agent_no"),
         (assign, "$mission_show_horse", ":agent_no"),
      ]),

      (ti_inventory_key_pressed, 0, 0, 
      [
         (set_trigger_result, 0),
      ], []),  

      (ti_tab_pressed, 0, 0,
       [],
       [
         (show_object_details_overlay, 1),
         (finish_mission),
#         (change_screen_map),
       ]),
    ],
  ),


  (
    "troop_window",0,-1,
     "character window background.",
    [
      (0, mtef_visitor_source, af_override_horse, 0, 1, []),
      (1, mtef_visitor_source, af_override_horse, 0, 1, []),
      (2, mtef_visitor_source, af_override_horse, 0, 1, []),
      (3, mtef_visitor_source, af_override_horse, 0, 1, []),
      (4, mtef_visitor_source, af_override_horse, 0, 1, []),
    ],
    AoM_battle_triggers + [
#      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [],
      [
#         (show_object_details_overlay, 0),
         (assign, "$mission_show_horse", -1),
         (start_presentation, "prsnt_troop_window"),
      ]),

      (ti_on_agent_spawn, 0, 0, [],#人物
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (neq, ":troop_no", "trp_player"),
         (assign, "$mission_show_agent", ":agent_no"),

         (assign, ":proficiency_count", 0),
         (assign, ":right_weapon", 0),
         (assign, ":left_weapon", 0),
         (try_for_range, ":count_no", 0, 4),
            (agent_get_item_slot, ":itm_no", ":agent_no", ":count_no"),
            (gt, ":itm_no", 0),
            (item_get_type, ":type_no",":itm_no"),
            (try_begin),
               (try_begin),
                  (eq, ":type_no", itp_type_one_handed_wpn),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_one_handed_weapon),
               (else_try),
                  (eq, ":type_no", itp_type_two_handed_wpn),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_two_handed_weapon),
               (else_try),
                  (eq, ":type_no", itp_type_polearm),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_polearm),
               (else_try),
                  (eq, ":type_no", itp_type_bow),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_archery),
               (else_try),
                  (eq, ":type_no", itp_type_crossbow),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_crossbow),
               (else_try),
                  (eq, ":type_no", itp_type_thrown),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_throwing),
               (else_try),
                  (this_or_next|eq, ":type_no", itp_type_pistol),
                  (eq, ":type_no", itp_type_musket),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_firearm),
               (else_try),
                  (assign, ":proficiency_count_2", 0),
               (try_end),
               (gt, ":proficiency_count_2", ":proficiency_count"),
               (assign, ":right_weapon", ":itm_no"),
               (assign, ":proficiency_count", ":proficiency_count_2"),
            (else_try),
               (eq, ":type_no", itp_type_shield),
               (assign, ":left_weapon", ":itm_no"),
            (try_end),
         (try_end),
         (try_begin),
            (gt, ":left_weapon", 0),
            (agent_set_wielded_item, ":agent_no", ":left_weapon"),
         (try_end),
         (try_begin),
            (gt, ":right_weapon", 0),
            (agent_set_wielded_item, ":agent_no", ":right_weapon"),#先左后右，避免盾把双手顶掉
         (try_end),

         (try_begin),
            (this_or_next|troop_is_mounted, ":troop_no"),
            (this_or_next|troop_is_guarantee_horse, ":troop_no"),
            (troop_is_hero, ":troop_no"),
            (troop_get_inventory_capacity, ":inventory_capacity", ":troop_no"),
            (try_for_range, ":count_no", 0, ":inventory_capacity"),
               (troop_get_inventory_slot, ":item_no", ":troop_no", ":count_no"),
               (gt, ":item_no", 0),
               (item_get_type, ":item_type_no", ":item_no"),
               (eq, ":item_type_no", itp_type_horse),#坐骑
               (entry_point_get_position, pos1, 5),
               (set_spawn_position, pos1),
               (spawn_horse, ":item_no"),
               (assign, ":inventory_capacity", 0),#break
            (try_end),
         (try_end),

         (troop_get_slot, ":anim_no", ":troop_no", slot_troop_window_animation),#站姿
         (try_begin),
            (gt, ":anim_no", 0),
            (agent_set_animation, ":agent_no", ":anim_no"),
         (try_end),

         (assign, "$troop_show_2", ":troop_no"),#用于刷新信息
      ]),

      (ti_on_agent_spawn, 0, 0, [],#坐骑
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),
         (neg|agent_is_human, ":agent_no"),
         (assign, "$mission_show_horse", ":agent_no"),
      ]),

      (ti_after_mission_start, 0, 0, [],        #cam
      [
         (assign, "$troop_show", -1),
         (entry_point_get_position, pos3, 3),
         (mission_cam_set_mode, 1),   
         (mission_cam_set_position, pos3),    
      ]),
#pos3 is this mission's normal camera position

      (0,0,0,[(gt, "$troop_show", 0),],
      [
         (agent_set_visibility, "$mission_show_agent", 0),
         (agent_fade_out, "$mission_show_agent"),
         (try_begin),
            (ge, "$mission_show_horse", 0),
            (agent_set_visibility, "$mission_show_horse", 0),
            (agent_fade_out, "$mission_show_horse"),
            (assign, "$mission_show_horse", -1),
         (try_end),
         (add_visitors_to_current_scene, 2, "$troop_show", 1),
         (assign, "$troop_show", -1),
      ]),

      (ti_inventory_key_pressed, 0, 0, 
      [
         (set_trigger_result, 0),
      ], []),  

      (ti_tab_pressed, 0, 0,
       [],
       [
         (show_object_details_overlay, 1),
         (finish_mission),
       ]),
    ],
  ),


  (
    "boss_window",0,-1,
     "character window background.",
    [
      (0, mtef_visitor_source, af_override_horse, 0, 1, []),
      (1, mtef_visitor_source, af_override_horse, 0, 1, []),
      (2, mtef_visitor_source, af_override_horse, 0, 1, []),
      (3, mtef_visitor_source, af_override_horse, 0, 1, []),
      (4, mtef_visitor_source, af_override_horse, 0, 1, []),
    ],
    AoM_battle_triggers + [
#      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [],
      [
#         (show_object_details_overlay, 0),
         (assign, "$mission_show_horse", -1),
      ]),

      (ti_on_agent_spawn, 0, 0, [],#人物
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (neq, ":troop_no", "trp_player"),
         (assign, "$mission_show_agent", ":agent_no"),

         (assign, ":proficiency_count", 0),
         (try_for_range, ":count_no", 0, 4),
            (agent_get_item_slot, ":itm_no", ":agent_no", ":count_no"),
            (gt, ":itm_no", 0),
            (item_get_type, ":type_no",":itm_no"),
            (try_begin),
               (try_begin),
                  (eq, ":type_no", itp_type_one_handed_wpn),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_one_handed_weapon),
               (else_try),
                  (eq, ":type_no", itp_type_two_handed_wpn),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_two_handed_weapon),
               (else_try),
                  (eq, ":type_no", itp_type_polearm),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_polearm),
               (else_try),
                  (eq, ":type_no", itp_type_bow),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_archery),
               (else_try),
                  (eq, ":type_no", itp_type_crossbow),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_crossbow),
               (else_try),
                  (eq, ":type_no", itp_type_thrown),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_throwing),
               (else_try),
                  (this_or_next|eq, ":type_no", itp_type_pistol),
                  (eq, ":type_no", itp_type_musket),
                  (store_proficiency_level, ":proficiency_count_2", ":troop_no", wpt_firearm),
               (else_try),
                  (assign, ":proficiency_count_2", 0),
               (try_end),
               (gt, ":proficiency_count_2", ":proficiency_count"),
               (agent_set_wielded_item, ":agent_no", ":itm_no"),
               (assign, ":proficiency_count", ":proficiency_count_2"),
            (else_try),
               (eq, ":type_no", itp_type_shield),
               (agent_set_wielded_item, ":agent_no", ":itm_no"),
            (try_end),
         (try_end),

         (try_begin),
            (this_or_next|troop_is_mounted, ":troop_no"),
            (this_or_next|troop_is_guarantee_horse, ":troop_no"),
            (troop_is_hero, ":troop_no"),
            (troop_get_inventory_capacity, ":inventory_capacity", ":troop_no"),
            (try_for_range, ":count_no", 0, ":inventory_capacity"),
               (troop_get_inventory_slot, ":item_no", ":troop_no", ":count_no"),
               (gt, ":item_no", 0),
               (item_get_type, ":item_type_no", ":item_no"),
               (eq, ":item_type_no", itp_type_horse),#坐骑
               (entry_point_get_position, pos1, 5),
               (set_spawn_position, pos1),
               (spawn_horse, ":item_no"),
               (assign, ":inventory_capacity", 0),#break
            (try_end),
         (try_end),

         (start_presentation, "prsnt_boss_window"),
      ]),

      (ti_on_agent_spawn, 0, 0, [],#坐骑
      [
         (store_trigger_param_1, ":agent_no"),
         (agent_set_no_dynamics, ":agent_no", 1),
         (neg|agent_is_human, ":agent_no"),
         (assign, "$mission_show_horse", ":agent_no"),
      ]),

      (ti_after_mission_start, 0, 0, [],        #cam
      [
         (entry_point_get_position, pos3, 3),
         (mission_cam_set_mode, 1),   
         (set_fixed_point_multiplier, 100),
         (position_move_x, pos3, -30),
         (mission_cam_set_position, pos3),  
      ]),
#pos3 is this mission's normal camera position

      (ti_before_mission_start, 0, 0, [],
      [
         (assign, "$mission_show_agent", -1),  
         (assign, "$mission_show_horse", -1),
      ]),

      (0,0,0,[(gt, "$boss_num_3", 0),],#刷新
      [
         (try_begin),
            (ge, "$mission_show_agent", 0),
            (agent_set_visibility, "$mission_show_agent", 0),
            (agent_fade_out, "$mission_show_agent"),
            (assign, "$mission_show_agent", -1),
         (try_end),
         (try_begin),
            (ge, "$mission_show_horse", 0),
            (agent_set_visibility, "$mission_show_horse", 0),
            (agent_fade_out, "$mission_show_horse"),
            (assign, "$mission_show_horse", -1),
         (try_end),
         (troop_get_slot, ":troop_no", "trp_boss_array", "$boss_num_3"),
         (assign, "$boss_num_2", "$boss_num_3"),#用于记录当前boss序号
         (assign, "$boss_num_3", -1),
         (add_visitors_to_current_scene, 2, ":troop_no", 1),
      ]),

      (ti_inventory_key_pressed, 0, 0, 
      [
         (set_trigger_result, 0),
      ], []),  

      (ti_tab_pressed, 0, 0,
       [],
       [
         (show_object_details_overlay, 1),
         (finish_mission),
       ]),
    ],
  ),


  (
    "film_test",0,-1,
     "film_test.",
    [
      (0, mtef_visitor_source, af_override_horse, 0, 1, []),
      (1, mtef_visitor_source, af_override_horse, 0, 1, []),
      (2, mtef_visitor_source, af_override_horse, 0, 1, []),
      (3, mtef_visitor_source, af_override_horse, 0, 1, []),
      (4, mtef_visitor_source, af_override_horse, 0, 1, []),
      (5, mtef_visitor_source, af_override_horse, 0, 1, []),
      (6, mtef_visitor_source, af_override_horse, 0, 1, []),
      (7, mtef_visitor_source, af_override_horse, 0, 1, []),
      (8, mtef_visitor_source, af_override_horse, 0, 1, []),
      (9, mtef_visitor_source, af_override_horse, 0, 1, []),
      (10, mtef_visitor_source, af_override_horse, 0, 1, []),
      (11, mtef_visitor_source, af_override_horse, 0, 1, []),
      (12, mtef_visitor_source, af_override_horse, 0, 1, []),
      (13, mtef_visitor_source, af_override_horse, 0, 1, []),
      (14, mtef_visitor_source, af_override_horse, 0, 1, []),
      (15, mtef_visitor_source, af_override_horse, 0, 1, []),
      (16, mtef_visitor_source, af_override_horse, 0, 1, []),
      (17, mtef_visitor_source, af_override_horse, 0, 1, []),
      (18, mtef_visitor_source, af_override_horse, 0, 1, []),
      (19, mtef_visitor_source, af_override_horse, 0, 1, []),
      (20, mtef_visitor_source, af_override_horse, 0, 1, []),
      (21, mtef_visitor_source, af_override_horse, 0, 1, []),
      (22, mtef_visitor_source, af_override_horse, 0, 1, []),
      (23, mtef_visitor_source, af_override_horse, 0, 1, []),
      (24, mtef_visitor_source, af_override_horse, 0, 1, []),
      (25, mtef_visitor_source, af_override_horse, 0, 1, []),
      (26, mtef_visitor_source, af_override_horse, 0, 1, []),
      (27, mtef_visitor_source, af_override_horse, 0, 1, []),
      (28, mtef_visitor_source, af_override_horse, 0, 1, []),
      (29, mtef_visitor_source, af_override_horse, 0, 1, []),
      (30, mtef_visitor_source, af_override_horse, 0, 1, []),
      (31, mtef_visitor_source, af_override_horse, 0, 1, []),
      (32, mtef_visitor_source, af_override_horse, 0, 1, []),
      (33, mtef_visitor_source, af_override_horse, 0, 1, []),
      (34, mtef_visitor_source, af_override_horse, 0, 1, []),
      (35, mtef_visitor_source, af_override_horse, 0, 1, []),
      (36, mtef_visitor_source, af_override_horse, 0, 1, []),
      (37, mtef_visitor_source, af_override_horse, 0, 1, []),
      (38, mtef_visitor_source, af_override_horse, 0, 1, []),
      (39, mtef_visitor_source, af_override_horse, 0, 1, []),
      (40, mtef_visitor_source, af_override_horse, 0, 1, []),
      (41, mtef_visitor_source, af_override_horse, 0, 1, []),
      (42, mtef_visitor_source, af_override_horse, 0, 1, []),
      (43, mtef_visitor_source, af_override_horse, 0, 1, []),
      (44, mtef_visitor_source, af_override_horse, 0, 1, []),
    ],
    AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_tab_pressed, 0, 0, [],
       [
         (show_object_details_overlay, 1),
         (finish_mission,0),
        ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (scene_set_day_time, 3),
         (set_rain, 1, 90),
         ]),

      (ti_after_mission_start, 0, 0, [],
       [
         (assign, "$g_film_state", 0),
         (assign, "$g_film_cam", 0),
         (show_object_details_overlay, 0),
         (set_fixed_point_multiplier, 100),
         (reset_mission_timer_c),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_fallen_warrior"),
            (agent_set_speed_modifier, ":agent_no", 30),
            (assign, "$film_character_1", ":agent_no"),#boss
            (agent_set_wielded_item, "$film_character_1", "itm_mozu_changjian"),
         (else_try),
            (eq, ":troop_no", "trp_gold_adventurer"),#dead body
            (assign, "$film_character_3", ":agent_no"),#dead body
         (else_try),
            (eq, ":troop_no", "trp_temp_substitute"),
            (agent_set_speed_modifier, ":agent_no", 25),
            (agent_set_is_alarmed, ":agent_no", 1),
            (assign, "$film_character_2", ":agent_no"),
            (try_begin),
               (troop_get_inventory_slot, reg1, "trp_temp_substitute", 0),
               (gt, reg1, 0),
               (agent_set_wielded_item, "$film_character_2", reg1),
            (try_end),
            (try_begin),
               (troop_get_inventory_slot, reg1, "trp_temp_substitute", 1),
               (gt, reg1, 0),
               (agent_set_wielded_item, "$film_character_2", reg1),
            (try_end),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (store_mission_timer_c_msec, ":cur_time"),
         (try_begin),
            (eq, "$g_film_state", 0),
            (agent_set_animation, "$film_character_1", "anim_crazy_continuous_chopping"),
            (agent_set_animation, "$film_character_3", "anim_dead_body"),
            (assign, "$g_film_state", 1),
         (else_try),
            (eq, "$g_film_state", 1),
            (ge, ":cur_time", 4000),
            (agent_get_position, pos1, "$film_character_2"),
            (position_move_y, pos1, 700),
            (agent_set_scripted_destination, "$film_character_2", pos1, 1),
            (assign, "$g_film_state", 2),
         (else_try),
            (eq, "$g_film_state", 2),
            (is_between, ":cur_time", 17000, 19000),
            (agent_set_animation, "$film_character_1", "anim_jump_end"),
            (assign, "$g_film_state", 3),
         (else_try),
            (eq, "$g_film_state", 3),
            (is_between, ":cur_time", 19000, 23000),
            (agent_get_position, pos1, "$film_character_1"),
            (position_move_y, pos1, -100),
            (agent_set_scripted_destination, "$film_character_1", pos1, 1),
            (agent_set_animation, "$film_character_1", "anim_turn_left"),
            (assign, "$g_film_state", 4),
         (else_try),
            (eq, "$g_film_state", 4),
            (is_between, ":cur_time", 23000, 23400),
            (agent_set_attack_action, "$film_character_1", 2, 1),
            (assign, "$g_film_state", 5),
         (else_try),
            (eq, "$g_film_state", 5),
            (is_between, ":cur_time", 23400, 23900),
            (agent_set_attack_action, "$film_character_1", 2, 0),
            (assign, "$g_film_state", 6),
         (else_try),
            (eq, "$g_film_state", 6),
            (ge, ":cur_time", 23900),
            (agent_set_animation, "$film_character_1", "anim_standard_twohand_stand"),
            (assign, "$g_film_state", 7),
         (try_end),

         (try_begin),
            (eq, "$g_film_cam", 0),#brazier pot
            (le, ":cur_time", 6000),
            (init_position, pos1),
            (position_set_x, pos1, 11674),
            (position_set_y, pos1, 12205),
            (position_set_z, pos1, 920),
            (position_rotate_x, pos1, 24),
            (position_rotate_z, pos1, 184),
            (position_move_x, pos1, -20),
            (mission_cam_set_mode, 1, 0, 0),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 1),
         (else_try),
            (eq, "$g_film_cam", 1),#walk in
            (is_between, ":cur_time", 6000, 9500),
            (init_position, pos1),
            (position_set_x, pos1, 13085),
            (position_set_y, pos1, 12987),#13087
            (position_set_z, pos1, 806),#783
            (position_rotate_x, pos1, 15),
            (position_rotate_z, pos1, 216),
            (mission_cam_set_position, pos1),
#            (mission_cam_animate_to_screen_color, 0x00000000, 1000),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),#cut the corpse
            (is_between, ":cur_time", 9500, 17000),
            (init_position, pos1),
            (position_set_x, pos1, 11985),
            (position_set_y, pos1, 12201),
            (position_set_z, pos1, 838),
            (position_rotate_x, pos1, 15),
            (position_rotate_z, pos1, 200),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 3),
         (else_try),
            (eq, "$g_film_cam", 3),#find player come in
            (is_between, ":cur_time", 17000, 20000),
            (entry_point_get_position, pos1, 41),
            (position_move_y, pos1, 100),
            (position_move_z, pos1, 260),
            (position_rotate_z, pos1, 180),
            (copy_position, pos2, pos1),
            (position_move_x, pos2, 100),
            (mission_cam_set_position, pos1),
            (mission_cam_animate_to_position, pos2, 3000, 1),
            (assign, "$g_film_cam", 4),
         (else_try),
            (eq, "$g_film_cam", 4),#turn back
            (is_between, ":cur_time", 20000, 25000),
            (init_position, pos1),
            (agent_get_position, pos2, "$film_character_2"),
            (copy_position, pos1, pos2),
            (agent_get_look_position, pos3, "$film_character_2"),
            (position_copy_rotation, pos1, pos3),
            (position_move_x, pos1, -100),
            (position_move_y, pos1, 600),
            (position_move_z, pos1, 100),
            (mission_cam_set_position, pos1),
            (copy_position, pos2, pos1),
            (position_move_y, pos2, -300),
            (mission_cam_animate_to_position, pos2, 3000, 1),
            (assign, "$g_film_cam", 5),
#            (eq, "$g_film_cam", 5),
#            (mission_cam_set_mode, 0),   
         (try_end),
         ], []),

      (0, 0, 0, [(key_clicked, key_v),],
      [
         (agent_get_position, pos1, "$mission_player_agent"),
         (copy_position, pos3, pos1),
         (agent_get_look_position, pos2, "$mission_player_agent"),
         (position_copy_rotation, pos3, pos2),
(position_get_x, reg1, pos3),
(display_message, "@{reg1}"),
(position_get_y, reg1, pos3),
(display_message, "@{reg1}"),
(position_get_z, reg1, pos3),
(display_message, "@{reg1}"),
(position_get_rotation_around_x, reg1, pos3),
(display_message, "@{reg1}"),
(position_get_rotation_around_y, reg1, pos3),
(display_message, "@{reg1}"),
(position_get_rotation_around_z, reg1, pos3),
(display_message, "@{reg1}"),
         ]),
    ],
  ),


  (
    "quick_battle_new",mtf_battle_mode,charge,
     "fight a match in the arena.",
    [
     (0, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (1, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (2, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (3, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (4, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (5, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (6, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (7, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (8, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
     (9, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (10, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (11, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (12, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (13, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (14, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (15, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
     (16, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 1, []),
#观战模式用
     (17, mtef_visitor_source, 0, aif_start_alarmed, 1, []),
     (18, mtef_visitor_source, 0, aif_start_alarmed, 1, []),
#     (17, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
#     (18, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
    ],
    deathcam_triggers + AoM_battle_triggers + AoM_boss_triggers_summary + [

      common_battle_init_banner,
      common_inventory_not_available,
      common_battle_order_panel,
      common_battle_order_panel_tick,

      (ti_on_agent_spawn, 0, 0,
       [],
       [
       (store_trigger_param_1, ":agent_no"),
       (agent_is_human, ":agent_no"),
       (agent_is_alive, ":agent_no"),
(agent_get_troop_id, ":troop_no", ":agent_no"),
(neq, ":troop_no", "trp_player"),

#       (agent_set_no_dynamics, ":agent_no", 1),
#          (agent_add_relation_with_agent, ":agent_no", "$mission_player_agent", 0),
#(assign, "$test_agent_no", ":agent_no"),
       ]),

      (0, 0, 0,
       [(key_clicked, key_v),],
       [
       ]),

      (0, 0, 0,
       [(key_clicked, key_b),],
       [
       ]),

      (0, 0, 0,
       [(key_clicked, key_x),],
       [
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (finish_mission),
        (change_screen_return),
       ]),

    ],
  ),




###############################################################剧情##########################################################
#####
  (
    "ship_room",mtf_battle_mode,charge, #开局剧情：玩家在船上的一个房间里醒来，周围是六具尸体。
     "Ship Room.",
    [
     (0, mtef_visitor_source, af_override_horse, 0, 1, []),
     (1, mtef_visitor_source, af_override_horse, 0, 1, []),
     (2, mtef_visitor_source, af_override_horse, 0, 1, []),
     (3, mtef_visitor_source, af_override_horse, 0, 1, []),
     (4, mtef_visitor_source, af_override_horse, 0, 1, []),
     (5, mtef_visitor_source, af_override_horse, 0, 1, []),
     (6, mtef_visitor_source, af_override_horse, 0, 1, []),
     (7, mtef_visitor_source, af_override_horse, 0, 1, []),
     (8, mtef_visitor_source, af_override_horse, 0, 1, []),
     (9, mtef_visitor_source, af_override_horse, 0, 1, []),
    ],
    deathcam_triggers + AoM_battle_triggers + [

      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [],
       [
         (scene_set_day_time, 3),
         ]),

      (ti_after_mission_start, 0, 0, [],
       [
         (entry_point_get_position, pos1, 8),
         (set_spawn_position, pos1),
         (spawn_item, "itm_small_life_talisman", 0), #小生命护符
         (entry_point_get_position, pos1, 9),
         (set_spawn_position, pos1),
         (spawn_item, "itm_highly_toxin", 0), #剧毒油脂
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (neq, ":troop_no", "trp_player"),
            (assign, "$film_character_1", ":agent_no"),
            (agent_set_animation, ":agent_no", "anim_dead_body", 0),
            (remove_agent, ":agent_no"),
         (try_end),
         ]),

      (1, 1, ti_once,
       [         (play_sound_at_position, "snd_storm", pos1),],
       [
         (dialog_box, "@MOD 特 殊 功 能 ： ^^一 、 新 物 品 栏 ： 大 地 图 点 击 “ 物 品 ” 或 者 部 分 场 景 按 I键 启 动 物 品 栏 ， 其 中 “ 右 手 武 器 ” 项 目 可 装 填 单 双 手 长 杆 火 器 投 掷 和 弩 ， “ 左 手 武 器 ” 项 目 可 装 填 弓 和 盾 ， 弹 药 有 专 门 两 个 槽 装 备 。 ^ 二 、 翻 滚 和 垫 步 ： 方 向 键 加 左 shift可 四 向 翻 滚 ， 方 向 键 连 点 两 次 可 垫 步 。  ^三 、 按 \键 卸 下 装 备 ， 靠 近 可 拾 捡 物 品 时 建 议 卸 下 装 备 再 捡 取 。 拾 取 可 拾 捡 物 会 占 用 手 ， 导 致 武 器 无 法 拔 出 ， 因 而 建 议 拾 取 后 按 一 次 \收 回 。 "),
       ]),

      (0, 0, 0,
       [],
       [
         (set_fixed_point_multiplier, 100),
         (init_position, pos1),
         (position_set_x, pos1, 137),
         (position_set_y, pos1, -1599),
         (position_set_z, pos1, 785),
         (particle_system_burst, "psys_game_rain", pos1, 30),
       ]),

      (ti_on_item_picked_up, 0, 0,
       [],
       [
         (store_trigger_param_2, ":item_no"),
         (try_begin),
            (eq, ":item_no", "itm_highly_toxin"), #剧毒油脂
            (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_highly_toxin", 0, 0, 0),
            (dialog_box, "@装 备 之 后 ， 按 H可 使 用 补 给 品 快 速 回 血 ， R可 使 用 小 道 具 。 （ 未 实 装 ） "),
         (else_try),
            (eq, ":item_no", "itm_small_life_talisman"), #小生命护符
            (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_small_life_talisman", 0, 0, 0),
            (dialog_box, "@装 备 饰 物 后 能 获 得 一 定 加 成 。 装 备 复 数 同 种 饰 物 时 ， 只 有 一 个 能 生 效 。 "),
         (try_end),
       ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "str_cannot_leave_now"),
       ]),
    ]
  ),


  (
    "ship_attacked",mtf_battle_mode,charge, #开局剧情：走出来后被岩雷狂战士袭击
     "Ship under attack.",
    [
     (0, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (1, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (2, mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, []),#玩家
     (3, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (4, mtef_visitor_source, af_override_everything, aif_start_alarmed, 1, [itm_blue_gambeson, itm_xihai_pixue, itm_leather_gloves, itm_nordic_helmet, itm_longshoujian]),#狂战士
     (5, mtef_visitor_source|mtef_team_0, af_override_horse|af_override_weapons, aif_start_alarmed, 1, []),#水手
     (6, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),#暗枭埃洛伊斯
     (7, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
    ],
     AoM_battle_triggers + boss_triggers_megalith_berserker + [

      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [], #准备过场动画
       [
         (scene_set_day_time, 3),
         (set_rain, 1, 540),
         (show_object_details_overlay, 0),
         ]),

      (ti_after_mission_start, 0, 0, [], #启动过场动画
       [
         (assign, "$g_film_state", 1),#cam和stage都是0时关停，123456逐步推进
         (assign, "$g_film_cam", 1),
         (reset_mission_timer_c),
         (mission_cam_set_mode, 1),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_starkhook_megalith_berserker"),
            (agent_set_wielded_item, ":agent_no", "itm_longshoujian"),
         (else_try),
            (eq, ":troop_no", "trp_lesaff_armed_sailor"),#水手
            (agent_set_animation, ":agent_no", "anim_dead_body", 0),
            (assign, "$film_character_1", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_dark_owl_eloise"),#暗枭埃洛伊斯
            (agent_set_animation, ":agent_no", "anim_ship_attacked_pos_2", 0),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (store_mission_timer_c_msec, ":cur_time"),
#动作等
         (try_begin),
            (eq, "$g_film_state", 1),
            (remove_agent, "$film_character_1"),
            (assign, "$g_film_state", 2),
         (else_try),
            (eq, "$g_film_state", 2),
            (ge, ":cur_time", 3000),
            (agent_set_animation, "$mission_boss_1", "anim_ship_attacked_pos_1", 0),
            (assign, "$g_film_state", 3),
         (else_try),
            (eq, "$g_film_state", 3),
            (ge, ":cur_time", 8000),
            (show_object_details_overlay, 1),
            (agent_set_team, "$mission_boss_1", 1),
            (assign, "$g_film_state", 0),#过场动画结束
         (else_try),
            (eq, "$g_film_state", 4),#落败
            (entry_point_get_position, pos1, 11),
            (agent_set_position, "$mission_boss_1", pos1),
            (agent_set_animation, "$mission_boss_1", "anim_ship_attacked_pos_3", 0),
#            (agent_set_team, "$mission_boss_1", 0),
            (entry_point_get_position, pos1, 10),
            (agent_set_position, "$mission_player_agent", pos1),
            (assign, "$g_film_state", 6),
         (else_try),
            (eq, "$g_film_state", 5),#胜利
            (entry_point_get_position, pos1, 10),
            (agent_set_position, "$mission_boss_1", pos1),
            (assign, "$g_film_state", 7),
         (else_try),
            (eq, "$g_film_state", 6),
            (ge, ":cur_time", 3000),
            (agent_set_animation, "$mission_boss_1", "anim_ship_attacked_pos_4", 0),#落败结局，敌方看向船外
            (assign, "$g_film_state", 7),
         (else_try),
            (eq, "$g_film_state", 7),#升起
            (ge, ":cur_time", 4000),
            (entry_point_get_position, pos1, 14),
            (set_spawn_position, pos1),
            (spawn_agent, "trp_blood_moon_birth_one"),
            (agent_set_animation, reg0, "anim_ship_attacked_pos_5", 0),
            (assign, "$g_film_state", 8),
         (else_try),
            (eq, "$g_film_state", 8),#剧烈振荡
            (ge, ":cur_time", 10000),
            (mission_cam_get_position, pos1),
            (play_sound_at_position, "snd_hit_ground", pos1),
            (assign, "$g_film_state", 9),
         (else_try),
            (eq, "$g_film_state", 9),
            (ge, ":cur_time", 12000),#结束
            (mission_cam_set_mode, 0),
            (assign, "$current_startup_quest_phase", 2),
            (finish_mission),
            (change_screen_return),
         (try_end),

#镜头
         (try_begin),
            (eq, "$g_film_cam", 1),#注视
            (le, ":cur_time", 3000),
            (mission_cam_set_mode, 1, 0, 0),
            (entry_point_get_position, pos1, 8),
            (mission_cam_set_position, pos1),
            (play_sound_at_position, "snd_storm", pos1),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),#拔出斧头
            (is_between, ":cur_time", 3000, 5000),
            (entry_point_get_position, pos1, 15),
            (mission_cam_set_position, pos1),
            (play_sound_at_position, "snd_storm", pos1),
            (assign, "$g_film_cam", 3),
         (else_try),
            (eq, "$g_film_cam", 3),#运镜拉回
            (is_between, ":cur_time", 5000, 8000),
            (entry_point_get_position, pos1, 16),
            (mission_cam_set_position, pos1),
            (entry_point_get_position, pos3, 17),
            (mission_cam_animate_to_position, pos3, 3000, 1),
            (assign, "$g_film_cam", 4),
         (else_try),
            (eq, "$g_film_cam", 4),#过场动画结束
            (ge, ":cur_time", 8000),
            (mission_cam_set_mode, 0),
            (assign, "$g_film_cam", 0),#暂时关停过场动画
         (else_try),
            (eq, "$g_film_cam", 5),#战斗结束动画，计时重启
            (mission_cam_set_mode, 1, 0, 0),
            (entry_point_get_position, pos1, 9),
            (mission_cam_set_position, pos1),
            (play_sound_at_position, "snd_storm", pos1),
            (assign, "$g_film_cam", 6),
         (else_try),
            (eq, "$g_film_cam", 6),
            (main_hero_fallen),
            (ge, ":cur_time", 3000),
            (entry_point_get_position, pos1, 12),#落败结局，敌方看向船外
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 7),
         (else_try),
            (eq, "$g_film_cam", 6),
            (neg|agent_is_alive, "$mission_boss_1"),#战胜结局
            (assign, "$g_film_cam", 7),
         (else_try),
            (eq, "$g_film_cam", 7),
            (ge, ":cur_time", 4000),
            (entry_point_get_position, pos1, 13),#镜头转向船外，升起
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 8),
         (else_try),
            (eq, "$g_film_cam", 8),#剧烈震荡
            (ge, ":cur_time", 10000),
            (store_random_in_range, ":count_no", 0, 1000),
            (le, ":count_no", 10),
            (set_fixed_point_multiplier, 100),
            (mission_cam_get_position, pos1),
            (store_random_in_range, ":count_no", -20, 20),
            (position_move_x, pos1, ":count_no"),
            (position_move_y, pos1, ":count_no"),
            (position_move_z, pos1, ":count_no"),
            (store_random_in_range, ":count_no", -4, 4),
            (position_rotate_x, pos1, ":count_no"),
            (position_rotate_y, pos1, ":count_no"),
            (position_rotate_z, pos1, ":count_no"),
            (mission_cam_set_position, pos1),
         (try_end),

         (try_begin),
            (eq, "$g_film_state", 0),#战斗过程中
            (main_hero_fallen),
            (reset_mission_timer_c),
            (assign, "$g_film_state", 4), #落败
            (assign, "$g_film_cam", 5),#再次启动动画
         (else_try),
            (eq, "$g_film_state", 0),#战斗过程中
            (neg|agent_is_alive, "$mission_boss_1"),
            (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_mark_of_scars", 0, 0, 0),
            (reset_mission_timer_c),
            (assign, "$g_film_state", 5), #胜利
            (assign, "$g_film_cam", 5),#再次启动动画
         (try_end),

         (try_begin),
            (store_random_in_range, ":count_no", 0, 10000),#暴雨声
            (eq, ":count_no", 0),
            (mission_cam_get_position, pos1),
            (play_sound_at_position, "snd_storm", pos1),
         (try_end),
         ], []),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "str_cannot_leave_now"),
       ]),
    ]
  ),


  (
    "libra_smuggle_wharf",mtf_battle_mode,charge, #开局剧情：登陆后在走私码头潜行
     "Libra Smuggle Wharf",
    [
      (0,mtef_visitor_source|mtef_team_1,0, aif_start_alarmed, 1,[]),
      (1, mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (3, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (4, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (5, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (6, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (7, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (8, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (9, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (10, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (11, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (12, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (13, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (14, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (15, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (16, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (17, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (18, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (19, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (20, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (21, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (22, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (23, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
    ],
     AoM_battle_triggers + AoM_inflitration_triggers + [
      common_battle_init_banner,

      (ti_after_mission_start, 0, 0, [], #准备过场动画
       [
       (assign, "$environment_visibility", 80),#能见度
       (entry_point_get_position, pos1, 26),
       (set_spawn_position, pos1),
       (spawn_item, "itm_dagger", 0), #匕首

       (assign, "$g_film_state", 1),#cam、dialog和stage都是0时关停，123456逐步推进
       (assign, "$g_film_cam", 1),
       (assign, "$g_film_dialog", 1),
       (show_object_details_overlay, 0),
       (mission_cam_set_mode, 1),
       (reset_mission_timer_c),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_libra_slave_merchant"),#奴贩
            (assign, "$film_character_1", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_libra_drug_dealer"),#毒贩
            (assign, "$film_character_2", ":agent_no"),
         (try_end),
         ]),

      (ti_on_item_picked_up, 0, 0,
       [],
       [
         (store_trigger_param_2, ":item_no"),
         (try_begin),
            (eq, ":item_no", "itm_dagger"), #匕首
            (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_dagger", 0, 0, 0),
            (dialog_box, "@部 分 武 器 带 有 战 技 ， 攻 击 的 同 时 按 住 E 键 即 可 使 用 。 除 此 之 外 ， 部 分 装 备 也 带 有 加 成 。 战 技 和 加 成 可 在 新 物 品 栏 界 面 的 物 品 描 述 处 查 看 。 "),
         (try_end),
       ]),

      (0, 0, 0,
       [
         (try_begin),
            (eq, "$g_film_state", 0),#动画结束
            (main_hero_fallen),
            (assign, "$current_startup_quest_phase", 4),
            (call_script, "script_troop_remove_item_with_modifier_new", "trp_player", "itm_small_life_talisman", -1),
            (finish_mission),
            (change_screen_return),
         (try_end),
         (this_or_next|gt, "$g_film_state", 0),
         (gt, "$g_film_cam", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#动作等
         (try_begin),
            (eq, "$g_film_state", 1),
            (ge, ":cur_time", 6000),
            (entry_point_get_position, pos1, 28),
            (agent_set_position, "$mission_player_agent", pos1),
            (agent_set_animation, "$mission_player_agent", "anim_smuggle_wharf_infliation_1", 0),#探头偷听
            (entry_point_get_position, pos1, 30),
            (agent_set_position, "$film_character_1", pos1),
            (entry_point_get_position, pos1, 31),
            (agent_set_position, "$film_character_2", pos1),
            (assign, "$g_film_state", 2),
         (else_try),
            (eq, "$g_film_state", 2),
            (ge, ":cur_time", 30000),
            (dialog_box, "@潜 行 模 式 ： ^^隐 蔽 水 平 ： 潜 行 模 式 下 ， 右 下 角 将 会 显 示 玩 家 的 隐 蔽 水 平 ， 隐 蔽 水 平 极 低 时 靠 近 敌 人 将 会 被 直 接 发 现 。 隐 蔽 水 平 受 装 备 重 量 、 技 能 、 潜 行 术 、 移 速 以 及 环 境 因 素 影 响 。 ^^疑 心 和 警 戒 ： 敌 人 在 远 处 看 到 玩 家 后 ， 会 产 生 疑 心 ， 开 始 搜 查 。 而 近 距 离 目 击 或 者 受 击 将 会 使 敌 人 进 入 最 高 警 戒 ， 对 玩 家 进 行 不 死 不 休 的 追 击 ， 同 时 所 有 其 他 敌 人 都 会 前 来 调 查 。 发 现 尸 体 也 会 使 敌 人 进 入 警 戒 。 ^^潜 行 术 ： 按 Z键 开 始 潜 行 。 "),
            (assign, "$g_film_state", 0),
            (assign, "$current_startup_quest_phase", 3),
         (try_end),
#镜头
         (try_begin),
            (eq, "$g_film_cam", 1),#全景
            (le, ":cur_time", 6000),
            (entry_point_get_position, pos1, 27),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_x, pos1, 500),
            (mission_cam_animate_to_position, pos1, 6000, 1),
            (str_store_string, s67, "@走 私 者 的 无 名 港 口 "),
            (assign, "$g_scene_name", 1),
            (start_presentation, "prsnt_total_battle_interface"),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),#偷听
            (is_between, ":cur_time", 6000, 10000),
            (entry_point_get_position, pos1, 29),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_x, pos1, 100),
            (mission_cam_animate_to_position, pos1, 3000, 1),
            (assign, "$g_scene_name", -1),#关停地名展示
            (assign, "$g_film_cam", 3),
         (else_try),
            (eq, "$g_film_cam", 3),#镜头推进
            (is_between, ":cur_time", 10000, 20000),
            (entry_point_get_position, pos1, 32),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_y, pos1, 1000),
            (mission_cam_animate_to_position, pos1, 10000, 1),
            (assign, "$g_film_cam", 4),
         (else_try),
            (eq, "$g_film_cam", 4),#结束
            (ge, ":cur_time", 30000),
            (show_object_details_overlay, 1),
            (mission_cam_set_mode, 0),
            (assign, "$g_film_cam", 0),
         (try_end),
#对话
         (try_begin),
            (eq, "$g_film_dialog", 1),
            (ge, ":cur_time", 6000),
            (str_store_string, s67, "@妈 的 ， 地 牢 里 那 小 娘 们 ， 什 么 时 候 能 让 我 玩 一 下 ？ 憋 得 慌 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 2),
         (else_try),
            (eq, "$g_film_dialog", 2),
            (ge, ":cur_time", 9000),
            (str_store_string, s67, "@别 想 了 ， 队 长 说 她 大 有 来 头 ， 要 换 赎 金 的 。 被 你 上 了 ， 就 不 值 钱 了 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 3),
         (else_try),
            (eq, "$g_film_dialog", 3),
            (ge, ":cur_time", 14000),
            (str_store_string, s67, "@一 张 膜 值 几 个 钱 ， 惺 惺 作 态 的 贵 族 ， 呸 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 4),
         (else_try),
            (eq, "$g_film_dialog", 4),
            (ge, ":cur_time", 17000),
            (str_store_string, s67, "@嘿 ， 惺 惺 作 态 的 贵 族 们 交 的 赎 金 ， 够 你 去 妓 院 耍 一 年 了 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 5),
         (else_try),
            (eq, "$g_film_dialog", 5),
            (ge, ":cur_time", 20000),
            (str_store_string, s67, "@算 了 吧 ， 落 到 我 们 手 上 还 剩 几 个 子 … … 对 了 ， 来 打 捞 的 人 还 没 到 吗 ？ "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 6),
         (else_try),
            (eq, "$g_film_dialog", 6),
            (ge, ":cur_time", 23000),
            (str_store_string, s67, "@没 呢 ， 听 说 外 海 发 生 了 一 些 变 故 ， 搞 得 海 盗 们 跟 热 锅 上 的 蚂 蚁 一 样 。 请 的 那 人 回 自 己 的 船 团 报 道 了 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 7),
         (else_try),
            (eq, "$g_film_dialog", 7),
            (ge, ":cur_time", 27000),
            (str_store_string, s67, "@希 望 不 会 影 响 我 们 的 生 意 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 8),
         (else_try),
            (eq, "$g_film_dialog", 8),
            (ge, ":cur_time", 30000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (try_end),
       ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@前 往 出 口 才 能 逃 离 。 "),
       ]),
    ]
  ),



  (
    "lesaff_street_execution",0,-1, #开局剧情：勒塞夫街头观摩公开处刑
     "Lesaff Street Execution",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse,0,1,[]),
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse,0,1,[]),
      (5, mtef_visitor_source,af_override_everything,0,1,[itm_chains_full]),#被处刑者
      (6, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (7, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (8, mtef_visitor_source,af_override_horse,0,1,[]),
      (9, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (10, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (11, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (12, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (13, mtef_visitor_source,af_override_horse,0,1,[]),
      (14, mtef_visitor_source,af_override_horse,0,1,[]),
      (15, mtef_visitor_source,af_override_head,0,1,[]),#克莉斯特
      (16, mtef_visitor_source,0,0,1,[]),
      (17, mtef_visitor_source,0,0,1,[]),
      (18, mtef_visitor_source,0,0,1,[]),#梅薇丝的目的地
      (19, mtef_visitor_source,af_override_horse,0,1,[]),
      (20, mtef_visitor_source,af_override_horse,0,1,[]),
      (21, mtef_visitor_source,0,0,1,[]),
      (22, mtef_visitor_source,0,0,1,[]),
      (23, mtef_visitor_source,0,0,1,[]),
      (24, mtef_visitor_source,af_override_horse,0,1,[]),
      (25, mtef_visitor_source,af_override_horse,0,1,[]),
      (26, mtef_visitor_source,af_override_horse,0,1,[]),
      (27, mtef_visitor_source,af_override_horse,0,1,[]),
      (28, mtef_visitor_source,af_override_everything,0,1,[itm_pilgrim_disguise, itm_yinse_xue, itm_faceless_mask]),#梅薇丝,
      (29, mtef_visitor_source,0,0,1,[]),
      (30, mtef_visitor_source,0,0,1,[]),
      (31, mtef_visitor_source,0,0,1,[]),
      (32, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (33, mtef_visitor_source,0,0,1,[]),
      (34, mtef_visitor_source,af_override_horse,0,1,[]),
      (35, mtef_visitor_source,af_override_horse,0,1,[]),
      (36, mtef_visitor_source,af_override_horse,0,1,[]),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [], #准备过场动画
       [
       (mission_cam_set_mode, 1),
       (reset_mission_timer_c),
       (assign, "$film_prop_instance_1", -1),#避免剧情触发点瞬间生效
       (assign, "$film_prop_instance_2", -1),
       (set_fog_distance, 30, 0xC4C4C4),
       ]),

      (ti_after_mission_start, 0, 0, [], 
       [
       (assign, "$g_film_cam", 1),#展示全景

       (entry_point_get_position, pos1, 5),
       (set_spawn_position, pos1),
       (spawn_scene_prop, "spr_fire_big"),
       (entry_point_get_position, pos1, 19),
       (set_spawn_position, pos1),
       (spawn_scene_prop, "spr_fire_big"),
       (spawn_scene_prop, "spr_radio"),#收音机
       (entry_point_get_position, pos1, 20),
       (set_spawn_position, pos1),
       (spawn_scene_prop, "spr_fire_big"),
       (entry_point_get_position, pos1, 27),
       (set_spawn_position, pos1),
       (spawn_scene_prop, "spr_fire_big"),

       (try_begin),
          (lt, "$mayvis_quest_phase", 1),
          (entry_point_get_position, pos1, 29),#梅薇丝剧情触发点
          (set_spawn_position, pos1),
          (spawn_scene_prop, "spr_barrier_16m"),
          (assign, "$film_prop_instance_1", reg0),
       (try_end),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_npc19"),#梅薇丝
            (assign, "$film_character_1", ":agent_no"),
            (agent_set_animation, ":agent_no", "anim_lesaff_square_pos_1", 0),#靠墙
         (else_try),
            (eq, ":troop_no", "trp_the_forsaken"),#被处刑者
            (agent_set_no_dynamics, ":agent_no", 1),
            (agent_set_animation, ":agent_no", "anim_lesaff_square_pos_2", 0),#被烧
         (else_try),
            (eq, ":troop_no", "trp_red_dolphin_banneret"),#讲话者
            (assign, "$film_character_2", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_townsman"),
            (assign, "$film_character_3", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_powell_peasant"),
            (assign, "$film_character_4", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_powell_executioner"),#行刑官
            (assign, "$film_character_5", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_knight_1_20"),#克莉斯特
            (assign, "$film_character_6", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_elemental_knight"),#元素骑士
            (assign, "$film_character_7", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_libra_hitman"),#权厄之秤杀手
            (assign, "$film_character_8", ":agent_no"),
         (try_end),
         ]),


      (0, 0, 0,
       [
         (this_or_next|gt, "$g_film_state", 0),
         (this_or_next|gt, "$g_film_cam", 0),
         (gt, "$g_film_dialog", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#动作等
         (try_begin),
            (eq, "$g_film_state", 1),
            (le, ":cur_time", 23000),
            (entry_point_get_position, pos1, 31),
            (agent_set_position, "$mission_player_agent", pos1),
            (agent_set_animation, "$film_character_2", "anim_lesaff_square_pos_4", 0),#讲话
            (assign, "$g_film_state", 2),
         (else_try),
            (eq, "$g_film_state", 2),
            (gt, ":cur_time", 23000),
            (try_for_agents, ":agent_no"),
               (agent_is_alive, ":agent_no"),
               (agent_is_human, ":agent_no"),
               (agent_get_troop_id, ":troop_no", ":agent_no"),
               (this_or_next|eq, ":troop_no", "trp_townsman"),
               (eq, ":troop_no", "trp_powell_peasant"),
               (agent_set_animation, ":agent_no", "anim_cheer", 0),#欢呼
            (try_end),
            (assign, "$g_film_state", 3),
         (else_try),
            (eq, "$g_film_state", 3),
            (gt, ":cur_time", 31000),
            (try_for_agents, ":agent_no"),
               (agent_is_alive, ":agent_no"),
               (agent_is_human, ":agent_no"),
               (agent_get_troop_id, ":troop_no", ":agent_no"),
               (this_or_next|eq, ":troop_no", "trp_townsman"),
               (eq, ":troop_no", "trp_powell_peasant"),
               (agent_set_animation, ":agent_no", "anim_cheer", 0),#杀喊
            (try_end),
            (mission_cam_get_position, pos1),
            (play_sound_at_position, "snd_kill_repeat", pos1),
            (assign, "$g_film_state", 4),
         (else_try),
            (eq, "$g_film_state", 4),
            (gt, ":cur_time", 40000),
            (agent_set_animation, "$film_character_6", "anim_lesaff_square_pos_5", 1),#克莉斯特看向玩家
            (assign, "$g_film_state", 5),
         (else_try),
            (eq, "$g_film_state", 5),
            (gt, ":cur_time", 42000),
            (agent_set_animation, "$film_character_7", "anim_lesaff_square_pos_6", 1),#元素骑士看向玩家
            (assign, "$g_film_state", 6),
         (else_try),
            (eq, "$g_film_state", 6),
            (gt, ":cur_time", 47000),
            (agent_set_no_dynamics, "$mission_player_agent", 0),
            (entry_point_get_position, pos1, 38),
            (agent_set_position, "$film_character_8", pos1),#权厄之秤的信使
            (assign, "$current_startup_quest_phase", 7),#结束
            (assign, "$g_film_state", 0),
         (try_end),
#镜头
         (try_begin),
            (eq, "$g_film_cam", 1),#全景
            (le, ":cur_time", 6000),
            (entry_point_get_position, pos1, 25),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_x, pos1, 500),
            (mission_cam_animate_to_position, pos1, 6000, 1),
            (str_store_string, s67, "@勒 塞 夫 - 平 民 区 "),
            (assign, "$g_scene_name", 1),
            (start_presentation, "prsnt_total_battle_interface"),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),#结束
            (gt, ":cur_time", 6000),
            (assign, "$g_scene_name", -1),#关停地名展示
            (mission_cam_set_mode, 0),
            (assign, "$g_film_cam", 0),
         (else_try),
            (eq, "$g_film_cam", 3),#看向火刑台
            (le, ":cur_time", 35000),
            (entry_point_get_position, pos1, 33),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 4),
         (else_try),
            (eq, "$g_film_cam", 4),#看向收音机
            (gt, ":cur_time", 35000),
            (entry_point_get_position, pos1, 35),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 5),
         (else_try),
            (eq, "$g_film_cam", 5),
            (gt, ":cur_time", 40000),
            (entry_point_get_position, pos1, 36),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 6),
         (else_try),
            (eq, "$g_film_cam", 6),
            (gt, ":cur_time", 41000),
            (entry_point_get_position, pos1, 37),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 7),
         (else_try),
            (eq, "$g_film_cam", 7),
            (gt, ":cur_time", 42000),
            (entry_point_get_position, pos1, 36),
            (mission_cam_set_position, pos1),
            (assign, "$g_film_cam", 8),
         (else_try),
            (eq, "$g_film_cam", 8),
            (gt, ":cur_time", 47000),
            (show_object_details_overlay, 1),
            (mission_cam_set_mode, 0),
            (assign, "$g_film_cam", 0),
         (try_end),
#对话
         (try_begin),
            (eq, "$g_film_dialog", 1),
            (le, ":cur_time", 5000),
            (str_store_string, s67, "@在 很 久 很 久 以 前 ， 创 世 女 神 星 璃 从 无 垠 黑 夜 中 攫 取 一 缕 ， 污 染 了 整 个 世 界 。 自 此 之 后 … … "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 2),
         (else_try),
            (eq, "$g_film_dialog", 2),
            (gt, ":cur_time", 5000),
            (str_store_string, s67, "@正 义 亦 是 邪 恶 ， 光 明 亦 是 黑 暗 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 3),
         (else_try),
            (eq, "$g_film_dialog", 3),
            (gt, ":cur_time", 9000),
            (str_store_string, s67, "@美 丽 亦 是 丑 陋 ， 圣 洁 亦 是 肮 脏 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 4),
         (else_try),
            (eq, "$g_film_dialog", 4),
            (gt, ":cur_time", 13000),
            (str_store_string, s67, "@和 平 亦 是 战 争 ， 秩 序 亦 是 混 乱 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 5),
         (else_try),
            (eq, "$g_film_dialog", 5),
            (gt, ":cur_time", 17000),
            (str_store_string, s67, "@真 相 亦 是 谎 言 ， 理 智 亦 是 癫 狂 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 6),
         (else_try),
            (eq, "$g_film_dialog", 6),
            (gt, ":cur_time", 21000),
            (str_store_string, s67, "@过 去 亦 是 未 来 ， 生 命 亦 是 死 亡 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 7),
         (else_try),
            (eq, "$g_film_dialog", 7),
            (gt, ":cur_time", 25000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (else_try),
            (eq, "$g_film_dialog", 8),
            (le, ":cur_time", 3000),
            (str_store_string, s67, "@这 个 人 ， 犯 下 了 重 罪 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 9),
         (else_try),
            (eq, "$g_film_dialog", 9),
            (gt, ":cur_time", 3000),
            (str_store_string, s67, "@他 被 界 外 邪 力 污 染 ， 堕 入 魔 躯 ， 成 为 了 最 近 为 祸 西 海 岸 的 黑 暗 尖 兵 的 一 员 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 10),
         (else_try),
            (eq, "$g_film_dialog", 10),
            (gt, ":cur_time", 7000),
            (str_store_string, s67, "@这 支 黑 暗 尖 兵 只 有 13 骑 ， 然 而 在 这 一 个 半 月 里 ， 它 们 肆 虐 了 方 圆 五 百 里 ， 摧 毁 了 三 座 城 市 和 二 十 七 个 村 镇 ， 腐 化 了 数 千 平 方 公 里 的 土 地 ， 屠 杀 了 至 少 两 万 三 千 人 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 11),
         (else_try),
            (eq, "$g_film_dialog", 11),
            (gt, ":cur_time", 14000),
            (str_store_string, s67, "@宰 了 它 ！ ！ ！ ！  "),
            (call_script, "script_start_conversation_battle", "$film_character_3"),
            (assign, "$g_film_dialog", 12),
         (else_try),
            (eq, "$g_film_dialog", 12),
            (gt, ":cur_time", 16000),
            (str_store_string, s67, "@所 幸 ， 罗 德 里 格 斯 勋 爵 阁 下 与 她 率 领 的 元 素 骑 士 团 ， 击 溃 了 这 伙 黑 暗 尖 兵 ， 阵 斩 十 一 骑 ， 俘 获 一 骑 ， 最 后 一 骑 重 伤 遁 走 ， 不 日 即 可 擒 获 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_2"),
            (assign, "$g_film_dialog", 13),
         (else_try),
            (eq, "$g_film_dialog", 13),
            (gt, ":cur_time", 23000),
            (str_store_string, s67, "@勋 爵 万 岁 ！ 元 素 骑 士 团 万 岁 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_4"),
            (assign, "$g_film_dialog", 14),
         (else_try),
            (eq, "$g_film_dialog", 14),
            (gt, ":cur_time", 26000),
            (str_store_string, s67, "@在 此 ， 我 们 将 此 獠 ， 与 缴 获 的 各 种 魔 性 物 品 一 同 ， 公 开 焚 毁 ！ 诸 位 务 必 警 惕 侵 蚀 ， 引 以 为 戒 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_5"),
            (assign, "$g_film_dialog", 15),
         (else_try),
            (eq, "$g_film_dialog", 15),
            (gt, ":cur_time", 31000),
            (str_store_string, s67, "@烧 ！ 烧 ！ 烧 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_4"),
            (assign, "$g_film_dialog", 16),
         (else_try),
            (eq, "$g_film_dialog", 16),
            (gt, ":cur_time", 33000),
            (str_store_string, s67, "@烧 ！ 烧 ！ 烧 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_3"),
            (assign, "$g_film_dialog", 17),
         (else_try),
            (eq, "$g_film_dialog", 17),
            (gt, ":cur_time", 35000),
            (str_store_string, s67, "@（ 等 等 ， 那 是 … … 收 音 机 ？ ！ ） "),
            (call_script, "script_start_conversation_battle", "$mission_player_agent"),
            (assign, "$g_film_dialog", 18),
         (else_try),
            (eq, "$g_film_dialog", 18),
            (gt, ":cur_time", 38000),
            (str_store_string, s67, "@（ 界 外 ， 侵 蚀 ， 收 音 机 ， 难 道 这 个 人 也 是 … … ） "),
            (call_script, "script_start_conversation_battle", "$mission_player_agent"),
            (assign, "$g_film_dialog", 19),
         (else_try),
            (eq, "$g_film_dialog", 19),
            (gt, ":cur_time", 41000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 20),
         (else_try),
            (eq, "$g_film_dialog", 20),
            (gt, ":cur_time", 44000),
            (str_store_string, s67, "@（ 不 行 ， 我 不 能 继 续 留 在 这 里 了 。 ） "),
            (call_script, "script_start_conversation_battle", "$mission_player_agent"),
            (assign, "$g_film_dialog", 21),
         (else_try),
            (eq, "$g_film_dialog", 21),
            (gt, ":cur_time", 47000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (try_end),
       ]),

      (3, 3, ti_once, [(eq, "$current_startup_quest_phase", 5),],#剧情刷新
       [
         (add_visitors_to_current_scene, 2, "trp_red_dolphin_knight", 1),
         (add_visitors_to_current_scene, 3, "trp_powell_conjuring_infantry", 2),
         (add_visitors_to_current_scene, 4, "trp_lesaff_iron_axe_sergeant", 2),
         (add_visitors_to_current_scene, 5, "trp_the_forsaken", 1),#被处决者
         (add_visitors_to_current_scene, 6, "trp_townsman", 8),
         (add_visitors_to_current_scene, 7, "trp_powell_peasant", 3),
         (add_visitors_to_current_scene, 8, "trp_red_dolphin_knight"),
         (add_visitors_to_current_scene, 9, "trp_townsman", 8),
         (add_visitors_to_current_scene, 10, "trp_townsman", 6),
         (add_visitors_to_current_scene, 11, "trp_townsman", 7),
         (add_visitors_to_current_scene, 12, "trp_townsman", 5),
         (add_visitors_to_current_scene, 13, "trp_powell_executioner", 1),
         (add_visitors_to_current_scene, 14, "trp_red_dolphin_banneret", 1),#讲话者
         (add_visitors_to_current_scene, 15, "trp_knight_1_20", 1),#克莉斯特·罗德里格斯
         (add_visitors_to_current_scene, 16, "trp_bloodfire_vanguard", 3),
         (add_visitors_to_current_scene, 17, "trp_elemental_ranger", 2),
         (add_visitors_to_current_scene, 21, "trp_elemental_attendant", 5),
         (add_visitors_to_current_scene, 22, "trp_elemental_knight", 1),
         (add_visitors_to_current_scene, 23, "trp_elemental_ranger", 2),
         (add_visitors_to_current_scene, 24, "trp_bloodfire_mercenary_corps_veteran", 4),
         (add_visitors_to_current_scene, 32, "trp_powell_peasant", 6),
         (add_visitors_to_current_scene, 34, "trp_libra_hitman", 1),#权厄之秤的信使

         (try_begin),
            (lt, "$mayvis_quest_phase", 1),
            (add_visitors_to_current_scene, 28, "trp_npc19", 1),#梅薇丝
         (try_end),

         (entry_point_get_position, pos1, 30),#剧情触发点
         (set_spawn_position, pos1),
         (spawn_scene_prop, "spr_barrier_16m"),
         (assign, "$film_prop_instance_2", reg0),
       ]),


      (0.1, 0, 0,#剧情触发
       [
         (le, "$g_film_state", 0),
         (le, "$g_film_cam", 0),
         (le, "$g_film_dialog", 0),
         (ge, "$film_prop_instance_1", 0),
         (ge, "$film_prop_instance_2", 0),
       ],
       [
         (try_begin),
            (lt, "$mayvis_quest_phase", 1),
            (ge, "$film_prop_instance_1", 0),
            (ge, "$mission_player_agent", 0),
            (scene_prop_has_agent_on_it, "$film_prop_instance_1", "$mission_player_agent"),#玩家到达指定位置
            (assign, "$mayvis_quest_phase", 1),
            (start_mission_conversation, "trp_npc19"),
         (else_try),
            (eq, "$mayvis_quest_phase", 2),
            (neg|conversation_screen_is_active),
            (entry_point_get_position, pos1, 18),
            (agent_set_scripted_destination_no_attack, "$film_character_1", pos1, 0, 1),#走向后巷
            (agent_set_speed_limit, "$film_character_1", 3),
         (else_try),
            (eq, "$mayvis_quest_phase", 3),
            (neg|conversation_screen_is_active),
            (reset_mission_timer_c),
            (assign, "$g_film_dialog", 1),
            (agent_fade_out, "$film_character_1"),
            (agent_set_animation, "$film_character_1", "anim_lesaff_square_pos_3", 0),#后退离场
            (assign, "$mayvis_quest_phase", 4),
         (try_end),

         (try_begin),
            (eq, "$current_startup_quest_phase", 5),
            (ge, "$film_prop_instance_2", 0),
            (ge, "$mission_player_agent", 0),
            (scene_prop_has_agent_on_it, "$film_prop_instance_2", "$mission_player_agent"),#玩家到达指定位置
            (reset_mission_timer_c),
            (mission_cam_set_mode, 1),
            (assign, "$g_film_state", 1),#重新开始动画
            (assign, "$g_film_cam", 3),
            (assign, "$g_film_dialog", 8),
            (show_object_details_overlay, 0),
            (agent_set_no_dynamics, "$mission_player_agent", 1),
            (assign, "$current_startup_quest_phase", 6),
         (else_try),
            (eq, "$current_startup_quest_phase", 7),
            (agent_get_position, pos1, "$film_character_8"),
            (agent_get_position, pos2, "$mission_player_agent"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (try_begin),
               (ge, ":cur_distance", 3),
               (agent_set_scripted_destination, "$film_character_8", pos2, 1),
            (else_try),
               (agent_clear_scripted_mode, "$film_character_8"),
               (start_mission_conversation, "trp_libra_hitman"),
           (try_end),
         (else_try),
            (eq, "$current_startup_quest_phase", 8),
            (neg|conversation_screen_is_active),
            (finish_mission),
            (assign, "$g_player_rank", 8),
            (assign, "$g_player_procession", 9),#平民区
            (assign, "$g_current_rank", "$g_player_rank"),
            (assign, "$g_current_procession", "$g_player_procession"),
            (jump_to_menu, "mnu_center_new"),
         (try_end),
       ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@现 在 不 能 离 开 。 "),
       ]),
    ]
  ),


  (
    "lesaff_underworld_stronghold",0,-1, #开局剧情：和权厄之秤会谈
     "Lesaff Street Execution",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse|af_override_weapons|af_require_civilian,0,1,[]),#分舵主
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse,0,1,[]),
      (5, mtef_visitor_source,af_override_horse,0,1,[]),
      (6, mtef_visitor_source,af_override_horse,0,1,[]),
      (7, mtef_visitor_source,af_override_horse,0,1,[]),
      (8, mtef_visitor_source,af_override_horse,0,1,[]),
      (9, mtef_visitor_source,af_override_horse,0,1,[]),
      (10, mtef_visitor_source,af_override_horse,0,1,[]),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [], #准备过场动画
       [
       (reset_mission_timer_c),
       (set_fog_distance, 50, 0xC4C4C4),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_anne_laure_deschamps"),#分舵主
            (assign, "$film_character_1", ":agent_no"),
            (agent_set_animation, ":agent_no", "anim_lesaff_underworld_stronghold_1", 0),#坐
         (else_try),
            (eq, ":troop_no", "trp_libra_spy"),
            (agent_set_animation, ":agent_no", "anim_lesaff_square_pos_1", 0),#靠墙
         (try_end),
         ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (try_begin),
           (lt, "$current_startup_quest_phase", 11),#还未对话
           (display_message, "@现 在 不 能 离 开 。 "),
        (else_try),
           (finish_mission),
           (mission_enable_talk),
           (change_screen_return),
           (str_store_party_name_link, s1, "p_libra_smuggle_wharf"),
           (str_store_string, s2, "@权 厄 之 秤 要 挟 你 执 行 一 项 计 划 — — 接 近 公 爵 之 女 、 下 一 任 公 爵 ， 为 此 你 需 要 杀 进 {s1}， 解 救 其 被 绑 架 的 密 友 。 你 觉 得 这 背 后 应 该 还 有 更 大 的 阴 谋 ， 但 目 前 你 别 无 它 法 ， 只 能 遵 从 。 第 一 步 ， 你 需 要 去 注 册 一 个 冒 险 者 身 份 。 "),
           (add_quest_note_from_sreg, "qst_game_start_quest", 4, s2, 1),
           (call_script, "script_set_quest_zone", "qst_game_start_quest", "p_town_4", 9, 8, 1),#设置任务地点
           (display_message, "str_quest_log_updated"),
        (try_end),
       ]),
    ]
  ),


  (
    "libra_smuggle_wharf_2",mtf_battle_mode,charge, #开局剧情：重返码头
     "Libra Smuggle Wharf",
    [
      (0, mtef_visitor_source|mtef_team_1,af_override_horse, 0, 1,[]),#玩家
      (1, mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
      (2, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (3, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (4, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (5, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (6, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (7, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (8, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (9, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (10, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (11, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (12, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (13, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (14, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (15, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (16, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (17, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (18, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (19, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (20, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (21, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (22, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (23, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (24, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (25, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (26, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (27, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (28, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (29, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (30, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (31, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
      (32, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),
    ],
     AoM_battle_triggers + AoM_inflitration_triggers + [
      common_battle_init_banner,

      (ti_after_mission_start, 0, 0, [], 
       [
       (assign, "$environment_visibility", 100),#能见度
       ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@前 往 出 口 才 能 逃 离 。 "),
       ]),

      (0, 0, 0,
       [
         (main_hero_fallen),
         (finish_mission),
         (jump_to_menu, "mnu_death_end"),
       ],
       [],),
    ]
  ),


  (
    "libra_smuggle_wharf_stronghold",mtf_battle_mode,charge, #开局剧情：码头要塞战斗
     "Libra Smuggle Wharf Stronghold",
    [
      (0, mtef_visitor_source|mtef_team_1,af_override_horse, 0, 1,[]),
      (1, mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source|mtef_team_2,af_override_horse,0,1,[]),#权厄之秤杀手
      (3, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),#范伦汀娜
    ],
     AoM_battle_triggers + boss_triggers_libra_hitman + [
      common_battle_init_banner,

      (ti_after_mission_start, 0, 0, [], #启动过场动画
       [
         (assign, "$g_film_dialog", 1),
         (reset_mission_timer_c),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_libra_hitman"),#权厄之秤杀手
            (assign, "$mission_boss_1", ":agent_no"),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (this_or_next|gt, "$g_film_state", 0),
         (this_or_next|gt, "$g_film_cam", 0),
         (gt, "$g_film_dialog", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#对话
         (try_begin),
            (eq, "$g_film_dialog", 1),
            (is_between, ":cur_time", 1000, 5000),
            (str_store_string, s67, "@等 等 ， 是 你 ？ 我 们 不 是 已 经 … … "),
            (call_script, "script_start_conversation_battle", "$mission_boss_1"),
            (assign, "$g_film_dialog", 2),
         (else_try),
            (eq, "$g_film_dialog", 2),
            (is_between, ":cur_time", 5000, 8000),
            (str_store_string, s67, "@你 想 干 什 么 ？ 该 死 ， 该 死 ！ "),
            (call_script, "script_start_conversation_battle", "$mission_boss_1"),
            (assign, "$g_film_dialog", 3),
         (else_try),
            (eq, "$g_film_dialog", 3),
            (gt, ":cur_time", 8000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (try_end),
       ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@现 在 不 能 离 开 。 "),
       ]),

      (3, 0, 0,#检测倒地
       [
         (try_begin),
            (main_hero_fallen),
            (finish_mission),
            (jump_to_menu, "mnu_death_end"),#玩家死亡
         (else_try),
            (eq, "$current_startup_quest_phase", 12),
            (ge, "$mission_boss_1", 0),#boss刷出后
            (neg|agent_is_alive, "$mission_boss_1"),#胜利
            (assign, "$current_startup_quest_phase", 13),
            (mission_enable_talk),
         (try_end),
       ],
       []),
    ]
  ),



  (
    "champion_auction_mission",0,-1, #支线剧情：冠军拍卖
     "Champion Auction",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse,0,1,[]),
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse,0,1,[]),
      (5, mtef_visitor_source,af_override_horse,0,1,[]),
      (6, mtef_visitor_source,af_override_horse,0,1,[]),
      (7, mtef_visitor_source,af_override_horse,0,1,[]),
      (8, mtef_visitor_source,af_override_horse,0,1,[]),#迎接者
      (9, mtef_visitor_source,af_override_horse,0,1,[]),#拍卖员
      (10, mtef_visitor_source,af_override_horse,0,1,[]),
      (11, mtef_visitor_source,af_override_horse,0,1,[]),
      (12, mtef_visitor_source,af_override_horse,0,1,[]),
      (13, mtef_visitor_source,af_override_horse,0,1,[]),
      (14, mtef_visitor_source,af_override_everything,0,1,[itm_chains_full]),#俘虏
      (15, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_party_mask]),
      (16, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_steel_mask]),
      (17, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_beak_mask]),
      (18, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_party_mask]),
      (19, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_steel_mask]),
      (20, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_party_mask]),
      (21, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_beak_mask]),
      (22, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_beak_mask]),
      (23, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_steel_mask]),
      (24, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_party_mask]),
      (25, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_party_mask]),
      (26, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_steel_mask]),
      (27, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_party_mask]),
      (28, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_steel_mask]),
      (29, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_beak_mask]),
      (30, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[itm_steel_mask]),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_after_mission_start, 0, 0, [], #启动过场动画
       [
       (assign, "$g_film_state", 1),
       (try_begin),
          (check_quest_active, "qst_champion_auction"),
          (assign, "$g_film_cam", 1),#展示全景
          (mission_cam_set_mode, 1),
          (reset_mission_timer_c),
       (try_end),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_libra_slave_merchant"),#看守者
            (agent_set_is_alarmed, ":agent_no", 1),
            (agent_set_wielded_item, ":agent_no", "itm_practice_bow_2"),
         (else_try),
            (eq, ":troop_no", "trp_libra_slave_catching_cavalry"),#拍卖员
            (assign, "$film_character_1", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_sword_sister"),#接待员
            (assign, "$film_character_2", ":agent_no"),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (this_or_next|gt, "$g_film_state", 0),
         (this_or_next|gt, "$g_film_cam", 0),
         (gt, "$g_film_dialog", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#动作等
         (try_begin),
            (eq, "$g_film_state", 1),
            (gt, ":cur_time", 500),
            (try_for_agents, ":agent_no"),
               (agent_is_human, ":agent_no"),
               (agent_is_alive, ":agent_no"),
               (agent_get_entry_no, ":entry_no", ":agent_no"),
               (is_between, ":entry_no", 15, 31),#买家
               (agent_set_animation, ":agent_no", "anim_champion_auction_pos_1", 0),
            (try_end),
            (assign, "$g_film_state", 0),
         (try_end),
#镜头
         (try_begin),
            (eq, "$g_film_cam", 1),#全景
            (le, ":cur_time", 6000),
            (entry_point_get_position, pos1, 31),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_x, pos1, 100),
            (mission_cam_animate_to_position, pos1, 6000, 1),
            (str_store_string, s67, "@地 下 奴 隶 拍 卖 所 "),
            (assign, "$g_scene_name", 1),
            (start_presentation, "prsnt_total_battle_interface"),
            (agent_set_no_dynamics, "$mission_player_agent", 1),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),#结束
            (gt, ":cur_time", 6000),
            (assign, "$g_scene_name", -1),#关停地名展示
            (mission_cam_set_mode, 0),
            (agent_set_no_dynamics, "$mission_player_agent", 0),
            (assign, "$g_film_cam", 0),
         (try_end),
#对话
         (try_begin),
            (eq, "$g_film_dialog", 1),
            (is_between, ":cur_time", 2000, 6000),
            (str_store_string, s67, "@那 么 ， 现 在 拍 卖 开 始 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 2),
         (else_try),
            (eq, "$g_film_dialog", 2),
            (is_between, ":cur_time", 6000, 12000),
            (store_random_in_range, reg10, 40, 60),
            (assign, "$champion_auction_caculate_money", reg10),
            (store_random_in_range, reg11, 7, 15),
            (assign, "$champion_auction_add_money", reg11),
            (str_store_string, s67, "@今 天 的 商 品 ， 曾 经 在 竞 技 场 中 取 得 {reg10}场 胜 利 ， 最 多 连 胜 {reg11}场 ， 在 方 圆 百 里 的 贱 民 中 都 无 人 不 知 ， 无 人 不 晓 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 3),
         (else_try),
            (eq, "$g_film_dialog", 3),
            (is_between, ":cur_time", 12000, 17000),
            (val_mul, "$champion_auction_caculate_money", 50),
            (assign, reg10, "$champion_auction_caculate_money"),
            (val_div, "$champion_auction_add_money", 7),
            (val_mul, "$champion_auction_add_money", 100),
            (assign, reg11, "$champion_auction_add_money"),
            (str_store_string, s67, "@现 在 ， 让 我 们 吞 吃 这 位 英 雄 的 一 切 吧 。 起 拍 价 {reg10}， 每 次 加 价 不 能 低 于 {reg11}。 各 位 来 宾 ， 请 开 始 吧 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 4),
         (else_try),
            (eq, "$g_film_dialog", 4),
            (gt, ":cur_time", 15000),
            (reset_mission_timer_c),
            (assign, "$g_film_dialog", 5),
         (else_try),
            (is_between, "$g_film_dialog", 5, 8),
            (store_sub, ":time_count", "$g_film_dialog", 5),
            (val_mul, ":time_count", 2000),
            (gt, ":cur_time", ":time_count"),
            (store_add, ":count_no", "$champion_auction_add_money", 300),
            (store_random_in_range, ":add_no", "$champion_auction_add_money", ":count_no"),
            (val_div, ":add_no", 10),
            (val_mul, ":add_no", 10),
            (val_add, "$champion_auction_caculate_money", ":add_no"),
            (assign, reg10, "$champion_auction_caculate_money"),
            (str_store_string, s67, "@{reg10} ！ "),
            (store_random_in_range, ":entry_no", 15, 31),
            (try_for_agents, ":agent_no"),
               (agent_is_human, ":agent_no"),
               (agent_is_alive, ":agent_no"),
               (agent_get_entry_no, ":agent_entry_no", ":agent_no"),
               (eq, ":entry_no", ":agent_entry_no"),#买家
               (call_script, "script_start_conversation_battle", ":agent_no"),
            (try_end),
            (val_add, "$g_film_dialog", 1),
         (else_try),
            (eq, "$g_film_dialog", 8),
            (gt, ":cur_time", 6000),
            (call_script, "script_start_conversation_battle", -1),
            (agent_get_troop_id, ":troop_no", "$film_character_1"),
            (start_mission_conversation, ":troop_no"),
            (assign, "$g_film_dialog", 0),
         (else_try),
            (eq, "$g_film_dialog", 9),
            (gt, ":cur_time", 2000),
            (neg|conversation_screen_is_active),
            (agent_get_troop_id, ":troop_no", "$film_character_2"),
            (start_mission_conversation, ":troop_no"),
         (try_end),
       ]),

      (0.1, 0, 0,#剧情触发
       [
         (le, "$g_film_state", 0),
         (le, "$g_film_cam", 0),
         (le, "$g_film_dialog", 0),
       ],
       [
         (eq, "$champion_auction_quest_phase", 1),
         (agent_get_position, pos1, "$film_character_2"),
         (agent_get_position, pos2, "$mission_player_agent"),
         (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
         (le, ":cur_distance", 2),
         (assign, "$champion_auction_quest_phase", 2),
         (agent_get_troop_id, ":troop_no", "$film_character_2"),
         (start_mission_conversation, ":troop_no"),
       ]),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [(eq, 0, 1)],
       [
        (finish_mission),
        (mission_enable_talk),
        (change_screen_return),
       ]),
    ]
  ),


  (
    "champion_auction_battle",mtf_battle_mode,charge, #支线剧情：冠军拍卖的战斗部分
     "Champion Auction Battle.",
    [
     (0, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (1, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (2, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (3, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (4, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (5, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (6, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (7, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (8, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (9, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (10, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (11, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (12, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (13, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (14, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (15, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (16, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (17, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (18, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (19, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (20, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (21, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (22, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (23, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (24, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (25, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (26, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (27, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (28, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (29, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (30, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (31, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (32, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),#玩家
     (33, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (34, mtef_visitor_source|mtef_team_2, af_override_horse|af_override_weapons, aif_start_alarmed, 1, [itm_fake_halberd]),#对手
     (35, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (36, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (37, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (38, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (39, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (40, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (41, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (42, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (43, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (44, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (45, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (46, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (47, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (48, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (49, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (50, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (51, mtef_visitor_source, af_override_horse, 0, 1, []),
     (52, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (53, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (54, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (55, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (56, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (57, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (58, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (59, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
    ],
     AoM_battle_triggers + boss_triggers_confederation_gladiator_champion + boss_triggers_zela + [
      common_battle_init_banner,

      (ti_after_mission_start, 0, 0, [], #启动过场动画
       [
       (assign, "$g_film_dialog", 1),
       (reset_mission_timer_c),
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_confederation_gladiator_champion"),#对手
            (assign, "$mission_boss_1", ":agent_no"),
         (else_try),
            (check_quest_active, "qst_champion_auction"),
            (eq, ":troop_no", "trp_zela"),#对手
            (assign, "$mission_boss_1", ":agent_no"),
         (else_try),
            (quest_slot_eq, "qst_champion_auction", slot_quest_giver_troop, ":troop_no"),#竞技场老板
            (assign, "$film_character_1", ":agent_no"),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (this_or_next|gt, "$g_film_state", 0),
         (this_or_next|gt, "$g_film_cam", 0),
         (gt, "$g_film_dialog", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#对话
         (try_begin),
            (eq, "$g_film_dialog", 1),
            (is_between, ":cur_time", 2000, 6000),
            (troop_get_slot, ":troop_renown", "trp_player", slot_troop_renown),
            (try_begin),
               (ge, ":troop_renown", 1000),
               (str_store_string, s10, "@大 名 鼎 鼎 "),
            (else_try),
               (ge, ":troop_renown", 500),
               (str_store_string, s10, "@小 有 名 气 "),
            (else_try),
               (str_store_string, s10, "@名 不 见 经 传 "),
            (try_end),
            (str_store_troop_name, s11, "trp_player"),
            (str_store_string, s67, "@女 士 们 ， 先 生 们 ， 万 众 瞩 目 的 大 战 ， 由 我 们 {s10}的 {s11}， 挑 战 角 斗 场 的 常 胜 冠 军 ， 如 今 正 式 拉 开 帷 幕 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 2),
         (else_try),
            (eq, "$g_film_dialog", 2),
            (is_between, ":cur_time", 6000, 9000),
            (str_store_string, s67, "@经 过 双 方 同 意 ， 这 将 是 一 场 毫 无 保 留 ， 真 刀 真 枪 的 对 决 ！ 为 鲜 血 欢 呼 吧 ！ "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 3),
         (else_try),
            (eq, "$g_film_dialog", 3),
            (is_between, ":cur_time", 9000, 10000),
            (str_store_string, s67, "@咳 … … 咳 … … "),
            (call_script, "script_start_conversation_battle", "$mission_boss_1"),
            (agent_set_hit_points, "$mission_boss_1", 70, 0),
            (call_script, "script_proceed_state", "$mission_boss_1", "itm_state_strong_toxin", 50),#下毒
            (agent_set_damage_modifier, "$mission_boss_1", 30),
            (assign, "$g_film_dialog", 4),
         (else_try),
            (neg|check_quest_active, "qst_champion_auction"),
            (eq, "$g_film_dialog", 4),
            (gt, ":cur_time", 10000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (else_try),
            (check_quest_active, "qst_champion_auction"),#支线：冠军拍卖
            (eq, "$g_film_dialog", 4),
            (is_between, ":cur_time", 10000, 13000),
            (str_store_string, s67, "@纸 斧 ， 毒 药 ， 殴 打 … … 你 们 这 些 卑 鄙 小 人 ！ 敢 不 敢 和 老 娘 堂 堂 正 正 地 对 决 ！ "),
            (call_script, "script_start_conversation_battle", "$mission_boss_1"),
            (assign, "$g_film_dialog", 5),
         (else_try),
            (check_quest_active, "qst_champion_auction"),#支线：冠军拍卖
            (eq, "$g_film_dialog", 5),
            (is_between, ":cur_time", 13000, 16000),
            (str_store_string, s67, "@我 们 的 冠 军 好 像 说 了 什 么 ， 但 可 惜 没 有 听 清 啊 ， 想 必 是 激 动 人 心 的 豪 言 壮 语 吧 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 6),
         (else_try),
            (check_quest_active, "qst_champion_auction"),#支线：冠军拍卖
            (eq, "$g_film_dialog", 6),
            (is_between, ":cur_time", 16000, 19000),
            (str_store_string, s67, "@我 不 想 死 … … 我 怎 么 可 以 死 在 这 种 地 方 ！ "),
            (call_script, "script_start_conversation_battle", "$mission_boss_1"),
            (assign, "$g_film_dialog", 7),
         (else_try),
            (check_quest_active, "qst_champion_auction"),#支线：冠军拍卖
            (eq, "$g_film_dialog", 7),
            (gt, ":cur_time", 19000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (try_end),
       ]),

      (3, 0, ti_once, [
         (this_or_next|main_hero_fallen),#玩家失败
         (neg|agent_is_alive, "$mission_boss_1"),#胜利
         (assign, "$g_film_dialog", 0),
       ],
      [
         (try_begin),
            (main_hero_fallen),#玩家失败
            (display_message, "@你 成 为 了 百 年 难 遇 的 输 在 冠 军 拍 卖 中 的 买 家 ， 一 举 在 上 层 圈 子 里 成 为 笑 柄 。 不 过 ， 普 罗 大 众 并 不 知 晓 内 幕 ， 在 他 们 看 来 ， 这 不 过 是 一 次 正 常 的 攻 擂 失 败 而 已 。 无 论 如 何 ， 为 表 歉 意 ， 竞 技 场 返 还 了 一 部 分 你 的 钱 。 "),
            (val_div, "$champion_auction_caculate_money", 2),
            (troop_add_gold, "trp_player", "$champion_auction_caculate_money"),
            (finish_mission),
            (check_quest_active, "qst_champion_auction"),
            (call_script, "script_fail_quest", "qst_champion_auction"),
            (add_xp_to_troop, 1000, "trp_player"),
         (else_try),
            (neg|check_quest_active, "qst_champion_auction"),
            (neg|agent_is_alive, "$mission_boss_1"),#胜利
            (display_message, "@昔 日 的 冠 军 倒 在 血 泊 中 ， 观 众 们 寂 静 了 数 秒 ， 随 后 爆 发 了 欢 呼 ， 为 新 的 冠 军 献 上 喝 彩 。 胜 利 、 荣 耀 、 声 名 和 生 命 ， 一 切 都 不 过 是 金 钱 的 游 戏 ， 这 便 是 冠 军 拍 卖 。 "),
            (call_script, "script_change_troop_renown", "trp_player", "$champion_auction_add_money"),
            (finish_mission),
         (else_try),
            (check_quest_active, "qst_champion_auction"),
            (neg|agent_is_alive, "$mission_boss_1"),#胜利
            (neg|conversation_screen_is_active),
            (agent_get_troop_id, ":troop_no", "$film_character_1"),
            (start_mission_conversation, ":troop_no"),
         (try_end),
       ]),	  

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "str_cannot_leave_now"),
       ]),
    ]
  ),


  (
    "common_competition",mtf_battle_mode,charge, #随机事件通用的竞技场比赛mission
     "Common Competition",
    [
     (0, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (1, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (2, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (3, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (4, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (5, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (6, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (7, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (8, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (9, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (10, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (11, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (12, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (13, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (14, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (15, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (16, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (17, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (18, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (19, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (20, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (21, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (22, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (23, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (24, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (25, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (26, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (27, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (28, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (29, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (30, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (31, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (32, mtef_visitor_source, af_override_horse|af_override_weapons, aif_start_alarmed, 1, [itm_heavy_practice_sword]),#玩家
     (33, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (34, mtef_visitor_source, af_override_horse|af_override_weapons, aif_start_alarmed, 1, [itm_heavy_practice_sword]),#对手
     (35, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (36, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (37, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (38, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (39, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (40, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (41, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (42, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (43, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (44, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (45, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (46, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (47, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (48, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (49, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (50, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (51, mtef_visitor_source, af_override_horse, 0, 1, []),
     (52, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (53, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (54, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (55, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (56, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (57, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (58, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
     (59, mtef_visitor_source, af_override_horse, aif_start_alarmed, 1, []),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_inventory_allow", 1),#关停新物品栏
       ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (neq, ":troop_no", "trp_player"),
            (agent_set_team, ":agent_no", 2),
            (assign, "$mission_boss_1", ":agent_no"),
         (else_try),
            (agent_set_team, ":agent_no", 1),
         (try_end),
         ]),

      (3, 0, ti_once, [
         (this_or_next|main_hero_fallen),#玩家失败
         (neg|agent_is_alive, "$mission_boss_1"),#胜利
         (assign, "$g_inventory_allow", 0),#新物品栏恢复默认
       ],
      [
         (try_begin),
            (eq, "$g_current_event", event_small_competition),
            (try_begin),
               (main_hero_fallen),#玩家失败
               (display_message, "@你 在 比 试 中 落 败 了 ， 不 过 胜 败 乃 兵 家 常 事 。 商 会 对 你 的 捧 场 表 示 感 谢 。 "),
               (finish_mission),
               (jump_to_menu,"mnu_center_new"),
            (else_try),
               (display_message, "@你 获 得 了 胜 利 ！ 雷 动 的 掌 声 中 ， 举 办 比 赛 的 商 会 如 约 给 了 你 一 大 笔 奖 金 。 除 此 之 外 ， 你 的 名 声 也 流 传 得 更 广 了 。 "),
               (call_script, "script_change_troop_renown", "trp_player", 10),
               (troop_add_gold, "trp_player", 2000),
               (finish_mission),
               (jump_to_menu,"mnu_center_new"),
            (try_end),
         (try_end),
       ]),	  

      (ti_on_agent_killed_or_wounded, 0, 0, [], #不会死
        [  
         (set_trigger_result, 2),
        ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@你 放 弃 了 比 试 。 "),
        (finish_mission),
        (jump_to_menu,"mnu_center_new"),
       ]),
    ]
  ),



  (
    "third_death_1",mtf_battle_mode,-1, #支线剧情：第三个死，第一次进入加尔村
     "Old Jayer",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse,0,1,[]),#范伦汀娜
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (5, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (6, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (7, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (8, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (9, mtef_visitor_source|mtef_team_2,af_override_horse|af_override_weapons,0,1,[itm_sword_two_handed_b]),#无法安息的士兵
      (10, mtef_visitor_source,af_override_horse,0,1,[]),
    ],
     AoM_battle_triggers + boss_triggers_restless_soldier + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [], #准备
       [
       (scene_set_day_time, 3),
       (set_fog_distance, 30, 0xCCFFFF),
       (play_track, "track_horror_music", 1),
       ]),

      (ti_after_mission_start, 0, 0, [], 
       [
       (assign, "$g_film_state", 1),#展示全景
       (assign, "$g_film_cam", 1),
       (assign, "$g_film_dialog", 1),
       (mission_cam_set_mode, 1),
       (reset_mission_timer_c),
       (mission_enable_talk),
       ]),

      (5, 0, 0,
       [
       (play_track, "track_horror_music", 1),
       ],
       []),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_npc4"),#范伦汀娜
            (assign, "$film_character_1", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_yannick_village_elder"),#扬尼克村长
            (assign, "$film_character_2", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_restless_soldier"),#无法安息的士兵
            (agent_play_sound, ":agent_no", "snd_man_die"),
            (assign, "$film_character_3", ":agent_no"),
            (agent_set_wielded_item, ":agent_no", "itm_sword_two_handed_b"),
            (agent_set_animation, ":agent_no", "anim_third_death_pos_2_1", 0),
         (else_try),
            (neg|troop_is_hero, ":troop_no"),
            (neq, ":troop_no", "trp_restless_soldier"),
            (agent_set_visibility, ":agent_no", 0),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (this_or_next|gt, "$g_film_state", 0),
         (this_or_next|gt, "$g_film_cam", 0),
         (gt, "$g_film_dialog", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#动作
         (try_begin),
            (eq, "$g_film_state", 1),
            (gt, ":cur_time", 6000),
            (agent_set_animation, "$film_character_1", "anim_third_death_pos_1", 0),
            (assign, "$g_film_state", 0),
         (try_end),
#镜头
         (try_begin),
            (eq, "$g_film_cam", 1),#全景
            (le, ":cur_time", 6000),
            (entry_point_get_position, pos1, 10),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_x, pos1, 400),
            (mission_cam_animate_to_position, pos1, 6000, 1),
            (str_store_string, s67, "@加 尔 村 ？ "),
            (assign, "$g_scene_name", 2),
            (start_presentation, "prsnt_total_battle_interface"),
            (agent_set_no_dynamics, "$mission_player_agent", 1),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),
            (gt, ":cur_time", 6000),
            (assign, "$g_scene_name", -1),#关停地名展示
            (entry_point_get_position, pos1, 11),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_z, pos1, -50),
            (mission_cam_animate_to_position, pos1, 3000, 1),
            (assign, "$g_film_cam", 3),
         (else_try),
            (eq, "$g_film_cam", 3),#结束
            (gt, ":cur_time", 9000),
            (mission_cam_set_mode, 0),
            (agent_set_no_dynamics, "$mission_player_agent", 0),
            (assign, "$g_film_cam", 0),
         (try_end),
#对话
         (try_begin),
            (eq, "$g_film_dialog", 1),
            (is_between, ":cur_time", 6500, 9000),
            (str_store_troop_name, s11, "trp_player"),
            (str_store_string, s67, "@这 个 雾 并 不 寻 常 。 {s11}大 人 ， 我 们 小 心 行 事 。 "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 2),
         (else_try),
            (eq, "$g_film_dialog", 2),
            (is_between, ":cur_time", 9000, 12000),
            (str_store_string, s67, "@前 方 好 像 有 人 。 我 们 去 了 解 一 下 情 况 ？ "),
            (call_script, "script_start_conversation_battle", "$film_character_1"),
            (assign, "$g_film_dialog", 3),
         (else_try),
            (eq, "$g_film_dialog", 3),
            (gt, ":cur_time", 12000),
            (call_script, "script_start_conversation_battle", -1),
            (assign, "$g_film_dialog", 0),
         (try_end),
       ]),

      (1, 0, 0,
       [
         (le, "$g_film_state", 0),
         (le, "$g_film_cam", 0),
       ],
       [
         (try_begin),#范伦汀娜
            (neg|conversation_screen_is_active),
            (this_or_next|eq, "$third_death_quest_phase", 1),
            (this_or_next|eq, "$third_death_quest_phase", 5),#去后山
            (eq, "$third_death_quest_phase", 6),#去后山
            (agent_get_position, pos1, "$film_character_1"),
            (agent_get_position, pos2, "$mission_player_agent"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (agent_set_speed_limit, "$film_character_1", 100),
            (try_begin),
               (ge, ":cur_distance", 2),
               (agent_set_scripted_destination, "$film_character_1", pos2, 1),
            (else_try),
               (agent_clear_scripted_mode, "$film_character_1"),
            (try_end),
         (else_try),
            (neg|conversation_screen_is_active),
            (eq, "$third_death_quest_phase", 2),#借一步说话
            (entry_point_get_position, pos1, 12),
            (agent_set_scripted_destination, "$film_character_1", pos1, 1),
            (agent_set_speed_limit, "$film_character_1", 3),
         (else_try),
            (eq, "$third_death_quest_phase", 3),#去来时路上看看
            (entry_point_get_position, pos1, 2),
            (agent_set_scripted_destination, "$film_character_1", pos1, 1),
         (else_try),
            (eq, "$third_death_quest_phase", 4),#回来
            (entry_point_get_position, pos1, 12),
            (agent_set_scripted_destination, "$film_character_1", pos1, 1),
         (else_try),
            (eq, "$third_death_quest_phase", 7),#去后山
            (entry_point_get_position, pos1, 14),
            (agent_set_scripted_destination, "$film_character_1", pos1, 1),
         (else_try),
            (eq, "$third_death_quest_phase", 9),#战后跑过来
            (agent_get_position, pos1, "$mission_boss_1"),
            (agent_set_scripted_destination, "$film_character_1", pos1, 1),
         (try_end),

         (try_begin),#村长
            (neg|conversation_screen_is_active),
            (this_or_next|eq, "$third_death_quest_phase", 6),#去后山
            (eq, "$third_death_quest_phase", 7),#去后山
            (entry_point_get_position, pos1, 13),
            (agent_set_scripted_destination, "$film_character_2", pos1, 1),
         (else_try),
            (neg|conversation_screen_is_active),
            (eq, "$third_death_quest_phase", 9),#战后跑过来
            (agent_get_position, pos1, "$mission_boss_1"),
            (agent_get_position, pos2, "$film_character_2"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (try_begin),
               (ge, ":cur_distance", 8),
               (agent_set_scripted_destination, "$film_character_2", pos1, 1),
            (else_try),
               (agent_clear_scripted_mode, "$film_character_2"),
               (start_mission_conversation, "trp_yannick_village_elder"),
            (try_end),
         (try_end),

         (try_begin),#玩家
            (neg|conversation_screen_is_active),
            (this_or_next|eq, "$third_death_quest_phase", 5),#去后山
            (eq, "$third_death_quest_phase", 6),#去后山
            (entry_point_get_position, pos1, 13),
            (agent_get_position, pos2, "$mission_player_agent"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (le, ":cur_distance", 12),
            (try_for_agents, ":agent_no"),
              (agent_is_human, ":agent_no"),
              (agent_is_alive, ":agent_no"),
              (agent_get_troop_id, ":troop_no", ":agent_no"),
              (neg|troop_is_hero, ":troop_no"),
              (agent_fade_out, ":agent_no", 1),
            (try_end),
            (assign, "$third_death_quest_phase", 7),
            (add_visitors_to_current_scene, 9, "trp_restless_soldier", 1, 2),#无法安息的士兵
            (start_mission_conversation, "trp_npc4"),
         (else_try),
            (neg|conversation_screen_is_active),
            (eq, "$third_death_quest_phase", 7),
            (agent_get_position, pos1, "$film_character_3"),
            (agent_get_position, pos2, "$mission_player_agent"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (le, ":cur_distance", 10),
            (assign, "$third_death_quest_phase", 8),
            (agent_set_team, "$mission_player_agent", 1),#开打
            (agent_set_team, "$film_character_3", 2),
            (assign, "$mission_boss_1", "$film_character_3"),#设置为boss，正式开打
            (agent_set_animation, "$mission_boss_1", "anim_third_death_pos_2_2", 0),
         (try_end),
       ]),

      (3, 0, 0,#检测倒地
       [
         (try_begin),
            (main_hero_fallen),#玩家倒下
            (finish_mission),
            (jump_to_menu, "mnu_death_end"),
         (else_try),
            (eq, "$third_death_quest_phase", 8),
            (ge, "$mission_boss_1", 0),#boss刷出后
            (neg|agent_is_alive, "$mission_boss_1"),#胜利
            (assign, "$third_death_quest_phase", 9),
            (entry_point_get_position, pos1, 13),
            (agent_set_position, "$film_character_2", pos1),
         (try_end),
       ],
       []),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@现 在 不 能 离 开 。 "),
       ]),
    ]
  ),


  (
    "third_death_2",mtf_battle_mode,-1, #支线剧情：第三个死，第二次进入加尔村
     "Old Jayer",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse,0,1,[]),#范伦汀娜
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse,0,1,[]),
      (5, mtef_visitor_source,af_override_horse,0,1,[]),
      (6, mtef_visitor_source,af_override_horse,0,1,[]),
      (7, mtef_visitor_source,af_override_horse,0,1,[]),
      (8, mtef_visitor_source,af_override_horse,0,1,[]),
      (9, mtef_visitor_source,af_override_horse,0,1,[]),
      (10, mtef_visitor_source,af_override_horse,0,1,[]),
      (11, mtef_visitor_source,af_override_horse,0,1,[]),
      (12, mtef_visitor_source,af_override_horse,0,1,[]),
      (13, mtef_visitor_source,af_override_horse,0,1,[]),
      (14, mtef_visitor_source,af_override_horse,0,1,[]),
      (15, mtef_visitor_source,af_override_horse,0,1,[]),
      (16, mtef_visitor_source,af_override_horse|af_override_head,0,1,[]),
      (17, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (18, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (19, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (20, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
      (21, mtef_visitor_source,af_override_horse|af_override_head,0,1,[itm_the_absurd]),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [], #准备
       [
       (scene_set_day_time, 3),
       (set_fog_distance, 30, 0xCCFFFF),
       (play_track, "track_horror_music", 1),
       (mission_disable_talk),
       ]),

      (5, 0, 0,
       [
       (play_track, "track_horror_music", 1),
       ],
       []),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_npc4"),#范伦汀娜
            (assign, "$film_character_1", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_lance_protector_antoine_moro"),#护枪官安托万·莫罗
            (assign, "$film_character_2", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_caravan_master"),#商队头领
            (assign, "$film_character_3", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_restless_sergeant"),#无法安息的士兵
            (assign, "$mission_boss_1", ":agent_no"),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (neg|conversation_screen_is_active),
         (this_or_next|gt, "$g_film_state", 0),
         (this_or_next|gt, "$g_film_cam", 0),
         (gt, "$g_film_dialog", 0),
       ],
       [
         (store_mission_timer_c_msec, ":cur_time"),
#动作等
         (try_begin),
            (eq, "$g_film_state", 1),
            (le, ":cur_time", 4000),
            (agent_set_animation, "$film_character_3", "anim_fall_chest_front", 0),
            (agent_fade_out, "$film_character_3", 1),
            (assign, "$g_film_state", 2),
         (else_try),
            (eq, "$g_film_state", 2),
            (gt, ":cur_time", 4000),
            (agent_get_position, pos1, "$film_character_3"),
            (particle_system_burst, "psys_normal_splash", pos1, 30),
            (set_spawn_position, pos1),
            (spawn_agent, "trp_restless_sergeant"),
            (assign, ":spawn_agent_no", reg0),
            (agent_set_team, ":spawn_agent_no", 2),
            (agent_set_animation, ":spawn_agent_no", "anim_third_death_pos_2_2", 0),
            (agent_set_is_alarmed, "$film_character_2", 1),
            (entry_point_get_position, pos1, 24),
            (agent_set_position, "$film_character_2", pos1),
            (assign, "$g_film_state", 3),
         (else_try),
            (eq, "$g_film_state", 3),
            (gt, ":cur_time", 6000),
            (try_for_agents, ":agent_no"),
              (agent_is_human, ":agent_no"),
              (agent_is_alive, ":agent_no"),
              (agent_get_troop_id, ":troop_no", ":agent_no"),
              (try_begin),
                 (this_or_next|troop_is_hero, ":troop_no"),
                 (eq, ":troop_no", "trp_grenier_wellselected_militia"),#戈兰尼尔精选民兵
                 (agent_set_team, ":agent_no", 1),
              (else_try),
                 (neg|troop_is_hero, ":troop_no"),
                 (neq, ":troop_no", "trp_restless_sergeant"),#无法安息的士兵
                 (entry_point_get_position, pos1, 22),
                 (agent_set_scripted_destination, ":agent_no", pos1, 1),
              (try_end),
            (try_end),
            (assign, "$g_film_state", 0),
         (try_end),
#镜头
         (try_begin),
            (eq, "$g_film_cam", 1),
            (entry_point_get_position, pos1, 23),
            (mission_cam_set_position, pos1),
            (set_fixed_point_multiplier, 100),
            (position_move_y, pos1, -100, 1),
            (mission_cam_animate_to_position, pos1, 3000, 1),
            (assign, "$g_film_cam", 2),
         (else_try),
            (eq, "$g_film_cam", 2),#结束
            (gt, ":cur_time", 6000),
            (mission_cam_set_mode, 0),
            (assign, "$g_film_cam", 0),
         (try_end),
       ]),

      (1, 0, 0,#范伦汀娜跟随
       [
         (le, "$g_film_state", 0),
         (le, "$g_film_cam", 0),
       ],
       [
         (try_begin),#范伦汀娜跟随
            (neg|conversation_screen_is_active),
            (is_between, "$third_death_quest_phase", 12, 14),
            (agent_get_position, pos1, "$film_character_1"),
            (agent_get_position, pos2, "$mission_player_agent"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (agent_set_speed_limit, "$film_character_1", 100),
            (try_begin),
               (ge, ":cur_distance", 2),
               (agent_set_scripted_destination, "$film_character_1", pos2, 1),
            (else_try),
               (agent_clear_scripted_mode, "$film_character_1"),
            (try_end),
         (try_end),

         (try_begin),#护枪官
            (neg|conversation_screen_is_active),
            (eq, "$third_death_quest_phase", 12),
            (agent_get_position, pos1, "$mission_player_agent"),
            (agent_get_position, pos2, "$film_character_2"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (le, ":cur_distance", 5),
            (start_mission_conversation, "trp_lance_protector_antoine_moro"),
         (try_end),
       ]),

      (3, 0, 0,#检测倒地
       [
         (try_begin),
            (main_hero_fallen),#玩家倒下
            (finish_mission),
            (jump_to_menu, "mnu_death_end"),
         (else_try),
            (eq, "$third_death_quest_phase", 14),
            (ge, "$mission_boss_1", 0),#boss刷出后
            (neg|agent_is_alive, "$mission_boss_1"),#胜利
            (assign, "$third_death_quest_phase", 15),
            (show_object_details_overlay, 1),
            (start_mission_conversation, "trp_lance_protector_antoine_moro"),
         (try_end),
       ],
       []),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@现 在 不 能 离 开 。 "),
       ]),
    ]
  ),


  (
    "third_death_3",mtf_battle_mode,-1, #支线剧情：第三个死，第三次进入加尔村
     "Old Jayer",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse,0,1,[]),#范伦汀娜
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse,0,1,[]),
      (5, mtef_visitor_source,af_override_horse,0,1,[]),
      (6, mtef_visitor_source,af_override_horse,0,1,[]),
      (7, mtef_visitor_source,af_override_horse,0,1,[]),
      (8, mtef_visitor_source,af_override_horse,0,1,[]),
      (9, mtef_visitor_source,af_override_horse,0,1,[]),
      (10, mtef_visitor_source,af_override_horse,0,1,[]),
      (11, mtef_visitor_source,af_override_horse,0,1,[]),
      (12, mtef_visitor_source,af_override_horse,0,1,[]),
      (13, mtef_visitor_source,af_override_horse,0,1,[]),
      (14, mtef_visitor_source,af_override_horse,0,1,[]),
      (15, mtef_visitor_source,af_override_horse,0,1,[]),
      (16, mtef_visitor_source,af_override_horse,0,1,[]),
      (17, mtef_visitor_source,af_override_horse,0,1,[]),
      (18, mtef_visitor_source,af_override_horse,0,1,[]),
      (19, mtef_visitor_source,af_override_horse,0,1,[]),
      (20, mtef_visitor_source,af_override_horse,0,1,[]),
      (21, mtef_visitor_source,af_override_horse,0,1,[]),
      (22, mtef_visitor_source,af_override_horse|af_override_head,0,1,[]),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [], #准备
       [
       (scene_set_day_time, 3),
       (set_fog_distance, 50, 0xCCFFFF),
       (play_track, "track_mount_and_blade_title_screen", 1),
       (mission_disable_talk),
       ]),

      (5, 0, 0,
       [
       (play_track, "track_mount_and_blade_title_screen", 1),
       ],
       []),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (try_begin),
            (eq, ":troop_no", "trp_npc4"),#范伦汀娜
            (assign, "$film_character_1", ":agent_no"),
         (else_try),
            (eq, ":troop_no", "trp_lance_protector_antoine_moro"),#护枪官安托万·莫罗
            (assign, "$film_character_2", ":agent_no"),
         (try_end),
         ]),

      (1, 0, 0,#范伦汀娜跟随
       [
         (le, "$g_film_state", 0),
         (le, "$g_film_cam", 0),
       ],
       [
         (try_begin),#范伦汀娜跟随
            (neg|conversation_screen_is_active),
            (eq, "$third_death_quest_phase", 20),
            (agent_get_position, pos1, "$film_character_1"),
            (agent_get_position, pos2, "$mission_player_agent"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (agent_set_speed_limit, "$film_character_1", 100),
            (try_begin),
               (ge, ":cur_distance", 2),
               (agent_set_scripted_destination, "$film_character_1", pos2, 1),
            (else_try),
               (agent_clear_scripted_mode, "$film_character_1"),
            (try_end),
         (try_end),

         (try_begin),#护枪官
            (neg|conversation_screen_is_active),
            (eq, "$third_death_quest_phase", 20),
            (agent_get_position, pos1, "$mission_player_agent"),
            (agent_get_position, pos2, "$film_character_2"),
            (get_distance_between_positions_in_meters, ":cur_distance", pos1, pos2),
            (le, ":cur_distance", 8),
            (start_mission_conversation, "trp_lance_protector_antoine_moro"),
         (try_end),
       ]),

      (3, 0, 0,#检测倒地
       [
         (try_begin),
            (main_hero_fallen),#玩家倒下
            (finish_mission),
            (jump_to_menu, "mnu_death_end"),
         (try_end),
       ],
       []),

      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (display_message, "@现 在 不 能 离 开 。 "),
       ]),
    ]
  ),


  (
    "normal_building_enter",0,-1, #通用的进入建筑
     "Enter Building",
    [
      (0,mtef_visitor_source,0, 0, 1,[]),
      (1, mtef_visitor_source,af_override_horse,0,1,[]),#玩家
      (2, mtef_visitor_source,af_override_horse,0,1,[]),#派系首领
      (3, mtef_visitor_source,af_override_horse,0,1,[]),
      (4, mtef_visitor_source,af_override_horse,0,1,[]),
      (5, mtef_visitor_source,af_override_horse,0,1,[]),
      (6, mtef_visitor_source,af_override_horse,0,1,[]),
      (7, mtef_visitor_source,af_override_horse,0,1,[]),
      (8, mtef_visitor_source,af_override_horse,0,1,[]),
      (9, mtef_visitor_source,af_override_horse,0,1,[]),
      (10, mtef_visitor_source,af_override_horse,0,1,[]),
      (11, mtef_visitor_source,af_override_horse,0,1,[]),
      (12, mtef_visitor_source,af_override_horse,0,1,[]),
      (13, mtef_visitor_source,af_override_horse,0,1,[]),
      (14, mtef_visitor_source,af_override_horse,0,1,[]),
      (15, mtef_visitor_source,af_override_horse,0,1,[]),
      (16, mtef_visitor_source,af_override_horse,0,1,[]),
      (17, mtef_visitor_source,af_override_horse,0,1,[]),
      (18, mtef_visitor_source,af_override_horse,0,1,[]),
      (19, mtef_visitor_source,af_override_horse,0,1,[]),
      (20, mtef_visitor_source,af_override_horse,0,1,[]),
      (21, mtef_visitor_source,af_override_horse,0,1,[]),
      (22, mtef_visitor_source,af_override_horse,0,1,[]),
      (23, mtef_visitor_source,af_override_horse,0,1,[]),
      (24, mtef_visitor_source,af_override_horse,0,1,[]),
      (25, mtef_visitor_source,af_override_horse,0,1,[]),
      (26, mtef_visitor_source,af_override_horse,0,1,[]),
      (27, mtef_visitor_source,af_override_horse,0,1,[]),
      (28, mtef_visitor_source,af_override_horse,0,1,[]),
      (29, mtef_visitor_source,af_override_horse,0,1,[]),
      (30, mtef_visitor_source,af_override_horse,0,1,[]),
    ],
     AoM_battle_triggers + [
      common_battle_init_banner,
      (ti_inventory_key_pressed, 0, 0,
       [],
       [(start_presentation, "prsnt_inventory_new_battle"),
       ]),

      (ti_tab_pressed, 0, 0,
       [],
       [
        (finish_mission),
        (change_screen_return),
       ]),
    ]
  ),

]
