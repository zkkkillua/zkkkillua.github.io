---
title: 232. 用栈实现队列
date: 2021-03-05 11:00:31
categories: 
- leetcode
tags:
---
## 1. 来回倒
使用两个栈，一个作为输入栈，一个作为输出栈。  
`push`: 添加到输入栈中  
`pop`: 将输入栈的元素弹出并添加到输出栈，实现逆序，弹出首元素后，再将剩余元素弹回输入栈  
`peek`: 同pop  
这种方法比较繁琐，pop和peek操作都是`O(n)`的。  
  
## 2. 不来回倒
使用两个栈，一个作为输入栈，一个作为输出栈。  
几乎同方法1，但是当元素被弹到输出栈之后，不再弹回到输入栈。  
因为输出栈本身就是“队列”的前部分，当输出栈为空时，再将输入栈弹到输出栈，得到的又是队列接下来的一部分。  
这样可以将pop和peek的操作降低到均摊`O(1)`。  
```cpp
class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {}
    
    /** Push element x to the back of queue. */
    void push(int x) {
        inStack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (outStack.empty())
            move();
        int val = outStack.top();
        outStack.pop();

        return val;
    }
    
    /** Get the front element. */
    int peek() {
        if (outStack.empty())
            move();
        return outStack.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return inStack.empty() && outStack.empty();
    }
private:
    stack<int> inStack, outStack;
    void move() {
        while (!inStack.empty()) {
            outStack.push(inStack.top());
            inStack.pop();
        }
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```
  
## 3. 225.用队列实现栈
“用队列实现栈”和“用栈实现队列”是不同的。  
因为两个栈可以通过先入后出倒倒队列的顺序，而两个队列都是先入先出，不管怎么倒都是同样的顺序。  
