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

void solve()
{
    ll n;
    cin >> n;

    vector<ll> v(5, 0);
    
    for(ll i = 0; i < n; i++) {
        ll x;
        cin >> x;
        v[x]++;
    }

    ll cnt = 0;

    cnt += v[4];

    cnt += v[3];
    v[1] = max((ll)0, v[1] - v[3]);

    cnt += v[2] / 2;
    
    if (v[2] % 2 == 1) {
        cnt++;
        v[1] = max((ll)0, v[1] - 2);
    }

    cnt += (v[1] + 3) / 4;
    
    cout << cnt << endl;
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
