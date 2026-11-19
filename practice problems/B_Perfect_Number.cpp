#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int k;
    cin >> k;

    int cnt = 0;

    for (int x = 19; ; x += 9) {
        int y = x, s = 0;

        while (y > 0) {
            s += y % 10;
            y /= 10;
        }

        if (s == 10) {
            cnt++;

            if (cnt == k) {
                cout << x << endl;
                return;
            }
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