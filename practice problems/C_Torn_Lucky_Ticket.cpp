#include <bits/stdc++.h>
using namespace std;

static long long cnt[6][50];

long long countSide(const vector<string>& s) {
    long long ans = 0;
    for (const string& t : s) {
        int len = t.size();
        int total = 0;
        for (char c : t) total += c - '0';
        for (int m = 1; m <= len; m++) {      
            if ((len + m) % 2) continue;
            int half = (len + m) / 2;
            int pre = 0;
            for (int k = 0; k < half; k++) pre += t[k] - '0';
            int need = pre - (total - pre);
            if (need >= 0 && need < 50) ans += cnt[m][need];
        }
    }
    return ans;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<string> a(n), b(n);
    char buf[10];
    for (int i = 0; i < n; i++) {
        scanf("%s", buf);
        a[i] = buf;
        b[i] = string(a[i].rbegin(), a[i].rend());
        int sum = 0;
        for (char c : a[i]) sum += c - '0';
        cnt[a[i].size()][sum]++;
    }

    long long ans = countSide(a);         
    for (int i = 0; i < n; i++) {
        const string& t = b[i];
        int len = t.size();
        int total = 0;
        for (char c : t) total += c - '0';
        for (int m = 1; m < len; m++) {      
            if ((len + m) % 2) continue;
            int half = (len + m) / 2;
            int pre = 0;
            for (int k = 0; k < half; k++) pre += t[k] - '0';
            int need = pre - (total - pre);
            if (need >= 0 && need < 50) ans += cnt[m][need];
        }
    }
    printf("%lld\n", ans);
}