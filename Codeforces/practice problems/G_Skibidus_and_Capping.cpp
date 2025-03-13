#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<int> prime_factors(int x){
	vector<int> pf;
	for(ll i = 2; i * i <= x; i++){
		while(x % i == 0){
			pf.push_back(i);
			x /= i;
		}
	}
	if(x > 1) pf.push_back(x);
	return pf;
}

int main(){
	int t; cin >> t;
	while(t--){
		int n; cin >> n;
		ll ans = 0;
		vector<int> one(n+1), two_same(n+1), two_diff(n+1), cnt(n+1);
		int prime_so_far = 0;
		for(int i = 0; i < n; i++){
			int x; cin >> x;
			vector<int> pf = prime_factors(x);
			if(pf.size() > 2) continue;
			if(pf.size() == 1){
				one[x]++;
				prime_so_far++;
				ans += two_same[x] + two_diff[x] + (prime_so_far - one[x]);
			}
			else if(pf[0] == pf[1]){
				two_same[pf[0]]++;
				ans += one[pf[0]] + two_same[pf[0]];
			}
			else{
				two_diff[pf[0]]++;
				two_diff[pf[1]]++;
				cnt[x]++;
				ans += one[pf[0]] + one[pf[1]] + cnt[x];
			}
		}
		cout << ans << "\n";
	}
}