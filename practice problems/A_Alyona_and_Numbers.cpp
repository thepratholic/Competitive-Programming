#include<bits/stdc++.h>
using namespace std;

void solve() {
    long long n, m;

    cin >> n >> m;
    long long cnt = 0;

    vector<long long> cntN(5 , 0), cntM(5, 0);

    for(int i = 1;i <= n;i++) {
        cntN[i % 5] ++;
    }

    for(int i = 1;i <= m;i++) {
        cntM[i % 5] ++;
    }

    for(int i = 0;i < 5;i++){
        if(i == 0) {
            cnt += cntN[i] * cntM[i];
        }
        else{
            cnt += cntN[i] * cntM[5 - i];
        }
    }

    cout << cnt << endl;
}

int main() {
    solve();
}