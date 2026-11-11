#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50005;

int n, k;
vector<int> adj[MAXN];
long long ans = 0;
int dp[MAXN][505];

void dfs(int u, int parent) {
    dp[u][0] = 1;

    for (int v : adj[u]) {
        if (v == parent) continue;

        dfs(v, u);

        // count pairs
        for (int d = 0; d < k; d++) {
            ans += 1LL * dp[u][k - d - 1] * dp[v][d];
        }

        // merge dp
        for (int d = 0; d < k; d++) {
            dp[u][d + 1] += dp[v][d];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    cout << ans << '\n';
    return 0;
}