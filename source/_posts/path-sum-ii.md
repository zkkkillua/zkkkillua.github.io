---
title: 113.路径总和 II
date: 2020-09-27 16:46:09
categories: 
- leetcode
tags: 
- 树
- 回溯
---
## 1. 递归+回溯
类似于“112.路经总和”，不过要记录路径上的各个点。  
只需要在原有递归访问子节点并修改目标值的基础上，增加把当前节点加入数组的过程即可，在回到上一层时需要回溯。  
时间`O(n^2)`，空间`O(n^2)`  
```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        dfs(root, sum);
        return ans;
    }
private:
    void dfs(TreeNode* root, int sum) {
        if (root == nullptr)
            return;
        
        subAns.push_back(root->val);

        if (root->left == nullptr && root->right == nullptr && root->val == sum) 
            ans.push_back(subAns);

        if (root->left != nullptr) 
            dfs(root->left, sum - root->val);
        if (root->right != nullptr)
            dfs(root->right, sum - root->val);
        
        subAns.pop_back();
    }
    vector<int> subAns;
    vector<vector<int>> ans;
};
```

## 2. 迭代
层次遍历的访问方法，同“112.路径总和”的迭代访问一样，使用队列同时暂存对应的节点和当前目标值。  
此外，由于这道题还需要获得具体路径，因此还需要一个额外的队列记录开头到当前节点的路径。  

这样的问题在于使用了较多的空间存储了较多重复还不一定有用的路径。  
可以考虑最后确定路经总和能够到达目标值时，再寻找根到叶子结点的路径。  
为了方便路径的寻找，可以使用hash表记录每个节点的根节点，从叶子节点出发直接一路找到根节点。  

另外此处需要扩展的是，使用hash表需要提供hash函数的问题。  
- **自建类型**使用hash表是**需要**提供hash函数的，比如`unordered_map<pair<int, int>, int> m`就会报错，因为没提供pair类型的hash函数。  
- 而**自建类型的指针**是**不需要**的，比如`unordered_map<pair<int, int>*, int> m`就没有问题，同时指针不论指向何种类型，大小都是一样的。  
  

时间`O(n^2)`，空间`O(n^2)`。  
```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if (root == nullptr)
            return {};
        
        parent[root] = nullptr;
        queue<pair<TreeNode*, int>> q;
        q.emplace(root, sum);
        while (!q.empty()) {
            TreeNode* cur = q.front().first;
            int curSum = q.front().second;
            q.pop();
            
            if (cur->left == nullptr && cur->right == nullptr && cur->val == curSum)
                ans.push_back(getPath(cur));
            if (cur->left != nullptr) {
                parent[cur->left] = cur;
                q.emplace(cur->left, curSum - cur->val);
            }
            if (cur->right != nullptr) {
                parent[cur->right] = cur;
                q.emplace(cur->right, curSum - cur->val);
            }
        }

        return ans;
    }
private:
    vector<int> getPath(TreeNode* node) {
        vector<int> path;
        while (node != nullptr) {
            path.push_back(node->val);
            node = parent[node];
        }
        reverse(path.begin(), path.end());      //#include <algorithm>
        
        return path;
    }
    vector<vector<int>> ans;
    unordered_map<TreeNode*, TreeNode*> parent;
};
```