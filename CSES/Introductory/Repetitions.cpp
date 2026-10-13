#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >> s;

    int n = s.size();

    int mx = 0;
    int i = 0;

    while (i < n) {
        int j = i;
        while (j < n and s[j] == s[i]) {
            j ++;
        }

        mx = max(mx, j - i);
        i = j;
    }

    cout << mx << endl;
    
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