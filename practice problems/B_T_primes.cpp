#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define f(i, n) for (ll i = 0; i < n; i++)
#define iv(v, n) \
    vector<ll> v(n); \
    f(i, n) cin >> v[i]
#define MOD (1000000007)
#define INF 1000000000000000000LL // Infinity for ll
#define mp make_pair
#define nline '\n'
#define yes cout << "YES\n"
#define no cout << "NO\n"

const int N = 1e6 + 5;
vector<bool> primes(N, true);
unordered_set<ll> prime_set;

void compute() {
    primes[0] = primes[1] = false;

    for (ll i = 2; i * i < N; i++) {
        if (primes[i]) {
            for (ll j = i * i; j < N; j += i) {
                primes[j] = false;
            }
        }
    }

    for (ll i = 2; i < N; i++) {
        if (primes[i]) {
            ll sq = i * i;
            if (sq < 1e12) {
                prime_set.insert(sq);
            } else {
                break;
            }
        }
    }
}

void solve() {
    ll n;
    cin >> n;

    vector<ll> v(n);
    for (ll &x : v) {
        cin >> x;
        if (prime_set.count(x)) {
            yes;
        } else {
            no;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    compute();

    long long t = 1;
    // cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}
