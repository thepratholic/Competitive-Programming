#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll add(ll y) {
	cout << "add " << y << endl;
	ll r; cin >> r;
	return r; 
}

ll mul(ll y) {
	cout << "mul " << y << endl;
	ll r; cin >> r;
	return r; 
}

ll div(ll y) {
	cout << "div " << y << endl;
	ll r; cin >> r;
	return r; 
}

ll dig() {
	cout << "digit" << endl;
	ll r; cin >> r;
	return r; 
}

ll done() {
	cout << "!" << endl;
	ll r; cin >> r;
	if(r == -1) exit(0);
	return r;
}

int main() {
	int tc; cin >> tc;
	while(tc--) {
		ll n; cin >> n;
		mul(9);
		dig(); dig();
		add(n-9);
		done();
	}

	return 0;
}