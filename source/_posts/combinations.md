---
title: 77. 组合
date: 2020-09-08 16:29:41
categories: leetcode
tags: 
- 回溯
---
## 1. 递归
n中选k个数，可以看作在对当前的数进行选择或放弃之后，在剩余的n-1个数中选k或k-1个数。  
时间`O(k*C(n, k))`，空间`O(n)`递归栈。  
```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        return selection(1, n, k);
    }

private:
    vector<vector<int>> selection(int begin, int end, int k) {
        if (begin > end || k <= 0 || end - begin + 1 < k)
            return {};
        
        vector<vector<int>> ans, subAns;
        // choose begin
        subAns = selection(begin + 1, end, k - 1);
        for (int i = 0; i < subAns.size(); i++)
            subAns[i].insert(subAns[i].begin(), begin);
        if (subAns.empty())
            subAns = {{begin}};
        ans.insert(ans.end(), subAns.begin(), subAns.end());
        
        // not choose begin
        subAns = selection(begin + 1, end, k);
        ans.insert(ans.end(), subAns.begin(), subAns.end());

        return ans;
    }
};
```

## 2. dfs
方法1的思路是利用递归思想，找到一系列更短的组合。  
另一种思想是每次直接找定长为k的组合序列，类似于dfs，判断长度到达k时直接储存结果。  
时间`O(k*C(n, k))`，空间`O(n)`递归栈。  
```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        dfs(1, n, k);
        return ans;
    }

private:
    void dfs(int start, int end, int k) {
        if (k <= 0 || subAns.size() + end - start + 1 < k)
            return;
        
        if (subAns.size() == k) {
            ans.push_back(subAns);
            return;
        }

        for (int i = start; i <= end; i++) {
            subAns.push_back(i);
            dfs(i + 1, end, k);
            subAns.pop_back();
        }
    }
    vector<int> subAns;
    vector<vector<int>> ans;
};
```