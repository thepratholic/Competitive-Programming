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
// #define MOD (1000000007)
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
const int MOD = 998244353;
const int MAXN = 100005;

int pow2[MAXN];

void precompute_powers() {
    pow2[0] = 1;
    for (int i = 1; i < MAXN; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
}

void solve()
{
    precompute_powers();
    ll n;
    cin >> n;

    iv(p, n);
    iv(q, n);

    vector<int> r(n);

    for (int i = 0; i < n; ++i) {
        int max_val = 0;
        for (int j = 0; j <= i; ++j) {
            int a = pow2[p[j]];
            int b = pow2[q[i - j]];
            int sum = (a + b) % MOD;
            max_val = max(max_val, sum);
        }
        r[i] = max_val;
    }

    for (int i = 0; i < n; ++i) cout << r[i] << " ";
    cout << "\n";
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