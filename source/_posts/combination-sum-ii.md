---
title: 40.组合总和II
date: 2020-09-11 10:40:30
categories: leetcode
tags: 
- 回溯
---
## 1. 递归+回溯
39.组合总和是无重复数字，可重复使用；这道题是有重复数字，不可重复使用。  
如果直接按照普通的回溯做，是可能出现重复组合的。  
比如[1, 1, 3, 1]和4，会出现3组[1, 3]的组合。  

解决方法是排序后，每一层级的相同数字只使用第一个元素向后扫描一次。  
如[1, 2, 3, 2, 2]和5，首先排序为[1, 2, 2, 2, 3]，排序的目的是为了能够得到一连串的相同元素。  
在普通的递归和回溯的过程中，框架一般如下：  
```cpp
for (int i = begin; i < end; i++) {
    subAns.push_back(candidates[i]);
    dfs(i, end, k - candidates[i]);
    subAns.pop_back();
}
```
问题就出在循环上，比如已经得到了[1, 2, 2]，然后又弹出2，通过循环又加入了下一个2.  
但实际上只加入当前层级（即i == begin时）中相等元素的第一个就足够了，因为如果不需要当前的元素，则后面相等的元素也不会被需要，可以直接跳过；如果需要当前的元素，则后面剩余元素组合产生的可能解一定包含弹出当前元素再选择下一个元素再使用后面剩余元素组合产生解的个数多。  
所以调整之后的框架是  
```cpp
for (int i = begin; i < end; i++) {
    // i == begin是当前层级的第一个元素，所以不能跳过
    if (i > begin && candidates[i] == candidates[i - 1])    // 同一层级 && 前面已经求解
        continue;           // 直接跳过
    subAns.push_back(candidates[i]);
    dfs(i, end, k - candidates[i]);
    subAns.pop_back();
}
```

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        int n = candidates.size();
        sort(candidates.begin(), candidates.end());
        dfs(candidates, 0, target);
        
        return ans;
    }
private:
    void dfs(vector<int>& candidates, int begin, int k) {
        if (k < 0)
            return;
        else if (k == 0) {
            ans.push_back(subAns);
            return;
        }

        int n = candidates.size();
        for (int i = begin; i < n; i++) {
            if (i > begin && candidates[i] == candidates[i - 1])
                continue;
            subAns.push_back(candidates[i]);
            dfs(candidates, i + 1, k - candidates[i]);
            subAns.pop_back();
        }
    }
    vector<int> subAns;
    vector<vector<int>> ans;
};
```