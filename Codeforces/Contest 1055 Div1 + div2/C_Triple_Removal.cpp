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
    int n, q; cin >> n >> q;

    if (n == 0) {
        cout << -1 << endl;
        return;
    }
    
    vector<int> ones(n + 1, 0);
    vector<int> v(n + 1, -1), bad(n + 1, 0), prefix(n + 1, -1);
    for(int i = 1; i <= n; i++) {
        cin >> v[i];

        if(v[i] == 1) {
            ones[i] = 1;
        }

        if (v[i] == v[i - 1]) {
            bad[i] = 1;
        }

        ones[i] += ones[i - 1];
        prefix[i] = bad[i] + prefix[i - 1];

    }



    while(q--) {
        int l, r;
        cin >> l >> r;

        int one = ones[r] - ones[l - 1];
        int zeros = (r - l + 1) - one;


        if(one % 3 != 0 || zeros % 3 != 0) {
            cout << -1 << endl;
            continue;
        }


        if (prefix[l] == prefix[r]) {
            cout << ((r - l + 1) / 3) + 1 << endl;
        }

        else {
            cout << (r - l + 1) / 3 << endl;
        }

    }

}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}