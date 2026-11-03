#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto &x : a) cin >> x;

    vector<int> v;

    for (int i = 0; i < n; i++) {
        int j = i;

        // ab 1-run dekho
        while (j < n and a[j] == 1) j++;

        if (j == n) {
            cout << "NO\n"; // agar 0 nai hai, toh yeh saare i...j ones invert nai ho skte
            return;
        }

        v.push_back(j - i); // this is the p-integer
        for (int k = i; k < j; k++) {
            v.push_back(0);
        }

        i = j;
    }

    reverse(v.begin(), v.end());
    cout << "YES\n";

    for (auto &x : v) {
        cout << x << " ";
    }

    cout << "\n";
}
// TC : O(n)
// SC : O(n)

signed main() {
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