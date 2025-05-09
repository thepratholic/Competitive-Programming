#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    string S;
    cin >> N >> S;

    deque<char> dq(S.begin(), S.end());
    long long score = 0;

    while (!dq.empty()) {
        char c = dq.front();
        dq.pop_front();

        switch (c) {
            case 'V':
                score += 5;
                break;

            case 'W':
                score += 2;
                break;

            case 'X':
                if (!dq.empty()) {
                    dq.pop_front();
                }
                break;

            case 'Y':
                if (!dq.empty()) {
                    char next = dq.front();
                    dq.pop_front();
                    dq.push_back(next);
                }
                break;

            case 'Z':
                if (!dq.empty()) {
                    char nxt = dq.front();
                    if (nxt == 'V') {
                        score /= 5;
                        dq.pop_front();
                    } else if (nxt == 'W') {
                        score /= 2;
                        dq.pop_front();
                    }
                }
                break;
        }
    }

    cout << score << "\n";
    return 0;
}
