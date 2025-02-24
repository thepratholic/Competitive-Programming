#include<bits/stdc++.h>
using namespace std;

void solve() {
    long long n;
    cin >> n;

    if(n % 2 == 1 || n == 2) {
        cout << -1 << endl;
    }

    else {
        n /= 2;
        cout << ((n+3-1)/3) << " " << n/2 << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}