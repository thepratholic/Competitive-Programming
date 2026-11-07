#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<ll> a(n + 1), p(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        p[i] = p[i - 1] + a[i];
    }

    vector<ll> pmx(n + 1), pmn(n + 1), smx(n + 2), smn(n + 2);
    pmx[0] = pmn[0] = p[0];
    for (int i = 1; i <= n; i++) {
        pmx[i] = max(pmx[i - 1], p[i]);
        pmn[i] = min(pmn[i - 1], p[i]);
    }
    smx[n] = smn[n] = p[n];
    for (int i = n - 1; i >= 0; i--) {
        smx[i] = max(smx[i + 1], p[i]);
        smn[i] = min(smn[i + 1], p[i]);
    }

    ll ans = pmx[n] - pmn[n] + 1;
    for (int i = 1; i <= n; i++) {
        ll mx = max(pmx[i - 1], smx[i] - 2 * a[i]);
        ll mn = min(pmn[i - 1], smn[i] - 2 * a[i]);
        ans = max(ans, mx - mn + 1);
    }
    cout << ans << "\n";
    return 0;
}