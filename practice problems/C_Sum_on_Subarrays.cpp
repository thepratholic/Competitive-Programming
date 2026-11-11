#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, k;
    cin >> n >> k;

    int m = 0;
    while ((m + 1) * (m + 2) / 2 <= k) m++;

    int rem = k - (m * (m + 1) / 2);

    vector<int> ans(n, -1000);

    for (int i = 0; i < m; i++) ans[i] = 2;

    if (m < n) ans[m] = -(2 * (m - rem) + 1);

    for (int i = 0; i < n; i++) cout << ans[i] << " ";
    cout << "\n";
}
// TC : O(n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}