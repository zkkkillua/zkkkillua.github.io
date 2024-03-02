---
title: 202.快乐数
date: 2020-04-30 21:16:02
categories: leetcode
tags: 
- 双指针
---
## 1. 直接模拟，set检测是否重复
`set`：`find()`和`count()`对数级别复杂度，插入`insert()`在给定迭代器作为位置的情况下是`O(1)`，不给则是对数级别复杂度。  
`unordered_set`：`find()`和`count()`平均是`O(1)`，最坏`O(n)`（hash函数太差了），插入`insert()`同查找。  
```cpp
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> unique;
        unique.insert(n);
        int copyn = n;
        while (n != 1) {
            n = 0;
            while (copyn != 0) {
                n += pow((copyn % 10), 2);
                copyn /= 10;
            }
            copyn = n;
            if (unique.count(n) == 1)
                return false;
            else
                unique.insert(n);
        }

        return true;
    }
};
```

## 2. 快慢指针
如果有结果，那么就好像是一条链一样。  
如果没结果，不是快乐数，则代表有循环，也就可以转换成环形链表来做，快慢指针重合时代表不是快乐数。  
这样就避免了set一直存数。  
时间上跟unordered_set一样都是`O(logn)`，空间更优，是`O(1)`。  
```cpp
class Solution {
public:
    int getNext(int n) {
        int ans = 0;
        while (n != 0) {
            ans += pow(n % 10, 2);
            n /= 10;
        }
        return ans;
    }

    bool isHappy(int n) {
        int slow = n, quick = getNext(n);

        while (quick != 1 && slow != quick) {
            slow = getNext(slow);
            quick = getNext(getNext(quick));
        }

        return quick == 1;
    }
};
```