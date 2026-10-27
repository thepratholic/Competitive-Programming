#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long n, m; cin >> n >> m;                
    if (m < n || m > n * (n + 1) / 2) {           
        cout << -1 << "\n"; return;             
    }                                              
    long long R = m - n;                           
    vector<int> chain;                             
    vector<char> inChain(n + 1, 0);                
    for (long long v = n - 1; v >= 1; v--) {       
        if (R >= v) {                              
            R -= v;                                
            chain.push_back(v + 1);                
            inChain[v + 1] = 1;                    
        }                                          
    }                                              
    chain.push_back(1); inChain[1] = 1;            
    cout << chain[0] << "\n";                      
    for (size_t i = 0; i + 1 < chain.size(); i++)  
        cout << chain[i] << " " << chain[i+1] << "\n"; 
    for (int x = 2; x <= n; x++)                   
        if (!inChain[x]) cout << 1 << " " << x << "\n"; 
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