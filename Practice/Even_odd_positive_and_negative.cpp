#include<iostream>
using namespace std;
 
int main(){
    int t;
    cin >> t;
    int pos = 0, neg = 0, odd = 0, even = 0;
    for(int i = 0;i < t;i++){
        int num;
        cin >> num;
        if(num > 0) pos++;
        if(num < 0) neg++;
        if(num%2 == 0) even++;
        if(num%2 == 1 || num%2 == -1) odd++;
    }
 
    cout << "Even: " << even << endl;
    cout << "Odd: " << odd << endl;
    cout << "Positive: " << pos << endl;
    cout << "Negative: " << neg << endl;
    return 0;
}