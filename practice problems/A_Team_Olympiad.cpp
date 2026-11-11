#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;
    
    vector<int> a(n + 1);
    vector<vector<int>> players(4);

    for (int i = 1; i <= n; i++) {
        cin >> a[i];

        if (a[i] == 1) {
            players[1].push_back(i);
        }

        else if (a[i] == 2) {
            players[2].push_back(i);
        }

        else players[3].push_back(i);
    }

    int teams = INT_MAX;

    for (int i = 1; i < 4; i++) {
        teams = min(teams, (int)players[i].size());
    }


    cout << teams << "\n";

    for (int i = 0; i < teams; i++) {
        cout << players[1][i] << " " << players[2][i] << " " << players[3][i] << "\n";
    }


}
// TC : O(n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}