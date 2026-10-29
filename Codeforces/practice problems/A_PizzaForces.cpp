#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int ans = (n + 1) / 2;

    ans *= 5;

    cout << max(15LL, ans) << '\n';
}
// TC : O(1)
// SC : O(1)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}