#include <bits/stdc++.h>
using namespace std;

#define int         long long
#define pb          push_back
#define ppb         pop_back
#define pf          push_front
#define ppf         pop_front
#define all(x)      (x).begin(), (x).end()
#define rall(x)     (x).rbegin(), (x).rend()
#define sz(x)       (int)(x).size()
#define mp          make_pair
#define ff          first
#define ss          second
#define yes         cout << "YES\n"
#define no          cout << "NO\n"
#define endl        "\n"
#define MOD         1000000007
#define INF         1e18
#define PI          acos(-1.0)

typedef pair<int,int>   pii;
typedef vector<int>     vi;
typedef vector<pii>     vpii;

void solve() {
    int a, b;
    cin >> a >> b;

    if ((a % 2) == (b % 2)) {
        if (b <= a) {
            cout << a << endl;
        }

        else {
            cout << -1 << endl;
        }
    }

    else {
        if (b <= a + 1) cout << a + 1 << endl;
        else cout << -1 << endl;
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}