#include <bits/stdc++.h>
using namespace std;

using ll = long long int;

void solve() {
    ll n, k, t;
    cin >> n >> k >> t;

    vector<ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    sort(a.begin(), a.end());

    ll cnt = 0;
    ll reach = 0;

    for (ll x : a) {
        if (reach >= t) break;

        if (x > reach) {
            ll target = min(x, t);
            ll need = (target - reach + k - 1) / k;
            cnt += need;
            reach += need * k;
        }
        reach = max(reach, x + k);
    }

    if (reach < t) {
        cnt += (t - reach + k - 1) / k;
    }

    cout << cnt << "\n";

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}