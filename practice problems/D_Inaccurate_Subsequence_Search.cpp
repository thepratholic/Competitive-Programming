#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

const int MAXV = 1000001;
int cntB[MAXV], cntW[MAXV];

void solve() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> a(n), b(m);
    for (auto &x : a) cin >> x;
    for (auto &x : b) cin >> x;

    for (int x : b) cntB[x]++;

    int match = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        if (cntW[a[i]] < cntB[a[i]]) match++;
        cntW[a[i]]++;

        if (i >= m) {
            int y = a[i - m];
            cntW[y]--;
            if (cntW[y] < cntB[y]) match--;
        }

        if (i >= m - 1 && match >= k) ans++;
    }
    cout << ans << endl;

    for (int x : b) cntB[x] = 0;
    for (int i = max(0LL, n - m); i < n; i++) cntW[a[i]] = 0;
}

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