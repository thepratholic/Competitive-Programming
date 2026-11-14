#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto &x : a) cin >> x;

    vector<int> cnt(n + 1, 0);
    int ans = 1;
    for (int i = 0; i < n; i++) {
        if (i > 0 && a[i] != a[i - 1]) {
            ans += i - cnt[a[i]];
        }
        cnt[a[i]]++;
    }

    cout << ans << "\n";
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