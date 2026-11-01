#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int a, b;
    cin >> a >> b;

    int n;
    cin >> n;

    double ans = 1e9;

    while (n--) {
        int x, y, v;
        cin >> x >> y >> v;

        int dx = x - a;
        int dy = y - b;

        double dist = sqrt(pow(dx, 2) + pow(dy, 2));
        double time = dist / v;

        ans = min(ans, time);
    }

    cout << fixed << setprecision(20) << ans << "\n";
    
}
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}