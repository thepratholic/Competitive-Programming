#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;
vector<bool> vis;
int ans = 0;

void dfs(int node, int parent) {
    for (int nei : adj[node]) {
        if (nei == parent) continue;

        dfs(nei, node);

        if (!vis[nei] && !vis[node]) {
            vis[nei] = vis[node] = true;
            ans++;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    adj.resize(n + 1);
    vis.assign(n + 1, false);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, -1);

    cout << ans << '\n';

    return 0;
}