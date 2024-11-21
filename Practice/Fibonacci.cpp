#include<iostream>
using namespace std;
 
int main(){
    long long n; 
    cin >> n;
    long long fib[n];
    fib[0] = 0;
    if(n!=1){
        fib[1] = 1;
    }
    for(int i=2;i<n;i++){
        fib[i] = fib[i-1] + fib[i-2];
    }
    cout << fib[n-1] << endl;
    return 0;
}