# -*- coding: UTF-8 -*-

from header_common import *
from header_items import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *
from module_constants import *


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.  
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

dialogs_mission = [
#######################################################主线剧情#####################################################
####
###—————————————————————————————第一章：疑城——————————————————————————————
##
#勒塞夫广场烧人
  [trp_npc19, "start", [
    (check_quest_active, "qst_game_start_quest"),#开局剧情：勒塞夫广场
    (eq, "$mayvis_quest_phase", 1),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_lesaff_square"),
  ], "远 方 而 来 之 人 ， 请 留 步 。 ", "mayvis_conversarion_1_begin", []],
  [trp_npc19|plyr, "mayvis_conversarion_1_begin", [], "您 在 和 我 说 话 ？ 有 什 么 事 吗 ？ ", "mayvis_conversarion_1_1", []],
  [trp_npc19, "mayvis_conversarion_1_1", [], "我 叫 梅 薇 丝 ， 只 是 一 介 漂 泊 者 。 我 有 一 些 薄 礼 ， 权 且 相 赠 ， 只 不 过 ， 此 处 人 多 眼 杂 ， 请 您 与 我 移 步 一 叙 。 ", "mayvis_conversarion_1_2", [
    (agent_set_animation, "$film_character_1", "anim_lesaff_square_pos_1_b", 0),#起身
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_1_2", [], "… … … …", "close_window", [
    (assign, "$mayvis_quest_phase", 2),
  ]],

  [trp_npc19, "start", [
    (eq, "$mayvis_quest_phase", 2),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_lesaff_square"),
  ], "您 果 然 跟 上 来 了 ， 呵 呵 。 ", "mayvis_conversarion_2_begin", [
    (agent_clear_scripted_mode, "$film_character_1"),]],
  [trp_npc19|plyr, "mayvis_conversarion_2_begin", [], "所 以 … … … … ", "mayvis_conversarion_2_1", []],
  [trp_npc19, "mayvis_conversarion_2_1", [], "毋 需 紧 张 ， 我 绝 非 您 的 敌 人 。 但 暗 潮 汹 涌 ， 多 股 势 力 正 图 谋 碾 碎 您 的 存 在 。 其 势 磅 礴 ， 超 乎 想 象 ， 足 以 轻 易 将 现 在 的 您 吞 噬 。 ", "mayvis_conversarion_2_2", []],
  [trp_npc19, "mayvis_conversarion_2_2", [], "您 觉 得 ， 想 要 在 此 世 存 活 下 去 ， 最 需 要 的 事 物 是 什 么 ？ ", "mayvis_conversarion_2_3", []],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "万 夫 莫 当 的 力 量 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_power_strike, 1),
    (troop_raise_skill, "trp_player", skl_power_throw, 1),
    (display_message, "@强 击 和 强 掷 提 升 了 ! ", 0x32CD32),
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "坚 不 可 摧 的 防 护 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_ironflesh, 1),
    (troop_raise_skill, "trp_player", skl_shield, 1),
    (display_message, "@铁 骨 和 盾 防 提 升 了 ！ ", 0x32CD32),
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "来 去 如 风 的 速 度 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_athletics, 1),
    (troop_raise_skill, "trp_player", skl_riding, 1),
    (display_message, "@身 法 和 骑 乘 提 升 了 ！ ", 0x32CD32),
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "用 之 不 竭 的 金 钱 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_trade, 1),
    (display_message, "@交 易 提 升 了 ！ ", 0x32CD32),
    (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_booty", 0, 0, 0),#战利品
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "足 以 自 保 的 武 艺 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_weapon_master, 1),
    (troop_raise_skill, "trp_player", skl_horse_archery, 1),
    (display_message, "@娴 熟 和 稳 定 提 升 了 ！ ", 0x32CD32),
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "洞 若 观 火 的 智 慧 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_study, 1),
    (troop_raise_skill, "trp_player", skl_memory, 1),
    (display_message, "@洞 见 和 强 识 提 升 了 ！ ", 0x32CD32),
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "忠 心 耿 耿 的 部 队 。 ", "mayvis_conversarion_2_4", [
    (troop_raise_skill, "trp_player", skl_leadership, 1),
    (troop_raise_skill, "trp_player", skl_trainer, 1),
    (display_message, "@统 御 和 教 练 提 升 了 ！ ", 0x32CD32),
  ]],
  [trp_npc19|plyr, "mayvis_conversarion_2_3", [], "相 互 扶 持 的 伙 伴 。 ", "mayvis_conversarion_2_5", []],
  [trp_npc19, "mayvis_conversarion_2_5", [], "原 来 如 此 ， 您 是 这 么 想 的 啊 … … … … ", "mayvis_conversarion_2_4", []],
  [trp_npc19, "mayvis_conversarion_2_4", [], "那 么 ， 就 此 别 过 了 。 请 尽 量 存 活 去 下 吧 ， 我 们 还 会 有 再 见 面 的 一 天 的 。 ", "close_window", [
    (assign, "$mayvis_quest_phase", 3),
  ]],

  [trp_libra_hitman, "start", [
    (eq, "$current_startup_quest_phase", 7),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_lesaff_square"),
    (assign, "$current_startup_quest_phase", 8),
  ], "站 住 ！ ", "libra_hitman_conversarion_begin", []],
  [trp_libra_hitman|plyr, "libra_hitman_conversarion_begin", [], "你 又 是 谁 ？ ", "libra_hitman_conversarion_1", []],
  [trp_libra_hitman, "libra_hitman_conversarion_1", [], "开 门 见 山 地 说 吧 ， 我 是 权 厄 之 秤 的 人 ， 而 我 知 道 你 是 界 外 人 — — 用 你 们 的 话 说 ， 叫 穿 越 者 ？ ", "libra_hitman_conversarion_2", []],
  [trp_libra_hitman|plyr, "libra_hitman_conversarion_2", [], "权 厄 之 秤 ， 是 个 犯 罪 团 伙 吧 。 过 街 老 鼠 这 么 光 明 正 大 地 出 现 ， 胆 子 挺 肥 。 ", "libra_hitman_conversarion_3", []],
  [trp_libra_hitman, "libra_hitman_conversarion_3", [], "哈 哈 ， 别 装 傻 ， 你 也 看 到 台 上 那 货 的 惨 状 了 ， 你 还 敢 要 挟 我 ？ ", "libra_hitman_conversarion_4", []],
  [trp_libra_hitman, "libra_hitman_conversarion_4", [], "放 轻 松 点 ， 我 只 是 来 送 个 口 信 的 。 我 们 分 舵 主 想 要 和 你 谈 谈 ， 似 乎 是 想 要 拉 你 入 伙 — — 你 就 知 足 吧 ， 那 位 大 人 可 是 在 黑 社 会 说 一 不 二 的 大 佬 ， 能 在 她 面 前 好 好 表 现 ， 这 辈 子 荣 华 富 贵 不 在 话 下 ， 一 般 人 可 没 这 个 机 会 。 ", "libra_hitman_conversarion_5", []],
  [trp_libra_hitman, "libra_hitman_conversarion_5", [], "荣 华 富 贵 还 是 烧 成 焦 炭 ， 你 自 己 选 。 ", "libra_hitman_conversarion_6", []],
  [trp_libra_hitman|plyr, "libra_hitman_conversarion_6", [], "… … 看 来 我 是 没 有 选 择 了 。 ", "libra_hitman_conversarion_7", []],
  [trp_libra_hitman, "libra_hitman_conversarion_7", [], "很 识 时 务 ， 不 错 。 那 么 ， 分 舵 主 大 人 会 在 勒 塞 夫 贫 民 窟 的 据 点 里 等 你 。 你 不 会 想 让 那 位 大 人 失 望 的 。 ", "close_window", [
    (str_store_party_name_link, s1, "p_town_4"),
    (str_store_string, s2, "@不 久 前 曾 打 过 交 道 的 “ 权 厄 之 秤 ” 犯 罪 集 团 ， 不 知 为 何 知 晓 了 你 的 界 外 人 身 份 ， 并 以 此 为 要 挟 ， 要 求 你 前 往 他 们 位 于 {s1}贫 民 窟 的 据 点 一 叙 。 在 {s1}中 指 定 区 域 使 用 “ 探 索 ” 寻 找 其 据 点 。 "),
    (add_quest_note_from_sreg, "qst_game_start_quest", 3, s2, 1),
    (call_script, "script_set_quest_zone", "qst_game_start_quest", "p_town_4", 13, 5, 1),#设置任务地点
    (display_message, "str_quest_log_updated"),
    (dialog_box, "@重 要 ！ ！ ^本 mod 一 部 分 涉 及 战 斗 的 副 本 中 ， 一 旦 死 亡 将 强 制 结 束 游 戏 ， 因 此 开 始 前 请 务 必 存 档 。 "),
  ]],

#开局剧情：勒塞夫权厄之秤据点
  [trp_anne_laure_deschamps, "start", [
    (check_quest_active, "qst_game_start_quest"),#开局剧情：权厄之秤据点
    (eq, "$current_startup_quest_phase", 10),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_underworld_stronghold_1"),
  ], "来 了 ？ 界 外 人 {playername}， 你 很 识 时 务 。 我 喜 欢 识 时 务 的 人 。 ", "anne_laure_deschamps_1_begin", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_begin", [], "自 我 介 绍 一 下 吧 ， 我 是 权 厄 之 秤 的 分 舵 主 ， 安 妮 -洛 尔 ·德 尚 ， 统 管 整 个 勒 塞 夫 南 岸 的 业 务 ， 在 明 面 上 也 有 男 爵 的 身 份 。 ", "anne_laure_deschamps_1_1", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_1", [], "你 找 我 干 什 么 ？ 有 话 快 说 。 ", "anne_laure_deschamps_1_2", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_2", [], "如 果 我 是 你 ， 现 在 就 不 会 用 这 种 口 气 说 话 了 。 你 可 是 有 把 柄 在 我 们 手 上 的 ， 界 外 人 ， 呵 呵 ， 这 个 身 份 够 你 死 十 次 ， 尸 体 都 要 被 挫 骨 扬 灰 。 ", "anne_laure_deschamps_1_3", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_3", [], "但 是 ， 我 可 以 帮 你 保 守 秘 密 ， 只 要 你 能 为 我 所 用 — — 我 要 你 去 接 近 克 莉 斯 特 ·罗 德 里 格 斯 ， 并 取 得 她 的 信 任 。 ", "anne_laure_deschamps_1_4", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_4", [], "那 是 谁 ？ ", "anne_laure_deschamps_1_5", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_5", [], "你 见 过 她 的 ， 在 那 个 广 场 上 ， 骑 着 马 的 紫 头 发 女 人 。 克 莉 斯 特 · 罗 德 里 格 斯 ， 元 素 骑 士 团 的 骑 士 长 ， 勋 爵 爵 位 ， 山 铜 级 … … 这 个 人 很 关 键 ， 因 为 她 是 罗 德 里 格 斯 公 爵 的 独 女 ， 日 后 的 勒 塞 夫 领 主 。 ", "anne_laure_deschamps_1_6", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_6", [], "公 爵 老 儿 年 龄 不 小 了 ， 正 在 慢 慢 地 放 权 给 她 。 然 而 ， 这 个 小 娘 们 初 生 牛 犊 不 怕 虎 ， 不 顾 几 十 年 来 的 政 治 默 契 ， 对 与 我 们 合 作 的 达 官 显 贵 大 加 清 算 ， 拔 掉 了 我 们 很 多 暗 桩 ， 甚 至 威 胁 到 了 我 们 的 … … 真 是 多 事 之 秋 呐 。 ^不 过 ， 走 运 的 是 ， 一 伙 魔 王 尖 兵 在 这 个 节 骨 眼 上 杀 了 出 来 ， 让 她 那 一 边 阵 脚 大 乱 。 浑 水 才 能 摸 鱼 ， 接 下 来 就 是 需 要 你 办 事 的 时 候 了 。 ", "anne_laure_deschamps_1_7", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_7", [], "这 女 人 有 一 个 旧 识 ， 是 她 在 国 立 龙 学 院 上 学 时 的 同 学 ， 叫 范 伦 汀 娜 ， 加 西 亚 侯 爵 的 女 儿 。 此 人 机 缘 巧 合 中 落 到 就 我 们 手 上 ， 被 秘 密 关 押 在 我 们 的 一 个 港 口 里 — — 就 是 你 上 岸 的 那 个 地 方 。 杀 进 去 ， 救 出 她 ， 你 就 能 接 近 罗 德 里 格 斯 勋 爵 ， 得 到 她 的 初 步 信 任 。 ", "anne_laure_deschamps_1_8", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_8", [], "那 不 是 你 们 自 己 的 据 点 吗 ？ 让 我 去 杀 人 ？ ", "anne_laure_deschamps_1_9", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_9", [], "正 因 为 是 我 的 牌 ， 所 以 才 能 在 需 要 的 时 候 打 出 去 。 假 戏 要 真 做 ， 才 能 唬 住 人 。 我 会 用 一 些 合 理 的 理 由 ， 把 我 的 亲 信 和 你 打 不 赢 的 强 者 撤 出 去 ， 剩 下 的 那 些 ， 都 是 货 真 价 实 、 一 无 所 知 的 权 厄 之 秤 人 员 ， 经 得 起 任 何 核 查 。 ", "anne_laure_deschamps_1_10", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_10", [], "况 且 ， 我 知 道 你 很 讨 厌 我 们 ， 现 在 给 你 一 个 惩 恶 扬 善 的 机 会 ， 何 乐 而 不 为 呢 ？ 而 且 ， 我 会 把 之 前 给 你 传 话 的 人 也 安 排 在 港 口 里 ， 只 要 你 把 他 杀 了 ， 世 界 上 知 道 你 界 外 人 身 份 的 就 只 剩 你 我 ， 算 是 我 的 一 点 诚 意 … … 我 这 个 人 最 喜 欢 双 赢 的 买 卖 。 ", "anne_laure_deschamps_1_11", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_11", [], "真 是 心 狠 手 辣 啊 。 ", "anne_laure_deschamps_1_12", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_12", [], "手 不 够 狠 ， 又 怎 么 能 坐 稳 这 个 位 置 呢 ？ 好 了 ， 我 知 道 你 还 有 想 问 的 事 ， 问 吧 。 ", "anne_laure_deschamps_1_pretalk", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_end", [], "还 有 什 么 想 问 的 ？ ", "anne_laure_deschamps_1_pretalk", []],

  [trp_anne_laure_deschamps, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_underworld_stronghold_1"),
  ], "{playername}， 有 什 么 事 ？ ", "anne_laure_deschamps_1_pretalk", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_pretalk", [], "“ 权 厄 之 秤 ” 是 个 什 么 东 西 ？ 是 你 们 黑 帮 的 名 字 吗 ？ ", "anne_laure_deschamps_1_13", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_13", [], "你 说 笑 了 ， 尽 管 我 们 黑 烛 帮 控 制 着 勒 塞 夫 南 部 所 有 的 地 下 生 意 ， 也 仅 仅 只 是 权 厄 之 秤 的 一 个 小 小 分 舵 ， 或 者 说 ， 只 是 下 游 组 织 而 已 。 ", "anne_laure_deschamps_1_14", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_14", [], "权 厄 之 秤 是 遍 及 全 世 界 的 犯 罪 帝 国 ， 即 使 是 我 们 这 些 干 部 ， 也 不 知 道 其 真 正 规 模 有 多 恐 怖 。 徘 徊 在 社 会 的 边 缘 、 法 律 灰 黑 色 地 带 的 人 ， 没 有 不 想 加 入 权 厄 之 秤 的 。 然 而 ， 只 有 足 够 强 大 的 帮 派 才 能 入 其 法 眼 ， 被 它 收 编 。 我 们 黑 烛 帮 ， 也 是 经 过 了 十 几 年 的 血 腥 搏 杀 ， 才 得 到 了 “ 秤 ” 的 垂 青 。 ", "anne_laure_deschamps_1_15", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_15", [], "据 说 ， 权 厄 之 秤 的 幕 后 主 使 者 是 一 位 真 正 的 神 明 呢 。 ", "anne_laure_deschamps_1_16", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_16", [], "神 ？ 黑 社 会 的 神 吗 ？ 真 是 让 人 笑 不 出 来 的 笑 话 。 ", "anne_laure_deschamps_1_end", []],

  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_pretalk", [], "你 能 不 能 说 说 你 的 来 历 ？ ", "anne_laure_deschamps_1_17", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_17", [], "你 还 是 我 成 为 权 厄 之 秤 的 分 舵 主 后 ， 第 一 个 够 胆 当 面 问 我 过 去 的 人 。 过 去 曾 有 十 七 个 人 这 么 问 我 ， 其 中 八 个 被 我 当 场 格 杀 ， 五 个 被 我 废 掉 了 舌 头 耳 朵 和 眼 睛 ， 还 有 四 个 日 后 被 我 用 各 种 方 式 刺 杀 。 不 过 ， 谅 在 你 是 个 真 的 什 么 都 不 知 道 的 界 外 人 ， 我 原 谅 你 了 。 ", "anne_laure_deschamps_1_18", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_18", [], "你 只 需 要 知 道 我 出 身 低 微 到 你 难 以 想 象 ， 全 靠 自 己 的 努 力 、 智 慧 和 勇 气 取 得 了 今 天 的 地 位 。 我 的 贵 族 身 份 是 在 斯 塔 胡 克 人 那 里 买 的 ， 因 为 展 现 出 了 自 己 的 利 用 价 值 ， 被 权 厄 之 秤 收 编 ， 在 他 们 的 运 作 下 ， 爵 位 得 到 了 联 合 王 国 的 承 认 ， 最 后 一 步 一 步 从 骑 士 爬 到 了 男 爵 。 贵 族 圈 子 对 我 非 议 不 少 ， 但 你 只 需 管 我 叫 博 尚 夫 人 就 行 了 。 ", "anne_laure_deschamps_1_end", []],

  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_pretalk", [], "所 以 为 什 么 找 上 我 ？ ", "anne_laure_deschamps_1_19", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_19", [], "这 个 嘛 ， 你 是 界 外 人 。 ", "anne_laure_deschamps_1_20", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_20", [], "界 外 人 ， 然 后 呢 ？ 我 是 界 外 人 ， 对 你 想 做 的 事 有 任 何 帮 助 吗 ？ ", "anne_laure_deschamps_1_21", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_21", [], "呵 呵 ， 无 可 奉 告 。 ", "anne_laure_deschamps_1_end", []],

  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_pretalk", [], "你 们 为 什 么 要 搜 捕 界 外 人 ？ 我 想 知 道 具 体 原 因 。 ", "anne_laure_deschamps_1_22", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_22", [], "明 知 故 问 ？ 界 外 是 多 么 污 秽 、 诡 异 、 恐 怖 、 邪 恶 的 地 方 ， 你 肯 定 比 我 更 清 楚 。 ", "anne_laure_deschamps_1_23", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_23", [], "不 ， 我 真 不 清 楚 … … ", "anne_laure_deschamps_1_24", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_24", [], "来 自 界 外 的 人 事 物 ， 甚 至 描 述 界 外 的 信 息 本 身 ， 都 对 这 个 世 界 造 成 了 严 重 的 侵 蚀 。 污 染 土 地 ， 扭 曲 人 心 ， 制 造 怪 物 。 听 你 这 么 说 ， 难 道 这 不 是 你 们 有 意 为 之 的 吗 ？ ", "anne_laure_deschamps_1_25", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_25", [], "那 我 不 就 站 在 这 里 跟 你 对 话 吗 ？ 怎 么 不 见 天 地 变 色 ， 日 月 无 光 。 ", "anne_laure_deschamps_1_26", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_26", [], "你 不 是 占 了 别 人 的 身 体 吗 ？ 或 许 是 这 样 骗 过 了 世 界 吧 。 你 们 管 这 种 技 术 叫 什 么 ？ 是 不 是 叫 “ 魂 穿 ” 来 着 ？ ", "anne_laure_deschamps_1_27", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_27", [], "不 ， 我 想 在 我 的 认 知 里 并 没 有 这 种 技 术 … … 你 说 的 界 外 和 我 想 的 是 一 个 地 方 吗 ？ 我 们 — — ", "anne_laure_deschamps_1_28", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_28", [], "打 住 ！ 不 要 告 诉 我 细 节 ， 我 还 不 想 变 成 非 人 。 ", "anne_laure_deschamps_1_29", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_29", [], "封 建 迷 信 … … ", "anne_laure_deschamps_1_end", []],

  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_pretalk", [], "跟 我 讲 点 常 识 吧 ， 比 如 政 局 ？ ", "anne_laure_deschamps_1_30", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_30", [], "你 这 是 把 我 当 向 导 了 ？ 也 罢 ， 就 跟 你 讲 讲 ， 省 得 你 临 到 关 键 时 露 馅 。 ", "anne_laure_deschamps_1_31", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_31", [], "现 在 是 神 历 1413年 ， 亦 即 黑 铁 纪 第 五 个 世 纪 。 在 此 之 前 人 类 文 明 还 有 三 个 纪 元 ， 据 说 有 上 万 年 的 历 史 。 ", "anne_laure_deschamps_1_32", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_32", [], "黑 铁 纪 之 前 ， 是 将 近 一 千 年 的 赤 铜 纪 ， 那 是 一 个 创 世 女 神 教 统 治 全 世 界 ， 上 千 个 世 俗 王 室 臣 服 于 教 皇 国 淫 威 之 下 的 时 代 ， 不 过 在 教 皇 国 被 魔 王 军 重 创 后 — — 对 了 ， 魔 族 也 是 外 神 的 眷 族 — — 世 俗 诸 国 开 始 了 互 相 攻 伐 、 兼 并 、 吞 噬 的 残 酷 战 争 。 ", "anne_laure_deschamps_1_33", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_33", [], "现 在 ， 人 界 上 只 剩 七 个 — — 或 者 说 ， 为 我 们 所 熟 知 的 只 有 七 个 国 家 。 首 先 是 我 们 普 威 尔 联 合 王 国 ， 最 为 世 俗 主 义 ， 与 龙 种 “ 关 系 密 切 ” ； 沿 海 往 北 ， 是 一 个 叫 斯 塔 胡 克 大 公 国 的 国 家 ， 不 算 大 国 ， 但 是 战 斗 力 凶 悍 ， 和 海 寇 暗 通 款 曲 ； 再 往 北 ， 是 沼 泽 人 、 鱼 人 、 归 化 蛮 族 和 创 世 女 神 教 的 一 个 新 教 分 支 组 成 的 乌 -迪 默 -安 基 亚 邦 联 ； 极 北 之 地 ， 则 是 精 灵 统 治 的 伊 希 斯 公 国 。 ", "anne_laure_deschamps_1_34", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_34", [], "联 合 王 国 的 东 北 边 ， 是 旧 日 霸 主 教 皇 国 ， 实 力 依 然 不 容 小 觑 ， 是 联 合 王 国 的 宿 敌 ； 东 南 边 ， 则 是 兽 人 酋 长 们 的 联 盟 ， 科 鲁 托 酋 长 国 ； 正 东 边 ， 是 一 个 自 称 自 由 城 邦 的 小 国 联 盟 ， 在 联 合 王 国 、 教 皇 国 、 酋 长 国 三 国 制 衡 之 下 生 存 。 ", "anne_laure_deschamps_1_35", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_35", [], "更 东 边 ， 越 过 龙 树 山 脉 ， 是 东 方 人 的 领 土 。 哲 布 大 门 被 封 死 后 ， 谁 也 不 知 道 他 们 发 展 成 什 么 样 了 。 而 大 陆 以 西 的 尽 头 洋 上 ， 零 星 分 布 着 一 片 群 岛 ， 称 为 外 海 列 岛 。 有 传 言 说 他 们 接 受 了 从 深 渊 中 游 来 的 异 种 的 统 治 ， 深 海 巨 蟒 海 寇 船 团 也 是 归 属 于 它 们 的 舰 队 。 ", "anne_laure_deschamps_1_36", []],
  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_36", [], "说 说 联 合 王 国 内 部 的 情 况 ？ ", "anne_laure_deschamps_1_37", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_37", [], "联 合 王 国 现 在 的 国 王 叫 克 罗 龙 斯 七 世 ， 国 内 大 致 分 为 东 南 西 北 中 五 派 贵 族 、 或 者 说 附 属 国 ， 勒 塞 夫 的 领 主 ， 罗 德 里 格 斯 公 爵 就 是 西 方 这 一 派 — — 罗 德 里 格 斯 公 国 的 首 脑 。 各 个 派 系 之 间 纷 争 不 断 ， 甚 至 会 在 王 室 的 监 护 下 进 行 可 控 的 战 争 。 ^而 如 果 是 不 可 控 的 战 争 ， 那 就 是 内 战 了 ， 这 种 情 况 在 一 百 年 前 就 发 生 过 一 次 ， 一 口 气 打 了 三 四 十 年 。 ", "anne_laure_deschamps_1_38", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_38", [], "嘴 都 讲 干 了 ， 不 说 了 。 就 先 这 样 吧 。 ", "anne_laure_deschamps_1_end", []],

  [trp_anne_laure_deschamps|plyr, "anne_laure_deschamps_1_pretalk", [], "没 有 别 的 问 题 了 。 ", "anne_laure_deschamps_1_39", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_39", [
    (eq, "$current_startup_quest_phase", 10),
    (troop_add_gold, "trp_player", 1500),
  ], "15枚 银 币 ， 拿 着 ， 全 是 给 你 的 经 费 。 普 通 冒 险 者 干 一 年 都 赚 不 了 这 么 多 钱 ， 为 权 厄 之 秤 卖 命 ， 钱 总 是 管 够 的 。 ", "anne_laure_deschamps_1_40", []],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_40", [], "为 了 不 露 破 绽 ， 我 建 议 你 去 注 册 一 个 冒 险 者 身 份 ， 然 后 把 营 救 加 西 亚 的 委 托 接 了 — — 现 在 ， 为 你 的 小 命 着 想 ， 去 执 行 你 的 任 务 吧 。 ", "close_window", [
    (assign, "$current_startup_quest_phase", 11),
    (display_message, "@按 TAB 键 离 开 。 "),
    (mission_disable_talk),
  ]],
  [trp_anne_laure_deschamps, "anne_laure_deschamps_1_39", [
    (ge, "$current_startup_quest_phase", 11),
  ], "好 的 ， 好 的 。 再 见 。 ", "close_window", []],


