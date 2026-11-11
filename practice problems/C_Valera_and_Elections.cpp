#include <bits/stdc++.h>
using namespace std;

#define int long long

vector<vector<int>> tree;
vector<int> bad;
vector<int> subtree;

int dfs(int node, int parent) {

    if (bad[node])
        subtree[node]++;

    for (int child : tree[node]) {

        if (child == parent)
            continue;

        subtree[node] += dfs(child, node);
    }

    return subtree[node];
}

void solve() {

    int n;
    cin >> n;

    tree.assign(n + 1, {});
    bad.assign(n + 1, 0);
    subtree.assign(n + 1, 0);

    for (int i = 0; i < n - 1; i++) {

        int u, v, t;
        cin >> u >> v >> t;

        tree[u].push_back(v);
        tree[v].push_back(u);

        if (t == 2) {
            bad[u] = 1;
            bad[v] = 1;
        }
    }

    dfs(1, 0);

    vector<int> ans;

    for (int node = 1; node <= n; node++) {
        if (subtree[node] == 1)
            ans.push_back(node);
    }

    cout << ans.size() << '\n';

    for (int node : ans)
        cout << node << ' ';

    cout << '\n';
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}