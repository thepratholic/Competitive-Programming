#include <bits/stdc++.h>
using namespace std;
#define int long long

/*
    in the sequence , all the elements
    are pairwise distinct.
    a1 = a2 - a3 + a4 - a5 ......


*/

void solve() {
    int n;
    cin >> n;

    vector<int> b(2 * n);
    for (int i = 0; i < 2 * n; i++) cin >> b[i];

    sort(b.begin(), b.end());

    int s = 0;

    vector<int> g;
    for (int i = 1; i < n; i++) {
        g.push_back(b[i]);
        g.push_back(b[i + n - 1]);
        s += (b[i + n - 1] - b[i]);
    }

    g.push_back(s + b[2 * n - 1] + b[0]);
    g.push_back(b[0]);

    cout << b[2 * n - 1];

    for (int i = 0; i < 2 * n; i++) cout << " " << g[i];

    cout << "\n";
    
}

// TC : O(n log n) + O(n)
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