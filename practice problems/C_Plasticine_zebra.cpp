#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    string s;
    cin >> s;

    int n = s.size();
    string t = s + s;

    int cur = 1, ans = 1;
    for (int i = 1; i < n * 2; i++) {
        if (t[i] != t[i - 1]) {
            cur++;
        } else {
            cur = 1;
        }
        ans = max(ans, cur);
    }

    cout << min(ans, n) << "\n";
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