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

    vector<int> ans;

    if (n == 1) {
        cout << -1 << endl;
        return;
    }

    vector<int> vis(n+1, 0);
    for(int i = 2;i <= n;i+=2) {
        ans.push_back(i);
        vis[i] =1;
    }

    for(int i = 1;i <= n;i++) {
        if(vis[i] == 0) {
            ans.push_back(i);
        }
    }



    long long sum = 0;
    for(int i = 1; i<= n;i++) {
        sum += ans[i];
        if(i * i == sum) {
            if(i + 1 <= n) {
                swap(ans[i], ans[i+1]);
            }
        }
    }

    for(auto ele : ans) {
        cout << ele << " ";
    }
    cout << endl;
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