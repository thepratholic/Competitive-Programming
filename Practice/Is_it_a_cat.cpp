#include <iostream>
#include <string>
#include <set>
 
using namespace std;
 
bool isCatMeowing(const string& s) {
    string lower_s;
    for (char c : s) {
        lower_s += tolower(c);
    }
 
    set<char> unique_chars(lower_s.begin(), lower_s.end());
 
    if (unique_chars.size() == 4 && unique_chars.count('m') && unique_chars.count('e') 
        && unique_chars.count('o') && unique_chars.count('w')) {
 
        string target = "meow";
        int j = 0;  
 
        for (int i = 0; i < lower_s.size(); ++i) {
            if (lower_s[i] == target[j]) {
                continue;
            } else if (j < 3 && lower_s[i] == target[j + 1]) {
                j++;
            } else {
                return false;
            }
        }
 
        return j == 3;  
    }
 
    return false;  
}
 
int main() {
    int t;
    cin >> t;
 
    while (t--) {
        int n;
        string s;
        cin >> n >> s;
 
        if (isCatMeowing(s)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
 
    return 0;
}