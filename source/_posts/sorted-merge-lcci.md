---
title: 面试题 10.01. Sorted Merge LCCI
date: 2020-03-16 18:05:58
categories: leetcode
tags: 
- 双指针
---
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

Initially the number of elements in A and B are m and n respectively.

Example:

Input:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sorted-merge-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
________________________

## 框架
```cpp
class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {

    }
};
```

## 1. 双指针
想法就是双指针遍历，然后把B的数据插入到A中。  
不过应该不能用`insert()`，因为A后面已经有0来占位了，插入的时候可能会保留0而继续开拓空间导致超出内存限制。  
所以可以对于B的一个元素，挨个往后移A的数据，直到B可以插入的位置，这样是`O(mn)`的。
不过既然A后面已经预留位置了，那么A和B可以直接从A的最后开始放最大值，这样就变成`O(m+n)`了。  
```cpp
class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int iterA = m - 1, iterB = n - 1;
        int loc = m + n - 1;
        while (loc >= 0) {
            if (iterA == -1)
                A[loc--] = B[iterB--];
            else if (iterB == -1)
                A[loc--] = A[iterA--];
            else {
                if (A[iterA] >= B[iterB])
                    A[loc--] = A[iterA--];
                else
                    A[loc--] = B[iterB--];
            }
        }
    }
};
```