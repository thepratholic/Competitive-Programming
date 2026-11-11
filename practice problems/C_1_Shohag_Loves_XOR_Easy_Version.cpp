#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve()
{
    int x;
    ll m;
    cin >> x >> m;

    int ans = 0;
    for (int y = 1; y <= min(2LL * x, m); y++)
    {
        if (x != y and ((x % (x ^ y)) == 0 or (y % (x ^ y) == 0)))
        {
            ++ans;
        }
    }
    cout << ans << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}