#include<bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    int plus = 0, minus = 0;
    for (auto &x : s) {
        if (x == '+') plus++;
        else minus++;
    }

    int tot = plus - minus;

    int q;
    cin >> q;

    while (q-- > 0) {
        int a, b;
        cin >> a >> b;

        if (a == b) {
            if (tot == 0)
                cout << "YES\n";
            else
                cout << "NO\n";
            continue; 
        }

        int x = b * (minus - plus); 
        int y = a - b;

        if (x % y != 0) {
            cout << "NO\n";
            continue; 
        }

        int k = x / y;

        if (k <= plus && k >= -minus)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T = 1;
    // cin >> T;
    while (T--)
        solve();
    
    return 0;
}
