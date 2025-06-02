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
    int n;
    cin >> n;
    vector<int> d(n);
    for (auto &x : d) {
        cin >> x;
    }
    vector<int> l(n), r(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i] >> r[i];
    }
    int left = 0;
    vector<int> last;
    for (int i = 0; i < n; ++i) {
        if (d[i] == -1) {
            last.push_back(i);
        } else {
            left += d[i];
        }
        while (left < l[i]) {
            if (last.empty()) {
                cout << -1 << nline;
                return;
            }
            d[last.back()] = 1;
            ++left;
            last.pop_back();
        }
        while (left + last.size() > r[i]) {
            if (last.empty()) {
                cout << -1 << nline;
                return;
            }
            d[last.back()] = 0;
            last.pop_back();
        }
    }
    for (auto &x : d) {
        cout << max(0, x) << " ";
    }
    cout << nline;
    return;
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