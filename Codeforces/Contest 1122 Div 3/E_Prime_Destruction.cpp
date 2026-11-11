#include <bits/stdc++.h>
using namespace std;

#define int long long

const long long INF = 1e18;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (auto &x : a) cin >> x;

    // primes[x] = all prime divisors of x
    vector<vector<int>> primes(n + 1);

    for (int p = 2; p <= n; p++) {
        if (!primes[p].empty())
            continue;

        for (int x = p; x <= n; x += p) {
            primes[x].push_back(p);
        }
    }

    vector<int> dp(n + 1, -1);

    function<int(int)> f = [&](int x) -> int {
        if (x <= k)
            return 0;

        if (dp[x] != -1)
            return dp[x];

        int ans = INF;

        for (int p : primes[x]) {
            ans = min(ans, 1 + p * f(x / p));
        }

        return dp[x] = ans;
    };

    int res = 0;

    for (int x : a) {
        res += f(x);
    }

    cout << res << '\n';
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}