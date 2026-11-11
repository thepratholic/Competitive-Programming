#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, s;
    cin >> n >> s;

    if (s < 2 * n) {
        cout << "NO\n";
        return;
    }

    cout << "YES\n";
    for (int i = 0; i < n - 1; i++) {
        cout << "2 ";
        s -= 2;
    }

    cout << s << "\n";
    cout << "1\n";

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