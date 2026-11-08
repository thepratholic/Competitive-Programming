#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // if the last digit in a is < 10^m, then Anna will win, otherwise Sasha will win
    int total = 0;
    vector<int> z(n);
    for (int i = 0; i < n; i++) {
        while (a[i] % 10 == 0) {
            z[i]++;
            a[i] /= 10;
        }

        while (a[i] > 0) {
            total++;
            a[i] /= 10;
        }
    }

    sort(z.begin(), z.end(), greater<int>());

    for (int i = 1; i < n; i += 2) {
        total += z[i];
    }

    if (total <= m) {
        cout << "Anna\n";
    } else {
        cout << "Sasha\n";
    }
}
// TC : O(n log n)
// SC : O(n)

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