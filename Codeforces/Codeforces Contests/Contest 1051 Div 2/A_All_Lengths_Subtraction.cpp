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

int n;
map<pair<int, vector<int>>, bool> memo;

bool rec(int k, vector<int>& t) {
    if (k == 0) {
        for (int x : t) if (x != 0) return false;
        return true;
    }

    pair<int, vector<int>> st = {k, t};
    if (memo.count(st)) return memo[st];
    
    for (int s = 0; s <= n - k; ++s) {
        bool ok = true;
        for (int i = 0; i < k; ++i) {
            if (t[s + i] < 1) {
                ok = false;
                break;
            }
        }

        if (ok) {
            vector<int> nt = t;
            for (int i = 0; i < k; ++i) nt[s + i]--;
            if (rec(k - 1, nt)) return memo[st] = true;
        }
    }

    return memo[st] = false;
}

void solve() {
    cin >> n;
    vector<int> p(n);
    for (int &x : p) cin >> x;

    vector<int> t(n);
    for(int i = 0; i < n; ++i) t[i] = p[i] - 1;
    
    memo.clear();
    
    if (rec(n - 1, t)) {
        printf("YES");
    } else {
        printf("NO");
    }
}

int32_t main() {
    fastio
    int t; cin >> t;      
    while (t--) solve();
    return 0;
}