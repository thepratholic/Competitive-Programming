#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; i++) cin >> c[i];

    const int INF = INT_MAX;
    vector<int> ans(n + 1, INF);

    int l = 1;
    while (l <= n) {
        int r = l;
        while (r + 1 <= n && c[r + 1] == c[l]) r++;
        for (int i = l; i <= r; i++) {
            if (l > 1) ans[i] = min(ans[i], i - (l - 1));
            if (r < n) ans[i] = min(ans[i], (r + 1) - i);
        }
        l = r + 1;
    }

    for (int i = 1; i <= n; i++) cout << ans[i] << " ";
    cout << endl;
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