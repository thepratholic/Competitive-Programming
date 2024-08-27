#include<iostream>
#include<string>
#include<algorithm>
#include<cctype>
using namespace std;
 
int main(){
    int tc; cin >> tc;
    while(tc--){
        int n;
        cin >> n;
        int a[n];
        for(int i=0;i<n;i++) cin >> a[i];
 
        int oi = 0, ei = 0, oe = 0, ee = 0, nm = 0;
        for(int i = 0;i < n;i++){
            if(i % 2 == 0)
                ei++;
            else 
                oi++;
 
            if(a[i] % 2 == 0)
                ee++;
            else 
                oe++;
 
            if(i % 2 != a[i] % 2)
                nm++;            
        }
 
        if(ei != ee || oi != oe){
            cout << -1 << endl;
            continue;
        }
        cout << nm / 2 << endl;
    }
    return 0;
}