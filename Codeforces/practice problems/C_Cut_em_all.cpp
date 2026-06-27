#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> tree;
vector<int> sz;

void dfs(int node, int parent) {
    sz[node] = 1;

    for (int child : tree[node]) {
        if (child == parent) continue;

        dfs(child, node);
        sz[node] += sz[child];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n & 1) {
        cout << -1 << '\n';
        return 0;
    }

    tree.resize(n + 1);
    sz.resize(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    dfs(1, 0);

    int ans = 0;
    for (int i = 2; i <= n; i++) {
        if (sz[i] % 2 == 0)
            ans++;
    }

    cout << ans << '\n';

    return 0;
}