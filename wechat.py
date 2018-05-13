# coding:utf-8
# 导入模块
from wxpy import *
import requests
import json
import sys
import time
from matplotlib import pyplot as plt
reload(sys)
sys.setdefaultencoding('utf8')


def login_c():
    pass

def analyseSex(sex_dict):
    sexs = list(key for key, value in sex_dict.items())
    counts = list(value for key, value in sex_dict.items())
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,  # 性别统计结果
            labels=sexs,  # 性别展示标签
            colors=colors,  # 饼图区域配色
            labeldistance=1.1,  # 标签距离圆点距离
            autopct='%3.1f%%',  # 饼图区域文本格式
            shadow=False,  # 饼图是否显示阴影
            startangle=90,  # 饼图起始角度
            pctdistance=0.6  # 饼图区域文本距离圆点距离
    )
    plt.legend(loc='upper right',)
    plt.title(u'微信好友性别组成')
    plt.show()

# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True, login_callback=login_c())
# bot = Bot()

# 获取所有好友
my_friends = bot.friends()
print(type(my_friends))

# 使用一个字典统计好友男性和女性的数量
sex_dict = {'male': 0, 'female': 0, 'unknown': 0}

for friend in my_friends:
    # 统计性别
    if friend.sex == 1:
        sex_dict['male'] += 1
    elif friend.sex == 2:
        sex_dict['female'] += 1
    else:
        sex_dict['unknown'] += 1

print(sex_dict)
# analyseSex(sex_dict)


# 使用一个字典统计各省好友数量
province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
    '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
    '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
    '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
    '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
    '四川': 0, '贵州': 0, '云南': 0,
    '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
    '香港': 0, '澳门': 0, '国外及未知': 0}

# 统计省份
for friend in my_friends:
    if friend.province in province_dict.keys():
        province_dict[str(friend.province)] += 1
    else:
        province_dict['国外及未知'] += 1

# 为了方便数据的呈现，生成JSON Array格式数据
data = []
for key, value in province_dict.items():
    data.append({'name': key, 'value': value})

print(json.dumps(data, ensure_ascii=False))


embed()
