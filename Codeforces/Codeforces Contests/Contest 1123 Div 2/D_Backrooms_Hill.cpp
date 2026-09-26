#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> parity(n + 1);
    
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (i % 2 == 0) {
            parity[a[i]] = 1; 
        } else {
            parity[a[i]] = 0; 
        }
    }
    
    int o = 0, e = 0;
    bool poss = true;
    
    for (int x = n; x >= 1; --x) {
        if (parity[x] == 1) {
            o++;
        } else {
            e++;
        }
        
        if (abs(o - e) > 1) {
            poss = false;
            break;
        }
    }
    
    if (poss) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}