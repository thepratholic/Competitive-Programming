#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool canFormTMT(string s) {
    int n = s.size();
    vector<int> leftT, rightT, m;

    // First pass: Check from left to right
    for (int i = 0; i < n; i++) {
        if (s[i] == 'T') leftT.push_back(i);
        else if (s[i] == 'M') m.push_back(i);
    }

    // Check if there are enough T's for the M's
    if (leftT.size() != 2 * m.size()) return false;

    int tIndex = 0;
    // Check for valid TMT formation from left to right
    for (int i = 0; i < m.size(); i++) {
        if (leftT[tIndex] < m[i]) {
            tIndex++;
        } else {
            return false;
        }
    }

    // Second pass: Check from right to left
    tIndex = leftT.size() - 1;
    for (int i = m.size() - 1; i >= 0; i--) {
        if (leftT[tIndex] > m[i]) {
            tIndex--;
        } else {
            return false;
        }
    }

    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        string s;
        cin >> n >> s;

        if (canFormTMT(s)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
