---
title: 1248.统计「优美子数组」
date: 2020-04-21 23:21:26
categories: leetcode
tags: 
- 滑动窗口
---
## 1. 滑动窗口
```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        if (n < k)
            return 0;

        int left = 0, right = 0, ans = 0;
        int oddcount = nums[0] % 2 == 1 ? 1 : 0;
        int leftcount = 0, rightcount = 0;
        while (left < n) {
            if (oddcount == k) {
                while (right < n - 1 && nums[right + 1] % 2 == 0) {
                    right++;
                    rightcount++;
                }
                while (left <= right && left < n - 1 && nums[left] % 2 == 0) {
                    left++;
                    leftcount++;
                }
                ans += (leftcount + 1) * (rightcount + 1);
                leftcount = 0;
                rightcount = 0;

                if (right < n - 1) {
                    right++;
                    oddcount++;
                }
                if (left <= right && left < n - 1) {
                    left++;
                    oddcount--;
                } else if (left == n - 1)
                    break;
            }

            if (oddcount < k && right < n - 1) {
                right++;
                if (nums[right] % 2 == 1)
                    oddcount++;
            } else if (oddcount < k && right >= n - 1)
                break;
        }

        return ans;
    }
};
```