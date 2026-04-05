#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int n;
    vector<int> cost;
    vector<vector<int>> dp;

    int solve(int i, int k, int end) {
        if (k == 0) return 0;
        if (i > end) return 1e9;

        if (dp[i][k] != -1) return dp[i][k];

        int notTake = solve(i + 1, k, end);
        int take = cost[i] + solve(i + 2, k - 1, end);

        return dp[i][k] = min(take, notTake);
    }

    int minOperations(vector<int>& nums, int k) {
        n = nums.size();

        if (k == 0) return 0;
        if (k > n / 2) return -1;

        cost.resize(n);

        for (int i = 0; i < n; i++) {
            int left = nums[(i - 1 + n) % n];
            int right = nums[(i + 1) % n];
            int need = max(left, right) + 1;
            cost[i] = max(0, need - nums[i]);
        }

        // case 1: exclude last
        dp.assign(n, vector<int>(k + 1, -1));
        int ans1 = solve(0, k, n - 2);

        // case 2: exclude first
        dp.assign(n, vector<int>(k + 1, -1));
        int ans2 = solve(1, k, n - 1);

        int ans = min(ans1, ans2);
        return (ans >= 1e9 ? -1 : ans);
    }
};