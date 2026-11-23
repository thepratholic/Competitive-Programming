#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    bool ok = true;
    for (int i = 1; i <= n; i++) {
        bool found = false;
        for (int j = 2; j <= i + 1; j++) {
            if (a[i] % j != 0) {
                found = true;
                break;
            }
        }
        if (!found) {
            ok = false;
            break;
        }
    }

    cout << (ok ? "YES" : "NO") << endl;
}

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