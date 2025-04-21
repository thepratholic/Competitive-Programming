#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    int m = k - 1;

    vector<int> left(n), right(n);
    for (int i = 0; i < n; ++i) {
        cin >> left[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> right[i];
    }

    vector<int> max_side(n);
    vector<int> min_side(n); 
    long long worst_case_sum = 0;

    for (int i = 0; i < n; ++i) {
        max_side[i] = max(left[i], right[i]);
        min_side[i] = min(left[i], right[i]);
        worst_case_sum += max_side[i];
    }

    sort(min_side.begin(), min_side.end(), greater<>());

    for (int i = 0; i < m; ++i) {
        worst_case_sum += min_side[i];
    }

    long long result = worst_case_sum + 1;

    cout << result << '\n';
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
