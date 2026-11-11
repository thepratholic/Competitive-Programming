#include<bits/stdc++.h>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void solve() {
    int n;
    cin >> n;
    
    for(int i = 1;i <= 1000;i++){
        if(!isPrime(n * i + 1)){
            cout << i << endl;
            break;
        }
    }
}

int main() {
    solve();
    return 0;
}