#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> v(n);
    for(int i = 0; i < n;i++) {
        cin >> v[i];
    }

    if( n % 2 == 0) {
        cout << 2 << endl;
        cout << 1 << " " << n << endl;
        cout << 1 << " " << n << endl;
    }

    else{
        cout << 4 << endl;
        cout << 1 << " " << n << endl;
        cout << 2 << " " << n << endl;
        cout << 1 << " " << 2 << endl;
        cout << 1 << " " << 2 << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
    return 0;
}