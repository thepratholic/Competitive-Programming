#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for(auto &x : a) {
        cin >> x;
    }

    int ans = 0;
    vector<int> bits(1e6 + 25, 0);

    for(auto &i : a) bits[i]++;

    for(int i = 0; i <= 1e6 + 24; i++) {
        bits[i + 1] += bits[i] / 2;
        if(bits[i] & 1) ans++;
    }

    cout << ans << "\n";
    
}

signed main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 1;
    // cin >> T;

    while (T--)
        solve();

    return 0;
}