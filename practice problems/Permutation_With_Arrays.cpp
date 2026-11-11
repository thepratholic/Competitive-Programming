#include <bits/stdc++.h>
#define ll long long
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define Code                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define vr(vec) vec.begin(), vec.end()
#define printy cout << "YES" << endl
#define printn cout << "NO" << endl
#define pi 3.141592653589793238
using namespace std;

int main()
{
    Code int t = 1;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> v1(n), v2(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v1[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> v2[i];
        }
        bool chk = false;
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        for (int i = 0; i < n; i++)
        {
            if (v1[i] != v2[i])
            {
                cout << "no" << endl;
                chk = true;
                break;
            }
        }
        if (chk == false)
            cout << "yes" << endl;
    }

    return 0;
}