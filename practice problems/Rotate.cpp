#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<vector<int>> a(n, vector<int> (n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            char c;
            cin >> c;
            a[i][j] = c - '0';
        }
    }

    int t1 = a[0][n - 1];
    int t2 = a[n - 1][n - 1];
    int t3 = a[n - 1][0];

    for (int j = n - 1; j >= 1; j--) a[0][j] = a[0][j - 1];

    for (int i = n - 1; i >= 2; i--) a[i][n - 1] = a[i - 1][n - 1];
    a[1][n - 1] = t1;

    for (int j = 0; j <= n - 2; j++) a[n - 1][j] = a[n - 1][j + 1];
    a[n - 1][n - 2] = t2;

    for (int i = 0; i <= n - 2; i++) a[i][0] = a[i + 1][0];
    a[n - 2][0] = t3;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << a[i][j];
        }

        cout << endl;
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