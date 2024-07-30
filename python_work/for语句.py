sum = 0
while 1:
	temp = input("想要结束计算，请输入sd\n请输入N的值，我会告诉你它从1开始的求和值\n")	
	if temp == 'sd':
		print("计算结束，拜拜！")
		break
	else:
		N = int(temp)
		for i in range(0,N+1):
		 sum  += i  
		print("1+2+3+...+"+str(N)+"="+str(sum))

