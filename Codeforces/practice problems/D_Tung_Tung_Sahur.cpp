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

void solve() {
    string a, b; cin >> a >> b;
    int n = a.size();
    int m = b.size();
    if (m < n || m > 2 * n || a[0] != b[0]) {
        cout << "NO" << nline;
        return;
    }
    vector<int> aa, bb;
    int cnt = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] != a[i-1]) {
            aa.push_back(cnt);
            cnt = 1;
        }
        else cnt++;
    }
    aa.push_back(cnt);
    cnt = 1;
    for (int i = 1; i < m; i++) {
        if (b[i] != b[i-1]) {
            bb.push_back(cnt);
            cnt = 1;
        }
        else cnt++;
    }
    bb.push_back(cnt);
    if (aa.size() != bb.size()) {
        cout << "NO" << nline;
        return;
    }
    n = aa.size();
    for (int i = 0; i < n; i++) {
        if (aa[i] > bb[i] || aa[i] * 2 < bb[i]) {
            cout << "NO\n";
            return;
        }
    }
    cout << "YES" << nline;
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