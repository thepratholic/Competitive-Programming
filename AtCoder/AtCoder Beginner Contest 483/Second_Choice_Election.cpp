#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, m;
    cin >> n >> m;

    vector<int> cnt(n + 1, 0);
    vector<vector<int>> adj(n + 1); 

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        cnt[a]++;
        adj[a].push_back(b);
    }

    vector<int> order(n);
    iota(order.begin(), order.end(), 1);
    sort(order.begin(), order.end(), [&](int x, int y) {
        if (cnt[x] != cnt[y]) return cnt[x] > cnt[y];
        return x < y;
    });

    vector<int> mark(n + 1, 0);

    for (int k = 1; k <= n; k++) {
        int best1 = -1, best = -1;
        auto f = [&](int c, int v) {
            if (v > best1 || (v == best1 && c < best)) {
                best1 = v;
                best = c;
            }
        };

        sort(adj[k].begin(), adj[k].end());
        auto &s = adj[k];
        for (int i = 0; i < (int)s.size();) {
            int j = i;
            while (j < (int)s.size() && s[j] == s[i]) j++;
            mark[s[i]] = k;
            f(s[i], cnt[s[i]] + (j - i));
            i = j;
        }

        for (int c : order) {
            if (c == k || mark[c] == k) continue;
            f(c, cnt[c]);
            break;
        }

        cout << best << "\n";
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    while (t--) {
        solve();
    }
    return 0;
}