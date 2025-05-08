#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    string s;
    cin >> s;

    while (q--) {
        string cmd;
        cin >> cmd;

        if (cmd == "pop_back") {
            s.pop_back();
        } 
        else if (cmd == "front") {
            cout << s.front() << '\n';
        } 
        else if (cmd == "back") {
            cout << s.back() << '\n';
        } 
        else if (cmd == "push_back") {
            char x;
            cin >> x;
            s.push_back(x);
        } 
        else if (cmd == "print") {
            int pos;
            cin >> pos;
            cout << s[pos - 1] << '\n';
        } 
        else if (cmd == "substr") {
            int l, r;
            cin >> l >> r;
            if (l > r) swap(l, r);
            cout << s.substr(l - 1, r - l + 1) << '\n';
        } 
        else if (cmd == "sort") {
            int l, r;
            cin >> l >> r;
            if (l > r) swap(l, r);
            sort(s.begin() + l - 1, s.begin() + r);
        } 
        else if (cmd == "reverse") {
            int l, r;
            cin >> l >> r;
            if (l > r) swap(l, r);
            reverse(s.begin() + l - 1, s.begin() + r);
        }
    }

    return 0;
}
