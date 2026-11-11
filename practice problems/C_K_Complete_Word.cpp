#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        string s;
        cin >> n >> k >> s;

        long long ans = 0;
        for (int r = 0; r <= (k - 1) / 2; r++) {
            int r2 = k - 1 - r;
            int cnt[26] = {0};
            int total = 0;
            for (int i = r; i < n; i += k) {
                cnt[s[i] - 'a']++;
                total++;
            }
            if (r2 != r) {
                for (int i = r2; i < n; i += k) {
                    cnt[s[i] - 'a']++;
                    total++;
                }
            }
            int mx = *max_element(cnt, cnt + 26);
            ans += total - mx;
        }
        cout << ans << "\n";
    }
    return 0;
}