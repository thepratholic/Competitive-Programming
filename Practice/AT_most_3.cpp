#include<bits/stdc++.h>
using namespace std;

bool cnt[3000001];

int main(){
    int n, w;
    cin >> n >> w;
    int nums[n];
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    memset(cnt, false, sizeof(cnt));

    for(int i=0;i<n;i++){
        cnt[nums[i]] = true;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            cnt[nums[i] + nums[j]] = true;
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            for(int k=j+1;k<n;k++){
                cnt[nums[i] + nums[j] + nums[k]] = true;
            }
        }
    }
    int ans = 0;
    for(int i = 1;i <= w;i++){
        if(cnt[i] == true){
            ans++;
        }
    }

    cout << ans << endl;
}