---
title: 117. 填充每个节点的下一个右侧节点指针 II
date: 2020-09-29 16:20:20
categories: 
- leetcode
tags: 
- 树
---
## 1. 层次遍历
层次遍历获得同一层的节点，然后依次让next指向右侧的节点。  
时间`O(n)`，空间`O(n)`。  
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr)
            return nullptr;

        queue<Node*> q;
        Node* cur = root;
        q.push(cur);
        while (!q.empty()) {
            int n = q.size();
            while (n-- > 0) {
                cur = q.front();
                q.pop();
                if (cur->left != nullptr)
                    q.push(cur->left);
                if (cur->right != nullptr)
                    q.push(cur->right);
                if (n > 0)
                    cur->next = q.front();
            }
        }

        return root;
    }
};
```
  
## 2. 迭代
通过上一层已经构造好的next指针获取下一层新的节点，并不断修改下一层节点的next值。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr)
            return nullptr;

        Node* lastLayer = root;
        Node* cur = nullptr;
        curHead = nullptr;
        while (lastLayer != nullptr) {
            while (lastLayer != nullptr) {
                if (lastLayer->left != nullptr) {
                    if (cur == nullptr) {
                        cur = lastLayer->left;
                        curHead = cur;
                    } else {
                        cur->next = lastLayer->left;
                        cur = cur->next;
                    }
                }
                if (lastLayer->right != nullptr) {
                    if (cur == nullptr) {
                        cur = lastLayer->right;
                        curHead = cur;
                    } else {
                        cur->next = lastLayer->right;
                        cur = cur->next;
                    }
                }
                lastLayer = lastLayer->next;
            }
            cur = nullptr;
            lastLayer = curHead;
            curHead = nullptr;
        }

        return root;
    }
};
```