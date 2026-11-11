#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;

    string p;
    cin >> p;

    string q;
    cin >> q;

    vector<int> cnt(26, 0);

    for (int i = 0; i < n; i++) {
        cnt[p[i] - 'a']++;
    }

    for (int i = 0; i < m; i++) {
        cnt[q[i] - 'a']--;
    }

    bool ok = true;
    for (int i = 0; i < 26; i++) {
        char c = 'a' + i;
        int need = (c == 's' || c == 'i' || c == 'x') ? 1 : 0;
        if (cnt[i] != need) {
            ok = false;
            break;
        }
    }
    cout << (ok ? "YES" : "NO") << "\n";

}
// TC : 
// SC : 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}