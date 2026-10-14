#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    if (n >= 2 && n < 4) {
        cout << "NO SOLUTION" << endl;
        return;
    }

    if (n == 4) {
        cout << "2 4 1 3" << endl;
        return;
    }

    for (int i = 1; i < n + 1; i += 2) {
        cout << i << " ";
    }

    for (int i = 2; i < n + 1; i += 2) {
        cout << i << " ";
    }

    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}