#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> b(n);
    for(auto &x : b) {
        cin >> x;
    }

    vector<int> a(n);
    a[0] = 1;
    int num = 1;

    for(int i = 1; i < n; i++) {
        int index = i + 1;
        int diff = b[i] - b[i - 1];
        if(diff == index) {
            a[i] = ++num;
        }

        else {
            a[i] = a[i - diff];
        }
    }


    for(auto &x : a) cout << x << " ";
    cout << "\n";

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