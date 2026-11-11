#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto &x : a) cin >> x;

    if (n == 1) {
        cout << -1 << "\n";
        return;
    }

    int best = INT_MAX;
    int x = a[0];
    int run = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] == x) run++;
        else {
            if (run > 0) best = min(best, run); run = 0;
        }
    }

    if (run > 0) best = min(best, run);

    bool same = true;
    for (int i = 0; i < n; i++) {
        if (a[i] != x) {
            same = false;
            break;
        }
    }

    if (same) cout << -1 << "\n";
    else cout << best << "\n";
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