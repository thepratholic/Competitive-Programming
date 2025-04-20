#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef vector<ll> vl;
 
#define FAST_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl;
#define pb push_back
 
int main() {
    FAST_IO;
    
    ll n;
    cin >> n;
    
    if ((n * (n + 1)) % 4 != 0) {
        NO;
        return 0;
    }
    
    YES;
    vl first, second;
    bool toggle = false;
    
    while (n > 0) {
        if (!toggle) {
            first.pb(n--);
            if (n > 0) second.pb(n--);
        } else {
            second.pb(n--);
            if (n > 0) first.pb(n--);
        }
        toggle = !toggle;
    }
    
    cout << first.size() << endl;
    for (ll num : first) cout << num << " ";
    cout << endl;
    
    cout << second.size() << endl;
    for (ll num : second) cout << num << " ";
    cout << endl;
    
    return 0;
}