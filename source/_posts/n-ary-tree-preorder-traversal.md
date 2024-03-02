---
title: 589.N叉树的前序遍历
date: 2020-05-13 17:46:22
categories: leetcode
tags: 
- 树
---
## 相关
1. 二叉树的前序遍历：144
2. 二叉树的中序遍历：94
3. 二叉树的后序遍历：145
4. N叉树的后序遍历：590

## 1. 递归
跟二叉树一样，时间`O(n)`，空间`O(n)`。  
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> preorder(Node* root) {
        if (root == nullptr)
            return {};
        
        vector<int> ans;
        ans.push_back(root->val);
        for (int i = 0; i < root->children.size(); i++) {
            vector<int> subArray = preorder(root->children[i]);
            ans.insert(ans.end(), subArray.begin(), subArray.end());
        }

        return ans;
    }
};
```

## 2. 迭代
仿照二叉树的前序遍历的迭代实现方式。  
访问根节点  -> 将右部分的节点按照从右往左的顺序入栈 -> 左节点入栈 ->  
同样，我们还是可以将左节点入栈出栈的部分省去。  
时间`O(n)`，空间`O(n)`.  
```cpp
class Solution {
public:
    vector<int> preorder(Node* root) {
        stack<Node*> st;
        vector<int> ans;
        while (!st.empty() || root != nullptr) {
            if (root == nullptr) {
                root = st.top();
                st.pop();
            }
            ans.push_back(root->val);
            for (int i = root->children.size() - 1; i > 0; i--)
                st.push(root->children[i]);
            root = root->children.empty() ? nullptr : root->children[0];
        }

        return ans;
    }
};
```