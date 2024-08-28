#include<bits/stdc++.h>
using namespace std;
void solve(){
    string s;
    cin >> s;
    int n = s.size();
    int arr[26];
    memset(arr, 0, sizeof(arr));
    for (int i = 0; i < n; i++)
    {
        arr[s[i] - 'a']++;
    }

    string ans= "";
    for (int i = 0; i < 26; i++)
    {
        char c = i + 'a';
        while (arr[i] > 0)
        {
            ans += c;
            arr[i]--;
        }
    }
    cout << ans << endl;
}
int main(){
    solve();
}