#include<iostream>
using namespace std;
 
int main(){
    long long n, m;
    cin >> n >> m;
 
    // n = 13, m = 12
 
    int ld1 = n % 10;
    int ld2 = m % 10;
 
    cout << ld1 + ld2 << endl;
    
    return 0;
}