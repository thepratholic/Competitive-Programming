#include <bits/stdc++.h>
using namespace std;
#define int long long

string norm(const string &s) {
    string ans;
    for (char ch : s) {
        if (ch == '-' || ch == ';' || ch == '_') continue;
        ans += tolower(ch);
    }

    return ans;
}

void solve() {
    vector<string> a(3);
    for (int i = 0; i < 3; i++) {
        string x;
        cin >> x;
        a[i] = norm(x);
    }

    sort(a.begin(), a.end());

    set<string> seen;
    do {
        seen.insert(a[0] + a[1] + a[2]);
    } while (next_permutation(a.begin(), a.end()));

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        string ans = norm(s);
        if (seen.count(ans)) cout << "ACC\n";
        else cout << "WA\n";
    }

}
// TC : (n * l) n <= 1000, l <= 600
// SC : O(300)

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