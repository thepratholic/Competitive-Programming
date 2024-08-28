#include<bits/stdc++.h>
using namespace std;
void solve(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0;i < n;i++){
        cin >> a[i];
    }
    long long int coins = 0;
    long long int surplus = 0;
    for(int i = 0;i < n; i++){
        surplus += a[i];
        if(surplus < 0){
            coins += -surplus;
            surplus = 0;
        }
    }
    cout << coins << endl;
    cout << endl;
}
int main(){
    int t; cin >> t;
    while(t--){
        solve();
    }
}