#include<bits/stdc++.h>
using namespace std;

void solve() {
    long long n;
    cin >> n;

    string s;
    cin >> s;

    map<char, int> mpp;

    for(char c: s) {
        mpp[c]++;
    }

    int mi = 1000, ma = 0;
    char mini, maxi;
    for(auto i : mpp) {
        if(i.second < mi) {
            mi = i.second;
            mini = i.first;
        }

        if(i.second >= ma) {
            ma = i.second;
            maxi = i.first;
        }
    }

    for(int i = 0;i < n;i++) {
        if(s[i] == mini) {
            s[i] = maxi;
            break;
        }
    }

    cout << s << endl;
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
    return 0;
}