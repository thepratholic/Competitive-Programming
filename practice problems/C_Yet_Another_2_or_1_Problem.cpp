#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    bool done = false;
    int m = n;
    string ans;

    while (k > 0 and !done) {
        bool pal = true, same = true;

        for (int i = 0; i < m / 2; i++) {
            if (s[i] != s[m - i - 1]) { pal = false; break; }
        }

        if (pal) {
            for (int i = 0; i < m; i++) {
                if (s[i] != s[0]) {
                    same = false;
                    break;
                }
            }
        }

        if (!pal) {
            k--;
            m /= 2;
        }
        else if (same) {
            ans = s.substr(0, m) + string(k, s[0]);
            done = true;
        }
        else {
            k--;
            if (k == 0) {
                ans = s.substr(0, m) + s[m - 1];
                done = true;
            }
            else {
                k--;
                m = (m + 1) / 2;
            }
        }
    }

    if (!done) ans = s.substr(0, m);
    cout << ans << "\n";
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) solve();

    return 0;
}