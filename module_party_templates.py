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
    ("none", "none", icon_gray_knight, 0, fac_commoners, merchant_personality, []),
    ("rescued_prisoners", "Rescued Prisoners", icon_gray_knight, 0, fac_commoners, merchant_personality, []),
    ("enemy", "Enemy", icon_gray_knight, 0, fac_undeads, merchant_personality, []),
    ("hero_party", "Hero Party", icon_gray_knight, 0, fac_commoners, merchant_personality, []),
    ("village_defenders", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_farmer, 10, 20), (trp_peasant_woman, 0, 4)]),
    ("cattle_herd", "Cattle Herd", icon_cattle | carries_goods(10), 0, fac_neutral, merchant_personality, [(trp_cattle, 80, 120)]),
    ("looters", "Looters", icon_axeman | carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_looter, 3, 30), (trp_bandit, 2, 15)]),  ## CC
    ("manhunters", "Manhunters", icon_gray_knight, 0, fac_manhunters, soldier_personality, [(trp_manhunter, 9, 40)]),
    ("forest_bandits", "Forest Bandits", icon_axeman | carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_veteran_forest_bandit, 4, 11), (trp_trained_forest_bandit, 5, 14), (trp_forest_bandit, 10, 30)]),
    ("taiga_bandits", "Tundra Bandits", icon_axeman | carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_veteran_taiga_bandit, 4, 9), (trp_trained_taiga_bandit, 5, 12), (trp_taiga_bandit, 9, 29)]),
    ("steppe_bandits", "Steppe Bandits", icon_khergit | carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_veteran_steppe_bandit, 3, 7), (trp_trained_steppe_bandit, 3, 9), (trp_steppe_bandit, 7, 20)]),
    ("sea_raiders", "Sea Raiders", icon_axeman | carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_veteran_sea_raider, 4, 9), (trp_trained_sea_raider, 5, 12), (trp_sea_raider, 9, 25)]),
    ("mountain_bandits", "Mountain Bandits", icon_axeman | carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_veteran_mountain_bandit, 4, 11), (trp_trained_mountain_bandit, 5, 14), (trp_mountain_bandit, 10, 30)]),
    ("desert_bandits", "Desert Bandits", icon_vaegir_knight | carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_veteran_desert_bandit, 3, 7), (trp_trained_desert_bandit, 3, 9), (trp_desert_bandit, 7, 20)]),
    ("deserters", "Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("deserters_swadian", "Swadian Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("deserters_vaegir", "Vaegir Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("deserters_khergit", "Khergit Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("deserters_nord", "Nord Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("deserters_rhodok", "Rhodok Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("deserters_sarranid", "Sarranid Deserters", icon_vaegir_knight | carries_goods(3), 0, fac_deserters, bandit_personality, []),
    ("merchant_caravan", "Merchant Caravan", icon_gray_knight | carries_goods(20) | pf_auto_remove_in_town | pf_quest_party, 0, fac_commoners, escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_caravan_guard, 6, 15), (trp_watchman, 4, 10)]),  ## CC
    ("troublesome_bandits", "Troublesome Bandits", icon_axeman | carries_goods(9) | pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit, 14, 55)]),
    ("bandits_awaiting_ransom", "Bandits Awaiting Ransom", icon_axeman | carries_goods(9) | pf_auto_remove_in_town | pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit, 24, 58), (trp_kidnapped_girl, 1, 1, pmf_is_prisoner)]),
    ("kidnapped_girl", "Kidnapped Girl", icon_woman | pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_kidnapped_girl, 1, 1)]),
    ("village_farmers", "Village Farmers", icon_peasant | pf_civilian, 0, fac_innocents, merchant_personality, [(trp_farmer, 5, 10), (trp_peasant_woman, 3, 8)]),
    ("spy_partners", "Unremarkable Travellers", icon_gray_knight | carries_goods(10) | pf_default_behavior | pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_spy_partner, 1, 1), (trp_caravan_guard, 5, 11)]),
    ("runaway_serfs", "Runaway Serfs", icon_peasant | carries_goods(8) | pf_default_behavior | pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_farmer, 6, 7), (trp_peasant_woman, 3, 3)]),
    ("spy", "Ordinary Townsman", icon_gray_knight | carries_goods(4) | pf_default_behavior | pf_quest_party, 0, fac_neutral, merchant_personality, [(trp_spy, 1, 1)]),
    ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight | carries_goods(3) | pf_default_behavior | pf_quest_party, 0, fac_neutral, merchant_personality, []),
    ("horse_merchant_party", "Horse Caravan", icon_horse_caravan | carries_goods(25), 0, fac_neutral, merchant_personality, [(trp_mercenary_cavalry, 8, 10), (trp_mercenary_horseman, 12, 15), (trp_caravan_guard, 24, 30)]),
    ("scout_party", "Scouts", icon_gray_knight | carries_goods(1) | pf_show_faction, 0, fac_commoners, bandit_personality, []),
    ("patrol_party", "Patrol", icon_gray_knight | carries_goods(2) | pf_show_faction, 0, fac_commoners, soldier_personality, []),
    ("messenger_party", "Messenger", icon_gray_knight | pf_show_faction, 0, fac_commoners, merchant_personality, []),
    ("raider_party", "Raiders", icon_gray_knight | carries_goods(16) | pf_quest_party, 0, fac_commoners, bandit_personality, []),
    ("raider_captives", "Raider Captives", 0, 0, fac_commoners, 0, [(trp_peasant_woman, 6, 30, pmf_is_prisoner)]),
    ("kingdom_caravan_party", "Caravan", icon_mule | carries_goods(25) | pf_show_faction, 0, fac_commoners, merchant_personality, [(trp_caravan_master, 1, 1), (trp_caravan_guard, 12, 40)]),
    ("prisoner_train_party", "Prisoner Train", icon_gray_knight | carries_goods(5) | pf_show_faction, 0, fac_commoners, merchant_personality, []),
    ("default_prisoners", "Default Prisoners", 0, 0, fac_commoners, 0, [(trp_bandit, 5, 10, pmf_is_prisoner)]),
    ("routed_warriors", "Routed Enemies", icon_vaegir_knight, 0, fac_commoners, soldier_personality, []),
    ("center_reinforcements", "Reinforcements", icon_axeman | carries_goods(16), 0, fac_commoners, soldier_personality, [(trp_watchman, 4, 20), (trp_caravan_guard, 2, 10), (trp_mercenary_crossbowman, 2, 10)]),
    
    ("kingdom_hero_party", "War Party", icon_flagbearer_a | pf_show_faction | pf_default_behavior, 0, fac_commoners, soldier_personality, []),
    ## recruiting cost, about 600 to 900
    ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_militia, 5, 9), (trp_swadian_footman, 2, 4), (trp_swadian_skirmisher, 3, 5)]),
    ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman, 5, 8), (trp_swadian_crossbowman, 2, 4)]),
    ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_sergeant, 1, 2), (trp_swadian_sharpshooter, 1, 2), (trp_swadian_infantry, 1, 3), (trp_swadian_noble_lad, 1, 3)]),
    ("kingdom_1_reinforcements_c_hero", "{!}kingdom_1_reinforcements_c_hero", 0, 0, fac_commoners, 0, [(trp_swadian_knight, 1, 2), (trp_swadian_man_at_arms, 1, 3), (trp_swadian_novice_horseman, 1, 2)]),
    
    ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_footman, 5, 8), (trp_vaegir_veteran, 2, 4), (trp_vaegir_skirmisher, 3, 6)]),
    ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran, 5, 7), (trp_vaegir_archer, 2, 5)]),
    ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_guard, 1, 2), (trp_vaegir_marksman, 1, 2), (trp_vaegir_infantry, 1, 3), (trp_vaegir_noble_lad, 1, 3)]),
    ("kingdom_2_reinforcements_c_hero", "{!}kingdom_2_reinforcements_c_hero", 0, 0, fac_commoners, 0, [(trp_vaegir_knight, 1, 2), (trp_vaegir_horseman, 1, 3), (trp_vaegir_novice_horseman, 1, 3)]),
    
    ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman, 3, 5), (trp_khergit_skirmisher, 3, 6)]),
    ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman, 3, 5), (trp_khergit_horse_archer, 2, 4)]),
    ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer, 1, 3), (trp_khergit_horse_archer, 1, 2), (trp_khergit_horseman, 1, 3)]),
    ("kingdom_3_reinforcements_c_hero", "{!}kingdom_3_reinforcements_c_hero", 0, 0, fac_commoners, 0, [(trp_khergit_khan_guard, 1, 2), (trp_khergit_horseman, 2, 5)]),
    
    ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman, 3, 6), (trp_nord_archer, 3, 5), (trp_nord_trained_footman, 3, 5)]),
    ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_warrior, 1, 3), (trp_nord_veteran_archer, 2, 4), (trp_nord_trained_footman, 3, 5)]),
    ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion, 1, 2), (trp_nord_veteran, 1, 3), (trp_nord_warrior, 2, 4)]),
    ("kingdom_4_reinforcements_c_hero", "{!}kingdom_4_reinforcements_c_hero", 0, 0, fac_commoners, 0, [(trp_nord_scout, 1, 3), (trp_nord_champion, 1, 2), (trp_nord_veteran, 1, 3)]),
    
    ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman, 3, 6), (trp_rhodok_trained_crossbowman, 4, 6), (trp_rhodok_trained_spearman, 2, 4)]),
    ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman, 2, 4), (trp_rhodok_trained_crossbowman, 2, 4), (trp_rhodok_trained_spearman, 3, 5)]),
    ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant, 1, 2), (trp_rhodok_veteran_crossbowman, 2, 4), (trp_rhodok_veteran_spearman, 2, 4)]),
    ("kingdom_5_reinforcements_c_hero", "{!}kingdom_5_reinforcements_c_hero", 0, 0, fac_commoners, 0, [(trp_rhodok_scout, 1, 3), (trp_rhodok_sergeant, 1, 2), (trp_rhodok_veteran_crossbowman, 1, 2), (trp_rhodok_veteran_spearman, 1, 3)]),
    
    ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_footman, 5, 8), (trp_sarranid_veteran_footman, 2, 4), (trp_sarranid_skirmisher, 3, 6)]),
    ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_veteran_footman, 5, 8), (trp_sarranid_archer, 2, 4)]),
    ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_guard, 1, 2), (trp_sarranid_master_archer, 1, 2), (trp_sarranid_infantry, 1, 3), (trp_sarranid_noble_lad, 1, 3)]),
    ("kingdom_6_reinforcements_c_hero", "{!}kingdom_6_reinforcements_c_hero", 0, 0, fac_commoners, 0, [(trp_sarranid_mamluke, 1, 2), (trp_sarranid_horseman, 1, 3), (trp_sarranid_novice_horseman, 1, 3)]),
    
    ("mercenary_template_a", "{!}mercenary_template_a", 0, 0, fac_commoners, 0, [(trp_mercenary_cavalry, 1, 1), (trp_mercenary_horseman, 3, 3), (trp_caravan_guard, 2, 2)]),
    ("mercenary_template_b", "{!}mercenary_template_b", 0, 0, fac_commoners, 0, [(trp_hired_blade, 1, 1), (trp_mercenary_swordsman, 3, 3), (trp_caravan_guard, 2, 2)]),
    ("mercenary_template_c", "{!}mercenary_template_c", 0, 0, fac_commoners, 0, [(trp_mercenary_sharpshooter, 2, 2), (trp_mercenary_crossbowman, 4, 4), (trp_watchman, 3, 3)]),
    ("mercenary_template_d", "{!}mercenary_template_d", 0, 0, fac_commoners, 0, [(trp_slaver_chief, 1, 1), (trp_slave_hunter, 2, 2), (trp_manhunter, 4, 4)]),
    
    ("forest_bandit_lair", "Forest Bandit Camp", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_forest_bandit, 15, 58)]),
    ("taiga_bandit_lair", "Tundra Bandit Lair", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_taiga_bandit, 15, 58)]),
    ("steppe_bandit_lair", "Steppe Bandit Lair", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_steppe_bandit, 15, 58)]),
    ("sea_raider_lair", "Sea Raider Landing", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_sea_raider, 15, 50)]),
    ("mountain_bandit_lair", "Mountain Bandit Hideout", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mountain_bandit, 15, 58)]),
    ("desert_bandit_lair", "Desert Bandit Lair", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_desert_bandit, 15, 58)]),
    ("looter_lair", "Kidnappers' Hideout", icon_bandit_lair | carries_goods(2) | pf_is_static | pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_looter, 15, 25)]),
    ("bandit_lair_templates_end", "{!}bandit_lair_templates_end", icon_axeman | carries_goods(2) | pf_is_static, 0, fac_outlaws, bandit_personality, [(trp_sea_raider, 15, 50)]),
    ("leaded_looters", "Band of robbers", icon_axeman | carries_goods(8) | pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_looter_leader, 1, 1), (trp_looter, 3, 3)]),
]