#开局剧情：冒险者协会
#斯特林分会长
  [trp_sterling_branch_president, "start", [
    (eq, "$current_building", "itm_adventurer_station"),#在协会建筑里
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_adventurer_station_1"),
  ], "我 是 冒 险 者 协 会 在 勒 塞 夫 分 会 的 负 责 人 ， 斯 特 林 。 ", "sterlin_station_talk_1", []],
  [trp_sterling_branch_president, "sterlin_station_talk_1", [], "过 去 我 也 当 过 冒 险 者 ， 不 过 目 前 我 已 经 退 居 二 线 了 ， 有 什 么 问 题 问 那 边 的 职 员 劳 瑞 吧 。 ", "sterlin_station_talk_2", []],
  [trp_sterling_branch_president|plyr, "sterlin_station_talk_2", [], "能 跟 我 讲 讲 您 的 经 历 和 经 验 吗 ？ ", "sterlin_station_talk_3", []],
  [trp_sterling_branch_president|plyr, "sterlin_station_talk_2", [], "好 的 ， 再 见 。 ", "close_window", []],
  [trp_sterling_branch_president, "sterlin_station_talk_3", [], "协 会 组 织 编 撰 过 很 多 刊 物 和 手 册 ， 我 能 分 享 的 冒 险 经 验 都 在 上 面 了 。 不 过 经 历 我 倒 是 能 讲 一 讲 。 ", "sterlin_station_talk_4", []],
  [trp_sterling_branch_president, "sterlin_station_talk_4", [], "过 去 我 最 爱 用 细 剑 ， 靠 一 手 击 剑 术 达 到 了 秘 银 级 ， 混 得 了 一 个 “ 银 蛰 ” 的 诨 号 。 不 过 ， 在 一 次 任 务 中 我 的 惯 用 手 受 了 重 伤 ， 从 此 我 转 为 了 文 职 ， 靠 着 资 历 老 当 了 个 分 会 长 ， 哈 哈 。 ", "close_window", []],

#劳瑞
  [trp_npc10, "start", [
    (check_quest_active, "qst_game_start_quest"),#开局剧情：冒险者协会
    (eq, "$current_startup_quest_phase", 11),
    (eq, "$current_building", "itm_adventurer_station"),#在协会建筑里
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_adventurer_station_1"),
  ], "您 好 ， 协 会 职 员 劳 瑞 为 您 服 务 ， 请 问 您 有 什 么 需 要 办 理 的 吗 ？ ", "mission_npc10_talk_1", []],
  [trp_npc10|plyr, "mission_npc10_talk_1", [], "我 要 注 册 冒 险 者 身 份 。 ", "mission_npc10_talk_2", []],
  [trp_npc10, "mission_npc10_talk_2", [], "了 解 ， 我 需 要 问 您 一 些 简 单 的 问 题 ， 请 问 您 是 哪 里 人 ？ ", "mission_npc10_talk_3", []],
  [trp_npc10|plyr, "mission_npc10_talk_3", [], "嗯 … … 我 的 家 乡 被 魔 灾 毁 灭 了 ， 不 得 已 来 勒 塞 夫 讨 生 活 。 ", "mission_npc10_talk_4", []],
  [trp_npc10, "mission_npc10_talk_4", [], "请 节 哀 ， 我 登 记 一 下 … … 第 二 个 问 题 是 ， 请 问 您 有 任 何 违 法 犯 罪 记 录 吗 ？ ", "mission_npc10_talk_5", []],
  [trp_npc10|plyr, "mission_npc10_talk_5", [], "没 有 。 ", "mission_npc10_talk_6", []],
  [trp_npc10, "mission_npc10_talk_6", [], "斩 钉 截 铁 ， 很 好 。 最 后 一 个 问 题 ， 请 问 您 实 力 如 何 ？ 是 否 曾 战 斗 过 ？ ", "mission_npc10_talk_7", []],
  [trp_npc10|plyr, "mission_npc10_talk_7", [], "可 以 说 没 有 。 ", "mission_npc10_talk_8", []],
  [trp_npc10, "mission_npc10_talk_8", [], "了 解 ， 那 我 暂 且 给 您 定 一 个 黑 铁 级 吧 。 冒 险 等 阶 的 提 升 办 法 ， 我 之 后 会 另 行 说 明 。 ", "mission_npc10_pretalk", [
    (assign, "$current_startup_quest_phase", 12),
    (assign, "$player_adventuror_level", 0),#冒险等阶
    (display_message, "@已 为 黑 铁 级 冒 险 者 ！ "),
    (call_script, "script_remove_faction_affiliation", "trp_matton_adams", 1),##移除马顿·亚当斯的隶属，不再刷新在协会里
#更新委托板
    (call_script, "script_set_center_quest_target", "p_town_4", 1, "trp_npc4", 1, 1),#带回范伦汀娜
    (call_script, "script_set_center_quest_recycle", "p_town_4", 1, 0),#不用回收
    (call_script, "script_set_center_quest_reward", "p_town_4", 1, 20000),#两万赏金
    (call_script, "script_clear_quest_zone", "qst_game_start_quest", 1),#清除任务地点
    (assign, "$current_startup_quest_phase", 12),
  ]],

  [trp_npc10, "start", [#日常对话起始
    (check_quest_active, "qst_game_start_quest"),#开局剧情：冒险者协会
    (ge, "$current_startup_quest_phase", 12),
    (eq, "$current_building", "itm_adventurer_station"),#在协会建筑里
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_adventurer_station_1"),
  ], "您 好 ， 请 问 有 什 么 需 要 咨 询 的 吗 ？ ", "mission_npc10_pretalk_1", []],
  [trp_npc10, "mission_npc10_pretalk", [], "您 还 有 什 么 需 要 咨 询 的 吗 ？ ", "mission_npc10_pretalk_1", []],
  [trp_npc10|plyr, "mission_npc10_pretalk_1", [], "能 否 介 绍 一 下 等 阶 ？ ", "mission_npc10_pretalk_2", []],
  [trp_npc10, "mission_npc10_pretalk_2", [], "没 问 题 。 我 们 目 前 实 行 的 实 力 评 估 体 系 ， 分 为 七 个 档 次 ， 黑 铁 级 、 赤 铜 级 、 白 银 级 、 黄 金 级 、 秘 银 级 、 山 铜 级 、 奥 钢 级 。 ", "mission_npc10_pretalk_3", []],
  [trp_npc10, "mission_npc10_pretalk_3", [], "黑 铁 级 是 最 弱 的 、 几 乎 没 经 历 过 战 斗 的 普 通 人 ， 以 及 哥 布 林 等 最 弱 小 的 魔 物 。 ^赤 铜 级 是 经 受 过 一 定 训 练 的 民 兵 、 土 匪 等 。 ^白 银 级 是 精 锐 民 兵 、 二 线 部 队 。 ^黄 金 级 包 括 强 国 的 主 力 军 、 小 有 名 气 的 佣 兵 和 冒 险 者 ， 如 果 是 魔 物 或 土 匪 足 以 为 祸 一 乡 。 ", "mission_npc10_pretalk_4", []],
  [trp_npc10, "mission_npc10_pretalk_4", [], "秘 银 级 则 是 正 规 骑 士 、 高 级 军 士 和 著 名 冒 险 者 的 级 别 。 比 如 我 们 分 会 长 就 曾 是 秘 银 级 冒 险 者 。 ", "mission_npc10_pretalk_5", []],
  [trp_npc10, "mission_npc10_pretalk_5", [], "山 铜 级 是 正 常 人 类 在 没 有 奇 遇 、 传 承 或 神 器 的 情 况 下 ， 通 过 不 懈 的 训 练 和 精 良 的 武 装 所 能 达 到 的 最 高 水 准 ， 比 如 各 个 骑 士 团 的 上 级 骑 士 。 如 果 落 草 为 寇 ， 能 当 山 贼 王 ， 为 祸 一 方 。 ", "mission_npc10_pretalk_6", []],
  [trp_npc10, "mission_npc10_pretalk_6", [], "最 后 是 奥 钢 级 。 古 时 奥 钢 级 也 被 称 为 准 神 、 半 神 、 下 位 神 。 移 山 填 海 ， 伟 力 万 能 。 在 战 役 部 署 中 ， 一 尊 奥 钢 级 等 同 于 至 少 一 千 人 的 主 力 部 队 。 ", "mission_npc10_pretalk", []],

  [trp_npc10|plyr, "mission_npc10_pretalk_1", [], "我 要 如 何 提 升 自 己 的 冒 险 者 等 阶 ？ ", "mission_npc10_pretalk_7", []],
  [trp_npc10, "mission_npc10_pretalk_7", [], "您 可 以 常 来 协 会 看 看 ， 有 时 能 够 见 到 考 官 。 这 些 都 是 从 优 秀 老 资 格 冒 险 者 中 返 聘 的 专 业 人 员 。 与 他 们 对 话 ， 通 过 考 核 ， 就 能 升 阶 了 。 ", "mission_npc10_pretalk_8", []],
  [trp_npc10, "mission_npc10_pretalk_8", [], "不 过 咱 们 的 考 官 最 多 只 能 负 责 黄 金 级 升 秘 银 级 的 考 核 ， 位 于 各 个 国 家 首 都 的 地 区 总 部 ， 才 能 执 行 秘 银 级 升 山 铜 级 的 考 核 ， 而 达 到 奥 钢 级 ， 原 则 上 需 要 去 位 于 大 公 国 的 协 会 总 部 。 不 过 如 果 您 都 已 经 是 奥 钢 级 的 英 雄 了 ， 应 该 是 协 会 来 求 您 。 ", "mission_npc10_pretalk", []],

  [trp_npc10|plyr, "mission_npc10_pretalk_1", [], "我 想 招 募 冒 险 者 的 话 该 怎 么 办 ？ ", "mission_npc10_pretalk_9", []],
  [trp_npc10, "mission_npc10_pretalk_9", [], "您 可 以 与 协 会 中 来 往 的 冒 险 者 沟 通 ， 邀 请 他 们 加 入 队 伍 。 不 过 如 果 您 的 冒 险 等 阶 不 如 他 们 高 ， 他 们 是 不 会 同 意 的 。 ", "mission_npc10_pretalk_10", []],
  [trp_npc10, "mission_npc10_pretalk_10", [], "冒 险 等 阶 达 到 一 定 程 度 后 ， 还 能 直 接 发 布 委 托 招 募 人 员 ， 建 立 冒 险 团 。 ", "mission_npc10_pretalk", []],

  [trp_npc10|plyr, "mission_npc10_pretalk_1", [], "如 何 接 取 委 托 ？ ", "mission_npc10_pretalk_11", []],
  [trp_npc10, "mission_npc10_pretalk_11", [], "事 实 上 ， 现 在 我 们 已 经 不 需 要 再 “ 接 取 ” 委 托 了 。 在 协 会 成 立 之 初 ， 接 取 委 托 者 会 得 到 一 份 卷 轴 ， 作 为 委 托 凭 证 ， 但 随 着 几 百 年 间 协 会 的 壮 大 、 冒 险 者 的 增 加 和 业 务 的 拓 展 ， 这 套 办 法 早 已 不 再 适 用 。 ", "mission_npc10_pretalk_12", []],
  [trp_npc10, "mission_npc10_pretalk_12", [], "现 在 ， 本 地 的 所 有 委 托 都 会 挂 在 委 托 板 上 ， 您 可 以 根 据 上 面 的 要 求 准 备 物 品 ， 满 足 条 件 即 可 直 接 交 付 ， 完 成 委 托 ， 获 得 酬 金 。 流 程 比 过 去 方 便 许 多 — — 尤 其 对 于 我 们 协 会 职 员 而 言 。 ", "mission_npc10_pretalk_13", []],
  [trp_npc10|plyr, "mission_npc10_pretalk_13", [], "如 果 准 备 了 东 西 ， 却 被 别 人 抢 先 完 成 了 怎 么 办 ？ ", "mission_npc10_pretalk_14", []],
  [trp_npc10, "mission_npc10_pretalk_14", [], "很 抱 歉 这 么 说 ， 但 这 也 是 冒 险 者 生 涯 不 可 忽 或 缺 的 一 环 。 我 们 的 委 托 一 般 两 周 更 新 一 次 ， 所 以 还 请 您 算 准 时 间 。 不 过 ， 一 些 特 殊 委 托 是 即 使 更 新 也 会 继 续 保 留 的 。 ", "mission_npc10_pretalk_15", []],
  [trp_npc10, "mission_npc10_pretalk_15", [], "除 此 之 外 ， 有 些 比 较 重 要 或 者 比 较 复 杂 的 委 托 ， 委 托 人 会 直 接 到 协 会 里 来 招 募 人 员 ， 您 可 以 多 多 留 意 。 ", "mission_npc10_pretalk", []],

  [trp_npc10|plyr, "mission_npc10_pretalk_1", [], "没 别 的 问 题 了 。 ", "close_window", []],


