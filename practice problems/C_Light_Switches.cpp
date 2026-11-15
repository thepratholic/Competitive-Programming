#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        long long n, k;
        cin >> n >> k;
        vector<long long> a(n);
        long long mx = 0;
        for (auto &x : a) {
            cin >> x;
            mx = max(mx, x);
        }

        long long p = 2 * k;
        long long lo = mx, hi = LLONG_MAX;

        for (auto x : a) {
            long long s = x + ((mx - x) / p) * p; 
            long long l, r;
            if (s + k > mx) {     
                l = mx;
                r = s + k - 1;
            } else {                
                l = s + p;
                r = s + p + k - 1;
            }
            lo = max(lo, l);
            hi = min(hi, r);
        }

        cout << (lo <= hi ? lo : -1) << "\n";
    }
    return 0;
}