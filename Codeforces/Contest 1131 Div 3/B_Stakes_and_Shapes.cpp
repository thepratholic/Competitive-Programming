#include <bits/stdc++.h>
using namespace std;

void solve() {
    int x, y, z;
    cin >> x >> y >> z;
    
    int n = x + y + z;
    char c;
    if (z >= x) c = 'S';
    else if (y >= z) c = 'R';
    else c = 'P';
    cout << string(n, c) << "\n";
}
// TC : 
// SC : 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}