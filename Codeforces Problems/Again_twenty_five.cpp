#include <bits/stdc++.h>
using namespace std;
 
void solve(int num){
    long long int square = 5;
    for(int i = 0;i < num; i++){
        square = square * 5;
    }
    long long int last_digit = square % 10;
    square = square / 10;
    long long int second_last = square % 10;
    square /= 10;
    cout << second_last << last_digit<< endl;
}
 
int main() {
    solve(2);
    return 0;
}