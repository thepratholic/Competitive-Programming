#include <iostream>
#include <vector>
#include <string>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while(t--){
        int n, m, k;
        cin >> n >> m >> k;
        string A;
        cin >> A;
 
        vector<int> logs;
        for (int i = 0; i < n; i++){
            if(A[i] == 'L'){
                logs.push_back(i);
            }
        }
        logs.push_back(n + 1);
 
        int pos = -1;
        int next_log = 0;
        bool possible = true;
 
        while(pos < n - 1){
            if (next_log < (int)logs.size() && (logs[next_log] - pos) <= m) {
                pos = logs[next_log];
            } 
            else {
                pos += m;
                if (pos > n - 1) {
                    break;
                }
                while(pos < n && pos < logs[next_log]){
                    if(A[pos] == 'C' || k <= 0){
                        possible = false;
                        break;
                    }
                    pos++;
                    k--;
                }
                if(!possible)
                    break;
            }
            next_log++;
        }
 
        cout << (possible ? "YES" : "NO") << "\n";
    }
    
    return 0;
}
