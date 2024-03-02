---
title: 2. Add Two Numbers
date: 2020-03-07 19:34:01
categories: leetcode
tags:
---
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
_______________________

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
    }
};
```

## 1. 遍历得到数据，相加后直接修改成符合条件的链表格式，O(n)
**………………溢出了，只能模拟了**
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
        int n1 = 0, n2 = 0, sum = 0;
        ListNode *iter1 = l1;
        ListNode *iter2 = l2;
        int pw1 = 0, pw2 = 0;

        while(iter1 != NULL){
            n1 += (iter1->val * pow(10, pw1++));
            iter1 = iter1->next;
        }
        while(iter2 != NULL){
            n2 += (iter2->val * pow(10, pw2++));
            iter2 = iter2->next;
        }

        sum = n1 + n2;
        ListNode *ans = new ListNode(sum % 10);
        sum /= 10;
        ListNode *iter = ans;
        while(sum != 0){
            iter->next = new ListNode(sum % 10);
            sum /= 10;
            iter = iter->next;
        }

        return ans;
    }
};
```

## 2. 模拟
链表头是低位，链表尾是高位，可以两条链对应从低位向高位做加法，用temp记录进位。`O(n)`  
*提交错了好几次，主要是因为没有处理好长度之间的关系。*  
*比如一条链结束了，直接把另一条链接到ans链上了，但是这个时候还可能temp是有值的，需要继续加*
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
        ListNode *iter1 = l1;
        ListNode *iter2 = l2;
        int temp = iter1->val + iter2->val;
        iter1 = iter1->next;
        iter2 = iter2->next;
        ListNode *ans = new ListNode(temp % 10);
        temp /= 10;
        ListNode *iter = ans;

        while(iter1 != NULL || iter2 != NULL || temp != 0){
            int v1 = 0, v2 = 0;
            if(iter1 != NULL){
                v1 = iter1->val;
                iter1 = iter1->next;
            }
            if(iter2 != NULL){
                v2 = iter2->val;
                iter2 = iter2->next;
            }

            //对啊，上边这个其实不用这么麻烦，直接判断，如果是NULL不加就可以了，没必要再定义变量

            temp += (v1 + v2);

            iter->next = new ListNode(temp % 10);
            temp /= 10;
            iter = iter->next;
        }

        return ans;
    }
};
```