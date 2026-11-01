#include <bits/stdc++.h>
using namespace std;

#define int long long

void solve() {
    int n;
    cin >> n;
    vector<int> o, e;
    int sum = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        sum += x;

        if (i % 2 == 0) o.push_back(x);
        else e.push_back(x);
    }

    sort(o.begin(), o.end());
    sort(e.begin(), e.end());

    int m = min(o.size(), e.size());
    for (int i = 0; i < m; i++) {
        int s = o[i] + e[i];

        if (s >= 0) break;

        sum -= 2 * s;
    }
    cout << sum << "\n";
}
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}