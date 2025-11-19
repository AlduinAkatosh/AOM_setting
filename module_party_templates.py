# -*- coding: UTF-8 -*-

from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_outlaws,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer, 10, 20, 0),(trp_peasant_woman, 0, 4, 0),(trp_blackiron_adventurer, 5, 12, 0),(trp_barecopper_adventurer, 0, 5, 0)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
# Ryan END
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

##kouruto refugees
  ("steppe_bandits", "Kouruto Refugee Plunder", icon_khergit|pf_show_faction|carries_goods(2), 0, fac_commoners, 312, [(trp_kouruto_refugee_looter, 8, 18, 0),(trp_kouruto_refugee_thief, 6, 23, 0),(trp_steppe_bandit, 8, 22, 0),(trp_kouruto_human_settler, 1, 3, 1)]),

##Abyssal pirates
  ("sea_raiders", "Sea Raiders", icon_axeman|pf_show_faction|carries_goods(2), 0, fac_commoners, 312, [(trp_abyssal_plunder_captain, 1, 1, 0),(trp_abyssal_horseman, 3, 15, 0),(trp_abyssal_priate_warrior, 2, 18, 0),(trp_abyssal_axeman, 3, 24, 0),(trp_abyssal_axe_thrower, 0, 18, 0),(trp_abyssal_sailor, 4, 30, 0)]),

##Ankiya
  ("taiga_bandits", "Ankiya Looter", icon_axeman|pf_show_faction|carries_goods(2), 0, fac_commoners, 312, [(trp_ankiya_looter_leader, 1, 1, 0),(trp_ankiya_warrior, 5, 12, 0),(trp_ankiya_barbarian, 15, 24, 0),(trp_taiga_bandit, 8, 35, 0),(trp_diemer_freeman, 1, 3, 1)]),

##Desert bandits
  ("desert_bandits", "Desert Bandits", icon_vaegir_knight|pf_show_faction|carries_goods(2), 0, fac_commoners, 312, [(trp_desert_leader, 1, 1, 0),(trp_desert_thief, 3, 22, 0),(trp_desert_bandit, 4, 38, 0)]),

##Forest bandits
  ("forest_bandits", "Forest Bandits", icon_axeman|pf_show_faction|carries_goods(2), 0, fac_commoners, 312, [(trp_forest_bandit, 2, 30, 0),(trp_mountain_bandit, 4, 40, 0)]),

##Bandit
  ("looters", "Looters", icon_axeman|pf_show_faction|carries_goods(8), 0, fac_commoners, 312, [(trp_looter, 3, 45, 0)]),
  ("mountain_bandits", "Bandit", icon_axeman|pf_show_faction|carries_goods(2), 0, fac_commoners, 312, [(trp_bandit_leader, 0, 1, 0),(trp_brigand, 2, 18, 0),(trp_bandit, 4, 32, 0),(trp_looter, 0, 12, 0),(trp_powell_nobility, 0, 1, 1)]),

##Deserters
  ("deserters", "Deserters", icon_vaegir_knight|pf_show_faction|carries_goods(3), 0, fac_commoners, 312, []),

##Manhunters
  ("manhunters", "Manhunters", icon_gray_knight|pf_show_faction, 0, fac_manhunters, aggressiveness_8|aggressiveness_0|courage_9, [(trp_manhunter, 9, 40, 0)]),




  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_starkhook_mercenary,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_starkhook_mercenary,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_starkhook_mercenary,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_starkhook_armoured_crossbowman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total




##########################################################联合王国######################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_1_reinforcements_a", "kingdom 1 reinforcements a", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                  #145到178人
    (trp_powell_nobility, 5, 8, 0), #普威尔贵族
    (trp_powell_horseman, 15, 20, 0), #普威尔骑手
    (trp_powell_footman, 20, 25, 0), #普威尔步兵
    (trp_powell_huntsman, 10, 15, 0), #普威尔猎人
    (trp_powell_militia, 35, 40, 0), #普威尔民兵
    (trp_powell_peasant, 60, 70, 0), #普威尔平民
   ]),
("kingdom_1_reinforcements_b", "kingdom 1 reinforcements b", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                  #140到176人
    (trp_powell_noble_trainee, 5, 8, 0), #普威尔贵族习武者
    (trp_powell_conjuring_rider, 20, 25, 0), #普威尔术骑手
    (trp_powell_conjuring_infantry, 40, 50, 0), #普威尔术步兵
    (trp_powell_skirmisher, 20, 22, 0), #普威尔散兵
    (trp_powell_horseman, 25, 28, 0), #普威尔骑手
    (trp_powell_footman, 30, 33, 0), #普威尔步兵
   ]),
("kingdom_1_reinforcements_c", "kingdom 1 reinforcements c", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                  #141到161人
    (trp_powell_noble_knight, 5, 7, 0), #普威尔贵胄骑士
    (trp_powell_armored_conjurer, 6, 8, 0), #普威尔铠甲术士
    (trp_powell_windscorching_lancer, 25, 28, 0), #普威尔风炎枪骑兵
    (trp_powell_rockglacier_ranger, 20, 23, 0), #普威尔冰岩枪骑兵
    (trp_powell_conjuring_infantry, 55, 60, 0), #普威尔术步兵
    (trp_powell_conjuring_rider, 30, 35, 0), #普威尔术骑手
   ]),
##—————————————————————————————普威尔王都市民—————————————————————————————
##
("kingcity_citizen_reinforcements_a", "kingcity citizen reinforcements a", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                  #133到159人
    (trp_powell_bodyguard, 7, 9, 0), #普威尔近侍
    (trp_powell_court_nobility, 18, 20, 0), #普威尔宫廷贵族
    (trp_powell_strike_swordman, 30, 33, 0), #普威尔突击剑士
    (trp_powell_heavy_infantry, 26, 28, 0), #普威尔重步兵
    (trp_powell_armed_footman, 35, 40, 0), #普威尔武装步兵
    (trp_powell_kingcity_citizen, 17, 19, 0), #普威尔王都市民
   ]),
("kingcity_citizen_reinforcements_b", "kingcity citizen reinforcements b", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                  #123到138人
    (trp_powell_court_knight, 2, 4, 0), #普威尔内府骑士
    (trp_powell_praetorian, 4, 6, 0), #普威尔贵族禁卫
    (trp_powell_great_swordman, 13, 15, 0), #普威尔大剑师
    (trp_powell_halberd_cavalry, 24, 27, 0), #普威尔戟骑兵
    (trp_powell_sword_cavalry, 30, 33, 0), #普威尔剑骑兵
    (trp_powell_halberd_infantry, 50, 53, 0), #普威尔戟兵
   ]),
##肃正之镰
("eliminater_reinforcements", "eliminater reinforcements", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                  #138到154人
    (trp_eliminater_knight, 2, 4, 0), #肃正骑士
    (trp_eliminater_vanguard, 10, 13, 0), #肃正尖兵
    (trp_eliminater_recruit, 15, 17, 0), #肃正军士
    (trp_powell_executioner, 17, 20, 0), #普威尔行刑官
    (trp_eliminater_recruit, 44, 47, 0), #肃正新兵
    (trp_powell_headsman, 50, 53, 0), #普威尔刽子手
   ]),
