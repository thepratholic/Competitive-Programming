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
    ll n;
    cin >> n;
 
    if(n == 1) {
        cout << 1 << endl;
        return;
    }
 
    else if(n ==2 || n == 3) {
        cout << "NO SOLUTION" << endl;
        return;
    }
 
    else {
        ll i = 1, j = 2;
        while(j <= n) {
            cout << j << " ";
            j += 2;
        }
 
        while(i <= n) {
            cout << i << " ";
            i += 2;
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