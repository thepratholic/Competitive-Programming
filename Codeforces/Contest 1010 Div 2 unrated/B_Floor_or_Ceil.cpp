#include <iostream>
using namespace std;
typedef long long ll;

ll halve_n_times(ll x, ll n) {
    while (n--) {
        if (x == 0) return 0;
        x /= 2;
    }
    return x;
}


ll ceil_halve_n_times(ll x, ll n) {
    while (n--) {
        if (x <= 1) return x;
        x = (x + 1) / 2;  
    }
    return x;
}

int main() {
    ll t, x, n, m;
    cin >> t;  
    while (t--) {
        cin >> x >> n >> m; 
        cout << halve_n_times(ceil_halve_n_times(x, m), n) << " "
             << ceil_halve_n_times(halve_n_times(x, n), m) << endl;
    }
    return 0;
}
