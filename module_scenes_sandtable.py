# -*- coding: UTF-8 -*-

from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

## CC
open_field_small       = "0x00000002296028000005415000003efe00004b34000059be"     #  336*336
open_field_normal      = "0x0000000229602800000691a400003efe00004b34000059be"     #  420*420
open_field_large       = "0x00000002296028000009da7600003efe00004b34000059be"     #  630*630
open_field_extra_large = "0x0000000229602800000d234800003efe00004b34000059be"     #  840*840

forest_small       = "0x30002800000320c80000034e00004b34000059be"     #  200*200
forest_normal      = "0x300028000003e8fa0000034e00004b34000059be"     #  250*250
forest_large       = "0x300028000005dd770000034e00004b34000059be"     #  375*375
forest_extra_large = "0x300028000007D1F40000034e00004b34000059be"     #  500*500
## CC


scenes_sandtable = [
#沙盘地图
  ("town_4_sandtable",sf_generate,"none", "none", (0,0),(160,160),-50,"0x000000005000050000025896000006e300002bf700003f8c", [],[]),


#随机沙盘地图
#平原
  ("random_sandtable_plain_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_6",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_7",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_8",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_9",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_10",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_11",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_12",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_13",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_14",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_15",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_16",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_17",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_18",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_19",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_20",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_21",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_22",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_23",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_24",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_25",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_26",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_27",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_28",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_29",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_plain_30",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#山地
  ("random_sandtable_mountain_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_6",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_7",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_8",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_9",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_10",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_11",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_12",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_13",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_14",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_15",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_16",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_17",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_18",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_19",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_mountain_20",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#草原
  ("random_sandtable_steppe_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_6",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_7",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_8",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_9",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_10",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#荒山
  ("random_sandtable_steppe_mountain_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_mountain_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_mountain_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_mountain_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_steppe_mountain_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#沼泽
  ("random_sandtable_marsh_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_6",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_7",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_8",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_9",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_marsh_10",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#雪原
  ("random_sandtable_snow_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_6",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_7",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_8",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_9",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_10",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#雪山
  ("random_sandtable_snow_mountain_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_6",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_7",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_8",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_9",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_snow_mountain_10",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#沙漠
  ("random_sandtable_desert_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
#戈壁
  ("random_sandtable_desert_mountain_1",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_mountain_2",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_mountain_3",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_mountain_4",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),
  ("random_sandtable_desert_mountain_5",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),

  ("random_sandtable_end",sf_generate,"none", "none", (0,0),(160,160),-50,"0x0000000030000500000258960000229400001d73000012e7", [],[]),

#建筑场景
  ("adventurer_station_1",sf_indoors,"interior_castle_g", "bo_interior_castle_g", (-100,-100),(100,100),-105,"0",#冒险者协会
    ["exit"],[]),

  ("underworld_stronghold_1",sf_indoors,"interior_tavern_e_new", "bo_interior_tavern_e", (-100,-100),(100,100),-105,"0",#黑帮据点
    ["exit"],[]),
]