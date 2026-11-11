#include <bits/stdc++.h>
using namespace std;

#define int long long
#define all(x) x.begin(), x.end()
#define pb push_back
#define endl '\n'
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

bool isq(int n) {
    return ceil(sqrtl(n)) == floor(sqrtl(n));
}

void solve() {
    int n;
    cin >> n;

    if (isq(n * (n + 1) / 2)) {
        cout << -1 << endl;
        return;
    }

    vector<int> arr;
    vector<int> brr(n);

    for (int i = 0; i < n; i++) {
        brr[i] = i + 1;
    }

    int ptr = 0, sum = 0;

    for (int i = 0; i < n; i++) {
        if (ptr + 1 < n && isq(sum + brr[ptr])) {
            arr.push_back(brr[ptr + 1]);
            brr[ptr + 1] = brr[ptr];
            ptr++;
        } else {
            arr.push_back(brr[ptr]);
            ptr++;
        }
        sum += arr.back();
    }

    for (auto ele : arr) {
        cout << ele << " ";
    }
    cout << endl;
}

signed main() {
    fast_io;
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
