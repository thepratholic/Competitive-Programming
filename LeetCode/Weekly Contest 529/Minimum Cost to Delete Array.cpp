#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minCost(vector<int>& nums) {
        int n = nums.size();
        int cnt = 0, mn = INT_MAX;
        long long res = 0LL + nums[0] + nums[n - 1];

        for (int i = 1; i < n - 1; i++) {
            if (nums[i] < 0) {
                res += nums[i];
                cnt ^= 1;
            }

            mn = min(mn, abs(nums[i]));
        }

        if (cnt) {
            res += mn;
        }

        return res;
    }

};