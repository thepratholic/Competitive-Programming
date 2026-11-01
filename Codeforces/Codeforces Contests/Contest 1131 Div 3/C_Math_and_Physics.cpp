#include <bits/stdc++.h>
using namespace std;
#define int long long

/*
    if I take maximum element, then
    I have to maximise that only.

    I can take other elements to maximise that....

*/

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);

    int sum = 0;
    bool any_big = false, i_big = false;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];

        if (a[i] >= 2) {
            any_big = true;

            if (i > 0 && i < n - 1) i_big = true;
        }
    }

    if (!any_big) cout << -1 << "\n";
    else if (i_big) cout << sum - 1 << "\n";
    else cout << sum - (n - 1) << "\n";

}
// TC : 
// SC : 

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