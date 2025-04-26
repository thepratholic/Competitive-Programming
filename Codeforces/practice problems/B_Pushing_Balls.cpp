#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll t,n,m,a[59][59],vis[59][59];
char s[59];
inline ll read(){
	ll s = 0,w = 1;
	char ch = getchar();
	while (ch > '9' || ch < '0'){ if (ch == '-') w = -1; ch = getchar();}
	while (ch <= '9' && ch >= '0') s = (s << 1) + (s << 3) + (ch ^ 48),ch = getchar();
	return s * w;
}
int main(){
	t = read();
	while (t --){
		n = read(),m = read();
		for (ll i = 1;i <= n;i += 1){
			scanf("%s",s + 1);
			for (ll j = 1;j <= m;j += 1){
				a[i][j] = s[j] - '0';
				vis[i][j] = 0;
			}
		}
		for (ll i = 1;i <= n;i += 1){
			for (ll j = 1;j <= m;j += 1){
				if (!a[i][j]) break;
				vis[i][j] = 1;
			}
		}
		for (ll j = 1;j <= m;j += 1){
			for (ll i = 1;i <= n;i += 1){
				if (!a[i][j]) break;
				vis[i][j] = 1;
			}
		}
		bool fl = 1;
		for (ll i = 1;i <= n && fl;i += 1){
			for (ll j = 1;j <= m;j += 1){
				if (a[i][j] && !vis[i][j]){
					fl = 0;
					break;
				}
			}
		}
		puts(fl ? "YES" : "NO");
	}
	return 0;
}