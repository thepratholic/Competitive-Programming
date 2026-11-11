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

    iv(a, n);

    ll o = 0, e = 0;

    for(ll i = 0; i < n; i++) {
        if(a[i] & 1) o++;
        else e++;
    }
    
    if(o == n || e == n) {
        cout << 0 << nline;
        return;
    }

    ll s = -1;
    vector<ll> v;
    for(auto &x : a) {
        if(x % 2 == 0) {
            v.push_back(x);
        }

        else if(x > s) {
            s = x;
        }
    }

    sort(begin(v), end(v));

    ll ans = v.size();
    for(auto &t : v) {
        if(t < s) {
            s += t;
        }

        else {
            ans++;
            break;
        }
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