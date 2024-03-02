---
title: 1423. 可获得的最大点数
date: 2021-02-06 20:32:29
categories: 
- leetcode
tags: 
- dp
- 滑动窗口
---
## 1. 动态规划
由于不能贪心抽两侧最大的牌，因此考虑dp，两侧都抽，然后对剩下的部分同样进行一次“可获得的最大点数”的求解。  
为了避免重复计算，使用hash表记录求解过的每一段数组的最大点数。  
另外，由于hash表的key是`pair`类型，因此还需要手动提供`pair`类型的hash函数。  
时间`O(k^2)`，空间`O(k^2)`，因为要求解和记录k从0到k每种情况下，对应数组段的最大点数。超时。  
```cpp
struct pairhash {
public:
    template <class T, class U>
    std::size_t operator () (const std::pair<T, U>& p) const {
        // sizt_t = typeof(sizeof(x))，是sizeof()函数返回值的类型，代表目标平台下最大可能的数组尺寸
        // size_t是unsigned，保证跨平台
        std::hash<T> Thasher;
        std::hash<U> Uhasher;
        return Thasher(p.first) ^ Uhasher(p.second);
        // 使用first和second的hash值的异或作为pair的hash值
    }
};

class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        // unordered_map<pair<int, int>, int> scores;
        unordered_map<pair<int, int>, int, pairhash> scores;
        subMaxScore(cardPoints, 0, n, scores, k);

        return scores[make_pair(0, n)];
    }

private:
    int subMaxScore(vector<int>& cardPoints, int beg, int end, unordered_map<pair<int, int>, int, pairhash>& scores, int k) {
        if (k == 0)
            return 0;
        
        pair<int, int> cur = make_pair(beg, end);
        if (scores.count(cur))
            return scores[cur];

        int leftScore = cardPoints[beg], rightScore = cardPoints[end - 1];
        pair<int, int> left = make_pair(beg + 1, end), right = make_pair(beg, end - 1);
        if (scores.count(left))     // 选最左元素
            leftScore += scores[left];
        else 
            leftScore += subMaxScore(cardPoints, beg + 1, end, scores, k - 1);
        if (scores.count(right))    // 选最右元素
            rightScore += scores[right];
        else 
            rightScore += subMaxScore(cardPoints, beg, end - 1, scores, k - 1);
        
        scores[cur] = max(leftScore, rightScore);
        return scores[cur];
    }
};
```

## 2. 滑动窗口
并不一定是窗口两侧初始化为数组两侧，窗口向内收缩；也可以是固定窗口大小，移动窗口位置。  
因为要从n个数中选k个，因此可以固定窗口大小为n-k个，代表剩余的数据。窗口从左向右滑动，在此过程中统计结果。  
时间`O(k)`，空间`O(1)`。  
```cpp
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int left = 0, right = n - k;    // [left, right)
        int sum = 0, maxSum = 0;

        for (int i = right; i < n; i++)
            sum += cardPoints[i];
        maxSum = sum;

        while (right < n) {
            sum += cardPoints[left++];
            sum -= cardPoints[right++];
            maxSum = max(maxSum, sum);
        }

        return maxSum;
    }
};
```