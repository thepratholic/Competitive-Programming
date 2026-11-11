// Changed from Py to Cpp for this problem 

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n, q;
        cin >> n >> q;

        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];


        vector<int> order(n);
        iota(order.begin(), order.end(), 0);

        stable_sort(order.begin(), order.end(), [&](int i, int j) {
            return a[i] < a[j];
        });

        vector<int> pi(n);
        for (int rank = 0; rank < n; rank++) {
            pi[order[rank]] = rank;
        }

        int max_diff = 0;
        for (int i = 0; i < n; i++) {
            int d = i ^ pi[i];
            if (d > max_diff) max_diff = d;
        }

        int ans;
        if (max_diff == 0) {
            ans = 0;
        } else {
            int bits = 32 - __builtin_clz(max_diff);
            long long B = 1LL << bits;
            ans = (int)(B / 2);
        }

        cout << ans << "\n";
    }

    return 0;
}