#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define int long long

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

void solve() {
    int n;
    cin >> n;

    vector<pair<int, int>> a(n);
    for (auto &p : a) cin >> p.first >> p.second;

    sort(a.begin(), a.end());

    ordered_set os;
    int ans = 0;

    for (int i = 0; i < n; i++) {
        ans += (int)os.size() - (int)os.order_of_key(a[i].second);
        os.insert(a[i].second);
    }

    cout << ans << "\n";
}
// TC : O(n log n) per test
// SC : O(n)

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