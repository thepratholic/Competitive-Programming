#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int k, s;
    cin >> k >> s;

    int ans = 0;

    for (int x = 0; x <= k; x++) {
        for (int y = 0; y <= k; y++) {
            int z = s - x - y;

            if (z >= 0 and z <= k) ans++;
        }
    }

    cout << ans << endl;
}
// TC : O(k^2)
// SC : O(1)

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