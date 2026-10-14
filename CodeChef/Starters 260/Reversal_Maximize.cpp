#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> p(n + 1), pre(n + 1, 0);
    vector<vector<int>> g(2 * n + 2);

    for (int i = 1; i <= n; i++) {
        cin >> p[i];
        pre[i] = pre[i - 1] + (p[i] == i);
        g[i + p[i]].push_back(i);
    }

    int base = pre[n];
    int best = 0;

    for (int s = 2; s <= 2 * n; s++) {
        if (g[s].empty()) continue;

        vector<int> d;

        for (int j : g[s]) {
            int m = s - j;

            if (m < 1 || m > n) continue;

            d.push_back(min(j, m));
        }

        sort(d.rbegin(), d.rend());

        for (int i = 0; i < (int)d.size(); i++) {
            int L = d[i];
            int R = s - L;

            int fi = pre[R] - pre[L - 1];

            best = max(best, (i + 1) - fi);
        }
    }

    cout << base + best << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}