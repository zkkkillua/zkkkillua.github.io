---
title: 167.两数之和 II - 输入有序数组
date: 2020-07-20 11:11:28
categories: leetcode
tags: 
- 二分
- 双指针
---
## 1. 朴素
遍历每一个数字，然后从它右侧的数字中查找是否有数字满足要求。  
时间`O(n^2)`，空间`O(1)`。  
**超时。**  
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int i = 0, j = 0;
        bool flag = false;
        for (i = 0; i < n - 1; i++) {
            for (j = i + 1; j < n; j++) {
                if (numbers[i] + numbers[j] == target) {
                    flag = true;
                    break;
                }
            }
            if (flag)
                break;
        }
        
        return {i + 1, j + 1};
    }
};
```

## 2. 二分
利用数组是递增的特点，遍历每个数据，然后对它右侧的数据进行二分，判断是否满足target。  
时间`O(nlogn)`，空间`O(1)`。  
**超时。**  
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int i, j;
        for (i = 0; i < n - 1; i++) {
            int l = i + 1, r = n - 1;
            bool flag = false;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (numbers[i] + numbers[mid] == target) {
                    j = mid;
                    flag = true;
                    break;
                } else if (numbers[i] + numbers[mid] < target)
                    l++;
                else
                    r--;
            }
            if (flag)
                break;
        }

        return {i + 1, j + 1};
    }
};
```

## 3. 滑动窗口/双指针
初始化窗口的左右两侧分别为数组的起始和结束位置，然后向中间收窄。  
- `numbers[left] + numbers[right] < target, left++`  
- `numbers[left] + numbers[right] > target, right--`  
时间`O(n)`，空间`O(1)`。  
  

由于数组是递增的，还可以先用二分法确定右侧指针的位置，而不是默认从最右侧开始。  

*会不会移动过程中跳过答案？*  
不会，可以参考[削减矩形搜索空间](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/yi-zhang-tu-gao-su-ni-on-de-shuang-zhi-zhen-jie-fa/)  

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        while (l < r) {
            if (numbers[l] + numbers[r] == target)
                break;
            else if (numbers[l] + numbers[r] < target)
                l++;
            else
                r--;
        }

        return {l + 1, r + 1};
    }
};
```