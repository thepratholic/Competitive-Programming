#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<string> members(n);
        for (int i = 0; i < n; ++i) {
            cin >> members[i];
        }


        string president = members[0];

        int max_members = 1; 

    
        for (int i = 1; i < n; ++i) {
            bool can_stay = true;
            for (int j = 0; j < k; ++j) {
                if (members[i][j] != president[j]) {
                    can_stay = false;
                    break;
                }
            }
            if (can_stay) {
                max_members++;
            }
        }

        cout << max_members << endl;
    }
    return 0;
}
