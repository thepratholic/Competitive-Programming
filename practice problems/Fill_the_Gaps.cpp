#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<int> ans;

    for (int i = 0; i < n - 1; i++) {
        if (llabs(a[i] - a[i + 1]) == 1) {
            ans.push_back(a[i]);
        }

        else {
            if (a[i] > a[i + 1]) {
                ans.push_back(a[i]);
                for (int num = a[i] - 1; num > a[i + 1]; num--) ans.push_back(num);
            }

            else {
                ans.push_back(a[i]);
                for (int num = a[i] + 1; num < a[i + 1]; num++) ans.push_back(num);
            }
        }
    }

    ans.push_back(a[n-1]);

    for (auto &i : ans) cout << i << " ";
    cout << "\n";
}
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}