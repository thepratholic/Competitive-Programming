#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    int a = 0, d = 0;
    for (char c : s) {
        if (c == 'A') {
            a++;
        } else {
            d++;
        }
    }

    if (a > d) {
        cout << "Anton\n";
    } else if (d > a) {
        cout << "Danik\n";
    } else {
        cout << "Friendship\n";
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