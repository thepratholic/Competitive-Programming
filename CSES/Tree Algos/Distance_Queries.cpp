// Choose cpp when the time
// limit will for sure give tle in pypy
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

#define int long long
#define INF LLONG_MAX
#define fastio ios::sync_with_stdio(false); cin.tie(0);
#define len(arr) arr.size()
#define f first
#define s second
#define pb push_back
#define all(x) x.begin(), x.end()
#define range(i, n) for (int i = 0; i < (n); ++i)
#define rangea(i, a, b) for (int i = (a); i < (b); ++i)
#define MOD1 998244353
#define MOD 1000000007
using vi = vector<int>;
using vii = vector<vector<int>>;
using pi = pair<int,int>;
#pragma GCC optimize("O3,unroll-loops")

template <typename T>
using ordered_multiset = tree<
    std::pair<T, int>,
    null_type,
    std::less<std::pair<T, int>>,
    rb_tree_tag,
    tree_order_statistics_node_update
>;
template<typename T> istream& operator>>(istream& in, vector<T>& v) {for (auto& x : v) in >> x;return in;}
template<typename T1, typename T2> istream& operator>>(istream& in, pair<T1, T2>& p) {in >> p.first >> p.second;return in;}
template<typename T>
class is_printable {
    template<typename U> static auto test(int) -> decltype(cout << declval<U>(), true_type{});
    template<typename> static auto test(...) -> false_type;
public: static constexpr bool value = decltype(test<T>(0))::value;
};
template<typename T> enable_if_t<is_printable<T>::value> __print(const T& val) { cout << val; }
template<typename T1, typename T2> void __print(const pair<T1, T2>& p) {
    cout << "("; __print(p.first); cout << ":"; __print(p.second); cout << ")";
}
template<typename T> enable_if_t<!is_printable<T>::value> __print(const T& container) {
    cout << "{"; bool first = true;
    for (const auto& x : container) { if (!first) cout << ", "; __print(x); first = false; }
    cout << "}";
}
void print() { cout << "\n"; }
template<typename T, typename... Args>
void print(const T& t, const Args&... rest) {
    __print(t); if constexpr (sizeof...(rest)) cout << " "; print(rest...);
}

int gcd(int a, int b) {if (b == 0) return a;return gcd(b, a % b);}
int lcm(int a, int b) {return a / gcd(a, b) * b;}
int II(){int a;cin>>a;return a;}
string SI(){string s;cin>>s;return s;}
vi LII(int n){vi a(n);cin>>a;return a;}

const int MAXN = 200005;
const int LOG = 20;
int up[200005][20];
vector<int> adj[MAXN];
int depth[MAXN];

vector<pair<int, int>> pairs;

void dfs(int root, int par) {
    stack<pair<int,int>> st;
    st.push({root, par});

    while(!st.empty()) {
        auto [node, parent] = st.top();
        st.pop();

        up[node][0] = parent;

        for(auto &child : adj[node]) {
            if(child != parent) {
                depth[child] = depth[node] + 1;
                st.push({child, node});
            }
        }
    }
}

int kth_anc(int node, int k) {
    for(int bit = LOG - 1; bit >= 0; bit--) {
        if(k & (1 << bit)) {
            if(node == -1) break;
            node = up[node][bit];
        }
    }
    return node;
}

int lca(int u, int v) {
    if(depth[u] < depth[v]) swap(u, v);

    int diff = depth[u] - depth[v];
    u = kth_anc(u, diff);

    if(u == v) return u;

    for(int k = LOG - 1; k >= 0; k--) {
        if(up[u][k] != -1 and up[u][k] != up[v][k]) {
            u = up[u][k];
            v = up[v][k];
        }
    }

    return up[u][0];
}

void solve() {
    int n, q;
    cin >> n >> q;

    pairs.clear(); // FIXED
    memset(up, -1, sizeof(up)); // FIXED

    for (int i = 1; i <= n; i++) {
        adj[i].clear();
        depth[i] = 0;
    }

    for(int i = 1; i <= n - 1; i++) {
        int a, b;
        cin >> a >> b;

        pairs.push_back({a, b});

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(1, -1);

    // pre-process the sparse table
    for(int k = 1; k < 20; k++) {
        for(int node = 1; node <= n; node++) {
            if(up[node][k - 1] != -1) {
                up[node][k] = up[up[node][k - 1]][k - 1];
            }
        }
    }

    while(q--) {
        int a, b;
        cin >> a >> b;

        cout << depth[a] + depth[b] - (2 * depth[lca(a, b)]) << "\n";
    }
}

int32_t main() {
    fastio
    int t=1;
    cin >> t;
    while (t--) solve();
    return 0;
}