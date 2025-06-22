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
// Template : https://github.com/OmAmar106/Template-for-Competetive-Programming

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> a(n, vector<int> (m));

    int mx = 0, cnt_mx = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> a[i][j];

            if(a[i][j] > mx) {
                mx = a[i][j];
                cnt_mx = 1;
            }

            else if(a[i][j] == mx) cnt_mx ++;
        }
    }

    vector<int> r(n), c(m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {

            if(a[i][j] == mx) {
                r[i] ++;
                c[j]++;
            }

        }
    }

    int f = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(r[i] + c[j] - (a[i][j] == mx) == cnt_mx) f = 1;
        }
    }

    cout << mx - f << endl;   

}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}