##———————————————————————————罗德里格斯公国模板—————————————————————————————
##
("rodriguez_duchy_reinforcements_a", "rodriguez duchy reinforcements a", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #154到178人
    (trp_elemental_attendant, 5, 7, 0), #元素侍从
    (trp_red_dolphin_worrier, 12, 15, 0), #红海豚卫士
    (trp_red_dolphin_attendant, 20, 23, 0), #红海豚侍从
    (trp_lesaff_axe_warrior, 27, 30, 0), #勒塞夫斧战士
    (trp_lesaff_shipboard_infantry, 40, 43, 0), #勒塞夫船上步兵
    (trp_lesaff_armed_sailor, 50, 60, 0), #勒塞夫武装水手
   ]),
("rodriguez_duchy_reinforcements_b", "rodriguez duchy reinforcements b", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #121到145人
    (trp_elemental_knight, 2, 3, 0), #元素骑士
    (trp_red_dolphin_banneret, 4, 8, 0), #红海豚方旗骑士
    (trp_elemental_ranger, 8, 12, 0), #元素游侠
    (trp_red_dolphin_knight, 17, 20, 0), #红海豚骑士
    (trp_lesaff_iron_axe_sergeant, 30, 35, 0), #勒塞夫铁斧军士
    (trp_grenier_longbow_archer, 60, 67, 0), #戈兰尼尔长弓手
   ]),
##血火佣兵团模板
("bloodfire_mercenary_reinforcements", "bloodfire mercenary reinforcements", 
   0, 0, fac_commoners, aggressiveness_0, [                   #125到170人
    (trp_bloodfire_berserker_warrior, 25, 35, 0), #血火狂战勇士
    (trp_bloodfire_vanguard, 30, 40, 0), #血火先锋
    (trp_bloodfire_mercenary_corps_veteran, 40, 50, 0), #血火佣兵团老手
    (trp_mercenary_skirmisher, 20, 30, 0), #雇佣散兵
    (trp_watchman, 10, 15, 0), #眼线
   ]),
##戈兰尼尔民兵自卫军模板
("grenier_militia_reinforcements", "grenier militia reinforcements", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #160到183人
    (trp_grenier_chivalric_knight, 5, 8, 0), #戈兰尼尔侠义骑士
    (trp_grenier_longbow_archer, 25, 30, 0), #戈兰尼尔长弓手
    (trp_grenier_rider, 20, 25, 0), #戈兰尼尔骑手
    (trp_grenier_wellselected_militia, 50, 55, 0), #戈兰尼尔精选民兵
    (trp_grenier_militia, 60, 65, 0), #戈兰尼尔民兵
   ]),
##———————————————————————————北境开拓领模板—————————————————————————————
##
("northern_reclaimer_reinforcements_a", "northern reclaimer reinforcements a", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #155到177人
    (trp_northern_hunter, 23, 27, 0), #北境猎人
    (trp_northern_serf_infantry, 22, 25, 0), #北境农奴步兵
    (trp_northern_serf, 38, 42, 0), #北境农奴
    (trp_northern_crossbowman, 17, 20, 0), #北境弩手
    (trp_northern_infantry, 25, 23, 0), #北境步兵
    (trp_northern_militia, 30, 40, 0), #北境民兵
   ]),
("northern_reclaimer_reinforcements_b", "northern reclaimer reinforcements b", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #142到162人
    (trp_northern_tower_shield_sergeant, 26, 30, 0), #北境塔盾军士
    (trp_northern_serf_rider, 24, 29, 0), #北境农奴骑手
    (trp_dragon_scout, 30, 33, 0), #寻龙猎手
    (trp_revenge_iron_hoof, 25, 30, 0), #复仇铁骑
    (trp_northern_heavy_crossbow_shooter, 37, 40, 0), #北境强弩攻坚手
   ]),
("northern_reclaimer_reinforcements_c", "northern reclaimer reinforcements c", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #108到138人
    (trp_dragonblood_knight, 1, 3, 0), #龙血骑士
    (trp_hometownless_knight, 13, 17, 0), #无乡骑士
    (trp_northern_ministeriales, 20, 25, 0), #北境农奴骑士
    (trp_powell_dragon_archer, 34, 38, 0), #普威尔猎龙射手
    (trp_northern_cavalry, 40, 55, 0), #北境枪骑兵
   ]),
##龙孽囚兵领模板
("brand_dragonmania_reinforcements", "brand dragonmania reinforcements", 
   0, 0, fac_monster, aggressiveness_0, [                   #80到101人
    (trp_extinction_tornado, 0, 1, 0), #灭绝龙卷
    (trp_brand_dragon_abomination, 10, 13, 0), #烙印龙孽
    (trp_brand_dragonfrenzy, 28, 32, 0), #烙印龙狂
    (trp_brand_dragonmania, 42, 55, 0), #烙印龙癫
   ]),
##———————————————————————————普属自由城邦模板—————————————————————————————
##
("powell_state_reinforcements", "powell state reinforcements", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #150到181人
    (trp_preist_noble_cavalry, 8, 14, 0), #奉神城贵胄骑兵
    (trp_preist_horseback_crossbow_sergeant, 15, 19, 0), #奉神城骑弩军士
    (trp_preist_attendant, 20, 23, 0), #奉神侍从
    (trp_preist_noble_crossbowman, 32, 35, 0), #奉神城贵胄弩手
    (trp_preist_infantry, 35, 40, 0), #奉神城步兵
    (trp_preist_porter, 40, 50, 0), #奉神城门卫
   ]),
##普威尔正教会模板
("powell_orthodox_reinforcements", "powell orthodox reinforcements", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #146到178人
    (trp_powell_armour_divineguider, 6, 9, 0), #普威尔圣军士
    (trp_powell_orthodox_zealot, 21, 25, 0), #普威尔正教狂信徒
    (trp_powell_military_divineguider, 25, 29, 0), #普威尔军事神术使
    (trp_powell_conscripted_therapist, 30, 35, 0), #普威尔治疗师
    (trp_powell_parishioner_warrier, 44, 50, 0), #普威尔教友战士
    (trp_powell_novice_divineguider, 20, 30, 0), #普威尔新手神术使
   ]),
##———————————————————————————南沙公国模板—————————————————————————————
##
("sousanth_duchy_reinforcements_a", "sousanth duchy reinforcements a", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #146到183人
    (trp_sousanth_servant, 15, 18, 0), #南沙仆从
    (trp_araiharsa_mercenary_infantry, 24, 27, 0), #阿利哈沙雇佣步兵
    (trp_sousanth_rider, 15, 19, 0), #南沙骑手
    (trp_sousanth_guard, 17, 23, 0), #南沙城卫队
    (trp_sousanth_militia, 35, 40, 0), #南沙民兵
    (trp_powell_rogue_farmer, 40, 56, 0), #普威尔无赖农民
   ]),
("sousanth_duchy_reinforcements_b", "sousanth duchy reinforcements b", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #141到163人
    (trp_sandboat_knight, 4, 8, 0), #沙舟骑士
    (trp_gurorrion_guard, 22, 24, 0), #古洛隆卫士
    (trp_sousanth_darts_sergeant, 35, 40, 0), #南沙战镖军士
    (trp_araiharsa_mercenary_rider, 40, 45, 0), #阿利哈沙雇佣骑手
    (trp_sousanth_elite_bowman, 40, 46, 0), #南沙精锐射手
   ]),
