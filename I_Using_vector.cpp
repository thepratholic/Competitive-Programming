#include <bits/stdc++.h>

using namespace std;

#define ll long long

void solve() {
    ll n, q;
    cin >> n >> q;

    vector<ll> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];

    while (q--) {
        string s;
        cin >> s;

        if (s == "pop_back") {
            v.pop_back();
        }

        else if (s == "front") {
            cout << v.front() << '\n';
        }

        else if (s == "back") {
            cout << v.back() << '\n';
        }

        else if (s == "sort") {
            ll l, r;
            cin >> l >> r;
            sort(v.begin() + (l - 1), v.begin() + r);
        }

        else if (s == "reverse") {
            ll l, r;
            cin >> l >> r;
            reverse(v.begin() + (l - 1), v.begin() + r);
        }

        else if (s == "print") {
            ll pos;
            cin >> pos;
            cout << v[pos - 1] << '\n';
        }

        else if (s == "push_back") {
            ll x;
            cin >> x;
            v.push_back(x);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();

    return 0;
}
