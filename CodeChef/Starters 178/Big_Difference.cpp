#include <bits/stdc++.h>
#include<numeric>
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

// read question properly
// don't forget newlines!!!!!!
// take care about cin >> t;
// comment the optimization before debugging
// ALWAYS USE FIXED << SETPRECISION WHILE OUTPUTTING FLOATS

void solve()
{
    ll n, k;
    cin >> n >> k;
    if (k >= n)
    {
        cout << -1 << ' ' << -1 << nline;
        return;
    }

    if (n - k <= 50)
    {
        for (ll a = 1; a + k <= n; a++)
        {
            for (ll b = a + k; b <= n; b++)
            {
                if ((a * b) / __gcd(a, b) - __gcd(a, b) >= 2 * k)
                {
                    cout << a << ' ' << b << nline;
                    return;
                }
            }
        }
        cout << -1 << ' ' << -1 << nline;
    }
    else
    {
        ll a = n;
        for (ll b = 2;; b++)
        {
            if (__gcd(a, b) == 1)
            {
                cout << a << ' ' << b << nline;
                return;
            }
        }
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