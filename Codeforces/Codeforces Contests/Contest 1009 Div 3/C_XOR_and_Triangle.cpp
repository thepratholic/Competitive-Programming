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
#define nl '\n'
#define yes cout << "YES\n"
#define no cout << "NO\n"

// read question properly
// don't forget newlines!!!!!!
// take care about cin >> t;
// comment the optimization before debugging
// ALWAYS USE FIXED << SETPRECISION WHILE OUTPUTTING FLOATS

void solve()
{
    int x;
    cin >> x;
    if (__builtin_popcountll(x) == 1) {
        cout << "-1\n";
        return;
    }
    int y = 0;
    int f1 = 0, f0 = 0;
    for (int i = 0; i <= 30; i++) {
        if (x & (1 << i)) {
            if (f1 == 0) {
                y |= 1 << i;
                f1 = 1;
            }
        } else {
            if (f0 == 0) {
                y |= 1 << i;
                f0 = 1;
            }
        }
    }
    if (y < x) {
        cout << y << '\n';
    } else
        cout << "-1\n";
    
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

    long long t = 1;
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