#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void solve() {
    int a, b, c;
    cin >> a >> b >> c;

    vector<int> arr = {a, b, c};
    sort(arr.begin(), arr.end());

    if (arr[0] == arr[1] - 1 && arr[0] == arr[2] - 2) {
        cout << "YES\n";
    }
    else cout << "NO\n";
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