#马顿·亚当斯
  [trp_matton_adams, "start", [
    (eq, "$current_building", "itm_adventurer_station"),#在协会建筑里
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_adventurer_station_1"),
  ], "你 好 ， 组 队 吗 ？ 我 是 马 顿 ·亚 当 斯 ， 目 前 正 在 筹 办 冒 险 团 。 别 的 不 敢 自 夸 ， 至 少 在 狩 猎 魔 物 这 方 面 我 经 受 过 不 少 训 练 了 。 ", "mission_matton_adams_1", []],
  [trp_matton_adams, "mission_matton_adams_1", [], "受 魔 灾 影 响 ， 最 近 什 么 好 做 的 委 托 都 没 有 ， 你 自 己 一 个 人 也 很 难 赚 到 钱 吧 ， 不 如 我 们 一 起 来 ， 还 能 接 受 一 些 大 型 的 雇 佣 任 务 。 ", "mission_matton_adams_2", []],
  [trp_matton_adams|plyr, "mission_matton_adams_2", [], "呃 ， 不 了 ， 我 还 有 别 的 事 。 下 次 再 说 吧 。 ", "mission_matton_adams_3", []],
  [trp_matton_adams, "mission_matton_adams_3", [], "那 再 见 了 。 我 有 预 感 ， 我 们 以 后 还 会 再 见 面 的 。 ", "close_window", []],




#开局剧情：权厄之秤码头要塞，范伦汀娜入队
  [trp_npc4|plyr, "start", [
    (check_quest_active, "qst_game_start_quest"),#开局剧情：重回权厄之秤码头
    (eq, "$current_startup_quest_phase", 13),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_libra_smuggle_wharf_stronghold"),
  ], "你 就 是 范 伦 汀 娜 吗 ？ ", "mission_npc4_recruit_1", []],
  [trp_npc4, "mission_npc4_recruit_1", [], "是 的 ， 我 是 加 西 亚 侯 爵 的 女 儿 ， 范 伦 汀 娜 · 加 西 亚 ， 我 在 前 往 勒 塞 夫 的 途 中 遭 遇 魔 王 尖 兵 的 袭 击 ， 侥 幸 逃 脱 后 又 被 权 厄 之 秤 绑 架 ， 失 陷 于 此 。 请 问 您 是 … … ？ ", "mission_npc4_recruit_2", []],
  [trp_npc4|plyr, "mission_npc4_recruit_2", [], "我 是 路 过 的 冒 险 者 ， 接 到 委 托 过 来 救 你 的 。 跟 我 走 吧 ， 我 带 你 去 勒 塞 夫 。 ", "mission_npc4_recruit_3", []],
  [trp_npc4, "mission_npc4_recruit_3", [], "是 这 样 吗 ？ … … 好 的 多 谢 了 ， 麻 烦 您 了 。 ", "close_window", [
    (display_message, "@范 伦 汀 娜 微 妙 的 目 光 从 你 身 上 扫 过 ， 你 突 然 觉 得 自 己 似 乎 整 个 人 都 被 看 透 了 ， 如 芒 在 背 。 不 过 这 种 感 觉 转 瞬 即 逝 ， 消 失 无 踪 。"),
    (troop_set_slot, "trp_npc4", slot_troop_first_encountered, "p_libra_smuggle_wharf"),#初次见面的位置
    (troop_set_slot, "trp_npc4", slot_troop_payment_request, 0),
    (call_script, "script_recruit_troop_as_companion", "trp_npc4"),
    (finish_mission),
    (change_screen_return),

    (str_store_party_name_link, s1, "p_town_4"),
    (str_store_string, s2, "@任 务 完 成 ， 是 时 候 返 回 {s1}的 冒 险 者 协 会 领 取 赏 金 ， 并 在 城 堡 与 公 爵 之 女 克 莉 斯 特 会 面 了 。 "),
    (add_quest_note_from_sreg, "qst_game_start_quest", 5, s2, 1),
    (call_script, "script_set_quest_zone", "qst_game_start_quest", "p_town_4", 5, 4, 1),#设置任务地点
    (display_message, "str_quest_log_updated"),
  ]],





#######################################################支线剧情#####################################################
####
###——————————————————————————————冠军拍卖——————————————————————————————-
##
  [trp_sword_sister, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_champion_auction"),
    (neq, "$g_film_dialog", 9),
  ], "这 位 客 人 ， 您 好 ， 请 问 我 有 什 么 能 为 您 服 务 的 吗 ？ ", "champion_auction_begin", []],
  [trp_sword_sister|plyr, "champion_auction_begin", [], "这 是 个 什 么 地 方 ？ ", "champion_auction_1", []],
  [trp_sword_sister|plyr, "champion_auction_begin", [], "跟 我 讲 讲 规 则 。 ", "champion_auction_2", []],
  [trp_sword_sister|plyr, "champion_auction_begin", [], "我 能 带 走 买 下 的 奴 隶 吗 ？ ", "champion_auction_3", []],
  [trp_sword_sister|plyr, "champion_auction_begin", [
    (check_quest_active, "qst_champion_auction"),
    (eq, "$champion_auction_quest_phase", 2),
  ], "我 是 第 一 次 来 ， 有 什 么 要 注 意 的 吗 ？ ", "champion_auction_4", []],
  [trp_sword_sister|plyr, "champion_auction_begin", [], "没 有 问 题 了 。 我 要 加 入 竞 拍 。 ", "champion_auction_5", []],
  [trp_sword_sister, "champion_auction_1", [], "每 个 城 市 的 地 底 都 有 这 样 的 场 所 ， 为 想 要 进 行 不 能 公 之 于 众 的 买 卖 的 大 人 物 们 ， 提 供 一 个 能 安 心 交 易 的 场 所 。 这 个 地 堡 现 在 虽 然 由 我 们 长 期 租 赁 ， 但 是 建 造 者 和 所 有 者 还 是 权 厄 之 秤 … … 赞 美 权 厄 之 秤 吧 。 ", "champion_auction_pretalk", []],
  [trp_sword_sister, "champion_auction_2", [], "拍 卖 开 始 后 ， 拍 卖 师 会 给 出 起 拍 价 和 每 次 加 价 的 金 额 ， 您 只 需 与 其 他 来 宾 一 同 竞 拍 即 可 。 金 额 越 高 ， 有 人 跟 拍 的 可 能 性 就 越 低 。 拍 下 后 ， 我 们 会 将 他 妥 善 处 理 好 送 到 您 的 角 斗 场 上 。 不 用 劳 您 费 心 。 ", "champion_auction_pretalk", []],
  [trp_sword_sister, "champion_auction_3", [], "这 恐 怕 不 符 合 规 矩 。 毕 竟 ， 我 们 这 儿 的 成 交 价 往 往 在 一 万 以 下 ， 这 样 的 价 码 ， 在 明 面 上 的 奴 隶 市 场 里 可 远 远 买 不 到 一 位 角 斗 冠 军 。 角 斗 冠 军 对 战 名 不 见 经 传 的 黑 马 ， 这 样 一 场 对 决 能 卖 出 多 少 门 票 ， 最 后 的 惊 天 反 转 又 能 为 我 们 的 赌 场 带 来 多 少 收 益 啊 … … 我 们 也 是 要 吃 饭 的 ， 请 您 理 解 我 们 的 苦 衷 。 ", "champion_auction_pretalk", []],
  [trp_sword_sister, "champion_auction_4", [], "逢 人 只 说 三 分 话 ， 不 可 全 抛 一 片 心 。 我 们 服 务 的 可 都 是 心 机 深 沉 的 大 佬 ， 被 发 现 出 席 这 种 场 合 ， 日 后 或 许 会 成 为 把 柄 — — 当 然 ， 我 们 一 直 是 建 议 和 气 生 财 的 ， 但 是 来 宾 间 的 恩 怨 就 不 是 我 们 能 置 喙 的 了 。 因 此 ， 我 会 建 议 您 带 上 这 个 面 具 。 ", "champion_auction_pretalk", [
    (assign, "$champion_auction_quest_phase", 3),
    (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_steel_mask", 0, 0, 0),#铁假面
  ]],
  [trp_sword_sister, "champion_auction_pretalk", [], "还 有 什 么 问 题 吗 ？ ", "champion_auction_begin", []],
  [trp_sword_sister, "champion_auction_5", [], "好 的 ， 我 登 记 一 下 。 ", "close_window", [
    (mission_disable_talk),
    (assign, "$g_film_dialog", 1),#开始竞拍
    (reset_mission_timer_c),
  ]],

  [trp_libra_slave_catching_cavalry, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_champion_auction"),
    (assign, reg10, "$champion_auction_caculate_money"),
  ], "{reg10} 一 次 ， {reg10} 两 次 … … ", "champion_auction_6", []],
  [trp_libra_slave_catching_cavalry|plyr, "champion_auction_6", [
    (store_add, reg10, "$champion_auction_caculate_money", 1500),
  ], "{reg10} ！ ！ ！ ", "champion_auction_end_1", [
    (val_add, "$champion_auction_caculate_money", 1500),
  ]],
  [trp_libra_slave_catching_cavalry|plyr, "champion_auction_6", [
    (store_add, reg10, "$champion_auction_caculate_money", 600),
  ], "{reg10} ！ ", "champion_auction_end_1", [
    (val_add, "$champion_auction_caculate_money", 600),
  ]],
  [trp_libra_slave_catching_cavalry|plyr, "champion_auction_6", [
    (store_add, reg10, "$champion_auction_caculate_money", 200),
  ], "{reg10} 。 ", "champion_auction_end_1", [
    (val_add, "$champion_auction_caculate_money", 200),
  ]],
  [trp_libra_slave_catching_cavalry, "champion_auction_end_1", [
    (store_random_in_range, ":count_no", 4000, 10000),
    (ge, "$champion_auction_caculate_money", ":count_no"),
    (assign, reg10, "$champion_auction_caculate_money"),
  ], "{reg10}一 次 ！ {reg10}两 次 ！ {reg10}三 次 ！ 成 交 ！ ", "close_window", [
    (reset_mission_timer_c),
    (assign, "$g_film_dialog", 9),
  ]],
  [trp_libra_slave_catching_cavalry, "champion_auction_end_1", [
    (assign, reg10, "$champion_auction_caculate_money"),
  ], "{reg10} 一 次 — — 啊 ， 又 有 客 人 出 价 了 。 ", "close_window", [
    (reset_mission_timer_c),
    (assign, "$g_film_dialog", 5),
  ]],
  [trp_libra_slave_catching_cavalry|plyr, "champion_auction_6", [], "不 跟 。 ", "champion_auction_end_2", []],
  [trp_libra_slave_catching_cavalry, "champion_auction_end_2", [
    (store_random_in_range, ":count_no", 4000, 10000),
    (ge, "$champion_auction_caculate_money", ":count_no"),
    (assign, reg10, "$champion_auction_caculate_money"),
  ], "{reg10}三 次 ！ 那 么 ， 商 品 就 归 这 位 客 人 所 有 了 。 ", "close_window", [
    (display_message, "@你 在 竞 价 中 失 败 了 ， 是 时 候 离 开 这 里 了 。 但 是 无 妨 ， 人 的 欲 望 是 没 有 止 境 的 ， 总 会 有 源 源 不 断 的 角 斗 冠 军 ， 为 你 们 的 欲 望 提 供 取 之 不 竭 的 养 料 。 "),
    (check_quest_active, "qst_champion_auction"),
    (call_script, "script_end_quest", "qst_champion_auction"),
    (add_xp_to_troop, 600, "trp_player"),
    (assign, "$champion_auction_quest_phase", 8),
  ]],
  [trp_libra_slave_catching_cavalry, "champion_auction_end_2", [], "哦 ？ 又 有 客 人 出 价 了 。 ", "close_window", [
    (reset_mission_timer_c),
    (assign, "$g_film_dialog", 5),
  ]],

  [trp_sword_sister, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_champion_auction"),
    (eq, "$g_film_dialog", 9),
    (assign, "$g_film_dialog", 0),
  ], "这 位 客 人 ， 恭 喜 您 拍 下 了 今 天 的 商 品 ， 需 要 我 稍 后 为 您 安 排 角 斗 吗 ？ ", "champion_auction_success", []],
  [trp_sword_sister|plyr, "champion_auction_success", [], "没 问 题 。 ", "close_window", [
    (troop_remove_gold, "trp_player", "$champion_auction_caculate_money"),
    (party_get_slot, ":scene", "$current_town", slot_town_arena),
    (modify_visitors_at_site, ":scene"),
    (reset_visitors),
    (set_visitor, 32, "trp_player"),
    (store_sub, ":troop_no", "$current_town", "p_town_1"),
    (val_add, ":troop_no", "trp_town_1_arena_master"),
    (set_visitor, 51, ":troop_no"),#竞技场老板
    (try_begin),
       (check_quest_active, "qst_champion_auction"),
       (assign, "$champion_auction_quest_phase", 4),
       (str_store_string, s2, "@你 赢 下 了 拍 卖 ， 并 准 备 与 冠 军 斗 士 一 战 。 "),
       (add_quest_note_from_sreg, "qst_champion_auction", 3, s2, 0),
       (display_message, "str_quest_log_updated"),
       (set_visitor, 34, "trp_zela"),
    (else_try),
       (set_visitor, 34, "trp_confederation_gladiator_champion"),
    (try_end),
    (set_jump_mission, "mt_champion_auction_battle"),
    (jump_to_scene, ":scene"),
  ]],

  [anyone, "start", [
    (check_quest_active, "qst_champion_auction"),
    (eq, "$champion_auction_quest_phase", 4),
    (quest_slot_eq, "qst_champion_auction", slot_quest_giver_troop, "$g_talk_troop"),#竞技场老板
    (str_store_troop_name, s11, "trp_player"),
  ], "惊 天 反 转 ！ 经 过 了 酣 畅 淋 漓 的 战 斗 ， 我 们 的 冠 军 竟 然 倒 下 了 ！ 现 在 {s11}会 怎 么 做 呢 ？ ", "champion_auction_bettle_end", []],
  [anyone|plyr, "champion_auction_bettle_end", [], "杀 了 她 。 ", "close_window", [
    (call_script, "script_succeed_quest_special", "qst_champion_auction"),
    (add_xp_to_troop, 1500, "trp_player"),
    (assign, "$champion_auction_quest_phase", 8),
    (display_message, "@昔 日 的 冠 军 倒 在 血 泊 中 ， 观 众 们 寂 静 了 数 秒 ， 随 后 爆 发 了 欢 呼 ， 为 新 的 冠 军 献 上 喝 彩 。 胜 利 、 荣 耀 、 声 名 和 生 命 ， 一 切 都 不 过 是 金 钱 的 游 戏 ， 这 便 是 冠 军 拍 卖 。 "),
    (call_script, "script_change_troop_renown", "trp_player", "$champion_auction_add_money"),
    (finish_mission),
  ]],
  [anyone|plyr, "champion_auction_bettle_end", [], "留 她 一 命 。 ", "champion_auction_bettle_end_1", []],
  [anyone, "champion_auction_bettle_end_1", [], "啊 ？ 这 不 合 … 嗯 … … 真 是 一 位 仁 慈 的 人 啊 ， 观 众 朋 友 们 ， 让 我 们 为 之 欢 呼 吧 ！ ", "close_window", [
    (assign, "$champion_auction_quest_phase", 5),
    (call_script, "script_change_troop_renown", "trp_player", "$champion_auction_add_money"),
    (str_store_string, s2, "@用 下 作 的 手 段 赢 得 了 比 赛 ， 看 着 倒 地 的 对 手 不 甘 的 眼 神 ， 你 于 心 不 忍 。 或 许 你 可 以 另 找 时 间 与 竞 技 场 老 板 谈 谈 ？ 既 然 竞 技 场 靠 假 赛 赚 钱 的 目 的 已 经 达 到 了 ， 或 许 你 可 以 带 走 她 。 "),
    (display_message, "str_quest_log_updated"),
    (add_quest_note_from_sreg, "qst_champion_auction", 4, s2, 0),
    (finish_mission),
  ]],


  [anyone, "start", [
    (check_quest_active, "qst_champion_auction"),
    (eq, "$champion_auction_quest_phase", 5),
    (quest_slot_eq, "qst_champion_auction", slot_quest_giver_troop, "$g_talk_troop"),#竞技场老板
  ], "那 么 ， {playername}… … ", "champion_auction_after_battle", []],
  [anyone, "champion_auction_after_battle", [], "我 知 道 你 的 来 意 ， 也 知 道 你 在 想 什 么 。 你 远 远 不 是 第 一 个 这 么 干 的 人 ， 也 不 会 是 最 后 一 个 。 ", "champion_auction_after_battle_1", []],
  [anyone, "champion_auction_after_battle_1", [], "我 就 开 门 见 山 地 说 吧 ， {playername}， 我 们 会 给 她 藏 一 段 时 间 ， 之 后 我 们 便 会 给 她 改 头 换 面 一 番 ， 然 后 卖 掉 。 但 是 ， 这 个 买 家 不 能 是 你 。 ", "champion_auction_after_battle_2", []],
  [anyone|plyr, "champion_auction_after_battle_2", [], "我 已 经 付 了 足 够 的 钱 ， 你 们 也 靠 这 场 比 赛 的 门 票 和 赌 局 赚 得 盆 满 钵 满 ， 为 什 么 还 不 撒 手 呢 ？ ", "champion_auction_after_battle_3", []],
  [anyone, "champion_auction_after_battle_3", [], "你 想 算 帐 ， 那 我 就 跟 你 算 算 — — 你 花 的 那 笔 钱 ， 是 用 来 购 买 声 名 的 ， 现 在 你 已 经 得 偿 所 愿 了 ， 一 手 交 钱 一 手 交 货 ， 我 们 的 交 易 已 经 圆 满 完 成 了 。 不 肯 撒 手 的 是 你 ， {playername}。 然 后 ， 若 是 把 她 当 赠 品 送 给 你 ， 我 们 又 会 失 去 什 么 呢 ？ ", "champion_auction_after_battle_4", []],
  [anyone, "champion_auction_after_battle_4", [], "— — 安 全 。 你 的 恻 隐 之 心 ， 让 我 们 所 有 人 处 于 危 险 之 中 。 如 果 她 从 你 手 上 逃 跑 了 怎 么 办 ？ 如 果 你 被 她 打 动 ， 把 她 放 走 了 怎 么 办 ？ 甚 至 ， 如 果 你 被 她 蛊 惑 ， 联 合 起 来 揭 露 我 们 的 交 易 怎 么 办 ？ 这 也 是 我 们 不 允 许 你 再 去 购 买 她 的 原 因 。 ", "champion_auction_after_battle_5", []],
  [anyone|plyr, "champion_auction_after_battle_5", [], "你 们 这 是 在 进 行 服 从 性 测 试 。 ", "champion_auction_after_battle_6", []],
  [anyone, "champion_auction_after_battle_6", [], "唉 ， 话 不 用 说 得 这 么 难 听 ， 我 的 朋 友 。 我 们 都 是 手 握 权 钱 或 者 力 量 的 人 ， 没 人 愿 意 被 别 人 规 训 和 考 核 ， 这 个 我 也 能 理 解 。 不 过 正 因 如 此 ， 你 才 更 应 意 识 到 ， 我 们 才 是 朋 友 和 同 类 ， 与 那 些 贱 民 不 同 。 不 要 为 餐 桌 上 的 肉 动 恻 隐 之 心 。 ", "champion_auction_after_battle_7", []],
  [anyone|plyr, "champion_auction_after_battle_7", [], "… … … … ", "champion_auction_after_battle_8", []],
  [anyone, "champion_auction_after_battle_8", [], "亲 爱 的 {playername}， 我 的 朋 友 ， 我 真 心 地 奉 劝 你 好 好 休 息 几 天 ， 享 受 享 受 贱 民 们 对 你 的 崇 敬 ， 获 胜 的 喜 悦 ， 好 好 想 想 这 个 问 题 。 你 只 是 太 累 了 ， 后 续 的 事 由 我 们 处 理 即 可 ， 毕 竟 … … ", "champion_auction_after_battle_9", []],
  [anyone, "champion_auction_after_battle_9", [], "毕 竟 ， 过 去 那 些 想 要 插 手 到 底 的 人 ， 结 局 都 不 是 太 好 。 ", "close_window", [
    (assign, "$champion_auction_quest_phase", 6),
    (str_store_party_name_link, s20, "$current_town"),
    (str_store_string, s2, "@竞 技 场 老 板 软 硬 兼 施 ， 让 你 碰 了 个 钉 子 ， 无 计 可 施 ， 你 只 能 另 作 打 算 。 或 许 就 和 他 说 的 一 样 ， 好 好 休 息 休 息 ， 不 插 手 这 件 事 ， 才 是 最 好 的 结 果 。 ^在 {s20}休 息 。 "),
    (add_quest_note_from_sreg, "qst_champion_auction", 5, s2, 0),
    (display_message, "str_quest_log_updated"),
  ]],




