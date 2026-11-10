#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, m, k;
    cin >> n >> m >> k;

    set<pair<int, int>> fences;
    int ans = 4LL * k;

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        fences.insert({x, y});
    }

    for (auto fence : fences) {
        int x = fence.first;
        int y = fence.second;

        if (fences.count({x + 1, y})) ans -= 2;
        if (fences.count({x, y + 1})) ans -= 2;
    }

    cout << ans << "\n";
}
// TC : O(k log k)
// SC : O(k)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}