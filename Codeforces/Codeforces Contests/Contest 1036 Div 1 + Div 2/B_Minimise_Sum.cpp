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

int f(vector<int>& a) {
    int sum = 0, mn = LLONG_MAX;
    for (int x : a) {
        mn = min(mn, x);
        sum += mn;
    }
    return sum;
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto& x : a) cin >> x;

    int ans = f(a);

    int max_val = -1, max_idx = -1;
    for (int i = 0; i < n; ++i) {
        if (a[i] > max_val) {
            max_val = a[i];
            max_idx = i;
        }
    }

    for (int i = 0; i < max_idx; ++i) {
        vector<int> temp = a;
        temp[i] += temp[max_idx];
        temp[max_idx] = 0;
        ans = min(ans, f(temp));
    }

    cout << ans << "\n";
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
