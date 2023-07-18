import random
rand1 = random.randint(0,2)
name = None

def Adjective():
    name = None
    rand2 = random.randint(0,10)
    if rand2 == 0:
        name = "帅气的"
    elif rand2 == 1:
        name = "狂笑的"
    elif rand2 == 2:
        name = "欢乐的"
    elif rand2 == 3:
        name = "野性的"
    elif rand2 == 4:
        name = "憔悴的"
    elif rand2 == 5:
        name = "贪吃的"
    elif rand2 == 6:
        name = "欢快的"
    elif rand2 == 7:
        name = "笔挺的"
    elif rand2 == 8:
        name = "好玩的"
    elif rand2 == 9:
        name = "忠实的"
    elif rand2 == 10:
        name = "坚强的"
    return name

def Noun():
    name = None
    rand2 = random.randint(0,10)
    if rand2 == 0:
        name = "蛇"
    elif rand2 == 1:
        name = "猴子"
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
        name = "皇后"
    elif rand2 == 9:
        name = "螃蟹"
    elif rand2 == 10:
        name = "山羊"
    return name

def Verb():
    name = None
    rand2 = random.randint(0,10)
    if rand2 == 0:
        name = "将写散文"
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
        name = "灌篮"
    elif rand2 == 7:
        name = "跑酷"
    elif rand2 == 8:
        name = "打电话"
    elif rand2 == 9:
        name = "敷面膜"
    elif rand2 == 10:
        name = "骑羊驼"
    return name

if rand1 == 0 or rand1 == 1:
    name = Adjective() + Noun() + Verb()
elif rand1 == 2:
    name = Verb() + "的" + Noun()
print(name)