---
title: 面试题59 - II. 队列的最大值
date: 2020-03-29 22:35:10
categories: leetcode
tags:
---
```cpp
class listNode {
public:
    listNode() {val = 0; next = NULL;}
    listNode(int v) {val = v; next = NULL;}
    listNode(int v, listNode *n) {val = v; next = n;}
    int val;
    listNode *next;
};

class MaxQueue {
public:
    MaxQueue() {
        head = NULL;
        tail = NULL;
        maxVal = NULL;
    }
    
    int max_value() {
        if (maxVal == NULL)
            return -1;
        else
            return maxVal->val;
    }
    
    void push_back(int value) {
        listNode *newNode = new listNode(value, NULL);
        if (head == NULL) {
            head = newNode;
            tail = newNode;
            maxVal = newNode;
        }
        else {
            tail->next = newNode;
            tail = newNode;
            if (value >= maxVal->val)
                maxVal = newNode;
        }
    }
    
    int pop_front() {
        if (head == NULL)
            return -1;
        else {
            int res;
            if (head == tail) {
                res = head->val;
                delete head;
                head = NULL;
                tail = NULL;
                maxVal = NULL;
            } else {
                listNode *temp = head->next;
                res = head->val;
                if (head == maxVal) {
                    maxVal = head->next;
                    listNode *p = maxVal->next;
                    while (p != NULL) {
                        if (p->val >= maxVal->val)
                            maxVal = p;
                        p = p->next;
                    }
                }
                delete head;
                head = temp;
            }
            return res;
        }
    }
private:
    listNode *head;
    listNode *tail;
    listNode *maxVal;
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue* obj = new MaxQueue();
 * int param_1 = obj->max_value();
 * obj->push_back(value);
 * int param_3 = obj->pop_front();
 */
```