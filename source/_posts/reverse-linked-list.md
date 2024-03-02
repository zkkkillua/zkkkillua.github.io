---
title: 206.Reverse Linked List
date: 2020-03-15 21:32:09
categories: leetcode
tags:
---
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
________________________

## 框架
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
    ListNode* reverseList(ListNode* head) {

    }
};
```

## 1. Iteratively
(1). 建立新的反向链表。记得所有的结点都得是`new`的，不然一返回就被清空了。  
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
    ListNode* reverseList(ListNode* head) {
        ListNode* rev = NULL;
        ListNode* iter = head;
        while (iter != NULL) {
            ListNode* newNode = new ListNode(iter->val);
            newNode->next = rev;
            rev = newNode;
            iter = iter->next;
        }
        
        return rev;
    }
};
```

(2). 在原有链表基础上直接反向。  
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
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = NULL;
        ListNode* pre = head;
        while (pre != NULL) {
            ListNode* temp = pre->next;
            pre->next = cur;
            cur = pre;
            pre = temp;
        }
        
        return cur;
    }
};
```

## 2. Recursively
ABCDEF的逆序`(ABCDEF)逆`就相当于`A <- (BCDEF)逆`.
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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        ListNode* revHead = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;

        return revHead;
    }
};
```