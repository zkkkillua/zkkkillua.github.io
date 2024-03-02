---
title: 925.长按键入
date: 2020-10-21 16:49:51
categories: 
- leetcode
tags:
---

## 1. 模拟
两个指针分别指向`name`和`typed`即可。  
时间`O(m + n)`，空间`O(1)`。  
```cpp
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int nameLen = name.length(), typedLen = typed.length();
        int nameIdx = 0, typedIdx = 0;
        bool res = true;

        while (res && (nameIdx < nameLen || typedIdx < typedLen)) {
            if (nameIdx == nameLen) {
                if (typedIdx == 0) 
                    res = false;
                else {
                    while (typedIdx < typedLen) {
                        if (typed[typedIdx] == typed[typedIdx - 1])
                            typedIdx++;
                        else {
                            res = false;
                            break;
                        }
                    }
                }
            } else if (typedIdx == typedLen)
                res = false;
            else {
                if (name[nameIdx] == typed[typedIdx]) {
                    nameIdx++;
                    typedIdx++;
                    if (nameIdx < nameLen && name[nameIdx] != name[nameIdx - 1]) {
                        while (typedIdx < typedLen && typed[typedIdx] == typed[typedIdx - 1])
                            typedIdx++;
                    }
                } else
                    res = false;
            }
        }

        return res;
    }
};
```