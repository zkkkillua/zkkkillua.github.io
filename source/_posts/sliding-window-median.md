---
title: 480. 滑动窗口中位数
date: 2021-02-04 15:02:04
categories: 
- leetcode
tags: 
- 滑动窗口
- 堆
---

## 1. 暴力
每移动一下窗口，就对新窗口的内容排序，得到中位数。  
时间`O(nklogk)`，超时。  
```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> saveNums(nums);
        int left = 0;
        vector<double> res;

        while (left + k <= n) {
            nums = saveNums;
            sort(nums.begin() + left, nums.begin() + left + k);
            int a = nums[(2 * left + k - 1) / 2], b = nums[(2 * left + k) / 2];
            res.push_back((a - b) / 2.0 + b);   // 2.0保证转换为小数，(a-b)/2.0+b避免溢出
            left++;
        }

        return res;
    }
};
```

## 2. 堆+延迟删除
由于移动窗口之后，绝大多数的数据是不变的，因此对窗口内的所有数据重新排序是很费时的。  
考虑用一个大根堆和一个小根堆储存有序数组左右两侧的部分，大根堆存较小的数据，小根堆存较大的数据，使得大小根堆的堆顶都是有序数据中间的部分。  
这样如果窗口是奇数大小，则令大根堆比小根堆多1个数，大根堆的堆顶就是中位数；如果窗口大小是偶数，则取二者的平均值。  
当窗口向右移动时，右侧新增的元素如果>=大根堆堆顶元素，则加入大根堆，否则加入小根堆。  
窗口向右移动之后，左侧减少了一个元素。假设已经从堆中删除了这个元素，则可能会导致两个堆各自的元素个数不再满足要求，因此需要弹出数据偏多的堆的堆顶元素，加入数据偏少的堆中。  
考虑删除左侧元素。因为窗口左侧的元素可能在堆的内部，而堆只能对堆顶进行操作，所以不能直接删除可能在内部的窗口左侧元素。又因为如果不考虑数据个数的话，在堆内部的这个元素对于求中位数是没有影响的，因此可以考虑延迟删除。  
使用一个hash表记录每个元素要删除的次数，当要删除的元素在堆的内部时，暂时不删除，因为对于求解问题没有影响。直到在堆将要删除的元素移动到堆顶时，才可能会对中位数的求解产生影响，此时检查hash表，将其删除即可。  
时间`O(nlogk)`。  
```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> res;

        for (int i = 0; i < k; i++)
            small.push(nums[i]);
        for (int i = 0; i < k / 2; i++) {
            big.push(small.top());
            small.pop();
        }
        int smallOverBig = 0;       // small数据的堆的元素个数比big数据的堆的元素个数多多少，初始为0，假设多1个的奇数状态也算平衡

        int left = 0, right = k;    // [left, right)
        while (right <= n) {
            // 在计算中位数之前，首先把可能影响中位数计算的可延迟删除的数据删除掉
            while (!small.empty() && delayed[small.top()] != 0) {
                delayed[small.top()]--;
                small.pop();
            }
            while (!big.empty() && delayed[big.top()] != 0) {
                delayed[big.top()]--;
                big.pop();
            }

            res.push_back(getMedian(k));
            if (right == n)
                break;

            // 加入窗口右侧数据
            if (nums[right] <= small.top()) {
                small.push(nums[right]);
                smallOverBig++;
            }
            else {
                big.push(nums[right]);
                smallOverBig--;
            }

            // 移除窗口左侧数据
            if (nums[left] <= small.top())
                smallOverBig--;
            else
                smallOverBig++;
            delayed[nums[left]]++;

            // 调整small和big堆的平衡
            if (smallOverBig == 2) {
                big.push(small.top());
                small.pop();
            } else if (smallOverBig == -2) {
                small.push(big.top());
                big.pop();
            }
            smallOverBig = 0;

            left++;
            right++;
        }

        return res;
    }

private:
    double getMedian(int k) {
        if (k % 2 == 1)
            return small.top();
        else 
            // return (small.top() - big.top()) / 2.0 + big.top();  // 还是溢出了..
            return ((double)small.top() + big.top()) / 2;
    }
    priority_queue<int> small;          // 大根堆，存small的元素
    priority_queue<int, vector<int>, greater<int>> big;     // 小根堆，存big的元素
    unordered_map<int, int> delayed;    // 延迟删除表
};
```