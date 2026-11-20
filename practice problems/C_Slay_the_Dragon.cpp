#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    vector<int> heros(n);
    int s = 0;
    for (auto &x : heros) {
        cin >> x;
        s += x;
    }

    sort(heros.begin(), heros.end());

    int dragons;
    cin >> dragons;

    while (dragons--) {
        int x, y;
        cin >> x >> y;

        int best = LLONG_MAX;
        int idx = lower_bound(heros.begin(), heros.end(), x) - heros.begin();

        auto calc = [&](int h) {
            int kill = max(0LL, x - h);
            int def = max(0LL, y - (s - h));
            return kill + def;
        };

        if (idx < n) best = min(best, calc(heros[idx]));
        if (idx > 0) best = min(best, calc(heros[idx - 1]));

        cout << best << endl;
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