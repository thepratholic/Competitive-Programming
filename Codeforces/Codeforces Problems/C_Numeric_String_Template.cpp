#include<bits/stdc++.h>
using namespace std;

void solve(){
	int n;
	cin>>n;
	int a[n];
	map<int,vector<int>> mp;
	for(int i=0;i<n;i++){
		cin>>a[i];
		mp[a[i]].push_back(i);
	}
	vector<vector<int>> v;
	for(auto ele:mp){
		v.push_back(ele.second);
	}
	sort(v.begin(),v.end());
	int m;
	cin>>m;
	for(int i=0;i<m;i++){
		string s;
		cin>>s;
		if(s.length()!=n){
			cout<<"NO"<<endl;
			continue;
		}
		else{
			map<char,vector<int>> temp;
			for(int j=0;j<s.length();j++){
				temp[s[j]].push_back(j);
			}
			vector<vector<int>> v1;
			for(auto ele:temp){
				v1.push_back(ele.second);
			}
			sort(v1.begin(),v1.end());
			if(v==v1){
				cout<<"YES"<<endl;
			}
			else{
				cout<<"NO"<<endl;
			}
		}
	}
}
 
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		solve();
	}
 
}