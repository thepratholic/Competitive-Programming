#include <bits/stdc++.h>
using namespace std;

#define ll long long

vector<ll> sieve(int n) {
    vector<bool> is_prime(n + 1, true);
    vector<ll> primes;

    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return primes;
}

bool isPrime(ll num) {
    if (num < 2) return false;
    for (ll i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

void solution() {
    vector<ll> prime = sieve(1001);

    ll n, k;
    cin >> n >> k;

    vector<ll> valid;
    for (ll i = 1; i < prime.size(); i++) {
        ll num = prime[i] + prime[i - 1] + 1;
        if (isPrime(num)) {
            valid.push_back(num);
        }
    }

    ll cnt = 0;
    for (ll i = 0; i < valid.size(); i++) {
        if (valid[i] <= n) {
            cnt++;
        }
    }

    if (cnt >= k) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

// Driver function
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    solution();
    
    return 0;
}
