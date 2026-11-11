#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int res = 0;

    for (int b = 30; b >= 0; b--) {
        int cnt = 0;

        for (int x : a) {
            cnt += ((x >> b) & 1);
        }

        if (cnt == n) {
            res |= (1 << b);
        }

        else if(cnt > 0) {
            res |= (1 << (b + 1)) - 1;
            break;
        }

    }

    cout << res << "\n";
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