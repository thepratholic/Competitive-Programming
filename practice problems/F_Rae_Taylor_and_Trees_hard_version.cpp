#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> p(n), suf(n + 1, 0);
    for (auto &x : p) cin >> x;

    for (int i = n - 1; i >= 0; i--) {
        suf[i] = max(suf[i + 1], p[i]);
    }

    vector<pair<int, int>> edges;
    bool ok = true;

    int cur = p[0];

    for (int j = 1; j < n && ok; j++) {
        if (p[j] > cur) {
            edges.push_back({cur, p[j]});
        } else {
            if (suf[j] < cur) {
                ok = false;
                break;
            }

            edges.push_back({cur, suf[j]});
            cur = p[j];
        }
    }

    if (!ok) {
        cout << "No\n";
    } else {
        cout << "Yes\n";

        for (auto &e : edges) {
            cout << e.first << " " << e.second << "\n";
        }
    }
}

// TC : O(n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}