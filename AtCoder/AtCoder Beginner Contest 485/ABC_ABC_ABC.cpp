#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    string s;
    cin >> n >> s;

    int a = -1;
    {
        int seen = 0;
        for (int i = 0; i < n; i++) {
            seen |= 1 << (s[i] - 'A');
            if (seen == 7) { a = i + 1; break; }
        }
    }
    int b = -1;
    {
        int seen = 0;
        for (int j = n - 1; j >= 0; j--) {
            seen |= 1 << (s[j] - 'A');
            if (seen == 7) { b = j; break; }
        }
    }
    if (a == -1 || b == -1) { puts("0"); return 0; }

    vector<array<int,3>> pre(n + 1, {0,0,0});
    for (int i = 0; i < n; i++) {
        pre[i + 1] = pre[i];
        pre[i + 1][s[i] - 'A']++;
    }
    auto ok = [&](int i, int j) {
        for (int k = 0; k < 3; k++)
            if (pre[j][k] - pre[i][k] == 0) return false;
        return true;
    };

    long long ans = 0;
    int j = 0;
    for (int i = a; i < n; i++) {
        if (j < i + 1) j = i + 1;
        while (j <= n && !ok(i, j)) j++;
        if (j > b) break;
        ans += b - j + 1;
    }
    cout << ans << endl;
    return 0;
}