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
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    bool sorted = 1, have0 = 0, have1 = 0;
    for(int i = 1; i <= n; i++)
    {
        cin >> a[i];
        if(i >= 2 && a[i] < a[i - 1])
            sorted = 0;
    }
    for(int i = 1; i <= n; i++)
    {
        cin >> b[i];
        if(!b[i])
            have0 = 1;
        else
            have1 = 1;
    }
    if(have0 && have1)
        cout << "Yes" << endl;
    else if(sorted)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
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