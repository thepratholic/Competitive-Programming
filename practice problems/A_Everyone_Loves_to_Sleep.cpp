#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, h, m;
    cin >> n >> h >> m;

    int bed = h * 60 + m;
    int best = INT_MAX;

    for (int i = 0; i < n; i++) {
        int hi, mi;
        cin >> hi >> mi;

        int alarm = hi * 60 + mi;

        int sleep;

        if (alarm >= bed) {
            sleep = alarm - bed;
        }

        else {
            sleep = 1440 - (bed - alarm);
        }

        best = min(best, sleep);
    }

    cout << best / 60 << " " << best % 60 << "\n";
} 
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}