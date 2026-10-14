#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    ll n;
    cin >> n;

    ll ans = 0, i = 1;

    while (i <= n) {
        ll q = n / i;
        ll r = n / q;

        ans += q * (r - i + 1);
        i = r + 1;
    }

    cout << ans - n << endl;
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