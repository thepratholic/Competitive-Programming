#include <bits/stdc++.h>
using namespace std;
#define int long long

// void solve() {
    
// }
// TC : 
// SC : 

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int n, r;
        cin >> n >> r;

        unordered_map<int, vector<int>> mp;
        bool bad = false;

        for (int q = 0; q < r; q++) {
            int student, subject;
            cin >> student >> subject;

            if (mp.find(subject) == mp.end()) {
                mp[subject].assign(n + 1, 0);
            }

            mp[subject][student]++;

            if (mp[subject][student] >= 2) bad = true;
        }

        cout << "Scenario #" << tc << ": " << (bad ? "impossible" : "possible") << "\n";


    }

    return 0;
}