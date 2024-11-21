#include<bits/stdc++.h>
using namespace std;
int solve(int N, int A, int B, int C, int D)
{
	if (abs(B - C) > 1) return 0;
	else if (abs(B - C) == 1) return 1;
	else if (B != 0) return 1;
	else if (A == 0 || D == 0) return 1;
	else return 0;
}
int main(){
    int N, A, B, C, D;
    cin >> N>>A>>B>>C>>D;
    if(solve(N, A, B, C, D) != 0) cout << "Yes";
    else cout << "No";
}