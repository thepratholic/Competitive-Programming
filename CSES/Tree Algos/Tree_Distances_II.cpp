#include <bits/stdc++.h>
using namespace std;

#define ll long long

int n;
vector<vector<int>> adj;
vector<ll> subtree_size, dp;
vector<ll> res;

void preCalc(int node, int parent) {
    for (auto child : adj[node]) {
        if (child != parent) {
            preCalc(child, node);

            subtree_size[node] += subtree_size[child];
            dp[node] += (dp[child] + subtree_size[child]);
        }
    }
}

void dfs(int node, int parent) {
    res[node] = dp[node];

    for (auto child : adj[node]) {
        if (child != parent) {

            // detach child
            dp[node] -= (dp[child] + subtree_size[child]);
            subtree_size[node] -= subtree_size[child];

            // attach node to child
            dp[child] += (dp[node] + subtree_size[node]);
            subtree_size[child] += subtree_size[node];

            dfs(child, node);

            // restore
            dp[child] -= (dp[node] + subtree_size[node]);
            subtree_size[child] -= subtree_size[node];

            dp[node] += (dp[child] + subtree_size[child]);
            subtree_size[node] += subtree_size[child];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    adj.assign(n + 1, vector<int>());
    subtree_size.assign(n + 1, 1);
    dp.assign(n + 1, 0);
    res.assign(n + 1, 0);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    preCalc(1, -1);
    dfs(1, -1);

    for (int i = 1; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << "\n";

    return 0;
}