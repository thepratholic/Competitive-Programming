#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve() {
    int n;
    cin >> n;

    vector<int> parents(n), childs(n);

    for(int i = 0; i < n; i++) {
        cin >> parents[i] >> childs[i];

        if (parents[i] > 0) {
            --parents[i];
        } 
    }


    vector<bool> good(n, false);

    for(int i = 0; i < n; i++) {
        if((childs[i] == 0) and (parents[i] >= 0)) {
            good[parents[i]] = true;
        }
    }

    vector<int> ans;
    for(int i = 0; i < n; i++) {
        if((childs[i] == 1) and (good[i] == false)) {
            ans.push_back(i + 1);
        }
    }

    if(ans.size() == 0) {
        cout << "-1" << "\n";
    }

    else{
        for(auto &x : ans) {
            cout << x << " ";
        }
        cout << "\n";
        return;
    }

    
}

signed main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 1;
    // cin >> T;

    while (T--)
        solve();

    return 0;
}