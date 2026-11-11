#include <bits/stdc++.h>
using namespace std;

bool check(int a, int b, int c, int d, int e, int f) {
    
    if (b == d && d == f && a + c + e == b) return true;
    
    if (a == c && c == e && b + d + f == a) return true;
    
    if (b == d && a + c == e && b + f == e) return true;
    
    if (a == c && b + d == f && a + e == f) return true;
    
    if (d == f && c + e == a && b + d == a) return true;
    
    if (c == e && d + f == b && a + c == b) return true;
    
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        int l1, b1, l2, b2, l3, b3;
        cin >> l1 >> b1 >> l2 >> b2 >> l3 >> b3;
        
        bool found = false;
        
        vector<vector<int>> perms = {
            {l1, b1, l2, b2, l3, b3},
            {l1, b1, l3, b3, l2, b2},
            {l2, b2, l1, b1, l3, b3},
            {l2, b2, l3, b3, l1, b1},
            {l3, b3, l1, b1, l2, b2},
            {l3, b3, l2, b2, l1, b1}
        };
        
        for (auto& p : perms) {
            if (check(p[0], p[1], p[2], p[3], p[4], p[5])) {
                found = true;
                break;
            }
        }
        
        cout << (found ? "YES" : "NO") << "\n";
    }
    
    return 0;
}