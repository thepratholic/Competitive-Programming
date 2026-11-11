#include <bits/stdc++.h>
using namespace std;

// Macros for faster coding
#define int long long
#define all(x) x.begin(), x.end()
#define pb push_back
#define endl '\n'
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

// Debugging Macros
#define debug(x) cerr << #x << " = " << (x) << endl;

void solve() {
    long long n;
    cin >> n;

    if (n == 0) {
        cout << 1 << endl;
        return;
    }

    cout << 3 * (n / 15) + min(3LL, (n % 15) + 1LL) << endl;
}

int32_t main() {
    fast_io;
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}