#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    string s = "";
    for (int i = 0; i < n; i++) {
        if (i % 4 == 0 || i % 4 == 1) s += 'a';
        else s += 'b';
    }

    cout << s << endl;
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