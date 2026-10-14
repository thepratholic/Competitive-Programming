#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    long long ans = 0;

    for (int i = 1; i < n; i++) {
        if (a[i] >= a[i - 1]) continue;
        else {
            ans += 1LL * (a[i - 1] - a[i]);
            a[i] = a[i - 1];
        }
    }

    cout << ans << "\n";
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