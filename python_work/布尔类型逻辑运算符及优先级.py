#布尔类型bool
#True 1 和 False 0 
#逻辑符  and or not
#短路逻辑(从左往右，只有当第一个操作值无法确认定逻辑运算时，才进行第二个操作数求值)
print(3 and 4 == 4) #第二个才能确定
print(3 or 4 == 3)#第一个就确定了
print(0 and 3 == 0)
print(0 or 4 == 4)

print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9) == 4)
 #先运算小括号，即小括号优先级高
 #False or 0 or 4 or 6 or 9
 #短路逻辑，结果为4

print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9 == 4)
  #运算优先级 not and or
 # False or 0 or 4 or 6 or 9
