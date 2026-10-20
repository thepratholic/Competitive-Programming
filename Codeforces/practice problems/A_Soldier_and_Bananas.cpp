#include <bits/stdc++.h>
using namespace std;

void solve() {
    int k, n, w;
    cin >> k >> n >> w;

    int need = 0;
    for (int i = 1; i <= w; i++) {
        need += (i * k);
    }

    int ans = (need - n);

    if (ans > 0) {
        cout << ans << endl;
    }

    else {
        cout << 0 << endl;
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