#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n{};
    cin >> n;

    if (n == 2 or n & 1) {
        cout << "NO\n";
    }

    else cout << "YES\n";
}
// TC : O(1)
// SC : O(1)

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}