#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i] = 1LL << a[i];
    }

    sort(a.rbegin(), a.rend());

    int x = 0, y = 0;
    for (int i = 0; i < n; i++) {
        if (x <= y) {
            x += a[i];
        } else {
            y += a[i];
        }
    }

    cout << x * y << "\n";


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