###——————————————————————————————第三个死——————————————————————————————-
##
  [trp_lance_protector_francois_beaumont, "start", [
    (neg|troop_slot_ge, "$g_talk_troop", slot_troop_met_previously, 1),#以前没见过
  ], "你 好 ， {playername}， 我 听 说 过 你 的 名 字 。 ", "lance_protector_first_meet", [
    (troop_set_slot, "$g_talk_troop", slot_troop_met_previously, 1),
  ]],
  [trp_lance_protector_francois_beaumont, "lance_protector_first_meet", [], "我 是 现 任 戈 兰 尼 尔 民 兵 自 卫 军 的 护 枪 官 ， 亦 即 指 挥 官 ， 弗 朗 索 瓦 ·博 蒙 。 ", "lance_protector_first_meet_2", []],
  [trp_lance_protector_francois_beaumont, "start", [
    (troop_slot_ge, "$g_talk_troop", slot_troop_met_previously, 1),
  ], "你 好 ， {playername}。 今 天 你 有 什 么 事 ？ ", "lance_protector_first_meet_2", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_first_meet_2", [], "那 么 ， 你 有 什 么 事 吗 ？ ", "lance_protector_pretalk", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [], "能 介 绍 一 下 戈 兰 尼 尔 民 兵 自 卫 军 吗 ？ ", "lance_protector_introduce_1", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_1", [], "要 是 现 在 是 两 个 世 纪 前 ， 我 会 非 常 乐 意 向 你 说 明 的 ， 但 是 现 在 … … 戈 兰 尼 尔 低 地 大 平 原 一 直 是 举 世 闻 名 的 粮 仓 ， 百 姓 生 活 富 裕 ， 足 以 自 行 组 建 治 安 军 ， 协 助 领 主 维 护 本 地 的 安 宁 。 最 辉 煌 时 ， 自 卫 军 人 数 超 过 了 八 千 ， 受 罗 德 里 格 斯 王 室 所 托 保 管 着 三 件 国 宝 之 一 ， 还 有 自 己 的 骑 兵 队 ， 由 被 人 民 的 热 情 与 善 良 吸 引 的 侠 义 骑 士 领 导 。 不 过 … … ", "lance_protector_introduce_2", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_2", [], "我 们 曾 经 自 夸 能 媲 美 骑 士 团 ， 然 而 当 真 正 走 上 战 场 时 ， 我 们 被 普 威 尔 人 的 骑 兵 轻 而 易 举 地 碾 碎 了 。 罗 德 里 格 斯 王 国 沦 陷 了 两 百 年 ， 我 们 也 沦 为 一 个 边 缘 小 团 体 ， 充 其 量 只 能 和 土 匪 掰 掰 手 腕 了 。 这 就 是 自 卫 军 的 现 状 。 ", "lance_protector_introduce_end", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [], "能 和 我 说 说 “ 护 枪 官 ” 这 个 头 衔 吗 ？ ", "lance_protector_introduce_3", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_3", [], "罗 德 里 格 斯 王 国 曾 经 拥 有 三 件 神 器 ， 一 是 能 无 限 涌 出 食 粮 的 金 杯 ， 二 是 受 击 能 回 复 持 盾 者 生 命 的 盾 牌 ， 三 是 挥 舞 即 能 恢 复 生 命 的 神 枪 ， 即 护 枪 官 所 护 的 丰 收 女 神 肖 像 枪 。 曾 经 ， 为 了 体 现 对 人 民 的 信 任 ， 王 室 将 神 枪 交 给 我 们 自 卫 军 保 管 ， 以 示 人 民 对 王 室 的 监 督 。 不 过 这 三 件 神 器 都 先 后 遗 失 了 。 ", "lance_protector_introduce_4", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_4", [], "肖 像 枪 在 与 普 威 尔 军 的 决 战 中 下 落 不 明 。 护 枪 官 安 托 万 ·莫 罗 手 持 神 枪 ， 在 如 今 鲁 克 斯 领 处 与 入 侵 者 血 战 ， 斩 杀 过 千 ， 凭 一 己 之 力 阻 拦 普 威 尔 主 力 超 过 两 个 小 时 ， 血 战 而 死 ， 尸 体 依 然 持 枪 而 立 。 普 威 尔 人 甚 至 不 敢 去 收 敛 他 的 尸 体 ， 绕 行 数 公 里 才 继 续 前 进 。 在 那 以 后 ， 他 的 尸 首 和 神 枪 便 都 下 落 不 明 了 。 ", "lance_protector_introduce_5", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_introduce_5", [], "是 被 普 威 尔 王 室 收 去 了 吗 ？ ", "lance_protector_introduce_6", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_6", [], "很 遗 憾 ， 并 没 有 。 八 十 年 前 ， 内 战 之 中 ， 我 们 公 国 曾 短 暂 入 主 普 威 尔 王 都 ， 第 一 个 做 的 便 是 查 证 此 事 。 据 说 普 威 尔 王 室 对 此 事 也 是 一 头 雾 水 。 神 枪 的 下 落 已 是 历 史 悬 案 了 … … 可 惜 。 护 枪 官 也 再 就 名 不 副 实 了 。 ", "lance_protector_introduce_end", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [], "能 和 我 说 说 两 百 年 前 的 战 争 吗 ？ ", "lance_protector_introduce_7", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_7", [], "早 在 赤 铜 纪 ， 罗 德 里 格 斯 王 国 和 普 威 尔 人 就 是 常 年 征 战 的 老 冤 家 了 。 我 们 经 济 发 达 ， 人 民 富 足 ， 他 们 地 盘 广 大 ， 人 口 众 多 ， 双 方 你 来 我 往 ， 僵 持 不 下 。 你 看 地 图 就 会 知 道 ， 从 普 威 尔 地 区 入 侵 戈 兰 尼 尔 大 平 原 ， 要 么 从 北 线 经 过 加 西 亚 领 ， 要 么 从 南 线 穿 过 杜 朋 领 ， 这 两 个 家 族 曾 经 合 称 王 国 双 璧 ， 阻 挡 普 威 尔 人 的 野 心 数 百 年 。 ", "lance_protector_introduce_8", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_8", [], "不 过 在 1180年 ， 普 威 尔 人 收 买 了 内 奸 ， 在 鬼 哭 崖 中 找 寻 到 一 条 绝 大 多 数 当 地 人 都 不 知 道 的 小 径 ， 秘 密 地 分 批 运 了 两 千 余 人 进 来 。 那 一 块 是 我 们 民 兵 自 卫 军 的 管 辖 范 围 ， 我 们 曾 有 机 会 一 举 歼 灭 他 们 ， 但 我 们 错 失 了 机 会 ， 最 终 导 致 他 们 站 稳 脚 跟 ， 前 后 夹 击 ， 突 袭 了 杜 朋 领 … … 最 终 ， 罗 德 里 格 斯 王 国 沦 陷 了 。 这 就 是 故 事 的 结 局 。 ", "lance_protector_introduce_end", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [], "能 和 我 说 说 你 自 己 吗 ？ ", "lance_protector_introduce_9", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_9", [], "哈 哈 ， 对 我 这 种 小 角 色 的 身 世 感 兴 趣 的 人 可 不 多 。 ", "lance_protector_introduce_10", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_10", [], "你 大 概 会 失 望 了 ， 我 没 有 什 么 波 澜 壮 阔 的 过 往 ， 曾 经 就 只 是 公 爵 手 下 一 名 普 通 的 内 府 骑 士 。 在 一 次 清 剿 魔 物 的 任 务 中 ， 我 们 错 估 了 形 势 ， 最 后 只 有 身 受 重 伤 的 我 逃 出 生 天 。 是 自 卫 军 的 民 兵 救 下 了 我 ， 给 我 治 疗 ， 保 住 了 我 一 条 小 命 。 了 解 到 他 们 一 盘 散 沙 、 濒 临 解 散 的 现 状 后 ， 我 便 自 告 奋 勇 成 为 了 他 们 的 指 挥 官 。 ", "lance_protector_introduce_end", []],

  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [
    (neg|check_quest_active, "qst_third_death"),
    (le, "$third_death_quest_phase", 0),
  ], "我 听 说 你 有 一 些 任 务 需 要 人 做 。 ", "lance_protector_mission_1", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_1", [], "是 罗 德 里 格 斯 勋 爵 让 你 来 的 吧 。 是 这 样 没 错 ， 不 过 也 只 是 一 件 不 大 不 小 的 事 情 。 ", "lance_protector_mission_2", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_2", [], "是 这 样 的 ， 两 百 年 前 普 威 尔 人 入 侵 的 第 一 个 前 哨 战 ， 就 位 于 如 今 的 加 尔 村 附 近 。 加 尔 村 的 村 长 向 我 们 报 告 ， 他 们 最 近 挖 出 了 几 座 一 两 百 年 的 野 坟 。 ", "lance_protector_mission_3", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_3", [], "我 抽 不 开 身 ， 因 此 希 望 有 人 能 替 我 去 看 看 情 况 ， 如 果 有 值 得 研 究 的 文 物 ， 就 带 回 来 ， 就 是 这 样 。 你 能 帮 我 这 个 忙 吗 ？ ", "lance_protector_mission_4", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_4", [], "听 起 来 不 是 什 么 大 事 ， 没 问 题 。 ", "lance_protector_mission_5", [
    (call_script, "script_change_player_relation_with_troop","$g_talk_troop", 10),
    (call_script, "script_change_faction_relarion_with_player", "itm_grenier_militia", 5),
  ]],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_5", [], "那 就 多 谢 了 。 遇 上 拿 不 准 的 情 况 ， 可 以 随 时 回 来 问 我 。 ", "lance_protector_introduce_end", [
    (str_store_troop_name_link, s21, "$g_talk_troop"),
    (str_store_party_name_link, s22, "p_village_1_12"),
    (str_store_string, s2, "@{s22}的 村 长 报 告 称 发 现 了 几 座 古 代 战 争 时 期 留 下 的 荒 坟 ， {s21}让 你 去 接 收 发 掘 到 的 有 价 值 的 物 资 。 "),
    (call_script, "script_start_quest", "qst_third_death", -1),
    (assign, "$third_death_quest_phase", 1),
  ]],

  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [
    (check_quest_active, "qst_third_death"),
    (is_between, "$third_death_quest_phase", 9, 11),
  ], "关 于 你 给 我 任 务 … … ", "lance_protector_mission_6", [
    (assign, "$third_death_quest_phase", 11),
  ]],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_6", [], "你 们 的 奇 遇 ， 我 已 经 听 加 西 亚 小 姐 说 了 。 没 想 到 仅 仅 是 去 取 个 东 西 ， 你 们 还 能 遇 到 这 种 奇 遇 … … ", "lance_protector_mission_7", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_7", [
    (troop_add_gold, "trp_player", 10000),
  ], "如 论 如 何 辛 苦 你 们 跑 一 趟 了 ， 一 点 心 意 ， 还 望 笑 纳 。 ", "lance_protector_mission_8", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_8", [], "那 么 我 就 回 去 向 罗 德 里 格 斯 勋 爵 复 命 了 。 ", "lance_protector_mission_9", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_9", [], "等 等 ， 我 还 有 一 个 请 求 。 ", "lance_protector_mission_10", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_10", [], "你 不 会 是 还 想 让 我 们 再 去 一 趟 吧 。 ", "lance_protector_mission_11", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_11", [], "哈 哈 ， 什 么 都 瞒 不 过 您 啊 。 是 这 样 的 ， 我 在 想 ， 既 然 能 回 溯 到 那 个 时 代 的 历 史 ， 或 许 能 得 知 护 枪 官 安 托 万 ·莫 罗 的 去 向 ， 甚 至 可 能 见 到 他 本 人 ？ 如 果 能 得 到 有 用 的 信 息 ， 您 将 得 到 我 和 我 们 戈 兰 尼 尔 民 兵 自 卫 军 全 体 的 最 高 谢 意 。 ", "lance_protector_mission_12", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_12", [], "再 次 回 去 未 必 还 能 进 入 历 史 迷 雾 。 虽 然 不 清 楚 它 的 机 理 ， 但 我 觉 得 这 种 东 西 不 会 持 续 太 长 时 间 的 。 ", "lance_protector_mission_13", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_13", [], "如 果 是 那 样 ， 那 也 只 能 说 是 神 的 旨 意 。 我 有 心 理 准 备 。 ", "lance_protector_mission_14", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_14", [], "另 外 我 说 句 不 好 听 的 … … 你 为 什 么 不 自 己 去 呢 ？ ", "lance_protector_mission_15", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_15", [], "公 务 缠 身 啊 。 不 知 您 是 否 接 到 情 报 ， 说 有 最 近 有 一 队 魔 王 尖 兵 在 戈 兰 尼 尔 地 区 肆 虐 。 虽 然 它 们 被 元 素 骑 士 团 击 溃 了 ， 但 还 有 几 骑 侥 幸 脱 逃 。 对 于 有 城 墙 保 护 的 我 们 来 说 ， 这 几 个 残 兵 败 将 是 构 不 成 威 胁 了 ， 但 是 对 于 广 大 农 村 地 区 而 言 ， 一 队 魔 王 尖 兵 是 灭 村 ， 一 头 魔 王 尖 兵 也 是 灭 村 。 ", "lance_protector_mission_16", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_16", [], "这 种 多 事 之 秋 ， 如 果 我 们 戈 兰 尼 尔 民 兵 自 卫 军 不 能 挺 身 而 出 ， 保 护 百 姓 ， 那 如 何 还 有 脸 自 称 民 兵 自 卫 军 ？ ", "lance_protector_mission_17", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_17", [], "恕 我 直 言 ， 以 戈 兰 尼 尔 民 兵 自 卫 军 的 平 均 水 准 ， 面 对 这 种 对 手 ， 恐 怕 … … ", "lance_protector_mission_18", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_18", [], "哈 哈 ， 您 不 用 担 心 。 在 和 魔 王 尖 兵 正 面 对 抗 的 战 场 上 ， 我 们 是 帮 不 上 什 么 忙 ， 但 在 搜 索 它 们 的 过 程 中 ， 我 们 还 是 能 发 挥 巨 大 作 用 的 … … 说 来 很 残 酷 ， 我 们 将 人 员 大 面 积 地 分 散 出 去 ， 广 泛 全 面 地 搜 索 ， 只 要 某 一 个 方 向 的 人 员 牺 牲 了 ， 就 能 知 道 魔 王 尖 兵 位 于 何 方 。 ", "lance_protector_mission_19", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_19", [], "我 们 都 是 百 姓 的 父 亲 、 儿 子 、 丈 夫 ， 我 们 做 好 了 牺 牲 的 准 备 。 而 在 小 伙 子 们 抛 头 颅 洒 热 血 的 时 候 ， 我 这 个 长 官 又 怎 么 能 不 顾 一 切 地 跑 掉 ， 去 找 一 把 消 失 二 百 三 十 年 的 枪 呢 ？ 即 便 它 很 重 要 。 ", "lance_protector_mission_20", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_20", [], "所 以 ， 这 就 是 我 希 望 您 能 替 我 再 跑 一 趟 的 原 因 ， 请 让 我 代 表 戈 兰 尼 尔 民 兵 自 卫 军 再 次 恳 求 您 。 如 果 您 还 有 什 么 需 要 提 供 的 ， 请 尽 管 开 口 。 ", "lance_protector_mission_21", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_21", [], "这 趟 很 危 险 ， 我 还 需 要 一 点 经 费 整 顿 装 备 。 ", "lance_protector_mission_22", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_22", [
    (troop_add_gold, "trp_player", 5000),
  ], "没 问 题 ， 我 会 为 您 准 备 好 的 。 戈 兰 尼 尔 低 地 大 平 原 自 古 就 是 王 国 粮 仓 ， 钱 还 是 不 怎 么 缺 的 ， 哈 哈 。 ", "close_window", [
    (str_store_string, s2, "@护 枪 官 恳 请 你 们 再 次 回 到 历 史 迷 雾 ， 设 法 调 查 古 代 护 枪 官 安 托 万 ·莫 罗 和 丰 收 女 神 肖 像 枪 的 下 落 。 "),
    (add_quest_note_from_sreg, "qst_third_death", 5, s2, 0),
    (display_message, "str_quest_log_updated"),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_21", [], "不 必 了 ， 把 钱 留 给 战 士 们 吧 。 ", "lance_protector_mission_23", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_23", [], "您 是 一 位 高 尚 的 人 。 那 么 ， 我 就 祝 您 一 路 顺 风 了 。 ", "close_window", [
    (call_script, "script_change_player_relation_with_troop","$g_talk_troop", 20),
    (call_script, "script_change_faction_relarion_with_player", "itm_grenier_militia", 20),
    (str_store_string, s2, "@护 枪 官 恳 请 你 们 再 次 回 到 历 史 迷 雾 ， 设 法 调 查 古 代 护 枪 官 安 托 万 ·莫 罗 和 丰 收 女 神 肖 像 枪 的 下 落 。 "),
    (add_quest_note_from_sreg, "qst_third_death", 5, s2, 0),
    (display_message, "str_quest_log_updated"),
  ]],

  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 18),
  ], "关 于 你 给 我 任 务 … … ", "lance_protector_mission_24", [
    (assign, "$third_death_quest_phase", 19),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_24", [], "我 们 在 谬 史 中 见 到 了 安 托 万 ·莫 罗 本 人 ， 他 还 随 身 携 带 了 肖 像 枪 。 ", "lance_protector_mission_25", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_25", [], "真 的 ？ 太 好 了 ！ 这 可 是 这 么 多 天 以 来 的 第 一 个 好 消 息 了 ！ ", "lance_protector_mission_26", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_26", [], "战 况 很 吃 紧 吗 ？ ", "lance_protector_mission_27", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_27", [], "何 止 ？ 这 伙 魔 王 尖 兵 极 其 狡 猾 ， 被 我 们 追 踪 到 了 两 次 后 ， 它 们 改 变 了 策 略 ， 转 而 开 始 大 批 量 地 制 造 魔 卒 ， 让 这 些 追 随 者 制 造 假 象 ， 诱 导 我 们 的 注 意 力 。 靠 这 一 招 ， 它 们 已 经 三 次 从 我 们 的 包 围 网 里 突 围 了 ， 我 们 的 阵 亡 人 数 也 达 到 了 三 百 。 ", "lance_protector_mission_28", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_28", [], "大 家 的 心 情 都 很 低 落 ， 几 乎 要 打 不 下 去 了 。 如 果 有 肖 像 枪 … … 只 要 能 有 肖 像 枪 ！ ", "lance_protector_mission_29", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_29", [], "恐 怕 要 给 你 泼 冷 水 了 ， 我 们 无 法 从 谬 史 中 知 道 安 托 万 ·莫 罗 的 去 向 ， 因 为 对 于 我 们 进 入 的 那 段 谬 史 ， 他 的 战 死 是 未 来 。 ", "lance_protector_mission_30", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_30", [], "这 … … 唉 … … … 我 想 再 拜 托 你 最 后 一 件 事 可 以 吗 ？ — — 杀 掉 莫 罗 ， 直 接 抢 走 肖 像 枪 。 ", "lance_protector_mission_31", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_31", [], "你 疯 了 ？ 那 可 是 你 的 前 辈 。 ", "lance_protector_mission_32", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_32", [], "他 在 二 百 三 十 年 前 就 是 个 死 人 了 ， 而 我 们 的 人 每 时 每 刻 都 在 死 ， 包 括 此 时 此 刻 ！ ", "lance_protector_mission_33", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_33", [
    (troop_add_gold, "trp_player", 5000),
  ], "但 是 … … 我 也 不 能 道 德 绑 架 你 。 这 是 你 的 报 酬 ， 你 在 我 这 里 的 任 务 已 经 完 成 了 ， 我 会 给 勋 爵 阁 下 写 信 的 。 只 是 … … ", "lance_protector_mission_34", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_34", [], "唉 ， 罢 了 ， 罢 了 ！ ", "close_window", []],

  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 23),
    (call_script, "script_troop_has_item_with_modifier_new", "trp_player", "itm_harvest_goddess_portrait_lance", -1),#带了肖像枪
    (ge, reg1, 0),
  ], "我 拿 到 了 肖 像 枪 。 ", "lance_protector_mission_35", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_35", [], "我 、 我 不 是 在 做 梦 吧 ， 你 居 然 真 的 拿 回 了 肖 像 枪 ！ 不 ， 我 不 是 不 信 任 你 ， 只 是 我 不 敢 相 信 这 是 真 的 … … ", "lance_protector_mission_36", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_36", [
    (call_script, "script_troop_remove_item_with_modifier_new", "trp_player", "itm_harvest_goddess_portrait_lance", -1),#移除肖像枪
    (call_script, "script_change_player_relation_with_troop","$g_talk_troop", 40),
    (call_script, "script_change_faction_relarion_with_player", "itm_grenier_militia", 30),
  ], "我 感 觉 到 了 ， 这 毫 无 疑 问 是 真 的 丰 收 女 神 肖 像 枪 ！ 民 兵 自 卫 军 有 救 了 ！ 太 棒 了 ， {playername}阁 下 ， 我 向 你 致 以 最 高 的 谢 意 ， 你 将 永 远 是 我 们 最 好 的 朋 友 。 ", "lance_protector_mission_37", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_37", [], "你 过 奖 了 。 事 实 上 … … 嗯 。 ", "lance_protector_mission_38", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_mission_38", [], "另 外 ， 民 兵 自 卫 军 在 最 辉 煌 的 时 候 ， 曾 经 吸 引 了 大 量 侠 义 骑 士 前 来 供 职 ， 这 些 精 锐 使 得 我 们 的 实 力 能 比 肩 骑 士 团 。 在 肖 像 枪 失 而 复 得 后 ， 我 有 信 心 能 再 现 往 日 的 荣 光 。 ", "lance_protector_mission_39", []],  
