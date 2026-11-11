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
    int n; cin >> n;
    int x, y;

    vector<pair<int, int>> pts(n);

    for(int i = 0; i < n; i++) {
        cin >> pts[i].first >> pts[i].second;
    }

    vector<pair<int,int>> sx;
    for (int i = 0; i < n; i++) sx.push_back({pts[i].first, i});
    sort(sx.begin(), sx.end());

    vector<pair<int,int>> sy;
    for (int i = 0; i < n; i++) sy.push_back({pts[i].second, i});
    sort(sy.begin(), sy.end());

    vector<int> posx(n), posy(n);
    for (int i = 0; i < n; i++) posx[sx[i].second] = i;
    for (int i = 0; i < n; i++) posy[sy[i].second] = i;

    vector<int> t1, t2, t3, t4;
    for (int i = 0; i < n; i++) {
        if (posx[i] < n/2 && posy[i] < n/2) t1.push_back(i);
        else if (posx[i] >= n/2 && posy[i] < n/2) t2.push_back(i);
        else if (posx[i] >= n/2 && posy[i] >= n/2) t3.push_back(i);
        else t4.push_back(i);
    }

    for (int i = 0; i < (int)t1.size(); i++)
        cout << t1[i]+1 << " " << t3[i]+1 << "\n";
    for (int i = 0; i < (int)t2.size(); i++)
        cout << t2[i]+1 << " " << t4[i]+1 << "\n";


}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}