##———————————————————————————龙神教模板—————————————————————————————
##
("dragon_worship_reinforcements_a", "dragon worship reinforcements a", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                   #143到170人
    (trp_dragonword_practitioner, 13, 17, 0), #龙言修习者
    (trp_dragon_blood_swordsman, 27, 31, 0), #龙血剑士
    (trp_sedative_pavilion_maid, 3, 6, 0), #镇静公馆侍女
    (trp_sedative_pavilion_nurse, 8, 12, 0), #镇静公馆护士
    (trp_dragon_god_follower, 40, 50, 0), #龙神追随者
    (trp_dragon_power_worshipper, 52, 54, 0), #龙力崇拜者
   ]),
("dragon_worship_reinforcements_b", "dragon worship reinforcements b", 
   0, 0, fac_kingdom_1, aggressiveness_0, [                    #42到61人
    (trp_dragonword_great_presbyter, 5, 9, 0), #龙吼大司祭
    (trp_dragonwings_knight, 12, 16, 0), #龙翼骑士
    (trp_dragon_power_great_swordman, 14, 18, 0), #龙力大剑师
    (trp_tranquility_chief_physician, 1, 2, 0), #安宁主治
    (trp_sedative_pavilion_physician, 10, 16, 0), #镇静公馆医师
   ]),



############################################################公国######################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_2_reinforcements_a", "kingdom 2 reinforcements a", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #154到172人
    (trp_yishith_elf_woodguard, 4, 8, 0), #伊希斯精灵巡林者
    (trp_yishith_human_cavalry, 32, 34, 0), #伊希斯人类马兵
    (trp_yishith_human_infantry, 43, 46, 0), #伊希斯人类步兵
    (trp_yishith_human_militia, 43, 45, 0), #伊希斯征召民兵
    (trp_yishith_human_resident, 32, 39, 0), #伊希斯人类居民
   ]),
("kingdom_2_reinforcements_b", "kingdom 2 reinforcements b", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #124到154人
    (trp_yishith_elf_woodguard, 13, 20, 0), #伊希斯精灵巡林者
    (trp_yishith_elf_skirmisher, 23, 28, 0), #伊希斯精灵散兵
    (trp_yishith_elf_hunter, 20, 25, 0), #伊希斯精灵猎户
    (trp_yishith_inferior_elf, 26, 31, 0), #伊希斯劣等精灵
    (trp_yishith_human_heavyinfantry, 42, 50, 0), #伊希斯人类重步兵
   ]),
("kingdom_2_reinforcements_c", "kingdom 2 reinforcements c", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #125到145人
    (trp_yishith_elf_outrider, 12, 18, 0), #伊希斯精灵巡狩
    (trp_yishith_jungleslaughterer, 16, 20, 0), #伊希斯密林游猎
    (trp_yishith_elf_woodguard, 21, 25, 0), #伊希斯精灵巡林者
    (trp_yishith_human_cavalry, 32, 34, 0), #伊希斯人类马兵
    (trp_yishith_human_guard, 44, 48, 0), #伊希斯盾兵
   ]),
##———————————————————————————————灵魄之灵树———————————————————————————————
##
("spirittree_of_soul_reinforcements_a", "spirittree of soul reinforcements a", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #128到151人
    (trp_yishith_elf_outrider, 6, 8, 0), #伊希斯骑士侍从
    (trp_soul_full_elf, 4, 7, 0), #灵魄之树纯血精灵
    (trp_seddlined_crazy_cavalry, 22, 28, 0), #灵苗狂骑兵
    (trp_seddlined_puppet, 42, 48, 0), #灵芽傀儡
    (trp_seddlined_thrall, 54, 60, 0), #灵芽隶从
   ]),
("spirittree_of_soul_reinforcements_b", "spirittree of soul reinforcements b", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #101到130人
    (trp_spirittree_knight, 1, 3, 0), #灵树骑士
    (trp_seddlined_apostle, 8, 11, 0), #灵花使徒
    (trp_seddlined_dare_to_die_corp, 17, 22, 0), #灵花决死剑士
    (trp_yishith_spiritual_horse_knight, 14, 19, 0), #伊希斯灵马骑士
    (trp_seddlined_puppet, 61, 75, 0), #灵苗死士
   ]),
##———————————————————————————————死亡之灵树———————————————————————————————
##
("spirittree_of_demise_reinforcements_a", "spirittree of demise reinforcements a", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #151到174人
    (trp_hotbed_gatekeeper, 6, 9, 0), #温床守门人
    (trp_demise_full_elf, 3, 6, 0), #死亡之树纯血精灵
    (trp_humic_vanguard, 16, 20, 0), #腐殖先锋
    (trp_humic_walker, 17, 20, 0), #腐殖行者
    (trp_root_borning_one, 54, 59, 0), #根生者
    (trp_living_root, 55, 60, 0), #活根
   ]),
("spirittree_of_demise_reinforcements_b", "spirittree of demise reinforcements b", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #128到155人
    (trp_spiritrain_ranger, 1, 3, 0), #灵雨游侠
    (trp_demise_gardener, 7, 10, 0), #死亡园丁
    (trp_humus_lord, 17, 23, 0), #腐土领主
    (trp_hotbed_farmer, 16, 19, 0), #温床护苗人
    (trp_hotbed_hollow, 37, 40, 0), #温床幽魂
    (trp_humic_walker, 50, 60, 0), #腐殖行者
   ]),
##———————————————————————————————先祖之灵树———————————————————————————————
##
("molter_legion_reinforcements", "molter legion reinforcements", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #176到205人
    (trp_molter_knight, 2, 3, 0), #蜕生骑士
    (trp_yishith_crossbow_ranger, 11, 15, 0), #伊希斯弩游侠
    (trp_yishith_crossbowman, 26, 32, 0), #伊希斯弩手
    (trp_yishith_sword_armedman, 30, 35, 0), #伊希斯剑甲兵
    (trp_yishith_swordman, 40, 50, 0), #伊希斯剑士
    (trp_half_molter, 67, 70, 0), #半蜕生者
   ]),
("spirittree_of_ancester_reinforcements", "spirittree of ancester reinforcements", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #118到146人
    (trp_immortal_assassin, 1, 3, 0), #永世者刺客
    (trp_yishith_heavy_ranger, 11, 15, 0), #伊希斯重甲游侠
    (trp_yishith_elf_heavy_cavalry, 17, 20, 0), #伊希斯精灵重骑兵
    (trp_yishith_elf_sergeant, 23, 29, 0), #伊希斯精灵军士
    (trp_ancester_full_elf, 13, 16, 0), #先祖之树纯血精灵
    (trp_yishith_sword_dancer, 53, 66, 0), #伊希斯剑舞者
   ]),
##———————————————————————————————生命之灵树———————————————————————————————
##
("yishith_westcoast_militia_reinforcements", "Yishith Westcoast Militia reinforcements", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #159到195人
    (trp_yishith_throwing_axe_ranger, 4, 7, 0), #伊希斯飞斧游侠
    (trp_yishith_sentry_cavalry, 9, 13, 0), #伊希斯哨戒骑兵
    (trp_yishith_recruiting_rider, 23, 30, 0), #伊希斯募集骑手
    (trp_vita_shield_axe_guardian, 27, 33, 0), #生命之都盾斧卫士
    (trp_yishith_boat_guard, 36, 42, 0), #伊希斯船队护卫
    (trp_yishith_armed_sailor, 60, 70, 0), #伊希斯武装水手
   ]),
