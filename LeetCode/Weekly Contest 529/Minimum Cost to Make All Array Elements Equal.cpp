#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minCost(vector<int>& nums) {
        int n = nums.size(), cnt = 0;
        long long res = LLONG_MAX;

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                cnt += 1;
            }

            else cnt = 1;

            bool valid = (cnt > 1 or (0 < i and i < n - 1));

            if (valid) {
                res = min(res, 1LL * (n - cnt) * nums[i]);
            }
        }

        return res;

    }
};