#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;
const int NINF = INT_MIN;

int n, q, sz;
vector<int> mn, mx;

void setLeaf(int p, int v) {
    if (v == -1) {
        mn[p] = INF;
        mx[p] = NINF;
    } else {
        mn[p] = mx[p] = v;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    sz = 1;
    while (sz < n) sz <<= 1;
    mn.assign(2 * sz, INF);
    mx.assign(2 * sz, NINF);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        setLeaf(sz + i, x);
    }
    for (int i = sz - 1; i >= 1; i--) {
        mn[i] = min(mn[2 * i], mn[2 * i + 1]);
        mx[i] = max(mx[2 * i], mx[2 * i + 1]);
    }

    while (q--) {
        int t, a, b;
        cin >> t >> a >> b;
        if (t == 1) {
            int p = sz + a - 1;
            setLeaf(p, b);
            for (p >>= 1; p >= 1; p >>= 1) {
                mn[p] = min(mn[2 * p], mn[2 * p + 1]);
                mx[p] = max(mx[2 * p], mx[2 * p + 1]);
            }
        } else {
            int lo = INF, hi = NINF;
            int l = a - 1 + sz, r = b + sz;  // [l, r)
            while (l < r) {
                if (l & 1) {
                    lo = min(lo, mn[l]);
                    hi = max(hi, mx[l]);
                    l++;
                }
                if (r & 1) {
                    --r;
                    lo = min(lo, mn[r]);
                    hi = max(hi, mx[r]);
                }
                l >>= 1;
                r >>= 1;
            }
            cout << ((lo == INF || lo == hi) ? "Yes" : "No") << "\n";
        }
    }
    return 0;
}