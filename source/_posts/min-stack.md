---
title: 155. 最小栈
date: 2020-05-12 12:14:06
categories: leetcode
tags: 
- 栈
---
## 1. 直接模拟
用一个变量记录最小元素的位置就可以了。  
```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        vals = new int[10];
        capacity = 10;
        minLoc = 0;
        size = 0;
    }
    
    ~MinStack() {
        delete []vals;
        vals = nullptr;
    }
    
    void push(int x) {      // 时间复杂度均摊`O(1)`
        if (size == capacity) {
            int* temp = new int[capacity * 2];
            capacity *= 2;
            for (int i = 0; i < size; i++)
                temp[i] = vals[i];
            
            delete []vals;
            vals = temp;
        }

        vals[size++] = x;
        if (x < vals[minLoc])
            minLoc = size - 1;
    }
    
    void pop() {            // 时间复杂度最坏`O(n)`
        if (size == 0)
            return;
        
        size--;
        if (minLoc == size) {
            minLoc = 0;
            for (int i = 1; i < size; i++)
                if (vals[i] < vals[minLoc])
                    minLoc = i;
        }
    }
    
    int top() {
        if (size == 0)
            return -1;
        return vals[size - 1];
    }
    
    int getMin() {
        if (size == 0)
            return -1;
        return vals[minLoc];
    }

private:
    int* vals;
    int capacity;
    int minLoc;
    int size;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

## 2. 辅助栈
用一个辅助栈记录过程中的最小值，用额外`O(n)`的空间将`pop()`的复杂度降低为`O(1)`。  
以下两种方式都可以：  
- **同步辅助栈**
数据栈：3, 1, 2, 4, 5, 1  
辅助栈：3, 1, 1, 1, 1, 1  
- **不同步辅助栈**
数据栈：3, 1, 2, 4, 5, 1  
辅助栈：3, 1, 1  
```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        vals = new int[10];
        auxiliary = new int[10];
        capacity = 10;
        size = 0;
        auxCapa = 10;
        auxSize = 0;
    }

    ~MinStack() {
        delete []vals;
        delete []auxiliary;
    }
    
    void push(int x) {
        if (size == capacity) {
            vals = doubleArray(vals, size);
            capacity *= 2;
        }
        if (auxSize == auxCapa) {
            auxiliary = doubleArray(auxiliary, auxSize);
            auxCapa *= 2;
        }

        vals[size++] = x;
        if (auxSize == 0 || (auxSize > 0 && x <= auxiliary[auxSize - 1]))
            auxiliary[auxSize++] = x;
    }
    
    void pop() {
        if (size == 0)
            return;
        if (vals[size - 1] == auxiliary[auxSize - 1])
            auxSize--;
        size--;
    }
    
    int top() {
        if (size == 0)
            return -1;
        return vals[size - 1];
    }
    
    int getMin() {
        if (size == 0)
            return -1;
        return auxiliary[auxSize - 1];
    }

private:
    int* vals;
    int* auxiliary;
    int capacity;
    int size;
    int auxCapa;
    int auxSize;

    int* doubleArray(int* before, int n) {
        int* after = new int[n * 2];
        for (int i = 0; i < n; i++)
            after[i] = before[i];
        delete []before;
        return after;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```