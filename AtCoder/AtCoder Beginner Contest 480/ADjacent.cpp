#include <bits/stdc++.h>
using namespace std;

void solve() {
    char a, b, c, d;
    cin >> a >> b >> c >> d;

    if (a == 'A' && (b == 'D' || c == 'D')) {
        cout << "Yes\n";
    }
    else if (b == 'A' && (a == 'D' || d == 'D')) {
        cout << "Yes\n";
    }
    else if (c == 'A' && (a == 'D' || d == 'D')) {
        cout << "Yes\n";
    }
    else if (d == 'A' && (b == 'D' || c == 'D')) {
        cout << "Yes\n";
    }
    else {
        cout << "No\n";
    }
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