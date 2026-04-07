#include <bits/stdc++.h>
using namespace std;

#define int long long

vector<vector<int>> tree;
vector<set<int>> st;
vector<int> color, res;

void dfs(int node, int parent) {
    st[node].insert(color[node]);

    for (auto child : tree[node]) {
        if (child == parent) continue;

        dfs(child, node);

        // small-to-large merge
        if (st[node].size() < st[child].size()) {
            swap(st[node], st[child]);
        }

        for (auto x : st[child]) {
            st[node].insert(x);
        }
    }

    res[node] = st[node].size();
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    color.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    tree.resize(n + 1);
    st.resize(n + 1);
    res.resize(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    dfs(1, -1);

    for (int i = 1; i <= n; i++) {
        cout << res[i] << " ";
    }
    cout << "\n";

    return 0;
}