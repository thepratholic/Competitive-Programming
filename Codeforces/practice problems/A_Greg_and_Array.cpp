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
    int n, m, k;
    cin >> n >> m >> k;

    vector<ll> a(n + 2);
    for (int i = 1; i <= n; i++) cin >> a[i];

    vector<tuple<int, int, int>> ops(m + 1);
    for(int i = 1; i <= m; i++) {
        int l, r, d;
        cin >> l >> r >> d;
        ops[i] = {l, r, d};
    }

    vector<ll> ops_cnt(m + 2, 0);
    for(int i = 1; i <= k; i++) {
        int x, y;
        cin >> x >> y;
        ops_cnt[x]++;
        ops_cnt[y + 1]--;
    }

    for(int i = 1; i <= m; i++) {
        ops_cnt[i] += ops_cnt[i - 1];
    }

    vector<ll> add(n + 2, 0);
    for(int i = 1; i <= m; i++) {
        auto [l, r, d] = ops[i];
        ll times = ops_cnt[i];
        add[l] += 1LL * d * times;
        add[r + 1] -= 1LL * d * times;
    }

    for (int i = 1; i <= n; i++) {
        add[i] += add[i - 1];
        cout << a[i] + add[i] << " ";
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