("spirittree_of_vita_reinforcements", "spirittree of vita reinforcements", 
   0, 0, fac_kingdom_2, aggressiveness_0, [                    #123到152人
    (trp_spiritwind_bowcavalry, 1, 3, 0), #灵风游骑士
    (trp_yishith_seawind_ranger, 7, 10, 0), #伊希斯海风游侠
    (trp_yishith_navy_archer, 24, 30, 0), #伊希斯海军射手
    (trp_yishith_chivalric_knight, 15, 20, 0), #伊希斯侠义骑士
    (trp_vita_full_elf, 26, 29, 0), #生命之树纯血精灵
    (trp_vita_shield_axe_guardian, 50, 60, 0), #生命之都盾斧卫士
   ]),



###########################################################酋长国######################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_3_reinforcements_a", "kingdom 3 reinforcements a", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #120到155人
    (trp_kouruto_therianthropy_mercenary, 20, 25, 0), #科鲁托兽人佣兵
    (trp_kouruto_stray_therianthropy, 30, 40, 0), #科鲁托离群兽人
    (trp_kouruto_young_mercenary, 40, 50, 0), #科鲁托年轻佣兵
    (trp_kouruto_human_settler, 30, 40, 0), #科鲁托人类定居者
]),
("kingdom_3_reinforcements_b", "kingdom 3 reinforcements b", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #125到150人
    (trp_kouruto_therianthropy_riding_mercenary, 20, 25, 0), #科鲁托兽人骑马佣兵
    (trp_kouruto_auxiliary_rider, 20, 25, 0), #科鲁托辅军骑手
    (trp_kouruto_auxiliary_spearman, 40, 50, 0), #科鲁托辅军矛兵
    (trp_kouruto_auxiliary_light_infantry, 45, 50, 0), #科鲁托辅军轻步兵
]),
("kingdom_3_reinforcements_c", "kingdom 3 reinforcements c", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #105到130人
    (trp_kouruto_therianthropy_mercenary_captain, 15, 20, 0), #科鲁托兽人佣兵头领
    (trp_kouruto_auxiliary_ranger, 25, 30, 0), #科鲁托辅军游骑兵
    (trp_kouruto_auxiliary_heavy_rider, 25, 30, 0), #科鲁托辅军重骑兵
    (trp_kouruto_auxiliary_longbowman, 40, 50, 0), #科鲁托辅军长弓手
]),
##————————————————————————————————图腾同盟————————————————————————————————
##部落模式模板
("tiger_tribe_reinforcements", "tiger tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #132到167人
    (trp_kouruto_sword_master, 0, 1, 0), #科鲁托剑豪
    (trp_kouruto_tiger_machete_rider, 3, 6, 0), #科鲁托虎族刀骑兵
    (trp_kouruto_tiger_berserk_saber, 4, 7, 0), #科鲁托虎族狂剑士
    (trp_kouruto_tiger_rider, 12, 16, 0), #科鲁托虎族骑手
    (trp_kouruto_tiger_saber, 13, 17, 0), #科鲁托虎族剑士
    (trp_kouruto_tiger_herdsman, 100, 120, 0), #科鲁托虎族牧民
]),
("bear_tribe_reinforcements", "bear tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #142到177人
    (trp_kouruto_earthshaker_guardian, 0, 1, 0), #科鲁托撼地守护者
    (trp_kouruto_bear_heavy_cavalry, 3, 6, 0), #科鲁托熊族重骑兵
    (trp_kouruto_bear_rider, 4, 7, 0), #科鲁托熊族骑手
    (trp_kouruto_bear_tower_shieldman, 12, 16, 0), #科鲁托熊族塔盾兵
    (trp_kouruto_bear_shieldman, 13, 17, 0), #科鲁托熊族盾手
    (trp_kouruto_bear_herdsman, 110, 130, 0), #科鲁托熊族牧民
]),
("wolf_tribe_reinforcements", "wolf tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #135到179人
    (trp_kouruto_cyclone_marauder, 0, 1, 0), #科鲁托旋风劫掠者
    (trp_kouruto_wolf_lancer, 3, 6, 0), #科鲁托狼族枪骑兵
    (trp_kouruto_wolf_rider, 3, 6, 0), #科鲁托狼族骑手
    (trp_kouruto_wolf_ranger, 12, 16, 0), #科鲁托狼族弓骑兵
    (trp_kouruto_wolf_scout, 12, 16, 0), #科鲁托狼族斥候
    (trp_kouruto_wolf_herdsman, 115, 135, 0), #科鲁托狼族牧民
]),
("lion_tribe_reinforcements", "lion tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #97到119人
    (trp_kouruto_sword_fighter, 1, 1, 0), #科鲁托剑斗士
    (trp_kouruto_gladiator, 5, 9, 0), #科鲁托角斗士
    (trp_kouruto_lion_baatur, 6, 9, 0), #科鲁托猛狮八都鲁
    (trp_kouruto_lion_warrior, 15, 20, 0), #科鲁托狮战士
    (trp_kouruto_lion_therianthropy, 70, 80, 0), #科鲁托狮兽人
]),
##改革模板
("totem_allience_reinforcements_a", "totem allience reinforcements a", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #117到145人
    (trp_kouruto_tiger_rider, 9, 14, 0), #科鲁托虎族骑手
    (trp_kouruto_bear_rider, 13, 17, 0), #科鲁托熊族骑手
    (trp_kouruto_wolf_rider, 16, 20, 0), #科鲁托狼族骑手
    (trp_kouruto_tiger_saber, 21, 26, 0), #科鲁托虎族剑士
    (trp_kouruto_bear_shieldman, 25, 30, 0), #科鲁托熊族盾手
    (trp_kouruto_wolf_scout, 33, 38, 0), #科鲁托狼族斥候
]),
("totem_allience_reinforcements_b", "totem allience reinforcements b", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #119到148人
    (trp_kouruto_sword_master, 1, 3, 0), #科鲁托剑豪
    (trp_kouruto_earthshaker_guardian, 3, 6, 0), #科鲁托撼地守护者
    (trp_kouruto_gladiator, 11, 17, 0), #科鲁托角斗士
    (trp_kouruto_tiger_berserk_saber, 24, 28, 0), #科鲁托虎族狂剑士
    (trp_kouruto_bear_tower_shieldman, 30, 34, 0), #科鲁托熊族塔盾兵
    (trp_kouruto_lion_warrior, 50, 60, 0), #科鲁托狮战士
]),
("totem_allience_reinforcements_c", "totem allience reinforcements c", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #121到148人
    (trp_kouruto_rampant_slaughterer, 2, 4, 0), #科鲁托狂鬃屠戮者
    (trp_kouruto_ragefist_obliterator, 5, 9, 0), #科鲁托怒拳碾压者
    (trp_kouruto_bloodclaw_ravager, 9, 15, 0), #科鲁托血爪突袭者
    (trp_kouruto_tiger_machete_rider, 30, 35, 0), #科鲁托虎族刀骑兵
    (trp_kouruto_bear_heavy_cavalry, 35, 40, 0), #科鲁托熊族重骑兵
    (trp_kouruto_wolf_lancer, 40, 45, 0), #科鲁托狼族枪骑兵
]),
#洪炉监视者
("furnace_watch_brigade_reinforcements", "furnace watch brigade reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #117到141人
    (trp_furnace_hunter, 2, 4, 0), #洪炉猎人
    (trp_furnace_watch_stalker, 4, 8, 0), #洪炉监视者密探
    (trp_furnace_watch_warrior, 36, 49, 0), #洪炉监视者战士
    (trp_furnace_watch_recruit, 75, 80, 0), #洪炉监视者新兵
]),
#科鲁托人类辅助军
("kouruto_auxiliary_reinforcements", "kouruto auxiliary reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #158到197人
    (trp_kouruto_auxiliary_ranger, 10, 14, 0), #科鲁托辅军游骑兵
    (trp_kouruto_auxiliary_heavy_rider, 13, 18, 0), #科鲁托辅军重骑兵
    (trp_kouruto_auxiliary_rider, 20, 25, 0), #科鲁托辅军骑手
    (trp_kouruto_auxiliary_longbowman, 30, 40, 0), #科鲁托辅军长弓手
    (trp_kouruto_auxiliary_light_infantry, 45, 50, 0), #科鲁托辅军轻步兵
    (trp_kouruto_young_mercenary, 40, 50, 0), #科鲁托年轻佣兵
]),
##————————————————————————————————麦汗族————————————————————————————————
##部落模式模板
("cow_tribe_reinforcements", "cow tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #147到170人
    (trp_kouruto_ritualist, 1, 1, 0), #科鲁托巫祭
    (trp_kouruto_bloodhoof_axe_reaver, 2, 4, 0), #科鲁托血蹄斧战士
    (trp_kouruto_ironhorn_ravager, 1, 3, 0), #科鲁托铁角狂战士
    (trp_kouruto_cow_warrior, 8, 12, 0), #科鲁托牛族战士
    (trp_kouruto_cow_axeman, 15, 20, 0), #科鲁托牛族斧手
    (trp_kouruto_cow_herdsman, 120, 130, 0), #科鲁托牛族牧民
]),
("sheep_tribe_reinforcements", "sheep tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #153到181人
    (trp_kouruto_ritualist, 1, 1, 0), #科鲁托巫祭
    (trp_kouruto_novice_shaman, 4, 7, 0), #科鲁托新手萨满
    (trp_kouruto_stonecliff_guardian, 4, 8, 0), #科鲁托岩壁戍卫
    (trp_kouruto_sheep_skirmisher, 15, 20, 0), #科鲁托羊族散兵
    (trp_kouruto_sheep_light_infantry, 19, 25, 0), #科鲁托羊族轻兵
    (trp_kouruto_sheep_herdsman, 110, 120, 0), #科鲁托羊族牧民
]),
("deer_tribe_reinforcements", "deer tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #143到171人
    (trp_kouruto_ritualist, 0, 1, 0), #科鲁托巫祭
    (trp_kouruto_novice_shaman, 8, 13, 0), #科鲁托新手萨满
    (trp_kouruto_swiftstrike_marirm, 4, 8, 0), #科鲁托游击剑士
    (trp_kouruto_deer_sword_warrior, 16, 19, 0), #科鲁托鹿族持剑勇士
    (trp_kouruto_deer_swordman, 15, 20, 0), #科鲁托鹿族佩剑牧民
    (trp_kouruto_deer_herdsman, 100, 110, 0), #科鲁托鹿族牧民
]),
("rabbit_tribe_reinforcements", "rabbit tribe reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #142到171人
    (trp_kouruto_ritualist, 0, 1, 0), #科鲁托巫祭
    (trp_kouruto_novice_shaman, 9, 14, 0), #科鲁托新手萨满
    (trp_kouruto_ambulancer, 4, 8, 0), #科鲁托伏击者
    (trp_kouruto_rabbit_slingshoter, 14, 18, 0), #科鲁托兔族弹弓手
    (trp_kouruto_rabbit_stone_thrower, 15, 20, 0), #科鲁托兔族投石手
    (trp_kouruto_rabbit_herdsman, 100, 110, 0), #科鲁托兔族牧民
]),
##————————————————————————————————金爪子帮————————————————————————————————
##
("goldclaw_reinforcements", "goldclaw reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #133到156人
    (trp_midul_knight, 1, 2, 0), #米德骑士
    (trp_midul_assassin, 2, 3, 0), #米德刺客
    (trp_kouruto_fox_blade_rdier, 20, 25, 0), #科鲁托狐族刀骑兵
    (trp_kouruto_fox_horseman, 40, 46, 0), #科鲁托狐族骑手
    (trp_kouruto_cat_killer, 22, 28, 0), #科鲁托猫族暗杀者
    (trp_kouruto_cat_hitman, 48, 52, 0), #科鲁托猫族打手
]),
##————————————————————————————————守望派————————————————————————————————
##
("sentinel_clique_reinforcements", "sentinel clique reinforcements", 
   0, 0, fac_kingdom_3, aggressiveness_0, [                    #145到176人
    (trp_kouruto_tercio_centurion, 3, 7, 0), #科鲁托战阵百夫长
    (trp_sentinel_servant, 13, 17, 0), #守望者奴仆
    (trp_kouruto_tercio_spearman, 20, 25, 0), #科鲁托战阵矛兵
    (trp_kouruto_tercio_infantry, 42, 49, 0), #科鲁托战阵步兵
    (trp_kouruto_dog_recuit, 55, 60, 0), #科鲁托犬族新兵
    (trp_kouruto_dog_herdsman, 12, 18, 0), #科鲁托犬族牧民
]),




