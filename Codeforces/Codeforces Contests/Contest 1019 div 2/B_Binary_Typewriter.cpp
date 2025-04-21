#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define f(i, n) for (int i = 0; i < (n); ++i)
#define nline '\n'
#define fastio() ios::sync_with_stdio(false); cin.tie(NULL)

void solve() {
    int n;
    string s;
    cin >> n >> s;

    int flips = 0;
    for (int i = 1; i < n; ++i)
        if (s[i] != s[i-1])
            ++flips;

    int m  = flips + 1;          
    int v1 = (s[0] == '1');       

    int best_improve = 0;
    if (m >= 4 || (v1 == 1 && m >= 3)) {
        best_improve = 2;
    } else if (m >= 3 || (v1 == 1 && m == 2)) {
        best_improve = 1;
    }


    int ans = n + flips + v1 - best_improve;
    cout << ans << nline;
}

int main() {
    fastio();
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
