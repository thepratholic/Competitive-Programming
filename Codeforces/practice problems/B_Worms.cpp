#include <bits/stdc++.h>

using namespace std;

#define ll long long

void solve()
{
    ll n;
    cin >> n;

    vector<ll> v(n);
    vector<ll> pre(n);

    for (ll i = 0; i < n; i++) cin >> v[i];

    // Compute prefix sums
    pre[0] = v[0];  
    for (int i = 1; i < n; i++) {
        pre[i] = pre[i - 1] + v[i];
    }

    ll m;
    cin >> m;

    while (m--) {
        ll q;
        cin >> q;

        auto it = lower_bound(pre.begin(), pre.end(), q);

        cout << (it - pre.begin()) + 1 << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();

    return 0;
}
