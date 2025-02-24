#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    deque<int> q;
    for (int i = 1; i <= n; i++) {
        q.push_back(i);
    }

    vector<int> ans(n, 0);
    int p1 = k - 1;

    for (int i = 0; i < n; i++) {
        while (ans[p1] != 0) {
            p1 = (p1 + 1) % n;
        }
        ans[p1] = q.front();
        q.pop_front();
        p1 = (p1 + k) % n;
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
