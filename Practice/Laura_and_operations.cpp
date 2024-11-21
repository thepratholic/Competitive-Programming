#include <bits/stdc++.h>
using namespace std;
 
long long is_possible(long long x, long long y, long long z)
{
    if (y % 2 == z % 2)
        return 1;
    return 0;
}
 
void solve()
{
    long long a, b, c;
    cin >> a >> b >> c;
    int ans[3] = {0, 0, 0};
    ans[0] = is_possible(a, b, c);
    ans[1] = is_possible(b, a, c);
    ans[2] = is_possible(c, a, b);
    for (int i = 0; i < 3; i++)
        cout << ans[i] << " ";
    cout << endl;
}
 
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}