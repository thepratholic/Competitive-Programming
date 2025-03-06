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
    ll row, col;
    cin >> row >> col;
 
    ll ans;
    if(col > row) {
        if(col % 2 == 1) {
            ans = (col * col) - row + 1;
            cout << ans << endl;
            return;
        }
        else {
            ans = ((col - 1) * (col - 1) + row);
            cout << ans << endl;
            return;
        }
    }
 
    else {
        if(row % 2 == 1) {
            ans = ((row - 1) * (row - 1) + col);
            cout << ans << endl;
            return;
        }
 
        else {
            ans = (row * row) - col + 1;
            cout << ans << endl;
            return;
        }
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