#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    int a[3][5005];
    for(int i = 1;i <= 2;i++) {
        for(int j = 1;j <= n;j++) {
            cin >> a[i][j];
        }
    }

    int sum = 0, maxn = INT_MIN;
    for(int i = 1; i <= n;i++) {
        sum += max(a[1][i], a[2][i]);
        maxn = max(maxn, min(a[1][i], a[2][i]));
    }

    cout << sum + maxn << endl;
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }

    return 0;
}