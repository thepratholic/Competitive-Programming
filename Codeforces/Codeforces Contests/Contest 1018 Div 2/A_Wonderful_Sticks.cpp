#include <bits/stdc++.h>
using namespace std;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int n;
        string s;
        cin >> n >> s;

        vector<int> L;
        vector<char> t;
        for(int i = 0; i < n-1; ){
            char c = s[i];
            int j = i;
            while(j < n-1 && s[j] == c) j++;
            t.push_back(c);
            L.push_back(j - i);
            i = j;
        }
        int m = (int)L.size();
        vector<int> B(m);
        B[0] = L[0] + 1;
        for(int i = 1; i < m; i++){
            B[i] = L[i];
        }

        vector<int> x(m), y(m);
        bool found = false;

        if(t[0] == '<'){
            for(int y0 = B[0]; y0 <= n; y0++){
                int x0 = y0 - (B[0]-1);
                if(x0 < 1) continue;
                x[0] = x0;  y[0] = y0;
                int gmin = x0, gmax = y0;
                bool ok = true;

                for(int i = 1; i < m; i++){
                    if(t[i] == '<'){
                        y[i] = gmin - 1;
                        x[i] = y[i] - (B[i]-1);
                        if(x[i] < 1){ ok = false; break; }
                    } else {
                        x[i] = gmax + 1;
                        y[i] = x[i] + (B[i]-1);
                        if(y[i] > n){ ok = false; break; }
                    }
                    gmin = min(gmin, x[i]);
                    gmax = max(gmax, y[i]);
                }

                if(ok){
                    found = true;
                    break;
                }
            }
        }
        else {
            for(int x0 = 1; x0 + (B[0]-1) <= n; x0++){
                int y0 = x0 + (B[0]-1);
                x[0] = x0;  y[0] = y0;
                int gmin = x0, gmax = y0;
                bool ok = true;

                for(int i = 1; i < m; i++){
                    if(t[i] == '<'){
                        y[i] = gmin - 1;
                        x[i] = y[i] - (B[i]-1);
                        if(x[i] < 1){ ok = false; break; }
                    } else {
                        x[i] = gmax + 1;
                        y[i] = x[i] + (B[i]-1);
                        if(y[i] > n){ ok = false; break; }
                    }
                    gmin = min(gmin, x[i]);
                    gmax = max(gmax, y[i]);
                }

                if(ok){
                    found = true;
                    break;
                }
            }
        }

        vector<int> ans;
        ans.reserve(n);
        for(int i = 0; i < m; i++){
            if(t[i] == '<'){
                for(int d = 0; d < B[i]; d++){
                    ans.push_back(y[i] - d);
                }
            } else {
                for(int d = 0; d < B[i]; d++){
                    ans.push_back(x[i] + d);
                }
            }
        }

        for(int v : ans) cout << v << ' ';
        cout << "\n";
    }
    return 0;
}
