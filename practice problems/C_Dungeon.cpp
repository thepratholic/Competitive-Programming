#include <bits/stdc++.h>
using namespace std;

#define int long long
using pii = array<int, 2>;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(m), c(m);
    for (int &x : a) cin >> x;
    for (int &x : b) cin >> x;
    for (int &x : c) cin >> x;

    vector<pii> rw;
    vector<int> kl;

    multiset<int> ms(a.begin(), a.end());

    for (int i = 0; i < m; i++) {
        if (c[i] == 0) kl.push_back(b[i]);
        else rw.push_back({b[i], c[i]});
    }

    sort(rw.begin(), rw.end());
    sort(kl.begin(), kl.end());

    int ans = 0;

    for (auto &x : rw) {
        auto it = ms.lower_bound(x[0]);
        if (it == ms.end()) continue;
        int nv = max(x[1], *it);
        ms.erase(it);
        ms.insert(nv);
        ans++;
    }

    for (int x : kl) {
        auto it = ms.lower_bound(x);
        if (it == ms.end()) continue;
        ms.erase(it);
        ans++;
    }

    cout << ans << "\n";
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
