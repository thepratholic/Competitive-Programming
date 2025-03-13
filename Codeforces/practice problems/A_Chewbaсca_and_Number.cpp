#include <bits/stdc++.h>

using namespace std;

#define ll long long

void solve() {
    ll n;
    cin >> n;

    string ans;
    string num = to_string(n);

    for (int i = 0; i < num.size(); i++) {
        int digit = num[i] - '0';
        int inverted = 9 - digit;

        if (i == 0 && digit == 9) continue;
        if (inverted < digit) num[i] = '0' + inverted;
    }

    cout << num << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
