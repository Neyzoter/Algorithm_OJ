# 文件作用
用于Python的数据类型的改变、赋值等特性测试

# 描述
* 赋值问题</br>
1.**在函数体内给列表“整个”赋值（见TEST1）**</br>
不会改变外部列表的地址</br>只在函数体内有效</br>
2.**在函数体内给列表某个元素赋值**</br>
会改变外部列表的那个元素的地址</br>而不会改变列表的整体地址</br></br>
* 直接等于、浅复制、深复制问题</br>
字典的赋值、拷贝等</br>
（1）直接赋值</br>
b = a</br>
两者完全一样，指向同一个地址</br>
（2）浅复制</br>
b = a.copy()</br>
a和b整体指向不同的地址，但是元素指向相同的地址</br>
（3）深复制</br>
b = copy.deepcopy(a)</br>
a和b整体和元素都指向不通过的地址，只是数值相同</br>
* 循环语句</br>
1.**for循环体内改变索引的值**</br>
for 循环语句能否改变索引的值</br>
不能</br>必须按照顺序来，就算在for中赋值，在再一次循环时会被赋值成顺序</br>

