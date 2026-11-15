#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    string s, t, p;
    cin >> s >> t >> p;

    int j = 0;
    for (int i = 0; i < (int)t.size(); i++) {
        if (t[i] == s[j]) j++;
    }

    if (j != (int)s.size()) {
        cout << "NO\n";
        return;
    }

    vector<int> count_s(26, 0), count_t(26, 0), count_p(26, 0);
    for (char ch : s) count_s[ch - 'a']++;
    for (char ch : t) count_t[ch - 'a']++;
    for (char ch : p) count_p[ch - 'a']++;

    for (int c = 0; c < 26; c++) {
        if (count_s[c] + count_p[c] < count_t[c]) {
            cout << "NO\n";
            return;
        }
    }

    cout << "YES\n";
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