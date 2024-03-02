---
title: 945.Minimum Increment to Make Array Unique
date: 2020-03-22 19:41:18
categories: leetcode
tags:
---
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40000
0 <= A[i] < 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
_________________________________

## 框架
```cpp
class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {

    }
};
```

## 1. 计数`O(n+range)`
数据是`[0, 40000)`，所以移动之后占的位置是`[0, 79998]`.  
但是我们并不需要`80000`大的数组，`40001`就足够了，因为`39999`位置上的次数-1加到`40000`位置上，这些数就被均匀地分布到`40000~之后`了。  
同理，我们可以记录`maxv`，到达`maxv`之后，后面的`maxv+1, maxv+2, ...`用公式算就好了。  
```cpp
class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        int count[40010];
        for (int i = 0; i < 40010; i++)
            count[i] = 0;
        int maxv = 0;
        int ans = 0;
        for (int i = 0; i < A.size(); i++) {
            count[A[i]]++;
            maxv = maxv >= A[i] ? maxv : A[i];
        }
        
        for (int i = 0; i <= maxv; i++) {
            if (count[i] > 1) {
                count[i + 1] += count[i] - 1;
                ans += count[i] - 1;
                count[i] = 1;
            }
        }

        ans += count[maxv + 1] * (count[maxv + 1] - 1) / 2;

        return ans;
    }
};
```