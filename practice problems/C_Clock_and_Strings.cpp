#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (a > b) swap(a, b);

    int cnt = 0;

    if (a < c and c < b) cnt++;
    if (a < d and d < b) cnt++;

    if (cnt == 1) cout << "YES" << endl;
    else cout << "NO" << endl;
}
// TC : 
// SC : 

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