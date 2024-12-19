#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    while(n--){
        int x;
        cin >> x;

        int cnt = 0;
        for (int i = 1; i <= sqrt(x); i++){
            if(x % i == 0){
                cnt++;
                if(x/i != i){
                    cnt++;
                }
            }
        }
        
        cout << cnt << endl;
    }
}