#include <bits/stdc++.h>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        if(n % 2 == 0) {
            cout << -1 << endl;
        } 
        
        else {
            vector<int> p(n);
            p[0] = n;  
            p[1] = 2;  
            p[2] = 1;   
            for (int i = 4; i <= n; i++){
                p[i-1] = i - 1;
            }
            for (int x : p) cout << x << " ";
            cout << endl;
        }
    }
    
    return 0;
}
