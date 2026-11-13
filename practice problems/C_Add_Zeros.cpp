#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        map<long long, vector<long long>> g;
        for (int i = 1; i <= n; i++) {
            long long a;
            scanf("%lld", &a);
            if (i == 1) continue;
            long long u = a + i - 1;
            if (u >= n) g[u].push_back(u + i - 1);
        }
        set<long long> vis;
        vector<long long> st = {n};
        vis.insert(n);
        long long best = n;
        while (!st.empty()) {
            long long x = st.back();
            st.pop_back();
            best = max(best, x);
            auto it = g.find(x);
            if (it == g.end()) continue;
            for (long long y : it->second)
                if (vis.insert(y).second) st.push_back(y);
        }
        printf("%lld\n", best);
    }
}