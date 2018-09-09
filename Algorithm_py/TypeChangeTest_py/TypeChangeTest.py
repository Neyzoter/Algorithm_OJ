
'''
TEST1
列表整体赋值测试
对外部列表没有影响
'''
def listTest1(lst):
	print('##listTest1##：在函数内给整个lst赋值')
	lst = ['1','2','3','4']

print('---------TEST1---------\n列表整体赋值测试\n对外部列表没有影响\n')
lst = ['ini','go','me','meide']
print('原始lst',lst)
print('原始lst[0]的地址',id(lst[0]))
print('原始lst的地址',id(lst),'\n\n')
listTest1(lst)
print('lstTest1后的lst',lst)
print('lstTest1后的lst[0]的地址',id(lst[0]))
print('lstTest1后的lst的地址',id(lst))

'''
TEST2
列表元素赋值测试
对外部列表整体地址没有影响
对元素地址有影响
'''
def listTest2(lst):
	print('##listTest1##：在函数内给lst[0]赋值')
	lst[0] = '1'
print('\n\n---------TEST2---------\n列表元素赋值测试\n对外部列表整体地址没有影响\n对元素地址有影响\n')
lst = ['ini','go','me','meide']
print('原始lst\t',lst)
print('原始lst[0]的地址',id(lst[0]))
print('原始lst的地址',id(lst),'\n\n')
listTest2(lst)
print('lstTest2后的lst\t',lst)
print('lstTest2后的lst[0]的地址',id(lst[0]))
print('lstTest2后的lst的地址',id(lst))


'''
TEST3
for 循环语句能否改变索引的值
不能
必须按照顺序来，就算在for中赋值，在再一次循环时会被赋值成顺序
'''
print('\n\n---------TEST3---------\nfor 循环语句能否改变索引的值\n不能\n必须按照顺序来，就算在for中赋值，在再一次循环时会被赋值成顺序\n')
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for i in range(len(lst)):
	print(lst[i],'  ',end = '')
	if i == 4:
		i = 10
print('\n')
'''
TEST4
字典的赋值、拷贝等
（1）直接赋值
b = a
两者完全一样，指向同一个地址
（2）浅复制
b = a.copy()
a和b整体指向不同的地址，但是元素指向相同的地址
（3）深复制
b = copy.deepcopy(a)
a和b整体和元素都指向不通过的地址，只是数值相同
'''
import copy
print('\n\n---------TEST4-----------\n字典的赋值、拷贝\n')
dct1 = {'user':'runoob','num':[1,2,3]}
dct2 = dct1
dct3 = dct1.copy()
dct4 = copy.deepcopy(dct1)
print('dct1\t\t%d'%id(dct1))
print('直接赋值的dct2\t%d'%id(dct2))
print('浅复制的dct3\t%d'%id(dct3))
print('dct1的元素0\t\t%d'%id(dct1['user']))
print('浅复制的dct3的元素0\t%d'%id(dct3['user']))
print('深复制的dct4\t%d'%id(dct4))
dct1['user'] = 'root'
dct1['num'].remove(1)
print(dct1)
print(dct2)
print(dct3)
print(dct4)







