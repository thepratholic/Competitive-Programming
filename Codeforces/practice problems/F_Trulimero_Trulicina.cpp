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
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> last(m, -1);

        for (int i = 0; i < n; ++i) {
            bool shift = false;
            vector<int> CUR(m);

            for (int j = 0; j < m; ++j) {
                int elm = ((i * m + j) % k) + 1;
                if (elm == last[j]) {
                    shift = true;
                }
                CUR[j] = elm;
            }

            if (shift) {
                vector<int> shifted(m);
                for (int j = 0; j < m; ++j) {
                    shifted[j] = CUR[(j + 1) % m];
                }
                CUR = shifted;
            }

            for (int val : CUR) {
                cout << val << " ";
            }
            cout << endl;

            last = CUR;
        }
}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}