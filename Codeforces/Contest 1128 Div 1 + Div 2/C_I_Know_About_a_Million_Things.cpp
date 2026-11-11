#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    int odd = 0;

    for (auto &x : a) {
        cin >> x;
        odd += (x & 1);
    }

    int even = n - odd;

    if ((odd == 1 and even == 1) or (odd == 3 and even == 0)) {
        cout << "Larpity" << "\n";
    }

    else {
        cout << "Moggity" << "\n";
    }

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}