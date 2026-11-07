#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    string ans(n, '0');
    int d = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            d++;
            if (d % 2 == 1) {
                ans[i] = '1';
            }
        }

        else {
            if (d % 2 == 1) {
                ans[i] = '1';
            }
            d--;
        }
    }

    cout << ans << "\n";
}
// TC : O(n)
// SC : O(n)

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