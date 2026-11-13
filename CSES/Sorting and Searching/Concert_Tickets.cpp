#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, m;
    cin >> n >> m;

    multiset<int> tickets;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        tickets.insert(x);
    }

    for (int i = 0; i < m; i++) {
        int price;
        cin >> price;

        auto it = tickets.upper_bound(price);


        if (tickets.empty() or price < *tickets.begin()) {
            cout << "-1\n";
            continue;
        }


        it--;
        cout << *it << "\n";
        tickets.erase(it);
    }
}
// TC : O(n log n) + O(m log n)
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