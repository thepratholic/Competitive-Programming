#include<bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    string t;
    cin >> t;
    int x = 0, y = 0;
    int dir = 0;
    for(char move : t){
        if(move == 'S'){
            if(dir == 0){
                x += 1;
            }
            else if(dir == 1){
                y-=1;
            }
            else if(dir == 2){
                x-=1;
            }
            else if(dir == 3){
                y+=1;
            }
        }
        else if(move == 'R'){
            dir = (dir + 1) % 4;
        }
    }
    cout << x << " " << y << endl;
}