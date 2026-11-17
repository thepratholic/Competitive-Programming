#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];

    int i = 0;
    while (i < n - 1 && a[i] < a[i + 1]) i++;

    while (i < n - 1 && a[i] == a[i + 1]) i++;

    while (i < n - 1 && a[i] > a[i + 1]) i++;

    if (i == n - 1) {
        cout << "YES" << endl;
    }

    else cout << "NO" << endl;
}
// TC : 
// SC : 

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