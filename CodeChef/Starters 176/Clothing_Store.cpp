#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        int X, Y, Z, A, B, C;
        cin >> X >> Y >> Z >> A >> B >> C;

        int happy = 0;

        int useS = min(X, A);
        happy += useS;
        A -= useS;
        X -= useS;

        int useL = min(Y, B);
        happy += useL;
        B -= useL;
        Y -= useL;

        int useXL = min(Z, C);
        happy += useXL;
        C -= useXL;
        Z -= useXL;

        int convertXLtoL = min(Z, B);
        happy += convertXLtoL;
        B -= convertXLtoL;
        Z -= convertXLtoL;

        int convertXLtoS = min(Z, A);
        happy += convertXLtoS;
        A -= convertXLtoS;
        Z -= convertXLtoS;

        int convertLtoS = min(Y, A);
        happy += convertLtoS;
        A -= convertLtoS;
        Y -= convertLtoS;

        cout << happy << endl;
    }
    
    return 0;
}
