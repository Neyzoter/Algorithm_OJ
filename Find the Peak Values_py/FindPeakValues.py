'''
你给出一个整数数组（size 为 n），其具有以下特点：
1、相邻位置的数字是不同的
2、A[0] < A[1] 并且 A[n - 2] > A[n - 1]

假定P是峰值的位置则满足 A[P] > A[P-1] 且 A[P] > A[P+1]，写一个函数返回数组中所有峰值的位置。

格式：

输入行输入一个整数数组，输出行输出所有数组中的峰值的位置。

样例输入

[ 1，2，1，3，4，5，7，6 ]

样例输出

1，6
'''

List = [1,2,1,3,4,5,7,6]

def FindPeakIndex(List):
	PeakIndex = []
	iRange = range(1,len(List)-1)
	for i in iRange:
		if (List[i] > List[i-1]) and (List[i] > List[i+1]):
			PeakIndex.append(i)
	return PeakIndex

PeakIndex = FindPeakIndex(List)
for i in PeakIndex:
	print('下标',i,'数值',List[i])
	

	