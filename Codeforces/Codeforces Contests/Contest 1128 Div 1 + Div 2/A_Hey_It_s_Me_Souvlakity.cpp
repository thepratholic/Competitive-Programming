#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    int k = count(s.begin(), s.end(), '1');

    if (k == 1) {
        cout << 0 << "\n";
    }

    else if (k == 2) {
        cout << 1 << '\n';
    } 
    else {
        cout << s.rfind('1') - s.find('1') << '\n';
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