#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int mx = 0;
    vector<int> nums;
    while (n--) {
        int x;
        cin >> x;
        nums.push_back(x);

        mx = max(mx, x);
    }

    vector<int> divs(mx + 1, 0);

    for (int i = 1; i <= mx; i++) {
        for (int j = i; j <= mx; j += i) {
            divs[j]++;
        }
    }

    for (auto &x : nums) {
        cout << divs[x] << "\n";
    }

}
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}