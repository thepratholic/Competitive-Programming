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
    vector<int> fib(11);
    fib[1] = 1; fib[2] = 2;
    for (int i = 3; i <= 10; ++i) fib[i] = fib[i - 1] + fib[i - 2];


    int n, m;
    cin >> n >> m;
    vector<array<int,3>> box(m);
    for (int i = 0; i < m; ++i) {
        cin >> box[i][0] >> box[i][1] >> box[i][2];
    }
    string res(m, '0');
    for (int i = 0; i < m; ++i) {
        array<int,3> b = box[i];
        bool ok = 0;
        sort(b.begin(), b.end());
        do {
            int w = b[0], l = b[1], h = b[2];
            int total_h = 0;
            bool can = 1;
            for (int j = n; j >= 1; --j) {
                int sz = fib[j];
                if (sz > w || sz > l) {
                    can = 0;
                    break;
                }
                total_h += sz;
            }
            if (can && total_h <= h) {
                ok = 1;
                break;
            }
        } while (next_permutation(b.begin(), b.end()));
        if (ok) res[i] = '1';
    }
    cout << res << '\n';

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





// #include <bits/stdc++.h>
// using namespace std;

// vector<int> fib(11);

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(0);

//     // Precompute Fibonacci numbers for n up to 10 (1-based, f1=1, f2=2)
//     fib[1] = 1; fib[2] = 2;
//     for (int i = 3; i <= 10; ++i) fib[i] = fib[i - 1] + fib[i - 2];

//     int t;
//     cin >> t;
//     while (t--) {
//         int n, m;
//         cin >> n >> m;
//         vector<array<int, 3>> box(m);
//         for (int i = 0; i < m; ++i) {
//             cin >> box[i][0] >> box[i][1] >> box[i][2];
//         }
//         string ans(m, '0');
//         for (int i = 0; i < m; ++i) {
//             int ok = 0;
//             int a[3] = {box[i][0], box[i][1], box[i][2]};
//             sort(a, a + 3);
//             do {
//                 int rem = a[2];
//                 bool can = 1;
//                 for (int j = n; j >= 1; --j) {
//                     if (fib[j] > a[0] || fib[j] > a[1] || fib[j] > rem) {
//                         can = 0;
//                         break;
//                     }
//                     rem -= fib[j];
//                 }
//                 if (can) ok = 1;
//             } while (next_permutation(a, a + 3));
//             if (ok) ans[i] = '1';
//         }
//         cout << ans << '\n';
//     }
//     return 0;
// }
