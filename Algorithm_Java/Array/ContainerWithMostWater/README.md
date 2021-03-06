# 盛最多水的容器问题

(下标1-下标2)*(高度)

# 思路
## 暴力法
1、两个for循环

获取最大的面积

*时间复杂度*:O(n^2)

*空间复杂度*:O(1)

## 双指针法
由于限制面积的总是高度低的，所以需要将高度低的指针向内侧移动。

为了使面积最大化，我们需要考虑更长的两条线段之间的区域。如果我们试图将指向较长线段的指针向内侧移动，矩形区域的面积将受限于较短的线段而不会获得任何增加。

另外的理解：移动高度高的，没有必要了。不过就算没有遍历，也不会有遗漏的地方。