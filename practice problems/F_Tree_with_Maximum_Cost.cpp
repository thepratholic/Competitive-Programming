#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int N = 200005;

vector<int> adj[N];
ll a[N];
ll subtree_sum[N];
ll distv[N];  
ll mx = LLONG_MIN;

void pre_calc(int node, int parent) {
    subtree_sum[node] = a[node];
    distv[node] = 0;

    for (int adjNode : adj[node]) {
        if (adjNode != parent) {
            pre_calc(adjNode, node);

            subtree_sum[node] += subtree_sum[adjNode];
            distv[node] += distv[adjNode] + subtree_sum[adjNode];
        }
    }
}

void reroot(int node, int parent) {
    mx = max(mx, distv[node]);

    for (int adjNode : adj[node]) {
        if (adjNode != parent) {

            // remove adjNode subtree from node
            subtree_sum[node] -= subtree_sum[adjNode];
            distv[node] -= (distv[adjNode] + subtree_sum[adjNode]);

            // add node contribution to adjNode
            subtree_sum[adjNode] += subtree_sum[node];
            distv[adjNode] += (distv[node] + subtree_sum[node]);

            reroot(adjNode, node);

            // revert changes
            subtree_sum[adjNode] -= subtree_sum[node];
            distv[adjNode] -= (distv[node] + subtree_sum[node]);

            subtree_sum[node] += subtree_sum[adjNode];
            distv[node] += (distv[adjNode] + subtree_sum[adjNode]);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    pre_calc(1, -1);
    reroot(1, -1);

    cout << mx << '\n';

    return 0;
}