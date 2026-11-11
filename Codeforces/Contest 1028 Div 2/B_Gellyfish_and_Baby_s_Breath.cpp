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
#define MOD (998244353)
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

ll po[100001];
void solve()
{
    ll n;
    cin >> n;

    iv(p, n);
    iv(q, n);

    vector<ll> posa(n), posb(n);

    f(i, n) {
        posa[p[i]] = i;
        posb[q[i]] = i;
    }

    vector<ll> ans;

    ll pa = p[0], pb = q[0];

    f(i, n) {
        pa = max(pa, p[i]);
        pb = max(pb, q[i]);

        pair<ll, ll> p1 = mp(pa, q[i - posa[pa]]);
        pair<ll, ll> p2 = mp(pb, p[i - posb[pb]]);

        pair<ll, ll> ansp = max(p1, p2);
        ans.push_back((po[ansp.first] + po[ansp.second]) % MOD);
    }

    f(i, n) {
        cout << ans[i] << " ";
    }

    cout << nline;

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

    po[0] = 1;
    for(int i =1 ; i<= 100000; i++) {
        po[i] = 2 * po[i-1] % MOD;
    }

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