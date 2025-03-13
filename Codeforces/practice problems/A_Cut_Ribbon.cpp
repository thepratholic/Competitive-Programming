#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b, c;
    cin >> n >> a >> b >> c;
    
    int max_pieces = 0;
    
    for (int i = 0; i <= n / a; ++i) {
        for (int j = 0; j <= n / b; ++j) {
            int remaining = n - (i * a + j * b);
            
            if (remaining >= 0 && remaining % c == 0) {
                int k = remaining / c;  
                max_pieces = max(max_pieces, i + j + k);
            }
        }
    }
    
    cout << max_pieces << endl;
    return 0;
}
