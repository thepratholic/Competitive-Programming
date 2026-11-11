#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        for (int i = 0; i < N; ++i) {
            vector<int> row(M);
            for (int j = 0; j < M; ++j) {
                cin >> row[j];
            }

            for (int j = M - 1; j >= 0; --j) {
                cout << row[j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
