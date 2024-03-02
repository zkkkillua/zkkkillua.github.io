---
title: 1111. 有效括号的嵌套深度
date: 2020-04-01 18:30:03
categories: leetcode
tags:
---
## 框架
```cpp
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {

    }
};
```

## 1. 直接模拟
首先遍历一遍获得最大深度`maxDepth`，若想令`max(depth(A), depth(B))`的可能取值最小，则结果必为`(maxDepth+1)/2`。  
因此再次遍历序列，将深度小于最大深度一半的括号都分到A类中，之后的括号除去与A左括号匹配的右括号之外，其余全部放入B类中。  
时间复杂度`O(n)`。  
```cpp
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int n = seq.length();
        int maxDepth = 0, curDepth = 0;
        for (int i = 0; i < n; i++) {
            if (seq[i] == '(')
                curDepth++;
            else {
                maxDepth = maxDepth >= curDepth ? maxDepth : curDepth;
                curDepth--;
            }
        }

        int halfDepth = (maxDepth + 1) / 2;
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            if (seq[i] == '(') {
                curDepth++;
                if (curDepth <= halfDepth)
                    ans[i] = 0;
                else 
                    ans[i] = 1;
            }
            else {
                if (curDepth <= halfDepth)
                    ans[i] = 0;
                else
                    ans[i] = 1;
                curDepth--;
            }
        }

        return ans;
    }
};
```