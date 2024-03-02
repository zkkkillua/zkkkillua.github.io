---
title: 703. 数据流中的第 K 大元素
date: 2021-02-11 17:02:16
categories: 
- leetcode
tags: 
- 堆
---
## 1. 堆
由于类只需要求第k大元素，因此只保留第k大和比它大的元素作为比较即可，其他元素可以丢弃。  
因此可以使用一个大小为k的小根堆，储存前k大元素。  
当要插入元素时，与小根堆堆顶元素比较，如果偏小则抛弃，如果偏大则弹出堆顶，插入该元素。  
时间`O(nlogk)`，空间`O(k)`。  
```cpp
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        int n = nums.size();
        this->k = k;
        for (int i = 0; i < n; i++)
            add(nums[i]);
    }
    
    int add(int val) {
        if (smallHeap.size() == k && val > smallHeap.top()) {
            smallHeap.pop();
            smallHeap.push(val);
        } else if (smallHeap.size() < k)
            smallHeap.push(val);
        
        return smallHeap.top();
    }

private:
    int k;
    priority_queue<int, vector<int>, greater<int>> smallHeap;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```