#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fastio() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

void solve() {
    int n, x;
    cin >> n >> x;
    vector<int> a(n);
    for (int &num : a) cin >> num;

    sort(a.rbegin(), a.rend());

    int count = 0, teams = 0;
    for (int skill : a) {
        count++; 
        if (count * skill >= x) {
            teams++;
            count = 0; 
        }
    }

    cout << teams << '\n';
}

int32_t main() {
    fastio();
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
