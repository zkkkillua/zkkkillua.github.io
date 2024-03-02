---
title: 992. K个不同整数的子数组
date: 2021-02-10 22:11:44
categories: 
- leetcode
tags: 
- 滑动窗口
---
## 1. 滑动窗口
固定窗口的左边界，右边界向右滑动，可以找到一个最大的不可再扩展的大小为k的好子数组。此时如果也找到一个最大的不可再扩展的大小为k-1的好子数组，则二者右边界的差值即为当前左边界对应的大小为k的好子数组的个数，因为二者右侧的差值中含有第k种数据。  
这种做法需要使用两个`freq`数组记录k-1和k窗口（简称为大、小窗口）出现的各个元素的次数，因为当左边界向右移动之后，小窗口内部的元素数据可能变为k-2个，而大窗口仍为k个。所以需要分开保存，分别扩展。  
  
如果固定的是窗口的右边界，大小窗口只有左边界不同。实际操作中，相较于固定左边界，固定右边界更加简单，因为此时每次扩展移动的都是同一个右边界，而固定左边界时右边界扩展是要扩展两个右边界。  
使用这种算法，同样地需要找到一个最大的不可再扩展的大小为k和k-1的好子数组的左边界，二者的差值即为当前固定右边界对应的好子数组的种数。  
之后右边界继续向右移动1个位置，有三种情况：  
1. 大小窗口的元素种数都没有改变，仍为k和k-1
2. 大窗口的元素种类没有改变，小窗口的元素种类变为k
3. 大小窗口的元素种数都增加，变为k+1和k
对于第一种情况，二者的左边界不需要改变，并计算差值增加到答案，作为新的右边界对应的好子数组的个数；对于第二种情况，小窗口需要向右移动左边界，移动到最大的不可再扩展的大小为k-1的好子数组的左边界，而大窗口的左边界不变；对于第三种情况，小窗口的左边界向右移动到最大的不可再扩展的大小为k-1的好子数组的左边界，大窗口的左边界移动到小窗口的左边界的原位置即可。  
  
通过这个题要学会固定一个边界，滑动另一个边界求解问题的方法。  
时间`O(n)`，空间`O(n)`。  
```cpp
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        int n = A.size();
        vector<int> freqSmall(n + 1, 0), freqBig(n + 1, 0);
        int leftSmall = 0, leftBig = 0, right = 0;
        int countSmall = 0, countBig = 0;
        int res = 0;

        while (right < n) {
            if (freqSmall[A[right]] == 0) 
                countSmall++;
            freqSmall[A[right]]++;
            if (freqBig[A[right]] == 0)
                countBig++;
            freqBig[A[right]]++;
            right++;

            // if (countBig == K + 1) {
            //     leftBig = leftSmall;
            //     freqBig = freqSmall;
            //     countBig = K;
            // }
            while (countBig == K + 1) {
                freqBig[A[leftBig]]--;
                if (freqBig[A[leftBig]] == 0)
                    countBig--;
                leftBig++;
            }
            while (countSmall == K) {
                freqSmall[A[leftSmall]]--;
                if (freqSmall[A[leftSmall]] == 0)
                    countSmall--;
                leftSmall++;
            }

            res += leftSmall - leftBig;
        }

        return res;
    }
};
```