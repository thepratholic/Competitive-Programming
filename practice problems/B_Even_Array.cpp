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

    int x = 0, y = 0;

    for (int i = 0; i < n; i++) {
        if (i % 2 != a[i] % 2) {
            if (i % 2 == 0) {
                x++;
            } else {
                y++;
            }
        }
    }

    if (x != y) {
        cout << -1 << "\n";
    } else {
        cout << x << "\n";
    }
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