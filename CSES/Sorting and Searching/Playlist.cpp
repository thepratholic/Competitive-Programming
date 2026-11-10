#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    map<int, int> last;   // unordered_map -> map

    int ans = 0;
    int left = 0;

    for (int i = 0; i < n; i++) {
        auto it = last.find(a[i]);

        if (it != last.end() and it->second >= left) {
            left = it->second + 1;
        }

        last[a[i]] = i;
        ans = max(ans, i - left + 1);
    }

    cout << ans << "\n";
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    solve();
    return 0;
}