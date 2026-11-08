#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, t;
    cin >> n >> t;

    vector<pair<int,int>> v(n);
    for (int i = 0; i < n; i++) { 
        cin >> v[i].first; v[i].second = i + 1; 
    }

    sort(v.begin(), v.end());
    
    int l = 0, r = n - 1;

    while (l < r) {
        int s = v[l].first + v[r].first;
        if (s == t) { 
            cout << v[l].second << " " << v[r].second << "\n"; 
            return; 
        }
        
        if (s < t) l++; else r--;
    }

    cout << "IMPOSSIBLE\n";
}
// TC : O(n)
// SC : O(n)

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