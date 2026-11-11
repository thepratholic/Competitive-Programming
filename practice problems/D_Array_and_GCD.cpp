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


void solve(vector<int> &p)
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto& x : a) cin >> x;
    sort(a.begin(), a.end(), greater<int>());
    int ans = 0;
    long long suma = 0, sump = 0;
    for (int i = 0; i < n; ++i) {
      suma += a[i];
      sump += p[i];
      if (suma >= sump) ans = i + 1;
    }
    cout << n - ans << endl;
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

    const int N = 6e6;
    vector<int> p, ip(N, 1);
    for (int i = 2; i < N; ++i) {
        if (!ip[i]) continue;
        p.push_back(i);
        for (int j = i; j < N; j += i) {
            ip[j] = 0;  
        }
    }

    long long t = 1;
    cin >> t;

    while (t--)
    {
        solve(p);
    }

#ifdef thepratholic
    cout << "\nTime taken: " << ((float)(clock() - T)) / CLOCKS_PER_SEC << " seconds";
#endif
    return 0;
}