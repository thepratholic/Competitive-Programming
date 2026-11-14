#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int b, r;
    cin >> b >> r;

    cout << (30 - b) * (30 - r) << endl;
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