[trp_lance_protector_francois_beaumont, "lance_protector_mission_39", [], "给 我 们 一 点 时 间 ， 之 后 我 会 发 信 件 给 您 。 到 那 时 ， 您 可 以 每 周 来 看 看 ， 说 不 定 会 有 骑 士 受 您 历 险 故 事 的 感 召 ， 愿 意 为 您 效 力 。 ", "lance_protector_mission_40", []],
[trp_lance_protector_francois_beaumont|plyr, "lance_protector_mission_40", [], "好 的 ， 我 会 期 待 的 。 ", "lance_protector_introduce_end", [
    (assign, "$third_death_quest_phase", 24),
    (assign, "$portrait_lance_corrosion", 0),
    (call_script, "script_succeed_quest_special", "qst_third_death"),
    (troop_add_gold, "trp_player", 30000),
    (add_xp_to_troop, 5000, "trp_player"),
    (call_script, "script_change_troop_renown", "trp_player", 100),
  ]],


  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [#招募士兵
    (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
    (ge, reg0, 10),
  ], "我 想 雇 佣 一 些 民 兵 自 卫 军 的 战 士 。 ", "lance_protector_rectuit", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_rectuit", [
    (item_slot_ge, "itm_grenier_militia", slot_faction_military_provide, 1),
  ], "没 问 题 ， 我 这 里 正 好 有 些 小 伙 子 想 出 去 打 拼 打 拼 。 ", "lance_protector_rectuit_1", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_rectuit", [
    (neg|item_slot_ge, "itm_grenier_militia", slot_faction_military_provide, 1),
  ], "今 天 不 行 ， 我 们 现 在 没 有 多 余 的 人 手 了 。 你 下 周 再 来 看 看 吧 。 ", "lance_protector_introduce_end", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_1", [], "我 想 雇 佣 20名 戈 兰 尼 尔 民 兵 。 ", "lance_protector_rectuit_2", [
    (assign, "$temp", "trp_grenier_militia"),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_1", [
    (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
    (ge, reg0, 20),
  ], "我 想 雇 佣 10名 戈 兰 尼 尔 精 选 民 兵 。 ", "lance_protector_rectuit_2", [
    (assign, "$temp", "trp_grenier_wellselected_militia"),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_1", [
    (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
    (ge, reg0, 40),
  ], "我 想 雇 佣 10名 戈 兰 尼 尔 骑 手 。 ", "lance_protector_rectuit_2", [
    (assign, "$temp", "trp_grenier_rider"),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_1", [
    (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
    (ge, reg0, 40),
  ], "我 想 雇 佣 10名 戈 兰 尼 尔 长 弓 手 。 ", "lance_protector_rectuit_2", [
    (assign, "$temp", "trp_grenier_longbow_archer"),
  ]],
  [trp_lance_protector_francois_beaumont, "lance_protector_rectuit_2", [
    (str_store_troop_name, s10, "$temp"),
  ], "可 以 ，{s10}。 您 需 要 付 1000铁 币 。 ", "lance_protector_rectuit_3", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_3", [
    (store_troop_gold, ":gold_count", "trp_player"),
    (ge, ":gold_count", 1000),
  ], "没 问 题 。 ", "lance_protector_introduce_end", [
    (troop_remove_gold, "trp_player", 1000),
    (try_begin),
       (eq, "$temp", "trp_grenier_militia"),
       (party_add_members, "p_main_party", "$temp", 20),
    (else_try),
       (eq, "$temp", "trp_grenier_wellselected_militia"),
       (party_add_members, "p_main_party", "$temp", 15),
    (else_try),
       (eq, "$temp", "trp_grenier_rider"),
       (party_add_members, "p_main_party", "$temp", 10),
    (else_try),
       (eq, "$temp", "trp_grenier_longbow_archer"),
       (party_add_members, "p_main_party", "$temp", 10),
    (try_end),
    (item_set_slot, "itm_grenier_militia", slot_faction_military_provide, 0),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_3", [], "我 再 想 想 。 ", "lance_protector_introduce_end", []],

  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_1", [
    (neg|check_quest_active, "qst_third_death"),#任务已完成
    (ge, "$third_death_quest_phase", 24),
    (ge, "$portrait_lance_corrosion", 40),
  ], "我 希 望 寻 找 几 位 侠 义 骑 士 为 我 效 力 。 ", "lance_protector_rectuit_4", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_rectuit_4", [
    (item_get_slot, "$temp", "itm_grenier_militia", slot_faction_relation_with_player),
    (val_div, "$temp", 30),
    (assign, reg20, "$temp"),
  ], "没 问 题 ， 这 周 有 {reg20}名 年 轻 骑 士 愿 意 为 您 效 力 。 您 愿 意 接 收 他 们 吗 ？ ", "lance_protector_rectuit_5", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_5", [], "没 问 题 ， 非 常 欢 迎 。 ", "lance_protector_introduce_end", [
    (party_add_members, "p_main_party", "trp_grenier_chivalric_knight", "$temp"),
    (item_set_slot, "itm_grenier_militia", slot_faction_military_provide, 0),
  ]],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_1", [], "算 了 ， 今 天 先 不 用 。 ", "lance_protector_introduce_end", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_rectuit_5", [], "我 再 想 想 。 ", "lance_protector_introduce_end", []],

  [trp_lance_protector_francois_beaumont, "lance_protector_introduce_end", [], "还 有 什 么 想 问 的 吗 ？ ", "lance_protector_pretalk", []],
  [trp_lance_protector_francois_beaumont|plyr, "lance_protector_pretalk", [], "请 让 我 告 辞 。 ", "lance_protector_leave", []],
  [trp_lance_protector_francois_beaumont, "lance_protector_leave", [], "当 然 ， {playername}， 再 会 了 。 ", "close_window", []],


  [trp_npc4, "start", [
    (eq, "$third_death_quest_phase", 1),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "这 个 雾 并 不 寻 常 。  {playername}大 人 ， 我 们 小 心 行 事 。 ", "third_death_fanlentina_1", []],
  [trp_npc4, "third_death_fanlentina_1", [], "前 方 好 像 有 人 。 我 们 去 了 解 一 下 情 况 ？ ", "close_window", []],

  [trp_yannick_village_elder|plyr, "start", [
    (eq, "$third_death_quest_phase", 1),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "请 问 您 就 是 这 里 的 村 长 吗 ？ ", "third_death_yannick_1", []],
  [trp_yannick_village_elder, "third_death_yannick_1", [], "是 的 ， 我 就 是 加 尔 村 的 村 长 扬 尼 克 … … 但 你 们 是 谁 ？ 外 乡 人 ， 我 以 前 没 见 过 你 们 。 ", "third_death_yannick_2", []],
  [trp_yannick_village_elder|plyr, "third_death_yannick_2", [], "你 们 村 不 是 说 发 现 了 几 个 古 墓 吗 ？ ", "third_death_yannick_3", []],
  [trp_yannick_village_elder, "third_death_yannick_3", [
    (agent_set_is_alarmed, "$film_character_2", 1),
  ], "墓 ？ 哦 … … 你 们 是 圣 别 渴 求 者 啊 。 这 都 什 么 时 候 了 ， 还 在 说 这 些 。 ", "third_death_yannick_4", []],
  [trp_yannick_village_elder, "third_death_yannick_4", [], "我 劝 你 们 一 句 吧 ， 最 近 时 局 不 太 平 ， 山 中 出 现 了 很 多 怪 事 。 山 雨 欲 来 ， 加 尔 村 只 怕 过 不 了 多 久 也 要 乱 起 来 了 ， 你 们 还 是 赶 紧 逃 命 为 好 。 ", "third_death_yannick_5", []],
  [trp_yannick_village_elder|plyr, "third_death_yannick_5", [], "这 都 什 么 和 什 么 啊 … … ", "third_death_yannick_6", []],
  [trp_yannick_village_elder, "third_death_yannick_6", [], "请 回 吧 ， 我 们 现 在 没 空 接 待 二 位 。 ", "third_death_yannick_7", []],
  [trp_yannick_village_elder|other(trp_npc4), "third_death_yannick_7", [], " {playername}大 人 ， 我 们 借 一 步 说 话 吧 。 ", "close_window", [
    (assign, "$third_death_quest_phase", 2),
  ]],

  [trp_yannick_village_elder, "start", [
    (is_between, "$third_death_quest_phase", 2, 5),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "请 回 吧 ， 我 们 现 在 没 空 接 待 二 位 。 ", "third_death_player_1", []],
  [anyone|plyr, "third_death_player_1", [
    (eq, "$third_death_quest_phase", 4),
  ], "（ 了 解 的 差 不 多 了 ， 回 去 和 范 伦 汀 娜 说 说 你 的 发 现 。 ） ", "close_window", []],
  [anyone|plyr, "third_death_player_1", [], "… …  … … ", "close_window", []],

  [trp_npc4, "start", [
    (is_between, "$third_death_quest_phase", 2, 4),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "{playername}大 人 ， 此 人 并 不 是 加 尔 村 的 村 长 。 我 记 得 加 尔 村 村 长 的 脸 。 ", "third_death_fanlentina_2", []],
  [trp_npc4, "third_death_fanlentina_2", [], "他 年 轻 时 是 鲁 克 斯 伯 爵 的 侍 从 ， 因 为 长 年 侍 奉 有 功 ， 获 封 勋 爵 骑 士 ， 得 到 了 加 尔 村 附 近 的 一 个 庄 园 作 为 产 业 。 我 曾 在 宴 会 上 远 远 一 窥 他 的 脸 。 ", "third_death_fanlentina_3", []],
  [trp_npc4|plyr, "third_death_fanlentina_3", [], "亏 你 还 记 得 … … 那 么 现 在 这 人 是 谁 ？ ", "third_death_fanlentina_4", []],
  [trp_npc4, "third_death_fanlentina_4", [], "对 不 起 ， 此 人 我 也 是 毫 无 印 象 呢 。 ", "third_death_fanlentina_5", []],
  [trp_npc4|plyr, "third_death_fanlentina_5", [], "我 们 没 走 错 地 方 吧 ？ 不 过 ， 他 也 说 自 己 是 加 尔 村 的 村 长 。 ", "third_death_fanlentina_6", []],
  [trp_npc4|plyr, "third_death_fanlentina_6", [], "那 边 是 不 是 还 有 其 他 人 ？ 我 去 问 问 他 们 好 了 。 ", "third_death_fanlentina_7", []],
  [trp_npc4, "third_death_fanlentina_7", [], "好 的 ， 我 也 回 去 我 们 来 时 路 上 看 看 。 ", "third_death_fanlentina_8", []],
  [trp_npc4|plyr, "third_death_fanlentina_8", [], "注 意 安 全 。 ", "close_window", [
    (try_begin),
       (eq, "$third_death_quest_phase", 2),
       (display_message, "@一 阵 阴 风 吹 过 ， 有 几 个 人 影 在 雾 里 现 身 了 … … 或 者 他 们 从 一 开 始 就 在 那 里 ？ "),
       (try_for_agents, ":agent_no"),
          (agent_is_human, ":agent_no"),
          (agent_is_alive, ":agent_no"),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (neg|troop_is_hero, ":troop_no"),
          (agent_set_visibility, ":agent_no", 1),
       (try_end),
    (try_end),
    (val_max, "$third_death_quest_phase", 3),
  ]],

  [anyone, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
    (eq, "$g_talk_troop", "trp_farmer"),
  ], "我 感 觉 有 点 不 安 ， 山 中 有 东 西 盯 着 我 们 … … （ 模 糊 不 清 ） ", "third_death_player_1", []],
  [anyone, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
    (eq, "$g_talk_troop", "trp_grenier_wellselected_militia"),
  ], "商 人 不 太 对 劲 ， 他 带 来 了 一 些 以 前 从 没 见 过 的 伙 计 。 而 且 我 看 他 带 了 八 人 ， 有 人 却 他 说 带 了 十 一 人 ， 还 有 说 十 五 人 的 … … … （ 模 糊 不 清 ） ", "third_death_player_1", []],
  [anyone, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
    (eq, "$g_talk_troop", "trp_hunter"),
  ], "后 山 的 猎 物 好 像 比 往 年 少 了 很 多 ， 再 这 样 下 去 … … 就 只 能 … … （ 模 糊 不 清 ） ", "third_death_player_1", []],

  [anyone, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
    (eq, "$g_talk_troop", "trp_caravan_master"),
    (val_max, "$third_death_quest_phase", 4),
  ], "你 这 个 蠢 妇 ， 我 租 你 的 仓 库 ， 可 不 是 让 你 一 把 火 给 它 烧 个 干 净 的 ！ 活 该 死 老 公 ！ ", "third_death_caravan_master_1", []],
  [anyone|other(trp_peasant_woman), "third_death_caravan_master_1", [], "不 ， 我 发 誓 我 没 有 在 仓 库 里 点 过 蜡 烛 … … （ 模 糊 不 清 ） ", "third_death_caravan_master_2", []],
  [anyone, "third_death_caravan_master_2", [], "我 不 管 ， 我 只 要 我 的 钱 ！ ", "third_death_player_1", []],

  [anyone|auto_proceed, "start", [
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
    (eq, "$g_talk_troop", "trp_peasant_woman"),
    (val_max, "$third_death_quest_phase", 4),
  ], "none", "third_death_peasant_woman_1", []],
  [anyone|other(trp_caravan_master), "third_death_peasant_woman_1", [], "你 这 个 蠢 妇 ， 我 租 你 的 仓 库 ， 可 不 是 让 你 一 把 火 给 它 烧 个 干 净 的 ！ 活 该 死 老 公 ！ ", "third_death_peasant_woman_2", []],
  [anyone, "third_death_peasant_woman_2", [], "不 ， 我 发 誓 我 没 有 在 仓 库 里 点 过 蜡 烛 … … （ 模 糊 不 清 ） ", "third_death_peasant_woman_3", []],
  [anyone|other(trp_caravan_master), "third_death_peasant_woman_3", [], "我 不 管 ， 我 只 要 我 的 钱 ！ ", "third_death_player_1", []],

  [trp_npc4|plyr, "start", [
    (is_between, "$third_death_quest_phase", 4, 6),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "范 伦 汀 娜 ， 我 们 来 交 换 一 下 信 息 吧 。 ", "third_death_fanlentina_9", []],
  [trp_npc4, "third_death_fanlentina_9", [], "好 的 ， {playername}大 人 ， 您 请 问 吧 。  ", "third_death_fanlentina_pretalk", []],
  [trp_npc4, "third_death_fanlentina_answer_end", [], "{playername}大 人 ， 您 还 有 什 么 想 问 的 吗 ？ ", "third_death_fanlentina_pretalk", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk", [], "你 有 什 么 发 现 ？ ", "third_death_fanlentina_answer_1", []],
  [trp_npc4, "third_death_fanlentina_answer_1", [], "我 去 雾 的 深 处 转 了 一 圈 ， 没 有 发 现 离 开 的 路 。 这 样 的 情 况 我 过 去 也 只 是 有 所 耳 闻 ， 今 天 第 一 次 遇 到 — — 历 史 迷 雾 ， 历 史 中 的 某 一 幕 ， 在 某 种 力 量 的 影 响 下 ， 以 怪 异 扭 曲 的 方 式 展 现 了 出 来 呢 。 ", "third_death_fanlentina_answer_2", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_2", [], "历 史 再 现 ？ 但 扬 尼 克 对 我 们 有 反 应 。 ", "third_death_fanlentina_answer_3", []],
  [trp_npc4, "third_death_fanlentina_answer_3", [], "更 像 是 穿 越 时 空 ， 我 们 被 卷 入 了 历 史 的 乱 流 里 ， 和 过 去 交 织 在 了 一 起 。 据 说 越 是 强 大 的 存 在 能 穿 透 迷 雾 ， 和 闯 入 者 对 话 — — 您 看 ， 只 有 扬 尼 克 村 长 的 头 没 被 迷 雾 遮 挡 。 ", "third_death_fanlentina_answer_4", []],
  [trp_npc4, "third_death_fanlentina_answer_4", [], "据 说 更 强 大 的 人 甚 至 能 意 识 到 自 己 处 在 历 史 迷 雾 之 中 ， 而 普 罗 大 众 则 只 能 留 下 模 糊 的 影 子 ， 正 如 … … 嗯 ， 普 通 人 的 名 字 永 远 不 会 被 记 录 在 史 册 中 一 样 呢 。 ", "third_death_fanlentina_answer_5", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_5", [], "确 实 ， 我 听 其 他 人 说 话 ， 大 多 都 模 糊 不 清 ， 不 明 所 以 ， 除 了 … … ", "third_death_fanlentina_answer_end", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk", [], "我 们 有 办 法 出 去 吗 ？ ", "third_death_fanlentina_answer_6", []],
  [trp_npc4, "third_death_fanlentina_answer_6", [], "很 遗 憾 ， 我 过 去 接 触 到 的 资 料 里 ， 几 乎 没 有 描 述 如 何 脱 离 历 史 迷 雾 的 办 法 ， 毕 竟 案 例 太 少 了 ， 无 法 总 结 哪 类 行 为 才 是 脱 困 的 关 键 。 ", "third_death_fanlentina_answer_7", []],
  [trp_npc4, "third_death_fanlentina_answer_7", [], "而 且 … … 绝 大 多 数 遭 遇 历 史 迷 雾 的 人 ， 可 能 都 死 在 了 雾 里 呢 。 ", "third_death_fanlentina_answer_8", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_8", [], "所 以 我 们 现 在 只 能 等 待 — — 或 者 ， 可 以 试 试 大 肆 破 坏 。 ", "third_death_fanlentina_answer_end", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk", [], "扬 尼 克 说 我 们 是 圣 别 渴 求 者 ， 那 是 什 么 ？ ", "third_death_fanlentina_answer_9", []],
  [trp_npc4, "third_death_fanlentina_answer_9", [], "圣 别 渴 求 者 是 创 世 女 神 教 的 一 个 教 派 ， 成 员 主 要 分 布 在 教 皇 国 的 文 教 系 统 ， 是 一 群 怪 人 。 在 整 个 赤 铜 纪 中 ， 教 皇 国 都 控 制 着 全 部 的 西 大 陆 ， 于 各 地 都 留 下 了 数 不 清 的 教 堂 和 圣 物 ， 当 然 现 在 他 们 已 经 不 行 了 呢 。 圣 别 渴 求 者 试 图 回 收 这 些 古 迹 。 ", "third_death_fanlentina_answer_10", []],
  [trp_npc4, "third_death_fanlentina_answer_10", [], "这 群 人 相 信 只 要 成 天 泡 在 圣 物 堆 里 ， 就 能 把 自 己 也 圣 物 化 ， 原 地 “ 圣 别 ” 升 上 天 国 。 因 此 为 了 达 到 这 个 目 标 ， 这 群 人 可 谓 无 所 不 用 其 极 地 搜 罗 古 物 ， 讨 、 买 、 偷 、 骗 、 抢 ， 走 私 ， 什 么 手 段 都 用 呢 ， 导 致 他 们 的 名 声 臭 不 可 闻 。 ", "third_death_fanlentina_answer_11", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_11", [], "哈 哈 ， 看 来 你 很 鄙 视 他 们 。 ", "third_death_fanlentina_answer_12", []],
  [trp_npc4, "third_death_fanlentina_answer_12", [], "正 常 人 都 该 鄙 视 他 们 呢 。 不 过 理 性 地 说 ， 他 们 也 不 是 十 恶 不 赦 的 坏 人 ， 所 以 只 是 鄙 视 ， 呵 呵 。 ", "third_death_fanlentina_answer_end", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk", [], "关 于 历 史 迷 雾 ， 你 还 知 道 些 什 么 ？ ", "third_death_fanlentina_answer_13", []],
  [trp_npc4, "third_death_fanlentina_answer_13", [], "历 史 迷 雾 这 种 东 西 ， 是 邦 联 的 光 瘴 学 派 研 究 得 最 深 入 ， 他 们 认 为 一 切 迷 雾 的 源 头 都 是 迪 默 巨 沼 泽 中 央 的 旱 湖 。 不 过 ， 因 为 邦 联 人 说 话 喜 欢 故 弄 玄 虚 ， 装 得 高 深 莫 测 ， 玄 而 又 玄 ， 他 们 的 理 论 我 不 是 特 别 了 解 。 ", "third_death_fanlentina_answer_14", []],
  [trp_npc4, "third_death_fanlentina_answer_14", [], "光 瘴 学 士 有 时 候 也 会 往 头 上 顶 一 团 迷 雾 ， 就 像 我 们 看 到 的 这 些 历 史 投 影 一 样 。 不 过 他 们 顶 的 是 白 色 的 。 据 说 那 是 在 历 史 迷 雾 中 安 全 旅 行 的 必 要 手 段 。 ", "third_death_fanlentina_answer_end", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk", [], "关 于 我 的 发 现 … … ", "third_death_fanlentina_answer_15", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_15", [], "我 发 现 有 好 几 个 影 子 ， 都 提 到 了 后 山 。 ", "third_death_fanlentina_answer_16", []],
  [trp_npc4, "third_death_fanlentina_answer_16", [], "加 尔 村 的 后 山 ， 就 是 鬼 哭 崖 了 ， 亦 即 分 割 普 威 尔 地 区 和 戈 兰 尼 尔 低 地 大 平 原 的 天 堑 。 山 中 的 小 道 ， 便 是 两 百 三 十 年 前 普 威 尔 军 奇 袭 罗 德 里 格 斯 王 国 的 道 路 。 ", "third_death_fanlentina_answer_17", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_17", [], "我 有 一 种 感 觉 ， 想 要 脱 离 这 片 迷 雾 ， 就 要 去 山 中 看 看 。 而 且 ， 我 有 一 种 要 开 片 的 预 感 。 范 伦 汀 娜 ， 做 好 准 备 吧 ， 如 果 开 打 了 就 找 个 地 方 躲 起 来 。 ", "third_death_fanlentina_answer_18", []],
  [trp_npc4, "third_death_fanlentina_answer_18", [], "{playername}大 人 ， 请 小 心 。 ", "third_death_fanlentina_answer_end", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk", [], "没 别 的 了 ， 我 们 走 吧 。 ", "close_window", [
    (val_max, "$third_death_quest_phase", 5),
  ]],

  [trp_yannick_village_elder, "start", [
    (eq, "$third_death_quest_phase", 5),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "你 们 怎 么 还 在 ？ ", "third_yannick_village_elder_8", []],
  [trp_yannick_village_elder|plyr, "third_yannick_village_elder_8", [], "鬼 哭 崖 往 哪 里 走 ， 你 能 给 我 指 个 路 吗 ？ ", "third_yannick_village_elder_9", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_9", [], "鬼 哭 崖 ？ 那 是 哪 里 ？ ", "third_yannick_village_elder_10", []],
  [trp_yannick_village_elder|other(trp_npc4), "third_yannick_village_elder_10", [], "{playername}大 人 ， 我 大 概 知 道 现 在 是 什 么 历 史 时 间 段 了 。 戈 兰 尼 尔 低 地 大 平 原 和 普 威 尔 台 地 之 间 的 断 崖 ， 曾 经 有 另 一 个 名 字 ， 直 到 罗 德 里 格 斯 王 国 和 普 威 尔 王 国 的 最 后 一 战 ， 双 方 杀 得 血 流 成 河 ， 这 个 悬 崖 也 被 改 名 为 鬼 哭 崖 。 ", "third_yannick_village_elder_11", []],
  [trp_yannick_village_elder|other(trp_npc4), "third_yannick_village_elder_11", [], "— — 雾 语 崖 ， 村 长 先 生 ， 请 带 我 们 去 雾 语 崖 吧 。 ", "third_yannick_village_elder_12", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_12", [], "你 是 在 说 … … 嗯 … … 行 吧 ， 我 带 你 们 过 去 。 ", "close_window", [
    (assign, "$third_death_quest_phase", 6),
    (mission_disable_talk),
  ]],

  [trp_npc4, "start", [
    (eq, "$third_death_quest_phase", 7),#到达后山
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "前 面 是 不 是 有 什 么 声 音 ？ ", "third_death_player_2", []],
  [trp_npc4|plyr, "third_death_player_2", [], "呆 在 这 别 动 ， 我 进 去 看 看 。 ", "close_window", []],

  [trp_yannick_village_elder, "start", [
    (eq, "$third_death_quest_phase", 9),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "天 哪 ， 这 是 … … 普 威 尔 的 士 兵 ？ ", "third_yannick_village_elder_13", []],
  [trp_yannick_village_elder|plyr, "third_yannick_village_elder_13", [], "你 说 什 — — ", "close_window", [
    (finish_mission),
    (jump_to_menu, "mnu_plot_special_leave"),
  ]],

  [trp_npc4, "event_triggered", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 9),#返回大地图
  ], "不 出 意 料 的 话 ， 刚 才 我 们 经 历 的 ， 就 是 第 五 次 普 罗 战 争 ， 普 威 尔 精 锐 取 道 鬼 哭 崖 的 小 径 ， 奇 袭 罗 德 里 格 斯 王 国 的 历 史 事 件 了 。 更 具 体 一 点 ， 应 该 是 普 威 尔 军 正 在 慢 慢 潜 入 ， 还 未 站 稳 脚 跟 之 时 呢 。 暴 风 来 临 前 的 平 静 。 ", "third_death_fanlentina_10", []],
  [trp_npc4, "third_death_fanlentina_10", [], "{playername}大 人 ， 接 下 来 我 们 该 怎 么 办 ？ ", "third_death_fanlentina_11", []],
  [trp_npc4|plyr, "third_death_fanlentina_11", [], "兹 事 体 大 ， 可 比 什 么 回 收 文 物 重 要 多 了 。 我 们 直 接 去 向 护 枪 官 回 报 … … 或 者 我 们 顺 便 去 把 文 物 拿 了 也 可 以 ？ 不 过 我 觉 得 你 应 该 暂 时 不 想 再 去 加 尔 村 了 。 ", "third_death_fanlentina_12", []],
  [trp_npc4, "third_death_fanlentina_12", [], "呵 呵 ， 大 人 您 已 经 这 么 了 解 我 了 。 ", "close_window", [
    (assign, "$third_death_quest_phase", 10),
  ]],

  [trp_npc4, "event_triggered", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 11),#返回大地图
  ], "{playername}大 人 ， 我 刚 刚 去 查 阅 了 一 下 史 料 。 ", "third_death_fanlentina_13", []],
  [trp_npc4, "third_death_fanlentina_13", [], "传 说 ， 被 普 威 尔 军 收 买 、 为 他 们 指 路 的 是 一 个 贫 穷 的 猎 户 。 而 后 ， 普 威 尔 军 为 急 行 军 做 准 备 ， 掠 夺 了 一 切 能 吃 的 东 西 — — 包 括 人 类 。 旧 加 尔 村 的 男 女 老 少 全 部 被 屠 杀 一 空 ， 葬 身 人 腹 ， 其 中 也 包 括 那 个 内 鬼 。 但 是 更 详 细 的 资 料 就 没 有 了 。 毕 竟 罗 德 里 格 斯 方 的 当 事 人 全 都 身 死 ， 而 普 威 尔 方 也 知 道 此 事 道 义 上 过 不 去 ， 没 有 详 细 记 载 。 ", "third_death_fanlentina_14", []],
  [trp_npc4, "third_death_fanlentina_14", [], "戈 兰 尼 尔 的 吟 游 诗 人 为 这 件 事 写 过 很 多 打 油 诗 ， 我 都 背 得 几 首 ， 比 如 《 猎 人 之 哀 》 ： ^^百 年 之 前 祸 事 殃 ， ^猎 户 引 敌 致 国 亡 。 ^可 怜 身 死 成 口 粮 ， ^耻 辱 悲 哀 岁 月 长 。 ^^往 昔 悲 剧 心 中 藏 ， ^国 破 家 散 泪 汪 汪 。 ^如 今 旧 恨 仍 难 忘 ， ^警 示 后 人 莫 轻 狂 。 ", "third_death_fanlentina_15", []],
  [trp_npc4, "third_death_fanlentina_15", [], "除 此 之 外 ， 我 还 从 民 兵 自 卫 军 的 队 史 中 翻 到 ， 护 枪 官 曾 在 那 个 时 间 段 短 暂 地 造 访 加 尔 村 ， 但 是 从 结 果 上 看 ， 他 应 该 没 有 发 现 普 威 尔 军 的 行 踪 。 这 应 该 就 是 博 蒙 阁 下 说 他 们 曾 有 能 力 阻 止 一 切 的 原 因 了 。 历 史 真 是 由 无 数 巧 合 组 成 的 呢 。 ", "third_death_fanlentina_16", []],
  [trp_npc4|plyr, "third_death_fanlentina_16", [], "要 我 说 的 话 ， 偶 然 性 之 中 一 定 蕴 含 着 某 种 必 然 性 。 ", "close_window", [
    (assign, "$third_death_quest_phase", 12),
  ]],

  [trp_lance_protector_antoine_moro, "start", [
    (eq, "$third_death_quest_phase", 12),#进入场景后
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "等 一 下 ， 那 边 两 位 。 我 是 戈 兰 尼 尔 民 兵 自 卫 军 的 护 枪 官 ， 安 托 万 ·莫 罗 ， 正 在 调 查 一 起 通 敌 案 ， 请 两 位 留 步 配 合 调 查 。 ", "third_death_antoine_moro_1", []],
  [trp_lance_protector_antoine_moro|other(trp_yannick_village_elder), "third_death_antoine_moro_1", [], "安 托 万 ， 这 两 位 是 圣 别 ， 我 是 说 ， 两 位 偶 然 到 此 的 旅 行 者 。 正 是 这 两 位 撞 破 了 普 威 尔 军 的 布 置 , 可 以 信 任 。 ", "third_death_antoine_moro_2", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_2", [], "原 来 如 此 ， 我 了 解 了 。 多 谢 两 位 了 。 民 兵 自 卫 军 接 到 了 扬 尼 克 的 报 案 ， 说 怀 疑 这 个 村 里 有 人 秘 密 为 普 威 尔 军 提 供 协 助 ， 不 知 道 有 什 么 阴 谋 。 据 我 调 查 ， 嫌 犯 就 在 眼 前 这 五 人 之 中 。 ", "third_death_antoine_moro_3", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_3", [], "既 然 普 威 尔 军 是 被 你 们 二 位 发 现 的 ， 可 否 赏 脸 帮 我 分 辨 一 下 ， 他 们 到 底 谁 是 内 奸 ？ ", "third_death_antoine_moro_4", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_4", [], "好 吧 ， 我 和 他 们 谈 谈 。 ", "close_window", [
    (mission_enable_talk),
    (assign, "$third_death_quest_phase", 13),
  ]],

  [trp_yannick_village_elder|plyr, "start", [
    (eq, "$third_death_quest_phase", 13),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "扬 尼 克 先 生 ， 能 不 能 和 我 们 说 说 村 子 里 的 人 ？ ", "third_yannick_village_elder_14", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_14", [], "没 问 题 。 西 里 尔 是 村 庄 的 门 卫 ， 也 是 民 兵 自 卫 军 的 人 。 他 对 村 里 所 有 人 的 行 踪 了 如 指 掌 ， 也 是 能 轻 而 易 举 放 外 人 入 村 的 人 。 ", "third_yannick_village_elder_15", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_15", [], "伊 夫 是 个 普 通 农 民 ， 但 他 总 是 神 神 叨 叨 ， 疯 疯 癫 癫 ， 人 们 说 他 被 恶 魔 附 体 了 。 ", "third_yannick_village_elder_16", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_16", [], "法 比 安 是 从 我 们 村 子 里 走 出 去 的 商 人 ， 据 说 只 用 了 三 年 时 间 就 当 上 了 一 个 商 会 的 商 队 头 领 ， 手 下 有 十 几 号 人 。 不 过 这 些 年 他 在 外 面 打 拼 的 经 历 ， 我 们 几 乎 一 无 所 知 。 ", "third_yannick_village_elder_17", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_17", [], "米 蕾 耶 是 个 寡 妇 ， 靠 着 三 任 亡 夫 的 遗 产 成 为 了 一 个 有 钱 人 ， 有 很 多 不 好 的 传 闻 。 法 比 安 租 用 了 她 的 仓 库 ， 但 是 据 说 被 她 失 手 烧 掉 了 。 这 起 案 件 还 在 调 查 中 。 ", "third_yannick_village_elder_18", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_18", [], "最 后 ， 洛 朗 是 一 个 倒 霉 的 猎 户 ， 因 为 种 种 原 因 几 乎 一 贫 如 洗 ， 几 乎 饿 死 ， 靠 着 我 们 的 接 济 才 能 生 活 。 他 是 对 山 里 的 各 种 兽 径 小 道 最 熟 悉 的 人 。 ", "third_yannick_village_elder_19", []],
  [trp_yannick_village_elder|plyr, "third_yannick_village_elder_19", [], "戈 兰 尼 尔 地 区 不 是 号 称 粮 仓 吗 ？ 为 什 么 他 不 去 种 地 ？ ", "third_yannick_village_elder_20", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_20", [], "唉 ， 罗 德 里 格 斯 王 国 的 粮 种 市 场 ， 五 十 年 前 被 王 室 出 售 给 了 商 会 联 盟 ， 从 此 以 后 ， 他 们 垄 断 了 市 场 ， 低 价 收 购 粮 食 ， 高 价 出 售 种 子 ， 即 使 在 丰 年 ， 农 民 也 要 勒 紧 裤 腰 带 才 能 买 来 足 够 的 种 子 供 来 年 使 用 。 ", "third_yannick_village_elder_21", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_21", [], "对 了 ， 法 比 安 任 职 的 商 会 ， 似 乎 就 是 做 这 个 生 意 的 。 唉 ， 想 当 年 他 们 两 人 还 是 一 起 光 屁 股 长 大 的 ， 一 起 在 山 里 上 蹿 下 跳 的 ， 同 人 不 同 命 啊 。 ", "third_yannick_village_elder_22", []],
  [trp_yannick_village_elder|plyr, "third_yannick_village_elder_22", [], "囤 积 居 奇 ， 王 室 不 管 管 吗 ？ ", "third_yannick_village_elder_23", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_23", [], "据 说 大 前 年 王 室 试 图 收 回 特 许 权 ， 结 果 遭 到 了 商 会 联 盟 的 抗 议 游 行 。 不 过 这 事 是 发 生 在 勒 塞 夫 的 ， 无 论 多 大 的 风 波 ， 传 播 到 我 们 这 个 无 足 轻 重 的 边 陲 小 村 ， 都 只 剩 一 点 风 言 风 语 了 。 ", "third_yannick_village_elder_24", []],
  [trp_yannick_village_elder|plyr, "third_yannick_village_elder_24", [], "原 来 如 此 ， 最 后 ， 扬 尼 克 先 生 ， 能 不 能 说 说 你 自 己 ？ 你 好 想 和 护 枪 官 阁 下 特 别 熟 络 。 ", "third_yannick_village_elder_25", []],
  [trp_yannick_village_elder|other(trp_lance_protector_antoine_moro), "third_yannick_village_elder_25", [], "扬 尼 克 老 师 可 是 我 的 老 上 级 ， 更 是 我 的 授 业 恩 师 。 ", "third_yannick_village_elder_26", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_26", [], "哈 哈 哈 ， 你 的 成 就 早 已 远 远 超 过 我 了 。 你 离 白 金 级 都 只 差 临 门 一 脚 了 ， 而 我 现 在 只 是 个 待 在 小 村 里 养 老 的 老 头 ， 早 已 不 复 当 年 勇 啰 。 ", "third_yannick_village_elder_27", []],
  [trp_yannick_village_elder|other(trp_lance_protector_antoine_moro), "third_yannick_village_elder_27", [], "您 说 笑 了 。 我 和 老 师 以 前 都 是 为 王 室 服 役 的 骑 士 ， 老 师 退 休 后 ， 我 就 申 请 调 去 了 民 兵 自 卫 军 ， 驻 守 在 加 西 亚 领 。 ", "third_yannick_village_elder_28", []],
  [trp_yannick_village_elder|other(trp_npc4), "third_yannick_village_elder_28", [], "加 西 亚 领 … … ", "third_yannick_village_elder_29", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_29", [], "前 线 的 生 活 怎 么 样 ， 苦 不 苦 ？ ", "third_yannick_village_elder_30", []],
  [trp_yannick_village_elder|other(trp_lance_protector_antoine_moro), "third_yannick_village_elder_30", [], "我 倒 觉 得 还 好 。 虽 然 总 是 有 仗 要 打 ， 倒 是 远 离 了 勒 塞 夫 的 尔 虞 我 诈 ， 舒 服 多 了 。 等 以 后 我 也 要 找 个 这 样 的 村 隐 居 。 ", "third_yannick_village_elder_31", []],
  [trp_yannick_village_elder, "third_yannick_village_elder_31", [], "你 说 这 话 还 早 呢 ！ 先 解 决 了 眼 下 的 事 再 说 吧 。 ", "close_window", []],

  [trp_npc4, "start", [
    (eq, "$third_death_quest_phase", 13),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "{playername}大 人 ， 您 有 什 么 看 法 ？ ", "third_death_fanlentina_pretalk_2", []],
  [trp_npc4, "third_death_fanlentina_answer_end_2", [], "您 还 有 什 么 看 法 ？ ", "third_death_fanlentina_pretalk_2", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk_2", [], "关 于 嫌 犯 … … ", "third_death_fanlentina_answer_19", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_19", [], "传 说 中 ， 当 内 鬼 的 是 这 个 猎 户 ， 他 也 确 实 有 动 机 和 条 件 。 但 是 还 有 一 个 人 比 他 更 可 疑 。 ", "third_death_fanlentina_answer_20", []],
  [trp_npc4, "third_death_fanlentina_answer_20", [], "您 是 说 商 队 头 领 ？ ", "third_death_fanlentina_answer_21", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_21", [], "没 错 ， 首 先 ， 普 威 尔 军 需 要 带 路 。 他 和 猎 户 是 一 起 长 大 的 ， 猎 户 能 知 道 的 小 道 ， 他 也 有 可 能 知 道 。 ", "third_death_fanlentina_answer_22", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_22", [], "其 次 ， 普 威 尔 军 需 要 粮 食 ， 而 他 正 是 做 粮 食 生 意 的 。 存 放 货 物 的 仓 库 也 蹊 跷 地 烧 毁 了 ， 就 像 … … 平 账 。 ", "third_death_fanlentina_answer_23", []], 
  [trp_npc4|plyr, "third_death_fanlentina_answer_23", [], "第 三 ， 最 关 键 的 是 ， 按 你 之 前 说 的 ， 越 强 的 人 在 历 史 中 的 回 响 就 越 清 晰 。 村 长 和 护 枪 官 能 和 我 们 对 话 ， 是 因 为 他 们 有 黑 金 级 往 上 的 实 力 ； 精 选 民 兵 能 说 的 话 比 农 民 农 妇 猎 人 都 多 ， 因 为 他 有 白 银 级 ； 但 是 ， 一 个 商 队 头 领 ， 却 是 这 五 人 中 唯 一 一 个 说 话 没 有 任 何 模 糊 的 。 ", "third_death_fanlentina_answer_24", []],
  [trp_npc4, "third_death_fanlentina_answer_24", [], "他 在 隐 藏 实 力 … … 甚 至 ， 他 可 能 也 已 意 识 到 我 们 了 ， 只 是 在 伪 装 。 想 到 这 一 层 真 是 有 些 让 人 有 些 脊 背 发 凉 呢 。 ", "third_death_fanlentina_answer_end_2", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk_2", [], "关 于 商 会 … … ", "third_death_fanlentina_answer_25", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_25", [], "关 于 商 队 头 领 的 动 机 ， 他 做 这 件 事 大 概 是 他 上 级 的 命 令 。 商 会 联 盟 想 要 无 限 制 地 扩 大 商 业 版 图 ， 而 王 室 想 要 收 回 特 许 权 ， 双 方 的 冲 突 ， 使 得 商 会 被 普 威 尔 人 秘 密 收 买 。 ", "third_death_fanlentina_answer_26", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_26", [], "法 比 安 在 商 会 中 平 步 青 云 ， 大 概 也 是 因 为 他 出 生 在 旧 加 尔 村 ， 对 鬼 哭 崖 足 够 了 解 ， 在 关 键 时 刻 能 充 当 棋 子 。 ", "third_death_fanlentina_answer_27", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_27", [], "这 就 是 我 说 的 ， 历 史 的 偶 然 背 后 是 必 然 。 没 有 加 尔 村 的 法 比 安 ， 商 会 也 会 推 出 卡 尔 村 的 嘎 比 安 ， 拉 尔 村 的 哈 比 安 。 大 敌 当 前 仍 在 内 斗 ， 这 就 是 罗 德 里 格 斯 王 国 走 向 灭 亡 的 必 然 原 因 。 ", "third_death_fanlentina_answer_28", []],
  [trp_npc4, "third_death_fanlentina_answer_28", [], "您 说 的 是 呢 … … 受 教 了 。 ", "third_death_fanlentina_answer_end_2", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk_2", [], "关 于 谬 史 … … ", "third_death_fanlentina_answer_29", []],
  [trp_npc4|plyr, "third_death_fanlentina_answer_29", [], "有 一 个 很 严 肃 的 问 题 ， 如 果 我 们 在 谬 史 中 改 变 了 历 史 的 走 向 ， 现 实 会 发 生 改 变 吗 ？ ", "third_death_fanlentina_answer_30", []],
  [trp_npc4, "third_death_fanlentina_answer_30", [], "不 知 道 呢 。 据 我 所 知 过 去 并 没 有 发 生 过 这 样 的 案 例 ， 但 是 ， 谁 知 道 我 们 的 史 书 、 我 们 的 记 载 ， 我 们 的 — — 记 忆 ， 不 是 已 经 被 改 变 过 了 的 呢 ？ ", "third_death_fanlentina_answer_end_2", []],
  [trp_npc4|plyr, "third_death_fanlentina_pretalk_2", [], "没 有 别 的 问 题 了 。  ", "close_window", []],

  [trp_lance_protector_antoine_moro, "start", [
    (eq, "$third_death_quest_phase", 13),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "如 何 ？ 两 位 旅 行 者 ， 我 想 听 听 你 们 的 意 见 。 ", "third_death_antoine_moro_5", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_5", [], "我 有 头 绪 了 。 ", "third_death_antoine_moro_6", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_5", [], "再 等 等 。 ", "close_window", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_6", [], "我 觉 得 ， 幕 后 黑 手 是 … … ", "third_death_antoine_moro_7", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_7", [], "猎 户 。 ", "third_death_antoine_moro_8", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_7", [], "商 人 。 ", "third_death_antoine_moro_8", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_7", [], "寡 妇 。 ", "third_death_antoine_moro_8", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_7", [], "农 民 。 ", "third_death_antoine_moro_8", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_7", [], "民 兵 。 ", "third_death_antoine_moro_8", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_8", [], "猎 户 （ 商 人 ）  ", "third_death_antoine_moro_9", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_9", [], "… … ？  ", "third_death_antoine_moro_10", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_10", [], "您 也 是 这 么 认 为 的 啊 ， 那 么 就 … … ", "third_death_antoine_moro_11", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_11", [], "等 等 ， 我 是 说 — — ", "third_death_antoine_moro_12", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_12", [], "商 人 。 ", "third_death_antoine_moro_13", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_12", [], "猎 户 。 ", "third_death_antoine_moro_13", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_13", [], "猎 户 （ 商 人 ） ", "third_death_antoine_moro_14", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_14", [], "（ 怎 么 回 事 ？ ） ", "third_death_antoine_moro_15", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_15", [], "您 看 起 来 脸 色 不 太 对 劲 ， 是 不 是 需 要 再 考 虑 一 下 ？ 或 者 休 息 一 下 ？ 我 和 老 师 反 正 也 要 再 讨 论 一 下 。 ", "third_death_antoine_moro_16", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_16", [], "我 … … 我 是 说 … … ", "third_death_antoine_moro_17", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_17", [], "猎 户 。 ", "third_death_antoine_moro_18", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_18", [], "… … ！ ", "third_death_antoine_moro_19", [
    (display_message, "@你 的 话 语 被 某 种 回 声 盖 住 了 。 细 细 听 来 ， 那 是 两 百 余 年 间 不 断 传 唱 的 历 史 、 故 事 、 歌 谣 、 传 说 。 一 切 杂 乱 的 声 音 ， 汇 聚 为 了 那 首 《 猎 人 之 歌 》 — — 此 时 此 刻 ， 你 似 乎 理 解 了 一 切 ： 何 为 … … "),
    (display_message, "@“ 谬 史 ” ", 0xFF0000),
  ]],
  [trp_lance_protector_antoine_moro|other(trp_npc4), "third_death_antoine_moro_19", [], "{playername}大 人 ， 您 刚 才 … … 是 被 什 么 力 量 影 响 了 吗 ？ ", "third_death_antoine_moro_20", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_20", [], "看 来 是 的 ， 大 概 是 谬 史 发 力 了 … … 不 过 无 妨 ， 看 我 直 接 攻 击 他 ！ ", "third_death_antoine_moro_21", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_21", [], "你 干 什 么 ！ 等 等 ， 这 是 龙 血 的 力 量 。 法 比 安 ， 你 从 哪 里 得 到 的 龙 血 ？ ", "close_window", [
    (assign, "$third_death_quest_phase", 14),
    (mission_disable_talk),
    (show_object_details_overlay, 0),
    (reset_mission_timer_c),
    (assign, "$g_film_state", 1),
    (assign, "$g_film_cam", 1),
    (mission_cam_set_mode, 1),
  ]],

  [trp_lance_protector_antoine_moro, "start", [
    (eq, "$third_death_quest_phase", 15),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "为 了 力 量 ， 饮 下 龙 血 ， 成 为 怪 物 ， 这 是 普 威 尔 的 狂 徒 才 会 做 的 事 。 而 且 龙 血 补 剂 都 是 普 威 尔 军 方 的 管 制 品 。 看 来 他 的 确 是 投 靠 普 威 尔 人 了 。 ", "third_death_antoine_moro_22", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_22", [], "旅 行 者 ， 我 还 得 感 谢 你 识 破 了 他 的 阴 谋 。 现 在 我 必 须 尽 快 回 报 ， 让 大 军 搜 山 了 … … （ 模 糊 不 清 ） ", "third_death_antoine_moro_23", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_23", [], "等 等 ， 你 之 后 会 去 哪 里 ？ ", "third_death_antoine_moro_24", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_24", [], "我 ？ 之 后 我 会 去 — — ", "close_window", [
    (finish_mission),
    (jump_to_menu, "mnu_plot_special_leave"),
  ]],

  [trp_npc4, "event_triggered", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 15),#返回大地图
  ], "刚 刚 发 生 了 什 么 ， 我 们 … … 改 变 了 历 史 ？ ", "third_death_fanlentina_17", []],
  [trp_npc4|plyr, "third_death_fanlentina_17", [], "难 说 。 最 简 单 的 验 证 方 法 ， 我 们 去 找 个 吟 游 诗 人 问 问 ， 看 他 们 还 记 不 记 得 那 首 猎 人 之 歌 吧 。 ", "close_window", [
    (str_store_string, s2, "@在 谬 史 中 你 们 揪 出 了 真 凶 ， 斩 杀 了 内 鬼 ， 现 实 的 历 史 或 许 会 因 此 而 大 不 相 同 。 去 酒 馆 寻 找 吟 游 诗 人 加 以 求 证 。 "),
    (add_quest_note_from_sreg, "qst_third_death", 6, s2, 0),
    (display_message, "str_quest_log_updated"),
    (assign, "$third_death_quest_phase", 16),
  ]],

  [trp_npc4, "event_triggered", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 17),#返回大地图
  ], "我 们 的 历 史 并 未 发 生 改 变 ， 不 知 是 不 幸 还 是 幸 事 。 ", "third_death_fanlentina_18", []],
  [trp_npc4, "third_death_fanlentina_18", [], "看 来 ， 谬 史 说 到 底 也 只 是 历 史 长 河 中 偶 然 的 一 个 漩 涡 ， 它 无 法 阻 止 水 流 向 它 们 的 应 去 的 方 向 。 我 们 能 通 过 谬 史 改 变 的 ， 大 概 也 只 有 我 们 自 己 的 阅 历 了 。 ", "third_death_fanlentina_19", []],
  [trp_npc4|plyr, "third_death_fanlentina_19", [], "说 到 这 个 ， 到 最 后 我 们 也 没 能 知 道 安 托 万 ·莫 罗 和 他 的 枪 最 终 去 了 哪 里 。 ", "third_death_fanlentina_20", []],
  [trp_npc4, "third_death_fanlentina_20", [], "而 且 ， 谬 史 中 历 史 的 走 向 已 经 改 变 了 ， 他 有 很 大 概 率 不 会 死 在 第 五 次 普 罗 战 争 中 ， 已 经 没 有 参 考 意 义 了 。 ", "third_death_fanlentina_21", []],
  [trp_npc4|plyr, "third_death_fanlentina_21", [], "知 天 易 ， 逆 天 难 啊 。 我 们 回 去 向 护 枪 官 复 命 吧 。 ", "close_window", [
    (str_store_string, s2, "@猜 想 得 到 验 证 ， 现 在 是 回 去 向 护 枪 官 报 告 的 时 候 了 。 "),
    (add_quest_note_from_sreg, "qst_third_death", 7, s2, 0),
    (display_message, "str_quest_log_updated"),
    (assign, "$third_death_quest_phase", 18),
  ]],

  [trp_npc4, "event_triggered", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 19),#返回大地图
  ], "{playername}大 人 ， 您 的 决 定 是 什 么 ？ ", "third_death_fanlentina_22", [
    (assign, "$third_death_quest_phase", 20),
  ]],
  [trp_npc4|plyr, "third_death_fanlentina_22", [], "我 觉 得 ， 未 必 没 有 一 试 的 价 值 — — 当 然 并 不 是 和 安 托 万 ·莫 罗 战 斗 ， 何 况 就 算 打 也 大 概 打 不 赢 。 ", "third_death_fanlentina_23", []],
  [trp_npc4, "third_death_fanlentina_23", [], "您 是 想 说 ， 和 他 谈 谈 ？ ", "third_death_fanlentina_24", []],
  [trp_npc4|plyr, "third_death_fanlentina_24", [], "没 错 。 既 然 谬 史 不 会 改 变 现 在 ， 那 么 无 论 谬 史 中 的 他 有 没 有 肖 像 枪 ， 对 于 真 实 历 史 中 的 他 的 结 局 ， 以 及 现 在 的 一 切 ， 都 不 会 有 改 变 。 跟 他 说 说 民 兵 自 卫 军 的 现 状 ， 我 觉 得 他 会 理 解 的 。 ", "third_death_fanlentina_25", []],
  [trp_npc4|plyr, "third_death_fanlentina_25", [], "而 如 果 拿 到 了 枪 却 无 法 带 出 谬 史 ， 那 我 们 也 算 仁 至 义 尽 了 。 ", "third_death_fanlentina_26", []],
  [trp_npc4, "third_death_fanlentina_26", [], "这 个 办 法 不 错 呢 。 不 过 ， 我 还 有 要 说 的 。 ", "third_death_fanlentina_27", []],
  [trp_npc4, "third_death_fanlentina_27", [], "关 于 丰 收 女 神 肖 像 枪 ， 以 及 所 有 这 些 超 凡 神 物 。 您 觉 不 觉 得 ， 博 蒙 阁 下 已 经 有 点 … … 失 常 了 ？ ", "third_death_fanlentina_28", []],
  [trp_npc4|plyr, "third_death_fanlentina_28", [], "他 或 许 只 是 太 累 了 。 ", "third_death_fanlentina_29", []],
  [trp_npc4, "third_death_fanlentina_29", [], "我 还 有 一 种 解 释 呢 。 我 看 过 很 多 书 ， 其 中 不 乏 英 雄 人 物 与 传 奇 之 物 的 故 事 ， 比 如 勇 者 拔 出 了 圣 剑 ， 骑 士 发 现 了 圣 杯 ， 学 者 钻 研 出 了 玄 奥 的 理 论 ， 盗 墓 贼 打 开 了 尘 封 已 久 的 地 宫 等 等 — — 所 有 这 些 人 ， 他 们 的 落 幕 都 不 会 太 好 。 ", "third_death_fanlentina_30", []],
  [trp_npc4, "third_death_fanlentina_30", [], "一 切 超 凡 的 、 神 圣 的 、 伟 大 的 、 玄 妙 的 事 物 ， 人 们 以 为 自 己 在 追 求 它 们 ， 实 则 是 它 们 在 追 逐 人 类 。 ", "third_death_fanlentina_31", []],
  [trp_npc4, "third_death_fanlentina_31", [], "其 残 酷 无 情 ， 一 如 鹰 犬 追 猎 野 兔 。 ", "close_window", []],

  [trp_lance_protector_antoine_moro, "start", [
    (eq, "$third_death_quest_phase", 20),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_third_death"),
  ], "是 你 们 二 位 啊 。 ", "third_death_antoine_moro_25", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_25", [], "莫 罗 阁 下 ， 怎 么 就 剩 你 一 个 人 了 ， 其 他 人 去 哪 里 了 ？ ", "third_death_antoine_moro_26", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_26", [], "… … … … ", "third_death_antoine_moro_27", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_27", [], "告 诉 我 真 相 ， 两 位 。 我 现 在 是 在 幻 境 里 ？ 抑 或 在 阴 间 ？ 还 是 … … 谬 史 ？", "third_death_antoine_moro_28", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_28", [], "你 居 然 自 己 发 现 了 啊 。 不 错 ， 对 于 我 们 而 言 ， 你 已 经 是 二 百 三 十 年 前 的 人 了 。 ", "third_death_antoine_moro_29", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_29", [], "那 么 … … 未 来 之 人 ， 告 诉 我 结 局 吧 。 我 们 … … 是 不 是 输 了 ？ ", "third_death_antoine_moro_30", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_30", [], "是 的 ， 罗 德 里 格 斯 王 室 投 降 了 普 威 尔 人 ， 现 在 是 普 威 尔 王 国 下 的 一 个 附 属 公 国 。 ", "third_death_antoine_moro_31", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_31", [], "是 吗 ？ 那 么 ， 我 有 没 有 奋 战 到 最 后 ？ ", "third_death_antoine_moro_32", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_32", [], "你 英 勇 作 战 ， 凭 一 己 之 力 杀 死 了 近 千 敌 军 ， 拖 住 普 威 尔 军 主 力 数 小 时 ， 力 竭 而 死 。 直 到 今 天 ， 戈 兰 尼 尔 民 兵 自 卫 军 还 以 你 为 荣 。 ", "third_death_antoine_moro_33", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_33", [], "我 还 做 出 了 这 么 英 勇 的 事 情 吗 ？ 哈 哈 哈 ， 那 倒 是 也 死 而 无 憾 了 。 而 且 那 群 小 崽 子 居 然 在 两 百 年 后 还 存 在 ？ 他 们 现 状 怎 么 样 ？ 在 普 威 尔 人 的 统 治 下 过 得 不 太 好 吧 。 ", "third_death_antoine_moro_34", []],
  [trp_lance_protector_antoine_moro|other(trp_npc4), "third_death_antoine_moro_34", [], "很 艰 难 ， 但 是 还 算 是 能 够 继 续 生 存 。 另 外 不 得 不 面 对 的 现 实 是 ， 自 认 为 是 罗 德 里 格 斯 人 的 人 已 经 越 来 越 少 了 。 大 多 数 人 在 对 外 自 称 时 都 会 说 自 己 是 普 威 尔 人 ， 或 者 至 少 是 联 合 王 国 人 。 ", "third_death_antoine_moro_35", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_35", [], "这 样 吗 … … 唉 ， 这 或 许 也 是 没 有 办 法 的 事 情 。 我 这 一 个 古 代 人 ， 就 不 去 替 你 们 操 心 了 。 ", "third_death_antoine_moro_36", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_36", [], "感 觉 你 们 告 诉 我 这 么 多 。 相 应 的 ， 我 也 该 为 你 们 做 些 事 情 ， 比 如 ， 你 们 似 乎 很 在 乎 丰 收 女 神 肖 像 枪 ？ ", "third_death_antoine_moro_37", []],
  [trp_lance_protector_antoine_moro|plyr, "third_death_antoine_moro_37", [], "是 的 ， 我 们 就 是 受 现 任 护 枪 官 之 托 ， 前 来 取 肖 像 枪 的 。 在 你 战 死 之 后 ， 你 的 尸 体 和 肖 像 枪 就 一 起 消 失 了 。 护 枪 官 觉 得 ， 或 许 能 从 缪 史 中 着 手 。 ", "third_death_antoine_moro_38", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_38", [], "连 枪 都 没 了 ， 现 在 的 自 卫 军 也 够 落 魄 的 。 不 过 很 可 惜 ， 我 也 不 知 道 未 来 的 “ 我 ” 会 去 到 哪 里 。 但 … … 既 然 现 在 肖 像 枪 就 在 我 手 上 ， 或 许 可 以 试 试 直 接 交 给 你 。 ", "third_death_antoine_moro_39", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_38", [], "… … 真 是 一 个 疯 狂 的 想 法 ， 要 是 能 从 历 史 中 随 意 带 出 物 品 ， 那 岂 不 是 可 以 有 无 数 的 神 器 、 不 死 的 军 队 、 无 限 的 生 命 ？ 不 过 ， 如 果 有 一 个 神 祇 能 司 掌 时 间 ， 那 祂 确 实 应 该 有 如 此 伟 力 吧 。 ", "third_death_antoine_moro_39", []],
  [trp_lance_protector_antoine_moro, "third_death_antoine_moro_39", [], "肖 像 枪 给 你 ， 拿 好 了 — — ", "close_window", [
    (finish_mission),
    (jump_to_menu, "mnu_plot_special_leave"),
  ]],

  [trp_npc11, "start", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 22),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_village_1_12"),
  ], "总 算 来 了 。 可 让 我 们 好 等 。 ", "third_death_lilian_1", []],
  [trp_npc11, "third_death_lilian_1", [], "我 是 丽 莲 ， 是 — — ", "close_window", [
    (start_mission_conversation, "trp_village_1_12_elder"),
  ]],

  [trp_village_1_12_elder, "start", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 22),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_village_1_12"),
  ], "这 位 就 是 我 们 请 来 的 挖 坟 专 家 。 ", "third_death_lilian_2", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_2", [], "哈 ？ 我 那 么 多 头 衔 你 就 只 报 这 一 个 ， 难 道 我 是 什 么 盗 墓 贼 ？ 我 是 个 博 物 学 家 ， 国 立 龙 学 院 和 白 泉 城 大 学 联 盟 的 客 座 教 授 ， 普 威 尔 王 立 研 究 院 和 斯 嘉 丽 秘 研 院 的 荣 誉 研 究 员 ， 现 在 是 元 素 游 侠 和 公 爵 的 宫 廷 科 学 家 。 ", "third_death_lilian_3", []],
  [trp_village_1_12_elder|plyr, "third_death_lilian_3", [
    (troop_set_slot, "$g_talk_troop", slot_troop_met_previously, 1),#记录见面
  ], "你 好 ， 我 是 {playername}。 ", "third_death_lilian_4", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_4", [], "你 的 身 体 有 一 种 让 我 想 … … 解 剖 你 的 冲 动 ， 咳 ， 不 过 算 了 ， 今 天 不 说 这 个 了 。 ", "third_death_lilian_5", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_5", [], "啊 ， 终 于 挖 通 了 ！ ", "third_death_lilian_6", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_6", [], "我 看 看 … … 慢 着 ， 这 是 ！ ", "third_death_lilian_7", []],
  [trp_village_1_12_elder|plyr, "third_death_lilian_7", [], "丰 收 女 神 肖 像 枪 … … ", "third_death_lilian_8", []],
  [trp_village_1_12_elder, "third_death_lilian_8", [], "不 对 ， 不 对 ， 神 枪 怎 么 会 在 我 们 加 尔 村 ？ 护 枪 官 安 托 万 ·莫 罗 战 死 的 地 方 距 我 们 这 里 几 百 公 里 远 ， 而 且 当 时 旧 加 尔 村 的 人 都 死 绝 了 ， 谁 会 来 给 他 收 尸 呢 ？ ", "third_death_lilian_9", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_9", [], "而 且 这 个 坟 墓 里 还 雕 刻 了 丰 收 女 神 纹 样 的 图 案 ， 这 种 形 式 的 墓 葬 在 普 威 尔 取 胜 后 就 被 废 弃 了 。 这 至 少 能 说 明 两 个 问 题 ， 一 是 这 个 墓 的 建 成 时 间 不 会 晚 于 1200年 ， 二 是 他 是 被 厚 葬 的 。 ", "third_death_lilian_10", []],
  [trp_village_1_12_elder|plyr, "third_death_lilian_10", [], "可 能 是 后 人 所 为 吗 ？ ", "third_death_lilian_11", []],
  [trp_village_1_12_elder, "third_death_lilian_11", [], "这 个 墓 是 之 前 天 降 大 雨 ， 山 体 滑 坡 ， 才 被 我 们 发 现 的 ， 之 前 一 直 被 埋 在 这 座 小 山 底 下 。 不 过 谁 知 道 呢 ？ 知 识 分 子 ， 有 没 有 什 么 说 法 ？ ", "third_death_lilian_12", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_12", [], "要 我 说 ， 这 东 西 可 能 两 百 年 来 一 直 在 这 里 ， 也 可 能 不 是 。 ", "third_death_lilian_13", []],
  [trp_village_1_12_elder|plyr, "third_death_lilian_13", [], "听 君 一 席 话 ， 如 听 一 席 话 啊 。 ", "third_death_lilian_14", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_14", [], "错 错 错 。 你 们 知 道 什 么 叫 “ 虚 妄 的 古 物 ” 吗 ？ 有 时 候 ， 一 支 箭 可 能 在 同 一 时 刻 射 中 了 两 个 相 隔 千 里 的 人 ， 三 台 断 头 台 砍 下 了 同 一 个 国 王 的 脑 袋 ， 前 10世 纪 的 人 陪 葬 在 前 2世 纪 的 坟 墓 里 ， 成 为 孤 例 的 文 物 指 向 一 个 从 未 在 任 何 史 册 中 出 现 过 的 国 度 … … 这 一 切 被 称 为 “ 谬 史 ” 。 时 间 线 越 是 往 前 ， 谬 史 的 迷 雾 就 越 浓 。 ", "third_death_lilian_15", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_15", [], "所 以 在 考 古 界 有 这 么 一 句 话 ： “ 畏 惧 历 史 吧 。 探 究 历 史 ， 就 是 凝 视 深 渊 。 ” ", "third_death_lilian_16", []],
  [trp_village_1_12_elder, "third_death_lilian_16", [], "什 么 牛 屎 羊 屎 的 ， 不 就 是 挖 坟 没 挖 明 白 找 的 借 口 吗 ？ ", "third_death_lilian_17", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_17", [
    (call_script, "script_troop_add_item_with_modifier_new", "trp_player", "itm_harvest_goddess_portrait_lance", 0, 0, 0),#丰收女神肖像枪
  ], "是 是 是 ， 你 还 是 先 搞 明 白 怎 么 让 你 的 儿 子 继 承 骑 士 爵 位 吧 。 总 之 呢 ， 这 把 枪 就 给 你 了 ， 护 枪 官 让 你 带 点 文 物 回 去 ， 你 直 接 把 枪 给 他 了 ， 这 下 他 不 高 兴 得 飞 起 来 ？ ", "third_death_lilian_18", []],
  [trp_village_1_12_elder|other(trp_npc11), "third_death_lilian_18", [], "你 要 自 己 偷 偷 留 着 我 也 没 意 见 ， 不 过 这 是 从 世 俗 的 角 度 讲 。 而 从 神 秘 学 的 角 度 讲 ， 我 是 不 会 建 议 你 这 么 干 的 。 ", "close_window", [
    (assign, "$third_death_quest_phase", 23),
    (str_store_string, s2, "@肖 像 枪 以 一 种 荒 谬 的 方 式 来 到 了 你 的 手 中 。 从 逻 辑 上 讲 ， 你 们 直 接 等 到 丽 莲 挖 开 坟 墓 也 能 得 到 它 ， 但 是 经 历 了 三 次 谬 史 ， 你 的 感 性 却 给 出 了 不 同 的 看 法 。 无 论 如 何 ， 现 在 你 应 该 把 枪 交 给 护 枪 官 ， 得 到 他 的 重 谢 和 友 谊 了 … … 或 者 ， 你 也 可 以 自 己 保 留 ？ "),
    (add_quest_note_from_sreg, "qst_third_death", 9, s2, 0),
    (display_message, "str_quest_log_updated"),
    (assign, "$g_mission_allow_leave", 0),#允许离开
  ]],

  [trp_npc11, "start", [
    (check_quest_active, "qst_third_death"),
    (eq, "$third_death_quest_phase", 23),
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_village_1_12"),
  ], "还 有 别 的 事 吗 ？ 我 们 要 把 所 有 这 些 文 物 、 壁 画 通 通 拆 走 ， 还 有 的 忙 呢 。 不 然 就 为 圣 别 渴 求 者 做 嫁 衣 了 。 ", "third_death_lilian_19", []],
  [trp_npc11|plyr, "third_death_lilian_19", [], "没 别 的 事 了 ， 再 见 。 ", "third_death_lilian_20", []],
  [trp_npc11, "third_death_lilian_20", [], "我 们 肯 定 会 再 见 面 的 … … 呵 呵 。 ", "close_window", []],

  [trp_npc19|plyr, "event_triggered", [
    (check_quest_active, "qst_third_death"),#支线剧情：第三个死
    (eq, "$third_death_quest_phase", 23),
    (eq, "$portrait_lance_corrosion", 15),#未归还肖像枪超过15天
  ], "你 是 那 个 … … 梅 薇 丝 ？ 什 么 风 把 你 吹 来 了 ？ ", "third_death_mayvis_1", []],
  [trp_npc19, "third_death_mayvis_1", [], "我 来 是 为 了 肖 像 枪 的 事 … … 丰 收 女 神 肖 像 枪 。 ", "third_death_mayvis_2", []],
  [trp_npc19, "third_death_mayvis_2", [], "哎 呀 … … 一 条 时 枢 竟 然 因 这 种 东 西 陨 落 了 ， 真 是 世 事 难 料 啊 。 言 尽 于 此 ， 我 先 告 辞 了 。 ", "third_death_mayvis_3", []],
  [trp_npc19|plyr, "third_death_mayvis_3", [], "什 么 谜 语 人 ？ 喂 ， 把 话 说 清 楚 啊 ！ ", "close_window", [
    (assign, "$portrait_lance_corrosion", 16),
  ]],




#######################################################日常对话#####################################################
####
###——————————————————————————————大地图相关——————————————————————————————-
##
  [anyone, "start", [
    (eq, "$talk_context", tc_party_encounter),#大地图遭遇
    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_kingdom_hero_party), #领主部队
    (neq, "$g_encountered_party_faction", "$players_kingdom"), #不是玩家领主
    (faction_get_slot, ":party_culture", "$g_encountered_party_faction", slot_faction_culture), #获取文化
    (item_slot_eq, ":party_culture", slot_culture_messenger_troop, "$g_talk_troop"), #信使
    (party_stack_get_troop_id, ":lord_troop_no", "$g_encountered_party", 0), #获取领队
    (str_store_faction_name, s10, "$g_encountered_party_faction"),
    (str_store_troop_name, s11, ":lord_troop_no"),

    (try_begin),
       (eq, "$encountered_party_friendly", 1), #关系超过50，友好
       (str_store_string, s3, "@很 高 兴 见 到 您 ， {playername}阁 下 。 {s11}阁 下 欢 迎 您 前 去 一 叙 。 "),
    (else_try),
       (ge, "$g_encountered_party_relation", 0), #不敌对，且玩家只是一个小人物
       (troop_get_slot, ":renown_no", "trp_player", slot_troop_renown), 
       (lt, ":renown_no", 2000), #声望少于两千
       (store_character_level, ":level_no", "trp_player"),
       (lt, ":level_no", 50), #不到山铜级
       (str_store_string, s3, "@我 是 {s10}{s11}阁 下 的 使 者 ， 陌 生 人 ， 请 说 明 你 的 来 意 。"),
    (else_try),
       (ge, "$g_encountered_party_relation", 0), #不敌对，玩家略有实力
       (str_store_string, s3, "@您 好 ， {playername}阁 下 。 我 是 {s10}{s11}阁 下 的 使 者 ， 请 问 您 有 何 贵 干 ？ "),
    (else_try),
       (eq, "$encountered_party_hostile", 1), #敌对，玩家被攻击
       (encountered_party_is_attacker),
       (str_store_string, s3, "@我 代 表 {s10}的 {s11}而 来 。 投 降 吧 ， 我 们 会 给 你 一 个 体 面 的 死 法 。 "),
    (else_try),
       (eq, "$encountered_party_hostile", 1), #敌对，玩家主动攻击
       (str_store_string, s3, "@我 代 表 {s10}的 {s11}而 来 。 告 诉 我 你 的 目 的 ， 乞 降 ， 还 是 领 死 ？ "),
    (try_end),
  ], "{s3}", "faction_messenger_encounter_talk_begin", []],

#友好
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (eq, "$encountered_party_friendly", 1), #友好
  ], "好 的 ， 我 正 有 些 事 需 要 详 谈 。 ", "close_window", [
    (eq,"$talk_context", tc_party_encounter),
    (assign, "$g_start_campaign", "itm_formation_station"), #开始摆阵
    (assign, "$g_lord_talk", 2), #在军营会面
  ]],
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (eq, "$encountered_party_friendly", 1), #友好
  ], "谢 谢 你 们 的 好 意 ， 但 今 天 不 行 ， 改 日 吧 。 ", "faction_messenger_encounter_talk_1", []],
  [anyone, "faction_messenger_encounter_talk_1", [], "那 太 可 惜 了 ， 再 见 ， {playername}阁 下 。 我 们 随 时 恭 候 您 的 大 驾 。 ", "close_window", [
    (eq,"$talk_context", tc_party_encounter),
    (assign, "$g_leave_encounter", 1), #可以离开
  ]],

#陌生
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (neq, "$encountered_party_friendly", 1), 
    (ge, "$g_encountered_party_relation", 0), #不敌对
  ], "我 想 见 {s11}， 你 能 为 我 引 路 吗 ？ ", "faction_messenger_encounter_talk_2", []],
  [anyone, "faction_messenger_encounter_talk_2", [
    (troop_get_slot, ":renown_no", "trp_player", slot_troop_renown), 
    (store_character_level, ":level_no", "trp_player"),
    (this_or_next|ge, ":renown_no", 2000), #声望少于两千或达到山铜级
    (ge, ":level_no", 50), 
  ], "没 问 题 ， 跟 我 来 吧 ， 我 会 将 您 带 到 {s11}阁 下 的 面 前 。 不 过 ， 您 只 能 一 个 人 前 往 ， 而 且 不 能 携 带 武 器 。 ", "close_window", [
    (eq,"$talk_context", tc_party_encounter),
    (assign, "$g_lord_talk", 1), #简单会面
  ]],
  [anyone, "faction_messenger_encounter_talk_2", [], "{s11}阁 下 是 很 忙 的 ， 每 天 试 图 在 阁 下 面 前 露 脸 的 人 多 如 牛 毛 ， 阻 拦 他 们 也 是 我 的 职 责 所 在 … … 你 有 什 么 事 要 见 阁 下 ， 跟 我 说 吧 ， 我 会 酌 情 转 达 ， 或 者 直 接 帮 你 处 理 。 ", "faction_messenger_encounter_talk_3", []],
  [anyone|plyr, "faction_messenger_encounter_talk_3", [], "我 暂 时 没 什 么 要 事 ， 打 扰 了 。 ", "close_window", [
    (eq,"$talk_context", tc_party_encounter),
    (assign, "$g_leave_encounter", 1), #可以离开
  ]],

  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (neq, "$encountered_party_friendly", 1), 
    (ge, "$g_encountered_party_relation", 0), #不敌对
  ], "没 事 ， 只 是 路 过 … … ", "close_window", [
    (eq,"$talk_context", tc_party_encounter),
    (assign, "$g_leave_encounter", 1), #可以离开
  ]],

