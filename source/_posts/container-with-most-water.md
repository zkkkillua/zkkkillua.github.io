---
title: 11.Container With Most Water
date: 2020-04-18 12:19:57
categories: leetcode
tags: 
- 双指针
---
## 1. 双指针
两个指针初始时在左右两侧，逐渐向内靠拢。  
每次两个指针形成的容器，最小的那个是瓶颈，接下来需要向内移动瓶颈或非瓶颈的指针。  
如果保持瓶颈指针不动，向内移动非瓶颈指针，由于宽度减小，并且无论非瓶颈指针向内移动后得到的边界是大是小，容器的总容积总是减小（一定受瓶颈指针的影响）  
因此需要向内移动瓶颈指针，这样才可能遇到更大的容积。  
时间复杂度`O(n)`，空间复杂度`O(1)`.  
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int left = 0, right = n - 1;
        int ans = (right - left) * min(height[left], height[right]);

        while (left < right) {
            if (height[left] < height[right])
                left++;
            else if (height[left] == height[right]) {
                left++;
                right--;
            }
            else
                right--;
            ans = max(ans, (right - left) * min(height[left], height[right]));
        }

        return ans;
    }
};
```