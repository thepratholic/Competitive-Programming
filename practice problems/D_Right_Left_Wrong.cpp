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

    vector<ll> v(n), pre(n);

    for(ll i = 0; i < n; i++) {
        cin >> v[i];
        if(i == 0) {
            pre[0] = v[0];
        }
        else {
            pre[i] = pre[i - 1] + v[i];
        }
    }

    string s;
    cin >> s;

    ll l = 0, r = n - 1, ans = 0;

    while(l < r) {
        if(s[l] == 'L' && s[r] == 'R') {
            if(l == 0) {
                ans += pre[r];
            }
            else {
                ans += pre[r] - pre[l - 1];
            }
            l += 1;
            r -= 1;
        }

        else if(s[l] == 'R') {
            l += 1;
        }
        else{
            r--;
        }

    }


    cout << ans << endl;

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