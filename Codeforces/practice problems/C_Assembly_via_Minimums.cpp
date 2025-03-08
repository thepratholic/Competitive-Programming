#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

void solve() {
    ll n;
    cin >> n;

    ll m = n * (n - 1) / 2; // Size of array b
    vector<ll> b(m);

    for (ll &x : b) cin >> x;
    
    sort(b.begin(), b.end()); // Sorting b

    vector<ll> a;
    ll index = 0;
    
    for (ll i = n - 1; i > 0; --i) {
        a.push_back(b[index]);
        index += i;  // Move to the next group
    }

    a.push_back(1000000000); // Appending last element

    for (ll x : a) cout << x << " ";
    cout << "\n";
}

int main() {
    fast_io;
    
    ll t;
    cin >> t;
    
    while (t--) {
        solve();
    }

    return 0;
}
