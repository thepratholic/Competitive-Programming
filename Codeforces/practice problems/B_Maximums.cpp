#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<long long> b(n), a(n);
    for (int i = 0; i < n; i++){
        cin >> b[i];
    }
    
    long long current_max = 0;
    for (int i = 0; i < n; i++){
        a[i] = b[i] + current_max;
        current_max = max(current_max, a[i]);
    }
    
    for (int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << "\n";
    return 0;
}
