---
title: 96.不同的二叉搜索树
date: 2020-07-15 18:22:07
categories: leetcode
tags: 
- 树
- dp
---
## 1. 动态规划
设`G(n)`是以1 ... n为节点组成的二叉搜索树的种数，`f(i)`是以i为根节点的二叉搜索树的种数，则有：  
`G(n) = f(1) + f(2) + ... + f(n)`  
以`f(i)`为例，其左子树为1 ... i-1节点组成的二叉搜索树，右子树为i+1 ... n节点组成的二叉搜索树，即  
`f(i) = G(i - 1) * G(n - i)`  
综上，有：
`G(n) = G(0)G(n-1) + G(1)G(n-2) + ... + G(n-1)G(0)`  
时间复杂度：`(n^2)`，需要算n个`G(i)`，每个需要`O(n)`。  
空间复杂度：`O(n)`。  

```cpp
class Solution {
public:
    int numTrees(int n) {
        int* g = new int[n + 1]();
        // new的过程是 分配空间 - 使用默认构造函数初始化
        // 而对于内置数据类型，new仅分配内存而不进行初始化，需要加()表示进行初始化
        // int* a = new int [10](1, 2) 之类的这种在()内部指定值的方法是错误的
        // 上一行的()可以改为{}代表列表初始化
        g[0] = 1;
        g[1] = 1;

        for (int i = 2; i <= n; i++)
            for (int j = 0; j < i; j++)
                g[i] += g[j] * g[i - 1 - j];

        int ans = g[n];
        delete []g;

        return ans;
    }
};
```