---
title: 55.跳跃游戏
date: 2020-05-04 10:53:25
categories: leetcode
tags: 
- 贪心
---
## 1. 朴素
`bool reach[]`记录是否可以到达。  
遍历`nums[i]`，将其可以到达的位置置为true。时间复杂度是`O(n)`，因为就算修改`reach[]`是`O(n)`，但是还是可能会去访问后续的元素（即使没有修改），导致需要的时间很长。空间复杂度`O(n)`。  
```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1)
            return true;
        bool *reach = new bool[n] {false};

        reach[0] = true;
        for (int i = 0; i < n; i++) {
            if (!reach[i])
                continue;
            for (int k = 1; k <= nums[i]; k++) {
                if (i + k >= n)
                    break;
                if (!reach[i + k])
                    reach[i + k] = true;
                if (i + k == n - 1) {       // 适当剪枝
                    delete []reach;
                    return true;
                }
            }
        }

        bool ans = reach[n - 1];
        delete []reach;
        return ans;
    }
};
```

## 2. 记录右侧最远距离
考虑题目要求，由于可走的长度是>=0的，因此可以直接记录最远的距离，而最远距离左侧的距离一定可达。  
当当前距离超过最远距离时，意味着当前距离无法到达。  
时间复杂度`O(n)`，空间复杂度`O(1)`。  

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1)
            return true;
        int farthest = 0;

        for (int i = 0; i < n; i++) {
            if (i > farthest)
                return false;
            farthest = farthest >= i + nums[i] ? farthest : i + nums[i];
            if (farthest >= n - 1)
                break;
        }

        return true;
    }
};
```