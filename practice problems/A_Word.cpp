#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    string s;
    cin >> s;

    int lo = 0, up = 0;

    for (char ch : s) {
        if (ch == toupper(ch)) up++;
        else lo++;
    }

    bool equal = (lo == up);
    bool small = (lo > up);
    
    string ans;

    if (equal) {
        for (char ch : s) {
            ans += tolower(ch);
        }
    }

    else {
        if (small) {
            for (char ch : s) {
                ans += tolower(ch);
            }
        }

        else {
            for (char ch : s) {
                ans += toupper(ch);
            }
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