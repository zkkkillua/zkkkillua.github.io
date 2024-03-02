---
title: 面试题51. 数组中的逆序对
date: 2020-04-25 00:11:13
categories: leetcode
tags:
---
## 1. 归并排序
归并排序的讲解见每日1题-912，[归并排序的一个用途之一就是求解逆序对](https://oi-wiki.org/basic/merge-sort/).  
归并排序在每次合并的时候，如果是将右半部分的一个元素移入到合并后的数组中，则说明左侧数组中剩下部分的元素都大于右半部分的这个元素。  
这样一下子就得到了好多逆序对。  
只需要对原有的归并排序添加count即可。  
时间复杂度`O(nlogn)`，空间复杂度`O(n)`，均同于归并排序。  
```cpp
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int n = nums.size();
        if (n < 2)
            return 0;
        
        int ans = 0;
        vector<int> cpnums(nums);   // 不破坏原有数组nums
        vector<int> temp(n);        // 临时数组，避免内部频繁构造和析构
        mergeSort(cpnums, temp, 0, n - 1, ans);

        return ans;
    }

private:
    void mergeSort(vector<int>& nums, vector<int>& temp, int left, int right, int& count) {
        if (left >= right)
            return;
        
        int mid = (left + right) / 2;
        mergeSort(nums, temp, left, mid, count);       // 对左半部分排序
        mergeSort(nums, temp, mid + 1, right, count);  // 对右半部分排序

        // 合并有序的左右两部分

        if (nums[mid] <= nums[mid + 1])         // 已经有序
            return;

        int i = left, j = mid + 1;
        for (int k = left; k <= right; k++) {
            if (i > mid)
                temp[k] = nums[j++];
            else if (j > right)
                temp[k] = nums[i++];
            else {
                if (nums[i] <= nums[j])
                    temp[k] = nums[i++];
                else {
                    temp[k] = nums[j++];
                    count += mid - i + 1;
                }
            }
        }

        for (int k = left; k <= right; k++)
            nums[k] = temp[k];
    }
};
```