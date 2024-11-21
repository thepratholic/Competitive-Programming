#include <bits/stdc++.h>
using namespace std;

void solve()
{
    long long n, x;
    cin >> n >> x;
    long long a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    long long max_fuel_needed = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (i == 0)
            max_fuel_needed = max(max_fuel_needed, a[i] - 0);
        if (i == n - 1)
            max_fuel_needed = max(max_fuel_needed, 2 * (x - a[i]));
        else
            max_fuel_needed = max(max_fuel_needed, a[i + 1] - a[i]);
    }
    cout << max_fuel_needed << endl;
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