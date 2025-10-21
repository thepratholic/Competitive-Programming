#include<bits/stdc++.h>
using namespace std;

#define int long long
#define nline "\n"

void solve() {
    int x, y, a;
    cin >> x >> y >> a;

    int repeat = a / (x + y);
    int dig = repeat * (x + y);

    if (a < (dig + x)) {
        cout << "NO" << nline;
        return;
    }
    
    cout << "YES" << nline;
}

signed main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--)
        solve();

    return 0;
}