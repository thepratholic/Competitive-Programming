#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; 
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int &x : a) cin >> x;

        bool liar = false;

        if (n == 2) {
            if (a[0] + a[1] != 1)
                liar = true;
        } else {
            bool any_zero = false;
            for (int x : a) if (x == 0) { any_zero = true; break; }
            if (!any_zero) {
                liar = true;
            }
            if (!liar) {
                for (int i = 0; i + 1 < n; i++) {
                    if (a[i] == 0 && a[i+1] == 0) {
                        liar = true;
                        break;
                    }
                }
            }
        }

        cout << (liar ? "YES\n" : "NO\n");
    }
    return 0;
}
