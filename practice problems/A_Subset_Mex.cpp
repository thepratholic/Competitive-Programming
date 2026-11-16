#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int cnt[101];
    for (int i = 0; i < 101; i++) cnt[i] = 0;

    for (int i = 0; i < n; i++) cnt[a[i]]++;

    int mexa = 0;

    while (cnt[mexa] >= 1) mexa++;

    int mexb = 0;

    while (cnt[mexb] >= 2) mexb++;

    cout << mexa + mexb << "\n";
}
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}