#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    map<int, int> count;

    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }

    vector<int> good;
    for (auto it : count) {
        if (it.second >= k) {
            good.push_back(it.first);
        }
    }

    if (good.empty()) {
        cout << -1 << endl;
        return;
    }

    sort(good.begin(), good.end());

    int start = good[0], l = good[0], r = good[0];

    for (int i = 1; i < good.size(); i++) {
        if (good[i] - 1 != good[i - 1]) {
            start = good[i];
        }

        if (good[i] - start > r - l) {
            l = start;
            r = good[i];
        }
    }

    cout << l << " " << r << endl;
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