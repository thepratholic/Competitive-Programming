#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    const int MOD = 1000000007LL;
    int n; cin >> n;

    int f = 1, p = 1;
    for (int i = 2; i <= n; i++) f = f * i % MOD;
    for (int i = 1; i < n; i++) p = p * 2 % MOD;

    cout << ((f - p) % MOD + MOD) % MOD << endl;
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