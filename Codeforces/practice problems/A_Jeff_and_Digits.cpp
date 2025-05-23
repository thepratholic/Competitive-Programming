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

    ll cnt5 = 0, cnt0 = 0, actual = 0;

    for(int i = 0;i < n;i++) {
        int a;
        cin >> a;
        if(a == 5) cnt5++;
        else cnt0++;

        if((cnt5 * 5) % 9 == 0){
            actual = cnt5;
        }
    }

    if(actual != 0 && cnt0 > 0) {
        for(int i = 0; i < actual; i++) {
            cout << 5;
        }

        for(int i = 0; i < cnt0; i++) {
            cout << 0;
        }
    }

    else if(cnt0 > 0) {
        cout << 0 << endl;
    }

    else{
        cout << -1 << endl;
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

    // while (t--)
    // {
    solve();
    // }

#ifdef thepratholic
    cout << "\nTime taken: " << ((float)(clock() - T)) / CLOCKS_PER_SEC << " seconds";
#endif
    return 0;
}