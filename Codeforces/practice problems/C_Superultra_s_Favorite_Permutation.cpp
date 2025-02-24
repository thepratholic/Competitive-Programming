#include <bits/stdc++.h>
using namespace std;

// Macros for faster coding
#define int long long
#define all(x) x.begin(), x.end()
#define pb push_back
#define endl '\n'
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

#define debug(x) cerr << #x << " = " << (x) << endl;

bool isPrime(int n) {
    for(int i = 2;i * i <= n;i++) {
        if(n % i == 0) return false;
    }
    return true;
}

void solve() {
    int n;
    cin >> n;

    if (n < 5) {
        cout << "-1\n";
        return;
    }
    for (int i = 2; i <= n; i += 2) {
        if (i != 4) cout << i << " ";
    }
    cout << "4 5 ";

    for (int i = 1; i <= n; i += 2) {
        if (i != 5) cout << i << " ";
    }
    cout << "\n";
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