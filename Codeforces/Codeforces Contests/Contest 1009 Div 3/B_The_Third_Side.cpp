#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    ll n;
    cin >> n;

    priority_queue<ll> pq;
    for (ll i = 0; i < n; i++) {
        ll x;
        cin >> x;
        pq.push(x);
    }

    while (pq.size() > 1) {
        ll f = pq.top(); pq.pop();
        ll s = pq.top(); pq.pop();
        pq.push(f + s - 1);
    }

    cout << pq.top() << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
