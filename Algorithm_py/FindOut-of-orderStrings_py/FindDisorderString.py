import copy
def FindDisorderString(lst):
	lstTemp = copy.deepcopy(lst)
	for idx in range(len(lst)):
		# 创建一个字符串分裂后的缓存数组
		strTemp = list(lst[idx]) 
		# 排序
		strTemp.sort() 
		lstTemp[idx] = ''.join(strTemp)
	print('原始字符串列表：',lst)	
	print('排序后字符串列表：',lstTemp)
	lstTempLen = len(lstTemp)
	# print('lstTempLen = ',lstTempLen)
	idx = [] # 要返回的下标
	temp = '' # 给temp赋初值
	i = 0
	while i < lstTempLen:
		if temp:
			if lstTemp[i] == temp:
				idx.append(i)
		elif i < lstTempLen-1:
			if lstTemp[i] == lstTemp[i+1]:
				idx.append(i)
				idx.append(i+1)
				temp = lstTemp[i]
				i += 1
		i += 1
	return idx
	
lst = ["lint","intl","inlt","code",'dfdsfjkdf','sfdsfs','sdfsdf','ere','dfsdf','dfasdfadfe',]	
idx = FindDisorderString(lst)	
print('\n\n字符串下标',idx)
DisorderList = []
for i in idx:
	DisorderList.append(lst[i])
print('乱序字符串',DisorderList)