#敌对，攻击玩家
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (eq, "$encountered_party_hostile", 1), #敌对，玩家被攻击
    (encountered_party_is_attacker),
  ], "废 话 少 说 ， 告 诉 你 的 主 子 吧 ， 今 日 就 是 你 死 我 活 之 时 ！ ", "close_window", [
    (assign, "$g_start_campaign", "itm_formation_common"), #开始摆阵
  ]],
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (eq, "$encountered_party_hostile", 1), #敌对，玩家被攻击
    (encountered_party_is_attacker),
  ], "别 打 我 ， 我 们 投 降 … … ", "close_window", [
    (assign,"$g_player_surrenders",1),
  ]],

#敌对，玩家主动攻击
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (eq, "$encountered_party_hostile", 1), #敌对，玩家主动攻击
    (neg|encountered_party_is_attacker),
  ], "回 去 告 诉 你 的 主 子 ， 今 天 就 是 你 们 的 死 期 ！ ", "close_window", [
    (assign, "$g_start_campaign", "itm_formation_common"), #开始摆阵
  ]],
  [anyone|plyr, "faction_messenger_encounter_talk_begin", [
    (eq, "$encountered_party_hostile", 1), #敌对，玩家主动攻击
    (neg|encountered_party_is_attacker),
  ], "回 去 告 诉 你 们 的 主 子 ， 我 会 宰 了 你 们 ， 但 不 是 今 天 。 ", "close_window", [
    (eq,"$talk_context", tc_party_encounter),
    (assign, "$g_leave_encounter", 1), #可以离开
  ]],








