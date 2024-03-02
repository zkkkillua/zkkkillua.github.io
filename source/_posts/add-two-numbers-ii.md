---
title: 445. 两数相加II
date: 2020-04-14 12:13:17
categories: leetcode
tags: 
- 栈
---
## 1. 利用栈使链表逆序
这道题可以是把链表逆序，变成低位到高位，也可以通过栈存储每一个节点，从而通过后入先出将链表逆序。  
对于逆序处理的问题，可以优先考虑栈。  
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> v1, v2;
        while (l1 != nullptr) {
            v1.push(l1->val);
            l1 = l1->next;
        }
        while (l2 != nullptr) {
            v2.push(l2->val);
            l2 = l2->next;
        }

        ListNode* ans = nullptr;
        int c = 0;
        while (!v1.empty() || !v2.empty() || c != 0) {
            int a = 0, b = 0;
            if (!v1.empty()) {
                a = v1.top();
                v1.pop();
            }
            if (!v2.empty()) {
                b = v2.top();
                v2.pop();
            }

            int d = a + b + c;
            ListNode* new_node = new ListNode(d % 10);
            c = d / 10;
            new_node->next = ans;
            ans = new_node;
        }

        return ans;
    }
};
```