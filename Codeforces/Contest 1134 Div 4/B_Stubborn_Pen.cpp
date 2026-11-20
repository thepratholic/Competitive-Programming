#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n; cin >> n;

    string s;
    cin >> s;

    char init = 'R';
    int ans = 0;

    for (char &ch : s) {
        if (ch != init) {
            ans += 1;
        }

        init = (ch == 'B') ? 'R' : 'B';
    }

    cout << ans << endl;
}
// TC : 
// SC : 

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