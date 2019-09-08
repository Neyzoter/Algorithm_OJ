# 1、两数之和问题
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]

# 2、思路
## 2.1 暴力法
两个for循环依次遍历，较简单

*时间复杂度*:O(n^2)

*空间复杂度*:O(1)

## 2.2 两次遍历Hash表法
1、将nums数据保存在哈希表中，以<数值，下标>存储，即数值对因键值，下标对因数值。

2、for循环遍历nums（得到nums[i]），并得到对应的另外一个数的数值target-nums[i]。

3、哈希表查找对因的数值，并判断查找到的下标是否和i相同，相同则舍弃（不能重复使用）

说明：哈希表查询可以达到O(1)时间复杂度

*时间复杂度*:O(n)

*空间复杂度*:O(n)

## 2.3 一次遍历hash表法
一边存一边回退查看hash表中是否有对因的值

*时间复杂度*:O(n^2)

*空间复杂度*:O(1)

# 3、感悟
HashMap可以提高遍历的速度，达到O(1)时间复杂度。

用空间换取了时间。