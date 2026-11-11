#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n{};
    cin >> n;

    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first;
        a[i].second = i + 1; // 1-based
    }

    sort(a.begin(), a.end(), greater<pair<int, int>>());

    vector<int> x(n + 1);
    x[0] = 0;

    int total = 0;

    for (int i = 0; i < n; i++) {
        int dist = (i / 2) + 1;
        int pos = (i % 2 == 0) ? dist : -dist;

        x[a[i].second] = pos;
        total += (2LL * dist * a[i].first);
    }

    cout << total << "\n";
    for (auto &i : x) {
        cout << i << " ";
    }

    cout << "\n";

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