#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<int> p(n + 1);
        for (int i = 1; i <= n; i++) scanf("%d", &p[i]);
        vector<char> vis(n + 1, 0);
        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            if (vis[i]) continue;
            int len = 0, j = i;
            while (!vis[j]) {
                vis[j] = 1;
                j = p[j];
                len++;
            }
            ans += (len - 1) / 2;
        }
        printf("%lld\n", ans);
    }
    return 0;
}