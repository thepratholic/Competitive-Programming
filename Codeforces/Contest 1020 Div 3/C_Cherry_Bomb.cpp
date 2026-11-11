#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; 
    cin >> t;
    while(t--){
        int n; ll k;
        cin >> n >> k;
        vector<ll> a(n), b(n);
        for(int i = 0; i < n; i++) 
            cin >> a[i];
        for(int i = 0; i < n; i++) 
            cin >> b[i];

        bool hasKnown = false;
        ll x = -1;
        bool ok = true;

        for(int i = 0; i < n; i++){
            if(b[i] != -1){
                ll s = a[i] + b[i];
                if(!hasKnown){
                    hasKnown = true;
                    x = s;
                } else if(s != x){
                    ok = false;
                    break;
                }
            }
        }

        if(!ok){
            cout << 0 << "\n";
            continue;
        }

        if(hasKnown){
            for(int i = 0; i < n; i++){
                if(b[i] == -1){
                    ll bj = x - a[i];
                    if(bj < 0 || bj > k){
                        ok = false;
                        break;
                    }
                }
            }
            cout << (ok ? 1 : 0) << "\n";

        } else {
            ll mn = *min_element(a.begin(), a.end());
            ll mx = *max_element(a.begin(), a.end());
            // x ∈ [mx, k + mn]
            ll lo = mx;
            ll hi = k + mn;
            ll cnt = hi - lo + 1;
            if(cnt < 0) cnt = 0;
            cout << cnt << "\n";
        }
    }

    return 0;
}
