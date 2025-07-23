// Write your code here
#include<bits/stdc++.h>
using namespace std;
#define int long long
vector<int> queens(8);
vector<vector<char>> v;
bool check(int row,int column){
    if(v[row][column]=='*'){
        return 0;
    }
    for(int pr=0; pr<row; pr++){
        int pc=queens[pr];
        if(pc==column || abs(row-pr)==abs(column-pc)){
            return 0;
        }
    }
    return 1;
}
int rec(int level){
    if(level==8){
        return 1;
    }
    int ans =0;
    for(int c=0; c<8; c++){
        if(check(level,c)){
            queens[level]=c;
            ans+=rec(level+1);
            queens[level]=-1;
        }
    }
    return ans;
}
signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    for(int i=0; i<8; i++){
        vector<char> row;
        for(int j=0; j<8; j++){
            char ch;
            cin>>ch;
            row.push_back(ch);
        }
        v.push_back(row);
    }
    for(int i=0; i<8; i++){
        queens[i]=-1;
    }
    cout<<rec(0);
   
}