#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n + 1];
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    vector<int> dp(n + 1, 1);
    int ans = 1;

    for (int i = 1; i <= n; i++) {
        ans = max(ans, dp[i]);

        for (int j = 2 * i; j <= n; j += i) {
            if (a[i] < a[j]) {
                dp[j] = max(dp[j], dp[i] + 1);
            }
        }
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
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}