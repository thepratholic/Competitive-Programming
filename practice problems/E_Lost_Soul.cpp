#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;
#define INF(t) numeric_limits<t>::max()

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int tc; cin >> tc;
	while(tc--) {
		int n; cin >> n;
		vector<int> a(n), b(n);
		for(auto &x : a) cin >> x;
		for(auto &x : b) cin >> x;

		int i = n-1;
		unordered_set<int> alter1, alter2;
		for(; i >= -1; i--) {
			if(i == -1) break;
			if(a[i] == b[i]) break;
			if(i % 2 == 0) {
				if(alter1.count(a[i])) break;
				if(alter2.count(b[i])) break;
				if(i+1 < n) alter2.insert(a[i+1]);
				if(i+1 < n) alter1.insert(b[i+1]);
				if(alter2.count(a[i])) break;
				if(alter1.count(b[i])) break;
			}
			else {
				if(alter2.count(a[i])) break;
				if(alter1.count(b[i])) break;
				if(i+1 < n) alter1.insert(a[i+1]);
				if(i+1 < n) alter2.insert(b[i+1]);
				if(alter1.count(a[i])) break;
				if(alter2.count(b[i])) break;
			}
		}

		cout << i + 1 << "\n";
	}

	return 0;
}