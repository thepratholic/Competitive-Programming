#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

int32_t main()
{
    fastio();
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        if (n % 2 == 0)
        {
            cout << -1 << "\n";
        }
        else
        {
            vector<int> perm(n);
            for (int i = 1; i <= n; i++)
            {
                int x = (2 * i) % n;
                if (x == 0)
                    x = n;
                perm[i - 1] = x;
            }
            for (auto x : perm)
                cout << x << " ";
            cout << "\n";
        }
    }
    return 0;
}