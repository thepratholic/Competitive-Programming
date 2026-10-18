#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<string> s(n);
    vector<string> t(m);

    for(int i = 0; i < n; i++) {
        cin >> s[i];
    }

    for (int i = 0; i < m; i++) {
        cin >> t[i];
    }

    vector<int> ans(n, 0);

    for (int i = 0; i < m; i++) {
        int exact = -1;

        for (int j = 0; j < n; j++) {
            if (t[i] == s[j]) {
                exact = j;
                break;
            }
        }

        if (exact != -1) {
            ans[exact]++;
            continue;
        }

        int cnt = 0, idx = -1;

        for (int j = 0; j < n; j++) {
            if (t[i].size() != s[j].size()) continue;

            int diff = 0;

            for (int k = 0; k < s[j].size(); k++) {
                if (t[i][k] != s[j][k]) diff++;
            }

            if (diff == 1) {
                idx = j;
                cnt++;
            }
        }

        if (cnt == 1) {
            ans[idx]++;
        }

    }
    
    for (int i = 0; i < n; i++) {
        cout << ans[i] << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}