###########################################################酋长国######################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_4_reinforcements_a", "kingdom 4 reinforcements a", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #152到190人
    (trp_confederation_slave_trainer, 2, 5, 0), #邦联奴隶训练师
    (trp_confederation_slave_footman, 20, 25, 0), #邦联奴隶步兵
    (trp_confederation_deepone_slave, 20, 25, 0), #邦联鱼人奴兵
    (trp_confederation_recruits_slave, 30, 40, 0), #邦联奴隶新兵
    (trp_confederation_fishing_serf, 40, 45, 0), #邦联渔奴
    (trp_confederation_serf, 40, 50, 0), #邦联农奴
]),
("kingdom_4_reinforcements_b", "kingdom 4 reinforcements b", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #142到169人
    (trp_confederation_slave_dominator, 2, 4, 0), #邦联奴隶调教师
    (trp_confederation_slave_perdue, 10, 15, 0), #邦联奴隶敢死军
    (trp_confederation_serf_gladiator, 30, 35, 0), #邦联奴隶斗士
    (trp_confederation_serf_warrior, 60, 70, 0), #邦联奴隶战士
    (trp_confederation_swamp_bandit, 40, 45, 0), #邦联沼泽匪兵
]),
("kingdom_4_reinforcements_c", "kingdom 4 reinforcements c", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #134到173人
    (trp_confederation_enslavement_warlock, 2, 4, 0), #邦联役奴术士
    (trp_diemer_hired_adventurer, 25, 30, 0), #迪默受雇冒险者
    (trp_meat_puppet, 17, 24, 0), #肉傀儡
    (trp_confederation_ship_looter, 40, 50, 0), #邦联袭船者
    (trp_confederation_toxin_dealer, 10, 15, 0), #邦联吐毒者
    (trp_confederation_slave_footman, 40, 50, 0), #邦联奴隶步兵
]),
##————————————————————————————————黑沼议事会————————————————————————————————
##
("black_marsh_council_reinforcements_a", "black marsh council reinforcements a", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #139到169人
    (trp_diemer_young_slaveholder, 2, 4, 0), #迪默年轻奴隶主
    (trp_diemer_shortbow_archer, 10, 14, 0), #迪默短弓手
    (trp_diemer_warrior, 17, 21, 0), #迪默战士
    (trp_diemer_light_footman, 35, 45, 0), #迪默轻步兵
    (trp_diemer_heavy_footman, 30, 35, 0), #迪默重步兵
    (trp_diemer_freeman, 45, 50, 0), #迪默自由民
]),
("black_marsh_council_reinforcements_b", "black marsh council reinforcements b", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #143到170人
    (trp_diemer_knight_retinue, 2, 4, 0), #迪默骑士扈从
    (trp_diemer_light_cavalry, 7, 11, 0), #迪默轻骑兵
    (trp_diemer_noviciate_cavalory, 19, 24, 0), #迪默见习骑兵
    (trp_diemer_swordman, 28, 34, 0), #迪默剑斗士
    (trp_diemer_grenadier, 35, 40, 0), #迪默投掷兵
    (trp_diemer_warrior, 52, 57, 0), #迪默战士
]),
("black_marsh_council_reinforcements_c", "black marsh council reinforcements c", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #131到169人
    (trp_diemer_monster_enslaving_knight, 2, 4, 0), #迪默役兽骑士
    (trp_marsh_council_guard, 15, 20, 0), #暗沼议会守卫
    (trp_diemer_guardian, 28, 33, 0), #迪默近卫
    (trp_diemer_hetairoi, 25, 32, 0), #迪默伙友骑兵
    (trp_diemer_heaveybow_marksman, 36, 40, 0), #迪默重弓手
    (trp_diemer_swordman, 35, 40, 0), #迪默剑斗士
]),
#暗沼之花佣兵团
("marsh_flower_reinforcements_a", "marsh flower reinforcements a", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #146到179人
    (trp_marsh_flower_feldweibel, 1, 1, 0), #暗沼之花军士
    (trp_confederation_hiring_conjurer, 10, 20, 0), #邦联雇佣术士
    (trp_confederation_hiring_spearman, 35, 40, 0), #邦联雇佣长枪兵
    (trp_confederation_hiring_infantry, 45, 50, 0), #邦联雇佣步兵
    (trp_confederation_new_recruit, 50, 60, 0), #邦联新募佣兵
    (trp_marsh_flower_camp_woman, 5, 8, 0), #暗沼之花随营妇女
]),
("marsh_flower_reinforcements_b", "marsh flower reinforcements b", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #142到167人
    (trp_marsh_flower_generalobrist, 1, 1, 0), #暗沼之花上校
    (trp_marsh_flower_elemental_conjurer, 15, 20, 0), #暗沼之花元素使
    (trp_marsh_flower_dopplesoldner, 32, 36, 0), #暗沼之花双薪剑士
    (trp_confederation_hiring_spearman, 40, 44, 0), #邦联雇佣长枪兵
    (trp_confederation_hiring_infantry, 45, 52, 0), #邦联雇佣步兵
    (trp_marsh_flower_hurenweibel, 9, 14, 0), #暗沼之花女中士
]),
##————————————————————————————————乌尔之子女————————————————————————————————
##
("offspring_of_uhr_reinforcements_a", "offspring of uhr reinforcements a", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #134到153人
    (trp_marsh_deepone_commander, 1, 1, 0), #大沼鱼人统领
    (trp_marsh_deepone_professional_soldier, 20, 24, 0), #大沼鱼人职业士兵
    (trp_marsh_hunter, 15, 20, 0), #大沼猎手
    (trp_marsh_deepone_self_trained_militia, 45, 50, 0), #大沼鱼人自训民兵
    (trp_marsh_deepone_freeman, 53, 58, 0), #大沼鱼人自由民
]),
("offspring_of_uhr_reinforcements_b", "offspring of uhr reinforcements b", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #124到141人
    (trp_dreadmarsh_knight, 2, 4, 0), #噩沼骑士
    (trp_deep_dread_assassin, 1, 3, 0), #深惧刺客
    (trp_marsh_venomfin_hunter, 24, 29, 0), #大沼毒鳍猎手
    (trp_dreadmarsh_warrior, 35, 40, 0), #噩沼武夫
    (trp_marsh_deepone_warrior, 60, 65, 0), #大沼鱼人勇士
]),
##————————————————————————————————净世军————————————————————————————————
##
("purifier_reinforcements_a", "purifier reinforcements a", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #135到166人
    (trp_purifier_infantry, 20, 25, 0), #净世军团步兵
    (trp_purifier_combat_pastor, 7, 12, 0), #净世军战斗牧师
    (trp_purifier_pastor, 14, 19, 0), #净世派神官
    (trp_purifier_light_soldier, 29, 35, 0), #净世军团轻甲兵
    (trp_purifier_recruit, 30, 35, 0), #净世军团新兵
    (trp_confederation_armed_faithful, 35, 40, 0), #邦联武装教友
]),
("purifier_reinforcements_b", "purifier reinforcements b", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #118到146人
    (trp_storm_follower, 3, 6, 0), #风暴追随者
    (trp_purifier_dismounted_knight, 8, 13, 0), #净世军步行骑士
    (trp_storm_servant, 10, 15, 0), #风暴仆从
    (trp_storm_white_shadow, 24, 30, 0), #风暴白影
    (trp_holy_wing_guard, 33, 38, 0), #圣翼侍卫
    (trp_purifier_ballistaman, 40, 44, 0), #净世军团弩炮手
]),
##————————————————————————————————食莲人沙龙————————————————————————————————
##
("lotus_eater_reinforcements", "lotus eater reinforcements", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #143到167人
    (trp_ankiya_rider, 8, 12, 0), #安基亚骑手
    (trp_ankiya_naturalized_noble, 11, 16, 0), #安基亚归化贵族
    (trp_ankiya_horseback_mercenary, 19, 24, 0), #安基亚骑马佣兵
    (trp_ankiya_mercenary, 25, 30, 0), #安基亚佣兵
    (trp_ankiya_recruit, 40, 45, 0), #安基亚征召兵
    (trp_ankiya_civilized_barbarian, 45, 40, 0), #安基亚开化蛮族
]),
##————————————————————————————————人类狩猎者————————————————————————————————
##
("human_hunter_reinforcements", "human hunter reinforcements", 
   0, 0, fac_kingdom_4, aggressiveness_0, [                    #139到162人
    (trp_venery_knight, 1, 1, 0), #狩猎骑士
    (trp_venery_slaver, 4, 7, 0), #狩猎奴从
    (trp_confederation_human_hunting_cavalry, 9, 14, 0), #邦联猎人骑兵
    (trp_confederation_slave_catcher_rider, 25, 30, 0), #邦联捕奴骑手
    (trp_confederation_slave_catcher_infantry, 40, 45, 0), #邦联捕奴步兵
    (trp_confederation_slave_catcher_hitman, 60, 65, 0), #邦联捕奴打手
]),




