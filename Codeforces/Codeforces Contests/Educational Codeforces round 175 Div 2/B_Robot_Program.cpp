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
    long long n, x, k;
    cin >> n >> x >> k;

    string s;
    cin >> s;

    bool f = 0;
    for(int i = 0; i < n;i++) {
        if(s[i] == 'L') {
            x--;
        }
        else{
            x++;
        }
        k--;

        if(x == 0) {
            f = 1;
            break;
        }
        if(k == 0) {
            cout << "0" << endl;
            return;
        }
    }

    if(f == 0) {
        cout << "0" << endl;
        return;
    }

    int ans = 1;
    f = 0;
    int t = 0;

    for(int i = 0;i < n;i++) {
        if(s[i] == 'L') x--;
        else x++;

        t++;
        if(x == 0) {
            f = 1;
            break;
        }
    }

    if(f) ans += k / t;
    cout << ans << endl;
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