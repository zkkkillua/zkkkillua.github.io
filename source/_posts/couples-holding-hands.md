---
title: 765. 情侣牵手
date: 2021-02-14 21:09:55
categories: 
- leetcode
tags: 
- 并查集
---
## 1. 并查集
有1对情侣时，需要交换0次。  
有2对情侣交叉坐时，需要交换1次。  
有3对情侣交叉坐时，需要交换2次。  
...  
有k对情侣交叉坐时，需要交换k-1次。  
因为有k对情侣交叉坐时，交换1次可以使且仅使1对情侣牵手，剩余k-1对情侣交叉坐，以此类推。  
交换1次仅能使1对情侣牵手，因为如果可以使2对情侣牵手，剩余k-2对情侣交叉坐，则之前不是k对情侣交叉坐的。  
  
因此考虑使用并查集，每次遍历两个位置，并获取他们所属的组别。组别是值/2，如0和1属于0组，2和3属于1组...  
判断二者组别如果一致，则跳过；否则使用并查集将二者的组别合并，合并成为1个连通分支。同一个连通分支中的各个数据一定是多组同队情侣交叉分散在不同的位置上。  
最终答案为每个连通分支中`情侣对数 - 1的和`，实际上也等于`总情侣对数 - 连通分支数`，而后者更容易计算。  
时间`O(n)`，空间`O(n)`。  
```cpp
class UnionFind {
public:
    UnionFind (int n) {
        // parent.reserve(n);       // reserve()只预留空间，不修改size，故修改后不能直接访问
        parent.resize(n);
        cnt = n;
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find (int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int a, int b) {
        int pa = find(a), pb = find(b);
        if (pa != pb) {
            parent[pb] = pa;
            cnt--;
        }
    }

    int getCnt() {
        return cnt;
    }
private:
    vector<int> parent;
    int cnt;    // 连通分支数
};

class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int n = row.size();
        UnionFind uf(n);

        for (int i = 0; i < n; i += 2) {
            int group1 = row[i] / 2, group2 = row[i + 1] / 2;
            if (group1 != group2)
                uf.unite(group1, group2);
        }

        return n / 2 - uf.getCnt();
    }
};
```