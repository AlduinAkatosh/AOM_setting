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

from module_scripts_initialized_data import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts_branch = [

###These are some small tools used frequently.
##求积
  ("store_power", [      #use for power operations
         (store_script_param, ":base number", 1),     #底数
         (store_script_param, ":exponent", 2),     #指数
         (assign, ":power", 0),

         (try_begin),
            (le, ":base number", 0),#底数为零
            (assign, ":power", 0), 
         (else_try),
            (eq, ":exponent", 0),#底数非零，指数为零
            (assign, ":power", 1),
         (else_try),
            (eq, ":exponent", 1),#底数非零，指数为1
            (assign, ":power", ":base number"),
         (else_try),
            (assign, ":power", ":base number"),            #if input 10 and 5, this part will be 10*10(count=1)*10(count=2)*10(count=3)*10(count=4)=100000
            (try_for_range, ":count", 1, ":exponent"),
               (lt, ":count", ":exponent"),
               (val_mul, ":power", ":base number"),
            (try_end),
         (try_end),
         (assign, reg1, ":power"),
    ]),

#数位获取
#Digital storage starts from individual bits and is equivalent to 0 bits in power operations. However, the vast majority of references to this script treat each bit as a 1 bit, so the median calculation in this script starts from 1.
  ("get_digital_position", [      #use for get certain digital position
         (store_script_param, ":raw_data", 1),     #raw data原始数据
         (store_script_param, ":digital_position", 2),     #digital position数位     #1表示个位数
                                                                                                            #比如， 原始数据为12745，数位输入3
         (val_sub, ":digital_position", 1),                                                 #":digital_position"=2
         (call_script, "script_store_power", 10, ":digital_position"),
#        (store_pow, ":digit_position_1", 10, ":digital_position"),
         (assign, ":digit_position_1", reg1),                                            #":digital_position_1"=100
         (store_mul, ":digit_position_2", ":digit_position_1", 10),           #":digital_position_2"=1000

         (val_mod, ":raw_data", ":digit_position_2"),                               #":raw_data"=745
         (store_div, reg1, ":raw_data", ":digit_position_1"),                     #reg1=7输出
    ]),

#数位储存
  ("set_digital_position", [      #use for set certain digital position, output raw data
         (store_script_param, ":raw_data", 1),     #原始数据
         (store_script_param, ":digital_position", 2),     #digital position      #1表示个位数
         (store_script_param, ":input", 3),     #input number                   #比如， 原始数据为12345，数位输入3，输入数据为7

         (val_sub, ":digital_position", 1),                                                 #":digital_position"=2
         (call_script, "script_store_power", 10, ":digital_position"),
         (assign, ":digit_position_1", reg1),                                            #":digit_position_1"=100
         (store_mul, ":digit_position_2", ":digit_position_1", 10),          #":digit_position_12"=1000
         (val_mul, ":input", ":digit_position_1"),                                     #":input"=700

         (store_mod, ":raw_data_1", ":raw_data", ":digit_position_1"),   #":raw_data_1"=45
         (val_div, ":raw_data", ":digit_position_2"),                                #":raw_data"=12
         (val_mul, ":raw_data", ":digit_position_2"),                               #":raw_data"=12000
         (val_add, ":raw_data", ":input"),                                                #":raw_data"=12700
         (val_add, ":raw_data", ":raw_data_1"),                                       #":raw_data"=12745输出
         (assign, reg1, ":raw_data"),
    ]),


#小工具
#用于场景，余特殊的scn prop配合，生成一个会小幅度高频位移的透明场景物，用作非常精确计时器，多用于特效的控制
  ("mission_create_timer", [      #使用scene prop里small_timer这个东西做小幅度定时位移，并辅以ti_on_scene_prop_animation_finished，以替代对场景物的遍历
         (store_script_param, ":user_agent_no", 1),
         (store_script_param, ":user_instance_no", 2),#使用者为agent或者场景物
         (store_script_param, ":timer_count", 3),#需要的时间，单位百分之一秒。注意顶点动画的单位是千分之一秒，且注意场景物存在时间。
         (store_script_param, ":stage_count", 4),#有些计时有多个阶段，保留这个参数作备用

         (try_begin),
            (set_fixed_point_multiplier, 100),
            (assign, ":instance_no", -1),
            (try_for_prop_instances, ":scene_prop_no", "spr_small_timer"),#获取是否有现成且未被使用的计时器
               (neg|scene_prop_slot_ge, ":scene_prop_no", slot_instance_agent_used, 0),
               (neg|scene_prop_slot_ge, ":scene_prop_no", slot_instance_prop_used, 0),
               (assign, ":instance_no", ":scene_prop_no"),
            (try_end),

            (try_begin),
               (lt, ":instance_no", 0),#没有现成的
               (init_position, pos62),
               (position_move_z, pos62, -10000),#生成在地下
               (set_spawn_position, pos62),
               (spawn_scene_prop, "spr_small_timer"),
               (assign, ":instance_no", reg0),
               (scene_prop_set_visibility, ":instance_no", 0),
            (try_end),

            (scene_prop_set_slot, ":instance_no", slot_instance_agent_used, -1),
            (scene_prop_set_slot, ":instance_no", slot_instance_prop_used, -1),
            (scene_prop_set_slot, ":instance_no", slot_instance_stage, -1),
            (try_begin),
               (ge, ":user_agent_no", 0),
               (scene_prop_set_slot, ":instance_no", slot_instance_agent_used, ":user_agent_no"),
               (else_try),
               (ge, ":user_instance_no", 0),
               (scene_prop_set_slot, ":instance_no", slot_instance_prop_used, ":user_instance_no"),
            (try_end),
            (scene_prop_set_slot, ":instance_no", slot_instance_stage, ":stage_count"),
            (prop_instance_get_position, pos45, ":instance_no"),
            (prop_instance_animate_to_position, ":instance_no", pos45, ":timer_count"),#通过位移来计时
         (try_end),
    ]),


#小工具
#获取某部队NPC的数量
#输入部队ID，返回数量至reg1
("party_count_hero_num",     #small tool of party
[
      (store_script_param, ":party_no", 1),
      (assign, ":count_no", 0),
      (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
      (try_for_range, ":target_stack", 0, ":num_stacks"), 
         (party_stack_get_troop_id, ":stack_troop", ":party_no", ":target_stack"),
         (troop_is_hero, ":stack_troop"),#英雄
         (val_add, ":count_no", 1),
      (try_end),
      (assign, reg1, ":count_no"),
]),


#小工具
#按等级从高到低重排部队
("party_reorder",     #small tool of party
[
      (store_script_param, ":party_no", 1),
      (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
      (assign, ":last_stack", ":num_stacks"), #记录未调整的堆的数量
      (try_for_range, ":unused", 0, ":num_stacks"),           # find highest-level troop
         (assign, ":best_stack", -1),
         (assign, ":best_level", -999999),
         (try_for_range, ":cur_stack", 0, ":last_stack"),
            (party_stack_get_troop_id, ":cur_troop", ":party_no", ":cur_stack"),
            (neg|troop_is_hero, ":cur_troop"),
            (store_character_level, ":troop_level", ":cur_troop"),
            (gt, ":troop_level", ":best_level"),
            (assign, ":best_level", ":troop_level"), #寻找未处理的兵种中，等级最高的那个
            (assign, ":best_stack", ":cur_stack"),
         (try_end),
         (gt, ":best_stack", -1), #已找到，进入移除和添加阶段
         (party_stack_get_troop_id, ":stack_troop", ":party_no", ":best_stack"),
         (party_stack_get_size, ":stack_size", ":party_no", ":best_stack"),
         (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":best_stack"),
         (party_remove_members, ":party_no", ":stack_troop", ":stack_size"), #移除
         (party_add_members, ":party_no", ":stack_troop", ":stack_size"),
         (party_wound_members, ":party_no", ":stack_troop", ":num_wounded"),
         (val_sub, ":last_stack", 1), #减少待处理的堆数量
      (try_end),
]),


#根据不同mission、不同场景获取当前是否会刷出哪个boss
  ("get_boss", [      #use for get boss id
         (assign, ":boss_1", 0),
         (assign, ":boss_2", 0),
         (assign, ":boss_3", 0),
         (assign, ":distance", 0),   #to caculate in how far will the lifebar display, in the other hand can decide if the lifebar should display

         (store_current_scene, ":cur_scene"),
         (try_begin),
            (check_quest_active, "qst_cemetery_travel"),
            (eq, ":cur_scene", "scn_village_cemetery"),
            (quest_get_slot, ":boss_1", "qst_cemetery_travel", slot_quest_object_troop),
            (assign, ":distance", 30),#30 meter
         (else_try),
            (check_quest_active, "qst_undead_test"),
            (eq, ":cur_scene", "scn_east_castle"),
            (quest_get_slot, ":boss_1", "qst_undead_test", slot_quest_object_troop),
            (assign, ":distance", 30),#30 meter
         (else_try),
            (eq, ":cur_scene", "scn_town_1_arena"),
            (assign, ":boss_1", "trp_starkhook_megalith_berserker"),
            (assign, ":distance", 40),#40 meter
         (try_end),

         (assign, reg1, ":boss_1"),
         (assign, reg2, ":boss_2"),
         (assign, reg3, ":boss_3"),
         (assign, reg4, ":distance"),
    ]),


#小工具
#用于界面，生成样式特殊的按钮
     ("display_troop_image",            #small tool in presetation
        [
         (store_script_param, ":troop_no", 1),     #troop name
         (store_script_param, ":string_no", 2),     #text below
         (store_script_param, ":position_x", 3),     #poxition_x
         (store_script_param, ":position_y", 4),     #poxition_y
         (store_script_param, ":size_x", 5),     #size_x
         (store_script_param, ":size_y", 6),     #size_y

         (val_mul, ":troop_no", 2),     #with weapons
         (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":troop_no"),
         (val_sub, ":position_x", 40),
         (position_set_x, pos1, ":position_x"),
         (position_set_y, pos1, ":position_y"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, ":size_x"),
         (position_set_y, pos1, ":size_y"),
         (overlay_set_size, reg1, pos1),  

         (create_text_overlay, reg2, ":string_no", 0),
         (store_add, ":name_x", ":position_x", 20),
         (store_sub, ":name_y", ":position_y", 15),
         (position_set_x, pos1, ":name_x"),
         (position_set_y, pos1, ":name_y"),
         (overlay_set_position, reg2, pos1),
         (val_mul, ":size_x", 3),
         (val_mul, ":size_y", 3),
         (position_set_x, pos1, ":size_x"),
         (position_set_y, pos1, ":size_y"),
         (overlay_set_size, reg2, pos1),  
      ]),


#计算兵种的新基础血量，公式为35+铁骨×10＋力
     ("store_troop_max_hit_points",            #small tool to caculate troop max hp
        [
         (store_script_param, ":troop_no", 1),

         (assign, reg1, 35),#basic hp
         (store_skill_level, ":return_value", skl_ironflesh, ":troop_no"),
         (val_mul, ":return_value", 10),
         (val_add, reg1, ":return_value"),
         (store_attribute_level, ":return_value", ":troop_no", ca_strength),
         (val_add, reg1, ":return_value"),#35+10*ironflesh+strength
      ]),


     ("mouse_fix_pos_load",            #small tool in presetation
      [
            (create_text_overlay, "$g_presentation_obj_39", "@ ", tf_center_justify|tf_vertical_align_center),
            (create_mesh_overlay, "$g_presentation_obj_38", "mesh_white_plane"),
            (position_set_x, pos1, 50),
            (position_set_y, pos1, 37500),
            (overlay_set_size, "$g_presentation_obj_38", pos1),
            (create_mesh_overlay, "$g_presentation_obj_37", "mesh_white_plane"),
            (position_set_x, pos1, 50000),
            (position_set_y, pos1, 50),
            (overlay_set_size, "$g_presentation_obj_37", pos1),
      ]),


     ("mouse_fix_pos_run",            #small tool in presetation
      [
            (set_fixed_point_multiplier, 1000),
            (mouse_get_position, pos30),
            (position_get_x, reg50, pos30),
            (position_get_y, reg51, pos30),
            
            (position_set_x, pos1, reg50),
            (position_set_y, pos1, 0),
            (overlay_set_position, "$g_presentation_obj_38", pos1),
            (position_set_x, pos1, 0),
            (position_set_y, pos1, reg51),
            (overlay_set_position, "$g_presentation_obj_37", pos1),
            (try_begin),
              (le, reg50, 500),
              (assign, ":x_offset", 70),
            (else_try),
              (assign, ":x_offset", -70),
            (try_end),
            (try_begin),
              (le, reg51, 375),
              (assign, ":y_offset", 20),
            (else_try),
              (assign, ":y_offset", -20),
            (try_end),
            (store_add, ":pos_x", reg50, ":x_offset"),
            (store_add, ":pos_y", reg51, ":y_offset"),
            (position_set_x, pos1, ":pos_x"),
            (position_set_y, pos1, ":pos_y"),
            (overlay_set_position, "$g_presentation_obj_39", pos1),
            (overlay_set_text, "$g_presentation_obj_39", "@({reg50},{reg51})"),
            (overlay_set_color, "$g_presentation_obj_39", 0xFFFFFF),
      ]),

#生成特殊按钮
#输入的xy值为文字的中部，输入文本需事先存入s1
#输出reg1，将reg1赋给某个全局变量即可作为按钮使用。
("create_special_button_overlay",     #small tool in presetation, output reg1
[
      #input s1 as text
      (store_script_param, ":cur_x", 1),
      (store_script_param, ":cur_y", 2),

      (create_text_overlay, reg1, s1, tf_center_justify),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 900),
      (overlay_set_size, reg1, pos1),

      (val_sub, ":cur_x", 54),
      (val_sub, ":cur_y", 7),
      (create_image_button_overlay, reg1, "mesh_button_drop","mesh_button_drop_clicked"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 500),
      (overlay_set_size, reg1, pos1),
]),


#agland
#已知起点pos1和目标pos2，pos1位置坐标不变，角度坐标改为瞄准pos2，得到pos1和距离reg0。主要用于add missile射击，直接将pos1填入starting position一项即可。
  #script_pos_aim_at_pos:
  # Input: arg1 = pos_1, arg2 = pos_2,
  # Output: reg0 = distance_between_pos
  # Input:pos1对准pos2,等同"agent_set_look_target_position ,再读取头部骨骼pos",
  # Output: 两点投影距离
  ("pos_aim_at_pos",
   [
    (store_script_param, ":pos_1", 1),
    (store_script_param, ":pos_2", 2),
   
#还原
    (position_get_x, ":old_x_1", ":pos_1"),
    (position_get_y, ":old_y_1", ":pos_1"),
    (position_get_z, ":old_z_1", ":pos_1"),
    (init_position,":pos_1"),
    (position_set_x, ":pos_1", ":old_x_1"),
    (position_set_y, ":pos_1", ":old_y_1"),
    (position_set_z, ":pos_1", ":old_z_1"),
   
    #看是否重合
    (get_distance_between_positions,":dist",":pos_1",":pos_2"),
   
#水平方向 瞄准
    (position_get_x, ":x_1", ":pos_1"),
    (position_get_y, ":y_1", ":pos_1"),
    (position_get_x, ":x_2", ":pos_2"),
    (position_get_y, ":y_2", ":pos_2"),
    (store_sub, ":off_x", ":x_2", ":x_1"),
    (store_sub, ":off_y", ":y_2", ":y_1"),

    (try_begin),
        (gt, ":dist", 0),   
        #atan 把tan换算成角度 不能用tan,sin,cos,因为没有小数点
        (store_atan2, ":angle_z", ":off_y", ":off_x"),
    (try_end),         
    #将起始点放在x轴上而不是y轴上
    (position_rotate_z,":pos_1",-90),
    #水平瞄准
    (position_rotate_z_floating,":pos_1", ":angle_z"),

#垂直方向 瞄准
    #两点高度差 代码多元化
    (get_sq_distance_between_position_heights,":height_sq",":pos_2",":pos_1"),
    (get_sq_distance_between_positions,":distance_sq",":pos_2",":pos_1"),
    (store_sqrt,":height", ":height_sq"),
    #朝上朝下
    (try_begin),
        (position_get_z, ":z_1", ":pos_1"),
        (position_get_z, ":z_2", ":pos_2"),
        (gt,":z_1",":z_2"),
        (val_mul,":height",-1),
    (try_end),            

    #两点直线距离
    (val_sub,":distance_sq",":height_sq"),
    (store_sqrt,":dist", ":distance_sq"),

    #atan 把tan换算成角度 不能用tan,sin,cos,因为没有小数点
    (try_begin),
        (gt, ":dist", 0),
        (store_atan2, ":angle_x",":height", ":dist"),
    (try_end),
    #垂直瞄准
    (position_rotate_x_floating,":pos_1", ":angle_x"),

#两点直线距离   
    (assign, reg0, ":dist"), 
   ]),


#输入pos1和pos2，返回修改后的pos1
#将pos2的三个旋转角复制到pos1上（或者说是将pos2移动到pos1的位置）
  ("pos_copy_rotation_from_pos",
   [
    (store_script_param, ":pos_1", 1),
    (store_script_param, ":pos_2", 2),
   
    (position_get_x, ":old_x_1", ":pos_1"),
    (position_get_y, ":old_y_1", ":pos_1"),
    (position_get_z, ":old_z_1", ":pos_1"),
    (position_set_x, ":pos_2", ":old_x_1"),
    (position_set_y, ":pos_2", ":old_y_1"),
    (position_set_z, ":pos_2", ":old_z_1"),

    (copy_position, ":pos_1", ":pos_2"),
   ]),


#获取弓所使用的投射物（弓所用的箭矢必然是顺序第一位残留有弹药的箭）
#输入agent；1是箭矢，2是弩矢，3是子弹
#箭矢的ID储存在reg1，slot_no（从0开始）储存在reg2，ammo数量储存在reg3。没获取到的话前两个是-1，弹药量是0
  ("get_missile",
   [
    (store_script_param, ":agent", 1),   
    (store_script_param, ":missile_type", 2),   
    (try_begin),
       (eq, ":missile_type", 1),
       (assign, ":missile_type", itp_type_arrows),
    (else_try),
       (eq, ":missile_type", 2),
       (assign, ":missile_type", itp_type_bolts),
    (else_try),
       (eq, ":missile_type", 3),
       (assign, ":missile_type", itp_type_bullets),
    (try_end),
    (assign, ":count_no_1", -1),
    (assign, ":count_no_2", -1),
    (assign, ":count_no_3", 0),
    (assign, ":limit_no", 4),

    (try_for_range, ":slot_no", 0, ":limit_no"),
       (agent_get_item_slot, ":arrow_no", ":agent", ":slot_no"),
       (gt, ":arrow_no", 0),
       (item_get_type, ":type_no", ":arrow_no"),
       (eq, ":type_no", ":missile_type"),
       (agent_get_item_cur_ammo, ":ammo_no", ":agent", ":slot_no"),
       (gt, ":ammo_no", 0),
       (assign, ":count_no_1", ":arrow_no"),#选中最前一位的箭矢
       (assign, ":count_no_2", ":slot_no"),#获取其最前一位的槽位
       (assign, ":limit_no", -1),#break
    (try_end),
    (try_for_range, ":slot_no", 0, 4),
       (agent_get_item_slot, ":arrow_no", ":agent", ":slot_no"),
       (gt, ":arrow_no", 0),
       (eq, ":count_no_1", ":arrow_no"),
       (agent_get_item_cur_ammo, ":ammo_no", ":agent", ":slot_no"),
       (gt, ":ammo_no", 0),
       (val_add, ":count_no_3", ":ammo_no"),#统计所有和选中箭矢同种的箭矢的数量
    (try_end),
    (assign, reg1, ":count_no_1"),
    (assign, reg2, ":count_no_2"),
    (assign, reg3, ":count_no_3"),
   ]),


###This two script used when player is fight with walkers. May be change in the fulture.
###
      ("become_walker",#killed by walker
      [
        (try_begin),
            (neq, "$your_type", 0x4),
            (troop_set_type,"trp_player",0x4),
            (display_message,"@you become walker!",0xCE0000),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -20),#powell
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", -20),#yishith
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_5", -20),#papal
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_6", -20),#longshu
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_8", -20),#state
        (try_end),
      ]),


      ("change_back_walker",#use holy sand talisman
      [
        (try_begin),
            (neq, "$your_type", 0x4),
            (troop_set_type,"trp_player","$your_type"),
            (display_message,"@you get cured!",0x28FF28),
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 20),#powell
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", 20),#yishith
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_5", 20),#papal
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_6", 20),#longshu
            (call_script, "script_change_player_relation_with_faction", "fac_kingdom_8", 20),#state
            (troop_remove_item,"trp_player","itm_holy_sand_talisman"),
        (try_end),
      ]),


### 支队系统生成支队
###
     ("create_auxiliary_forces",#npc attendants parties
        [
          (store_script_param_1,":npc"), 
          (set_spawn_radius,1),
          (spawn_around_party,"p_main_party","pt_attendants"),
          (assign,":temp_party_id",reg0),
          
          (party_clear,":temp_party_id"),
          (party_add_leader,":temp_party_id", ":npc"),
          (party_set_morale,":temp_party_id", 100),
          (party_set_faction,":temp_party_id", "fac_player_supporters_faction"),
          (party_set_name,":temp_party_id","@Attendant"),
          (party_set_slot,":temp_party_id",slot_party_type,spt_attendant_party),

          (troop_set_slot,":npc",slot_troop_leading_auxiliary, ":temp_party_id"),

          (party_set_extra_text,":temp_party_id", "@Auxiliary"),

          (party_set_slot, ":temp_party_id", slot_party_orders_type, spai_accompanying_army),
          (party_set_slot, ":temp_party_id", slot_party_orders_object, "p_main_party"),
      ]),


     ("caculate_auxiliary_limit",#npc attendants parties
        [
          (store_script_param_1,":party_no"), 

          (party_get_num_companion_stacks,":num_stack",":party_no"),
          (assign, "$auxiliary_limit", 0),
          (try_for_range,":stack_no",0,":num_stack"),
             (party_stack_get_troop_id,":troop_no",":party_no",":stack_no"),
             (troop_is_hero,":troop_no"),
             (store_skill_level, ":limit_add", skl_leadership,":troop_no"),
             (val_add, "$auxiliary_limit", ":limit_add"),
          (try_end),
          (store_skill_level, ":limit_add", skl_leadership,"trp_player"),
          (val_add, "$auxiliary_limit", ":limit_add"),
          (val_mul, "$auxiliary_limit", 12),
          (val_add, "$auxiliary_limit", 30),
          (assign, reg0, "$auxiliary_limit"),
      ]),


     ("troop_in_which_party",#small tool
        [
          (store_script_param_1,":troop_no"), 

          (try_for_parties,":party_no"),
             (party_get_num_companion_stacks,":num_stack",":party_no"),
             (try_for_range,":stack_no",0,":num_stack"),
                 (party_stack_get_troop_id,":member_no",":party_no",":stack_no"),
                 (eq,":member_no",":troop_no"),
                 (assign, ":target_party", ":party_no"),
             (try_end),
          (try_end),
          (assign, reg0, ":target_party"),
      ]),

#####################################################不死者结社相关#################################################
#更换导师（可能需要以新阵营系统更新）
("troop_change_teacher",     #use for necromancer
[
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":teacher_no", 2),

      (str_store_troop_name_link, s8, ":teacher_no"),
      (str_store_troop_name_link, s9, ":troop_no"),
      (troop_set_slot, ":troop_no", slot_troop_teacher, ":teacher_no"),
      (display_log_message, "str_change_teacher"),
]),


#获取结社日常任务
  # script_necromancer_get_quest
  # Input: arg1 = troop_no (of the troop in conversation), arg2 = min_importance (of the quest)
  # Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
  ("necromancer_get_quest",
    [            
      (store_script_param_1, ":giver_troop"),

      (assign, ":giver_center_no", "p_town_17"),
      (try_begin),
          (is_between, ":giver_troop", "trp_inflammation_necromancer", "trp_assistant_1"),#teacher
          (assign, ":quests_begin", "qst_destroy_results"),
          (assign, ":quests_end", "qst_upgrade_of_necromancer"),
      (else_try),
          (is_between, ":giver_troop", "trp_assistant_1", "trp_apprentice_1"),#assistant
          (assign, ":quests_begin", "qst_undead_test"),
          (assign, ":quests_end", "qst_retrieve_materials"),
      (else_try),
          (is_between, ":giver_troop", "trp_apprentice_1", "trp_reception"),#student
          (assign, ":quests_begin", "qst_substitute_homework"),
          (assign, ":quests_end", "qst_escort_necromancer"),
      (try_end),

      (assign, ":result", -1),
	  (assign, ":quest_target_troop", -1),
	  (assign, ":quest_target_center", -1),
	  (assign, ":quest_target_faction", -1),
	  (assign, ":quest_object_faction", -1),
	  (assign, ":quest_object_troop", -1),
	  (assign, ":quest_object_center", -1),
	  (assign, ":quest_target_party", -1),
	  (assign, ":quest_target_party_template", -1),
	  (assign, ":quest_target_amount", -1),
	  (assign, ":quest_target_dna", -1),
	  (assign, ":quest_target_item", -1),
	  (assign, ":quest_importance", 1),
	  (assign, ":quest_xp_reward", 0),
	  (assign, ":quest_gold_reward", 0),
	  (assign, ":quest_credit_reward", 0),
	  (assign, ":quest_convince_value", 0),
	  (assign, ":quest_expiration_days", 0),
	  (assign, ":quest_dont_give_again_period", 0),	 

      (store_random_in_range,":quest_no", ":quests_begin", ":quests_end"),

      (try_begin),
      (neg|check_quest_active,":quest_no"),
      (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
      (try_begin),
           (eq, ":quest_no", "qst_substitute_homework"),
           (troop_get_slot, ":quest_target_troop", ":giver_troop", slot_troop_teacher),
           (store_random_in_range, ":number", 0, 4),
           (try_begin),
              (eq, ":number", 0),
              (assign, ":quest_object_troop", "trp_low_grade_zombie"),
           (else_try),
              (eq, ":number", 1),
              (assign, ":quest_object_troop", "trp_zombie_footman"),
           (else_try),
              (eq, ":number", 2),
              (assign, ":quest_object_troop", "trp_rebirth_skeleton"),
           (else_try),
              (eq, ":number", 3),
              (assign, ":quest_object_troop", "trp_skeleton_warrior"),
           (try_end),
           (assign, ":quest_target_amount", 1),
           (assign, ":quest_xp_reward", 300),
           (assign, ":quest_gold_reward", 500),
           (assign, ":quest_credit_reward", 500),
           (assign, ":quest_expiration_days", 14),
           (assign, ":quest_dont_give_again_period", 7),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_books_reading_help"),
           (assign, ":quest_target_item", "itm_book_necromancer_low"),  
           (assign, ":quest_xp_reward", 300),
           (assign, ":quest_gold_reward", 400),
           (assign, ":quest_credit_reward", 1500),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 15),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_send_a_message"),
           (troop_get_slot, ":quest_target_troop", ":giver_troop", slot_troop_teacher),
           (assign, ":quest_xp_reward", 100),
           (assign, ":quest_gold_reward", 150),
           (assign, ":quest_credit_reward", 300),
           (assign, ":quest_expiration_days", 1),
           (assign, ":quest_dont_give_again_period", 7),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_cemetery_travel"),
           (store_random_in_range, ":number", 0, 3),
           (try_begin),
                (eq, ":number", 0),
                (assign, ":quest_target_center", "p_village_3_12"),
           (else_try),
                (eq, ":number", 1),
                (assign, ":quest_target_center", "p_village_3_13"),
           (else_try),
                (eq, ":number", 2),
                (assign, ":quest_target_center", "p_village_3_14"),
           (try_end),
           (store_random_in_range, ":number", 0, 5),
           (try_begin),
               (eq, ":number", 0),
               (assign, ":quest_object_troop", "trp_zombie_swordman"),
           (else_try),
               (eq, ":number", 1),
               (assign, ":quest_object_troop", "trp_zombie_lancer"),
           (else_try),
               (eq, ":number", 2),
               (assign, ":quest_object_troop", "trp_zombie_destroyer"),
           (else_try),
               (eq, ":number", 3),
               (assign, ":quest_object_troop", "trp_skeleton_swordman"),
           (else_try),
               (eq, ":number", 4),
               (assign, ":quest_object_troop", "trp_skeleton_heavy_archer"),
           (try_end),
           (assign, ":quest_xp_reward", 1000),
           (assign, ":quest_gold_reward", 1500),
           (assign, ":quest_credit_reward", 1000),
           (assign, ":quest_expiration_days", 40),
           (assign, ":quest_dont_give_again_period", 14),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_takeout_specialist"),
           (assign, ":quest_xp_reward", 50),
           (assign, ":quest_gold_reward", 50),
           (assign, ":quest_credit_reward", 100),
           (assign, ":quest_expiration_days", 1),
           (assign, ":quest_dont_give_again_period", 3),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_undead_test"),
           (try_begin),
               (is_between, ":giver_troop", "trp_assistant_1", "trp_apprentice_1"),#assistant
               (store_random_in_range, ":number", 0, 8),
               (try_begin),
                  (eq, ":number", 0),
                  (assign, ":quest_object_troop", "trp_zombie_swordman"),
               (else_try),
                  (eq, ":number", 1),
                  (assign, ":quest_object_troop", "trp_zombie_lancer"),
               (else_try),
                  (eq, ":number", 2),
                  (assign, ":quest_object_troop", "trp_zombie_archer"),
               (else_try),
                  (eq, ":number", 3),
                  (assign, ":quest_object_troop", "trp_zombie_destroyer"),
               (else_try),
                  (eq, ":number", 4),
                  (assign, ":quest_object_troop", "trp_skeleton_swordman"),
               (else_try),
                  (eq, ":number", 5),
                  (assign, ":quest_object_troop", "trp_skeleton_rider"),
               (else_try),
                  (eq, ":number", 6),
                  (assign, ":quest_object_troop", "trp_skeleton_archer"),
               (else_try),
                  (eq, ":number", 7),
                  (assign, ":quest_object_troop", "trp_skeleton_heavy_archer"),
               (try_end),
           (else_try),
               (is_between, ":giver_troop", "trp_apprentice_1", "trp_reception"),#student
               (store_random_in_range, ":number", 0, 4),
               (try_begin),
                  (eq, ":number", 0),
                  (assign, ":quest_object_troop", "trp_low_grade_zombie"),
               (else_try),
                  (eq, ":number", 1),
                  (assign, ":quest_object_troop", "trp_zombie_footman"),
               (else_try),
                  (eq, ":number", 2),
                  (assign, ":quest_object_troop", "trp_rebirth_skeleton"),
               (else_try),
                  (eq, ":number", 3),
                  (assign, ":quest_object_troop", "trp_skeleton_warrior"),
               (try_end),
           (try_end),
           (assign, ":quest_xp_reward", 1000),
           (assign, ":quest_gold_reward", 1000),
           (assign, ":quest_credit_reward", 1000),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 10),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_escort_necromancer"),
           (assign, ":quest_target_center", "p_fiend_nest_3"),
           (assign, ":quest_xp_reward", 1000),
           (assign, ":quest_gold_reward", 2000),
           (assign, ":quest_credit_reward", 1500),
           (assign, ":quest_expiration_days", 60),
           (assign, ":quest_dont_give_again_period", 30),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_urge_learning"),
           (store_random_in_range, ":quest_target_troop", "trp_apprentice_1", "trp_reception"),
           (assign, ":quest_xp_reward", 1000),
           (assign, ":quest_gold_reward", 2000),
           (assign, ":quest_credit_reward", 300),
           (assign, ":quest_expiration_days", 4),
           (assign, ":quest_dont_give_again_period", 10),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_destroy_results"),
           (troop_get_slot, ":teacher_no", "trp_player", slot_troop_teacher),
           (this_or_next|troop_slot_eq, ":giver_troop", slot_troop_teacher, ":teacher_no"),
           (eq, ":giver_troop", ":teacher_no"),
           (call_script, "script_necromancer_quest_get_target", ":giver_troop"),
           (assign, ":quest_target_troop", reg1),
           (store_random_in_range, ":number", 0, 6),
           (store_add, ":quest_target_center", ":number", "p_village_8_1"),
           (call_script, "script_necromancer_quest_get_object_troop", ":quest_target_troop"),
           (assign, ":quest_object_troop", reg1),
           (assign, ":quest_xp_reward", 1200),
           (assign, ":quest_gold_reward", 1500),
           (assign, ":quest_credit_reward", 2000),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 20),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_retrieve_materials"),
           (store_random_in_range, ":quest_target_center", "p_town_1", "p_town_16"),
           (assign, ":quest_xp_reward", 1000),
           (assign, ":quest_gold_reward", 1500),
           (assign, ":quest_credit_reward", 1500),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 30),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_solve_the_patrol"),
           (assign, ":quest_xp_reward", 1000),
           (assign, ":quest_gold_reward", 1500),
           (assign, ":quest_credit_reward", 2000),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 30),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_bring_disaster"),
           (troop_slot_eq, "trp_player", slot_troop_teacher, ":giver_troop"),
           (call_script, "script_necromancer_quest_get_target", ":giver_troop"),
           (assign, ":quest_target_troop", reg1),
           (assign, ":quest_xp_reward", 400),
           (assign, ":quest_gold_reward", 2000),
           (assign, ":quest_credit_reward", 2000),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 30),
           (assign, ":result", ":quest_no"),
      (else_try),
           (eq, ":quest_no", "qst_acquisition_of_resources"),
           (store_random_in_range, ":quest_target_item", "itm_salt", "itm_raw_date_fruit"),
           (store_random_in_range, ":quest_target_amount", 4, 8),
           (assign, ":quest_xp_reward", 400),
           (store_mul, ":quest_gold_reward", ":quest_target_amount", 200),
           (assign, ":quest_credit_reward", 500),
           (assign, ":quest_expiration_days", 30),
           (assign, ":quest_dont_give_again_period", 20),
           (assign, ":result", ":quest_no"),
      (try_end),
      (try_end),

      (try_begin),
        (neq, ":result", -1),        
        (quest_set_slot, ":result", slot_quest_target_troop, ":quest_target_troop"),
        (quest_set_slot, ":result", slot_quest_target_center, ":quest_target_center"),
        (quest_set_slot, ":result", slot_quest_object_troop, ":quest_object_troop"),
        (quest_set_slot, ":result", slot_quest_target_faction, ":quest_target_faction"),
        (quest_set_slot, ":result", slot_quest_object_faction, ":quest_object_faction"),
        (quest_set_slot, ":result", slot_quest_object_center, ":quest_object_center"),
        (quest_set_slot, ":result", slot_quest_target_party, ":quest_target_party"),
        (quest_set_slot, ":result", slot_quest_target_party_template, ":quest_target_party_template"),
        (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
        (quest_set_slot, ":result", slot_quest_importance, ":quest_importance"),
        (quest_set_slot, ":result", slot_quest_xp_reward, ":quest_xp_reward"),
        (quest_set_slot, ":result", slot_quest_gold_reward, ":quest_gold_reward"),
        (quest_set_slot, ":result", slot_quest_credit_reward, ":quest_credit_reward"),
        (quest_set_slot, ":result", slot_quest_convince_value, ":quest_convince_value"),
        (quest_set_slot, ":result", slot_quest_expiration_days, ":quest_expiration_days"),
        (quest_set_slot, ":result", slot_quest_dont_give_again_period, ":quest_dont_give_again_period"),
        (quest_set_slot, ":result", slot_quest_current_state, 0),
        (quest_set_slot, ":result", slot_quest_giver_troop, ":giver_troop"),
        (quest_set_slot, ":result", slot_quest_giver_center, ":giver_center_no"),
        (quest_set_slot, ":result", slot_quest_target_dna, ":quest_target_dna"),
        (quest_set_slot, ":result", slot_quest_target_item, ":quest_target_item"),
      (try_end),

      (assign, reg0, ":result"),
  ]),

#获取结社日常任务的目标
  ("necromancer_quest_get_target", [      #a small tool for necromancer quest get target troop
      (store_script_param_1, ":giver_troop"),

      (assign, ":target", 0),
      (try_begin),
           (is_between, ":giver_troop", "trp_assistant_1", "trp_apprentice_1"),
           (store_random_in_range, ":quest_target_troop", "trp_assistant_1", "trp_apprentice_1"),
           (neq, ":quest_target_troop", ":giver_troop"),         # not same assistant
           (troop_get_slot, ":teacher_no", ":giver_troop", slot_troop_teacher),
           (neg|troop_slot_eq, ":quest_target_troop", slot_troop_teacher, ":teacher_no"), #not same clique
           (assign, ":target", ":quest_target_troop"),
      (else_try),
           (is_between, ":giver_troop", "trp_inflammation_necromancer", "trp_turbid_necromancer"),
           (store_random_in_range, ":quest_target_troop", "trp_inflammation_necromancer", "trp_turbid_necromancer"),
           (neq, ":quest_target_troop", ":giver_troop"),         #not same master
           (neg|troop_slot_eq, ":quest_target_troop", slot_troop_teacher, ":giver_troop"),
           (neg|troop_slot_eq, ":giver_troop", slot_troop_teacher, ":quest_target_troop"),
           (assign, ":target", ":quest_target_troop"),
      (try_end),

      (try_begin),
           (gt, ":target", 0),
           (assign, reg1, ":target"),
      (else_try),
           (call_script, "script_necromancer_quest_get_target", ":giver_troop"),
      (try_end),
    ]),

#获取结社日常任务的目标兵种（需要击杀等）
  ("necromancer_quest_get_object_troop", [      #a small tool for necromancer quest get object troop
      (store_script_param_1, ":target_troop"),

      (troop_get_slot, ":clique_no",":target_troop", slot_troop_necromancer_clique),
      (assign, ":object_troop", 0),
      (try_begin),
           (is_between, ":target_troop", "trp_assistant_1", "trp_apprentice_1"),
           (store_random_in_range, ":quest_object_troop", "trp_low_grade_zombie", "trp_new_walker_mission_1"),
           (troop_get_type, ":troop_race", ":quest_object_troop"),
           (val_sub, ":troop_race", 1),
           (eq, ":troop_race", ":clique_no"),
           (store_character_level, ":level_no", ":quest_object_troop"),
           (is_between, ":level_no", 30, 43),
           (assign, ":object_troop", ":quest_object_troop"),
      (else_try),
           (is_between, ":target_troop", "trp_inflammation_necromancer", "trp_turbid_necromancer"),
           (store_random_in_range, ":quest_object_troop", "trp_low_grade_zombie", "trp_new_walker_mission_1"),
           (troop_get_type, ":troop_race", ":quest_object_troop"),
           (val_sub, ":troop_race", 1),
           (eq, ":troop_race", ":clique_no"),
           (store_character_level, ":level_no", ":quest_object_troop"),
           (ge, ":level_no", 43),
           (assign, ":object_troop", ":quest_object_troop"),
      (try_end),

      (try_begin),
           (gt, ":object_troop", 0),
           (assign, reg1, ":object_troop"),
      (else_try),
           (call_script, "script_necromancer_quest_get_object_troop", ":target_troop"),
      (try_end),
    ]),


  ("increase_necromancer_credits", [      #use for necromancer upgarde
      (store_script_param, ":credit_num", 1),

      (assign, reg1, ":credit_num"),
      (val_add, "$necromancer_credits", ":credit_num"),
      (assign, reg2, "$necromancer_credits"),
      (display_message, "@Your_necromancer_credits_increase"),
    ]),


  ("learn_certain_undead", [      #use for unlocking the production of undead
      (store_script_param, ":undead_no", 1),
      (troop_set_slot, ":undead_no", slot_troop_be_learned, 1),
      (str_store_troop_name, s50, ":undead_no"),
      (display_message, "@Learn_undead", 0x0000FF),
    ]),


  ("get_an_unlearned_undead", [      #use for getting an unlearned undead after reading books
      (store_random_in_range, ":troop_no", "trp_farmer", "trp_knight_master_1_1"),
      (try_begin),
         (troop_get_type, ":troop_race", ":troop_no"),
         (this_or_next|eq, ":troop_race", 2),#zombie
         (eq, ":troop_race", 3),#skeleton
         (neg|troop_slot_eq, ":troop_no", slot_troop_be_learned, 1),
         (assign, reg1, ":troop_no"),
      (else_try),
         (call_script, "script_get_an_unlearned_undead"),
      (try_end),
    ]),



#####################################################特殊战技相关#################################################
###Here are some battle concerned scripts 
###
  ("cf_shield_against_common", [      #use for item triggers
        (store_script_param_1, ":defender_no"),
        (store_script_param_2, ":attacker_no"),
        (store_script_param, ":attacker_weapon_no", 3),
        (store_script_param, ":shield_against_coefficient", 4),

        (agent_get_slot, ":blocking_count", ":defender_no", slot_agent_blocking),
        (gt, ":blocking_count", 0),
        (le, ":blocking_count", ":shield_against_coefficient"),

        (agent_is_alive, ":attacker_no"),
        (agent_is_human, ":attacker_no"),
        (agent_get_horse, ":agent_horse", ":attacker_no"),
        (lt, ":agent_horse", 0),

        (item_get_type, ":weapon_type", ":attacker_weapon_no"),
        (neq, ":weapon_type", itp_type_bow),
        (neq, ":weapon_type", itp_type_crossbow),
        (neq, ":weapon_type", itp_type_thrown),
        (neq, ":weapon_type", itp_type_pistol),
        (neq, ":weapon_type", itp_type_musket),

        (agent_set_animation, ":attacker_no", "anim_shield_against"),
        (call_script, "script_proceed_state", ":attacker_no", "itm_state_lose_balance", 18),#1.8秒的增伤时间

        (eq, "$mission_player_agent", ":defender_no"),
        (display_message, "@完 美 格 挡 ！"),
    ]),



#####################################################潜行#################################################
##
#used in infitration related triggers, called per second. As agent_is_in_line_of_sight is an extremely highly space_used operation, limiting its usage as much as possible. If player was witnessed store 1 or 2 in agent slot slot_agent_witness_player.
  ("caculate_player_witnesses", [
      (agent_get_position, pos54, "$mission_player_agent"),
      (assign, ":alarm_level", 0),
      (try_for_agents, ":enemy_no"),
         (neq, ":enemy_no", "$mission_player_agent"),
         (agent_is_alive, ":enemy_no"),
         (agent_is_human, ":enemy_no"),
         (agent_get_position, pos53, ":enemy_no"),


         (try_begin),
            (agent_slot_ge, ":enemy_no", slot_agent_alarmed_level, 3),#警戒等级三的敌人不需要再判断目击，直接就是目击等级2
            (agent_set_slot, ":enemy_no", slot_agent_witness_player, 2),
         (else_try),
            (get_distance_between_positions_in_meters, ":distance", pos54, pos53),
            (eq, "$infiltrate_alarm_level", 3),                      #玩家正在战斗，其他敌人跑过来看发生了什么，目击等级1
            (ge, ":distance", 5),
            (agent_set_slot, ":enemy_no", slot_agent_witness_player, 1),
         (else_try),
            (ge, ":distance", 20),                                                 #距离太远，不需要判断目击
            (agent_set_slot, ":enemy_no", slot_agent_witness_player, 0),
         (else_try),
            (neg|position_is_behind_position, pos54, pos53),#排除背后
            (agent_is_in_line_of_sight, ":enemy_no", pos54),
            (try_begin),
               (is_between, ":distance", 5, 20),                 #玩家在中远处被看见了，目击等级1
               (agent_set_slot, ":enemy_no", slot_agent_witness_player, 1),
            (else_try),
               (lt, ":distance", 5),                                   #玩家在近处被看见了，目击等级2
               (agent_set_slot, ":enemy_no", slot_agent_witness_player, 2),
            (try_end),
         (else_try),
            (agent_set_slot, ":enemy_no", slot_agent_witness_player, 0),
         (try_end),

         (agent_slot_ge, ":enemy_no", slot_agent_alarmed_level, ":alarm_level"),
         (agent_get_slot, ":alarm_level", ":enemy_no", slot_agent_alarmed_level),#获取最高一个守卫的警戒等级，作为整体的警戒等级。
      (try_end),
      (assign, "$infiltrate_alarm_level", ":alarm_level"),
    ]),

#统计全身装备重量
  ("cf_agent_caculate_weight", [
      (store_script_param_1, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (set_fixed_point_multiplier, 1000),
      (assign, ":weight_count", 0),
      (try_begin),
         (neq, ":agent_no", "$mission_player_agent"),
         (try_for_range, ":slot_no", 0, 8),
            (agent_get_item_slot, ":item_no", ":agent_no", ":slot_no"),
            (gt, ":item_no", 0),
            (item_get_weight, ":count_no", ":item_no"),
            (val_add, ":weight_count", ":count_no"),
         (try_end),
      (else_try),
         (eq, ":agent_no", "$mission_player_agent"),#玩家
         (try_for_range, ":slot_no", 2, 8),#箭矢和防具
            (agent_get_item_slot, ":item_no", ":agent_no", ":slot_no"),
            (gt, ":item_no", 0),
            (item_get_weight, ":count_no", ":item_no"),
            (val_add, ":weight_count", ":count_no"),
         (try_end),
         (try_for_range, ":slot_no", slot_agent_weapon_1, slot_agent_weapon_ammo_1),#武器
            (agent_get_item_slot, ":item_no", ":agent_no", ":slot_no"),
            (gt, ":item_no", 0),
            (item_get_weight, ":count_no", ":item_no"),
            (val_add, ":weight_count", ":count_no"),
         (try_end),
         (try_for_range, ":slot_no", ek_accessorise_1, ek_accessorise_1+4),#饰物
            (troop_get_inventory_slot, ":item_no", "trp_player", ":slot_no"),
            (gt, ":item_no", 0),
            (item_get_weight, ":count_no", ":item_no"),
            (val_add, ":weight_count", ":count_no"),
         (try_end),
      (try_end),
      (assign, reg1, ":weight_count"),
    ]),


#计算移动速度（单位分米/s）
  ("cf_agent_caculate_speed", [
      (store_script_param_1, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (set_fixed_point_multiplier, 1000),
      (agent_get_speed, pos1, ":agent_no"),#移动速度
      (position_get_x, ":cur_x", pos1),
      (position_get_y, ":cur_y", pos1),
      (val_mul, ":cur_x", ":cur_x"),
      (val_mul, ":cur_y", ":cur_y"),
      (val_add, ":cur_x", ":cur_y"),
      (val_div, ":cur_x", 1000),
      (store_sqrt, ":speed_count", ":cur_x"),
      (val_div, ":speed_count", 100),
      (assign, reg1, ":speed_count"),
    ]),


#统计隐蔽值，隐蔽值越高越难发现
  ("cf_agent_caculate_hiding_level", [
      (store_script_param_1, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (store_sub, ":hiding_level", 100, "$environment_visibility"),#能见度（在mission处设置）
      (try_begin),
         (ge, "$crouch_mode", 1),
         (val_add, ":hiding_level", 35),#下蹲
      (try_end),
      (try_begin),
         (call_script, "script_cf_agent_caculate_weight", ":agent_no"),#装备重量
         (store_sub, ":weight_count", 10000, reg1),#以10公斤为界
         (val_div, ":weight_count", 1000),
         (val_add, ":hiding_level", ":weight_count"),
      (try_end),
      (try_begin),
         (is_currently_night),
         (val_add, ":hiding_level", 40),#夜晚
      (try_end),

      (try_begin),
         (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_concealing"),#匿踪
         (gt, reg1, 0),                                                                                                                          #success
         (val_mul, reg1, 10),
         (val_add, ":hiding_level", reg1),
      (try_end),

      (try_begin),
         (call_script, "script_cf_agent_caculate_speed", ":agent_no"),#速度
         (assign, ":speed_no", reg1),
         (try_begin),
            (gt, ":speed_no", 0),
            (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_lightly_run"),#轻声奔跑
            (gt, reg1, 0),                                                                                                                          #success
            (assign, ":speed_no", 0),
         (try_end),
         (val_sub, ":hiding_level", ":speed_no"),
      (try_end),
      (assign, reg1, ":hiding_level"),
    ]),


###########################################################主动技能相关###################################################

#主动技能激活
#Check if troop have certain active skill, input troop no and active skill id. Output number as this skill's level
  ("set_troop_active_skill_level", [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":skill_no"),

      (store_sub, ":count_no", ":skill_no", "itm_active_skills_begin"),#count begin from 1
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_active_skill_learned_1),#15 skills in a group

      (troop_get_slot, ":active_skill_count", ":troop_no", ":count_no_group"),
      (call_script, "script_set_digital_position", ":active_skill_count", ":count_no_position", 1),
      (troop_set_slot, ":troop_no", ":count_no_group", reg1),
    ]),


#主动技能激活检测
#Check if troop have certain active skill, input troop no and active skill id. Output number as this skill's level
  ("check_troop_active_skill", [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":skill_no"),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_active_skills_begin"),#count begin from 1
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_active_skill_learned_1),#15 skills in a group

      (troop_get_slot, ":active_skill_count", ":troop_no", ":count_no_group"),
      (try_begin),
         (gt, ":active_skill_count", 0),
         (call_script, "script_get_digital_position", ":active_skill_count", ":count_no_position"),
      (try_end),
#output reg1
    ]),


#查询某技能为某troop启动的第几个主动技能，若已经装填，返回0到5表示槽位，若为装填，返回-1
#输出reg1
  ("check_if_skill_activited_by_troop", [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":skill_no"),
      (assign, reg1, -1),

      (try_for_range, ":count_no", 0, 6),
         (store_add, ":slot_no", ":count_no", slot_troop_active_skill_1),
         (troop_slot_eq, ":troop_no", ":slot_no", ":skill_no"),
         (assign, reg1, ":count_no"),
      (try_end),
    ]),


#——————————————————————————————————主动技能界面相关———————————————————————————————
#主动技能显示（界面相关）
  ("cf_show_active_skill", [
      (store_script_param, ":active_skill_no", 1),
      (gt, ":active_skill_no", 0),

      (str_store_item_name, s1, ":active_skill_no"),
      (str_store_item_name_plural, s2, ":active_skill_no"),
      (overlay_set_text, "$g_presentation_text_5", "@{s1}^{s2}"),

      (set_fixed_point_multiplier, 1000),
      (item_get_weight, reg1, ":active_skill_no"),
      (val_div, reg1, 1000),
      (try_begin),
         (item_has_property, ":active_skill_no", itp_unique),#martial art
         (str_store_string, s1, "str_martial_art"),
         (overlay_set_color, "$g_presentation_text_6", 0xFFFFFF),
         (overlay_set_text, "$g_presentation_text_7", "str_vigour_consume"),
         (overlay_set_color, "$g_presentation_text_7", 0x33CC33),
      (else_try),
         (item_has_property, ":active_skill_no", itp_always_loot),#sorcery
         (str_store_string, s1, "str_sorcery"),
         (overlay_set_color, "$g_presentation_text_6", 0xCCFFFF),
         (overlay_set_text, "$g_presentation_text_7", "str_chant_time_consume"),
         (overlay_set_color, "$g_presentation_text_7", 0xFFFFFF),
      (else_try),
         (item_has_property, ":active_skill_no", itp_always_loot),#magic
         (str_store_string, s1, "str_magic"),
         (overlay_set_color, "$g_presentation_text_6", 0x663399),
         (overlay_set_text, "$g_presentation_text_7", "str_magic_consume"),
         (overlay_set_color, "$g_presentation_text_7", 0x663399),
      (try_end),
      (overlay_set_text, "$g_presentation_text_6", "@{s1}"),

      (try_begin),
         (call_script, "script_check_troop_active_skill", "trp_player", ":active_skill_no"),
         (gt, reg1, 0),
         (overlay_set_display, "$g_presentation_obj_10", 1),
         (store_add, ":overlay_no", "$g_presentation_obj_10", 1),
         (overlay_set_display, ":overlay_no", 1),
      (else_try),
         (overlay_set_display, "$g_presentation_obj_10", 0),
         (store_add, ":overlay_no", "$g_presentation_obj_10", 1),
         (overlay_set_display, ":overlay_no", 0),
      (try_end),
    ]),

#主动技能显示（界面相关）
#specific script
  ("active_skill_mesh_change", [
      (store_script_param_1, ":count_no"),#1 to 6
      (store_script_param_2, ":skill_no"),

      (try_begin),
         (eq, ":count_no", 1),
         (overlay_set_display, "$g_presentation_mesh_1", 0),
         (create_mesh_overlay_with_item_id, "$g_presentation_mesh_1", ":skill_no"),
         (position_set_x, pos1, 435),
         (position_set_y, pos1, 385),
         (overlay_set_position, "$g_presentation_mesh_1", pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, "$g_presentation_mesh_1", pos1),
         (overlay_set_additional_render_height, "$g_presentation_mesh_1", 3),
      (else_try),
         (eq, ":count_no", 2),
         (overlay_set_display, "$g_presentation_mesh_2", 0),
         (create_mesh_overlay_with_item_id, "$g_presentation_mesh_2", ":skill_no"),
         (position_set_x, pos1, 510),
         (position_set_y, pos1, 385),
         (overlay_set_position, "$g_presentation_mesh_2", pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, "$g_presentation_mesh_2", pos1),
         (overlay_set_additional_render_height, "$g_presentation_mesh_2", 3),
      (else_try),
         (eq, ":count_no", 3),
         (overlay_set_display, "$g_presentation_mesh_3", 0),
         (create_mesh_overlay_with_item_id, "$g_presentation_mesh_3", ":skill_no"),
         (position_set_x, pos1, 585),
         (position_set_y, pos1, 385),
         (overlay_set_position, "$g_presentation_mesh_3", pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, "$g_presentation_mesh_3", pos1),
         (overlay_set_additional_render_height, "$g_presentation_mesh_3", 3),
      (else_try),
         (eq, ":count_no", 4),
         (overlay_set_display, "$g_presentation_mesh_4", 0),
         (create_mesh_overlay_with_item_id, "$g_presentation_mesh_4", ":skill_no"),
         (position_set_x, pos1, 660),
         (position_set_y, pos1, 385),
         (overlay_set_position, "$g_presentation_mesh_4", pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, "$g_presentation_mesh_4", pos1),
         (overlay_set_additional_render_height, "$g_presentation_mesh_4", 3),
      (else_try),
         (eq, ":count_no", 5),
         (overlay_set_display, "$g_presentation_mesh_5", 0),
         (create_mesh_overlay_with_item_id, "$g_presentation_mesh_5", ":skill_no"),
         (position_set_x, pos1, 735),
         (position_set_y, pos1, 385),
         (overlay_set_position, "$g_presentation_mesh_5", pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, "$g_presentation_mesh_5", pos1),
         (overlay_set_additional_render_height, "$g_presentation_mesh_5", 3),
      (else_try),
         (eq, ":count_no", 6),
         (overlay_set_display, "$g_presentation_mesh_6", 0),
         (create_mesh_overlay_with_item_id, "$g_presentation_mesh_6", ":skill_no"),
         (position_set_x, pos1, 810),
         (position_set_y, pos1, 385),
         (overlay_set_position, "$g_presentation_mesh_6", pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, "$g_presentation_mesh_6", pos1),
         (overlay_set_additional_render_height, "$g_presentation_mesh_6", 3),
      (try_end),
    ]),



#——————————————————————动作命中判定（涉及多个脚本，但最终只需要使用close_combat_technique）—————————————————

#动作命中判定（获取目标部分）
#Used in triggers of (0, 0, 0) to handle the activation and determination of active skills. The input is the attacker's agent serial number and the number of skills (1 to 6) that will be activated. The skill number will be calculated before the script starts. If it is 0, it means that the active skill activation part in the script will not be activated.
  ("cf_close_combat_technique", [
      (store_script_param_1, ":attacker_agent_no"),
      (store_script_param_2, ":active_skill_no"),

      (agent_is_human, ":attacker_agent_no"),#是人
      (agent_is_alive, ":attacker_agent_no"),

      (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_skill_timer, 1),
      (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_activiting_skill, 1),#当前未使用技能
#武技完成最后一个判定点后就会消除slot_agent_activiting_skill，停止继续判定以节省算力，但slot_agent_skill_timer还会继续运行作为后摇。因此两个都需要检测。
      (assign, ":attacker_anim_no", 0),

#获取目标
      (try_begin),                          #activation part, only working at the point when the button is clicked or ai gets permission.
         (item_has_property, ":active_skill_no", itp_damage_type),#通用的造成伤害型所需要的释放准备
         (try_for_range, ":count_no", 0, 10),
            (store_add, ":slot_no", ":count_no", slot_agent_surrounded_enemy_1),#清空
            (agent_set_slot, ":attacker_agent_no", ":slot_no", -1),
         (try_end),

         (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
         (lt, ":attacker_agent_horse", 0),#马上施放的技能见骑技部分

         (item_get_slot, ":attacker_anim_no", ":active_skill_no", slot_active_skill_attacker_anim),
         (gt, ":attacker_anim_no", 0),                                                                              #获取主动技能动作
         (assign, ":body_area", 0),#全身
         (agent_get_position, pos1, ":attacker_agent_no"),#获取位置

         (set_fixed_point_multiplier, 100),
         (agent_get_team, ":attacker_team_no",  ":attacker_agent_no"),
         (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),
         (gt, ":weapon_no", 0),
         (item_get_weapon_length, ":weapon_length", ":weapon_no"),#cm
         (item_get_weight, ":weapon_weight", ":weapon_no"),
         (agent_set_slot, ":attacker_agent_no", slot_agent_weapon_length, ":weapon_length"),#记录武器长度
#         (val_add, ":weapon_length", 150),

         (assign, ":slot_no", slot_agent_surrounded_enemy_1),                                    #获取目标
         (try_for_agents, ":agent_no", pos1, 700),#7米范围内
            (agent_is_alive,  ":agent_no"),
            (neq, ":attacker_agent_no", ":agent_no"),                                                     #不是进攻者
            (le, ":slot_no", slot_agent_surrounded_enemy_10),                                      #最多命中十人
            (assign, ":continue", 0),
            (try_begin),
               (agent_is_human,  ":agent_no"),#人
               (agent_get_team, ":team_no",  ":agent_no"),
               (teams_are_enemies, ":attacker_team_no", ":team_no"), #敌对
               (assign, ":continue", 1),
            (else_try),
               (neg|agent_is_human,  ":agent_no"),#无主马
               (agent_get_rider, ":rider_agent_no", ":agent_no"),
               (lt, ":rider_agent_no", 0),#have no rider
               (assign, ":continue", 1),
            (else_try),
               (neg|agent_is_human,  ":agent_no"),#有主马
               (ge, ":rider_agent_no", 0),#have rider
               (agent_get_team, ":team_no",  ":rider_agent_no"),
               (teams_are_enemies, ":attacker_team_no", ":team_no"), #敌对骑手
               (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),

            (agent_set_slot, ":attacker_agent_no", ":slot_no", ":agent_no"),
            (val_add, ":slot_no", 1),
         (try_end),

      (else_try),
         (item_has_property, ":active_skill_no", itp_special_type),#有特殊效果
         (try_begin),
            (eq, ":active_skill_no", "itm_active_left_hand_block_arrow"),#左手反箭术
            (assign, ":attacker_anim_no", "anim_left_hand_block_arrow_prepare"),
            (assign, ":timer_count", 8),
            (try_begin),
               (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 1),#盾
               (eq, ":weapon_no", "itm_sadi_dagger"),#萨蒂的匕首
               (val_add, ":timer_count", 4),
            (try_end),
            (call_script, "script_activate_state", ":attacker_agent_no", "itm_state_left_hand_block_arrow", ":timer_count"),
            (assign, ":body_area", 1),#上半身

         (else_try),
            (this_or_next|eq, ":active_skill_no", "itm_active_power_shot"),#拉满弓
            (this_or_next|eq, ":active_skill_no", "itm_active_continuous_shooting"),#三连射
            (this_or_next|eq, ":active_skill_no", "itm_active_multiple_arrow"),#多重箭
            (eq, ":active_skill_no", "itm_active_throwing_arrow"),#投箭
            (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
            (lt, ":attacker_agent_horse", 0),#步行
            (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
            (gt, ":weapon_no", 0),
            (item_get_type, ":type_no", ":weapon_no"),#弓才能用
            (eq, ":type_no", itp_type_bow),
            (agent_get_ammo, ":ammo_count", ":attacker_agent_no", 1),
            (try_begin),
               (eq, ":active_skill_no", "itm_active_power_shot"),#拉满弓
               (ge, ":ammo_count", 1),#至少要留有一发箭矢
               (assign, ":attacker_anim_no", "anim_active_power_shot"),
            (else_try),
               (eq, ":active_skill_no", "itm_active_continuous_shooting"),#三连射
               (ge, ":ammo_count", 3),#至少要留有三发箭矢
               (assign, ":attacker_anim_no", "anim_active_continuous_shot"),
            (else_try),
               (eq, ":active_skill_no", "itm_active_multiple_arrow"),#多重箭
               (ge, ":ammo_count", 5),#至少要留有五发箭矢
               (assign, ":attacker_anim_no", "anim_active_multiple_arrow"),
            (else_try),
               (eq, ":active_skill_no", "itm_active_throwing_arrow"),#投箭
               (ge, ":ammo_count", 1),#至少要留有一发箭矢
               (assign, ":attacker_anim_no", "anim_active_throwing_arrow"),
            (try_end),
            (assign, ":body_area", 0),#全身
            (try_begin),
               (agent_get_slot, ":target_agent_no", ":attacker_agent_no", slot_ai_target),
               (ge, ":target_agent_no", 0),
               (agent_get_bone_position, pos2, ":target_agent_no", hb_thorax, 1),#有目标，射击目标胸口
            (else_try),
               (agent_get_bone_position, pos2, ":attacker_agent_no", hb_thorax, 1),#没有目标
               (agent_get_position, pos6, ":attacker_agent_no"),
               (position_copy_rotation, pos2, pos6),
               (position_move_y, pos2, 100),
            (try_end),
            (agent_set_look_target_position, ":attacker_agent_no", pos2),

         (else_try),
            (eq, ":active_skill_no", "itm_active_flame_sweep"),#火焰横扫
            (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
            (lt, ":attacker_agent_horse", 0),#步行
            (assign, ":attacker_anim_no", "anim_active_flame_sweep"),
            (assign, ":body_area", 0),#全身

         (else_try),
            (eq, ":active_skill_no", "itm_active_blood_strike"),#血星冲击
            (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
            (lt, ":attacker_agent_horse", 0),#步行
            (try_begin),
               (agent_has_item_equipped, ":attacker_agent_no", "itm_garrison_sickle_axe"),#卫戍镰刃斧
               (assign, ":attacker_anim_no", "anim_active_blood_strike"),
               (assign, ":body_area", 0),#全身
            (else_try),
               (call_script, "script_get_state_count", ":attacker_agent_no", "itm_state_blood_burst"),#两层血潮汹涌
               (ge, reg1, 2),                                                                                                                          #success
               (call_script, "script_restrain_state_full", ":attacker_agent_no", "itm_state_blood_burst", 1),#减少一层血潮汹涌
               (assign, ":attacker_anim_no", "anim_active_blood_strike"),
               (assign, ":body_area", 0),#全身
            (try_end),

         (else_try),
            (eq, ":active_skill_no", "itm_active_release_toxin_fog"),#释放毒雾
            (assign, ":attacker_anim_no", "anim_active_release_toxin_fog"),
            (try_begin),
               (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
               (lt, ":attacker_agent_horse", 0),#步行就全身，骑马只上半身
               (assign, ":body_area", 0),#全身
            (else_try),
               (assign, ":body_area", 1),#上半身
            (try_end),

         (else_try),
            (eq, ":active_skill_no", "itm_active_earthsplitting_charge"),#裂地猛进
            (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
            (gt, ":weapon_no", 0),
            (set_fixed_point_multiplier, 100),
            (item_get_weight, ":weapon_weight", ":weapon_no"),
            (ge, ":weapon_weight", 400),#武器超过四千克
            (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
            (lt, ":attacker_agent_horse", 0),#步行
            (assign, ":attacker_anim_no", "anim_active_earthsplitting_charge"),
            (assign, ":body_area", 0),#全身
         (else_try),
            (eq, ":active_skill_no", "itm_active_ground_heaving"),#掀地
            (agent_get_horse, ":attacker_agent_horse", ":attacker_agent_no"),
            (lt, ":attacker_agent_horse", 0),#步行
            (assign, ":attacker_anim_no", "anim_active_ground_heaving"),
            (assign, ":body_area", 0),#全身

         (else_try),
            (eq, ":active_skill_no", "itm_active_spectre_burst"),#灵爆
            (try_begin),
               (agent_has_item_equipped, ":attacker_agent_no", "itm_death_omen"),#死兆之镰
               (assign, ":attacker_anim_no", "anim_active_enchant_6"),
               (assign, ":body_area", 1),#上半身
            (else_try),
               (call_script, "script_check_agent_passive_skill", ":attacker_agent_no", "itm_passive_resentment"),#积怨
               (ge, reg1, 3),                                                                                                                          #success
               (assign, ":attacker_anim_no", "anim_active_enchant_6"),
               (assign, ":body_area", 1),#上半身
            (try_end),
         (try_end),
      (try_end),

      (gt, ":attacker_anim_no", 0),#成功获取
      (agent_set_animation, ":attacker_agent_no", ":attacker_anim_no", ":body_area"),
(str_store_item_name, s1, ":active_skill_no"),
(display_message, "@成 功 发 动 {s1}"),

      (item_get_max_ammo, ":max_timer", ":active_skill_no"),           #获取技能时间，都是以0.1秒为单位。
      (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":max_timer"),#开始计时
      (agent_set_slot, ":attacker_agent_no", slot_agent_activiting_skill, ":active_skill_no"),#设置当前使用的技能
    ]),


#检测受击（动作命中判定的一部分），特殊武技也共用这个脚本
#use for weapon hit check
#input timer and skill id
  ("cf_AoM_active_weapon_hit", [
      (store_script_param_1, ":timer_count"),
      (store_script_param_2, ":active_skill_no"),
      (store_script_param, ":attacker_agent_no", 3),

      (store_item_value, ":attack_check_point", ":active_skill_no"),#受击检测时间点
      (gt, ":attack_check_point", 0),#排除不需要检测点的技能

      (item_get_max_ammo, ":max_timer", ":active_skill_no"),           #获取技能总时间
      (val_sub, ":max_timer", ":timer_count"),#由于计时从大往小，所以进行处理

#一个技能最多五段攻击，每个时间点占两个数位，从大到小储存在value中
#比如一个2.6秒的技能，在3秒、7秒和12秒有三次判定，就填30712即可
      (try_begin),
         (store_div, ":attack_point", ":attack_check_point", 100000000), #获取检查点
         (gt, ":attack_point", 0),
         (eq, ":attack_point", ":max_timer"),#can attack
         (call_script, "script_cf_AoM_weapon_hit_check_high", ":attacker_agent_no", ":active_skill_no"),#开始受击检测判定
         (val_add, ":timer_count", 1000),
         (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":timer_count"),#千位数用于记录每个检查点还能不能再次判伤。每个检查点只能判伤一次。
      (else_try),
         (val_mod, ":attack_check_point", 100000000),
         (store_div, ":attack_point", ":attack_check_point", 1000000),#获取检查点
         (gt, ":attack_point", 0),
         (eq, ":attack_point", ":max_timer"),#can attack
         (call_script, "script_cf_AoM_weapon_hit_check_high", ":attacker_agent_no", ":active_skill_no"),#开始受击检测判定
         (val_add, ":timer_count", 1000),
         (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":timer_count"),#千位数用于记录每个检查点还能不能再次判伤。每个检查点只能判伤一次。
      (else_try),
         (val_mod, ":attack_check_point", 1000000),
         (store_div, ":attack_point", ":attack_check_point", 10000),   #获取检查点
         (gt, ":attack_point", 0),
         (eq, ":attack_point", ":max_timer"),#can attack
         (call_script, "script_cf_AoM_weapon_hit_check_high", ":attacker_agent_no", ":active_skill_no"),#开始受击检测判定
         (val_add, ":timer_count", 1000),
         (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":timer_count"),#千位数用于记录每个检查点还能不能再次判伤。每个检查点只能判伤一次。
      (else_try),
         (val_mod, ":attack_check_point", 10000),
         (store_div, ":attack_point", ":attack_check_point", 100),       #获取检查点
         (gt, ":attack_point", 0),
         (eq, ":attack_point", ":max_timer"),#can attack
         (call_script, "script_cf_AoM_weapon_hit_check_high", ":attacker_agent_no", ":active_skill_no"),#开始受击检测判定
         (val_add, ":timer_count", 1000),
         (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":timer_count"),#千位数用于记录每个检查点还能不能再次判伤。每个检查点只能判伤一次。
      (else_try),
         (store_mod, ":attack_point", ":attack_check_point", 100),                                 #获取检查点
         (gt, ":attack_point", 0),
         (eq, ":attack_point", ":max_timer"),#can attack
         (call_script, "script_cf_AoM_weapon_hit_check_high", ":attacker_agent_no", ":active_skill_no"),#开始受击检测判定
         (val_add, ":timer_count", 1000),
         (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":timer_count"),#千位数用于记录每个检查点还能不能再次判伤。每个检查点只能判伤一次。

##这是最后一个检查点。尽管在这之后动作可能没有结束，但依然将技能清空以节省算力
#不过0.1秒一次的倒计时没有清空，作为后摇。
         (agent_set_slot, ":attacker_agent_no", slot_agent_activiting_skill, -1),
         (try_for_range, ":count_no", 0, 10),
            (store_add, ":slot_no", ":count_no", slot_agent_surrounded_enemy_1),
            (agent_set_slot, ":attacker_agent_no", ":slot_no", -1),
         (try_end),
      (try_end),
    ]),

#检测受击精密版（动作命中判定的一部分）
#这个版本与普通版不同之处在于遍历了受击者的所有骨骼，并且根据手臂伸太长从敌方身体中穿体而过的情况进行了补充。不过相应的占用算力会极大提高。
#use for weapon hit check
  ("cf_AoM_weapon_hit_check_high", [
      (store_script_param, ":attacker_agent_no", 1),
      (store_script_param, ":active_skill_no", 2),
      (set_fixed_point_multiplier, 100),

      (agent_get_bone_position, pos4, ":attacker_agent_no", 15, 1),                    #获取shoulder.R骨骼的位置，即右肩的位置备用。在skel human里找骨骼序号。
      (agent_get_bone_position, pos5, ":attacker_agent_no", 19, 1),                   #获取item.R骨骼的位置，即右手的位置备用
#      (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),
      (agent_get_slot, ":weapon_length", ":attacker_agent_no", slot_agent_weapon_length),#攻击范围
      (val_add, ":weapon_length", 30),
      (copy_position, pos6, pos5),
      (position_move_y, pos6, ":weapon_length"),                                               #获取武器尖端的位置备用

      (assign, ":if_attack", 0),
      (try_for_range, ":count_no", 0, 10),
         (store_add, ":slot_no", ":count_no", slot_agent_surrounded_enemy_1),
         (agent_get_slot, ":beattacked_agent_no", ":attacker_agent_no", ":slot_no"),
         (ge, ":beattacked_agent_no", 0),
         (agent_is_alive,  ":beattacked_agent_no"),
         (try_begin),
            (agent_is_human, ":beattacked_agent_no"),
            (assign, ":skeleton_total", 20),#人有20块骨骼（从0到19）
         (else_try),
            (assign, ":skeleton_total", 28),#马有28块骨骼（从0到27）
         (try_end),
         (try_for_range, ":skeleton_no", 0, ":skeleton_total"),
            (agent_get_bone_position, pos3, ":beattacked_agent_no", ":skeleton_no", 1),           #获取受击者骨骼的位置pos3
            (try_begin),
               (get_distance_between_positions, ":cur_distance_1", pos3, pos4),#该骨骼到攻击者右肩的距离
               (get_distance_between_positions, ":cur_distance_2", pos5, pos4),#攻击者右手到右肩的距离
               (val_add, ":cur_distance_2", 10),
               (le, ":cur_distance_1", ":cur_distance_2"),#手臂击中对方
               (copy_position, pos1, pos4),#以右肩为原点
               (copy_position, pos2, pos5),#以右手为端点#目标点pos3为敌方骨骼
#               (assign, ":attack_position_type", 1),#手臂击中
            (else_try),
               (copy_position, pos1, pos5),#以右手为原点
               (copy_position, pos2, pos6),#以武器尖端为端点#目标点pos3为敌方骨骼
#               (assign, ":attack_position_type", 2),#武器击中
            (try_end),
            (call_script, "script_cf_dot_line_position_check", 40),#输入误差角                                                 #受击判定

#造成伤害阶段
            (call_script, "script_active_skill_damage_part", ":attacker_agent_no", ":beattacked_agent_no", ":skeleton_total", ":skeleton_no", ":active_skill_no"),

            (assign, ":if_attack", 1),
            (assign, ":skeleton_total", 0),#break一个人只需要检测到一个被击中的骨骼即可
         (try_end),
      (try_end),
      (gt, ":if_attack", 0),
    ]),

#点线判定
#本脚本用于判断一点是否能被某条线击中。运行逻辑为先判断该点到原点的距离是否小于这条细线的长度，是就进行下一步，判断该点与原点的连线和细线之间的夹角是不是小于给定值，是就成功。简而言之，判断目标点pos3在不在以原点pos1为顶点、细线为中轴、细线末端pos2为底部的圆锥内。
#输入原点pos1、末端点pos2、目标点pos3，以及允许的夹角（误差范围），夹角在0到90度间。
#cf脚本，可直接用作判断语句。
  ("cf_dot_line_position_check", [
      (store_script_param, ":error_angle", 1),#误差角
      (set_fixed_point_multiplier, 100),
#原点pos1
#轴线末端点pos2，其中末端点pos2已经事先转化为原点pos1的local坐标
#目标点pos3

#线判定
      (get_distance_between_positions, ":axis_distance", pos1, pos2),#轴线长度
      (get_distance_between_positions, ":cur_distance", pos1, pos3),#目标点到原点的距离
      (ge, ":axis_distance", ":cur_distance"),#目标点到原点的距离比轴线短，进入角判定

#角判定
      (position_get_x, ":cur_x", pos1),#原点坐标
      (position_get_y, ":cur_y", pos1),
      (position_get_z, ":cur_z", pos1),
      (position_get_x, ":cur_x_1", pos2),#末端点坐标
      (position_get_y, ":cur_y_1", pos2),
      (position_get_z, ":cur_z_1", pos2),
      (position_get_x, ":cur_x_2", pos3),#目标点坐标
      (position_get_y, ":cur_y_2", pos3),
      (position_get_z, ":cur_z_2", pos3),

      (val_sub, ":cur_x_1", ":cur_x"),#折算至原点坐标系
      (val_sub, ":cur_y_1", ":cur_y"),
      (val_sub, ":cur_z_1", ":cur_z"),
      (val_sub, ":cur_x_2", ":cur_x"),
      (val_sub, ":cur_y_2", ":cur_y"),
      (val_sub, ":cur_z_2", ":cur_z"),

      (val_mul, ":cur_x_1", ":cur_x_2"),
      (val_mul, ":cur_y_1", ":cur_y_2"),
      (val_mul, ":cur_z_1", ":cur_z_2"),
      (store_add, ":numerator", ":cur_x_1", ":cur_y_1"),
      (val_add, ":numerator", ":cur_z_1"),#x1*x2+y1*y2+z1*z2, dot product
      (store_mul, ":denominator", ":axis_distance", ":cur_distance"),#magnitude1*magnitude2
#利用夹角公式，点乘除以两线模长等于夹角的cos值。
#由于直接除得到的cos值为小于1的数，事先为分子乘100
      (val_mul, ":numerator", 100),
      (val_div, ":numerator", ":denominator"),#目标点的偏离角cos值（×100）

      (val_mul, ":error_angle", 100),#输入的是0到90度的角，在100分辨率下应乘以100，得到的cos值也是乘过100的。
      (store_cos, ":error_angle", ":error_angle"),#误差角的cos值
      (ge, ":numerator", ":error_angle"),#偏离角小于等于误差角，由于cos是递减的，所以这里取大于等于
    ]),



#矩形受击范围判定
#输入起始点，需要判断的点，效果距离、边长和纵向长度（厘米）
#比如一个技能能对前方5米、左右不超过两米、高度不超过1.5米范围内的所有敌人造成伤害，就输入5、2、1.5，敌方在玩家前方3米往左1.2米，能够打到，就判定通过
  ("cf_square_area_check", [
      (store_script_param, ":anchor_pos", 1),#起始点pos
      (store_script_param, ":check_pos", 2),#需要判定的点pos
      (store_script_param, ":skill_length", 3),#攻击距离（往前）
      (store_script_param, ":skill_width", 4),#攻击范围（左右）
      (store_script_param, ":skill_height", 5),#技能高度（为了避免在一楼放技能打到五楼的情况出现，实际填个2米就行）

      (set_fixed_point_multiplier, 100),
      (position_transform_position_to_local, ":check_pos", ":anchor_pos", ":check_pos"),
      (position_get_x, ":count_no", ":check_pos"),#左右
      (val_abs, ":count_no"),
      (le, ":count_no", ":skill_width"),
      (position_get_y, ":count_no", ":check_pos"),#前方
      (le, ":count_no", ":skill_length"),
      (position_get_z, ":count_no", ":check_pos"),#上下
      (val_abs, ":count_no"),
      (le, ":count_no", ":skill_height"),
    ]),



#用于主动技能造成伤害时计算伤害量并造成各种效果。
  ("active_skill_damage_part", [
      (store_script_param, ":attacker_agent_no", 1),#攻击者
      (store_script_param, ":beattacked_agent_no", 2),#受击者
      (store_script_param, ":skeleton_total", 3),#受击者类型，20为人，28为动物
      (store_script_param, ":skeleton_no", 4),#受击骨骼
      (store_script_param, ":active_skill_no", 5),#技能
      (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
      (agent_get_troop_id, ":attacker_troop_no", ":attacker_agent_no"),

      (agent_get_position, pos1, ":beattacked_agent_no"),
      (play_sound_at_position, "snd_metal_hit_low_armor_high_damage", pos1),

#受击伤害
      (item_get_food_quality, ":damage", ":active_skill_no"),#基础伤害
      (assign, ":damage_caculate", ":damage"),
      (store_attribute_level, ":value_no", ":attacker_troop_no", ca_strength),#力
      (val_mul, ":damage_caculate", ":value_no"),
      (val_div, ":damage_caculate", 10),

      (try_begin),
         (gt, ":weapon_no", 0),
         (item_get_difficulty, ":value_no", ":active_skill_no"),#调用的武器攻击力来源于挥还是刺
         (try_begin),
            (eq, ":value_no", 1),#挥
            (item_get_swing_damage, ":value_no", ":weapon_no"),#武器挥舞的伤害
            (val_mul, ":damage_caculate", ":value_no"),
            (val_div, ":damage_caculate", 40),
         (else_try),
            (eq, ":value_no", 2),#刺
            (item_get_thrust_damage, ":value_no", ":weapon_no"),#武器戳刺的伤害
            (val_mul, ":damage_caculate", ":value_no"),
            (val_div, ":damage_caculate", 40),
         (try_end),

         (item_get_type, ":value_no", ":weapon_no"),
         (try_begin),
            (eq, ":value_no", itp_type_one_handed_wpn),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_one_handed_weapon),#单手熟练
         (else_try),
            (eq, ":value_no", itp_type_two_handed_wpn),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_two_handed_weapon),#双手熟练
         (else_try),
            (eq, ":value_no", itp_type_polearm),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_polearm),#长杆熟练
         (else_try),
            (eq, ":value_no", itp_type_bow),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_archery),#弓熟练
         (else_try),
            (eq, ":value_no", itp_type_crossbow),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_crossbow),#弩熟练
         (else_try),
            (eq, ":value_no", itp_type_thrown),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_throwing),#投掷熟练
         (else_try),
            (this_or_next|eq, ":value_no", itp_type_pistol),
            (eq, ":value_no", itp_type_musket),
            (store_proficiency_level, ":value_no", ":attacker_troop_no", wpt_firearm),#火器熟练
         (try_end),
         (val_mul, ":damage_caculate", ":value_no"),
         (val_div, ":damage_caculate", 300),
      (try_end),

      (store_skill_level, ":value_no", skl_power_strike, ":attacker_troop_no"),#强击
      (val_mul, ":value_no", 2),
      (val_add, ":damage_caculate", ":value_no"),
      (store_skill_level, ":value_no", skl_weapon_master, ":attacker_troop_no"),#娴熟
      (val_add, ":damage_caculate", ":value_no"),
#武技基础伤害计算公式：伤害基础值×力/10×武器攻击力/40×相应熟练度/300＋强击×2＋娴熟

#武器加成
      (try_begin),
         (eq, ":weapon_no", "itm_jinshiwandao"),#金饰弯刀
         (eq, ":active_skill_no", "itm_active_sweep_away"),#旋刃斩
         (val_add, ":damage_caculate", ":damage"),#提升等同于基础伤害的伤害量
      (else_try),
         (eq, ":weapon_no", "itm_anti_cavalry_great_sword"),#反骑巨剑
         (eq, ":active_skill_no", "itm_active_thump"),#横扫
         (store_mul, ":value_no", ":damage", 2),
         (val_add, ":damage_caculate", ":value_no"),#提升等同于两倍基础伤害的伤害量
      (else_try),
         (eq, ":weapon_no", "itm_stone_hammer"),#石重锤
         (eq, ":active_skill_no", "itm_active_casual_attack"),#盲击
         (store_mul, ":value_no", ":damage", 2),
         (val_add, ":damage_caculate", ":value_no"),#提升等同于两倍基础伤害的伤害量
      (else_try),
         (eq, ":weapon_no", "itm_kouruto_beast_sabre_simple"),#简易科鲁托猛兽剑
         (eq, ":active_skill_no", "itm_active_casual_attack"),#盲击
         (val_add, ":damage_caculate", 6),#伤害提高6点
      (else_try),
         (eq, ":weapon_no", "itm_kouruto_beast_sabre"),#科鲁托野兽剑
         (eq, ":active_skill_no", "itm_active_heavy_casual_attack"),#野盲击
         (val_add, ":damage_caculate", ":damage"),#提升等同于基础伤害的伤害量
         (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_bleeding", 2),#流血＋2
      (else_try),
         (eq, ":weapon_no", "itm_jinshi_longshoujian"),#金饰侧剑
         (this_or_next|eq, ":active_skill_no", "itm_active_lunge"),#穿刺
         (eq, ":active_skill_no", "itm_active_double_lunge"),#二连穿刺
         (val_add, ":damage_caculate", ":damage"),#提升等同于基础伤害的伤害量
      (else_try),
         (eq, ":weapon_no", "itm_crushing_hammer"),#粉碎重锤
         (eq, ":active_skill_no", "itm_active_leap_attack"),#跳劈
         (store_mul, ":value_no", ":damage", 2),
         (val_add, ":damage_caculate", ":value_no"),#提升等同于两倍基础伤害的伤害量

         (set_fixed_point_multiplier, 100),
         (agent_get_position, pos1, ":attacker_agent_no"),
         (try_for_agents, ":agent_no", pos1, 150),#1.5米
            (neq, ":agent_no", ":attacker_agent_no"),
            (agent_deliver_damage_to_agent, ":attacker_agent_no", ":agent_no", 30, ":weapon_no"),#造成范围伤害
         (try_end),
      (try_end),

      (try_begin),#双持
         (eq, ":active_skill_no", "itm_active_undercover_slash"),#潜身斩
         (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 1),
         (gt, ":weapon_no", 0),
         (item_has_property, ":weapon_no", itp_left_hand_weapon),#左手装备左手武器
         (store_div, ":value_no", ":damage_caculate", 2),
         (val_add, ":damage_caculate", ":value_no"),#提升现有伤害量的一半
      (try_end),

      (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage_caculate", ":weapon_no"),#造成伤害

#受击动作
      (try_begin),
         (gt, ":damage_caculate", 7),#受击僵直的伤害阈值
         (eq, ":skeleton_total", 20),#受击者为人
         (try_begin),
            (this_or_next|eq, ":skeleton_no", 0),#abdome腹部
            (eq, ":skeleton_no", 7),#spine脊柱
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_abdomen_front"),#腹部受击
         (else_try),
            (this_or_next|eq, ":skeleton_no", 1),#thigh.L左大腿
            (this_or_next|eq, ":skeleton_no", 2),#calf.L左小腿
            (eq, ":skeleton_no", 3),#foot.L左足
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_legs_left"),#下半身受击（左）
         (else_try),
            (this_or_next|eq, ":skeleton_no", 4),#thigh.R右大腿
            (this_or_next|eq, ":skeleton_no", 5),#calf.R右小腿
            (eq, ":skeleton_no", 6),#foot.R右足
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_legs_right"),#下半身受击（右）
         (else_try),
            (eq, ":skeleton_no", 9),#head头
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_head_front"),#头部受击
         (else_try),
            (eq, ":skeleton_no", 8),#thorax胸
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_chest_front"),#胸部受击
         (else_try),
            (eq, ":skeleton_no", 10),#shoulder.L左肩
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_head_left"),#头部受击（左）
         (else_try),
            (eq, ":skeleton_no", 15),#shoulder.R右肩
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_head_right"),#头部受击（右）
         (else_try),
            (this_or_next|eq, ":skeleton_no", 11),#upperarm.L左大臂
            (this_or_next|eq, ":skeleton_no", 12),#forearm.L左小臂
            (this_or_next|eq, ":skeleton_no", 13),#hand.L左手
            (eq, ":skeleton_no", 14),#item.L左武器
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_chest_left"),#胸部受击（左）
         (else_try),
            (this_or_next|eq, ":skeleton_no", 16),#upperarm.R右大臂
            (this_or_next|eq, ":skeleton_no", 17),#forearm.R右小臂
            (this_or_next|eq, ":skeleton_no", 18),#hand.R右手
            (eq, ":skeleton_no", 19),#item.R右武器
            (agent_set_animation, ":beattacked_agent_no", "anim_strike_chest_right"),#胸部受击（右）
         (try_end),
      (try_end),
    ]),


#特殊武技效果处理
#输入agent、skill no和时间点
  ("AoM_special_skill", [
      (store_script_param, ":attacker_agent_no", 1),#攻击者
      (store_script_param, ":active_skill_no", 2),#技能
      (store_script_param, ":time_point", 3),#检查点
      (set_fixed_point_multiplier, 100),#单位都是厘米

      (try_begin),
         (eq, ":active_skill_no", "itm_active_flame_sweep"),#火焰横扫
         (is_between, ":time_point", 7, 16),#0.1秒一发
         (agent_get_bone_position, pos1, ":attacker_agent_no", hb_head, 1),
         (agent_get_bone_position, pos2, ":attacker_agent_no", hb_hand_l, 1),
         (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
         (agent_get_bone_position, pos2, ":attacker_agent_no", hb_hand_l, 1),
         (position_copy_rotation, pos2, pos1),
         (add_missile, ":attacker_agent_no", pos2, 200, "itm_fire_arrow", 0, "itm_fire_arrow", 0),

      (else_try),
         (eq, ":active_skill_no", "itm_active_blood_strike"),#血星冲击
         (agent_get_position, pos1, ":attacker_agent_no"),
         (try_begin),
            (eq, ":time_point", 9),#0.9秒将攻击者瞬移至目标上方
#            (agent_set_visibility, ":attacker_agent_no", 0),
            (try_begin),
               (agent_get_slot, ":target_agent_no", ":attacker_agent_no", slot_ai_target),
               (ge, ":target_agent_no", 0),
               (agent_get_position, pos1, ":target_agent_no"),
            (else_try),
               (position_move_y, pos1, 1500),
            (try_end),
            (agent_set_position, ":attacker_agent_no", pos1),
         (else_try),
            (eq, ":time_point", 18),#1.8秒造成伤害＋烟雾特效
            (particle_system_burst, "psys_blood_splash", pos1, 30),
            (play_sound_at_position, "snd_hit_ground", pos1),
            (item_get_food_quality, ":damage_count", "itm_active_blood_strike"),#伤害
            (assign, ":range_count", 200),#2米
            (try_begin),
               (agent_has_item_equipped, ":attacker_agent_no", "itm_westcoast_black_glove"),#西海黑手套
               (val_add, ":damage_count", 10),#伤害加10
            (try_end),
            (try_begin),
               (agent_has_item_equipped, ":attacker_agent_no", "itm_westcoast_guard_boot"),#西海卫士靴
               (val_add, ":range_count", 100),#范围加1米
            (try_end),
            (try_for_agents, ":beattacked_agent_no", pos1, ":range_count"),
               (agent_is_alive, ":beattacked_agent_no"),
               (neq, ":beattacked_agent_no", ":attacker_agent_no"),
               (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage_count"),#造成伤害
            (try_end),
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_earthsplitting_charge"),#裂地猛进
         (eq, ":time_point", 9),#0.9秒时砸到地上
         (agent_get_position, pos1, ":attacker_agent_no"),
         (particle_system_burst, "psys_normal_splash", pos1, 30),
         (play_sound_at_position, "snd_hit_ground", pos1),
         (item_get_food_quality, ":damage_count", "itm_active_earthsplitting_charge"),#伤害
         (try_for_agents, ":beattacked_agent_no", pos1, 300),
            (agent_is_alive, ":beattacked_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_agent_no"),
            (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage_count"),#造成伤害
         (try_end),
      (else_try),
         (eq, ":active_skill_no", "itm_active_ground_heaving"),#掀地
         (eq, ":time_point", 14),#1.4秒时掀起
         (agent_get_position, pos1, ":attacker_agent_no"),
         (play_sound_at_position, "snd_hit_ground", pos1),
         (item_get_food_quality, ":damage_count", "itm_active_ground_heaving"),#伤害
         (try_for_agents, ":beattacked_agent_no", pos1, 700),
            (agent_is_alive, ":beattacked_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_agent_no"),
            (agent_get_position, pos2, ":beattacked_agent_no"),
            (copy_position, pos4, pos2),
            (call_script, "script_cf_square_area_check", pos1, pos2, 400, 150, 150),
            (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage_count"),#造成伤害
            (particle_system_burst, "psys_normal_splash", pos4, 5),#烟雾特效
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_release_toxin_fog"),#释放毒雾
         (this_or_next|eq, ":time_point", 10),
         (this_or_next|eq, ":time_point", 17),
         (this_or_next|eq, ":time_point", 24),
         (eq, ":time_point", 31),
         (agent_get_bone_position, pos2, ":attacker_agent_no", hb_hand_r, 1),
         (particle_system_burst, "psys_toxin_fog", pos2, 20),#烟雾特效
         (try_for_agents, ":beattacked_agent_no", pos2, 200),#两米内
            (agent_is_alive, ":beattacked_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_agent_no"),
            (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_strong_toxin", 40),#强毒＋40
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_power_shot"),#拉满弓
         (eq, ":time_point", 11),#1.1秒时射出
         (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
         (gt, ":weapon_no", 0),
         (item_get_type, ":type_no", ":weapon_no"),#弓才能用
         (eq, ":type_no", itp_type_bow),
         (call_script, "script_get_missile", ":attacker_agent_no", 1),#箭
         (gt, reg1, 0),
         (assign, ":arrow_no", reg1),
         (store_sub, ":ammo_no", reg3, 1),
         (agent_set_ammo, ":attacker_agent_no", ":arrow_no", ":ammo_no"),#箭减少1

         (agent_get_bone_position, pos5, ":attacker_agent_no", hb_item_l, 1),#弓的位置
         (agent_get_look_position, pos2, ":attacker_agent_no"),
         (position_copy_rotation, pos5, pos2),
         (add_missile, ":attacker_agent_no", pos5, 9900, ":weapon_no", 0, "itm_power_shot_special_effect", 0),

      (else_try),
         (eq, ":active_skill_no", "itm_active_continuous_shooting"),#三连射
         (this_or_next|eq, ":time_point", 12),#1.2秒时射出
         (this_or_next|eq, ":time_point", 17),#1.6秒时射出
         (eq, ":time_point", 20),#2.0秒时射出
         (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
         (gt, ":weapon_no", 0),
         (item_get_type, ":type_no", ":weapon_no"),#弓才能用
         (eq, ":type_no", itp_type_bow),
         (call_script, "script_get_missile", ":attacker_agent_no", 1),#箭
         (gt, reg1, 0),
         (assign, ":arrow_no", reg1),
         (store_sub, ":ammo_no", reg3, 1),
         (agent_set_ammo, ":attacker_agent_no", ":arrow_no", ":ammo_no"),#箭减少1

         (agent_get_bone_position, pos5, ":attacker_agent_no", hb_item_l, 1),#弓的位置
         (agent_get_look_position, pos2, ":attacker_agent_no"),
         (position_copy_rotation, pos5, pos2),
         (position_rotate_x, pos5, 10),#避免下坠太严重
         (add_missile, ":attacker_agent_no", pos5, 9900, ":weapon_no", 0, ":arrow_no", 0),

      (else_try),
         (eq, ":active_skill_no", "itm_active_multiple_arrow"),#多重箭
         (eq, ":time_point", 16),#1.6秒时射出
         (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
         (gt, ":weapon_no", 0),
         (item_get_type, ":type_no", ":weapon_no"),#弓才能用
         (eq, ":type_no", itp_type_bow),

         (agent_get_bone_position, pos5, ":attacker_agent_no", hb_item_l, 1),#弓的位置
         (agent_get_look_position, pos2, ":attacker_agent_no"),
         (position_copy_rotation, pos5, pos2),
         (position_rotate_z, pos5, -12),
         (try_for_range, reg10, 0, 5),
            (call_script, "script_get_missile", ":attacker_agent_no", 1),#箭
            (gt, reg1, 0),
            (assign, ":arrow_no", reg1),
            (store_sub, ":ammo_no", reg3, 1),
            (agent_set_ammo, ":attacker_agent_no", ":arrow_no", ":ammo_no"),#箭五次减少1
            (add_missile, ":attacker_agent_no", pos5, 9900, ":weapon_no", 0, ":arrow_no", 0),
            (position_rotate_z, pos5, 6),
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_throwing_arrow"),#投箭
         (eq, ":time_point", 6),#0.6秒时射出
         (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),#武器
         (gt, ":weapon_no", 0),
         (item_get_type, ":type_no", ":weapon_no"),#拿着弓时才会右手拿箭
         (eq, ":type_no", itp_type_bow),
         (call_script, "script_get_missile", ":attacker_agent_no", 1),#箭
         (gt, reg1, 0),
         (assign, ":arrow_no", reg1),
         (store_sub, ":ammo_no", reg3, 1),
         (agent_set_ammo, ":attacker_agent_no", ":arrow_no", ":ammo_no"),#箭减少1
         (agent_get_bone_position, pos5, ":attacker_agent_no", hb_hand_r, 1),#右手的位置
         (agent_get_look_position, pos2, ":attacker_agent_no"),
         (position_copy_rotation, pos5, pos2),
         (position_rotate_x, pos5, 10),#避免下坠太严重
         (add_missile, ":attacker_agent_no", pos5, 2500, ":weapon_no", 0, ":arrow_no", 0),

      (else_try),
         (eq, ":active_skill_no", "itm_active_war_stomp"),#战争践踏
         (eq, ":time_point", 22),#2.2秒时砸到地上
         (neg|agent_is_human, ":attacker_agent_no"),#马
         (agent_get_position, pos1, ":attacker_agent_no"),
         (particle_system_burst, "psys_normal_splash", pos1, 30),
         (play_sound_at_position, "snd_hit_ground", pos1),
         (item_get_food_quality, ":damage_count", "itm_active_war_stomp"),#伤害
         (agent_get_rider, ":attacker_rider_no", ":attacker_agent_no"),
         (try_begin),
            (agent_is_alive, ":attacker_rider_no"),
            (ge, ":attacker_rider_no", 0),
            (agent_get_team, ":attacker_team_no", ":attacker_rider_no"),
         (try_end),
         (try_for_agents, ":beattacked_agent_no", pos1, 500),
            (agent_is_alive, ":beattacked_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_rider_no"),
            (agent_get_team, ":beattacked_team_no", ":beattacked_agent_no"),
            (neq, ":attacker_team_no", ":beattacked_team_no"),
            (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage_count"),#造成伤害
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_silver_fall"),#银落
         (eq, ":time_point", 28),#2.8秒时砸到地上
         (agent_is_human, ":attacker_agent_no"),#人
         (agent_get_bone_position, pos1, ":attacker_agent_no", hb_item_r, 1),#武器
         (position_move_z, pos1, -50),
         (particle_system_burst, "psys_normal_splash", pos1, 28),
         (play_sound_at_position, "snd_hit_ground", pos1),
         (item_get_food_quality, ":damage_count", "itm_active_silver_fall"),#伤害
         (agent_get_horse, ":attacker_horse_no", ":attacker_agent_no"),
         (agent_get_team, ":attacker_team_no", ":attacker_agent_no"),
         (try_for_agents, ":beattacked_agent_no", pos1, 600),
            (agent_is_alive, ":beattacked_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_agent_no"),
            (neq, ":beattacked_agent_no", ":attacker_horse_no"),
            (agent_get_team, ":beattacked_team_no", ":beattacked_agent_no"),
            (neq, ":attacker_team_no", ":beattacked_team_no"),
            (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage_count"),#造成伤害
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_spectre_burst"),#灵爆
         (eq, ":time_point", 8),#0.8秒时起爆
         (agent_get_bone_position, pos5, ":attacker_agent_no", hb_thorax, 1),#胸部
         (particle_system_burst, "psys_spectre_burst", pos5, 10),
         (particle_system_burst, "psys_ghost_smoke", pos5, 3),

         (agent_get_position, pos6, ":attacker_agent_no"),
         (call_script, "script_pos_copy_rotation_from_pos", pos5, pos6),#复制旋转角
         (try_begin),
            (agent_get_slot, ":target_agent_no", ":attacker_agent_no", slot_ai_target),
            (ge, ":target_agent_no", 0),
            (try_for_range, ":count_no", 0, 5),
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
               (add_missile, ":attacker_agent_no", pos1, 1000, "itm_spectre", 0, "itm_spectre", 0),
            (try_end),
         (else_try),
            (try_for_range, reg1, 0, 5),
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
               (add_missile, ":attacker_agent_no", pos1, 1000, "itm_spectre", 0, "itm_spectre", 0),
            (try_end),
         (try_end),

         (store_agent_hit_points, ":agent_hp", ":attacker_agent_no", 1),
         (val_sub, ":agent_hp", 30),
         (try_begin),
            (gt, ":agent_hp", 0),
            (agent_set_hit_points, ":attacker_agent_no", ":agent_hp", 1),
         (else_try),
            (agent_set_hit_points, ":attacker_agent_no", 1, 1),#不会扣血到0。
         (try_end),
      (try_end),
    ]),


#旧版
#检测受击（动作命中判定的一部分）
#input pos1, pos2 and origin position pos3.
#pos1 is weapon end point, pos2 is enemy position, pos3 is player position
#If pos1 and pos2 are in same direction of pos1 and long enough, return reg1 = 1, means can hit. 
  ("cf_position_check_hit", [
      (set_fixed_point_multiplier, 100),
      (assign, reg1, 0),
      (get_distance_between_positions, ":cur_distance_1", pos1, pos3),#weapon attack range
      (get_distance_between_positions, ":cur_distance_2", pos2, pos3),#enemy distance
      (ge, ":cur_distance_1", ":cur_distance_2"),#can hit
      (position_get_x, ":cur_x_1", pos1),
      (position_get_y, ":cur_y_1", pos1),
      (position_get_z, ":cur_z_1", pos1),
      (position_get_x, ":cur_x_2", pos2),
      (position_get_y, ":cur_y_2", pos2),
      (position_get_z, ":cur_z_2", pos2),
      (position_get_x, ":cur_x", pos3),
      (position_get_y, ":cur_y", pos3),
      (position_get_z, ":cur_z", pos3),
      (val_sub, ":cur_x_1", ":cur_x"),
      (val_sub, ":cur_y_1", ":cur_y"),
      (val_sub, ":cur_z_1", ":cur_z"),
      (val_sub, ":cur_x_2", ":cur_x"),
      (val_sub, ":cur_y_2", ":cur_y"),
      (val_sub, ":cur_z_2", ":cur_z"),
      (val_mul, ":cur_x_1", ":cur_x_2"),
      (val_mul, ":cur_y_1", ":cur_y_2"),
      (val_mul, ":cur_z_1", ":cur_z_2"),
      (store_add, ":numerator", ":cur_x_1", ":cur_y_1"),
      (val_add, ":numerator", ":cur_z_1"),#x1*x2+y1*y2+z1*z2, dot product
      (store_mul, ":denominator", ":cur_distance_1", ":cur_distance_2"),#magnitude1*magnitude2
#cos=numerator/denominator. When cos equals 1, these two are in the same direction. We need their included angle to be within plus or minus 60 degrees, that is, cos must be greater than 0.5
#But considering that Python may not be able to obtain 0.5, let's transform the inequality and apply 0.5 to the denominator side, that is, the numerator must be greater than the denominator multiplied by 0.5
#      (val_mul, ":denominator", 9),
      (val_div, ":denominator", 2),
      (ge, ":numerator", ":denominator"),
      (assign, reg1, 1),#can hit
    ]),

#旧版
#检测受击（动作命中判定的一部分）
#use for weapon hit check
  ("AoM_weapon_hit_check", [
      (store_script_param, ":attacker_agent_no", 1),

      (agent_get_bone_position, pos3, ":attacker_agent_no", 19, 1),                   #获取item.R骨骼的位置pos3，即右手的位置
      (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),
      (item_get_weapon_length, ":weapon_length", ":weapon_no"),#cm
      (val_add, ":weapon_length", 30),
      (copy_position, pos1, pos3),
      (position_move_y, pos1, ":weapon_length"),                                       #获取武器尖端的位置pos1

      (try_for_range, ":count_no", 0, 10),
         (store_add, ":slot_no", ":count_no", slot_agent_surrounded_enemy_1),
         (agent_get_slot, ":beattacked_agent_no", ":attacker_agent_no", ":slot_no"),
         (gt, ":beattacked_agent_no", 0),
         (agent_is_alive,  ":beattacked_agent_no"),
         (agent_get_position, pos2, ":beattacked_agent_no"),
         (position_move_z, pos2, 100),                                                           #敌方中心位置pos2

         (call_script, "script_cf_position_check_hit"),#受击判定
         (eq, reg1, 1),
         (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no"),
      (try_end),
    ]),

#————————————————————————————————————咏唱类————————————————————————————————
#咏唱启动
#咏唱的机制为，首先咏唱的基础时间储存在abundance中，单位是秒。然后灼言等级减咏唱时间，一级减3%，15级45%。判这个咏唱时间是不是小于强识技能×3，小于就不能发动（记不住）。然后计时器读条，在agent hit里加个判定，判最终伤害是不是小于稳定（骑射）×4，否则就slot归零咏唱失败。
  ("cf_sorcery_chant_technique", [
      (store_script_param, ":attacker_agent_no", 1),
      (store_script_param, ":active_skill_no", 2),

      (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_skill_timer, 1),
      (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_activiting_skill, 1),#当前未使用技能

      (item_get_abundance, ":time_count", ":active_skill_no"),#基础咏唱时间
      (val_mul, ":time_count", 10),#计时器0.1秒一跳

      (agent_get_troop_id, ":attacker_troop_no", ":attacker_agent_no"),
      (store_skill_level, ":level_no", skl_persuasion, ":attacker_troop_no"),#灼言
      (store_mul, ":value_no", ":level_no", 3),
      (store_sub, ":value_no", 100, ":value_no"),
      (val_mul, ":time_count", ":value_no"),
      (val_div, ":time_count", 100),#基础时间×（1-灼言×3%）（x10，以0.1秒为单位）

#减少咏唱时间的技能与装备
      (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 1),#盾
      (try_begin),
         (eq, ":weapon_no", "itm_patron_tower_shield"),#守护者塔盾
         (this_or_next|eq, ":active_skill_no", "itm_active_pray_holy_aegis"),#神术：圣盾
         (this_or_next|eq, ":active_skill_no", "itm_active_pray_heavenly_wall"),#神术：天国之壁
         (eq, ":active_skill_no", "itm_active_pray_drop_of_reasoning_sea"),#神术：理海的一滴
         (val_sub, ":time_count", 40),
      (try_end),

      (try_begin),
         (call_script, "script_check_agent_passive_skill", ":attacker_agent_no", "itm_passive_heart_of_the_vast_reasoning_sea"),#万顷理海之心
         (gt, reg1, 0),
         (gt, ":time_count", 10),
         (assign, ":time_count", 10),#若大于1秒，则设置为一秒
      (try_end),

#能不能释放的判定
      (try_begin),#需要状态：移动墓地的类型（骸派）
         (this_or_next|eq, ":active_skill_no", "itm_active_rib_shot"),#肋骨射击要求3
         (this_or_next|eq, ":active_skill_no", "itm_active_triple_rib_shot"),#三重肋骨射击要求9
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton"),#创造复生骷髅要求7
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton_pikeman"),#创造骷髅战士要求12
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton_swordman"),#创造骷髅剑士要求12
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton_archer"),#创造骷髅重弓手要求16
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_wild_hunter"),#召来狂猎要求500
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_giant"),#创造不死组合巨人要求80
         (eq, ":active_skill_no", "itm_active_undead_creation_giant_sword"),#创造剑骸组合巨人要求100
         (item_get_food_quality, ":skill_request", ":active_skill_no"),
         (call_script, "script_get_state_count", ":attacker_agent_no", "itm_state_moving_cemetery"),#移动墓地
         (lt, reg1, ":skill_request"),                                                                                                                          #fail
         (assign, ":time_count", 1919810),
      (else_try),#要求被动：积怨的类型（魂派）
         (this_or_next|eq, ":active_skill_no", "itm_active_create_spectre"),#创造屑灵要求1
         (eq, ":active_skill_no", "itm_active_create_spectre_group"),#创造屑灵集群要求2
         (item_get_food_quality, ":skill_request", ":active_skill_no"),
         (call_script, "script_check_agent_passive_skill", ":attacker_agent_no", "itm_passive_resentment"),#积怨
         (lt, reg1, ":skill_request"),                                                                                                                          #fail
         (assign, ":time_count", 1919810),
      (try_end),
      (store_skill_level, ":value_no", skl_memory, ":attacker_troop_no"),#强识
      (val_mul, ":value_no", 30),#允许的最长咏唱时间
      (ge, ":value_no", ":time_count"),

(str_store_item_name, s1, ":active_skill_no"),
(display_message, "@成 功 发 动 {s1}"),

      (try_begin),
         (le, ":time_count", 0),
         (assign, ":time_count", 1),#避免咏唱时间小于等于零
      (try_end),
      (val_add, ":time_count", 10000),#万位用于记录术法释放的阶段，万位为1表示咏唱，为0则是效应阶段的后摇。千位用于记录武技的阶段了，不要混淆，检测时检测ge 10000即可。
      (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":time_count"),#开始计时
      (agent_set_slot, ":attacker_agent_no", slot_agent_activiting_skill, ":active_skill_no"),#设置当前使用的技能

      (try_begin),
         (le, ":level_no", 6),#灼言小于等于6级
         (agent_set_animation, ":attacker_agent_no", "anim_chant_long", 1),#长咏唱动作
      (else_try),
         (agent_set_animation, ":attacker_agent_no", "anim_chant_short", 1),#短咏唱动作
      (try_end),
    ]),

#术法效果
  ("AoM_active_sorcery_result", [
      (store_script_param_1, ":active_skill_no"),
      (store_script_param_2, ":agent_no"),

(str_store_item_name, s1, ":active_skill_no"),
(display_message, "@{s1}生 效 "),

      (set_fixed_point_multiplier, 100),

      (try_begin),
         (this_or_next|eq, ":active_skill_no", "itm_active_fire_arrow"),#火矢射击
         (this_or_next|eq, ":active_skill_no", "itm_active_ice_arrow"),#冰矢射击
         (eq, ":active_skill_no", "itm_active_wind_blade"),#风刃射击
         (agent_set_animation, ":agent_no", "anim_active_enchant_7", 1),
         (agent_get_bone_position, pos1, ":agent_no", hb_head, 1),#头
         (agent_get_look_position, pos2, ":agent_no"),
         (position_copy_rotation, pos1, pos2),
         (try_begin),
            (eq, ":active_skill_no", "itm_active_fire_arrow"),#火矢射击
            (add_missile, ":agent_no", pos1, 1700, "itm_fire_arrow", 0, "itm_fire_arrow", 0),
         (else_try),
            (eq, ":active_skill_no", "itm_active_ice_arrow"),#冰矢射击
            (add_missile, ":agent_no", pos1, 1200, "itm_ice_arrow", 0, "itm_ice_arrow", 0),
         (else_try),
            (eq, ":active_skill_no", "itm_active_wind_blade"),#风刃射击
            (add_missile, ":agent_no", pos1, 2000, "itm_wind_blade", 0, "itm_wind_blade", 0),
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_stone_shoot"),#地刺射击
         (agent_set_animation, ":agent_no", "anim_active_enchant_8", 1),
         (agent_get_bone_position, pos1, ":agent_no", hb_head, 1),#头
         (agent_get_look_position, pos2, ":agent_no"),
         (position_copy_rotation, pos1, pos2),
         (try_begin),
            (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),
            (ge, ":target_agent_no", 0),
            (agent_get_bone_position, pos1, ":target_agent_no", hb_abdomen, 1),
            (agent_get_position, pos2, ":target_agent_no"),
            (position_copy_rotation, pos1, pos2),
         (else_try),
            (agent_get_position, pos1, ":agent_no"),
            (position_move_y, pos1, 500),#身前5米
         (try_end),
         (position_set_z_to_ground_level, pos1),
         (position_move_z, pos1, 300),#向上移避免直接卡在地上
         (position_rotate_x, pos1, 90),#朝上发射
         (position_rotate_y, pos1, 90),#朝上发射
         (add_missile, ":agent_no", pos1, 1000, "itm_stone_snag", 0, "itm_stone_snag", 0),

      (else_try),
#######有待后续使用prop更新
         (eq, ":active_skill_no", "itm_active_flame_weapon"),#引燃炎锋
         (neg|agent_slot_ge, ":agent_no", slot_agent_enchant, 1),#没有启用别的附魔
         (item_get_max_ammo, ":value_no", "itm_state_flame_weapon"),#阈值
         (val_add, ":value_no", 10000),
         (call_script, "script_activate_state", ":agent_no", "itm_state_flame_weapon", ":value_no"),
         (store_sub, ":value_no", "itm_state_flame_weapon", "itm_state_begin"),
         (agent_set_slot, ":agent_no", slot_agent_enchant, ":value_no"),#设置附魔

      (else_try),
         (this_or_next|eq, ":active_skill_no", "itm_active_warcy_blooddrum"),#血鼓战吼
         (eq, ":active_skill_no", "itm_active_warcy_bloodsteel"),#血钢战吼
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_blood_burst", 1),#自身减少最多一层血潮汹涌
         (assign, ":timer_count", 30),#30秒
         (try_begin),
            (ge, reg1, 1),#实际消耗了一层
            (val_add, ":timer_count", 30),#消耗一层血潮汹涌提升30秒增益时间
         (try_end),
         (try_begin),
            (eq, ":active_skill_no", "itm_active_warcy_blooddrum"),#血鼓战吼
            (assign, ":state_no", "itm_state_generous_death"),#背水一战
         (else_try),
            (eq, ":active_skill_no", "itm_active_warcy_bloodsteel"),#血钢战吼
            (assign, ":state_no", "itm_state_war_anger"),#血脉偾张
         (try_end),
         (call_script, "script_proceed_state", ":agent_no", ":state_no", ":timer_count"),
         (agent_set_animation, ":agent_no", "anim_active_enchant_2", 1),

      (else_try),
         (this_or_next|eq, ":active_skill_no", "itm_active_warcy_blooddrum_group"),#血鼓战号
         (eq, ":active_skill_no", "itm_active_warcy_bloodsteel_group"),#血钢战号
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_blood_burst", 1),#自身减少最多一层血潮汹涌
         (assign, ":timer_count", 30),#30秒
         (assign, ":distance_no", 1500),#十五米
         (try_begin),
            (ge, reg1, 1),#实际消耗了一层
            (val_add, ":timer_count", 30),#消耗一层血潮汹涌提升30秒增益时间
            (val_add, ":distance_no", 500),#半径扩大五米
         (try_end),
         (try_begin),
            (eq, ":active_skill_no", "itm_active_warcy_blooddrum_group"),#血鼓战号
            (assign, ":state_no", "itm_state_generous_death"),#背水一战
         (else_try),
            (eq, ":active_skill_no", "itm_active_warcy_blooddrum_group"),#血钢战号
            (assign, ":state_no", "itm_state_war_anger"),#血脉偾张
         (try_end),
         (agent_set_animation, ":agent_no", "anim_active_enchant_2", 1),

         (agent_get_position, pos1, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (try_for_agents, ":object_agent_no", pos1, ":distance_no"),
            (agent_is_alive, ":object_agent_no"),
            (agent_is_human, ":object_agent_no"),
            (agent_get_team, ":object_team_no", ":object_agent_no"),
            (neg|teams_are_enemies, ":team_no", ":object_team_no"),#不是敌军

            (call_script, "script_proceed_state", ":object_agent_no", ":state_no", ":timer_count"),
            (agent_set_animation, ":object_agent_no", "anim_cheer_new", 1),
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_warcy_bloodburst"),#血涌战号
         (agent_get_wielded_item, ":weapon_no", ":agent_no", 0),#武器
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_blood_burst", 3),#自身减少最多三层血潮汹涌
         (this_or_next|gt, reg1, 0),                                             #success
         (eq, ":weapon_no", "itm_bloodburst_sword"),#具有血潮汹涌或正在使用血涌剑
         (try_begin),
            (this_or_next|ge, reg1, 3),#实际消耗了三层，发动血爆
            (eq, ":weapon_no", "itm_bloodburst_sword"),#达到三层或正在使用血涌剑
            (assign, ":item_no", "itm_blood_explosion"),
         (else_try),
            (assign, ":item_no", "itm_blood_overflow"),#血溢
         (try_end),
         (agent_set_animation, ":agent_no", "anim_active_enchant_3"),

         (try_begin),
            (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),
            (ge, ":target_agent_no", 0),
            (agent_get_position, pos1, ":target_agent_no"),
         (else_try),
            (agent_get_position, pos1, ":agent_no"),
         (try_end),
         (set_spawn_position, pos1),
         (spawn_item, ":item_no", 0, 3),
         (assign, ":cur_instance", reg0),
         (scene_prop_set_slot, ":cur_instance", slot_instance_item, ":item_no"),
         (prop_instance_deform_in_range, ":cur_instance", 0, 110, 3100),
         (call_script, "script_mission_create_timer", -1, ":cur_instance", 300, 1),#计时器

      (else_try),
         (eq, ":active_skill_no", "itm_active_warcy_red_tide"),#赤潮战号
         (agent_set_animation, ":agent_no", "anim_active_enchant_3"),
         (agent_get_position, pos1, ":agent_no"),
         (particle_system_burst, "psys_blood_splash", pos1),
         (play_sound_at_position, "snd_body_fall_big", pos1),
         (try_for_agents, ":beattacked_agent_no", pos1, 300),
            (agent_is_alive, ":beattacked_agent_no"),
            (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_blood_burst", 3),#增加三层血潮汹涌
         (try_end),

      (else_try),
         (eq, ":active_skill_no", "itm_active_warcy_bloodrain"),#唤来血雨的战吼
         (agent_set_animation, ":agent_no", "anim_active_warcy_bloodrain"),
         (store_mul, "$battle_environment", "itm_active_warcy_bloodrain", 10000),#血雨环境
         (val_add, "$battle_environment", 1000),#10秒

         (try_for_agents, ":beattacked_agent_no"),
            (agent_is_alive, ":beattacked_agent_no"),
#            (agent_is_human, ":beattacked_agent_no"),
            (call_script, "script_proceed_state", ":beattacked_agent_no", "itm_state_blood_burst", 3),#全场施加三层血潮汹涌,
         (try_end),
         (play_track, "track_blood_rain", 2),#立即播放音乐

      (else_try),
         (eq, ":active_skill_no", "itm_active_rib_shot"),#肋骨射击
         (agent_set_animation, ":agent_no", "anim_active_enchant_5", 1),
         (agent_get_position, pos1, ":agent_no"),
         (position_move_y, pos1, 150),#身前1.5米
         (set_spawn_position, pos1),
         (spawn_item, "itm_skeleton_spear_anim", 0, 2),
         (assign, ":cur_instance", reg0),
         (scene_prop_set_slot, ":cur_instance", slot_instance_agent_used, ":agent_no"),
         (scene_prop_set_slot, ":cur_instance", slot_instance_item, "itm_skeleton_spear_anim"),
         (prop_instance_deform_in_range, ":cur_instance", 0, 600, 2300),
         (call_script, "script_mission_create_timer", -1, ":cur_instance", 180, 1),#计时器

      (else_try),
         (eq, ":active_skill_no", "itm_active_triple_rib_shot"),#三重肋骨射击
         (agent_set_animation, ":agent_no", "anim_active_enchant_5", 1),
         (agent_get_position, pos1, ":agent_no"),
         (position_move_y, pos1, 150),#身前1.5米
         (position_move_x, pos1, -50),
         (try_for_range, reg1, 0, 3),
            (set_spawn_position, pos1),
            (spawn_item, "itm_skeleton_spear_anim", 0, 2),
            (assign, ":cur_instance", reg0),
            (scene_prop_set_slot, ":cur_instance", slot_instance_agent_used, ":agent_no"),
            (scene_prop_set_slot, ":cur_instance", slot_instance_item, "itm_skeleton_spear_anim"),
            (prop_instance_deform_in_range, ":cur_instance", 0, 600, 2300),
            (call_script, "script_mission_create_timer", -1, ":cur_instance", 180, 1),#计时器
            (position_move_x, pos1, 50),
         (try_end),

      (else_try),
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton"),#创造复生骷髅要求7
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton_pikeman"),#创造骷髅战士要求12
         (this_or_next|eq, ":active_skill_no", "itm_active_undead_creation_skeleton_swordman"),#创造骷髅剑士要求12
         (eq, ":active_skill_no", "itm_active_undead_creation_skeleton_archer"),#创造骷髅重弓手要求16
         (agent_set_animation, ":agent_no", "anim_command_anim_1", 1),
         (agent_get_position, pos1, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (position_move_y, pos1, 200),
         (set_spawn_position, pos1),
         (try_begin),
            (eq, ":active_skill_no", "itm_active_undead_creation_skeleton"),#创造复生骷髅
            (spawn_agent, "trp_rebirth_skeleton"),
         (else_try),
            (eq, ":active_skill_no", "itm_active_undead_creation_skeleton_pikeman"),#创造骷髅战士
            (spawn_agent, "trp_skeleton_warrior"),
         (else_try),
            (eq, ":active_skill_no", "itm_active_undead_creation_skeleton_swordman"),#创造骷髅剑士
            (spawn_agent, "trp_skeleton_swordman"),
         (else_try),
            (eq, ":active_skill_no", "itm_active_undead_creation_skeleton_archer"),#创造骷髅重弓手
            (spawn_agent, "trp_skeleton_heavy_archer"),
         (try_end),

         (assign, ":spawn_agent_no", reg0),
         (agent_set_team, ":spawn_agent_no", ":team_no"),
         (agent_add_relation_with_agent, ":spawn_agent_no", ":agent_no", 1),
         (agent_set_animation, ":spawn_agent_no", "anim_active_skeleton_rebirth_1", 0),#出场动作
         (agent_get_position, pos1, ":spawn_agent_no"),
         (particle_system_burst, "psys_normal_splash", pos1, 30),
         (play_sound_at_position, "snd_break_ground", pos1),
         (item_get_food_quality, ":skill_request", ":active_skill_no"),
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_moving_cemetery", ":skill_request"),#减少移动墓地
#         (call_script, "script_creature_load_to_slot", ":agent_no", ":spawn_agent_no"),#存进slot里

      (else_try),
         (eq, ":active_skill_no", "itm_active_undead_creation_wild_hunter"),#召来狂猎要求500
         (agent_set_animation, ":agent_no", "anim_command_anim_1", 1),
         (agent_get_position, pos1, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (position_move_y, pos1, 200),
         (position_move_x, pos1, -1100),

         (try_for_range, reg1, 0, 12),
            (set_spawn_position, pos1),
            (spawn_agent, "trp_kouruto_wild_hunter_cavalry"),
            (assign, ":spawn_agent_no", reg0),
            (agent_set_team, ":spawn_agent_no", ":team_no"),
            (agent_add_relation_with_agent, ":spawn_agent_no", ":agent_no", 1),
            (agent_set_animation, ":spawn_agent_no", "anim_command_anim_2", 1),
            (agent_get_horse, ":agent_horse_no", ":spawn_agent_no"),
            (agent_set_animation, ":agent_horse_no", "anim_active_skeleton_horse_rebirth", 0),#出场动作

            (agent_get_position, pos1, ":spawn_agent_no"),
            (particle_system_burst, "psys_normal_splash", pos1, 30),
            (play_sound_at_position, "snd_break_ground", pos1),
            (position_move_x, pos1, 200),
         (try_end),
         (item_get_food_quality, ":skill_request", ":active_skill_no"),
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_moving_cemetery", ":skill_request"),#减少移动墓地

      (else_try),
         (eq, ":active_skill_no", "itm_active_undead_creation_giant"),#创造不死组合巨人
         (agent_set_animation, ":agent_no", "anim_command_anim_1", 1),
         (try_begin),
            (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),#目标前方八米处
            (ge, ":target_agent_no", 0),
            (agent_get_position, pos1, ":target_agent_no"),
            (position_move_y, pos1, 800),
            (position_rotate_z, pos1, 180),
         (else_try),
            (agent_get_position, pos1, ":agent_no"),
         (try_end),

         (set_spawn_position, pos1),
         (particle_system_burst, "psys_normal_splash", pos1, 100),
         (play_sound_at_position, "snd_hit_ground", pos1),
         (spawn_item, "itm_skeleton_giant", 0, 6),
         (assign, ":cur_instance", reg0),
         (scene_prop_set_slot, ":cur_instance", slot_instance_item, "itm_skeleton_giant"),
         (scene_prop_set_slot, ":cur_instance", slot_instance_agent_used, ":agent_no"),
         (prop_instance_deform_in_range, ":cur_instance", 0, 320, 6300),
         (call_script, "script_mission_create_timer", -1, ":cur_instance", 400, 1),#计时器
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_moving_cemetery", 20),#减少20份移动墓地

      (else_try),
         (eq, ":active_skill_no", "itm_active_undead_creation_giant_sword"),#创造剑骸组合巨人
         (agent_set_animation, ":agent_no", "anim_command_anim_1", 1),
         (try_begin),
            (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),#目标前方十米处
            (ge, ":target_agent_no", 0),
            (agent_get_position, pos1, ":target_agent_no"),
            (position_move_y, pos1, 1000),
            (position_rotate_z, pos1, 180),
         (else_try),
            (agent_get_position, pos1, ":agent_no"),
         (try_end),

         (set_spawn_position, pos1),
         (particle_system_burst, "psys_normal_splash", pos1, 100),
         (play_sound_at_position, "snd_hit_ground", pos1),
         (spawn_item, "itm_skeleton_giant_sword", 0, 6),
         (assign, ":cur_instance", reg0),
         (scene_prop_set_slot, ":cur_instance", slot_instance_item, "itm_skeleton_giant_sword"),
         (scene_prop_set_slot, ":cur_instance", slot_instance_agent_used, ":agent_no"),
         (prop_instance_deform_in_range, ":cur_instance", 0, 470, 6300),
         (call_script, "script_mission_create_timer", -1, ":cur_instance", 400, 1),#计时器
         (call_script, "script_restrain_state_full", ":agent_no", "itm_state_moving_cemetery", 30),#减少30份移动墓地

      (else_try),
         (eq, ":active_skill_no", "itm_active_create_spectre"),#创造屑灵
         (agent_set_animation, ":agent_no", "anim_command_anim_1", 1),
         (agent_get_bone_position, pos1, ":agent_no", hb_head, 1),#头
         (agent_get_position, pos2, ":agent_no"),
         (call_script, "script_pos_copy_rotation_from_pos", pos1, pos2),#复制旋转角
         (position_move_y, pos1, -30),
         (try_begin),
            (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),
            (ge, ":target_agent_no", 0),
            (agent_get_bone_position, pos2, ":target_agent_no", hb_abdomen, 1),#腹部
         (else_try),
            (copy_position, pos2, pos1),#向前射击
            (position_move_y, pos2, 1000),
         (try_end),
         (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
         (add_missile, ":agent_no", pos1, 1000, "itm_spectre", 0, "itm_spectre", 0),

      (else_try),
         (eq, ":active_skill_no", "itm_active_create_spectre_group"),#创造屑灵集群
         (agent_set_animation, ":agent_no", "anim_command_anim_1", 1),
         (agent_get_bone_position, pos5, ":agent_no", hb_head, 1),#头
         (agent_get_position, pos6, ":agent_no"),
         (call_script, "script_pos_copy_rotation_from_pos", pos5, pos6),#复制旋转角
#         (position_move_y, pos5, -30),
         (position_move_x, pos5, -50),
         (try_begin),
            (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),
            (ge, ":target_agent_no", 0),
            (agent_get_bone_position, pos6, ":target_agent_no", hb_abdomen, 1),#腹部
         (else_try),
            (copy_position, pos6, pos5),#向前射击
            (position_move_y, pos6, 1000),
         (try_end),

         (try_for_range, reg1, 0, 3),
            (copy_position, pos1, pos5),
            (copy_position, pos2, pos6),
            (call_script, "script_pos_aim_at_pos", pos1, pos2),#获取射击方向
            (add_missile, ":agent_no", pos1, 1000, "itm_spectre", 0, "itm_spectre", 0),
            (position_move_y, pos5, -30),
            (position_move_x, pos5, 50),
         (try_end),

      (else_try),
         (this_or_next|eq, ":active_skill_no", "itm_active_pray_holy_aegis"),#神术：圣盾
         (this_or_next|eq, ":active_skill_no", "itm_active_pray_heavenly_wall"),#神术：天国之壁
         (eq, ":active_skill_no", "itm_active_pray_drop_of_reasoning_sea"),#神术：理海之心
         (try_begin),
            (eq, ":active_skill_no", "itm_active_pray_holy_aegis"),
            (assign, ":scene_prop_target", "spr_sorcery_aegis"),
            (assign, ":duration", 400),#持续四秒
         (else_try),
            (eq, ":active_skill_no", "itm_active_pray_heavenly_wall"),
            (assign, ":scene_prop_target", "spr_sorcery_heavenly_wall"),
            (assign, ":duration", 800),#持续八秒
         (else_try),
            (eq, ":active_skill_no", "itm_active_pray_drop_of_reasoning_sea"),
            (assign, ":scene_prop_target", "spr_sorcery_drop_of_reasoning_sea"),
            (assign, ":duration", 1200),#持续十二秒
         (try_end),
         (agent_set_animation, ":agent_no", "anim_active_pray_shield"),

         (try_begin),
            (agent_has_item_equipped, ":agent_no", "itm_patron_plate"),#守护者板甲
            (val_add, ":duration", 2),
         (else_try),
            (agent_has_item_equipped, ":agent_no", "itm_patron_high_plate"),#高阶守护者板甲
            (val_add, ":duration", 4),
         (try_end),

         (agent_get_position, pos1, ":agent_no"),
         (position_move_y, pos1, 200),
         (position_move_z, pos1, 120),#生成在前方
         (call_script, "script_sepcial_effect_create", ":agent_no", ":scene_prop_target", pos1),#生成正规spr
         (assign, ":instance_no", reg1),
         (call_script, "script_mission_create_timer", -1, ":instance_no", ":duration", 1),#计时器
      (try_end),
    ]),



#生成正规scene prop的特效件
#返回生成的instance的ID，储存至reg1
  ("sepcial_effect_create", [
      (store_script_param, ":master_agent_no", 1),
      (store_script_param, ":scene_prop_target", 2),#目标特效件
      (store_script_param, ":pos_no", 3),#生成位置

      (try_begin),
         (assign, ":instance_no", -1),
         (try_for_prop_instances, ":scene_prop_no", ":scene_prop_target"),#获取是否有现成且未被使用的该特效件
            (neg|scene_prop_slot_ge, ":scene_prop_no", slot_instance_agent_used, 0),
            (assign, ":instance_no", ":scene_prop_no"),
         (try_end),
         (try_begin),
            (lt, ":instance_no", 0),#没有现成的
            (set_spawn_position, ":pos_no"),
            (spawn_scene_prop, ":scene_prop_target"),
            (assign, ":instance_no", reg0),
         (else_try),
           (scene_prop_set_visibility, ":instance_no", 1),
            (prop_instance_set_position, ":instance_no", ":pos_no"),
         (try_end),
         (scene_prop_set_slot, ":instance_no", slot_instance_agent_used, ":master_agent_no"),
        (scene_prop_set_slot, ":instance_no", slot_instance_item, -1),#正规spr无原型item
      (try_end),
      (assign, reg1, ":instance_no"),
    ]),

#特效件加载进slot
#有空位就往空位填，没空位就填进slot 1。返回实际存入的slot值。
  ("sepcial_effect_load_to_slot", [
      (store_script_param, ":master_agent_no", 1),
      (store_script_param, ":instance_no", 2),
      (store_script_param, ":bone_no", 3),#特效件附加到其上的骨骼

      (val_add, ":bone_no", 1),
      (val_mul, ":bone_no", 10000),
      (val_add, ":instance_no", ":bone_no"),
      (assign, ":continue_no", 0),
      (try_for_range, ":count_no", 0, 3),
         (store_add, ":slot_no", slot_agent_prop_using_1, ":count_no"),
         (neg|agent_slot_ge, ":master_agent_no", ":slot_no", 0),
         (agent_set_slot, ":master_agent_no", ":slot_no", ":instance_no"),
         (assign, ":continue_no", ":slot_no"),
      (try_end),
      (try_begin),
         (eq, ":continue_no", 0),
         (agent_set_slot, ":master_agent_no", slot_agent_prop_using_1, ":instance_no"),
         (assign, ":continue_no", slot_agent_prop_using_1),
      (try_end),

      (agent_get_slot, ":sepcial_effect_count", ":master_agent_no", slot_agent_sepcial_effect_num),#统计
      (val_max, ":sepcial_effect_count", 0),
      (val_add, ":sepcial_effect_count", 1),
      (val_min, ":sepcial_effect_count", 3),#最多三个特效件
      (agent_set_slot, ":master_agent_no", slot_agent_sepcial_effect_num, ":sepcial_effect_count"), 
      (assign, reg1, ":continue_no"),
    ]),

#召唤物加载进slot
#有空位就往空位填，没空位就填进slot 1。返回实际存入的slot值。
  ("creature_load_to_slot", [
      (store_script_param_1, ":master_agent_no"),
      (store_script_param_2, ":creature_agent_no"),

      (assign, ":continue_no", 0),
      (try_for_range, ":count_no", 0, 5),
         (store_add, ":slot_no", slot_agent_creature_1, ":count_no"),
         (neg|agent_slot_ge, ":master_agent_no", ":slot_no", 0),
         (agent_set_slot, ":master_agent_no", ":slot_no", ":creature_agent_no"),
         (assign, ":continue_no", ":slot_no"),
      (try_end),
      (try_begin),
         (eq, ":continue_no", 0),
         (agent_set_slot, ":master_agent_no", slot_agent_creature_1, ":creature_agent_no"),
         (assign, ":continue_no", slot_agent_creature_1),
      (try_end),
      (assign, reg1, ":continue_no"),
    ]),


#————————————————————————————————————骑技类————————————————————————————————
#骑技启动
  ("cf_riding_skill_technique", [
      (store_script_param_1, ":attacker_agent_no"),
      (store_script_param_2, ":active_skill_no"),

      (item_has_property, ":active_skill_no", itp_riding_skill),
#骑技涉及骑手（如果有的话）和坐骑，且以坐骑为主，因此双方都要判断是否能使用武技
      (agent_is_alive, ":attacker_agent_no"),
      (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_skill_timer, 1),
      (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_activiting_skill, 1),#当前未使用技能
#武技完成最后一个判定点后就会消除slot_agent_activiting_skill，停止继续判定以节省算力，但slot_agent_skill_timer还会继续运行作为后摇。因此两个都需要检测。
      (assign, ":continue_no", 0),
      (try_begin),
         (neg|agent_is_human, ":attacker_agent_no"),#是马
         (agent_get_rider, ":attacker_rider_agent", ":attacker_agent_no"),
         (try_begin),
            (ge, ":attacker_rider_agent", 0),#如果有骑手
            (neg|agent_slot_ge, ":attacker_rider_agent", slot_agent_skill_timer, 1),
            (neg|agent_slot_ge, ":attacker_rider_agent", slot_agent_activiting_skill, 1),#当前未使用技能
            (assign, ":continue_no", 1),
         (else_try),
            (lt, ":attacker_rider_agent", 0),#无骑手
            (neg|item_has_property, ":active_skill_no", itp_damage_type),#近战类型的技能，必须有骑手
            (assign, ":continue_no", 1),
         (try_end),
      (else_try),
         (agent_is_human, ":attacker_agent_no"),#是人
         (assign, ":attacker_rider_agent", ":attacker_agent_no"),
         (agent_get_horse, ":attacker_agent_no", ":attacker_rider_agent"),
         (ge, ":attacker_agent_no", 0),#避免步兵发动骑技
         (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_skill_timer, 1),
         (neg|agent_slot_ge, ":attacker_agent_no", slot_agent_activiting_skill, 1),#当前未使用技能
         (assign, ":continue_no", 1),
      (try_end),
      (eq, ":continue_no", 1),
#获取结果：":attacker_agent_no"是马，":attacker_rider_agent"是人（不一定存在），双方都没有被其他技能占用。带itp_damage_type的必须人马配合。

#获取目标
      (try_begin),
         (item_has_property, ":active_skill_no", itp_damage_type),#通用的造成伤害型所需要的释放准备
         (try_for_range, ":count_no", 0, 10),
            (store_add, ":slot_no", ":count_no", slot_agent_surrounded_enemy_1),#清空
            (agent_set_slot, ":attacker_rider_agent", ":slot_no", -1),
         (try_end),

         #获取主动技能动作
         (item_get_slot, ":attacker_anim_no", ":active_skill_no", slot_active_skill_attacker_horse_anim),#坐骑
         (gt, ":attacker_anim_no", 0), 
         (item_get_slot, ":rider_anim_no", ":active_skill_no", slot_active_skill_attacker_anim),#骑手
         (gt, ":rider_anim_no", 0),
         (agent_get_position, pos1, ":attacker_rider_agent"),#获取位置

         (set_fixed_point_multiplier, 100),
         (agent_get_team, ":attacker_team_no",  ":attacker_rider_agent"),
         (agent_get_wielded_item, ":weapon_no", ":attacker_rider_agent", 0),
         (gt, ":weapon_no", 0),
         (item_get_weapon_length, ":weapon_length", ":weapon_no"),#cm
         (agent_set_slot, ":attacker_rider_agent", slot_agent_weapon_length, ":weapon_length"),#记录武器长度
#         (val_add, ":weapon_length", 150),

         (assign, ":slot_no", slot_agent_surrounded_enemy_1),                                    #获取目标
         (try_for_agents, ":agent_no", pos1, 1000),#10米范围内
            (agent_is_alive,  ":agent_no"),
            (neq, ":attacker_rider_agent", ":agent_no"),                                                     #不是进攻者
            (le, ":slot_no", slot_agent_surrounded_enemy_10),                                      #最多命中十人
            (assign, ":continue", 0),
            (try_begin),
               (agent_is_human,  ":agent_no"),#人
               (agent_get_team, ":team_no",  ":agent_no"),
               (teams_are_enemies, ":attacker_team_no", ":team_no"), #敌对
               (assign, ":continue", 1),
            (else_try),
               (neg|agent_is_human,  ":agent_no"),#无主马
               (agent_get_rider, ":rider_agent_no", ":agent_no"),
               (lt, ":rider_agent_no", 0),#have no rider
               (assign, ":continue", 1),
            (else_try),
               (neg|agent_is_human,  ":agent_no"),#有主马
               (ge, ":rider_agent_no", 0),#have rider
               (agent_get_team, ":team_no",  ":rider_agent_no"),
               (teams_are_enemies, ":attacker_team_no", ":team_no"), #敌对骑手
               (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),

            (agent_set_slot, ":attacker_rider_agent", ":slot_no", ":agent_no"),
            (val_add, ":slot_no", 1),
         (try_end),

      (else_try),
         (item_has_property, ":active_skill_no", itp_special_type),#有特殊效果
         (try_begin),
            (eq, ":active_skill_no", "itm_active_war_stomp"),#战争践踏
            (assign, ":attacker_anim_no", "anim_active_war_stomp"),#马
            (assign, ":rider_anim_no", "anim_active_war_stomp_rider"),#人
         (else_try),
            (eq, ":active_skill_no", "itm_active_silver_fall"),#银落
            (ge, ":attacker_rider_agent", 0),
            (assign, ":attacker_anim_no", "anim_active_silver_fall"),#马
            (assign, ":rider_anim_no", "anim_active_silver_fall_rider"),#人
         (try_end),
      (try_end),

      (gt, ":attacker_anim_no", 0),#成功获取
      (agent_set_animation, ":attacker_agent_no", "anim_horse_rear", 0),#用惊马的动作停马
      (agent_set_animation, ":attacker_agent_no", ":attacker_anim_no", 0),#马的动作一定有
      (item_get_max_ammo, ":max_timer", ":active_skill_no"),           #获取技能时间，都是以0.1秒为单位。
      (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":max_timer"),#开始计时
      (agent_set_slot, ":attacker_agent_no", slot_agent_activiting_skill, ":active_skill_no"),#设置当前使用的技能

      (try_begin),
         (ge, ":attacker_rider_agent", 0),
         (gt, ":rider_anim_no", 0),
         (agent_set_animation, ":attacker_rider_agent", ":rider_anim_no", 0),
         (agent_set_slot, ":attacker_rider_agent", slot_agent_skill_timer, ":max_timer"),#开始计时
         (agent_set_slot, ":attacker_rider_agent", slot_agent_activiting_skill, ":active_skill_no"),#设置当前使用的技能
      (try_end),
(str_store_item_name, s1, ":active_skill_no"),
(display_message, "@成 功 发 动 {s1}"),
    ]),


#————————————————————————————————————投技类————————————————————————————————
#投技启动
  ("cf_grab_skill_technique", [
      (store_script_param_1, ":attacker_agent_no"),
      (store_script_param_2, ":active_skill_no"),
      (item_has_property, ":active_skill_no", itp_grab_skill),
      (agent_is_human, ":attacker_agent_no"),#是人
      (agent_is_alive, ":attacker_agent_no"),
      (set_fixed_point_multiplier, 100),
      (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),

#获取目标
      (assign, ":attacker_anim_no", 0),
      (try_begin),
         (item_has_property, ":active_skill_no", itp_special_type),#有特殊效果
         (try_begin),
            (eq, ":active_skill_no", "itm_active_cutthroat"),#割喉
            (gt, ":weapon_no", 0),
            (item_get_weapon_length, ":weapon_length", ":weapon_no"),#cm
            (le, ":weapon_length", 120),#1.2米以下的武器才能用
            (agent_get_horse, ":attacker_horse_no", ":attacker_agent_no"),#步行
            (lt, ":attacker_horse_no", 0),
            (assign, ":attacker_anim_no", "anim_active_cutthroat_prepare"),
         (try_end),
      (try_end),
      (gt, ":attacker_anim_no", 0),#成功获取

      (agent_set_animation, ":attacker_agent_no", ":attacker_anim_no", 0),
      (item_get_abundance, ":time_count", ":active_skill_no"),#获取基础前摇时长
      (val_add, ":time_count", 10000),#万位用于记录投技前摇的阶段，万位为1表示前摇，为0则是效应阶段的后摇。千位用于记录武技的阶段了，不要混淆，检测时检测ge 10000即可。
      (agent_set_slot, ":attacker_agent_no", slot_agent_skill_timer, ":time_count"),#开始计时
      (agent_set_slot, ":attacker_agent_no", slot_agent_activiting_skill, ":active_skill_no"),#设置当前使用的技能

(str_store_item_name, s1, ":active_skill_no"),
(display_message, "@准 备 发 动 {s1}"),
    ]),


#投技开始生效
#即在前摇结束以后，判断敌方是不是还在捕捉范围里，是就是继续后续的结果。
  ("cf_AoM_active_grab_skill_success", [
      (store_script_param_1, ":active_skill_no"),
      (store_script_param_2, ":agent_no"),

      (set_fixed_point_multiplier, 100),
      (item_get_weapon_length, ":grab_distance", ":active_skill_no"),#捕捉距离（单位厘米）
      (assign, ":grabed_agent_no", -1),
      (agent_get_position, pos1, ":agent_no"),
      (agent_get_team, ":attacker_team_no",  ":agent_no"),
      (try_begin),
         (agent_get_slot, ":target_agent_no", ":agent_no", slot_ai_target),
         (ge, ":target_agent_no", 0),
         (agent_is_human, ":target_agent_no"),#是人
         (agent_is_alive, ":target_agent_no"),
         (agent_get_team, ":target_team_no",  ":target_agent_no"),
         (teams_are_enemies, ":attacker_team_no", ":target_team_no"),#排除友军
         (neg|agent_slot_ge, ":target_agent_no", slot_agent_skill_timer, 1),#正在使用技能等，有霸体
         (agent_get_horse, ":target_horse_no", ":target_agent_no"),#步行
         (lt, ":target_horse_no", 0),

         (agent_get_position, pos2, ":target_agent_no"),
         (neg|position_is_behind_position, pos2, pos1),#排除背后
         (get_distance_between_positions, ":position_distance_1", pos1, pos2),
         (le, ":position_distance_1", ":grab_distance"),#捕捉范围内
         (assign, ":grabed_agent_no", ":target_agent_no"),

      (else_try),
         (try_for_agents, ":target_agent_no", pos1, ":grab_distance"),#捕捉范围内
            (agent_is_human, ":target_agent_no"),#是人
            (agent_is_alive, ":target_agent_no"),
            (agent_get_team, ":target_team_no",  ":target_agent_no"),
            (teams_are_enemies, ":attacker_team_no", ":target_team_no"),#排除友军
            (neg|agent_slot_ge, ":target_agent_no", slot_agent_skill_timer, 1),#正在使用技能等，有霸体
            (agent_get_horse, ":target_horse_no", ":target_agent_no"),#步行
            (lt, ":target_horse_no", 0),

            (agent_get_position, pos2, ":target_agent_no"),
            (neg|position_is_behind_position, pos2, pos1),#排除背后
            (assign, ":grabed_agent_no", ":target_agent_no"),
         (try_end),
      (try_end),
      (ge, ":grabed_agent_no", 0),
      (agent_set_slot, ":agent_no", slot_ai_target, ":grabed_agent_no"),

(str_store_item_name, s1, ":active_skill_no"),
(display_message, "@{s1}命 中 "),

      (item_get_max_ammo, ":timer_count", ":active_skill_no"),
      (try_begin),
         (eq, ":active_skill_no", "itm_active_cutthroat"),#割喉
         (agent_set_animation, ":agent_no", "anim_active_cutthroat_1", 0),
         (agent_set_animation, ":grabed_agent_no", "anim_active_cutthroat_2", 0),
         (agent_get_position, pos1, ":agent_no"),
         (agent_set_position, ":grabed_agent_no", pos1),
         (agent_set_slot, ":grabed_agent_no", slot_agent_skill_timer, ":timer_count"),#被抓取者的僵直
      (try_end),
    ]),


#投技结果
#效应部分，投机和其他武技一样都有阶段的控制
  ("AoM_grab_skill", [
      (store_script_param, ":attacker_agent_no", 1),#攻击者
      (store_script_param, ":active_skill_no", 2),#技能
      (store_script_param, ":time_point", 3),#检查点
#      (set_fixed_point_multiplier, 100),

      (try_begin),
         (eq, ":active_skill_no", "itm_active_cutthroat"),#割喉
         (try_begin),
            (eq, ":time_point", 13),
            (agent_get_slot, ":beattacked_agent_no", ":attacker_agent_no", slot_ai_target),
            (ge, ":beattacked_agent_no", 0),
            (agent_is_human, ":beattacked_agent_no"),#是人
            (agent_is_alive, ":beattacked_agent_no"),
            (item_get_food_quality, ":damage", ":active_skill_no"),#基础伤害
            (agent_get_wielded_item, ":weapon_no", ":attacker_agent_no", 0),
            (gt, ":weapon_no", 0),
            (try_begin),
               (eq, "$infiltrate_tut", 1),                                                                    #潜行模式敌方无警戒或警戒一，即死
               (neg|agent_slot_eq, ":beattacked_agent_no", slot_agent_alarmed_level, 2),
               (agent_set_hit_points, ":beattacked_agent_no", 0, 1),
            (else_try),
               (assign, ":hp_level", 60),
               (store_agent_hit_points, ":agent_hp", ":beattacked_agent_no", 1),#血量少于60，即死
               (try_begin),
                  (eq, ":weapon_no", "itm_ghost_knife"),#灵体匕首
                  (val_add, ":hp_level", 20),
               (else_try),
                  (eq, ":weapon_no", "itm_ghost_sickle"),#午夜割喉之镰
                  (val_add, ":hp_level", 60),
               (try_end),
               (lt, ":agent_hp", ":hp_level"),
               (agent_set_hit_points, ":beattacked_agent_no", 0, 1),
            (try_end),
            (agent_deliver_damage_to_agent, ":attacker_agent_no", ":beattacked_agent_no", ":damage", ":weapon_no"),#造成伤害
         (try_end),
      (try_end),
    ]),




#############################################################被动技能相关###################################################

#习得被动技能
#Input troop no, skill no and level
  ("set_troop_passive_skill_level", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":skill_no", 2),
      (store_script_param, ":level_no", 3),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_passive_skills_begin"),
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_passive_skill_learned_1),#15 skills in a group

      (troop_get_slot, ":passive_skill_count", ":troop_no", ":count_no_group"),
      (try_begin),
         (item_get_abundance, ":value_no", ":skill_no"),
         (gt, ":value_no", ":level_no"),
         (assign, ":level_no", ":value_no"),
      (try_end),
      (call_script, "script_set_digital_position", ":passive_skill_count", ":count_no_position", ":level_no"),
      (troop_set_slot, ":troop_no", ":count_no_group", reg1),
    ]),

#激活被动技能
#Input troop no, skill no and level
  ("set_troop_passive_skill_on", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":skill_no", 2),
      (store_script_param, ":level_no", 3),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_passive_skills_begin"),
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_passive_skill_1),#15 skills in a group

      (troop_get_slot, ":passive_skill_count", ":troop_no", ":count_no_group"),
      (try_begin),
         (item_get_abundance, ":value_no", ":skill_no"),
         (lt, ":value_no", ":level_no"),
         (assign, ":level_no", ":value_no"),
      (try_end),
      (call_script, "script_set_digital_position", ":passive_skill_count", ":count_no_position", ":level_no"),
      (troop_set_slot, ":troop_no", ":count_no_group", reg1),
    ]),


#关闭被动技能（设为0级）
#Input troop no, skill no
  ("set_troop_passive_skill_off", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":skill_no", 2),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_passive_skills_begin"),
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_passive_skill_1),#15 skills in a group

      (troop_get_slot, ":passive_skill_count", ":troop_no", ":count_no_group"),
      (call_script, "script_set_digital_position", ":passive_skill_count", ":count_no_position", 0),
      (troop_set_slot, ":troop_no", ":count_no_group", reg1),
    ]),


#激活被动技能（简易版）
#不需要输入等级，自动获取等级并激活。
#因为是玩家专用（只有玩家才有习得但未激活状态），只需输入技能ID。
#Input troop no, skill no and level
  ("set_player_passive_skill_on_simple", [
      (store_script_param, ":skill_no", 1),
      (call_script, "script_check_troop_passive_skill_learned", "trp_player", ":skill_no"),
      (try_begin),
         (gt, reg1, 0),
         (call_script, "script_set_troop_passive_skill_on", "trp_player", ":skill_no", reg1),
      (try_end),
    ]),


#检测被动技能是否习得
#Check if troop learned certain passive skill, input troop no and passive skill id. Output number as this skill's level
  ("check_troop_passive_skill_learned", [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":skill_no"),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_passive_skills_begin"),
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_passive_skill_learned_1),#15 skills in a group

      (troop_get_slot, ":passive_skill_count", ":troop_no", ":count_no_group"),
      (try_begin),
         (gt, ":passive_skill_count", 0),
         (call_script, "script_get_digital_position", ":passive_skill_count", ":count_no_position"),
      (try_end),
#output reg1
    ]),


#提升被动技能（只看是否已学习，对玩家用）
#输入兵种、技能、提升的数值
  ("improve_troop_passive_skill_learned", [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":skill_no"),
      (store_script_param, ":count_no", 3),#提升的数值
      (assign, reg1, 0),

      (call_script, "script_check_troop_passive_skill_learned", ":troop_no", ":skill_no"),
      (val_add, reg1, ":count_no"),
      (item_get_abundance, ":level_no", ":skill_no"),
      (val_min, ":level_no", reg1),
      (call_script, "script_set_troop_passive_skill_level", ":troop_no", ":skill_no", ":level_no"),

      (try_begin),
         (eq, ":troop_no", "trp_player"),
         (call_script, "script_check_troop_passive_skill_activited", ":troop_no", ":skill_no"),
         (call_script, "script_set_player_passive_skill_on_simple", ":skill_no"),
      (else_try),
         (neq, ":troop_no", "trp_player"),
         (call_script, "script_set_troop_passive_skill_on", ":troop_no", ":skill_no", ":level_no"),
      (try_end),
    ]),


#检测被动技能是否激活
#Check if troop activited certain passive skill, input troop no and passive skill id. Output number as this skill's level
  ("check_troop_passive_skill_activited", [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":skill_no"),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_passive_skills_begin"),
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_troop_passive_skill_1),#15 skills in a group

      (troop_get_slot, ":passive_skill_count", ":troop_no", ":count_no_group"),
      (try_begin),
         (gt, ":passive_skill_count", 0),
         (call_script, "script_get_digital_position", ":passive_skill_count", ":count_no_position"),
      (try_end),
#output reg1
    ]),


#统计激活的被动
#输出reg1
  ("calculate_troop_passive_skill_activited", [
      (store_script_param_1, ":troop_no"),

      (assign, ":count_no", 0),
      (store_add, ":skill_begin", "itm_passive_skills_begin", 1),
      (try_for_range, ":skill_no", ":skill_begin", "itm_passive_skills_end"),
         (call_script, "script_check_troop_passive_skill_activited", ":troop_no", ":skill_no"),#已激活
         (gt, reg1, 0),
         (val_add, ":count_no", 1),
      (try_end),
      (assign, reg1, ":count_no"),
#output reg1
    ]),


#agent检测激活
#Check if agent have certain passive skill, input agent no and passive skill id. Output number as this skill's level
  ("check_agent_passive_skill", [
      (store_script_param_1, ":agent_no"),
      (store_script_param_2, ":skill_no"),
      (assign, reg1, 0),

      (store_sub, ":count_no", ":skill_no", "itm_passive_skills_begin"),
      (val_sub, ":count_no", 1),
      (store_div, ":count_no_group", ":count_no", 15),
      (store_mod, ":count_no_position", ":count_no", 15),
      (val_add, ":count_no_position", 1),
      (val_add, ":count_no_group", slot_agent_passive_skill_1),#15 skills in a group

      (agent_get_slot, ":passive_skill_count", ":agent_no", ":count_no_group"),
      (try_begin),
         (gt, ":passive_skill_count", 0),
         (call_script, "script_get_digital_position", ":passive_skill_count", ":count_no_position"),
      (try_end),
#output reg1
    ]),




#############################################################状态相关###################################################

#计时类状态效果控制器
#input agent no and state no, output new timer_count in reg1.
  ("timer_state_technique", [
      (store_script_param, ":agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":timer_count", 3),

##############参数准备##############
      (item_get_abundance, ":add_value", ":state_no"),
      (item_get_max_ammo, ":timer_threshold", ":state_no"),#阈值
      (item_get_food_quality, ":reduce_value", ":state_no"),#每秒减少值
      (item_get_value, ":action_value", ":state_no"),#触发后的效用值

      (store_div, ":situation_check", ":timer_count", 10000),#阶段参数
      (store_mod, ":timer", ":timer_count", 10000),#计时参数

#      (store_agent_hit_points, ":agent_hp_percent", ":agent_no", 0),
      (store_agent_hit_points, ":agent_hp", ":agent_no", 1),

##############效应部分##############
      (try_begin),
         (eq, ":state_no", "itm_state_weak_toxin"),    #弱毒
         (try_begin),
            (lt, ":situation_check", 1),                                       #未毒发
            (ge, ":timer", ":timer_threshold"),                                              #reach threshold
            (store_add, ":timer_count", ":timer_threshold", 10000),           #毒发，用阈值代替time count以免超出限度
         (else_try),
            (ge, ":situation_check", 1),                                      #毒发阶段：每秒扣除1血量
            (val_sub, ":agent_hp", ":action_value"),
            (val_max, ":agent_hp", 1),
            (agent_set_hit_points, ":agent_no", ":agent_hp", 1),#不会扣血到0。
         (try_end),

      (else_try),
         (eq, ":state_no", "itm_state_venom_toxin"),     #猛毒
         (ge, ":timer", ":timer_threshold"),                          #reach threshold
         (val_sub, ":agent_hp", ":action_value"),                 #毒发阶段：直接扣除15血量
         (val_max, ":agent_hp", 1),
         (agent_set_hit_points, ":agent_no", ":agent_hp", 1),#不会扣血到0。
         (assign, ":timer_count", 0),                           #毒发后清空计时器

      (else_try),
         (eq, ":state_no", "itm_state_strong_toxin"),      #强毒
         (gt, ":timer", 0),
         (val_sub, ":agent_hp", ":action_value"),            #只要有毒素就会每秒造成1点血量的伤害
         (val_max, ":agent_hp", 1),
         (agent_set_hit_points, ":agent_no", ":agent_hp", 1),#不会扣血到0。

      (else_try),
         (eq, ":state_no", "itm_state_paralytic_toxin"),    #惊厥毒
         (ge, ":timer", ":timer_threshold"),                       #reach threshold
         (try_begin),
            (agent_is_human,  ":agent_no"),
            (agent_set_animation, ":agent_no", "anim_strike2_chest_back", 1),     #人类毒发：动作停滞一瞬
         (else_try),
            (agent_set_animation, ":agent_no", "anim_horse_rear"),                      #动物毒发：惊马动作
            (agent_play_sound, ":agent_no", "snd_neigh"),
            (try_begin),
               (agent_get_rider, ":rider_agent_no", ":agent_no"),
               (gt, ":rider_agent_no", 0),
               (agent_get_troop_id, ":rider_troop_no", ":rider_agent_no"),
               (store_skill_level, ":npc_skl", skl_riding, ":rider_troop_no"),
               (val_mul, ":npc_skl", 10),

               (agent_get_item_id, ":horse_item_no", ":agent_no"),
               (item_get_horse_maneuver, ":return_value", ":horse_item_no"),
#               (call_script, "script_item_property_modifier", 2715, ":original_modifier_no", ":return_value"),
               (val_add, ":return_value", ":npc_skl"),
               (lt, ":return_value", 100),                                   #10*riding+horse_maneuver<100  骑术×10加上马的顺从小于100，就会落马

               (agent_set_animation, ":rider_agent_no", "anim_strike2_chest_back", 1), 
               (agent_start_running_away, ":agent_no"),
               (agent_stop_running_away, ":agent_no"),
            (try_end),
         (try_end),

      (else_try),
         (eq, ":state_no", "itm_state_weaken_toxin"),     #虚弱毒
         (try_begin),
            (le, ":situation_check", 0),                                      #未毒发 
            (ge, ":timer", ":timer_threshold"),                                                      #reach threshold
            (store_add, ":timer_count", ":timer_threshold", 10000),           #毒发，用阈值代替time count以免超出限度

            (agent_get_damage_modifier, ":damage_caculate", ":agent_no"),
            (val_sub, ":damage_caculate", 20),
            (gt, ":damage_caculate", 0),
            (agent_set_damage_modifier, ":agent_no", ":damage_caculate"),
         (else_try),
            (ge, ":situation_check", 1),                                      #毒效结束
            (le, ":timer", ":reduce_value"),
            (agent_get_damage_modifier, ":damage_caculate", ":agent_no"),
            (val_add, ":damage_caculate", 20),
            (agent_set_damage_modifier, ":agent_no", ":damage_caculate"),
         (try_end),

      (else_try),
         (eq, ":state_no", "itm_state_bleeding"),     #流血
         (gt, ":timer", 0),
         (val_add, ":timer_count", ":add_value"),                    #每秒加2，直到20

         (try_begin),
            (agent_is_human, ":agent_no"),
            (try_begin),
               (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_blood_intoxication"),#血醉
               (gt, reg1, 0),     
               (val_add, ":timer_threshold", 40),#激活被动血醉时失血阶段的阈值提升40
            (try_end),
            (ge, ":timer", ":timer_threshold"),                                                #失血判定，若剩余血量大于流血值，扣除对应血量，否则直接死亡。

            (agent_get_bone_position, pos1, ":agent_no", hb_thorax, 1),
            (particle_system_burst, "psys_game_blood", pos1),
            (try_begin),
               (gt, ":agent_hp", ":timer"),
               (val_sub, ":agent_hp", ":timer"),
               (agent_set_hit_points, ":agent_no", ":agent_hp", 1),
               (agent_set_animation, ":agent_no", "anim_strike2_chest_back", 1),
               (try_begin),
                  (call_script, "script_restrain_state_full", ":agent_no", "itm_state_blood_burst", 3),#减少三层血潮汹涌
                  (ge, reg1, 3),
               (else_try),                                                                                           #失血判定会试图减少三层血潮汹涌，如果实际减少了三层，则不会进入失血状态。
                  (call_script, "script_activate_state_unconditional_type", ":agent_no", "itm_state_lose_blood", 1),
               (try_end),
               (assign, ":timer_count", 0), #结束
            (else_try),
               (agent_set_hit_points, ":agent_no", 0, 1),
               (agent_deliver_damage_to_agent, ":agent_no", ":agent_no", 1),#击杀agent
            (try_end),
            (eq, ":agent_no", "$mission_player_agent"),#玩家
            (display_message, "@出 血 ！"),
         (try_end), 

      (else_try),
         (eq, ":state_no", "itm_state_decay_changing"),     #腐死转化
         (try_begin),
            (is_between, ":timer", 1, 11),                                     #只要有一点感染就会不断扩大
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到10
         (else_try),
            (eq, ":timer", 11),                                                       #转化阶段开始
            (agent_get_horse, ":agent_horse_no", ":agent_no"),
            (agent_start_running_away, ":agent_horse_no"),                   #坠马
            (agent_set_animation, ":agent_no", "anim_decay_transforming"),
            (val_add, ":timer_count", ":add_value"), 
         (else_try),
            (is_between, ":timer", 12, 17),                                   #转化阶段
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到16。
         (else_try),
            (ge, ":timer", 17),                                                       #转化完成
            (store_random_in_range, ":random_head_no", "itm_jiangshitou_1", "itm_jiangshitou_3"),   #换成丧尸头
            (agent_equip_item, ":agent_no", ":random_head_no", ek_head),
            (store_random_in_range, ":random_sound_no", "snd_walker_roar_1", "snd_walker_roar_4"),   #咆哮
            (agent_play_sound, ":agent_no", ":random_sound_no"),
            (agent_set_animation, ":agent_no", "anim_decay_transformed"),
            (agent_set_speed_modifier, ":agent_no", 30),
            (assign, ":timer_count", 0), 
         (try_end),

      (else_try),
         (eq, ":state_no", "itm_state_cancer_changing"),     #活癌转化
         (try_begin),
            (is_between, ":timer", 1, 9),                                     #只要有一点感染就会不断扩大
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到8
         (else_try),
            (eq, ":timer", 9),                                                       #转化阶段开始
            (agent_get_horse, ":agent_horse_no", ":agent_no"),
            (agent_start_running_away, ":agent_horse_no"),                   #坠马
            (agent_set_animation, ":agent_no", "anim_cancer_transforming"),
            (val_add, ":timer_count", ":add_value"), 
         (else_try),
            (is_between, ":timer", 10, 15),                                   #转化阶段
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到14。
         (else_try),
            (is_between, ":timer", 15, 16),                                                       #转化完成
            (agent_set_animation, ":agent_no", "anim_cancer_transformed"),
            (agent_set_speed_modifier, ":agent_no", 30),
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到18换头。
         (else_try),
            (eq, ":timer", 16),
            (agent_equip_item, ":agent_no", "itm_jiangshitou_3", ek_head),                                       #换成丧尸头
            (store_random_in_range, ":random_sound_no", "snd_walker_roar_1", "snd_walker_roar_4"),   #咆哮
            (agent_play_sound, ":agent_no", ":random_sound_no"),
            (assign, ":timer_count", 0), 
         (try_end),

      (else_try),
         (eq, ":state_no", "itm_state_submerge_changing"),     #湮沦转化
         (try_begin),
            (is_between, ":timer", 1, 7),                                     #只要有一点感染就会不断扩大
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到6
         (else_try),
            (eq, ":timer", 7),                                                       #转化阶段开始
            (agent_get_horse, ":agent_horse_no", ":agent_no"),
            (agent_start_running_away, ":agent_horse_no"),                   #坠马
            (agent_set_animation, ":agent_no", "anim_submerge_transforming"),
            (agent_get_position, pos1, ":agent_no"),
            (set_spawn_position, pos1),
            (spawn_item, "itm_carrion", 0, 11),
            (val_add, ":timer_count", ":add_value"), 
         (else_try),
            (is_between, ":timer", 8, 16),                                   #转化阶段
            (val_add, ":timer_count", ":add_value"),                    #每秒加1，直到16。
         (else_try),
            (eq, ":timer", 16),                                                       #转化完成
            (agent_equip_item, ":agent_no", "itm_jiangshitou_4", ek_head),                                       #换成丧尸头
            (agent_play_sound, ":agent_no", "snd_walker_roar_4"),   #咆哮
            (agent_set_animation, ":agent_no", "anim_submerge_transformed"),
            (agent_set_speed_modifier, ":agent_no", 30),
            (assign, ":timer_count", 0), 
         (try_end),

      (else_try),
         (eq, ":state_no", "itm_state_blurs"),     #虚影化
         (try_begin),
            (is_between, ":timer", 1, ":timer_threshold"),           #幽灵始终保持该状态大于1，大于等于4时进入虚影化。
            (val_add, ":timer_count", ":add_value"),                   #每秒加1，直到3
         (else_try),
            (eq, ":timer", ":timer_threshold"),                              #虚影化。进场的时候给所有幽灵设置为4。
            (try_begin),
               (store_current_scene, ":scene_no"),
               (neq, ":scene_no", "scn_character_window_dungon"),#不在图鉴界面
               (agent_set_visibility, ":agent_no", 0),
               (agent_get_bone_position, pos5, ":agent_no", hb_thorax, 1),#胸部
               (particle_system_burst, "psys_ghost_smoke", pos5, 3),
            (try_end),
#            (agent_set_invulnerable_shield, ":agent_no", 1),
            (val_add, ":timer_count", ":add_value"),                   #加1避免一直设置
         (try_end),

      (else_try),
         (item_has_property, ":state_no", itp_enchant),#附魔类
         (try_begin),
            (eq, ":timer", 2),#等于2时结束附魔，通过刷新武器取消特效。附魔类效果的检测条件均为大于1。若是在附魔持续时间内更换了武器（切换武器或者捡起武器等），则直接设置为1，避免重复刷新武器。
            (agent_get_wielded_item, ":weapon_no", ":agent_no", 0),
            (agent_unequip_item, ":agent_no", ":weapon_no", 1),
            (agent_equip_item, ":agent_no", ":weapon_no", 1),
            (agent_set_wielded_item, ":agent_no", ":weapon_no"),#清除特效
         (else_try),
            (eq, ":timer", 1),
            (agent_set_slot, ":agent_no", slot_agent_enchant, -1),#清除附魔记录
         (try_end),
         (try_begin),
            (lt, ":situation_check", 1),#附魔时设置为阶段1，不会随时间减少。在物品触发器中附魔过一次后进入阶段2，开始随时间减少。
            (val_sub, ":timer_count", 1),
            (val_sub, ":timer", 1),
         (try_end),
      (try_end),

##############计时部分##############
      (val_sub, ":timer_count", ":reduce_value"),
      (try_begin),
         (val_sub, ":timer", ":reduce_value"),
         (le, ":timer", 0),
         (assign, ":timer_count", 0),#生效结束，全部归零
      (try_end),
      (assign, reg1, ":timer_count"),
    ]),


#计次型状态效果控制器
#注意储存slot在这个脚本结束之后，因此如果效应部分还要调用状态slot，应提前进行设置。
#输入agent no、状态ID和层数，返回新的层数（比如叠满九层就扣除巨额血量，同时血量清零）
  ("count_state_technique", [
      (store_script_param, ":agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":count_no", 3),

##############获取信息部分##############
      (item_get_max_ammo, ":count_threshold", ":state_no"),#阈值

##############效应部分##############
      (try_begin),
         (eq, ":state_no", "itm_state_blood_burst"),    #血潮汹涌
         (try_begin),
            (ge, ":count_no", 3),
            (call_script, "script_get_state_count", ":agent_no", "itm_state_lose_blood"),#失血与血潮汹涌互相抵消。
            (gt, reg1, 0),#正在失血
            (call_script, "script_activate_state_unconditional_type", ":agent_no", "itm_state_lose_blood", 0),#消耗三层解除失血
            (val_sub, ":count_no", 3),
         (try_end),

         (ge, ":count_no", ":count_threshold"),#达到九层即自爆
         (agent_is_alive, ":agent_no"),
         (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
         (val_sub, ":slot_no", 1),
         (val_add, ":slot_no", slot_agent_state_count_1),
         (agent_set_slot, ":agent_no", ":slot_no", 9),#死亡在设置返回设置slot之前，因此事先设置至九层。
         (agent_set_hit_points, ":agent_no", 0, 1),
         (agent_deliver_damage_to_agent, ":agent_no", ":agent_no", 1),#击杀agent
         (assign, ":count_no", 0),

      (else_try),
         (eq, ":state_no", "itm_state_breath_holding"),    #闭气
         (ge, ":count_no", 120),
         (call_script, "script_check_agent_passive_skill", ":agent_no", "itm_passive_scuba"),#水肺
         (le, reg1, 0),
         (store_agent_hit_points, ":agent_hp", ":agent_no", 1),
         (val_sub, ":agent_hp", 3),
         (val_max, ":agent_hp", 0),
         (agent_set_hit_points, ":agent_no", ":agent_hp", 1),
         (agent_deliver_damage_to_agent, ":agent_no", ":agent_no", 1),#能被憋死
      (try_end),

##############返回次数部分##############
      (assign, reg1, ":count_no"),
    ]),


#———————————————————————————————————状态增减控制——————————————————————————————

#激活状态：计时型和计次型（不包括阶段计数值）
#输入对象agent，状态序号，状态值（如果是计时型就是以秒为单位，如果是次数型就是以次为单位，无条件型用专门的脚本）
  ("activate_state", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":value", 3),

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),#获取slot
      (try_begin),
         (item_has_property, ":state_no", itp_count_type),         #计次类型
         (call_script, "script_count_state_technique", ":object_agent_no", ":state_no", ":value"),#计次型效应
         (assign, ":value", reg1),
      (else_try),
         (item_has_property, ":state_no", itp_timing_type),         #计时类型，只有计时型需要统计
         (agent_get_slot, ":value_2", ":object_agent_no", ":slot_no"),
         (le, ":value_2", 0),
         (gt, ":value", 0),
         (agent_get_slot, ":total_state", ":object_agent_no", slot_agent_state_caculate),
         (val_max, ":total_state", 0),
         (val_add, ":total_state", 1),
         (agent_set_slot, ":object_agent_no", slot_agent_state_caculate, ":total_state"),#增加一统计
      (try_end),
      (agent_set_slot, ":object_agent_no", ":slot_no", ":value"),
    ]),


#推进状态
#最常用
#输入对象agent，状态序号，状态值（如果是计时型就是以秒为单位，如果是次数型就是以次为单位）
  ("proceed_state", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":value", 3),

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),
      (agent_get_slot, ":count_value", ":object_agent_no", ":slot_no"),
      (try_begin),
         (item_has_property, ":state_no", itp_timing_type),#只有计时型需要统计
         (le, ":count_value", 0),
         (assign, ":count_value", 0),#归零
         (agent_get_slot, ":total_state", ":object_agent_no", slot_agent_state_caculate),
         (val_add, ":total_state", 1),
         (agent_set_slot, ":object_agent_no", slot_agent_state_caculate, ":total_state"),#增加一个状态
      (try_end),
      (val_add, ":count_value", ":value"),
      (try_begin),
         (item_has_property, ":state_no", itp_timing_type),#只有计时型需要统计
         (le, ":count_value", 0),
         (assign, ":count_value", 0),#归零
         (agent_get_slot, ":total_state", ":object_agent_no", slot_agent_state_caculate),
         (val_sub, ":total_state", 1),
         (agent_set_slot, ":object_agent_no", slot_agent_state_caculate, ":total_state"),#减少一个状态
      (else_try),
         (item_has_property, ":state_no", itp_count_type),         #计次型
         (call_script, "script_count_state_technique", ":object_agent_no", ":state_no", ":count_value"),#计次型效应
         (assign, ":count_value", reg1),
      (try_end),
      (agent_set_slot, ":object_agent_no", ":slot_no", ":count_value"),
    ]),

#减少状态（不会因此减到0，但若是0则不变）
#输入对象agent，状态序号，状态值（如果是计时型就是以秒为单位，如果是次数型就是以次为单位）
  ("restrain_state", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":value", 3),

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),
      (agent_get_slot, ":count_value", ":object_agent_no", ":slot_no"),
      (try_begin),
         (gt, ":count_value", 0),
         (val_sub, ":count_value", ":value"),
         (val_max, ":count_value", 1),#不会减到0
      (try_end),
      (try_begin),
         (item_has_property, ":state_no", itp_count_type),         #计次型
         (call_script, "script_count_state_technique", ":object_agent_no", ":state_no", ":count_value"),#计次型效应
         (assign, ":count_value", reg1),
      (try_end),
      (agent_set_slot, ":object_agent_no", ":slot_no", ":count_value"),
    ]),

#减少状态（会减到0）
#输入对象agent，状态序号，状态值（如果是计时型就是以秒为单位，如果是次数型就是以次为单位）
#输出reg1为实际减少的值
  ("restrain_state_full", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":value", 3),

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),
      (agent_get_slot, ":count_value", ":object_agent_no", ":slot_no"),
      (try_begin),
         (gt, ":count_value", 0),
         (store_sub, ":count_value_2", ":count_value", ":value"),
         (try_begin),
            (le, ":count_value_2", 0),
            (assign, ":count_value_2", 0),#归零
            (assign, ":value", ":count_value"),#如果减到了0，那实际减少的值就等于状态值
         (try_end),

         (try_begin),
            (item_has_property, ":state_no", itp_timing_type),#只有计时型需要统计
            (gt, ":count_value", 0),
            (le, ":count_value_2", 0),#原本大于0，现在归零
            (agent_get_slot, ":total_state", ":object_agent_no", slot_agent_state_caculate),
            (val_sub, ":total_state", 1),
            (agent_set_slot, ":object_agent_no", slot_agent_state_caculate, ":total_state"),#减少一个状态
         (else_try),
            (item_has_property, ":state_no", itp_count_type),         #计次型
            (call_script, "script_count_state_technique", ":object_agent_no", ":state_no", ":count_value_2"),#计次型效应
            (assign, ":count_value_2", reg1),
         (try_end),
         (assign, ":count_value", ":count_value_2"),
      (else_try),
         (assign, ":value", 0),#":count_value"小于等于0，没这个状态，没有减少任何值
      (try_end),
      (agent_set_slot, ":object_agent_no", ":slot_no", ":count_value"),
      (assign, reg1, ":value"),#输出实际减少的值
    ]),


#获取状态（计时）
#不包括阶段值
#输入对象agent，状态序号
  ("get_state_timer", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),

      (agent_get_slot, ":count_value", ":object_agent_no", ":slot_no"),
      (try_begin),
         (ge, ":count_value", 0),
         (store_mod, reg1, ":count_value", 10000),
      (else_try),
         (assign, reg1, 0),
      (try_end),
    ]),

#获取状态（计次）
#输入对象agent，状态序号
  ("get_state_count", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),

      (agent_get_slot, ":count_value", ":object_agent_no", ":slot_no"),
      (val_max, ":count_value", 0),
      (assign, reg1, ":count_value"),
    ]),

#激活状态（无条件型）
#输入对象agent，状态序号，启动或关闭（1启动，0关闭）
  ("activate_state_unconditional_type", [
      (store_script_param, ":object_agent_no", 1),
      (store_script_param, ":state_no", 2),
      (store_script_param, ":value", 3),#0或1

      (store_sub, ":slot_no", ":state_no", "itm_state_begin"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_agent_state_count_1),
      (agent_set_slot, ":object_agent_no", ":slot_no", ":value"),

      (try_begin),
         (eq, ":state_no", "itm_state_lose_blood"),#失血
         (try_begin),
            (eq, ":value", 1),#激活
            (agent_get_damage_modifier, ":damage_caculate", ":object_agent_no"),
            (val_sub, ":damage_caculate", 15),
            (gt, ":damage_caculate", 0),
            (agent_set_damage_modifier, ":object_agent_no", ":damage_caculate"),#减15%伤害
            (agent_get_damage_modifier, ":speed_caculate", ":object_agent_no"),
            (val_sub, ":speed_caculate", 40),
            (gt, ":speed_caculate", 0),
            (agent_set_speed_modifier, ":object_agent_no", ":speed_caculate"),#减40%速度
         (else_try),
            (eq, ":value", 0),#解除
            (agent_get_damage_modifier, ":damage_caculate", ":object_agent_no"),
            (val_add, ":damage_caculate", 15),
            (agent_set_damage_modifier, ":object_agent_no", ":damage_caculate"),#还原伤害
            (agent_get_damage_modifier, ":speed_caculate", ":object_agent_no"),
            (val_add, ":speed_caculate", 40),
            (agent_set_speed_modifier, ":object_agent_no", ":speed_caculate"),#还原速度
         (try_end),
      (try_end),
    ]),



###########################################################AI相关###################################################

#分析兵种是否骑马
#由于agent是先生成人再生成马，所以想要在ti on agent spawn里获取agent是否骑马，只能通过troop
#输入troop，返回1：步行，2：骑兵（保证马且装备马），3：骑行步兵（不标配马）
  ("troop_mounted_check", [
      (store_script_param_1, ":troop_no"),
      (assign, ":mounted_type_no", 1),
      (try_begin),
         (troop_is_hero, ":troop_no"),#英雄单位直接看ek_horse装备槽
         (troop_get_inventory_slot, ":horse_no", ":troop_no", ek_horse),
         (gt, ":horse_no", 0),
         (assign, ":mounted_type_no", 2),
      (else_try),
         (neg|troop_is_hero, ":troop_no"),
         (troop_get_inventory_capacity, ":item_capacity", ":troop_no"),
         (try_for_range, ":slot_no", 0, ":item_capacity"),
            (troop_get_inventory_slot, ":horse_no", ":troop_no", ":slot_no"),
            (gt, ":horse_no", 0),
            (item_get_type, ":type_no", ":horse_no"),
            (eq, ":type_no", itp_type_horse),
            (assign, ":item_capacity", 0),#break
         (try_end),
         (eq, ":item_capacity", 0),#有马，判定成功
         (try_begin),
            (troop_is_mounted, ":troop_no"),
            (troop_is_guarantee_horse, ":troop_no"),#标配马，正规骑兵
            (assign, ":mounted_type_no", 2),
         (else_try),
            (assign, ":mounted_type_no", 3),#概率骑马，归类为骑马步兵
         (try_end),
      (try_end),
      (assign, reg1, ":mounted_type_no"),
#      (assign, reg2, ":horse_no"),
    ]),

#分析当前装备模式
#剑盾1、枪兵2、双手3、步射4、混战骑5、枪骑6、游骑7，标签定义在header_mission_template里。
#输入对象agent，返回装备模式序号，返回后储存进slot_ai_battle_mode
  ("agent_ai_battle_mode", [
      (store_script_param_1, ":agent_no"),

      (assign, ":battle_mode_no", 0),
      (agent_get_wielded_item, ":weapon_no_1", ":agent_no", 0),#右手
      (agent_get_wielded_item, ":weapon_no_2", ":agent_no", 1),#左手
      (agent_get_horse, ":horse_no", ":agent_no"),
      (try_begin),
         (ge, ":horse_no", 0),#骑马
         (gt, ":weapon_no_1", 0),
         (item_get_type, ":type_no", ":weapon_no_1"),
         (this_or_next|eq, ":type_no", itp_type_bow),#远程
         (this_or_next|eq, ":type_no", itp_type_crossbow),
         (this_or_next|eq, ":type_no", itp_type_thrown),
         (this_or_next|eq, ":type_no", itp_type_pistol),
         (eq, ":type_no", itp_type_musket),
         (assign, ":battle_mode_no", ai_ranger),        #游骑兵
      (else_try),
         (ge, ":horse_no", 0),#骑马
         (gt, ":weapon_no_1", 0),
         (item_get_type, ":type_no", ":weapon_no_1"),
         (this_or_next|eq, ":type_no", itp_type_polearm),#长杆
         (item_has_property, ":weapon_no_1", itp_couchable),#骑枪冲锋
         (assign, ":battle_mode_no", ai_lancer),        #枪骑兵
      (else_try),
         (ge, ":horse_no", 0),#骑马
         (gt, ":weapon_no_1", 0),
         (assign, ":battle_mode_no", ai_cavalry),        #混战骑兵
     (else_try),
         (lt, ":horse_no", 0),#步行
         (gt, ":weapon_no_1", 0),
         (item_get_type, ":type_no", ":weapon_no_1"),
         (this_or_next|eq, ":type_no", itp_type_bow),#远程
         (this_or_next|eq, ":type_no", itp_type_crossbow),
         (this_or_next|eq, ":type_no", itp_type_thrown),
         (this_or_next|eq, ":type_no", itp_type_pistol),
         (eq, ":type_no", itp_type_musket),
         (assign, ":battle_mode_no", ai_archer),        #步射手
     (else_try),
         (lt, ":horse_no", 0),#步行
         (gt, ":weapon_no_1", 0),
         (item_get_type, ":type_no", ":weapon_no_1"),
         (neg|eq, ":type_no", itp_type_bow),#近战
         (neg|eq, ":type_no", itp_type_crossbow),
         (neg|eq, ":type_no", itp_type_thrown),
         (neg|eq, ":type_no", itp_type_pistol),
         (neg|eq, ":type_no", itp_type_musket),
         (le, ":weapon_no_2", 0),#不带盾
         (assign, ":battle_mode_no", ai_berserker),        #双手豪杰
     (else_try),
         (lt, ":horse_no", 0),#步行
         (gt, ":weapon_no_1", 0),
         (item_get_type, ":type_no", ":weapon_no_1"),
         (eq, ":type_no", itp_type_polearm),#长杆
         (gt, ":weapon_no_2", 0),#带盾
         (assign, ":battle_mode_no", ai_pikeman),        #长矛兵
     (else_try),
         (lt, ":horse_no", 0),#步行
         (gt, ":weapon_no_2", 0),#带盾
         (gt, ":weapon_no_1", 0),
         (item_get_type, ":type_no", ":weapon_no_1"),
         (this_or_next|eq, ":type_no", itp_type_one_handed_wpn),#单手武器
         (eq, ":type_no", itp_type_two_handed_wpn),#单双手武器
         (assign, ":battle_mode_no", ai_saber),        #剑盾兵
     (try_end),
     (assign, reg1, ":battle_mode_no"),
    ]),

#录入权重，将其储存进trp_temp_array_ai的slot里，便于统计与调用
#输入数值，加权为正，减权为负。可以不填。
#param输入录入数据的数量
  ("agent_ai_weight_input", [
      (store_script_param, ":total_num", 1),#录入数据的数量
      (try_for_range, ":slot_no", 0, ":total_num"),
         (store_add, ":param_no", ":slot_no", 2),
         (store_script_param, ":cur_weight", ":param_no"),
         (neq, ":cur_weight", 0),
         (troop_get_slot, ":weight_count", "trp_temp_array_ai", ":slot_no"),
         (val_add, ":weight_count", ":cur_weight"),
         (troop_set_slot, "trp_temp_array_ai", ":slot_no", ":weight_count"),
      (try_end),
    ]),

#获取权重最高的一项，返回序号
#权重最高的一项必须大于500才能执行，否则认定为所有项目都不应执行，不下指令，由原有AI自行普通攻击
  ("agent_ai_weight_output", [
      (assign, ":weight_range", 500),
      (assign, ":chosen_action", 0),
      (try_for_range, ":slot_no", 0, 10),
         (troop_get_slot, ":weight_count", "trp_temp_array_ai", ":slot_no"),
         (gt, ":weight_count", ":weight_range"),
         (assign, ":weight_range", ":weight_count"),
         (assign, ":chosen_action", ":slot_no"),
         (val_add, ":chosen_action", 1),
      (try_end),
      (assign, reg1, ":chosen_action"),
    ]),

#清空权重
  ("agent_ai_weight_clear", [
      (store_script_param, ":total_num", 1),#录入数据的数量
      (try_for_range, ":slot_no", 0, ":total_num"),
         (troop_set_slot, "trp_temp_array_ai", ":slot_no", 0),
      (try_end),
    ]),



###########################################################新阵营系统相关###################################################

##Be awared that since factions can only reach 128, new factions will be made by items. Normal factions will only used as IDENTITIES.
#set a substitude for player in film mode. Output two weapon no in game variables.
  ("set_faction_affiliation", [
      (store_script_param, ":joiner_no", 1),
      (store_script_param, ":joiner_type", 2),#0 is faction(item), 1 is troop.
      (store_script_param, ":superior_faction_no", 3),
      (store_script_param, ":joiner_status", 4),#0 is normal member, 1 is pillar member, 2 is leader.

      (try_begin),
         (eq, ":joiner_type", 0),#faction
         (item_set_slot, ":joiner_no", slot_faction_affiliation, ":superior_faction_no"),
         (item_set_slot, ":joiner_no", slot_faction_member_position, ":joiner_status"),
      (else_try),
         (eq, ":joiner_type", 1),#troop
         (troop_set_slot, ":joiner_no", slot_troop_affiliation, ":superior_faction_no"),
         (troop_set_slot, ":joiner_no", slot_troop_member_position, ":joiner_status"),
      (try_end),

#      (try_begin),
#         (eq, ":joiner_status", 2),
#         (faction_get_slot, ":leader_no", ":superior_faction_no", slot_faction_leader)
#         (try_begin),
#            (gt, ":leader_no", 0),#already have leader
#            (display_message, "@Already_have_leader", 0xFF0000),
#         (else_try),
#            (faction_set_slot, ":superior_faction_no", slot_faction_leader, ":joiner_no"),
#         (try_end),
#      (else_try),
#         (eq, ":joiner_status", 1),
#         (assign, ":end_cond", slot_faction_bottom_begin),
#         (try_for_range, ":slot_no", slot_faction_pillar_begin, ":end_cond"),
#            (faction_get_slot, ":pillar_no", ":superior_faction_no", ":slot_no")
#            (le, ":pillar_no", 0),
#            (faction_set_slot, ":superior_faction_no", ":slot_no", ":joiner_no"),
#            (assign, ":end_cond", slot_faction_pillar_begin),#break
#         (try_end),
#         (eq, ":end_cond", slot_faction_bottom_begin),
#         (display_message, "@Already_have_enough_pillar", 0xFF0000),
#      (else_try),
#         (eq, ":joiner_status", 0),
#         (assign, ":end_cond", 100),
#         (try_for_range, ":slot_no", slot_faction_bottom_begin, ":end_cond"),
#            (faction_get_slot, ":bottom_no", ":superior_faction_no", ":slot_no")
#            (le, ":bottom_no", 0),
#            (faction_set_slot, ":superior_faction_no", ":slot_no", ":joiner_no"),
#            (assign, ":end_cond", slot_faction_bottom_begin),#break
#         (try_end),
#      (try_end),
    ]),

#移除隶属关系
  ("remove_faction_affiliation", [
      (store_script_param, ":joiner_no", 1),
      (store_script_param, ":joiner_type", 2),#0 is faction(item), 1 is troop.

      (try_begin),
         (eq, ":joiner_type", 0),#faction
         (item_set_slot, ":joiner_no", slot_faction_affiliation, -1),
         (item_set_slot, ":joiner_no", slot_faction_member_position, -1),
      (else_try),
         (eq, ":joiner_type", 1),#troop
         (troop_set_slot, ":joiner_no", slot_troop_affiliation, -1),
         (troop_set_slot, ":joiner_no", slot_troop_member_position, -1),
      (try_end),
    ]),

#获取隶属的派系
  ("get_faction_affiliation", [#output reg1
      (store_script_param, ":joiner_no", 1),
      (store_script_param, ":joiner_type", 2),#0 is faction(item), 1 is troop.

      (try_begin),
         (eq, ":joiner_type", 0),#faction
         (item_get_slot, reg1, ":joiner_no", slot_faction_affiliation),
      (else_try),
         (eq, ":joiner_type", 1),#troop
         (troop_get_slot, reg1, ":joiner_no", slot_troop_affiliation),
      (try_end),
    ]),

#获取地位
  ("get_faction_position", [#output reg1
      (store_script_param, ":joiner_no", 1),
      (store_script_param, ":joiner_type", 2),#0 is faction(item), 1 is troop.

      (try_begin),
         (eq, ":joiner_type", 0),#faction
         (item_get_slot, reg1, ":joiner_no", slot_faction_member_position),
      (else_try),
         (eq, ":joiner_type", 1),#troop
         (troop_get_slot, reg1, ":joiner_no", slot_troop_member_position),
      (try_end),
    ]),

#改变该阵营和玩家的关系
  ("change_faction_relarion_with_player", [
      (store_script_param, ":faction_no", 1),
      (store_script_param, ":relation_no", 2),

      (item_get_slot, ":relation_count", ":faction_no", slot_faction_relation_with_player),
      (str_store_item_name, s1, ":faction_no", 0),
      (try_begin),
         (gt, ":relation_no", 0),
         (try_begin),
            (ge, ":relation_count", 100),
            (display_message, "@{s1}对 你 忠 心 耿 耿 。 ", 0xccff33),
         (else_try),
            (val_add, ":relation_count", ":relation_no"),
            (val_min, ":relation_count", 100),
            (assign, reg1, ":relation_count"),
            (display_message, "@{s1}与 你 的 关 系 提 升 至 {reg1} 。 ", 0x99ff99),
         (try_end),
      (else_try),
         (lt, ":relation_no", 0),
         (try_begin),
            (le, ":relation_count", -100),
            (display_message, "@{s1}与 你 不 共 戴 天 。 ", 0x990000),
         (else_try),
            (val_sub, ":relation_count", ":relation_no"),
            (val_max, ":relation_count", -100),
            (assign, reg1, ":relation_count"),
            (display_message, "@{s1}与 你 的 关 系 恶 化 至 {reg1} 。 ", 0x993300),
         (try_end),
      (try_end),
      (item_set_slot, ":faction_no", slot_faction_relation_with_player, ":relation_count"),
    ]),


#设置阵营部队模板
#输入阵营ID，部队模板ID，征兵概率（用于替换国家阵营征兵模板，只有一个就填0，表示100%），填入哪个位置（1、2、3）
  ("set_faction_template", [
      (store_script_param, ":faction_no", 1),
      (store_script_param, ":template_no", 2),#不超过999
      (store_script_param, ":rate", 3),
      (store_script_param, ":position", 4),

      (val_mul, ":rate", 1000),
      (val_add, ":template_no", ":rate"),
      (item_get_slot, ":value_no", ":faction_no", slot_faction_military_provide),
      (try_begin),
         (eq, ":position", 1),
         (val_div, ":value_no", 100000),
         (val_mul, ":value_no", 100000),
         (val_add, ":value_no", ":template_no"),
         (item_set_slot, ":faction_no", slot_faction_military_provide, ":value_no"),
      (else_try),
         (eq, ":position", 2),
         (store_mod, ":value_no_1", ":value_no", 100000),
         (val_div, ":value_no", 10000000000),
         (val_mul, ":value_no", 10000000000),
         (val_add, ":value_no", ":value_no_1"),
         (val_mul, ":template_no", 100000),
         (val_add, ":value_no", ":template_no"),
         (item_set_slot, ":faction_no", slot_faction_military_provide, ":value_no"),
      (else_try),
         (eq, ":position", 3),
         (val_mod, ":value_no", 10000000000),
         (val_mul, ":template_no", 10000000000),
         (val_add, ":value_no", ":template_no"),
         (item_set_slot, ":faction_no", slot_faction_military_provide, ":value_no"),
      (try_end),
    ]),

#获取阵营部队模板
#输入阵营ID和存储位置，返回reg1为部队模板，reg2为概率（百分数）
  ("cf_get_faction_template", [
      (store_script_param, ":faction_no", 1),
      (store_script_param, ":position", 2),

      (item_get_slot, ":value_no", ":faction_no", slot_faction_military_provide),
      (try_begin),
         (eq, ":position", 1),
         (val_mod, ":value_no", 100000),
      (else_try),
         (eq, ":position", 2),
         (val_mod, ":value_no", 10000000000),
         (val_div, ":value_no", 100000),
      (else_try),
         (eq, ":position", 3),
         (val_div, ":value_no", 10000000000),
      (try_end),
      (gt, ":value_no", 0),
      (store_mod, reg1, ":value_no", 1000), #模板
      (store_div, reg2, ":value_no", 1000), #概率
      (try_begin),
         (gt, reg1, 0), #有模板但没概率，算100%
         (le, reg2, 0),
         (assign, reg2, 100),
      (try_end),
    ]),


  ("draw_faction_image", [#output reg1 (overlay id of button)
      (store_script_param, ":faction_no", 1),
      (store_script_param, ":type_no", 2),#0 is faction(item), 1 is troop.
      (store_script_param, ":cur_x", 3),
      (store_script_param, ":cur_y", 4),

      (try_begin),
         (neq, ":type_no", 1),
         (create_mesh_overlay_with_item_id, reg1, ":faction_no"),#阵营类型
         (position_set_x, pos1, ":cur_x"),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),

         (val_sub, ":cur_y", 65),
         (str_store_item_name, s1, ":faction_no"),
         (create_text_overlay, reg1, s1, tf_center_justify),
         (position_set_x, pos1, ":cur_x"),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 800),
         (position_set_y, pos1, 800),
         (overlay_set_size, reg1, pos1),
         (overlay_set_color, reg1, 0xFFFFFF),

         (val_sub, ":cur_x", 40),
         (val_add, ":cur_y", 25),
         (create_image_button_overlay, reg1, "mesh_white_plane", "mesh_white_plane"),
         (position_set_x, pos1, ":cur_x"),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 4000),
         (position_set_y, pos1, 4000),
         (overlay_set_size, reg1, pos1),
         (overlay_set_color, reg1, 0x000000),

      (else_try),
         (val_sub, ":cur_y", 65),
         (str_store_troop_name, s1, ":faction_no"),#人物类型
         (create_text_overlay, reg1, s1, tf_center_justify),
         (position_set_x, pos1, ":cur_x"),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 800),
         (position_set_y, pos1, 800),
         (overlay_set_size, reg1, pos1),
         (overlay_set_color, reg1, 0xFFFFFF),

         (val_sub, ":cur_x", 60),
         (val_add, ":cur_y", 20),
         (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_troop_note_mesh", ":faction_no"),
         (set_fixed_point_multiplier, 1000),
         (position_set_x, pos1, ":cur_x"),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 300),
         (position_set_y, pos1, 300),
         (overlay_set_size, reg1, pos1),
      (try_end),
    ]),


#show in the right of faction  window
  ("faction_brief_show", [
      (store_script_param, ":faction_no", 1),#item no
      (create_mesh_overlay_with_item_id, reg1, ":faction_no"),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 550),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 1300),
      (position_set_y, pos1, 1300),
      (overlay_set_size, reg1, pos1),

      (str_store_item_name, s1, ":faction_no"),
      (create_text_overlay, reg1, s1, tf_center_justify),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 450),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 1000),
      (position_set_y, pos1, 1000),
      (overlay_set_size, reg1, pos1),

      (item_get_difficulty, ":grade_no", ":faction_no"),#faction grade
      (val_sub, ":grade_no", 1),
      (val_add, ":grade_no", "str_faction_grade_1"),
      (str_store_string, s1, ":grade_no"),
      (create_text_overlay, reg1, s1, tf_center_justify),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 410),
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

      (create_game_button_overlay, "$g_presentation_obj_3", "@查 看 该 势 力 "),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 350),
      (overlay_set_position, "$g_presentation_obj_3", pos1),
    ]),

#领主图鉴
  ("lord_brief_show", [
      (store_script_param, ":troop_no", 1),
      (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
      (create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
      (set_fixed_point_multiplier, 1000),
      (position_set_x, pos1, 720),
      (position_set_y, pos1, 420),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, reg1, pos1),

      (str_store_troop_name, s1, ":troop_no"),
      (create_text_overlay, reg1, s1, tf_center_justify),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 390),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 1000),
      (position_set_y, pos1, 1000),
      (overlay_set_size, reg1, pos1),

      (create_game_button_overlay, "$g_presentation_obj_3", "@Check_this_lord"),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 350),
      (overlay_set_position, "$g_presentation_obj_3", pos1),
      (overlay_set_display, "$g_presentation_obj_3", 0),
#领地
      (create_text_overlay, reg1, "@此 人 控 制 的 地 区 包 括 ： "),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 370),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),

      (create_text_overlay, reg1, "@ ", tf_scrollable),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 340),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
      (position_set_x, pos1, 250),
      (position_set_y, pos1, 30),
      (overlay_set_area_size, reg1, pos1),
      (set_container_overlay, reg1),
      (assign, ":cur_y", 5),
      (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_town_lord, ":troop_no"),
         (str_store_party_name, s1, ":party_no"),
         (create_text_overlay, reg1, s1),
         (position_set_x, pos1, 750),
         (position_set_y, pos1, 750),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 5),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),
         (val_add, ":cur_y", 15),
      (try_end),
      (set_container_overlay, -1),
#私兵
      (create_text_overlay, reg1, "@此 人 的 亲 卫 有 ： "),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 320),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),

      (create_text_overlay, reg1, "@ ", tf_scrollable),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 290),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
      (position_set_x, pos1, 250),
      (position_set_y, pos1, 30),
      (overlay_set_area_size, reg1, pos1),
      (set_container_overlay, reg1),
      (assign, ":cur_y", 5),
      (try_for_range, ":slot_no", 0, 2),
         (val_add, ":slot_no", slot_bodygaurd_troop_1),
         (troop_get_slot, ":bodyguard_troop_no", ":troop_no", ":slot_no"),
         (gt, ":bodyguard_troop_no", 0),
         (store_div, reg2, ":bodyguard_troop_no", 10000000),#上限
         (val_mod, ":bodyguard_troop_no", 10000000),
         (store_div, reg1, ":bodyguard_troop_no", 10000),#增员数额
         (val_mod, ":bodyguard_troop_no", 10000),
         (str_store_troop_name, s1, ":bodyguard_troop_no"),
         (create_text_overlay, reg1, "@{s1}：增 员 {reg1}， 上 限 {reg2}"),
         (position_set_x, pos1, 750),
         (position_set_y, pos1, 750),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 5),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, reg1, pos1),
         (val_add, ":cur_y", 15),
      (try_end),
      (set_container_overlay, -1),
#声望争议
      (troop_get_slot, reg10, ":troop_no", slot_troop_renown),
      (troop_get_slot, reg11, ":troop_no", slot_troop_controversy),
      (create_text_overlay, reg1, "@声 望 {reg10}/争 议 {reg11}"),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 270),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
#财富
      (troop_get_slot, reg10, ":troop_no", slot_troop_wealth),
      (create_text_overlay, reg1, "@资 产 ： {reg10}铁 币 "),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 250),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
#部队规模
      (call_script, "script_leader_get_ideal_size", ":troop_no"), 
      (assign, ":ideal_size", reg1),
      (try_begin),
         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),#有带领部队
         (ge, ":party_no", 1),
         (party_is_active, ":party_no"),
         (party_get_num_companions, reg10, ":party_no"),
         (assign, ":total_size", reg10),
         (val_mul, ":total_size", 100),
         (store_div, reg11, ":total_size", ":ideal_size"),
         (str_store_string, s10, "@当 前 正 领 导 {reg10}人 的 部 队 ， 为 理 想 人 数 的 {reg11}% 。 "),
      (else_try),
         (str_store_string, s10, "@当 前 未 带 领 部 队 "),
      (try_end),
      (create_text_overlay, reg2, "@理 想 部 队 规 模 为 {reg1}人 ， {s10}", tf_scrollable),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 218),
      (overlay_set_position, reg2, pos1),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, reg2, pos1),
      (position_set_x, pos1, 250),
      (position_set_y, pos1, 30),
      (overlay_set_area_size, reg2, pos1),
#征兵制
      (call_script, "script_get_troop_conscription_mode", ":troop_no"), 
      (assign, ":conscription_mode", reg1), #征兵模式
      (assign, reg10, reg2), #修正
      (assign, ":template_no", reg3), #模板
      (try_begin),
         (gt, ":template_no", 0),
         (val_sub, ":template_no", party_template_uesd_begin),
         (val_add, ":template_no", party_template_name_begin),
         (str_store_string, s12, ":template_no"),
      (else_try),
         (str_store_string, s12, "@无 "),
      (try_end),
      (try_begin),
         (eq, ":conscription_mode", rsm_professional),
         (str_store_string, s10, "@职 业 士 兵 制 "),
         (str_store_string, s11, "@对 理 想 部 队 规 模 无 影 响 。 "),
      (else_try),
         (eq, ":conscription_mode", rsm_conscriptive),
         (str_store_string, s10, "@征 召 兵 役 制 "),
         (str_store_string, s11, "@将 理 想 部 队 规 模 修 正 至 {reg10}% ， 动 员 时 采 用 {s12}。 "),
      (else_try),
         (eq, ":conscription_mode", rsm_mercenary),
         (str_store_string, s10, "@雇 佣 士 兵 制 "),
         (str_store_string, s11, "@将 理 想 部 队 规 模 修 正 至 {reg10}% ， 进 入 战 争 状 态 将 以 雇 佣 兵 扩 充 军 队 。 "),
      (else_try),
         (eq, ":conscription_mode", rsm_tribe),
         (str_store_string, s10, "@部 落 兵 模 式 "), 
         (str_store_string, s11, "@将 理 想 部 队 规 模 修 正 至 {reg10}% ， 绝 大 部 分 部 队 为 {s12}。 "),
      (else_try),
         (eq, ":conscription_mode", rsm_elite),
         (str_store_string, s10, "@精 锐 模 式 "), 
         (str_store_string, s11, "@将 理 想 部 队 规 模 修 正 至 {reg10}% ， 以 {s12}为 核 心 。 "),
      (try_end),
      (create_text_overlay, reg2, "@采 用 {s10}， {s11}", tf_scrollable),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 186),
      (overlay_set_position, reg2, pos1),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, reg2, pos1),
      (position_set_x, pos1, 250),
      (position_set_y, pos1, 30),
      (overlay_set_area_size, reg2, pos1),
    ]),


#兵种介绍
  ("troop_brief_show", [
      (store_script_param, ":troop_no", 1),
      (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
      (create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
      (set_fixed_point_multiplier, 1000),
      (position_set_x, pos1, 650),
      (position_set_y, pos1, 420),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, reg1, pos1),

      (str_store_troop_name, s1, ":troop_no"),
      (create_text_overlay, reg1, s1, tf_center_justify),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 420),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 1000),
      (position_set_y, pos1, 1000),
      (overlay_set_size, reg1, pos1),

      (store_character_level, reg1, ":troop_no"),
      (create_text_overlay, reg1, "@等 级 ： {reg1} "),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 615),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),

#attributes
      (try_for_range, ":count", 0, 4),
         (store_add, ":string_no", ":count", "str_strength"),
         (str_store_string, s1, ":string_no"),
         (store_mul, ":high", ":count", -15),
         (val_add, ":high", 600),

         (create_text_overlay, reg1, s1),
         (position_set_x, pos1, 800),
         (position_set_y, pos1, ":high"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, reg1, pos1),

         (store_add, ":attribute_no", ":count", ca_strength),
         (store_attribute_level, ":attribute_level", ":troop_no", ":attribute_no"),
         (assign, reg2, ":attribute_level"),
         (create_text_overlay, reg1, "@_{reg2}_"),
         (position_set_x, pos1, 890),
         (position_set_y, pos1, ":high"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, reg1, pos1),
      (try_end),

#weapon talent
      (try_for_range, ":count", 0, 7),
         (store_add, ":string_no", ":count", "str_wpt_one_handed"),
         (str_store_string, s1, ":string_no"),
         (store_mul, ":high", ":count", -15),
         (val_add, ":high", 535),

         (create_button_overlay, reg1, s1),
         (position_set_x, pos1, 800),
         (position_set_y, pos1, ":high"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, reg1, pos1),

         (store_add, ":weapon_no", wpt_one_handed_weapon, ":count"),
         (store_proficiency_level, ":weapon_level", ":troop_no", ":weapon_no"),
         (assign, reg2, ":weapon_level"),
         (create_button_overlay, reg1, "@_{reg2}_"),
         (position_set_x, pos1, 890),
         (position_set_y, pos1, ":high"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, reg1, pos1),
      (try_end),

#技能
      (create_text_overlay, reg1, "@ ", tf_scrollable),
      (position_set_x, pos1, 710),
      (position_set_y, pos1, 330),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 230),
      (position_set_y, pos1, 85),
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
      (val_mul, ":height_no", 15),#高度

      (assign, ":count_3", -1),
      (try_for_range, ":count", 0, 42),
         (store_sub, ":skill_no", skl_reserved_18, ":count"),
         (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
         (gt, ":skill_level", 0),
         (val_add, ":count_3", 1),
         (store_add, ":string_no", ":count", "str_reserved_18"),
         (str_store_string, s1, ":string_no"),

         (store_div, ":count_1", ":count_3", 3),
         (store_mod, ":count_2", ":count_3", 3),
         (val_mul, ":count_1", -15),
         (store_add, ":cur_height", ":height_no", ":count_1"),

         (create_button_overlay, reg1, s1),
         (try_begin),
            (eq, ":count_2", 0),
            (position_set_x, pos1, 18),
         (else_try),
            (eq, ":count_2", 1),
            (position_set_x, pos1, 88),
         (else_try),
            (position_set_x, pos1, 158),
         (try_end),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, reg1, pos1),

         (assign, reg2, ":skill_level"),
         (create_button_overlay, reg1, "@_{reg2}_"),
         (try_begin),
            (eq, ":count_2", 0),
            (position_set_x, pos1, 53),
         (else_try),
            (eq, ":count_2", 1),
            (position_set_x, pos1, 123),
         (else_try),
            (position_set_x, pos1, 193),
         (try_end),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 700),
         (position_set_y, pos1, 700),
         (overlay_set_size, reg1, pos1),
      (try_end),
      (set_container_overlay, -1),

#兵种介绍
      (troop_get_slot, ":function_no", ":troop_no", slot_troop_function),
      (val_max, ":function_no", "itm_function_combat"), #不填就默认是格斗
      (str_store_item_name, s2, ":function_no"),
      (str_store_troop_name_plural, s1, ":troop_no"),
      (create_text_overlay, reg1, "@兵 种 职 能 ： {s2}^^{s1}", tf_scrollable),
      (position_set_x, pos1, 710),
      (position_set_y, pos1, 225),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
      (position_set_x, pos1, 230),
      (position_set_y, pos1, 100),
      (overlay_set_area_size, reg1, pos1),

      (create_game_button_overlay, "$g_presentation_obj_3", "@Check_this_troop"),
      (position_set_x, pos1, 825),
      (position_set_y, pos1, 350),
      (overlay_set_position, "$g_presentation_obj_3", pos1),
      (overlay_set_display, "$g_presentation_obj_3", 0),

#inventory
      (create_text_overlay, reg1, "@ ", tf_scrollable),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 58),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 250),
      (position_set_y, pos1, 160),
      (overlay_set_area_size, reg1, pos1),
      (set_container_overlay, reg1),
      
      (troop_get_inventory_capacity, ":inventroy_limit", ":troop_no"),
      (store_div, ":cur_y", ":inventroy_limit", 6),
      (val_mul, ":cur_y", 40),
      (assign, ":cur_x", 5),
      (try_for_range, ":count_no", 0, ":inventroy_limit"),
         (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
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

         (troop_get_inventory_slot, ":item_no", ":troop_no", ":count_no"),
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
            (store_mod, ":position_change", ":count_no", 6),
            (neq, ":position_change", 5),
            (val_add, ":cur_x", 40),
         (else_try),
            (assign, ":cur_x", 5),
            (val_sub, ":cur_y", 40),
         (try_end),
      (try_end),
      (set_container_overlay, -1),
    ]),


#retrival condition
  ("cf_faction_retrival_check", [
      (store_script_param, ":faction_no", 1),#item no
      (assign, ":continue_no", 0),

      (try_begin),                                          #faction grade
         (eq, "$faction_grade", 0),#total
         (val_add, ":continue_no", 1),
      (else_try),
         (item_get_difficulty, ":grade_no", ":faction_no"),#faction grade
         (eq, ":grade_no", "$faction_grade"),
         (val_add, ":continue_no", 1),
      (try_end),

      (try_begin),                                          #faction character
         (eq, "$faction_character", 0),#total
         (val_add, ":continue_no", 1),
      (else_try),
         (eq, "$faction_character", 1),#country_faction
         (call_script, "script_faction_superior_country_check", ":faction_no", 0),
         (gt, reg1, 0),
         (val_add, ":continue_no", 1),
      (else_try),
         (eq, "$faction_character", 2),#non-country_faction
         (call_script, "script_faction_superior_country_check", ":faction_no", 0),
         (le, reg1, 0),
         (val_add, ":continue_no", 1),
      (try_end),

      (try_begin),                                          #faction affiliation
         (eq, "$faction_affiliation", 0),#total
         (val_add, ":continue_no", 1),
      (else_try),
         (eq, "$faction_affiliation", 1),#highest faction
         (call_script, "script_get_faction_affiliation", ":faction_no", 0),
         (le, reg1, 0),
         (val_add, ":continue_no", 1),
      (else_try),
         (eq, "$faction_affiliation", 2),#not highest faction
         (call_script, "script_get_faction_affiliation", ":faction_no", 0),
         (gt, reg1, 0),
         (val_add, ":continue_no", 1),
      (else_try),
         (eq, "$faction_affiliation", 3),#bottom faction
         (assign, ":count_no_2", 0),
         (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),
            (call_script, "script_get_faction_affiliation", ":count_no", 0),
            (eq, reg1, ":faction_no"),
            (assign, ":count_no_2", 1),
         (try_end),
#         (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),
#            (call_script, "script_get_faction_affiliation", ":count_no", 1),
#            (eq, reg1, ":faction_no"),
#            (assign, ":count_no_2", 1),
#         (try_end),
         (eq, ":count_no_2", 0),
         (val_add, ":continue_no", 1),
      (else_try),
         (eq, "$faction_affiliation", 4),#not bottom faction
         (assign, ":count_no_2", 0),
         (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),
            (call_script, "script_get_faction_affiliation", ":count_no", 0),
            (eq, reg1, ":faction_no"),
            (assign, ":count_no_2", 1),
         (try_end),
         (eq, ":count_no_2", 1),
         (val_add, ":continue_no", 1),
      (try_end),
      (eq, ":continue_no", 3),
    ]),

#Check if certain faction is the object faction's superior, including itself
  ("cf_faction_superior_check", [
      (store_script_param, ":object_faction_no", 1),
      (store_script_param, ":superior_faction_no", 2),
      (store_script_param, ":joiner_type", 3),#0 is faction(item), 1 is troop.

      (assign, ":continue_no", 0),
      (try_begin),
         (eq, ":object_faction_no", ":superior_faction_no"),
         (assign, ":continue_no", 1),
      (else_try),
         (call_script, "script_get_faction_affiliation", ":object_faction_no", ":joiner_type"),
         (try_begin),
            (eq, ":superior_faction_no", reg1),
            (assign, ":continue_no", 1),
         (else_try),
            (item_get_difficulty, ":return_value", reg1),#faction grade
            (le, ":return_value", 5),
            (call_script, "script_cf_faction_superior_check", reg1, ":superior_faction_no", 0),#check superior faction's superior.
            (assign, ":continue_no", 1),
         (try_end),
      (try_end),
      (eq, ":continue_no", 1),
    ]),


#Check if certain faction is affiliated to ceratin country, return country faction id. Otherwise return 0.
  ("faction_superior_country_check", [
      (store_script_param, ":object_faction_no", 1),
      (store_script_param, ":joiner_type", 2),#0 is faction(item), 1 is troop.

      (assign, ":continue_no", 0),
      (try_begin),
         (item_has_property, ":object_faction_no", itp_country_power),
         (assign, ":continue_no",":object_faction_no"),
      (else_try),
         (call_script, "script_get_faction_affiliation", ":object_faction_no", ":joiner_type"),
         (try_begin),
            (item_has_property, reg1, itp_country_power),
            (assign, ":continue_no", reg1),
         (else_try),
            (item_get_difficulty, ":return_value", reg1),#faction grade
            (le, ":return_value", 4),
            (gt, reg1, 0),
            (call_script, "script_faction_superior_country_check", reg1, 0),#check superior faction's superior.
            (assign, ":continue_no", reg1),
         (try_end),
      (try_end),
      (assign, reg1, ":continue_no"),
    ]),

#派系获取首领
  ("faction_leader_check", [#ouput reg1 and reg2, if there is no leader, output -1
      (store_script_param, ":object_faction_no", 1),

      (assign, ":target_faction_no", -1),
      (assign, ":target_faction_type", -1),
      (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),
         (call_script, "script_get_faction_affiliation", ":count_no", 0),
         (eq, reg1, ":object_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 0),
         (eq, reg1, 2),#leader
         (assign, ":target_faction_no", ":count_no"),
         (assign, ":target_faction_type", 0),
      (try_end),

      (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),
         (troop_is_hero, ":count_no"),
         (call_script, "script_get_faction_affiliation", ":count_no", 1),
         (eq, reg1, ":object_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 1),
         (eq, reg1, 2),#leader
         (assign, ":target_faction_no", ":count_no"),
         (assign, ":target_faction_type", 1),
      (try_end),
      (assign, reg1, ":target_faction_no"),
      (assign, reg2, ":target_faction_type"),#0 is faction(item), 1 is troop.
    ]),

#派系获取支柱数量
  ("faction_pillar_number_check", [#ouput reg1
      (store_script_param, ":object_faction_no", 1),

      (assign, ":target_faction_num", 0),
      (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),
         (call_script, "script_get_faction_affiliation", ":count_no", 0),
         (eq, reg1, ":object_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 0),
         (eq, reg1, 1),#pillar
         (val_add, ":target_faction_num", 1),
      (try_end),

      (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),
         (troop_is_hero, ":count_no"),
         (call_script, "script_get_faction_affiliation", ":count_no", 1),
         (eq, reg1, ":object_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 1),
         (eq, reg1, 1),#pillar
         (val_add, ":target_faction_num", 1),
      (try_end),
      (assign, reg1, ":target_faction_num"),
    ]),

#派系获取普通成员数量
  ("faction_normal_number_check", [#ouput reg1
      (store_script_param, ":object_faction_no", 1),

      (assign, ":target_faction_num", 0),
      (try_for_range, ":count_no", "itm_faction_begin", "itm_faction_end"),
         (call_script, "script_get_faction_affiliation", ":count_no", 0),
         (eq, reg1, ":object_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 0),
         (eq, reg1, 0),#normal member
         (val_add, ":target_faction_num", 1),
      (try_end),

      (try_for_range, ":count_no", "trp_player", "trp_relative_of_merchants_end"),
         (troop_is_hero, ":count_no"),
         (call_script, "script_get_faction_affiliation", ":count_no", 1),
         (eq, reg1, ":object_faction_no"),
         (call_script, "script_get_faction_position", ":count_no", 1),
         (eq, reg1, 0),#normal member
         (val_add, ":target_faction_num", 1),
      (try_end),
      (assign, reg1, ":target_faction_num"),
    ]),

#draw troop tree
  ("faction_troop_tree_recursive_backtracking", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":cur_x", 2),
      (store_script_param, ":cur_y", 3),
      (store_script_param, ":offset_x", 4),   #troops in one upgarde tree have a distance of 125
      
      (store_add, ":next_x", ":cur_x", ":offset_x"),
      (troop_get_upgrade_troop, ":upgrade_troop_1", ":troop_no", 0),      # upgrade_troop
      (troop_get_upgrade_troop, ":upgrade_troop_2", ":troop_no", 1),
      (try_begin),
         (gt,  ":upgrade_troop_2", 0),
         (call_script, "script_faction_troop_tree_recursive_backtracking", ":upgrade_troop_2", ":next_x", reg2, ":offset_x"),
         (assign, ":upgrade_troop_2_y", reg0),
         (val_add, reg2, 200), # current global y
         (call_script, "script_faction_troop_tree_recursive_backtracking", ":upgrade_troop_1", ":next_x", reg2, ":offset_x"),
         (assign, ":upgrade_troop_1_y", reg0),
      (else_try),
         (gt,  ":upgrade_troop_1", 0),
         (call_script, "script_faction_troop_tree_recursive_backtracking", ":upgrade_troop_1", ":next_x", reg2, ":offset_x"),
         (assign, ":upgrade_troop_1_y", reg0),
      (try_end),
      
      # troop_tree_line
      (try_begin),
         (gt,  ":upgrade_troop_2", 0),
         (store_add, reg0, ":upgrade_troop_1_y", ":upgrade_troop_2_y"),
         (val_div, reg0, 2),
         #                       3---- upgrade_troop_1
         #                       |2
         # troop_no ----1
         #                       |2
         #                       3---- upgrade_troop_2
         (store_div, ":half_offset_x", ":offset_x", 2),
         (store_add, ":middle_x", ":cur_x", ":half_offset_x"),
         (call_script, "script_prsnt_line", ":half_offset_x", 1, ":cur_x", reg0, 0xFFFFFF),#1
         (call_script, "script_prsnt_line", ":half_offset_x", 1, ":middle_x", ":upgrade_troop_1_y", 0xFFFFFF),#3
         (call_script, "script_prsnt_line", ":half_offset_x", 1, ":middle_x", ":upgrade_troop_2_y", 0xFFFFFF),#3
         (store_sub, ":size_y", ":upgrade_troop_1_y", ":upgrade_troop_2_y"),
         (val_add, ":size_y", 1),
         (call_script, "script_prsnt_line", 1, ":size_y", ":middle_x", ":upgrade_troop_2_y", 0xFFFFFF),#2
      (else_try),
         (gt,  ":upgrade_troop_1", 0),
         (assign, reg0, ":upgrade_troop_1_y"),
         #
         # troop_no -------- upgrade_troop_1
         #
         (call_script, "script_prsnt_line", ":offset_x", 2, ":cur_x", ":upgrade_troop_1_y", 0xFFFFFF),
      (else_try),
         (assign, reg0, ":cur_y"),
      (try_end),
      
      # troop name
      (str_store_troop_name, s1, ":troop_no"),
      (create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_vertical_align_center|tf_double_space|tf_scrollable),
      (store_sub, ":name_x", ":cur_x", 50),
      (store_sub, ":name_y", reg0, 130),
      (position_set_x, pos1, ":name_x"),
      (position_set_y, pos1, ":name_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 100),
      (position_set_y, pos1, 60),
      (overlay_set_area_size, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),
      
      # troop avatar
      (store_sub, ":avatar_x", ":cur_x", 75),
      (store_sub, ":avatar_y", reg0, 75),
      (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
      (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
      (set_fixed_point_multiplier, 1000),
      (position_set_x, pos1, 450),
      (position_set_y, pos1, 600),
      (overlay_set_size, reg1, pos1),
      (position_set_x, pos1, ":avatar_x"),
      (position_set_y, pos1, ":avatar_y"),
      (overlay_set_position, reg1, pos1),
      (troop_set_slot, "trp_temp_array_a", reg1, ":troop_no"),
    ]),

#场景随机生成小兵，如果该阵营没有小兵，就从上级获取，上级也没有就更上级，以此迭代
#输出reg3作为可用小兵总数
  ("get_scene_random_troop", [
      (store_script_param, ":item_faction_no", 1),
      (store_script_param, ":level_limit", 2),#等级上限
      (try_for_range, ":cur_troop_no", soldiers_begin, soldiers_end),
         (neg|troop_is_hero, ":cur_troop_no"),
         (troop_slot_eq, ":cur_troop_no", slot_troop_affiliation, ":item_faction_no"),#暂且先只刷新一阶兵
         (store_character_level, ":level_no", ":cur_troop_no"),
         (le, ":level_no", ":level_limit"),
         (troop_set_slot, "trp_temp_array_a", reg3, ":cur_troop_no"),
         (val_add, reg3, 1),
      (try_end),
      (try_begin),
         (lt, reg3, 3),#不够多，就向上级迭代
         (call_script, "script_get_faction_affiliation", ":item_faction_no", 0),
         (gt, reg1, 0),#存在上级
         (call_script, "script_get_scene_random_troop", reg1, ":level_limit"),
      (try_end),
    ]),



#开局选人的选项卡
#输入角色序号（1到6），自动从原有快速战斗角色处获取角色模板。返回reg1，在脚本外设置为全局变量
  ("characer_choose_card", [
      (store_script_param, ":num", 1),
      (store_script_param, ":cur_x", 2),
      (val_sub, ":num", 1),
      (val_add, ":num", "trp_quick_battle_troop_1"),
      (str_store_troop_name, s1, ":num"),

      (create_text_overlay, reg1, s1, tf_scrollable|tf_center_justify),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, 195),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 115),
      (position_set_y, pos1, 440),
      (overlay_set_area_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),
      (set_container_overlay, reg1),

      (assign, ":cur_height", 25),
      (try_for_range, ":count", 0, 7),
         (store_add, ":weapon_no", wpt_one_handed_weapon, ":count"),
         (store_proficiency_level, reg2, ":num", ":weapon_no"),#熟练
         (gt, reg2, 0),
         (store_add, ":string_no", ":count", "str_wpt_one_handed"),
         (str_store_string, s1, ":string_no"),

         (create_button_overlay, reg1, "@{s1}_{reg2}"),
         (position_set_x, pos1, 1),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 600),
         (position_set_y, pos1, 600),
         (overlay_set_size, reg1, pos1),
         (overlay_set_color, reg1, 0xFFFFFF),
         (val_add, ":cur_height", 11),
      (try_end),

      (try_for_range, ":count", 0, 42),
         (store_sub, ":skill_no", skl_reserved_18, ":count"),
         (store_skill_level, ":skill_level", ":skill_no", ":num"),#技能
         (gt, ":skill_level", 0),
         (store_add, ":string_no", ":count", "str_reserved_18"),
         (str_store_string, s1, ":string_no"),
         (assign, reg2, ":skill_level"),

         (create_button_overlay, reg1, "@{s1}_{reg2}"),
         (position_set_x, pos1, 1),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 600),
         (position_set_y, pos1, 600),
         (overlay_set_size, reg1, pos1),
         (overlay_set_color, reg1, 0xFFFFFF),
         (val_add, ":cur_height", 11),
      (try_end),

      (try_for_range, ":count", 0, 4),
         (store_add, ":string_no", ":count", "str_strength"),
         (str_store_string, s1, ":string_no"),
         (store_add, ":attribute_no", ":count", ca_strength),
         (store_attribute_level, reg2, ":num", ":attribute_no"),#属性

         (create_text_overlay, reg1, "@{s1}_{reg2}"),
         (position_set_x, pos1, 1),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),
         (position_set_x, pos1, 600),
         (position_set_y, pos1, 600),
         (overlay_set_size, reg1, pos1),
         (overlay_set_color, reg1, 0xFFFFFF),
        (val_add, ":cur_height", 11),
      (try_end),

      (val_add, ":cur_height", 7),
      (troop_get_inventory_capacity, ":inventroy_limit", ":num"),
      (try_for_range, ":count_no", 0, ":inventroy_limit"),
         (troop_get_inventory_slot, ":item_no", ":num", ":count_no"),#物品栏
         (gt, ":item_no", 0),
         (create_mesh_overlay, reg1, "mesh_inv_slot"),
         (position_set_x, pos1, 200),
         (position_set_y, pos1, 200),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 11),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),

         (create_mesh_overlay_with_item_id, reg1, ":item_no"),
         (position_set_x, pos1, 200),
         (position_set_y, pos1, 200),
         (overlay_set_size, reg1, pos1),
         (position_set_x, pos1, 21),
         (val_add, ":cur_height", 10),
         (position_set_y, pos1, ":cur_height"),
         (overlay_set_position, reg1, pos1),
         (val_add, ":cur_height", 11),
      (try_end),

      (store_mul, ":cur_troop", ":num", 2), #with weapons
      (create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
      (position_set_x, pos1, -58),
      (position_set_y, pos1, 130),
      (overlay_set_position, reg1, pos1),

      (set_container_overlay, -1),

      (val_sub, ":cur_x", 12),
      (create_image_button_overlay, reg1, "mesh_character_choose_window", "mesh_character_choose_window_lighten"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, 160),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 238),
      (position_set_y, pos1, 1350),
      (overlay_set_size, reg1, pos1),
      (overlay_set_additional_render_height, reg1, -1),
    ]),



######################################################图鉴######################################################
#用于troop场景图鉴的属性刷新
#输入显示的troop（$troop_show_2）
  ("troop_attribute_refresh", [
      (store_script_param, ":troop_no", 1),
      (set_fixed_point_multiplier, 1000),

      (str_store_troop_name, s1, ":troop_no"),
      (overlay_set_text, "$g_presentation_text_1", s1),#名字
      (str_store_troop_name_plural, s1, ":troop_no"),
      (overlay_set_text, "$g_presentation_text_2", "@{s1}^_"),#介绍

      (store_faction_of_troop, ":faction_no", ":troop_no"),
      (str_store_faction_name, s1, ":faction_no"),
      (overlay_set_text, "$g_presentation_text_3", s1),#阵营

      (store_character_level, reg2, ":troop_no"),
      (overlay_set_text, "$g_presentation_text_4", "@等 级 ：{reg2}"),#等级

      (assign, ":height_no", 0),
      (try_for_range, ":count", 0, 42),
         (store_sub, ":skill_no", skl_reserved_18, ":count"),
         (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
         (gt, ":skill_level", 0),
         (val_add, ":height_no", 1),#统计
      (try_end),
      (val_add, ":height_no", 1),
      (val_div, ":height_no", 2),
      (val_add, ":height_no", 1),
      (val_mul, ":height_no", 20),#高度

      (assign, ":count_no_3", 0),
      (try_for_range, ":count_no", 0, 54),
         (lt, ":count_no", 4),
         (store_add, ":overlay_no", ":count_no", "$g_presentation_mesh_1"),
         (val_add, ":overlay_no", 1),                                                               #获取overlay序号
         (store_add, ":string_no", ":count_no", "str_strength"),
         (str_store_string, s1, ":string_no"),                                                   #获取文本
         (store_add, ":attribute_no", ":count_no", ca_strength),
         (store_attribute_level, ":attribute_level", ":troop_no", ":attribute_no"),#获取属性
         (assign, reg2, ":attribute_level"),
         (overlay_set_text, ":overlay_no", "@{s1}_{reg2}"),
      (else_try),
         (lt, ":count_no", 11),
         (store_add, ":overlay_no", ":count_no", "$g_presentation_mesh_1"),
         (val_add, ":overlay_no", 1),                                                              #获取overlay序号
         (store_sub, ":count_no_2", ":count_no", 4),
         (store_add, ":string_no", ":count_no_2", "str_wpt_one_handed"),
         (str_store_string, s1, ":string_no"),                                                  #获取文本
         (store_add, ":weapon_no", wpt_one_handed_weapon, ":count_no_2"),
         (store_proficiency_level, ":weapon_level", ":troop_no", ":weapon_no"),#获取熟练
         (assign, reg2, ":weapon_level"),
         (overlay_set_text, ":overlay_no", "@{s1}_{reg2}"),
      (else_try),
         (is_between, ":count_no", 12, 55),
         (store_add, ":overlay_no", ":count_no", "$g_presentation_mesh_1"),#技能
         (val_add, ":overlay_no", 1),                                                             #获取overlay序号
         (store_sub, ":count_no_2", ":count_no", 11),
         (store_sub, ":skill_no", skl_reserved_18, ":count_no_2"),
         (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
         (try_begin),
            (gt, ":skill_level", 0),
            (assign, reg2, ":skill_level"),
            (store_add, ":string_no", ":count_no_2", "str_reserved_18"),
            (str_store_string, s1, ":string_no"),
            (overlay_set_text, ":overlay_no", "@{s1}_{reg2}"),
            (overlay_set_display, ":overlay_no", 1),

            (store_mod, ":count_no_4", ":count_no_3", 2),
            (store_div, ":count_no_5", ":count_no_3", 2),
            (try_begin),
               (eq, ":count_no_4", 0),
               (position_set_x, pos1, 10),
            (else_try),
               (position_set_x, pos1, 75),
            (try_end),
            (val_mul, ":count_no_5", -20),
            (store_add, ":cur_height", ":height_no", ":count_no_5"),
            (position_set_y, pos1, ":cur_height"),
            (overlay_set_position, ":overlay_no", pos1),
            (val_add, ":count_no_3", 1),
         (else_try),
            (position_set_x, pos1, 10),
            (position_set_y, pos1, 10),
            (overlay_set_position, ":overlay_no", pos1),
            (overlay_set_display, ":overlay_no", 0),
         (try_end),
      (try_end),

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
      (try_for_range, ":count_no", ":passive_begin", "itm_passive_skills_end"),#被动
         (store_sub, ":overlay_no", ":count_no", "itm_passive_skills_begin"),
         (val_add, ":overlay_no", "$g_presentation_container_2"),

         (call_script, "script_check_agent_passive_skill", "$mission_show_agent", ":count_no"),#持有该被动
         (gt, reg1, 0),

         (position_set_x, pos1, ":cur_x"),
         (position_set_y, pos1, ":cur_y"),
         (overlay_set_position, ":overlay_no", pos1),
         (overlay_set_display, ":overlay_no", 1),
         (try_begin),
            (eq, ":cur_x", 20),
            (assign, ":cur_x", 65),
         (else_try),
            (eq, ":cur_x", 65),
            (assign, ":cur_x", 20),
            (val_sub, ":cur_y", 45),
         (try_end),
      (else_try),
         (position_set_x, pos1, 5),
         (position_set_y, pos1, 5),
         (overlay_set_position, ":overlay_no", pos1),
         (overlay_set_display, ":overlay_no", 0),
      (try_end),

      (store_agent_hit_points, reg2, "$mission_show_agent", 1),#血量
      (try_begin),
         (store_mod, ":count_no", reg2, 10),
         (eq, ":count_no", 9),
         (val_add, reg2, 1),
      (try_end),
      (overlay_set_text, "$g_presentation_text_5", "@生 命 ：{reg2}"),

      (agent_get_damage_modifier, reg2, "$mission_show_agent"),#伤害
      (try_begin),
         (store_mod, ":count_no", reg2, 10),
         (eq, ":count_no", 9),
         (val_add, reg2, 1),
      (try_end),
      (overlay_set_text, "$g_presentation_text_6", "@攻 击 ：{reg2}%"),

      (agent_get_speed_modifier, reg2, "$mission_show_agent"),#速度
      (try_begin),
         (store_mod, ":count_no", reg2, 10),
         (eq, ":count_no", 9),
         (val_add, reg2, 1),
      (try_end),
      (overlay_set_text, "$g_presentation_text_7", "@速 度 ：{reg2}%"),

      (agent_get_accuracy_modifier, reg2, "$mission_show_agent"),#精准
      (try_begin),
         (store_mod, ":count_no", reg2, 10),
         (eq, ":count_no", 9),
         (val_add, reg2, 1),
      (try_end),
      (overlay_set_text, "$g_presentation_text_8", "@精 准 ：{reg2}%"),

      (agent_get_reload_speed_modifier, reg2, "$mission_show_agent", 1),#装填
      (try_begin),
         (store_mod, ":count_no", reg2, 10),
         (eq, ":count_no", 9),
         (val_add, reg2, 1),
      (try_end),
      (overlay_set_text, "$g_presentation_text_9", "@装 填 ：{reg2}%"),
    ]),

#用于troop场景图鉴的检索刷新
  ("troop_retrieve_refresh", [
           (set_fixed_point_multiplier, 1000),
           (store_add, ":troop_begin", "$g_presentation_container_1", 1),
           (try_for_range, ":overlay_no", ":troop_begin", "$g_presentation_obj_2"),
              (overlay_set_display, ":overlay_no", 0),
              (position_set_x, pos1, 10),
              (position_set_y, pos1, 10),
              (overlay_set_position, ":overlay_no", pos1),#全部隐藏
           (try_end),

           (assign, ":cur_y", 5),
           (try_for_range, ":overlay_no", ":troop_begin", "$g_presentation_obj_2"),
              (troop_get_slot, ":troop_no", "trp_temp_array_a", ":overlay_no"),
              (store_troop_faction, ":faction_no", ":troop_no"),
              (this_or_next|eq, ":faction_no", "$troop_faction_choose"),
              (eq, "$troop_faction_choose", -1),#阵营
              (store_character_level, ":level_no", ":troop_no"),
              (val_div, ":level_no", 10),
              (this_or_next|eq, ":level_no", "$troop_grade_choose"),
              (eq, "$troop_grade_choose", -1),#等级

              (assign, ":continue_no", -1),
              (try_begin),
                 (eq, "$troop_class_choose", -1),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 0),#步兵
                 (neg|troop_is_guarantee_ranged, ":troop_no"),
                 (neg|troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 1),#投射手
                 (troop_is_guarantee_ranged, ":troop_no"),
                 (neg|troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 2),#骑手
                 (neg|troop_is_guarantee_ranged, ":troop_no"),
                 (troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 3),#游骑
                 (troop_is_guarantee_ranged, ":troop_no"),
                 (troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (try_end),
              (eq, ":continue_no", 1),

              (overlay_set_display, ":overlay_no", 1),
              (val_add, ":cur_y", 20),#统计高度
           (try_end),

           (try_for_range, ":overlay_no", ":troop_begin", "$g_presentation_obj_2"),
              (troop_get_slot, ":troop_no", "trp_temp_array_a", ":overlay_no"),
              (store_troop_faction, ":faction_no", ":troop_no"),
              (this_or_next|eq, ":faction_no", "$troop_faction_choose"),
              (eq, "$troop_faction_choose", -1),#阵营
              (store_character_level, ":level_no", ":troop_no"),
              (val_div, ":level_no", 10),
              (this_or_next|eq, ":level_no", "$troop_grade_choose"),
              (eq, "$troop_grade_choose", -1),#等级

              (assign, ":continue_no", -1),
              (try_begin),
                 (eq, "$troop_class_choose", -1),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 0),#步兵
                 (neg|troop_is_guarantee_ranged, ":troop_no"),
                 (neg|troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 1),#投射手
                 (troop_is_guarantee_ranged, ":troop_no"),
                 (neg|troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 2),#骑手
                 (neg|troop_is_guarantee_ranged, ":troop_no"),
                 (troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (else_try),
                 (eq, "$troop_class_choose", 3),#游骑
                 (troop_is_guarantee_ranged, ":troop_no"),
                 (troop_is_guarantee_horse, ":troop_no"),
                 (assign, ":continue_no", 1),
              (try_end),
              (eq, ":continue_no", 1),

              (val_sub, ":cur_y", 20),
              (position_set_x, pos1, 10),
              (position_set_y, pos1, ":cur_y"),
              (overlay_set_position, ":overlay_no", pos1),
           (try_end),
    ]),

#用于获得下一个可用faction
#输入目前的faction
#输出reg1
  ("troop_get_next_faction", [
      (store_script_param, ":faction_no", 1),

      (val_add, ":faction_no", 1),
      (try_begin),
         (eq, ":faction_no", "fac_faction_end"),
         (str_store_string, s1, "@全 部 "),
         (assign, reg1, -1),
      (else_try),
         (faction_slot_ge, ":faction_no", slot_faction_is_availiable, 1),
         (str_store_faction_name, s1, ":faction_no"),
         (assign, reg1, ":faction_no"),
      (else_try),
         (call_script, "script_troop_get_next_faction", ":faction_no"),
      (try_end),
    ]),

#用于获得玩家下一个激活的被动技能
#输入目前的被动技能
#输出reg1, -1即为全部结束
  ("player_get_next_passive", [
      (store_script_param, ":passive_no", 1),

      (val_add, ":passive_no", 1),
      (try_begin),
         (eq, ":passive_no", "itm_passive_skills_end"),
         (assign, reg1, -1),
      (else_try),
         (call_script, "script_check_troop_passive_skill_activited", "trp_player", ":passive_no"),
         (gt, reg1, 0),
         (assign, reg1, ":passive_no"),
      (else_try),
         (call_script, "script_player_get_next_passive", ":passive_no"),
      (try_end),
    ]),

#用于部队所选兵种的刷新
  ("troop_party_refresh", [
      (try_for_range, ":count_no", 1, 9),
         (store_add, ":overlay_no", "$g_presentation_text_13", ":count_no"),
         (overlay_set_text, ":overlay_no" , "@_"),#刷新
      (try_end),

      (store_add, ":overlay_no", "$g_presentation_text_13", 1),
      (party_get_num_companion_stacks, ":stack_num", "$party_show"),
      (try_for_range, ":count_no", 0, ":stack_num"),
         (party_stack_get_troop_id, ":troop_no", "$party_show", ":count_no"),
         (str_store_troop_name, s1, ":troop_no"),
         (party_stack_get_size, reg2, "$party_show", ":count_no"),
         (overlay_set_text, ":overlay_no" , "@{s1}_{reg2}"),
         (val_add, ":overlay_no", 1),
      (try_end),
    ]),



#用于围绕某个点位，获取按某一半径环绕该点的位置的坐标，用于后续生成overlay
#输入position精度均为1000
#默认从x轴正方向开始生成，若需要改变起始点，输入偏转的角度
#输入圆心xy坐标、半径、偏转角
#xy坐标输入reg3和reg4（避免与生成overlay常用的reg1混淆）
  ("overlay_get_position_around_center", [
      (store_script_param, ":pos_x", 1),
      (store_script_param, ":pos_y", 2),#圆心坐标xy值
      (store_script_param, ":radius", 3),#半径（1000精度，prsnt常用精度）
      (store_script_param, ":angle", 4),#初始角度（360度下）

      (val_mul, ":angle", 1000),
      (store_cos, ":cur_x", ":angle"),
      (store_sin, ":cur_y", ":angle"),

      (val_mul, ":cur_x", ":radius"),
      (val_mul, ":cur_y", ":radius"),
      (val_div, ":cur_x", 1000),
      (val_div, ":cur_y", 1000),
      (val_add, ":cur_x", ":pos_x"),
      (val_add, ":cur_y", ":pos_y"),

      (assign, reg3, ":cur_x"),
      (assign, reg4, ":cur_y"),
    ]),



######################################################私兵######################################################
#录入私兵
#比如123|041|1024就是1024号兵种作为私兵，每次增员41个最多123人。
  ("bodyguard_troop_import", [
      (store_script_param, ":lord_troop_no", 1),
      (store_script_param, ":bodyguard_troop_no", 2),
      (store_script_param, ":num_increase", 3), #每次增员的数量
      (store_script_param, ":num_limit", 4), #上限
      (store_script_param, ":slot_no", 5), #槽1或者2

      (val_mul, ":num_increase", 10000),
      (val_mul, ":num_limit", 10000000),
      (val_add, ":num_limit", ":num_increase"),
      (val_add, ":bodyguard_troop_no", ":num_limit"),
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_bodygaurd_troop_1),
      (troop_set_slot, ":lord_troop_no", ":slot_no", ":bodyguard_troop_no"),
    ]),




######################################################侵蚀######################################################
#物品栏内服用各种物品的效果
  ("expendable_item_effect", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":item_no", 2),

      (try_begin),
         (this_or_next|is_between, ":item_no", "itm_inferior_dragonblood_wine", "itm_dragon_heart"),
         (eq, ":item_no", "itm_dragon_heart"),
         (item_get_hit_points, ":power_add_no", ":item_no"),#龙力
         (item_get_food_quality, ":crazy_add_no", ":item_no"),#龙癫
         (item_get_max_ammo, ":stage_no", ":item_no"),#等级
         (call_script, "script_dragon_power_add", ":troop_no", ":power_add_no", ":crazy_add_no", ":stage_no"),
      (try_end),
    ]),


#输入troop id和增加的龙力、龙癫
  ("dragon_power_add", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":power_add_no", 2),#增加的龙力
      (store_script_param, ":crazy_add_no", 3),#增加的龙癫
      (store_script_param, ":value_no", 4),#阶段

      (troop_get_slot, ":count_no", ":troop_no", slot_troop_dragon_power),
      (store_mod, ":power_count_no", ":count_no", 100000),#龙力
      (val_div, ":count_no", 100000),
      (store_mod, ":stage_no", ":count_no", 10),#阶段
      (val_div, ":count_no", 10),#龙癫

      (val_add, ":count_no", ":crazy_add_no"),
      (try_begin),
         (le, ":value_no", ":stage_no"),
         (eq, ":troop_no", "trp_player"),
         (display_message, "@此 物 已 不 能 使 你 继 续 提 升 ， 你 需 要 摄 取 更 加 精 纯 的 龙 力 。 "),
      (else_try),
         (gt, ":value_no", ":stage_no"),
         (val_add, ":power_count_no", ":power_add_no"),
         (try_begin),
            (eq, ":stage_no", 0),
            (ge, ":power_count_no", 1000),
            (val_sub, ":power_count_no", 1000),
            (val_add, ":stage_no", 1),
            (troop_raise_attribute, ":troop_no", ca_strength, 2),
            (troop_raise_attribute, ":troop_no", ca_agility, 2),
            (troop_raise_attribute, ":troop_no", ca_intelligence, 2),
            (troop_raise_attribute, ":troop_no", ca_charisma, 2),
            (display_message, "@你 的 龙 力 攀 升 了 ！ ", 0xff9933),
            (call_script, "script_improve_troop_passive_skill_learned", ":troop_no", "itm_passive_dragon_power_surging", 1),
         (else_try),
            (eq, ":stage_no", 1),
            (ge, ":power_count_no", 2000),
            (val_sub, ":power_count_no", 2000),
            (val_add, ":stage_no", 1),
            (troop_raise_attribute, ":troop_no", ca_strength, 2),
            (troop_raise_attribute, ":troop_no", ca_agility, 2),
            (troop_raise_attribute, ":troop_no", ca_intelligence, 2),
            (troop_raise_attribute, ":troop_no", ca_charisma, 2),
            (display_message, "@你 的 龙 力 攀 升 了 ！ ", 0xff9933),
            (call_script, "script_improve_troop_passive_skill_learned", ":troop_no", "itm_passive_dragon_power_surging", 1),
         (else_try),
            (eq, ":stage_no", 2),
            (ge, ":power_count_no", 3000),
            (val_sub, ":power_count_no", 3000),
            (val_add, ":stage_no", 1),
            (troop_raise_attribute, ":troop_no", ca_strength, 3),
            (troop_raise_attribute, ":troop_no", ca_agility, 3),
            (troop_raise_attribute, ":troop_no", ca_intelligence, 3),
            (troop_raise_attribute, ":troop_no", ca_charisma, 3),
            (display_message, "@你 的 龙 力 攀 升 了 ！ ", 0xff9933),
            (call_script, "script_improve_troop_passive_skill_learned", ":troop_no", "itm_passive_dragon_power_surging", 1),
         (else_try),
            (eq, ":stage_no", 3),
            (ge, ":power_count_no", 4000),
            (val_sub, ":power_count_no", 4000),
            (val_add, ":stage_no", 1),
            (troop_raise_attribute, ":troop_no", ca_strength, 3),
            (troop_raise_attribute, ":troop_no", ca_agility, 3),
            (troop_raise_attribute, ":troop_no", ca_intelligence, 3),
            (troop_raise_attribute, ":troop_no", ca_charisma, 3),
            (display_message, "@你 的 龙 力 攀 升 了 ！ ", 0xff9933),
            (call_script, "script_improve_troop_passive_skill_learned", ":troop_no", "itm_passive_dragon_power_surging", 1),
         (else_try),
            (eq, ":stage_no", 4),
            (ge, ":power_count_no", 5000),
            (val_sub, ":power_count_no", 5000),
            (val_add, ":stage_no", 1),
            (troop_raise_attribute, ":troop_no", ca_strength, 4),
            (troop_raise_attribute, ":troop_no", ca_agility, 4),
            (troop_raise_attribute, ":troop_no", ca_intelligence, 4),
            (troop_raise_attribute, ":troop_no", ca_charisma, 4),
            (display_message, "@你 的 龙 力 攀 升 了 ！ ", 0xff9933),
            (call_script, "script_improve_troop_passive_skill_learned", ":troop_no", "itm_passive_dragon_power_surging", 1),
         (else_try),
            (eq, ":stage_no", 5),
            (val_min, ":power_count_no", 9999),
         (try_end),

         (try_begin),
            (eq, ":troop_no", "trp_player"),
            (assign, reg1, ":power_count_no"),
            (assign, reg2, ":stage_no"),
            (try_begin),
               (le, ":count_no", 0),
               (str_store_string, s10, "@你 感 觉 很 好 。 "),
            (else_try),
               (le, ":count_no", 2),
               (str_store_string, s10, "@一 丝 狂 乱 渗 入 你 的 脊 髓 。 "),
            (else_try),
               (le, ":count_no", 6),
               (str_store_string, s10, "@些 许 癫 狂 流 入 你 的 心 脏 ， 你 感 到 不 安 。 "),
            (else_try),
               (str_store_string, s10, "@莫 名 的 疯 狂 涌 入 你 的 大 脑 ， 恐 惧 攥 紧 了 你 ， 但 旋 即 又 被 幻 觉 、 痛 苦 和 来 自 远 方 的 异 吼 扯 碎 。 "),
            (try_end), 
            (display_message, "@当 前 龙 力 {reg2}阶 {reg1}点 。 {s10}"),
         (try_end), 
      (try_end),

      (val_mul, ":count_no", 1000000),
      (val_mul, ":stage_no", 100000),
      (val_add, ":count_no", ":stage_no"),
      (val_add, ":count_no", ":power_count_no"),
      (troop_set_slot, ":troop_no", slot_troop_dragon_power, ":count_no"),
    ]),





######################################################委托相关######################################################
#冒险者协会中给出的城镇委托，最多十个，一般只有六个左右。储存内容包括委托目标ID、委托目标类型、委托目标数量、是否回收委托目标、报酬。
#比如20000|1|03|0|2345，从前往后分别为20000的报酬，1需要回收委托目标，需要3个委托目标，委托目标为item，ID为2345，实际表现为需要交付3个ID2345的item，给2万块。
##
#设置目标ID、类型和数量（最多99）
  ("set_center_quest_target", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始
      (store_script_param, ":target_no", 3),
      (store_script_param, ":type_no", 4),#0为item，1为troop
      (store_script_param, ":target_num", 5),

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_get_slot, ":count_no", ":party_no", ":quest_no"),
      (val_div, ":count_no", 10000000),
      (val_mul, ":count_no", 10000000),
      (val_add, ":count_no", ":target_no"),
      (val_mul, ":type_no", 10000),
      (val_add, ":count_no", ":type_no"),
      (val_mul, ":target_num", 100000),
      (val_add, ":count_no", ":target_num"),
      (party_set_slot, ":party_no", ":quest_no", ":count_no"),
    ]),

#获取目标ID、类型和数量
#分别由reg1、reg2和reg3输出
  ("get_center_quest_target", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_get_slot, ":count_no", ":party_no", ":quest_no"),
      (val_mod, ":count_no", 10000000),
      (store_div, reg3, ":count_no", 100000),#数量
      (val_mod, ":count_no", 100000),
      (store_div, reg2, ":count_no", 10000),#类型，0为item，1为troop
      (store_mod, reg1, ":count_no", 10000),#ID
    ]),

#设置委托目标是否要回收，0不用1用
  ("set_center_quest_recycle", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始
      (store_script_param, ":type_no", 3),

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_get_slot, ":count_no", ":party_no", ":quest_no"),
      (call_script, "script_set_digital_position", ":count_no", 8, ":type_no"),
      (party_set_slot, ":party_no", ":quest_no", reg1),
    ]),

#获取委托目标是否要回收，0不用1用
#输出reg1
  ("get_center_quest_recycle", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_get_slot, ":count_no", ":party_no", ":quest_no"),
      (call_script, "script_get_digital_position", ":count_no", 8),
    ]),

#设置委托报酬
  ("set_center_quest_reward", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始
      (store_script_param, ":reward_count", 3),

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_get_slot, ":count_no", ":party_no", ":quest_no"),
      (val_mod, ":count_no", 10000000),
      (val_mul, ":reward_count", 10000000),
      (val_add, ":count_no", ":reward_count"),
      (party_set_slot, ":party_no", ":quest_no", ":count_no"),
    ]),

#获取委托报酬
#输出reg1
  ("get_center_quest_reward", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_get_slot, ":count_no", ":party_no", ":quest_no"),
      (store_div, reg1, ":count_no", 10000000),
    ]),

#结束委托
  ("set_center_quest_end", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始

      (val_add, ":quest_no", slot_center_quest_begin),
      (val_sub, ":quest_no", 1),
      (party_set_slot, ":party_no", ":quest_no", -1),
    ]),

#玩家完成委托，包括清空slot，给予赏金，弹消息
  ("set_center_quest_finish", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":quest_no", 2),#委托的序号，从1开始

      (call_script, "script_get_center_quest_reward", ":party_no", ":quest_no"),#赏金
      (troop_add_gold, "trp_player", reg1),
      (display_message, "@委 托 完 成 。 ", 0x1d953f),
      (call_script, "script_set_center_quest_end", ":party_no", ":quest_no"),#清空
    ]),





######################################################新会战相关######################################################
#填入坐标（从左往右，从上往下），获取序号（从零开始）
  ("change_coordinate_to_number", [
      (store_script_param, ":length_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (val_sub, ":axis_x", 1),
      (val_sub, ":axis_y", 1),
      (val_mul, ":length_no", ":axis_x"),
      (val_add, ":length_no", ":axis_y"),
      (assign, reg1, ":length_no"),
    ]),

#填入序号（从零开始），获取坐标（y从左往右，x从上往下）
#输出reg1为x，reg2为y值
  ("change_number_to_coordinate", [
      (store_script_param, ":length_no", 1),
      (store_script_param, ":slot_no", 2),
      (store_div, reg1, ":slot_no", ":length_no"),#x值（行）
      (val_add, reg1, 1),
      (store_mod, reg2, ":slot_no", ":length_no"),#y值（列）
      (val_add, reg2, 1),
    ]),

#初始化设置该center的区块
#center的拓扑图尺寸为15×15，每个zone区域都是一个slot。其储存的内容包括环境（下垫面），局部气候，对应的scene，其上的建筑采用数位储存，比如3|1|165|09|0456|6|02，就是09类建筑建在6气候的2类下垫面上，所有者是第165个阵营（建筑只能由阵营所有，没有设置就属于土地所有者），1表示此建筑未被发现，3表示该建筑调用的是其第三种场景（排序注册在data initialize里）；场景是0456，如果没有场景就填0。
#气候因为是随时变化的，所以为0
  ("set_center_zone", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）
      (store_script_param, ":ground_type", 4),#下垫面类型
      (store_script_param, ":scene_no", 5),#调用的场景
      (store_script_param, ":building_no", 6),#建筑槽
      (store_script_param, ":building_owner_no", 7),#建筑产权
      (store_script_param, ":building_scene_no", 8),#建筑场景

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (val_mul, ":scene_no", 1000),
      (val_sub, ":ground_type", "itm_zone_none"),
      (val_add, ":ground_type", ":scene_no"),
      (try_begin),
         (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#有建筑
         (try_begin),
            (item_has_property, ":building_no", itp_always_loot),
            (val_add, ":ground_type", 1000000000000),#隐藏建筑
         (try_end),
         (val_sub, ":building_no", "itm_building_begin"),#建筑
         (val_max, ":building_no", 0),
         (val_mul, ":building_no", 10000000),
         (val_add, ":ground_type", ":building_no"),
         (val_sub, ":building_owner_no", "itm_faction_begin"),#产权
         (val_max, ":building_owner_no", 0),
         (val_mul, ":building_owner_no", 1000000000),
         (val_mul, ":building_scene_no", 10000000000000),#建筑场景
         (val_add, ":building_owner_no", ":building_scene_no"),
         (val_add, ":ground_type", ":building_owner_no"),
      (try_end),
      (party_set_slot, ":party_no", ":slot_no", ":ground_type"),
    ]),

#获取下垫面，返回item ID
  ("get_center_zone_ground", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, reg1, ":party_no", ":slot_no"),
      (val_mod, reg1, 100),
      (val_add, reg1, "itm_zone_none"),
    ]),

#获取建筑。
#reg1和reg2返回item ID，如果没有就返回0
  ("get_center_zone_building", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, ":building_no", ":party_no", ":slot_no"),
      (val_div, ":building_no", 10000000),
      (val_mod, ":building_no", 100),
      (store_add, reg1, ":building_no", "itm_building_begin"),
    ]),

#获取建筑所有者（阵营），没有所有者或者没有建筑都返回0
  ("get_center_zone_building_owner", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, ":building_owner_no", ":party_no", ":slot_no"),
      (val_div, ":building_owner_no", 1000000000),
      (val_mod, ":building_owner_no", 1000),
      (store_add, reg1, ":building_owner_no", "itm_faction_begin"),
    ]),

#查看建筑是否能显示
  ("cf_check_building_showed", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, ":building_no", ":party_no", ":slot_no"),
      (val_div, ":building_no", 1000000000000),
      (val_mod, ":building_no", 10),
      (lt, ":building_no", 1),
    ]),

#设置建筑显示
  ("set_building_showed", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, ":building_no", ":party_no", ":slot_no"),
      (store_mod, ":building_no_1", ":building_no", 1000000000000),
      (val_div, ":building_no", 10000000000000),
      (val_mul, ":building_no", 10000000000000),
      (val_add, ":building_no", ":building_no_1"),
      (party_set_slot, ":party_no", ":slot_no", ":building_no"),
    ]),

#设置建筑场景
  ("set_building_scene", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）
      (store_script_param, ":scene_no", 4),

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, ":building_no", ":party_no", ":slot_no"),
      (store_mod, ":building_no_1", ":building_no", 10000000000000),
      (store_mod, ":building_no_2", ":building_no", 100000000000000),
      (val_mul, ":building_no_2", 100000000000000),
      (assign, ":building_no", ":scene_no"),
      (val_mul, ":building_no", 10000000000000),
      (val_add, ":building_no", ":building_no_1"),
      (val_add, ":building_no", ":building_no_2"),
      (party_set_slot, ":party_no", ":slot_no", ":building_no"),
    ]),

#获取建筑场景
#输出reg1为序号
  ("get_building_scene", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）

      (call_script, "script_change_coordinate_to_number", 15, ":axis_x", ":axis_y"),
      (val_add, reg1, slot_center_zone_begin),
      (assign, ":slot_no", reg1),
      (party_get_slot, ":building_no", ":party_no", ":slot_no"),
      (val_div, ":building_no", 10000000000000),
      (val_mod, ":building_no", 10),
      (assign, reg1, ":building_no"),
    ]),


#绘制方格
  ("draw_center_zone", [
      (set_fixed_point_multiplier, 100),
      (store_script_param, ":center_no", 1),#party ID
      (store_script_param, ":rank", 2),#中心点的坐标
      (store_script_param, ":procession", 3),

      (store_mul, ":cur_x", ":rank", 1000),
      (val_sub, ":cur_x", 500),
      (store_mul, ":cur_y", ":procession", 1000),
      (val_sub, ":cur_y", 500),
      (init_position, pos30),
      (position_set_x, pos30, ":cur_x"),
      (position_set_y, pos30, ":cur_y"),#中心点位置
      (copy_position, pos31, pos30),
      (position_move_x, pos31, -375),
      (position_move_y, pos31, -375),

      (try_for_range, ":count_no", 1, 17),
         (troop_set_slot, "trp_temp_array_new_map_1", ":count_no", -1),#清空，用于记录建筑摆放
      (try_end),

      (call_script, "script_get_center_zone_ground", ":center_no", ":rank", ":procession"),#地块类型
      (assign, ":ground_type", reg1),
      (call_script, "script_chess_set_building_position", ":center_no", ":rank", ":procession"),#建筑

      (try_for_range, ":count_no", 1, 17),
         (assign, ":current_zone_no", ":ground_type"),#防止数据被覆盖
         (assign, ":angel_turn_count", 0),
#计算生成物
         (troop_get_slot, ":building_no", "trp_temp_array_new_map_1", ":count_no"),#建筑
         (try_begin),
            (store_div, ":angel_turn_count", ":building_no", 10000),
            (val_mod, ":angel_turn_count", 10),
            (val_mod, ":building_no", 10000),
            (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#有建筑
            (assign, ":current_zone_no", ":building_no"),
         (else_try),
            (gt, ":building_no", 0),#无建筑但是不用摆方格（被占据多格位置的建筑覆盖）
            (assign, ":current_zone_no", "itm_zone_none"),
         (try_end),
         (try_begin),
            (eq, ":current_zone_no", ":ground_type"),#被建筑覆盖了就不用处理扩散了
            (call_script, "script_chess_get_contiguous_zone", ":center_no", ":count_no", ":rank", ":procession"),
            (gt, reg1, 0),
            (assign, ":contiguous_zone_no", reg1),
            (item_get_max_ammo, ":contiguous_priority_count", ":contiguous_zone_no"),#毗连区扩散等级
            (item_get_max_ammo, ":priority_count", ":current_zone_no"),
            (ge, ":contiguous_priority_count", ":priority_count"),#被扩散
            (store_random_in_range, ":count_no_2", 0, 100),
            (gt, ":count_no_2", 50),
            (assign, ":current_zone_no", ":contiguous_zone_no"),
         (try_end),
#生成位置
         (position_set_z_to_ground_level, pos31),
         (position_get_z, ":pos_z", pos31),
         (try_begin),
            (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#建筑
            (val_max,":pos_z", 50),
            (position_set_z, pos31, ":pos_z"),
         (try_end),
         (set_spawn_position, pos31),#确定生成位置
         (val_mul, ":angel_turn_count", 90),
#生成
         (assign, ":instance_no", -1),
         (try_begin),
            (item_get_abundance, ":random_type", ":current_zone_no"),
            (gt, ":random_type", 1),#非空地块
            (gt, ":pos_z", 10),
            (store_random_in_range, ":count_no_2", 1, ":random_type"),
            (spawn_item, ":current_zone_no", ":count_no_2"),
            (assign, ":instance_no", reg0),
            (prop_instance_get_position, pos32, ":instance_no"),
            (position_rotate_z, pos32, ":angel_turn_count"),
            (prop_instance_set_position, ":instance_no", pos32),
         (try_end),
         (troop_set_slot, "trp_temp_array_new_map_1", ":count_no", ":instance_no"),
#移到下一个小区块
         (try_begin),
            (store_mod, ":count_no_3", ":count_no", 4),
            (eq, ":count_no_3", 0),
            (position_move_y, pos31, -750),
            (position_move_x, pos31, 250),
         (else_try),
            (position_move_y, pos31, 250),
         (try_end),
      (try_end),

#绘制城墙连接段
      (try_begin),
         (call_script, "script_cf_chess_set_wall", ":center_no", ":rank", ":procession"),
      (try_end),
    ]),


#获取地块上下左右的类型，输入1上、2右、3下、4左
#reg1输出地块的item ID。若为边缘，则输出-1
  ("zone_get_contiguous_zone", [
      (store_script_param, ":center_no", 1),
      (store_script_param, ":rank", 2),#地块的坐标
      (store_script_param, ":procession", 3),
      (store_script_param, ":count_no", 4),#上下左右

      (try_begin),
         (eq, ":count_no", 1),
         (eq, ":rank", 1),
         (assign, reg1, -1),
      (else_try),
         (eq, ":count_no", 1),      
         (val_sub, ":rank", 1),
         (call_script, "script_get_center_zone_ground", ":center_no", ":rank", ":procession"),
      (else_try),
         (eq, ":count_no", 2),
         (eq, ":procession", 15),
         (assign, reg1, -1),
      (else_try),
         (eq, ":count_no", 2),
         (val_add, ":procession", 1),
         (call_script, "script_get_center_zone_ground", ":center_no", ":rank", ":procession"),
      (else_try),
         (eq, ":count_no", 3),
         (eq, ":rank", 15),
         (assign, reg1, -1),
      (else_try),
         (eq, ":count_no", 3),
         (val_add, ":rank", 1),
         (call_script, "script_get_center_zone_ground", ":center_no", ":rank", ":procession"),
      (else_try),
         (eq, ":count_no", 4),
         (eq, ":procession", 1),
         (assign, reg1, -1),
      (else_try),
         (eq, ":count_no", 4),
         (val_sub, ":procession", 1),
         (call_script, "script_get_center_zone_ground", ":center_no", ":rank", ":procession"),
      (try_end),
    ]),


#判断小方格的毗连区，输入其序号（1到16），返回毗连的地块类型，如果没有就返回-1。四个边角处左上角识别为上，右上角识别为右，由此类推。
#reg1输出地块的item ID，不毗邻就返回-1。
  ("chess_get_contiguous_zone", [
      (store_script_param, ":center_no", 1),
      (store_script_param, ":count_no", 2),#在大方格内的序号
      (store_script_param, ":rank", 3),#地块的坐标
      (store_script_param, ":procession", 4),
      (assign, ":value_no", -1),

      (val_sub, ":count_no", 1),
      (store_mod, ":count_no_2", ":count_no", 4),#列
      (val_div, ":count_no", 4),#行
      (val_add, ":count_no", 1),
      (val_add, ":count_no_2", 1),
      (try_begin),
         (is_between, ":count_no_2", 1, 4),#上面三格
         (eq, ":count_no", 1),
         (call_script, "script_zone_get_contiguous_zone", ":center_no", ":rank", ":procession", 1),
         (assign, ":value_no", reg1),
      (else_try),
         (is_between, ":count_no", 1, 4),#右边三格
         (eq, ":count_no_2", 4),
         (call_script, "script_zone_get_contiguous_zone", ":center_no", ":rank", ":procession", 2),
         (assign, ":value_no", reg1),
      (else_try),
         (is_between, ":count_no_2", 2, 5),#下面三格
         (eq, ":count_no", 4),
         (call_script, "script_zone_get_contiguous_zone", ":center_no", ":rank", ":procession", 3),
         (assign, ":value_no", reg1),
      (else_try),
         (is_between, ":count_no", 2, 5),#左边三格
         (eq, ":count_no_2", 1),
         (call_script, "script_zone_get_contiguous_zone", ":center_no", ":rank", ":procession", 4),
         (assign, ":value_no", reg1),
      (try_end),
      (assign, reg1, ":value_no"),
    ]),


#绘制建筑。有些建筑不止一格，且没什么规律可言，只能用try逐一设置。输入后将数据存储到trp_temp_array_new_map_1内。原则上，棋子不会超过八格，最多各占一半方格，从左上角开始往下数。
#slot的万分位有时还会记录一个取123的值，这个值是旋转角，对应顺时针转90度、180度、270度。
#slot的十万分位设置0或1记录是否是边角位置（对应到abundance记录的不同前缀）
  ("chess_set_building_position", [
      (store_script_param, ":center_no", 1),
      (store_script_param, ":rank", 2),#地块的坐标
      (store_script_param, ":procession", 3),
      (call_script, "script_get_center_zone_building", ":center_no", ":rank", ":procession"),#建筑类型
      (assign, ":building_no", reg1),
      (assign, ":angel_count_no", 0),

      (try_begin),
         (eq, ":building_no", "itm_bridge"),#桥
         (call_script, "script_zone_get_contiguous_zone", ":center_no", ":rank", ":procession", 1),#上方
         (assign, ":upper_zone_type", reg1),
         (call_script, "script_zone_get_contiguous_zone", ":center_no", ":rank", ":procession", 3),#下方
         (assign, ":bellow_zone_type", reg1),
         (try_begin),
            (this_or_next|eq, ":upper_zone_type", "itm_zone_water"),#纵向水流
            (eq, ":bellow_zone_type", "itm_zone_water"),
            (assign, ":angel_count_no", 3),
            (val_mul, ":angel_count_no", 10000),
            (val_add, ":building_no", ":angel_count_no"),
            (troop_set_slot, "trp_temp_array_new_map_1", 9, ":building_no"),
            (troop_set_slot, "trp_temp_array_new_map_1", 5, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 6, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 7, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 8, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 10, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 11, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 12, 1),
         (else_try),
            (eq, ":angel_count_no", 0),
            (troop_set_slot, "trp_temp_array_new_map_1", 2, ":building_no"),
            (troop_set_slot, "trp_temp_array_new_map_1", 3, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 6, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 7, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 10, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 11, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 14, 1),
            (troop_set_slot, "trp_temp_array_new_map_1", 15, 1),
         (try_end),

      (else_try),
         (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#建筑
         (item_get_max_ammo, ":area_count", ":building_no"),
         (eq, ":area_count", 1),
         (troop_set_slot, "trp_temp_array_new_map_1", 6, ":building_no"),
      (else_try),
         (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#建筑
         (item_get_max_ammo, ":area_count", ":building_no"),
         (eq, ":area_count", 4),
         (troop_set_slot, "trp_temp_array_new_map_1", 6, ":building_no"),
         (troop_set_slot, "trp_temp_array_new_map_1", 7, 1),
         (troop_set_slot, "trp_temp_array_new_map_1", 10, 1),
         (troop_set_slot, "trp_temp_array_new_map_1", 11, 1),
      (try_end),
    ]),


#绘制城墙连接段
#从（0，0）开始遍历，每个都只获取自己右、下、右下、右上四处的信息，避免重复。不同类型的城墙不能连接在一起，不过从实际效果上看并无分别。
  ("cf_chess_set_wall", [
      (store_script_param, ":center_no", 1),
      (store_script_param, ":rank", 2),#地块的坐标
      (store_script_param, ":procession", 3),
      (call_script, "script_get_center_zone_building", ":center_no", ":rank", ":procession"),#建筑类型
      (is_between, reg1, "itm_building_begin", "itm_building_end"),
      (item_has_property, reg1, itp_unique),#城墙
      (assign, ":building_no", reg1),
      (store_sub, ":wall_connection_1", ":building_no", "itm_small_wall"),#登记连接件
      (val_mul, ":wall_connection_1", 2),
      (val_add, ":wall_connection_1", "spr_sandbox_small_wall_connection_1"),#横向
      (store_add, ":wall_connection_2", ":wall_connection_1", 1),#斜向

      (try_begin),
         (neq, ":procession", 15),
         (store_add, ":procession_2", ":procession", 1),
         (call_script, "script_get_center_zone_building", ":center_no", ":rank", ":procession_2"),#右方
         (eq, ":building_no", reg1),
         (copy_position, pos31, pos30),
         (position_move_y, pos31, 500),
         (position_set_z_to_ground_level, pos31),
         (position_rotate_z, pos31, 90),
         (set_spawn_position, pos31),#确定生成位置
         (spawn_scene_prop, ":wall_connection_1"),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 5),#隐藏途径上的建筑物。
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 8),
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 9),
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 12),
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
      (try_end),
      (try_begin),
         (neq, ":rank", 15),
         (store_add, ":rank_2", ":rank", 1),
         (call_script, "script_get_center_zone_building", ":center_no", ":rank_2", ":procession"),#下方
         (eq, ":building_no", reg1),
         (copy_position, pos31, pos30),
         (position_move_x, pos31, 500),
         (position_set_z_to_ground_level, pos31),
         (set_spawn_position, pos31),#确定生成位置
         (spawn_scene_prop, ":wall_connection_1"),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 2),#隐藏途径上的建筑物。
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 3),
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 14),
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
         (try_begin),
            (troop_get_slot, ":instance_no", "trp_temp_array_new_map_1", 15),
            (gt, ":instance_no", 0),
            (scene_prop_set_visibility, ":instance_no", 0),
         (try_end),
      (try_end),
      (try_begin),
         (neq, ":rank", 15),
         (neq, ":procession", 15),
         (store_add, ":rank_2", ":rank", 1),
         (store_add, ":procession_2", ":procession", 1),
         (call_script, "script_get_center_zone_building", ":center_no", ":rank_2", ":procession_2"),#右下方
         (eq, ":building_no", reg1),
         (copy_position, pos31, pos30),
         (position_move_x, pos31, 500),
         (position_move_y, pos31, 500),
         (position_set_z_to_ground_level, pos31),
         (position_rotate_z, pos31, 90),
         (set_spawn_position, pos31),#确定生成位置
         (spawn_scene_prop, ":wall_connection_2"),
      (try_end),
      (try_begin),
         (neq, ":rank", 1),
         (neq, ":procession", 15),
         (store_sub, ":rank_2", ":rank", 1),
         (store_add, ":procession_2", ":procession", 1),
         (call_script, "script_get_center_zone_building", ":center_no", ":rank_2", ":procession_2"),#右上方
         (eq, ":building_no", reg1),
         (copy_position, pos31, pos30),
         (position_move_x, pos31, -500),
         (position_move_y, pos31, 500),
         (position_set_z_to_ground_level, pos31),
         (set_spawn_position, pos31),#确定生成位置
         (spawn_scene_prop, ":wall_connection_2"),
      (try_end),
    ]),


#记录任务区域
  ("set_quest_zone", [
      (store_script_param, ":quest_no", 1),
      (store_script_param, ":party_no", 2),
      (store_script_param, ":rank", 3),#地块的坐标
      (store_script_param, ":procession", 4),
      (store_script_param, ":slot_no", 5),#储存至第几个槽（1、2、3）

      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_quest_zone_1),
      (call_script, "script_change_coordinate_to_number", 15, ":rank", ":procession"),
      (val_add, reg1, slot_center_zone_begin),
      (val_mul, ":party_no", 1000),
      (val_add, ":party_no", reg1),
      (quest_set_slot, ":quest_no", ":slot_no", ":party_no"),
    ]),
#清空任务区域
  ("clear_quest_zone", [
      (store_script_param, ":quest_no", 1),
      (store_script_param, ":slot_no", 2),#储存至第几个槽（1、2、3）
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_quest_zone_1),
      (quest_set_slot, ":quest_no", ":slot_no", 0),
    ]),
#获取任务区域，输入任务和槽，获取行储存在reg1，列储存在reg2，center ID储存在reg3
  ("get_quest_zone", [
      (store_script_param, ":quest_no", 1),
      (store_script_param, ":slot_no", 2),#储存至第几个槽（1、2、3）
      (val_sub, ":slot_no", 1),
      (val_add, ":slot_no", slot_quest_zone_1),
      (quest_get_slot, ":party_no", ":quest_no", ":slot_no"),
      (store_mod, reg1, ":party_no", 1000),
      (val_sub, reg1, slot_center_zone_begin),
      (call_script, "script_change_number_to_coordinate", 15, reg1),
      (store_div, reg3, ":party_no", 1000),
    ]),


#记录随机战场的地形分块，储存在其scene slot里，以便后续生成p_campaign_temp时获取。
#因为只需要填入沙盘固有的地形：默认、水体和岩壁，所以只需要输入scene类型、xy坐标、水体或岩壁的itemID，比较简单，不用填建筑等
  ("store_scene_zone", [
      (store_script_param, ":scene_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）
      (store_script_param, ":ground_type", 4),#下垫面类型
      (call_script, "script_change_coordinate_to_number", 15,":axis_x", ":axis_y"),
      (scene_set_slot, ":scene_no", reg1, ":ground_type"), #scene slot几乎没用，直接从0开始
    ]),
#获取随机战场的地形分块
#输入scene、xy，返回地形的item ID，储存进reg1
  ("get_scene_zone", [
      (store_script_param, ":scene_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）
      (call_script, "script_change_coordinate_to_number", 15,":axis_x", ":axis_y"),
      (scene_get_slot, ":ground_type", ":scene_no", reg1), #scene slot几乎没用，直接从0开始
      (assign, reg1, ":ground_type"),
    ]),

#获取随机战场的地形分块
#输入scene、xy，返回地形的item ID，储存进reg1
  ("set_forest_diffusion", [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #y轴的坐标（从左往右，列）
      (store_script_param, ":ground_type", 4),#下垫面类型
      (store_script_param, ":diffusion_value", 5),#扩散强度（还能扩散几次）

      (val_sub, ":diffusion_value", 1),
      (try_begin),
         (store_random_in_range, ":value_no", 0, 3), #概率
         (le, ":value_no", ":diffusion_value"),
         (store_sub, ":cur_x", ":axis_x", 1), #上方区块
         (ge, ":cur_x", 1),
         (assign, ":cur_y", ":axis_y"),
         (call_script, "script_get_center_zone_ground", ":party_no", ":cur_x", ":cur_y"),
         (eq, reg1, "itm_zone_none"), #只有默认才能继续生成，水体、岩壁等基础地形，和已经生成了其他区块包括其他森林的不动
         (call_script, "script_set_center_zone", ":party_no", ":cur_x", ":cur_y", ":ground_type", 0, 0, 0, 0), #生成森林
         (call_script, "script_set_forest_diffusion", ":party_no", ":cur_x", ":cur_y", ":ground_type", ":diffusion_value"), #森林扩散
      (try_end),
      (try_begin),
         (store_random_in_range, ":value_no", 0, 3), #概率
         (le, ":value_no", ":diffusion_value"),
         (store_add, ":cur_x", ":axis_x", 1), #下方区块
         (le, ":cur_x", 15),
         (assign, ":cur_y", ":axis_y"),
         (call_script, "script_get_center_zone_ground", ":party_no", ":cur_x", ":cur_y"),
         (eq, reg1, "itm_zone_none"), #只有默认才能继续生成，水体、岩壁等基础地形，和已经生成了其他区块包括其他森林的不动
         (call_script, "script_set_center_zone", ":party_no", ":cur_x", ":cur_y", ":ground_type", 0, 0, 0, 0), #生成森林
         (call_script, "script_set_forest_diffusion", ":party_no", ":cur_x", ":cur_y", ":ground_type", ":diffusion_value"), #森林扩散
      (try_end),
      (try_begin),
         (store_random_in_range, ":value_no", 0, 3), #概率
         (le, ":value_no", ":diffusion_value"),
         (assign, ":cur_x", ":axis_x"),
         (store_sub, ":cur_y", ":axis_y", 1), #左方区块
         (ge, ":cur_y", 1),
         (call_script, "script_get_center_zone_ground", ":party_no", ":cur_x", ":cur_y"),
         (eq, reg1, "itm_zone_none"), #只有默认才能继续生成，水体、岩壁等基础地形，和已经生成了其他区块包括其他森林的不动
         (call_script, "script_set_center_zone", ":party_no", ":cur_x", ":cur_y", ":ground_type", 0, 0, 0, 0), #生成森林
         (call_script, "script_set_forest_diffusion", ":party_no", ":cur_x", ":cur_y", ":ground_type", ":diffusion_value"), #森林扩散
      (try_end),
      (try_begin),
         (store_random_in_range, ":value_no", 0, 3), #概率
         (le, ":value_no", ":diffusion_value"),
         (assign, ":cur_x", ":axis_x"),
         (store_add, ":cur_y", ":axis_y", 1), #右方区块
         (le, ":cur_y", 15),
         (call_script, "script_get_center_zone_ground", ":party_no", ":cur_x", ":cur_y"),
         (eq, reg1, "itm_zone_none"), #只有默认才能继续生成，水体、岩壁等基础地形，和已经生成了其他区块包括其他森林的不动
         (call_script, "script_set_center_zone", ":party_no", ":cur_x", ":cur_y", ":ground_type", 0, 0, 0, 0), #生成森林
         (call_script, "script_set_forest_diffusion", ":party_no", ":cur_x", ":cur_y", ":ground_type", ":diffusion_value"), #森林扩散
      (try_end),
    ]),


#野外战场
#绘制野外战场，首先输入经过script_get_natural_zone特殊处理的terrain类型（比如在绿洲用的是稀树草原的terrain，经过处理返回的是沙漠），获取使用的沙盘底版，然后再直接获取真实terrain，判断树木长势等，生成一套野外会战的沙盘区块，储存在p_campaign_temp里
#输入1为特殊处理的terrain，2选填，为因为某些特殊目的而指定的底板，如果填0此处就正常随机
#不需要输出，获取的沙盘底板直接存进"$current_scene"里，区块信息也直接存进campaign_temp的slot
  ("draw_random_sandtable", [
      (store_script_param, ":current_terrain_new", 1),
      (store_script_param, ":sandtable_scene_special", 2),
      (party_get_current_terrain, ":current_terrain", "p_main_party"), #获取真实地形

      (assign, ":tree_count", 0), #生成树的多寡
      (assign, ":tree_type", 0), #树的种类
      (try_begin),#获取沙盘
        (this_or_next|eq, ":current_terrain_new", rt_plain), #平原和森林都用平原沙盘
         (eq, ":current_terrain_new", rt_forest), 
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_plain_1", "scn_random_sandtable_mountain_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_forest), #生成在平原上的森林
            (store_random_in_range, ":tree_count", 3, 6), #生成3到5处森林
            (assign, ":tree_type", "itm_zone_forest"), 
         (else_try),
            (store_random_in_range, ":tree_count", 1, 3), #生成1到2处森林
            (assign, ":tree_type", "itm_zone_forest"), 
         (try_end),
      (else_try),
         (eq, ":current_terrain_new", rt_mountain),  #山地、山地森林（归一到山地里）用山地沙盘
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_mountain_1", "scn_random_sandtable_steppe_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_forest), #生成在山地上的森林
            (store_random_in_range, ":tree_count", 4, 7), #生成4到6处森林
            (assign, ":tree_type", "itm_zone_forest"), 
         (else_try),
            (store_random_in_range, ":tree_count", 2, 4), #生成2到3处森林
            (assign, ":tree_type", "itm_zone_forest"), 
         (try_end),
      (else_try),
         (this_or_next|eq, ":current_terrain_new", rt_steppe), #草原和稀树草原都用草原沙盘
         (eq, ":current_terrain_new", rt_steppe_forest), 
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_steppe_1", "scn_random_sandtable_steppe_mountain_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_steppe_forest), #生成在草原上的稀树草原
            (store_random_in_range, ":tree_count", 2, 4), #生成2到3处稀树林
            (assign, ":tree_type", "itm_zone_steppe_forest"), 
         (try_end),
      (else_try),
         (eq, ":current_terrain_new", rt_steppe_mountain), #草原山地、稀树草原山地（归一到草原山地里）用荒山沙盘
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_steppe_mountain_1", "scn_random_sandtable_marsh_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_steppe_forest), #生成在草原上的稀树草原
            (store_random_in_range, ":tree_count", 1, 3), #生成1到2处稀树林
            (assign, ":tree_type", "itm_zone_steppe_forest"), 
         (try_end),
      (else_try),
         (eq, ":current_terrain_new", rt_marsh), #沼泽、沼泽林（归一到沼泽里）用沼泽沙盘
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_marsh_1", "scn_random_sandtable_snow_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_forest), #生成在沼泽上的森林
            (store_random_in_range, ":tree_count", 2, 6), #生成2到5处森林
            (assign, ":tree_type", "itm_zone_forest"), 
         (try_end),
      (else_try),
         (this_or_next|eq, ":current_terrain_new", rt_snow), #雪原和雪林都用雪原沙盘
         (eq, ":current_terrain_new", rt_snow_forest), 
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_snow_1", "scn_random_sandtable_snow_mountain_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_snow_forest), #生成在雪原上的森林
            (store_random_in_range, ":tree_count", 4, 7), #生成4到6处针叶林
            (assign, ":tree_type", "itm_zone_taiga_forest"), 
         (try_end),
      (else_try),
         (eq, ":current_terrain_new", rt_snow_mountain), #雪山、雪山森林（归一到雪山里）用雪山沙盘
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_snow_mountain_1", "scn_random_sandtable_desert_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_snow_forest), #生成在雪原上的森林
            (store_random_in_range, ":tree_count", 5, 8), #生成5到7处针叶林
            (assign, ":tree_type", "itm_zone_taiga_forest"), 
         (try_end),
      (else_try),
         (eq, ":current_terrain_new", rt_desert), #沙漠和绿洲（归一化到沙漠里）都用沙漠沙盘
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_desert_1", "scn_random_sandtable_desert_mountain_1"),
         (try_begin),
            (eq, ":current_terrain",  rt_steppe_forest), #生成在沙漠里的绿洲
            (store_random_in_range, ":tree_count", 1, 3), #生成1到2处绿洲
            (assign, ":tree_type", "itm_zone_oasis"), 
         (try_end),
      (else_try),
         (eq, ":current_terrain_new", rt_desert_mountain), #沙漠和绿洲（归一化到沙漠里）都用戈壁沙盘
         (store_random_in_range, ":sandtable_scene", "scn_random_sandtable_desert_mountain_1", "scn_random_sandtable_end"),
         (try_begin),
            (eq, ":current_terrain",  rt_steppe_forest), #生成在戈壁里的绿洲
            (assign, ":tree_count", 1), #生成1处绿洲
            (assign, ":tree_type", "itm_zone_oasis"), 
         (try_end),
      (try_end),
      (try_begin),
         (gt, ":sandtable_scene_special", 0),
         (assign, ":sandtable_scene", ":sandtable_scene_special"), #指定场景
      (try_end),
      (assign, "$current_scene", ":sandtable_scene"), #定下所用的沙盘底板

      (try_for_range, ":cur_x", 1, 16),
         (try_for_range, ":cur_y", 1, 16),
            (call_script, "script_get_scene_zone", "$current_scene", ":cur_x", ":cur_y"), #获取储存的地形信息，包括水体岩壁等无法被直接获取的
            (assign, ":ground_type", reg1),
            (try_begin),
               (le, ":ground_type", 0), #无地形
               (assign, ":ground_type", "itm_zone_none"), #默认
            (try_end),
            (call_script, "script_set_center_zone", "p_campaign_temp", ":cur_x", ":cur_y", ":ground_type", 0, 0, 0, 0), #初始化（只包括水体岩壁，不包括各种森林）
         (try_end),
      (try_end),

      (assign, ":diffusion_intensity", ":tree_count"), #森林的扩散强度
      (try_for_range, ":cur_x", 1, 16), #生成森林
         (try_for_range, ":cur_y", 1, 16),
            (gt, ":tree_count", 0), #还能够生成森林
            (call_script, "script_get_center_zone_ground", "p_campaign_temp", ":cur_x", ":cur_y"),
            (eq, reg1, "itm_zone_none"), #只有默认才能继续生成，水体、岩壁等基础地形，和已经生成了其他区块包括其他森林的不动
            (call_script, "script_change_coordinate_to_number", 15, ":cur_x", ":cur_y"),
            (assign, ":count_no", reg1),
            (store_random_in_range, ":value_no", ":count_no", 225),
            (val_add, ":count_no", ":tree_count"),
            (eq, ":count_no", ":value_no"),
            (val_sub, ":tree_count", 1), #减少待生成森林量
            (call_script, "script_set_center_zone", "p_campaign_temp", ":cur_x", ":cur_y", ":tree_type", 0, 0, 0, 0), #生成森林
            (call_script, "script_set_forest_diffusion", "p_campaign_temp", ":cur_x", ":cur_y", ":tree_type", ":diffusion_intensity"), #森林扩散
         (try_end),
      (try_end),
    ]),




######################################################战略AI相关######################################################
##
##统计一个兵种（尤其是npc，尤其是领主）能领导的理想部队规模
#输入troop ID，返回reg1
  ("leader_get_ideal_size", [
      (store_script_param_1, ":troop_no"),
      (assign, ":limit", 10),#最少10人 
      (store_skill_level, ":skill", "skl_leadership", ":troop_no"),
      (store_attribute_level, ":charisma", ":troop_no", ca_charisma),
      (val_mul, ":skill", 50),
      (val_mul, ":charisma", 10),
      (val_add, ":limit", ":skill"),#每点统御提高50点
      (val_add, ":limit", ":charisma"),#每点魅力提高10点

      (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),#每5声望提高1点
      (val_max, ":troop_renown", 0),
      (store_div, ":renown_bonus", ":troop_renown", 5),
      (val_add, ":limit", ":renown_bonus"),

      (try_begin),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#是领主
        (store_troop_faction, ":faction_no", ":troop_no"),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),#在某国内
        (try_begin),
          (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),#元帅提高5000
          (val_add, ":limit", 5000),
        (try_end), 
      (try_end),

      (try_begin),#每级派系三个等级都有对应的部队规模加成。如果是该派系的首领，则可以享受到上一级派系中本派系所在位置的加成，并每差一级都要乘以一个0.8的系数。
         (call_script, "script_get_faction_affiliation", ":troop_no", 1), #获取隶属的派系
         (gt, reg1, 0),
         (assign, ":affiliation_faction", reg1),
         (call_script, "script_get_faction_position", ":troop_no", 1), #获取地位
         (assign, ":affiliation_position", reg1),
         (item_get_difficulty, ":grade_no", ":affiliation_faction"),#派系等级
         (assign, ":continue_no", 0),
         (try_begin),
            (eq, ":affiliation_position", 2),#本派系首领
            (call_script, "script_get_faction_affiliation", ":affiliation_faction", 0),#存在上级派系
            (gt, reg1, 0),
            (item_get_difficulty, ":grade_no_2", reg1),#派系等级
            (store_sub, ":continue_no", ":grade_no_2", ":grade_no"),#每差一级乘0.8的系数，比如一个2级势力是国家的支柱，其首领只能享受国家支柱的加成×0.64
            (ge, ":continue_no", 1),
            (assign, ":affiliation_old", ":affiliation_faction"),
            (assign, ":affiliation_faction", reg1),
            (call_script, "script_get_faction_position", ":affiliation_old", 0),#所属派系在上级派系中的地位
            (assign, ":affiliation_position", reg1),
            (item_get_difficulty, ":grade_no", ":affiliation_faction"),#派系等级
         (try_end),
         (try_begin),
            (eq, ":grade_no", 5),#超然势力
            (try_begin),
               (eq, ":affiliation_position", 2),#首领
               (assign, ":limit_add", 100000),
            (else_try),
               (eq, ":affiliation_position", 1),#支柱
               (assign, ":limit_add", 60000),
            (else_try),
               (eq, ":affiliation_position", 0),#普通成员
               (assign, ":limit_add", 42500),
            (try_end),
         (else_try),
            (eq, ":grade_no", 4),#利维坦
            (try_begin),
               (eq, ":affiliation_position", 2),#首领
               (assign, ":limit_add", 34000),
            (else_try),
               (eq, ":affiliation_position", 1),#支柱
               (assign, ":limit_add", 22000),
            (else_try),
               (eq, ":affiliation_position", 0),#普通成员
               (assign, ":limit_add", 10000),
            (try_end),
         (else_try),
            (eq, ":grade_no", 3),#宏观势力
            (try_begin),
               (eq, ":affiliation_position", 2),#首领
               (assign, ":limit_add", 8000),
            (else_try),
               (eq, ":affiliation_position", 1),#支柱
               (assign, ":limit_add", 6000),
            (else_try),
               (eq, ":affiliation_position", 0),#普通成员
               (assign, ":limit_add", 1000),
            (try_end),
         (else_try),
            (eq, ":grade_no", 2),#庞然组织
            (try_begin),
               (eq, ":affiliation_position", 2),#首领
               (assign, ":limit_add", 800),
            (else_try),
               (eq, ":affiliation_position", 1),#支柱
               (assign, ":limit_add", 400),
            (else_try),
               (eq, ":affiliation_position", 0),#普通成员
               (assign, ":limit_add", 200),
            (try_end),
         (else_try),
            (eq, ":grade_no", 1),#基石单位
            (try_begin),
               (eq, ":affiliation_position", 2),#首领
               (assign, ":limit_add", 160),
            (else_try),
               (eq, ":affiliation_position", 1),#支柱
               (assign, ":limit_add", 60),
            (else_try),
               (eq, ":affiliation_position", 0),#普通成员
               (assign, ":limit_add", 20),
            (try_end),
         (try_end),
         (try_for_range, reg2, 0, ":continue_no"),#每差一级乘0.8的系数
            (val_mul, ":limit_add", 8),
            (val_div, ":limit_add", 10),
         (try_end),
         (val_add, ":limit", ":limit_add"),
      (try_end),

      (call_script, "script_get_troop_conscription_mode", ":troop_no"), #征兵制对理想部队规模的修正
      (assign, ":conscription_mode", reg1), #征兵模式
      (assign, ":rate", reg2), #修正
      (try_begin), 
         (neq, ":conscription_mode", rsm_professional), #职业士兵制无影响
         (val_mul, ":limit", ":rate"), 
         (val_div, ":limit", 100), 
      (try_end), 

      (assign, reg1, ":limit"),
    ]),

#输入派系，随机看它能否获取替换部队模板，获取哪个
#输入troop ID，返回reg1
  ("cf_random_get_party_template", [
      (store_script_param_1, ":affliation_faction_no"),
      (try_begin),
         (assign, ":template_no_1",0),
         (assign, ":count_no_1", 0),
         (call_script, "script_cf_get_faction_template", ":affliation_faction_no", 1),
         (assign, ":template_no_1", reg1),
         (assign, ":count_no_1", reg2),
      (try_end),
      (try_begin),
         (assign, ":template_no_2",0),
         (assign, ":count_no_2", 0),
         (call_script, "script_cf_get_faction_template", ":affliation_faction_no", 2),
         (assign, ":template_no_2", reg1),
         (assign, ":count_no_2", reg2),
      (try_end),
      (try_begin),
         (assign, ":template_no_3",0),
         (assign, ":count_no_3", 0),
         (call_script, "script_cf_get_faction_template", ":affliation_faction_no", 3),
         (assign, ":template_no_3", reg1),
         (assign, ":count_no_3", reg2),
      (try_end),
      (store_add, ":count_no", ":count_no_1", ":count_no_2"),
      (val_add, ":count_no", ":count_no_3"),
      (store_random_in_range, ":value_no", 1, 101),
      (le, ":value_no", ":count_no"), #替换为额外征兵模板
      (try_begin),
         (le, ":value_no", ":count_no_1"),
         (assign, ":template_no", ":template_no_1"),
      (else_try),
         (val_sub, ":value_no", ":count_no_1"),
         (le, ":value_no", ":count_no_2"),
         (assign, ":template_no", ":template_no_2"),
      (else_try),
         (val_sub, ":value_no", ":count_no_2"),
         (le, ":value_no", ":count_no_3"),
         (assign, ":template_no", ":template_no_3"),
      (try_end),
      (gt, ":template_no", 0),
      (assign, reg1, ":template_no"),
    ]),

#设置npc征兵模式
#输入npc ID，征兵模式，对理想规模的修正，采用的部队模板，没有就填0
  ("set_troop_conscription_mode", [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":conscription_mode", 2),
      (store_script_param, ":rate", 3),
      (store_script_param, ":template_no", 4),

      (val_mul, ":rate", 10),
      (val_add, ":conscription_mode", ":rate"),
      (val_mul, ":template_no", 10000),
      (val_add, ":conscription_mode", ":template_no"),
      (troop_set_slot, ":troop_no", slot_troop_conscription_mode, ":conscription_mode"),
    ]),

#获取领主征兵模式
#输入npc ID，返回征兵模式reg1，对理想规模的修正reg2，采用的部队模板reg3
  ("get_troop_conscription_mode", [
      (store_script_param, ":troop_no", 1),
      (assign, reg1, 0),
      (assign, reg2, 0),
      (assign, reg3, 0),
      (troop_get_slot, ":conscription_mode", ":troop_no", slot_troop_conscription_mode),
      (store_div, ":template_no", ":conscription_mode", 10),
      (store_mod, reg1, ":conscription_mode", 10),#征兵制
      (store_mod, reg2, ":template_no", 1000), #征兵制对理想规模的修正
      (val_div, ":template_no", 1000),
      (store_mod, reg3, ":template_no", 1000), #部分模式采用的部队模板，比如部落制的部落兵模板
    ]),


#统计部队职能的主要占比，用于会战分兵算法，party_count_members_with_full_health的上位替代
#输入party，返回总能战斗的人数在reg0，最多的职能类型储存在reg1，高等级兵（黄金级级以上，主力部队）中最多的职能储存在reg2，是否有战略力量储存在reg3（有1没有-1）
  ("party_count_members_function",
    [
      (store_script_param_1, ":party_no"),
      (assign, reg0, 0),
      (assign, reg1, -1),
      (assign, reg2, -1),
      (assign, reg3, -1),
      (try_for_range, ":count_no", 0, 100), #清空数据
         (troop_set_slot, "trp_temp_array_a", ":count_no", 0),
         (troop_set_slot, "trp_temp_array_b", ":count_no", 0),
      (try_end),

      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
#         (neq, ":stack_troop", "trp_player"),
         (assign, ":num_fit",0),
         (try_begin),
            (troop_is_hero, ":stack_troop"), #npc
            (store_troop_health, ":troop_hp", ":stack_troop"),
            (ge, ":troop_hp", 50),#50%血以上
            (assign, ":num_fit",1),
         (else_try),
            (neg|troop_is_hero, ":stack_troop"), #小兵
            (party_stack_get_size, ":num_fit", ":party_no", ":i_stack"),
            (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":i_stack"),
            (val_sub, ":num_fit", ":num_wounded"),
            (val_max, ":num_fit", 0),

            (troop_get_slot, ":function_no", ":stack_troop", slot_troop_function),
            (val_sub, ":function_no", "itm_function_combat"), #计算插值，防止slot到几千去
            (troop_get_slot, ":count_no", "trp_temp_array_a", ":function_no"),
            (val_add, ":count_no", ":num_fit"),
            (troop_set_slot, "trp_temp_array_a", ":function_no", ":count_no"),

            (store_character_level, ":level_no", ":stack_troop"),
            (ge, ":level_no", 30), #黄金级及以上
            (troop_get_slot, ":count_no", "trp_temp_array_b", ":function_no"),
            (val_add, ":count_no", ":num_fit"),
            (troop_set_slot, "trp_temp_array_b", ":function_no", ":count_no"),
         (try_end),
         (val_add, reg0, ":num_fit"), #输出总数
      (try_end),

      (assign, ":num_count", 0), #输出数量最多的职能
      (try_for_range, ":function_no", "itm_function_combat", "itm_function_end"),
         (store_sub, ":slot_no", ":function_no", "itm_function_combat"),
         (troop_get_slot, ":count_no", "trp_temp_array_a", ":slot_no"),
         (gt, ":count_no", ":num_count"),
         (assign, ":num_count", ":count_no"),
         (assign, reg1, ":function_no"),
      (try_end),
      (assign, ":num_count", 0), #输出高级兵中数量最多的职能
      (try_for_range, ":function_no", "itm_function_combat", "itm_function_end"),
         (store_sub, ":slot_no", ":function_no", "itm_function_combat"),
         (troop_get_slot, ":count_no", "trp_temp_array_b", ":slot_no"),
         (gt, ":count_no", ":num_count"),
         (assign, ":num_count", ":count_no"),
         (assign, reg2, ":function_no"),
      (try_end),

      (try_begin),
         (troop_get_slot, ":count_no", "trp_temp_array_a", "itm_function_strategic_strength"), #战略力量超过5名
         (ge, ":count_no", 5),
         (assign, reg3, 1),
      (try_end),
  ]),

#统计部队的主要阵营。采用人数×等级进行加权比较。
#输入party，返回权重最高阵营的为reg1，其中fac_slavers的按二分之一算。
  ("party_count_members_faction",
    [
      (store_script_param_1, ":party_no"),
      (assign, reg1, -1),
      (try_for_range, ":count_no", 0, 150), #清空数据
         (troop_set_slot, "trp_temp_array_a", ":count_no", 0),
      (try_end),

      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
         (store_troop_faction, ":faction_no", ":stack_troop"),
         (party_stack_get_size, ":num_fit", ":party_no", ":i_stack"),
         (store_character_level, ":level_no", ":stack_troop"), #获取等级
         (val_mul, ":num_fit", ":level_no"),
         (try_begin),
            (eq, ":faction_no", fac_slavers), #奴隶阵营权重大幅减少，以区分全是奴隶的起义军和奴隶加奴隶主的混编队
            (val_div, ":num_fit", 10),
         (try_end),
         (troop_get_slot, ":count_no", "trp_temp_array_a", ":faction_no"),
         (val_add, ":count_no", ":num_fit"),
         (troop_set_slot, "trp_temp_array_a", ":faction_no", ":count_no"),
      (try_end),

      (assign, ":num_count", 0), #输出权重最高的阵营
      (try_for_range, ":faction_no", "fac_no_faction", "fac_faction_end"),
         (troop_get_slot, ":count_no", "trp_temp_array_a", ":faction_no"),
         (gt, ":count_no", ":num_count"),
         (assign, ":num_count", ":count_no"),
         (assign, reg1, ":faction_no"),
      (try_end),
  ]),


#根据总人数计算编队人数和数量，并生成临时party以待备用
#编队理想人数为总数的平方根乘10，比如1000人时生成三个编队，每个330余人，160000时生成4000人的编队共40个，10000人时生成1000人编队十个。
#输入部队和总人数，输出编队数量
  ("auto_create_detachment",
    [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":total_num", 2),
      (store_script_param, ":team_no", 3), #0中立1玩家方2敌方，默认分边，有些可能会在生成后修改
      (store_script_param, ":mode_no", 4), #模式0是大地图用的，用模板生成新的工具人部队。1是快速战斗用的，套用原有城镇村party。以后在城镇村地图中作战，可能需要把该地从中排除。

      (set_fixed_point_multiplier, 100),
      (store_sqrt, ":detachment_capacity", ":total_num"), 
      (val_add, ":detachment_capacity", 10),
      (store_div, ":detachment_count", ":total_num", ":detachment_capacity"),

      (try_begin),
         (neq, ":mode_no", 1), #大地图使用
         (set_spawn_radius, 0), 
         (try_for_range, reg3, 0, ":detachment_count"), #生成对应数量的工具人party
            (spawn_around_party, "p_main_party", "pt_tool_party"), 
            (assign, ":temp_party_id", reg0), 
            (troop_set_slot, "trp_temp_array_detachment", "$g_total_detachment", ":temp_party_id"), #记录编队
            (disable_party, ":temp_party_id"), 
            (party_clear, ":temp_party_id"), 
            (party_set_slot, ":temp_party_id", slot_tool_party_resource, ":party_no"), #记录编队来源
            (party_set_slot, ":temp_party_id", slot_tool_party_team, ":team_no"), #记录编队是哪方的
            (store_add, reg4, reg3, 1),
            (party_set_name, ":temp_party_id", "@{reg4}"), #准备生成名字
            (val_add, "$g_total_detachment", 1),
         (try_end),
      (else_try),
         (eq, ":mode_no", 1), #快速战斗使用
         (try_for_range, reg3, 0, ":detachment_count"), #找到对应数量的工具人party
            (try_begin),
               (is_between, "$g_quick_battle_encounter_mode", 1, 3), 
               (eq, "$g_quick_battle_encounter_map", "$g_quick_battle_party_used"), #选择城镇村战时，避开已选的那个据点
               (val_add, "$g_quick_battle_party_used", 1),
            (try_end),
            (assign, ":temp_party_id", "$g_quick_battle_party_used"), 
            (troop_set_slot, "trp_temp_array_detachment", "$g_total_detachment", ":temp_party_id"), #记录编队
            (disable_party, ":temp_party_id"), 
            (party_clear, ":temp_party_id"), 
            (party_set_slot, ":temp_party_id", slot_tool_party_resource, ":party_no"), #记录编队来源
            (party_set_slot, ":temp_party_id", slot_tool_party_team, ":team_no"), #记录编队是哪方的
            (store_add, reg4, reg3, 1),
            (party_set_name, ":temp_party_id", "@{reg4}"), #准备生成名字
            (val_add, "$g_total_detachment", 1),
            (val_add, "$g_quick_battle_party_used", 1),
         (try_end),
      (try_end),

      (assign, reg1, ":detachment_count"), #总数已经在遍历过程中增加，不能在外面再加一次
  ]),


#储存阵型所用的编队，输入阵型（item ID）、编队职能（item ID）和权重。其中编队职能所谓slot使用，不过为避免slot太多，按它与起始职能的插值作为slot序号使用
#用于在生成工具人party以后，根据阵型分配编队职能。比如某个阵型可能只有一个指挥，强袭：支援：比炮灰为3：2：1，一共生成了七个部队，于是最后是一指挥三强袭二支援一炮灰的分布。
#所有阵型最多只有一个指挥，填0表示没有，1表示只有一个。
  ("store_formation_function",
    [
      (store_script_param, ":formation_no", 1),
      (store_script_param, ":party_function_no", 2), #所选职能
      (store_script_param, ":power", 3), #权重
      (val_sub, ":party_function_no", "itm_formation_common"),
      (item_set_slot, ":formation_no", ":party_function_no", ":power"),
  ]),
#输入阵型和编队，返回其权重进reg1。注意如果是指挥编队，1表示只有一个，0表示没有。
  ("get_formation_function",
    [
      (store_script_param, ":formation_no", 1),
      (store_script_param, ":party_function_no", 2), #所选职能
      (val_sub, ":party_function_no", "itm_formation_common"),
      (item_get_slot, reg1, ":formation_no", ":party_function_no"),
      (val_max, reg1, 0),
  ]),

#记录每个阵营核心兵种职能的ID和比例，采用数位储存，ID×100＋百分比的比例。存在itm_formation_end减去common的那一位上
#用于获取阵型，比如检测到某部队是普威尔文化，普威尔文化喜好进攻阵型，进攻阵型在这里设置了突击职能的比例至少要40%。然后检测其部队里相应职能的比例，超过即可通过，少于则随机。
#输入阵型的item ID，职能的iem ID，比例的百分数
  ("store_formation_prefer_function",
    [
      (store_script_param, ":formation_no", 1),
      (store_script_param, ":troop_function_no", 2), #喜好的兵种职能
      (store_script_param, ":percent", 3), #比例
      (val_mul, ":troop_function_no", 100),
      (val_add, ":troop_function_no", ":percent"),
      (store_sub, ":slot_no", "itm_formation_common", "itm_formation_common"),
      (item_set_slot, ":formation_no", ":slot_no", ":troop_function_no"),
  ]),
#输入阵型的item ID，获取职能iem ID储存在reg1，比例的百分数储存在reg2
  ("get_formation_prefer_function",
    [
      (store_script_param, ":formation_no", 1),
      (store_sub, ":slot_no", "itm_formation_common", "itm_formation_common"),
      (item_get_slot, ":troop_function_no", ":formation_no", ":slot_no"),
      (store_div, reg1, ":troop_function_no", 100),
      (store_mod, reg2, ":troop_function_no", 100),
  ]),

#储存编队的兵种倾向，用于分兵。编队使用各个兵种的倾向默认是1，少数情况会把某些职能设置为0。一般而言想要保证某种编队都是由某种特定职能编成，将其数值给大即可。
#对于一个职能而言最倾向于去的编队应该填50，如果没有特别倾向于去的，相对会去的一批填30
  ("store_detachment_tendency",
    [
      (store_script_param, ":troop_function_no", 1), #兵种职能itemID。先输入兵种职能再填编队职能，以便在录入数据时把一个兵种摆在一起处理
      (store_script_param, ":detachment_no", 2),
      (store_script_param, ":power", 3), #权重
      (val_sub, ":troop_function_no", "itm_function_combat"),
      (item_set_slot, ":detachment_no", ":troop_function_no", ":power"),
  ]),
#输入编队职能和兵种职能，返回权重reg1
  ("get_detachment_tendency",
    [
      (store_script_param, ":detachment_no", 1),
      (store_script_param, ":troop_function_no", 2), #兵种职能itemID
      (val_sub, ":troop_function_no", "itm_function_combat"),
      (item_get_slot, reg1, ":detachment_no", ":troop_function_no"),
      (val_max, reg1, 0),
  ]),


#自动获取某部队将会选用的阵型
#返回获取阵型的item ID至reg1
  ("auto_choose_formation",
    [
      (store_script_param, ":party_no", 1),

      (party_stack_get_troop_id, ":troop_no", ":party_no", 0), #获取部队阵营，如果第一位是领主或者奥钢级及以上，就跟着他们的阵营来。没有则统计全队阵营。
      (try_begin),
         (this_or_next|troop_slot_eq, ":troop_no", slot_troop_function, "itm_function_hero_agent"), #英雄单位
         (troop_is_hero, ":troop_no"), #npc
         (store_troop_faction, ":faction_no", ":troop_no"),
      (else_try),
         (call_script, "script_party_count_members_faction", ":party_no"),
         (assign, ":faction_no", reg1),
      (try_end),

      (try_begin),
         (assign, ":percent", 0), #职能需求的比例，评判能不能使用阵型的标准
         (try_begin),
            (gt, ":faction_no", 1),
            (faction_get_slot, ":culture_no", ":faction_no", slot_faction_culture), #获取文化
            (gt, ":culture_no", 0),
            (item_get_slot, ":formation_no", ":culture_no",  slot_culture_formation), #获取文化倾向的阵型
            (gt, ":formation_no", 0),
            (neq, ":formation_no", "itm_formation_common"), #不是普通阵型
            (call_script, "script_get_formation_prefer_function", ":formation_no"), #获取阵型倾向的职能和比例
            (assign, ":function_no", reg1),
            (assign, ":percent", reg2),
         (else_try),
            (call_script, "script_party_count_members_function", ":party_no"), #如果没有文化，或者文化没有设置阵型，就获取最多的那个
            (assign, ":function_no", reg1),
            (assign, ":formation_no", -1),
            (try_for_range, ":cur_formation", "itm_formation_common", "itm_formation_end"), #反向获取有什么阵型倾向于使用该职能
               (call_script, "script_get_formation_prefer_function", ":cur_formation"), #获取阵型倾向的职能和比例
               (eq, ":function_no", reg1),
               (assign, ":percent", reg2),
               (assign, ":formation_no", ":cur_formation"),
            (try_end),
         (try_end),
         (is_between, ":formation_no", "itm_formation_common", "itm_formation_end"), #检测需要的信息是否都获取成功
         (is_between, ":function_no", "itm_function_combat", "itm_function_end"),
         (is_between, ":percent", 1, 101),

         (assign, ":function_count", 0),
         (party_get_num_companion_stacks, ":num_stacks",":party_no"), #获取该职能在部队中的数量
         (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
            (troop_slot_eq, ":stack_troop", slot_troop_function, ":function_no"), #是该职能
            (party_stack_get_size, ":num_fit", ":party_no", ":i_stack"),
            (val_add, ":function_count", ":num_fit"),
         (try_end),
         (gt, ":function_count", 0),
         (val_mul, ":function_count", 100),
         (party_get_num_companions, ":total_num", ":party_no"),
         (val_div, ":function_count", ":total_num"), #该职能的百分比

         (assign, ":continue_no", 0),
         (try_begin),
            (ge, ":function_count", ":percent"), #多于需求的百分比，通过
            (assign, ":continue_no", 1),
         (else_try),
            (val_add, ":percent", 1), #不够时，就只有现比例/需求比例的概率通过
            (store_random_in_range, ":function_count_2", 1, ":percent"),
            (ge, ":function_count", ":function_count_2"),
            (assign, ":continue_no", 1),
         (try_end),
         (eq, ":continue_no", 1),

      (else_try),
          (assign, ":formation_no", "itm_formation_common"), #有一项不通过就默认设置为普通阵型
      (try_end),
      (assign, reg1, ":formation_no"),
  ]),


#根据所选阵型和对部队进行分配
#编队理想人数为总数的平方根乘10，比如1000人时生成三个编队，每个330余人，160000时生成4000人的编队共40个，10000人时生成1000人编队十个。
  ("auto_allocate_troop",
    [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":formation_no", 2), #所选阵型
      (store_script_param, ":detachment_count", 3), #该部队的编队总数，不可动。总编队数是"$g_total_detachment"
      (try_for_range, ":slot_no", 0, 30), 
         (troop_set_slot, "trp_temp_array_a", ":slot_no", -1), #清空
      (try_end),

 #分配预先生成好的编队与职能
      (try_begin),
         (call_script, "script_get_formation_function", ":formation_no", "itm_detachment_commander"), #先判断与没有指挥编队，有的话只能有一个
         (gt, reg1, 0),
         (assign, ":detachment_count_limit", "$g_total_detachment"), 
         (try_for_range, ":slot_no", 0, ":detachment_count_limit"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (neg|party_slot_ge, ":temp_party_id", slot_tool_party_function, 1), #未储存编队职能
            (party_set_slot, ":temp_party_id", slot_tool_party_function, "itm_detachment_commander"), #储存
            (party_set_name, ":temp_party_id", "@指 挥 部 队 "), #设置名字
            (assign, ":detachment_count_limit", 0), #结束遍历
         (try_end),
      (try_end),

      (assign, ":count_num", 0), #获取权重计算的分母，即统计目前选用的阵型会生成哪些职能的编队
      (try_for_range, ":detachment_function_no", "itm_detachment_common", "itm_detachment_end"),
         (neq, ":detachment_function_no", "itm_detachment_commander"), #排除指挥编队
         (call_script, "script_get_formation_function", ":formation_no", ":detachment_function_no"),
         (assign, ":power", reg1),
         (val_add, ":count_num", ":power"),
      (try_end),

      (assign, ":detachment_count_used", 0),
      (try_for_range, ":detachment_function_no", "itm_detachment_common", "itm_detachment_end"),
         (neq, ":detachment_function_no", "itm_detachment_commander"), #排除指挥编队
         (call_script, "script_get_formation_function", ":formation_no", ":detachment_function_no"),
         (assign, ":power", reg1),
         (store_mul, ":cur_detachment_count", ":detachment_count", ":power"), #当前职能编队的数量（先向下取整，之后再分配剩余编队）
         (val_mul, ":cur_detachment_count", 1000),
         (val_div, ":cur_detachment_count", ":count_num"),
         (store_div, ":cur_detachment_count_1", ":cur_detachment_count", 1000),

         (val_add, ":detachment_count_used", ":cur_detachment_count_1"), #统计已使用的编队
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), 
            (gt, ":cur_detachment_count_1", 0),
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (neg|party_slot_ge, ":temp_party_id", slot_tool_party_function, 1), #未储存编队职能
            (party_set_slot, ":temp_party_id", slot_tool_party_function, ":detachment_function_no"), #储存
            (str_store_party_name, s1, ":temp_party_id"),
            (str_store_item_name, s2, ":detachment_function_no"), 
            (party_set_name, ":temp_party_id", "@第 {s1}{s2}团 "), #设置名字
            (val_sub, ":cur_detachment_count_1", 1), 
         (try_end),
         (val_mod, ":cur_detachment_count", 1000),
         (store_sub, ":slot_no", ":detachment_function_no", "itm_detachment_common"), #减一下避免slot存到几千去
         (troop_set_slot, "trp_temp_array_a", ":slot_no", ":cur_detachment_count"), #储存余数，用于后续分配剩余的编队
      (try_end),

      (store_sub, ":detachment_count_remain", ":detachment_count", ":detachment_count_used"), #剩余未分配编队
      (try_for_range, ":slot_no", 0, ":detachment_count_remain"), #每个未分配职能的编队，都要找一遍当前最大的余数对应的职能
         (assign, ":max_detachment_function_no", -1),
         (assign, ":max_detachment_count", 0),
         (try_for_range, ":detachment_function_no", "itm_detachment_common", "itm_detachment_end"),
            (neq, ":detachment_function_no", "itm_detachment_commander"), #排除指挥编队
            (store_sub, ":slot_no", ":detachment_function_no", "itm_detachment_common"), #减一下避免slot存到几千去
            (troop_get_slot, ":cur_detachment_count", "trp_temp_array_a", ":slot_no"), #获取余数，从余数最大的那个往下分配剩余编队
            (lt, ":max_detachment_count", ":cur_detachment_count"),
            (assign, ":max_detachment_count", ":cur_detachment_count"),
            (assign, ":max_detachment_function_no", ":detachment_function_no"), #获取从上往下数第一个余数最大的职能，分配给它一个编队
         (try_end),

         (troop_set_slot, "trp_temp_array_a", ":max_detachment_function_no", -1), #清空余数最大的一项，下轮找第二大的
         (assign, ":detachment_count_limit", "$g_total_detachment"), 
         (try_for_range, ":slot_no", 0, ":detachment_count_limit"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (neg|party_slot_ge, ":temp_party_id", slot_tool_party_function, 1), #未储存编队职能
            (party_set_slot, ":temp_party_id", slot_tool_party_function, ":max_detachment_function_no"), #储存
            (str_store_party_name, s1, ":temp_party_id"),
            (str_store_item_name, s2, ":max_detachment_function_no"), 
            (party_set_name, ":temp_party_id", "@第 {s1}{s2}团 "), #设置名字
            (assign, ":detachment_count_limit", 0), #结束遍历
         (try_end),
      (try_end),

 #分兵，向编队中填充士兵
      (try_for_range, ":slot_no", 0, 200), 
         (troop_set_slot, "trp_temp_array_a", ":slot_no", -1), #清空
      (try_end),
      (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
      (try_for_range, ":target_stack", 0, ":num_stacks"), 
         (party_stack_get_troop_id, ":stack_troop", ":party_no", ":target_stack"),
         (troop_is_hero, ":stack_troop"),#英雄
         (call_script, "script_auto_allocate_hero", ":stack_troop", ":party_no", ":target_stack", ":formation_no"), #分配NPC
         (ge, reg1, 0),
         (party_add_members, reg1, ":stack_troop", 1), #将领队加入指挥编队，未找到默认加入第一个编队

      (else_try),
         (neg|troop_is_hero, ":stack_troop"),#一般兵
         (party_stack_get_size, ":troop_num", ":party_no", ":target_stack"), 
         (troop_get_slot, ":function_no", ":stack_troop", slot_troop_function),
         (val_max, ":function_no", "itm_function_combat"), #不填就默认是格斗

         (assign, ":count_num", 0), #获取分母，即统计属于该部队的所有编队，对于该职能兵种的吸引力之和
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (party_get_slot, ":detachment_function_no", ":temp_party_id", slot_tool_party_function), #获取上面记录的编队职能
            (call_script, "script_get_detachment_tendency", ":detachment_function_no", ":function_no"), #获取该编队的职能，对于该职能兵种的权重或者说吸引力
            (assign, ":power", reg1),
            (val_add, ":count_num", ":power"),
         (try_end),

         (assign, ":troop_num_used", 0),
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), #遍历的是已经划分好职能的编队
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (party_get_slot, ":detachment_function_no", ":temp_party_id", slot_tool_party_function), #获取上面记录的编队职能
            (call_script, "script_get_detachment_tendency", ":detachment_function_no", ":function_no"), #获取该编队的职能，对于该职能兵种的权重或者说吸引力
            (gt, ":power", 0),
            (assign, ":power", reg1),

            (store_mul, ":cur_troop_num", ":troop_num", ":power"), #当前职能编队的数量（先向下取整，之后再分配剩余编队）
            (val_mul, ":cur_troop_num", 1000),
            (val_div, ":cur_troop_num", ":count_num"),
            (store_div, ":cur_troop_num_1", ":cur_troop_num", 1000),
            (party_add_members, ":temp_party_id", ":stack_troop", ":cur_troop_num_1"), #向该编队初步加入部分该兵种
            (val_add, ":troop_num_used", ":cur_troop_num_1"), #统计已分配的兵种
            (val_mod, ":cur_troop_num", 1000),
            (troop_set_slot, "trp_temp_array_a", ":slot_no", ":cur_troop_num"), #储存余数，用于后续分配剩余的该兵种
         (try_end),

         (store_sub, ":troop_num_remain", ":troop_num", ":troop_num_used"), #剩余未分配的该兵种
         (try_for_range, reg5, 0, ":troop_num_remain"), #每个未分配编队的该兵种，都要找一遍当前最大的余数对应的编队
            (assign, ":max_detachment_no", -1),
            (assign, ":max_troop_num", 0),
            (try_for_range, ":slot_no", 0, "$g_total_detachment"), #循一遍所有编队，找到余数最大的那个
               (troop_get_slot, ":cur_troop_num", "trp_temp_array_a", ":slot_no"), #获取余数，从余数最大的那个往下分配剩余兵种
               (lt, ":max_troop_num", ":cur_troop_num"),
               (assign, ":max_troop_num", ":cur_troop_num"),
               (assign, ":max_detachment_no", ":slot_no"), #获取从前往后数第一个余数最大的编队，分配给它一个该兵种
            (try_end),
            (troop_set_slot, "trp_temp_array_a", ":max_detachment_no", -1), #清空余数最大的一项，下轮找第二大的
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":max_detachment_no"), 
            (party_add_members, ":temp_party_id", ":stack_troop", 1), #向该编队一个该兵种
         (try_end),
      (try_end),
  ]),


##输入npc、部队、stack序号和阵型，将它放入最适合的编队中
#返回编队储存在reg1中，留作备用
  ("auto_allocate_hero",
    [
      (store_script_param, ":troop_no", 1), #npc单位
      (store_script_param, ":party_no", 2), #原部队ID
      (store_script_param, ":stack_no", 3), #堆序号
      (store_script_param, ":formation_no", 4), #阵型

      (assign, ":target_party", -1), #清空
      (try_begin),
         (troop_get_slot, ":party_leaded_no", ":troop_no", slot_troop_leaded_party), #正在带领该部队，比如领主，加入指挥编队或者第一个编队
         (this_or_next|eq, ":party_leaded_no", ":party_no"),
         (eq, ":stack_no", 0), #未设置slot的第一位，比如野怪部队的npc
         (assign, ":target_party", -1), 
         (try_for_range_backwards, ":slot_no", 0, "$g_total_detachment"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (assign, ":target_party", ":temp_party_id"), #没有指挥编队就退而求其次，找隶属于该部队的第一个编队
            (party_slot_eq, ":temp_party_id", slot_tool_party_function, "itm_detachment_commander"), #指挥编队
            (assign, ":target_party", ":temp_party_id"), 
         (try_end),
      (else_try),
         (assign, ":target_detachment", -1), 
         (assign, ":power_count", -1), #计算权重，找到当前阵型拥有的编队中，权重最大的那个
         (try_for_range, ":detachment_function_no", "itm_detachment_common", "itm_detachment_end"), 
            (call_script, "script_get_formation_function", ":formation_no", ":detachment_function_no"), #有该编队
            (gt, reg1, 0),
            (try_begin),
            (else_try),
               (eq, ":detachment_function_no", "itm_detachment_monster"), #敌意单位：和一般兵一样由兵种职能决定
               (troop_get_slot, ":function_no", ":troop_no", slot_troop_function),
               (eq, ":function_no", "itm_function_monster"),
               (assign, ":cur_power", 100),
            (else_try),
               (this_or_next|eq, ":detachment_function_no", "itm_detachment_strike"), #强袭编队：受伤不能加入
               (eq, ":detachment_function_no", "itm_detachment_support"), #支援编队：受伤不能加入
               (assign, ":cur_power", 10),
               (try_begin),
                  (troop_is_wounded, ":troop_no"), #受伤不能加入
                  (val_sub, ":cur_power", 100),
               (try_end),
               (try_begin),
                  (troop_get_inventory_slot, ":item_get", ":troop_no", 8), #坐骑槽
                  (gt, ":item_get", 0), #骑马
                  (val_add, ":cur_power", 10),
               (try_end),
            (else_try),
               (eq, ":detachment_function_no", "itm_detachment_common"), #普通编队：不受技能影响
               (assign, ":cur_power", 20),
            (else_try),
               (assign, ":cur_power", 10), 
            (try_end),

            (try_for_range, ":slot_no", 1, 4),
               (item_get_slot, ":skill_no", ":detachment_function_no", ":slot_no"), #主要影响的技能
               (ge, ":skill_no", 0),
               (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
               (val_add, ":cur_power", ":skill_level"),
            (try_end),
            (try_for_range, ":slot_no", 4, 7),
               (item_get_slot, ":skill_no", ":detachment_function_no", ":slot_no"), #次要影响的技能
               (ge, ":skill_no", 0),
               (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
               (val_div, ":skill_level", 2),
               (val_add, ":cur_power", ":skill_level"),
            (try_end),
            (gt, ":cur_power", ":power_count"),
            (assign, ":power_count", ":cur_power"), #当前最大权重
            (assign, ":target_detachment", ":detachment_function_no"), 
         (try_end),
         (gt, ":target_detachment", 0), #已获取到目标编队职能

         (assign, ":target_party", -1), 
         (assign, ":npc_count", 1000), #寻找同职能编队中npc数量最少的那个
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (party_slot_eq, ":temp_party_id", slot_tool_party_function, ":target_detachment"), #目标编队
            (call_script, "script_party_count_hero_num", ":temp_party_id"), #统计该部队npc数量
            (lt, reg1, ":npc_count"), #从前往后发
            (assign, ":npc_count", reg1), 
            (assign, ":target_party", ":temp_party_id"), 
         (try_end),
      (try_end),
      (assign, reg1, ":target_party"),
  ]),


##输入原部队party ID，根据职能设置其下属编队的初始姿态。第二个参数用于特殊模式会战中统一设置的行为，比如追逃模式被追一方无论是何编队全部设为溃逃
  ("set_detachment_attitude",
    [
      (store_script_param, ":party_no", 1), #原部队ID
      (store_script_param, ":special_attitude_no", 2), #特殊的姿态预设

      (try_begin),
         (lt, ":special_attitude_no", 0), #无预设，根据职能自动录入
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (party_get_slot, ":function_no", ":temp_party_id", slot_tool_party_function), #目标编队
            (eq, ":function_no", "itm_detachment_common"), #普通编队预设为冲锋
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_charge), 
         (else_try),
            (eq, ":function_no", "itm_detachment_strike"), #突击编队预设为冲锋
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_charge), 
         (else_try),
            (eq, ":function_no", "itm_detachment_support"), #支援编队预设为无姿态
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_none), 
         (else_try),
            (eq, ":function_no", "itm_detachment_firepower"), #火力编队预设为牵制
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_harass), 
         (else_try),
            (eq, ":function_no", "itm_detachment_defend"), #固守编队预设为守卫
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_guard), 
         (else_try),
            (eq, ":function_no", "itm_detachment_commander"), #指挥编队预设为无姿态
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_none), 
         (else_try),
            (eq, ":function_no", "itm_detachment_special_force"), #特种编队预设为无姿态
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_none), 
         (else_try),
            (eq, ":function_no", "itm_detachment_strategic"), #战略编队预设为自我保护
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_selfprotect), 
         (else_try),
            (eq, ":function_no", "itm_detachment_cannon_fodder"), #炮灰编队预设为冲锋
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_charge), 
         (else_try),
            (eq, ":function_no", "itm_detachment_sapper"), #工兵编队预设为回避
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_evade), 
         (else_try),
            (eq, ":function_no", "itm_detachment_logistic"), #后勤编队预设为回避
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_evade), 
         (else_try),
            (eq, ":function_no", "itm_detachment_monster"), #敌意单位预设为冲锋
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ai_attitude_charge), 
         (try_end),

      (else_try),
         (ge, ":special_attitude_no", 0), #有特殊预设姿态
         (try_for_range, ":slot_no", 0, "$g_total_detachment"), 
            (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
            (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
            (party_get_slot, ":function_no", ":temp_party_id", slot_tool_party_function), #目标编队
            (party_set_slot, ":temp_party_id", slot_tool_party_attitude, ":special_attitude_no"), 
         (try_end),
      (try_end),
  ]),


#指定一个位置，在沙盘中寻找一块距其最近的指定大小的方形平地，保证其中不被水体和岩壁分割。
#输入战场party、起始点编号x、y，需要找到的平地尺寸x和y。起始点在获取时将会是中心点
#返回找到的位置（reg1，reg2），注意这个点是区域左上角的点，即最接近（0，0）的那个。如果找不到，就返回-1
  ("sandtable_find_area",
    [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":axis_x", 2), #指定起点x轴的坐标（从上往下，行）
      (store_script_param, ":axis_y", 3), #指定起点y轴的坐标（从左往右，列）
      (store_script_param, ":rank", 4), #需要平地的行数（x）
      (store_script_param, ":procession", 5), #需要平底的列数（y）

      (assign, ":get_x", -1),
      (assign, ":get_y", -1),
      (assign, ":distance_count", 114514), #距离的平方，用于寻找离给定点最近的区域。判断的是该区域离给定点最近的那个点的距离。
      (try_for_range, ":cur_x", 1, 16),
         (try_for_range, ":cur_y", 1, 16),
            (call_script, "script_get_center_zone_ground", ":party_no", ":cur_x", ":cur_y"),
            (neq, reg1, "itm_zone_water"), 
            (neq, reg1, "itm_zone_cliff"), #排除本身就是水体或岩壁的，减少运算
            (store_add, ":count_x", ":cur_x", ":rank"), 
            (le, ":count_x", 15), 
            (val_add, ":count_x", 1), 
            (store_add, ":count_y", ":cur_y", ":procession"), 
            (le, ":count_y", 15), 
            (val_add, ":count_y", 1), 
            (assign, ":count_no", 0),
            (assign, ":cur_distance_count", 1919810), 
            (try_for_range, ":slot_x", ":cur_x", ":count_x"),
               (try_for_range, ":slot_y", ":cur_y", ":count_y"),
                  (call_script, "script_get_center_zone_ground", ":party_no", ":slot_x", ":slot_y"),
                  (this_or_next|eq, reg1, "itm_zone_water"), 
                  (eq, reg1, "itm_zone_cliff"), #水体或岩壁
                  (assign, ":count_no", 1),
               (else_try),
                  (store_sub, ":distance_x", ":slot_x", ":axis_x"), 
                  (store_sub, ":distance_y", ":slot_y", ":axis_y"), 
                  (val_mul, ":distance_x", ":distance_x"),
                  (val_mul, ":distance_y", ":distance_y"),
                  (val_add, ":distance_x", ":distance_y"),
                  (lt, ":distance_x", ":cur_distance_count"),
                  (assign, ":cur_distance_count", ":distance_x"), #不是水体或岩壁的点，离起始点的距离。找最近的点
               (try_end),
            (try_end),
            (neq, ":count_no", 1), #确保范围内没有水体或岩壁这些不能放部队的
            (le, ":cur_distance_count", 50), #控制距离，不能随机得太远，如果是直线就是7格，如果是斜对角就是（5，5）的差异
            (gt, ":distance_count", ":cur_distance_count"),
            (assign, ":distance_count", ":cur_distance_count"), #获取离给定点最近的那个
            (assign, ":get_x", ":cur_x"), #获取到的区域的左上角点
            (assign, ":get_y", ":cur_y"),
         (try_end),
      (try_end),
      (assign, reg1, ":get_x"),
      (assign, reg2, ":get_y"),
  ]),


#在会战沙盘上刷出编队，暂时先不管后续阵型展开（因为阵型要对着敌人展开，得等所有编队刷出完毕）。
#输入部队ID，阵型item ID，沙盘底板的部队ID和编队总数，用于遍历
  ("auto_spawn_detachment",
    [
      (store_script_param, ":party_no", 1), #来源party
      (store_script_param, ":formation_no", 2), #所选阵型
      (store_script_param, ":area_no", 3), #沙盘所用的部队，随机野战就是p_campaign_temp

      (party_get_slot, ":team_no", ":party_no", slot_tool_party_team), #设置起始点，由此点开始向外寻找适合刷新的点。要求：能立足，已有部队不多
      (try_begin),
         (eq, ":formation_no", "itm_formation_station"), #驻扎阵型的刷在场中央
         (assign, ":count_x", 8),
      (else_try),
         (eq, ":team_no", 1), #友方在靠近屏幕一侧
         (assign, ":count_x", 11),
      (else_try),
         (eq, ":team_no", 2), #敌方在对面
         (assign, ":count_x", 5),
      (try_end),
      (assign, ":count_y", 8),

      (try_for_range, ":slot_no", 0, "$g_total_detachment"), #遍历编队，刷出在初始位置
         (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
         (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
         (party_set_slot, ":temp_party_id", slot_tool_party_position_x, ":count_x"),#设置位置
         (party_set_slot, ":temp_party_id", slot_tool_party_position_y, ":count_y"),
         (try_begin),
            (party_slot_eq, ":temp_party_id", slot_tool_party_function, "itm_detachment_cannon_fodder"), #炮灰编队初始组织力只有200
            (party_set_slot, ":temp_party_id", slot_tool_party_cohesion, 200), 
         (else_try),
            (party_set_slot, ":temp_party_id", slot_tool_party_cohesion, 300), #设置组织力，初始默认300
         (try_end), 
         (try_begin),
            (party_slot_eq, ":temp_party_id", slot_tool_party_function, "itm_detachment_commander"), #指挥编队开局设置启动摆阵
            (party_set_slot, ":temp_party_id", slot_tool_party_rally, ":formation_no"), 
         (try_end), 
      (try_end),
  ]),


#绘制编队，输入编队partyID，坐标xy
  ("draw_detachment", [
      (set_fixed_point_multiplier, 100),
      (store_script_param, ":detachment_no", 1),#party ID
      (store_script_param, ":rank", 2), #行，从上往下
      (store_script_param, ":procession", 3), #列，从左往右

      (store_mul, ":cur_x", ":rank", 1000),
      (val_sub, ":cur_x", 500),
      (store_mul, ":cur_y", ":procession", 1000),
      (val_sub, ":cur_y", 500),
      (init_position, pos30),
      (position_set_x, pos30, ":cur_x"),
      (position_set_y, pos30, ":cur_y"),#中心点位置
      (copy_position, pos31, pos30),
      (position_move_x, pos31, -375),
      (position_move_y, pos31, -375),
      (position_set_z_to_ground_level, pos31),

      (party_get_slot, ":function_no", ":detachment_no", slot_tool_party_function),
      (set_spawn_position, pos31),#确定生成位置
      (spawn_item, ":function_no"),
      (assign, ":cur_instance", reg0),
      (party_set_slot, ":detachment_no", slot_tool_party_prop, ":cur_instance"), #记录编队的模型，以便后续移动
#      (prop_instance_deform_in_cycle_loop, ":cur_instance", 0, 140, 300),
    ]),

#绘制编队在沙盘里的页面，每个都是一个container
  ("draw_detachment_window", [
      (set_fixed_point_multiplier, 1000),
      (store_script_param, ":detachment_no", 1),#编队的party ID
      (store_script_param, ":cur_x", 2), #overlay坐标
      (store_script_param, ":cur_y", 3), 
      (store_mul, ":slot_set_no", ":detachment_no", 10), #用于数位储存overlay ID

      (create_image_button_overlay, reg1, "mesh_character_choose_window", "mesh_character_choose_window_lighten"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 428),
      (position_set_y, pos1, 428),
      (overlay_set_size, reg1, pos1),
      (overlay_set_additional_render_height, reg1, -5), #模型层数为2
      (party_get_slot, ":team_no", ":detachment_no", slot_tool_party_team), #敌我方
      (try_begin),
         (eq, ":team_no", 3), #非人
         (overlay_set_color, reg1, 0x9932CC),
      (else_try),
         (eq, ":team_no", 2), #敌方
         (overlay_set_color, reg1, 0xB22222),
      (else_try),
         (eq, ":team_no", 1), #友方
         (overlay_set_color, reg1, 0x87CEFA),
      (try_end),
      (troop_set_slot, "trp_temp_array_new_map_3", reg1, ":slot_set_no"), #最基础的框

      (val_add, ":cur_x", 25),
      (val_add, ":cur_y", 135),
      (str_store_party_name, s1, ":detachment_no"), #编队名字
      (create_text_overlay, reg1, "@{s1}"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),

      (val_add, ":cur_x", 140),
      (val_sub, ":cur_y", 50),
      (party_get_num_companion_stacks, ":value_no", ":detachment_no"),
      (try_begin),
         (gt, ":value_no", 0), #非空白编队（一般不会出现，以防万一）
         (party_stack_get_troop_id, ":stack_troop", ":detachment_no", 0),
         (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_troop_note_mesh", ":stack_troop"),
         (set_fixed_point_multiplier, 1000),
      (else_try),
         (create_text_overlay, reg1, "@ "),
      (try_end),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 240),
      (position_set_y, pos1, 240),
      (overlay_set_size, reg1, pos1),
      (val_add, ":slot_set_no", 2),
      (troop_set_slot, "trp_temp_array_new_map_3", reg1, ":slot_set_no"), #领队头像

      (val_sub, ":cur_x", 140),
      (val_add, ":cur_y", 35),
      (party_get_slot, ":function_no", ":detachment_no", slot_tool_party_function), 
      (str_store_item_name, s1, ":function_no"), 
      (create_text_overlay, reg1, "@职 能 : {s1}"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 600),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),

      (val_sub, ":cur_y", 15),
      (call_script, "script_party_count_members_function", ":detachment_no"), 
      (party_get_num_companions, reg1, ":detachment_no"),
      (try_begin),
         (lt, reg1, 300), #少于300，不占规模，不会增加由于同一区块编队太多造成的减益
         (str_store_string, s1, "@不 占 规 模 "),
      (else_try),
         (store_div, reg2, reg1, 2000), #编队人数太多，再计算拥挤程度时会等效于多个编队，2000一算，不少于1
         (val_max, reg2, 1),
         (str_store_string, s1, "@{reg2}规 模 "),
      (try_end),
      (create_text_overlay, reg1, "@兵 力 ： {reg0}/ {reg1}({s1}) "),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 600),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),

      (val_sub, ":cur_y", 15),
      (party_get_slot, reg2, ":detachment_no", slot_tool_party_cohesion), #组织力
      (try_begin),
         (ge, reg2, 150), 
         (str_store_string, s1, "@充 沛 "),
      (else_try),
         (ge, reg2, 50), 
         (str_store_string, s1, "@短 缺 "),
      (else_try),
         (str_store_string, s1, "@即 将 崩 溃 "),
      (try_end),
      (create_text_overlay, reg1, "@组 织 力 : {reg2}({s1}) "),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 600),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),

      (val_sub, ":cur_y", 15),
      (party_get_slot, ":party_no", ":detachment_no", slot_tool_party_resource), 
      (str_store_party_name, s1, ":party_no"), 
      (create_text_overlay, reg1, "@所 属 : {s1}"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 600),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),

      (val_sub, ":cur_y", 15),
      (party_get_slot, ":attitude_no", ":detachment_no", slot_tool_party_attitude), 
      (val_add, ":attitude_no", "str_attitude_none"),
      (str_store_string, s1, ":attitude_no"), 
      (create_text_overlay, reg1, "@行 为 : {s1}"),
      (position_set_x, pos1, ":cur_x"),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg1, pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 600),
      (overlay_set_size, reg1, pos1),
      (overlay_set_color, reg1, 0xFFFFFF),
    ]),



##新增

#预设用于摆阵的权重，具体操作为获取输入部队的指挥编队，看是否存在，并获取slot_tool_party_rally中储存的阵型。然后，获取敌方朝向，将指挥编队周围位置全部记下一个权重，用于沙盘AI中引导其他编队进入阵型位置。
#记录权重时不需要考虑地形，因为权重是扩散的，如果被地形阻隔，会自动朝其他位置扩散。
  ("auto_create_formation", [
      (store_script_param, ":party_no", 1), #原部队
      (assign, ":commander_detachment_no", -1),
      (try_for_range, ":slot_no", 0, "$g_total_detachment"), #寻找指挥编队
         (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
         (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
         (party_slot_eq, ":temp_party_id", slot_tool_party_function, "itm_detachment_commander"), #指挥编队
         (assign, ":commander_detachment_no", ":temp_party_id"), 
      (try_end),

      (try_begin),
         (ge, ":commander_detachment_no", 0), #已找到
         (party_get_slot, ":formation_no", ":commander_detachment_no", slot_tool_party_rally), #获取阵型
         (gt, ":formation_no", 0), #已激活阵型
         (neq, ":formation_no", "itm_formation_common"), #普通和驻扎不用处理
         (neq, ":formation_no", "itm_formation_station"), 
         (party_get_slot, ":cur_x", ":commander_detachment_no", slot_tool_party_position_x),#获取指挥部队位置，也是判断敌方方向、展开阵型的基点
         (party_get_slot, ":cur_y", ":commander_detachment_no", slot_tool_party_position_y),
         (party_get_slot, ":team_no", ":commander_detachment_no", slot_tool_party_team), #获取阵营

         (assign, ":enemy_power_count_old", 0), #敌对力量在指挥编队位置的计分
         (try_for_range, ":count_no", 0, 4),
            (call_script, "script_campaign_caculate_team_power",  ":cur_x",  ":cur_y", ":count_no", ":commander_detachment_no"), #指挥编队位置上的计分
            (eq, ":team_no", 1), #1军检测2军＋非人
            (this_or_next|eq, ":count_no", 2),
            (eq, ":count_no", 3),
            (val_add, ":enemy_power_count_old", reg1),
         (else_try),
            (eq, ":team_no", 2), #2军检测1军＋非人
            (this_or_next|eq, ":count_no", 1),
            (eq, ":count_no", 3),
            (val_add, ":enemy_power_count_old", reg1),
         (try_end),

         (assign, ":vector_x", 0), #指示敌方方向的单位向量（模长为1）
         (assign, ":vector_y", 0), 
         (assign, ":enemy_power_count_new_max", 0), #用于寻找敌方评分最高的方向
         (try_for_range, ":vector_no", 0, 4), #检测上、下、左、右的点，获取比现位置敌方评分更高的点，作为认为的敌方方向
            (try_begin),
               (eq, ":vector_no", 0), #上
               (assign, ":count_x", ":cur_x"),
               (store_sub, ":count_y", ":cur_y", 1),
            (else_try),
               (eq, ":vector_no", 1), #下
               (assign, ":count_x", ":cur_x"),
               (store_add, ":count_y", ":cur_y", 1), 
            (else_try),
               (eq, ":vector_no", 2), #左
               (store_sub, ":count_x", ":cur_x", 1),
               (assign, ":count_y", ":cur_y"),
            (else_try),
               (eq, ":vector_no", 3), #右
               (store_add, ":count_x", ":cur_x", 1),
               (assign, ":count_y", ":cur_y"),
            (try_end),
            (is_between, ":count_x", 1, 16), #没超出棋盘范围
            (is_between, ":count_y", 1, 16),

            (assign, ":enemy_power_count_new", 0), #敌对力量在新位置的计分
            (try_for_range, ":count_no", 0, 4), 
               (call_script, "script_campaign_caculate_team_power",  ":count_x",  ":count_y", ":count_no", ":commander_detachment_no"), #新位置上的计分
               (eq, ":team_no", 1), #1军检测2军＋非人
               (this_or_next|eq, ":count_no", 2),
               (eq, ":count_no", 3),
               (val_add, ":enemy_power_count_new", reg1),
            (else_try),
               (eq, ":team_no", 2), #2军检测1军＋非人
               (this_or_next|eq, ":count_no", 1),
               (eq, ":count_no", 3),
               (val_add, ":enemy_power_count_new", reg1),
            (try_end),

            (gt, ":enemy_power_count_new", ":enemy_power_count_old"), #敌方评分比原位置更高，认为是向着敌方去的方向
            (gt, ":enemy_power_count_new", ":enemy_power_count_new_max"), #寻找敌方评分最高的方向
            (assign, ":enemy_power_count_new_max", ":enemy_power_count_new"),
            (assign,  ":vector_x", ":count_x"),
            (val_sub,  ":vector_x", ":cur_x"),
            (assign,  ":vector_y", ":count_y"),
            (val_sub,  ":vector_y", ":cur_y"), 
         (try_end),
         (this_or_next|neq,  ":vector_x", 0), #获取到方向向量，为（":vector_x"，":vector_y"），模为1
         (neq,  ":vector_y", 0),

         (try_for_range, ":slot_no", 0, 225), #清空
            (val_add, ":slot_no", slot_tool_party_rally), #指挥编队的slot_tool_party_rally往后，用于存它的阵型带来的权重加成
            (val_add, ":slot_no", 1), 
            (party_set_slot, ":commander_detachment_no", ":slot_no", -1), 
         (try_end),

         #设置由于阵型带来的权重，向量之后两个参数，第一个是相对指挥部队朝向的前后，正前负后，第二个是左右，正右负左。结合向量可以得出在global沙盘上的位移。能设置至多两种职能，不需要就填0。
         (try_begin),
            (eq, ":formation_no", "itm_formation_assault"), #进攻阵型
            (call_script,"script_formation_set_position", ":commander_detachment_no", ":vector_x", ":vector_y", 0, 0, "itm_detachment_strike", 0), #指挥周围
            (try_for_range, ":position_no", -5, 6), #前一排
               (call_script,"script_formation_set_position", ":commander_detachment_no", ":vector_x", ":vector_y", 1, ":position_no", "itm_detachment_strike", 0),
            (try_end),
            (try_for_range, ":position_no", -5, 6), #指挥编队左右
               (call_script,"script_formation_set_position", ":commander_detachment_no", ":vector_x", ":vector_y", 0, ":position_no", "itm_detachment_support", 0),
            (try_end),
            (try_for_range, ":position_no", -5, 6), #后一排
               (call_script,"script_formation_set_position", ":commander_detachment_no", ":vector_x", ":vector_y", -1, ":position_no", "itm_detachment_logistic", 0),
            (try_end),
         (else_try),
            (eq, ":formation_no", "itm_formation_suppress"), #压制阵型
         (try_end),
      (try_end),
    ]),


#输入指挥编队party ID，敌军方向向量x和y，相对位置前后和左右，前右为正，以及在这个位置上会有权重加成的编队职能的item ID。
#信息储存在从slot_tool_party_rally开始的指挥编队slot中，采用数位储存
#实际的沙盘中，会先判定该部分信息，如果有阵型的权重，就不会设置姿态的权重，免得需要对抗比如冲锋编队猪突的欲望。
  ("formation_set_position", [
      (store_script_param, ":detachment_no", 1), #指挥编队party ID
      (store_script_param, ":vector_x", 2), #方向向量xy，比如（1，0）是朝下的，（0，1）是朝右的
      (store_script_param, ":vector_y", 3), 
      (store_script_param, ":pos_x", 4), #当前位置相对指挥编队的位置，以指挥面朝的方向为x正，右侧为y正
      (store_script_param, ":pos_y", 5), 
      (store_script_param, ":function_no_1", 6), #在此有加成的编队职能
      (store_script_param, ":function_no_2", 7),

      (party_get_slot, ":cur_x", ":detachment_no", slot_tool_party_position_x),#获取指挥部队位置，展开阵型的基点
      (party_get_slot, ":cur_y", ":detachment_no", slot_tool_party_position_y),
      (try_begin),
         (eq, ":vector_x", 1), #敌军在下方，指挥编队的前也是global的正，但是右相对来说是左，要减
         (val_add, ":cur_x", ":pos_x"),
         (val_sub, ":cur_y", ":pos_y"),
      (else_try),
         (eq, ":vector_x", -1), #敌军在上方，右还是正，但是比指挥编队更前的需要减x
         (val_sub, ":cur_x", ":pos_x"),
         (val_add, ":cur_y", ":pos_y"),
      (else_try),
         (eq, ":vector_y", 1), #敌军在右方，前将会是global的右，右将会是global的下，都是加
         (val_add, ":cur_x", ":pos_y"),
         (val_add, ":cur_y", ":pos_x"),
      (else_try),
         (eq, ":vector_y", -1), #敌军在左方，前将会是global的左，右将会是global的上，都是减
         (val_sub, ":cur_x", ":pos_y"),
         (val_sub, ":cur_y", ":pos_x"),
      (try_end),

      (try_begin),
         (is_between, ":cur_x", 1, 16), #没超出棋盘范围
         (is_between, ":cur_y", 1, 16),
         (call_script, "script_change_coordinate_to_number", 15, ":cur_x", ":cur_y"), #坐标转序号（从0开始）
         (assign, ":slot_no", reg1),
         (val_add, ":slot_no", slot_tool_party_rally), #指挥编队的slot_tool_party_rally往后，用于存它的阵型带来的权重加成
         (val_add, ":slot_no", 1), 

         (val_sub, ":function_no_1", "itm_detachment_common"),
         (val_mul, ":function_no_1", 100),
         (val_max, ":function_no_1", 0),
         (val_sub, ":function_no_2", "itm_detachment_common"),
         (val_max, ":function_no_2", 0),
         (val_add, ":function_no_1", ":function_no_2"), #数位储存两种在此有加成的编队
         (party_set_slot, ":detachment_no", ":slot_no", ":function_no_1"),
      (try_end),
  ]),

#检测编队对于自己所属部队的指挥编队，是否在此有阵型加成。
#输入编队的party ID，当前正在检测的xy。输入reg1表示检测见过，0为阵型为展开，或者该处不存在阵型的设置，转姿态检测；1表示检测编队在当前位置有需求；-1表示该位置有阵型，但是不是检测的编队，要扣分，以免挡别的编队的路。
  ("formation_check_position", [
      (store_script_param, ":detachment_no", 1), #编队party ID
      (store_script_param, ":cur_x", 2), #xy位置
      (store_script_param, ":cur_y", 3), 
      (assign, ":check_result", 0), #检测结果

      (party_get_slot, ":party_no", ":detachment_no", slot_tool_party_resource), #获取原部队
      (assign, ":commander_detachment_no", -1),
      (try_for_range, ":slot_no", 0, "$g_total_detachment"), #寻找指挥编队
         (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
         (party_slot_eq, ":temp_party_id", slot_tool_party_resource, ":party_no"), #属于该部队的编队
         (party_slot_eq, ":temp_party_id", slot_tool_party_function, "itm_detachment_commander"), #指挥编队
         (assign, ":commander_detachment_no", ":temp_party_id"), 
      (try_end),

      (try_begin),
         (ge, ":commander_detachment_no", 0), #已找到指挥编队
         (party_get_slot, ":formation_no", ":commander_detachment_no", slot_tool_party_rally), #指挥编队已启动阵型
         (gt, ":formation_no", 0), #已激活阵型
         (neq, ":formation_no", "itm_formation_common"), #排除普通和驻扎
         (neq, ":formation_no", "itm_formation_station"), 

         (call_script, "script_change_coordinate_to_number", 15, ":cur_x", ":cur_y"), #坐标转序号（从0开始）
         (assign, ":slot_no", reg1),
         (val_add, ":slot_no", slot_tool_party_rally), #指挥编队的slot_tool_party_rally往后，用于存它的阵型带来的权重加成
         (val_add, ":slot_no", 1), 
         (party_get_slot, ":value_no", ":commander_detachment_no", ":slot_no"),
         (gt, ":value_no", 0),
         (assign, ":check_result", -1), #阵型展开且该处有设置，先预设为-1，下面如果发现该编队确有加成再改为1

         (store_div, ":function_no_1", ":value_no", 100),
         (val_add, ":function_no_1", "itm_detachment_common"),
         (store_mod, ":function_no_2", ":value_no", 100),
         (val_add, ":function_no_2", "itm_detachment_common"),
         (this_or_next|party_slot_eq, ":detachment_no", slot_tool_party_function, ":function_no_1"), #当前检测的编队，其职能是该位置需求的编队职能之一
         (party_slot_eq, ":detachment_no", slot_tool_party_function, ":function_no_2"), 
         (assign, ":check_result", 1),
      (try_end),
      (assign, reg1, ":check_result"),
  ]),


##新增


#————————————————————————————沙盘AI——————————————————————————
#沙盘AI，输入处理编队party ID，沙盘地图的party ID。
  ("cf_campaign_ai",
    [
      (store_script_param, ":detachment_no", 1), #编队ID
      (store_script_param, ":area_no", 2), #沙盘所用的部队，随机野战就是p_campaign_temp

      (call_script, "script_campaign_ai_technology", ":detachment_no", ":area_no"), #沙盘移动AI

(party_get_slot, reg3, ":detachment_no", slot_tool_party_position_x),
(party_get_slot, reg4, ":detachment_no", slot_tool_party_position_y),
(str_store_party_name, s1, ":detachment_no"),
(display_message, "@{s1} 评 估 完 毕 ，从 （{reg3}，{reg4}） 前 往 （{reg1}，{reg2}） "),

      (party_set_slot, ":detachment_no", slot_tool_party_position_x, reg1),#设置位置
      (party_set_slot, ":detachment_no", slot_tool_party_position_y, reg2),

      (party_get_slot, ":cohesion_count", ":detachment_no", slot_tool_party_cohesion),#扣除组织力
      (val_sub, ":cohesion_count", reg4),
      (party_set_slot, ":detachment_no", slot_tool_party_cohesion, ":cohesion_count"),
  ]),


#根据编队的行动能力，一轮动可能会动一到数次，每次执行一个此脚本。逻辑是获取周围四个点，假设编队移动到这四个点或者留在原地不同上，评分会升高还是降低。选择评分最高的脚本行动。
#输入编队party ID和沙盘party ID，返回推荐的移动位置为（reg1, reg2），将会消耗的组织力为reg4
  ("campaign_ai_technology",
    [
      (store_script_param, ":detachment_no", 1), #编队
      (store_script_param, ":area_no", 2), #沙盘
      (party_get_slot, ":cur_x", ":detachment_no", slot_tool_party_position_x),#获取位置
      (party_get_slot, ":cur_y", ":detachment_no", slot_tool_party_position_y),
      (assign, ":power_count", -999), #权重初始化
      (assign, ":target_x", ":cur_x"),
      (assign, ":target_y", ":cur_y"),
      (assign, ":cohesion_count", 0), #组织力消耗初始化

      (try_for_range, ":count_no", 0, 5),
         (try_begin),
            (eq, ":count_no", 0), #留在原地
            (assign, ":count_x", ":cur_x"),
            (assign, ":count_y", ":cur_y"),
         (else_try),
            (eq, ":count_no", 1), #下移
            (store_add, ":count_x", ":cur_x", 1),
            (assign, ":count_y", ":cur_y"),
         (else_try),
            (eq, ":count_no", 2), #上移
            (store_sub, ":count_x", ":cur_x", 1),
            (assign, ":count_y", ":cur_y"),
         (else_try),
            (eq, ":count_no", 3), #右移
            (assign, ":count_x", ":cur_x"),
            (store_add, ":count_y", ":cur_y", 1),
         (else_try),
            (eq, ":count_no", 4), #左移
            (assign, ":count_x", ":cur_x"),
            (store_sub, ":count_y", ":cur_y", 1),
         (try_end),
         (is_between, ":count_x", 1, 16), #没超出沙盘范围
         (is_between, ":count_y", 1, 16), 
         (call_script, "script_get_center_zone_ground", ":area_no", ":count_x", ":count_y"), #不是岩壁等无法立足的区块
#         (neq, reg1, "itm_zone_water"), #水体，以后要改
         (neq, reg1, "itm_zone_cliff"), 

         (call_script, "script_campaign_ai_count", ":detachment_no", ":count_x", ":count_y"), #计算评分

         (gt, reg1, ":power_count"),
         (assign, ":power_count", reg1), #target xy就是cur xy
         (assign, ":target_x", ":count_x"),
         (assign, ":target_y", ":count_y"),
         (assign, ":cohesion_count", reg3), #消耗的组织力
      (try_end),

      (assign, reg1, ":target_x"),
      (assign, reg2, ":target_y"),
      (assign, reg4, ":cohesion_count"),
  ]),


#部队规模积分，算法是确定某点后，将所有指定方的部队到该点的距离参数乘以规模之和。距离的计算方法为50减（x距离+y距离），毕竟此算法计算的是敌军对此处的影响，越近影响应该越大。
#输入位置xy，检测的team，以及该编队自己，输出总分reg1，离自己最近的某该方编队距离reg2，ID reg3
  ("campaign_caculate_team_power",
    [
      (store_script_param, ":cur_x", 1), #xy坐标
      (store_script_param, ":cur_y", 2), 
      (store_script_param, ":team_no", 3), #检测的阵营
      (store_script_param, ":detachment_no", 4), #该编队，用于在计算友军影响时排除自己，填-1就显示全体

      (assign, ":count_power", 0),
      (assign, ":nearest_distance", 50),
      (assign, ":nearest_detachment", 0),
      (try_for_range, ":slot_no", 0, "$g_total_detachment"), #遍历编队
         (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
         (party_slot_eq, ":temp_party_id", slot_tool_party_team, ":team_no"), #目标阵营
         (neq, ":temp_party_id", ":detachment_no"), #排除自己

         (party_get_num_companions, ":troop_num", ":temp_party_id"),
         (ge, ":troop_num", 300), #只算人数够多的，排除人数极少的比如小股密探、刺客、信使等
         (val_div, ":troop_num", 2000), #编队人数太多，再计算拥挤程度时会等效于多个编队，2000一算，不少于1
         (val_max, ":troop_num", 1),

         (party_get_slot, ":count_x", ":temp_party_id", slot_tool_party_position_x),#位置
         (party_get_slot, ":count_y", ":temp_party_id", slot_tool_party_position_y),
         (val_sub, ":count_x", ":cur_x"),
         (val_abs, ":count_x"),
         (val_sub, ":count_y", ":cur_y"),
         (val_abs, ":count_y"),
         (val_add, ":count_x", ":count_y"),
         (try_begin),
            (lt, ":count_x", ":nearest_distance"), #寻找最近的该方编队
            (assign, ":nearest_distance", ":count_x"),
            (assign, ":nearest_detachment", ":temp_party_id"),
         (try_end),

         (store_sub, ":count_x", 50, ":count_x"),  
         (try_begin), #部队距离积分
            (party_get_num_companions, ":troop_num", ":temp_party_id"),
            (ge, ":troop_num", 300), #只算人数够多的，排除人数极少的比如小股密探、刺客、信使等
            (val_div, ":troop_num", 2000), #编队人数太多，再计算拥挤程度时会等效于多个编队，2000一算，不少于1
            (val_max, ":troop_num", 1),
            (store_mul, ":troop_num", ":count_x", ":troop_num"),
            (val_add, ":count_power", ":troop_num"),
         (try_end),
      (try_end),
      (assign, reg1, ":count_power"), #部队位置评分
      (assign, reg2, ":nearest_distance"), #最近的部队距离和ID
      (assign, reg3, ":nearest_detachment"),
  ]),


#计算编队位移到某个目标区域的评分，并且除了移动本身提供评分，移动之后执行的战术也会提供评分，将会获取评分最高的战术。
#输入编队party ID和目标地点的横x纵y坐标，返回最高评分reg1，与评分最高的战术reg2，该行动结果将会消耗的组织力reg3
  ("campaign_ai_count",
    [
      (store_script_param, ":detachment_no", 1), #编队
      (store_script_param, ":cur_x", 2), #将要计算评分的横纵坐标xy
      (store_script_param, ":cur_y", 3), 
      (assign, ":power_count", 0), #初始化评分
      (assign, ":cohesion_count", 0), #初始化消耗的组织力

#基础信息汇总
      (party_get_slot, ":team_no", ":detachment_no", slot_tool_party_team), #哪一方阵营
      (party_get_slot, ":last_x", ":detachment_no", slot_tool_party_position_x),#该编队当前所在的位置
      (party_get_slot, ":last_y", ":detachment_no", slot_tool_party_position_y),

#编队数量评估
      (assign, ":detachment_count", 0), #总编队数
      (assign, ":ally_count", 0), #友军编队数（不包括该编队）
      (assign, ":enemy_count", 0), #敌对编队数（包括除了中立以外的所有编队）

      (try_for_range, ":slot_no", 0, "$g_total_detachment"), #遍历编队
         (troop_get_slot, ":temp_party_id", "trp_temp_array_detachment", ":slot_no"), 
         (party_slot_eq, ":temp_party_id", slot_tool_party_position_x, ":cur_x"),#在该位置的编队
         (party_slot_eq, ":temp_party_id", slot_tool_party_position_y, ":cur_y"),
         (party_get_num_companions, ":troop_num", ":temp_party_id"),
         (ge, ":troop_num", 300), #只算人数够多的，排除人数极少的比如小股密探、刺客、信使等
         (val_div, ":troop_num", 2000), #编队人数太多，再计算拥挤程度时会等效于多个编队，2000一算，不少于1
         (val_max, ":troop_num", 1),
         (val_add, ":detachment_count", ":troop_num"),
         (try_begin),
            (party_slot_eq, ":temp_party_id", slot_tool_party_team, ":team_no"), #友军
            (neq, ":temp_party_id", ":detachment_no"), #排除自己
            (val_add, ":ally_count", ":troop_num"),
         (else_try),
            (neg|party_slot_eq, ":temp_party_id", slot_tool_party_team, ":team_no"), #不是友军且不是中立的就是敌军
            (neg|party_slot_eq, ":temp_party_id", slot_tool_party_team, 0), 
            (val_add, ":enemy_count", ":troop_num"),
         (try_end),
      (try_end),

      (try_begin),
         (assign, ":cur_detachment_num", 0), #自己的人数
         (this_or_next|neq, ":last_x", ":cur_x"),#排除评估原地不动选项时的重复
         (neq, ":last_y", ":cur_y"),
         (party_get_num_companions, ":cur_detachment_num", ":detachment_no"), #该编队人数
         (try_begin),
            (ge, ":cur_detachment_num", 300), #不小于300
            (val_div, ":cur_detachment_num", 2000), 
            (val_max, ":cur_detachment_num", 1),
         (else_try),
            (assign, ":cur_detachment_num", 0), #少于300不占规模
         (try_end),
         (val_add, ":detachment_count", ":cur_detachment_num"), #因为是预设已经移到那里去了，所以要加上该编队占据的位置
      (try_end),

(str_store_string, s4, "@无 部 队 规 模 减 益 "),
      (try_begin),
         (gt, ":detachment_count", 4),
         (store_sub, ":value_no", ":detachment_count", 4), #超过4就会受到减益，每多一个少30，达到7时将会减接近100，软上限
         (val_mul, ":value_no", 30),
         (val_sub, ":power_count", ":value_no"), 
(assign, reg1, ":value_no"),
(str_store_string, s4, "@因 部 队 规 模 造 成 的 -{reg1} "),
      (try_end),

#敌我人数评估
(str_store_string, s3, "@邻 近 无 交 战 "),
      (store_add, ":count_no", ":cur_detachment_num", ":ally_count"), #己方和友军的总和
      (try_begin),
         (gt, ":enemy_count", 0), #存在敌军
         (le, ":ally_count", ":enemy_count"), #友军本来和敌军在此势均力敌或有劣势，进入后有了优势，会倾向于雪中送炭
         (ge, ":count_no", ":enemy_count"),
         (val_add, ":power_count", 40), 
(str_store_string, s3, "@支 援 邻 近 友 军 +40 "),
      (else_try),
         (lt, ":count_no", ":enemy_count"), #进入后人数少于敌军，不倾向于前往
         (val_sub, ":power_count", 30), 
(str_store_string, s3, "@邻 近 敌 军 力 量 太 强 -30 "),
      (try_end),

#行动姿态评估
      (assign, ":enemy_power_count_new", 0), #敌对力量在新位置的计分
      (try_for_range, ":count_no", 0, 4),
         (call_script, "script_campaign_caculate_team_power",  ":cur_x",  ":cur_y", ":count_no", ":detachment_no"), #新位置上的计分
         (eq, ":team_no", ":count_no"),
         (neq, ":team_no", 3), #非人彼此之间无协调
         (assign, ":ally_power_count_new", reg1), #同阵型计分
         (assign, ":ally_nearest_distance", reg2), #最近友军的距离
      (else_try),
         (eq, ":team_no", 0), #无势力的敌对方只有非人
         (eq, ":count_no", 3),
         (val_add, ":enemy_power_count_new", reg1),
      (else_try),
         (eq, ":team_no", 3), #非人检测所有阵营
         (val_add, ":enemy_power_count_new", reg1),
      (else_try),
         (eq, ":team_no", 1), #1军检测2军＋非人
         (this_or_next|eq, ":count_no", 2),
         (eq, ":count_no", 3),
         (val_add, ":enemy_power_count_new", reg1),
         (assign, ":enemy_nearest_distance", reg2), #最近敌军的距离
      (else_try),
         (eq, ":team_no", 2), #2军检测1军＋非人
         (this_or_next|eq, ":count_no", 1),
         (eq, ":count_no", 3),
         (val_add, ":enemy_power_count_new", reg1),
         (assign, ":enemy_nearest_distance", reg2), #最近敌军的距离
      (try_end),

      (assign, ":enemy_power_count_old", 0), #敌对力量在原位置的计分
      (try_for_range, ":count_no", 0, 4),
         (call_script, "script_campaign_caculate_team_power",  ":last_x",  ":last_y", ":count_no", ":detachment_no"), #原位置上的计分
         (eq, ":team_no", ":count_no"),
         (neq, ":team_no", 3), #非人彼此之间无协调
         (assign, ":ally_power_count_old", reg1), #同阵型计分
      (else_try),
         (eq, ":team_no", 0), #无势力的敌对方只有非人
         (eq, ":count_no", 3),
         (val_add, ":enemy_power_count_old", reg1),
      (else_try),
         (eq, ":team_no", 3), #非人检测所有阵营
         (val_add, ":enemy_power_count_old", reg1),
      (else_try),
         (eq, ":team_no", 1), #1军检测2军＋非人
         (this_or_next|eq, ":count_no", 2),
         (eq, ":count_no", 3),
         (val_add, ":enemy_power_count_old", reg1),
      (else_try),
         (eq, ":team_no", 2), #2军检测1军＋非人
         (this_or_next|eq, ":count_no", 1),
         (eq, ":count_no", 3),
         (val_add, ":enemy_power_count_old", reg1),
      (try_end),


##新增

(str_store_string, s2, "@姿 态 判 定 未 生 效 "),
      (party_get_slot, ":attitude_no", ":detachment_no", slot_tool_party_attitude), 
      (try_begin),
         (neg|party_slot_eq, ":detachment_no", slot_tool_party_function, "itm_detachment_commander"), #不是指挥编队
         (call_script, "script_formation_check_position", ":detachment_no",  ":cur_x",  ":cur_y"), #判断部队是否在该位置有阵型需求，有就不做姿态判断了。以阵型为优先。
         (neq, reg1, 0), 
         (try_begin),
            (eq, reg1, 1), #检测成功
            (val_add, ":power_count", 100), 
(str_store_string, s2, "@阵 型 检 测 成 功 +100 "),
         (else_try),
            (eq, reg1, -1), #检测失败
            (val_sub, ":power_count", 100),
(str_store_string, s2, "@阵 型 检 测 失 败 -100 "), 
         (try_end),

##新增

      (else_try),                                      #既不成功也不失败，reg1＝0时表示该处与阵型无关时，检测姿态
         (eq, ":attitude_no", ai_attitude_charge), #冲锋
         (gt, ":enemy_power_count_new", ":enemy_power_count_old"), #向敌人多的地方去
         (val_add, ":power_count", 50), 
(str_store_string, s2, "@冲 锋 姿 态 判 定 生 效 加 50 "),
      (else_try), 
         (eq, ":attitude_no", ai_attitude_rout), #溃逃
         (lt, ":enemy_power_count_new", ":enemy_power_count_old"), #向敌人少的地方去
         (val_add, ":power_count", 50), 
(str_store_string, s2, "@溃 逃 姿 态 判 定 生 效 加 50 "),
      (else_try),
         (eq, ":attitude_no", ai_attitude_harass), #牵制
         (eq, ":enemy_nearest_distance", 3), #3是射程，以后要改
         (val_add, ":power_count", 50), 
(str_store_string, s2, "@牵 制 姿 态 判 定 生 效 加 50 "),
      (else_try),
         (eq, ":attitude_no", ai_attitude_guard), #守卫
         (gt, ":enemy_power_count_new", ":enemy_power_count_old"), #向敌人多的地方去且距离最近友军不超过1
         (le, ":ally_nearest_distance", 1), 
         (val_add, ":power_count", 50), 
(str_store_string, s2, "@守 卫 姿 态 判 定 生 效 加 50 "),
      (else_try),
         (eq, ":attitude_no", ai_attitude_evade), #回避
         (lt, ":enemy_power_count_new", ":enemy_power_count_old"), #向敌人少的地方去且距离最近友军不超过1
         (le, ":ally_nearest_distance", 1), 
         (val_add, ":power_count", 50), 
(str_store_string, s2, "@回 避 姿 态 判 定 生 效 加 50 "),
      (else_try),
         (eq, ":attitude_no", ai_attitude_selfprotect), #自我保护
         (gt, ":ally_power_count_new", ":ally_power_count_old"), #向友军多的地方去
         (val_add, ":power_count", 50), 
(str_store_string, s2, "@自 我 保 护 姿 态 判 定 生 效 加 50 "),
      (try_end),

#组织力消耗评估
      #一般来说编队不会因为组织力消耗而倾向于不做进行某项战术，只会在剩余组织力逼近危险线时做出应对。但是移动选项将会减少些微的组织力，抵消用于模糊系统优先级的微小扰动。表现为如果移动和停留在原地评分相同，编队会倾向于原地待命。
      (try_begin),
         (this_or_next|neq, ":last_x", ":cur_x"),#排除评估原地不动选项时的重复
         (neq, ":last_y", ":cur_y"),
         (assign, ":value_no", ":cur_detachment_num"),
         (val_max, ":value_no", 1), #移动最少消耗1组织力，即使不占规模的部队也是一样
         (val_add, ":cohesion_count", ":value_no"), #该移动会消耗的组织力
         (val_mul, ":value_no", 5), #编队规模×5
         (val_sub, ":power_count", ":value_no"), 
      (try_end),

#扰动和结果输出
      (store_random_in_range, ":value_no", 0, 6), #为估值增加一个微小的扰动，模糊掉由于系统结构造成的优先级
      (val_add, ":power_count", ":value_no"), 
      (assign, reg1, ":power_count"),
      (assign, reg3, ":cohesion_count"),


         (assign, reg4, ":cur_x"),
         (assign, reg5, ":cur_y"),
         (assign, reg6, ":enemy_power_count_old"),
         (assign, reg7, ":enemy_power_count_new"),
(str_store_party_name, s1, ":detachment_no"),
(display_message, "@{s1} 在（{reg4}，{reg5}）上 {s4}， {s3}， {s2}— — 总 评 分 {reg1}"),
  ]),





######################################################剧情相关######################################################

#set a substitude for player in film mode. Output two weapon no in game variables.
  ("set_player_substitute", [
      (troop_get_type, ":return_value", "trp_player"),
      (troop_set_type, "trp_temp_substitute", ":return_value"),

      (str_store_troop_face_keys, s1, "trp_player"),
      (troop_set_face_keys, "trp_temp_substitute", s1),

      (troop_clear_inventory, "trp_temp_substitute"),

      (try_for_range, ":count_no", 2, 9),#ammo and armour
         (call_script, "script_player_get_new_inventory_slot", ":count_no"),
         (gt, reg0, 0),
         (troop_set_inventory_slot, "trp_temp_substitute", ":count_no", reg0),
      (try_end),

      (assign, ":end_cond", 13),
      (try_for_range, ":count_no", 10, ":end_cond"),#right hand
         (call_script, "script_player_get_new_inventory_slot", ":count_no"),
         (gt, reg0, 0),
         (troop_set_inventory_slot, "trp_temp_substitute", 0, reg0),
         (assign, ":end_cond", 10),
      (try_end),

      (assign, ":end_cond", 16),
      (try_for_range, ":count_no", 13, ":end_cond"),#left hand
         (call_script, "script_player_get_new_inventory_slot", ":count_no"),
         (gt, reg0, 0),
         (troop_set_inventory_slot, "trp_temp_substitute", 1, reg0),
         (assign, ":end_cond", 13),
      (try_end),
    ]),

#在剧情演出时展示对话，刷新prsnt_total_battle_interface
#对话内容储存在s67中
#填-1就能关闭
  ("start_conversation_battle", [
      (store_script_param, ":agent_no", 1),
      (assign, "$g_talking_agent", ":agent_no"),
      (start_presentation, "prsnt_total_battle_interface"),
    ]),


##_______________________________________________________________________________others___________________________________________________________________________
#script_output_troop_itms_text
  ("output_troop_itms_text", [
      (store_script_param, ":troop_no", 1),

      (display_message, "@["),
      (assign, ":str_itm_0", "str_string_end"),
      (val_add, ":str_itm_0", 1),
      (troop_get_inventory_capacity, ":inventory_capacity", ":troop_no"),
      (try_for_range, ":slot_no", 0, ":inventory_capacity"),
         (troop_get_inventory_slot, ":item_no", ":troop_no", ":slot_no"),
         (gt, ":item_no", 0),
         (store_add, ":string_no", ":str_itm_0", ":item_no"),
         (str_store_string, s1, ":string_no"),
         (display_message, "@{s1},_"),
      (try_end),
      (display_message, "@]"),
    ]),


#获取一本书可以卖的书，返回书的item ID储存在reg1里
  ("get_book_sold", [
      (assign, ":book_begin", "itm_book_item"),
      (val_add, ":book_begin", 1),
      (store_random_in_range, ":item_no", ":book_begin", "itm_good_item"),
      (try_begin),
         (neg|item_has_property, ":item_no", itp_unique), 
         (assign, reg1, ":item_no"),
      (else_try),
         (call_script, "script_get_book_sold"),
      (try_end),
    ]),

] + scripts_initialized_data