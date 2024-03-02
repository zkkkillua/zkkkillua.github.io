---
title: 191. 位1的个数
date: 2021-03-06 21:02:49
categories: 
- leetcode
tags: 
- 位运算
---

## 1. 位运算
```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int sum = 0;
        for (int i = 0; i < 32; i++) {
            sum += n & 1;
            n >>= 1;
        }

        return sum;
    }
};
```

## 2. 不修改n
方法1会修改n，且由于右移如果是负数，最高位补的是1，故不能写`while(n)`  
方法2使用一个辅助变量，不是右移n，而是左移辅助变量  

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int sum = 0;
        uint32_t f = 1;
        while (f) {
            if (n & f)
                sum++;
            f <<= 1;
        }

        return sum;
    }
};
```

## 3. `n & (n - 1)`
上述两个方法的复杂度都是`O(32)`，需要遍历全部的32位。  
考虑`n-1`，相比`n`，`n`中的最后一个1变成了0，右侧的0全部变成了1。  
因此`n & (n - 1)`相当于把`n`最右侧的1去掉了，不论n是正还是负。  
利用这个性质，可以在`O(m)`的时间内算出二进制中1的个数，m为二进制中1的个数，优于`O(32)`。  
```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int sum = 0;
        while (n) {
            n = n & (n - 1);
            sum++;
        }

        return sum;
    }
};
```