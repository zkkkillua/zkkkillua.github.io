---
title: 47.全排列 II
date: 2020-09-18 15:19:15
categories: 
- leetcode
tags: 
- 回溯
---
## 1. 回溯
类似的题目是46.全排列，数组中不包含可重复数字，所以直接对于每一位遍历每一个，选择然后回溯不选择。  
而这道题目的数组中包含重复数字，因此如果按照上述方法，会出现重复排列。  
如：  
```
    /   |   \  
   1    1    2      位置1 
  /\   /\    /\  
 1  2  1 2   1 1    位置2  
 |  |  | |   | |  
 2  1  2 1   1 1    位置3  
```
出现重复排列的原因是，对于当前位置，已经选择过的数字在之后又被重新选择了（但选择的不是同一个元素，只是它们的值相等）  
因此避免重复的方法就是，在当前位置，避免选择之前已经选择过的数字。  

想象在当前位置，第一次选择某个数字，则这个数字一定是所有相等的数字中，第一个在数组中未被选择的，选择它并置vis为true。  
在获得当前位置为这个数字得到的所有排列之后，当前位置的数字被重新选择，并将之前元素的vis置为false。  
如果选择到的元素还是相等的数字，则之后的排列一定是已经获得过的，并且可以发现它不是数组的相等数字中第一个未被选择的。  
因此算法是，先将数组排序，将相等的元素放在一起，然后dfs，选择元素时只选择前一个相等元素被选择过的。  
时间`O(n*n!)`，空间`O(n)`。  
```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return {};

        vector<bool> vis(n, false);
        vector<int> subAns;
        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());
        dfs(nums, vis, subAns, ans);

        return ans;
    }
private:
    void dfs(vector<int>& nums, vector<bool>& vis, vector<int>& subAns, vector<vector<int>>& ans) {
        int n = nums.size();
        if (subAns.size() == n) {
            ans.push_back(subAns);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1] && !vis[i - 1])
                continue;
            if (!vis[i]) {
                subAns.push_back(nums[i]);
                vis[i] = true;
                dfs(nums, vis, subAns, ans);
                subAns.pop_back();
                vis[i] = false;
            }
        }
    }
};
```