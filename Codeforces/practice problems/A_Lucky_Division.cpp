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
    int n;
    cin >> n;

    if(n%4==0||n%7==0||n%47==0||n%744==0||n%477==0){
        cout << "YES" << endl;
        return;
    }

    cout << "NO" << endl;
}

int32_t main() {
    fast_io;
    // int t = 1;
    // cin >> t;
    // while (t--) {
    solve();
    // }
    return 0;
}