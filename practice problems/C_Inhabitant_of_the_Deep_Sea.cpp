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
    ll n, k;
    cin >> n >> k;

    deque<ll int> dq;

    for(ll i = 0; i < n; i++) {
        int x;
        cin >> x;

        dq.push_back(x);
    }

    int f = 1, ans = 0;

    while(k > 0 && dq.size()) {
        if(dq.size() == 1) {
            if(dq.front() <= k) {
                ans++;
            }
            break;
        }

        int x = dq.front(), y = dq.back();
        dq.pop_front();
        dq.pop_back();

        int z = min(x, y);

        if(f == 1) {
            if(z == x) {
                if(k < 2 * z - 1) break;

                k -= 2 * z - 1;
                y -= z - 1;
                f = !f;
                dq.push_back(y);
                ans++;
            }

            else {
                if(k < 2 * z) break;

                k -= 2 * z;
                x -= z;
                dq.push_front(x);
                ans++;
            }
        }

        else
            {
                if(z == y)
                {
                    if(k < 2 * z - 1) break;
 
                    k -= 2 * z - 1;
                    x -= z - 1;
                    f = 1;
                    dq.push_front(x);
                    ans++;
                }
                else
                {
                    if(k < 2 * z) break;
 
                    k -= 2 * z;
                    y -= z;
                    dq.push_back(y);
                    ans++;
                }
            }
    }

    cout << ans << nline;

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