#include <iostream>
#include <set>
using namespace std;
 
bool hasDistinctDigits(int year) {
    string strYear = to_string(year);
    set<char> digits(strYear.begin(), strYear.end());
    return digits.size() == strYear.length();
}
 
int main() {
    int y;
    cin >> y;
    while (true) {
        y++;
        if (hasDistinctDigits(y)) {
            cout << y << endl;
            break;
        }
    }
    return 0;
}