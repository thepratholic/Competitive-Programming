#include <bits/stdc++.h>
using namespace std;

const int maxn = 200100;

int n, a[maxn], b[maxn], m, p[maxn], ans[maxn][2];

inline void work(int x, int y) {
	if (x == y) {
		return;
	}
	ans[++m][0] = x;
	ans[m][1] = y;
	swap(a[x], a[y]);
	swap(p[a[x]], p[a[y]]);
	swap(b[x], b[y]);
}

void solve() {
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> a[i];
		p[a[i]] = i;
	}
	for (int i = 1; i <= n; ++i) {
		cin >> b[i];
	}
	m = 0;
	int x = 0;
	for (int i = 1; i <= n; ++i) {
		if (a[i] == b[i]) {
			if (n % 2 == 0 || x) {
				cout << "-1\n";
				return;
			}
			x = i;
		} else if (b[p[b[i]]] != a[i]) {
			cout << "-1\n";
			return;
		}
	}
	if (n & 1) {
		work(x, (n + 1) / 2);
	}
	for (int i = 1; i <= n / 2; ++i) {
		work(p[b[i]], n - i + 1);
	}
	cout << m << '\n';
	for (int i = 1; i <= m; ++i) {
		cout << ans[i][0] << ' ' << ans[i][1] << '\n';
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	while (T--) {
		solve();
	}
	return 0;
}