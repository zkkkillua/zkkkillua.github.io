---
title: 331. 验证二叉树的前序序列化
date: 2021-03-12 10:47:02
categories: 
- leetcode
tags: 
- 栈
- 树
---
## 1. 辅助栈
使用一个辅助栈记录当前期待访问的是栈中元素的左子节点还是右子节点。  
如果栈顶记录的是左子节点，则修改为期待访问右子节点。  
如果栈顶记录的是右子节点，代表当前访问的节点是其右子节点，弹出栈顶。  
如果访问的是数字，将其入栈，之后访问的是它的子树。  
如果访问的是#，不入栈，因为其对应的栈顶节点的左子树或者右子树为空。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int n = preorder.length();
        if (n == 0 || (n > 1 && preorder[0] == '#'))
            return false;
        else if (n == 1 && preorder[0] == '#')
            return true;

        stack<bool> isLeft;
        int idx = 0;
        while (idx < n && preorder[idx] >= '0' && preorder[idx] <= '9')
            idx++;
        isLeft.push(true);
        
        while (!isLeft.empty() && idx < n) {
            if (preorder[idx] == ',') {
                idx++;
                continue;
            } else if (preorder[idx] == '#') {
                if (isLeft.top() == true)
                    isLeft.top() = false;   // stack.top() returns a "reference"
                else 
                    isLeft.pop();
                idx++;
            } else {
                while (idx < n && preorder[idx] >= '0' && preorder[idx] <= '9')
                    idx++;
                if (isLeft.top() == true) 
                    isLeft.top() = false;
                else 
                    isLeft.pop();
                isLeft.push(true);
            }
        }
        
        return isLeft.empty() && idx == n;
    }
};
```
  
## 2. 优化空间到`O(1)`
方法1中使用的栈记录了当前期待的是每个节点的左子树还是右子树，使得我们可以直接构建出这棵树。  
但实际上并不需要这么详细的信息，因为每个节点都是首先期待左子树，之后期待右子树，然后出栈。  
所以我们可以只用一个变量记录栈中节点期待的子树的总数目，当遇到下一个节点时，期待--。减小的期待可能是栈顶节点的左子树也可能是其右子树，但我们并不关心。  
所以将方法1中的栈改为一个整型变量`expect`，模拟一个虚拟栈即可。  
时间`O(n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int n = preorder.length();
        if (n == 0 || (n > 1 && preorder[0] == '#'))
            return false;
        else if (n == 1 && preorder[0] == '#')
            return true;

        int expect = 0;
        int idx = 0;
        while (idx < n && preorder[idx] >= '0' && preorder[idx] <= '9')
            idx++;
        expect += 2;
        
        while (expect > 0 && idx < n) {
            if (preorder[idx] == ',') {
                idx++;
                continue;
            } else if (preorder[idx] == '#') {
                expect--;
                idx++;
            } else {
                while (idx < n && preorder[idx] >= '0' && preorder[idx] <= '9')
                    idx++;
                expect--;
                expect += 2;
            }
        }
        
        return expect == 0 && idx == n;
    }
};
```