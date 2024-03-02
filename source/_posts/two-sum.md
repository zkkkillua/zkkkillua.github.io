---
title: 1.两数之和
date: 2020-09-07 11:54:30
categories: leetcode
tags:
---
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
——————————————————————————————————

## 框架
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }
};
```

## 1. 暴力求解
直接遍历，O(n^2)
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> ans;
    for(int i = 0; i < nums.size() - 1; ++i) {
        for(int j = i + 1; j < nums.size(); ++j){
            if(nums[i] + nums[j] == target){
                ans.push_back(i);
                ans.push_back(j);
                break;
            }
        }
    }
    
    return ans;
}
```

## 2. hash/对数级查找
遍历nums的数据，每遍历一个数据x，去hash表中查找有无target - x的数据，并将该数据x插入到hash表中。  
hash表中，key储存数据x或者数据x需要的数据target - x，value储存其index 
ash表的查找可以看作是O(1)*（如果不发生碰撞的话）*~~（map是O(logn)）~~，所以复杂度为O(n)~~或O(nlogn)~~  
后补：  
*`map`的实现依赖于红黑树，内部是有序的，实现了对数级别的查找，以下代码是依靠`map`实现的。*  
*`map`与hash表没有关系。hash表用更大的空间实现了更快的查找：`O(1)`。*  
*hash表可以使用`unordered_map`，由hash函数实现，所以查找插入和删除都是`O(1)`的。*  
*也正因为如此，`unordered_map`的内部元素是无序的，而`map`内部是有序的。*  
*至于`hash-map`，它与`unordered_map`功能相同，但是不属于STL，是历史原因，使用`unordered_map`即可。*  
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> ans;
    map<int, int> need;
    for(int i = 0; i < nums.size(); ++i) {
        if(need.count(nums[i])){    //返回0 or 1，用来判断在不在，也可以使用need.find(nums[i]) != need.end()
            ans.push_back(need[nums[i]]);
            ans.push_back(i);
            break;
        }else
            need[target - nums[i]] = i;
    }
    return ans;
}
```