#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define f(i, n) for (ll i = 0; i < n; i++)
#define MOD (1000000007)
#define INF 1000000000000000000LL // Infinity for ll
#define nline '\n'

void solve()
{
    ll n, m, a, b;
    cin >> n >> m >> a >> b;

    ll mini = INF;

    ll cost_single = n * a;
    mini = min(mini, cost_single);

    ll cost_only_multi = ceil((double)n / m) * b;
    mini = min(mini, cost_only_multi);

    ll full_multi_tickets = n / m;
    ll remaining_rides = n % m;
    ll cost_mixed = (full_multi_tickets * b) + (remaining_rides * a);
    mini = min(mini, cost_mixed);

    cout << mini << nline;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long t = 1;
    // cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}
