'''
实现atoi这个函数，将一个字符串转换为整数。如果没有合法的整数，返回0。若整数超出了32位整数的范围，如果是正整数则返回 INT_MAX（2147483647），或者如果是负整数则返回 INT_MIN（-2147483648）。

格式：

输入行每一行输入一个字符串，最后每一行输出经过转换后得到的整数。

样例输入

"10" 
"-1" 
"123123123123123" 
"1.0" 

样例输出

10
-1
2147483647
1
'''
import re
import math
def atoi(string):
	positiveBIGEST = int(math.pow(2,31)-1)
	negtiveBIGEST = int(-positiveBIGEST-1)
	def getInt(string):
		if string == '0':
			flag = 1
			return [0,1]
		try:
			return [int(string)	,0]
		except ValueError:
			print('Catch the ValueError')
			return [0,0]
		except:
			print('Unknow exception')
			return [0,0]
	atoiResult = getInt(string)
	if atoiResult[0]< negtiveBIGEST :
		return {'value':negtiveBIGEST,'is0':atoiResult[1]}
	elif atoiResult[0] > positiveBIGEST:
		return {'value':positiveBIGEST,'is0':atoiResult[1]}
	elif atoiResult[0] or atoiResult[1]:
		return {'value':atoiResult[0],'is0':atoiResult[1]}	
string = '9999999999999999999999999999999999999999999999999999'
getNum = atoi(string)	
if getNum['value'] or getNum['is0']:
	print(getNum['value'],type(getNum['value']))

	
	
		