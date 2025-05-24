#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        int max_keep = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int min_val = min(a[i], a[j]);
                int max_val = max(a[i], a[j]);
                
                if ((min_val + max_val) % 2 == 0) {
                    int cnt = 0;
                    for (int k = 0; k < n; k++) {
                        if (a[k] >= min_val && a[k] <= max_val) {
                            cnt++;
                        }
                    }
                    max_keep = max(max_keep, cnt);
                }
            }
        }
        
        cout << n - max_keep << "\n";
    }
    
    return 0;
}