#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    bool used[26] = {false};
    for (int i = 0; i < n / 2; i++) {
        int a = s[i] - 'a';
        int b = s[n - i - 1] - 'a';
        if (a > b) swap(a, b);

        for (int x = a + 1; x <= b; x++) used[x] = true;
    }

    int ans = 0;
    for (int i = 1; i < 26; i++) {
        if (used[i]) ans += 1;
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