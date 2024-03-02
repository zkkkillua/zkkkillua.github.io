---
title: 142.环形链表 II
date: 2020-10-10 21:39:23
categories: 
- leetcode
tags: 
- 双指针
---

## 1. hash表
遍历链表，使用hash表记录途中的节点，直到到达链表尾或者出现hash表中储存的节点，该节点即为环的入口。  
时间`O(n)`，空间`O(n)`。  
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
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> table;
        ListNode* ans = nullptr;

        while (head != nullptr) {
            if (table.count(head)) {
                ans = head;
                break;
            }
            table.insert(head);
            head = head->next;
        }

        return ans;
    }
};
```

## 2. 双指针
参考“[关于环形链表的一切](https://zkkkillua.github.io/circular-linked-list/)”。  
设置快指针速度为2，慢指针速度为1，首先获得二者的相遇点（如果有环的话），然后另设一个速度为1的指针从起点出发，与慢指针同步前进，二者的相遇位置即为环的入口。  
时间`O(n)`，空间`O(1)`。  
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
    ListNode *detectCycle(ListNode *head) {
        ListNode* meet = meetPoint(head);
        ListNode* slow = head;
        while (meet != nullptr && slow != meet) {
            slow = slow->next;
            meet = meet->next;
        }

        return meet;
    }
private:
    ListNode* meetPoint(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        bool meet = false;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                meet = true;
                break;
            }
        }

        return meet ? slow : nullptr;
    }
};
```