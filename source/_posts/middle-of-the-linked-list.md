---
title: 876.Middle of the Linked List
date: 2020-03-23 17:17:07
categories: leetcode
tags: 
- 双指针
---
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
__________________________________

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
    ListNode* middleNode(ListNode* head) {

    }
};
```

## 1. 遍历
先遍历一次获取长度，然后遍历到中间位置。时间`O(n)`，空间`O(1)`。  
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
    ListNode* middleNode(ListNode* head) {
        int len = 0;
        ListNode *ans = head;
        while (ans != NULL) {
            len++;
            ans = ans->next;
        }

        ans = head;
        for (int i = 0; i < len / 2; i++)
            ans = ans->next;
        
        return ans;
    }
};
```

## 2. 快慢指针
新学的。快慢指针还可以用来判断一个链表中是否有环（根据快慢指针能否相遇来判断）  
快指针走2步，慢指针走1步，这样的话慢指针停止的时候指向的就是链表中点。时间`O(n)`，空间`O(1)`。  
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
    ListNode* middleNode(ListNode* head) {
        ListNode *fast = head, *slow = head;
        //星花还是跟变量呆在一起吧，表示*fast是ListNode类型。连续定义指针的话*得在变量上。
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```