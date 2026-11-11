#include <bits/stdc++.h>
using namespace std;

#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL);
#define ll long long
#define f(i, n) for (ll i = 0; i < n; i++)

void solve() {
    ll n, m;
    cin >> n >> m;

    vector<ll> row_xor(n, 0), col_xor(m, 0);
    char x;

    f(i, n) {
        f(j, m) {
            cin >> x;
            row_xor[i] ^= (x - '0');
            col_xor[j] ^= (x - '0');
        }
    }

    ll row_count = accumulate(row_xor.begin(), row_xor.end(), 0);
    ll col_count = accumulate(col_xor.begin(), col_xor.end(), 0);

    cout << max(row_count, col_count) << endl;
}

int main() {
    fast_io;
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
