#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        bool ok = false;
        for (int i = 0; i < n; i++) {
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            if (b == c) ok = true;
        }
        cout << ((m % 2 == 0 && ok) ? "YES" : "NO") << "\n";
    }
    return 0;
}