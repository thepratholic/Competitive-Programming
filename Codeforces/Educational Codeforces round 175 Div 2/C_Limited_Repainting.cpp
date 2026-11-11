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
    long long n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    vector<int> v(n);
    for(int i = 0;i < n;i++) {
        cin >> v[i];
    }

    int low = 0, high = 1e9, ans = 0;

    while (low <= high) {
        int mid = (low + high) >> 1;

        int cnt = 0, f = 1;
        for(int i = 0;i < n;i++) {
            if(v[i] <= mid) continue;
            
            if((s[i] == 'R') ^ f) {
                cnt += f;
                f ^= 1;
            }

        }

        if(cnt <= k) {
            ans = mid;
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }

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