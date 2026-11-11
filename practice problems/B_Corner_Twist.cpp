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

void op(char &ch, int delta) {
    ch = char('0' + ((ch - '0') + delta) % 3);
}
void solve()
{
    ll n, m;
    cin >> n >> m;

    vector<string> a(n), b(n);

    for(ll i = 0; i < n; i++) {
        cin >> a[i];
    }

    for(ll i = 0; i < n; i++) {
        cin >> b[i];
    }

    for(ll i = 0; i < n - 1; i++) {
        for(ll j = 0; j < m - 1; j++) {
            while(a[i][j] != b[i][j]) {
                op(a[i][j], 1);
                op(a[i][j + 1], 2);
                op(a[i + 1][j], 2);
                op(a[i + 1][j + 1], 1);
            }
        }
    }

    if (a == b) {
        cout << "YES" << endl;
    }

    else {
        cout << "NO" << endl;
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