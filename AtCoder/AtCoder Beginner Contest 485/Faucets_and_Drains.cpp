#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n, m;
    cin >> n >> m;

    vector<string> s(n);
    for (auto &row : s) cin >> row;

    for (int i = 0; i < n; i++) {
        bool allX = true;
        for (char c : s[i]) {
            if (c != 'x') { allX = false; break; }
        }
        if (allX) {
            cout << "Faucet " << i + 1 << endl;
            return;
        }
    }

    for (int j = 0; j < m; j++) {
        bool allX = true;
        for (int i = 0; i < n; i++) {
            if (s[i][j] != 'x') { allX = false; break; }
        }
        if (allX) {
            cout << "Drain " << j + 1 << endl;
            return;
        }
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