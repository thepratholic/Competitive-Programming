#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    map<int, int> cnt;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int k = 0;
    for (auto &[v, c] : cnt) {
        k += min(c, 2LL); 
    }

    vector<int> res;
    res.reserve(n);
    int mx = cnt.rbegin()->first;

    for (auto &[v, c] : cnt) {
        if (v != mx) res.push_back(v);
    }

    for (int i = 0; i < cnt[mx]; i++) res.push_back(mx);

    for (auto it = cnt.rbegin(); it != cnt.rend(); ++it) {
        if (it->first == mx) continue;
        for (int i = 0; i < it->second - 1; i++) res.push_back(it->first);
    }

    cout << k << "\n";
    for (int i = 0; i < n; i++) cout << res[i] << " ";
    cout << endl;
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