# Algorithm CPP
## 反转整数
**IntegerReverse.h**

### 问题描述
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

```
输入: 123
输出: 321
```

 示例 2:

```
输入: -123
输出: -321
```

示例 3:

```
输入: 120
输出: 21
```

注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

### 思路
* 暴力法

1、数字每位存在vector1中

不大于9，切全部存为正

2、判断x正负并确定最大值，以一位一位的形式存在vector2

x如果为正，则最大是0x7FFF FFFF

x如果为负，则最大是0x7FFF FFFF + 1

低位在前，高位在后。

注意：个位要判断x正负，决定是+1还是不+1。

3、对比目标x的vector1和最大的结果vector2

vector1分别是高->低，vector2分别是低->高

所以vector从begin开始遍历，vector2从end-1开始遍历（end返回的是最后一位的下标+1）

* 弹出和推入数字 & 溢出前进行检查

```cpp
class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
```
