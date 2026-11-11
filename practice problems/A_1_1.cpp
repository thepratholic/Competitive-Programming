#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    int start = -1, last = -1;
    int mn = 0, mx = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] == '0') continue;

        if (start == -1) {
            start = i;
            last = i;
        }

        else if ((i - last) < 3) {
            last = i;
        }

        else {
            mx += (last - start + 1);
            mn += (last - start + 3) / 2;

            start = i;
            last = i;
        }

    }
    
    if (start != -1) {
        mx += (last - start + 1);
        mn += (last - start + 3) / 2;
    }

    cout << mn << " " << mx << endl;

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}