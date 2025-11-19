# -*- coding: UTF-8 -*-

from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, ["operations"], ["options"]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus_AoM = [

#######################################################会战相关######################################################
##
##城镇沙盘的基础菜单，所有分支菜单、界面都由这里引出
  ("center_new", menu_text_color(0xFFFFFF), 
    "{s9}^^{s12}^^{s13}",
    "none",
    [
      (store_encountered_party, "$current_town"),
      (set_background_mesh, "mesh_city_window"),
      (try_begin),
         (eq, "$g_town_visit_after_exploration", 1),
         (assign, "$g_town_visit_after_exploration", 0),
         (try_begin),
            (le, "$exporation_time", 0),
            (assign, "$g_event_continue", -1),#记录事件是否已经结束（比如商人返回后就不能再进入了）
            (jump_to_menu,"mnu_explore_random_event"),
         (else_try),
            (display_message, "@探 索 中 止 。 "),
         (try_end),
      (else_try),
         (assign, "$g_current_event", 0),
      (try_end),

      (call_script, "script_get_center_zone_ground", "$current_town", "$g_player_rank", "$g_player_procession"),
      (assign, ":cur_zone", reg1),
      (str_store_party_name, s5, "$current_town"),
      (str_store_item_name, s6, ":cur_zone"),
      (str_store_string, s7, "@你 正 在 {s5}的 {s6}。 "),
      (try_begin),
#         (party_slot_eq, "$current_town", slot_party_type, spt_town),#繁荣度的描述语句
         (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
         (str_clear, s8),
         (try_begin),
            (eq, ":cur_zone", "itm_zone_rich_area"),#富人区
            (try_begin),
               (gt, ":prosperity", 50),
               (str_store_string, s8, "@这 里 的 宅 邸 高 大 威 严 ， 石 墙 上 爬 满 常 春 藤 ， 大 门 敞 开 着 ， 门 前 有 仆 人 恭 敬 地 侍 立 。 街 上 的 行 人 衣 着 奢 华 ， 锦 缎 与 皮 草 在 阳 光 下 熠 熠 生 辉 ， 相 遇 时 微 微 欠 身 行 礼 ， 展 示 着 虚 伪 的 优 雅 。 不 时 有 华 丽 的 马 车 驶 过 ， 骏 马 毛 发 油 亮 ， 马 车 雕 饰 精 美 ， 贵 族 的 家 徽 在 阳 光 下 闪 耀 。 "),
            (else_try),
               (str_store_string, s8, "@这 里 的 宅 邸 院 落 大 门 紧 闭 ， 街 上 行 人 虽 衣 着 华 丽 ， 但 各 个 行 色 匆 匆 ， 相 遇 时 仅 促 狭 地 点 头 示 意 ， 捂 着 衣 裳 不 让 外 人 看 到 内 衬 里 的 补 丁 。 偶 尔 路 过 一 匹 瘦 马 拖 着 的 马 车 ， 摘 去 装 饰 物 的 车 厢 上 ， 贵 族 的 家 徽 被 黑 布 遮 挡 ， 车 轮 碾 过 地 面 ， 发 出 吱 呀 的 声 响 。 "),
            (try_end),
         (else_try),
            (eq, ":cur_zone", "itm_zone_residential_area"),#平民区
            (try_begin),
               (gt, ":prosperity", 50),
               (str_store_string, s8, "@这 里 的 房 屋 低 矮 且 密 集 ， 狭 窄 的 街 道 上 满 是 行 人 和 小 摊 贩 。 人 们 穿 着 朴 素 但 干 净 的 衣 物 ， 街 头 巷 尾 弥 漫 着 食 物 的 香 气 ， 那 是 小 饭 馆 里 传 出 的 廉 价 但 能 饱 腹 的 饭 菜 味 道 。 孩 子 们 在 街 边 嬉 笑 玩 耍 ， 偶 有 小 孩 手 拿 糖 果 和 蜂 蜜 饼 干 等 高 档 零 食 经 过 ， 引 来 其 他 孩 子 羡 慕 的 目 光 。 "),
            (else_try),
               (str_store_string, s8, "@这 里 的 房 屋 显 得 破 旧 ， 不 少 屋 顶 的 茅 草 有 修 补 的 痕 迹 ， 人 们 脚 步 匆 匆 ， 脸 上 带 着 生 活 的 疲 惫 。 路 边 看 不 到 小 贩 的 踪 迹 ， 翻 找 垃 圾 桶 的 妇 女 们 用 布 把 脸 遮 得 严 严 实 实 ， 生 怕 被 人 发 现 是 某 个 体 面 人 家 的 主 妇 。 孩 子 们 光 着 脚 在 泥 地 里 玩 耍 ， 偶 尔 为 了 争 抢 一 点 食 物 而 哭 闹 。 "),
            (try_end),
         (else_try),
            (eq, ":cur_zone", "itm_zone_slum"),#贫民区
            (try_begin),
               (gt, ":prosperity", 50),
               (str_store_string, s8, "@这 里 的 人 们 虽 然 贫 穷 ， 但 也 能 勉 强 维 持 生 计 。 男 人 们 前 往 码 头 和 农 田 干 一 点 日 结 苦 工 ， 女 人 们 手 持 货 篮 进 城 叫 卖 ， 黑 帮 们 在 各 自 的 领 地 内 巡 视 ， 维 持 基 本 秩 序 的 同 时 向 人 们 收 取 保 护 费 ， 虽 然 不 情 愿 ， 但 人 们 也 并 非 交 不 起 这 笔 钱 。 "),
            (else_try),
               (str_store_string, s8, "@空 气 中 飘 荡 着 贫 穷 和 死 亡 的 腐 朽 味 。 泥 泞 恶 臭 的 土 路 上 看 不 到 几 个 行 人 ， 披 着 烂 布 的 乞 丐 颓 然 坐 倒 在 路 边 ， 对 路 旁 小 巷 里 野 狗 啃 食 腐 尸 的 动 静 不 闻 不 问 。 当 你 走 过 他 们 身 边 时 ， 他 们 抬 头 看 向 了 你 ， 那 是 野 狗 看 向 猎 物 — — 看 向 食 物 的 眼 神 。 但 他 们 也 看 到 了 你 腰 间 的 武 器 ， 木 然 地 低 下 了 头 。 "),
            (try_end),
         (try_end),
         (str_store_string, s9, "@{s7}{s8}"),
      (else_try),
         (str_store_string, s9, "@{s7}"),
      (try_end),
#建筑的描述
      (assign, "$current_building", -1),
      (str_clear, s12),
      (try_begin),
         (call_script, "script_get_center_zone_building", "$current_town", "$g_current_rank", "$g_current_procession"),#建筑类型
         (assign, ":building_no", reg1),
         (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#有建筑
         (gt, ":building_no", "itm_building_begin"),
         (call_script, "script_cf_check_building_showed", "$current_town", "$g_current_rank", "$g_current_procession"),#已经发现
         (str_store_item_name, s10, ":building_no"),
         (assign, "$current_building", ":building_no"),
         (try_begin),
            (call_script, "script_get_center_zone_building_owner", "$current_town", "$g_current_rank", "$g_current_procession"),#建筑所有者
            (assign, ":building_owner_no", reg1),
            (is_between, ":building_owner_no", "itm_faction_begin", "itm_faction_end"),#有所有者
            (gt, ":building_owner_no", "itm_faction_begin"),
            (str_store_item_name, s11, ":building_owner_no"),
            (str_store_string, s12, "@这 个 区 域 里 有 归 属 于 {s11}的 {s10} 。 "),
         (else_try),
            (str_store_string, s12, "@这 个 区 域 里 有 {s10} 。 "),
         (try_end),
      (else_try),
         (str_store_string, s12, "@这 个 区 域 中 暂 未 发 现 特 殊 地 点 。 "),
      (try_end),

#侵蚀的描述
      (str_clear, s13),
      (store_skill_level, ":skill_level", skl_study, "trp_player"),#洞见
      (try_begin),
         (le, ":skill_level", 5),
         (str_store_string, s13, "@一 切 如 常 ， 运 行 在 万 事 万 物 应 有 的 轨 道 上 。 "),
      (else_try),
         (le, ":skill_level", 10),
         (str_store_string, s13, "@空 气 中 散 发 着 令 人 安 心 的 氛 围 ， 你 不 知 这 种 感 觉 从 何 而 来 ， 但 知 道 它 并 非 来 自 于 五 感 。 "),
      (else_try),
         (str_store_string, s13, "@一 切 凌 驾 于 凡 世 之 物 均 保 持 着 克 制 ， 人 们 今 夜 依 然 可 以 享 有 无 知 但 幸 福 的 酣 眠 。 "),
      (try_end),
    ],

    [
      ("explore_this_area",[
         (store_skill_level, ":skill_level", skl_spotting, "trp_player"),#侦察3、6、9级时各减少一小时的探索
         (val_div, ":skill_level", 3),
         (store_sub, "$exporation_time", 6, ":skill_level"),
         (assign, reg1, "$exporation_time"),
      ],"探 索 该 地 区 （ {reg1}小 时 ）。 ",[
         (rest_for_hours_interactive, "$exporation_time", 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_exploration", 1),
         (change_screen_return),
      ]),


      ("enter_underworld_stronghold",[
         (eq, "$current_building", "itm_underworld_stronghold"),
      ],"进 入 黑 帮 的 据 点 。 ",[
         (try_begin),
            (eq, "$current_town", "p_town_4"),
            (eq, "$g_player_rank", 13),
            (eq, "$g_player_procession", 5),
            (check_quest_active, "qst_game_start_quest"),#开局剧情：进入权厄之秤的据点
            (eq, "$current_startup_quest_phase", 10),
            (call_script, "script_lesaff_underworld_stronghold"),
         (else_try),
            (item_get_slot, ":building_scene_no", "itm_underworld_stronghold", slot_building_scene_begin),
            (call_script, "script_get_building_scene", "$current_town", "$g_player_rank", "$g_player_procession"),#建筑场景
            (val_add, ":building_scene_no", reg1),
            (val_sub, ":building_scene_no", 1),
            (call_script, "script_get_center_zone_building_owner", "$current_town", "$g_player_rank", "$g_player_procession"),#建筑所有者
            (assign, ":building_owner_no", reg1),
            (call_script, "script_scene_auto_visitor", ":building_scene_no", ":building_owner_no", 10),
         (try_end),
      ]),

      ("enter_adventurer_station",[
         (eq, "$current_building", "itm_adventurer_station"),
      ],"进 入 冒 险 者 协 会 。 ",[
         (item_get_slot, ":building_scene_no", "itm_adventurer_station", slot_building_scene_begin),
         (call_script, "script_get_building_scene", "$current_town", "$g_player_rank", "$g_player_procession"),#建筑场景
         (val_add, ":building_scene_no", reg1),
         (val_sub, ":building_scene_no", 1),
         (call_script, "script_get_center_zone_building_owner", "$current_town", "$g_player_rank", "$g_player_procession"),#建筑所有者
         (assign, ":building_owner_no", reg1),
         (call_script, "script_scene_auto_visitor", ":building_scene_no", ":building_owner_no", 14),
      ]),

      ("check_center_map",[
      ],"返 回 区 域 地 图 。 ",[
         (modify_visitors_at_site, "$current_scene"),
         (reset_visitors),
         (set_visitor, 1, "trp_player"),
         (set_jump_mission,"mt_sandbox"),
         (jump_to_scene, "$current_scene"),
         (change_screen_mission),
      ]),
      ("leave_the_center",[
         (this_or_next|eq, "$g_player_rank", 1),
         (this_or_next|eq, "$g_player_rank", 15),
         (this_or_next|eq, "$g_player_procession", 1),
         (eq, "$g_player_procession", 15),
#         (le, "$g_inner_city", 0),#判断是不是在城墙内
      ],"回 到 世 界 地 图 。 ",[
         (change_screen_return),
      ]),
    ]
  ),


###探索引出的随机事件
  ("explore_random_event", menu_text_color(0xFFFFFF), 
    "{s10}",
    "none",
    [
      (str_clear, s10),
      (str_store_string, s10, "@什 么 事 都 没 有 发 生 。 "),
      (set_background_mesh, "mesh_city_window"),
      (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),#繁荣度

      (call_script, "script_get_center_zone_ground", "$current_town", "$g_player_rank", "$g_player_procession"),
      (assign, ":cur_zone", reg1),
#item里记录了该区块各个事件的默认权重，获取后根据各种条件进行修正
      (assign, ":total_event_count", 1),
      (try_for_range, ":event_no", 1, 100),
         (item_get_slot, ":power_no", ":cur_zone", ":event_no"), #该事件的默认权重

         (try_begin),#添加修正
            (eq, ":event_no", event_find_hidden_place),#已经发现隐藏建筑就不用再探索了
            (call_script, "script_get_center_zone_building", "$current_town", "$g_current_rank", "$g_current_procession"),#建筑类型
            (assign, ":building_no", reg1),
            (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#有建筑
            (gt, ":building_no", "itm_building_begin"),
            (call_script, "script_cf_check_building_showed", "$current_town", "$g_current_rank", "$g_current_procession"),#已经发现
            (assign, ":power_no", 0),
         (else_try),
            (eq, ":event_no", event_assassination),#刺杀
            (neg|troop_slot_ge, "trp_player", slot_troop_renown, 1000),#声望超过1000才会被刺杀
            (neq, "$character_choose", "trp_quick_battle_troop_7"),#不是困难模式
            (assign, ":power_no", 0),
         (else_try),
            (this_or_next|eq, ":event_no", event_found_wallet),#捡钱
            (this_or_next|eq, ":event_no", event_street_singing),#街头卖唱
            (eq, ":event_no", event_handling_expired_food),#商家处理临期产品
            (lt, ":prosperity", 40),
            (assign, ":power_no", 0),#萧条时不会有人掉钱
         (else_try),
            (eq, ":event_no", event_bookcollector),#藏书家
            (lt, ":prosperity", 30),
            (val_add, ":power_no", 1),#萧条时藏书家抛售书本的概率增加
         (else_try),
            (eq, ":event_no", event_small_competition),#小型挑战赛
            (try_begin),
               (gt, ":prosperity", 66),
               (val_add, ":power_no", 1),#经济繁荣时挑战赛增多，萧条时减少
            (else_try),
               (lt, ":prosperity", 33),
               (val_sub, ":power_no", 1),
               (val_max, ":power_no", 0),
            (try_end),
         (else_try),
            (eq, ":event_no", event_beggar_begging),#乞讨
            (try_begin),
               (gt, ":prosperity", 66),
               (val_sub, ":power_no", 1),#经济繁荣时乞丐减少，萧条时乞丐增加
               (val_max, ":power_no", 0),
            (else_try),
               (lt, ":prosperity", 33),
               (val_add, ":power_no", 2),
            (try_end),
         (else_try),
            (this_or_next|eq, ":event_no", event_recruit_noble),#招募贵族子弟
            (this_or_next|eq, ":event_no", event_recruit_citizen),#招募市民
            (eq, ":event_no", event_recruit_refugee),#招募难民
            (lt, ":prosperity", 40),
            (val_add, ":power_no", 1),#萧条时外出打工意愿增加
         (try_end),

         (try_begin),
            (eq, ":event_no", event_street_singing),#街头卖唱
            (call_script, "script_cf_troop_has_item_equipped_with_modifier_new", "trp_player", "itm_lyre", -1),#里拉琴
            (val_mul, ":power_no", 6),
         (try_end),

         (try_for_range, reg10, 0, ":power_no"),
            (troop_set_slot, "trp_temp_array_a", ":total_event_count", ":event_no"), #在array里记录event，比如3号event权重是4，就占据四个slot
            (val_add, ":total_event_count", 1),
         (try_end),
      (try_end),
      (store_random_in_range, ":count_no", 1, ":total_event_count"),
      (troop_get_slot, "$g_current_event", "trp_temp_array_a", ":count_no"), #抽取的事件

#内定事件
      (try_begin),
         (this_or_next|eq, "$current_startup_quest_phase", 8),#新手剧情：在勒塞夫的贫民区发现权厄之秤的据点
         (eq, "$current_startup_quest_phase", 9),#困难模式被刺杀后
         (eq, "$current_town", "p_town_4"),
         (eq, "$g_player_rank", 13),
         (eq, "$g_player_procession", 5),
         (assign, "$g_current_event", event_find_hidden_place),
         (assign, "$current_startup_quest_phase", 10),
      (try_end),

#描述
      (try_begin),
         (eq, "$g_current_event", event_default),#无事发生
         (str_store_string, s10, "@什 么 事 都 没 有 发 生 。 你 度 过 了 安 宁 平 和 但 无 所 事 事 的 几 个 小 时 。 "),
      (else_try),
         (eq, "$g_current_event", event_find_hidden_place),#发现隐藏场所
         (call_script, "script_get_center_zone_building", "$current_town", "$g_current_rank", "$g_current_procession"),#建筑类型
         (assign, ":building_no", reg1),
         (is_between, ":building_no", "itm_building_begin", "itm_building_end"),#有建筑
         (gt, ":building_no", "itm_building_begin"),
         (str_store_item_name, s9, ":building_no"),
         (call_script, "script_set_building_showed", "$current_town", "$g_current_rank", "$g_current_procession"),#设置为发现
         (str_store_string, s10, "@你 发 现 了 隐 藏 的 {s9}！ 你 记 下 了 这 个 地 点 ， 之 后 你 能 直 接 前 往 此 处 。 "),
      (else_try),
         (eq, "$g_current_event", event_encountered_pickpocket),#遭遇扒手
         (str_store_string, s10, "@行 走 在 街 道 上 时 ， 你 突 然 感 到 腰 间 一 轻 ， 一 只 抓 着 钱 袋 的 手 从 你 口 袋 里 迅 速 抽 离 。 你 朝 那 只 手 抓 去 — — "),
      (else_try),
         (eq, "$g_current_event", event_encountered_robbery),#遭遇抢劫
         (store_random_in_range, "$temp", 200, 500),
         (val_div, "$temp", 10),
         (val_mul, "$temp", 10),
         (assign, reg8, "$temp"),
         (str_store_string, s10, "@你 发 现 有 几 道 不 怀 好 意 的 目 光 盯 着 你 ， 几 个 手 拿 武 器 的 混 混 从 四 面 向 你 走 来 。 周 围 的 本 地 人 似 乎 都 很 熟 悉 这 种 场 景 ， 沉 默 地 作 鸟 兽 散 ， 无 一 人 敢 上 前 阻 拦 。 ^“ 我 在 一 公 里 外 就 闻 到 了 你 这 个 鼓 鼓 囊 囊 的 钱 包 ， ” 为 首 的 人 说 道 ， “ 不 过 我 们 也 不 为 难 你 ， 给 我 们 {reg8}过 路 费 ， 我 们 就 放 你 离 开 。 ” ^^你 左 右 看 看 ， 并 没 有 士 兵 警 卫 等 任 何 能 帮 你 的 人 存 在 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_assassination),#遭遇刺杀
         (str_store_string, s10, "@你 的 余 光 瞥 见 一 抹 寒 意 袭 向 你 的 侧 腹 。 那 是 一 把 匕 首 ， 你 在 千 钧 一 发 之 际 躲 开 了 它 的 攻 击 。 目 标 明 确 、 下 手 利 落 ， 对 方 是 来 刺 杀 你 的 。 ^^你 拔 出 武 器 ， 逼 退 刺 客 ， 街 上 的 其 他 行 人 落 荒 而 逃 。 刺 客 见 偷 袭 未 果 ， 也 拔 出 兵 刃 ， 摆 好 架 势 ， 准 备 正 面 格 杀 你 。 你 决 定 — — "),

      (else_try),
         (eq, "$g_current_event", event_recruit_noble),#招募贵族子弟
         (try_begin),
            (troop_slot_ge, "trp_player", slot_troop_renown, 1500),#声望超过1500，荣誉超过40，现金超过10000
            (ge, "$player_honor", 40),
            (store_troop_gold, ":gold_count", "trp_player"),
            (ge, ":gold_count", 10000),
            (troop_slot_ge, "trp_player", slot_troop_banner_scene_prop, 1),#是贵族
            (str_store_string, s10, "@你 看 到 几 个 衣 冠 楚 楚 、 腰 挎 利 剑 的 年 轻 人 在 街 边 交 谈 ， 他 们 是 贵 族 家 族 的 旁 支 或 者 私 生 子 ， 虽 然 自 小 接 受 骑 士 的 教 育 ， 但 一 切 都 需 要 靠 自 己 去 打 拼 。 他 们 一 看 到 你 ， 便 向 你 行 了 个 礼 ， 向 你 走 来 。 ^^他 们 几 人 轮 番 进 行 了 自 我 介 绍 。 “ 我 们 接 受 过 良 好 的 教 育 ， 刻 苦 的 训 练 ， 渴 望 跟 随 一 位 实 力 雄 厚 的 大 人 ， 用 剑 为 自 己 开 创 一 番 事 业 。 ” 你 决 定 — — "),
         (else_try),
            (str_store_string, s10, "@你 看 到 几 个 衣 冠 楚 楚 、 腰 挎 利 剑 的 年 轻 人 在 街 边 交 谈 ， 他 们 是 贵 族 家 族 的 旁 支 或 者 私 生 子 ， 虽 然 自 小 接 受 骑 士 的 教 育 ， 但 一 切 都 需 要 靠 自 己 去 打 拼 。 在 你 观 察 他 们 的 同 时 ， 他 们 也 在 打 量 你 ， 并 很 快 就 失 去 了 兴 趣 。 很 明 显 ， 你 现 在 的 荣 誉 、 声 望 、 资 产 和 地 位 还 不 足 以 吸 引 他 们 为 你 效 力 。 "),
         (try_end),
      (else_try),
         (eq, "$g_current_event", event_recruit_citizen),#招募市民
         (try_begin),
            (troop_slot_ge, "trp_player", slot_troop_renown, 800),#声望超过800，荣誉超过20，现金超过3000
            (ge, "$player_honor", 20),
            (store_troop_gold, ":gold_count", "trp_player"),
            (ge, ":gold_count", 3000),
            (str_store_string, s10, "@你 看 到 几 个 衣 着 朴 素 的 年 轻 人 在 街 边 闲 逛 ， 他 们 是 普 通 市 民 家 的 孩 子 ， 但 不 甘 于 就 这 么 平 淡 度 过 一 辈 子 ， 希 望 过 上 用 刀 剑 赚 钱 的 刺 激 生 活 。 ^^看 到 你 走 过 ， 他 们 立 即 迎 了 上 来 ， 七 嘴 八 舌 地 自 我 介 绍 了 一 番 ， 激 动 地 表 达 了 对 你 的 崇 拜 和 敬 仰 ， 表 示 渴 望 加 入 你 的 部 队 ， 成 为 像 你 一 样 知 名 的 人 物 。 你 决 定 — — "),
         (else_try),
            (str_store_string, s10, "@你 看 到 几 个 衣 着 朴 素 的 年 轻 人 在 街 边 闲 逛 ， 他 们 是 普 通 市 民 家 的 孩 子 ， 但 不 甘 于 就 这 么 平 淡 度 过 一 辈 子 ， 希 望 过 上 用 刀 剑 赚 钱 的 刺 激 生 活 。  ^^看 到 你 身 上 的 甲 胄 和 武 器 ， 他 们 小 声 交 换 了 一 下 意 见 ， 最 终 还 是 没 有 什 么 表 示 。 你 现 在 的 荣 誉 、 声 望 和 资 产 还 不 足 以 吸 引 他 们 跟 随 你 。 "),
         (try_end),
      (else_try),
         (eq, "$g_current_event", event_recruit_refugee),#招募难民
         (try_begin),
            (ge, "$player_honor", 10),                                         #荣誉超过10，现金超过500
            (store_troop_gold, ":gold_count", "trp_player"),
            (ge, ":gold_count", 500),
            (str_store_string, s10, "@你 看 到 几 个 衣 不 蔽 体 的 人 在 街 边 乞 讨 ， 他 们 是 因 为 重 税 、 战 乱 、 魔 物 、 侵 蚀 而 流 离 失 所 的 难 民 ， 好 不 容 易 混 入 城 内 试 图 找 口 饭 吃 ， 却 许 久 无 法 找 到 一 个 容 身 之 所 。 ^^看 到 你 走 过 ， 他 们 立 即 围 了 上 来 ， 小 心 翼 翼 地 询 问 你 的 势 力 是 否 能 给 他 们 提 供 一 个 差 事 。 你 决 定 — — "),
         (else_try),
            (str_store_string, s10, "@你 看 到 几 个 衣 不 蔽 体 的 人 在 街 边 乞 讨 ， 他 们 是 因 为 重 税 、 战 乱 、 魔 物 、 侵 蚀 而 流 离 失 所 的 难 民 ， 好 不 容 易 混 入 城 内 试 图 找 口 饭 吃 ， 却 许 久 无 法 找 到 一 个 容 身 之 所 。 ^^他 们 木 然 地 看 着 你 走 过 。 你 的 荣 誉 与 财 力 还 不 足 以 让 他 们 把 你 当 成 救 星 。 "),
         (try_end),

      (else_try),
         (eq, "$g_current_event", event_commercial_information),#偷听商业信息
         (str_store_string, s10, "@在 一 座 宅 邸 旁 ， 你 通 过 半 掩 的 窗 户 听 到 了 两 人 的 对 谈 ， 大 意 是 对 市 场 行 情 的 分 析 和 预 估 。 意 识 到 这 些 信 息 或 许 会 有 用 ， 你 拿 纸 笔 记 录 了 下 来 。 "),
      (else_try),
         (eq, "$g_current_event", event_found_wallet),#捡到钱包
         (str_store_string, s10, "@你 看 到 了 一 个 鼓 鼓 囊 囊 的 钱 包 ！ 你 在 旁 边 等 待 了 一 下 ， 并 没 有 见 到 前 来 收 回 失 物 的 人 。 如 果 在 地 球 ， 你 或 许 会 把 它 交 给 警 察 ， 但 这 个 世 界 并 没 有 承 担 这 种 职 能 的 组 织 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_bookcollector),#藏书家抛售书籍
         (str_store_string, s10, "@你 听 说 本 地 有 个 藏 书 家 因 为 某 种 原 因 ， 正 在 大 量 抛 售 他 的 书 籍 。 当 你 赶 到 时 ， 他 的 藏 书 不 是 已 经 卖 出 ， 就 是 被 其 他 人 预 定 了 。 不 过 ， 经 过 一 番 翻 找 ， 你 还 是 捡 到 了 小 小 的 便 宜 。 "),
      (else_try),
         (eq, "$g_current_event", event_visit_master),#拜访大师
         (str_store_string, s10, "@你 偶 遇 了 一 位 在 当 地 小 有 名 气 的 格 斗 大 师 ， 他 对 你 有 些 兴 趣 ， 邀 请 你 切 磋 了 两 招 ， 并 讨 论 了 一 番 使 用 武 器 的 心 得 。 你 感 觉 你 的 武 器 熟 练 度 提 升 了 。 "),
         (store_random_in_range, ":count_no", 0, 6),
         (troop_raise_proficiency, "trp_player", ":count_no", 5),
      (else_try),
         (eq, "$g_current_event", event_slave_trader),#奴隶贩子贩卖奴隶
         (assign, "$temp", "trp_refugee"),
         (str_store_troop_name, s11, "$temp"),
         (store_random_in_range, "$temp_2", 3, 10),
         (assign, reg21, "$temp_2"),
         (str_store_string, s10, "@你 在 街 上 遇 到 了 一 个 奴 隶 商 人 ， 他 神 秘 兮 兮 地 凑 过 来 对 你 说 ， 自 己 搞 到 了 一 些 {s11}俘 虏 ， 可 以 低 价 卖 给 你 {reg21} 个 。 ^^奴 隶 买 卖 在 很 多 国 家 属 于 非 法 ， 在 合 法 的 地 方 也 被 课 以 重 税 ， 像 这 样 一 小 批 一 小 批 销 赃 的 奴 贩 并 不 鲜 见 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_ransom_broker),#赎金经纪人贩卖士兵
         (assign, "$temp", "trp_yishith_chivalric_knight"),
         (str_store_troop_name, s11, "$temp"),
         (str_store_string, s10, "@你 在 街 上 遇 到 了 一 个 自 称 赎 金 经 纪 人 的 人 ， 他 神 秘 兮 兮 地 凑 过 来 对 你 说 ， 自 己 手 头 有 一 位 被 俘 的 {s11}， 因 为 找 不 到 人 支 付 赎 金 ， 一 直 滞 留 在 他 的 手 上 。 ^在 连 绵 不 断 的 战 争 中 ， 各 国 已 经 学 会 了 保 持 克 制 和 底 线 ， 被 俘 虏 的 贵 族 、 军 官 和 部 分 正 规 军 并 不 会 遭 到 残 酷 的 对 待 ， 而 是 会 通 过 特 殊 的 渠 道 交 换 成 大 笔 赎 金 。 不 过 找 不 到 人 为 某 人 支 付 赎 金 的 情 况 也 存 在 ， 这 时 赎 金 经 纪 人 便 会 通 过 其 他 手 段 — — 有 时 是 见 不 得 光 的 — — 来 收 回 自 己 的 成 本 。 ^^你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_small_competition),#小型挑战赛
         (str_store_string, s10, "@你 听 说 本 地 的 一 个 商 会 举 行 活 动 ， 举 办 了 一 场 小 型 挑 战 赛 ， 拿 出 了 一 笔 不 小 的 奖 金 作 为 挑 战 获 胜 的 奖 励 。 任 何 人 都 能 参 加 ， 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_dragon_blood_merchant),#龙血商人
         (str_store_string, s10, "@一 个 商 人 模 样 的 人 拉 住 了 你 。 “ 你 想 要 力 量 吗 ？ ” 他 如 此 问 你 ， “ 你 知 道 贵 族 老 爷 们 强 大 的 秘 诀 吗 ？ 他 们 人 人 都 在 定 期 、 大 量 地 吞 吃 龙 种 ， 由 此 获 得 了 龙 力 ， 而 我 恰 好 是 个 售 卖 龙 血 的 商 人 。 ” ^^据 他 所 言 ， 贵 族 购 入 一 整 条 龙 后 ， 会 将 精 华 割 走 ， 把 边 角 料 当 作 赏 赐 发 给 麾 下 士 兵 。 这 之 中 总 有 人 不 想 要 力 量 ， 只 要 想 金 钱 ， 他 手 上 的 龙 血 酒 就 是 从 这 种 渠 道 收 购 来 的 。 虽 不 违 法 ， 但 若 被 贵 族 发 现 ， 难 免 会 招 致 一 些 非 议 ， 只 能 偷 偷 售 卖 。 ^^了 解 了 上 述 情 况 后 ， 你 决 定 — — "),

      (else_try),
         (eq, "$g_current_event", event_discover_scandal_1),#发现丑闻一
         (str_store_string, s10, "@你 穿 过 一 条 小 巷 时 ， 撞 见 一 对 衣 着 华 丽 的 年 轻 男 女 正 在 激 情 拥 吻 。 还 没 等 你 从 记 忆 里 挖 掘 出 这 两 人 的 家 世 背 景 ， 他 们 就 像 装 了 弹 簧 一 样 快 速 分 开 。 ^^“ 我 恳 请 您 忘 掉 这 里 发 生 的 事 ， 这 些 钱 是 我 的 心 意 。 ” 男 青 年 给 了 你 一 个 鼓 鼓 囊 囊 的 钱 袋 ， 拉 着 他 的 小 情 侣 飞 快 跑 掉 了 。 虽 然 你 根 本 不 认 识 他 们 ， 但 还 是 欣 然 收 下 了 这 笔 封 口 费 。 "),
         (troop_add_gold, "trp_player", 200),
      (else_try),
         (eq, "$g_current_event", event_discover_scandal_2),#发现丑闻二
         (str_store_string, s10, "@你 穿 过 一 条 小 巷 时 ， 撞 见 两 个 衣 冠 楚 楚 的 人 ， 在 保 镖 和 打 手 的 簇 拥 下 交 谈 着 某 些 东 西 。 你 感 觉 气 氛 有 些 不 对 ， 刚 想 避 开 ， 他 们 看 到 了 你 ， 脸 色 大 变 。 ^^“ 不 能 让 别 人 发 现 ， 动 手 ！ ” 几 个 保 镖 和 打 手 气 势 汹 汹 地 围 了 上 来 ， 作 势 要 用 剑 让 你 永 远 闭 嘴 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_noble_beat_servant),#贵族殴打仆人
         (str_store_string, s10, "@你 看 到 一 个 衣 冠 楚 楚 的 人 正 在 当 街 殴 打 他 的 仆 人 ， 足 以 轻 松 打 碎 红 砖 的 重 拳 如 雨 点 般 落 下 ， 把 对 方 打 得 浑 身 青 紫 ， 只 有 进 的 气 ， 没 有 出 的 气 了 。 ^^周 围 的 人 大 多 冷 眼 旁 观 着 ， 虽 有 少 数 面 露 恻 隐 ， 但 也 不 想 上 前 阻 拦 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_noble_assassinated),#贵族遭遇刺杀
         (str_store_string, s10, "@你 正 在 街 上 走 着 ， 突 然 一 旁 的 人 群 中 爆 发 出 一 阵 骚 乱 ， 随 后 是 连 续 几 声 金 铁 相 击 的 鸣 响 。 路 人 四 散 而 逃 ， 你 看 到 一 个 贵 族 打 扮 的 年 轻 人 正 在 刺 客 的 进 攻 下 苦 苦 支 撑 ， 在 他 身 边 躺 着 两 具 护 卫 的 尸 体 。 ^^“ 那 边 的 人 ， 救 下 我 我 家 里 必 重 重 有 赏 ！ ” 年 轻 贵 族 冲 你 喊 道 。 你 决 定 — — "),

      (else_try),
         (eq, "$g_current_event", event_street_singing),#街头卖唱
         (assign, ":count_no", 0),
         (val_add, ":count_no", "$allegoric_poem_recitations"),
         (val_add, ":count_no", "$mystic_poem_recitations"),
         (val_add, ":count_no", "$tragic_poem_recitations"),
         (val_add, ":count_no", "$heroic_poem_recitations"),
         (val_add, ":count_no", "$comic_poem_recitations"),
         (call_script, "script_get_center_zone_ground", "$current_town", "$g_player_rank", "$g_player_procession"),
         (assign, ":cur_zone", reg1),
         (try_begin),
            (eq, ":cur_zone", "itm_zone_rich_area"),
            (val_mul, ":count_no", 60),
         (else_try),
            (val_mul, ":count_no", 40),
         (try_end),
         (try_begin),
            (call_script, "script_cf_troop_has_item_equipped_with_modifier_new", "trp_player", "itm_lute", -1),#鲁特琴
            (val_mul, ":count_no", 2),
         (try_end),

         (try_begin),
            (eq, ":count_no", 0),
            (str_store_string, s11, "@可 是 临 到 要 唱 了 你 才 发 现 ， 自 己 竟 然 一 首 本 地 的 诗 歌 都 不 会 。 本 来 你 想 唱 两 首 地 球 的 口 水 歌 ， 但 转 念 一 想 ， 要 是 因 为 歌 曲 太 过 摩 登 暴 露 穿 越 者 的 身 份 ， 那 就 糗 大 了 。 最 后 你 灰 溜 溜 地 离 开 了 。 "),
         (else_try),
            (lt, ":count_no", 200),
            (str_store_string, s11, "@你 这 一 唱 的 反 响 不 错 ， 也 赚 到 了 一 些 钱 。 不 过 你 自 觉 还 有 提 升 空 间 ， 或 许 能 从 乐 器 、 学 会 的 诗 歌 数 量 、 选 择 驻 唱 的 地 区 等 方 面 加 以 改 进 。 "),
            (troop_add_gold, "trp_player", ":count_no"),
         (else_try),
            (str_store_string, s11, "@你 的 歌 声 吸 引 了 大 量 路 人 围 观 ， 甚 至 还 有 一 个 自 称 吟 游 诗 人 社 团 的 组 织 拉 你 入 伙 ， 对 此 你 表 示 婉 拒 。 最 后 你 收 获 颇 丰 。 "),
            (troop_add_gold, "trp_player", ":count_no"),
         (try_end), 
         (str_store_string, s10, "@你 发 现 了 一 个 极 好 驻 唱 的 场 所 ， 心 血 来 潮 ， 拉 开 架 势 弹 唱 了 一 首 。 {s11}"),

      (else_try),
         (eq, "$g_current_event", event_handling_expired_food),#商家处理临期产品
         (str_store_string, s10, "@你 路 过 一 个 店 铺 时 ， 看 到 店 家 提 着 一 大 包 临 期 的 肉 食 ， 丢 到 门 外 的 垃 圾 堆 上 。 或 许 你 可 以 把 它 捡 起 来 … … "),
      (else_try),
         (eq, "$g_current_event", event_beggar_begging),#乞丐乞讨
         (str_store_string, s10, "@“ 行 行 好 ， 打 发 打 发 点 吧 。 ” 路 边 一 个 衣 着 破 烂 的 乞 丐 向 你 晃 荡 他 的 破 碗 ， 碗 中 只 有 两 个 陶 币 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_discover_orphanage),#发现孤儿院
         (str_store_string, s10, "@你 偶 遇 了 一 座 规 模 不 大 的 孤 儿 院 ， 其 中 收 养 了 十 几 个 小 孩 ， 大 部 分 是 因 为 战 乱 和 瘟 疫 失 去 父 母 的 。 这 家 孤 儿 院 经 营 状 况 并 不 算 好 ， 但 孩 子 们 却 很 快 乐 ， 由 此 观 之 孤 儿 院 管 理 者 的 品 行 应 该 值 得 信 任 。 你 决 定 — — "),
      (else_try),
         (eq, "$g_current_event", event_find_stolen_goods),#发现赃物
         (str_store_string, s10, "@你 误 打 误 撞 地 发 现 了 一 幢 摇 摇 欲 坠 的 小 木 屋 ， 透 过 墙 上 的 缝 隙 ， 你 看 到 一 口 与 建 筑 格 格 不 入 的 箱 子 。 怀 着 来 都 来 了 ， 不 如 看 一 眼 的 心 态 ， 你 打 开 了 箱 子 ， 发 现 里 面 堆 满 了 钱 币 。 你 决 定 — — "),
      (try_end),
    ],
    [
      ("event_encountered_pickpocket_1",[
         (eq, "$g_current_event", event_encountered_pickpocket),#遭遇扒手
         (store_skill_level, ":skill_level", skl_tracking, "trp_player"),#追猎
         (le, ":skill_level", 3),#追猎小于3
      ],"你 没 能 抓 住 对 方 。 ",[
         (store_random_in_range, ":count_no", 30, 100),
         (troop_remove_gold, "trp_player", ":count_no"),
         (jump_to_menu,"mnu_center_new"),
      ]),
      ("event_encountered_pickpocket_2",[#遭遇扒手
         (eq, "$g_current_event", event_encountered_pickpocket),
         (store_skill_level, ":skill_level", skl_tracking, "trp_player"),#追猎
         (gt, ":skill_level", 3),#追猎小于3
      ],"你 抓 住 了 对 方 ， 现 在 他 成 为 你 的 俘 虏 了 。 ",[
         (party_add_prisoners, "p_main_party", "trp_refugee", 1),
         (call_script, "script_change_player_relation_with_center", "$current_town", 1),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_encountered_robbery_1",[#遭遇抢劫
         (eq, "$g_current_event", event_encountered_robbery),
      ],"老 实 付 钱 。 ",[
         (troop_remove_gold, "trp_player", "$temp"),
         (jump_to_menu,"mnu_center_new"),
      ]),
      ("event_encountered_robbery_2",[#遭遇抢劫
         (eq, "$g_current_event", event_encountered_robbery),
      ],"让 他 们 后 悔 出 生 。 ",[
         (call_script, "script_random_event_center_bandit"),
      ]),

      ("event_assassination",[#遭遇刺杀
         (eq, "$g_current_event", event_assassination),
      ],"把 他 剁 成 肉 泥 。 ",[
         (call_script, "script_random_event_center_assassin"),
      ]),

      ("event_recruit_noble",[#招募贵族子弟
         (eq, "$g_current_event", event_recruit_noble),
         (troop_slot_ge, "trp_player", slot_troop_renown, 1500),#声望超过1500，荣誉超过40，现金超过10000
         (ge, "$player_honor", 40),
         (store_troop_gold, ":gold_count", "trp_player"),
         (ge, ":gold_count", 10000),
         (troop_slot_ge, "trp_player", slot_troop_banner_scene_prop, 1),#是贵族
      ],"接 受 他 们 的 投 靠 。 ",[
         (store_random_in_range, ":count_no", 2, 6),
         (party_add_members, "p_main_party", "trp_gold_adventurer", ":count_no"),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_recruit_citizen",[#招募市民
         (eq, "$g_current_event", event_recruit_citizen),
         (troop_slot_ge, "trp_player", slot_troop_renown, 800),#声望超过800，荣誉超过20，现金超过3000
         (ge, "$player_honor", 20),
         (store_troop_gold, ":gold_count", "trp_player"),
         (ge, ":gold_count", 3000),
      ],"接 受 他 们 的 投 靠 。 ",[
         (store_random_in_range, ":count_no", 4, 10),
         (party_add_members, "p_main_party", "trp_barecopper_adventurer", ":count_no"),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_recruit_refugee",[#招募难民
         (eq, "$g_current_event", event_recruit_refugee),
         (ge, "$player_honor", 10),                                              #荣誉超过10，现金超过500
         (store_troop_gold, ":gold_count", "trp_player"),
         (ge, ":gold_count", 500),
      ],"接 受 他 们 的 投 靠 。 ",[
         (store_random_in_range, ":count_no", 6, 14),
         (party_add_members, "p_main_party", "trp_refugee", ":count_no"),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_found_wallet",[#捡钱
         (eq, "$g_current_event", event_found_wallet),
      ],"据 为 己 有 。 ",[
         (store_random_in_range, ":count_no", 50, 150),
         (troop_add_gold, "trp_player", ":count_no"),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_bookcollector",[#藏书家抛售书籍
         (eq, "$g_current_event", event_bookcollector),
         (call_script, "script_get_book_sold"),
         (gt, reg1, 0),
         (assign, "$temp", reg1),
         (str_store_item_name, s20, "$temp"),
         (item_get_value, "$temp_2", "$temp"),
         (val_div, "$temp_2", 3),
         (assign, reg10, "$temp_2"),
      ],"花 {reg10}铁 币 买 下 {s20}。 ",[
         (try_begin),
            (store_troop_gold, ":gold_count", "trp_player"),
            (ge, ":gold_count", "$temp_2"),
            (troop_remove_gold, "trp_player", "$temp_2"),
            (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "$temp", 0, 0, 0),
            (jump_to_menu,"mnu_center_new"),
         (else_try),
            (display_message, "@你 没 这 么 多 现 金 。 "),
            (jump_to_menu,"mnu_center_new"),
         (try_end),
      ]),

      ("event_slave_trader",[#奴隶贩子贩卖奴隶
         (eq, "$g_current_event", event_slave_trader),
         (store_character_level, ":count_no", "$temp"),
         (val_add, ":count_no", 10),
         (val_mul, ":count_no", ":count_no"),
         (val_div, ":count_no", 9),
         (val_max, ":count_no", 35),
         (val_mul, ":count_no", "$temp_2"),
         (store_troop_gold, ":gold_count", "trp_player"),
         (ge, ":gold_count", ":count_no"),
         (assign, "$temp_3", ":count_no"),
         (assign, reg10, "$temp_3"),
      ],"花 {reg10}铁 币 买 下 这 些 奴 隶 。 ",[
         (troop_remove_gold, "trp_player", "$temp_3"),
         (party_add_prisoners, "p_main_party", "$temp", "$temp_2"),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_ransom_broker",[#赎金经纪人贩卖士兵
         (eq, "$g_current_event", event_ransom_broker),
         (store_character_level, ":count_no", "$temp"),
         (val_add, ":count_no", 10),
         (val_mul, ":count_no", ":count_no"),
         (val_div, ":count_no", 6),
         (val_max, ":count_no", 50),
         (store_troop_gold, ":gold_count", "trp_player"),
         (ge, ":gold_count", ":count_no"),
         (assign, "$temp_2", ":count_no"),
         (assign, reg10, "$temp_2"),
      ],"花 {reg10}铁 币 赎 回 这 个 士 兵 。 ",[
         (troop_remove_gold, "trp_player", "$temp_2"),
         (party_add_members, "p_main_party", "$temp", 1),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_small_competition",[#小型挑战赛
         (eq, "$g_current_event", event_small_competition),
         (assign, "$temp", "trp_starkhook_condottiere"),
         (str_store_troop_name, s11, "$temp"),
      ],"迎 战 出 战 的 {s11}。 ",[
         (call_script, "script_random_event_competition"),
      ]),

      ("event_dragon_blood_merchant",[#龙血商人
         (le, "$g_event_continue", 0),
         (eq, "$g_current_event", event_dragon_blood_merchant),
         (troop_clear_inventory, "trp_temp_array_a"),
         (store_troop_gold, ":count_no", "trp_temp_array_a"),
         (troop_remove_gold, "trp_temp_array_a", ":count_no"),

         (store_random_in_range, ":count_no", 4, 8),
         (troop_add_items, "trp_temp_array_a", "itm_raw_dragonblood", ":count_no"),
         (store_random_in_range, ":count_no", 3, 6),
         (troop_add_items, "trp_temp_array_a", "itm_inferior_dragonblood_wine", ":count_no"),
         (store_random_in_range, ":count_no", 2, 5),
         (troop_add_items, "trp_temp_array_a", "itm_superior_dragonblood_wine", ":count_no"),
         (try_begin),
            (store_random_in_range, ":count_no", 1, 5),
            (eq, ":count_no", 5),
            (troop_add_items, "trp_temp_array_a", "itm_raw_dragon_meat", 1),
         (else_try),
         (try_begin),
            (store_random_in_range, ":count_no", 1, 10),
            (eq, ":count_no", 5),
            (troop_add_items, "trp_temp_array_a", "itm_powell_noble_hand_and_a_half_sword", 1),
         (else_try),
      ],"看 看 他 的 商 品 。 ",[
         (assign, "$g_event_continue", 1),#进入一次就不能再进入了
         (change_screen_trade, "trp_temp_array_a"),
      ]),

      ("event_discover_scandal_2",[#发现丑闻二
         (eq, "$g_current_event", event_discover_scandal_2),
      ],"撕 碎 他 们 。 ",[
         (call_script, "script_random_event_discover_scandal"),
      ]),

      ("event_noble_beat_servant",[#贵族殴打仆人
         (eq, "$g_current_event", event_noble_beat_servant),
         (store_skill_level, ":skill_level", skl_persuasion, "trp_player"),#灼言
         (ge, ":skill_level", 6),#灼言大于等于6
         (store_attribute_level, ":skill_level", "trp_player", ca_charisma),#魅力
         (ge, ":skill_level", 20),#魅力大于20
      ],"说 服 他 停 手 。 ",[
         (jump_to_menu,"mnu_center_new"),
         (call_script, "script_change_player_honor", 2),#荣誉提升
         (call_script, "script_change_player_relation_with_center", "$current_town", 2),
      ]),

      ("event_noble_assassinated",[#贵族遭遇刺杀
         (eq, "$g_current_event", event_noble_assassinated),
      ],"助 他 一 臂 之 力 。 ",[
         (call_script, "script_random_event_noble_assassinated"),
      ]),

      ("event_handling_expired_food",[#商家处理临期产品
         (eq, "$g_current_event", event_handling_expired_food),
      ],"捡 ！ 民 以 食 为 天 。 ",[
         (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_chicken", "itm_imod_39", 0, 0),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_beggar_begging",[#乞丐乞讨
         (eq, "$g_current_event", event_beggar_begging),
         (store_troop_gold, ":count_no", "trp_player"),
         (ge, ":count_no", 1),
      ],"给 他 一 枚 铁 币 。 ",[
         (try_begin),
            (store_random_in_range, ":count_no", 0, 5),
            (eq, ":count_no", 2),
            (call_script, "script_change_player_honor", 1),#荣誉提升
         (try_end),
         (try_begin),
            (store_random_in_range, ":count_no", 0, 5),
            (eq, ":count_no", 2),
            (call_script, "script_change_player_relation_with_center", "$current_town", 1),
         (try_end),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_beggar_begging",[#发现孤儿院
         (eq, "$g_current_event", event_discover_orphanage),
         (store_troop_gold, ":count_no", "trp_player"),
         (ge, ":count_no", 300),
      ],"赞 助 他 们 三 百 铁 币 。 ",[
         (call_script, "script_change_player_honor", 1),#荣誉提升
         (call_script, "script_change_player_relation_with_center", "$current_town", 2),
         (jump_to_menu,"mnu_center_new"),
      ]),

      ("event_find_stolen_goods",[#发现赃物
         (eq, "$g_current_event", event_find_stolen_goods),
      ],"全 部 搜 刮 走 。 ",[
         (store_random_in_range, ":count_no", 500, 800),
         (troop_add_gold, "trp_player", ":count_no"),
         (jump_to_menu,"mnu_center_new"),
      ]),


      ("leave_exploration",[
         (neq, "$g_current_event", event_assassination),#刺杀
         (neq, "$g_current_event", event_encountered_pickpocket),#遭遇扒手
         (neq, "$g_current_event", event_encountered_robbery),#抢劫
         (neq, "$g_current_event", event_discover_scandal_2),#发现丑闻二
      ],"直 接 离 开 。 ",[
         (jump_to_menu,"mnu_center_new"),
      ]),
    ]
  ),



##会战沙盘，野战遭遇的第一个menu，能选择进入会战菜单或者常规的直接进攻模式，用于快速清理野怪。
##
  ("campaign_enter", menu_text_color(0xFFFFFF), 
    "{s2}",
    "none",
    [  #遭遇的敌方部队为"$g_encountered_party"，如果有己方部队（比如已经在攻城或者交战中）为"$g_encountered_party_2"
      (set_background_mesh, "mesh_campaign_window"),
      (assign, "$current_town", "p_campaign_temp"), #为了与城镇统一，使用"$current_town"，不过并不影响"$g_encountered_party"

      (set_fixed_point_multiplier, 1000),
      (party_get_position, pos1, "p_main_party"),
      (party_get_current_terrain, ":current_terrain", "p_main_party"),
      (position_get_x, ":map_x", pos1),
      (position_get_y, ":map_y", pos1),
      (call_script, "script_get_natural_zone", ":map_x", ":map_y", ":current_terrain"), #获取自然环境名称s10
      (assign, ":current_terrain_new", reg1), #特殊处理用于确定沙盘底板的terrain

      (try_begin),
         (eq, "$campaign_round", -1), #刚接触
         (assign, "$campaign_round", 0), 
         (assign, "$encountered_party_hostile", 0),
         (assign, "$encountered_party_friendly", 0),
         (assign, "$g_start_campaign", 0), #先不摆阵，此全局变量储存对方使用的阵型
         (assign, "$g_lord_talk", 0), #控制是否在军营会面
         (try_begin),
            (gt, "$g_encountered_party_relation", 50),
            (assign, "$encountered_party_friendly", 1),
         (try_end),
         (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (try_begin),
               (encountered_party_is_attacker),
               (assign, "$g_leave_encounter", 0), #不准离开
            (try_end),
         (try_end),
         (assign, "$talk_context", tc_party_encounter), #设定谈话内容为大地图遭遇类型
         (call_script, "script_setup_party_meeting", "$g_encountered_party"),
      (else_try),
         (eq, "$campaign_round", 0), #第0轮，会战准备阶段，将初始化沙盘等信息，后续将不会再动此处
         (call_script, "script_party_count_members_function", "p_main_party"), #玩家人数
         (assign, ":player_count", reg0),
         (call_script, "script_party_count_members_function", "$g_encountered_party"), #敌方人数和职能
         (assign, ":enemy_count", reg0),
         (this_or_next|ge, ":enemy_count", 1000), #双方都低于1000人就不会区分编队
         (ge, ":player_count", 1000),
         (ge, "$g_start_campaign", "itm_formation_common"), #摆阵

##获取地形信息
         (assign, "$campaign_cam_set", -1), #初始化镜头设置
         (store_time_of_day, "$campaign_time"), #记录时间
         (call_script, "script_draw_random_sandtable", ":current_terrain_new", "scn_random_sandtable_plain_1"), #获取地图底板和随机生成区块信息

##生成编队，录入基础信息
         (try_for_range, ":slot_no", 0, 500), 
            (troop_set_slot, "trp_temp_array_detachment", ":slot_no", -1), #清空
         (try_end),
         (assign, "$g_total_detachment", 0), #编队总数，便于存取slot
         (try_begin),
            (eq, "$encountered_party_hostile", 1), #敌对
            (assign, ":team_no", 2),
         (else_try),
            (eq, "$encountered_party_friendly", 1), #友好
            (assign, ":team_no", 1),
         (else_try),
            (assign, ":team_no", 0), #中立
         (try_end), 
         (call_script, "script_auto_create_detachment", "$g_encountered_party", ":enemy_count", ":team_no", 0), #计算总人数获得编队人数、数量，并创建临时party以待使用
         (assign, ":detachment_count", reg1), #分队数量（全编队数储存为"$g_total_detachment"，此处只包括由这一个部队生成的）

##确定阵型
         (try_begin), 
            (neq, "$g_start_campaign", "itm_formation_station"), #驻扎状态不需要获取阵型（在预先对话等位置设置）
            (call_script, "script_auto_choose_formation", "$g_encountered_party"),
            (assign, "$g_start_campaign", reg1),
         (try_end),

##分兵，摆放编队
         (call_script, "script_auto_allocate_troop", "$g_encountered_party", "$g_start_campaign", ":detachment_count"), #分兵
         (call_script, "script_set_detachment_attitude", "$g_encountered_party", -1), #设置编队初始姿态，暂无预设，根据会战的模式可能会改
         (call_script, "script_auto_create_formation", "$g_encountered_party", "$g_start_campaign", "$current_town"), #根据阵型安放编队

         (try_for_range, ":unused", 0, 5), #先预设五步，后续可能根据会战情况，不同部队有所不同
            (call_script, "script_campaign_ai", "$current_town", "$g_encountered_party"), #AI自动行动
         (try_end),

         (val_add, "$campaign_round", 1), #生成完毕，进入第一轮
      (try_end),

      (party_is_active, "$g_encountered_party"), #获取部队名
      (str_store_party_name, s1,"$g_encountered_party"), 
      (party_stack_get_troop_id, ":lord_troop_no", "$g_encountered_party", 0), #获取领队
      (str_store_troop_name, s5, ":lord_troop_no"),
      (try_begin),
         (le, "$g_start_campaign", 0), #未摆阵
         (str_store_string, s3, "@对 方 未 做 战 斗 准 备 。 "),
      (else_try),
         (str_store_item_name, s3, "$g_start_campaign"),
         (str_store_string, s3, "@对 方 摆 出 了 {s3}。 "),
      (try_end),
      (try_begin),
         (eq, "$g_lord_talk", 1),  #简单会面
         (str_store_string, s4, "@{s5}允 许 你 临 时 见 其 一 面 。 "),
      (else_try),
         (eq, "$g_lord_talk", 2),  #正式会面
         (str_store_string, s4, "@{s5}邀 你 前 往 其 军 营 会 谈 。 "),
      (else_try),
         (str_store_string, s4, "@{s5}并 不 想 见 你 。 "),
      (try_end),

#      (call_script, "script_get_center_zone_ground", "p_campaign_temp", "$g_player_rank", "$g_player_procession"),
#      (assign, ":cur_zone", reg1),
#      (str_store_item_name, s6, ":cur_zone"),

      (str_store_string, s2, "@你 在 {s10}遭 遇 了 {s1}， {s3}^{s4}"),
    ],

    [
      ("check_campaign_map",[
         (ge, "$g_start_campaign", "itm_formation_common"), #摆阵
      ],"查 看 会 战 地 图 。 ",[
         (modify_visitors_at_site, "$current_scene"),
         (reset_visitors),
         (set_visitor, 1, "trp_player"),
         (set_jump_mission,"mt_sandbox"),
         (jump_to_scene, "$current_scene"),
         (change_screen_mission),
      ]),

      ("leave_battle",[
         (party_stack_get_troop_id, ":lord_troop_no", "$g_encountered_party", 0), #获取领队
         (str_store_troop_name, s11, ":lord_troop_no"),
         (ge, "$g_lord_talk", 1), #会面
      ],"会 见 {s11} 。 ",[
         (assign, "$g_leave_encounter", 1), #见完面允许离开
      ]),

      ("leave_battle",[
         (eq, "$g_leave_encounter", 1),
      ],"离 开 。 ",[
         (change_screen_return),
         (assign, "$campaign_round", -1), #清空会战轮次。会战结束的位置一定要留意将其清空，不然会很麻烦
      ]),
    ]
  ),



##会战沙盘的具体战斗界面，也是一轮一轮的行动后会回到的地方。
##
  ("campaign_round", menu_text_color(0xFFFFFF), 
    "{s2}",
    "none",
    [  #遭遇的敌方部队为"$g_encountered_party"，如果有己方部队（比如已经在攻城或者交战中）为"$g_encountered_party_2"
      (set_background_mesh, "mesh_campaign_window"),

#      (call_script, "script_get_center_zone_ground", "p_campaign_temp", "$g_player_rank", "$g_player_procession"),
#      (assign, ":cur_zone", reg1),
#      (str_store_item_name, s6, ":cur_zone"),
      (str_store_string, s2, "@会 战 菜 单 "),
    ],

    [
      ("next_round",[
      ],"进 入 下 一 轮 。 ",[
         (call_script, "script_campaign_ai", "$current_town", -1), #AI行动
         (jump_to_menu, "mnu_campaign_round"),
      ]),

      ("check_campaign_map",[
      ],"查 看 会 战 地 图 。 ",[
         (modify_visitors_at_site, "$current_scene"),
         (reset_visitors),
         (set_visitor, 1, "trp_player"),
         (set_jump_mission,"mt_sandbox"),
         (jump_to_scene, "$current_scene"),
         (change_screen_mission),
      ]),

      ("leave_battle",[
      ],"离 开 。 ",[
         (try_begin),
            (eq, "$g_quick_battle_encounter_mode_confirmed", 1), #只有快速战斗会用到的全局变量
            (change_screen_quit),
         (else_try),
            (change_screen_return),
            (assign, "$campaign_round", -1), #清空会战轮次。会战结束的位置一定要留意将其清空，不然会很麻烦
            (assign, "$campaign_cam_set", -1), #清空镜头设置
         (try_end),
      ]),
    ]
  ),







#######################################################剧情相关######################################################
##
  ("plot_special_enter", 0, #剧情需要的特殊菜单，比如进入某城堡村不进常规页面直接跳转到某场景。
    "{s5}",
    "none",
    [
      (store_encountered_party, "$current_town"),
      (try_begin),
         (eq, "$current_startup_quest_phase", 5),
         (eq, "$current_town", "p_town_4"),#勒塞夫
         (check_quest_active, "qst_game_start_quest"),#开局剧情：勒塞夫街头观摩公开处刑
         (str_store_string, s5, "@你 进 入 了 勒 塞 夫 。 大 雾 弥 漫 ， 伸 手 不 见 五 指 ， 本 应 熙 熙 攘 攘 的 街 道 现 在 空 无 一 人 ， 浓 雾 深 处 火 光 攒 动 ， 似 乎 正 在 举 行 什 么 活 动 。 "),
      (else_try),
         (eq, "$third_death_quest_phase", 1),
         (eq, "$current_town", "p_village_1_12"),#加尔村
         (check_quest_active, "qst_third_death"),#支线剧情：第三个死
         (str_store_string, s5, "@你 和 范 伦 汀 娜 进 入 加 尔 村 。 不 知 从 何 时 起 ， 暗 淡 的 雾 霭 升 腾 ， 渐 渐 笼 罩 了 你 的 视 野 。 走 了 许 久 也 没 有 听 见 人 声 ， 回 头 望 去 ， 来 时 路 亦 被 浓 雾 封 锁 。 一 种 不 祥 的 预 感 浮 上 你 的 心 头 。 "),
      (else_try),
         (is_between, "$third_death_quest_phase", 11, 13),
         (eq, "$current_town", "p_village_1_12"),#加尔村
         (check_quest_active, "qst_third_death"),#支线剧情：第三个死
         (str_store_string, s5, "@再 次 踏 上 前 往 旧 加 尔 村 的 路 ， 尽 管 你 极 力 地 想 去 观 察 雾 霭 升 腾 起 来 的 过 程 ， 但 回 过 神 来 时 ， 你 们 已 经 身 处 浓 雾 之 中 。 一 如 … … 曾 经 鲜 活 的 人 、 事 、 物 ， 不 知 不 觉 间 失 色 于 历 史 中 。 "),
      (else_try),
         (eq, "$third_death_quest_phase", 20),
         (eq, "$current_town", "p_village_1_12"),#加尔村
         (check_quest_active, "qst_third_death"),#支线剧情：第三个死
         (str_store_string, s5, "@雾 比 前 两 次 要 淡 ， 你 有 种 预 感 ， 这 将 会 是 你 们 最 后 一 次 踏 进 这 片 谬 史 。 "),
      (try_end),
    ],
    [
      ("continue",[
      ],"继 续 。 ",[
         (try_begin),
            (eq, "$current_startup_quest_phase", 5),
            (eq, "$current_town", "p_town_4"),#勒塞夫
            (check_quest_active, "qst_game_start_quest"),#支线剧情：勒塞夫街头观摩公开处刑
            (call_script, "script_lesaff_street_execution"),
         (else_try),
            (eq, "$current_town", "p_village_1_12"),#加尔村
            (check_quest_active, "qst_third_death"),#支线剧情：第三个死
            (call_script, "script_third_death"),
         (try_end),
      ]),
    ]
  ),


  ("plot_special_leave", 0, #剧情需要的特殊菜单，从场景里出来。
    "{s5}",
    "none",
    [
      (store_encountered_party, "$current_town"),
      (try_begin),
         (eq, "$third_death_quest_phase", 9),
         (eq, "$current_town", "p_village_1_12"),#加尔村
         (check_quest_active, "qst_third_death"),#支线剧情：第三个死
         (str_store_string, s5, "@眼 前 的 一 切 都 像 雾 气 般 烟 消 云 散 了 ， 你 和 范 伦 汀 娜 发 现 自 己 回 到 了 阳 光 之 下 ， 恍 如 隔 世 。 回 头 望 向 加 尔 村 ， 一 切 都 显 得 那 么 平 常 ， 但 你 们 已 不 敢 再 久 留 。 "),
         (str_store_string, s2, "@你 和 范 伦 汀 娜 在 加 尔 村 附 近 遭 遇 了 历 史 迷 雾 ， 回 到 了 两 百 年 前 的 某 日 。 向 护 枪 官 弗 朗 索 瓦 ·博 蒙 报 告 此 事 。 "),
         (add_quest_note_from_sreg, "qst_third_death", 4, s2, 0),
         (display_message, "str_quest_log_updated"),
      (else_try),
         (eq, "$third_death_quest_phase", 15),
         (eq, "$current_town", "p_village_1_12"),#加尔村
         (check_quest_active, "qst_third_death"),#支线剧情：第三个死
         (str_store_string, s5, "@一 切 都 消 失 了 ， 你 们 再 一 次 被 谬 史 扔 回 了 现 世 。 未 尽 的 话 语 停 留 在 嘴 边 ， 手 上 的 利 刃 还 留 有 砍 人 时 的 触 感 ， 然 而 一 切 都 已 被 两 个 世 纪 的 时 光 分 隔 。 "),
      (else_try),
         (eq, "$third_death_quest_phase", 20),
         (eq, "$current_town", "p_village_1_12"),#加尔村
         (check_quest_active, "qst_third_death"),#支线剧情：第三个死
         (str_store_string, s5, "@这 一 次 ， 你 切 实 地 将 肖 像 枪 握 在 了 手 中 ， 然 而 就 在 下 一 刻 ， 雾 气 彻 底 消 散 了 ， 阳 光 洒 在 你 们 身 上 ， 周 围 已 经 感 受 不 到 一 丝 一 毫 的 谬 史 的 气 息 。 冰 凉 的 触 感 依 然 在 你 手 心 中 暂 留 ， 但 枪 已 经 不 在 了 … … 好 似 南 柯 一 梦 。 ^^一 个 村 民 向 你 跑 来 ， 说 加 尔 村 请 来 的 专 家 已 经 打 开 了 墓 室 ， 邀 你 们 一 同 去 启 封 。 "),
         (str_store_string, s2, "@你 在 谬 史 中 取 得 了 肖 像 枪 ， 但 最 终 没 能 将 其 带 出 来 ， 这 事 就 算 这 么 告 一 段 落 了 。 现 在 不 妨 顺 便 去 完 成 最 初 的 工 作 ： 取 回 加 尔 村 墓 葬 里 的 文 物 。 "),
         (add_quest_note_from_sreg, "qst_third_death", 8, s2, 0),
         (display_message, "str_quest_log_updated"),
         (assign, "$third_death_quest_phase", 21),
      (try_end),
    ],
    [
      ("leave",[
      ],"离 开 。 ",[
      (change_screen_map),
      ]),
    ]
  ),


#玩家死亡
  ("death_end",menu_text_color(0xFFFFFF)|mnf_disable_all_keys,
    "{s5}",
    "none",
    [(set_background_mesh, "mesh_undead_production_window"),
      (try_begin),
         (str_store_string, s5, "@第 二 次 死 亡 不 约 而 至 ， 你 慢 慢 地 阖 上 了 眼 。 或 许 人 们 永 远 也 不 会 知 道 ， 一 个 异 乡 异 客 悄 无 声 息 地 死 在 这 片 看 不 到 星 空 的 土 地 上 ； 或 许 在 此 之 后 ， 还 会 有 更 多 的 冒 险 、 更 多 的 战 斗 、 更 多 的 死 亡 ； 从 今 往 后 ， 或 许 还 会 有 更 多 穿 越 者 ， 他 们 会 将 这 个 世 界 带 向 何 方 ？ 然 而 ， 这 一 切 的 一 切 ， 皆 与 你 毫 无 瓜 葛 了 。 "),
      (try_end),
      ],
    [
      ("end",[],
      "死 亡 是 … … 一 切 的 … … 终 结 … …",[
         (change_screen_quit),]),
    ]
  ),



  ("start_quest_battle_1", 0, #开局剧情：从码头出来后进入战斗
    "{s5}",
    "none",
    [
    ],
    [
      ("continue",[
      ],"继 续 。 ",[
      ]),
    ]
  ),

 ]