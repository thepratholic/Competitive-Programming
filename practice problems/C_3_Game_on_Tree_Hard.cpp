/* Three Golden Rules :
1) Solution is Simple
2) Proof is Simple
3) Implementation is Simple
*/


#include<bits/stdc++.h>
using namespace std;

#define int long long
#define nline "\n"

void solve() {
    int n, t;
    cin >> n >> t;

    vector<vector<int>> adj(n);
    vector<int> paired(n, -1);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // DFS for pairing (recursive is safe in C++)
    function<void(int,int)> dfs = [&](int u, int parent) {
        for (int v : adj[u]) {
            if (v == parent) continue;

            dfs(v, u);

            if (paired[u] == -1 && paired[v] == -1) {
                paired[u] = v;
                paired[v] = u;
            }
        }
    };

    dfs(0, -1);

    vector<bool> seen(n, false);
    queue<int> q;

    // initial losing nodes
    for (int i = 0; i < n; i++) {
        if (paired[i] == -1) {
            seen[i] = true;
            q.push(i);
        }
    }

    // BFS: propagate losing states
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int nei : adj[cur]) {
            int other = paired[nei];

            if (other == -1) continue;
            if (seen[other]) continue;

            seen[other] = true;
            q.push(other);
        }
    }

    // queries (t = 1 in easy, but keeping general)
    while (t--) {
        int x;
        cin >> x;
        --x;

        if (seen[x])
            cout << "Hermione\n";
        else
            cout << "Ron\n";
    }
    
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 1;
    // cin >> T;

    while (T--)
        solve();

    return 0;
}