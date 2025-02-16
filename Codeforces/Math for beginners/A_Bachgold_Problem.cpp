#include<bits/stdc++.h>
using namespace std;
#define ll long long

void solve() {
    int n;
    cin >> n;

    if(n % 2) {
        ll cnt = 1;
        n -= 3;
        cnt += n/2;
        cout << cnt << endl;
        cout << 3 << " ";
        for(int i = 0;i < n/2;i++) {
            cout << 2 << " ";
        }
        cout << endl;
    }

    else{
        cout << n/2 << endl;
        for(int i = 0;i < n/2;i++) {
            cout << 2 << " ";
        }
        cout << endl;
    }
}

int main() {
    solve();
    return 0;
}