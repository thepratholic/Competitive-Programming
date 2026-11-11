#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    for (char &c : s) {
        c = tolower(c);
    }

    set<char> unique_chars(s.begin(), s.end());
    if (unique_chars.size() == 26) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
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