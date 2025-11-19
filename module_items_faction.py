# -*- coding: UTF-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
faction_items = [

["faction_begin", "faction_begin", [("faction_kingdom_default", 0)], 0, 0, 1000, weight(0)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0)|hit_points(0)|weapon_length(0)|spd_rtng(0)|shoot_speed(0)|max_ammo(0)|accuracy(0)|shield_width(0)|shield_height(0)|horse_scale(0)|horse_speed(0)|horse_maneuver(0)|food_quality(0)|abundance(0)|thrust_damage(0, 0)|swing_damage(0, 0), 0, []], 

#Never use horse_charge, as horse_charge is just the same value of thrust_damage.
#thrust_damage用于表示秩序和混乱的倾向, 0秩序, 1表示混乱，具体数值则是程度。
#swing_damage用于表示善良和邪恶的倾向, 0善良, 1表示邪恶，具体数值则是程度。
#difficulty用于表示规模等级, 1 is footstone team, 2 is colossus organization, 3 is macro power ,4 is leviathan, 5 is detached institution
#abundance用于表示权力结构, 0 is blank, 1 is autocrat, 2 is centralization, 3 is co-discussion




##########################################################魔物#######################################################
["demon", "demon", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(5)|abundance(1)|thrust_damage(78, 0)|swing_damage(99, 1), 0, [], [fac_heresy_demon]], 

######魔王崇拜者#####
###
["devil_worshipper", "devil_worshipper", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(4)|abundance(3)|thrust_damage(45, 1)|swing_damage(80, 1), 0, [], [fac_heresy_demon]], 


######魔气侵蚀者#####
###
["demonic_corruptor", "Demonic Corruptor", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(4)|abundance(3)|thrust_damage(45, 1)|swing_damage(80, 1), 0, [], [fac_heresy_demon]], 




##########################################################创世女神教#######################################################
["creation_goddess_religion", "creation_goddess_religion", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(5)|abundance(1)|thrust_damage(99, 0)|swing_damage(99, 0), 0, [], [fac_kingdom_5]], 





##########################################################权厄之秤#######################################################
["libra", "libra", [("faction_libra", 0)], 0, 0, 1000, difficulty(5)|abundance(3)|thrust_damage(80, 0)|swing_damage(60, 1), 0, [], [fac_outlaws_libra]], 
#司秤人
["libra_in_lesaff", "Libra in Lesaff", [("faction_libra", 0)], 0, 0, 0, difficulty(3)|abundance(2)|thrust_damage(80, 0)|swing_damage(60, 1), 0, [], [fac_outlaws_libra]], #勒塞夫区

#分舵
["black_candle_gang", "Black Candle Gang", [("faction_libra", 0)], 0, 0, 0, difficulty(2)|abundance(2)|thrust_damage(80, 0)|swing_damage(60, 1), 0, [], [fac_outlaws_libra]], #黑烛帮
["splitting_sail_brotherhood", "Splitting Sail Brotherhood", [("faction_libra", 0)], 0, 0, 0, difficulty(2)|abundance(2)|thrust_damage(80, 0)|swing_damage(60, 1), 0, [], [fac_outlaws_libra]], #裂帆兄弟会





##########################################################七古王会议#######################################################
["seven_kings_alliance", "seven_kings_alliance", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(5)|abundance(3)|thrust_damage(75, 0)|swing_damage(80, 0), 0, [], [fac_saviour]], 





##########################################################冒险者协会#######################################################
["adventurers_association", "adventurers_association", [("faction_adventurers_association", 0)], 0, 0, 1000, difficulty(5)|abundance(3)|thrust_damage(65, 0)|swing_damage(85, 0), 0, [], [fac_adventurers_association]], 
#普威尔冒险者协会
["powell_adventures_association", "Powell Adventures Association", [("faction_adventurers_association", 0)], 0, 0, 0, difficulty(3)|abundance(2)|thrust_damage(65, 0)|swing_damage(85, 0), 0, [], [fac_adventurers_association]], #普威尔冒险者协会
["powell_adventures_association_in_lesaff", "Powell Adventures Association in Lesaff", [("faction_adventurers_association", 0)], 0, 0, 0, difficulty(2)|abundance(2)|thrust_damage(65, 0)|swing_damage(85, 0), 0, [], [fac_adventurers_association]], #冒险者协会勒塞夫分会






