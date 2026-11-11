#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n + 1), b(n + 1), c(m + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= n; i++) cin >> b[i];
    for (int j = 1; j <= m; j++) cin >> c[j];

    vector<int> ans(m + 1, 0);
    vector<vector<int>> need(n + 1);
    vector<int> any(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        any[b[i]] = i;
        if (a[i] != b[i]) {
            need[b[i]].push_back(i);
        }
    }

    if (any[c[m]] == 0) {
        cout << "NO\n";
        return;
    }

    bool ok = true;

    for (int j = 1; j <= m; j++) {
        if (!need[c[j]].empty()) {
            ans[j] = need[c[j]].back();
            need[c[j]].pop_back();
        }
    }

    for (int i = 1; i <= n; i++) {
        if (!need[b[i]].empty()) {
            ok = false;
            break;
        }
    }

    if (!ok) {
        cout << "NO\n";
        return;
    }

    int dump;
    if (ans[m] != 0) dump = ans[m];
    else dump = any[c[m]];

    for (int i = 1; i <= m; i++) {
        if (ans[i] == 0) ans[i] = dump;
    }

    cout << "YES\n";
    for (int i = 1; i <= m; i++) cout << ans[i] << " ";
    cout << "\n";

}
// TC : O(n + m)
// SC : O(n + m)

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