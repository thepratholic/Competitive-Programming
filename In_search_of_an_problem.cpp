#include<iostream>
using namespace std;
 
int main(){
    int n; cin >> n;
    bool ishard = false;
    for(int i = 0;i< n;i++){
        int in; cin >> in;
        if(in == 0){
            ishard = true;
            continue;
        }
        else if(in == 1){
            ishard = false;
            break;
        }
    }
    if(ishard == true) cout << "EASY" << endl;
    else cout << "HARD" << endl;
    return 0;
}