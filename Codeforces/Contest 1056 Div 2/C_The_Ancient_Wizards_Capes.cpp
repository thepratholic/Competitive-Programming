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

bool check(int n, vector<char>&directions, vector<int> &v) {
    vector<int> prefix(n,0), suffix(n,0);
    int l = 0;
    for(int i=1;i<n;i++) {
        prefix[i]=prefix[i-1];
        if(directions[i-1]=='L')prefix[i]+=1;
    }
    
    for(int i=n-2;i>=0;i--) {
        suffix[i]=suffix[i+1];
        if(directions[i+1]=='R')suffix[i]+=1;
    }
    
    for(int i=0;i<n;i++) {
        if((prefix[i]+suffix[i]+1) != v[i]) {
            return false;
        }
    }
    
    return true;
}

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    if (n == 1) {
        cout << 2 << "\n";
        return;
    }


    vector<string> pos(n - 1);

    for(int i = 0; i < n - 1; i++) {
        if(a[i] == a[i + 1]) {
            pos[i] = "OPPOSITE";
        }

        else if(a[i] - a[i + 1] == -1) {
            pos[i] = "LEFT";
        }

        else if(a[i] - a[i + 1] == 1) {
            pos[i] = "RIGHT";
        }

        else {
            cout << 0 << "\n";
            return;
        }
    }


    vector<char>directions(n);
    
    int i = 0;
    while((i<(n-1))&&(pos[i]=="OPPOSITE")) {
        i+=1;
    }
    
    if(i==n-1) {
        int ans = 0;
        directions[0]='L';
        for(int j=1;j<n;j++) {
            directions[j]=(directions[j-1]=='L')?'R':'L';
        }
        if(check(n,directions,a)==true) {
            ans+=1;
        }
        directions[0]='R';
        for(int j=1;j<n;j++) {
            directions[j]=(directions[j-1]=='L')?'R':'L';
        }
        if(check(n,directions,a)==true) {
            ans+=1;
        }
        cout<<ans<<"\n";
        return;
    }
    
    char ch=(pos[i]=="RIGHT")?'R':'L';
    directions[i]=ch;
    directions[i+1]=ch;
    
    for(int j=i-1;j>=0;j--) {
        directions[j]=(directions[j+1]=='L')?'R':'L';
    }
    
    for(int j=i+1;j<n-1;j++) {
        if(pos[j]=="OPPOSITE") {
            ch=(ch=='L')?'R':'L';
            directions[j+1]=ch;
        }
        else {
            if(ch=='L' && pos[j]=="RIGHT") {
                cout<<"0\n";
                return;
            }
            if(ch=='R' && pos[j]=="LEFT") {
                cout<<"0\n";
                return;
            }
            directions[j+1]=ch;
        }
    }
    
    if(check(n,directions,a)==false) {
        cout<<"0\n";
        return;
    }
    
    
    // cout<<position<<"\n";
    // cout<<directions<<"\n";
    cout<<"1\n";



}

int32_t main() {
    fastio
    int t; cin >> t;
    while (t--) solve();
    return 0;
}