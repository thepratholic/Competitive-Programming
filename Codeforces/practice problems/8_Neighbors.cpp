#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<string> A(N);
        for (int i = 0; i < N; ++i)
            cin >> A[i];

        int X, Y;
        cin >> X >> Y;
        X--, Y--;

        int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

        bool all_x = true;
        for (int k = 0; k < 8; ++k) {
            int nx = X + dx[k];
            int ny = Y + dy[k];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (A[nx][ny] != 'x') {
                    all_x = false;
                    break;
                }
            }
        }

        cout << (all_x ? "yes" : "no") << endl;
    }

    return 0;
}
