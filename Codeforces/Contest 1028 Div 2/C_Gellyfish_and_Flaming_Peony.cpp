#include <bits/stdc++.h>
using namespace std;

#define ll int
#define f(i, n) for (ll i = 0; i < n; i++)
#define iv(v, n) vector<ll> v(n); f(i, n) cin >> v[i]
#define nline '\n'

void solve() {
    ll n;
    cin >> n;

    iv(a, n);

    ll g = 0;
    f(i, n) g = __gcd(g, a[i]);

    ll cnt = 0;
    f(i, n) if (a[i] == g) cnt++;

    if (cnt > 0) {
        cout << n - cnt << nline;
        return;
    }

    vector<int> dist(5001, INT_MAX);
    set<int> current_gcds;

    for (auto val : a) {
        current_gcds.insert(val);
        dist[val] = 0;
    }

    queue<int> q;
    for (auto x : current_gcds) q.push(x);

    while (!q.empty()) {
        int val = q.front();
        q.pop();

        for (auto x : a) {
            ll gc = __gcd(val, x);
            if (dist[gc] > dist[val] + 1) {
                dist[gc] = dist[val] + 1;
                q.push(gc);
            }
        }
    }

    cout << n + dist[g] - 1 << nline;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;

    while (t--) solve();

    return 0;
}
