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
    int n;
    cin >> n;

    int m = 32 - __builtin_clz(n);
    int nn = 1 << m;

    vector<int> res;
    res.reserve(2 * nn);

    for (int i = 0; i < nn; i++) {
        if (i > 0) {
            int curr = i ^ (i >> 1);
            int prev = (i - 1) ^ ((i - 1) >> 1);

            res.push_back(curr ^ prev);
        }

        res.push_back(0);
    }

    cout << res.size() << endl;

    for (int x : res) {
        cout << x << ' ';
    }

    cout << endl;
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