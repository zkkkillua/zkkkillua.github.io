---
title: 42.接雨水
date: 2020-04-07 14:08:40
categories: leetcode
tags: 
- dp
- 栈
---
## 框架
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        
    }
};
```

## 1. 按列计算+dp
首先想到的是计算出一个“坑”，然后算这个坑可以储存多少水。  
但实际上也可以按列计算，计算每一列可以储存多少水，然后求和。  
算每一列存水的数量的方法就是找到该位置左侧的最大值和右侧的最大值，从而围成一个“坑”。  
所以：遍历每一个柱子，然后查找其左侧的最大值和右侧的最大值，时间复杂度是`O(n^2)`。  
可以使用记忆化搜索，`leftIndex[i]`和`rightIndex[i]`分别记录第i个元素左侧的最大高度的索引和右侧最大高度的索引。  
转移方程为`leftIndex[i] = i-1 || leftHeight[i-1]`  
这样，时间复杂度就降低为`O(n)`，而空间复杂度升高为`O(n)`。  
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int ans = 0;

        vector<int> leftIndex(n, 0), rightIndex(n, n - 1);
        for (int i = 1; i < n - 1; i++) {
            leftIndex[i] = height[leftIndex[i - 1]] >= height[i - 1] ? leftIndex[i - 1] : i - 1;
            rightIndex[n - i - 1] = height[rightIndex[n - i]] >= height[n - i] ? rightIndex[n - i] : n - i;
        }

        for (int i = 1; i < n - 1; i++) {
            int minHeight = min(height[leftIndex[i]], height[rightIndex[i]]);
            if (minHeight > height[i])
                ans += minHeight - height[i];
        }

        return ans;
    }
};
```

## 2. 单调栈
要形成一个坑，则高度要先降低后升高。  
之前的想法是先降低后升高，再降低的时候说明右边界已经达到了，取左右边界的最小值，重新遍历中间的部分，进行积水。然后以右边界为新的左边界，继续上述操作。  
然而这样的问题是，坑可能是`W`型的，中间有较低的突起，却以它为边界了，这样积水操作就算错了。  

**为什么使用单调栈？**  
上述操作的弊端是，只能够根据升高后再降低确定到一个右边界，却无法对应地处理这个右边界高度可以积累的雨水。  
如果使用一个容器，记录下从左边界到右边界的柱子高度值，则可以只弹出右侧部分柱子，与当前右边界组合进行积水，而后续遇到更高的右边界可能继续弹出并积水。  
如果容器种记录的是`3,5`，则这个`3`是无效的，因为和左边界组合积水，5比3大，所以不可能取3了。  
因此这里就可以选用*单调递减栈*。  

当遇到的元素<=栈顶元素时，入栈，保持栈的非递增性。  
当遇到的元素>栈顶元素时，出栈，计算出栈的元素和右侧当前元素组成的坑可以储存的水。重复操作直到栈顶元素<=当前元素。  
为了便于获取宽度，栈中储存的是索引。  
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        stack<int> index;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (index.empty())
                index.push(i);
            else {
                if (height[i] <= height[index.top()])
                    index.push(i);
                else {
                    while (height[i] > height[index.top()]) {
                        int left = index.top();
                        index.pop();
                        if (index.empty())
                            break;
                        ans += (min(height[index.top()], height[i]) - height[left]) * (i - index.top() - 1);
                    }
                    index.push(i);
                }
            }
        }

        return ans;
    }
};
```