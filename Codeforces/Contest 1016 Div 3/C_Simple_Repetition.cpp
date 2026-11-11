#include <bits/stdc++.h>
using namespace std;
bool is(long long n){
    if(n < 2) return false;
    if(n % 2 == 0) return n == 2;
    for(long long i = 3; i * i <= n; i += 2)
        if(n % i == 0) return false;
    return true;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--){
        long long x;
        int k;
        cin >> x >> k;
        if(k == 1){
            cout << (is(x) ? "YES" : "NO") << "\n";
        } else {
            if(x == 1 && k == 2)
                cout << "YES" << "\n";
            else
                cout << "NO" << "\n";
        }
    }
    return 0;
}
