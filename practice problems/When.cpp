#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int k;
    cin >> k;

    if (k < 10) {
        cout << "21:0" << k << endl;
        return;
    }

    if (k >= 10 and k < 60) {
        cout << "21:" << k << endl;
        return;
    }

    if (k == 60) {
        cout << "22:00" << endl;
        return;
    }

    if (k > 60 and k < 70) {
        cout << "22:0" << k << endl;
        return;
    }

    if (k >= 70) {
        cout << "22:" << k << endl;
        return;
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