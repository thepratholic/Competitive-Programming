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

// read question properly
// don't forget newlines!!!!!!
// take care about cin >> t;
// comment the optimization before debugging
// ALWAYS USE FIXED << SETPRECISION WHILE OUTPUTTING FLOATS

void solve()
{
    ll n, m;
    cin >> n >> m;
    ia(a, n);
    ia(b, m);
 
    ll s[m], p[m];
 
    f(i, m)
    {
        s[i] = -INF;
        p[i] = INF;
    }
 
    {
        ll p1 = 0;
        f(i, n)
        {
            if (p1 >= m)
                break;
 
            if (a[i] >= b[p1])
            {
                p[p1] = i;
                p1++;
            }
        }
    }
 
    {
        ll p2 = m - 1;
        for (int i = n - 1; i >= 0; i--)
        {
            if (p2 < 0)
                break;
 
            if (a[i] >= b[p2])
            {
                s[p2] = i;
                p2--;
            }
        }
    }
 
    if (p[m - 1] != INF)
    {
        cout << 0 << nline;
        return;
    }
 
    ll ans = LLONG_MAX;
 
    for (int i = 1; i < m - 1; i++)
    {
        if (s[i + 1] > p[i - 1])
        {
            ans = min(ans, b[i]);
        }
    }
 
    if (s[1] != -INF)
    {
        ans = min(ans, b[0]);
    }
 
    if (p[m - 2] != INF)
    {
        ans = min(ans, b[m - 1]);
    }
 
    if (ans == LLONG_MAX)
    {
        cout << -1 << nline;
        return;
    }
 
    cout << ans << nline;
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