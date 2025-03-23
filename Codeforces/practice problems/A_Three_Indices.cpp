#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define f(i, n) for (ll i = 0; i < n; i++)
#define nline '\n'

void solve() {
    ll n;
    cin >> n;

    vector<ll> p(n);
    for (ll &x : p) {
        cin >> x;
    }

    bool found = false;
    ll i_ans = -1, j_ans = -1, k_ans = -1;

    for (ll j = 1; j < n - 1 && !found; j++) {
        for (ll i = 0; i < j; i++) {
            if (p[i] < p[j]) {
                for (ll k = j + 1; k < n; k++) {
                    if (p[k] < p[j]) {
                        i_ans = i;
                        j_ans = j;
                        k_ans = k;
                        found = true;
                        break;
                    }
                }
                if (found) break;
            }
        }
    }

    if (found) {
        cout << "YES" << nline;
        cout << i_ans + 1 << " " << j_ans + 1 << " " << k_ans + 1 << nline;
    } else {
        cout << "NO" << nline;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    ll t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
