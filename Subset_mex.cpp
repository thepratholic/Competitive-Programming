#include<bits/stdc++.h>
using namespace std;
void solve(){
    int n; cin >> n;
    int arr[n+1];
    int cnt[101];

    for (int i = 0; i < 101; i++) cnt[i] = 0;
    
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        cnt[arr[i]]++;
    }

    int mexa = 0, mexb = 0;
    while(cnt[mexa] >= 2) mexa++;
    while(cnt[mexb] >= 1) mexb++;
    cout << mexa + mexb << endl;
}


int main(){
    int t; cin >> t;
    while(t--){
        solve();
    }
    return 0;
}