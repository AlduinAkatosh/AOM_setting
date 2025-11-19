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


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


scripts_map = [

#获取当前自然环境，返回在s10里。返回更进一步细分的地面类型，大部分不会变，但小部分比如沼泽会更改，返回进reg1，用于会战地图等位置
  ("get_natural_zone", [   #use for get natural area name
        (store_script_param, ":map_x", 1),
        (store_script_param, ":map_y", 2),
        (store_script_param, ":current_terrain", 3),
        (str_clear, s10),
             (try_begin),
                (this_or_next|eq, ":current_terrain", rt_water),#sea
                (eq, ":current_terrain", 0xB0E2FF),
                (try_begin),
                   (le, ":map_x", -320000),
                   (str_store_string, s10, "@尽 头 洋 "),#End Sea
                (else_try),
                   (ge, ":map_x", 345000),
                   (le, ":map_y", 210000),
                   (str_store_string, s10, "@沧 澜 洋 "),#Canglan Sea
                (else_try),
                   (ge, ":map_x", 283000),
                   (gt, ":map_y", 210000),
                   (str_store_string, s10, "@飘 零 洋 "),#Piaoling Sea
                (else_try),
                   (ge, ":map_x", 217000),
                   (gt, ":map_y", 48000),
                   (str_store_string, s10, "@帝 庭 内 海 "),#Diting Sea
                (else_try),
                   (ge, ":map_x", 264000),
                   (gt, ":map_y", -53000),
                   (str_store_string, s10, "@汐 海 "),#Xi Sea
                (else_try),
                   (ge, ":map_x", 247000),
                   (str_store_string, s10, "@千 帆 海 岸 "),#Qianfan Coast
                (else_try),
                   (le, ":map_x", -270000),
                   (gt, ":map_y", 270000),
                   (str_store_string, s10, "@极 雾 海 岸 "),#Jiwu Sea
                (else_try),
                   (gt, ":map_y", 118000),
                   (str_store_string, s10, "@无 光 海 岸 "),#Dark Coast
                (else_try),
                   (gt, ":map_y", 0),
                   (str_store_string, s10, "@噬 人 湾 "),#Man-eater Gulf
                (else_try),
                   (gt, ":map_y", -150000),
                   (str_store_string, s10, "@信 风 湾 "),#Trade-wind Gulf
                (else_try),
                   (str_store_string, s10, "@绝 迹 海 "),#Jueji Sea
                (try_end),
             (else_try),
                (assign, ":continue", 0),
                (try_begin),
                   (this_or_next|eq, ":current_terrain", rt_river),
                   (eq, ":current_terrain", rt_bridge),
                   (assign, ":continue", 1),
                (else_try),
                   (this_or_next|eq, ":current_terrain", 0x0080FF),
                   (eq, ":current_terrain", 0x808080),
                   (assign, ":continue", 1),
                (try_end),
                (eq, ":continue", 1),
                (try_begin),
                   (is_between, ":map_x", -174000, -114000),
                   (is_between, ":map_y", -186000, -155000),
                   (str_store_string, s10, "@龙 饮 湖 "),#Dragon_drink Lake
                (else_try),
                   (le, ":map_x", -189000),
                   (le, ":map_y", -306000),
                   (str_store_string, s10, "@逆 生 湖 "),#Rebirth Lake
                (else_try),
                   (is_between, ":map_x", 16000, 75000),
                   (is_between, ":map_y", -252000, -100000),
                   (str_store_string, s10, "@米 德 湖 "),#Midul Lake
                (else_try),
                   (is_between, ":map_x", 196000, 270000),
                   (is_between, ":map_y", -264000, -202000),
                   (str_store_string, s10, "@洪 明 湖 "),#Hongming Lake
                (else_try),
                   (is_between, ":map_x", -102000, -71000),
                   (is_between, ":map_y", 86000, 123000),
                   (str_store_string, s10, "@光 栖 湖 "),#Guangqi Lake
                (else_try),
                   (is_between, ":map_x", -296000, -211000),
                   (is_between, ":map_y", 191000, 256000),
                   (str_store_string, s10, "@迪 默 巨 沼 泽 "),#Diemer Marsh
                (else_try),
                   (le, ":map_x", -143000),
                   (is_between, ":map_y", 82000, 219000),
                   (str_store_string, s10, "@迪 默 巨 沼 泽 "),#Diemer Marsh
                (else_try),
                   (le, ":map_x", -109000),
                   (is_between, ":map_y", 82000, 184000),
                   (str_store_string, s10, "@迪 默 巨 沼 泽 "),#Diemer Marsh
                (else_try),
                   (le, ":map_x", -21000),
                   (le, ":map_y", -11000),
                   (str_store_string, s10, "@奔 流 河 "),#Flowing River
                (else_try),
                   (ge, ":map_x", 148000),
                   (le, ":map_y", -182000),
                   (str_store_string, s10, "@洞 江 "),#Dojiang River
                (else_try),
                   (le, ":map_y", -228000),
                   (str_store_string, s10, "@咆 哮 河 "),#Roaring River
                (else_try),
                   (le, ":map_x", 55000),
                   (le, ":map_y", -31000),
                   (str_store_string, s10, "@圣 迁 溪 "),#Saint Stream
                (else_try),
                   (le, ":map_x", 90000),
                   (le, ":map_y", 23000),
                   (str_store_string, s10, "@南 巡 河 "),#South Inspection River
                (else_try),
                   (ge, ":map_x", 115000),
                   (le, ":map_y", -49000),
                   (str_store_string, s10, "@桃 江 "),#Taojiang River
                (else_try),
                   (ge, ":map_x", 166000),
                   (ge, ":map_y", 176000),
                   (str_store_string, s10, "@削 山 江 "),#Xiaoshanjiang River
                (else_try),
                   (ge, ":map_x", 291000),
                   (str_store_string, s10, "@度 江 "),#Dujiang River
                (else_try),
                   (ge, ":map_x", 84000),
                   (str_store_string, s10, "@浩 河 "),#Haohe River
                (else_try),
                   (str_store_string, s10, "@流 冰 河 "),#Iceflow River
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_desert),
                (eq, ":current_terrain", 0xBDB76B),
                (try_begin),
                   (le, ":map_x", -256000),
                   (le, ":map_y", -286000),
                   (str_store_string, s10, "@埋 葬 漠 "),#Burying Desert
                   (assign, ":current_terrain", rt_desert_mountain),
                (else_try),
                   (le, ":map_x", -196000),
                   (le, ":map_y", -330000),
                   (str_store_string, s10, "@无 归 漠 "),#Unreturnable Desert
                (else_try),
                   (ge, ":map_x", -221000),
                   (le, ":map_y", -316000),
                   (str_store_string, s10, "@入 漠 戈 壁 "),#Entrance Gobi Desert
                   (assign, ":current_terrain", rt_desert_mountain),
                (else_try),
                   (le, ":map_y", -316000),
                   (str_store_string, s10, "@生 机 漠 "),#Life Desert
                (else_try),
                   (str_store_string, s10, "@科 鲁 托 沙 漠 "),#Kouruto Desert
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_steppe),
                (eq, ":current_terrain", 0x9ACD32),
                (try_begin),
                   (le, ":map_x", 64000),
                   (le, ":map_y", -320000),
                   (str_store_string, s10, "@南 科 鲁 托 草 原 回 廊 "),#South Kouruto Corridor
                   (assign, ":current_terrain", rt_steppe_mountain),
                (else_try),
                   (ge, ":map_x", 99000),
                   (le, ":map_y", -315000),
                   (str_store_string, s10, "@天 源 山 高 山 草 甸 带 "),#Mount Tianyuan Grassy Marshland
                (else_try),
                   (ge, ":map_x", 103000),
                   (str_store_string, s10, "@西 南 草 原 "),#Southwest Steppe
                (else_try),
                   (ge, ":map_x", 50000),
                   (str_store_string, s10, "@咆 哮 河 下 游 草 原 "),#Southcost of Roaring River Steppe
                (else_try),
                   (is_between, ":map_x", -294000, -248000),
                   (is_between, ":map_y", -84000, -44000),
                   (str_store_string, s10, "@孟 那 米 尔 台 地 "),#Monamir Horst
                   (assign, ":current_terrain", rt_steppe_mountain),
                (else_try),
                   (ge, ":map_x", 34000),
                   (ge, ":map_y", -236000),
                   (str_store_string, s10, "@米 德 湖 畔 草 原 "),#Midul Lakeshore Steppe
                (else_try),
                   (str_store_string, s10, "@科 鲁 托 草 原 "),#Kouruto Steppe
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_snow),
                (eq, ":current_terrain", 0xFFFFF0),
                (try_begin),
                   (ge, ":map_x", 191000),
                   (ge, ":map_y", 335000),
                   (str_store_string, s10, "@不 释 冰 域 "),#Bushibing Land
                (else_try),
                   (is_between, ":map_x", 72000, 145000),
                   (ge, ":map_y", 274000),
                   (str_store_string, s10, "@皓 雪 境 "),#Haoxue Land
                (else_try),
                   (ge, ":map_x", 81000),
                   (ge, ":map_y", 194000),
                   (str_store_string, s10, "@常 寒 雪 国 "),#Changhan Snowland
                (else_try),
                   (ge, ":map_x", 10000),
                   (ge, ":map_y", 305000),
                   (str_store_string, s10, "@死 冻 冰 谷 "),#Death Icevalley
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (is_between, ":map_x", -58000, -21000),
                   (ge, ":map_y", 328000),
                   (str_store_string, s10, "@冰 蚀 谷 "),#Ice Erosion Valley
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (is_between, ":map_x", -174000, -58000),
                   (ge, ":map_y", 325000),
                   (str_store_string, s10, "@寒 霜 谷 "),#Frost Valley
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (is_between, ":map_x", -255000, -178000),
                   (ge, ":map_y", 337000),
                   (str_store_string, s10, "@冰 棺 盆 地 "),#Ice Tomb Basin
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (le, ":map_x", -217000),
                   (le, ":map_y", -361000),
                   (str_store_string, s10, "@雪 之 尽 头 "),#Endless of Snow
                (else_try),
                   (str_store_string, s10, "@伊 希 斯 雪 国 "),#Snowland of Yishith
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_mountain),
                (eq, ":current_terrain", 0xCDC1C5),
                (try_begin),
                   (is_between, ":map_x", -331000, -282000),
                   (is_between, ":map_y", -296000, -261000),
                   (str_store_string, s10, "@第 二 环 脉 山 系 - 归 还 山 "),#The Second Annulus Mountain System Mountain Return
                (else_try),
                   (is_between, ":map_x", -247000, -201000),
                   (is_between, ":map_y", -308000, -271000),
                   (str_store_string, s10, "@入 漠 戈 壁 "),#Entrance Gobi Desert
                (else_try),
                   (is_between, ":map_x", -248000, -104000),
                   (is_between, ":map_y", -287000, -242000),
                   (str_store_string, s10, "@第 二 环 脉 山 系 - 隔 断 山 "),#The Second Annulus Mountain System Mountain Interdiction
                (else_try),
                   (is_between, ":map_x", -196000, -144000),
                   (is_between, ":map_y", -236000, -189000),
                   (str_store_string, s10, "@索 尔 丘 "),#Mountain Thol
                (else_try),
                   (is_between, ":map_x", -86000, -28000),
                   (is_between, ":map_y", -300000, -242000),
                   (str_store_string, s10, "@孟 那 米 尔 台 地 "),#Monamir Horst
                (else_try),
                   (is_between, ":map_x", -10000, 20000),
                   (is_between, ":map_y", -306000, -241000),
                   (str_store_string, s10, "@草 原 地 垒 "),#Platform of Steppe
                (else_try),
                   (is_between, ":map_x", -47000, 49000),
                   (is_between, ":map_y", -379000, -317000),
                   (str_store_string, s10, "@南 科 鲁 托 回 廊 "),#South Kouruto Corridor
                (else_try),
                   (is_between, ":map_x", -105000, 8000),
                   (is_between, ":map_y", -234000, -195000),
                   (str_store_string, s10, "@第 二 环 脉 山 系 - 科 鲁 托 草 原 门 户 山 脉 "),#The Second Annulus Mountain System Entrance of Kouruto Steppe
                (else_try),
                   (is_between, ":map_x", 12000, 36000),
                   (is_between, ":map_y", -209000, -187000),
                   (str_store_string, s10, "@米 德 高 岩 "),#Midul Highrock
                (else_try),
                   (is_between, ":map_x", 87000, 123000),
                   (is_between, ":map_y", -321000, -281000),
                   (str_store_string, s10, "@第 二 环 脉 山 系 - 尽 头 龙 树 山 脉 "),#The Second Annulus Mountain System End of Longshu Mountain
                (else_try),
                   (is_between, ":map_x", 56000, 136000),
                   (is_between, ":map_y", -275000, -102000),
                   (str_store_string, s10, "@第 二 环 脉 山 系 - 南 龙 树 山 脉 "),#The Second Annulus Mountain System South Longshu Mountain
                (else_try),
                   (is_between, ":map_x", 55000, 143000),
                   (is_between, ":map_y", -102000, 0),
                   (str_store_string, s10, "@第 一 环 脉 山 系 - 中 龙 树 山 脉 "),#The First Annulus Mountain System Middle Longshu Mountain
                (else_try),
                   (is_between, ":map_x", 44000, 87000),
                   (is_between, ":map_y", 0, 60),
                   (str_store_string, s10, "@第 一 环 脉 山 系 - 外 龙 树 山 脉 "),#The First Annulus Mountain System Extra Longshu Mountain
                (else_try),
                   (is_between, ":map_x", 45000, 74000),
                   (is_between, ":map_y", 67000, 98000),
                   (str_store_string, s10, "@雪 望 峰 "),#Peak Snowview
                (else_try),
                   (is_between, ":map_x", 45000, 99000),
                   (is_between, ":map_y", 86000, 128000),
                   (str_store_string, s10, "@圣 巴 托 洛 谬 山 "),#Mountain Saint Bartholomew
                (else_try),
                   (is_between, ":map_x", 143000, 168000),
                   (is_between, ":map_y", -34000, -5000),
                   (str_store_string, s10, "@龙 侍 山 "),#Peak Longshi
                (else_try),
                   (is_between, ":map_x", 72000, 155000),
                   (is_between, ":map_y", 0, 143000),
                   (str_store_string, s10, "@第 二 环 脉 山 系 - 北 龙 树 山 脉 "),#The Second Annulus Mountain System North Longshu Mountain
                (else_try),
                   (is_between, ":map_x", 42000, 79000),
                   (is_between, ":map_y", 194000, 224000),
                   (str_store_string, s10, "@落 叶 山 "),#Mountain Abscission
                (else_try),
                   (is_between, ":map_x", -60000, 184000),
                   (is_between, ":map_y", 172000, 246000),
                   (str_store_string, s10, "@林 中 断 崖 "),#Forest Cliff
                (else_try),
                   (is_between, ":map_x", 37000, 141000),
                   (is_between, ":map_y", 143000, 286000),
                   (str_store_string, s10, "@龙 椅 山 "),#The Second Annulus Mountain System North Longshu Mountain
                (else_try),
                   (is_between, ":map_x", 154000, 197000),
                   (is_between, ":map_y", 147000, 223000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 新 山 "),#Longyi Mountain
                (else_try),
                   (is_between, ":map_x", 273000, 305000),
                   (is_between, ":map_y", 221000, 239000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 断 山 "),#The Third Annulus Mountain System Xin Mountain
                (else_try),
                   (is_between, ":map_x", 305000, 345000),
                   (is_between, ":map_y", 208000, 221000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 神 笔 山 "),#The Third Annulus Mountain System Duan Mountain
                (else_try),
                   (is_between, ":map_x", 333000, 355000),
                   (is_between, ":map_y", 70000, 119000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 维 辉 山 "),#The Third Annulus Mountain System Shenbi Mountain
                (else_try),
                   (is_between, ":map_x", 292000, 325000),
                   (is_between, ":map_y", 67000, 100000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 雨 雾 山 "),#The Third Annulus Mountain System Weihui Mountain
                (else_try),
                   (is_between, ":map_x", 311000, 341000),
                   (is_between, ":map_y", 14000, 55000),
                   (str_store_string, s10, "@江 右 山 "),#The Third Annulus Mountain System Yuwu Mountain
                (else_try),
                   (is_between, ":map_x", 252000, 274000),
                   (is_between, ":map_y", 65000, 83000),
                   (str_store_string, s10, "@绵 山 "),#Jiangyou Mountain
                (else_try),
                   (is_between, ":map_x", 232000, 272000),
                   (is_between, ":map_y", -8000, 26000),
                   (str_store_string, s10, "@坚 山 "),#Mian Mountain
                (else_try),
                   (is_between, ":map_x", 242000, 260000),
                   (is_between, ":map_y", -28000, -12000),
                   (str_store_string, s10, "@青 郁 山 "),#Jian Mountain
                (else_try),
                   (is_between, ":map_x", 190000, 212000),
                   (is_between, ":map_y", 0, 23000),
                   (str_store_string, s10, "@青 郁 山 "),#Qingyu Mountian
                (else_try),
                   (is_between, ":map_x", 185000, 216000),
                   (is_between, ":map_y", -22000, -3000),
                   (str_store_string, s10, "@烛 山 "),#Zhu Mountian
                (else_try),
                   (is_between, ":map_x", 167000, 191000),
                   (is_between, ":map_y", 43000, 72000),
                   (str_store_string, s10, "@罗 山"),#Luo Mountian
                (else_try),
                   (is_between, ":map_x", 287000, 306000),
                   (is_between, ":map_y", -153000, -109000),
                   (str_store_string, s10, "@铜 羊 山 "),#Tongyang Mountian
                (else_try),
                   (is_between, ":map_x", 255000, 305000),
                   (is_between, ":map_y", -197000, -160000),
                   (str_store_string, s10, "@虾 弓 山 "),#Xiagong Mountian
                (else_try),
                   (is_between, ":map_x", 232000, 254000),
                   (is_between, ":map_y", -142000, -108000),
                   (str_store_string, s10, "@上 齐 山 "),#Shang Qi Mountian
                (else_try),
                   (is_between, ":map_x", 213000, 241000),
                   (is_between, ":map_y", -192000, -144000),
                   (str_store_string, s10, "@下 齐 山 "),#Xia Qi Mountian
                (else_try),
                   (is_between, ":map_x", 149000, 210000),
                   (is_between, ":map_y", -199000, -147000),
                   (str_store_string, s10, "@聚 义 山 "),#Juyi Mountian
                (else_try),
                   (is_between, ":map_x", 163000, 176000),
                   (is_between, ":map_y", -134000, -122000),
                   (str_store_string, s10, "@室 女 姊 丘 "),#Shinvzi Mountian
                (else_try),
                   (is_between, ":map_x", 145000, 163000),
                   (is_between, ":map_y", -142000, -134000),
                   (str_store_string, s10, "@室 女 妹 丘 "),#Shinvmei Mountian
                (else_try),
                   (is_between, ":map_x", 126000, 193000),
                   (is_between, ":map_y", -370000, -300000),
                   (str_store_string, s10, "@囚 门 山 "),#Qiumen Mountian
                (else_try),
                   (is_between, ":map_x", 202000, 258000),
                   (is_between, ":map_y", -334000, -304000),
                   (str_store_string, s10, "@金 墙 山 "),#Jinqiang Mountian
                (else_try),
                   (le, ":map_y", -250000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 南 方 荒 漠 诸 山 "),#The Third Annulus Mountain System South Mountains
                (else_try),
                   (is_between, ":map_x", -48000, -20000),
                   (is_between, ":map_y", -182000, -146000),
                   (str_store_string, s10, "@卫 士 山 "),#Protection Mountian
                (else_try),
                   (is_between, ":map_x", -96000, 25000),
                   (is_between, ":map_y", -138000, -93000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 圣 诺 伯 托 山 脉 "),#The First Annulus Mountain System Saint Norberto Mountain
                (else_try),
                   (is_between, ":map_x", -2000, 28000),
                   (is_between, ":map_y", -42000, 13000),
                   (str_store_string, s10, "@世 界 山 "),#The World Mountain
                (else_try),
                   (is_between, ":map_x", -111000, -68000),
                   (is_between, ":map_y", -75000, -40000),
                   (str_store_string, s10, "@第 一 环 脉 山 系 - 龙 愁 山 脉 "),#The First Annulus Mountain System Dragonworry Mountain
                (else_try),
                   (is_between, ":map_x", -139000, -49000),
                   (is_between, ":map_y", -33000, 58000),
                   (str_store_string, s10, "@龙 息 山 地 "),#Dragon Inhabitation Mountainland
                (else_try),
                   (is_between, ":map_x", -57000, -38000),
                   (is_between, ":map_y", 134000, 153000),
                   (str_store_string, s10, "@第 一 环 脉 山 系 - 圣 唐 纳 琳 山 "),#The First Annulus Mountain System Saint Donnalyn Mountain
                (else_try),
                   (is_between, ":map_x", -111000, -16000),
                   (is_between, ":map_y", 62000, 143000),
                   (str_store_string, s10, "@第 一 环 脉 山 系 - 安 基 亚 山 脉 "),#The First Annulus Mountain System Ankiya Mountain
                (else_try),
                   (is_between, ":map_x", -142000, -84000),
                   (is_between, ":map_y", 158000, 240000),
                   (str_store_string, s10, "@南 伊 希 斯 山 脉 "),#South Yixith Mountain
                (else_try),
                   (is_between, ":map_x", -174000, -108000),
                   (is_between, ":map_y", 17000, 130000),
                   (str_store_string, s10, "@悲 泣 高 崖 "),#Mourngelith Cliff
                (else_try),
                   (is_between, ":map_x", -53000, -145000),
                   (is_between, ":map_y", -195000, -19000),
                   (str_store_string, s10, "@双 牙 峰 "),#Bicuspid Mountain
                (else_try),
                   (is_between, ":map_x", -23000, -5000),
                   (is_between, ":map_y", -278000, -227000),
                   (str_store_string, s10, "@脊 梁 山 脉 "),#Spine Mountain
                (else_try),
                   (is_between, ":map_x", -324000, -292000),
                   (is_between, ":map_y", -26000, 33000),
                   (str_store_string, s10, "@第 三 环 脉 山 系 - 枕 涛 山 "),#The Third Annulus Mountain System Wave-pillow Mountain
                (else_try),
                   (is_between, ":map_x", -169000, -134000),
                   (is_between, ":map_y", -147000, -121000),
                   (str_store_string, s10, "@普 威 尔 山 "),#Powell Mountain
                (else_try),
                   (is_between, ":map_x", -227000, -199000),
                   (is_between, ":map_y", -153000, -114000),
                   (str_store_string, s10, "@鬼 哭 崖 "),#Ghostcry Cliff
                (else_try),
                   (is_between, ":map_x", -312000, -279000),
                   (is_between, ":map_y", -179000, -137000),
                   (str_store_string, s10, "@黎 明 山 "),#Dawn Mountain
                (else_try),
                   (is_between, ":map_x", -159000, -77000),
                   (is_between, ":map_y", 310000, 344000),
                   (str_store_string, s10, "@苦 寒 山 脉 "),#Bitter Cold Mountain
                (else_try),
                   (is_between, ":map_x", 308000, 334000),
                   (is_between, ":map_y", -6000, 16000),
                   (str_store_string, s10, "@厄 兆 山 "),#Ominous Peak
                (else_try),
                   (is_between, ":map_x", -248000, -224000),
                   (is_between, ":map_y", 291000, 304000),
                   (str_store_string, s10, "@血 根 山 "),#Blood Forest Mountain
                (else_try),
                   (ge, ":map_y", 302000),
                   (str_store_string, s10, "@第 一 环 脉 山 系 - 北 境 冰 川 诸 山 "),#The Third Annulus Mountain System North Mountains
                (else_try),
                   (is_between, ":map_x", -21000, 28000),
                   (is_between, ":map_y", 132000, 158000),
                   (str_store_string, s10, "@第 一 环 脉 诸 山 - 盾 墙 山 "),#The First Annulus Mountain Shield wall Mountains
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_forest),
                (eq, ":current_terrain", 0x006400),
                (try_begin),
                   (le, ":map_x", -303000),
                   (le, ":map_y", -250000),
                   (str_store_string, s10, "@近 漠 树 林 "),#Near-desert Forest
                (else_try),
                   (le, ":map_x", -314000),
                   (is_between, ":map_y", -225000, -208000),
                   (str_store_string, s10, "@勒 塞 夫 林 场 "),#Lesaff Forest
                (else_try),
                   (le, ":map_x", -264000),
                   (le, ":map_y", -228000),
                   (str_store_string, s10, "@索 恩 德 林 场 "),#Souende Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -231000),
                   (le, ":map_y", -201000),
                   (str_store_string, s10, "@石 根 树 林 "),#Stonebone Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -281000),
                   (le, ":map_y", -192000),
                   (str_store_string, s10, "@多 拉 科 河 畔 树 林 "),#Dorack Forest
                (else_try),
                   (le, ":map_x", -215000),
                   (le, ":map_y", -223000),
                   (str_store_string, s10, "@春 尽 森 林 "),#Springend Forest
                (else_try),
                   (le, ":map_x", -199000),
                   (le, ":map_y", -191000),
                   (str_store_string, s10, "@格 罗 弗 树 林 "),#Gloff Forest
                (else_try),
                   (le, ":map_x", -124000),
                   (le, ":map_y", -198000),
                   (str_store_string, s10, "@索 尔 丘 山 区 森 林 "),#Thol Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -256000),
                   (le, ":map_y", -169000),
                   (str_store_string, s10, "@河 岸 森 林 "),#Riverside Forest
                (else_try),
                   (le, ":map_x", -295000),
                   (le, ":map_y", -128000),
                   (str_store_string, s10, "@黎 明 山 森 林 "),#Dawn Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -205000),
                   (le, ":map_y", -113000),
                   (str_store_string, s10, "@古 战 场 森 林 "),#Old battlefield Forest
                (else_try),
                   (le, ":map_x", -98000),
                   (le, ":map_y", -223000),
                   (str_store_string, s10, "@科 鲁 托 草 原 入 口 森 林 "),#Entrance Forest of Kouruto Steppe
                (else_try),
                   (le, ":map_x", -105000),
                   (le, ":map_y", -178000),
                   (str_store_string, s10, "@埋 剑 森 林 "),#Sword Burried Forest
                (else_try),
                   (le, ":map_x", -162000),
                   (le, ":map_y", -130000),
                   (str_store_string, s10, "@普 威 尔 国 立 林 场 "),#Kingdom Forest
                (else_try),
                   (le, ":map_x", -60000),
                   (le, ":map_y", -165000),
                   (str_store_string, s10, "@断 崖 森 林 "),#Cliff Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -53000),
                   (le, ":map_y", -119000),
                   (str_store_string, s10, "@东 普 威 尔 树 林 "),#East Powell Forest
                (else_try),
                   (le, ":map_x", -91000),
                   (le, ":map_y", -83000),
                   (str_store_string, s10, "@北 山 麓 树 林 "),#Northside Mountain Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -171000),
                   (le, ":map_y", -31000),
                   (str_store_string, s10, "@布 兰 登 大 森 林 "),#Blanden Forest
                (else_try),
                   (le, ":map_x", -285000),
                   (le, ":map_y", 35000),
                   (str_store_string, s10, "@枕 涛 山 麓 树 林 "),#Wave-pillow Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -253000),
                   (le, ":map_y", 4000),
                   (str_store_string, s10, "@脊 梁 山 山 林 "),#Spine Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -159000),
                   (le, ":map_y", 77000),
                   (str_store_string, s10, "@岩 底 树 林 "),#Stone button Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -106000),
                   (le, ":map_y", 60000),
                   (str_store_string, s10, "@南 安 基 亚 森 林 "),#South Ankiya Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -5000),
                   (le, ":map_y", -144000),
                   (str_store_string, s10, "@卫 士 山 树 林 "),#Protection Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 22000),
                   (le, ":map_y", -140000),
                   (str_store_string, s10, "@米 德 森 林 "),#Midul Forest
                (else_try),
                   (le, ":map_x", 17000),
                   (le, ":map_y", -76000),
                   (str_store_string, s10, "@巴 罗 内 大 森 林 "),#Barroney Forest
                (else_try),
                   (le, ":map_x", -8000),
                   (le, ":map_y", 57000),
                   (str_store_string, s10, "@龙 境 大 山 林 "),#Dragonland Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -136000),
                   (le, ":map_y", 225000),
                   (str_store_string, s10, "@沼 泽 稀 树 林 "),#Marsh Forest
                   (assign, ":current_terrain", rt_marsh),
                (else_try),
                   (le, ":map_x", -286000),
                   (le, ":map_y", 280000),
                   (str_store_string, s10, "@灾 生 林 "),#Disaster Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -253000),
                   (le, ":map_y", 363000),
                   (str_store_string, s10, "@西 进 守 卫 森 林 "),#West Wachter Forest
                (else_try),
                   (le, ":map_x", -69000),
                   (le, ":map_y", 129000),
                   (str_store_string, s10, "@北 安 基 亚 森 林 "),#North Ankiya Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 144000),
                   (le, ":map_y", -136000),
                   (str_store_string, s10, "@南 龙 树 山 脉 森 林 "),#South Longshu Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 78000),
                   (le, ":map_y", -20000),
                   (str_store_string, s10, "@圣 溪 树 林 "),#Saint River Forest
                (else_try),
                   (le, ":map_x", 252000),
                   (le, ":map_y", -330000),
                   (str_store_string, s10, "@孽 兽 林 "),#Evil Monster Forest
                (else_try),
                   (le, ":map_x", 277000),
                   (le, ":map_y", -280000),
                   (str_store_string, s10, "@南 方 森 林 "),#South Forest
                (else_try),
                   (le, ":map_x", 165000),
                   (le, ":map_y", -219000),
                   (str_store_string, s10, "@平 州 林 场 "),#Pingzhou Forest
                (else_try),
                   (le, ":map_x", 280000),
                   (le, ":map_y", -227000),
                   (str_store_string, s10, "@洞 湖 湖 畔 森 林 "),#Donghu Forest
                (else_try),
                   (le, ":map_x", 208000),
                   (le, ":map_y", -168000),
                   (str_store_string, s10, "@聚 义 山 林 "),#Juyi Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 120000),
                   (le, ":map_y", -47000),
                   (str_store_string, s10, "@三 千 里 森 林 "),#Sanqianli Forest
                (else_try),
                   (le, ":map_x", 188000),
                   (le, ":map_y", -112000),
                   (str_store_string, s10, "@双 丘 山 林 "),#Shuangqiu Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 215000),
                   (le, ":map_y", -136000),
                   (str_store_string, s10, "@聚 义 山 林 "),#Juyi Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 263000),
                   (le, ":map_y", -104000),
                   (str_store_string, s10, "@齐 山 林 "),#Qishan Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 324000),
                   (le, ":map_y", -103000),
                   (str_store_string, s10, "@东 山 森 林 "),#East Mountain Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 171000),
                   (le, ":map_y", -28000),
                   (str_store_string, s10, "@江 源 大 森 林 "),#Jiangyuan Forest
                (else_try),
                   (le, ":map_x", 223000),
                   (le, ":map_y", -29000),
                   (str_store_string, s10, "@桃 江 流 域 森 林 "),#Taojiang Forest
                (else_try),
                   (le, ":map_x", 303000),
                   (le, ":map_y", -55000),
                   (str_store_string, s10, "@三 角 洲 林 场 "),#Sanjiaozhou Forest
                (else_try),
                   (le, ":map_x", 123000),
                   (le, ":map_y", 98000),
                   (str_store_string, s10, "@外 省 山 林 "),#Outer Province Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 168000),
                   (le, ":map_y", 34000),
                   (str_store_string, s10, "@锡 林 "),#Xilin Forest
                (else_try),
                   (le, ":map_x", 168000),
                   (le, ":map_y", 34000),
                   (str_store_string, s10, "@罗 山 山 林 "),#Luoshan Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 284000),
                   (le, ":map_y", 33000),
                   (str_store_string, s10, "@新 月 山 林 "),#Xinyue Mountain Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -62000),
                   (le, ":map_y", 213000),
                   (str_store_string, s10, "@血 战 森 林 "),#Battlefield Forest
                (else_try),
                   (le, ":map_x", 43000),
                   (le, ":map_y", 178000),
                   (str_store_string, s10, "@新 生 林 "),#Newbirth Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -1000),
                   (le, ":map_y", 239000),
                   (str_store_string, s10, "@悲 风 森 林 "),#Northwind Forest
                (else_try),
                   (le, ":map_x", 50000),
                   (le, ":map_y", 279000),
                   (str_store_string, s10, "@行 踪 林 "),#Footstep Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 85000),
                   (le, ":map_y", 169000),
                   (str_store_string, s10, "@木 盐 森 林 "),#Tree Salt Forest
                (else_try),
                   (le, ":map_x", 93000),
                   (le, ":map_y", 269000),
                   (str_store_string, s10, "@山 谷 森 林 "),#Valley Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 298000),
                   (ge, ":map_y", 197000),
                   (str_store_string, s10, "@双 山 森 林 "),#Two Mountain Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 298000),
                   (ge, ":map_y", 172000),
                   (str_store_string, s10, "@海 角 树 林 "),#Haijiao Forest
                (else_try),
                   (ge, ":map_x", 263000),
                   (ge, ":map_y", 243000),
                   (str_store_string, s10, "@尚 州 林 场 "),#Shangzhou Forest
                (else_try),
                   (ge, ":map_x", 183000),
                   (ge, ":map_y", 173000),
                   (str_store_string, s10, "@京 畿 林 场 "),#Jinji Forest
                (else_try),
                   (ge, ":map_x", 245000),
                   (ge, ":map_y", 92000),
                   (str_store_string, s10, "@浩 河 入 海 口 树 林 "),#Haohe Ruhaikou Forest
                (else_try),
                   (ge, ":map_x", 317000),
                   (ge, ":map_y", 49000),
                   (str_store_string, s10, "@雾 连 山 林 "),#Wulian Forest
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 262000),
                   (ge, ":map_y", 38000),
                   (str_store_string, s10, "@河 阴 森 林 "),#Heyin Forest
                (else_try),
                   (ge, ":map_x", 147000),
                   (ge, ":map_y", 138000),
                   (str_store_string, s10, "@京 西 森 林 "),#Jinxi Forest
                (else_try),
                   (ge, ":map_x", 115000),
                   (ge, ":map_y", 117000),
                   (str_store_string, s10, "@古 河 道 森 林 "),#Guhedao Forest
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_snow_forest),
                (eq, ":current_terrain", 0xADFF2F),
                (try_begin),
                   (ge, ":map_x", 261000),
                   (ge, ":map_y", 327000),
                   (str_store_string, s10, "@冰 宫 雪 林 "),#Binggong Forest
                (else_try),
                   (ge, ":map_x", 264000),
                   (ge, ":map_y", 285000),
                   (str_store_string, s10, "@霜 杀 林 "),#Shuangsha Forest
                (else_try),
                   (ge, ":map_x", 236000),
                   (ge, ":map_y", 287000),
                   (str_store_string, s10, "@天 州 林 场 "),#Tianzhou Forest
                (else_try),
                   (ge, ":map_x", 155000),
                   (ge, ":map_y", 297000),
                   (str_store_string, s10, "@惊 寒 森 林 "),#Jinghan Forest
                (else_try),
                   (ge, ":map_x", 200000),
                   (ge, ":map_y", 247000),
                   (str_store_string, s10, "@新 雪 森 林 "),#Xinxue Forest
                (else_try),
                   (ge, ":map_x", 124000),
                   (ge, ":map_y", 284000),
                   (str_store_string, s10, "@雪 哨 林 "),#Xueshao Forest
                (else_try),
                   (ge, ":map_x", 151000),
                   (ge, ":map_y", 240000),
                   (str_store_string, s10, "@明 顺 林 场 "),#Mingshun Forest
                (else_try),
                   (ge, ":map_x", 100000),
                   (ge, ":map_y", 246000),
                   (str_store_string, s10, "@云 棉 林 场 "),#Yunmian Forest
                (else_try),
                   (ge, ":map_x", 42000),
                   (ge, ":map_y", 317000),
                   (str_store_string, s10, "@冰 谷 森 林 "),#Binggu Forest
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (ge, ":map_x", -19000),
                   (ge, ":map_y", 332000),
                   (str_store_string, s10, "@冻 骸 森 林 "),#Dongshi Forest
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (ge, ":map_x", 22000),
                   (ge, ":map_y", 302000),
                   (str_store_string, s10, "@生 路 林 "),#Shenglu Forest
                (else_try),
                   (ge, ":map_x", -55000),
                   (ge, ":map_y", 324000),
                   (str_store_string, s10, "@冰 蚀 谷 雪 林 "),#Bingshigu Forest
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (ge, ":map_x", -62000),
                   (ge, ":map_y", 296000),
                   (str_store_string, s10, "@陷 河 森 林 "),#Xianhe Forest
                (else_try),
                   (ge, ":map_x", -158000),
                   (ge, ":map_y", 328000),
                   (str_store_string, s10, "@深 冰 雪 林 "),#Shenbin Forest
                (else_try),
                   (ge, ":map_x", -160000),
                   (ge, ":map_y", 289000),
                   (str_store_string, s10, "@迷 踪 林 "),#Mizong Forest
                (else_try),
                   (ge, ":map_x", -101000),
                   (ge, ":map_y", 225000),
                   (str_store_string, s10, "@南 望 山 林 "),#Nanwang Forest
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (ge, ":map_x", -155000),
                   (ge, ":map_y", 296000),
                   (str_store_string, s10, "@傲 雪 林 "),#Aoxue Forest
                (else_try),
                   (ge, ":map_x", -251000),
                   (ge, ":map_y", 343000),
                   (str_store_string, s10, "@冰 锋 森 林 "),#Bingfeng Forest
                (else_try),
                   (ge, ":map_x", -222000),
                   (ge, ":map_y", 297000),
                   (str_store_string, s10, "@霜 铁 森 林 "),#Shuangtie Forest
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (ge, ":map_x", -224000),
                   (ge, ":map_y", 251000),
                   (str_store_string, s10, "@近 春 林 "),#Jinchun Forest
                (else_try),
                   (ge, ":map_x", -260000),
                   (ge, ":map_y", 288000),
                   (str_store_string, s10, "@血 根 山 林 "),#Xuegeng Forest
                   (assign, ":current_terrain", rt_snow_mountain),
                (else_try),
                   (ge, ":map_x", -338000),
                   (ge, ":map_y", 271000),
                   (str_store_string, s10, "@冬 风 之 末 森 林 "),#Dongfengzhimo Forest
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_steppe_forest),
                (eq, ":current_terrain", 0x808000),
                (try_begin),
                   (le, ":map_x", -262000),
                   (le, ":map_y", -298000),
                   (str_store_string, s10, "@遗 忘 绿 洲 "),#Forgotten Forest
                   (assign, ":current_terrain", rt_desert),
                (else_try),
                   (le, ":map_x", -262000),
                   (le, ":map_y", -298000),
                   (str_store_string, s10, "@扎 哈 洛 克 绿 洲 "),#Zaharoc Forest
                   (assign, ":current_terrain", rt_desert),
                (else_try),
                   (le, ":map_x", -125000),
                   (le, ":map_y", -268000),
                   (str_store_string, s10, "@沙 中 绿 洲 "),#Desert Forest
                   (assign, ":current_terrain", rt_desert),
                (else_try),
                   (le, ":map_x", -12000),
                   (le, ":map_y", -257000),
                   (str_store_string, s10, "@科 鲁 托 稀 树 草 原 "),#Savanna
                (else_try),
                   (le, ":map_x", -65000),
                   (le, ":map_y", -220000),
                   (str_store_string, s10, "@西 北 入 口 森 林 "),#Northwest extrance Forest
                (else_try),
                   (le, ":map_x", -22000),
                   (le, ":map_y", -209000),
                   (str_store_string, s10, "@东 北 入 口 森 林 "),#Northeast extrance Forest
                (else_try),
                   (le, ":map_x", 74000),
                   (le, ":map_y", -300000),
                   (str_store_string, s10, "@咆 哮 河 下 游 林 地 "),#Downstream Forest
                (else_try),
                   (le, ":map_x", 28000),
                   (le, ":map_y", -260000),
                   (str_store_string, s10, "@草 原 通 道 森 林 "),#Passage Forest
                (else_try),
                   (le, ":map_x", 44000),
                   (le, ":map_y", -204000),
                   (str_store_string, s10, "@咆 哮 河 西 岸 森 林 "),#Westcoast Forest
                (else_try),
                   (le, ":map_x", 75000),
                   (le, ":map_y", -227000),
                   (str_store_string, s10, "@咆 哮 河 东 岸 森 林 "),#Eastcoast Forest
                (else_try),
                   (le, ":map_x", 80000),
                   (le, ":map_y", -175000),
                   (str_store_string, s10, "@米 德 湖 畔 稀 树 草 原 "),#Midul Steppe Forest
                (else_try),
                   (str_store_string, s10, "@山 地 稀 树 草 原 "),#Mountain Steppe Forest
                (try_end),
             (else_try),
                (this_or_next|eq, ":current_terrain", rt_desert_mountain), #荒山
                (eq, ":current_terrain", 0xCDC9A5),
                (str_store_string, s10, "@荒 芜 诸 山 "),#Wildness Mountains
             (else_try),#plain
                (try_begin),
                   (le, ":map_x", -308000),
                   (le, ":map_y", -198000),
                   (str_store_string, s10, "@西 普 威 尔 海 岸 南 部 "),#West Powell South Coast
                (else_try),
                   (le, ":map_x", -311000),
                   (le, ":map_y", -160000),
                   (str_store_string, s10, "@西 普 威 尔 海 岸 北 部 "),#West Powell North Coast
                (else_try),
                   (le, ":map_x", -231000),
                   (le, ":map_y", -206000),
                   (str_store_string, s10, "@阿 尔 瓦 高 地 "),#Alva Highland
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -127000),
                   (le, ":map_y", -236000),
                   (str_store_string, s10, "@歌 乡 盆 地 "),#Songside Basin
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -211000),
                   (le, ":map_y", -171000),
                   (str_store_string, s10, "@奔 流 河 下 游 流 域 "),#Flowing Downstream Land
                (else_try),
                   (le, ":map_x", -224000),
                   (le, ":map_y", -102000),
                   (str_store_string, s10, "@戈 兰 尼 尔 低 地 大 平 原 "),#Grenier Lowland
                (else_try),
                   (is_between, ":map_x", -211000, -190000),
                   (is_between, ":map_y", -202000, -176000),
                   (str_store_string, s10, "@普 威 尔 古 要 道 "),#Ancient Thoroughfare
                (else_try),
                   (le, ":map_x", -124000),
                   (le, ":map_y", -176000),
                   (str_store_string, s10, "@索 尔 丘 地 区 "),#Thol Land
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -305000),
                   (le, ":map_y", 26000),
                   (str_store_string, s10, "@默 林 地 区 "),#Merlin Land
                (else_try),
                   (le, ":map_x", -256000),
                   (le, ":map_y", -21000),
                   (str_store_string, s10, "@摩 甘 地 区 "),#Morgan Land
                (else_try),
                   (le, ":map_x", -280000),
                   (le, ":map_y", 62000),
                   (str_store_string, s10, "@墨 菲 地 区 "),#Murphy Land
                (else_try),
                   (le, ":map_x", -290000),
                   (le, ":map_y", 79000),
                   (str_store_string, s10, "@斯 塔 胡 克 沿 海 洼 地 "),#Starkhook Lowland
                (else_try),
                   (le, ":map_x", -165000),
                   (le, ":map_y", -139000),
                   (str_store_string, s10, "@普 威 尔 台 地 "),#Powell Platform Plain
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (is_between, ":map_x", -124000, -51000),
                   (is_between, ":map_y", -247000, -160000),
                   (str_store_string, s10, "@奥 格 斯 特 半 地 堑 "),#August Half Graben
                (else_try),
                   (le, ":map_x", -176000),
                   (le, ":map_y", -59000),
                   (str_store_string, s10, "@风 门 平 原 "),#Windoor Lowland
                (else_try),
                   (le, ":map_x", -118000),
                   (le, ":map_y", -106000),
                   (str_store_string, s10, "@王 室 直 辖 地 区 "),#Crown Territory
                (else_try),
                   (le, ":map_x", -37000),
                   (le, ":map_y", -117000),
                   (str_store_string, s10, "@山 麓 地 带 "),#Foothill Zone
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -42000),
                   (le, ":map_y", -128000),
                   (str_store_string, s10, "@埃 利 斯 地 区 "),#Ellis Territory
                (else_try),
                   (le, ":map_x", -122000),
                   (le, ":map_y", -28000),
                   (str_store_string, s10, "@四 方 平 原 "),#Fourway Plain
                (else_try),
                   (le, ":map_x", -80000),
                   (le, ":map_y", -55000),
                   (str_store_string, s10, "@四 方 平 原 "),#Fourway Plain
                (else_try),
                   (le, ":map_x", -119000),
                   (le, ":map_y", 6000),
                   (str_store_string, s10, "@纷 争 平 原"),#Controversy Plain
                (else_try),
                   (le, ":map_x", -167000),
                   (le, ":map_y", 74000),
                   (str_store_string, s10, "@步 亡 长 滩 "),#Death Long Beach
                (else_try),
                   (le, ":map_x", -111000),
                   (le, ":map_y", 77000),
                   (str_store_string, s10, "@南 安 基 亚 高 原 "),#South Ankiya Plateau
                (else_try),
                   (is_between, ":map_x", -113000, -85000),
                   (is_between, ":map_y", 44000, 75000),
                   (str_store_string, s10, "@安 基 亚 山 阙 "),#Ankiya Mountain Gap
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (is_between, ":map_x", -110000, -96000),
                   (is_between, ":map_y", -15000, 38000),
                   (str_store_string, s10, "@龙 骸 山 谷"),#Dragonbone Valley
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (is_between, ":map_x", -96000, -86000),
                   (is_between, ":map_y", 14000, 38000),
                   (str_store_string, s10, "@龙 骸 山 谷 "),#Dragonbone Valley
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -21000),
                   (le, ":map_y", -63000),
                   (str_store_string, s10, "@圣 山 西 南 山 坡 "),#Southwest of Holy Mountain
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", -42000),
                   (le, ":map_y", 55000),
                   (str_store_string, s10, "@龙 息 山 地 "),#Dragon Inhabitation Mountainland
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (le, ":map_x", 103000),
                   (le, ":map_y", -151000),
                   (str_store_string, s10, "@避 世 盆 地 "),#Cryptic Basin
                (else_try),
                   (le, ":map_x", 118000),
                   (le, ":map_y", -187000),
                   (str_store_string, s10, "@避 世 盆 地 "),#Cryptic Basin
                (else_try),
                   (le, ":map_x", -303000),
                   (le, ":map_y", 286000),
                   (str_store_string, s10, "@无 光 海 岸 "),#Dark Coast
                (else_try),
                   (le, ":map_x", -200000),
                   (le, ":map_y", 110000),
                   (str_store_string, s10, "@无 光 海 岸 "),#Dark Coast
                (else_try),
                   (le, ":map_x", -148000),
                   (le, ":map_y", 149000),
                   (str_store_string, s10, "@湿 瘴 沼 泽 "),#Damp Marsh
                   (assign, ":current_terrain", rt_marsh),
                (else_try),
                   (le, ":map_x", -148000),
                   (le, ":map_y", 149000),
                   (str_store_string, s10, "@盐 风 沼 泽 "),#Saline Marsh
                   (assign, ":current_terrain", rt_marsh),
                (else_try),
                   (le, ":map_x", -113000),
                   (le, ":map_y", 285000),
                   (str_store_string, s10, "@洪 涝 地 "),#Norwind Marsh
                   (assign, ":current_terrain", rt_marsh),
                (else_try),
                   (le, ":map_x", -253000),
                   (le, ":map_y", 382000),
                   (str_store_string, s10, "@战 利 品 平 原 "),#Spoil Plain
                (else_try),
                   (le, ":map_x", -77000),
                   (le, ":map_y", 164000),
                   (str_store_string, s10, "@悲 泣 高 崖 "),#Mourning Rock
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 285000),
                   (ge, ":map_y", 198000),
                   (str_store_string, s10, "@高 涛 半 岛 平 原 "),#Gaotao Plain
                (else_try),
                   (ge, ":map_x", 224000),
                   (ge, ":map_y", 190000),
                   (str_store_string, s10, "@北 境 平 原 "),#Beijing Plain
                (else_try),
                   (ge, ":map_x", 287000),
                   (ge, ":map_y", 152000),
                   (str_store_string, s10, "@京 畿 平 原 "),#Jinji Plain
                (else_try),
                   (ge, ":map_x", 287000),
                   (ge, ":map_y", 152000),
                   (str_store_string, s10, "@神 笔 山 山 麓 "),#Shenbi Piedmont
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 299000),
                   (ge, ":map_y", 38000),
                   (str_store_string, s10, "@雨 雾 山 山 麓 "),#Yuwu Piedmont
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 189000),
                   (ge, ":map_y", 82000),
                   (str_store_string, s10, "@浩 河 中 下 游 平 原 "),#Haohe Zhongxiayou Plain
                (else_try),
                   (ge, ":map_x", 117000),
                   (ge, ":map_y", 124000),
                   (str_store_string, s10, "@西 河 道 "),#Xihe Dao
                (else_try),
                   (ge, ":map_x", 187000),
                   (ge, ":map_y", -37000),
                   (str_store_string, s10, "@中 原 群 山 地 区 "),#Zhongyuan Qunshan
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 126000),
                   (ge, ":map_y", -19000),
                   (str_store_string, s10, "@中 原 盆 地 "),#Zhongyuan Pengdi
                (else_try),
                   (ge, ":map_x", 250000),
                   (ge, ":map_y", -84000),
                   (str_store_string, s10, "@桃 江 入 海 口 平 原 "),#Taojiang Ruhaikou Plain
                (else_try),
                   (ge, ":map_x", 80000),
                   (is_between, ":map_y", -84000,-13000),
                   (str_store_string, s10, "@桃 江 流 域 平 原 "),#Taojiang Liuyu Plain
                (else_try),
                   (ge, ":map_x", 213000),
                   (ge, ":map_y", -198000),
                   (str_store_string, s10, "@南 方 丘 陵 "),#Nanfang Qiulin
                (else_try),
                   (ge, ":map_x", 76000),
                   (is_between, ":map_y", -143000,-84000),
                   (str_store_string, s10, "@中 原 大 平 原 "),#Zhongyuan Dapingyuan
                (else_try),
                   (ge, ":map_x", 74000),
                   (is_between, ":map_y", -206000,-143000),
                   (str_store_string, s10, "@龙 南 山 地 "),#Longnan Shandi
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 232000),
                   (ge, ":map_y", -313000),
                   (str_store_string, s10, "@湖 海 平 原 "),#Huhai Pingyuan
                (else_try),
                   (ge, ":map_x", 111000),
                   (is_between, ":map_y", -242000,-206000),
                   (str_store_string, s10, "@千 里 连 城 平 原 "),#Qianli Liancheng
                (else_try),
                   (ge, ":map_x", 142000),
                   (is_between, ":map_y", -284000,-242000),
                   (str_store_string, s10, "@洪 阴 平 原 "),#Hongyin Plain
                (else_try),
                   (ge, ":map_x", 99000),
                   (is_between, ":map_y", -316000,-284000),
                   (str_store_string, s10, "@雁 回 原 "),#Yanhui Yuan
                (else_try),
                   (ge, ":map_x", 254000),
                   (ge, ":map_y", -354000),
                   (str_store_string, s10, "@远 乡 "),#Yuan Xiang
                (else_try),
                   (ge, ":map_x", 147000),
                   (ge, ":map_y", -380000),
                   (str_store_string, s10, "@千 落 谷 "),#Qianluo Gu
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", -84000),
                   (ge, ":map_y", 1080000),
                   (str_store_string, s10, "@新 生 大 森 林 "),#Xinsheng Dasenglin
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", 62000),
                   (ge, ":map_y", 7000),
                   (str_store_string, s10, "@教 皇 国 外 省 地 区 "),#Outer Province
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (ge, ":map_x", -58000),
                   (ge, ":map_y", 6000),
                   (str_store_string, s10, "@圣 山 南 方 缓 坡 "),#The gentle land of South Holy Mountain
                (else_try),
                   (ge, ":map_x", 26000),
                   (ge, ":map_y", -38000),
                   (str_store_string, s10, "@圣 山 东 侧 山 坡 "),#East of Holy Mountain
                (else_try),
                   (ge, ":map_x", 26000),
                   (ge, ":map_y", -38000),
                   (str_store_string, s10, "@圣 山 东 侧 山 坡 "),#East of Holy Mountain
                   (assign, ":current_terrain", rt_mountain),
                (else_try),
                   (str_store_string, s10, "@圣 山 东 南 山 坡"),#Southeast of Holy Mountain
                   (assign, ":current_terrain", rt_mountain),
                (try_end),
             (try_end),
             (assign, reg1, ":current_terrain"), #返回细化的地形，用于会战获取沙盘。获取完毕后还需使用一般terrain以判断是否有森林
    ]),


  ("initial_map_point", [      #use for create map view
#        (assign, ":cur_time", "$map_point_count_no"),
#        (val_add, ":cur_time", 1),
#        (store_add, ":cur_time_limit", ":cur_time", 500),
(assign, ":cur_time", 0),
(assign, ":cur_time_limit", 1000000),

        (assign, "$map_point_count_no", 0),
        (assign, ":former_color_1", 0),
        (assign, ":former_color_2", 0),
        (assign, ":count_no", 0),
        (assign, ":count_no_1", 0),
        (assign, ":count_no_2", 0),
        (set_fixed_point_multiplier, 1000),

        (try_for_range, "$map_point_count_no", ":cur_time", ":cur_time_limit"),
           (store_div, ":cur_x", "$map_point_count_no", 1000),
           (store_mod, ":cur_y", "$map_point_count_no", 1000),
           (val_sub, ":cur_x", 500),
           (val_sub, ":cur_y", 500),

           (assign, ":dest_color", 0xFFFFFF), # default

           (store_mul, ":map_x", ":cur_x", 750),
           (store_mul, ":map_y", ":cur_y", 750),

           (position_set_x, pos1, ":map_x"),
           (position_set_y, pos1, ":map_y"),
           (party_set_position, "p_temp_party", pos1),

           #natural feature
           (party_get_current_terrain, ":current_terrain", "p_temp_party"),
           (try_begin),
              (eq, ":current_terrain", rt_water),
              (assign, ":dest_color", 0xB0E2FF), #sea
           (else_try),
              (eq, ":current_terrain", rt_river),
              (assign, ":dest_color", 0x0080FF), #river
           (else_try),
              (eq, ":current_terrain", rt_bridge),
              (assign, ":dest_color", 0x808080), #ford
           (else_try),
              (eq, ":current_terrain", rt_steppe),
              (assign, ":dest_color", 0x9ACD32), #steppe
           (else_try),
              (eq, ":current_terrain", rt_plain),
              (assign, ":dest_color", 0x6B8E23), #plain
           (else_try),
              (eq, ":current_terrain", rt_snow),
              (assign, ":dest_color", 0xFFFFF0), #snow
           (else_try),
              (eq, ":current_terrain", rt_desert),
              (assign, ":dest_color", 0xBDB76B), #desert
           (else_try),
              (eq, ":current_terrain", rt_steppe_forest),
              (assign, ":dest_color", 0x808000), #steppe_forest
           (else_try),
              (eq, ":current_terrain", rt_forest),
              (assign, ":dest_color", 0x006400), #forest
           (else_try),
              (eq, ":current_terrain", rt_snow_forest),
              (assign, ":dest_color", 0xADFF2F), #snow forest
           (else_try),
              (eq, ":current_terrain", rt_mountain),
              (assign, ":dest_color", 0xCDC1C5), #mountain
           (else_try),
              (eq, ":current_terrain", rt_desert_mountain),
              (assign, ":dest_color", 0xCDC9A5), #steppe mountain
           (try_end),
           (troop_set_slot, "trp_temp_array_new_map_1", "$map_point_count_no", ":dest_color"), # natural terrain color
             
           (try_begin),
              (eq, ":former_color_1", ":dest_color"),
              (val_add, ":count_no_1", 1),
           (else_try),
              (assign, ":count_no_1", 0),
           (try_end),

           (assign, ":former_color_1", ":dest_color"),

           #get natural area name
           (call_script, "script_get_natural_zone", ":map_x", ":map_y", ":current_terrain"),
#           (troop_set_slot, "trp_temp_array_new_map_5", "$map_point_count_no", reg0),

           #faction feature
           (party_get_current_terrain, ":current_terrain", "p_temp_party"),
           (try_begin),
              (this_or_next|eq, ":current_terrain", rt_water),
              (eq, ":current_terrain", rt_river),
              (assign, ":dest_color", 0x0080FF), #river and sea
           (else_try),
              (eq, ":current_terrain", rt_bridge),
              (assign, ":dest_color", 0x808080), #ford
           (else_try),
              (this_or_next|eq, ":current_terrain", rt_mountain),
              (eq, ":current_terrain", rt_desert_mountain), #荒山
              (assign, ":dest_color", 0xCDC1C5), #mountain
           (else_try),
              (call_script, "script_get_closest_center", "p_temp_party"),
              (assign, ":nearest_center", reg0),
              (try_begin),
                 (gt, ":nearest_center", -1),
                 (store_faction_of_party, ":center_faction", ":nearest_center"),
                 (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
                 (faction_get_color, ":dest_color", ":center_faction"),
              (try_end),
           (try_end),
           (troop_set_slot, "trp_temp_array_new_map_6", "$map_point_count_no", ":dest_color"), #faction color
           
           (try_begin),
              (eq, ":former_color_2", ":dest_color"),
              (val_add, ":count_no_2", 10000),
           (else_try),
              (assign, ":count_no_2", 0),
           (try_end),
           (store_add, ":count_no", ":count_no_1", ":count_no_2"),
           (troop_set_slot, "trp_temp_array_new_map_2", "$map_point_count_no", ":count_no"),# same as former color

           (assign, ":former_color_2", ":dest_color"),
        (try_end),


        #center
        (try_for_range, ":center_no", centers_begin, centers_end),
           (party_get_position, pos1, ":center_no"),
           (position_get_x, ":pos_x", pos1),
           (position_get_y, ":pos_y", pos1),

           (val_div, ":pos_x", 1000),
           (val_div, ":pos_y", 1000),
           (val_add, ":pos_x", 375),
           (val_add, ":pos_y", 375),
           (val_mul, ":pos_x", 4),
           (val_mul, ":pos_y", 4),
           (val_div, ":pos_x", 3),
           (val_div, ":pos_y", 3),
           (val_mul, ":pos_x", 1000),
           (store_add, ":target_point", ":pos_x", ":pos_y"),

           (troop_set_slot, "trp_temp_array_new_map_3", ":target_point", ":center_no"), #in case the center can't be find in 750*750 size map
           (val_add, ":target_point", 1),
           (troop_set_slot, "trp_temp_array_new_map_3", ":target_point", ":center_no"), 
           (val_add, ":target_point", 1000),
           (troop_set_slot, "trp_temp_array_new_map_3", ":target_point", ":center_no"), 
           (val_sub, ":target_point", 1),
           (troop_set_slot, "trp_temp_array_new_map_3", ":target_point", ":center_no"), 
        (try_end),

        (assign, "$amplify_x", 250),
        (assign, "$amplify_y", 250),#use for amplify map
        (assign, "$show_town", 0),
        (assign, "$show_castle", 0),
        (assign, "$show_village", 0),
        (assign, "$show_faction_map", 0),#0 is natural map, 1 is faction map
    ]),


]