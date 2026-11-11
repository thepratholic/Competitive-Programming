#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long maxCoins(vector<int>& a) {
    int n = a.size();
    vector<long long> prefixSum(n + 1, 0);
    vector<long long> suffixSum(n + 1, 0);


    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + max(0, a[i]);
    }


    for (int i = n - 1; i >= 0; i--) {
        suffixSum[i] = suffixSum[i + 1] + max(0, -a[i]);
    }


    long long maxSum = 0;
    for (int i = 0; i <= n; i++) {
        maxSum = max(maxSum, prefixSum[i] + suffixSum[i]);
    }

    return maxSum;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        cout << maxCoins(a) << endl;
    }

    return 0;
}