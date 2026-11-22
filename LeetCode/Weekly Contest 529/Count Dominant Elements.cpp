#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countDominantElements(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 1;

        int ans = 0;

        for (int i = 0; i < n; i++) {
            ans += nums[i] * 2 >= nums[max(0, i - 1)] + nums[min(n - 1, i + 1)];
        } 

        return ans;
    }
};