#include <iostream>
#include <vector>
using namespace std;

bool is_unimodal(vector<int>& arr, int n) {
    int i = 0;

    // Step 1: Strictly increasing part
    while (i < n - 1 && arr[i] < arr[i + 1]) {
        i++;
    }

    // Step 2: Constant part
    while (i < n - 1 && arr[i] == arr[i + 1]) {
        i++;
    }

    // Step 3: Strictly decreasing part
    while (i < n - 1 && arr[i] > arr[i + 1]) {
        i++;
    }

    // If we have traversed the whole array, it is unimodal
    return (i == n - 1);
}

int main() {
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    if (is_unimodal(arr, n)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
