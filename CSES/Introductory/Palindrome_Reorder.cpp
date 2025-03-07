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

void solve()
{
    string s;
    cin >> s;

    ll n = s.size();

    vector<char> v(n);
    map<char, int> mpp;

    for(int i = 0; i < n; i++) {
        mpp[s[i]]++;
    }

    ll cnt = 0;
    char oddChar = 0;
    for(auto &p : mpp) {
        if(p.second % 2 == 1) {
            cnt++;
            oddChar = p.first;
        }
    }

    if(cnt > 1) {
        cout << "NO SOLUTION" << endl;
        return;
    }

    string firstHalf = "";
    string middle = "";
    
    for(auto &p : mpp) {
        ll chars = p.second;

        if(chars % 2 == 1) {
            middle = string(chars, p.first);
        } else {
            while(chars > 0) {
                firstHalf += p.first;
                chars -= 2;
            }
        }
    }

    string ans = firstHalf + middle + string(firstHalf.rbegin(), firstHalf.rend());
    
    cout << ans << endl;
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
