#include<bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >> s;
    int n = s.size();
    int idx = -1;

    for (int i = 0; i < n; i++) {
        if (s[i] == '0') {
            idx = i;
            break;
        }
    }

    if (idx == -1) idx = n-1;

    int k = idx - 1;
    for(int j = idx; j < n && k >= 0; j++, k--) {
        if (s[j] == '1') {
            break;
        }
    }

    k ++;

    cout << 1 << " " << n << " " << k + 1 << " " << k + n - idx << endl;

}


int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
    return 0;
}