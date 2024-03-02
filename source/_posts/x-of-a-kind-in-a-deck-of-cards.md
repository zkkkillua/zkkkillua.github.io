---
title: 914.X of a Kind in a Deck of Cards
date: 2020-03-27 13:58:56
categories: leetcode
tags:
---
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
_________________________________

## 框架
```cpp
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {

    }
};
```

## 1. hash表+最大公约数
首先hash表统计每个值出现的次数，排除特殊情况，然后求最大公约数判断是否>=2.  
时间`O(nlogC)`(C是数据范围。应该是，因为求gcd是对数级别的复杂度)，空间`O(n)`.  
```cpp
class Solution {
public:
    int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

    bool hasGroupsSizeX(vector<int>& deck) {
        map<int, int> counter;
        for (int i = 0; i < deck.size(); i++) {
            if (counter.count(deck[i]) == 0)
                counter[deck[i]] = 1;
            else
                counter[deck[i]]++;
        }

        if (counter.size() == 1) {
            map<int, int>::iterator iter = counter.begin();
            if (iter->second == 1)
                return false;
            else 
                return true;
        }

        map<int, int>::iterator iter = counter.begin();
        int ans = gcd(iter->second, (++iter)->second);
        while (iter != counter.end()) {
            ans = gcd(ans, iter->second);
            if (ans == 1)   //剪枝
                return false;
            ++iter;
        }

        return ans != 1;
    }
};
```