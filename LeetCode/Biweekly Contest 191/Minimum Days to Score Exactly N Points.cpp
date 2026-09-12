// Py was giving me MLE, so....
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDays(int n) {
        queue<tuple<int, int, int>> q; // score, streak, days
        q.push({0, 0, 0});

        vector<vector<bool>> vis(n + 1, vector<bool>(450, false));
        vis[0][0] = true;

        while (!q.empty()) {
            auto [score, streak, days] = q.front();
            q.pop();

            if (score == n)
                return days;

            // Earn
            int ns = score + streak + 1;

            if (ns <= n && !vis[ns][streak + 1]) {
                vis[ns][streak + 1] = true;
                q.push({ns, streak + 1, days + 1});
            }

            // Skip
            if (!vis[score][0]) {
                vis[score][0] = true;
                q.push({score, 0, days + 1});
            }
        }

        return -1;
    }
};