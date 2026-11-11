#include <bits/stdc++.h>
using namespace std;
const int N = 5e5 + 5;
long long a[N], s[N], s1[N], s2[N];
int main()
{
    // long long ans=0;
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i], a[i] += a[i - 1];
    if (a[n] % 3 != 0)
    {
        cout << 0;
        return 0;
    }
    long long t = a[n] / 3;
    // long long ans=0;
    // long long cnt=0;
    if (a[n] == 0)
    {
        long long cnt = 0;
        for (int i = 1; i < n; i++)
        {
            if (a[i] == 0)
            {
                cnt++;
            }
        }
        cout << cnt * (cnt - 1) / 2;
    }
    else
    {
        long long ans = 0, cnt = 0;
        for (int i = 1; i <= n; i++)
        {
            if (a[i] == t)
            {
                cnt++;
            }
            if (a[i] == t * 2)
                ans += cnt;
        }
        cout << ans;
    }
    return 0;
}
