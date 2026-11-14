#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n), b(n);
    for (auto &x : a) cin >> x;
    for (auto &x : b) cin >> x;

    if (a == b) {
        cout << "Yes\n";
        return;
    }

    int l = 0, r = n - 1;
    while (a[l] == b[l]) l++;
    while (a[r] == b[r]) r--;

    bool ok1 = (a[l] == b[r]);
    for (int i = l; i < r and ok1; i++) {
        if (a[i + 1] != b[i]) ok1 = false;
    }

    bool ok2 = (a[r] == b[l]);
    for (int i = l; i < r and ok2; i++) {
        if (a[i] != b[i + 1]) ok2 = false;
    }

    cout << ((ok1 or ok2) ? "Yes\n" : "No\n");
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    // cin >> t;  
    while (t--) {
        solve();
    }

    return 0;
}