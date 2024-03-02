---
title: 1095.山脉数组中查找目标值
date: 2020-04-29 16:01:21
categories: leetcode
tags: 
- 二分
---
## 1. 二分
~~二分，然后根据左右大小关系判断是上升还是下降，选择不同部分继续二分就好了。~~  
本来打算一次二分做的，不过发现当`nums[mid] > target`时，两侧部分都需要进行二分。  
所以还是先二分找到分界点，然后再二分左侧和右侧吧，最多是3次二分。  
```cpp
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        int left = 0, right = n - 1;
        int ans = -1;
        int topIndex = -1, topValue = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            int midv = mountainArr.get(mid);
            int midrv = mountainArr.get(mid + 1);
            if (midv < midrv) {
                left = mid + 1;
                topIndex = mid + 1;
                topValue = midrv;
            }
            else {
                int midlv = mountainArr.get(mid - 1);
                if (midv < midlv) {
                    right = mid - 1;
                    topIndex = mid - 1;
                    topValue = midlv;
                } else {
                    topIndex = mid;
                    topValue = midv;
                    break;
                }
            }
        }

        if (target > topValue)
            return -1;
        else if (target == topValue)
            return topIndex;

        left = 0;
        right = topIndex;
        while (left <= right) {
            int mid = (left + right) / 2;
            int midv = mountainArr.get(mid);
            if (midv == target) {
                ans = mid;
                break;
            } else if (midv < target) 
                left = mid + 1;
            else
                right = mid - 1;
        }
        if (ans != -1)
            return ans;
        
        left = topIndex + 1;
        right = n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int midv = mountainArr.get(mid);
            if (midv == target) {
                ans = mid;
                break;
            } else if (midv < target)
                right = mid - 1;
            else
                left = mid + 1;
        }

        return ans;
    }
};
```