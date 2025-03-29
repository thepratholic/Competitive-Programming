#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        string a, b;
        cin >> a >> b;
        
        int cntA1 = 0, zeros1 = 0;
        int cntA2 = 0, zeros2 = 0;
        
        for (int i = 1; i <= n; i++){
            if (i % 2 == 1){ 
                cntA1++;
                if(a[i-1] == '0') zeros1++;
                if(b[i-1] == '0') zeros2++;
            }
            else{ 
                cntA2++;
                if(a[i-1] == '0') zeros2++;
                if(b[i-1] == '0') zeros1++;
            }
        }
        
        if(zeros1 >= cntA1 && zeros2 >= cntA2)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    
    return 0;
}
