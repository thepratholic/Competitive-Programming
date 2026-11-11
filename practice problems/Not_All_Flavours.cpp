#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n + 1), last(k + 1, 0);

    int distinct = 0;
    int best = 0;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];

        if (last[a[i]] == 0) {
            distinct++;
        }

        best = max(best, i - last[a[i]] - 1);
        last[a[i]] = i;
    }

    if (distinct < k) {
        best = n;
    }

    else {
        for (int i = 1; i <= k; i++) {
            best = max(best, n - last[i]);
        }
    }

    cout << best << "\n";

}
// TC : O(n)
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