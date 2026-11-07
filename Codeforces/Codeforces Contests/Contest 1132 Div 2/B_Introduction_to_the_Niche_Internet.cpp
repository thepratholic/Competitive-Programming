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

    sort(a.begin(), a.end());
    int c = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] == a[n - 1]) {
            c++;
        }
    }

    if (k < c) {
        cout << "NO\n";
        return;
    }

    vector<int> ans;
    for (int i = n - k; i < n; i++) {
        ans.push_back(a[i]);
    }

    for (int i = n - k - 1; i >= 0; i--) {
        ans.push_back(a[i]);
    }

    cout << "YES\n";
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }

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