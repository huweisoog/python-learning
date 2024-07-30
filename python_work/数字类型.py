#数字类型
import decimal#转化为小数类型，提高精度
a = decimal.Decimal("0.1")#注意是字符串
b = decimal.Decimal("0.2")
print(a+b)
#0.3
c = decimal.Decimal('0.3')
if a + b == c:
	print("ture")

(0.3 == 0.1 + 0.2 ) and Ture #浮点数相加，不相等,浮点数可理解为只是多位的近视值

x = 1 + 2j#复数，实部和虚部
print(x.real)
#1.0
print(x.imag)
#2.0

print(5e-05)#科学计数法

print(3//2)#地板除，向下取整

print(abs(-520))#绝对值

tem = pow(2,3,5) #2**3%5
print(tem)
