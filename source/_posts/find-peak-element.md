---
title: 162.寻找峰值
date: 2020-07-18 23:39:39
categories: leetcode
tags: 
- 二分
---
## 1. 二分
要求复杂度是`O(logn)`，说明了是要二分。  
结果只要求一个值，因此二分到`nums[i-1] < nums[i] < nums[i+1]`的i即可。  

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int ans = 0;
        
        while (l <= r) {
            int mid = (l + r) / 2;
            if (l == r)
                ans = l++;
            else if (mid > 0 && nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) {
                ans = mid;
                break;
            } else if (nums[mid] < nums[mid + 1])
                l = mid + 1;
            else if (nums[mid] > nums[mid + 1])
                r = mid - 1;
        }

        return ans;
    }
};
```