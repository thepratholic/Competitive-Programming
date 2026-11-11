#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    if (n > 26) {
        cout << -1 << "\n";
        return;
    }

    unordered_set<char> st;
    for (int i = 0; i < n; i++) {
        st.insert(s[i]);
    }

    cout << n - st.size() << "\n";

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