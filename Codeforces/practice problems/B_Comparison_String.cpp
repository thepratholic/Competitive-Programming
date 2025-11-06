#include<bits/stdc++.h>
using namespace std;

#define int long long
#define nline "\n"

void solve() {

    int n;
    cin >> n;

    string s;
    cin >> s;
 
    int ans = 1, maxi = 1;
 
    for (int i = 1; i < n; ++i) {
 
        if (s[i] == s[i - 1]) ++maxi;
        else maxi = 1;
 
        ans = max(ans, maxi);
    }
 
    cout << ans + 1 << endl;
    return;
    
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--)
        solve();

    return 0;
}