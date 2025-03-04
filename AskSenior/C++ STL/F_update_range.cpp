#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define MOD 1000000007
#define INF 1000000000000000000LL 

void solve()
{
    ll n, q;
    cin >> n >> q;

    vector<ll> v(n + 1), diff(n + 2);
    
    // Input array (1-based indexing)
    for (ll i = 1; i <= n; i++) {
        cin >> v[i];
    }

    // Processing queries
    while (q--) {
        ll l, r, val;
        cin >> l >> r >> val;

        diff[l] += val;
        diff[r + 1] -= val;  // Ensuring range updates correctly
    }

    // Compute prefix sum for difference array
    for (ll i = 1; i <= n; i++) {
        diff[i] += diff[i - 1];
    }
    
    // Apply updates to the original array
    for (ll i = 1; i <= n; i++) {
        v[i] += diff[i];
    }
    
    // Output result
    for (ll i = 1; i <= n; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
    
    return 0;
}
