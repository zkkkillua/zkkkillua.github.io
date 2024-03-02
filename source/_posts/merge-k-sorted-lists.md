---
title: 23.合并K个排序链表
date: 2020-04-26 14:03:49
categories: leetcode
tags: 
- 堆
---
## 1. 两个有序链表合并的扩展
每次比较k个链表，这样每合并出一个节点，就需要`O(k^2)`的时间。所以此处可以优化一下，使用堆就可以以`O(klogk)`的时间得到最小值，花费最大`O(k)`空间。  
为了获得堆顶弹出的元素来自的链表，所以还需要一起记录一下，可以用pair。  
插入一次需要`O(logk)`的时间，一共nk个元素都需要进出堆，所以时间复杂度为`O(nklogk)`。  

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        if (n == 0)
            return nullptr;

        // pair->first记录节点值，pair->second记录来自的链表的编号
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        vector<ListNode*> nextLocs(n);
        for (int i = 0; i < n; i++) {       // 初始化
            if (lists[i] != nullptr) {
                heap.push(make_pair(lists[i]->val, i));
                nextLocs[i] = lists[i]->next;
            } else 
                nextLocs[i] = nullptr;
        }

        if (heap.empty())
            return nullptr;
        pair<int, int> temp = heap.top();
        heap.pop();
        ListNode* ans = new ListNode(temp.first);
        ListNode* p = ans;
        if (nextLocs[temp.second] != nullptr) {
            heap.push(make_pair(nextLocs[temp.second]->val, temp.second));
            nextLocs[temp.second] = nextLocs[temp.second]->next;
        }
        while (!heap.empty()) {
            temp = heap.top();
            heap.pop();
            p->next = new ListNode(temp.first);
            p = p->next;
            if (nextLocs[temp.second] != nullptr) {
                heap.push(make_pair(nextLocs[temp.second]->val, temp.second));
                nextLocs[temp.second] = nextLocs[temp.second]->next;
            }
        }

        return ans;
    }
};
```