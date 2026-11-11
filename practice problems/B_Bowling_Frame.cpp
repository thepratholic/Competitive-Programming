#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int w, b;
        cin >> w >> b;
        int sum = w + b, ans = 0;
        while (sum >= 0)
        {
            ans++;
            sum -= ans;
        }
        cout << ans - 1 << endl;
    }
}
