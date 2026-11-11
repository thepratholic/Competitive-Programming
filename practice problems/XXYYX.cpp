#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, a, b, c, d;
    cin >> n >> a >> b >> c >> d;

    if (llabs(b - c) > 1) {
        cout << "No\n";
        return;
    }

    if (b == 0 and c == 0 and a > 0 and d > 0) {
        cout << "No\n";
        return;
    }

    cout << "Yes\n";
    

}
// TC : O(1)
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