#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    string s;
    cin >> s;

    int n = s.size();
    map<char, int> freq;

    for (char c : s) {
        freq[c]++;
    }

    if (n % 2 == 1) {
        int odd = 0;
        char oddChar;
        for (auto it : freq) {
            if (it.second % 2 == 1) {
                odd++;
                oddChar = it.first;
            }
        }

        if (odd > 1) {
            cout << "NO SOLUTION\n";
            return;
        }

        string half = "";
        for (auto it : freq) {
            half += string(it.second / 2, it.first);
        }

        string palindrome = half + oddChar + string(half.rbegin(), half.rend());
        cout << palindrome << "\n";
    }

    else {
        for (auto it : freq) {
            if (it.second % 2 == 1) {
                cout << "NO SOLUTION\n";
                return;
            }
        }

        string half = "";
        for (auto it : freq) {
            half += string(it.second / 2, it.first);
        }

        string palindrome = half + string(half.rbegin(), half.rend());
        cout << palindrome << "\n";
    }
}
// TC : O(n)
// SC : O(n)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}