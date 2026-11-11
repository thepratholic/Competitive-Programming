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
    ll n, k;
    cin >> n >> k;

    iv(v, n);

    ll mx = *max_element(v.begin(), v.end());
    ll mn = *min_element(v.begin(), v.end());
    sort(v.begin(), v.end());

    if(mx - mn > k + 1) {
        cout << "Jerry" << nline;
        return;
    }


    ll f = 0;
    for(ll i = 0; i < n; i++) {
        if(v[i] == mx) f++;
    }

    if(mx - mn == k + 1 && f > 1) {
        cout << "Jerry" << nline;
    }

    else {
        ll s = accumulate(v.begin(), v.end(), 0LL);

        if(s % 2 == 1) {
            cout << "Tom" << nline;
        }
        else {
            cout << "Jerry" << nline;
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