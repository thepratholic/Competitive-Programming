#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    bool is_nine = false;
    int mn = INT_MAX;

    for (int i = 0; i < n; i++) {
        if (a[i] == 9) is_nine = true;
        mn = min(mn, a[i]);
    }

    if (is_nine) {
        cout << mn << endl;
    }

    else {
        cout << -1 << endl;
    }
}
// TC : 
// SC : 

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