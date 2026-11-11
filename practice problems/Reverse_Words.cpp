// Write your code here
#include <bits/stdc++.h>
using namespace std;

void solve(){

}

int main(){
    string s;
    while(cin>>s){
        int str_size = s.size();
        for(int i = str_size - 1; i>=0; i--){
            cout << s[i];
        }
        cout << " ";
    }

    return 0;
}