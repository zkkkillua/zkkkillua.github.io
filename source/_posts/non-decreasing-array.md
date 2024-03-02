---
title: 665. 非递减数列
date: 2021-02-07 22:22:04
categories: 
- leetcode
tags: 
- 贪心
---
## 1. 朴素
遍历直到出现不满足非递减的情况，此时需要进行调整，然后看调整之后是否可以继续满足非递减条件。  
调整时使用贪心策略，优先修改能使调整后的当前位置的元素更小。  
可能遇到的情况：`1 2 3 4 1 6 7 ...`, `1 2 3 8 4 5 6 ...`  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2)
            return true;

        bool changed = false, res = true;
        int preLoc = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[preLoc] && changed) {
                res = false;
                break;
            } else if (nums[i] < nums[preLoc] && !changed) {
                if (preLoc == 0) 
                    preLoc = i;
                else {
                    if (nums[i] >= nums[preLoc - 1]) 
                        preLoc = i;
                }
                changed = true;
            } else 
                preLoc = i;
        }

        return res;
    }
};
```