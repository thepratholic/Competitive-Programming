#include<bits/stdc++.h>
using namespace std;

#define int long long
#define nline "\n"

int get_sum(int x) {
    int s = 0;
    while (x) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    set<int> ids;

    for(int i = 0; i < n; i++) {
        cin >> a[i];
        ids.insert(i);
    }

    while(q--) {
        int type;
        cin >> type;

        if (type == 1) {
            int l, r;
            cin >> l >> r;
            --l;
            --r;

            auto it = ids.lower_bound(l);

            while(it != ids.end() && *it <= r) {
                int k = *it;

                a[k] = get_sum(a[k]);
                if(a[k] < 10) {
                    it = ids.erase(it);
                }

                else {
                    ++it;
                }

            }
        }

        else { 
            int x;
            cin >> x;

            cout << a[x - 1] << nline;
        }
    }
     
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--)
        solve();

    return 0;
}