#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> v(n);
    vector<int> freq(n+1, 0);
    for(int i = 0; i < n;i++) {
        cin >> v[i];
        freq[v[i]] ++;
    }

    vector<int> b;
    vector<int> visited(n+1, 0);

    for(int i = 0; i < n;i++) {
        if(freq[v[i]] > 0) {
            b.push_back(v[i]);
            freq[v[i]] = 0;
            visited[v[i]] = 1;
        }
    }


    for(int i = 1; i <= n; i++) {
        if(b.size() == n) break;
        if(!visited[i]) {
            b.push_back(i);
        }
    }

    for(int i = 0; i < b.size();i++) {
        cout << b[i] << " ";
    }

    cout << endl;
}


int main() {
    int t;
    cin >> t;
    while(t--) {
        solve();
    }

    return 0;
}