#######################################################普威尔联合王国#######################################################
["kingdom_1", "kingdom_1", [("faction_kingdom_1", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(67, 0)|swing_damage(73, 0), 0, [], [fac_kingdom_1]], 

######联合王国直属#####
###
#圣龙骑士团
["order_of_holy_dragoon", "Order Of Holy Dragoon", [("faction_order_of_holy_dragoon", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(80, 0)|swing_damage(50, 0), 0, [], [fac_kingdom_1]], 
#龙神教
["dragon_worship", "dragon_worship", [("faction_dragon_worship", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(68, 0)|swing_damage(71, 0), 0, [], [fac_kingdom_1]], 
["sedative_pavilion", "Sedative Pavilion", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(2)|thrust_damage(8, 1)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #镇静公馆
#合法拾荒者
["legal_scavenger", "legal_scavenger", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(13, 0)|swing_damage(40, 0), 0, [], [fac_kingdom_1]], 


######普威尔中央#####
###
["kingdom_1_1", "Powell Central", [("faction_kingdom_1_1", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(81, 0)|swing_damage(74, 0), 0, [], [fac_kingdom_1]], 

#王冠骑士团
["knight_order_1_1", "Knight Order of Crowns", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(80, 0)|swing_damage(70, 0), 0, [], [fac_kingdom_1]], 
["national_knights_order", "National  Knights Order", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(80, 0)|swing_damage(50, 0), 0, [], [fac_kingdom_1]], #国家骑士团
#王庭禁卫
["tocsin_forbidden_guard", "Tocsin Forbidden Guard", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(2)|thrust_damage(46, 0)|swing_damage(44, 0), 0, [], [fac_kingdom_1]], #戒钟禁卫队
["eliminater", "eliminater", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #肃正之镰
#普威尔学术机关
["royal_element_research_institute", "Royal Element Research Institute", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(2)|abundance(2)|thrust_damage(46, 0)|swing_damage(44, 0), 0, [], [fac_kingdom_1]], #王家元素研究院
["national_dragon_college", "National Dragon College", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(2)|abundance(2)|thrust_damage(46, 0)|swing_damage(44, 0), 0, [], [fac_kingdom_1]], #国立龙学院
["powell_military_factory", "Powell Military Factory", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #普威尔军工厂


######罗德里格斯公国#####
###
["kingdom_1_2", "Rodriguez Duchy", [("faction_kingdom_1_2", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(72, 0)|swing_damage(76, 0), 0, [], [fac_kingdom_1]], 

#元素骑士团
["knight_order_1_2", "Knight Order of Elements", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(70, 0), 0, [], [fac_kingdom_1]], 
["bloodfire_mercenary_corps", "bloodfire_mercenary_corps", [("faction_bloodfire_mercenary_corps", 0)], 0, 0, 0, difficulty(1)|abundance(2)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #血火佣兵团
#勒塞夫商会
["rodriguez_firm", "Rodriguez Firm", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(65, 0)|swing_damage(44, 0), 0, [], [fac_kingdom_1]], #罗德里格斯商会
#戈兰尼尔地方武装
["holding_guard_order", "holding_guard_order", [("faction_holding_guard_order", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #扼守之盾
["grenier_militia", "grenier_militia", [("faction_grenier_militia", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #戈兰尼尔民兵自卫队


######北境开拓领#####
###
["kingdom_1_3", "Northern Reclaimer", [("faction_kingdom_1_3", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(74, 0)|swing_damage(80, 0), 0, [], [fac_kingdom_1]], 
#龙血骑士团
["knight_order_1_3", "Knight Order of Dragonblood", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(55, 0)|swing_damage(80, 0), 0, [], [fac_kingdom_1]], 
#地方武装
["dragon_prison", "Dragon Prison", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #龙狱
["hometownless_knight_order", "Hometownless Knight Order", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #无乡骑士团


######普属自由城邦#####
###
["kingdom_1_4", "Powell State", [("faction_kingdom_1_4", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(70, 0)|swing_damage(65, 0), 0, [], [fac_kingdom_1]], 
#普威尔正教
["powell_orthodox", "powell_orthodox", [("faction_powell_orthodox", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(73, 0)|swing_damage(59, 0), 0, [], [fac_kingdom_1]], 
["divine_swordsworn_seminary", "Divine Swordsworn Seminary", [("faction_divine_swordsworn_seminary", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #奉剑修会
#奉神骑士团
["knight_order_1_4", "Knight Order of Preist", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(70, 0)|swing_damage(50, 0), 0, [], [fac_kingdom_1]], 


######南沙王国#####
###
["kingdom_1_5", "Sousanth Duchy", [("faction_kingdom_1_5", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(76, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_1]], 
#沙舟骑士团
["knight_order_1_5", "Knight Order of Sandboat", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(75, 0)|swing_damage(70, 0), 0, [], [fac_kingdom_1]], 
["gurorrion_guard", "Gurorrion Guard", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #古洛隆卫队





#######################################################伊希斯公国#######################################################
["kingdom_2", "kingdom_2", [("faction_kingdom_2", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(70, 0)|swing_damage(60, 0), 0, [], [fac_kingdom_2]], 

######灵魂之灵树#####grachite
###
["kingdom_2_1", "Spirittree of Soul", [("faction_kingdom_2_1", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 
#灵树骑士团
["knight_order_2_1", "Knight Order of Spirittree", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 
["spiritual_horse_pasture", "Spiritual Horse Pasture", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(85, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_1]], #灵马牧场

#墨钢工坊
["grachite_workshop", "Grachite Workshop", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 


######死亡之灵树#####
###
["kingdom_2_2", "Spirittree of Demisel", [("faction_kingdom_2_2", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(82, 0)|swing_damage(48, 0), 0, [], [fac_kingdom_2]], 
#灵雨游侠团
["knight_order_2_2", "Knight Order of Spiritwind", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(82, 0)|swing_damage(48, 0), 0, [], [fac_kingdom_2]], 

#冰河探险队
["glacier_exploration_team", "Glacier Exploration Team", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 


######先祖之灵树#####
###
["kingdom_2_3", "Spirittree of Ancester", [("faction_kingdom_2_3", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(80, 0)|swing_damage(41, 0), 0, [], [fac_kingdom_2]], 
#永世者刺客团
["knight_order_2_3", "Knight Order of Spiritrain", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(40, 0)|swing_damage(41, 0), 0, [], [fac_kingdom_2]], 

#嘉果园
["great_apple_garden", "Great Apple Garden", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 
#蜕生者战团
["molter_legion", "Molter Legion", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 

#库勒斯煤矿
["kules_coal_mine", "Kules Coal Mine", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 


######生命之灵树#####
###
["kingdom_2_4", "Spirittree of Vita", [("faction_kingdom_2_4", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(75, 0)|swing_damage(53, 0), 0, [], [fac_kingdom_2]], 
#灵风游骑团
["knight_order_2_4", "Immortal Assassin", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(65, 0)|swing_damage(53, 0), 0, [], [fac_kingdom_2]], 

#伊希斯人类西海自警团
["yishith_westcoast_militia", "yishith_westcoast_militia", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(70, 0)|swing_damage(76, 0), 0, [], [fac_kingdom_2]], 

#雪泥商会
["snow_trading_company", "Snow Trading Company", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(80, 0)|swing_damage(45, 0), 0, [], [fac_kingdom_2]], 





#######################################################科鲁托酋长国#######################################################
["kingdom_3", "kingdom_3", [("pic_arms_khergit", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(45, 0)|swing_damage(54, 0), 0, [], [fac_kingdom_3]], 

######图腾同盟#####
###
["kingdom_3_1", "Totem Allience", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(55, 0)|swing_damage(56, 0), 0, [], [fac_kingdom_3]], 
#科鲁托剑斗旅团
["knight_order_3_1", "Swordfight Brigade", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(23, 0)|swing_damage(36, 0), 0, [], [fac_kingdom_3]], 
#人类辅助军
["kouruto_auxiliary", "kouruto_auxiliary", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(35, 0)|swing_damage(21, 0), 0, [], [fac_kouruto_auxiliary]], 

#铁峰守备旅团
["ironpeak_garrison_brigade", "Ironpeak Garrison Brigade", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(52, 0)|swing_damage(27, 0), 0, [], [fac_kingdom_3]], 
#洪炉监视旅团
["furnace_watch_brigade", "Furnace Watch Brigade", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(60, 0)|swing_damage(23, 0), 0, [], [fac_kingdom_3]], 
["ironbite_gang", "Ironbite Gang", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(30, 1)|swing_damage(13, 0), 0, [], [fac_kingdom_3]], #啮铁帮


######麦汗族#####
###
["kingdom_3_2", "Mankhai Clan", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(45, 0)|swing_damage(63, 0), 0, [], [fac_kingdom_3]], 

#炉边萨满联盟
["fireside_circle_of_shaman", "Fireside Circle of Shaman", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(20, 0)|swing_damage(52, 0), 0, [], [fac_kingdom_3]], 


######金爪子帮#####
###
["kingdom_3_3", "Goldclaw Gang", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(60, 0)|swing_damage(60, 0), 0, [], [fac_kingdom_3]], 
["knight_order_3_2", "Knight Order of Divinecusp", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(69, 0)|swing_damage(54, 0), 0, [], [fac_kingdom_3]], 

#金爪子商会
["goldclaw_guild", "Goldclaw Guild", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(60, 0)|swing_damage(33, 0), 0, [], [fac_kingdom_3]], 
#不死者猎杀旅团
["undead_slayer_brigade", "Undead Slayer Brigade", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(46, 0)|swing_damage(28, 0), 0, [], [fac_kingdom_3]], 


######守望派#####
###
["kingdom_3_4", "Sentinel Clique", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(66, 0)|swing_damage(47, 0), 0, [], [fac_kingdom_3]], 
#守望者卫戍旅团
["knight_order_3_2", "Sentinel Bastion Brigade", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(69, 0)|swing_damage(54, 0), 0, [], [fac_kingdom_3]], 

######人子之刃#####
###
["kingdom_3_5", "kingdom_3_5", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(75, 0)|swing_damage(73, 0), 0, [], [fac_kingdom_3]], 





####################################################乌-迪默-安基亚邦联#####################################################
["kingdom_4", "kingdom_4", [("faction_kingdom_4", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(72, 0)|swing_damage(49, 0), 0, [], [fac_kingdom_4]], 

######黑沼议事会#####
###
["kingdom_4_1", "Black Marsh Council", [("faction_kingdom_4_1", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(78, 0)|swing_damage(33, 0), 0, [], [fac_kingdom_4]], 
#光瘴学派
["knight_order_4_1", "School of Optihazation", [("faction_knight_order_4_1", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(64, 0)|swing_damage(46, 0), 0, [], [fac_kingdom_4]], 
["lord_of_myriad_altars", "Lord of Myriad Altars", [("faction_knight_order_4_1", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(73, 0)|swing_damage(29, 0), 0, [], [fac_kingdom_4]], #万龛之主
#司奴局
["slave_bureau", "Slave Bureau", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(52, 0)|swing_damage(18, 1), 0, [], [fac_kingdom_4]],
#暗沼之花佣兵团
["marsh_flower_landsknechts", "Marsh Flower Landsknechts", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(5, 0)|swing_damage(39, 0), 0, [], [fac_kingdom_4]],


######乌尔之子女#####
###
["kingdom_4_2", "Offspring of Uhr", [("faction_kingdom_4_2", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(45, 0)|swing_damage(40, 0), 0, [], [fac_kingdom_4]], 
#深海恐惧刺客团
["dread_of_the_deep", "Dread of the Deep", [("faction_dread_of_the_deep", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(24, 0)|swing_damage(26, 0), 0, [], [fac_kingdom_4]], 
["deep_binder", "Deep Binder", [("faction_dread_of_the_deep", 0)], 0, 0, 1000, difficulty(1)|abundance(2)|thrust_damage(20, 1)|swing_damage(31, 1), 0, [], [fac_kingdom_4]], #深邃封印团


######净世军#####
###
["kingdom_4_3", "Purifier", [("faction_kingdom_4_3", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(10, 0)|swing_damage(70, 0), 0, [], [fac_kingdom_4]], 
#神牙修道军
["knight_order_4_2", "Friar Force of Divinecusp", [("faction_knight_order_4_2", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(26, 0)|swing_damage(76, 0), 0, [], [fac_kingdom_4]], 
["eagle_saint_hardship_seminary", "Eagle Saint Hardship Seminary", [("faction_knight_order_4_2", 0)], 0, 0, 1000, difficulty(1)|abundance(2)|thrust_damage(26, 0)|swing_damage(76, 0), 0, [], [fac_kingdom_4]], #鹰圣苦修会


######食莲人沙龙#####
###
["kingdom_4_4", "Lotus Eater", [("faction_kingdom_4_4", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(5, 1)|swing_damage(23, 1), 0, [], [fac_kingdom_4]], 


######人类狩猎者#####
###
["human_hunter", "Hunman Hunter", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(32, 1)|swing_damage(40, 1), 0, [], [fac_kingdom_4]],




##########################################################教皇国#####################################################
["kingdom_5", "kingdom_5", [("faction_kingdom_5", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(1)|thrust_damage(86, 0)|swing_damage(85, 0), 0, [], [fac_kingdom_5]], 

######圣廷#####
###
["kingdom_5_1", "Holy See", [("faction_kingdom_5_1", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(85, 0)|swing_damage(73, 0), 0, [], [fac_kingdom_5]], 
#圣骑士团
["order_of_holy_knight", "Order of Holy Knight", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 

#宗座骑士团
["knight_order_5_1", "Knight Order of Pontiff", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 
#圣誓剑勇团
["order_of_godward_warrior", "Order of Godward Warrior", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 
#永眠回廊
["eternal_galleries", "Eternal Galleries", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 
#弓圣遗泽射手团
["legacy_of_the_bow_saint", "Legacy of the Bow Saint", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(2)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 

######证信宗#####
###
["kingdom_5_2", "Verification Sect", [("faction_kingdom_5_2", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(80, 0)|swing_damage(70, 0), 0, [], [fac_kingdom_5]], 
#狩魔骑士团
["knight_order_5_2", "Knight Order of Hunter", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(83, 0)|swing_damage(63, 0), 0, [], [fac_kingdom_5]], 
["heretic_killer", "heretic_killer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], #异端猎手队
#宗教审判局
["religious_trial_bureau", "Religious Trial Bureau", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 
#罪奴辅助军团
["sin_slave_legion", "Sin Slave Legion", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 
#噬罪秘修会
["sect_of_devouring_sin", "Sect of Devouring Sin", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(3)|thrust_damage(70, 0)|swing_damage(51, 0), 0, [], [fac_kingdom_5]], 

######真信施洗会#####
###
["kingdom_5_3", "True Faith Baptist", [("faction_kingdom_5_3", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(82, 0)|swing_damage(65, 0), 0, [], [fac_kingdom_5]], 
#庇护骑士团
["knight_order_5_3", "Knight Order of Patron", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(70, 0)|swing_damage(90, 0), 0, [],[fac_kingdom_5]], 
["chaney_cavalry_army", "Chaney Cavalry Army", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], #查尼枪骑兵团

#萨顿卫兵团
["sutton_guard", "Sutton Guard", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 

#绘盾人
["shield_drawing_man", "Shield Drawing Man", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 

######神哲修道宗#####
###
["kingdom_5_4", "Deism Philosophical Order", [("faction_kingdom_5_4", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(73, 0)|swing_damage(78, 0), 0, [], [fac_kingdom_5]], 
#奥术骑士团
["knight_order_5_4", "Knight Order of Arcane", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(60, 0)|swing_damage(81, 0), 0, [],[fac_kingdom_5]], 

#哲学之卵学派
["egg_of_philosophy_school", "Egg of Philosophy School", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 

######圣别渴求者#####
###
["kingdom_5_5", "Sanctification Seeker", [("faction_kingdom_5_5", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(50, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 
#圣歌骑士团
["knight_order_5_5", "Knight Order of Hymn", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(76, 0)|swing_damage(77, 0), 0, [], [fac_kingdom_5]], 

#圣痕商会
["holy_scar_chamber_of_commerce", "Holy Scar Chamber of Commerce", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(2)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 
#剔圣人
["holy_picking_man", "Holy Picking Man", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_5]], 

######外省教友互助会#####
###
["kingdom_5_6", "kingdom_5_6", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(60, 0)|swing_damage(83, 0), 0, [], [fac_kingdom_5]], 





##########################################################东方龙树#####################################################
["kingdom_6", "kingdom_6", [("pic_sarranid_arms", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(1)|thrust_damage(90, 0)|swing_damage(78, 0), 0, [], [fac_kingdom_6]], 





#######################################################斯塔胡克大公国#####################################################
["kingdom_7", "kingdom_7", [("faction_kingdom_7", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(69, 0)|swing_damage(73, 0), 0, [], [fac_kingdom_7]], 

######白塔党#####
###
["kingdom_7_1", "Party of Tower", [("faction_kingdom_7", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(65, 0)|swing_damage(63, 0), 0, [], [fac_kingdom_7]], 
#血勋铁卫队
["knight_order_7_1", "Bloodhonor Iron Guard", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(56, 0)|swing_damage(66, 0), 0, [], [fac_kingdom_7]], 

#血湖之庭
["blood_lake_court", "Blood Lake Court", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(56, 0)|swing_damage(66, 0), 0, [], [fac_kingdom_7]], 
#英穹塔内势力
["blocked_fortress", "Blocked Fortress", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0),0, [], [fac_kingdom_7]], #闭锁之堡
#其他军事力量
["blood_hunter", "Blood Hunter", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(40, 0)|swing_damage(75, 0), 0, [], [fac_kingdom_7]], #戒血执法者


######斯塔胡克商业联合#####
###
["kingdom_7_2", "Starkhook Commercial Union", [("faction_kingdom_7_2", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(55, 0)|swing_damage(43, 0), 0, [], [fac_kingdom_7]], 
#猩红满月骑士团
["knight_order_of_scarlet_full_moon", "Knight Order of Scarlet Full Moon", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(56, 0)|swing_damage(66, 0), 0, [], [fac_kingdom_7]], 


######蛇夫党#####
###
["kingdom_7_3", "Ophiuchus", [("faction_kingdom_7_3", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(47, 0)|swing_damage(9, 1), 0, [], [fac_kingdom_7]], 





##########################################################自由城邦#####################################################
["kingdom_8", "kingdom_8", [("faction_kingdom_default", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(65, 0)|swing_damage(58, 0), 0, [], [fac_kingdom_8]], 

######城邦直属#####
###裁决之锤
["hammer_of_judgment", "hammer_of_judgment", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(65, 0)|swing_damage(71, 0), 0, [], [fac_hammer_of_judgment]], 

###权杖下马骑士团
["knight_order_8_1", "Knight Order of Scepter", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(75, 0)|swing_damage(43, 0), 0, [], [fac_kingdom_8]], 

######归宗派#####
###
["kingdom_8_1", "kingdom_8_1", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(75, 0)|swing_damage(50, 0), 0, [], [fac_kingdom_8]], 
#古力奥妖妇团
["guilio_vamp", "Guilio Vamp", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(5, 0)|swing_damage(13, 0), 0, [], [fac_kingdom_8]], 


######西求派#####
###
["kingdom_8_2", "kingdom_8_2", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(61, 0)|swing_damage(53, 0), 0, [], [fac_kingdom_8]], 
#裂空狙击团
["skytear_sniper_army", "Skytear Sniper Army", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(1)|abundance(1)|thrust_damage(11, 0)|swing_damage(3, 1), 0, [], [fac_kingdom_8]], 

######愚人派#####
###
["kingdom_8_3", "kingdom_8_3", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(35, 0)|swing_damage(90, 0), 0, [], [fac_kingdom_8]], 





##########################################################玩家派系#####################################################
["player_supporters_faction", "player_supporters_faction", [("faction_kingdom_default", 0)], itp_country_power, 0, 1000, difficulty(4)|abundance(2)|thrust_damage(0, 0)|swing_damage(0, 0), 0, [], [fac_kingdom_1]], 





##########################################################不死者结社#####################################################
["undead_association", "undead_association", [("faction_undead_association", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(15, 0)|swing_damage(23, 0), 0, [], [fac_heresy_undead]], 

######莉达·采尼的派阀#####
###
["beheading_necromancer", "beheading_necromancer", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 

#人类商会和佣兵团
["derlin_mercenary_corps", "derlin_mercenary_corps", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(15, 0)|swing_damage(34, 0), 0, [], [fac_heresy_undead]], #德林商会
["agouti_commerce_chamber", "agouti_commerce_chamber", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(23, 0)|swing_damage(42, 0), 0, [], [fac_heresy_undead]], #刺鼠商会
["dusk_locker_mercenary_corps", "dusk_locker_mercenary_corps", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(20, 0)|swing_damage(28, 0), 0, [], [fac_heresy_undead]], #黄昏之锁商会


######枯派#####
###
["zombie_clique", "zombie_clique", [("faction_zombie_clique", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(25, 0)|swing_damage(18, 0), 0, [], [fac_heresy_undead]], 
#泰斗级
["armor_necromancer", "armor_necromancer", [("faction_armor_necromancer", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
["power_necromancer", "power_necromancer", [("faction_power_necromancer", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
#教授级
["defend_necromancer", "defend_necromancer", [("faction_defend_necromancer", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 


######骸派#####
###
["skeleton_clique", "skeleton_clique", [("faction_skeleton_clique", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(35, 0)|swing_damage(18, 0), 0, [], [fac_heresy_undead]],
#泰斗级
["element_necromancer", "element_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
["inflammation_necromancer", "inflammation_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
#教授级
["shower_necromancer", "shower_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
["storm_necromancer", "storm_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 


######魂派#####
###
["fantom_clique", "fantom_clique", [("faction_fantom_clique", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(22, 0)|swing_damage(17, 0), 0, [], [fac_heresy_undead]], 
#泰斗级
["shattered_necromancer", "shattered_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
#教授级
["cyan_necromancer", "cyan_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 
["shadow_necromancer", "shadow_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [],[fac_heresy_undead]], 


######腐派#####
###
["walker_clique", "walker_clique", [("faction_walker_clique", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(95, 1)|swing_damage(91, 1), 0, [], [fac_heresy_undead]], 
#泰斗级
["turbid_necromancer", "turbid_necromancer", [("faction_kingdom_default", 0)], 0, 0, 0, difficulty(1)|abundance(1)|thrust_damage(50, 0)|swing_damage(2, 0), 0, [], [fac_heresy_undead]], 





##########################################################巫蛊世家#####################################################
["witchcraft_aristocrat", "witchcraft_aristocrat", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(31, 1)|swing_damage(10, 1), 0, [], [fac_heresy_witchcraft]], 




##########################################################赤铜孑遗#####################################################
["barecopper_relict", "barecopper_relict", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(25, 1)|swing_damage(53, 1), 0, [], [fac_heresy_eclipse]], 
["gold_adeptus", "gold_adeptus", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(60, 0)|swing_damage(75, 1), 0, [], [fac_heresy_mammonism]], 





##########################################################渊海异种#####################################################
["abyssal_order", "abyssal_order", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(1)|thrust_damage(65, 0)|swing_damage(13, 0), 0, [], [fac_outlaws_abyssal]], 

######深海巨蟒船团#####
###
["abyssal_pirate", "abyssal_pirate", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(25, 0)|swing_damage(5, 1), 0, [], [fac_outlaws_abyssal]], 


######不死者溺派#####
###
["drowner_clique", "drowner_clique", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(16, 0)|swing_damage(41, 0), 0, [], [fac_heresy_undead]], 





##########################################################热砂的末裔#####################################################
["desertus_tribe", "desertus_tribe", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(45, 0)|swing_damage(36, 0), 0, [], [fac_outlaws_desert]], 

######应许绿洲#####
###
["desertus_bandit", "desertus_bandit", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(40, 1)|swing_damage(13, 1), 0, [], [fac_outlaws_desert]], 





###########################################################失落灵树#####################################################
["yishith_rebel", "yishith_rebel", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(75, 0)|swing_damage(83, 0), 0, [], [fac_kingdom_1]], 





##########################################################法外骑士团#####################################################
["robber_knight", "robber_knight", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(3)|thrust_damage(22, 0)|swing_damage(24, 1), 0, [], [fac_outlaws_robber_knight]], 





##########################################################科鲁托浪民#####################################################
["kouruto_refugee", "kouruto_refugee", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(3)|abundance(2)|thrust_damage(48, 0)|swing_damage(71, 0), 0, [], [fac_outlaws_kouruto_refugee]], 





############################################################拜星教#####################################################
["sabianism", "sabianism", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(1)|thrust_damage(0, 0)|swing_damage(0, 0), 0, [], [fac_heresy_sabianism]], 





###########################################################安基亚蛮族#####################################################
["ankiya_barbarian", "ankiya_barbarian", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(28, 0)|swing_damage(17, 0), 0, [], [fac_outlaws_ankiya]], 





###########################################################丧钟刺客团#####################################################
["deathbell", "deathbell", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(2)|thrust_damage(25, 0)|swing_damage(11, 0), 0, [], [fac_deathbell]], 






###########################################################边缘人#####################################################
["outlawers", "Outlawers", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(5)|abundance(0)|thrust_damage(19, 1)|swing_damage(28, 1), 0, [], [fac_outlaws_bandit]], 

######盗拾者集团#####
###
["burglar_scavenger", "burglar_scavenger", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(0)|thrust_damage(29, 1)|swing_damage(12, 1), 0, [],[fac_outlaws_bandit]], 

######养皮人#####
###
["skin_raiser", "Skin Raiser", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(3)|thrust_damage(19, 1)|swing_damage(28, 1), 0, [], [fac_outlaws_bandit]], 






###########################################################自生者#####################################################
["ownerless_one", "ownerless_one", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(5)|abundance(0)|thrust_damage(19, 1)|swing_damage(28, 1), 0, [], [fac_monster]], 

######龙孽#####
###
["dragon_abomination", "Dragon Abomination", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(2)|abundance(0)|thrust_damage(40, 1)|swing_damage(15, 1), 0, [], [fac_monster]], 

######绯世#####
###
["crimson_world", "Crimson World", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(4)|abundance(0)|thrust_damage(56, 0)|swing_damage(66, 0), 0, [], [fac_monster]], 

######谬史#####
###
["erroneous_history", "Erroneous history", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(4)|abundance(0)|thrust_damage(56, 0)|swing_damage(66, 0), 0, [], [fac_monster]], 






###########################################################庸众凡夫#####################################################
["normal_people", "Normal People", [("faction_kingdom_default", 0)], 0, 0, 1000, difficulty(5)|abundance(3)|thrust_damage(19, 1)|swing_damage(28, 1), 0, [], [fac_heresy_undead]], 





["faction_end", "faction_end", [("faction_kingdom_default", 0)], 0, 0, 1000, weight(10.000000)|abundance(0)|max_ammo(0)|food_quality(0), 0], 





##########################################################文化##########################################################
["culture_powell", "Culture Powell", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #普威尔
["culture_elf", "Culture Elf", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #精灵
["culture_therianthropy_tribe", "Culture Therianthropy Tribe", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #兽人部落
["culture_confederation", "Culture Confederation", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #邦联
["culture_papal", "Culture Papal", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #教皇国
["culture_east", "Culture East", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #东方
["culture_westcoast", "Culture Westcoast", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #西海
["culture_state", "Culture State", [("sorcery_11_1", 0)], 0, 0, 0, abundance(1), imodbits_none], #城邦

["culture_end", "culture_end", [("sorcery_11_1", 0)], 0, 0, 0, abundance(10), imodbits_none], 
]