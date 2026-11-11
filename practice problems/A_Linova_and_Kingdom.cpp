#include <bits/stdc++.h>
using namespace std;

#define int long long

vector<vector<int>> g;
vector<int> depth, subtree;

void dfs(int u, int parent) {
    subtree[u] = 1;
    for (int v : g[u]) {
        if (v == parent) continue;
        depth[v] = depth[u] + 1;
        dfs(v, u);
        subtree[u] += subtree[v];
    }
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    g.resize(n);
    depth.assign(n, 0);
    subtree.assign(n, 0);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    dfs(0, -1); // root = node 0

    vector<int> gain;

    for (int i = 0; i < n; i++) {
        gain.push_back(depth[i] - (subtree[i] - 1));
    }

    sort(gain.rbegin(), gain.rend());

    int ans = 0;
    for (int i = 0; i < k; i++) {
        ans += gain[i];
    }

    cout << ans << '\n';

    return 0;
}