#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    unordered_map<int, int> cnt;
    cnt.reserve(n * 2);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        cnt[a[i]]++;
    }

    vector<int> f;
    for (auto &p : cnt) {
        f.push_back(p.second);
    }

    sort(f.begin(), f.end());

    int ans = 0;
    int m = f.size();

    for (int i = 0; i < m; i++) {
        int kept = 1LL * f[i] * (m - i);
        ans = max(ans, kept);
    }

    cout << n - ans << "\n";
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