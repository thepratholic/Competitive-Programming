// Choose cpp when the time
// limit will for sure give tle in pypy
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF LLONG_MAX
#define fastio                   \
    ios::sync_with_stdio(false); \
    cin.tie(0);
#define print(arr)         \
    for (auto it : arr)    \
    {                      \
        cout << it << " "; \
    }                      \
    cout << endl;
#define len(arr) arr.size()
#define printf(x) cout << x << endl;
#define printm(map)                                  \
    cout << "{";                                     \
    for (auto it : map)                              \
    {                                                \
        cout << it.first << ":" << it.second << ","; \
    };                                               \
    cout << "}" << endl;

// const int MOD = 998244353;
const int MOD = 1e9 + 7;

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int lcm(int a, int b)
{
    return a / gcd(a, b) * b;
}

// String hashing: sh/shclass, Number: numtheory, SparseTable: SparseTable
// Segment Tree(lazy propogation): SegmentTree, Merge Sort Tree: sorttree
// binary indexed tree: BIT, Segment Tree(point updates): SegmentPoint, Convex Hull: hull, Trie/Treap: Tries
// Combinatorics: pnc, Diophantine Equations: dpheq, Graphs: graphs, DSU: DSU, Geometry: Geometry, FFT: fft
// Persistent Segment Tree: perseg, FreqGraphs: bgraph
// Template : https://github.com/thepratholic/CP-Template-Py-Cpp

void solve()
{
    int m, n;

    cin >> m >> n;
    int answer[m][n];
    int input[m][n];
    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> input[i][j];
            answer[i][j] = 0;
        }
    }
    bool check = false;
    int zero = 0;

    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; j++)
        {
            bool r = false, c = false;
            if (input[i][j] == 1)
            {
                check = true;
                answer[i][j] = 1;

                for (int k = 0; k < m; ++k)
                {
                    if (input[k][j] == 0)
                    {
                        r = true;
                    }
                    answer[i][j] &= input[k][j];
                }
                for (int l = 0; l < n; ++l)
                {
                    if (input[i][l] == 0)
                    {
                        c = true;
                    }
                    answer[i][j] &= input[i][l];
                }
            }
            if (c && r)
            {
                cout << "NO\n";
                return;
            }
            if (answer[i][j] == 0)
                zero++;
        }
    }

    if (zero == m * n && check)
    {
        cout << "NO\n";
        return;
    }
    cout << "YES\n";
    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; j++)
        {
            cout << answer[i][j] << " ";
        }
        cout << "\n";
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tt = 1;
    // cin>>tt;
    while (tt--)
    {
        solve();
    }
}