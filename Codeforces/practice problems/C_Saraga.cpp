#include<bits/stdc++.h>
using namespace std;

#define int long long
#define nline "\n"

void solve() {
    string s, t;
    cin >> s;
    cin >> t;

    int m = s.size(), n = t.size();

    string ans = "";
    map<int, vector<int>> occurence_s, occurence_t;

    for(int i = 1; i < m; i++) occurence_s[s[i]].push_back(i);
    for(int i = 0; i < n - 1; i++) occurence_t[t[i]].push_back(i);

    for(auto &it : occurence_s) {
        char c = it.first;

        if(occurence_t.find(c) != occurence_t.end()) {
            int i = occurence_s[c].front();
            int j = occurence_t[c].back();

            string tmp = s.substr(0, i) + t.substr(j);

            if (ans.empty() or (ans.size() > tmp.size())) {
                ans = tmp;
            }
        }
    }

    if(ans.empty()) {
        cout << "-1" << nline;
    }

    else {
        cout << ans << nline;
    }
    
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 1;
    // cin >> T;

    while (T--)
        solve();

    return 0;
}