###########################################################教皇国######################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_5_reinforcements_a", "kingdom 5 reinforcements a", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #130到155人
    (trp_divine_legion_military_chaplain, 10, 15, 0), #圣教军团随军神官
    (trp_divine_legion_rider, 20, 25, 0), #圣教军团骑手
    (trp_divine_legion_infantry, 30, 35, 0), #圣教军团步兵
    (trp_divine_legion_armed_archer, 30, 35, 0), #圣教军团武装射手
    (trp_divine_legion_trained_recruit, 40, 45, 0), #圣教军团受训新兵
]),
("kingdom_5_reinforcements_b", "kingdom 5 reinforcements b", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #135到165人
    (trp_patron_warrior, 30, 35, 0), #庇护武士
    (trp_divine_legion_combat_pastor, 15, 20, 0), #圣教军团战斗牧师
    (trp_divine_legion_sergeant, 20, 25, 0), #圣教军团士官
    (trp_divine_legion_veteran, 30, 35, 0), #圣教军团老兵
    (trp_divine_legion_crossbowman, 20, 25, 0), #圣教军团弩手
    (trp_godward_swordman, 20, 25, 0), #圣誓剑士
]),
("kingdom_5_reinforcements_c", "kingdom 5 reinforcements c", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #120到150人
    (trp_patron_knight, 10, 15, 0), #庇护骑士
    (trp_divine_legion_insane_knight, 10, 15, 0), #圣教军团狂战骑士
    (trp_godward_great_swordman, 20, 25, 0), #圣誓大剑师
    (trp_patron_warrior, 40, 45, 0), #庇护武士
    (trp_divine_legion_veteran_knight, 20, 25, 0), #圣教军历战骑士
    (trp_divine_legion_insane_infantry, 20, 25, 0), #圣教军团狂战士兵
]),
("kingdom_5_reinforcements_d", "kingdom 5 reinforcements d", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #139到168人
    (trp_pontiff_knight, 4, 8, 0), #宗座骑士
    (trp_church_guard, 10, 15, 0), #教堂守卫
    (trp_church_apprentice_preist, 20, 25, 0), #教会见习神官
    (trp_church_senior_trainee, 20, 25, 0), #教会资深习武者
    (trp_mission_school_student, 40, 45, 0), #教会学校学员
    (trp_church_fresh_trainee, 45, 50, 0), #教会新手习武者
]),
#协防民兵
("defense_militia_reinforcements", "defense_militia reinforcements", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #140到170人
    (trp_faith_cavalry, 10, 15, 0), #信义骑兵
    (trp_papal_elite_archer, 10, 15, 0), #教国精锐射手
    (trp_holy_land_swordsman, 20, 25, 0), #圣地剑士
    (trp_holy_city_sentry, 25, 30, 0), #圣城哨兵
    (trp_holy_city_standing_infantry, 35, 40, 0), #圣城常备步兵
    (trp_papal_joint_defense_militia, 40, 45, 0), #圣城协防民兵
]),
("remote_militia_reinforcements", "remote militia reinforcements", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #140到170人
    (trp_papal_devout_noble, 10, 15, 0), #教国虔信贵族
    (trp_papal_senior_spearman, 30, 35, 0), #教国资深矛兵
    (trp_papal_recruit_spearman, 30, 35, 0), #教国征召矛兵
    (trp_papal_recruit_militia, 40, 45, 0), #教国征召民兵
    (trp_papal_standing_archer, 10, 15, 0), #教国常备弓手
    (trp_papal_hunter, 20, 25, 0), #教国猎人
]),
##————————————————————————————————证信宗————————————————————————————————
##
("sin_slave_legion_reinforcements", "sin slave legion reinforcements", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #143到171人
    (trp_doctrinal_sitting_magistrate, 3, 6, 0), #教义审判官
    (trp_trial_servant, 10, 15, 0), #审判仆役
    (trp_hyena_knight, 15, 20, 0), #鬣狗骑士
    (trp_sin_slave_infantry, 25, 30, 0), #罪仆步兵
    (trp_sin_slave_soldier, 40, 45, 0), #罪仆奴兵
    (trp_accused_believer, 50, 55, 0), #戴罪信众
]),
##———————————————————————————————真信施洗宗————————————————————————————————
##
("baptized_legion_reinforcements", "baptized legion reinforcements", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #133到162人
    (trp_powell_baptized_knight, 5, 10, 0), #普威尔受洗骑士
    (trp_yishith_baptized_ranger, 3, 7, 0), #伊希斯受洗游侠
    (trp_powell_baptized_rider, 25, 30, 0), #普威尔受洗骑手
    (trp_yishith_baptized_archer, 20, 25, 0), #伊希斯受洗射手
    (trp_yishith_baptized_half_elf, 30, 35, 0), #伊希斯受洗半精灵
    (trp_powell_baptized_infantry, 50, 55, 0), #普威尔受洗步兵
]),
##———————————————————————————————圣别渴求者————————————————————————————————
##
("armed_pilgrim_reinforcements", "armed pilgrim reinforcements", 
   0, 0, fac_kingdom_5, aggressiveness_0, [                    #139到166人
    (trp_saintly_thief_ranger, 1, 4, 0), #圣盗游侠
    (trp_holy_bandit_cavalry, 5, 10, 0), #圣匪骑兵
    (trp_holy_smuggler, 23, 27, 0), #圣迹走私者
    (trp_sacred_object_thief, 20, 25, 0), #圣物窃贼
    (trp_armed_archaeological_team, 40, 45, 0), #仗剑考古队
    (trp_armed_pilgrim, 50, 55, 0), #武装朝圣者
]),




