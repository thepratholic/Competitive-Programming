#include <bits/stdc++.h>

using namespace std;

const int MAX = 200007;
const int MOD = 1000000007;

long long merge(int a[], int temp[], int left, int mid, int right) {
   int i, j, k;
   long long count = 0;
   i = left;
   j = mid;
   k = left;
   while ((i <= mid - 1) && (j <= right)) {
      if (a[i] <= a[j]){
      temp[k++] = a[i++];
      } else {
         temp[k++] = a[j++];
         count += (mid - i);
      }
   }
   while (i <= mid - 1)
      temp[k++] = a[i++];
   while (j <= right)
      temp[k++] = a[j++];
   for (i=left; i <= right; i++)
      a[i] = temp[i];
   return count;
}
long long mergeSort(int a[], int temp[], int left, int right){
   int mid;
   long long count = 0;
   if (right > left) {
      mid = (right + left)/2;
      count = mergeSort(a, temp, left, mid);
      count += mergeSort(a, temp, mid+1, right);
      count += merge(a, temp, left, mid+1, right);
   }
   return count;
}
long long aInversion(int a[], int n) {
   int temp[n];
   return mergeSort(a, temp, 0, n - 1);
}

void solve() {
	int n;
	cin >> n;
	int a[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	long long res = aInversion(a, n);
	sort(a, a + n);
	long long curr = 1;
	for (int i = 1; i < n; i++) {
	    if (a[i] != a[i - 1]) {res += (curr * (curr - 1)) / 2; curr = 1;}
	    else {curr++;}
	}
	res += (curr * (curr - 1)) / 2;
	cout << res << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt; cin >> tt; for (int i = 1; i <= tt; i++) {solve();}
    // solve();
}