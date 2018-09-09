import sys 

# 读取和分析待机模式的功耗数据
file = open('StandbyData.txt')
data = file.read()
data = data.split(',')
data_float = [float(item) for item in data];
average = sum(data_float)/len(data_float)
print('Standby data len =',len(data_float))
print('Standby data average = ',average,'A')
file.close()

# 读取和分析数据传输时期的功耗数据
file = open('sendData.txt')
data = file.read()
data = data.split(',')
data_float = [float(item) for item in data];
average = sum(data_float)/len(data_float)
print('Send period\'s data len =',len(data_float))
print('Send period\'s data average = ',average,'A')	
file.close()

# 读取和分析数据传输时期的功耗数据
file = open('AttachInternet.txt')
data = file.read()
data = data.split(',')
data_float = [float(item) for item in data];
average = sum(data_float)/len(data_float)
print('Attach period\'s data len =',len(data_float))
print('Attack period\'s data average = ',average,'A')


