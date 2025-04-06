#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define f(i, n) for (ll i = 0; i < n; i++)
#define ia(a, n) \
    ll a[n];     \
    f(i, n) cin >> a[i]
#define iv(v, n) \
    vector<ll> v(n); \
    f(i, n) cin >> v[i]
#define MOD (1000000007)
#define INF 1000000000000000000LL // Infinity for ll
#define mp make_pair
#define nline '\n'
#define yes cout << "YES\n"
#define no cout << "NO\n"

// Updated solve function using long long instead of int.
void solve()
{
    ll n;
    cin >> n;

    vector<ll> v(n);
    for(ll &x : v) 
        cin >> x;

    // Find the position of the smallest element.
    ll p = min_element(v.begin(), v.end()) - v.begin();
    ll g = 0;

    // Calculate the gcd for all elements that are multiples of v[p], skipping the chosen occurrence.
    for(ll i = 0; i < n; i++) {
        if(i != p && v[i] % v[p] == 0) {
            g = __gcd(g, v[i]);
        }
    }

    // Check if the gcd equals the smallest element.
    if(g == v[p]) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}

int main()
{
#ifdef thepratholic
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    clock_t T = clock();
#endif

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll t = 1;
    cin >> t;

    while (t--)
    {
        solve();
    }

#ifdef thepratholic
    cout << "\nTime taken: " << ((float)(clock() - T)) / CLOCKS_PER_SEC << " seconds";
#endif
    return 0;
}