###########################################################龙树######################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_6_reinforcements_a", "{!}kingdom 6 reinforcements a", 0, 0, fac_commoners, aggressiveness_0, [(trp_longshu_bubazi, 2, 4, 0),(trp_longshu_tuanlianbing, 2, 4, 0),(trp_longshu_zhengzu, 3, 6, 0),(trp_longshu_jiji, 1, 3, 0),(trp_longshu_xiaoqi, 1, 1, 0),(trp_longshu_eunuch, 0, 1, 0)]),
("kingdom_6_reinforcements_b", "{!}kingdom 6 reinforcements b", 0, 0, fac_commoners, aggressiveness_0, [(trp_longshu_bow_guaizima, 2, 4, 0),(trp_longshu_eunuch_inspector, 0, 1, 0),(trp_longshu_eagle_ruishi, 1, 3, 0),(trp_longshu_spear_ruishi, 1, 3, 0),(trp_longshu_accurate_jicha, 1, 2, 0),(trp_longshu_power_jicha, 1, 2, 0)]),
("kingdom_6_reinforcements_c", "{!}kingdom 6 reinforcements c", 0, 0, fac_commoners, aggressiveness_0, [(trp_longshu_shenwujun, 0, 1, 0),(trp_longshu_longxiangjun, 0, 1, 0),(trp_longshu_cangtoujun, 1, 2, 0),(trp_longshu_baiganjun, 1, 2, 0),(trp_longshu_tielinjun, 0, 1, 0),(trp_longshu_yulinjun, 1, 2, 0)]),




