#include <bits/stdc++.h>
using namespace std;
 
long long gcd(long long a, long long b) {
    while(b) {
        a %= b;
        swap(a, b);
    }
    return a;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<long long> a(n);
        for(auto &x : a) cin >> x;
        
        long long m = *min_element(a.begin(), a.end());
        int count_m = 0;
        for(auto &x : a) {
            if(x == m) count_m++;
        }
 
        if(count_m >= 2) {
            cout << "Yes\n";
            continue;
        }
 
        long long g = 0;
        bool found = false;
        for(auto &x : a) {
            if(x != m && x % m == 0) {
                if(!found) {
                    g = x;
                    found = true;
                } else {
                    g = gcd(g, x);
                }
            }
        }
 
        if(found && g == m)
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
    }
    
    return 0;
}