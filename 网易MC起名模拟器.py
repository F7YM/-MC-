import random
rand1 = random.randint(0,2)
name = None

def Adjective():
    name = None
    rand2 = random.randint(0,18)
    if rand2 == 0:
        name = "帅气"
    elif rand2 == 1:
        name = "狂笑"
    elif rand2 == 2:
        name = "欢乐"
    elif rand2 == 3:
        name = "野性"
    elif rand2 == 4:
        name = "憔悴"
    elif rand2 == 5:
        name = "贪吃"
    elif rand2 == 6:
        name = "欢快"
    elif rand2 == 7:
        name = "诚实"
    elif rand2 == 8:
        name = "好玩"
    elif rand2 == 9:
        name = "忠实"
    elif rand2 == 10:
        name = "坚强"
    elif rand2 == 11:
        name = "努力"
    elif rand2 == 12:
        name = "美丽"
    elif rand2 == 13:
        name = "耐心"
    elif rand2 == 14:
        name = "散步"
    elif rand2 == 15:
        name = "极品"
    elif rand2 == 16:
        name = "虚无"
    elif rand2 == 17:
        name = "阴郁"
    elif rand2 == 18:
        name = "谦让"
    
    rand3 = random.randint(0,3)
    if rand3 == 0:
        return name + "的"
    elif rand3 == 1:
        return name + "之"
    else:
        return name

def Noun():
    name = None
    rand2 = random.randint(0,15)
    if rand2 == 0:
        name = "蛇"
    elif rand2 == 1:
        name = "西瓜"
    elif rand2 == 2:
        name = "野猪"
    elif rand2 == 3:
        name = "鱼"
    elif rand2 == 4:
        name = "石头"
    elif rand2 == 5:
        name = "犀牛"
    elif rand2 == 6:
        name = "冬瓜"
    elif rand2 == 7:
        name = "魔都"
    elif rand2 == 8:
        name = "太上老君"
    elif rand2 == 9:
        name = "螃蟹"
    elif rand2 == 10:
        name = "山羊"
    elif rand2 == 11:
        name = "太阳"
    elif rand2 == 12:
        name = "力士"
    elif rand2 == 13:
        name = "小象"
    elif rand2 == 14:
        name = "书生"
    elif rand2 == 15:
        name = "苍鹰"
    elif rand2 == 16:
        name = "蛾子"
    return name

def Verb():
    name = None
    rand2 = random.randint(0,21)
    if rand2 == 0:
        name = "写散文"
    elif rand2 == 1:
        name = "吃巧克力"
    elif rand2 == 2:
        name = "写作业"
    elif rand2 == 3:
        name = "开飞车"
    elif rand2 == 4:
        name = "修手机"
    elif rand2 == 5:
        name = "大笑"
    elif rand2 == 6:
        name = "跳舞"
    elif rand2 == 7:
        name = "跑酷"
    elif rand2 == 8:
        name = "打电话"
    elif rand2 == 9:
        name = "敷面膜"
    elif rand2 == 10:
        name = "作演讲"
    elif rand2 == 11:
        name = "睡觉"
    elif rand2 == 12:
        name = "散步"
    elif rand2 == 13:
        name = "吃饭"
    elif rand2 == 14:
        name = "拔牙"
    elif rand2 == 15:
        name = "洗脸"
    elif rand2 == 16:
        name = "放鞭炮"
    elif rand2 == 17:
        name = "吹喇叭"
    elif rand2 == 18:
        name = "扔东西"
    elif rand2 == 19:
        name = "上网"
    elif rand2 == 20:
        name = "吃辣条"
    elif rand2 == 21:
        name = "咆哮"
    
    if random.randint(0,1) == 0:
        return "将" + name
    else:
        return name

if rand1 == 0 or rand1 == 1:
    name = Adjective() + Noun() + Verb()
elif rand1 == 2:
    name = Verb() + "的" + Noun()
print(name)