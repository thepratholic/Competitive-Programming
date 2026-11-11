#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<long long> a(n);
        for(auto &x : a) cin >> x;

        bool sorted = true;
        for (int i = 0; i+1 < n; i++) 
            if (a[i] > a[i+1]) sorted = false;
        if (sorted) {
            cout << 0 << "\n";
            continue;
        }

        int maxIdx = max_element(a.begin(), a.end()) - a.begin();
        int minIdx = min_element(a.begin(), a.end()) - a.begin();

        vector<pair<int,int>> ops;

        if (a[maxIdx] >= abs(a[minIdx])) {
            while (a[maxIdx] < 20) {
                a[maxIdx] += a[maxIdx];
                ops.push_back({maxIdx+1, maxIdx+1});
            }
            for (int i = 0; i < n; i++) {
                if (a[i] < 0) {
                    a[i] += a[maxIdx];
                    ops.push_back({i+1, maxIdx+1});
                }
            }
            for (int i = 0; i+1 < n; i++) {
                a[i+1] += a[i];
                ops.push_back({i+2, i+1});
            }
        } else {
            while (a[minIdx] > -20) {
                a[minIdx] += a[minIdx];
                ops.push_back({minIdx+1, minIdx+1});
            }
            for (int i = 0; i < n; i++) {
                if (a[i] > 0) {
                    a[i] += a[minIdx];
                    ops.push_back({i+1, minIdx+1});
                }
            }
            for (int i = n-1; i >= 1; i--) {
                a[i-1] += a[i];
                ops.push_back({i, i+1});
            }
        }

        cout << ops.size() << "\n";
        for (auto &p : ops)
            cout << p.first << " " << p.second << "\n";
    }
}
