---
title: 21.合并两个有序链表
date: 2020-05-01 10:58:05
categories: leetcode
tags: 
- 双指针
---
## 1. 双指针
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ans = nullptr;
        ListNode* p = nullptr;
        while (l1 != nullptr || l2 != nullptr) {
            if (ans == nullptr) {
                if (l1 == nullptr || (l1 != nullptr && l2 != nullptr && l1->val > l2->val)) {
                    ans = new ListNode(l2->val);
                    l2 = l2->next;
                } else if (l2 == nullptr || (l1 != nullptr && l2 != nullptr && l1->val <= l2->val)) {
                    ans = new ListNode(l1->val);
                    l1 = l1->next;
                }
                p = ans;
                continue;
            }

            if (l1 == nullptr || (l1 != nullptr && l2 != nullptr && l1->val > l2->val)) {
                p->next = new ListNode(l2->val);
                p = p->next;
                l2 = l2->next;
            } else if (l2 == nullptr || (l1 != nullptr && l2 != nullptr && l1->val <= l2->val)) {
                p->next = new ListNode(l1->val);
                p = p->next;
                l1 = l1->next;
            }
        }

        return ans;
    }
};
```