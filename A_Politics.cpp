#include<bits/stdc++.h>
using namespace std;

void solve(){
    long long int n, k;
    cin >> n >> k;
    string arr[k];
    for(int i = 0;i < k;i++){
        cin >> arr[i];
    }
    long long int Y = 0, N = 0;
    long int no_of_members = n;

    for(int i = 0; i < k; i++){
        for(int j = 0; j < i;j++){
            if(arr[i] == "+"){
                Y++;
            }
            else{
                N++;
            }
        }
    }

}

int main(){
    int t; cin >> t;
    while(t--){
        solve();
    }
}