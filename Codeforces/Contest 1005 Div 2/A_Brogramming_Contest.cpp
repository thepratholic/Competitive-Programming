#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tc;
    cin >> tc;
    while (tc--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        bool a0 = true, a1 = true;
        for (auto c : s) {
            if (c == '0') a1 = false;
            if (c == '1') a0 = false;
        }
        if (a0) {
            cout << 0 << "\n";
            continue;
        }
        if (a1) {
            cout << 1 << "\n";
            continue;
        }
        int tcount = 0;
        for (int i = 0; i < n - 1; i++) {
            if (s[i] != s[i + 1]) tcount++;
        }
        cout << tcount + (s[0] == '1') << "\n";
    }

    return 0;
}