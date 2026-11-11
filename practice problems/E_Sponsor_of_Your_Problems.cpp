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
    string l, r;
        cin >> l >> r;
        if (l == r) {
            cout << 2 * l.size() << endl;
            return;
        }
        int ptr = 0;
        while (ptr < l.size() && l[ptr] == r[ptr]) ptr++;
        if (l[ptr] + 1 < r[ptr]) {
            cout << 2 * ptr << endl;
        } else {
            int res = 2 * ptr + 1;
            for (int i = ptr + 1; i < l.size(); i++) {
                if (l[i] == '9' && r[i] == '0') res++;
                else break;
            }
            cout << res << endl;
        }
}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}