#########################################################斯塔胡克大公国#####################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_7_reinforcements_b", "kingdom 7 reinforcements b", 
   0, 0, fac_kingdom_7, aggressiveness_0, [                    #140到163人
    (trp_starkhook_business_armed_captain, 1, 1, 0), #斯塔胡克武装船长
    (trp_starkhook_axe_thrower, 5, 8, 0), #斯塔胡克飞斧手
    (trp_starkhook_enhanced_warrior, 20, 25, 0), #斯塔胡克血益步兵
    (trp_starkhook_onboard_infantry, 24, 29, 0), #斯塔胡克船上步兵
    (trp_starkhook_armed_sailor, 40, 45, 0), #斯塔胡克武装水手
    (trp_starkhook_recruit, 50, 55, 0), #斯塔胡克平民
]),
("kingdom_7_reinforcements_a", "kingdom 7 reinforcements a", 
   0, 0, fac_kingdom_7, aggressiveness_0, [                    #141到166人
    (trp_starkhook_condottiere, 1, 1, 0), #斯塔胡克佣兵队长
    (trp_starkhook_enhanced_mercenary, 15, 20, 0), #斯塔胡克血益佣兵
    (trp_starkhook_armoured_crossbowman, 20, 25, 0), #斯塔胡克装甲弩手
    (trp_starkhook_armoured_horseman, 15, 20, 0), #斯塔胡克装甲骑手
    (trp_starkhook_armoured_swordman, 30, 35, 0), #斯塔胡克装甲剑士
    (trp_starkhook_mercenary, 60, 65, 0), #斯塔胡克佣兵
]),
("kingdom_7_reinforcements_c", "kingdom 7 reinforcements c", 
   0, 0, fac_kingdom_7, aggressiveness_0, [                    #147到171人
    (trp_starkhook_business_armed_captain, 2, 2, 0), #斯塔胡克武装船长
    (trp_starkhook_throwing_axe_ranger, 5, 8, 0), #斯塔胡克飞斧游侠
    (trp_starkhook_megalith_berserker, 12, 18, 0), #斯塔胡克岩雷狂战士
    (trp_starkhook_berserker_warrior, 43, 48, 0), #斯塔胡克狂战卫士
    (trp_starkhook_boat_fighter, 40, 45, 0), #斯塔胡克舷斗士
    (trp_starkhook_armed_sailor, 45, 50, 0), #斯塔胡克武装水手
]),
##————————————————————————————————白塔党————————————————————————————————
##
("party_of_tower_reinforcements", "party of tower reinforcements", 
   0, 0, fac_kingdom_7, aggressiveness_0, [                    #123到153人
    (trp_starkhook_bloody_berserker, 2, 5, 0), #斯塔胡克血塔狂战士
    (trp_starkhook_mangler_berserker, 1, 4, 0), #斯塔胡克厉海狂战士
    (trp_bloodburst_servant, 10, 16, 0), #血涌仆从
    (trp_starkhook_enhanced_swordman, 25, 30, 0), #斯塔胡克血益剑士
    (trp_starkhook_enhanced_halberdman, 23, 28, 0), #斯塔胡克血益斧手
    (trp_bloodburst_slave, 62, 70, 0), #血缚者
]),
##——————————————————————————————斯塔胡克商业联合——————————————————————————————
##
("starkhook_commercial_union_reinforcements_a", "starkhook commercial union reinforcements a", 
   0, 0, fac_kingdom_7, aggressiveness_0, [                    #137到159人
    (trp_starkhook_business_association_leader, 1, 1, 0), #斯塔胡克商联队长
    (trp_starkhook_attendant_cavalry, 4, 8, 0), #斯塔胡克侍从骑兵
    (trp_starkhook_commercial_nobility, 6, 10, 0), #斯塔胡克商业贵族
    (trp_starkhook_business_association_rider, 31, 34, 0), #斯塔胡克商联骑手
    (trp_armed_blood_slave, 40, 46, 0), #武装血仆
    (trp_blood_can_slave, 55, 60, 0), #血罐仆从
]),
("starkhook_commercial_union_reinforcements_b", "starkhook commercial union reinforcements b", 
   0, 0, fac_kingdom_7, aggressiveness_0, [                    #132到158人
    (trp_crimson_war_mage, 1, 3, 0), #猩红战法师
    (trp_starkhook_knight, 5, 9, 0), #斯塔胡克骑士
    (trp_starkhook_blood_arrow_shooter, 6, 10, 0), #斯塔胡克血箭射手
    (trp_starkhook_companion_infantry, 24, 30, 0), #斯塔胡克伙友步兵
    (trp_blood_servant_guard, 41, 46, 0), #血眷卫士
    (trp_armed_blood_slave, 55, 60, 0), #武装血仆
]),




##########################################################自由城邦#####################################################
##
##————————————————————————————————通用模板————————————————————————————————
##
("kingdom_8_reinforcements_a", "kingdom 8 reinforcements a", 
   0, 0, fac_kingdom_8, aggressiveness_0, [                    #131到158人
    (trp_citizen_patrol, 3, 7, 0), #自由城邦巡逻队员
    (trp_citizen_spearman, 10, 14, 0), #自由城邦矛兵
    (trp_citizen_light_infantry, 18, 22, 0), #自由城邦轻步兵
    (trp_citizen_defend_militia, 25, 30, 0), #自由城邦防卫民兵
    (trp_citizen_militia, 35, 40, 0), #自由城邦民兵
    (trp_citizen_pauper, 40, 45, 0), #自由城邦贫民
]),
("kingdom_8_reinforcements_b", "kingdom 8 reinforcements b", 
   0, 0, fac_kingdom_8, aggressiveness_0, [                    #131到156人
    (trp_states_nobility_crossbowman, 2, 5, 0), #自由城邦贵族弩手
    (trp_states_nobility, 5, 9, 0), #自由城邦贵族
    (trp_states_crossbow_ranger, 20, 24, 0), #自由城邦游击弩手
    (trp_states_rider, 24, 28, 0), #自由城邦骑手
    (trp_states_skirmisher, 35, 40, 0), #自由城邦散兵
    (trp_states_civilian, 45, 50, 0), #自由城邦公民
]),
("kingdom_8_reinforcements_c", "kingdom 8 reinforcements c", 
   0, 0, fac_kingdom_8, aggressiveness_0, [                    #133到161人
    (trp_states_fortress_ballistaman, 1, 3, 0), #自由城邦堡垒弩炮手
    (trp_states_fortress_crossbowman, 10, 16, 0), #自由城邦堡垒弩手
    (trp_states_heavy_armored_crossbowman, 34, 39, 0), #自由城邦重装弩手
    (trp_states_heavy_cavalry, 21, 26, 0), #自由城邦重骑兵
    (trp_states_crossbow_cavalry, 30, 35, 0), #自由城邦弩骑兵
    (trp_states_light_cavalry, 37, 42, 0), #自由城邦轻骑兵
]),




  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_abyssal_sailor,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_the_forsaken,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_abyssal_sailor,15,50)]),

  ("attendants","Attendents",icon_gray_knight,0,fac_commoners, aggressiveness_0,[]),
  ("tool_party", "Tool Party", icon_gray_knight|pf_is_static, 0, fac_commoners, aggressiveness_0, []), #工具人party

  ("leaded_looters","Band of robbers", #活祭猎人
    icon_axeman|carries_goods(8)|pf_quest_party, 0, fac_heresy_demon, bandit_personality,
    [(trp_degradation_rider, 1, 1), 
     (trp_the_forsaken, 40, 40)
   ]),
]
