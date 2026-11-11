#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    string a;
    cin >> a;
    
    unordered_map<char, int> b;
    for (char i : a) {
        b[i]++;
    }
    
    string ans = "";
    while (n) {
        for (auto& i : b) {
            if (i.second != 0) {
                ans += i.first;
                i.second--;
                n--;
            }
        }
    }
    
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
    return 0;
}
