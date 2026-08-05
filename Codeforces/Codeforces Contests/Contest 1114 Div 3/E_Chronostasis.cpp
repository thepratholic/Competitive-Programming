// Converted in C++, my py sol was ggiving TLE


#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    multiset<long long> st;
    long long sum = 0;

    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        sum += x;
        st.insert(x);
    }

    if (sum < 1) {
        cout << -1 << '\n';
        return;
    }

    vector<long long> ans;
    long long pref = 0;

    while (!st.empty()) {
        if (st.size() == 1) {
            pref += *st.begin();
            ans.push_back(pref);
            break;
        }

        long long mx = *st.rbegin();
        long long need = max(1LL - pref, 1LL - pref - mx);

        auto it = st.lower_bound(need);
        pref += *it;
        ans.push_back(pref);
        st.erase(it);
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] << " \n"[i == n - 1];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}