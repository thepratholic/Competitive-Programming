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
    int n, m, L;
    cin >> n >> m >> L;

    vector<tuple<int, int, int>> EV;

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        EV.emplace_back(a, b, 1);
    }

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        EV.emplace_back(a, b, 0);
    }

    sort(EV.begin(), EV.end());

    int k = 1;
    priority_queue<int> pwr;
    bool ok = true;

    for (auto &[a, b, t] : EV) {
        if (t == 0) {
            pwr.push(b);
        } else {
            while (!pwr.empty() && k < b - a + 2) {
                k += pwr.top();
                pwr.pop();
            }
            if (k < b - a + 2) {
                cout << "-1\n";
                ok = false;
                break;
            }
        }
    }

    if (ok) cout << m - (int)pwr.size() << nline;
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