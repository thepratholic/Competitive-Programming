#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    int z = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) z++;
    }

    if (z == n - 1 && a[n - 1] > 0) {
        cout << "0\n";
        return;
    }

    bool first_nz = false;
    int ops = 0;

    for (int i = 0; i < n - 1; i++) {
        if (a[i] > 0) {
            first_nz = true;
            ops += a[i];
        }

        else if (first_nz) {
            ops += 1;
        }
    }

    cout << ops << endl;

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