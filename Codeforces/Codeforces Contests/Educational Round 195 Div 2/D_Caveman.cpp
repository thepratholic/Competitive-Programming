#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<int> deg(n, 0);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;

        u--;
        v--;

        deg[u]++;
        deg[v]++;
        
    }

    sort(deg.begin(), deg.end());

    if (deg[0] == 0) {
        cout << "Brain Melt\n";
    }

    else if (deg[n - 1] == n - 1 and deg[n - 2] == 1) {
        cout << 2 << "\n";
    }

    else {
        cout << "Many\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}