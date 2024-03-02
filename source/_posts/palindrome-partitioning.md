---
title: 131. 分割回文串
date: 2021-03-07 19:29:38
categories: 
- leetcode
tags: 
- 回溯
---
## 1. 回溯
类似“全排列”，对于每个子答案：  
1. 从规定的起点向后遍历所有的回文串  
2. 对于遍历到的每个回文串，添加到子答案数组中，然后起点向后移动，继续调用dfs  
3. 当返回时，弹出当前添加到子答案数组中的回文串，回到2，即添加下一个可能的答案  

时间复杂度`O(n * 2^n)`；这里n为输入字符串的长度，每一个位置可拆分，也可不拆分，尝试所有拆分的时间复杂度为`O(2^n`，判断每一个子串是否是回文子串，时间复杂度为`O(n)`  
当然也可以用`O(n^2)`的时间预处理计算出每一段子串s[i][j]是否回文，则之后可以以`O(1)`的时间获取，不过空间要增加到`O(n^2)`  
空间复杂度：`O(n)`，递归调用栈的深度  

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<string> subAns;
        vector<vector<string>> ans;
        dfs(s, subAns, ans, 0);

        return ans;
    }
private:
    bool isPalindromic(string s, int start, int end) {
        bool res = true;
        while (end > start) {
            if (s[start] != s[end]) {
                res = false;
                break;
            }
            start++;
            end--;
        }

        return res;
    }

    void dfs(string s, vector<string>& subAns, vector<vector<string>>& ans, int start) {
        int n = s.length();
        if (start == 0)
            subAns.clear();
        else if (start == n) {
            ans.push_back(subAns);
            return;
        }

        for (int i = start; i < n; i++) {
            if (isPalindromic(s, start, i)) {
                subAns.push_back(s.substr(start, i - start + 1));
                dfs(s, subAns, ans, i + 1);
                subAns.pop_back();
            }
        }
    }
};
```