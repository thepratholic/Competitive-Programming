#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    if (n < 4) {
        cout << "NO" << endl;
        return;
    }

    string t;

    for (char ch : s) {
        ch = tolower(ch);

        if (t.empty() || t.back() != ch) t += ch;
    }

    if (t == "meow") {
        cout << "YES" << endl;
    }

    else cout << "NO" << endl;
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