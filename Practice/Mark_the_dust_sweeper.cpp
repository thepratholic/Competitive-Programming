#include <iostream>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while(t--){
        int n; cin >> n;
        int a[n];
        for(int i = 0;i < n;i++){
            cin >> a[i];
        }
 
        long long int num_of_ops = 0;
        bool non_zero = false;
        for(int  i = 0;i < n-1;++i){
            if(a[i] > 0){
                num_of_ops += a[i];
                non_zero = true;
            }
            else if(a[i] == 0 && non_zero){
                num_of_ops += 1;
            }
        }
        cout << num_of_ops << endl;
        cout << endl;
    }
    return 0;
}