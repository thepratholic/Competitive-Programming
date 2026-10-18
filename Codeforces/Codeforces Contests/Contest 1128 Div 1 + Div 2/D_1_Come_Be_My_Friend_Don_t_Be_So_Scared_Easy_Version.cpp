#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> r;

    if (n > 1) {
        int p = n - 1;
        int q = p / 2;

        if (p % 2 == 1) {
            for (int i = 1; i <= q; i++) {
                r.push_back({i + 1, i + q + 1});
            }
            r.push_back({1, q + 1});
        } else {
            for (int i = 1; i <= q; i++) {
                r.push_back({i + 1, i + q});
            }
            r.push_back({1, 1});
        }
    }

    cout << r.size() << '\n';

    for (auto [u, v] : r) {
        cout << u << ' ' << v << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}