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
        
        string result(n, '0');
        
        vector<int> prefix_min(n);
        prefix_min[0] = a[0];
        for (int i = 1; i < n; i++) {
            prefix_min[i] = min(prefix_min[i-1], a[i]);
        }
        
        vector<int> suffix_max(n);
        suffix_max[n-1] = a[n-1];
        for (int i = n-2; i >= 0; i--) {
            suffix_max[i] = max(suffix_max[i+1], a[i]);
        }
        
        for (int i = 0; i < n; i++) {
            bool is_prefix_min = (a[i] == prefix_min[i]);
            
            bool is_suffix_max = (a[i] == suffix_max[i]);
            
            if (is_prefix_min || is_suffix_max) {
                result[i] = '1';
            }
        }
        
        cout << result << "\n";
    }
    
    return 0;
}