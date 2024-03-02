---
title: 56.合并区间
date: 2020-04-16 15:18:18
categories: leetcode
tags:
---
## 1. 按左区间由小到大排序
时间复杂度需要排序`O(nlogn)`，空间复杂度存答案`O(n)`。 
```cpp
class Solution {
public:
    // static bool cmp(const vector<int>& a, const vector<int>& b) {
    //     if (a[0] < b[0])
    //         return true;
    //     else
    //         return false;
    // }

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if (n <= 1)
            return intervals;
        // sort(intervals.begin(), intervals.end(), cmp);
        sort(intervals.begin(), intervals.end());   // vector有比较操作符

        vector<vector<int> > ans;
        vector<int> cur(intervals[0]);
        int left = cur[0], right = cur[1];
        for (int i = 1; i < n; i++) {
            if (intervals[i][0] <= right)
                right = right >= intervals[i][1] ? right : intervals[i][1];
            else {
                ans.push_back({left, right});
                left = intervals[i][0];
                right = intervals[i][1];
            }
        }
        ans.push_back({left, right});

        return ans;
    }
};
```