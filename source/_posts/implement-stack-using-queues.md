---
title: 225. 用队列实现栈
date: 2020-03-15 17:30:12
categories: leetcode
tags:
---
## 1. 一个队列实现
`push`: 在队列后添加元素  
`pop`: 弹出的实际上是队尾的元素，因此可以用另一个队列暂存前半部分，也可以直接将队列前半部分的元素弹出并添加到队尾，保持了顺序不变。  
`top`: 同pop  
`pop`和`top`操作需要移动整个队列，复杂度为`O(n)`。  
```cpp
class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {}
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int n = q.size();
        for (int i = 1; i < n; i++) {
            q.push(q.front());
            q.pop();
        }
        int val = q.front();
        q.pop();

        return val;
    }
    
    /** Get the top element. */
    int top() {
        int val = pop();
        q.push(val);

        return val;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }

private:
    queue<int> q;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
```
  
## 2. 复杂度互换
方法1中插入的复杂度是`O(1)`，弹出复杂度是`O(n)`。  
如果pop和top操作较多，则复杂度较高。  
可以在插入时就将队列的顺序转为栈的顺序，即插入元素后，将其前部分弹出并插入到队尾。  
从而将插入的复杂度提高到`O(n)`，pop和top复杂度降低到`O(1)`。  
```cpp
class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {}
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
        int n = q.size();
        for (int i = 1; i < n; i++) {
            q.push(q.front());
            q.pop();
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int val = q.front();
        q.pop();

        return val;
    }
    
    /** Get the top element. */
    int top() {
        return q.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }

private:
    queue<int> q;
};
```
  
## 3. 232.用栈实现队列
“用队列实现栈”和“用栈实现队列”是不同的。  
因为两个栈可以通过先入后出倒倒队列的顺序，而两个队列都是先入先出，不管怎么倒都是同样的顺序。  
