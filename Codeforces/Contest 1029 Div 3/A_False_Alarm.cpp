#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, x;
    cin >> n >> x;
    vector<int> a(n);
    for (int &v : a) cin >> v;
    int first = -1, last = -1;
    for (int i = 0; i < n; ++i) {
        if (a[i] == 1) {
            if (first == -1) first = i;
            last = i;
        }
    }
    int segment = last - first + 1;
    cout << (segment <= x ? "YES" : "NO") << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
