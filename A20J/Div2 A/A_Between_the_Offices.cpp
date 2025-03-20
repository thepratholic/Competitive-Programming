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
    ll n;
    cin >> n;

    string s;
    cin >> s;

    ll s_to_f = 0;
    ll f_to_s = 0;

    for(ll i = 0; i < n - 1; i++) {
        if(s[i] == 'S' && s[i + 1] == 'F') {
            s_to_f ++;
        }

        if(s[i] == 'F' && s[i + 1] == 'S') {
            f_to_s ++;
        }
    }

    if(s_to_f > f_to_s) {
        cout << "YES" << endl;
        return;
    }

    else {
        cout << "NO" << endl;
        return;
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
    // cin >> t;

    while (t--)
    {
        solve();
    }

#ifdef thepratholic
    cout << "\nTime taken: " << ((float)(clock() - T)) / CLOCKS_PER_SEC << " seconds";
#endif
    return 0;
}