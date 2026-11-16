#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int r, c;
    cin >> r >> c;

    vector<string> a(r), b(r);

    for (int i = 0; i < r; i++) cin >> a[i];
    for (int i = 0; i < r; i++) cin >> b[i];

    for (int s = 0; s < r; s++) {
        for (int t = 0; t < c; t++) {
            bool ok = true;

            for (int i = 0; i < r && ok; i++) {
                for (int j = 0; j < c; j++) {
                    if (a[(i + s) % r][(j + t) % c] != b[i][j]) {
                        ok = false;
                        break;
                    }
                }
            }

            if (ok) {
                cout << "Yes\n";
                return;
            }
        }
    }

    cout << "No\n";
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