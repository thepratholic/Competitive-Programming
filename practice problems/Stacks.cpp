#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    multiset<int> ms;
    ms.insert(a[0]);

    for (int i = 1; i < n; i++) {
        if (a[i] >= *ms.rbegin()) ms.insert(a[i]);

        else {
            auto it = ms.upper_bound(a[i]);
            ms.erase(it);
            ms.insert(a[i]);
        }
    }

    cout << ms.size() << " ";
    for (auto it : ms) cout << it << " ";
    cout << "\n";
}
// TC : O(n log n)
// SC : O(n)

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