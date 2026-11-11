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
    int n, k; cin >> n >> k;

    if (k == (n * n) - 1) {
        cout << "NO" << endl;
        return;
    }

    // if all cells , we can escape from...
    vector<vector<int>> v(n, vector<int> (n, 0));
    if(k == n * n) {
        cout << "YES" << endl;

        for(int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << 'U';
            }

            cout << "\n";
        }
        return;
    }

    v[0][0] = 'R';
    v[0][1] = 'L';

    for(int i = 2; i < n * n - k; i++) {
        int r = i / n, c = i % n;

        if(!r) {
            v[r][c] = 'L';
        }

        else {
            v[r][c] = 'U';
        }
    }


    for(int i = n * n - k; i < n * n; i++) {
        int r = i / n, c = i % n;

        v[r][c] = 'D';
    }


    cout << "YES" << "\n";
    for(int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (char)v[i][j];
        }
        cout << "\n";
    }

}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}