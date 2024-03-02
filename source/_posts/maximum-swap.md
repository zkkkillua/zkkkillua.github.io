---
title: 670.最大交换
date: 2020-07-19 19:17:29
categories: leetcode
tags: 
- 贪心
---
## 1. 贪心，找一个右侧的最大值替换到左侧
最开始居然贼蠢，想找个右侧的最大值直接替换最左侧的位置，忽略了最左侧本身就是最大值，如5523这种情况。  
所以应该是找一个右侧的最大值替换左侧第一个比它小的值。  

可以是用一个0~9的数组记录每个数字出现的最右侧的位置，然后从左扫描看能否跟右侧互换一个最大值。  
因为是从最左侧开始，尽量交换最左侧的数和这个数右侧部分的最大值，所以也可以用一个数组记录数据的每一位数右侧的最大值的位置，这样的空间复杂度就由`O(10)`到了`O(length)`。  

```cpp
class Solution {
public:
    int maximumSwap(int num) {
        vector<int> digits(10, -1);
        string s = to_string(num);
        int n = s.length();

        for (int i = 0; i < n; i++)
            digits[s[i] - '0'] = i;
        bool flag = false;
        for (int i = 0; i < n; i++) {
            for (int k = 9; k > 0; k--) {
                if (digits[k] > i && k > s[i] - '0') {
                    char temp = s[i];
                    s[i] = k + '0';
                    s[digits[k]] = temp;
                    flag = true;
                    break;
                }
            }
            if (flag)
                break;
        }

        return stoi(s);
    }
};
```

上面算法的小缺点是至少需要`O(10)`的空间或者是`O(length)`的空间记录每个数字最右侧出现的位置或者是每位数右侧的最大数的位置。  
可以优化到只需要`O(1)`的空间直接找到右侧交换的最大值。  
为了实现`O(1)`的空间，需要找到一个位置将数据分为左右两端，找到右侧最大的数字，与左侧对应位置交换。  
这个位置是破坏从最左侧开始递减顺序的数字的位置，因为递减部分一定找不到一个数来与它左侧的数互换。  

1. 首先根据递减找到该分割位置。  
2. 然后在其右侧找一个最大值的位置，即为需要交换的位置。  
3. 在该分割位置的左侧找与右侧最大值相对应可以替换的位置，互换。  
```cpp
class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int n = s.length();
        int midLoc = 0, leftLoc = 0, rightLoc;
        
        for (int i = 0; i < n - 1; i++) {
            if (s[i] < s[i + 1]) {
                midLoc = i;     // 找到中间分割位置
                break;
            }
        }

        rightLoc = midLoc;
        for (int i = midLoc + 1; i < n; i++)
            if (s[i] >= s[rightLoc])
                rightLoc = i;   // 找到右半部分的最大值位置
        
        for (int i = 0; i <= midLoc; i++) { // 找到左半部分可交换的最左侧位置
            if (s[i] < s[rightLoc]) {
                leftLoc = i;
                break;
            }
        }

        char temp = s[leftLoc];
        s[leftLoc] = s[rightLoc];
        s[rightLoc] = temp;

        return stoi(s);
    }
};
```