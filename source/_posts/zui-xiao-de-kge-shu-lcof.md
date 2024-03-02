---
title: 面试题40. 最小的k个数
date: 2020-03-21 17:43:15
categories: leetcode
tags: 
- 堆
---
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
_______________________________

## 框架
```cpp
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {

    }
};
```

## 1. sort, `O(nlogn)`
```cpp
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        sort(arr.begin(), arr.end());
        
        return vector<int>(arr.begin(), arr.begin() + k);
    }
};
```

## 2. 大根堆priority_queue, 时间`O(nlogk)`，空间`O(k)`
```cpp
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        priority_queue<int> q;
        int arrLen = arr.size();
        for (int i = 0; i < arrLen; i++) {
            q.push(arr[i]);
            if (i >= k)
                q.pop();
        }

        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(q.top());
            q.pop();
        }

        return res;
    }
};
```

## 3. 计数排序
已知数据范围0~10000，则`int count[10001]`，遍历数据并计数，取前k个就可以。  
数组也需要初始化为0。时间`O(n+range)`，空间`O(range)`  
