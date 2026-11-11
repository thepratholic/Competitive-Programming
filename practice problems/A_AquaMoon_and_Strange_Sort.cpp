#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    if (is_sorted(a.begin(), a.end())) {
        cout << "YES\n";
        return;
    }

    vector<int> ev, od;

    for (int i = 0; i < n; i++) {
        if (i & 1) od.push_back(a[i]);
        else ev.push_back(a[i]);
    }

    sort(ev.begin(), ev.end());
    sort(od.begin(), od.end());

    vector<int> res(n);

    for (int i = 0, e = 0, o = 0; i < n; i++) {
        if (i & 1) res[i] = od[o++];
        else res[i] = ev[e++];
    }

    if (is_sorted(res.begin(), res.end())) {
        cout << "YES\n";
    }

    else {
        cout << "NO\n";
    }
}
// TC : O(n)
// SC : O(n)

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