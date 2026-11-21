#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int a, b;
    cin >> a >> b;

    if ((a < 0 and b < 0) || (a > 0 and b > 0)) {
        cout << "Yes" << endl;
    }

    else cout << "No" << endl;
}
// TC : O(1)
// SC : O(1)

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