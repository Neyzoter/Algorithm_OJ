'''
落单的数

给出 2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，写一个函数找到这个数字。

挑战：
一次遍历，常数级的额外空间复杂度

格式：

输入行输入一个数组，最后输出出现一次的数字。

样例输入

[ 1，2，2，1，3，4，3 ]

样例输出

4

'''

def findLonelyNum(lst):
	lst.sort()#快速排序
	for idx in range(len(lst)//2):
		idx = idx * 2
		# if lst[idx] != lst[idx+1]:
		if lst[idx] ^ lst[idx+1]:#异或是True的话，说明不一样
			return lst[idx]
	return lst[-1]
lst = [1,2,2,1,3,4,3,5,5,10,10,4,16]
print(findLonelyNum(lst))








