---
title: 面试题57 - II. 和为s的连续正数序列
date: 2020-03-23 17:44:28
categories: leetcode
tags: 
- 双指针
---
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
____________________________

## 框架
```cpp
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {

    }
};
```

## 1. 双指针
小了r++，大了l++
```cpp
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        int left = 1, right = 1;
        int sum = 1;
        vector<vector<int> > ans;
        while (left <= right) {
            if (sum < target) {
                right++;
                sum += right;
            } else if (sum > target) {
                sum -= left;
                left++;
            } else {
                vector<int> group;
                for (int i = left; i <= right; i++)
                    group.push_back(i);
                ans.push_back(group);
                left++;
                right++;
                sum = sum - left + right + 1;
            }

            if (left > target / 2)
                break;
        }

        return ans;
    }
};
```