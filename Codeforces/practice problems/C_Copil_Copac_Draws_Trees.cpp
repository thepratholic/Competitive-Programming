// Choose cpp when the time
// limit will for sure give tle in pypy
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF LLONG_MAX
#define fastio ios::sync_with_stdio(false); cin.tie(0);
#define print(arr) for (auto it : arr){cout<<it<<" ";}cout<<endl;
#define len(arr) arr.size()
#define printf(x) cout << x << endl;
#define printm(map) cout<<"{";for(auto it: map){cout<<it.first<<":"<<it.second<<",";};cout<<"}"<<endl; 

// const int MOD = 998244353;
const int MOD = 1e9 + 7;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

// String hashing: sh/shclass, Number: numtheory, SparseTable: SparseTable
// Segment Tree(lazy propogation): SegmentTree, Merge Sort Tree: sorttree
// binary indexed tree: BIT, Segment Tree(point updates): SegmentPoint, Convex Hull: hull, Trie/Treap: Tries
// Combinatorics: pnc, Diophantine Equations: dpheq, Graphs: graphs, DSU: DSU, Geometry: Geometry, FFT: fft
// Persistent Segment Tree: perseg, FreqGraphs: bgraph
// Template : https://github.com/thepratholic/CP-Template-Py-Cpp

void solve() {
    int n;
    cin >> n;

    vector<vector<pair<int,int>>> adj(n + 1);
    vector<int> dp(n + 1, 0);
    vector<int> id(n + 1, 0);

    for (int i = 1; i <= n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(make_pair(v, i));
        adj[v].push_back(make_pair(u, i));
    }

    dp[1] = 1;
    id[1] = 0;

    stack<int> st;
    st.push(1);

    while (!st.empty()) {
        int u = st.top();
        st.pop();

        int sz = (int)adj[u].size();
        for (int k = 0; k < sz; k++) {
            int v = adj[u][k].first;
            int e = adj[u][k].second;

            if (dp[v] == 0) { 
                if (e > id[u]) dp[v] = dp[u];
                else dp[v] = dp[u] + 1;

                id[v] = e;
                st.push(v);
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (dp[i] >= ans) ans = dp[i];
    }
    cout << ans << endl;
    

} 

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}