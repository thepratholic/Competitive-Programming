#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    int a[n];
    unordered_map<int, int> boxes;
    for (int i = 0; i < n; i++) {
        cin >> a[i]; 
        boxes[a[i]]++;
    }

    int ans = 0;

    for (auto &p : boxes) {
        ans = max(ans, p.second);
    }

    cout << ans << endl;


}
// TC : O(n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}