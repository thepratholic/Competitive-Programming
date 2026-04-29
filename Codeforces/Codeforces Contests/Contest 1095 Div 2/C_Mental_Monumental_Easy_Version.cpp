#include <bits/stdc++.h>
using namespace std;

// converted into cpp from py, was giving tle

void solve() {
    int n;
    cin >> n;

    vector<long long> a(n);
    for (auto &x : a) cin >> x;

    vector<int> cnt(n + 1, 0);
    for (auto x : a) {
        if (x <= n) cnt[x]++;
    }

    multiset<long long> b(a.begin(), a.end());

    unordered_map<long long, long long> d2p;
    unordered_map<long long, deque<long long>> p2d;

    for (int v = 0; v <= n; v++) {
        if (cnt[v] > 0) {
            auto it = b.lower_bound(v);
            if (it != b.end() && *it == v) {
                b.erase(it);
            } else {
                auto &dq = p2d[v];
                long long u = dq.front();
                dq.pop_front();

                if (dq.empty()) {
                    p2d.erase(v);
                }
                d2p.erase(u);

                auto it2 = b.lower_bound(2 * u + 1);
                if (it2 == b.end()) {
                    cout << v << '\n';
                    return;
                }

                long long p = *it2;
                b.erase(it2);

                d2p[u] = p;
                p2d[p].push_back(u);
            }
        } else {
            auto it = b.lower_bound(2LL * v + 1);
            if (it == b.end()) {
                cout << v << '\n';
                return;
            }

            long long p = *it;
            b.erase(it);

            d2p[v] = p;
            p2d[p].push_back(v);
        }
    }

    cout << n << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) solve();

    return 0;
}