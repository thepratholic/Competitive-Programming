#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << a[0] << "\n";
        return;
    }

    int suf = 0;
    int ans = 0;
    for (int i = n - 1; i >= 1; i--) {
        suf += a[i];

        if (suf > 0) {
            ans += suf;
        }
    }

    ans += a[0] + suf;
    cout << ans << "\n";
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