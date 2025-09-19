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
    int n, m; cin >> n >> m;
    vector<int> a(n);
    vector<int> b(m);
    for (int &x : a) cin >> x;
    for (int &x : b) cin >> x;


    // sort(a.begin(), a.end());
    // sort(b.begin(), b.end());

    auto check = [&] (int mid){
        int i = 0, j = 0;
        while(i < n && j < m) {
            if(abs(a[i] - b[j]) <= mid) {
                i++;
            }
            else j++;
        }

        return (i == n);
    };
    
    int l = 0, r = 2e9;
    int ans = -1;

    while(l <= r) {
        int mid = (l + r) / 2;
        if(check(mid)) {
            ans = mid;
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }


    cout << ans << endl;

}

int32_t main() {
    fastio
    int t = 1; 
    // cin >> t;
    while (t--) solve();
    return 0;
}