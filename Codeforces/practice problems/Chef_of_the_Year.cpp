#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int n, m;
    cin >> n >> m;

    unordered_map<string, string> chef_country;
    map<string, int> country_votes;
    map<string, int> chef_votes;

    for (int i = 0; i < n; i++) {
        string chef, country;
        cin >> chef >> country;
        chef_country[chef] = country;
    }

    for (int i = 0; i < m; i++) {
        string chef;
        cin >> chef;
        string country = chef_country[chef];
        country_votes[country]++;
        chef_votes[chef]++;
    }

    string best_country, best_chef;
    int mx = 0;

    for (auto &[country, votes] : country_votes) {
        if (votes > mx) {
            mx = votes;
            best_country = country;
        }
    }

    mx = 0;
    for (auto &[chef, votes] : chef_votes) {
        if (votes > mx) {
            mx = votes;
            best_chef = chef;
        }
    }

    cout << best_country << "\n" << best_chef << "\n";
}
// TC : O(n + m)
// SC : O(n + m)

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