#include<iostream>
#include<string>
#include<algorithm>
#include<cctype>
using namespace std;
 
int main(){
    string s; cin >> s;
    int upper = 0, lower = 0;
    for(int i = 0;i < s.size();i++){
        if(isupper(s[i])){
            upper ++;
        }
        else lower++;
    }
 
    if (upper > lower) transform(s.begin(), s.end(), s.begin(),::toupper);
    else if(upper == lower) transform(s.begin(), s.end(), s.begin(),::tolower);
    else transform(s.begin(), s.end(), s.begin(),::tolower);
 
    cout << s << endl;
    return 0;
}