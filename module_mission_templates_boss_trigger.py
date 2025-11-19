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


boss_triggers_megalith_berserker =   [#斯塔胡克岩雷狂战士
      (1, 0, 0,
       [
          (le, "$g_film_state", 0), #过场动画结束才执行，但是对话不受影响
          (le, "$g_film_cam", 0),
          (assign, "$mission_boss_agent", -1),
          (try_begin),
             (ge, "$mission_boss_1", 0),
             (agent_is_alive, "$mission_boss_1"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_1"),
             (eq, ":troop_no", "trp_starkhook_megalith_berserker"),#岩雷狂战士
             (assign, "$mission_boss_agent", "$mission_boss_1"),
          (else_try),
             (ge, "$mission_boss_2", 0),
             (agent_is_alive, "$mission_boss_2"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_2"),
             (eq, ":troop_no", "trp_starkhook_megalith_berserker"),#岩雷狂战士
             (assign, "$mission_boss_agent", "$mission_boss_2"),
          (else_try),
             (ge, "$mission_boss_3", 0),
             (agent_is_alive, "$mission_boss_3"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_3"),
             (eq, ":troop_no", "trp_starkhook_megalith_berserker"),#岩雷狂战士
             (assign, "$mission_boss_agent", "$mission_boss_3"),
          (try_end),
          (ge, "$mission_boss_agent", 0),
       ],
       [
#AI状态获取（主要获取距离相关的信息），信息储存进slot里
#—————————————————————————————————获取—————————————————————————————————
       (call_script, "script_agent_ai_battle_mode", "$mission_boss_agent"),#战斗模式分析
       (assign, ":agent_battle_mode", reg1),

       #目标
       (agent_get_slot, ":target_agent_no", "$mission_boss_agent", slot_ai_target),
       (try_begin),
          (lt, ":target_agent_no", 0),#boss战特供锁定玩家
          (assign, ":target_agent_no", "$mission_player_agent"),
          (agent_set_slot, "$mission_boss_agent", slot_ai_target, ":target_agent_no"),
       (try_end),

       (agent_get_position, pos1, "$mission_boss_agent"),
       (try_begin),
          (ge, ":target_agent_no", 0),
          (call_script, "script_agent_ai_battle_mode", ":target_agent_no"),#战斗模式分析
          (assign, ":target_battle_mode", reg1),
          (agent_get_position, pos2, ":target_agent_no"),
          (get_distance_between_positions_in_meters, ":distance_no", pos1, pos2),#距离
       (try_end),

#AI行为处理
#使用权重进行分析，每一种状态都会影响特定行为的权重，最后执行权重更高的行为。权重和状态的关系另外见表。
#—————————————————————————————————分析—————————————————————————————————
       (assign, ":action_observe", 1000),#观察
       (assign, ":action_sprint", 1000),#冲刺
       (call_script, "script_agent_ai_weight_input", 6, 1000, 1000, 1000, 1000, 1000, 1000),#slot0野盲击，slot1旋刃斩，slot2血星冲击，slot3赤潮战号，slot4血涌战号，slot5血钢战吼

       (try_begin),
          (eq, ":agent_battle_mode", ai_berserker),#双手
          (val_sub, ":action_observe", 20),
          (val_add, ":action_sprint", 60),
       (else_try),
          (eq, ":agent_battle_mode", ai_archer),#步射
          (val_add, ":action_observe", 80),
          (val_sub, ":action_sprint", 10),
          (call_script, "script_agent_ai_weight_input", 6, -1000, -1000, -1000, 70, 70, 70),
       (try_end),

       (try_begin),
          (agent_get_ammo, ":cur_ammo", "$mission_boss_agent", 0),#弹药量
          (ge, ":cur_ammo", 3),
          (val_add, ":action_observe", 10),
          (val_sub, ":action_sprint", 10),
       (try_end),

       (call_script, "script_get_state_count", "$mission_boss_agent", "itm_state_blood_burst"),#血潮汹涌
       (assign, ":bloodburst_count", reg1),
       (try_begin),
          (lt, ":bloodburst_count", 2),
          (call_script, "script_agent_ai_weight_input", 6, 0, 0, -1000, 60, -10, -40),
       (else_try),
          (is_between, ":bloodburst_count", 2, 5),
          (call_script, "script_agent_ai_weight_input", 6, 0, 0, 20, 10, 10, 10),
       (else_try),
          (ge, ":bloodburst_count", 5),
          (call_script, "script_agent_ai_weight_input", 6, -10, -10, 50, -1000, 70, 50),
       (try_end),

       (call_script, "script_get_state_timer", "$mission_boss_agent", "itm_state_war_anger"),#血脉偾张
       (try_begin),
          (gt, reg1, 2),#还剩两秒以上
          (call_script, "script_agent_ai_weight_input", 6, 0, 0, 0, 0, 0, -1000),
       (try_end),

       (try_begin),
          (lt, ":distance_no", 2),
          (val_sub, ":action_observe", 40),
          (call_script, "script_agent_ai_weight_input", 6, 120, 100, 0, -50, -80, -1000),
       (else_try),
          (lt, ":distance_no", 4),
          (call_script, "script_agent_ai_weight_input", 6, 100, 120, 30, 0, 30, 20),
       (else_try),
          (is_between, ":distance_no", 4, 6),
          (call_script, "script_agent_ai_weight_input", 6, -10, -10, 0, 40, 40, 50),
       (else_try),
          (is_between, ":distance_no", 6, 10),
          (val_add, ":action_observe", 10),
          (call_script, "script_agent_ai_weight_input", 6, -1000, -1000, 20, -30, 40, 50),
       (else_try),
          (ge, ":distance_no", 11),
          (val_add, ":action_sprint", 30),
          (call_script, "script_agent_ai_weight_input", 6, -1000, -1000, 50, -60, 40, 50),
       (try_end),

       (try_begin),
          (this_or_next|eq, ":target_battle_mode", ai_archer),
          (eq, ":target_battle_mode", ai_ranger),
          (val_sub, ":action_observe", 70),
          (val_add, ":action_sprint", 80),
          (call_script, "script_agent_ai_weight_input", 3, 0, 0, 70),
       (try_end),

       (try_begin),
          (agent_slot_ge, "$mission_boss_agent", slot_agent_skill_timer, 1),#技能后摇
          (call_script, "script_agent_ai_weight_input", 6, -1000, -1000, -1000, -1000, -1000, -1000),
       (try_end),
#—————————————————————————————————执行—————————————————————————————————
       (try_begin),#下半身
          (gt, ":action_observe", ":action_sprint"),#观察
          (agent_set_speed_limit, "$mission_boss_agent", 5),
       (else_try),
          (agent_set_speed_limit, "$mission_boss_agent", 114514),
       (try_end),

       (call_script, "script_agent_ai_weight_output"),
       (assign, ":chosen_action", reg1),
       (try_begin),
          (agent_slot_eq, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#避免反复执行同一个行动
          (assign, ":chosen_action", 0),
       (try_end),
       (try_begin),#上半身
          (eq, ":chosen_action", 1),#重盲击
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_heavy_casual_attack"),
       (else_try),
          (eq, ":chosen_action", 2),#裂地猛进
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_earthsplitting_charge"),
       (else_try),
          (eq, ":chosen_action", 3),#血星冲击
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_blood_strike"),
       (else_try),
          (eq, ":chosen_action", 4),#赤潮战誓
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_warcy_red_tide"),
       (else_try),
          (eq, ":chosen_action", 5),#血涌战誓
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_warcy_bloodburst"),
       (else_try),
          (eq, ":chosen_action", 6),#血钢战吼
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_warcy_bloodsteel"),
       (try_end),
       (agent_set_slot, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#记录本次执行的动作
       (call_script, "script_agent_ai_weight_clear", 6),#清空
       ]),
    ]



boss_triggers_libra_hitman =   [#权厄之秤杀手
      (1, 0, 0,
       [
          (le, "$g_film_state", 0), #过场动画结束才执行，但是对话不受影响
          (le, "$g_film_cam", 0),
          (assign, "$mission_boss_agent", -1),
          (try_begin),
             (ge, "$mission_boss_1", 0),
             (agent_is_alive, "$mission_boss_1"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_1"),
             (eq, ":troop_no", "trp_libra_hitman"),#权厄之秤杀手
             (assign, "$mission_boss_agent", "$mission_boss_1"),
          (else_try),
             (ge, "$mission_boss_2", 0),
             (agent_is_alive, "$mission_boss_2"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_2"),
             (eq, ":troop_no", "trp_libra_hitman"),#权厄之秤杀手
             (assign, "$mission_boss_agent", "$mission_boss_2"),
          (else_try),
             (ge, "$mission_boss_3", 0),
             (agent_is_alive, "$mission_boss_3"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_3"),
             (eq, ":troop_no", "trp_libra_hitman"),#权厄之秤杀手
             (assign, "$mission_boss_agent", "$mission_boss_3"),
          (try_end),
          (ge, "$mission_boss_agent", 0),
       ],
       [
#AI状态获取（主要获取距离相关的信息），信息储存进slot里
#—————————————————————————————————获取—————————————————————————————————
       (call_script, "script_agent_ai_battle_mode", "$mission_boss_agent"),#战斗模式分析
       (assign, ":agent_battle_mode", reg1),

       #目标
       (agent_get_slot, ":target_agent_no", "$mission_boss_agent", slot_ai_target),
       (try_begin),
          (lt, ":target_agent_no", 0),#boss战特供锁定玩家
          (assign, ":target_agent_no", "$mission_player_agent"),
          (agent_set_slot, "$mission_boss_agent", slot_ai_target, ":target_agent_no"),
       (try_end),

       (agent_get_position, pos1, "$mission_boss_agent"),
       (try_begin),
          (ge, ":target_agent_no", 0),
          (agent_get_position, pos2, ":target_agent_no"),
          (get_distance_between_positions_in_meters, ":distance_no", pos1, pos2),#距离
       (try_end),

#AI行为处理
#使用权重进行分析，每一种状态都会影响特定行为的权重，最后执行权重更高的行为。权重和状态的关系另外见表。
#—————————————————————————————————分析—————————————————————————————————
       (assign, ":action_observe", 1000),#观察
       (assign, ":action_sprint", 1000),#冲刺
       (call_script, "script_agent_ai_weight_input", 3, 1000, 1000, 1000),#slot0撩剑或潜身斩，slot1旋进突击斩或二连穿刺，slot2火弹投掷或风刃射击

       (try_begin),
          (eq, ":agent_battle_mode", ai_saber),#剑盾
          (val_add, ":action_observe", 10),
          (val_add, ":action_sprint", 30),
       (else_try),
          (eq, ":agent_battle_mode", ai_archer),#步射
          (val_add, ":action_observe", 20),
          (val_sub, ":action_sprint", 40),
          (call_script, "script_agent_ai_weight_input", 3, -1000, -1000, -1000),
       (try_end),

       (try_begin),
          (lt, ":distance_no", 2),
          (val_sub, ":action_observe", 40),
          (call_script, "script_agent_ai_weight_input", 3, 100, 0, -1000),
       (else_try),
          (lt, ":distance_no", 4),
          (call_script, "script_agent_ai_weight_input", 3, 0, 80, 0),
       (else_try),
          (ge, ":distance_no", 4),
          (call_script, "script_agent_ai_weight_input", 3, -1000, 0, 120),
       (try_end),

       (try_begin),
          (agent_slot_ge, "$mission_boss_agent", slot_agent_skill_timer, 1),#技能后摇
          (call_script, "script_agent_ai_weight_input", 3, -1000, -1000, -1000),
       (try_end),
#—————————————————————————————————执行—————————————————————————————————
       (try_begin),#下半身
          (gt, ":action_observe", ":action_sprint"),#观察
          (agent_set_speed_limit, "$mission_boss_agent", 5),
       (else_try),
          (agent_set_speed_limit, "$mission_boss_agent", 114514),
       (try_end),

       (call_script, "script_agent_ai_weight_output"),
       (assign, ":chosen_action", reg1),
       (try_begin),
          (agent_slot_eq, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#避免反复执行同一个行动
          (assign, ":chosen_action", 0),
       (try_end),
       (store_random_in_range, ":count_no", 1, 101),
       (try_begin),#上半身
          (eq, ":chosen_action", 1),#撩剑
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_curve_sword"),
       (else_try),
          (eq, ":chosen_action", 1),#潜身斩
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_undercover_slash"),
       (else_try),
          (eq, ":chosen_action", 2),#旋进突击斩
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_spinning_assault_slash"),
       (else_try),
          (eq, ":chosen_action", 2),#二连穿刺
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_double_lunge"),
       (else_try),
          (eq, ":chosen_action", 3),#火弹投掷
          (le, ":count_no", 50),
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_fire_throw"),
       (else_try),
          (eq, ":chosen_action", 3),#风刃射击
          (gt, ":count_no", 50),
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_wind_blade"),
       (try_end),
       (agent_set_slot, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#记录本次执行的动作
       (call_script, "script_agent_ai_weight_clear", 3),#清空
       ]),
    ]



boss_triggers_confederation_gladiator_champion =   [#邦联角斗冠军
      (1, 0, 0,
       [
          (le, "$g_film_state", 0), #过场动画结束才执行，但是对话不受影响
          (le, "$g_film_cam", 0),
          (assign, "$mission_boss_agent", -1),
          (try_begin),
             (ge, "$mission_boss_1", 0),
             (agent_is_alive, "$mission_boss_1"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_1"),
             (eq, ":troop_no", "trp_confederation_gladiator_champion"),#邦联角斗冠军
             (assign, "$mission_boss_agent", "$mission_boss_1"),
          (else_try),
             (ge, "$mission_boss_2", 0),
             (agent_is_alive, "$mission_boss_2"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_2"),
             (eq, ":troop_no", "trp_confederation_gladiator_champion"),#邦联角斗冠军
             (assign, "$mission_boss_agent", "$mission_boss_2"),
          (else_try),
             (ge, "$mission_boss_3", 0),
             (agent_is_alive, "$mission_boss_3"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_3"),
             (eq, ":troop_no", "trp_confederation_gladiator_champion"),#邦联角斗冠军
             (assign, "$mission_boss_agent", "$mission_boss_3"),
          (try_end),
          (ge, "$mission_boss_agent", 0),
       ],
       [
#AI状态获取（主要获取距离相关的信息），信息储存进slot里
#—————————————————————————————————获取—————————————————————————————————
       #目标
       (agent_get_slot, ":target_agent_no", "$mission_boss_agent", slot_ai_target),
       (try_begin),
          (lt, ":target_agent_no", 0),#boss战特供锁定玩家
          (assign, ":target_agent_no", "$mission_player_agent"),
          (agent_set_slot, "$mission_boss_agent", slot_ai_target, ":target_agent_no"),
       (try_end),

       (agent_get_position, pos1, "$mission_boss_agent"),
       (try_begin),
          (ge, ":target_agent_no", 0),
          (agent_get_position, pos2, ":target_agent_no"),
          (get_distance_between_positions_in_meters, ":distance_no", pos1, pos2),#距离
       (try_end),

#AI行为处理
#使用权重进行分析，每一种状态都会影响特定行为的权重，最后执行权重更高的行为。权重和状态的关系另外见表。
#—————————————————————————————————分析—————————————————————————————————
       (assign, ":action_observe", 1000),#观察
       (assign, ":action_sprint", 1000),#冲刺
       (call_script, "script_agent_ai_weight_input", 3, 1000, 1000, 1000),#slot0跳劈或小旋进斩，slot1刃旋舞或盲击，slot2旋退反击斩或旋刃斩

       (try_begin),#距离
          (lt, ":distance_no", 2),
          (val_sub, ":action_observe", 40),
          (call_script, "script_agent_ai_weight_input", 3, 0, 0, 120),
       (else_try),
          (lt, ":distance_no", 3),
          (call_script, "script_agent_ai_weight_input", 3, 0, 120, 0),
       (else_try),
          (is_between, ":distance_no", 3, 5),
          (call_script, "script_agent_ai_weight_input", 3, 120, 0, 0),
       (else_try),
          (ge, ":distance_no", 5),
          (val_add, ":action_sprint", 50),
          (call_script, "script_agent_ai_weight_input", 3, -1000, -1000, -1000),
       (try_end),

       (try_begin),
          (agent_slot_ge, "$mission_boss_agent", slot_agent_skill_timer, 1),#技能后摇
          (call_script, "script_agent_ai_weight_input", 3, -1000, -1000, -1000),
       (try_end),
#—————————————————————————————————执行—————————————————————————————————
       (try_begin),#下半身
          (gt, ":action_observe", ":action_sprint"),#观察
          (agent_set_speed_limit, "$mission_boss_agent", 5),
       (else_try),
          (agent_set_speed_limit, "$mission_boss_agent", 114514),
       (try_end),

       (call_script, "script_agent_ai_weight_output"),
       (assign, ":chosen_action", reg1),
       (try_begin),
          (agent_slot_eq, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#避免反复执行同一个行动
          (assign, ":chosen_action", 0),
       (try_end),
       (store_random_in_range, ":count_no", 1, 101),
       (try_begin),#上半身
          (eq, ":chosen_action", 1),
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_leap_attack"),#跳劈
       (else_try),
          (eq, ":chosen_action", 1),
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_spinning_slash_simple"),#小旋进斩
       (else_try),
          (eq, ":chosen_action", 2),
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_double_slant_slash"),#刃旋舞
       (else_try),
          (eq, ":chosen_action", 2),
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_casual_attack"),#盲击
       (else_try),
          (eq, ":chosen_action", 3),
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_spinning_defense_slash"),#旋退反击斩
       (else_try),
          (eq, ":chosen_action", 3),
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_sweep_away"),#旋刃斩
       (try_end),
       (agent_set_slot, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#记录本次执行的动作
       (call_script, "script_agent_ai_weight_clear", 3),#清空
       ]),
    ]



boss_triggers_zela =   [#泽拉（邦联角斗冠军）
      (1, 0, 0,
       [
          (le, "$g_film_state", 0), #过场动画结束才执行，但是对话不受影响
          (le, "$g_film_cam", 0),
          (assign, "$mission_boss_agent", -1),
          (try_begin),
             (ge, "$mission_boss_1", 0),
             (agent_is_alive, "$mission_boss_1"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_1"),
             (eq, ":troop_no", "trp_zela"),#泽拉
             (assign, "$mission_boss_agent", "$mission_boss_1"),
          (else_try),
             (ge, "$mission_boss_2", 0),
             (agent_is_alive, "$mission_boss_2"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_2"),
             (eq, ":troop_no", "trp_zela"),#泽拉
             (assign, "$mission_boss_agent", "$mission_boss_2"),
          (else_try),
             (ge, "$mission_boss_3", 0),
             (agent_is_alive, "$mission_boss_3"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_3"),
             (eq, ":troop_no", "trp_zela"),#泽拉
             (assign, "$mission_boss_agent", "$mission_boss_3"),
          (try_end),
          (ge, "$mission_boss_agent", 0),
       ],
       [
#AI状态获取（主要获取距离相关的信息），信息储存进slot里
#—————————————————————————————————获取—————————————————————————————————
       #目标
       (agent_get_slot, ":target_agent_no", "$mission_boss_agent", slot_ai_target),
       (try_begin),
          (lt, ":target_agent_no", 0),#boss战特供锁定玩家
          (assign, ":target_agent_no", "$mission_player_agent"),
          (agent_set_slot, "$mission_boss_agent", slot_ai_target, ":target_agent_no"),
       (try_end),

       (agent_get_position, pos1, "$mission_boss_agent"),
       (try_begin),
          (ge, ":target_agent_no", 0),
          (agent_get_position, pos2, ":target_agent_no"),
          (get_distance_between_positions_in_meters, ":distance_no", pos1, pos2),#距离
       (try_end),

#AI行为处理
#使用权重进行分析，每一种状态都会影响特定行为的权重，最后执行权重更高的行为。权重和状态的关系另外见表。
#—————————————————————————————————分析—————————————————————————————————
       (assign, ":action_observe", 1000),#观察
       (assign, ":action_sprint", 1000),#冲刺
       (call_script, "script_agent_ai_weight_input", 3, 1000, 1000, 1000),#slot0跳劈或小旋进斩，slot1刃旋舞或盲击，slot2旋退反击斩或旋刃斩

       (try_begin),#距离
          (lt, ":distance_no", 2),
          (val_sub, ":action_observe", 40),
          (call_script, "script_agent_ai_weight_input", 3, 0, 0, 120),
       (else_try),
          (lt, ":distance_no", 3),
          (call_script, "script_agent_ai_weight_input", 3, 0, 120, 0),
       (else_try),
          (is_between, ":distance_no", 3, 5),
          (call_script, "script_agent_ai_weight_input", 3, 120, 0, 0),
       (else_try),
          (ge, ":distance_no", 5),
          (val_add, ":action_sprint", 50),
          (call_script, "script_agent_ai_weight_input", 3, -1000, -1000, -1000),
       (try_end),

       (try_begin),
          (agent_slot_ge, "$mission_boss_agent", slot_agent_skill_timer, 1),#技能后摇
          (call_script, "script_agent_ai_weight_input", 3, -1000, -1000, -1000),
       (try_end),
#—————————————————————————————————执行—————————————————————————————————
       (try_begin),#下半身
          (gt, ":action_observe", ":action_sprint"),#观察
          (agent_set_speed_limit, "$mission_boss_agent", 5),
       (else_try),
          (agent_set_speed_limit, "$mission_boss_agent", 114514),
       (try_end),

       (call_script, "script_agent_ai_weight_output"),
       (assign, ":chosen_action", reg1),
       (try_begin),
          (agent_slot_eq, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#避免反复执行同一个行动
          (assign, ":chosen_action", 0),
       (try_end),
       (store_random_in_range, ":count_no", 1, 101),
       (try_begin),#上半身
          (eq, ":chosen_action", 1),
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_leap_attack"),#跳劈
       (else_try),
          (eq, ":chosen_action", 1),
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_spinning_slash_simple"),#小旋进斩
       (else_try),
          (eq, ":chosen_action", 2),
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_double_slant_slash"),#刃旋舞
       (else_try),
          (eq, ":chosen_action", 2),
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_casual_attack"),#盲击
       (else_try),
          (eq, ":chosen_action", 3),
          (le, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_spinning_defense_slash"),#旋退反击斩
       (else_try),
          (eq, ":chosen_action", 3),
          (gt, ":count_no", 50),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_sweep_away"),#旋刃斩
       (try_end),
       (agent_set_slot, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#记录本次执行的动作
       (call_script, "script_agent_ai_weight_clear", 3),#清空
       ]),
    ]


boss_triggers_restless_soldier =   [#无法安息的士兵
      (1, 0, 0,
       [
          (le, "$g_film_state", 0), #过场动画结束才执行，但是对话不受影响
          (le, "$g_film_cam", 0),
          (assign, "$mission_boss_agent", -1),
          (try_begin),
             (ge, "$mission_boss_1", 0),
             (agent_is_alive, "$mission_boss_1"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_1"),
             (eq, ":troop_no", "trp_restless_soldier"),#无法安息的士兵
             (assign, "$mission_boss_agent", "$mission_boss_1"),
          (else_try),
             (ge, "$mission_boss_2", 0),
             (agent_is_alive, "$mission_boss_2"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_2"),
             (eq, ":troop_no", "trp_restless_soldier"),#无法安息的士兵
             (assign, "$mission_boss_agent", "$mission_boss_2"),
          (else_try),
             (ge, "$mission_boss_3", 0),
             (agent_is_alive, "$mission_boss_3"),
             (agent_get_troop_id, ":troop_no", "$mission_boss_3"),
             (eq, ":troop_no", "trp_restless_soldier"),#无法安息的士兵
             (assign, "$mission_boss_agent", "$mission_boss_3"),
          (try_end),
          (ge, "$mission_boss_agent", 0),
       ],
       [
#AI状态获取（主要获取距离相关的信息），信息储存进slot里
#—————————————————————————————————获取—————————————————————————————————
       #目标
       (agent_get_slot, ":target_agent_no", "$mission_boss_agent", slot_ai_target),
       (try_begin),
          (lt, ":target_agent_no", 0),#boss战特供锁定玩家
          (assign, ":target_agent_no", "$mission_player_agent"),
          (agent_set_slot, "$mission_boss_agent", slot_ai_target, ":target_agent_no"),
       (try_end),

       (agent_get_position, pos1, "$mission_boss_agent"),
       (try_begin),
          (ge, ":target_agent_no", 0),
          (agent_get_position, pos2, ":target_agent_no"),
          (get_distance_between_positions_in_meters, ":distance_no", pos1, pos2),#距离
       (try_end),

#AI行为处理
#使用权重进行分析，每一种状态都会影响特定行为的权重，最后执行权重更高的行为。权重和状态的关系另外见表。
#—————————————————————————————————分析—————————————————————————————————
       (call_script, "script_agent_ai_weight_input", 4, 1000, 1000, 1000, 1000),#slot0重旋斩或旋退反击斩，slot1火焰横扫，slot2火矢射击， slot3风刃射击或地刺射击

       (try_begin),#距离
          (lt, ":distance_no", 3),
          (call_script, "script_agent_ai_weight_input", 4, 120, 0, 0, 0),
       (else_try),
          (is_between, ":distance_no", 3, 5),
          (call_script, "script_agent_ai_weight_input", 4, 0, 120, 0, 0),
       (else_try),
          (is_between, ":distance_no", 5, 8),
          (call_script, "script_agent_ai_weight_input", 4, 0, 0, 120, 0),
       (else_try),
          (ge, ":distance_no", 8),
          (call_script, "script_agent_ai_weight_input", 4, 0, 0, 0, 120),
       (try_end),

       (try_begin),
          (agent_slot_ge, "$mission_boss_agent", slot_agent_skill_timer, 1),#技能后摇
          (call_script, "script_agent_ai_weight_input", 4, -1000, -1000, -1000, -1000),
       (try_end),
#—————————————————————————————————执行—————————————————————————————————
       (call_script, "script_agent_ai_weight_output"),
       (assign, ":chosen_action", reg1),
       (try_begin),
          (agent_slot_eq, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#避免反复执行同一个行动
          (assign, ":chosen_action", 0),
       (try_end),
       (store_random_in_range, ":count_no", 1, 101),
       (try_begin),#上半身
          (eq, ":chosen_action", 1),
          (le, ":count_no", 80),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_heavy_spin_chop"),#重旋斩
       (else_try),
          (eq, ":chosen_action", 1),
          (gt, ":count_no", 80),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_spinning_defense_slash"),#旋退反击斩
       (else_try),
          (eq, ":chosen_action", 2),
          (call_script, "script_cf_close_combat_technique", "$mission_boss_agent", "itm_active_flame_sweep"),#火焰横扫
       (else_try),
          (eq, ":chosen_action", 3),
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_fire_arrow"),#火矢射击
       (else_try),
          (eq, ":chosen_action", 4),
          (le, ":count_no", 50),
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_wind_blade"),#风刃射击
       (else_try),
          (eq, ":chosen_action", 4),
          (gt, ":count_no", 50),
          (call_script, "script_cf_sorcery_chant_technique", "$mission_boss_agent", "itm_active_stone_shoot"),#地刺射击
       (try_end),
       (agent_set_slot, "$mission_boss_agent", slot_ai_action_number, ":chosen_action"),#记录本次执行的动作
       (call_script, "script_agent_ai_weight_clear", 4),#清空
       ]),
    ]