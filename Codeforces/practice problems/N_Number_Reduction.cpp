#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve() {

    string s;
    cin >> s;

    int k, n = s.size();;
    cin >> k;


    vector<vector<int>> positions (10);

    for (int i = 0; i < n; ++i) positions[s[i] - '0'].push_back(i);
    for (int i = 0; i < 10; ++i) reverse(positions[i].begin(), positions[i].end());

    string ans = "";

    int first = 0, size = n - k; 
    
    for (int i = 0; i < size; ++i) {

        for (int digit = (i == 0); digit <= 9; ++digit) {
            

            while (positions[digit].empty() == false and positions[digit].back() < first) 
                positions[digit].pop_back();
            
            if ((positions[digit].empty() == false) and (positions[digit].back() - first <= k)) {

                ans.push_back(digit + '0');

                k -= positions[digit].back() - first;

                first = positions[digit].back() + 1;
                break;
            }
        }
    }

    cout << ans << '\n';
    return;
}

signed main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) solve();
    return 0;
}
