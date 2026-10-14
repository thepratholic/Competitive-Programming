#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (auto &x : a) cin >> x;

    sort(a.rbegin(), a.rend());

    int ans = 0;
    for (int i = 0; i <= min(n - 1, k); i++) {
        ans += a[i];
    }

    cout << ans << endl;
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