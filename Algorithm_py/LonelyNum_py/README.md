# 函数说明

落单数字

# 描述

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

# 解决方案

快速排序+判断相邻数字异或是否是True，如果是则返回