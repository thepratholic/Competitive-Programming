#include <iostream>
using namespace std;

#define ll long long

// Function to calculate squared distance between two points
ll dis(int x1, int y1, int x2, int y2) {
    return 1LL * (x2 - x1) * (x2 - x1) + 1LL * (y2 - y1) * (y2 - y1);
}

int main() {
    int t;
    cin >> t; // Number of test cases

    while (t--) {
        int n;
        cin >> n; // Number of points

        int x[n], y[n];
        for (int i = 0; i < n; ++i) {
            cin >> x[i] >> y[i]; // Input points
        }

        int xs, ys, xt, yt;
        cin >> xs >> ys >> xt >> yt; // Input starting and target points

        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if (dis(xt, yt, x[i], y[i]) <= dis(xt, yt, xs, ys)) {
                ok = false;
                break;
            }
        }

        cout << (ok ? "YES" : "NO") << endl;
    }

    return 0;
}
