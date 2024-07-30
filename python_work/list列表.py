#list列表-小甲鱼学python
s =[1,2,3,4,5]#列表“增 删 改 查 ”
s.append(6)#列表增加对象单个是函数的（）直接写入
print(s)
s.extend([7,8,9])#集合是[]
print(s)
s[(len(s)):] = [10,11,12]#切片 相同的实现方法
print(s)
s[len(s):] = [13]
print(s)
s.insert(0,0)#插入特定未知添加第一个是未知第二是对象
print(s)
s.insert(len(s),14)
print(s)
s.insert(9,"a")
print(s)
s.remove("a")#删除特定对象
print(s)
s.pop(0)#剔除特定下标未知的元素
print(s)
#list第一节
a= s[0]#查 列表元素访问[]
print(a)
b = s[-1]
print(b)
c = s[1:3]#列表切片都是[]
print(c)
d= s[:3]
print(d)
f = s[3:]
print(f)
g = s[::2]
print(g)
s.clear()#清空列表
print(s)
k=[1,2,3,8,8,8,4,5,9]
k[2] = "钢铁侠"#改 改动列表元素
print(k)
print(k.index("钢铁侠"))#查找元素下标数
k[2]=10
print(k)
k.sort()#排序由小到大 不需要赋值变量 
print(k)
k.reverse()#倒序排列
print(k)
num= k.count(8)#改元素出现几次 一定要赋值变量print
print(num)
k.sort(reverse = 1)#倒序排列
print(k)
k_copy1 = k.copy()#复制函数
print(k_copy1)
k_copy2 = k[:]#利用切片复制
print(k_copy2)
