#include <bits/stdc++.h>
using namespace std;

#define int long long
#define all(x) x.begin(), x.end()
#define pb push_back
#define endl '\n'
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);


#define debug(x) cerr << #x << " = " << (x) << endl;

void solve() {
    string s;
    cin >> s;
    int n = s.size();

    string ans = "";
    for(int i = 0;i < n && ans.empty();i++) {
        if(i + 1 < n && s[i] == s[i + 1]) {
            ans = s.substr(i, 2);
        }
        else if(i + 2 < n && s[i] != s[i+1] && s[i] != s[i+2] && s[i+1] != s[i+2]) {
            ans = s.substr(i, 3);
        }
    }

    if(ans.empty()) {
        cout << "-1" << endl;
    }
    else{
        cout << ans << endl;
    }
}

int32_t main() {
    fast_io;
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}