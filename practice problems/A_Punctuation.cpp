#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    string s;
    getline(cin, s);

    bool pending = false;
    bool need = false;
    string ans;

    for (char c : s) {
        if (c == ' ') {
            pending = true;
        }

        else if (c == '.' or c == ',' or c == '?' or c == '!') {
            ans += c;
            need = true;
            pending = false;
        }

        else {
            if (need or (pending and !ans.empty())) {
                ans += ' ';
            }

            ans += c;
            pending = false;
            need = false;
        }
    }

    cout << ans << "\n";
}
// TC : 
// SC : 

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