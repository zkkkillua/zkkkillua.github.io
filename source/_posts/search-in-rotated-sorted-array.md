---
title: 33.搜索旋转排序数组
date: 2020-04-27 12:17:48
categories: leetcode
tags: 
- 二分
---
## 1. 二分查找
通过左和中的大小关系判断是升序还是中间旋转了。  
时间`O(logn)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0)
            return -1;
        
        int ans = -1;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[left] > target) {
                if (nums[mid] >= nums[left])
                    left = mid + 1;
                else {
                    if (nums[mid] > target)
                        right = mid - 1;
                    else if (nums[mid] < target)
                        left = mid + 1;
                    else {
                        ans = mid;
                        break;
                    }
                }
            } else if (nums[left] < target) {
                if (nums[mid] >= nums[left]) {
                    if (nums[mid] > target)
                        right = mid - 1;
                    else if (nums[mid] < target)
                        left = mid + 1;
                    else {
                        ans = mid;
                        break;
                    }
                } else 
                    right = mid - 1;
            } else {
                ans = left;
                break;
            }
        }

        return ans;
    }
};
```