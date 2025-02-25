#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end()); // Sort the array for easy pairing

    int mx = 0;
    for (int i = 0; i < n; i += 2) {
        if (max(mx, a[i]) != max(mx, a[i + 1])) {
            cout << "NO\n";
            return;
        }
        mx = max(mx, a[i]) + 1; // Move to the next possible increment
    }

    cout << "YES\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
