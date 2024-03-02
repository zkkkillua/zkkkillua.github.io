---
title: 590.N叉树的后序遍历
date: 2020-09-16 10:10:06
categories: 
- leetcode
tags: 
- 树
---

## 相关
1. 二叉树的前序遍历：144
2. 二叉树的中序遍历：94
3. 二叉树的后序遍历：145
4. N叉树的前序遍历：589

## 1. 递归
时间`O(n)`，空间`O(n)`。  
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
    vector<int> postorder(Node* root) {
        vector<int> ans;
        postorder(ans, root);
        return ans;
    }
private:
    void postorder(vector<int>& ans, Node* root) {
        if (root == nullptr)
            return;
        for (int i = 0; i < root->children.size(); i++)
            postorder(ans, root->children[i]);
        ans.push_back(root->val);
    }
};
```

## 2. 迭代
1. 访问到一个root节点时，将其子节点从右到左移次放入栈中。  
2. `root = root->children[0], if(!(root->children.empty())`
3. 当root为空时，并且栈顶元素的右子树已访问完毕时（使用nullptr入栈作为标记或者pre记录上一次访问的指针并与root的最右子节点比较），取栈顶元素访问；当栈顶元素的子节点还未被访问时，到1.
这里相比于145.二叉树的后序遍历的一点不同是需要将子节点自右向左放入栈中。  
实际上二叉树的后序遍历也是需要将子节点自右至左放入栈中，即先放右节点，再放左节点。但是由于在判断栈顶元素的右子节点还未访问时，需要将右子节点入栈，因此这两个过程就合并起来了。  
而在N叉树的后序遍历中，由于不方便记录到底是访问到了root的哪一个子节点，所以最好还是在开始时就将子节点自右向左存入栈中。  
```cpp
class Solution {
public:
    vector<int> postorder(Node* root) {
        if (root == nullptr)
            return {};
        vector<int> ans;
        stack<Node*> st;
        st.push(root);

        Node* pre = nullptr;
        while (root != nullptr || !st.empty()) {
            if (root == nullptr) {
                Node* temp = st.top();
                if (temp->children.empty() || pre == temp->children[temp->children.size() - 1]) {
                    st.pop();
                    ans.push_back(temp->val);
                    pre = temp;
                } else
                    root = temp;
            } else {
                for (int i = root->children.size() - 1; i >= 0; i--)
                    st.push(root->children[i]);
                root = root->children.empty() ? nullptr : root->children[0];
            }
        }

        return ans;
    }
};
```