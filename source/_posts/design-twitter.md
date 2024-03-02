---
title: 355. 设计推特
date: 2020-04-14 00:23:38
categories: leetcode
tags:
---
## 框架
```cpp
class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {

    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {

    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {

    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {

    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {

    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
```

## 1. 模拟
```cpp
struct tweet {
    tweet(int i = 0, int t = 0) { id = i; time = t; }
    int id;
    int time;
};

struct user {
    // int id;
    list<tweet> tweets;
    list<int> following;
};

class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {
        user_table.clear();
        cur_time = 1;
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        user_table[userId].tweets.push_front(tweet(tweetId, cur_time++));
        if (user_table[userId].tweets.size() > 10)
            user_table[userId].tweets.pop_back();
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<tweet> temp_ans(user_table[userId].tweets.begin(), user_table[userId].tweets.end());

        for (list<int>::iterator iter = user_table[userId].following.begin(); iter != user_table[userId].following.end(); ++iter) {
            if (*iter == userId)
                continue;

            vector<tweet> temp(temp_ans);
            temp_ans.clear();
            vector<tweet>::iterator temp_it = temp.begin();
            for (list<tweet>::iterator jter = user_table[*iter].tweets.begin(); jter != user_table[*iter].tweets.end(); ++jter) {
                if (temp_it != temp.end()) {
                    if (temp_it->time < jter->time) {
                        temp_ans.push_back(*jter);
                    } else {
                        temp_ans.push_back(*temp_it);
                        ++temp_it;
                        --jter;
                    }
                } else {
                    temp_ans.push_back(*jter);
                }
                if (temp_ans.size() == 10)
                    break;
            }
            while (temp_it != temp.end()) {
                if (temp_ans.size() == 10)
                    break;
                temp_ans.push_back(*temp_it);
                ++temp_it;
            }
        }

        vector<int> ans;
        for (vector<tweet>::iterator it = temp_ans.begin(); it != temp_ans.end(); ++it)
            ans.push_back(it->id);

        return ans;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        for (list<int>::iterator it = user_table[followerId].following.begin(); it != user_table[followerId].following.end(); ++it)
            if (*it == followeeId)
                return;
        user_table[followerId].following.push_back(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        for (list<int>::iterator it = user_table[followerId].following.begin(); it != user_table[followerId].following.end(); ++it)
            if (*it == followeeId) {
                user_table[followerId].following.erase(it);
                break;
            }
    }

private:
    unordered_map<int, user> user_table;
    int cur_time;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
```