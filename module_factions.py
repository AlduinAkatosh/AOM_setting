from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05)]
factions = [
  ("no_faction", "No_Faction", 0, 0.900000, [], [], 0xAAAAAA),


##_________________________________________________________________________system related identity____________________________________________________________________________
  ("commoners", "Commoners", 0, 0.100000, 
[("outlaws", -0.600000), ("player_faction", 0.100000), ("player_supporters_faction", 0.100000), ("outlaws_robber_knight", -0.600000), ("outlaws_kouruto_refugee", -0.600000), ("outlaws_abyssal", -0.600000), ("outlaws_ankiya", -0.600000), ("outlaws_desert", -0.600000), ("outlaws_forest", -0.600000), ("outlaws_bandit", -0.600000), ("outlaws_deserters", -0.600000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", 0.600000), ("manhunters", 0.600000), ("hammer_of_judgment", 0.100000)], [], 0xAAAAAA),

  ("outlaws", "Outlaws", max_player_rating(-30), 0.100000, 
[("commoners", -0.600000), ("innocents", -0.050000), ("merchants", -0.500000), ("player_faction", -0.150000), ("player_supporters_faction", -0.150000), ("kingdom_1", -0.100000), ("kingdom_2", -0.100000), ("kingdom_3", -0.100000), ("kingdom_4", 0.100000), ("kingdom_5", -0.100000), ("kingdom_6", -0.100000), ("kingdom_7", -0.100000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", 0.100000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -0.200000), ("outlaws_desert", 0.100000), ("outlaws_forest", 0.100000), ("outlaws_bandit", 0.100000), ("outlaws_deserters", 0.100000), ("deathbell", 0.020000), ("adventurers_association", -0.600000), ("manhunters", -0.600000)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral", "Neutral", 0, 0.100000, [], [], 0xFFFFFF),

  ("innocents", "Innocents", ff_always_hide_label, 0.500000, [("outlaws", -0.050000)], [], 0xAAAAAA),

  ("merchants", "Merchants", ff_always_hide_label, 0.500000, 
[("outlaws", -0.500000), ("outlaws_robber_knight", -0.500000), ("outlaws_kouruto_refugee", -0.500000), ("outlaws_abyssal", -0.500000), ("outlaws_ankiya", -0.500000), ("outlaws_desert", -0.500000), ("outlaws_forest", -0.500000), ("outlaws_bandit", -0.500000), ("outlaws_deserters", -0.500000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", 0.600000), ("manhunters", 0.600000), ("hammer_of_judgment", 0.200000)], [], 0xAAAAAA),


##____________________________________________________________________________________kingdom__________________________________________________________________________________
  ("player_faction", "Player_Faction", 0, 0.900000, 
[("commoners", 0.100000), ("outlaws", -0.150000), ("player_supporters_faction", 1.000000), ("outlaws_robber_knight", -0.100000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.100000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.100000), ("outlaws_forest", -0.150000), ("outlaws_bandit", -0.150000), ("outlaws_deserters", -0.100000), ("heresy_demon", -0.150000), ("heresy_undead", -0.150000), ("heresy_witchcraft", -0.100000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", 0.100000), ("peasant_rebels", -0.400000)], [], 0xAAAAAA),

  ("player_supporters_faction", "Player's_Supporters", 0, 0.900000, 
[("commoners", 0.100000), ("outlaws", -0.150000), ("player_faction", 1.000000), ("outlaws_robber_knight", -0.100000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.100000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.100000), ("outlaws_forest", -0.150000), ("outlaws_bandit", -0.150000), ("outlaws_deserters", -0.100000), ("heresy_demon", -0.150000), ("heresy_undead", -0.150000), ("heresy_witchcraft", -0.100000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", 0.100000), ("peasant_rebels", -0.400000)], [], 0xAAAAAA), #changed name so that can tell difference if shows up on map

  ("kingdom_1", "Kingdom_of_Powell", 0, 0.900000, 
[("outlaws", -0.100000), ("kingdom_5", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", 0.100000), ("manhunters", 0.100000)], [], 0xFF5809),

  ("kingdom_2", "Principality_of_Yishith", 0, 0.900000, 
[("outlaws", -0.100000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -1.000000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", 0.100000), ("heresy_sabianism", 0.100000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", -0.100000)], [], 0x76EF82),

  ("kingdom_3", "Sheikhdom_of_Kouruto", 0, 0.900000, 
[("outlaws", -0.100000), ("kingdom_5", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("heresy_sabianism", -0.200000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", -0.100000)], [], 0x977C00),

  ("kingdom_4", "Confederation_of_Uhr-Diemer-Ankiyat", 0, 0.900000, 
[("outlaws", 0.100000), ("kingdom_2", -0.200000), ("kingdom_7", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -1.000000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -1.000000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", 0.050000), ("adventurers_association", 0.100000), ("manhunters", 0.100000)], [], 0x8080C0),

  ("kingdom_5", "Papal_States", 0, 0.900000, 
[("outlaws", -0.100000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", 0.020000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", 0.020000), ("yishith_rebel", 0.020000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -1.000000), ("heresy_witchcraft", -1.000000), ("heresy_sabianism", -1.000000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", 0.500000)], [], 0xFFFFFF),

  ("kingdom_6", "Qian_Dynasty_of_Eastren_Longshu", 0, 0.900000, 
[("outlaws", -0.100000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("heresy_sabianism", -0.200000), ("deathbell", -0.200000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", -0.200000)], [], 0xF9F900),

  ("kingdom_7", "Emirate_of_Starkhook", 0, 0.900000, 
[("outlaws", -0.100000), ("kingdom_4", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", 0.200000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("adventurers_association", 0.100000), ("manhunters", 0.100000)], [], 0xFF8080),

  ("kingdom_8", "City_States", 0, 0.900000, 
[("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("deathbell", 0.100000), ("adventurers_association", 0.100000), ("manhunters", 0.100000), ("hammer_of_judgment", 0.100000)], [], 0xBEBEBE),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),
  ("outlaws_integration","{!}outlaws_integration", 0, 0,[], []),
  ("others_integration","{!}others_integration", 0, 0,[], []),
## This three objects are uesd for the upgrade trees.


##____________________________________________________________________________________outlaws_________________________________________________________________________________
  ("outlaws_libra", "Libra", 0, -0.200000, 
[("commoners", -0.600000), ("merchants", -0.500000), ("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0xAFAFAF),

  ("outlaws_robber_knight", "Robber_Knights", 0, -0.200000, 
[("commoners", -0.600000), ("outlaws", -0.200000), ("merchants", -0.500000), ("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0xAFAFAF),

  ("outlaws_kouruto_refugee", "Kouruto_Refugee", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", -0.200000), ("merchants", -0.500000), ("player_faction", -0.200000), ("player_supporters_faction", -0.200000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -1.000000), ("kingdom_5", 0.020000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_robber_knight", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0x808000),

  ("outlaws_abyssal", "Abyssal", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", 0.100000), ("merchants", -0.500000), ("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", 0.200000), ("kingdom_8", -0.200000), ("outlaws_ankiya", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0x5366EE),

  ("outlaws_ankiya", "Ankiya_Barbarian", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", -0.200000), ("merchants", -0.500000), ("player_faction", -0.200000), ("player_supporters_faction", -0.200000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -1.000000), ("kingdom_5", 0.020000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_abyssal", -0.200000), ("yishith_rebel", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", 0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0x804040),

  ("outlaws_desert", "Desert_bandit", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", 0.100000), ("merchants", -0.500000), ("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0xADB759),

  ("outlaws_forest", "Forest_Bandits", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", 0.100000), ("merchants", -0.500000), ("player_faction", -0.150000), ("player_supporters_faction", -0.150000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0x1C7B11),

  ("outlaws_bandit", "Bandit", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", 0.100000), ("merchants", -0.500000), ("player_faction", -0.150000), ("player_supporters_faction", -0.150000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0x888888),

  ("outlaws_deserters", "Deserters", 0, 0.500000, 
[("commoners", -0.600000), ("outlaws", 0.100000), ("merchants", -0.500000), ("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("adventurers_association", -0.200000), ("manhunters", -0.600000)], [], 0x888888),


##______________________________________________________________________________outer deity_______________________________________________________________________________
  ("heresy_demon", "Demon", 0, 1.000000, 
[("commoners", -1.000000), ("merchants", -1.000000), ("player_faction", -0.150000), ("player_supporters_faction", -0.150000), ("kingdom_1", -1.000000), ("kingdom_2", -1.000000), ("kingdom_3", -1.000000), ("kingdom_4", -1.000000), ("kingdom_5", -1.000000), ("kingdom_6", -1.000000), ("kingdom_7", -1.000000), ("kingdom_8", -1.000000), ("outlaws_robber_knight", -1.000000), ("outlaws_kouruto_refugee", -1.000000), ("outlaws_abyssal", -1.000000), ("outlaws_ankiya", -1.000000), ("yishith_rebel", -1.000000), ("outlaws_desert", -1.000000), ("outlaws_forest", -1.000000), ("outlaws_bandit", -1.000000), ("outlaws_deserters", -1.000000), ("heresy_undead", -1.000000), ("heresy_witchcraft", -1.000000), ("heresy_sabianism", -1.000000), ("deathbell", -1.000000), ("adventurers_association", -1.000000), ("manhunters", -0.600000), ("hammer_of_judgment", -1.000000)], [], 0x800080),

  ("heresy_undead", "Undead", 0, 0.500000, 
[("commoners", -0.200000), ("merchants", -0.200000), ("player_faction", -0.150000), ("player_supporters_faction", -0.150000), ("kingdom_1", -0.200000), ("kingdom_2", -0.200000), ("kingdom_3", -0.200000), ("kingdom_4", -0.200000), ("kingdom_5", -1.000000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("adventurers_association", -0.200000), ("manhunters", -0.600000), ("hammer_of_judgment", -1.000000)], [], 0xB04FA9),

  ("heresy_witchcraft", "Witchcraft", 0, 0.500000, 
[("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.020000), ("kingdom_2", 0.100000), ("kingdom_3", -0.200000), ("kingdom_4", 0.050000), ("kingdom_5", -1.000000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", 0.200000), ("heresy_demon", -1.000000), ("adventurers_association", -0.200000), ("manhunters", -0.600000), ("hammer_of_judgment", -1.000000)], [], 0x008080),

  ("heresy_sabianism", "Sabianism", 0, 1.000000, 
[("kingdom_2", 0.100000), ("kingdom_3", -0.200000), ("kingdom_5", -1.000000), ("kingdom_6", -0.200000), ("heresy_demon", -1.000000), ("deathbell", -0.200000), ("manhunters", -0.600000), ("hammer_of_judgment", -1.000000)], [], 0x8080FF),

  ("heresy_eclipse", "Eclipse", 0, 0.500000, 
[("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.020000), ("kingdom_2", 0.100000), ("kingdom_3", -0.200000), ("kingdom_4", 0.050000), ("kingdom_5", -1.000000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", 0.200000), ("heresy_demon", -1.000000), ("adventurers_association", -0.200000), ("manhunters", -0.600000), ("hammer_of_judgment", -1.000000)], [], 0x008080),

  ("heresy_mammonism", "Mammonism", 0, 0.500000, 
[("player_faction", -0.100000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.020000), ("kingdom_2", 0.100000), ("kingdom_3", -0.200000), ("kingdom_4", 0.050000), ("kingdom_5", -1.000000), ("kingdom_6", -0.200000), ("kingdom_7", -0.200000), ("kingdom_8", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", 0.200000), ("heresy_demon", -1.000000), ("adventurers_association", -0.200000), ("manhunters", -0.600000), ("hammer_of_judgment", -1.000000)], [], 0x008080),


##____________________________________________________________________________________others_________________________________________________________________________________
  ("deathbell", "Deathbell", 0, 0.500000, 
[("outlaws", 0.020000), ("kingdom_1", -0.200000), ("kingdom_6", -0.200000), ("kingdom_8", 0.100000), ("heresy_demon", -1.000000), ("heresy_sabianism", -0.200000), ("manhunters", -0.600000)], [], 0xB79BE3),

  ("yishith_rebel", "Yishith_Rebel", 0, 0.900000, 
[("outlaws", -0.200000), ("kingdom_2", -1.000000), ("kingdom_5", 0.020000), ("kingdom_6", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_ankiya", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("manhunters", -0.600000), ("hammer_of_judgment", 0.020000)], [], 0x5BAB0C),

  ("adventurers_association", "Adventurers_Association", 0, 0.800000, 
[("commoners", 0.600000), ("outlaws", -0.600000), ("merchants", 0.600000), ("player_faction", 0.100000), ("player_supporters_faction", 0.100000), ("kingdom_1", 0.100000), ("kingdom_2", 0.100000), ("kingdom_3", 0.100000), ("kingdom_4", 0.100000), ("kingdom_5", 0.100000), ("kingdom_6", 0.100000), ("kingdom_7", 0.100000), ("kingdom_8", 0.100000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("manhunters", 0.800000), ("hammer_of_judgment", 0.100000)], [], 0x0080FF),

  ("manhunters", "Manhunters", 0, 0.500000, 
[("commoners", 0.600000), ("outlaws", -0.600000), ("merchants", 0.600000), ("player_faction", 0.100000), ("player_supporters_faction", 0.100000), ("kingdom_1", 0.100000), ("kingdom_2", 0.100000), ("kingdom_3", 0.100000), ("kingdom_4", 0.100000), ("kingdom_5", 0.100000), ("kingdom_6", 0.100000), ("kingdom_7", 0.100000), ("kingdom_8", 0.100000), ("outlaws_robber_knight", -0.600000), ("outlaws_kouruto_refugee", -0.600000), ("outlaws_abyssal", -0.600000), ("outlaws_ankiya", -0.600000), ("yishith_rebel", -0.600000), ("outlaws_desert", -0.600000), ("outlaws_forest", -0.600000), ("outlaws_bandit", -0.600000), ("outlaws_deserters", -0.600000), ("heresy_demon", -0.600000), ("heresy_undead", -0.600000), ("heresy_witchcraft", -0.600000), ("heresy_sabianism", -0.600000), ("deathbell", -0.600000), ("adventurers_association", 0.800000), ("hammer_of_judgment", 0.200000)], [], 0xDFDFDF),

  ("hammer_of_judgment", "Hammer_of_Judgment", 0, 0.800000, 
[("commoners", 0.100000), ("merchants", 0.200000), ("player_faction", 0.100000), ("player_supporters_faction", 0.100000), ("kingdom_2", -0.100000), ("kingdom_3", -0.100000), ("kingdom_5", 0.500000), ("kingdom_6", -0.200000), ("kingdom_8", 0.100000), ("yishith_rebel", 0.020000), ("heresy_demon", -1.000000), ("heresy_undead", -1.000000), ("heresy_witchcraft", -1.000000), ("heresy_sabianism", -1.000000), ("adventurers_association", 0.100000), ("manhunters", 0.200000)], [], 0xEFEFEF),

  ("kouruto_auxiliary", "Kouruto_Auxiliary", 0, 0.500000, 
[("commoners", 0.100000), ("outlaws", -0.100000), ("merchants", 0.200000), ("player_faction", 0.100000), ("player_supporters_faction", 0.100000), ("kingdom_3", 0.500000), ("kingdom_5", -0.200000), ("kingdom_6", -0.200000), ("kingdom_8", 0.100000), ("outlaws_robber_knight", -0.200000), ("outlaws_kouruto_refugee", -1.000000), ("outlaws_abyssal", -0.200000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("adventurers_association", 0.100000), ("manhunters", 0.200000), ("hammer_of_judgment", -0.050000)], [], 0xE2930E),

  ("monster", "Monster", 0, 0, [], [], 0x85FAE9),

  ("saviour", "Saviour", 0, 0.800000, 
[("commoners", 0.100000), ("outlaws", -0.100000), ("merchants", 0.200000), ("player_faction", 0.100000), ("player_supporters_faction", 0.100000), ("kingdom_2", 0.400000), ("kingdom_4", -0.100000), ("kingdom_5", -0.100000), ("kingdom_6", -0.200000), ("outlaws_robber_knight", -0.200000), ("outlaws_abyssal", -0.200000), ("outlaws_ankiya", -0.200000), ("yishith_rebel", -1.000000), ("outlaws_desert", -0.200000), ("outlaws_forest", -0.200000), ("outlaws_bandit", -0.200000), ("outlaws_deserters", -0.200000), ("heresy_demon", -1.000000), ("heresy_undead", -0.200000), ("heresy_witchcraft", -0.200000), ("adventurers_association", 0.100000), ("manhunters", 0.200000), ("hammer_of_judgment", -0.050000)], [], 0x85FAE9),


##____________________________________________________________________________________unused_________________________________________________________________________________
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),

  ("faction_end", "Faction End", 0, 0.500000, [], [], 0xB79BE3),
]