###——————————————————————————————冒险者协会——————————————————————————————-
##
  [anyone, "start", [
    (neg|troop_is_hero, "$g_talk_troop"),#小兵
    (neq, "$g_talk_troop", "trp_association_examiner"),#不是协会考官
    (eq, "$current_building", "itm_adventurer_station"),#在协会建筑里
    (store_current_scene, ":cur_scene"),
    (eq, ":cur_scene", "scn_adventurer_station_1"),
  ], "有 什 么 事 ？ ", "adventurer_station_recuit_1", []],
  [anyone|plyr, "adventurer_station_recuit_1", [], "我 正 在 寻 找 冒 险 者 加 入 我 的 队 伍 。 ", "adventurer_station_recuit_2", []],
  [anyone|plyr, "adventurer_station_recuit_1", [], "没 事 ， 再 见 。 ", "close_window", []],
  [anyone, "adventurer_station_recuit_2", [
    (store_random_in_range, ":count_no", 1, 100),#招募有一定概率，后续可能会根据玩家声望修正
    (gt, ":count_no", 60),
    (store_character_level, ":level_no", "$g_talk_troop"),
    (val_div, ":level_no", 10),
    (ge, "$player_adventuror_level", ":level_no"),#玩家冒险者等阶大于等于对方才能招募
    (val_add, ":level_no", 1),
    (val_mul, ":level_no", ":level_no"),
    (store_mul, "$temp", ":level_no", 50),
    (assign, reg10, "$temp"),
  ], "我 有 别 的 事 ， 但 我 有 个 朋 友 可 以 会 为 你 效 力 的 。 不 过 在 那 之 前 ， 按 照 行 业 惯 例 ， 你 要 付 {reg10}的 开 拨 费 。 ", "adventurer_station_recuit_3", []],
  [anyone, "adventurer_station_recuit_2", [], "恐 怕 不 行 ， 不 太 合 适 。 ", "close_window", []],
  [anyone|plyr, "adventurer_station_recuit_3", [
    (store_troop_gold, ":gold_count", "trp_player"),
    (ge, ":gold_count", "$temp"),
  ], "可 以 ， 告 诉 他 收 拾 东 西 ， 准 备 动 身 吧 。 ", "close_window", [
    (party_add_members, "p_main_party", "$g_talk_troop", 1),
  ]],
  [anyone|plyr, "adventurer_station_recuit_3", [], "我 考 虑 一 下 。 ", "close_window", []],
]