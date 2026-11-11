#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> cnt(64, 0);
    bool ok = true;


    for (int i = 0; i < n; i++) {
        long long a;       
        cin >> a;

        int p = 0;
        while (a > 0) {
            long long r = a % k;
            if (r > 1) ok = false;
            else if (r == 1) {
                if (++cnt[p] > 1) ok = false;
            }

            p++;
            a /= k;
        }
    }

    cout << (ok ? "YES" : "NO") << "\n";
}

// TC : O(N log K)
// SC : O(1)

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}