#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    map<int, int> cnt;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        cnt[a[i]]++;
    }

    int ans = 0;
    for (auto &p : cnt) {
        int x = p.first, c = p.second;
        auto it = cnt.find(x - 1);
        int prev = (it == cnt.end()) ? 0 : it->second;
        
        if (prev < c) ans += c - prev;
    }

    cout << ans << "\n";

    
}
// TC : O(n log n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}