#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int &i : a) cin >> i;

    bool ok = true;
    for (int i = 0; i < n - 1; i++) {
        if (a[i + 1] - a[i] > 1) {
            ok = false;
            break;
        }
    }

    if (ok) cout << "Yes\n";
    else cout << "No\n";
}
// TC : O(n)
// SC : O(n) for vector

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}