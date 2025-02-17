#include<bits/stdc++.h>
using namespace std;

bool isPrime(int n) {
    for(int i = 2;i * i <= n;i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void solve() {
    int d;
    cin >> d;

    int x = 1 + d;
    int ans1 = 0, ans2 = 0;

    while(true) {
        if(isPrime(x)) {
            ans1 =x;
            break;
        }
        x ++;
    }
    x += d;
    while(true) {
        if(isPrime(x)) {
            ans2 = x;
            break;
        }
        x ++;
    }
    cout << ans1 * ans2 << endl;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
    return 0;
}