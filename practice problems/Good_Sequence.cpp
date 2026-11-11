#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    unordered_map<int, int> freq;

    int ans = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        freq[x]++;
    }

    for (auto it : freq) {
        if (it.first == it.second) {
            continue;
        }

        if (it.second > it.first) {
            ans += abs(it.first - it.second);
        }

        else {
            ans += it.second;
        }   
    }

    cout << ans << "\n";
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