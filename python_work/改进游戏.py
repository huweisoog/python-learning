""" 用python设计第一个游戏 """# 长字符串说明文档

import random#导入模块

counts = 3#设置循环次数，否则一直循环
answer = random.randint(1,10)#生成伪随机数

while counts > 0:#循环语句
    temp = input("我心里有1-10的整数，你可以猜3次，不妨猜我现在心里想的是哪个数字：")#赋值运算符
    guess = int(temp)#取整数函数
    
    if guess == answer:# 条件分支语句
        print("你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
        break#中止
    else:
        if guess < answer:#缩进符表示不同层级逻辑
            print("小啦")
        else:
            print("大啦")
    counts = counts - 1#不缩进，就是一直循环，不会每次执行玩-1；
                           #缩进一个，与第一个if对齐，均运行3次结束
                           #多缩进，只有大了时，猜有次数限制

print("游戏结束，不玩啦^_^")

