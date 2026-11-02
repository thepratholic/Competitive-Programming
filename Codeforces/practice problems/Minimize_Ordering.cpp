#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    string s;
    cin >> s;

    vector<int> cnt(26, 0);
    for (auto &ch : s) {
        cnt[ch - 'a']++;
    }

    string ans = "";

    for (int i = 0; i < 26; i++) {
        while (cnt[i] > 0) {
            ans.push_back('a' + i);
            cnt[i]--;
        }
    }

    cout << ans << "\n";
}
// TC : O(n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}