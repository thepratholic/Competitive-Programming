#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> p(n, 0);
    for (int i = 1; i < n; i++) {
        long long q;
        cin >> q;
        p[i] = p[i - 1] + q;
    }

    long long mn = *min_element(p.begin(), p.end());
    long long shift = 1 - mn;

    vector<bool> seen(n + 1, false);
    for (int i = 0; i < n; i++) {
        p[i] += shift;
        if (p[i] < 1 || p[i] > n || seen[p[i]]) {
            cout << -1 << "\n";
            return 0;
        }
        seen[p[i]] = true;
    }

    for (int i = 0; i < n; i++) cout << p[i] << " ";
    cout << "\n";
    return 0;
}