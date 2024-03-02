---
title: 145.二叉树的后序遍历
date: 2020-09-16 10:12:15
categories: 
- leetcode
tags: 
- 树
---

## 相关
1. 二叉树的前序遍历：144
2. 二叉树的中序遍历：94
3. N叉树的前序遍历：589
4. N叉树的后序遍历：590

## 1. 递归
左右根  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        postorderTraversal(ans, root);
        return ans;
    }
private:
    void postorderTraversal(vector<int>& ans, TreeNode* root) {
        if (root == nullptr)
            return;
        postorderTraversal(ans, root->left);
        postorderTraversal(ans, root->right);
        ans.push_back(root->val);
    }
};
```

## 2. 迭代
1. 左左左，放入栈中

2. 当`root == nullptr`时，取栈顶元素，如果当前栈顶元素的right不为nullptr，则放回栈顶元素，令`root = top->right`，回到1。（实际上就相当于先不弹出栈顶元素）

3. 但是只这样写的代码是可能陷入死循环的，原因是right访问完又回到父节点，而父节点又访问了right，造成循环。  
比如下面的错误代码：  
```
    1  
     \  
      2  
```
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;

        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                if (st.top()->right != nullptr)
                    root = st.top()->right;     // 此处死循环
                else {
                    root = st.top();
                    st.pop();
                    ans.push_back(root->val);
                    root = nullptr;
                }
            } else {
                st.push(root);
                root = root->left;
            }
        }

        return ans;
    }
};
```
**解决循环的方法：**  
1. 在访问栈顶的right前，push到栈中一个nullptr作为标记，当再次访问栈顶遇到nullptr时，说明次栈顶的right已访问过。  
2. 因为在栈中，root和root->right一定是相邻的（如果有的话），所以可以使用一个指针记录当前访问的地址，在需要取栈顶的right时，对比二者是否相等，可以得知是否已经访问过right。  

**方法1：**  
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;

        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                if (st.top() == nullptr) {
                    st.pop();
                    root = st.top();
                    st.pop();
                    ans.push_back(root->val);
                    root = nullptr;
                } else if (st.top()->right != nullptr) {
                    root = st.top()->right;
                    st.push(nullptr);
                } else if (st.top()->right == nullptr) {
                    root = st.top();
                    st.pop();
                    ans.push_back(root->val);
                    root = nullptr;
                }
            } else {
                st.push(root);
                root = root->left;
            }
        }

        return ans;
    }
};
```
**方法2：**  
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;

        TreeNode* pre = nullptr;
        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                if (st.top()->right != nullptr && st.top()->right != pre) 
                    root = st.top()->right;
                else {
                    root = st.top();
                    st.pop();
                    ans.push_back(root->val);
                    pre = root;
                    root = nullptr;
                }
            } else {
                st.push(root);
                root = root->left;
            }
        }

        return ans;
    }
};
```