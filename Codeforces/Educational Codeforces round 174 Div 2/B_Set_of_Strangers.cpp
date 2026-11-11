#include <bits/stdc++.h>
using namespace std;

#define int long long
#define all(x) x.begin(), x.end()
#define pb push_back
#define endl '\n'
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

#define debug(x) cerr << #x << " = " << (x) << endl;

void solve() {
    int n, m;
    cin >> n >> m;
    int arr[n][m];
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < m;j++){
            cin >> arr[i][j];
        }
    }

    unordered_map<int, int> mpp;
    int ans = 0, m1 = 0;

    for(int i = 0;i < n;i++) {
        for(int j = 0;j < m;j++) {
            if(mpp.find(arr[i][j]) == mpp.end()) mpp[arr[i][j]] = 1;
            if(j-1 >= 0 && arr[i][j-1] == arr[i][j]) mpp[arr[i][j]] = 2;
            if(j+1 < m && arr[i][j+1] == arr[i][j]) mpp[arr[i][j]] = 2;
            if(i-1 >= 0 && arr[i-1][j] == arr[i][j]) mpp[arr[i][j]] = 2;
            if(i+1 < n && arr[i+1][j] == arr[i][j]) mpp[arr[i][j]] = 2;
        }
    }

    for (auto &p : mpp) {
        ans += p.second;
        m1 = max(m1, p.second);
    }

    cout << ans - m1 << endl;
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