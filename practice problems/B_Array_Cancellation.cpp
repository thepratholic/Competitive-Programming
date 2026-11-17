#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int n; cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int pos = 0;
    int rem_neg = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] >= 0) pos += a[i];

        else {
            int needed = abs(a[i]); // yeh -ve hai

            if (pos >= needed) {
                pos -= needed;
            }

            else { // +ve elements kam hai, then cost operation karna padega
                rem_neg += (needed - pos);
                pos = 0;
            }
        }
    }

    cout << rem_neg << endl;
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