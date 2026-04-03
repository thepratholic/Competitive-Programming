#include <bits/stdc++.h>
using namespace std;

const int N = 200005;
const int LOG = 20;

vector<int> adj[N];
int up[N][LOG];
int depth[N];

int n, q;

void bfs() {
    queue<int> qu;
    qu.push(1);

    while (!qu.empty()) {
        int node = qu.front();
        qu.pop();

        for (int child : adj[node]) {
            if (child != up[node][0]) {
                depth[child] = depth[node] + 1;
                qu.push(child);
            }
        }
    }
}

int kth_anc(int node, int k) {
    for (int i = 0; i < LOG; i++) {
        if (k & (1 << i)) {
            node = up[node][i];
            if (node == -1) break;
        }
    }
    return node;
}

int lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);

    // bring u up
    int diff = depth[u] - depth[v];
    u = kth_anc(u, diff);

    if (u == v) return u;

    for (int i = LOG - 1; i >= 0; i--) {
        if (up[u][i] != -1 && up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }

    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < LOG; j++) {
            up[i][j] = -1;
        }
    }

    for (int i = 2; i <= n; i++) {
        int p;
        cin >> p;
        up[i][0] = p;

        adj[i].push_back(p);
        adj[p].push_back(i);
    }

    bfs();

    // binary lifting preprocess
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= n; i++) {
            if (up[i][j - 1] != -1) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }
    }

    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }

    return 0;
}