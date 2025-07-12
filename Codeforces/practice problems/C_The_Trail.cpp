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
typedef long long ll;
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
    int n, m;
    cin >> n >> m;

    string s;
    cin >> s;

    vector<vector<ll>> a(n, vector<ll>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> a[i][j];

    int x = 0, y = 0;
    for (char c : s) {
        if (c == 'D') {
            ll row_sum = 0;
            for (int i = 0; i < m; i++)
                row_sum += a[x][i];
            a[x][y] = -row_sum;
            x++;
        } else { 
            ll col_sum = 0;
            for (int i = 0; i < n; i++)
                col_sum += a[i][y];
            a[x][y] = -col_sum;
            y++;
        }
    }

    ll last_row_sum = 0;
    for (int i = 0; i < m; i++)
        last_row_sum += a[n - 1][i];
    a[n - 1][m - 1] = -last_row_sum;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cout << a[i][j] << " ";
        cout << "\n";
    }
}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}



