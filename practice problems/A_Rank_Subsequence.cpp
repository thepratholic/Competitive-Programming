#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> l(n), r(n), u(n), v(n);

    for (int i = 0; i < n; i++) {
        cin >> l[i] >> r[i] >> u[i] >> v[i];
    }

    int ans = 0;

    for (int m = 1; m <= n; m++) {
        int cnt = 0;

        for (int i = 0; i < n && cnt < m; i++) {
            int j = cnt + 1;
            int rr = m - j + 1;

            bool left = (l[i] <= j && j <= r[i]);
            bool right = (u[i] <= rr && rr <= v[i]);

            if (!left && !right) cnt++;
        }

        if (cnt == m) ans = m;
    }

    cout << ans << "\n";
}
// TC : O(n^2)
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