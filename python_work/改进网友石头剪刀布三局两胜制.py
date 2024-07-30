import random
a=random.randint(1,4)
i = 3
print('''
来我两来玩石头剪刀布游戏吧^_^!
1为剪刀，2为石头，3为布
三局两胜哦！
***************************    ''')
while i:
	
    b=input("请打出你要出的手势：")
    c=int(b)
    if a==1:
        print('我出的是剪刀')
    if a==2:
        print('我出的是石头')
    if a==3:
        print('我出的是布')
              
    if a==c:
        print('平局。\n这次不算再来\n')
        i = i + 1
        
    if a==1 and c==2:
        print('你赢了，真厉害！*****')
    if a==1 and c==3:
        print('你输了，真可惜。\n')
    if a==2 and c==3:
        print('你赢了，真厉害！*****')
    if a==2 and c==1:
        print('你输了，真可惜。\n')
    if a==3 and c==1:
        print('你赢了，真厉害！*****')
    if a==3 and c==2:
        print('你输了，真可惜。\n')
    i = i - 1

    if i > 0:
        stem = "你还有" + str(i) + "次机会！\n继续^_^\n"
        print(stem)
    else:
        print("很遗憾，你没有机会了！")
        

print('"不玩啦，游戏结束！"')
