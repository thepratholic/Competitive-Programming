#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        long long k;
        cin >> n >> k;
        vector<int> a(n);
        for (auto &x : a) cin >> x;

        if (k > 10) k = 10 + (k % 2);

        while (k--) {
            vector<int> cnt(n + 2, 0);
            for (int x : a) cnt[x]++;

            int m = 0;
            while (cnt[m] > 0) m++;

            for (int i = 0; i < n; i++) {
                if (a[i] < m && cnt[a[i]] == 1) continue;
                a[i] = m;
            }
        }

        long long sum = 0;
        for (int x : a) sum += x;
        cout << sum << "\n";
    }
    return 0;
}