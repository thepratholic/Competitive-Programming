#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        int cnt = 0;
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0;j < nums.size(); j++){
                if(i != j && nums[i] + nums[j] == target){
                    cnt++;
                }
            }
        }
        return cnt;
    }
};

int main(){
    vector<string> nums = {"123","4","12","34"};
    Solution s;
    cout << s.numOfPairs(nums, "1234") << endl;
    return 0;
}
